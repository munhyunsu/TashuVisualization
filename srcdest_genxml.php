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
	//$query = "SELECT c.rent_station AS rent_station, c.name AS rent_name, c.latlng AS rent_latlng, d.return_station AS return_station, d.name AS return_name, d.latlng AS return_latlng, c.count AS count FROM ( SELECT b.rent_station AS rent_station, a.name AS name, a.latlng AS latlng, b.return_station AS return_station, b.count AS count FROM (SELECT station_number, name, latlng FROM station) AS a RIGHT OUTER JOIN (SELECT rent_station, return_station, COUNT(*) AS count FROM innout WHERE rent_station != 0 AND return_station != 0 AND rent_station != return_station GROUP BY rent_station, return_station) AS b ON a.station_number = b.rent_station) AS c LEFT OUTER JOIN ( SELECT b.rent_station AS rent_station, a.name AS name, a.latlng AS latlng, b.return_station AS return_station, b.count AS count FROM (SELECT station_number, name, latlng FROM station) AS a RIGHT OUTER JOIN (SELECT rent_station, return_station, COUNT(*) AS count FROM innout WHERE rent_station != 0 AND return_station != 0 AND rent_station != return_station GROUP BY rent_station, return_station) AS b ON a.station_number = b.return_station) AS d ON c.rent_station = d.rent_station AND c.return_station = d.return_station ORDER BY count DESC LIMIT 50";
	$result = mysql_query($query);
	if(!$result) {
		die('Invalid query : ' . mysql_error());
	}

	// XML file create - header
	header("Content-type: text/xml");
	// Iterate through the rows, adding XML nodes for each
	while($row = @mysql_fetch_assoc($result)) {
		// Add to XML document node
		$node = $dom->createElement("route");
		$newnode = $parnode->appendChild($node);
		$newnode->setAttribute("rent_station", $row['rent_station']);
		$newnode->setAttribute("rent_name", $row['rent_name']);
		list($lat, $lng) = explode(",", $row['rent_latlng']);
		$newnode->setAttribute("rent_lat", $lat);
		$newnode->setAttribute("rent_lng", $lng);
		$newnode->setAttribute("return_station", $row['return_station']);
		$newnode->setAttribute("return_name", $row['return_name']);
		list($lat, $lng) = explode(",", $row['return_latlng']);
		$newnode->setAttribute("return_lat", $lat);
		$newnode->setAttribute("return_lng", $lng);
		$newnode->setAttribute("count", $row['count']);
	}

	// XML file end

	echo $dom->saveXML();

	mysql_close($connection);
?>
