'use strict';
exports.main = async (event, context) => {
	try {
		const res = await uniCloud.sendSms({
			appid: 'wxf1a1ab38fdf365fe',
			smsKey: '1a4a6df116fb7b3ab8e2ea4d0059a4e8',
			smsSecret: 'a5b20363c13dd7162ff2af4f90002496',
			phone: event.phone,
			templateId: '16395', // 请替换为自己申请的模板id
			data: event.data
		})
		// 调用成功，请注意这时不代表发送成功

		return res
	} catch (err) {
		// 调用失败
		console.log(err.errCode)
		console.log(err.errMsg)
		return {
			code: err.errCode,
			msg: err.errMsg
		}
	}
};
