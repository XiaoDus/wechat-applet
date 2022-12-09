<template>
	<view class="content">
		<!-- 通知 -->
		<uni-notice-bar style="z-index: 1;" show-icon scrollable text="此版本为1.0版本,出现BUG请联系管理员!" />
		<!-- welcome -->
		<view class="page" style="margin-top: -10px;">
			<view class="image-list">
				<view class="image-item">
					<view class="image-content">
						<!-- welcome图片 -->
						<image style="width: 100%; height: 200px; background-color: #eeeeee;" mode="scaleToFill"
							src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/20e1275f-04cb-4f7a-8759-b0ac55d6491b.jpg">
						</image>
					</view>
				</view>
			</view>
		</view>

		<!-- 积分 -->
		<view class="integral">
			<image style="width: 18px;height: 18px;margin-left: 8%;" mode="aspectFit"
				src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/bcb52907-c887-42e2-9fd1-f78834701e8b.png"></image>
			<text style="margin-left: 10px;vertical-align:3px;">积分</text>
			<view class="integralList">
				
				<view class="xiaoxuan">
					<text>小轩的积分：</text><text>{{Integral.xiaoxuan}}</text>
				</view>
			</view>
		</view>

		<!-- 欢迎回来 -->
		<view class="integral">
			<image style="width: 18px;height: 18px;margin-left: 8%;" mode="aspectFit"
				src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/cloudstorage/745c600f-237a-408e-af2d-b4f60070bbb3.jpg"></image>
			<text style="margin-left: 10px;vertical-align:3px;">欢迎回来</text>
			<view class="integralList">
				<view class="xiaodu">
					<text>欢迎回家!</text>
				</view>
				<view class="xiaoxuan">
					<text>欢迎小轩崽崽 要加油哟!</text>
				</view>
			</view>
		</view>



	</view>
</template>

<script>
	//通知栏
	// import notice from '../../uni_modules/uni-notice-bar/components/uni-notice-bar/uni-notice-bar.vue'
	export default {
		data() {
			return {
				Integral:{
					
					xiaoxuan:null
				}
			}
		},
		components: {
			// notice
		},
		created() {
			this.request()
			
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
		onLoad() {
			//定时请求获取积分
			setInterval(()=>{
				this.request()
			},2000)
		},
		
		methods: {
			request(){
				uni.request({
				    url: 'https://1el9898253.oicp.vip/Integral/', //仅为示例，并非真实接口地址。
					method:'post',
				    success: (res) => {
				        let datas=res.data.status.data
						
						this.Integral.xiaoxuan=datas.xiaogao.Integral
				    }
				});
				// 修改state中的值
				this.$store.commit("EDIT",this.Integral.xiaoxuan)
				
				
			}
		}
	}
</script>

<style lang="scss">
	.integral {
		// margin-left: 15px;
		margin-top: 10px;
		margin-bottom: 5%;
	}

	.integralList {
		height: 80%;
		width: 85%;
		background-color: white;
		margin: 10px auto;
		border-radius: 15px;
		padding-left: 13px;
		

	}

	.integralList text {
		font-family: Arial, Helvetica, sans-serif;
		font-size: 13px;
	}

	.xiaodu {
		line-height: 35px;
	}

	.xiaoxuan {
		line-height: 35px;
	}
</style>
