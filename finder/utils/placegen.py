import random

ADJECTIVES = """
        autumn hidden bitter misty silent empty dry dark summer
        icy delicate quiet white cool spring winter patient
        twilight dawn crimson wispy weathered blue billowing
        broken cold damp falling frosty green long late lingering
        bold little morning muddy old red rough still small
        sparkling throbbing shy wandering withered wild black
        young holy solitary fragrant aged snowy proud floral
        restless divine polished ancient purple lively nameless
    """.split()

NOUNS = """
        waterfall river breeze moon rain wind sea morning
        snow lake sunset pine shadow leaf dawn glitter forest
        hill cloud meadow sun glade bird brook butterfly
        bush dew dust field fire flower firefly feather grass
        haze mountain night pond darkness snowflake silence
        sound sky shape surf thunder violet water wildflower
        wave water resonance sun wood dream cherry tree fog
        frost voice paper frog smoke star
    """.split()

MIN_LON = -180
MAX_LON = 180
MIN_LAT = -85
MAX_LAT = 85


def generate_random_name():
    adj_noun_num = [random.choice(ADJECTIVES),
                    random.choice(NOUNS),
                    str(random.randint(1, 10000000))]

    return "-".join(adj_noun_num)


def generate_random_coords():
    lon, lat = random.randint(MIN_LON, MAX_LON), random.randint(MIN_LAT, MAX_LAT)

    return lon, lat


def generate_random_location():
    lon, lat = generate_random_coords()
    name = generate_random_name()

    return lon, lat, name


if __name__ == '__main__':
    for _ in range(10):
        print(generate_random_name())
