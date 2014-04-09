function load_gallery_photo_list(name,gallery_id,current_photo,category,editor_callback,simpleeditor_callback){
	$('#'+name+' option').remove();
	$.getJSON("/api/gallery/"+gallery_id+"/list", { "resultType": "json","category":category }, function(data, textStatus)  
	{  
		$('#'+name).append('<option value=""></option>');
	    for(var i in data){
	    	$('#'+name).append('<option data-img-src="'+data[i].small+'" data-medium-img-src="'+data[i].medium+'"  data-large-img-src="'+data[i].large+'" data-img-label="'+data[i].title+'" value="'+data[i].id+'" '+(current_photo==data[i].id?'selected="selected"':'')+'>'+data[i].title+'</option>');   
	    }
		$('#'+name).imagepicker({});
		$('.image_picker_image').attr('data-dismiss','modal');
		$('.image_picker_image').mouseover(function() {
		    $(this).css('cursor', 'pointer');
		});
		$('#'+name).on('change',function() {
			selected_thumbnail = $('#'+name).parent().find('.thumbnail.selected').find('img');
			
			if(category == 'activity_cover'){
				img_src = $('#'+name+' option[data-img-src="'+selected_thumbnail.attr('src')+'"]').attr('data-medium-img-src');
			}else if(category == 'photo'){
				img_src = $('#'+name+' option[data-img-src="'+selected_thumbnail.attr('src')+'"]').attr('data-large-img-src');
			}
			img_label = $('#'+name+' option[data-img-src="'+selected_thumbnail.attr('src')+'"]').attr('data-img-label');
		    if(simpleeditor_callback){
				simpleeditor_callback($('#'+name).val());
			}else if(editor_callback){
				editor_callback(img_src,img_label);
		    }else{
				$('#img-'+name).attr('src',img_src);
			}
		});
	}); 
}



function load_gallery_list(name,current_photo,category,editor_callback,simpleeditor_callback){
	$('#ip-gallery-'+name+' option').remove();
	$.getJSON("/api/gallery/list", { "resultType": "json" ,"category":category}, function(data, textStatus)  
	{
	    for(var i in data){
	    	$('#ip-gallery-'+name).append('<option value="'+data[i].id+'">'+data[i].title+'</option>');   
	    }
		if(data.length > 0){
			load_gallery_photo_list(name,data[0].id,current_photo,category,editor_callback,simpleeditor_callback);
		}
	}); 
}

function image_picker_widget_init(name,current_photo_id,category){
    $("#select-btn-"+name).click(function() {
    	load_gallery_list(name,current_photo_id,category);
    });
    $("#ip-gallery-"+name).change(function() {
        load_gallery_photo_list(name,this.value,current_photo_id,category);
    });
}

function image_picker_plugin_init(name,current_photo_id,category,editor_callback){
    load_gallery_list(name,current_photo_id,category,editor_callback);
    $("#ip-gallery-"+name).change(function() {
        load_gallery_photo_list(name,this.value,current_photo_id,category,editor_callback);
    });
}

function image_picker_simpleeditor_plugin_init(name,current_photo_id,category,simpleeditor_callback){
    load_gallery_list(name,current_photo_id,category,null,simpleeditor_callback);
    $("#ip-gallery-"+name).change(function() {
        load_gallery_photo_list(name,this.value,current_photo_id,category,null,simpleeditor_callback);
    });
}



function popup_page(page_url){ 
	window.open(page_url,"PopupWindow","width=500,height=400,toolbar=no,menubar=no,scrollbars=no,resizable=no,location=no,status=no"); 
} 

