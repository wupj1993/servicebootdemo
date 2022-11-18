# -*- coding: utf-8 -*-
import threading


def action_echo(**args):
    age = args["age"]
    address = args.get("address")
    name = args["name"]
    req = threading.current_thread().request_info
    print(req.get("http_request"))
    return {'age': age, 'address': address, 'name': name}
