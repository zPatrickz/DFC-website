// JavaScript Document

function seteditor(){
  //Color chooser
  $('#color1').click(function(event){
	  $('#full_area').css("color",$('#color1').css("background-color"));
	});
  $('#color2').click(function(event){
	  $('#full_area').css("color",$('#color2').css("background-color"));
	});
  $('#color3').click(function(event){
	  $('#full_area').css("color",$('#color3').css("background-color"));
	});
  $('#color4').click(function(event){
	  $('#full_area').css("color",$('#color4').css("background-color"));
	});
  $('#color5').click(function(event){
	  $('#full_area').css("color",$('#color5').css("background-color"));
	});
	
	$('#expand_editor').click(function(){
		$('#editor_simp').hide();
		$('#editor_full').show();
	});
	$('#editor_minimize').click(function(){
		$('#editor_full').hide();
		$('#editor_simp').show();
	});
	$('#simp_input').keydown(quicksend);
	$('#full_submit').click(sendmessage);
	$('#full_append').click(function(){
		$('#modal_repapp').modal();
	});
}



function quicksend(event){
	if(event.keyCode==13){
		//send message;
		sendmessage();
	}
}
function sendmessage(){
	$('#editor_tags').attr("value","operation");
	$('#editor_full').hide();
	$('#editor_simp').show();
	alert('Send Message!');
}