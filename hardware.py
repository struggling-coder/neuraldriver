import #communication stuff

def sense():
	"Return 2-list of sensor difference at [L, R]"
	#return string: S1, S2, S3 
	sensors = client("0").split(",")
	return [sensors[1] - sensors[2], sensors[3] - sensors[2]]

def pulse(inp):
	"Send pulse to engine"
	client(str(inp))

def rpulse(inp):
	"Execute pulse in reverse"
	inp.reverse()
	pulse(inp)

def client(command):
	"Send HTTP or equivalent request to Arduino
	return out
