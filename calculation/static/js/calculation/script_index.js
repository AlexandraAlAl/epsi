
	/*стрелка*/
	var meter_needle =  document.querySelector('#csi_index_meter_needle');
	var slider = document.querySelector('.csi_index #slider');
	var percent = slider.value;

	meter_needle.style.transform = 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';


	var meter_needle =  document.querySelector('#loy_index_meter_needle');
	var slider = document.querySelector('.loy_index #slider');
	var percent = slider.value;

	meter_needle.style.transform = 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';
