
$(document).ready(function(e) {
	//browser=checkbrowser();
	seteditor();
	$('#mail').click(function(){
		//Show The Detailed Mail
		$('#detailed_view').modal();
	});	
	
	$('#send_btn').click(function(){
		 $('#modal_send').modal();
	});
	$('#sended_link').click(function(){
		 $('#mail_ul li').removeClass('active');
		 $('#sended_link').addClass('active');
		 $('.mes_block').hide();
		 $('#sended_block').show();
	});
	$('#recieved_link').click(function(){
		 $('#mail_ul li').removeClass('active');
		 $('#recieved_link').addClass('active');
		 $('.mes_block').hide();
		 $('#received_block').show();
	});
	$('#recruit_link').click(function(){
		 $('#mail_ul li').removeClass('active');
		 $('#recruit_link').addClass('active');
		 $('.mes_block').hide();
		 $('#recruit_block').show();
	});
	$('#newact_link').click(function(){
		 $('#mail_ul li').removeClass('active');
		 $('#newact_link').addClass('active');
		 $('.mes_block').hide();
		 $('#newact_block').show();
	});
	$('#actnotice_link').click(function(){
		 $('#mail_ul li').removeClass('active');
		 $('#actnotice_link').addClass('active');
		 $('.mes_block').hide();
		 $('#actnotice_block').show();
	});
	$('#groupnotice_link').click(function(){
		 $('#mail_ul li').removeClass('active');
		 $('#groupnotice_link').addClass('active');
		 $('.mes_block').hide();
		 $('#groupnotice_block').show();
	});
	$('#contact_btn').click(function(){
		 $('#modal_contact').modal();
	});
});
