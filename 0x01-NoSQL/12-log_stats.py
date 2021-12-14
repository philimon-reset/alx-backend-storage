#!/usr/bin/env python3
""" nginx logs to mongo instance parser """

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    main = client.logs.nginx
    method_C = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    status = main.count_documents({"method": "GET", "path": "/status"})
    print(f"{main.estimated_document_count()} logs")
    print("Methods:")
    for i in method_C:
        check = main.count_documents({"method": i})
        print(f"\tmethod {i}: {check}")
    print(f"{status} status check")
