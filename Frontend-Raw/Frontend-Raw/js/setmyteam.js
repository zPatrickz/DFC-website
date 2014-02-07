// JavaScript Document

$(document).ready(function(e) {
	$('#show_mem').click(function(){
		$('#volunteer_block').hide();
		$('#member_block').show();
	});
	$('#show_vol').click(function(){
		$('#volunteer_block').show();
		$('#member_block').hide();
	});
});