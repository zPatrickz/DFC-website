// JavaScript Document
var browser='IE';
var action_steps=["action_feel","action_imagine","action_do","action_share"];
var four_steps=["step_feel","step_imagine","step_do","step_share"];
var current_step=0;
$(document).ready(function(e) {
	browser=checkbrowser();
	$('#'+action_steps[current_step]).show();
	$('#'+four_steps[current_step]).css("color","orange");
	//$(step_do).css("padding-bottom","30px");
	$('#'+four_steps[current_step]).css("background-color",'transparent')
	$('#'+four_steps[current_step]).css("border-bottom-width","0px");
	if(browser=='IE'){
		$('#copy_block').html('<input type="button" class="share_btn" value="复制分享链接" alt="file:///D:/dfcwebsite/activity_show.html" id="share_link">');
		$('#share_link').click(copydata);
	}
	else{
		$('#copy_block').html('<p class="introduction">您可以通过这个分享链接把这个故事告诉更多的人~<br>file:///D:/dfcwebsite/activity_show.html</p>');
	}
    addevents();
});
function addevents(){
	$('#step_do').click(changestep);
	$('#step_share').click(changestep);
	$('#step_feel').click(changestep);
	$('#step_imagine').click(changestep);
	$('#a0000001_1').click(zoominimg);
	$('#a0000001_2').click(zoominimg);
	$('#a0000001_3').click(zoominimg);
	$('#a0000001_4').click(zoominimg);
}

function changestep(event){
	target=event.target;
	//dehighlight
	if(current_step!=4){
		$('#'+four_steps[current_step]).css("color","gold");
		$('#'+four_steps[current_step]).css("background-color","rgba(61,122,183,1)");
		$('#'+action_steps[current_step]).hide();
		$('#'+four_steps[current_step]).css("border-bottom-width","3px");
	}
	var cstep=four_steps.indexOf($(target).attr("id"));
	if(cstep==-1){
		current_step=(current_step+1)%4;
	}
	else{
		current_step=cstep;
	}
	$('#'+action_steps[current_step]).show();
	$('#'+four_steps[current_step]).css("color","orange");
	//$(step_do).css("padding-bottom","30px");
	$('#'+four_steps[current_step]).css("background-color",'transparent')
	$('#'+four_steps[current_step]).css("border-bottom-width","0px");
	//show the step frame
}

function copydata(){
    var data = $('#share_link').attr("alt");
	if(browser=='IE'){
		window.clipboardData.setData('text', data );
		alert('YOU COPYED DATA: '+data);
	}
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