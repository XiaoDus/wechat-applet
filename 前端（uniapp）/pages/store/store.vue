<template>
	<view>

		<uni-notice-bar style="z-index: 1" show-icon scrollable text="本次活动最终解释权归管理员所有!" />
		<view style="margin-top: -10px;">
			<uni-grid :column="2" :showBorder='false' :highlight='false'>
				<uni-grid-item v-for="(item, index) in awardList" :index="index" :key="index"
					style="background-color: #fff;">
					<view class="grid-item-box">
						<!-- 商品图片 -->
						<image  style="width: 80%; height: 80%;align-items: center;"
							mode="scaleToFill" :src="item.awardUrl"></image>
					</view>
					<text class="textIntroduce">{{item.awardName}}</text>
					<view class="introduce">
						<view class="introduce_1">
							<image style="width: 20px;height: 20px;margin-left: 8%;" mode="aspectFill"
								src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/bcb52907-c887-42e2-9fd1-f78834701e8b.png">
							</image>
							<text class="text">{{item.awardintegral}}</text>

						</view>
						<view class="">
							<button class="mini-btn" type="primary" size="mini"
								@click="Introduce(item.awardintegral,item.awardName)">兑换</button>
						</view>
					</view>
				</uni-grid-item>
				
				
				<uni-grid-item  :index="index" style="background-color: #fff;">
					<view class="grid-item-box">
						<!-- 商品图片 -->
						<image  style="width: 80%; height: 80%;align-items: center;"
							mode="scaleToFill" src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/d45ed563-993e-4fb4-9354-ef4224d677aa.jpg"></image>
					</view>
					<text class="textIntroduce">待定</text>
					<view class="introduce">
						<view class="introduce_1">
							<image style="width: 20px;height: 20px;margin-left: 8%;" mode="aspectFill"
								src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/bcb52907-c887-42e2-9fd1-f78834701e8b.png">
							</image>
							<text class="text">999</text>

						</view>
						<view class="">
							<button class="mini-btn" type="primary" size="mini">兑换</button>
						</view>
					</view>
				</uni-grid-item>
				
				
				
			</uni-grid>

		</view>



	</view>
</template>

<script>
	import uGrid from '../../uni_modules/uni-grid/components/uni-grid/uni-grid.vue'
	import notice from '../../uni_modules/uni-notice-bar/components/uni-notice-bar/uni-notice-bar.vue'
	
	
	export default {
		data() {
			return {
				awardList: [{
						id: 0,
						awardName: '我也永远爱你',
						awardintegral: '1',
						awardintroduce: '我也永远爱你',
						awardUrl: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/977ae51b-aea6-418b-b050-88de8155117e.jpg'
					},
					{
						id: 1,
						awardName: '奶茶',
						awardintegral: '20',
						awardintroduce: '任意一杯奶茶',
						awardUrl: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/89c80731-0032-4558-8789-62336f13f0d7.jpg'
					},

					{
						id: 2,
						awardName: '一次简单许愿',
						awardintegral: '50',
						awardintroduce: '满足一个简单的要求',
						awardUrl: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/f406cb5d-80c7-4290-821b-c86df1522557.jpg'
					},
					

					{
						id: 3,
						awardName: '蛋糕',
						awardintegral: '100',
						awardintroduce: '奖励一个小蛋糕',
						awardUrl: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/c809057f-040e-49d6-9f74-e2c1be1db9c6.jpg'
					},
					
					{
						id: 4,
						awardName: '神秘零食大礼包',
						awardintegral: '120',
						awardintroduce: '奖励神秘零食大礼包',
						awardUrl: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/4bf7ac8d-c757-4696-b981-3dc33006cb95.jpg'
					},
					{
						id: 5,
						awardName: '一次合理的许愿',
						awardintegral: '150',
						awardintroduce: '满足一次合理的许愿',
						awardUrl: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/63cdee22-5469-4ad6-9183-440f04a3f308.jpg'
					},


					{
						id: 6,
						awardName: '大餐一顿',
						awardintegral: '200',
						awardintroduce: '奖励大餐一顿',
						awardUrl: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/0d3528eb-2ae6-43e1-bd79-e5eaedb95dcb.jpg'
					},


				],
			}
		},
		components: {
			uGrid,
			notice
		},
		onShow(){
			const userInfo=uni.getStorageSync('userInfo')
			if(Object.keys(userInfo).length==0){
				uni.showModal({
					title: '提示',
					showCancel:false,
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
			
			Introduce(integral, name) {
				// 个人总积分
				let Integral = this.$store.state.Integral
				let that=this
				
				uni.showModal({
					title: '提示',
					content: '确认兑换此奖励吗！',
					success: function(res) {
						if (res.confirm) {
							if (Integral >= integral) { //判断个人积分是否大商品积分
							let endIntegral =Integral - integral
								uni.request({
									url: 'https://1el9898253.oicp.vip/exchange/',
									method: "post",
									data: {
										integral: integral,
										name: name
									},
									success: () => {
										//需改vuex个人积分
										that.$store.commit('EDIT',endIntegral)
										uni.showToast({
											title: '兑换成功！',
											icon: 'none',
										})
										
									}
								});
								
							} else { //个人积分小于商品积分
								uni.showModal({
									title: '提示',
									content: '积分不足！',
								})
							}

						}
					}
				});
			}

		}
	}
</script>

<style>
	.text {
		font-size: 25px;
		/* font-weight: bold; */
		color: rgb(245, 119, 118);
		letter-spacing: -3px;
		/* 文字间距 */
		margin-top: -7px;


	}

	.grid-item-box {
		flex: 1;
		// position: relative;
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 15px 15px;
	}

	.introduce {
		padding: 10px 25px;
	}

	.textIntroduce {
		padding: 0 30px;
	}

	.introduce,
	.introduce_1 {
		display: flex;
		justify-content: space-between;
	}

	.introduce_1 {
		align-items: center;
	}
</style>
