#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from jinja2 import FileSystemLoader, Environment

loader = FileSystemLoader("templates", encoding="utf-8")
environment = Environment(loader=loader)
tpl = environment.get_template("vars.conf.tpl")

data = {"ip":"1.1.1.2"}

# with open('cicso_logging.conf', "w") as f:
#     f.write(tpl.render(data=data))

tpl.stream(data=data).dump('./templates/cicso_logging.conf')