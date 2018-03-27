# -*- coding: utf-8 -*-
"""
App Runner
"""
import os

import redis
import falcon

from finder.resources import IndexResource, NearbyResource, ClosestResource


# ============================================================================
# utility classes
# ============================================================================
class Setting(object):
    def __init__(self):
        for key, val in os.environ.items():
            setattr(self, key, val)


class LocationStorageEngine(object):

    def __init__(self, settings):
        self.key = 'locations'
        self.conn = redis.Redis(host=settings.REDIS_HOSTNAME,
                                port=settings.REDIS_PORT)

    def find_closest_locations(self, longitude, latitude, limit):
        radius = 6371000 * 2
        locs = self.conn.georadius(self.key, longitude, latitude, radius,
                                   unit='m', count=limit, sort='ASC',
                                   withdist=True, withcoord=True)

        return locs

    def find_nearby_locations(self, longitude, latitude, radius, limit):
        locs = self.conn.georadius(self.key, longitude, latitude, radius,
                                   count=limit, withcoord=True, unit='m')

        return locs

    def add_location(self, longitude, latitude, name):
        result = self.conn.geoadd(self.key, latitude, longitude, name)

        return result


# ============================================================================
# Create falcon app
# ============================================================================
app = falcon.API()
settings = Setting()
db = LocationStorageEngine(settings)

app.add_route('/', IndexResource())
app.add_route('/nearby', NearbyResource(db))
app.add_route('/closest', ClosestResource(db))
# ============================================================================
# EOF
# ============================================================================
