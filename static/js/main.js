$(document).ready(function (){

	// Ellipsis text by line
	$.each($(".truncate"), function (i, n) {
	    $(n).ellipsis({
	      lines: parseInt($(n).data('lines')),
	      ellipClass: 'ellip',
	      responsive: true
	    });
	});

});