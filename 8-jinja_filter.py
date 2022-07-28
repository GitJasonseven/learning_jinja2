#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from jinja2 import FileSystemLoader, Environment


def vendor_filter(vendor):
    new_vendor = vendor[:3]+["..."]
    return new_vendor

vendor_list = ["cisco","huawei","h3c","ruijie","fortinet","sangfor"]



loader = FileSystemLoader("templates", encoding="utf-8")
env = Environment(loader=loader)
env.filters["vendor_filter"] = vendor_filter
tpl = env.get_template("filter.conf.tpl")
output = tpl.render(vendor_list = vendor_list)
print(output)