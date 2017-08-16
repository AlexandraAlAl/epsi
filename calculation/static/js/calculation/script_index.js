
	/*стрелка*/
var count = document.getElementsByClassName('post_index').length;

	
for (var i = 0; i < count; i++) {
	var meter_needle =  document.querySelectorAll('#csi_index_meter_needle')[i];
	var slider = document.querySelectorAll('.csi_index #slider')[i];
	var percent = slider.value;

	meter_needle.style.transform = 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';


	var meter_needle =  document.querySelectorAll('#loy_index_meter_needle')[i];
	var slider = document.querySelectorAll('.loy_index #slider')[i];
	var percent = slider.value;

	meter_needle.style.transform = 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';
}