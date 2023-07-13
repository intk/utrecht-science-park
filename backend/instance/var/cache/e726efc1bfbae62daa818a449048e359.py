# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/i18n/locales/browser/languageselector.pt'

__tokens = {29: ('view/available', 1, 29), 118: ('view/showFlags', 4, 18), 151: (' view/language', 5, 17), 183: ('l context/@@plone_context_state/view_u', 6, 15), 241: ('rl view/portal_', 7, 16), 271: ("ons python:context.restrictedTraverse('@@iconresolv", 8, 10), 371: ('languages', 11, 31), 423: ('lang/code', 13, 17), 454: (' lang/selecte', 14, 20), 490: ('s string:language-${cod', 15, 20), 534: ("nt python: selected and 'currentLanguage ' or", 16, 17), 641: ('string:${current}${codeclass}', 19, 18), 753: ('lang/flag|nothing', 24, 18), 789: (' lang/native|lang/nam', 25, 17), 833: ('g python:showFlags and fl', 26, 20), 921: ('string:${here_url}?set_language=${code}', 29, 18), 980: (' nam', 30, 18), 1041: ('showflag', 33, 31), 1092: ("python:icons.tag(flag, tag_class='plone-icon-flag')", 34, 40), 1204: ('not: showflag', 36, 34), 1251: ('name', 37, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878367520 = {'href': '', 'title': 'name', }
_static_4878353744 = {'class': 'string:${current}${codeclass}', }
_static_4878357968 = {'id': 'portal-languageselector', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675201552
            __attrs_4675201552 = _static_4659865408

            # <Value 'view/available' (1:29)> -> __condition
            __token = 29
            try:
                __zt_tmp = __attrs_4675201552
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'view/available', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x122c5d5d0> name=None at 116a9d4d0> -> __attrs_4675400656
                __attrs_4675400656 = _static_4878357968
                __backup_showFlags_4878124080 = get('showFlags', __marker)

                # <Value 'view/showFlags' (4:18)> -> __value
                __token = 118
                try:
                    __zt_tmp = __attrs_4675400656
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/showFlags', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['showFlags'] = __value
                __backup_languages_4878780880 = get('languages', __marker)

                # <Value 'view/languages' (5:17)> -> __value
                __token = 151
                try:
                    __zt_tmp = __attrs_4675400656
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/languages', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['languages'] = __value
                __backup_here_url_4878448864 = get('here_url', __marker)

                # <Value 'context/@@plone_context_state/view_url' (6:15)> -> __value
                __token = 183
                try:
                    __zt_tmp = __attrs_4675400656
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'context/@@plone_context_state/view_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['here_url'] = __value
                __backup_portal_url_4878814896 = get('portal_url', __marker)

                # <Value 'view/portal_url' (7:16)> -> __value
                __token = 241
                try:
                    __zt_tmp = __attrs_4675400656
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/portal_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __backup_icons_4878833488 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (8:10)> -> __value
                __token = 271
                try:
                    __zt_tmp = __attrs_4675400656
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['icons'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul id="portal-languageselector" >\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675390416
                __attrs_4675390416 = _static_4659865408
                __backup_lang_4878233904 = get('lang', __marker)

                # <Value 'languages' (11:31)> -> __iterator
                __token = 371
                try:
                    __zt_tmp = __attrs_4675390416
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'languages', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4675389648, ) = getname('repeat')('lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x122c5c550> name=None at 116434e90> -> __attrs_4689733456
                    __attrs_4689733456 = _static_4878353744
                    __backup_code_4878251920 = get('code', __marker)

                    # <Value 'lang/code' (13:17)> -> __value
                    __token = 423
                    try:
                        __zt_tmp = __attrs_4689733456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'lang/code', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['code'] = __value
                    __backup_selected_4878333552 = get('selected', __marker)

                    # <Value 'lang/selected' (14:20)> -> __value
                    __token = 454
                    try:
                        __zt_tmp = __attrs_4689733456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'lang/selected', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __backup_codeclass_4878597760 = get('codeclass', __marker)

                    # <Value 'string:language-${code}' (15:20)> -> __value
                    __token = 490
                    try:
                        __zt_tmp = __attrs_4689733456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('string', 'language-${code}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['codeclass'] = __value
                    __backup_current_4878319968 = get('current', __marker)

                    # <Value "python: selected and 'currentLanguage ' or ''" (16:17)> -> __value
                    __token = 534
                    try:
                        __zt_tmp = __attrs_4689733456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', " selected and 'currentLanguage ' or ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['current'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4668479952
                    __default_4668479952 = _DEFAULT_MARKER

                    # <Substitution 'string:${current}${codeclass}' (19:18)> -> __attr_class
                    __token = 641
                    try:
                        __zt_tmp = __attrs_4689733456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4662095120('string', '${current}${codeclass}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x122c5fb20> name=None at 116654bd0> -> __attrs_4670126736
                    __attrs_4670126736 = _static_4878367520
                    __backup_flag_4878828256 = get('flag', __marker)

                    # <Value 'lang/flag|nothing' (24:18)> -> __value
                    __token = 753
                    try:
                        __zt_tmp = __attrs_4670126736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'lang/flag|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['flag'] = __value
                    __backup_name_4878365600 = get('name', __marker)

                    # <Value 'lang/native|lang/name' (25:17)> -> __value
                    __token = 789
                    try:
                        __zt_tmp = __attrs_4670126736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'lang/native|lang/name', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['name'] = __value
                    __backup_showflag_4878938896 = get('showflag', __marker)

                    # <Value 'python:showFlags and flag' (26:20)> -> __value
                    __token = 833
                    try:
                        __zt_tmp = __attrs_4670126736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', 'showFlags and flag', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['showflag'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4659145808
                    __default_4659145808 = _DEFAULT_MARKER

                    # <Substitution 'string:${here_url}?set_language=${code}' (29:18)> -> __attr_href
                    __token = 921
                    try:
                        __zt_tmp = __attrs_4670126736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('string', '${here_url}?set_language=${code}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4659136912
                    __default_4659136912 = _DEFAULT_MARKER

                    # <Substitution 'name' (30:18)> -> __attr_title
                    __token = 980
                    try:
                        __zt_tmp = __attrs_4670126736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4662095120('path', 'name', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4677014352
                    __attrs_4677014352 = _static_4659865408

                    # <Value 'showflag' (33:31)> -> __condition
                    __token = 1041
                    try:
                        __zt_tmp = __attrs_4677014352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'showflag', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674971088
                        __attrs_4674971088 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670255504
                        __default_4670255504 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(flag, tag_class='plone-icon-flag')" (34:40)> -> __cache_4674962704
                        __token = 1092
                        try:
                            __zt_tmp = __attrs_4674971088
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4674962704 = _static_4662095120('python', "icons.tag(flag, tag_class='plone-icon-flag')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(flag, tag_class='plone-icon-flag')" (34:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116a64690> -> __condition
                        __expression = __cache_4674962704

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append('<img />')
                        else:
                            __content = __cache_4674962704
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          ')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674973136
                    __attrs_4674973136 = _static_4659865408

                    # <Value 'not: showflag' (36:34)> -> __condition
                    __token = 1204
                    try:
                        __zt_tmp = __attrs_4674973136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('not', ' showflag', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674974800
                        __default_4674974800 = _DEFAULT_MARKER

                        # <Value 'name' (37:32)> -> __cache_4674969360
                        __token = 1251
                        try:
                            __zt_tmp = __attrs_4674973136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4674969360 = _static_4662095120('path', 'name', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'name' (37:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116a65a10> -> __condition
                        __expression = __cache_4674969360

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('language name')
                        else:
                            __content = __cache_4674969360
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n        </a>')
                    if (__backup_showflag_4878938896 is __marker):
                        del econtext['showflag']
                    else:
                        econtext['showflag'] = __backup_showflag_4878938896
                    if (__backup_name_4878365600 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_4878365600
                    if (__backup_flag_4878828256 is __marker):
                        del econtext['flag']
                    else:
                        econtext['flag'] = __backup_flag_4878828256
                    __append('\n      </li>')
                    if (__backup_current_4878319968 is __marker):
                        del econtext['current']
                    else:
                        econtext['current'] = __backup_current_4878319968
                    if (__backup_codeclass_4878597760 is __marker):
                        del econtext['codeclass']
                    else:
                        econtext['codeclass'] = __backup_codeclass_4878597760
                    if (__backup_selected_4878333552 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_4878333552
                    if (__backup_code_4878251920 is __marker):
                        del econtext['code']
                    else:
                        econtext['code'] = __backup_code_4878251920
                    __append('\n    ')
                    ____index_4675389648 -= 1
                    if (____index_4675389648 > 0):
                        __append('')
                if (__backup_lang_4878233904 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_4878233904
                __append('\n  </ul>')
                if (__backup_icons_4878833488 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_4878833488
                if (__backup_portal_url_4878814896 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_4878814896
                if (__backup_here_url_4878448864 is __marker):
                    del econtext['here_url']
                else:
                    econtext['here_url'] = __backup_here_url_4878448864
                if (__backup_languages_4878780880 is __marker):
                    del econtext['languages']
                else:
                    econtext['languages'] = __backup_languages_4878780880
                if (__backup_showFlags_4878124080 is __marker):
                    del econtext['showFlags']
                else:
                    econtext['showFlags'] = __backup_showFlags_4878124080
                __append('\n')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }