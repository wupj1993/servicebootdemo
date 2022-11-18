# -*- coding: utf-8 -*-
class AppCoreTwo(object):
    def __init__(self):
        self.name = "测试"

    def action_say_bye(self, name):
        return "bye {}".format(name)
