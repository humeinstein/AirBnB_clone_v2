#!/usr/bin/python3
"""fabric script that generates .tgz archive"""
from fabric.operations import *
from datetime import datetime


def do_pack():
    """create tgz archive"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time))
    except Exception:
        return None
    return ("versions/web_static_().tgz".format(temp))
