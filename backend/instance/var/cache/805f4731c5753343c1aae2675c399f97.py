# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/multilingual/browser/templates/controlpanel.pt'

__tokens = {520: ('string:$portal_url/@@overview-controlpanel', 19, 18), 715: ('view/label', 27, 25), 783: ('context/global_statusmessage/macros/portal_message', 30, 30), 783: ('context/global_statusmessage/macros/portal_message', 30, 30), 999: ('view/contents', 36, 39), 1164: ('string:${context/absolute_url}/multilingual-map', 42, 22), 1488: ('view/isLPinstalled', 50, 28), 1683: ('string:${context/absolute_url}/lp-migration', 55, 22), 247: ('here/prefs_main_template/macros/master', 6, 23), 247: ('here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4897199376 = {'href': 'string:${context/absolute_url}/lp-migration', }
_static_4897205520 = {'href': 'string:${context/absolute_url}/multilingual-map', }
_static_4897195632 = {'class': 'mt-4', }
_static_4897203696 = {'id': 'layout-contents', }
_static_4897206096 = {'id': 'content-core', }
_static_4897204800 = 'portal_message'
_static_4897210032 = {'class': 'documentFirstHeading', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4897201248 = {'class': 'link-parent', 'id': 'setup-link', 'href': 'string:$portal_url/@@overview-controlpanel', }
_static_4897204752 = 'master'
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4867403856
            __attrs_4867403856 = _static_4659865408
            __previous_i18n_domain_4867397264 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4893848640 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x123e56a10> name=None at 1221e9c50> -> __value
            __value = _static_4897204752
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4867391568
                __attrs_4867391568 = _static_4659865408
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4867398672
                __attrs_4867398672 = _static_4659865408

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n        ')

                # <Static value=<ast.Dict object at 0x123e55c60> name=None at 117821610> -> __attrs_4689377808
                __attrs_4689377808 = _static_4897201248

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="link-parent" id="setup-link"')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689365968
                __default_4689365968 = _DEFAULT_MARKER

                # <Substitution 'string:$portal_url/@@overview-controlpanel' (19:18)> -> __attr_href
                __token = 520
                try:
                    __zt_tmp = __attrs_4689377808
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4662095120('string', '$portal_url/@@overview-controlpanel', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')
                __stream_4689363984 = []
                __append_4689363984 = __stream_4689363984.append
                __append_4689363984('\n        Site Setup\n        ')
                __msgid_4689363984 = __re_whitespace(''.join(__stream_4689363984)).strip()
                if __msgid_4689363984:
                    __append(translate(__msgid_4689363984, mapping=None, default=__msgid_4689363984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>\n\n        ')

                # <Static value=<ast.Dict object at 0x123e57eb0> name=None at 116972190> -> __attrs_4894350864
                __attrs_4894350864 = _static_4897210032

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading" >')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689370192
                __default_4689370192 = _DEFAULT_MARKER

                # <Value 'view/label' (27:25)> -> __cache_4689364112
                __token = 715
                try:
                    __zt_tmp = __attrs_4894350864
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4689364112 = _static_4662095120('path', 'view/label', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/label' (27:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1178224d0> -> __condition
                __expression = __cache_4689364112

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('View Title')
                else:
                    __content = __cache_4689364112
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</h1>\n\n        ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4692323664
                __attrs_4692323664 = _static_4659865408
                __backup_macroname_4690853696 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x123e56a40> name=None at 117af1650> -> __value
                __value = _static_4897204800
                econtext['macroname'] = __value

                # <Value 'context/global_statusmessage/macros/portal_message' (30:30)> -> __macro
                __token = 783
                try:
                    __zt_tmp = __attrs_4692323664
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_4662095120('path', 'context/global_statusmessage/macros/portal_message', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __token = 783
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_4690853696 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_4690853696
                __append('\n      </header>\n      ')

                # <Static value=<ast.Dict object at 0x123e56f50> name=None at 1167f6790> -> __attrs_4866670672
                __attrs_4866670672 = _static_4897206096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n        ')

                # <Static value=<ast.Dict object at 0x123e565f0> name=None at 1175b9d50> -> __attrs_4686850000
                __attrs_4686850000 = _static_4897203696

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="layout-contents">\n          ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4868374288
                __attrs_4868374288 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686204944
                __default_4686204944 = _DEFAULT_MARKER

                # <Value 'view/contents' (36:39)> -> __cache_4894506448
                __token = 999
                try:
                    __zt_tmp = __attrs_4868374288
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4894506448 = _static_4662095120('path', 'view/contents', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/contents' (36:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 123bc1190> -> __condition
                __expression = __cache_4894506448

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span></span>')
                else:
                    __content = __cache_4894506448
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n        </div>\n        ')

                # <Static value=<ast.Dict object at 0x123e54670> name=None at 1222d7c50> -> __attrs_4893545168
                __attrs_4893545168 = _static_4897195632

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mt-4">\n          ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4893542864
                __attrs_4893542864 = _static_4659865408

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_4891232512_url = ''
                __stream_4893543440 = []
                __append_4893543440 = __stream_4893543440.append
                __append_4893543440('\n          The\n            ')
                __stream_4891232512_url = []
                __append_4891232512_url = __stream_4891232512_url.append

                # <Static value=<ast.Dict object at 0x123e56d10> name=None at 123adb910> -> __attrs_4893542800
                __attrs_4893542800 = _static_4897205520

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_4891232512_url('<a')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4893546384
                __default_4893546384 = _DEFAULT_MARKER

                # <Substitution 'string:${context/absolute_url}/multilingual-map' (42:22)> -> __attr_href
                __token = 1164
                try:
                    __zt_tmp = __attrs_4893542800
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4662095120('string', '${context/absolute_url}/multilingual-map', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append_4891232512_url((' href="%s"' % __attr_href))
                __append_4891232512_url(' >')
                __stream_4893546960 = []
                __append_4893546960 = __stream_4893546960.append
                __append_4893546960('multilingual map view\n            ')
                __msgid_4893546960 = __re_whitespace(''.join(__stream_4893546960)).strip()
                if __msgid_4893546960:
                    __append_4891232512_url(translate(__msgid_4893546960, mapping=None, default=__msgid_4893546960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_4891232512_url('</a>')
                __append_4893543440('${url}')
                __stream_4891232512_url = ''.join(__stream_4891232512_url)
                __append_4893543440('\n          allows you to view in a graphical manner the already translated items and its relations.\n          ')
                __msgid_4893543440 = __re_whitespace(''.join(__stream_4893543440)).strip()
                if __msgid_4893543440:
                    __append(translate(__msgid_4893543440, mapping={'url': __stream_4891232512_url, }, default=__msgid_4893543440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n          ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4893555792
                __attrs_4893555792 = _static_4659865408

                # <Value 'view/isLPinstalled' (50:28)> -> __condition
                __token = 1488
                try:
                    __zt_tmp = __attrs_4893555792
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'view/isLPinstalled', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p >')
                    __stream_4891232512_url = ''
                    __stream_4893553872 = []
                    __append_4893553872 = __stream_4893553872.append
                    __append_4893553872('\n          In case you want to migrate from Products.LinguaPlone access to the\n            ')
                    __stream_4891232512_url = []
                    __append_4891232512_url = __stream_4891232512_url.append

                    # <Static value=<ast.Dict object at 0x123e55510> name=None at 123a78910> -> __attrs_4893155344
                    __attrs_4893155344 = _static_4897199376

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4891232512_url('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4893158096
                    __default_4893158096 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/lp-migration' (55:22)> -> __attr_href
                    __token = 1683
                    try:
                        __zt_tmp = __attrs_4893155344
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('string', '${context/absolute_url}/lp-migration', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4891232512_url((' href="%s"' % __attr_href))
                    __append_4891232512_url(' >')
                    __stream_4390625040 = []
                    __append_4390625040 = __stream_4390625040.append
                    __append_4390625040('migration procedure.\n            ')
                    __msgid_4390625040 = __re_whitespace(''.join(__stream_4390625040)).strip()
                    if __msgid_4390625040:
                        __append_4891232512_url(translate(__msgid_4390625040, mapping=None, default=__msgid_4390625040, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_4891232512_url('</a>')
                    __append_4893553872('${url}')
                    __stream_4891232512_url = ''.join(__stream_4891232512_url)
                    __append_4893553872('\n          ')
                    __msgid_4893553872 = __re_whitespace(''.join(__stream_4893553872)).strip()
                    if __msgid_4893553872:
                        __append(translate(__msgid_4893553872, mapping={'url': __stream_4891232512_url, }, default=__msgid_4893553872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n        </div>\n      </div>\n\n    ')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_4867403856
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4662095120('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4893848640 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4893848640
            __i18n_domain = __previous_i18n_domain_4867397264
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }