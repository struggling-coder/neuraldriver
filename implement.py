from dd import DD
import hardware

driver = DD()
pulses = []; costs=[]

while True:
	command = raw_input("> ")

	if command is "test":
		hardware.test(driver, verbose=True)

	if command is "train":
		train()

def train():
	for j in range(0, raw_input("iterations: ")):
		for k in range(1, steps):
			_in = hardware.sense()
			_out = driver.forward(_in)
			hardware.pulse(_out)
			pulses.append(_out)
			costs.append(hardware.sense())
		[hardware.rpulse(pulses.pop()) for u in range(len(pulses))]
		driver.bp(costs)
		costs=[]; pulses=[]
