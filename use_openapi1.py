import requests

url="http://openAPI.seoul.go.kr:8088/인증키번호/json/RealtimeCityAir/1/25/"

res = requests.get(url)

data = res.json()

RealTime = data['RealtimeCityAir']['row']

for i in RealTime:
    print(i['MSRSTE_NM'])
    print('측정일시',i['MSRDT'][5],'월',i['MSRDT'][7],'일',i['MSRDT'][8:10],':',i['MSRDT'][10:])
    print("미세먼지 : ",i['PM10'],"(㎍/㎥)"," 초미세먼지 :",i['PM25'],"(㎍/㎥)")
    print()

