#!/usr/bin/env python3
""" list all documents using pymongo"""

import pymongo


def list_all(mongo_collection):
    """ main function to list documents"""
    main = [x for x in mongo_collection.find({})]
    return main
