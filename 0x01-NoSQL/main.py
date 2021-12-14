#!/usr/bin/env python3
""" nginx logs to mongo instance parser """

from pymongo import MongoClient
from collections import Counter


if __name__ == "__main__":
    """ main process """
    client = MongoClient()
    db = client.logs
    coll = [x for x in db.nginx.find()]
    ip = [x["ip"] for x in db.nginx.aggregate([{"$project": {"_id":0, "ip": 1}}])]
    method_C = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    status = 0
    count = 0
    main = {}
    for i in coll:
        if i["method"] in method_C:
            method_C[i["method"]] += 1
        if i["method"] == "GET" and i["path"] == "/status":
            status += 1
    print(f"{len(coll)} logs")
    print("Methods:")
    for key, value in method_C.items():
        print(f"\tmethod {key}: {value}")
    print(f"{status} status check")
    for x in list(set(ip)):
        main[x] = ip.count(x)
    print("IPs:")
    for y in sorted(main.items(), key=lambda x: x[1], reverse=True):
        if count > 10:
            break
        count += 1
        print(f"\t{y[0]}: {y[1]}")
