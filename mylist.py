from machine import Pin
import time

led1 = Pin(12,Pin.OUT)
led2 = Pin(26,Pin.OUT)
led3 = Pin(18,Pin.OUT)
led4 = Pin(5,Pin.OUT)

my_num = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

for i in my_num:
    led1.value(i[0])
    led2.value(i[1])
    led3.value(i[2])
    led4.value(i[3])
    time.sleep(0.1)#Create any list
