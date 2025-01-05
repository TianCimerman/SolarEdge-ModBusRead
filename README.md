Librarys:
influxdb-client    1.48.0
pymodbus           3.5.0
solaredge-modbus   0.8.0

Influx_atr:
bucket = "data"
org = "family"
token = "2B7SPpKmVGAnMCkWYTxRTU1_vtbruS2EBEYN_zqyKR0azK5S-lKyhTNdVf8IsmYleo566wIT3-fTTY_QhHQd9Q=="
url = "http://192.168.1.120:8086"

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
