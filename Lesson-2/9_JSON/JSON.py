#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('http://cn.udacity.com')
result = r.json()
print(result)