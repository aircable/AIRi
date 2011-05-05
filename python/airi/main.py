#!/usr/bin/env python
# -*- coding: utf-8 -*-
from airi.jinja import main as jmain
from twisted.internet import reactor
from twisted.python import log

def main():
  import sys
  if sys.platform == "linux2" and "-nopairing" not in sys.argv:
      import subprocess
      subprocess.Popen([sys.executable, "-m" "airi.pair"])
  log.startLogging(sys.stdout)
  jmain()
  reactor.run()

if __name__ == '__main__':
  main()