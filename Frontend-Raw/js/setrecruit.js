// JavaScript Document
$(document).ready(function(e) {
	//browser=checkbrowser();
	$('#enroll').tooltip({"placement":"right"});
	$('#probleminput').tooltip({'placement':'right'});
	$('#act_1').hover(function(){
		$('#operation_div').show();
	},
	function(){
		setTimeout(function(){
			$('#operation_div').hide();
		},200);
	});
	$('#facediv').click(function(event){
		zoominimg(event,'activity/a0000001/image/poster.jpg');
	});
	$('#enroll').click(function(){
		$('#notvol').modal();
	});
	$('#asfaci').click(function(){
		$('#befaci').modal();
	});
	crec('div2');
	crec('div3');
	crec('div1');
	crec('div2');
	crec('div3');
});

