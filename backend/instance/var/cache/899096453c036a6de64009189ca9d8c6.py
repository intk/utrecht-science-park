# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/contenttypes/browser/templates/document.pt'

__tokens = {519: ("python:  getattr(context, 'table_of_contents', False)", 15, 32), 781: ("python:getattr(context, 'text', None)", 22, 30), 669: ("${python: toc and 'pat-autotoc' or ''}", 20, 22), 671: ("python: toc and 'pat-autotoc' or ''", 20, 24), 858: ('python:context.text.output_relative_to(view.context)', 23, 38), 247: ('context/@@main_template/macros/master', 6, 23), 247: ('context/@@main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878547504 = 'master'
_static_4878542560 = {'class': "${python: toc and 'pat-autotoc' or ''}", 'id': 'parent-fieldname-text', }
_static_4878541936 = {'id': 'section-text', }
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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674274512
            __attrs_4674274512 = _static_4659865408
            __backup_toc_4868539152 = get('toc', __marker)

            # <Value "python:  getattr(context, 'table_of_contents', False)" (15:32)> -> __value
            __token = 519
            try:
                __zt_tmp = __attrs_4674274512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "  getattr(context, 'table_of_contents', False)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['toc'] = __value
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x122c8a470> name=None at 1169bd1d0> -> __attrs_4674275344
            __attrs_4674275344 = _static_4878541936

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="section-text">\n          ')

            # <Static value=<ast.Dict object at 0x122c8a6e0> name=None at 1169be2d0> -> __attrs_4686459792
            __attrs_4686459792 = _static_4878542560

            # <Value "python:getattr(context, 'text', None)" (22:30)> -> __condition
            __token = 781
            try:
                __zt_tmp = __attrs_4686459792
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('python', "getattr(context, 'text', None)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686457744
                __default_4686457744 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution "${python: toc and 'pat-autotoc' or ''}" (20:22)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1169bfa50> -> __attr_class
                __token = 669
                __token = 671
                try:
                    __zt_tmp = __attrs_4686459792
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_4662095120('python', " toc and 'pat-autotoc' or ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_class = __attr_class
                if (__attr_class is None):
                    pass
                else:
                    if (__attr_class is _DEFAULT_MARKER):
                        __attr_class = None
                    else:
                        __tt = type(__attr_class)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_class = str(__attr_class)
                        else:
                            if (__tt is bytes):
                                __attr_class = decode(__attr_class)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_class = __attr_class.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_class)
                                        __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                    else:
                                        __attr_class = __attr_class()
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))
                __append(' id="parent-fieldname-text" >')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674283216
                __default_4674283216 = _DEFAULT_MARKER

                # <Value 'python:context.text.output_relative_to(view.context)' (23:38)> -> __cache_4674287120
                __token = 858
                try:
                    __zt_tmp = __attrs_4686459792
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4674287120 = _static_4662095120('python', 'context.text.output_relative_to(view.context)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:context.text.output_relative_to(view.context)' (23:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11731bc10> -> __condition
                __expression = __cache_4674287120

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      Text\n          ')
                else:
                    __content = __cache_4674287120
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            __append('\n        </section>\n\n      ')
            if (__backup_toc_4868539152 is __marker):
                del econtext['toc']
            else:
                econtext['toc'] = __backup_toc_4868539152
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684087632
            __attrs_4684087632 = _static_4659865408
            __previous_i18n_domain_4671060304 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4684094144 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x122c8ba30> name=None at 115645290> -> __value
            __value = _static_4878547504
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4663383376
                __attrs_4663383376 = _static_4659865408
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/@@main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_4684087632
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4662095120('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4684094144 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4684094144
            __i18n_domain = __previous_i18n_domain_4671060304
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }