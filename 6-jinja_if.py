#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from jinja2 import FileSystemLoader, Environment

ports = [{"type":"ethernet", "slot":1, "port_num":1, "intf_type":"access", "vlan":10},
         {"type":"ethernet", "slot":1, "port_num":2, "intf_type":"trunk", "vlan":20}]


loader = FileSystemLoader("templates", encoding="utf-8")
env = Environment(loader=loader)
tpl = env.get_template("ports.conf.tpl")
output = tpl.render(ports = ports)
print(output)