#!/usr/bin/env python3
__author__ = 'kamilion@gmail.com'
from flask import Flask, Response
import sh  # Gotta have the SH module around. Make sure you don't feed it color.

flask_core = Flask(__name__)
#flask_core.debug = True

def list_xen():
    cmd = sh.Command("kamikazi-get-vms-json.sh")
    return cmd()


@flask_core.route("/")
def index():
    return Response(response=list_xen(), status=200, mimetype="application/json")


if __name__ == "__main__":
    flask_core.run(host='0.0.0.0')
