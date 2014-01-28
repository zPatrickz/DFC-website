
$(document).ready(function(e) {
	//browser=checkbrowser();
	$('#left_col div').click(function(){
		$('#left_col div').removeClass("selected");
		$(this).addClass("selected");
		$('#subframe').attr("src",$(this).attr("id")+'.html');
	});
});
