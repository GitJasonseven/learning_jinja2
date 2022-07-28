#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from jinja2 import Template
template = Template(source="Hello {{ name }}")
result = template.render(name="there")

print(result)

