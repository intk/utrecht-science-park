# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/nextprevious/links.pt'

__tokens = {181: ('view/enabled|nothing', 5, 15), 224: (' view/isViewTemplate|nothin', 6, 21), 281: ('python:enabled and isViewTemplate', 8, 20), 455: ('view/previous', 16, 19), 503: ('previous', 18, 23), 553: ('previous/url', 20, 15), 738: ('view/next', 29, 15), 782: ('next', 31, 23), 828: ('next/url', 33, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878928960 = {'href': '', 'rel': 'next', 'title': 'Go to next item', }
_static_4878933520 = {'href': '', 'rel': 'previous', 'title': 'Go to previous item', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878935056 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x122cea410> name=None at 116762fd0> -> __attrs_4684644752
            __attrs_4684644752 = _static_4878935056
            __backup_enabled_4873380064 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (5:15)> -> __value
            __token = 181
            try:
                __zt_tmp = __attrs_4684644752
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/enabled|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_4878544432 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (6:21)> -> __value
            __token = 224
            try:
                __zt_tmp = __attrs_4684644752
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (8:20)> -> __condition
            __token = 281
            try:
                __zt_tmp = __attrs_4684644752
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('python', 'enabled and isViewTemplate', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x122ce9e10> name=None at 116706990> -> __attrs_4684327440
                __attrs_4684327440 = _static_4878933520
                __backup_previous_4878367568 = get('previous', __marker)

                # <Value 'view/previous' (16:19)> -> __value
                __token = 455
                try:
                    __zt_tmp = __attrs_4684327440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/previous', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'previous' (18:23)> -> __condition
                __token = 503
                try:
                    __zt_tmp = __attrs_4684327440
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'previous', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append('<link')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670361360
                    __default_4670361360 = _DEFAULT_MARKER

                    # <Substitution 'previous/url' (20:15)> -> __attr_href
                    __token = 553
                    try:
                        __zt_tmp = __attrs_4684327440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('path', 'previous/url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="previous"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684321680
                    __default_4684321680 = _DEFAULT_MARKER

                    # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x122ce8760> at 1173500d0> -> __attr_title
                    __attr_title = 'Go to previous item'
                    __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                if (__backup_previous_4878367568 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_4878367568
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x122ce8c40> name=None at 117352890> -> __attrs_4686233104
                __attrs_4686233104 = _static_4878928960
                __backup_next_4878367856 = get('next', __marker)

                # <Value 'view/next' (29:15)> -> __value
                __token = 738
                try:
                    __zt_tmp = __attrs_4686233104
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/next', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['next'] = __value

                # <Value 'next' (31:23)> -> __condition
                __token = 782
                try:
                    __zt_tmp = __attrs_4686233104
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'next', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append('<link')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684330064
                    __default_4684330064 = _DEFAULT_MARKER

                    # <Substitution 'next/url' (33:15)> -> __attr_href
                    __token = 828
                    try:
                        __zt_tmp = __attrs_4686233104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('path', 'next/url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="next"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686231696
                    __default_4686231696 = _DEFAULT_MARKER

                    # <Translate msgid='title_next_item' node=<ast.Constant object at 0x122cea830> at 117521510> -> __attr_title
                    __attr_title = 'Go to next item'
                    __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                if (__backup_next_4878367856 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_4878367856
                __append('\n\n')
            if (__backup_isViewTemplate_4878544432 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_4878544432
            if (__backup_enabled_4873380064 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_4873380064
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }