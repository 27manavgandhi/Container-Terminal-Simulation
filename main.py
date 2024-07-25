import simpy
from terminal import Terminal
SIMULATION_TIME = 10000  # in minutes

def run_simulation(env):
    terminal = Terminal(env)
    env.process(terminal.vessel_arrival())

if __name__ == "__main__":
    env = simpy.Environment()
    run_simulation(env)
    env.run(until=SIMULATION_TIME)