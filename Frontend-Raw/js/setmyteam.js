// JavaScript Document

$(document).ready(function(e) {
	$('#liujinguo').popover();
	seteditor();
	$('#info_link').click(function(){
		 $('#team_ul li').removeClass('active');
		 $('#info_link').addClass('active');
		 $('.team_block').hide();
		 $('#info_block').show();
	});
	$('#chat_link').click(function(){
		 $('#team_ul li').removeClass('active');
		 $('#chat_link').addClass('active');
		 $('.team_block').hide();
		 $('#chat_block').show();
	});
	$('#vol_link').click(function(){
		 $('#team_ul li').removeClass('active');
		 $('#vol_link').addClass('active');
		 $('.team_block').hide();
		 $('#vol_block').show();
	});
	$('#member_link').click(function(){
		 $('#team_ul li').removeClass('active');
		 $('#member_link').addClass('active');
		 $('.team_block').hide();
		 $('#member_block').show();
	});
	$('#request_link').click(function(){
		 $('#team_ul li').removeClass('active');
		 $('#request_link').addClass('active');
		 $('.team_block').hide();
		 $('#request_block').show();
	});
});