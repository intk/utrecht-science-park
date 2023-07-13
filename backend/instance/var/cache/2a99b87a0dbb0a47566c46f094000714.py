# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/anontools.pt'

__tokens = {47: ('python:view.user_actions and view.anonymous', 2, 20), 181: ('view/user_actions', 6, 27), 296: ('action', 11, 11), 245: ('action/title', 9, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878821904 = set([])
_static_4878826896 = {'href': '', }
_static_4878826080 = {'class': 'list-inline-item', }
_static_4878825360 = {'class': 'list-inline', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878812928 = {'id': 'portal-anontools', }

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

            # <Static value=<ast.Dict object at 0x122ccc700> name=None at 116667350> -> __attrs_4689446736
            __attrs_4689446736 = _static_4878812928

            # <Value 'python:view.user_actions and view.anonymous' (2:20)> -> __condition
            __token = 47
            try:
                __zt_tmp = __attrs_4689446736
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('python', 'view.user_actions and view.anonymous', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="portal-anontools" >\n  ')

                # <Static value=<ast.Dict object at 0x122ccf790> name=None at 1179e3c50> -> __attrs_4691202320
                __attrs_4691202320 = _static_4878825360

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="list-inline">\n    ')

                # <Static value=<ast.Dict object at 0x122ccfa60> name=None at 1179e2d90> -> __attrs_4691202512
                __attrs_4691202512 = _static_4878826080
                __backup_action_4878250528 = get('action', __marker)

                # <Value 'view/user_actions' (6:27)> -> __iterator
                __token = 181
                try:
                    __zt_tmp = __attrs_4691202512
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'view/user_actions', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4691200272, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-inline-item" >\n      ')

                    # <Static value=<ast.Dict object at 0x122ccfd90> name=None at 117a5a650> -> __attrs_4691692368
                    __attrs_4691692368 = _static_4878826896

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Value 'action' (11:11)> -> __cache_4691691344
                    __token = 296
                    try:
                        __zt_tmp = __attrs_4691692368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4691691344 = _static_4662095120('path', 'action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if ('href' not in __chain(__cache_4691691344)):
                        __append(' href=""')
                    __attr_4691691152 = __cache_4691691344
                    for (name, value, ) in __attr_4691691152.items():
                        if ((name not in _static_4878821904) and (value is not None)):
                            __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4677569104
                    __default_4677569104 = _DEFAULT_MARKER

                    # <Value 'action/title' (9:22)> -> __cache_4691200592
                    __token = 245
                    try:
                        __zt_tmp = __attrs_4691692368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4691200592 = _static_4662095120('path', 'action/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/title' (9:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11729cbd0> -> __condition
                    __expression = __cache_4691200592

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n          action title\n      ')
                    else:
                        __content = __cache_4691200592
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n    </li>')
                    ____index_4691200272 -= 1
                    if (____index_4691200272 > 0):
                        __append('\n    ')
                if (__backup_action_4878250528 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_4878250528
                __append('\n  </ul>\n</div>')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }