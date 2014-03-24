// JavaScript Document
var username='Jack';
var character='Normal';//Team Volunteer Normal Administrator
var act1=new Activity('a0000001','cacate',['LiMing','Jack','谢闯','徐沐阳','王强华','cacate'],currentTime(),currentTime(),{'create':'','intro':new Intro('为流浪猫找个家','翠竹园小区的流浪猫非常可爱，软软的，绵绵的，暖暖的，像水一样，像糖一样，像永远不想醒来的被窝一样。','face.jpg'),'wherewhen':new WhereWhen(currentTime_min(),'翠竹园小区'),'volunteer':'','content':'','work_distri':'','feel':'','imagine':'','do':'','share':'','submit':''},[1,1,1,0,0,0,0,0,0,0],[1,2,3,4],0,0,0);
var act2=new Activity('a0000002','Jack',['LiMing','Jack','谢闯','徐沐阳','王强华','cacate'],currentTime(),currentTime(),{'create':'','intro':new Intro('翠竹园的童书屋建设','翠竹园小区居然没有童书屋，没有，完全没有，全部没有，要有，一定要有。','face.gif'),'wherewhen':new WhereWhen(currentTime_min(),'翠竹园小区'),'volunteer':'','content':'','work_distri':'','record':'','share':'','submit':''},[1,1,1,0,0,0,0,0],[],0,0,0);
var acts={'a0000001':act1,'a0000002':act2};

function Response(ID,sender,time,text,files,tags,father_id,color){
	if(!arguments[7]){color='white';}
	this.id=ID;
	this.sender=sender;
	this.time=time;
	this.text=text;
	this.files=files;
	this.tags=tags;
	this.operations=['reply'];
	this.color=color;
	this.father_id=father_id;
	if(character=='Team' || username==acts[father_id].creater || character=='Administrator'){
		this.operations.push("delete");
		this.operations.push("mark");
	}
	else if(sender==username){
		this.operations.push("delete");
	}
	this.reply=function(){};
}

function Mail(ID,sender,reciever,time,title,text,files,color){
	if(!arguments[7]){color='white';}
	this.id=ID;
	this.sender=sender;
	this.reciever=reciever;
	this.time=time;
	this.title=title;
	this.text=text;
	this.files=files;
	this.color=color;
}
function Activity(ID,creater,userlist,create_time,update_time,tasks,task_status,replys,abandoned,completed,frozen){
	this.userlist=[];
	this.id=ID;
	this.creater=creater;
	this.tasks=tasks;
	this.create_time=create_time;
	this.update_time=update_time;
	this.task_status=task_status;
	this.completed=completed;
	this.abandoned=abandoned;
	this.frozen=frozen;
	this.replys=replys;
	this.face=tasks['intro'].face;
	this.name=tasks['intro'].name;
	this.description=tasks['intro'].text;
}

function Intro(name,text,face){
	this.name=name;
	this.text=text;
	this.face=face;
}

function WhereWhen(time,place){
	this.time=time;
	this.place=place;
}
function append_reply(res,fatherdiv){
	var res_html='<div id="'+res.id+'" class="response_main">\
<table>\
<tr><td width="120px" align="right" valign="top" class="response_left">\
<div class="left_row"><a href="#">'+res.sender+'</a></div>\
<div class="left_row">'+res.time+'</div>\
<div class="left_row">';
	//Add Tags
	var n=res.tags.length;
	var i=0;
	for(i=0;i<n;i++){
		res_html=res_html+'<img src="image/icon/'+res.tags[i]+'.png" class="tag_img" alt="'+res.tags[i]+'" title="'+res.tags[i]+'">';
	}
	if(character=='Team' || username==acts[res.father_id].creater || character=='Administrator'){
		res_html=res_html+'<img src="image/icon/add.png" class="tag_img" alt="添加标签" title="添加标签">';
	}
	res_html=res_html+'</td><td valign="top">\
    <div class="response_content">\
    <div class="text_block"><p style="margin-left:30px; margin-right:30px; color:'+res.color+'">'+res.text+'</p></div>\
    <div class="file_block" align="left">';
	//Add Files
    n=res.files.length;
	i=0;
	for(i=0;i<n;i++){
		var elem=res.files[i].split('.');
		if(elem[elem.length-1].toLowerCase()=='jpg'){
			res_html=res_html+'<div class="figure_div" id="file_'+res.id+'_'+i+'"><a href="#"><img src="activity/'+res.father_id+'/image/'+res.files[i]+'" class="default_img" ></a></div>';
		}
		else{
			res_html=res_html+'<div class="figure_div" id="file_'+res.id+'_'+i+'"><a href="activity/'+res.father_id+'/file/'+res.files[i]+'"><img src="image/icon/files.png" class="default_img" ></a></div>';
		}
	}
	res_html=res_html+'<div class="reply" id="reply_'+res.id+'">';
	//Add Operations
	n=res.operations.length;
	i=0;
	for(i=0;i<n;i++){
		res_html=res_html+'<a href="#" class="link_operation">'+res.operations[i]+'</a>';
	}
	res_html=res_html+'</div></div></div></td></tr></table></div>';
	$('#'+fatherdiv).prepend(res_html);
	//Add Events
	$('#'+res.id).mouseenter(function(){
		$('#reply_'+res.id).show();
	});
	$('#'+res.id).mouseleave(function(){
		setTimeout(function(){
			$('#reply_'+res.id).hide();
		},100);
	});
    n=res.files.length;
	i=0;
	
	for(i=0;i<n;i++){
		var elem=res.files[i].split('.');
		if(elem[elem.length-1].toLowerCase()=='jpg'){
			$('#file_'+res.id+'_'+i).click(zoominimg);
		}
	}
}

