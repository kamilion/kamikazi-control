#!/usr/bin/env python3
__author__ = 'kamilion@gmail.com'
from flask import Flask, Response
import unicodedata

def clean_filename(filename):
    validchars = "abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ-0123456789"
    if (not isinstance(filename, str)) and (sys.version_info.major != 2):
        filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    return str(''.join(c for c in filename if c in validchars))

import sh  # Gotta have the SH module around. Make sure you don't feed it color.

flask_core = Flask(__name__)
#flask_core.debug = True

def list_xen():
    cmd = sh.Command("kamikazi-get-running-vms-json.sh")
    return cmd()


@flask_core.route("/")
def index():
    return Response(response=list_xen(), status=200, mimetype="application/json")


if __name__ == "__main__":
    flask_core.run(host='0.0.0.0')
