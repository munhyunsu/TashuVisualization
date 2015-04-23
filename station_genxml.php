<?php
	header('Content-Type: text/html; charset=utf-8');
	require("mysqlinfo.php");
	
	// get QUERY parameter from URL


	// Start XML file, create parent node
	$dom = new DOMDocument("1.0");
	$node = $dom->createElement("stations");
	$parnode = $dom->appendChild($node);
	
	// Opens a connection to a MySQL server
	$connection=mysql_connect ($server, $username, $password);
	if (!$connection) {  die('Not connected : ' . mysql_error());}
	
	// Set the active MySQL database
	$db_selected = mysql_select_db($database, $connection);
	if (!$db_selected) {
		die ('Can\'t use db : ' . mysql_error());
	}
	
	mysql_query("SET NAMES 'utf8'", $connection);

	// Select all the rows in the station table
	//$query = "SELECT * FROM station";
	$query = $_REQUEST["query"];
	//$query = "SELECT station_number, name, latlng, io.count FROM station AS st, (SELECT rent_station, COUNT(*) AS count FROM innout WHERE rent_station != 0 AND return_station != 0 GROUP BY rent_station ORDER BY COUNT(*) DESC LIMIT 10) AS io WHERE st.station_number = io.rent_station";
	$result = mysql_query($query);
	if (!$result) {
		die('Invalid query: ' . mysql_error());
	}
	
	// XML file create - header
	header("Content-type: text/xml;");
	// Iterate through the rows, adding XML nodes for each
	while($row = @mysql_fetch_assoc($result)) {
		// Add to XML document node
		$node = $dom->createElement("station");
		$newnode = $parnode->appendChild($node);
		$newnode->setAttribute("station_number",$row['station_number']);
		//$newnode->setAttribute("location_number", $row["location_number"]);
		//$newnode->setAttribute("kiosk_number", $row["kiosk_number"]);
		//$newnode->setAttribute("location", $row["location"]);
		$newnode->setAttribute("name", $row["name"]);
		//$newnode->setAttribute("loc_detail", $row["loc_detail"]);
		//$newnode->setAttribute("address", $row["address"]);
		//$newnode->setAttribute("line_number", $row["line_number"]);
		//$newnode->setAttribute("latlng", $row["latlng"]);
		list($lat, $lng) = explode(",", $row["latlng"]);
		$newnode->setAttribute("lat", $lat);
		$newnode->setAttribute("lng", $lng);
	}
	// XML file end
	echo $dom->saveXML();

	mysql_close($connection);
?>
