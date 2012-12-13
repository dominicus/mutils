#!/usr/bin/env python
# -*- utf-8 -*-

# lycsv.py
#
#   Walk through valid composers and create a comma separated values
#   (CSV) containing version and the path of the file where the
#   version was found.
#
#   Where UNICODE failures are caught, the version is marked.
#

import mutils
import sys
import logging
import os
import re
import codecs

muftp = 'ftp'
mubadUnicode = 'Invalid Unicode'

vpat = re.compile(u"\s*\\\\version\s+\"([^\"]+)\"", flags=re.UNICODE)

def findVersion(root,lyfile):
    # don't bother opening non-lilypond files
    if not (lyfile.rfind('.ly') or lyfile.rfind('.ily')):
        return None

    lylines = ()
    with codecs.open(os.path.join(root,lyfile), 'rt', encoding='utf-8') as f:
        try:
            lylines = f.readlines()
        except UnicodeDecodeError:
            return mubadUnicode

    for line in lylines:
        m = vpat.match(line)
        if m != None:
            return m.group(1)


def stripPath(upper, p):
    # Strip the part of the path above ftp
    chunks = upper.split(os.sep)
    for i, v in enumerate(chunks):
        if v == muftp:
            chunks.append(p)
            return os.sep.join(chunks[(i+1):])


def showVersionsFor(comp):
    walkTop = os.path.join(mutils.getMutopiaBase(), muftp, comp)
    for root, dirs, files in os.walk(walkTop):
        for f in files:
            version = findVersion(root,f)
            if version != None:
                print u"{!s},{!s}".format(version, stripPath(root, f))


if __name__ == "__main__":

    composers = mutils.loadComposers()

    for k,_ in composers.iteritems():
        logger = logging.getLogger("mutils")
        logger.info(u"Looking at {!s}".format(k))
        showVersionsFor(k)

    sys.exit(0)
