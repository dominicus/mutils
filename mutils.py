#!/usr/bin/env python
# -*- utf-8 -*-

"""
 Various routines for Mutopia Project maintenance.
"""

import os
import codecs
import logging

mutopia_base = "MUTOPIA_BASE"

# Load lines formatted as 2-line pairs into a dictionary.
# Not meant to be exported.
def _load_line_pairs(lines):
    d = dict()
    for n in range(0, len(lines), 2):
        key = lines[n].rstrip(os.linesep)
        val = lines[n+1].rstrip(os.linesep)
        d[key] = val

    return d


def getMutopiaBase():
    """Get the mutopia base environment variable.
    """
    mutop = os.getenv("MUTOPIA_BASE")
    if not mutop:
        logger.getLogger("mutils")
        logger.error('must have MUTOPIA_BASE environment set')

    return mutop


def loadComposers():
    """ Create a dict collection of the valid mutopia composers.
    """
    mutop = getMutopiaBase()

    compdata = codecs.open(
        os.path.join(mutop, 'datafiles','composers.dat'),
        'rt',
        encoding='utf-8')
    composers = compdata.readlines()
    compdata.close()

    return _load_line_pairs(composers)


def loadInstruments():
    """ Create a dict collection of the valid mutopia instruments.
    """
    mutop = getMutopiaBase()

    instrumentData = codecs.open(
        os.path.join(mutop, 'datafiles','instruments.dat'),
        'rt',
        encoding='utf-8')
    instruments = instrumentData.readlines()
    instrumentData.close()

    return _load_line_pairs(instruments)


def loadStyles():
    """ Create a dict collection of the valid mutopia styles.
    """
    mutop = getMutopiaBase()

    styleData = codecs.open(
        os.path.join(mutop, 'datafiles','styles.dat'),
        'rt',
        encoding='utf-8')
    styles = styleData.readlines()
    styleData.close()

    return _load_line_pairs(styles)
