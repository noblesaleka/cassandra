// Parse the URL parameter
	function getParameterByName(name, url) {
	    if (!url) url = window.location.href;
	    name = name.replace(/[\[\]]/g, "\\$&");
	    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
	        results = regex.exec(url);
	    if (!results) return null;
	    if (!results[2]) return '';
	    return decodeURIComponent(results[2].replace(/\+/g, " "));
	}

// Give the parameter a variable name
var dynamicContent = getParameterByName('dc');

$(document).ready(function() {
	// Check if the URL parameter is contact-contact-form
	if (dynamicContent == 'box1') {
		$('#box1').addClass('d-block');
        $('#box1').removeClass('d-none');
        $('#box2').addClass('d-none');
		$('#box2').removeClass('d-block');
	}
	// Check if the URL parameter is contact-register-form
	else if (dynamicContent == 'box2') {
		$('#box1').addClass('d-none');
        $('#box1').removeClass('d-block');
        $('#box2').addClass('d-block');
		$('#box2').removeClass('d-none');
	}
	// Check if the URL parmeter is empty or not defined, display default content
	else {
		$('#box1').addClass('d-block');
	}
});