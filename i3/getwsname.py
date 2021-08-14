#!/usr/bin/env python3
'''
getwsname.py

Usage:
  getwsname.py <output>
'''
import json
import subprocess as sp
from docopt import docopt

def shellRun(command):
    pr = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    rc = pr.wait()
    out = pr.stdout.read().decode("utf-8")
    err = pr.stderr.read().decode("utf-8")
    return rc, out, err

if __name__ == "__main__":
    args = docopt(__doc__, version="1")
    __, i3dat, __ = shellRun("i3-msg -t get_workspaces")
    
    i3dat = json.loads(i3dat)
    with open("/home/marco/.config/i3/wsname.json") as wsdatf:
        wsdat = json.load(wsdatf)

    for ws in i3dat:
        if ws['visible'] and ws['output'] == args['<output>']:
            print(wsdat[str(ws['num'])])
