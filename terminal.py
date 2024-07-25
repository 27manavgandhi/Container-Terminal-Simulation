import simpy
from vessel import Vessel
from utils import generate_interarrival_time
class Terminal:
    def __init__(self, env):
        self.env = env
        self.berths = simpy.Resource(env, capacity=2)
        self.cranes = simpy.Resource(env, capacity=2)
        self.trucks = simpy.Resource(env, capacity=3)
        self.vessel_id = 0

    def vessel_arrival(self):
        while True:
            yield self.env.timeout(generate_interarrival_time())
            self.vessel_id += 1
            vessel = Vessel(self.vessel_id)
            self.env.process(self.handle_vessel(vessel))

    def handle_vessel(self, vessel):
        arrival_time = self.env.now
        print(f"{self.env.now:.2f}: {vessel} arrived")

        with self.berths.request() as berth_req:
            yield berth_req
            print(f"{self.env.now:.2f}: {vessel} berthed")

            with self.cranes.request() as crane_req:
                yield crane_req
                while vessel.containers > 0:
                    with self.trucks.request() as truck_req:
                        yield truck_req
                        yield self.env.timeout(3)  # Crane operation time
                        vessel.containers -= 1
                        print(f"{self.env.now:.2f}: Container moved from {vessel} to truck")
                        
                        self.env.process(self.truck_transport(vessel))

        departure_time = self.env.now
        print(f"{self.env.now:.2f}: {vessel} departed. Total time at terminal: {departure_time - arrival_time:.2f}")

    def truck_transport(self, vessel):
        yield self.env.timeout(6)  # Truck transport time
        print(f"{self.env.now:.2f}: Container from {vessel} delivered to yard block")