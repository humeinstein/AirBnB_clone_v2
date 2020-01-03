#!/usr/bin/python3
# fabric script that generates .tgz archive from the contents of webstatic folder of airbnb clone repo


from fabric.api import local
from datetime import datetime


def do_pack():
    """file packer"""
    local("mkdir -p versions")
    datetimes = datetime.now().strftime("%Y%m%d%H%M%S")
    filepack = ("versions/web_static_().tgz").format(datetimes)
    local("sudo tar -cvsf {} web_static".format(filepack))
    return (file)
