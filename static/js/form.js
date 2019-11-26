$(function(){
	try {
		$.formValidator.initConfig({
			autotip: true,
			formid: "form",
			errorfocus: true,
			submitonce: false
			/*,
			onerror: function() {
				alert('部分信息输入非法，请根据提示修改！');
				$('#form').submit(function(){return false;});
			},
			onsuccess: function() {
				$('#form').submit(function(){return true;});
			}*/
		});

		//微信群所属行业、个人微信号所属行业、公众号所属行业、文章发布栏目
		if($('#type_id').length > 0 ){
			$("#type_id").formValidator({
				onshow: "必填",
				onfocus: "必填",
				oncorrect: "选择正确"
			}).inputValidator({
				min: 1,
				onerror: "不能为空"
			});
		}
		//微信群地区、个人微信号地区、公众号地区、货源地区、修改个人资料地区
		if($('#province_code').length > 0 ){
			$("#province_code").formValidator({
				onshow: "必填",
				onfocus: "必填",
				oncorrect: "选择正确"
			}).inputValidator({
				min: 1,
				onerror: "不能为空"
			});
		}
		//微信群名称、个人微信号昵称、公众号名称、文章名称、搞笑图片图片名称、搞笑段子标题
		if($('#name').length > 0 ){
			$("#name").formValidator({
				onshow: "必填",
				onfocus: "名称应该为1-20个汉字",
				oncorrect: "填写正确"
			}).inputValidator({
				min: 2,
				onerror: "不能为空"
			});
		}
		//微信群介绍、个人微信号介绍、公众号介绍、货源卖点、文章摘要、搞笑图片图片描述、搞笑段子笑话内容、发布广告品牌优势
		if($('.tarea').length > 0 ){
			$(".tarea").formValidator({
				onshow: "必填",
				onfocus: "介绍不低于10个汉字",
				oncorrect: "填写正确"
			}).inputValidator({
				min: 20,
				onerror: "介绍不低于10个汉字"
			});
		}
		//微信群标签、个人微信号标签、公众号标签
		if($('#tags').length > 0 ){
			$("#tags").formValidator({
				onshow: "请填写标签",
				onfocus: "标签应该为1-50个汉字",
				oncorrect: "填写正确"
			}).inputValidator({
				min: 2,
				max: 100,
				onerror: "标签应该为1-50个汉字",
				onerrormax: "不能超过50个汉字"
			});
		}
		//微信群群主微信号、个人微信号、货源微信号、发布广告微信号
		if($('#wx_id').length > 0 ){
			$("#wx_id").formValidator({
				onshow: "必填",
				onfocus: "微信号的ID",
				oncorrect: "填写正确"
			}).inputValidator({
				min: 2,
				max: 100,
				onerror: "不能为空",
				onerrormax: "不能超过50个汉字"
			});
		}
		//微信群头像上传、个人微信号头像上传、公众号封面、修改个人资料头像
		if($('#icon').length > 0 ){
			$("#icon").formValidator({
				onshow: "请上传群,禁止黄色,低俗,泳装照片",
				onfocus: "请上传图片,图片格式为jpg、gif、png",
				oncorrect: "格式正确"
			}).regexValidator({
				regexp: regexEnum.picture,
				onerror: "请上传图片,图片格式为jpg、gif、png"
			});
		}
		if($('.content').length > 0 ){
			$(".content").formValidator({
				onshow: "请上传群截图,请参照示例，群截图带人数",
				onfocus: "请上传图片,图片格式为jpg、gif、png",
				oncorrect: "格式正确"
			}).regexValidator({
				regexp: regexEnum.picture,
				onerror: "请上传图片,图片格式为jpg、gif、png"
			});
		}
		//微信群二维码上传、个人微信号二维码上传
		if($('#qrcode').length > 0 ){
			$("#qrcode").formValidator({
				onshow: "请上传图片",
				onfocus: "请上传图片,图片格式为jpg、gif、png",
				oncorrect: "格式正确"
			}).regexValidator({
				regexp: regexEnum.picture,
				onerror: "请上传图片,图片格式为jpg、gif、png"
			});
		}
		//高级群群主二维码上传
		if($('#wx_qrcode').length > 0 && $('#ground_auth').css('display')!='none' ){
			$("#wx_qrcode").formValidator({
				onshow: "请上传图片",
				onfocus: "请上传图片,图片格式为jpg、gif、png",
				oncorrect: "格式正确"
			}).regexValidator({
				regexp: regexEnum.picture,
				onerror: "请上传图片,图片格式为jpg、gif、png"
			});
		}
		//公众号原始ID
		if($('#open_id').length > 0 ){
			$("#open_id").formValidator({
				onshow: "必填",
				onfocus: "公众号ID",
				oncorrect: "填写正确"
			}).inputValidator({
				min: 2,
				max: 100,
				onerror: "不能为空",
				onerrormax: "不能超过50个字符"
			});
		}
		//货源类别
		if($('#col').length > 0 ){
			$("#col").formValidator({
				onshow: "必填",
				onfocus: "必填",
				oncorrect: "选择正确"
			}).inputValidator({
				min: 1,
				onerror: "不能为空"
			});
		}
		//货源名称、发布广告标题
		if($('#title').length > 0 ){
			$("#title").formValidator({
				onshow: "必填",
				onfocus: "名称应该为1-50个汉字",
				oncorrect: "填写正确"
			}).inputValidator({
				min: 2,
				max: 100,
				onerror: "不能为空",
				onerrormax: "不能超过50个汉字"
			});
		}
		//货源封面上传、文章发布上传图片、搞笑图片上传图片、发布广告微信二维码封面
		if($('#image').length > 0 ){
			$("#image").formValidator({
				onshow: "请上传图片",
				onfocus: "请上传图片,图片格式为jpg、gif、png",
				oncorrect: "格式正确"
			}).regexValidator({
				regexp: regexEnum.picture,
				onerror: "请上传图片,图片格式为jpg、gif、png"
			});
		}

	} catch (e) {

	}
})