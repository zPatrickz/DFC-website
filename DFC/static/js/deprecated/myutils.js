// JavaScript Document
var username='cacate';
var character='Normal';//Team Volunteer Normal Administrator
function checkbrowser(){
	try{
		window.clipboardData.setData('text', "我爱DFC，啊哈~ > <" );
		return "IE";
	}catch(exception){
		return "Chrome";
	}
}

function currentTime() {
    var date = new Date();
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    var currentdate =month + '月' + strDate
            + "日 " + date.getHours() + ':' + date.getMinutes()
            + ':' + date.getSeconds();
    return currentdate;
}


function currentTime_min() {
    var date = new Date();
    var month = date.getMonth() + 1;
    var strDate = date.getDate();
    var currentdate =month + '月' + strDate
            + "日 " + date.getHours() + ':' + date.getMinutes();
    return currentdate;
}
