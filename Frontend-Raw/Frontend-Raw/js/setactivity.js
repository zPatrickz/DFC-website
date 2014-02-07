// JavaScript Document
var topic_shown=false;
var messagebox_timer;
var editor_expanded=true;
var responseid_list=[];
var response={'id':['creater','time','tag','is_important']};
var activity_status=[1,1,1,0,0,1,0,0,0];
var process_shown=false;
var browser='IE';
$(document).ready(function(e) {
	browser=checkbrowser();
	expand_editor();
	setlayout();
	addevents();
	$('#center_bar').css("height",$(document).height()-30);
	$(window).resize(function(){$('#center_bar').css("height",$(document).height()-30);});
	$('#center_bar').click(show_process);
	if(browser!='IE'){
		$('#edit_area').css("margin-bottom",0);//为了能使输入框更加美观。
	}
});

function setlayout(){
}
function addevents(){
	$(window).resize(function(){
		$('#editor_block').css("top",50);}
	);
	//Show the invisible dialog
	$('#invite_friends').click(function(){
		$('#invite_block').css("left",$(window).width()/2-$(invite_block).width()/2);
		$('#invite_block').css("top",Math.max($(window).height()/2-$(invite_block).height()/2,0));
		$('#invite_block').show();
	});
	$('#submit_story').click(function(){
		$('#submit_block').css("left",$(window).width()/2-$(submit_block).width()/2);
		$('#submit_block').css("top",Math.max($(window).height()/2-$(submit_block).height()/2,0));
		$('#submit_block').show();
	});
	$('#dfc_intervene').click(function(){
		$('#intervene_block').css("left",$(window).width()/2-$(intervene_block).width()/2);
		$('#intervene_block').css("top",Math.max($(window).height()/2-$(intervene_block).height()/2,0));
		$('#intervene_block').show();
	});
	/*$(show_process).click(function(){
		$(process_block).css("left",$(window).width()/2-$(process_block).width()/2);
		$(process_block).css("top",Math.max($(window).height()/2-$(process_block).height()/2,0));
		$(process_block).show();
	});*/
	$('#show_contact').click(function(){
		$('#contact_block').css("left",$(window).width()/2-$(contact_block).width()/2);
		$('#contact_block').css("top",Math.max($(window).height()/2-$(contact_block).height()/2,0));
		$('#contact_block').show();
	});
	/*$(giveup_activity).click(function(){
		$(giveup_block).css("left",$(window).width()/2-$(giveup_block).width()/2);
		$(giveup_block).css("top",Math.max($(window).height()/2-$(giveup_block).height()/2,0));
		$(giveup_block).show();
	});
	alert('@');*/
	// Use Click to close the invisible dialog
	$('#invite_friends_close').click(function(){
		$('#invite_block').hide();
	});

/*	$('#show_process_close').click(function(){
		$('#process_block').hide();
	});*/
	$('#submit_story_close').click(function(){
		$('#submit_block').hide();
	});
	$('#dfc_intervene_close').click(function(){
		$('#intervene_block').hide();
	});
	$('#contact_close').click(function(){
		$('#contact_block').hide();
	});
	$('#giveup_story_close').click(function(){
		$('#giveup_block').hide();
	});
	
	//Use Esc to close the invisible Block
	$('#invite_block').keydown(function(event){
		if(event.keyCode==27){
			$('#invite_block').hide();
		}
	});
	$('#submit_block').keydown(function(event){
		if(event.keyCode==27){
			$('#submit_block').hide();
		}
	});
	$('#intervene_block').keydown(function(event){
		if(event.keyCode==27){
			$('#intervene_block').hide();
		}
	});
/*	$('#process_block').keydown(function(event){
		if(event.keyCode==27){
			$('#process_block').hide();
		}
  });
  */
  $('#contact_block').keydown(function(event){
	  if(event.keyCode==27){
		  $('#contact_block').hide();
	  }
  });
  $('#giveup_block').keydown(function(event){
	  if(event.keyCode==27){
		  $('#giveup_block').hide();
	  }
  });
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
	
/*	//Topic expansion
  $(topic_topbar).click(function(event){
	  if(topic_shown){
	  	$(topic_content).hide();
		topic_shown=false;
	  }
	  else{
	  	$(topic_content).show();
		topic_shown=true;
	}
	});
	//Editor block expansion
  $(editor_block).mouseenter(function(event){
	  $(editor_block).css("top",$(window).height()-220);
	  $(editor_content).show();
	  clearTimeout(messagebox_timer);
  });
  $(editor_block).mouseleave(function(event){
	  if(document.activeElement.id!='edit_area'){
		  messagebox_timer=setTimeout(function(){
			$(editor_content).hide();
			$(editor_block).css("top",$(window).height()-50);
		},1000);
	  }
  });
  $(document).click(function(event){
	  if((event.target.id!='edit_area')&&(event.target.id!='editor_topbar')&&(event.target.id!='edit_area')){
		  $(editor_content).hide();
		  $(editor_block).css("top",$(window).height()-50);
	  }
  });*/
	$('#expand_img').click(expand_editor);
	$('#edit_area').keydown(quicksend);
	$('#editor_tags').change(settags);
	$('#editor_submit').click(sendmessage);
	$('#editor_append').click(setattachment);
	refreshevents();
}
function refreshevents(){
	$('[id=img_activity0121]').click(zoominimg);
	$('[id=img_activity0113]').click(zoominimg);
	$('[id=select_operation]').change(perform_operation);
	$('[id=select_operation]').change(perform_operation);
	$('#center_bar').css("height",$(document).height()-30);
}
function setattachment(){
	alert('文件上传和有效性验证，10M以内，最多5个文件，指定文件格式。');
}
function settags(event){
	if($('#editor_tags').val()=='record'){
		alert('这将被当成活动记录处理。');
	}
}
function perform_operation(){
	//get the parent node
	var parent_id=$(this).parent().parent().parent().parent().parent().parent().attr("id");
	if(this.value=='delete'){
		do_delete(parent_id);
	}
	else if(this.value=='mark'){
		do_mark(parent_id);
	}
	else if(this.value=='edit'){
		do_edit(parent_id);
	}
	else if(this.value=='reply'){
		do_reply(parent_id);
	}
	this.value='operation';
}
function do_delete(parent_id){
	if(confirm('确认删除？')){
		alert('deleting reply! my parent is '+parent_id);
	}
}
function do_edit(parent_id){
	if(confirm('确认删除？')){
		alert('deleting reply! my parent is '+parent_id);
	}
}
function do_reply(parent_id){
	if(confirm('确认删除？')){
		alert('deleting reply! my parent is '+parent_id);
	}
}
function do_mark(parent_id){
	var important_txt=$('#'+parent_id).html();
	$('#table_important').append('<tr><td><div id=important_'+parent_id+'>'+important_txt+'</div></td></tr>');
	$('#important_'+parent_id).addClass("response_important");
	refreshevents();
	alert('已经加入永久区!');
}
function zoominimg(event){
	var target=event.target;
	var tempdiv="<div id='tempdiv_outer'><div id='tempdiv'><img src='"+$(target).attr("src")+"' id='tempimg'><div class='share_link' id='share_link'>SHARE LINK</div></div></div>";
	$(document.body).append(tempdiv);
	$('#tempdiv_outer').addClass('tempdiv_outer');
	$('#tempdiv_outer').css("top",$(document).scrollTop());
	$('#tempdiv_outer').css("width",'100%');
	$('#tempdiv_outer').css("height",'100%');
	$('#tempdiv').addClass("zoomin_div");
	$('#tempimg').addClass("zoomin_img");
	$('#tempdiv').css("left",$('#tempdiv_outer').width()/2-350);
	$('#tempdiv').css("top",Math.max($('#tempdiv_outer').height()/2-$('#tempdiv').height()/2,0));
	$('#tempdiv_outer').click(function(){
		$('#tempdiv_outer').remove();
	});
	$('#tempdiv').hover(function(){
		$('#share_link').css("display","inline");
	},
	function(){
		$('#share_link').css("display","none");
	});
	
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
function show_process(){
	if(process_shown){
		$('#process_block').hide();
		$('#center_bar').width(4);
		$('#important_block').show();
		process_shown=false;
	}
	else{
		$('#important_block').hide();
		$('#center_bar').width($(window).width()-$('#center_bar').offset().left-70);
		$('#process_block').show();
		process_shown=true;
	}
}
function expand_editor(){
	if(editor_expanded){
		//minimize;
		editor_expanded=false;
		$('#expand_img').attr("src","image/expand.png");
		$('#expand_img').css("top","8px");
		$('#edit_area').css("height","25px");
		$('#edit_area').css("margin-top","5px");
		$('#editor_attachment').hide();
		$('#editor_bottombar').hide();
		$('#editor_color').hide();
		$('#topspace').css("height",100);
		$('#editor_block').css("background","transparent");
		
	}
	else{
		//expand
		editor_expanded=true;
		$('#expand_img').attr("src","image/contract.png");
		$('#expand_img').css("top","3px");
		$('#edit_area').css("height","90px");
		$('#edit_area').css("margin-top","7px");
		$('#editor_attachment').show();
		$('#editor_bottombar').show();
		$('#editor_color').css("display","inline");
		$('#topspace').css("height",270);
		$('#editor_block').css("background","gold");
	}
}