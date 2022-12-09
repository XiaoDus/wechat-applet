<template>
	<view>
		<view class="userInfo">
			<ul class="info_ul">
				<li class="info_li">
					<view class="" style="line-height: 64px;">头像</view>
					<view class="">
						<image style="width: 50px; height: 50px;border-radius: 50%;margin-top: 12%;" mode="aspectFit"
							:src="userImg">
						</image>
					</view>
				</li>
				<li class="info_li">
					<view class="">昵称</view>
					<view style="color: #CCCCCC;">{{userName}}</view>
				</li>
				<li class="info_li">
					<view class="">手机号</view>
					<view style="color: #CCCCCC;">{{userPhone}}</view>
				</li>
				<li class="exit" @click="Exit">退出登录</li>

			</ul>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				userImg: '',
				userName: '',
				userPhone: '',
			}
		},
		onShow() {
			const userInfo = uni.getStorageSync('userInfo')
			if (Object.keys(userInfo).length != 0) {
				
				this.userImg = userInfo.userImg
				this.userName = userInfo.userName
				this.userPhone = userInfo.userPhone

			}

		},
		methods: {
			Exit() {
				if (this.userImg != '') {
					uni.showModal({
						title: '提示',
						content: '确认退出登录吗！',
						success: (res) => {
							if (res.confirm) {
								uni.clearStorageSync();
								let pages = getCurrentPages() //获取当前页
								let beforePage = pages[pages.length - 2] //获取上一页
								uni.navigateBack({ //返回任务列表
									success: () => {
										beforePage.$vm.clear() //调用上一页的method中的方法
									}
								})
								
								
							}
						}
					})
				}
			},
		}
	}
</script>

<style>
	.info_ul {
		margin: 20px 0;

	}

	.info_li {
		display: flex;
		justify-content: space-between;
		background-color: white;
		margin-top: 1px;
		padding: 10px 20px;
	}

	.exit {
		background-color: white;
		margin-top: 1px;
		padding: 10px 20px;
		text-align: center;
	}
</style>
