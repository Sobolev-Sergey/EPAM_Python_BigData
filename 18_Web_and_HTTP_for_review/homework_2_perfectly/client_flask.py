#
# Copyright 2020 Sobolev Sergey. All rights reserved. :-))
#

"""
Get of routes to handle requests for news endpoints
"""

import logging
import requests


BASE_URL = "http://localhost:5000/"
COUNTRY = "us"
CLIENT_LOG_NAME = "client.log"
NEWS_SUFFIX = "news"
SOURCE_FOX = "fox-news"


def show_top_news(country):
    """
    Show to users live top and breaking news headlines from country
    :param country: country name
    :return:
    """
    url = f"{BASE_URL}/{NEWS_SUFFIX}/country/{country}"
    logger.info(f"Get top news from: {url} for country: {country}")
    response = requests.get(url)

    if response.status_code == 200:
        for article in response.json()["articles"]:
            print(
                f"Author: {article['author']}. Date: {article['publishedAt']}"
            )
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']} \n")
    else:
        print(f"Can't get top and breaking news for the country: {country}")


def specific_source_news(specific_source):
    """
    Show to users live news headlines from a specific source
    :param country: country name
    :return:
    """
    url = f"{BASE_URL}/{NEWS_SUFFIX}/sources/{specific_source}"
    logger.info(
        f"Get top news from: {url} for a specific source: {specific_source}"
    )
    response = requests.get(url)

    if response.status_code == 200:
        for article in response.json()["articles"]:
            print(f"{article['author']}: {article['title']}")
            print(f"{article['description']} \n")
    else:
        print(f"Can't get news from a specific source: {specific_source}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename=CLIENT_LOG_NAME)
    logger = logging.getLogger(f"Client ")

    logger.info(f"Start client: {__name__}")

    # Show to users live top and breaking news headlines from the USA
    show_top_news(COUNTRY)

    # Show to users live news headlines from a specific source
    specific_source_news(SOURCE_FOX)
