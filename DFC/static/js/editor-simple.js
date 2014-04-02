var selection;
$(document).ready(function(){
	// TODO:
	// Notice that there might be more than one editor on a page,
	// So please do not use specific id such as "#link-link".
	// Add a name parameter to the function and use "#link-link"+name instead.
	$('.editor-field').keydown(function(event){
		if(event.keyCode==13 && event.ctrlKey){
			alert('Send!');
		}
	})
	
	
	$('.color-picker').click(function(){
		$('#editor-field').css('color',$(this).attr('value'));
		//var content=$('<div></div>');
		//content.append($('#editor-field').html());
		//content.css('color',$(this).attr('value'));
		//$('#editor-field').html(content);
	});
	
	$('#add-link').click(function(){
        selection = window.getSelection();
        range = window.getSelection().getRangeAt(0);
		$('#link-block').modal();
	});
	$('#link-insert').click(function(){
		$('#editor-field').focus();
		document.createRange(range);
		insertHtmlAfterSelection('<a href="'+$('#link-link').val()+'">'+$('#link-display').val()+'</a>',range,selection);
	});
	
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
//(function($) {

// $.fn.syncSimpleEditor = function() { 
//	alert("OK");
//    $(this).closest('form').preventDefault();
//	$(this).after('
//	<div contenteditable="" class="editor-field" id="editor-field-'+$(this).attr('name')+'"></div>'
//	);
// }
//})(jQuery);
