var editorcolor='#444';
$(document).ready(function(){
	initialize_editor();
		
	$('.editor-field').keydown(function(event){
		if(event.keyCode==13 && event.ctrlKey){
			var myid=$(this).closest('form').attr('id').split('-')[0];
			sbmt(myid);
		}
	});
	
	
	$('.color-picker').click(function(){
		myid=$(this).closest('form').attr('id').split('-')[0];
		editorcolor=$(this).attr('value');
		$('#'+myid+'-editor-field').css('color',editorcolor);
		//var content=$('<div></div>');
		//content.append($('#editor-field').html());
		//content.css('color',$(this).attr('value'));
		//$('#editor-field').html(content);
	});
	
	$('.add-link').click(function(){
		selection=null;
		var myid=$(this).attr('id').split('-')[0];
		var el=document.getElementById(myid+'-editor-field');
		getselection(el);
		if(selection){
			var node=$('<div class="modal" id="link-block"></div>');
			var htmltext='<div class="modal-dialog">\
				<div class="modal-content">\
					<div class="modal-header">\
						<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
						<h4 class="modal-title">添加链接</h4>\
					</div>\
					<div class="modal-body">\
						<form class="form-horizontal">\
							<div class="form-group">\
								<label class="col-md-2 control-label" for="link-link">Link to </label>\
								<div class="col-md-10">\
									<input class="form-control" id="link-link" />\
								</div>\
							</div>\
						</form>\
					</div>\
					<div class="modal-footer">\
				        <button type="button" class="btn btn-info" data-dismiss="modal" id="link-insert">插入</button>\
				    </div>\
				</div>\
			</div>';
			node.html(htmltext);
			$(document).append(node);
			$('#link-block').modal();
		}
	});
	$('#link-insert').click(function(){
		insertlink($('#link-link').val());
		$('#link-link').val('');
	});
	
	$('.editor-submit').click(sbmt);
	//use "@xxx + space" to reply.
	$('.editor-field').keyup(function(e) {
		var text = $(this).html();
		var firstAt = text.indexOf('@');
		if(e.keyCode === 32 && firstAt > -1) {
		    var textToReplace = text.substring(firstAt, text.len);
		    //alert(textToReplace);
		    var newText = "<a href='"+textToReplace.substring(1,textToReplace.len)+"' class='attext'>[" + textToReplace.substring(1, textToReplace.len) + "]</a>";
		    //alert(newText);
		    var complete = text.replace(textToReplace, newText);
		    //alert(complete);
		    $(this).html(complete);        
		    placeCaretAtEnd($(this).get(0));
		}
	});

		
});

function initialize_editor(){
	$('.editor-simple').each(function(){
		var myid=$(this).closest('form').attr('id').split('-')[0];
		var htmltext='<div>\
				<div contenteditable="" class="editor-field" id="'+myid+'-editor-field"></div>\
			</div>\
			<div class="editor-bottom">\
				<a href="javascript:void(0)" value="#256" class="color-picker"><span style="color: #256" class="glyphicon glyphicon-tint"></span></a>&nbsp;&nbsp;&nbsp;\
				<a href="javascript:void(0)" value="#444" class="color-picker"><span style="color: #444" class="glyphicon glyphicon-tint"></span></a>&nbsp;&nbsp;&nbsp;\
				<a href="javascript:void(0)" value="#525" class="color-picker"><span style="color: #525" class="glyphicon glyphicon-tint"></span></a>&nbsp;&nbsp;&nbsp;\
				<a href="javascript:void(0)" value="#226" class="color-picker"><span style="color: #226" class="glyphicon glyphicon-tint"></span></a>&nbsp;&nbsp;&nbsp;\
				<a href="javascript:void(0)" value="#373" class="color-picker"><span style="color: #373" class="glyphicon glyphicon-tint"></span></a>&nbsp;&nbsp;&nbsp;\
				<div class="pull-right">\
					<a href="javascript:void(0)" class="text-muted"><span class="glyphicon glyphicon-paperclip"></span>附件</a>&nbsp;&nbsp;&nbsp;\
					<a href="javascript:void(0)" class="text-muted add-link" id="'+myid+'-add-link"><span class="glyphicon glyphicon-link"></span>链接</a>&nbsp;&nbsp;&nbsp;\
					<a href="javascript:void(0)" class="text-muted"><span class="glyphicon glyphicon-picture"></span>图片</a>&nbsp;&nbsp;&nbsp;\
					<a href="javascript:void(0)" class="text-muted"><span class="glyphicon glyphicon-user"></span>表情</a>&nbsp;&nbsp;&nbsp;\
					<a href="javascript:void(0)" class="text-muted"><span class="glyphicon glyphicon-eye-open"></span>预览</a>&nbsp;&nbsp;&nbsp;\
					<button type="button" class="btn btn-default editor-submit" id="'+myid+'-editor-submit">Submit</button>\
				</div>\
			</div>\
			<p class="help-block" style="margin-top: 10px;" id="'+myid+'-alert-box"></p>';
		$(this).append(htmltext);
	});
}

