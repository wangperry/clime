#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect

def autotype(s):
    '''Automative detect the type (int, float or string) of `s` and convert `s`
    into it.'''

    if not isinstance(s, str):
        return s

    if s.isdigit():
        return int(s)

    try:
        return float(s)
    except ValueError:
        return s

def getargspec(func):
    '''Get the argument specification of the `func`.

    `func` can be a Python function, built-in function or bound method.

    It get the argument specification by parsing documentation of the
    function if `func` is a built-in function.

    .. versionchanged:: 0.1.4
       Remove `self` automatively if `func` is a method.

    .. versionadded:: 0.1.3
    '''

    if inspect.isfunction(func):
        return inspect.getargspec(func)

    if inspect.ismethod(func):
        argspec = inspect.getargspec(func)
        argspec[0].pop(0)
        return argspec

    def strbetween(s, a, b):
        return s[s.find(a): s.rfind(b)]

    argspecdoc = (inspect.getdoc(func) or '').split('\n')[0]
    argpart = strbetween(argspecdoc, '(', ')')
    args = argpart.split(',')
    args = (arg.strip(' ()[]') for arg in args)
    args = [arg for arg in args if arg]

    defaultpart = strbetween(argspecdoc, '[', ']')
    defaultcount = len([d for d in defaultpart.split(',') if d.strip('[]')])

    return (args or None, None, None, (None,) * defaultcount or None)