function generate_mail(mail,fatherdiv){

}

function zoominimg(event,target){
	//照片的弹出层效果
	var tempdiv="<div id='tempdiv_outer'><div id='tempdiv'><img src='"+target+"' id='tempimg'><div class='share_link' id='share_link'>SHARE LINK</div></div></div>";
	$(document.body).append(tempdiv);
	$('#tempdiv_outer').addClass('tempdiv_outer');
	$('#tempdiv_outer').css("top",$(document).scrollTop());
	$('#tempdiv_outer').css("width",'100%');
	$('#tempdiv_outer').css("height",$(document).height());
	$('#tempdiv').addClass("zoomin_div");
	$('#tempimg').addClass("zoomin_img");
	$('#tempdiv').css("left",$('#tempdiv_outer').width()/2-350);
	$('#tempdiv').css("top",Math.max($('#tempdiv_outer').height()/2-$('#tempdiv').height()/2,0));
	$('#tempdiv_outer').click(function(event){
		if(event.target.id=='tempdiv_outer'){
			$('#tempdiv_outer').remove();
		}
	}); 
	$('#tempdiv').hover(function(){
		$('#share_link').css("display","inline");
	},
	function(){
		$('#share_link').css("display","none");
	});
}
function popdialog(event,inner_div){
	//对话框的弹出层效果
	var target=event.target;
	var tempdiv="<div id='tempdiv_outer'><table id='temptable' class='poptable'><tr><td width='700px'><div id='tempdiv'></div></td><td><div class='share_link' id='share_link'>SHARE LINK</div></td></tr></table></div>";
	$(document.body).append(tempdiv);
	$('#tempdiv_outer').addClass('tempdiv_outer');
	$('#tempdiv_outer').css("top",$(document).scrollTop());
	$('#tempdiv_outer').css("width",'100%');
	$('#tempdiv_outer').css("height",'100%');
	$('#temptable').css("left",$('#tempdiv_outer').width()/2-350);
	$('#temptable').css("top",Math.max($('#tempdiv_outer').height()/2-$('#tempdiv').height()/2-200,0));
	$('#tempdiv_outer').click(function(event){
		if(event.target.id=='tempdiv_outer'){
			$('#tempdiv_outer').remove();
		}
	});
	$('#tempdiv').hover(function(){
		$('#share_link').show();
	},
	function(){
		$('#share_link').hide();
	});
	$('#tempdiv').append(inner_div);
}
function popmail(event,mail){
	//弹出邮件对话框
}
function create_act(act,father_div){
	//创建一个行动控件并为之添加事件。
	var act_block='<div class="outer_div" id="'+act.id+'">\
<div class="face_div">\
<img src="activity/'+act.id+'/image/'+act.face+'" class="face_img">\
</div>\
<div class="description_div" id="'+act.id+'_description">\
<div style="padding:10px;"><p>'+act.description+'</p></div></div>\
<div class="bottom_div"><div style="padding-left:10px;">'+act.name+'</div></div>\
<div class="operation_div" id="'+act.id+'_operation">\
<table class="operation_table"><tr><td style="border-right:silver 1px solid; text-align:left;width:60%;">\
<div class="operationlist">创建者：<a href="#">刘金国</a></div>\
<div class="operationlist">地点：翠竹园小区</div>\
<div class="operationlist"><a href="a0000001.html">查看详细</a></div>\
</td><td>\
<div class="operationlist"><a href="#">点赞（<strong><label class="decade">2</label>9</strong>）</a></div>\
<div class="operationlist"><a href="#">分享（<strong><label class="decade">8</label>3</strong>）</a></div>\
</td></tr></table></div>'

	$('#'+father_div).append(act_block);
	$('#'+act.id).hover(function(){
		$('#'+act.id+'_operation').show();
	},
	function(){
		setTimeout(function(){
			$('#'+act.id+'_operation').hide();
		},200);
	});	
}


