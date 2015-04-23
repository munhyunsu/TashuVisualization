<?php
	require("mysqlinfo.php");

	// Start XML file, create parent node
	$dom = new DOMDocument("1.0");
	$node = $dom->createElement("days");
	$parnode = $dom->appendChild($node);

	// Opens a connection to a MySQL server
	$connection = mysql_connect($server, $username, $password);
	if(!$connection) {
		die('Not connected : ' . mysql_error());
	}

	// Set the active MySQL database
	$db_selected = mysql_select_db($database, $connection);
	if(!$connection) {
		die('Can\'t use db : ' . mysql_error());
	}

	mysql_query("SET NAMES 'utf8'", $connection);

	// Query
	//$query = "SELECT a.day, a.hour, IFNULL(b.value, 0) AS value FROM (SELECT DATE_FORMAT(cal_date, '%w') AS day, DATE_FORMAT(cal_date, '%H') AS hour FROM 2013_cal GROUP BY WEEKDAY(cal_date), HOUR(cal_date)) AS a LEFT OUTER JOIN (SELECT DATE_FORMAT(rent_date, '%w') AS day, DATE_FORMAT(rent_date, '%H') AS hour, COUNT(*) AS value FROM innout WHERE rent_date AND rent_station != 0 AND return_station != 0 GROUP BY WEEKDAY(rent_date), HOUR(rent_date)) AS b ON a.day = b.day AND a.hour = b.hour ORDER BY a.day ASC, a.hour ASC";
	$query = $_REQUEST["query"];
	$result = mysql_query($query);
	if(!$result) {
		die('Invalid query: ' . mysql_error());
	}

	// create csv header
	header('Content-Type: text/csv');
	header('Content-Disposition: attachment;filename=data.csv');
	
	// output header (if atleast one row exists)
	$row = mysql_fetch_assoc($result);
	if($row) {
		echocsv(array_keys($row));
	}

	// output data (if atleast one row exists)
	while($row) {
		echocsv($row);
		$row = mysql_fetch_assoc($result);
	}
	
	// REFERNECE https://www.daniweb.com/web-development/php/threads/361569/export-mysql-results-to-csv-from-php-website
	// replay by rpv_sen
	// echocsv function
	// echo the input array as csv data maintaining consistency with most CSV implementations
	// * uses double-quotes as enclosure when necessary
	// * uses double double-quotes to escape double-quotes
	// * uses CRLF as a line separator
	//
	function echocsv($fields) {
		$separator = '';
		
		foreach($fields as $field) {
			if(preg_match('/\\r|\\n|,|"/', $field)) {
				$field = '"' . str_replace('"', '""', $field) . '"';
			}
			echo $separator . $field;
			$separator = ',';
		}

		echo "\r\n";
	}

	mysql_close($connection);

?>
