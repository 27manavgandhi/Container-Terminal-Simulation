Container Terminal Simulation
=============================

This project simulates a container terminal using SimPy, focusing on vessel arrivals, container unloading, and truck transportation.

Requirements
------------
- Python 3.7+
- SimPy 4.0.1

Installation
------------
1. Create a virtual environment:
   python -m venv venv

2. Activate the virtual environment:
   - On Windows:
     venv\Scripts\activate
   - On macOS and Linux:
     source venv/bin/activate

3. Install the required packages:
   pip install -r requirements.txt

Project Structure
-----------------
container_terminal_simulation/
│
├── main.py
├── terminal.py
├── vessel.py
├── utils.py
│
├── requirements.txt
└── README.txt

File Descriptions
-----------------
- main.py: Entry point of the simulation. Sets up the SimPy environment and runs the simulation.
- terminal.py: Contains the Terminal class, which manages berths, cranes, and trucks.
- vessel.py: Defines the Vessel class, representing ships arriving at the terminal.
- utils.py: Includes utility functions, such as generating interarrival times.

Simulation Parameters
---------------------
- Vessel arrivals: Follow an exponential distribution with an average of 5 hours between arrivals.
- Containers per vessel: 150
- Berths: 2
- Quay cranes: 2
- Trucks: 3
- Crane operation time: 3 minutes per container
- Truck transport time: 6 minutes per round trip

Running the Simulation
----------------------
1. Ensure you're in the project directory and the virtual environment is activated.
2. Run the following command:
   python main.py

3. The simulation will run and print events to the console, including vessel arrivals, container movements, and vessel departures.

Customization
-------------
- To change the simulation duration, modify the SIMULATION_TIME constant in main.py.
- Other parameters like the number of berths, cranes, or trucks can be adjusted in the Terminal class initialization in terminal.py.

Output
------
The simulation prints timestamped events to the console, including:
- Vessel arrivals
- Vessel berthing
- Container movements
- Truck transports
- Vessel departures

Note: The simulation time is in minutes, where 1 tick equals 1 minute.

Extending the Simulation
------------------------
To add more features or modify existing behavior, you can:
1. Add new methods to the Terminal class for additional processes.
2. Modify the Vessel class to include more attributes or behaviors.
3. Implement new resource types in the Terminal class.
4. Adjust the logging in various methods to capture different or additional information.

For any questions or issues, please refer to the SimPy documentation or contact the project maintainer.