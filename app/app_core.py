# -*- coding: utf-8 -*-

from app.service import hello_service


class AppCore(object):
    def __init__(self):
        self.name = "测试"

    def action_echo(self, **args):
        try:
            req = args.get('http_request')
        except:
            pass
        print(req)
        return hello_service.action_echo(**args)
