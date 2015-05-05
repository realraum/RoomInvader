

// just a quick & dirty code, clean up here!


function enqueueYoutube() {

	var url = $('#youtube').val();
	
	$.ajax({
	  url: "/enqueue/youtube",
	  method: "POST",
	  data: {
	    url: url
	  },
	  success: function( data ) {
	   	alert(data);
	  }
	});
}
 
