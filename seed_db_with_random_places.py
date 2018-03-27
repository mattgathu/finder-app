import redis

from finder.utils.placegen import generate_random_location


def main():
    conn = redis.Redis(host='redis')

    for _ in range(10000000):
        plc = generate_random_location()
        conn.geoadd('locations', *plc)
        print("Added: {}".format(plc))


if __name__ == '__main__':
    main()
