#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from jinja2 import FileSystemLoader, Environment
loader = FileSystemLoader('templates', encoding="utf-8")
enviroment = Environment(loader=loader)
tpl = enviroment.get_template('first.conf.tpl')
output = tpl.render()
print(output)