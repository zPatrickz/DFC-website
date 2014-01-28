// JavaScript Document
var index=0;
var npic=3;
var descriptions=["<a href='intro_dfc'>它专注于引导未成年人创造性的解决问题<br><p style='margin-top:0.7em;'>它是解决问题的艺术</p></a>",
"<a href='4steps.html'>它全程不收取任何费用<br><p style='margin-top:0.7em;'>用感受，现象，行动和分享4个简单的步骤把问题解决。</p></a>",
"<a href='activities.html'>很多很多有爱的行动的故事已经发生<br><p style='margin-top:0.7em;'>有时候，爱就是最好的创意。</p></a>",
"<a href='#'>请把你想解决的困难，想延续的感动告诉我们<br><p style='margin-top:0.7em;'>让我们一起来行动感染更多的人。</p></a>"]
$(document).ready(function() {
	shuffle();
	setInterval(shuffle,5000);
	$('#login_btn').click(show_login);
	$('#problem_btn').click(create_problem);
})

function shuffle(){
	$('#wall').css("background-image","url(image/wall/"+index+".JPG)");
	$('#description_text').html(descriptions[index]);
	index=(index+1)%npic;
}

function show_login(){
	//Show the Login Frame
	alert('Login!');
}

function create_problem(){
	//Show the Login Frame
	alert('Create Problem!');
	window.location.href='mydfc.html';
}