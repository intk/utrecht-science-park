# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {73: ('view/enabled|nothing', 3, 19), 120: (' view/isViewTemplate|nothin', 4, 25), 185: ('python:enabled and isViewTemplate', 6, 24), 300: ('view/site_url', 11, 26), 422: ('view/next', 16, 16), 452: (' view/previou', 17, 19), 503: ('python:previous is not None or next is not None', 19, 24), 696: ('previous', 24, 24), 748: ('previous/url', 26, 16), 1012: ('previous/title', 35, 29), 1240: ('next', 43, 24), 1288: ('next/url', 45, 16), 1500: ('next/title', 53, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878540592 = {'class': 'arrow', }
_static_4878536800 = {'class': 'label', }
_static_4878536128 = {'class': 'btn btn-sm btn-outline-secondary align-self-end next', 'title': 'Go to next item', 'href': 'next/url', }
_static_4878535072 = {'class': 'label', }
_static_4878544576 = {'class': 'arrow', }
_static_4878542848 = {'class': 'btn btn-sm btn-outline-secondary align-self-start previous', 'title': 'Go to previous item', 'href': 'previous/url', }
_static_4878545152 = {'class': 'pagination justify-content-between', }
_static_4659865408 = {}
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878534736 = {'id': 'section-next-prev', }

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

            # <Static value=<ast.Dict object at 0x122c88850> name=None at 1175369d0> -> __attrs_4676063312
            __attrs_4676063312 = _static_4878534736
            __backup_enabled_4878707312 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (3:19)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_4676063312
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/enabled|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_4878541408 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (4:25)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_4676063312
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (6:24)> -> __condition
            __token = 185
            try:
                __zt_tmp = __attrs_4676063312
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('python', 'enabled and isViewTemplate', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4676063184 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-next-prev" >\n\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676064080
                __attrs_4676064080 = _static_4659865408
                __backup_portal_url_4878545680 = get('portal_url', __marker)

                # <Value 'view/site_url' (11:26)> -> __value
                __token = 300
                try:
                    __zt_tmp = __attrs_4676064080
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/site_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x122c8b100> name=None at 116967ed0> -> __attrs_4681165584
                __attrs_4681165584 = _static_4878545152
                __backup_next_4878540256 = get('next', __marker)

                # <Value 'view/next' (16:16)> -> __value
                __token = 422
                try:
                    __zt_tmp = __attrs_4681165584
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/next', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_4878547120 = get('previous', __marker)

                # <Value 'view/previous' (17:19)> -> __value
                __token = 452
                try:
                    __zt_tmp = __attrs_4681165584
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/previous', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'python:previous is not None or next is not None' (19:24)> -> __condition
                __token = 503
                try:
                    __zt_tmp = __attrs_4681165584
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('python', 'previous is not None or next is not None', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="pagination justify-content-between" >\n\n      ')

                    # <Static value=<ast.Dict object at 0x122c8a800> name=None at 11704d110> -> __attrs_4681526160
                    __attrs_4681526160 = _static_4878542848

                    # <Value 'previous' (24:24)> -> __condition
                    __token = 696
                    try:
                        __zt_tmp = __attrs_4681526160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'previous', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-start previous"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681156496
                        __default_4681156496 = _DEFAULT_MARKER

                        # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x122c88460> at 11704cfd0> -> __attr_title
                        __attr_title = 'Go to previous item'
                        __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681516176
                        __default_4681516176 = _DEFAULT_MARKER

                        # <Substitution 'previous/url' (26:16)> -> __attr_href
                        __token = 748
                        try:
                            __zt_tmp = __attrs_4681526160
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4662095120('path', 'previous/url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x122c8aec0> name=None at 115f95c10> -> __attrs_4684318928
                        __attrs_4684318928 = _static_4878544576

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n        ')

                        # <Static value=<ast.Dict object at 0x122c889a0> name=None at 117350710> -> __attrs_4669862992
                        __attrs_4669862992 = _static_4878535072

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_4879262304_itemtitle = ''
                        __stream_4684322000 = []
                        __append_4684322000 = __stream_4684322000.append
                        __append_4684322000('\n              Previous:\n          ')
                        __stream_4879262304_itemtitle = []
                        __append_4879262304_itemtitle = __stream_4879262304_itemtitle.append

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4677546384
                        __attrs_4677546384 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4677546832
                        __default_4677546832 = _DEFAULT_MARKER

                        # <Value 'previous/title' (35:29)> -> __cache_4677543376
                        __token = 1012
                        try:
                            __zt_tmp = __attrs_4677546384
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4677543376 = _static_4662095120('path', 'previous/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'previous/title' (35:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116cdb710> -> __condition
                        __expression = __cache_4677543376

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_4879262304_itemtitle('<span ></span>')
                        else:
                            __content = __cache_4677543376
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_4879262304_itemtitle(__content)
                        __append_4684322000('${itemtitle}')
                        __stream_4879262304_itemtitle = ''.join(__stream_4879262304_itemtitle)
                        __append_4684322000('\n        ')
                        __msgid_4684322000 = __re_whitespace(''.join(__stream_4684322000)).strip()
                        if 'label_previous_item':
                            __append(translate('label_previous_item', mapping={'itemtitle': __stream_4879262304_itemtitle, }, default=__msgid_4684322000, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n      </a>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x122c88dc0> name=None at 117989b50> -> __attrs_4690853584
                    __attrs_4690853584 = _static_4878536128

                    # <Value 'next' (43:24)> -> __condition
                    __token = 1240
                    try:
                        __zt_tmp = __attrs_4690853584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'next', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-end next"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4690844880
                        __default_4690844880 = _DEFAULT_MARKER

                        # <Translate msgid='title_next_item' node=<ast.Constant object at 0x122c88100> at 11798bb90> -> __attr_title
                        __attr_title = 'Go to next item'
                        __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4690848016
                        __default_4690848016 = _DEFAULT_MARKER

                        # <Substitution 'next/url' (45:16)> -> __attr_href
                        __token = 1288
                        try:
                            __zt_tmp = __attrs_4690853584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_4662095120('path', 'next/url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x122c89060> name=None at 1169e5e10> -> __attrs_4674437648
                        __attrs_4674437648 = _static_4878536800

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_4879262304_itemtitle = ''
                        __stream_4686162576 = []
                        __append_4686162576 = __stream_4686162576.append
                        __append_4686162576('\n              Next:\n          ')
                        __stream_4879262304_itemtitle = []
                        __append_4879262304_itemtitle = __stream_4879262304_itemtitle.append

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683135248
                        __attrs_4683135248 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689482192
                        __default_4689482192 = _DEFAULT_MARKER

                        # <Value 'next/title' (53:29)> -> __cache_4689477840
                        __token = 1500
                        try:
                            __zt_tmp = __attrs_4683135248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4689477840 = _static_4662095120('path', 'next/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'next/title' (53:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11783cdd0> -> __condition
                        __expression = __cache_4689477840

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_4879262304_itemtitle('<span ></span>')
                        else:
                            __content = __cache_4689477840
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_4879262304_itemtitle(__content)
                        __append_4686162576('${itemtitle}')
                        __stream_4879262304_itemtitle = ''.join(__stream_4879262304_itemtitle)
                        __append_4686162576('\n        ')
                        __msgid_4686162576 = __re_whitespace(''.join(__stream_4686162576)).strip()
                        if 'label_next_item':
                            __append(translate('label_next_item', mapping={'itemtitle': __stream_4879262304_itemtitle, }, default=__msgid_4686162576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n        ')

                        # <Static value=<ast.Dict object at 0x122c89f30> name=None at 1172bc710> -> __attrs_4651676112
                        __attrs_4651676112 = _static_4878540592

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n      </a>')
                    __append('\n\n\n    </nav>')
                if (__backup_previous_4878547120 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_4878547120
                if (__backup_next_4878540256 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_4878540256
                __append('\n\n  ')
                if (__backup_portal_url_4878545680 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_4878545680
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4676063184
            if (__backup_isViewTemplate_4878541408 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_4878541408
            if (__backup_enabled_4878707312 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_4878707312
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }