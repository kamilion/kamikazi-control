#!/usr/bin/env python3
__author__ = 'kamilion@gmail.com'
from flask import Flask, Response
# import subprocess32 as subprocess  # uncomment for python2 compatibility
import subprocess

flask_core = Flask(__name__)
#flask_core.debug = True


def run_xen_cmd(cmd=["xl", "list", "-l"]):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    return p.communicate()[0]


def list_xen():
    cmd = ["kamikazi-get-vms-json.sh"]
    return run_xen_cmd(cmd)


@flask_core.route("/")
def index():
    return Response(response=list_xen(), status=200, mimetype="application/json")


if __name__ == "__main__":
    flask_core.run(host='0.0.0.0')
