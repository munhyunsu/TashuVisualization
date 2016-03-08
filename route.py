# -*- coding: utf8 -*-
import csv
import json

# 2013 ~ 2014 타슈 렌탈 데이터 오픈
rental_file = open('tashu_rental_2013to2014.csv', 'rU')
rental = csv.DictReader(rental_file)

# route Station Count Dictionary 생성
routeCount = {}

count=0
# 2013 ~ 2014 타슈 렌탈 데이터 for-each문
for rent in rental:
	count += 1
	
	if rent['RENT_STATION']=="" :
		rent['RENT_STATION']='0'
	
	if rent['RETURN_STATION']=="" :
		rent['RETURN_STATION']=='0'

	# 출발 정류장 번호>>도착 정류장 번호(Key)가 route Station Count Dictionary에 존재할 경우 
	if str(rent['RENT_STATION']+">>"+rent['RETURN_STATION']) in routeCount :
		# 출발 정류장 번호>>도착 정류장 번호(Key)의 Value Count 1 증가
		routeCount[str(rent['RENT_STATION']+">>"+rent['RETURN_STATION'])] += 1
		
	# 출발 정류장 번호>>도착 정류장 번호(Key)가 route station Count Dictionary에 존재하지 않을 경우
	else:
		# 출발 정류장 번호>>도착 정류장 번호(Key)의 Value Count를 1로 설정
		routeCount[str(rent['RENT_STATION']+">>"+rent['RETURN_STATION'])] = 1
print routeCount

# sorted 함수를 통하여 route Station Count Dictionary를 Value 값이 큰 순서대로 sorting 
for stationRoute in sorted(routeCount, key=routeCount.get, reverse=True):
	
	# station Info 데이터 오픈
	station_Info = open('201503_station_info.csv', 'rU')
	stInfo = csv.DictReader(station_Info)

	# 정류장 이름
	rentStationName = ''
	returnStationName = ''

	# station Info 
	for station in stInfo:

		# 상위 station Number와 station Info의 번호가 같을 경우
		if station.get('번호') == str(stationRoute.split('>>')[0]):
			# station Name에 station Info의 명칭에 저장된 정보를 저장
			rentStationName = station.get('명칭')
		elif str(stationRoute.split('>>')[0]) == '0':
			rentStationName = 'MISSING'

		if station.get('번호') == str(stationRoute.split('>>')[1]):
			# station Name에 station Info의 명칭에 저장된 정보를 저장
			returnStationName = station.get('명칭')
		elif str(stationRoute.split('>>')[1]) == '0':
			returnStationName = 'MISSING'
			
	#print "StationRouteNum\t:\t%-8s\tRouteStationName\t:\t%s\nCount\t:\t%-8s\n" % (str(stationRoute), str(rentStationName+">>"+returnStationName),str(routeCount[stationRoute]))

	station_Info.close()

data = '['
for rentS in range(0,146) :
	data += '['
	for returnS in range(0,146) :
		
		if str(str(rentS)+'>>'+str(returnS)) in routeCount :
			data += str(routeCount[str(str(rentS)+'>>'+str(returnS))])
			if returnS != 145 :
				data += ','
		else :
			data += '0'

			if returnS != 145 :
				data += ','

	data += ']'
	if rentS != 145 :
		data += ','
data += ']'

print data
rental_file.close()