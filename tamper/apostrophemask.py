#!/usr/bin/env python

"""
Copyright (c) 2006-2012 sqlmap developers (http://www.sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOWEST

def dependencies():
    pass

def tamper(payload):
    """
    Replaces apostrophe character with its UTF-8 full width counterpart

    Example:
        * Input: AND '1'='1'
        * Output: AND %EF%BC%871%EF%BC%87=%EF%BC%871%EF%BC%87

    References:
        * http://www.utf8-chartable.de/unicode-utf8-table.pl?start=65280&number=128
        * http://lukasz.pilorz.net/testy/unicode_conversion/
        * http://sla.ckers.org/forum/read.php?13,11562,11850
        * http://lukasz.pilorz.net/testy/full_width_utf/index.phps
    """

    return payload.replace('\'', '%EF%BC%87') if payload else payload
