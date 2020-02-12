from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import time

cpu = CPUTemperature()
print(cpu.temperature)

pinList = [2, 3, 4]
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

while True:


    if int(cpu.temperature) >= 40:
        GPIO.output(2, GPIO.LOW)
        print("Fan 1 on")
        break
    else:
        time.sleep(5)
        print(cpu.temperature)

while True:

    if int(cpu.temperature) >= 45:
            GPIO.output(3, GPIO.LOW)
            print("Fan 2 on")
            break
    else:
        time.sleep(5)
        print(cpu.temperature)

while True:

    if int(cpu.temperature) >= 50:
        GPIO.output(4, GPIO.LOW)
        print("Fan 3 on")
        break
    else:
        time.sleep(5)
        print(cpu.temperature)
