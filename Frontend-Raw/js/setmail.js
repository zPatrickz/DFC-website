
$(document).ready(function(e) {
	//browser=checkbrowser();
	seteditor();
	$('#mail').click(function(){
		//Show The Detailed Mail
		$('#editor_td').html($('#editor').html());
		var inner_div=$('#mail_detail').html();
		popdialog(event,inner_div);
	});	
	$('#new_mail').click(function(){
		//Write A new Mail
		$('#editor_new').html($('#editor').html());
		var inner_div=$('#send_block').html();
		popdialog(event,inner_div);
	});
});
