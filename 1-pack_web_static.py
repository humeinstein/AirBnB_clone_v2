#!/usr/bin/python3
# fabric script that generates .tgz archive


from fabric.operations import *
from datetime import datetime


def do_pack():
    """file packer"""
    try:
        local("mkdir -p versions")
        datetimes = datetime.now().strftime("%Y%m%d%H%M%S")
        filepack = ("versions/web_static_().tgz").format(datetimes)
        local("tar -cvsf {} web_static".format(filepack))
    except Exception:
        return file
