#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import *
from datetime import datetime

def do_pack():
    """making anarchive on web_static folder"""
     time = datetime.now()
     archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
     local('mkdir -p versions')
     create = local('tar -cvzf versions/{} web_static'.format(archive))
     if create is not None:
         return archive
     else:
         return None
