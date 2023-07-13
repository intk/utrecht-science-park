# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/portlets/browser/templates/footer.pt'

__tokens = {76: ('view/render_footer_portlets', 3, 32), 128: ('nothing', 4, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tal import ErrorInfo as _ErrorInfo
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4659865408 = {}
_static_4873509360 = {'class': 'col-xs-12', }
_static_4873516416 = {'class': 'row', }

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

            # <Static value=<ast.Dict object at 0x1227bf580> name=None at 11571a890> -> __attrs_4683135248
            __attrs_4683135248 = _static_4873516416

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="row">\n  ')

            # <Static value=<ast.Dict object at 0x1227bd9f0> name=None at 11558a7d0> -> __attrs_4676768080
            __attrs_4676768080 = _static_4873509360

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-xs-12">\n    ')
            ____fallback_4659653808 = len(__stream)
            try:

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4677832016
                __attrs_4677832016 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4677841552
                __default_4677841552 = _DEFAULT_MARKER

                # <Value 'view/render_footer_portlets' (3:32)> -> __cache_4677830544
                __token = 76
                try:
                    __zt_tmp = __attrs_4677832016
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4677830544 = _static_4662095120('path', 'view/render_footer_portlets', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/render_footer_portlets' (3:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116d20550> -> __condition
                __expression = __cache_4677830544

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div ></div>')
                else:
                    __content = __cache_4677830544
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            except (Exception, ) as __exc:
                econtext['error'] = _ErrorInfo(__exc, __tokens[__token][1:3])
                if (on_error_handler is not None):
                    on_error_handler(__exc)
                del __stream[____fallback_4659653808:]

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div >')

                # <Value 'nothing' (4:23)> -> __content
                __token = 128
                try:
                    __zt_tmp = __attrs_4676768080
                except get('NameError', NameError):
                    __zt_tmp = None

                __content = _static_4662095120('path', 'nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
                __append('</div>')

            __append('\n  </div>\n</div>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }