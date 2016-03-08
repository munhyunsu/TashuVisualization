#!/usr/bin/python
# -*- coding: utf8 -*-

# CSV 파일
import csv

def __main__():
	out_file = open('station_motion_static.html', 'w')
	out_file.write('<html>\n')
	out_file.write('<head>\n')
	out_file.write('<script type="text/javascript" src="https://www.google.com/jsapi"></script>\n')
	out_file.write('<script type="text/javascript">\n')
	out_file.write('google.load("visualization", "1", {packages:["motionchart"]});\n')
	out_file.write('google.setOnLoadCallback(drawChart);\n')
	out_file.write('function drawChart() {\n')
	out_file.write('var data = new google.visualization.DataTable();\n')
	out_file.write('data.addColumn("string", "Station");\n')
	out_file.write('data.addColumn("date", "Date");\n')
	out_file.write('data.addColumn("number", "The number of rent");\n')
	out_file.write('data.addColumn("number", "The usage time");\n')
	out_file.write('data.addColumn("number", "The distance");\n')
	out_file.write('data.addColumn("string", "The usage type");\n')
	out_file.write('data.addRows([\n')

	motion_file = open('motion_csv/motion.csv', 'r')
	motion_csv = csv.DictReader(motion_file, delimiter=',', quotechar='"')

	count = 1
	for row in motion_csv:
		date = row['V1']
		if count >= 24:
			out_file.write('["All" , ' + 'new Date(' + str(int(date[0:4])) + ', ' + str(int(date[4:6])-1) + '), ' + row['V2'] + ', ' + row['V3'] + ', ' + row['V4'] + ', "All"],\n')
			out_file.write('["Same" , ' + 'new Date(' + str(int(date[0:4])) + ', '  + str(int(date[4:6])-1) + '), ' + row['V5'] + ', ' + row['V6'] + ', ' + row['V7'] + ', "Same"],\n')
			out_file.write('["Diff" , ' + 'new Date(' + str(int(date[0:4])) + ', ' + str(int(date[4:6])-1) + '), ' + row['V8'] + ', ' + row['V9'] + ', ' + row['V10'] + ', "Diff"]\n')
		else:
			out_file.write('["All" , ' + 'new Date(' + str(int(date[0:4])) + ', ' + str(int(date[4:6])-1) + '), ' + row['V2'] + ', ' + row['V3'] + ', ' + row['V4'] + ', "All"],\n')
			out_file.write('["Same" , ' + 'new Date(' + str(int(date[0:4])) + ', ' + str(int(date[4:6])-1) + '), ' + row['V5'] + ', ' + row['V6'] + ', ' + row['V7'] + ', "Same"],\n')
			out_file.write('["Diff" , ' + 'new Date(' + str(int(date[0:4])) + ', ' + str(int(date[4:6])-1) + '), ' + row['V8'] + ', ' + row['V9'] + ', ' + row['V10'] + ', "Diff"],\n')
		count = count + 1

	motion_file.close()

	out_file.write(']);\n')
	out_file.write('\n')
	out_file.write('var chart = new google.visualization.MotionChart(document.getElementById("chart_div"));\n')
	out_file.write('var options = {};\n')
	out_file.write('\n')
	out_file.write('options["state"] = \n')
	out_file.write('\'{"sizeOption":"2","yZoomedIn":false,"xZoomedIn":false,"showTrails":false,"xLambda":1,"duration":{"timeUnit":"D","multiplier":1},"xZoomedDataMax":33.4523775151132,"yZoomedDataMax":2.01227209833262,"time":"2013","yZoomedDataMin":0,"dimensions":{"iconDimensions":["dim0"]},"playDuration":15000,"iconType":"BUBBLE","orderedByY":false,"xAxisOption":"3","uniColorForNonSelected":false,"yAxisOption":"4","iconKeySettings":[{"key":{"dim0":"All"}},{"key":{"dim0":"Same"}},{"key":{"dim0":"Diff"}}],"orderedByX":false,"yLambda":1,"xZoomedDataMin":6.27462661520389,"colorOption":"5","nonSelectedAlpha":0.4}\';\n')
	out_file.write('options["width"] = 1366;\n')
	out_file.write('options["height"] = 768;\n')
	out_file.write('\n')
	out_file.write('\n')
	out_file.write('\n')
	out_file.write('\n')
	out_file.write('chart.draw(data, options);\n')
	out_file.write('}\n')
	out_file.write('</script>\n')
	out_file.write('</head>\n')
	out_file.write('<body>\n')
	out_file.write('<div id="chart_div" styple="width: 1366px; height: 768px;"</div>\n')
	out_file.write('</body>\n')
	out_file.write('</html>\n')
	out_file.write('\n')
	out_file.write('\n')

	out_file.close()


if __name__ == '__main__':
	__main__()

