#!/usr/bin/env python3
""" nginx logs to mongo instance parser """

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    coll = db.nginx
    method_C = {"GET": 0, "POST": 0, "PUT" : 0, "PATCH" : 0, "DELETE" : 0}
    status = 0
    for i in coll.find():
        method_C[i["method"]] += 1
        if i["method"] == "GET" and i["path"] == "/status":
            status += 1
    print(f"{len(coll)} logs")
    print("Methods:")
    for key, value in method_C.items():
        print(f"\tmethod {key}: {value}")
    print(f"{status} status check")
