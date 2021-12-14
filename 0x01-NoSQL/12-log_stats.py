#!/usr/bin/env python3
""" nginx logs to mongo instance parser """

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    main = client.logs.nginx
    method_C = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    status = main.count_documents({"method": "GET", "path": "/status"})
    print(f"{main.estimated_document_count()} logs")
    print("Methods:")
    for i in method_C:
        check = main.count_documents({"method": i})
        print(f"    method {i}: {check}")
    print(f"{status} status check")