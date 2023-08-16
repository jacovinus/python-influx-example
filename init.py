import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision

from influxdb_client.client.write_api import SYNCHRONOUS

def initInflux():
    token = os.environ.get("INFLUXDB_TOKEN")
    org = "my-org"
    url = "http://localhost:8086"
    print (url)
    write_client = InfluxDBClient(url=url, token=token, org=org, debug=True) 
    return write_client


write_client = initInflux()
bucket = "my-bucket"
write_api = write_client.write_api(write_options=SYNCHRONOUS) 

for value in range(5):
    point = (
        Point("measurement1")
        .tag("location", "Madrid")
        .field("value",value)

    )
    write_api.write(bucket=bucket, org="my-org", record=point)
    time.sleep(1) # separate the points by 1 second

query_api = write_client.query_api()

query = """from(bucket: "my-bucket")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="my-org")

for table in tables:
    for record in table.records:
        print (record.values["_value"])

