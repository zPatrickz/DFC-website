$(document).ready(function(){
	$(".toggle-div").click(function() {
	   	if($("#"+this.id+'_content').hasClass("hide")){
	   		$("#"+this.id+'_content').removeClass("hide");
	    	$(this).text("关闭");
	   	}
	   	else{
	   		$("#"+this.id+'_content').addClass("hide");
	    	$(this).text("展开");
	   	}
	});
	$(".hover-div").hover(
		function() {
			share(this.id);
		   	if($("#"+this.id+'_content').hasClass("hide")){
		   		$("#"+this.id+'_content').removeClass("hide");
		   	}
	   	},
	   	function(){
		   	if(!$("#"+this.id+'_content').hasClass("hide")){
		   		$("#"+this.id+'_content').addClass("hide");
	    	}
	   	}
	);
	

});


function share(content){
	window._bd_share_config = {
		common : {
			bdText : content,	
			bdDesc : '自定义分享摘要',	
			bdUrl : '自定义分享url地址', 	
			bdPic : '自定义分享图片'
		},
		share : [{
			"bdSize" : 16
		}],
		image : [{
			viewType : 'list',
			viewPos : 'top',
			viewColor : 'black',
			viewSize : '16',
			viewList : ['qzone','tsina','huaban','tqq','renren']
		}]
	}
	with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?cdnversion='+~(-new Date()/36e5)];
}
