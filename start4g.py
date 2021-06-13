#!/usr/bin/python

import serial
import time

ser = serial.Serial('/dev/ttyUSB2',115200)
#USB AT or ttyS0
ser.flushInput()
EC20status=0

time.sleep(5)

def send_at(command,back,timeout):
	rec_buff = ''
	ser.write((command+'\r\n').encode())
	time.sleep(timeout)
	if ser.inWaiting():
		time.sleep(0.1)
		rec_buff = ser.read(ser.inWaiting())
	if rec_buff != '':
		if back not in rec_buff.decode():
			print(command + ' ERROR')
			print(command + ' back:\t' + rec_buff.decode())
			return 0
		else:
			print(rec_buff.decode())
			return 1
	else:
		print(command + ' no responce')

try:

	send_at('AT+CSQ','OK',1)
	EC20status=send_at('AT+CIMI','4600',1)
        # sim ready
	if EC20status==0:
	   while True:
         	EC20status=send_at('AT+CIMI','4600',1)
                #sim ready
         	if EC20status==1:
         	   break
	EC20status=send_at('AT+CGATT?','+CGATT: 1',1)
	if EC20status==0:
	   while True:
         	EC20status=send_at('AT+CGATT?','+CGATT: 1',1)
                #sim register
         	if EC20status==1:
         	   break
	send_at('AT+QNETDEVCTL=1,1,1','OK', 2)
        #set ecm
except:
	if ser != None:
		ser.close()


if ser != None:
		ser.close()


