// 字符串操作
String.prototype.startWith=function(str){
    var reg=new RegExp("^"+str);
    return reg.test(this);
}
//测试ok，直接使用str.endWith("abc")方式调用即可
String.prototype.endWith=function(str){
    var reg=new RegExp(str+"$");
    return reg.test(this);
};

Array.prototype.indexOf = function(val) {
    for (var i = 0; i < this.length; i++) {
        if (this[i] == val) return i;
    }
    return -1;
};
Array.prototype.remove = function(val) {
    var index = this.indexOf(val);
    if (index > -1) {
        this.splice(index, 1);
    }
};

String.prototype.format = function(args) {
    var result = this;
    if (arguments.length > 0) {
        if (arguments.length == 1 && typeof (args) == "object") {
            for (var key in args) {
                if(args[key]!=undefined){
                    var reg = new RegExp("({" + key + "})", "g");
                    result = result.replace(reg, args[key]);
                }
            }
        }
        else {
            for (var i = 0; i < arguments.length; i++) {
                if (arguments[i] != undefined) {
                    //var reg = new RegExp("({[" + i + "]})", "g");//这个在索引大于9时会有问题，谢谢何以笙箫的指出
                    var reg= new RegExp("({)" + i + "(})", "g");
                    result = result.replace(reg, arguments[i]);
                }
            }
        }
    }
    return result;
};

function strip(str){
    return str.replace(/^\s+|\s+$/g,"");
}

String.prototype.strip=function() {
    return this.replace(/^\s+|\s+$/g,"");
};

// 随机字条串
function randomString(len) {
    len = len || 32;
    var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';    /****默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1****/
    var maxPos = $chars.length;
    var pwd = '';
    for (i = 0; i < len; i++) {
        pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
    }
    return pwd;
}

// 原生取得cookie值
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

// 通用的原生URL POST请求
function http(data,url,callback) {

    function createXHttpRequest() {
        if (window.ActiveXObject) {
            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        else if (window.XMLHttpRequest) {
            xmlhttp = new XMLHttpRequest();
        }
        else {
            return;
        }
    }

    function starRequest(data) {
        createXHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4) {
                var code = xmlhttp.status;
                callback(code, xmlhttp.responseText);


            }
        };
        xmlhttp.open("POST", url, true);
        xmlhttp.send(data);
    }
    starRequest(data);
}

/***************************************************** 高度测试 *******************************************/
//获取滚动条当前的位置
function getScrollTop() {
    var scrollTop = 0;
    if (document.documentElement && document.documentElement.scrollTop) {
        scrollTop = document.documentElement.scrollTop;
    }
    else if (document.body) {
        scrollTop = document.body.scrollTop;
    }
    return scrollTop;
}

//获取当前可是范围的高度
function getClientHeight() {
    var clientHeight = 0;
    if (document.body.clientHeight && document.documentElement.clientHeight) {
        clientHeight = Math.min(document.body.clientHeight, document.documentElement.clientHeight);
    }
    else {
        clientHeight = Math.max(document.body.clientHeight, document.documentElement.clientHeight);
    }
    return clientHeight;
}

//获取文档完整的高度
function getScrollHeight() {
    return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);
}

function setOnScrollFun(fun){
    window.onscroll = function () {
        if (getScrollTop() + getClientHeight() == getScrollHeight()) {
            fun();
        }
    }
}

setOnScrollFun.get_min_column = function (column_name, num) {

        var height_array = [];
        for (var i = 0; i < num; i++) {
            height_array.push($(column_name + (i + 1)).height());
        }

        var min_index = 0;
        for (var i = 0; i < height_array.length; ++i) {
            if (height_array[min_index] > height_array[i]) {
                min_index = i;
            }
        }

        var column = $(column_name + (min_index+1));
        return column;
    };


/***************************************************** 自动调整 frame 高度 *********************************/

function getDocHeight(doc){
    //在IE中doc.body.scrollHeight的可信度最高
    //在Firefox中，doc.height就可以了
    var docHei = 0;
    var scrollHei;//scrollHeight
    var offsetHei;//offsetHeight，包含了边框的高度

    if (doc.height){
        //Firefox支持此属性，IE不支持
        docHei = doc.height;
    }
    else if(doc.documentElement){
        if(doc.documentElement.offsetHeight) docHei = offsetHei = doc.documentElement.offsetHeight;
        if(doc.documentElement.scrollHeight) docHei = scrollHei = doc.documentElement.scrollHeight;
    }
    else if (doc.body){
        //在IE中，只有body.scrollHeight是与当前页面的高度一致的，
        //其他的跳转几次后就会变的混乱，不知道是依照什么取的值！
        //似乎跟包含它的窗口的大小变化有关
        if(doc.body.offsetHeight) docHei = offsetHei = doc.body.offsetHeight;
        if(doc.body.scrollHeight) docHei = scrollHei = doc.body.scrollHeight;
    }

    /*
      docHei = Math.max(scrollHei,offsetHei);//取最大的值，某些情况下可能与实际页面高度不符！
    */
    return docHei+'px';
}

function doReSize(){
    var iframeWin = window.frames['center_frame'];
    var iframeEl = window.document.getElementById? window.document.getElementById('center_frame'): document.all? document.all['center_frame']: null;
    if ( iframeEl && iframeWin ){
        var docHei = getDocHeight(iframeWin.document);
        if (docHei != iframeEl.style.height) iframeEl.style.height = docHei;
    }
    else if(iframeEl){
        var docHei = getDocHeight(iframeEl.contentDocument);
        if (docHei != iframeEl.style.height) iframeEl.style.height = docHei;
    }
}

