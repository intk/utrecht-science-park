# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/globalstatusmessage.pt'

__tokens = {51: ('nocall: context/@@iconresolver', 2, 23), 135: ('python:view.messages', 4, 35), 279: ('message/type | nothing', 10, 15), 324: (' python:view.display_info_for_mtype(mtype', 11, 21), 399: ('mtype', 13, 22), 174: ("portalMessage ${python:display_info['cssclass']}", 7, 14), 190: ("python:display_info['cssclass']", 7, 30), 447: ("python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')", 15, 37), 573: ("${python:display_info['msg']}", 16, 12), 575: ("python:display_info['msg']", 16, 14), 661: ('message/message | nothing', 18, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878700736 = {'class': 'content', }
_static_4878700688 = {'class': "portalMessage ${python:display_info['cssclass']}", 'role': 'alert', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4668475792
            __attrs_4668475792 = _static_4659865408
            __backup_icons_4878233136 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (2:23)> -> __value
            __token = 51
            try:
                __zt_tmp = __attrs_4668475792
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', ' context/@@iconresolver', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_message_4878781696 = get('message', __marker)

            # <Value 'python:view.messages' (4:35)> -> __iterator
            __token = 135
            try:
                __zt_tmp = __attrs_4668475792
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4662095120('python', 'view.messages', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            (__iterator, ____index_4668481808, ) = getname('repeat')('message', __iterator)
            econtext['message'] = None
            for __item in __iterator:
                econtext['message'] = __item
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x122cb1090> name=None at 116435990> -> __attrs_4689244880
                __attrs_4689244880 = _static_4878700688
                __backup_mtype_4878439600 = get('mtype', __marker)

                # <Value 'message/type | nothing' (10:15)> -> __value
                __token = 279
                try:
                    __zt_tmp = __attrs_4689244880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'message/type | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['mtype'] = __value
                __backup_display_info_4878366032 = get('display_info', __marker)

                # <Value 'python:view.display_info_for_mtype(mtype)' (11:21)> -> __value
                __token = 324
                try:
                    __zt_tmp = __attrs_4689244880
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', 'view.display_info_for_mtype(mtype)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['display_info'] = __value

                # <Value 'mtype' (13:22)> -> __condition
                __token = 399
                try:
                    __zt_tmp = __attrs_4689244880
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'mtype', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4668476880
                    __default_4668476880 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "portalMessage ${python:display_info['cssclass']}" (7:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1164374d0> -> __attr_class
                    __token = 174
                    __token = 190
                    try:
                        __zt_tmp = __attrs_4689244880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4662095120('python', "display_info['cssclass']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('portalMessage ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append(' role="alert" >\n    ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689238224
                    __attrs_4689238224 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689246608
                    __default_4689246608 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')" (15:37)> -> __cache_4689244688
                    __token = 447
                    try:
                        __zt_tmp = __attrs_4689238224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4689244688 = _static_4662095120('python', "icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(display_info['icon'], tag_alt=display_info['msg'], tag_class='statusmessage-icon mb-1 me-2')" (15:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117802090> -> __condition
                    __expression = __cache_4689244688

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4689244688
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670717904
                    __attrs_4670717904 = _static_4659865408

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')

                    # <Interpolation value=<Substitution "${python:display_info['msg']}" (16:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1165e7150> -> __content_4386234736
                    __token = 573
                    __token = 575
                    try:
                        __zt_tmp = __attrs_4670717904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4386234736 = _static_4662095120('python', "display_info['msg']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __content_4386234736 = __quote(__content_4386234736, '\x00', '&#0;', None, None)
                    __content_4386234736 = __content_4386234736
                    if (__content_4386234736 is None):
                        pass
                    else:
                        if (__content_4386234736 is None):
                            __content_4386234736 = None
                        else:
                            __tt = type(__content_4386234736)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_4386234736 = str(__content_4386234736)
                            else:
                                if (__tt is bytes):
                                    __content_4386234736 = decode(__content_4386234736)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_4386234736 = __content_4386234736.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_4386234736)
                                            __content_4386234736 = (str(__content_4386234736) if (__content_4386234736 is __converted) else __converted)
                                        else:
                                            __content_4386234736 = __content_4386234736()
                    if (__content_4386234736 is not None):
                        __append(__content_4386234736)
                    __append('</strong>\n    ')

                    # <Static value=<ast.Dict object at 0x122cb10c0> name=None at 1165e5f50> -> __attrs_4390672400
                    __attrs_4390672400 = _static_4878700736

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4390669520
                    __default_4390669520 = _DEFAULT_MARKER

                    # <Value 'message/message | nothing' (18:23)> -> __cache_4671186256
                    __token = 661
                    try:
                        __zt_tmp = __attrs_4390672400
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4671186256 = _static_4662095120('path', 'message/message | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'message/message | nothing' (18:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 105b45350> -> __condition
                    __expression = __cache_4671186256

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="content" >\n            The status message.\n    </span>')
                    else:
                        __content = __cache_4671186256
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n  </div>')
                if (__backup_display_info_4878366032 is __marker):
                    del econtext['display_info']
                else:
                    econtext['display_info'] = __backup_display_info_4878366032
                if (__backup_mtype_4878439600 is __marker):
                    del econtext['mtype']
                else:
                    econtext['mtype'] = __backup_mtype_4878439600
                __append('\n\n')
                ____index_4668481808 -= 1
                if (____index_4668481808 > 0):
                    __append('')
            if (__backup_message_4878781696 is __marker):
                del econtext['message']
            else:
                econtext['message'] = __backup_message_4878781696
            if (__backup_icons_4878233136 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4878233136
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }