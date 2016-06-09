#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr", "/opt"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf wps-office_%s~a20p2_amd64.deb" % Version)
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "etc")