var editorcolor='#444';
	$('#editor-field').keydown(function(event){
		alert('@');
		if(event.keyCode==13 && event.ctrlKey){
			alert('Send!');
		}
	});
$(document).ready(function(){
		
	$('#editor-field').keydown(function(event){
		alert('@');
		if(event.keyCode==13 && event.ctrlKey){
			alert('Send!');
		}
	});
	
	
	$('.color-picker').click(function(){
		editorcolor=$(this).attr('value');
		$('#editor-field').css('color',editorcolor);
		//var content=$('<div></div>');
		//content.append($('#editor-field').html());
		//content.css('color',$(this).attr('value'));
		//$('#editor-field').html(content);
	});
	
	$('#add-link').click(function(){
		selection=null;
		getselection(document.getElementById('editor-field'));
		if(selection){
			$('#link-block').modal();
		}
	});
	$('#link-insert').click(function(){
		insertlink($('#link-link').val());
	});
	
	$('#editor-submit').click(sbmt);
		
});

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

//use "@xxx + space" to reply.
$(document).on('keyup', "#editor-field", function(e) {
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

function sbmt() {
  	var param = '"sdf"';
  	// jQuery
  	param = "<div style='color:"+editorcolor+";'>"+$('#editor-field').html()+"</div>"; //.replace("'","\\'").replace('"','\\"')

  	// Now that you have these values you should add them to your form as an input
  	// input fields are how you send data through forms to wherever you are posting them
  	// build the input field
  	var paraminput = $("<input type='text' name='param' class='hide'/>");
  	paraminput.val(param);
  	
	
  	// append it to the form
  	$('#editor-form').append(paraminput);
  	

  	// finally submit the form.
  	$('#editor-form').submit();
}

//select an area using rangy library;
function getselection(el){
	selection=rangy.getSelection().getRangeAt(0);
	if(!selection.intersectsNode(el) || selection.toString()==""){
		$('#alert-box').html('<span class="text-warning">Warning:</span> You need to specify a range of text before adding a link!');
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
(function($){

	$.fn.syncSimpleEditor = function() {
		var editor_input = this;
		$(this).closest('form').submit(function(e){
			//e.preventDefault();
			$(editor_input).val($('#editor-field-'+$(editor_input).attr('name')).html());
			//e.unbind("submit");
			//$(editor_input).closest('form').submit();
		});
	}

})(jQuery);
