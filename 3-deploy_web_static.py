#!/usr/bin/python3                  
"""fabric script that generates .tgz archive"""
from fabric.operations import local, env, put, run
from datetime import datetime
import os
env.hosts = ['34.74.144.148', '34.74.163.244']
env.user = 'ubuntu'


def do_pack():
    """create tgz archive"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p ./versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time))
    except Exception:
        return None
    return ("versions/web_static_().tgz".format(time))


def do_deploy(archive_path):
    """ distribute tgz archive """
    if (os.path.exists(archive_path)):
        try:
            path = archive_path.split('/')[1]
            no_ext = path.split('.')[0]
            data = "/data/web_static/releases/" + no_ext + "/"
            put(archive_path, "/tmp/")
            run("mkdir -p {}".format(data))
            run("tar -xzf /tmp/{} -C {}".format(path, data))
            run("rm /tmp/{}".format(path))
            run("mv {}web_static/* {}".format(data, data))
            run("rm -rf {}web_static".format(data))
            run("rm -rf /data/web_static/current")
            run("ln -s {} /data/web_static/current".format(data))
            return True
        except Exception:
            return False
    else:
        return False


def deploy ():
    """ distribute archive """
    try:
        tgz = do_pack()
    except Exception:
        return(False)
    do_deploy(tgz)
