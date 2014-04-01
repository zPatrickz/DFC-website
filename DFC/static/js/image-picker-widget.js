function load_gallery_list(name,current_photo){
	$('#ip-gallery-cover option').remove();
	$.getJSON("/api/gallery/list", { "resultType": "json" }, function(data, textStatus)  
	{
	    for(var i in data){
	    	$('#ip-gallery-'+name).append('<option value="'+data[i].id+'">'+data[i].title+'</option>');   
	    }
		if(data.length > 0){
			load_gallery_photo_list(name,data[0].id,current_photo);
		}
	}); 
}

function load_gallery_photo_list(name,gallery_id,current_photo){
	$('#'+name+' option').remove();
	$.getJSON("/api/gallery/"+gallery_id+"/list", { "resultType": "json" }, function(data, textStatus)  
	{  
		$('#'+name).append('<option value=""></option>');
	    for(var i in data){
	    	$('#'+name).append('<option data-img-src="'+data[i].thumbnail+'" data-img-label="'+data[i].title+'" value="'+data[i].id+'" '+(current_photo==data[i].id?'selected="selected"':'')+'>'+data[i].title+'</option>');   
	    }
		$('#'+name).imagepicker({});
		$('.image_picker_image').attr('data-dismiss','modal');
		$('.image_picker_image').mouseover(function() {
		    $(this).css('cursor', 'pointer');
		});
		$('.image_picker_image').click(function() {
		    $('#img-'+name).attr('src',$(this).attr('src'));
		});

	}); 
}

function popup_page(page_url){ 
	window.open(page_url,"PopupWindow","width=500,height=400,toolbar=no,menubar=no,scrollbars=no,resizable=no,location=no,status=no"); 
} 