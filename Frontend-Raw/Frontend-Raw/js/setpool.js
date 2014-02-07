// JavaScript Document
$(document).ready(function(e) {
	//browser=checkbrowser();
	var res1=new Response(1,'cacate',currentTime(),'DFC南京~LoVe',['0.JPG','活动策划.pdf'],['important','proposal'],'a0000001');
	append_reply(res1,'pool_div');
	var res2=new Response(2,'王强华',currentTime(),'刘金国啊，你该好好科研啦！',['1.JPG','2.JPG'],['important','record'],'a0000001');
	append_reply(res2,'pool_div');
	var res3=new Response(3,'谢闯',currentTime(),'其实，我想做个好人。',[],[],'a0000001');
	append_reply(res3,'pool_div');
	var res4=new Response(4,'徐沐阳',currentTime(),'今天天气不错~',[],[],'a0000001','green');
	append_reply(res4,'pool_div');
});
