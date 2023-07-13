# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/links/favicon.pt'

__tokens = {55: ('${python: view.mimetype}', 3, 14), 57: ('python: view.mimetype', 3, 16), 121: ('python: view.favicon_path', 5, 15), 227: ('python: view.favicon_path', 10, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878325920 = {'rel': 'mask-icon', 'href': 'python: view.favicon_path', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878327984 = {'rel': 'preload icon', 'type': '${python: view.mimetype}', 'href': 'python: view.favicon_path', }
_static_4659865408 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales, zope_version_5_8_3_):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684272912
            __attrs_4684272912 = _static_4659865408
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x122c560b0> name=None at 117346f90> -> __attrs_4664343056
            __attrs_4664343056 = _static_4878327984

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="preload icon"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684267792
            __default_4684267792 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python: view.mimetype}' (3:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117346e10> -> __attr_type
            __token = 55
            __token = 57
            try:
                __zt_tmp = __attrs_4664343056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_type = _static_4662095120('python', ' view.mimetype', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_type = __quote(__attr_type, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_type = __attr_type
            if (__attr_type is None):
                pass
            else:
                if (__attr_type is _DEFAULT_MARKER):
                    __attr_type = None
                else:
                    __tt = type(__attr_type)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_type = str(__attr_type)
                    else:
                        if (__tt is bytes):
                            __attr_type = decode(__attr_type)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_type = __attr_type.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_type)
                                    __attr_type = (str(__attr_type) if (__attr_type is __converted) else __converted)
                                else:
                                    __attr_type = __attr_type()
            if (__attr_type is not None):
                __append((' type="%s"' % __attr_type))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684270288
            __default_4684270288 = _DEFAULT_MARKER

            # <Substitution 'python: view.favicon_path' (5:15)> -> __attr_href
            __token = 121
            try:
                __zt_tmp = __attrs_4664343056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4662095120('python', ' view.favicon_path', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x122c558a0> name=None at 117583910> -> __attrs_4676677648
            __attrs_4676677648 = _static_4878325920

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="mask-icon"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4676845840
            __default_4676845840 = _DEFAULT_MARKER

            # <Substitution 'python: view.favicon_path' (10:15)> -> __attr_href
            __token = 227
            try:
                __zt_tmp = __attrs_4676677648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4662095120('python', ' view.favicon_path', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }