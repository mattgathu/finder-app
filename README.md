Finder Application
--

Challenge: **Design a system which can store and index a large number of places**

## Prototype

Prototype built using:
* [Redis](https://redis.io) - database backend
* [Falcon](https://falconframework.org) - web framework
* [Docker](https://www.docker.com) and [docker compose](https://docs.docker.com/compose/overview/) - container environment

To get up and running, run:

`docker-compose up`

The web interface will be availabe at [http://localhost:8000](http://localhost:8000)

The `seed_db_with_random_places.py` script is used to populate redis with random data,
the command to run is:

`docker-compose run app python seed_db_with_random_places.py`

## Design considerations

* High performance throughput
* data oriented as key-value 


## Assumptions made

* Data store size remains relatively constant (_slow growth_)
* API's radius units are in meters.



## Future improvements

* Use a production grade HTTP server such as Nginx infront of Gunicorn
* Disable Transparent Huge Tables for redis - better performance
* Tune redis's fsync settings
* Explore docker networking stack - default setting may not be ideal


## Performance report

Used [locust](https://locust.io) for benchmarking. Results are availabe in the
`benchmarks` folder including screenshots.