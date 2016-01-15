var deletion = function() {
	$( this ).parents(".js-worktype").remove();
};

$(".deletion").click(deletion);

$(".adding").click(function(){
	var curVal = parseInt($(".js-wt_counter").val());
	$(".js-wt_counter").val(curVal + 1);

	to_clone = $(".js-worktype").first().clone();
	$(".js-worktype").last().after(to_clone);

	//apply delete function for new button
	$(".deletion").click(deletion);		
});