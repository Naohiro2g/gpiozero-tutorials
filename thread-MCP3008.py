from gpiozero import MCP3008,LED
from time import sleep
import threading

pot = MCP3008(0) # Pot is connected to CH0
ldr = MCP3008(1) # LDR is connected to CH1
led = LED(21)
thresh = 0.5 # set threshold level to differentiate between light and dark

# Thread for handling MCP3008 data stream
class readMCP3008(threading.Thread):
 
    def __init__(self):
        super(readMCP3008, self).__init__()
        self.terminated = False
        self.start()
 
    def run(self):
        global read_pot
        global read_ldr
        print '\nMCP3008 started! Reading input channels....'
        while not self.terminated:
            # grab all available input from MCP3008
	    read_pot = pot.value
	    read_ldr = ldr.value
	    sleep(0.5)
	
            if self.terminated:
	        break
        print 'MCP3008 stopped'

# Startup sequence
print 'Initialize MCP3008'
readMCP3008 = readMCP3008()

if __name__ == "__main__":
    try:
	print 'Press CTRL+C to quit'
	running = True
	read_pot = 0
        read_ldr = 0
	while running:
            print("\nPot:{:.2f}  LDR:{:.2f}".format(read_pot,read_ldr))
            sleep(0.1)
            if read_ldr < thresh:
                led.on()
            else:
                led.off()
    except KeyboardInterrupt:
            print '\nShutting down...'
    readMCP3008.terminated = True
    readMCP3008.join()

    print
