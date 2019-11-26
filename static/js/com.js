var WEIXIN = {};
WEIXIN.method = {
	init: function() {
		this.search();
		this.tabs('.theNumber');
		this.tabs('.list');
		this.change();
		this.diagBox();
		this.showCode();
		this.showTip();
		this.showArticle();
		this.gotoLink();
	},
	search: function() {
		$('.label').click(function() {
			$('#s_label').toggle();
			$('#s_label li').click(function() {
				var s = $(this).html();
				$('.label span').html(s);
				$('#s_label').hide();
			});
		});
		$('.serTxt').focus(function() {
			$('#s_btn').css('background-position-y', '-47px')
		});
		$('.serTxt').blur(function() {
			$('#s_btn').css('background-position-y', '-20px')
		});
	},
	tabs: function(str) {
		$(str).siblings('.centerDisArea').find('.title a').hover(function() {
			$(this).parent().parent().siblings(str).hide();
			$(this).parent().parent().find('a').removeClass('active');
			$(this).parent().parent().siblings(str).eq($(this).parent().index()).show();
			$(this).addClass('active');
		});
	},
	change: function() {
		$('.td_tabs').click(function() {
			$('.td_tabs').children('span').removeClass('active');
			$(this).children('span').addClass('active');
		});
	},
	diagBox: function() {
		var layout = $('.blacklayout');
		var diag = $('.diagBox');
		var _w = $(document).width();
		var wid = $('.diagBox').width();
		var _hei = $(document).height();
		var _top = ($(window).height() - diag.height()) / 2;
		diag.css('top', _top);
		$(".top_login, .top_reg").live('click',function() {
			layout.show();
			layout.height(_hei);			
			if($(this).hasClass("top_login")){
				innerTabs(".mobile_login");
			}else {
				innerTabs(".mobile_reg");
			}
			diag.show();
		});		
	
		$('.closeBox').click(function() {
			layout.hide();
			diag.hide();
		});
		
		//注册
		$(".to_reg").click(function(){
			innerTabs(".mobile_reg");
		});
		
		//找回密码
		$(".to_find").click(function(){
			innerTabs(".mobile_find");
		});
		
		$('.wx_login a').click(function() {
			layout.hide();
			diag.hide();
		});
		function innerTabs(str) {
			$(".inner").hide();
			$(str).show();
		}
		diag.css({
            position: 'fixed',
            left: (_w - wid) / 2
        });
	},
	showCode: function() {
		$('.wechat-con').find('li').hover(
			function() {
				$(this).children('.wechat-code').show(300);
			}, function() {
				$(this).children('.wechat-code').hide(300);
			}
		)
	},
	showTip: function() {
		$('.p_c').find("li").each(function(){					
			$(this).hover(function() {
				var _hei = $(this).children(".tip").height()+12;			
				var a = $(this).width();
				var b = $(this).children(".tip").width();
				var _wid = (a-b)/2 - 5;	
				$(this).children(".tip").css({
					"top": -(_hei),
					"left": _wid
				})
				$(this).children(".tip:last-child").css("top",-(_hei-4));
				$(this).children(".tip").show();
			}, function() {
				$(this).children(".tip").hide();
			})
		})
	},
	showArticle:function(){
		$(".atten").hover(function(){
			$(this).siblings(".pos-box").show();
		},function(){
			$(this).siblings(".pos-box").hide();
		})
	},
	
	//翻页go
	gotoLink: function() {			
		
		var count = 0;
		$(".isTxtBig").focus(function(){
			if($(this).val())count = $(this).val();
		}).blur(function(){
			if($(this).val())count = $(this).val();
			var str = page_link;
			if(count != 0)
			{
				str += count - 1;
				$("#link").attr("href", str);
			}
		});
		
	}
}
$(document).ready(function() {
	WEIXIN.method.init();
	$("#tab1").find("h2").hover(function(){
		var i = $(this).index();
		$(this).siblings().removeClass("active");
		$(this).siblings().children("span").css("display","none");
		$(this).addClass("active");
		$(this).children("span").css("display","block");
		$("#more").children("a").hide();
		$("#more").children("a").eq(i).show();
		$(".wxqun").hide();
		$(".wxqun").eq(i).show();
	});
	$("#citymore").click(function(){$("#citybox").toggleClass("expend")});
	$(".menu li").hover(function(){
		$(this).children("div").show();
	},function(){
		$(this).children("div").hide();
	})
    
    if (!user_login){
        $('.user-center').each(function(index){
            $(this).addClass('diag');
        });
    }
})
$(document).ready(function() {
	WEIXIN.method.init();
	$("#tab2").find("h2").hover(function(){
		var i = $(this).index();
		$(this).siblings().removeClass("active");

		$(this).addClass("active");
		$(this).children("span").css("display","block");
		$("#more").children("a").hide();
		$("#more").children("a").eq(i).show();
		$(".gjqun").hide();
		$(".gjqun").eq(i).show();
		if(i==0){
			$("#publish_url").attr('href','/user_center/group?topic_id=2');
		}else{
			$("#publish_url").attr('href','/user_center/group?topic_id=1');
		}
	});
	$("#citymore").click(function(){$("#citybox").toggleClass("expend")});
	$(".menu li").hover(function(){
		$(this).children("div").show();
	},function(){
		$(this).children("div").hide();
	})	

})

