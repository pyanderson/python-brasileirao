# -*- coding: utf8 -*-


def to_unicode(string):
    if string:
        return u''.join(string).encode('utf-8').strip()
    return u''
