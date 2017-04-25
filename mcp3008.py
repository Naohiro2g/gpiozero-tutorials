from gpiozero import MCP3008,LED
from time import sleep

pot = MCP3008(0) # Pot is connected to CH0
ldr = MCP3008(1) # LDR is connected to CH1
led1 = LED(21)

while True:
	print("Pot:{:.2f}  LDR:{:.2f}".format(pot.value,ldr.value))
	sleep(0.5)
	if ldr.value < 0.5:
		led1.on()
	else:
		led1.off()
