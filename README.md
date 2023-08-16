# Python-InfluxDB example.
_This is just some playing with Python and InfluxDb_

This repo sets up basic local InfluxDb setting with docker compose to play around with python 

Prerequisites: 

- [Docker Compose](https://docs.docker.com/compose) 
- [Pyton3](https://www.python.org/downloads/)

Installations: 
```bash
pip3 install influx-client
```
**.env local variable:**

For setting up an environment variable for influx docker instance, we will need to create a .env file at root of project, just with one line:

```bash
DOCKERDIR="/home/$(whoami)/docker"
```

Then we should just put up our Dockerized influxdb:

```bash
docker-compose pull
docker-compose -d up
```
`InfluxDB will run on port 8086`


To take it down: 
```bash
docker-compose down
```
Run python (test) script

```bash
python3 init.py
```
It should write dummy data in your influxdb dockerized instance, according to the tutorial inside Influx UI.

---
Reference: https://www.influxdata.com/blog/getting-started-python-influxdb/