function runResizeTask(){
    doReSize();
    setTimeout("runResizeTask()",100);//每隔1秒执行一次
}

/****************************************************************************************************/


// 后台管理的标准发送文件
function sendFile(form_name, input_name, value_name) {

    if(jQuery("input[name='"+input_name+"']").val() === ""){
	alert('请先选择图片');
	return;
    }

    var data = new FormData(jQuery("form[name='"+form_name+"']")[0]);
    var url = "/upload_image"; // /upload

    var loading_img = jQuery("input#"+value_name).nextAll().find('img.load-flag');
    loading_img.css('display', 'block');

    var callback = function(code, html)
    {
       loading_img.css('display', 'none');
       if (code == 200){
            jQuery("input#"+value_name).val(html);
            var file = jQuery("input#"+input_name);
            file.after(file.clone().val(""));
            file.remove();
        }
    };

    http(data,url,callback);
}


// 后台的选择级联
function select_join(src, dst, parent, child){
    link = '/select/join/';

    var child_select= jQuery("#"+child);
    var parent_select= jQuery("#"+parent);
    var id = parent_select.val();

    var _xsrf = '_xsrf='+getCookie("_xsrf");
    jQuery.ajax({url: link+dst+'/'+src+'/'+id+'?'+_xsrf,
                 type: "get",
                 dataType: "json",
                 success: function(arr){
                     child_select.empty();

                     for (var i=0; i< arr['data'].length; ++i) {
                         e = arr['data'][i];
                         child_select.append("<option value='"+e.id+"'>"+e.name+"</option>");
                     }


		     if (child_select.prev('span'))
                 child_select.prev('span').html('');

                     try {
                         child_select.uniform({selectAutoWidth: false});
                     }
                     catch (e){}
                 }//function

                });
}

// 直接使用JS组织和发送FORM数据，发送前会做数据检查
function form_submit() {
    var form = jQuery(this).closest('form');

    try{

        var validator = form.validate();
        if (!validator.form()) return;

    }catch(error){}



    try {
        CKupdate();
    }
    catch(error){
    }

    var _xsrf = '&_xsrf='+getCookie("_xsrf");

    jQuery.ajax({
        type: 'POST',
        url: form.attr('action'),
        dataType: 'json',
        data: form.serialize()+_xsrf,
        success: function(data) {
            if(data.errno < 0){
                alert('操作失败: '+data.msg);
            }
            else{
                if(data.hasOwnProperty('msg'))
                    alert(data.msg);
                else
                    alert('操作成功');
                if(!data.hasOwnProperty('keep')){
                    var frame = window.parent.document.getElementById("center_frame");
                    frame.style.height= '0px';
                    frame.src = frame.getAttribute('return_src') ;
                }
            }
        }
    });

    return false;
}

function static_link(link){
    //var _xsrf = '&_xsrf='+getCookie("_xsrf");
    jQuery.ajax({
        type: 'GET',
        url: link,
        dataType: 'json',
        success: function(data) {
            if(data.errno < 0){
                alert('操作失败: '+data.msg);
            }
            else{
                alert('操作成功');
                if(data.hasOwnProperty('keep')){
                    var frame = window.parent.document.getElementById("center_frame");
                    frame.style.height= '0px';
                    frame.src = location.href;
                }
            }
        }
    });
}

function batch_opt(obj) {

    var select_list = ""

    var parent = jQuery(obj).parents('table');
    var opt = parent.find('select#batch_select').val();
    var check_list = parent.find('.checkchild');

    jQuery.each(check_list, function(){
        if(jQuery(this).is(':checked')) {
           select_list+='|'+jQuery(this).val();
        }
    });


    select_list = select_list.replace(/^\|/, '');
    var _xsrf = '&_xsrf='+getCookie("_xsrf");
    jQuery.ajax({
        type: 'POST',
        dataType: 'json',
        data: 'opt=batch&type='+opt+'&list='+select_list+_xsrf,
        success: function(data){
            if(data.errno<0){
                alert('操作失败: '+data.msg);
            }
            else{
                alert('操作成功');
                if(!data.hasOwnProperty('keep')){
                    var frame = window.parent.document.getElementById("center_frame");
                    frame.style.height= '0px';
                    frame.src = frame.getAttribute('return_src') ;
                }
            }
        }
    });

    return false;
}


jQuery(document).ready(function (){

    jQuery('.upload-image').mouseenter(function(e){
          var src = jQuery(this).val();

          if(src==""){
             return;
          }

          offset =jQuery(this).offset();
          var tooltip = jQuery('div.image_tooltip');

          tooltip.css('left', offset.left+'px');
          tooltip.css('top', (offset.top+30)+'px');
          tooltip.css('display', 'block');

          tooltip.find('img').attr('src', src);
    });

    jQuery('.upload-image').mouseleave(function(){
         var tooltip = jQuery('div.image_tooltip');
         tooltip.css('display','none');
    });

    jQuery('a.static_link').live('click', function(){
        var link = jQuery(this).attr('href');
        static_link(link);
        return false;
    });

    try {
    jQuery.validator.addMethod("datetime", function(value, element) {
                var reg_datetime = /^(\d{1,4})(-|\/)(\d{1,2})\2(\d{1,2}) (\d{1,2}):(\d{1,2})(:(\d{1,2}))?$/;
                return this.optional(element) || reg.test(value);
            }, "请填写正确的日期格式, 如 2014-06-12 12:00");

    }
    catch(e){

    }
});
