# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/portlets/browser/templates/column.pt'

__tokens = {27: ('options/portlets', 1, 27), 188: ('string:portletwrapper-${portlet/hash}', 5, 12), 252: (' portlet/has', 6, 25), 106: ("python:view.safe_render(portlet['renderer'])", 3, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4873379008 = {'class': 'portletWrapper', 'id': 'string:portletwrapper-${portlet/hash}', 'data-portlethash': 'portlet/hash', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674174032
            __attrs_4674174032 = _static_4659865408
            __backup_portlet_4878769872 = get('portlet', __marker)

            # <Value 'options/portlets' (1:27)> -> __iterator
            __token = 27
            try:
                __zt_tmp = __attrs_4674174032
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4662095120('path', 'options/portlets', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            (__iterator, ____index_4674168656, ) = getname('repeat')('portlet', __iterator)
            econtext['portlet'] = None
            for __item in __iterator:
                econtext['portlet'] = __item
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x12279dcc0> name=None at 1166b0410> -> __attrs_4681591888
                __attrs_4681591888 = _static_4873379008

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portletWrapper"')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681580944
                __default_4681580944 = _DEFAULT_MARKER

                # <Substitution 'string:portletwrapper-${portlet/hash}' (5:12)> -> __attr_id
                __token = 188
                try:
                    __zt_tmp = __attrs_4681591888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_4662095120('string', 'portletwrapper-${portlet/hash}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681595472
                __default_4681595472 = _DEFAULT_MARKER

                # <Substitution 'portlet/hash' (6:25)> -> __attr_data_portlethash
                __token = 252
                try:
                    __zt_tmp = __attrs_4681591888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_portlethash = _static_4662095120('path', 'portlet/hash', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_data_portlethash = __quote(__attr_data_portlethash, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_portlethash is not None):
                    __append((' data-portlethash="%s"' % __attr_data_portlethash))
                __append(' >')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671081744
                __default_4671081744 = _DEFAULT_MARKER

                # <Value "python:view.safe_render(portlet['renderer'])" (3:30)> -> __cache_4674159696
                __token = 106
                try:
                    __zt_tmp = __attrs_4681591888
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4674159696 = _static_4662095120('python', "view.safe_render(portlet['renderer'])", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value "python:view.safe_render(portlet['renderer'])" (3:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1169a1810> -> __condition
                __expression = __cache_4674159696

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4674159696
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n')
                ____index_4674168656 -= 1
                if (____index_4674168656 > 0):
                    __append('')
            if (__backup_portlet_4878769872 is __marker):
                del econtext['portlet']
            else:
                econtext['portlet'] = __backup_portlet_4878769872
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }