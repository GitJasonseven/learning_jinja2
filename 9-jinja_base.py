#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from jinja2 import FileSystemLoader, Environment

loader = FileSystemLoader("templates", encoding="utf-8")
env = Environment(loader=loader)
tpl = env.get_template("child.conf.tpl")
output = tpl.render()
print(output)