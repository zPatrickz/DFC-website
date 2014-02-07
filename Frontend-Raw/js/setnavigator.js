// JavaScript Document

$(document).ready(function(e) {
	$('#avatar').hover(function(){
		$("#hidden_div").css("display","inline-block");
		$('#avatar').width(170);
	},
	function(){
		setTimeout(function(){
			$("#hidden_div").hide();
			$('#avatar').width(40);
		},200);
	});
	$('.navitem').click(function(){
		 $('#navul li').removeClass('active');
		 $(this).addClass('active');
	});
});