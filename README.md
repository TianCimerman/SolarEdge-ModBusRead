☀️ SolarEdge-ModBusRead

A Python utility for reading data from SolarEdge inverters via the Modbus protocol and storing it into an InfluxDB time-series database.

🔧 Technologies & Dependencies

Python

pymodbus – Modbus communication

solaredge-modbus – SolarEdge Modbus helper library

influxdb-client – For writing data to InfluxDB

⚡ Features

Connects to SolarEdge inverter using Modbus TCP.

Reads inverter performance metrics (e.g., energy production, voltage, current).

Stores collected data in InfluxDB for analysis and visualization (e.g., with Grafana).

Supports running inside a Python virtual environment (Windows/Linux).

📈 Usage Example

Create and activate a Python virtual environment.

Install required dependencies (pymodbus, solaredge-modbus, influxdb-client).

Configure InfluxDB connection (bucket, org, token, URL).

Run ModBusRead.py to start collecting data.

🎯 Purpose

This project provides a lightweight way to integrate SolarEdge solar inverters with a time-series database, enabling real-time monitoring, dashboards, and energy analysis.
Librarys:
influxdb-client    1.48.0
pymodbus           3.5.0
solaredge-modbus   0.8.0


Python Venv-Windows:
cd path/to/your/project
python -m venv venv
source venv/bin/activate
Run:
cd path/to/your/project
venv\Scripts\activate
Stop:
deactivate

Python Venv-Linux:
cd /path/to/your/project
python3 -m venv venv
Run:
source venv/bin/activate
Stop:
deactivate
