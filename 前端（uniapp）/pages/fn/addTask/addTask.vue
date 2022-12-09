<template>
	<view>
		<view class="addTask">
			<!-- 任务名称 -->
			<view class="uni-form-item uni-column taskName">
				<view class="title">任务名称</view>
				
					<textarea maxlength="15" auto-height v-model="Task.TaskName" placeholder="请输入任务名称(15字以内)" />
			</view>

			<!-- 任务详情 -->
			<view class="taskDetails">
				<view class="uni-title uni-common-pl">任务详情</view>
				<view class="details">
					<textarea maxlength="80" v-model="Task.TaskDetails" placeholder="请输入任务详情介绍(80字以内)" />
				</view>
			</view>

			<!-- 奖励积分 -->
			<view class="uni-form-item uni-column taskAward">
				<view class="title">奖励积分</view>
				<textarea maxlength="1" v-model="Task.TaskAward" placeholder="请输入完成任务时的奖励积分(10分以下)" />
			</view>
		</view>
		<view class="taskBtn">
			<button type="warn" style="margin-left: 5%;margin-right: 2.5%;" @click="clearTask" plain="true">重置</button>
			<button type="primary" style="margin-left: 2.5%;margin-right: 5%;" @click="saveTask"
				plain="true">保存</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
				Task: {
					TaskName: '',
					TaskDetails: '',
					TaskAward: ''
				},
				

			}
		},
		methods: {
			//清楚输入的任务信息
			clearTask() {
				this.Task.TaskAward = ''
				this.Task.TaskDetails = ''
				this.Task.TaskName = ''
			},
			
			//保存任务并返回任务列表
			saveTask() { 
				if (this.Task.TaskName && this.Task.TaskDetails && this.Task.TaskAward) {
					
					uni.request({
						url: 'https://1el9898253.oicp.vip/addTask/', //仅为示例，并非真实接口地址。
						data: {
							Task: this.Task
						},
						method:'post',
						success: () => {
							let pages=getCurrentPages() //获取当前页
							let beforePage = pages[pages.length - 2] //获取上一页
							uni.navigateBack({
								success:()=>{
									beforePage.onLoad() //调用上一页的onLoad方法
									
								}
							})
						}
					});
				}else{
					uni.showToast({
						title: '必填项为空',
						duration: 1000,
						icon:'error'
					});
				}

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
