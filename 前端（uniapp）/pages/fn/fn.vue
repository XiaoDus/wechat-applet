<template>
	<view>
		<!-- 无任务 -->
		<view class="notTasks" v-if="isShowTask">
			<!-- 添加任务 -->
			<view class="addTasks" v-if="isShowAdd">
				<navigator url="/pages/fn/addTask/addTask"><button><img
							src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/810dee86-2049-455b-8012-121414dc257c.jpg"
							style="width: 30px;height: 30px;margin-top: 20px;" alt="">任务</button></navigator>
			</view>
			<image style="" mode="aspectFit" src="../../static/task/task.jpg"></image>
			<view class="notTaskText">
				<text style="font-size: 20px;font-weight: bold;">暂无任务\n\n</text>
				<text style="font-size: 13px;color: darkgray;">好像什么任务也没有...</text>
			</view>
		</view>

		<!-- 有任务 -->
		<view class="hasTask" v-else>
			<!-- 添加任务 -->
			<uni-fab v-if="isShowAdd" @trigger="trigger" ref="fab" horizontal="right" popMenu='true'
				:content='content' />

			<!-- 任务列表 -->
			<uni-collapse>
				<uni-collapse-item title="待完成的任务">
					<view class="content">
						<uni-list v-for="i in task" :key="i">
							<uni-list-chat :avatarList='url' v-if="i.isFinish==1?false:true" clickable='true'
								@longpress='longpress(i.id)' @click="taskFinisn(i.id)"
								:title="i.taskName+' ('+i.taskAward+'分)'" :note="i.taskDetails" :time="i.setTime"
								badge-positon="left" :badge-text="i.isFinish==2?'dot':''"></uni-list-chat>
						</uni-list>
					</view>
				</uni-collapse-item>
			</uni-collapse>




			<!-- 已完成的任务 -->
			<uni-collapse>
				<uni-collapse-item title="已完成的任务">
					<view class="content">
						<uni-list v-for="i in task" :key="i">
							<uni-list-chat :avatarList='url' v-if="i.isFinish==2?false:true" clickable='true'
								@longpress='longpress(i.id)' @click="taskFinisn(i.id)"
								:title="i.taskName+' ('+i.taskAward+'分)'" :note="i.taskDetails" :time="i.setTime"
								badge-positon="left" :badge-text="i.isFinish==2?'dot':''"></uni-list-chat>
						</uni-list>
					</view>
				</uni-collapse-item>
			</uni-collapse>
		</view>

	</view>

</template>

<script>
	import uFab from "../../uni_modules/uni-fab/components/uni-fab/uni-fab.vue"
	// import uCollapse from "../../uni_modules/uni-collapse/components/uni-collapse/uni-collapse.vue"
	// import uList from "../../uni_modules/uni-list/components/uni-list/uni-list.vue"

	export default {
		data() {
			return {
				url: [{
					url: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/d44d0d44-73f5-4633-86f7-f39c59b91142.jpg'
				}],
				isShowTask: false,
				task: [],
				isShowAdd: true,
				minus: '', //扣的积分
				content: [{
						iconPath: '/static/fn/jia.jpg',
						selectedIconPath: '/static/fn/jia.jpg',

						text: '添加',
						active: false
					},
					{
						iconPath: '/static/fn/jian.jpg',
						selectedIconPath: '/static/fn/jian.jpg',

						text: '扣分',
						active: false
					}
				]
			}
		},
		components: {
			// uIcons,
			uFab,
			// uCollapse
			// uList,


		},


		onLoad() {
			this.getRequest()
			const setTime = setInterval(() => { //定时向后端请求任务
				this.getRequest()
			}, 2000)
		},
		onShow() {

			const userInfo = uni.getStorageSync('userInfo')
			if (Object.keys(userInfo).length != 0) {
				if (userInfo.userPhone == '14785559975') {
					this.isShowAdd = false
				} else {
					this.isShowAdd = true
				}
			} else {
				uni.showModal({
					title: '提示',
					showCancel: false,
					content: '您未登录，请先登录！',
					success: (res) => {
						if (res.confirm) {
							uni.switchTab({
								url: '../user/user',
							});
						}
					}
				})
			}
		},
		methods: {
			//收藏按钮打开菜单点击的按钮
			trigger(e) {

				if (e.item.text == '添加') {
					uni.navigateTo({
						url: './addTask/addTask', //跳转并传参数，在跳转后的页面onLoad中获取
					});
				} else if (e.item.text == '扣分') {
					uni.showModal({
						title: '扣分',
						placeholderText: '请输入扣的积分',
						editable: true,
						success: (res) => {
							if (res.confirm) {
								uni.request({
									url: 'https://1el9898253.oicp.vip/Integral', //仅为示例，并非真实接口地址。
									data: {
										integral: res.content
									},
									success: () => {
										uni.showToast({
											title: '扣分成功！',
											icon: 'none'
										})
									}
								});
							}

						}

					});
				}

			},

			//长按删除任务
			longpress(nid) {
				let _this = this
				if (_this.isShowAdd) {
					uni.showModal({
						title: '提示',
						content: '确认删除该任务吗！',
						success: function(res) {
							if (res.confirm) {

								uni.request({
									url: 'https://1el9898253.oicp.vip/taskDelete/', //仅为示例，并非真实接口地址。
									data: {
										nid: nid
									},
									success: () => {
										_this.getRequest()

									}
								});
							}
						}
					});
				} else {
					uni.showModal({
						title: '提示',
						showCancel: false,
						content: '抱歉，您没有权限删除任务！',
					})
				}

			},

			//请求获取任务列表
			getRequest() {
				uni.request({
					url: 'https://1el9898253.oicp.vip/task/',
					method: 'post',
					success: (res) => {
						let taskList = res.data.status.taskList
						let taskGetList = [] //放请求返回的数据
						for (let i in taskList) {
							//获取任务ID，并添加到taskList
							taskList[i].fields['id'] = taskList[i].pk
							taskGetList.push(taskList[i].fields)
						}
						this.task = taskGetList
						if (this.task.length == 0) {
							this.isShowTask = true
						} else {
							this.isShowTask = false
						}

					}
				});
			},

			// 点击进入任务详情
			taskFinisn(id) {
				uni.request({

					url: 'https://1el9898253.oicp.vip/taskFinish/?id=' + id,
					success: (res) => {

						let msg = {
							id: id,
							taskName: res.data.status.taskList[0].fields.taskName,
							taskDetails: res.data.status.taskList[0].fields.taskDetails,
							taskAward: res.data.status.taskList[0].fields.taskAward,
							isFinish: res.data.status.taskList[0].fields.isFinish,
						}

						uni.navigateTo({
							url: './taskFinish/taskFinish?taskName=' + msg.taskName + '&taskDetails=' +
								msg.taskDetails + '&taskAward=' + msg.taskAward + '&id=' + id +
								'&isFinish=' + msg.isFinish, //跳转并传参数，在跳转后的页面onLoad中获取
							success: () => {
								clearInterval(this.setTime) //跳转后清除定时器

							}
						});

					}
				});

			},
		}
	}
</script>

<style>
	.notTasks {
		margin: 30% 15%;
		margin-bottom: 0;
	}

	.addTasks {
		position: fixed;
		top: 0;
		left: 5%;
	}

	.content {
		padding: 15px;
	}

	.addTasks button {
		width: 70px;
		height: 110px;
		background-color: darkgray;
		border: none;
		box-shadow: 5px 5px 5px darkgrey;
	}



	.notTaskText {
		text-align: center;

	}

	.button {
		margin-bottom: 10px;
	}
</style>
