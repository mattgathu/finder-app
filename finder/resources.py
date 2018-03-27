# -*- coding: utf-8 -*-
"""
App resources
"""
import json
import logging

import falcon


# ============================================================================
# resource classes
# ============================================================================
class BaseResource(object):

    def __init__(self, db):
        self.db = db
        self.logger = logging.getLogger("finder")


class LocationResource(BaseResource):

    def on_post(self, req, resp):
        """Handle POST requests"""
        lon = req.media.get('longitude')
        lat = req.media.get('latitude')
        name = req.media.get('name')

        res = self.db.add_location(lon, lat, name)

        resp.media = {'response': json.dumps(res)}
        resp.status = falcon.HTTP_200


class NearbyResource(BaseResource):

    def on_get(self, req, resp):
        """Handle GET requests"""
        lon = req.get_param('longitude')
        lat = req.get_param('latitude')
        rad = req.get_param('radius')
        lim = req.get_param('limit')

        try:
            result = self.db.find_nearby_locations(lon, lat, rad, lim)

        except Exception as exc:
            self.logger.error(exc)

            error_msg = "Service unavailable"
            raise falcon.HTTPServiceUnavailable(
                "Service Outage",
                error_msg,
                30
            )
        else:
            resp.media = {'locations': result}
            resp.status = falcon.HTTP_200


class ClosestResource(BaseResource):

    def on_get(self, req, resp):
        """Handle GET requests"""
        lon = req.get_param('longitude')
        lat = req.get_param('latitude')
        lim = req.get_param('limit')

        try:
            result = self.db.find_closest_locations(lon, lat, lim)
        except Exception as exc:
            self.logger.error(exc)

            error_msg = "Service unavailable"
            raise falcon.HTTPServiceUnavailable(
                "Service Outage",
                error_msg,
                30
            )
        else:
            results = []
            for entry in result:
                name, dist, coords = entry
                json_entry = {'name': name, 'distance': dist, 'lon': coords[0],
                              'lat': coords[1]}
                results.append(json_entry)
            resp.media = {'locations': results}
            resp.status = falcon.HTTP_200


class IndexResource(object):
    def on_get(self, req, resp):
        resp.media = {'response': "up and running"}
        resp.status = falcon.HTTP_200
# ============================================================================
# EOF
# ============================================================================
