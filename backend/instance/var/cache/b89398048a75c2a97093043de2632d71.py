# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/sections.pt'

__tokens = {218: ('python:view.navtree', 4, 29), 369: ('python:view.render_globalnav()', 11, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878789424 = {'class': 'navbar-toggler-icon', }
_static_4878784768 = {'class': 'navbar-toggler', 'aria-label': 'Toggle navigation', 'type': 'button', }
_static_4878782368 = {'class': 'navbar-nav', 'id': 'portal-globalnav', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4653417168
            __attrs_4653417168 = _static_4659865408

            # <Value 'python:view.navtree' (4:29)> -> __condition
            __token = 218
            try:
                __zt_tmp = __attrs_4653417168
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('python', 'view.navtree', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4670200272 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x122cc4fa0> name=None at 1165db710> -> __attrs_4670197072
                __attrs_4670197072 = _static_4878782368

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="navbar-nav" id="portal-globalnav" >\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4673672976
                __attrs_4673672976 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673676240
                __default_4673676240 = _DEFAULT_MARKER

                # <Value 'python:view.render_globalnav()' (11:36)> -> __cache_4684647376
                __token = 369
                try:
                    __zt_tmp = __attrs_4673672976
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4684647376 = _static_4662095120('python', 'view.render_globalnav()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:view.render_globalnav()' (11:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116928f90> -> __condition
                __expression = __cache_4684647376

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <navtree ... (0:0)
                    # --------------------------------------------------------
                    __append('<navtree></navtree>')
                else:
                    __content = __cache_4684647376
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </ul>\n\n  ')

                # <Static value=<ast.Dict object at 0x122cc5900> name=None at 11722fad0> -> __attrs_4390666832
                __attrs_4390666832 = _static_4878784768

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="navbar-toggler"')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4390672720
                __default_4390672720 = _DEFAULT_MARKER

                # <Translate msgid='label_toggle_navigation' node=<ast.Constant object at 0x122cc62f0> at 1172636d0> -> __attr_aria_label
                __attr_aria_label = 'Toggle navigation'
                __attr_aria_label = translate('label_toggle_navigation', default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' type="button" >\n    ')

                # <Static value=<ast.Dict object at 0x122cc6b30> name=None at 1156f0790> -> __attrs_4684094672
                __attrs_4684094672 = _static_4878789424

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="navbar-toggler-icon"></span>\n  </button>\n\n')
                __i18n_domain = __previous_i18n_domain_4670200272
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }