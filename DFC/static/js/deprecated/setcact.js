// JavaScript Document
$(document).ready(function() {
	$(window).resize(function(){
		$('.outerdiv').css("width",$(window).width());
		$('.maintable').css("width",$(window).width()*4);
	});
	$('.outerdiv').css("width",$(window).width());
	$('.maintable').css("width",$(window).width()*4);
	$('#tovol').click(function(){
		$('#maintable').css("left","-300%");
	});
	$('#finish').click(function(){
		document.location="myact.html"
	});
	$('#towherewhen,#towherewhen2').click(function(){
		$('#maintable').css("left","-200%");
	});
	$('#tointro,#tointro2').click(function(){
		$('#maintable').css("left","-100%");
	});
});
