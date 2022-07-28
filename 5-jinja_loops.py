#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from jinja2 import FileSystemLoader, Environment

allowed = ["192.168.1.1","192.168.1.2","192.168.1.3"]
disallowed = ["192.168.1.6","192.168.1.7","192.168.1.8"]

loader = FileSystemLoader("templates", encoding="utf-8")
environment = Environment(loader=loader, trim_blocks=True)
tpl = environment.get_template('acl.conf.tpl')
output = tpl.render(disallowed = disallowed, allowed = allowed)
print(output)