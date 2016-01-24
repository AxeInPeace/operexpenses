var deletion = function() {
	var cur_tab = $(this).parents(".tab-pane");

	//decrease amount of work types
	var cur_val = parseInt(cur_tab.find($(".js-wt_counter")).val());
	cur_tab.find($(".js-wt_counter")).val(cur_val - 1);

	$( this ).parents(".js-worktype").remove();
	global_recalculate(cur_tab);
	local_recalculate(cur_tab);
};

var custom_deletion = function() {
	var cur_tab = $(this).parents(".tab-pane");

	//decrease amount of work types
	var cur_val = parseInt(cur_tab.find($(".js-custom-wt-counter")).val());
	cur_tab.find($(".js-custom-wt-counter")).val(cur_val - 1);

	$( this ).parents(".js-custom-worktype").remove();
	global_recalculate(cur_tab);
	local_recalculate(cur_tab);
};

$(".deletion").click(deletion);

var recalculate = function() {
	var cur_worktype = $(this).parents(".js-worktype, .js-custom-worktype");

	var qnt = parseInt(cur_worktype.find(".qnt").val());
	if (isNaN(qnt)) qnt=0;
	var value = parseInt(cur_worktype.find(".time_value").val());
	if (isNaN(value)) value = 0;
	var prev_value = cur_worktype.find(".time_sum").val();

	cur_worktype.find(".time_sum").val( qnt * value );
	var cur_value = cur_worktype.find(".time_sum").val();
	if (isNaN(prev_value)) prev_value = 0;

	cur_tab = $(this).parents(".tab-pane");
	
	local_recalculate(cur_tab);
	global_recalculate(cur_tab);
};

$(".js-recalculate").on('change', recalculate);
$(document).ready($(".js-recalculate").trigger("change"));

function local_recalculate(cur_tab){
	cur_tab.find(".work-overtype").each(function(){
		var local_sum = 0;
		$(this).find(".js-worktype, .js-custom-worktype").each(function(){
			var cur_time = parseInt($(this).find(".time_sum").val());
			if (isNaN(cur_time)) cur_time = 0;
			local_sum += cur_time;
		});
		$(this).find(".oper_time").val(local_sum);
	});
}

function global_recalculate(cur_tab){
	global_sum = 0;
	cur_tab.find(".js-worktype, .js-custom-worktype").each(function(){
		var cur_time = parseInt($(this).find(".time_sum").val());
		if (isNaN(cur_time)) cur_time = 0;
		global_sum += cur_time;
	});
	
	cur_tab.find($(".time_tab")).val(global_sum);
};

$(".js-global_qnt").on('change', function(){
	cur_val = $(this).val();
	cur_tab = $(this).parents(".tab-pane");
	cur_tab.find(".qnt").each(function(){
		$(this).val(cur_val);
	});
	$(".js-recalculate").trigger("change")
});


$(".adding").click(function(){
	cur_tab = $(this).parents(".tab-pane");
	cur_block = $(this).parents(".form-container")

	//increase amount of work types
	var cur_val = parseInt(cur_tab.find($(".js-wt_counter")).val());
	cur_tab.find($(".js-wt_counter")).val(cur_val + 1);

	//clone to add new work type field
	var to_clone = cur_block.find(".adding_reserve").clone();
	to_clone.removeClass("hide adding_reserve").addClass("js-worktype");
	to_clone.find("select").addClass("wt-select");
	to_clone.find(".qnt_ar").addClass("qnt js-recalculate").removeClass("qnt_ar");
	to_clone.find(".time_ar").addClass("time_value js-recalculate").removeClass("time_ar");
	to_clone.find(".sum_time_ar").addClass("time_sum").removeClass("sum_time_ar");

	cur_block.find(".divider").before(to_clone);

	var added_block = cur_block.find(".js-worktype").last();
	//apply delete function for new button
	added_block.find(".deletion").on('click', deletion);

	//apply recalculate function
	added_block.find(".js-recalculate").on('change', recalculate);

	//apply update time function
	added_block.find(".wt-select").on('change', update_time);

	//apply update description function
	added_block.find(".wt-select").on('change', update_description);
	
	$(added_block.find(".wt-select")).trigger('change');
	$(added_block.find(".js-recalculate")).trigger('change');
});

