// JavaScript Document

$(document).ready(function() {
//	developermodeon();
//	detectversion();
	initialize();
	addevents(); 
})

function detectversion(){
	//此代码在windows 8 的 IE 12下无法正常运行。
	var userAgent=navigator.userAgent
  	browser={
		ischrome:/Chrome/.test(userAgent),
		version:(userAgent.match(/(?:Chrome|rv)[\/: ]([\d.]+)/))[1],
   	} /* 获得浏览器的名称及版本信息 */
}
function developermodeon(){
	//Show the borders of all div and table element
	$("div").css("border","dotted")
	$("td").css("border","dotted")
}
function setspecialentrance(user_type){
	//Displace the Entrances of special characters.
	if(user_type==0){
		$(login_tag).text("管理员通道");
	}
	else if(user_type==1){
		$(login_tag).text("团队成员通道");
	}
	else if(user_type==2){
		$(login_tag).text("志愿者通道");
	}
	else{
		$(login_tag).css("display","none");
	}
}
function initialize(){
	$(magazine_content).css("background-image","url(image/default_bg.jpg)");
	$(activity_img).attr("src","activity/"+activity_list[current_activity_index]+"/image/"+img_list[current_img_index]);
	gallery_changer=setInterval(next_img,5000);
}
function next_img(){
	//shuffle right
	current_img_index=(current_img_index+1)%img_n;
	var cindex=activity_indexer.indexOf(current_img_index);
	if(cindex!=-1){
		//change the activity;
		$('#title_'+current_activity_index).css("background-color","transparent");
		current_activity_index=cindex;
		$('#title_'+current_activity_index).css("background-color","black");
	}
	$(activity_img).attr("src","activity/"+activity_list[current_activity_index]+"/image/"+img_list[current_img_index]);
}
function pre_img(){
	//shuffle left
	var cindex=activity_indexer.indexOf(current_img_index);
	if(cindex!=-1){
		//change the activity;
		$('#title_'+current_activity_index).css("background-color","transparent");
		current_activity_index=(cindex+activity_n-1)%activity_n;
		$('#title_'+current_activity_index).css("background-color","black");
	}
	current_img_index=(current_img_index+img_n-1)%img_n;
	$(activity_img).attr("src","activity/"+activity_list[current_activity_index]+"/image/"+img_list[current_img_index]);
}
function addevents(){
	$(left_button).mouseenter(function(event){$(left_button_img).show();});
	$(left_button).mouseleave(function(event){$(left_button_img).hide();});
	$(right_button).mouseenter(function(event){$(right_button_img).show();});
	$(right_button).mouseleave(function(event){$(right_button_img).hide();});
	$(magazine_img).mouseenter(function(event){clearInterval(gallery_changer);});
	$(magazine_img).mouseleave(function(event){gallery_changer=setInterval(next_img,5000);});
	$(left_button).click(pre_img);
	$(right_button).click(next_img);
	$(activity_img).click(changeview);
	$(action_do).click(changestep);
	$(action_share).click(changestep);
	$(action_feel).click(changestep);
	$(action_imagine).click(changestep);
	$(step_do).click(changestep);
	$(step_share).click(changestep);
	$(step_feel).click(changestep);
	$(step_imagine).click(changestep);
	$(close_png).click(changeview);
	$(user_tag).click(show_userpanel);
	$(to_register).click(function(){
		$(login_div).hide();
		$(register_div).show();
		$(user_tag).text("请注册");
	});
	$(to_login).click(function(){
		$(register_div).hide();
		$(login_div).show();
		$(user_tag).text("请登陆");
	});
}
function show_userpanel(event){
	if(userpanel_shown){
		//Hide the user panel
		$(userpanel).css("left",'-310px');
		userpanel_shown=false;
	}
	else{
		//Show the user panel
		$(userpanel).css("left",$(window).width()/2-$(userpanel).width()/2);
		userpanel_shown=true;
	}
}
function changestep(event){
	target=event.target;
	//dehighlight
	if(current_step!=4){
		$('#'+four_steps[current_step]).css("color","rgba(255,255,0,1)");
		$('#'+four_steps[current_step]).css("border-bottom-color","rgba(255,255,0,1)");
		$('#'+action_steps[current_step]).hide();
	}
	var cstep=four_steps.indexOf($(target).attr("id"));
	if(cstep==-1){
		current_step=(current_step+1)%4;
	}
	else{
		current_step=cstep;
	}
	$('#'+action_steps[current_step]).show();
	$('#'+four_steps[current_step]).css("color","rgba(255,150,0,1)");
	//$(step_do).css("padding-bottom","30px");
	$('#'+four_steps[current_step]).css("border-bottom-color","rgba(255,150,0,1)");
	//show the step frame
}
function highlight(target){
	$(step_share).css("color","rgba(255,255,0,1)");
	$(step_share).css("border-bottom-color","rgba(255,255,0,1)");
	//$(step_do).css("text-indent","-10ch");
	$(target).css("color","rgba(255,150,0,1)");
	//$(step_do).css("padding-bottom","30px");
	$(target).css("border-bottom-color","rgba(255,150,0,1)");
}

//Show or hide the detail view and magic view;
function changeview(event){
	if(showing_details){
		$(magazine_main).show();
		$(detail_main).css("display","none");
		$(magic_main).show();
		showing_details=false;
		$('#'+action_steps[current_step]).hide();
		$('#'+four_steps[current_step]).css("color","rgba(255,255,0,1)");
		$('#'+four_steps[current_step]).css("border-bottom-color","rgba(255,255,0,1)");
		current_step=4;
	}
	else{
		$(magazine_main).hide();
		$(detail_main).css("display","block");
		$(magic_main).hide();
		showing_details=true;
		$(action_feel).show();
		$(step_feel).css("color","rgba(255,150,0,1)");
		//$(step_do).css("padding-bottom","30px");
		$(step_feel).css("border-bottom-color","rgba(255,150,0,1)");
		current_step=0;
	}
}