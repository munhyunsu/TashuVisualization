<?php
	require("mysqlinfo.php");

	// Start XML file, create parent node
	$dom = new DOMDocument("1.0");
	$node = $dom->createElement("routes");
	$parnode = $dom->appendChild($node);

	// Opens a connection to a MySQL server
	$connection = mysql_connect($server, $username, $password);
	if(!$connection) {
		die('Not connected : ' . mysql_error());
	}

	// Set the active MySQL database
	$db_selected = mysql_select_db($database, $connection);
	if(!$db_selected) {
		die('Can\'t use db : ' . mysql_error());
	}

	mysql_query("SET NAMES 'utf8'", $connection);

	// Set Query
	$query = $_REQUEST["query"];
	//$query = "SELECT d.name AS return_name, c.count AS count FROM  (SELECT b.rent_station AS rent_station, a.name AS name, a.latlng AS latlng, b.return_station AS return_station, b.count AS count FROM  (SELECT station_number, name, latlng FROM station) AS a  RIGHT OUTER JOIN  (SELECT rent_station, return_station, COUNT(*) AS count FROM innout WHERE rent_station =  1  AND return_station != 0 AND rent_station != return_station AND  rent_date   BETWEEN '
//2013/01/01 00:00:00
//' AND '
//2014/01/01 05:59:59
//' GROUP BY rent_station, return_station ORDER BY count DESC LIMIT  10  ) AS b  ON a.station_number = b.rent_station) AS c  LEFT OUTER JOIN  (SELECT b.rent_station AS rent_station, a.name AS name, a.latlng AS latlng, b.return_station AS return_station, b.count AS count FROM  (SELECT station_number, name, latlng FROM station) AS a  RIGHT OUTER JOIN  (SELECT rent_station, return_station, COUNT(*) AS count FROM innout WHERE rent_station =  1  AND return_station != 0 AND rent_station != return_station AND  rent_date   BETWEEN '
//2013/01/01 00:00:00
//' AND '
//2014/01/01 05:59:59
//' GROUP BY rent_station, return_station ORDER BY count DESC LIMIT  10 ) AS b  ON a.station_number = b.return_station) AS d ON c.rent_station = d.rent_station AND c.return_station = d.return_station ORDER BY count DESC  LIMIT 10";
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
