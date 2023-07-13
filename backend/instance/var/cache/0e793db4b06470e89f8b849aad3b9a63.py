# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/keywords.pt'

__tokens = {75: ('context/Subject|nothing', 3, 22), 120: (' nocall:modules/Products.PythonScripts.standard/url_quot', 4, 20), 214: ('categories', 6, 24), 481: ('categories', 18, 37), 627: ('python:url_quote(category)', 23, 21), 708: ('string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', 26, 16), 851: ('category', 29, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878778320 = {'class': 'btn btn-sm btn-outline-primary', 'href': '#', 'rel': 'nofollow', }
_static_4659865408 = {}
_static_4878764160 = {'class': 'card-title section-heading d-none', }
_static_4878768576 = {'class': 'viewlet keywords-viewlet', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878777024 = {'id': 'section-category', }

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

            # <Static value=<ast.Dict object at 0x122cc3ac0> name=None at 115694790> -> __attrs_4664384592
            __attrs_4664384592 = _static_4878777024
            __backup_categories_4878611264 = get('categories', __marker)

            # <Value 'context/Subject|nothing' (3:22)> -> __value
            __token = 75
            try:
                __zt_tmp = __attrs_4664384592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'context/Subject|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['categories'] = __value
            __backup_url_quote_4878765072 = get('url_quote', __marker)

            # <Value 'nocall:modules/Products.PythonScripts.standard/url_quote' (4:20)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_4664384592
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', 'modules/Products.PythonScripts.standard/url_quote', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['url_quote'] = __value

            # <Value 'categories' (6:24)> -> __condition
            __token = 214
            try:
                __zt_tmp = __attrs_4664384592
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'categories', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4664385872 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-category" >\n\n  ')

                # <Static value=<ast.Dict object at 0x122cc19c0> name=None at 11604d690> -> __attrs_4670782160
                __attrs_4670782160 = _static_4878768576

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet keywords-viewlet">\n\n    ')

                # <Static value=<ast.Dict object at 0x122cc0880> name=None at 1167d3a90> -> __attrs_4677542352
                __attrs_4677542352 = _static_4878764160

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-title section-heading d-none" >')
                __stream_4672272528 = []
                __append_4672272528 = __stream_4672272528.append
                __append_4672272528('\n      Keywords\n    ')
                __msgid_4672272528 = __re_whitespace(''.join(__stream_4672272528)).strip()
                if 'section_keywords_heading':
                    __append(translate('section_keywords_heading', mapping=None, default=__msgid_4672272528, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4668587536
                __attrs_4668587536 = _static_4659865408
                __backup_category_4878444784 = get('category', __marker)

                # <Value 'categories' (18:37)> -> __iterator
                __token = 481
                try:
                    __zt_tmp = __attrs_4668587536
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'categories', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4677544208, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x122cc3fd0> name=None at 117bb4a50> -> __attrs_4675387792
                    __attrs_4675387792 = _static_4878778320
                    __backup_quotedCat_4878440704 = get('quotedCat', __marker)

                    # <Value 'python:url_quote(category)' (23:21)> -> __value
                    __token = 627
                    try:
                        __zt_tmp = __attrs_4675387792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', 'url_quote(category)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['quotedCat'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="btn btn-sm btn-outline-primary"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4669128976
                    __default_4669128976 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}' (26:16)> -> __attr_href
                    __token = 708
                    try:
                        __zt_tmp = __attrs_4675387792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('string', '${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="nofollow" >\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675390736
                    __attrs_4675390736 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4675400528
                    __default_4675400528 = _DEFAULT_MARKER

                    # <Value 'category' (29:27)> -> __cache_4675388944
                    __token = 851
                    try:
                        __zt_tmp = __attrs_4675390736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4675388944 = _static_4662095120('path', 'category', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'category' (29:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116acf990> -> __condition
                    __expression = __cache_4675388944

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4675388944
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>')
                    if (__backup_quotedCat_4878440704 is __marker):
                        del econtext['quotedCat']
                    else:
                        econtext['quotedCat'] = __backup_quotedCat_4878440704
                    __append('\n    ')
                    ____index_4677544208 -= 1
                    if (____index_4677544208 > 0):
                        __append('')
                if (__backup_category_4878444784 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_4878444784
                __append('\n\n  </div>\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4664385872
            if (__backup_url_quote_4878765072 is __marker):
                del econtext['url_quote']
            else:
                econtext['url_quote'] = __backup_url_quote_4878765072
            if (__backup_categories_4878611264 is __marker):
                del econtext['categories']
            else:
                econtext['categories'] = __backup_categories_4878611264
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }