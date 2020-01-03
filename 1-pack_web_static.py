#!/usr/bin/python3
"""fabric script that generates .tgz archive"""
from fabric.operations import *
from datetime import datetime


def do_pack():
    """create tgz archive"""
    try:
        local("mkdir -p versions")
        time = dateime.now().strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
            time))
        return ("versions/web_static_{}.tgz".format(time))
    except Exception:
        return None
