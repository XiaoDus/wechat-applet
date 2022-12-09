<template>
	<view>
		<uni-card :title="!flag?'未登录，点击登录':userName" :sub-title="!flag?'':'电话： '+userPhone"
			:extra="!flag?'':'我的资料 >'" :thumbnail="!flag?'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/9e5ad88d-a010-4dcd-8784-d7ebb0116e76.png':userImg"
			@click="!flag && toggle('bottom');flag && userInfo()">
		</uni-card>
		<view style="border-bottom: 1px solid #CCCCCC;margin-top: 20px;" v-if="soll==[]?false:true"></view>
		<uni-card v-for="i in soll" :key="i" v-if="i.numCommodity<=0?false:true" :title="i.name" :sub-title="i.Details"
			:extra="'× '+i.numCommodity" @click="useCard(i.name)" is-shadow :thumbnail="i.imgUrl">
		</uni-card>

<!-- 扣分 -->

		<view>
			<!-- 登录弹窗 -->
			<uni-popup ref="popup" class="popup" background-color="#fff">
				<view class="popup-content">
					<uni-card style="display: flex;flex-direction: column;">
						<view slot="actions" class="card-actions userInput">
							<label for="">手机号：</label>
							<input type="number" placeholder="请输入手机号" v-model="userInputPhone" maxlength="11">
						</view>
						<view slot="actions" class="card-actions userInput inputCode">
							<label for="" style="text-align: center;">密码：</label>
							<input v-model="userInputCode" type="password" placeholder="请输入密码" maxlength="6"
								style="width: 40%;padding-left: 10px;">

						</view>

					</uni-card>
					<button style="width: 92%;" class="btnLogin" type="primary"  @click="login">
						登录
					</button>


				</view>
			</uni-popup>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {

				type: 'bottom',
				flag: false,
				soll: [],
				userImg: '', //用户头像
				userName: '', //用户名
				userPhone: '', //登录后保存的手机号
				userInputCode: '', //输入的密码
				userInputPhone: '' //登录输入的手机号
			}
		},

		created() {
			this.getRequest()
			//定时请求获取积分
			setInterval(() => {
				this.getRequest()
			}, 2000);
			() => {
				const userInfo = uni.getStorageSync('userInfo')
				console.log(uni.getStorageSync('userInfo'))
				if (userInfo) {
					this.userImg = userInfo.userImg
				}
			}

		},
		onShow() {
			//验证登录信息
			const userInfo = uni.getStorageSync('userInfo')
			if (Object.keys(userInfo).length != 0) {
				this.userImg = userInfo.userImg
				this.userName = userInfo.userName
				this.userPhone = userInfo.userPhone
				this.flag=true

			}

		},
		
		methods: {
			//登录弹出框
			toggle(type) {
				this.type = type
				// open 方法传入参数 等同在 uni-popup 组件上绑定 type属性
				this.$refs.popup.open(type)
			},
			//跳转至个人信息页面
			userInfo(){
				uni.navigateTo({
					url: './userInfo/userInfo'
				});
			},
			//退出登录
			clear(){
				this.userImg = ''
				this.userName = ''
				this.userPhone = ''
				this.flag=false
			},
//登录
			login() { 
				if (this.userInputPhone == '14785559975' && this.userInputCode == '011013' || this.userInputPhone ==
					'826012560' && this.userInputCode == '485741') {
					if (this.userName == '') {
						uni.getUserProfile({
							desc: '用户登录',
							success: (res) => {
								this.userImg = res.userInfo.avatarUrl
								this.userName = res.userInfo.nickName
								this.userPhone = this.userInputPhone
								this.flag=true
								this.$refs.popup.close()
								

								uni.setStorage({
									key: 'userInfo',
									data: {
										userName: this.userName,
										userImg: this.userImg,
										userPhone: this.userPhone
									},
									
								});
								uni.showToast({
									title: '登录成功！',
									icon: 'none',
									success: () => {
										this.userInputPhone = ''
										this.userInputCode = ''
									}
								})
							}
						})
					}
				} else if (!this.userInputPhone && !this.userInputCode) {
					uni.showToast({
						title: '必填项不能为空！',
						icon: 'none'
					})
				} else {
					uni.showToast({
						title: '手机号或密码错误！',
						icon: 'none'
					})
				}


			},

			//请求后端数据获取卡片信息
			getRequest() {
				uni.request({
					url: 'https://1el9898253.oicp.vip/sollList/',
					method: 'post',
					success: (res) => {
						let sollList = res.data.status.data
						let sollGetList = [] //放请求返回的数据

						for (let i in sollList) {
							sollGetList.push(sollList[i].fields)
						}

						this.soll = sollGetList

					}
				});
			},
			//使用卡片
			useCard(name) {
				uni.showModal({
					title: '提示',
					content: '确认使用此劵吗！',
					success: (res) => {
						if (res.confirm) {
							uni.request({
								url: 'https://1el9898253.oicp.vip/sollList/',
								data: {
									name: name
								},
								success: (res) => {
									uni.showToast({
										title: '兑换成功！',
										icon: 'none',
									})
								}
							});
						}
					}
				})
			}
		}
	}
</script>

<style>
	.popup {
		background-color: rgb(246, 246, 246);
	}

	.popup-content {
		height: 40vmax;

	}

	.card-actions {
		padding-top: 10px;
	}

	.userInput {

		padding: 10px 10px;
		margin: 0 auto;
		margin-bottom: 10px;
		border-radius: 3px;
		border: 1px solid darkgrey;
	}

	.userInput label {
		float: left;
		margin-top: 2px;
	}

	.userInput input {
		align-items: center;
	}

	.inputCode {
		display: flex;
		padding-right: 0;
		/* justify-content: space-around; */
	}

	.inputCode input {}

	.btnLogin {}
</style>