//used to insert a link after a selection 
function insertHtmlAfterSelection(html,range,sel) {
    var expandedSelRange, node;
    if (window.getSelection) {
        if (sel.getRangeAt && sel.rangeCount) {
            expandedSelRange = range.cloneRange();
            range.collapse(false);

            // Range.createContextualFragment() would be useful here but is
            // non-standard and not supported in all browsers (IE9, for one)
            var el = document.createElement("div");
            el.innerHTML = html;
            var frag = document.createDocumentFragment(), node, lastNode;
            while ( (node = el.firstChild) ) {
                lastNode = frag.appendChild(node);
            }
            range.insertNode(frag);

            // Preserve the selection
            if (lastNode) {
                expandedSelRange.setEndAfter(lastNode);
                sel.removeAllRanges();
                sel.addRange(expandedSelRange);
            }
        }
    } else if (document.selection && document.selection.createRange) {
        range = document.selection.createRange();
        expandedSelRange = range.duplicate();
        range.collapse(false);
        range.pasteHTML(html);
        expandedSelRange.setEndPoint("EndToEnd", range);
        expandedSelRange.select();
    }
}


function placeCaretAtEnd(el) {
	el.focus();
	if (typeof window.getSelection != "undefined"
	        && typeof document.createRange != "undefined") {
	    var range = document.createRange();
	    range.selectNodeContents(el);
	    range.collapse(false);
	    var sel = window.getSelection();
	    sel.removeAllRanges();
	    sel.addRange(range);
	} else if (typeof document.body.createTextRange != "undefined") {
	    var textRange = document.body.createTextRange();
	    textRange.moveToElementText(el);
	    textRange.collapse(false);
	    textRange.select();
	}
}


//highlight a selection, test function
function highlight(){
	var mainDiv = document.getElementById("editor-field");
	var startNode = mainDiv.firstChild.firstChild;
	var endNode = mainDiv.childNodes[2].firstChild;
	
	var range = document.createRange();
	range.setStart(startNode, 6); // 6 is the offset of "world" within "Hello world"
	range.setEnd(endNode, 7); // 7 is the length of "this is"
	var sel = window.getSelection();
	sel.removeAllRanges();
	sel.addRange(range);
}

function sbmt(myid) {
  	var param = '';
  	// jQuery
	var myform=$(this).closest('form');
	var myid=myform.attr('id').split('-')[0];
  	var param = "<div style='color:"+editorcolor+";'>"+$('#'+myid+'-editor-field').html()+"</div>"; //.replace("'","\\'").replace('"','\\"')

  	// Now that you have these values you should add them to your form as an input
  	// input fields are how you send data through forms to wherever you are posting them
  	// build the input field
  	$('#'+myid+'-area').text(param);
  	alert($('#'+myid+'-area').text());
  	
  	// finally submit the form.
  	myform.submit();
}

//select an area using rangy library;
function getselection(el){
	selection=rangy.getSelection().getRangeAt(0);
	alert(selection.toString());
	if(selection.toString()=="" || !selection.intersectsNode(el)){
		$('#'+el.id.split('-')[0]+'-alert-box').html('<span class="text-warning">Warning:</span> You need to specify a range of text before adding a link!');
		selection=null;
	}
}
function insertlink(linklink) {
    if(selection){
	    var mylink=document.createElement('a');
	    mylink.href=linklink;
		selection.surroundContents(mylink);
	}
	else{
		$('#alert-box').html('<span class="text-warning">Error:</span> No selection specified!');
	}
}

