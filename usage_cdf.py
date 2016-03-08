#!/usr/bin/python
# -*- coding: utf8 -*-

# CSV 파일
import csv

def __main__():
	out_file = open('usage_cdf.html', 'w')
	out_file.write('<html>\n')
	out_file.write('<head>\n')
	out_file.write('<script type="text/javascript" src="https://www.google.com/jsapi"></script>\n')
	out_file.write('<script type="text/javascript">\n')
	out_file.write('google.load("visualization", "1", {packages:["motionchart"]});\n')
	out_file.write('google.setOnLoadCallback(drawChart);\n')
	out_file.write('function drawChart() {\n')
	out_file.write('var data = new google.visualization.DataTable();\n')
	out_file.write('data.addColumn("string", "Usage Type");\n')
	out_file.write('data.addColumn("number", "Usage Time");\n')
	out_file.write('data.addColumn("number", "CDF");\n')
	out_file.write('data.addRows([\n')

	time_file = open('data/time_all.csv', 'r')
	time_csv = csv.DictReader(time_file, delimiter=',', quotechar='"')

	count = 0
	for row in time_csv:
		count = count + 1
		if count > 120:
			out_file.write('["2013 Different Rent/Return Station", ' + '%04d' % (1000 + int(row['V1'])) + ', ' + row['V9'] + '],\n')
			out_file.write('["2014 Different Rent/Return Station", ' + '%04d' % (1000 + int(row['V1'])) + ', ' + row['V10'] + '],\n')
			out_file.write('["2013 Same Rent/Return Station", ' + '%04d' % (1000 + int(row['V1'])) + ', ' + row['V6'] + '],\n')
			out_file.write('["2014 Same Rent/Return Station", ' + '%04d' % (1000 + int(row['V1'])) + ', ' + row['V7'] + ']\n')
			break
		out_file.write('["2013 Different Rent/Return Station", ' + '%04d' % (1000 + int(row['V1'])) + ', ' + row['V9'] + '],\n')
		out_file.write('["2014 Different Rent/Return Station", ' + '%04d' % (1000 + int(row['V1'])) + ', ' + row['V10'] + '],\n')
		out_file.write('["2013 Same Rent/Return Station", ' + '%04d' % (1000 + int(row['V1'])) + ', ' + row['V6'] + '],\n')
		out_file.write('["2014 Same Rent/Return Station", ' + '%04d' % (1000 + int(row['V1'])) + ', ' + row['V7'] + '],\n')

	time_file.close()

	out_file.write(']);\n')
	out_file.write('\n')
	out_file.write('var chart = new google.visualization.MotionChart(document.getElementById("chart_div"));\n')
	out_file.write('var options = {};\n')
	out_file.write('\n')
	out_file.write('options["state"] = \n')
	out_file.write('\'{"sizeOption":"_UNISIZE","yZoomedIn":false,"xZoomedIn":false,"orderedByX":false,"showTrails":true,"xLambda":1,"yAxisOption":"2","xZoomedDataMax":-26791862400000,"uniColorForNonSelected":false,"time":"1001","yZoomedDataMin":0.000014818656688771,"dimensions":{"iconDimensions":["dim0"]},"playDuration":15000,"iconType":"BUBBLE","yLambda":1,"yZoomedDataMax":1,"xZoomedDataMin":-30578688000000,"iconKeySettings":[],"duration":{"timeUnit":"Y","multiplier":1},"xAxisOption":"_TIME","orderedByY":false,"colorOption":"_UNIQUE_COLOR","nonSelectedAlpha":0.4}\';\n')
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

