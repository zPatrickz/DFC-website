// JavaScript Document
$(document).ready(function() {
	$(window).resize(function(){
		$('.outerdiv').css("width",$(window).width());
		$('.maintable').css("width",$(window).width()*4);
	});
	$('.outerdiv').css("width",$(window).width());
	$('.maintable').css("width",$(window).width()*4);
	$('#tocontent').click(function(){
		$('#maintable').css("left","-400%");
	});
	$('#tovol').click(function(){
		$('#maintable').css("left","-300%");
	});
	$('#finish').click(function(){
		document.location="mydfc_index.html"
	});
	$('#towherewhen').click(function(){
		$('#maintable').css("left","-200%");
	});
	$('#tointro').click(function(){
		$('#maintable').css("left","-100%");
	});
});
