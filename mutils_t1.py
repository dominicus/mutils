#!/usr/bin/env python
#

import sys
import mutils

if __name__ == "__main__":
    compInfo = mutils.loadComposers()
    for k,v in compInfo.iteritems():
        print k, v

    sys.exit(0)
