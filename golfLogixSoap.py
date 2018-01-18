#!/usr/bin/env python
# encoding: utf-8
#This code get the data from golfLogix
#WORKS

import requests
from xml.etree import ElementTree
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def CompleteReturnRequest():
	request = """<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
                xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Header>
                <AuthHeader xmlns="https://www.golflogix.com/">
                        <RegistrationId>4339756</RegistrationId>
                        <Nonce>39045384590786</Nonce>
                        <DeviceId>000000000000000</DeviceId>
                        <DeviceType>10</DeviceType>
                        <AppVersion>8.8</AppVersion>
                        <DeviceInfo>Samsung Galaxy S7 - 6.0.0 - API 23 - 1440x2560, vbox86p, 6.0, Android, 8.8, Market</DeviceInfo>
                        <DeviceModelType>1</DeviceModelType>
                        <SmartPhoneId>24</SmartPhoneId>
                        <SessionId>84537368</SessionId>
                </AuthHeader>
                </soap:Header>
                        <soap:Body>
                                <GetCourseKML xmlns="https://www.golflogix.com/">
                                        <courseId>8096</courseId>
                                        <isBoundsRequired>1</isBoundsRequired>
                                </GetCourseKML>
                        </soap:Body>
                </soap:Envelope>"""

	encoded_request = request.encode('utf-8')

	headers = {"Host": "golflogix.com",
			"Connection": "Keep-Alive",
			"Accept-Encoding": "gzip",
           "Content-Type": "text/xml; charset=UTF-8",
		   "SOAPAction": "https://www.golflogix.com/GetCourseKML",
           "Content-Length": "825"}

	response = requests.post(url="https://golflogix.com/golflogixservice.asmx",
                         headers = headers,
                         data = encoded_request,
                         verify=False)

	return response


if __name__ == "__main__":
	result = CompleteReturnRequest()
	print(result)
	print (str(result.text))