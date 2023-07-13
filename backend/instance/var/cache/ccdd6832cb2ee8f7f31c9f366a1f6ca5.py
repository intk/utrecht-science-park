# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/portlets/portlets/classic.pt'

__tokens = {47: ('view/use_macro', 2, 23), 91: (' view/path_expressio', 3, 28), 153: ('use_macro', 6, 24), 199: ('python:path(path_expression)', 7, 34), 199: ('python:path(path_expression)', 7, 34), 272: ('not:use_macro', 10, 24), 320: ('python:path(path_expression)', 11, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878241888 = 'python:path(path_expression)'
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4664385872
            __attrs_4664385872 = _static_4659865408
            __backup_use_macro_4878360656 = get('use_macro', __marker)

            # <Value 'view/use_macro' (2:23)> -> __value
            __token = 47
            try:
                __zt_tmp = __attrs_4664385872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/use_macro', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['use_macro'] = __value
            __backup_path_expression_4878367328 = get('path_expression', __marker)

            # <Value 'view/path_expression' (3:28)> -> __value
            __token = 91
            try:
                __zt_tmp = __attrs_4664385872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/path_expression', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['path_expression'] = __value
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690952464
            __attrs_4690952464 = _static_4659865408

            # <Value 'use_macro' (6:24)> -> __condition
            __token = 153
            try:
                __zt_tmp = __attrs_4690952464
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'use_macro', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4681583568
                __attrs_4681583568 = _static_4659865408
                __backup_macroname_4674341632 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x122c41060> name=None at 117763c90> -> __value
                __value = _static_4878241888
                econtext['macroname'] = __value

                # <Value 'python:path(path_expression)' (7:34)> -> __macro
                __token = 199
                try:
                    __zt_tmp = __attrs_4681583568
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4662095120('python', 'path(path_expression)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __token = 199
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4674341632 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4674341632
                __append('\n  ')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4681590864
            __attrs_4681590864 = _static_4659865408

            # <Value 'not:use_macro' (10:24)> -> __condition
            __token = 272
            try:
                __zt_tmp = __attrs_4681590864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('not', 'use_macro', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4681582608
                __attrs_4681582608 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681588816
                __default_4681588816 = _DEFAULT_MARKER

                # <Value 'python:path(path_expression)' (11:32)> -> __cache_4681589584
                __token = 320
                try:
                    __zt_tmp = __attrs_4681582608
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4681589584 = _static_4662095120('python', 'path(path_expression)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:path(path_expression)' (11:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1170b6e50> -> __condition
                __expression = __cache_4681589584

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_4681589584
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
            __append('\n\n')
            if (__backup_path_expression_4878367328 is __marker):
                del econtext['path_expression']
            else:
                econtext['path_expression'] = __backup_path_expression_4878367328
            if (__backup_use_macro_4878360656 is __marker):
                del econtext['use_macro']
            else:
                econtext['use_macro'] = __backup_use_macro_4878360656
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }