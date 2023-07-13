# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/path_bar.pt'

__tokens = {96: ('python:view.breadcrumbs', 5, 19), 292: ('${python:view.navigation_root_url}', 12, 43), 294: ('python:view.navigation_root_url', 12, 45), 423: ('breadcrumbs', 15, 34), 500: ('not: repeat/crumb/end', 17, 27), 541: ("${python:crumb['absolute_url']}", 18, 18), 543: ("python:crumb['absolute_url']", 18, 20), 574: ("${python:crumb['Title']}", 18, 51), 576: ("python:crumb['Title']", 18, 53), 710: ('repeat/crumb/end', 21, 27), 737: ("${python:crumb['Title']}", 22, 9), 739: ("python:crumb['Title']", 22, 11)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4873510608 = {'class': 'breadcrumb-item active', 'aria-current': 'page', }
_static_4873511040 = {'href': "${python:crumb['absolute_url']}", }
_static_4873511376 = {'class': 'breadcrumb-item', }
_static_4659865408 = {}
_static_4873516560 = {'href': '${python:view.navigation_root_url}', }
_static_4873519008 = {'class': 'breadcrumb-item', }
_static_4873507872 = {'class': 'breadcrumb', }
_static_4873506672 = {'class': 'container', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4873514688 = {'id': 'portal-breadcrumbs', 'aria-label': 'breadcrumb', 'label_breadcrumb': 'label_breadcrumb', }

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
            __append('\n')

            # <Static value=<ast.Dict object at 0x1227beec0> name=None at 116ad5c90> -> __attrs_4675427536
            __attrs_4675427536 = _static_4873514688
            __backup_breadcrumbs_4878788128 = get('breadcrumbs', __marker)

            # <Value 'python:view.breadcrumbs' (5:19)> -> __value
            __token = 96
            try:
                __zt_tmp = __attrs_4675427536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'view.breadcrumbs', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['breadcrumbs'] = __value
            __previous_i18n_domain_4675424464 = __i18n_domain
            __i18n_domain = 'plone'

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav id="portal-breadcrumbs" aria-label="breadcrumb"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4675428240
            __default_4675428240 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x1227bfd90> at 116ad5f10> -> __attr_label_breadcrumb
            __attr_label_breadcrumb = 'label_breadcrumb'
            __attr_label_breadcrumb = translate(__attr_label_breadcrumb, default=__attr_label_breadcrumb, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_label_breadcrumb is not None):
                __append((' label_breadcrumb="%s"' % __attr_label_breadcrumb))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x1227bcf70> name=None at 1164507d0> -> __attrs_4674168336
            __attrs_4674168336 = _static_4873506672

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container">\n    ')

            # <Static value=<ast.Dict object at 0x1227bd420> name=None at 1169a0a50> -> __attrs_4683064080
            __attrs_4683064080 = _static_4873507872

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append('<ol class="breadcrumb">\n      ')

            # <Static value=<ast.Dict object at 0x1227bffa0> name=None at 1169282d0> -> __attrs_4668656208
            __attrs_4668656208 = _static_4873519008

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li class="breadcrumb-item">')

            # <Static value=<ast.Dict object at 0x1227bf610> name=None at 1164d6c10> -> __attrs_4664383568
            __attrs_4664383568 = _static_4873516560

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4664384336
            __default_4664384336 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python:view.navigation_root_url}' (12:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11708db90> -> __attr_href
            __token = 292
            __token = 294
            try:
                __zt_tmp = __attrs_4664383568
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4662095120('python', 'view.navigation_root_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')
            __stream_4683246224 = []
            __append_4683246224 = __stream_4683246224.append
            __append_4683246224('Home')
            __msgid_4683246224 = __re_whitespace(''.join(__stream_4683246224)).strip()
            if 'tabs_home':
                __append(translate('tabs_home', mapping=None, default=__msgid_4683246224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a></li>\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4390671824
            __attrs_4390671824 = _static_4659865408
            __backup_crumb_4878700448 = get('crumb', __marker)

            # <Value 'breadcrumbs' (15:34)> -> __iterator
            __token = 423
            try:
                __zt_tmp = __attrs_4390671824
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4662095120('path', 'breadcrumbs', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            (__iterator, ____index_4664380688, ) = getname('repeat')('crumb', __iterator)
            econtext['crumb'] = None
            for __item in __iterator:
                econtext['crumb'] = __item
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x1227be1d0> name=None at 105b44250> -> __attrs_4671183952
                __attrs_4671183952 = _static_4873511376

                # <Value 'not: repeat/crumb/end' (17:27)> -> __condition
                __token = 500
                try:
                    __zt_tmp = __attrs_4671183952
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('not', ' repeat/crumb/end', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item" >')

                    # <Static value=<ast.Dict object at 0x1227be080> name=None at 1166c9a90> -> __attrs_4686097424
                    __attrs_4686097424 = _static_4873511040

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686099408
                    __default_4686099408 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:crumb['absolute_url']}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117500310> -> __attr_href
                    __token = 541
                    __token = 543
                    try:
                        __zt_tmp = __attrs_4686097424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('python', "crumb['absolute_url']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = __attr_href
                    if (__attr_href is None):
                        pass
                    else:
                        if (__attr_href is _DEFAULT_MARKER):
                            __attr_href = None
                        else:
                            __tt = type(__attr_href)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_href = str(__attr_href)
                            else:
                                if (__tt is bytes):
                                    __attr_href = decode(__attr_href)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_href = __attr_href.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_href)
                                            __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                        else:
                                            __attr_href = __attr_href()
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (18:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117510790> -> __content_4386234736
                    __token = 574
                    __token = 576
                    try:
                        __zt_tmp = __attrs_4686097424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4386234736 = _static_4662095120('python', "crumb['Title']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                    __append('</a></li>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x1227bded0> name=None at 1175101d0> -> __attrs_4677717776
                __attrs_4677717776 = _static_4873510608

                # <Value 'repeat/crumb/end' (21:27)> -> __condition
                __token = 710
                try:
                    __zt_tmp = __attrs_4677717776
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'repeat/crumb/end', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item active" aria-current="page" >')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (22:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116d05090> -> __content_4386234736
                    __token = 737
                    __token = 739
                    try:
                        __zt_tmp = __attrs_4677717776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4386234736 = _static_4662095120('python', "crumb['Title']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                    __append('</li>')
                __append('\n      ')
                ____index_4664380688 -= 1
                if (____index_4664380688 > 0):
                    __append('')
            if (__backup_crumb_4878700448 is __marker):
                del econtext['crumb']
            else:
                econtext['crumb'] = __backup_crumb_4878700448
            __append('\n    </ol>\n  </div>\n</nav>')
            __i18n_domain = __previous_i18n_domain_4675424464
            if (__backup_breadcrumbs_4878788128 is __marker):
                del econtext['breadcrumbs']
            else:
                econtext['breadcrumbs'] = __backup_breadcrumbs_4878788128
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }