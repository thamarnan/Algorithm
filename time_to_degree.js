function time_to_degree(hr, min)
{
	
	positionhr = 360 / 12;// 30 degree per hor
	positionmin = 360 / 60;// 6 degree per min

	position_hr_add = positionhr * (min/60)
	
	hr_actual = hr * positionhr + position_hr_add 
	mn_actual = positionmin * min

	diff = hr_actual - mn_actual
	
	if (diff > 180)
	{	return 360-diff
	}

	return diff
}


    time_to_degree(9,00)
    time_to_degree(3,00)
    time_to_degree(6,00)
    time_to_degree(9,15)
