<!DOCTYPE html>
<!--	
		Blackboard: bchen3
		Date: 10/29/2019
		File:	
		Purpose: Write a Web-based application consisting of a Web form 	(lastname-software-order.html) and a PHP progam (lastname-software-order.php) 
		
		lastname-software-order.html currently contains code meeting the following algorithm:
						
					lastname-software-order.html algorithm
						Prompt for numCopies
						Get numCopies
						Prompt for os
						Get os
						Submit numCopies, os to lastname-software-order.php
					END
					
		REQUIREMENT: Create a php program that meets the following algorithm:
					lastname-software-order.php algorithm:
						Receive numCopies, os from softwareOrder.html
						subtotal = numCopies * 35.00
						tax = subtotal * 0.07
						shippingHandling = numCopies * 1.25
						totalCost = subtotal + tax + shippingHandling
						Display os, numCopies, subtotal, tax, shippingHandling, totalCost
					END	
					
		ADDITIONAL REQUIREMENTS:  
				1. Modify lastname-software-order.html as needed
				2. Display for Sub-total, Sales-tax, Shipping and Handling and Total are required to display 2 decimal points. 
-->
<html>
<head>
	<title>SaveTheWorldSoftware</title>
	<link rel ="stylesheet" type="text/css" href="sample.css">
</head>
<body>
  <h1>Save The World Software</h1>
  <?php
	$operatingSys = $_POST['os'];
	$numberOfCopy = $_POST['numCopies'];
	$subtotal = $numberOfCopy * 35;
	$tax = $subtotal * 0.07;
	$shippingHandling = $numberOfCopy * 1.25;
	$total = $subtotal + $tax + $shippingHandling;

	
	print ("<p>Operating System: $operatingSys</p>");
	print ("<p>Number of Copies: $numberOfCopy</p>");
	print ("<p>Sub-Total:$".number_format($subtotal,2)."</p>");
	print ("<p>Sales Tax:$".number_format($tax,2)."</p>");
	print ("<p>Shipping and Handling:$".number_format($shippingHandling,2)."</p>");
	print ("<p></p>");
	print ("<p><h2>TOTAL: $".number_format($total,2)."</h2></p>");
  
  ?>
	
	
	
	
	</body>
</html>
