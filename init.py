import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from random import randrange, choice
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
country_list = ["Madrid", "Paris", "Rome", "Valencia"]

for value in range(35):
    randnum = randrange(0, 100, 2)
    randtime = randrange(1, 5, 1)
    randcity = choice(country_list)
    point = (
        Point("measurement1")
        .tag("location", randcity)
        .field("value",randnum)

    )
    write_api.write(bucket=bucket, org="my-org", record=point)
    time.sleep(randtime) # separate the points by 1 second

query_api = write_client.query_api()

query = """from(bucket: "my-bucket")
  |> range(start: -10m)
  |> filter(fn: (r) => r._measurement == "measurement1")
  |> mean()"""
tables = query_api.query(query, org="my-org")

for table in tables:
    for record in table.records:
        print (record.values["_value"])

