<?php

	//Armstrong (19-9-19)
	$num = 153;
	$total = 0;
	$x = $num;
	while($x != 0){
		$rem = $x%10;
		$total = ($total + ($rem * $rem * $rem));
		$x = $x/10;
	}
	if($num == $total)
		echo "Number is Armstrong";
	else
		echo "Number is Not Armstrong";

?>
