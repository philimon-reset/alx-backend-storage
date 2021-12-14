#!/usr/bin/env python3
"""  changes all topics of a school document based on the name """

import pymongo


def update_topics(mongo_collection, name, topics):
    """ main function """
    return mongo_collection.insert_one(kwargs).inserted_id