function cact(father_div){
    var content='<div class="outer_div" id="act_1">\
    <div class="operation_div" id="operation_div">\
    <span class="label"><a href="a0000001.html" class="goldlink">查看详细</a></span>\
    <span class="label"><a href="#" class="goldlink">顶(18)</a></span>\
    <span class="label" style="margin-left:120px;"><a href="#" class="goldlink">分享(26)</a></span>\
    </div><div class="face_div">\
    <img src="activity/a0000002/image/face.jpg" class="face_img">\
	</div><div class="description_div">\
    <p class="smallp">这是有翠竹园小区明志书屋项目组发起的一个活动。已经有7人参与。我是遗斯蒂芬斯蒂芬斯蒂芬斯蒂芬森防守对方传史哦就菲拉斯减肥啦睡觉了劳动法建立时间了。</p>\
        <div class="infodiv">  \
        <div class="pull-right"><a href="#" class="label goldlink">by: 双方都刘金国</a></div>\
        </div></div><div class="bottom_div">\
    <div style="padding-left:7px;">翠竹园童书屋算是建设</div></div></div>';
	$('#'+father_div).append(content);
	
}

function crec(father_div){
	var content='<div class="outer_div" id="act_1">\
            <div class="operation_div" id="operation_div" style="display:block;">\
            <span class="label"><a href="#" class="goldlink" id="track">跟踪动态</a></span>\
            <div style=" width:140px;text-align:right; display:inline-block">\
            <span class="label"><a href="#" class="goldlink">分享(18)</a></span>\
            <span class="label"><a href="#" rel="tooltip" class="goldlink" title="需求：引导员3名，摄影师1名，已有引导员2名，摄影师一名。" id="enroll">加入(3)</a></span></div></div>\
			<div class="face_div" id="facediv">\
            <img src="activity/a0000001/image/poster.jpg" class="face_img"></div>\
            <div class="description_div">\
            <p class="smallp">这是有翠竹园小区明志书屋项目组发起的一个活动。已经有7人参与。</p><div class="infodiv">\
                <div class="pull-right"><a href="#" class="label goldlink">by: 刘金国</a></div></div>\
            </div><div class="bottom_div">\
            <div style="padding-left:7px;"> 翠竹园童书屋建设 </div></div>\
          <div id="posterblock" class="modal hide fade">\
          	<div style="overflow:visible;"><img src="activity/a0000001/image/poster.jpg"></div></div> </div>'
	$('#'+father_div).append(content);
}
function create_recruit(act,father_div){
	//创建一个招募信息控件并为之添加事件。
	var act_block='<div class="outer_div"  style="" id="'+act.id+'">\
	<div class="face_div">\
<img src="activity/'+act.id+'/image/'+act.face+'" class="face_img"></div>\
<div class="operation_div" id="'+act.id+'_operation">\
<table class="operation_table"><tr><td style="border-right:silver 1px solid;text-align:left;padding-left:5px; width:60%;">\
<div class="operationlist">创建者：'+act.creater+'<br>日期：'+act.tasks['wherewhen'].time+'<br>地点：'+act.tasks['wherewhen'].place+'<br><a href="activity/'+act.id+'/image/'+act.face+'">海报</div>\
</td><td><div class="operationlist">引导员:<a href="#">1/3</a></div>\
<div class="operationlist" style="padding-bottom:10px;">摄影师:<a href="#">0/1</a></div>\
<div class="operationlist"><button class="recruit_img" id="enroll_'+act.id+'" title="加入"></div>\
</td></tr></table>\
</div>\
<div class="description_div" id="'+act.id+'_description"><p>'+act.description+'</p></div>\
<div class="bottom_div">'+act.name+'</div></div>'
	$('#'+father_div).append(act_block);
	$('#'+act.id).hover(function(){
		$('#'+act.id+'_description').hide();
		$('#'+act.id+'_operation').show();
	},
	function(){
		setTimeout(function(){
			$('#'+act.id+'_operation').hide();
			$('#'+act.id+'_description').show();
		},200);
	});	
	$('#enroll_'+act.id).click(enroll);
}

function enroll(){
	//报名
	alert('报名！');
}

