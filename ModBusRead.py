import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import solaredge_modbus
import time

bucket = "data"
org = "family"
token = "2B7SPpKmVGAnMCkWYTxRTU1_vtbruS2EBEYN_zqyKR0azK5S-lKyhTNdVf8IsmYleo566wIT3-fTTY_QhHQd9Q=="
# Store the URL of your InfluxDB instance
url = "http://192.168.1.120:8086"

# Initialize the InfluxDB client
client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

while True:
    try:
        # Connect to the SolarEdge inverter
        inverter = solaredge_modbus.Inverter(
            host="192.168.1.170",
            port=1502,
            timeout=1,
            unit=1
        )

        # Read all data from the inverter
        values = inverter.read_all()
        meters = inverter.meters()
        values["meters"] = {}

        for meter, params in meters.items():
            meter_values = params.read_all()
            values["meters"][meter] = meter_values
        
        print(json.dumps(values, indent=4))

        # Extract the power value from the meter data
        power_value = values.get("meters", {}).get("Meter1", {}).get("power", None)
        scale_value = values.get("meters", {}).get("Meter1", {}).get("power_scale", None)
        if scale_value==-1:
            power_value=power_value/10
        elif scale_value==-2:
            power_value=power_value/100
        


        if power_value is not None:
            # Write the power data to InfluxDB
            write_api = client.write_api(write_options=SYNCHRONOUS)
            point = influxdb_client.Point("meter_data2").field("power2", float(power_value) / -1000)
            write_api.write(bucket=bucket, org=org, record=point)
        else:
            print("Power value is None")

    except solaredge_modbus.exceptions.SolarEdgeError as e:
        print(f"Error reading from SolarEdge inverter: {e}")
    except influxdb_client.rest.ApiException as e:
        print(f"Error writing to InfluxDB: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    # Wait for 5 seconds before the next reading
    time.sleep(5)
