// JavaScript Document
$(document).ready(function(e) {
	//browser=checkbrowser();
	$('#enroll_link').tooltip({"placement":"right"});
	$('#probleminput').tooltip({'placement':'right'});
	$('#act_1').hover(function(){
		$('#operation_div').show();
	},
	function(){
		setTimeout(function(){
			$('#operation_div').hide();
		},200);
	});
	$('#enroll_link').click(function(){$('#modal_enroll').modal();});

});

