#!/usr/bin/python3
"""Fabric script that generates a tgz archive form folder web static"""


from datetime import datetime
from fabric.api import local
import os


def do_pack():
    if not os.path.exists("versions"):
        local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        result = local('tar -cvzf {} web_static'.format(archive_path))
        if result.failed:
            return None
        return result
