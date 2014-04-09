var editorcolor='#444';
(function($){
	$.fn.initialize_editor = function(init_val){
		
		var current_editor = $(this);
		var myid=$(this).attr('id');
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
					<a href="javascript:void(0)" class="text-muted" id="'+myid+'-add-doc"><span class="glyphicon glyphicon-paperclip"></span>文档</a>&nbsp;&nbsp;&nbsp;\
					<a href="javascript:void(0)" class="text-muted" id="'+myid+'-add-photo"><span class="glyphicon glyphicon-picture"></span>图片</a>&nbsp;&nbsp;&nbsp;\
					<a href="javascript:void(0)" class="text-muted" id="'+myid+'-add-emotion"><span class="glyphicon glyphicon-user"></span>表情</a>&nbsp;&nbsp;&nbsp;\
					<a href="javascript:void(0)" class="text-muted" id="'+myid+'-preview"><span class="glyphicon glyphicon-eye-open"></span>预览</a>&nbsp;&nbsp;&nbsp;\
				</div>\
			</div>\
			<div class="modal fade" id="'+myid+'-modal">\
				<div class="modal-dialog">\
					<div class="modal-content">\
						<div class="modal-header">\
							<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\
							<h4 class="modal-title"></h4>\
						</div>\
						<div class="modal-body">\
							\
						</div>\
						<div class="modal-footer">\
					        <button type="button" class="btn btn-info" data-dismiss="modal" id="link-insert">插入</button>\
					    </div>\
					</div>\
				</div>\
			</div>\
			<p class="help-block" style="margin-top: 10px;" id="'+myid+'-alert-box"></p>';
		current_editor.after(htmltext);
		
		current_editor.closest('form').on('submit',function(e){
			$(current_editor).val($('#'+myid+'-editor-field').html());
		});
		
		current_editor.parent().on('click', '#'+myid+'-add-doc', function() {
			 alert('add doc'); 
		});
		function add_image_callback(value){
			insertIntoSimpleEditor(myid+'-editor-field','{photo '+value+'}');
		}
		current_editor.parent().on('click', '#'+myid+'-add-photo', function() {
			 $('#'+myid+'-modal').find('.modal-body').html('<strong>Gallery:   </strong>\
			 <select id="ip-gallery-se-ip-'+myid+'"></select>\
      	   	 <hr/>\
      		 <select class="image-picker" id="se-ip-'+myid+'"></select>');
			 $('#'+myid+'-modal').find('.modal-footer').html('');
			 $('#'+myid+'-modal').modal();
			 image_picker_simpleeditor_plugin_init('se-ip-'+myid,null,'photo',add_image_callback);
		});
		current_editor.parent().on('click', '#'+myid+'-add-emotion', function() {
			 alert('add emotion'); 
		});
		current_editor.parent().on('click', '#'+myid+'-preview', function() {
			 alert('preview'); 
		});
		current_editor.parent().on('click', '.color-picker', function() {
			 alert('my color is'+$(this).attr('value')); 
		});
	}

})(jQuery);

function getRange(el){
	var selection = null;
	var range = null;
	selection=rangy.getSelection();
	if(selection.getRangeAt && selection.rangeCount){
		range = selection.getRangeAt(0);
	}
	if(range && range.intersectsNode($(el)[0])){
		return range;
	}
	return null;
}



function insertIntoSimpleEditor(editor_id,text){
	range = getRange($('#'+editor_id));
	if(!range){
		placeCaretAtEnd($('#'+editor_id));
		range = getRange($('#'+editor_id));
	}
	range.insertNode(document.createTextNode(text));
}

function placeCaretAtEnd(el) {
	el = $(el)[0];
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

