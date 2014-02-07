// JavaScript Document

var editor_expanded=false;
function seteditor(){
  //Color chooser
  $('#color1').click(function(event){
	  $('#edit_area').css("color",$('#color1').css("background-color"));
	});
  $('#color2').click(function(event){
	  $('#edit_area').css("color",$('#color2').css("background-color"));
	});
  $('#color3').click(function(event){
	  $('#edit_area').css("color",$('#color3').css("background-color"));
	});
  $('#color4').click(function(event){
	  $('#edit_area').css("color",$('#color4').css("background-color"));
	});
  $('#color5').click(function(event){
	  $('#edit_area').css("color",$('#color5').css("background-color"));
	});
	
	$('#expand_editor').click(expand_editor);
	$('#editor_topbar').click(expand_editor);
	$('#edit_area').keydown(quicksend);
	$('#editor_tags').change(settags);
	$('#editor_submit').click(sendmessage);
	$('#editor_append').click(setattachment);
}


function setattachment(){
	alert('文件上传和有效性验证，10M以内，最多5个文件，指定文件格式。');
}
function settags(event){
	if($('#editor_tags').val()=='record'){
		alert('这将被当成活动记录处理。');
	}
}

function expand_editor(){
	if(editor_expanded){
		//minimize;
		editor_expanded=false;
		$('#editor_bottombar').hide();
		$('#edit_area').css("height",24);
		$('#editor_color').hide();
		$('#editor_submit').hide();
		$('#expand_editor').css("height",32);
		$('#response_main').css("height","90%");
		
		
	}
	else{
		//expand
		editor_expanded=true;
		$('#editor_bottombar').show();
		$('#edit_area').css("height",130);
		$('#editor_color').show();
		$('#editor_submit').show();
		$('#expand_editor').css("height",132);
		if(browser=="IE"){
			$('#response_main').css("height","460px");
		}
	}
}


function quicksend(event){
	if(event.ctrlKey&&event.keyCode==13){
		//send message;
		$('#message_form').submit();
		sendmessage();
	}
}
function sendmessage(){
	$('#editor_tags').attr("value","operation");
	if(editor_expanded){
		expand_editor();
	}
	alert('Send Message!');
}