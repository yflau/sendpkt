#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# File: linux/setup.py
# Date: 2007-09-18
# Author: gashero
# Copyright@1999-2007, Harry Gashero Liu.

"""
posix兼容构建脚本，主要用于linux
"""

from distutils.core import setup,Extension

module_exlibnet=Extension('sendpkt',
        sources=['exlibnet.c',],
        libraries=['net','pcap']
        )

setup(name="sendpkt",
        version="0.1",
        description="Send ethernet frame in Linux or Win32",
        ext_modules=[module_exlibnet,],
        author="gashero",
        author_email="harry.python@gmail.com",
        url="http://gashero.yeax.com/"
        )