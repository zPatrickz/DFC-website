// JavaScript Document
// JavaScript Document
var topic_shown=false;
var messagebox_timer;
var responseid_list=[];
var response={'id':['creater','time','tag','is_important']};
var reply_list=[];
var process_shown=false;
var browser='IE';
var activity_id='a0000001';
var Creater='LiMing';
$(document).ready(function(e) {
	//browser=checkbrowser();
	addevents();
	showtask('share',0);
	seteditor();

});

function addevents(){
	$('#mark').tooltip({'placement':'right'});
	$('#cact_name').popover({'placement':'right'});
	$('#zhangsan').popover({'placement':'top'});
		$('#recruit_link').click(function(){
		$('#invitevol').modal();
	});
	$('#placetime_link').click(function(){
		$('#modal_placetime').modal();
	});
	$('#intro_link').click(function(){
		$('#modal_intro').modal();
	});
	$('#contentdes_link').click(function(){
		$('#modal_contentdes').modal();
	});
	$('#contentapp_link').click(function(){
		$('#modal_contentapp').modal();
	});
	$('#manage_link').click(function(){
		$('#modal_manage').modal();
	});
	$('#submit_link').click(function(){
		$('#modal_submit').modal();
	});
	$('#addwork_link').click(function(){
		$('#modal_addwork').modal();
	});
	$('#offline_link').click(function(){
		$('#modal_offline').modal();
	});
	$('#feel_link').click(function(){
		$('#modal_feel').modal();
	});
	$('#feelapp_link').click(function(){
		$('#modal_feelapp').modal();
	});
	$('#imagine_link').click(function(){
		$('#modal_imagine').modal();
	});
	$('#resource_link').click(function(){
		$('#modal_resource').modal();
	});
	$('#doapp_link').click(function(){
		$('#modal_doapp').modal();
	});
	$('#do_link').click(function(){
		$('#modal_do').modal();
	});
	$('#dowork_link').click(function(){
		$('#modal_dowork').modal();
	});
	$('#clip_link').click(function(){
		$('#modal_clip').modal();
	});
	$('#giveup_link').click(function(){
		$('#modal_giveup').modal();
	});
	$('#phone').tooltip({'placement':'right'});
	$('#qq').tooltip({'placement':'right'});
	$('#mail').tooltip({'placement':'right'});
	
	$('#btn-1').click(function(){
		$('.taskcell').hide();
		$('#task-1').show();
	});	
	$('#btn-2').click(function(){
		$('.taskcell').hide();
		$('#task-2').show();
	});
	$('#btn-3').click(function(){
		$('.taskcell').hide();
		$('#task-3').show();
	});
	$('#btn-4').click(function(){
		$('.taskcell').hide();
		$('#task-4').show();
	});
	$('#btn-5').click(function(){
		$('.taskcell').hide();
		$('#task-5').show();
	});
	$('#btn-6').click(function(){
		$('.taskcell').hide();
		$('#task-6').show();
	});
	$('#btn-7').click(function(){
		$('.taskcell').hide();
		$('#task-7').show();
	});
	$('#btn-8').click(function(){
		$('.taskcell').hide();
		$('#task-8').show();
	});
	$('#btn-9').click(function(){
		$('.taskcell').hide();
		$('#task-9').show();
	});
	$('#btn-10').click(function(){
		$('.taskcell').hide();
		$('#task-10').show();
	});
	$('#btn-11').click(function(){
		$('.taskcell').hide();
		$('#task-11').show();
	});
	$('#doublebar').click(function(event){
		if($('.unimportant').css('display')=='none'){
			$('.unimportant').show();
		}
		else if(event.target.id=='doublebar'){
			$('.unimportant').hide();
		}});
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

function showtask(name,op){
		//$('#'+activity_id+'_'+name).show();
		if(op==0){
			$('#'+name+'_show').show();
		}else{
			$('#'+name+'_edit').show();
		}
	}