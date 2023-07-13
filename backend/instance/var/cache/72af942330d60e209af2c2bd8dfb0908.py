# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/contentviews.pt'

__tokens = {61: ('context/@@plone', 2, 30), 131: ('ploneview/showToolbar', 4, 33), 240: ('view/tabSet1', 9, 23), 302: ('python: view.menu_template(actions=actions)', 11, 32), 459: ('provider:plone.contentmenu', 17, 34), 606: ('view/tabSet2', 23, 27), 676: ('python: view.menu_template(actions=actions)', 25, 36)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4873512528 = {'class': 'border-top my-2', }
_static_4873508352 = {'class': 'border-top my-2', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4682970192
            __attrs_4682970192 = _static_4659865408
            __backup_ploneview_4878780352 = get('ploneview', __marker)

            # <Value 'context/@@plone' (2:30)> -> __value
            __token = 61
            try:
                __zt_tmp = __attrs_4682970192
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'context/@@plone', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value 'ploneview/showToolbar' (4:33)> -> __condition
            __token = 131
            try:
                __zt_tmp = __attrs_4682970192
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'ploneview/showToolbar', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4690420624 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690421328
                __attrs_4690421328 = _static_4659865408
                __backup_actions_4878325968 = get('actions', __marker)

                # <Value 'view/tabSet1' (9:23)> -> __value
                __token = 240
                try:
                    __zt_tmp = __attrs_4690421328
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/tabSet1', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690420880
                __attrs_4690420880 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4690423696
                __default_4690423696 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (11:32)> -> __cache_4690417680
                __token = 302
                try:
                    __zt_tmp = __attrs_4690420880
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4690417680 = _static_4662095120('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (11:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117922990> -> __condition
                __expression = __cache_4690417680

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_4690417680
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
                if (__backup_actions_4878325968 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_4878325968
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x1227bd600> name=None at 1179235d0> -> __attrs_4690420432
                __attrs_4690420432 = _static_4873508352

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2">\n\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4654639056
                __attrs_4654639056 = _static_4659865408
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4668554448
                __attrs_4668554448 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4668554640
                __default_4668554640 = _DEFAULT_MARKER

                # <Value 'provider:plone.contentmenu' (17:34)> -> __cache_4675191888
                __token = 459
                try:
                    __zt_tmp = __attrs_4668554448
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4675191888 = _static_4662095120('provider', 'plone.contentmenu', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.contentmenu' (17:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116a9f7d0> -> __condition
                __expression = __cache_4675191888

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_4675191888
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    \n\n    ')

                # <Static value=<ast.Dict object at 0x1227be650> name=None at 117921210> -> __attrs_4671320336
                __attrs_4671320336 = _static_4873512528

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2">\n\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676680848
                __attrs_4676680848 = _static_4659865408
                __backup_actions_4878443680 = get('actions', __marker)

                # <Value 'view/tabSet2' (23:27)> -> __value
                __token = 606
                try:
                    __zt_tmp = __attrs_4676680848
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/tabSet2', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4672438608
                __attrs_4672438608 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4676094032
                __default_4676094032 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (25:36)> -> __cache_4676105936
                __token = 676
                try:
                    __zt_tmp = __attrs_4672438608
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4676105936 = _static_4662095120('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (25:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116b78ed0> -> __condition
                __expression = __cache_4676105936

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_4676105936
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')
                if (__backup_actions_4878443680 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_4878443680
                __append('\n\n    </li></li>')
                __i18n_domain = __previous_i18n_domain_4690420624
            if (__backup_ploneview_4878780352 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_4878780352
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }