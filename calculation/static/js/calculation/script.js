


	/*стрелка*/
	var meter_needle =  document.querySelector('#csi_meter_needle');
	var slider = document.querySelector('.csi #slider');
	var percent = slider.value;

	meter_needle.style.transform = 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';
	// 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';

	var meter_needle =  document.querySelector('#loy_meter_needle');
	var slider = document.querySelector('.loy #slider');
	var percent = slider.value;

	meter_needle.style.transform = 'rotate(' + (265 + (percent - 55)* 4.5) + 'deg)';