$(".custom-adding").click(function(){
	cur_tab = $(this).parents(".tab-pane");
	cur_block = $(this).parents(".form-container")

	//increase amount of work types
	var cur_val = parseInt(cur_tab.find($(".js-custom-wt-counter")).val());
	cur_tab.find($(".js-custom-wt-counter")).val(cur_val + 1);

	//clone to add new work type field
	var to_clone = cur_block.find(".adding-custom-wt").clone();
	to_clone.find("input.custom").addClass("wt-input");
	to_clone.removeClass("hide adding-custom-wt").addClass("js-custom-worktype");
	to_clone.find(".qnt_ar").addClass("qnt js-recalculate").removeClass("qnt_ar");
	to_clone.find(".time_ar").addClass("time_value custom js-recalculate").removeClass("time_ar");
	to_clone.find(".sum_time_ar").addClass("time_sum").removeClass("sum_time_ar");

	cur_block.find(".divider").before(to_clone);

	var added_block = cur_block.find(".js-custom-worktype").last();
	//apply delete function for new button
	added_block.find(".custom-deletion").on('click', custom_deletion);

	//apply recalculate function
	added_block.find(".js-recalculate").on('change', recalculate);
	
	$(added_block.find(".js-recalculate")).trigger('change');
});	

var update_time = function(){ 
	cur_tab = $(this).parents(".tab-pane");
	var amount_of_wt = parseInt(cur_tab.find(".js-wt_counter").val());
	
	var work_types = [];
	cur_tab.find(".wt-select").find(":selected").each(function(){
		work_types.push($(this).val());
	});

	var tool_id = cur_tab.find(".tool-type").find(":selected").val();
	$.get(
		"{% url 'get_time' %}",
		{
			tool_id: tool_id,
			work_types: work_types,
		},
		function(data){
			time_owners = [];
			cur_tab.find(".time_value").not(".custom").each(function(){
				time_owners.push($(this));
			});

			for (var i = 0; i < amount_of_wt; i++) {
				time_owners[i].val(data.data[i]);
			};
			$(".js-recalculate").trigger("change");
		}
	);
};

var update_description = function(){
	var caller = $( this )
	selected_item = parseInt(caller.val());

	$.get(
		"{% url 'get_description' %}",
		{
			item_id: selected_item,
		},
		function(data){
			element = caller.parents(".js-worktype").find(".wt-description");
			$(element).attr('data-original-title', data.data).tooltip('fixTitle');
		}
	);
};

$(".tool-type").change(update_time);
$(".wt-select").change(update_time);
$(".wt-select").change(update_description);

$(".submit").click(function(){
	alert("submit");
	amount_of_wt = 0;
	$(".newpathcard_form").find(".js-worktype").each(function(){
		cur_num = String(amount_of_wt);
		$(this).find(".wt-select").attr("name", "wt_" + cur_num);
		$(this).find(".qnt").attr("name", "qnt_" + cur_num);
		$(this).find(".time_value").attr("name", "time_"+cur_num);
		amount_of_wt++;
	});
	$(".newpathcard_form").find(".wt_amount").val(amount_of_wt);
	alert(amount_of_wt);
	amount_of_custom_wt = 0;
	$(".newpathcard_form").find(".js-custom-worktype").each(function(){
		alert("in");
		cur_num = String(amount_of_wt);
		$(this).find(".wt-input").attr("name", "wt_" + cur_num);
		$(this).find(".qnt").attr("name", "qnt_" + cur_num);
		$(this).find(".time_value").attr("name", "time_" + cur_num);
		$(this).find(".custom-wt-overtype").attr("name", "overtype_" + cur_num)
		amount_of_wt++;
		amount_of_custom_wt++;
	});
	$(".newpathcard_form").find(".custom_wt_amount").val(amount_of_custom_wt);

});

$(function () {
	$('[data-toggle="tooltip"]').tooltip()
});

$(document).ready(function() {
	$(window).keydown(function(event){
		if(event.keyCode == 13) {
			event.preventDefault();
			return false;
		}
	});
});