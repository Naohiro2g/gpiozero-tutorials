from gpiozero import MCP3008,LED
from time import sleep

pot = MCP3008(0) # Pot is connected to CH0
ldr = MCP3008(1) # LDR is connected to CH1
led1 = LED(21)

thresh = 0.5 # set threshold level to differentiate between light and dark

while True:
	print("Pot:{:.2f}  LDR:{:.2f}".format(pot.value,ldr.value))
	sleep(0.5)
	if ldr.value < thresh:
		led1.on()
	else:
		led1.off()
