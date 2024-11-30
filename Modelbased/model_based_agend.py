class Model_Based_Agent:
    def __init__(self, desired_temp):
        
        self.desired_temp = desired_temp
        self.current_temp = None

    def percept(self, temp):
        
        self.current_temp = temp

    def act(self):
        if self.current_temp > self.desired_temp:
            return "Turn off the heater"
        elif self.current_temp < self.desired_temp:
            return "Turn on the heater"
        else:
            return "Heater is off, temperature is just right"

agent = Model_Based_Agent(22)

rooms = {
    "Living Room": 28,
    "Bedroom": 18,
    "Kitchen": 32
}
for room, temp in rooms.items():
    agent.percept(temp)
    print(f"{room}: {temp} ==> {agent.act()}")
