<template>
	<view>
		<view class="addTask">
			<!-- 任务名称 -->
			<view class="uni-form-item uni-column taskName">
				<view class="title">任务名称</view>

				<textarea maxlength="15" auto-height v-model="task.taskName" placeholder="请输入任务名称(15字以内)" />
			</view>

			<!-- 任务详情 -->
			<view class="taskDetails">
				<view class="uni-title uni-common-pl">任务详情</view>
				<view class="details">
					<textarea maxlength="80" v-model="task.taskDetails" placeholder="请输入任务详情介绍(80字以内)" />
				</view>
			</view>

			<!-- 奖励积分 -->
			<view class="uni-form-item uni-column taskAward">
				<view class="title">奖励积分</view>
				<input class="uni-input" v-model="task.taskAward" maxlength="1" type="number"
					placeholder="请输入完成任务时的奖励积分" />
			</view>
		</view>
		<view class="taskBtn">
			<button type="default" style="margin-left: 5%;margin-right: 2.5%;" :disabled="isShowEdit?'':'true'"
				@click="saveTask" plain="true">保存</button>
			<button type="primary" style="margin-left: 2.5%;margin-right: 5%;" :disabled="task.isFinish==1?'true':''"
				@click="finishTask(task.id,task.taskAward)"
				plain="true">{{finishText |finishChangeText(task.isFinish)}}</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				finishText: '完成',

				task: {
					id: "",
					taskName: "",
					taskDetails: "",
					taskAward: "",
					isFinish: "",
					
				},
				isShowEdit: true

			}
		},
		onLoad(option) { //接收传过来的参数
			this.task.id = option.id
			this.task.taskName = option.taskName
			this.task.taskDetails = option.taskDetails
			this.task.taskAward = option.taskAward
			this.task.isFinish = option.isFinish
		},
		onShow() {
			const userInfo = uni.getStorageSync('userInfo')
			if(userInfo.userPhone=='14785559975'){
				this.isShowEdit=false
			}
			

		},
		filters: {
			finishChangeText(value, isFinish) {
				if (isFinish == 1) {
					return value = '已完成'
				} else {
					return value
				}
			}
		},
		methods: {
			//修改保存任务
			saveTask() {
				if (this.task.taskName && this.task.taskDetails && this.task.taskAward) {
					uni.request({
						url: 'https://1el9898253.oicp.vip/taskFinish/', //仅为示例，并非真实接口地址。
						data: {
							Task: this.task,
						},
						method: 'post',
						success: () => {
							let pages = getCurrentPages() //获取当前页
							let beforePage = pages[pages.length - 2] //获取上一页
							uni.navigateBack({
								success: () => {
									beforePage.onLoad() //调用上一页的onLoad方法
								}
							})

						}
					});
				} else {
					uni.showToast({
						title: '必填项为空',
						duration: 2000,
						icon: 'error'
					});
				}
			},

			//完成任务
			finishTask(nid, taskAward) {
				uni.showModal({
					title: '提示',
					content: '确认完成任务吗！',
					success: (res) => {
						if (res.confirm) {
							uni.request({
								url: 'https://1el9898253.oicp.vip/taskFinish/', //仅为示例，并非真实接口地址。
								data: {
									Task: {
										id: nid,
										taskAward: taskAward
							
									}
								},
								method: 'post',
								success: () => {
									let pages = getCurrentPages() //获取当前页
									let beforePage = pages[pages.length - 2] //获取上一页
									uni.navigateBack({ //返回任务列表
										success: () => {
											beforePage.onLoad() //调用上一页的onLoad方法
										}
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
	.addTask {
		width: 90%;
		margin: 10% auto;


	}

	.taskName {
		background-color: white;
		padding: 30px 20px;
		border-top-left-radius: 15px;
		border-top-right-radius: 15px;
	}

	.taskDetails {
		height: 150px;
		margin-top: 1px;
		background-color: white;
		padding: 30px 20px;
		border-bottom-left-radius: 15px;
		border-bottom-right-radius: 15px;
	}

	.taskAward {
		margin-top: 20px;
		height: 100px;
		border-radius: 15px;
		padding: 30px 20px;
		background-color: white;
	}

	.details,
	.addTask input {
		margin-top: 10px;
	}

	.taskBtn {
		display: flex;
		justify-content: space-around;
	}

	.taskBtn button {
		width: 40%;
		margin-bottom: 0;
	}
</style>
