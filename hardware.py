import serial
PORT = raw_input("port: ")
#The Arduino sends no unsolicited data. LOL

def sense():
	"Return 2-list of sensor difference at [L, R]"
	#return string: S1, S2, S3 
	sensors = client("0").split(".")
	return [(int(sensors[1]) - int(sensors[2]))/1024, (int(sensors[3]) - int(sensors[2]))/1024]

def pulse(inp):
	"Send pulse to engine"
	client("0%05.3f%05.3f" % (inp[0], inp[1]))

def rpulse(inp):
	"Execute pulse in reverse"
	client("1%05.3f%05.3f" % (inp[0], inp[1]))

def client(command):
	"Send request to Arduino, properly formatted"
	port = serial.Serial(PORT, 9600)
	if port.readline()[:-2] is "0":
		port.write(command)
		out = port.readline()
		sleep(0.1)
	port.close()
	return out
