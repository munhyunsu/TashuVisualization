#!/usr/bin/python
# -*- coding: utf8 -*-

# CSV 파일
import csv

def __main__():
	out_file = open('station_motion_osame.html', 'w')
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
	out_file.write('data.addRows([\n')

	sfile = open('motion_csv/station_info.csv', 'r')
	station = dict()
	sreader = csv.DictReader(sfile, delimiter = ',', quotechar = '"')
	for row in sreader:
		#print row['명칭'].strip()
		station[int(row['번호'])] = (row['명칭'].strip()).replace('\n', ' ')

	sfile.close()

	for station_num in range(1, 145, 1):
		motion_file = open('motion_csv/motion_' + str(station_num) + '.csv', 'r')
		motion_csv = csv.DictReader(motion_file, delimiter=',', quotechar='"')

		count = 1
		for row in motion_csv:
			#print row
			v1 = row['V1']
			v2 = row['V2']
			v3 = row['V3']
			v4 = row['V4']
			v5 = row['V5']
			v6 = row['V6']
			v7 = row['V7']
			v8 = row['V8']
			v9 = row['V9']
			v10 = row['V10']
			if (v1 == 'NA'):
				continue
			if (v2 == 'NA'):
				#print 'wow'
				v2 = str(0)
				v3 = str(0)
				v4 = str(0)
			if (v5 == 'NA'):
				v5 = str(0)
				v6 = str(0)
				v7 = str(0)
			if (v8 == 'NA'):
				v8 = str(0)
				v9 = str(0)
				v10 = str(0)

			if (station_num >= 144) and (count >= 24):
				out_file.write('["' + station[station_num] + '", ' + 'new Date(' + str(int(v1[0:4])) + ', ' + str(int(v1[4:6])-1) + '), ' + v5 + ', ' + v6 + ', ' + v7 + ']\n')
			else:
				out_file.write('["' + station[station_num] + '", ' + 'new Date(' + str(int(v1[0:4])) + ', ' + str(int(v1[4:6])-1) + '), ' + v5 + ', ' + v6 + ', ' + v7 + '],\n')
			count = count + 1

		motion_file.close()

	out_file.write(']);\n')
	out_file.write('\n')
	out_file.write('var chart = new google.visualization.MotionChart(document.getElementById("chart_div"));\n')
	out_file.write('var options = {};\n')
	out_file.write('\n')
	out_file.write('options["state"] = \n')
	out_file.write('\'{"xZoomedDataMin":-1.5257441373120564,"xZoomedIn":true,"nonSelectedAlpha":0.4,"yZoomedIn":true,"orderedByX":false,"dimensions":{"iconDimensions":["dim0"]},"xLambda":1,"xZoomedDataMax":60,"yAxisOption":"2","yZoomedDataMax":3000,"yZoomedDataMin":-259.5169491525424,"orderedByY":false,"time":"2013","playDuration":15000,"iconType":"BUBBLE","xAxisOption":"3","yLambda":1,"duration":{"multiplier":1,"timeUnit":"D"},"uniColorForNonSelected":false,"showTrails":false,"iconKeySettings":[],"sizeOption":"_UNISIZE","colorOption":"_UNIQUE_COLOR"}\';\n')
	#out_file.write('\'{"xZoomedDataMin":0.316666666666667,"xZoomedIn":false,"uniColorForNonSelected":false,"yZoomedIn":false,"iconType":"BUBBLE","showTrails":false,"xLambda":1,"orderedByX":false,"xAxisOption":"3","yZoomedDataMax":6102,"sizeOption":"_UNISIZE","yZoomedDataMin":1,"dimensions":{"iconDimensions":["dim0"]},"playDuration":15000,"nonSelectedAlpha":0.4,"orderedByY":false,"yLambda":1,"yAxisOption":"2","duration":{"multiplier":1,"timeUnit":"D"},"time":"2013","colorOption":"_UNIQUE_COLOR","xZoomedDataMax":43.5709770114943,"iconKeySettings":[]}\';\n')
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

