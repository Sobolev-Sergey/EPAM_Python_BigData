#
# Copyright 2020 Sobolev Sergey. All rights reserved. :-))
#

"""
Set of routes to handle requests for news endpoints
"""

import logging
import requests

from flask import Flask

server_flask = Flask(__name__)
API_KEY = "3f8ad63a4cd54fe0b3a7c499d8e33408"
URL_NEWS = "http://newsapi.org/v2/top-headlines?"
COUNTRY = "us&"
SOURCE_BBC = "bbc-news&"
SERVER_LOG_NAME = "server.log"


logging.basicConfig(level=logging.ERROR, filename=SERVER_LOG_NAME)
logger = logging.getLogger(f"Server: {__name__}")


@server_flask.route("/news/country/<country>", methods=["GET"])
def country(country=COUNTRY):
    """
    Handling country news endpoint requests
    """
    url = f"{URL_NEWS}country={country}&apiKey={API_KEY}"

    try:
        response = requests.get(url)
    except ConnectionError as exception:
        logger.error(
            f"Connection error. Can't connect to URL: {url}. Reason: {exception}"
        )

    return response.json()


@server_flask.route("/news/sources/<specific_source>", methods=["GET"])
def sources(specific_source=SOURCE_BBC):
    """
    Handling  just from a specific source news endpoint
    """
    url = f"{URL_NEWS}sources={specific_source}&apiKey={API_KEY}"

    try:
        response = requests.get(url)
    except ConnectionError as exception:
        logger.error(
            f"Connection error. Can't connect to URL: {url}. Reason: {exception}"
        )

    return response.json()
