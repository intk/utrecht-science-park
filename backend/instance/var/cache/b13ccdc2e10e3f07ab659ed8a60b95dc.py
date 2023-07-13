# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/z3cform/templates/singlecheckboxbool_input.pt'

__tokens = {129: ('view/items', 4, 14), 154: (' python:list(items', 5, 13), 197: ('x python:len(items) ==', 6, 22), 277: ('python:len(items) &gt', 10, 22), 324: ('single_checkbox', 11, 21), 377: ('view/id', 13, 12), 453: ('items', 17, 26), 500: ('python:single_checkbox and view.id or None', 19, 14), 826: ('item/checked', 32, 28), 1015: ('ss string:form-check-input ${view/kla', 37, 18), 888: ('item/id', 34, 18), 1864: ('              ', 59, 0), 1830: ('nly;\n   ', 57, 34), 916: (' item/nam', 35, 19), 1651: ('          tab', 53, 5), 1138: ('title view', 40, 15), 1074: ('lue item/v', 38, 17), 950: ("d python:view.required and 'required' or No", 36, 22), 1106: ('tyle view/', 39, 16), 1169: ('  lang vi', 41, 13), 1202: ('onclick view', 42, 15), 1241: ('dblclick view/o', 43, 17), 1284: ('mousedown view/o', 44, 17), 1326: (' onmouseup vie', 45, 14), 1368: ('onmouseover view', 46, 15), 1412: (' onmousemove vie', 47, 14), 1455: ('   onmouseout v', 48, 12), 1497: ('    onkeypress ', 49, 11), 1538: ('      onkeydow', 50, 9), 1576: ('         onk', 51, 6), 1613: ('         disa', 52, 6), 1688: ('            ', 54, 3), 1723: ('           ', 55, 1), 1759: ('             ', 56, 2), 1797: ('             ', 57, 1), 1903: (';\n           ', 59, 39), 2195: ('not:item/checked', 71, 28), 2388: ('ss string:form-check-input ${view/kla', 76, 18), 2261: ('item/id', 73, 18), 3237: ('              ', 98, 0), 3203: ('nly;\n   ', 96, 34), 2289: (' item/nam', 74, 19), 3024: ('          tab', 92, 5), 2511: ('title view', 79, 15), 2447: ('lue item/v', 77, 17), 2323: ("d python:view.required and 'required' or No", 75, 22), 2479: ('tyle view/', 78, 16), 2542: ('  lang vi', 80, 13), 2575: ('onclick view', 81, 15), 2614: ('dblclick view/o', 82, 17), 2657: ('mousedown view/o', 83, 17), 2699: (' onmouseup vie', 84, 14), 2741: ('onmouseover view', 85, 15), 2785: (' onmousemove vie', 86, 14), 2828: ('   onmouseout v', 87, 12), 2870: ('    onkeypress ', 88, 11), 2911: ('      onkeydow', 89, 9), 2949: ('         onk', 90, 6), 2986: ('         disa', 91, 6), 3061: ('            ', 93, 3), 3096: ('           ', 94, 1), 3132: ('             ', 95, 2), 3170: ('             ', 96, 1), 3276: (';\n           ', 98, 39), 3448: ('item/id', 105, 19), 3507: ('item/label', 108, 27), 3634: ('item/required', 111, 29), 3804: ('item/description', 116, 34), 3988: ('string:${view/name}-empty-marker', 126, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4897865984 = {'name': 'field-empty-marker', 'type': 'hidden', 'value': '1', }
_static_4880029376 = {'class': 'form-text', }
_static_4897871360 = {'class': 'required horizontal', 'title': 'Required', }
_static_4659865408 = {}
_static_4897869344 = {'class': 'form-check-label', 'for': '', }
_static_4897867136 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'name': '', 'tabindex': '', 'title': '', 'type': 'checkbox', 'value': '', 'required': "python:view.required and 'required' or None", 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', }
_static_4897880096 = {'class': '', 'id': '', 'accesskey': '', 'alt': '', 'checked': 'checked', 'name': '', 'tabindex': '', 'title': '', 'type': 'checkbox', 'value': '', 'required': "python:view.required and 'required' or None", 'style': 'view/style', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'onselect': 'view/onselect', }
_static_4897872608 = {'class': 'form-check', 'id': 'python:single_checkbox and view.id or None', }
_static_4897872128 = {'id': 'view/id', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4897873328 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x123ef9db0> name=None at 1175c8a50> -> __attrs_4686907472
            __attrs_4686907472 = _static_4897873328
            __backup_items_4881775536 = get('items', __marker)

            # <Value 'view/items' (4:14)> -> __value
            __token = 129
            try:
                __zt_tmp = __attrs_4686907472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/items', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_items_4878732160 = get('items', __marker)

            # <Value 'python:list(items)' (5:13)> -> __value
            __token = 154
            try:
                __zt_tmp = __attrs_4686907472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'list(items)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['items'] = __value
            __backup_single_checkbox_4897388096 = get('single_checkbox', __marker)

            # <Value 'python:len(items) == 1' (6:22)> -> __value
            __token = 197
            try:
                __zt_tmp = __attrs_4686907472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'len(items) == 1', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['single_checkbox'] = __value
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x123ef9900> name=None at 1175cb550> -> __attrs_4867307280
            __attrs_4867307280 = _static_4897872128

            # <Value 'python:len(items) > 0' (10:22)> -> __condition
            __token = 277
            try:
                __zt_tmp = __attrs_4867307280
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('python', 'len(items) > 0', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'single_checkbox' (11:21)> at 1221d1110> -> __cache_4867297552

                # <Value 'single_checkbox' (11:21)> -> __cache_4867297552
                __token = 324
                try:
                    __zt_tmp = __attrs_4867307280
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4867297552 = _static_4662095120('path', 'single_checkbox', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __cache_4867297552 = not __cache_4867297552
                __condition = __cache_4867297552
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4669644112
                    __default_4669644112 = _DEFAULT_MARKER

                    # <Substitution 'view/id' (13:12)> -> __attr_id
                    __token = 377
                    try:
                        __zt_tmp = __attrs_4867307280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4662095120('path', 'view/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >')
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x123ef9ae0> name=None at 1221d2090> -> __attrs_4867307600
                __attrs_4867307600 = _static_4897872608
                __backup_item_4897382528 = get('item', __marker)

                # <Value 'items' (17:26)> -> __iterator
                __token = 453
                try:
                    __zt_tmp = __attrs_4867307600
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'items', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4867309008, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4867307408
                    __default_4867307408 = _DEFAULT_MARKER

                    # <Substitution 'python:single_checkbox and view.id or None' (19:14)> -> __attr_id
                    __token = 500
                    try:
                        __zt_tmp = __attrs_4867307600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4662095120('python', 'single_checkbox and view.id or None', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n      ')

                    # <Static value=<ast.Dict object at 0x123efb820> name=None at 1222bb310> -> __attrs_4869010896
                    __attrs_4869010896 = _static_4897880096

                    # <Value 'item/checked' (32:28)> -> __condition
                    __token = 826
                    try:
                        __zt_tmp = __attrs_4869010896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'item/checked', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868255952
                        __default_4868255952 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (37:18)> -> __attr_class
                        __token = 1015
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4662095120('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869032016
                        __default_4869032016 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (34:18)> -> __attr_id
                        __token = 888
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4662095120('path', 'item/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866673104
                        __default_4866673104 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (59:0)> -> __attr_accesskey
                        __token = 1864
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_4662095120('path', 'view/accesskey', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866673808
                        __default_4866673808 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (57:34)> -> __attr_alt
                        __token = 1830
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_4662095120('path', 'view/alt', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))
                        __append(' checked="checked"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896182416
                        __default_4896182416 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (35:19)> -> __attr_name
                        __token = 916
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4662095120('path', 'item/name', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689662928
                        __default_4689662928 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (53:5)> -> __attr_tabindex
                        __token = 1651
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_4662095120('path', 'view/tabindex', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689663696
                        __default_4689663696 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (40:15)> -> __attr_title
                        __token = 1138
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4662095120('path', 'view/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append(' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688522832
                        __default_4688522832 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (38:17)> -> __attr_value
                        __token = 1074
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4662095120('path', 'item/value', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688520720
                        __default_4688520720 = _DEFAULT_MARKER

                        # <Substitution "python:view.required and 'required' or None" (36:22)> -> __attr_required
                        __token = 950
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_required = _static_4662095120('python', "view.required and 'required' or None", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_required is not None):
                            __append((' required="%s"' % __attr_required))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688524432
                        __default_4688524432 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (39:16)> -> __attr_style
                        __token = 1106
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_4662095120('path', 'view/style', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688526864
                        __default_4688526864 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (41:13)> -> __attr_lang
                        __token = 1169
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_4662095120('path', 'view/lang', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688525456
                        __default_4688525456 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (42:15)> -> __attr_onclick
                        __token = 1202
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_4662095120('path', 'view/onclick', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688516048
                        __default_4688516048 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (43:17)> -> __attr_ondblclick
                        __token = 1241
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_4662095120('path', 'view/ondblclick', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688512976
                        __default_4688512976 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (44:17)> -> __attr_onmousedown
                        __token = 1284
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_4662095120('path', 'view/onmousedown', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688517776
                        __default_4688517776 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (45:14)> -> __attr_onmouseup
                        __token = 1326
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_4662095120('path', 'view/onmouseup', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688514448
                        __default_4688514448 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (46:15)> -> __attr_onmouseover
                        __token = 1368
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_4662095120('path', 'view/onmouseover', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688526672
                        __default_4688526672 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (47:14)> -> __attr_onmousemove
                        __token = 1412
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_4662095120('path', 'view/onmousemove', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688522064
                        __default_4688522064 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (48:12)> -> __attr_onmouseout
                        __token = 1455
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_4662095120('path', 'view/onmouseout', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869011344
                        __default_4869011344 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (49:11)> -> __attr_onkeypress
                        __token = 1497
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_4662095120('path', 'view/onkeypress', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869000592
                        __default_4869000592 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (50:9)> -> __attr_onkeydown
                        __token = 1538
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_4662095120('path', 'view/onkeydown', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869001744
                        __default_4869001744 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (51:6)> -> __attr_onkeyup
                        __token = 1576
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_4662095120('path', 'view/onkeyup', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869006608
                        __default_4869006608 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (52:6)> -> __attr_disabled
                        __token = 1613
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_4662095120('path', 'view/disabled', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = None
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868999696
                        __default_4868999696 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (54:3)> -> __attr_onfocus
                        __token = 1688
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_4662095120('path', 'view/onfocus', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869009808
                        __default_4869009808 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (55:1)> -> __attr_onblur
                        __token = 1723
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_4662095120('path', 'view/onblur', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869005456
                        __default_4869005456 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (56:2)> -> __attr_onchange
                        __token = 1759
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_4662095120('path', 'view/onchange', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868997904
                        __default_4868997904 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (57:1)> -> __attr_readonly
                        __token = 1797
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_4662095120('path', 'view/readonly', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = None
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869002064
                        __default_4869002064 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (59:39)> -> __attr_onselect
                        __token = 1903
                        try:
                            __zt_tmp = __attrs_4869010896
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_4662095120('path', 'view/onselect', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')

                    # <Static value=<ast.Dict object at 0x123ef8580> name=None at 12210ba50> -> __attrs_4866824208
                    __attrs_4866824208 = _static_4897867136

                    # <Value 'not:item/checked' (71:28)> -> __condition
                    __token = 2195
                    try:
                        __zt_tmp = __attrs_4866824208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('not', 'item/checked', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869122064
                        __default_4869122064 = _DEFAULT_MARKER

                        # <Substitution 'string:form-check-input ${view/klass}' (76:18)> -> __attr_class
                        __token = 2388
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_4662095120('string', 'form-check-input ${view/klass}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869127824
                        __default_4869127824 = _DEFAULT_MARKER

                        # <Substitution 'item/id' (73:18)> -> __attr_id
                        __token = 2261
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_4662095120('path', 'item/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4869121424
                        __default_4869121424 = _DEFAULT_MARKER

                        # <Substitution 'view/accesskey' (98:0)> -> __attr_accesskey
                        __token = 3237
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_accesskey = _static_4662095120('path', 'view/accesskey', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_accesskey is not None):
                            __append((' accesskey="%s"' % __attr_accesskey))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4685002512
                        __default_4685002512 = _DEFAULT_MARKER

                        # <Substitution 'view/alt' (96:34)> -> __attr_alt
                        __token = 3203
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_4662095120('path', 'view/alt', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4685002832
                        __default_4685002832 = _DEFAULT_MARKER

                        # <Substitution 'item/name' (74:19)> -> __attr_name
                        __token = 2289
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_name = _static_4662095120('path', 'item/name', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_name is not None):
                            __append((' name="%s"' % __attr_name))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4893019920
                        __default_4893019920 = _DEFAULT_MARKER

                        # <Substitution 'view/tabindex' (92:5)> -> __attr_tabindex
                        __token = 3024
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_tabindex = _static_4662095120('path', 'view/tabindex', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_tabindex is not None):
                            __append((' tabindex="%s"' % __attr_tabindex))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4893030480
                        __default_4893030480 = _DEFAULT_MARKER

                        # <Substitution 'view/title' (79:15)> -> __attr_title
                        __token = 2511
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_4662095120('path', 'view/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append(' type="checkbox"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4893024400
                        __default_4893024400 = _DEFAULT_MARKER

                        # <Substitution 'item/value' (77:17)> -> __attr_value
                        __token = 2447
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4662095120('path', 'item/value', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866596688
                        __default_4866596688 = _DEFAULT_MARKER

                        # <Substitution "python:view.required and 'required' or None" (75:22)> -> __attr_required
                        __token = 2323
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_required = _static_4662095120('python', "view.required and 'required' or None", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_required is not None):
                            __append((' required="%s"' % __attr_required))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866592144
                        __default_4866592144 = _DEFAULT_MARKER

                        # <Substitution 'view/style' (78:16)> -> __attr_style
                        __token = 2479
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_style = _static_4662095120('path', 'view/style', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_style is not None):
                            __append((' style="%s"' % __attr_style))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866603088
                        __default_4866603088 = _DEFAULT_MARKER

                        # <Substitution 'view/lang' (80:13)> -> __attr_lang
                        __token = 2542
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_lang = _static_4662095120('path', 'view/lang', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_lang is not None):
                            __append((' lang="%s"' % __attr_lang))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866598224
                        __default_4866598224 = _DEFAULT_MARKER

                        # <Substitution 'view/onclick' (81:15)> -> __attr_onclick
                        __token = 2575
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onclick = _static_4662095120('path', 'view/onclick', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onclick is not None):
                            __append((' onclick="%s"' % __attr_onclick))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866596752
                        __default_4866596752 = _DEFAULT_MARKER

                        # <Substitution 'view/ondblclick' (82:17)> -> __attr_ondblclick
                        __token = 2614
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_ondblclick = _static_4662095120('path', 'view/ondblclick', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_ondblclick is not None):
                            __append((' ondblclick="%s"' % __attr_ondblclick))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866594320
                        __default_4866594320 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousedown' (83:17)> -> __attr_onmousedown
                        __token = 2657
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousedown = _static_4662095120('path', 'view/onmousedown', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousedown is not None):
                            __append((' onmousedown="%s"' % __attr_onmousedown))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866589072
                        __default_4866589072 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseup' (84:14)> -> __attr_onmouseup
                        __token = 2699
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseup = _static_4662095120('path', 'view/onmouseup', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseup is not None):
                            __append((' onmouseup="%s"' % __attr_onmouseup))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866603920
                        __default_4866603920 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseover' (85:15)> -> __attr_onmouseover
                        __token = 2741
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseover = _static_4662095120('path', 'view/onmouseover', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseover is not None):
                            __append((' onmouseover="%s"' % __attr_onmouseover))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868363088
                        __default_4868363088 = _DEFAULT_MARKER

                        # <Substitution 'view/onmousemove' (86:14)> -> __attr_onmousemove
                        __token = 2785
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmousemove = _static_4662095120('path', 'view/onmousemove', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmousemove is not None):
                            __append((' onmousemove="%s"' % __attr_onmousemove))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868363344
                        __default_4868363344 = _DEFAULT_MARKER

                        # <Substitution 'view/onmouseout' (87:12)> -> __attr_onmouseout
                        __token = 2828
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onmouseout = _static_4662095120('path', 'view/onmouseout', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onmouseout is not None):
                            __append((' onmouseout="%s"' % __attr_onmouseout))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868373200
                        __default_4868373200 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeypress' (88:11)> -> __attr_onkeypress
                        __token = 2870
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeypress = _static_4662095120('path', 'view/onkeypress', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeypress is not None):
                            __append((' onkeypress="%s"' % __attr_onkeypress))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868363408
                        __default_4868363408 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeydown' (89:9)> -> __attr_onkeydown
                        __token = 2911
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeydown = _static_4662095120('path', 'view/onkeydown', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeydown is not None):
                            __append((' onkeydown="%s"' % __attr_onkeydown))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868371024
                        __default_4868371024 = _DEFAULT_MARKER

                        # <Substitution 'view/onkeyup' (90:6)> -> __attr_onkeyup
                        __token = 2949
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onkeyup = _static_4662095120('path', 'view/onkeyup', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onkeyup is not None):
                            __append((' onkeyup="%s"' % __attr_onkeyup))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868370832
                        __default_4868370832 = _DEFAULT_MARKER

                        # <Boolean 'view/disabled' (91:6)> -> __attr_disabled
                        __token = 2986
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_disabled = _static_4662095120('path', 'view/disabled', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if (__attr_disabled is _DEFAULT_MARKER):
                            __attr_disabled = None
                        else:
                            if __attr_disabled:
                                __attr_disabled = 'disabled'
                            else:
                                __attr_disabled = None
                        if (__attr_disabled is not None):
                            __append((' disabled="%s"' % __attr_disabled))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4868363856
                        __default_4868363856 = _DEFAULT_MARKER

                        # <Substitution 'view/onfocus' (93:3)> -> __attr_onfocus
                        __token = 3061
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onfocus = _static_4662095120('path', 'view/onfocus', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onfocus is not None):
                            __append((' onfocus="%s"' % __attr_onfocus))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866827664
                        __default_4866827664 = _DEFAULT_MARKER

                        # <Substitution 'view/onblur' (94:1)> -> __attr_onblur
                        __token = 3096
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onblur = _static_4662095120('path', 'view/onblur', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onblur is not None):
                            __append((' onblur="%s"' % __attr_onblur))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866832912
                        __default_4866832912 = _DEFAULT_MARKER

                        # <Substitution 'view/onchange' (95:2)> -> __attr_onchange
                        __token = 3132
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onchange = _static_4662095120('path', 'view/onchange', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onchange is not None):
                            __append((' onchange="%s"' % __attr_onchange))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866829264
                        __default_4866829264 = _DEFAULT_MARKER

                        # <Boolean 'view/readonly' (96:1)> -> __attr_readonly
                        __token = 3170
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_readonly = _static_4662095120('path', 'view/readonly', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if (__attr_readonly is _DEFAULT_MARKER):
                            __attr_readonly = None
                        else:
                            if __attr_readonly:
                                __attr_readonly = 'readonly'
                            else:
                                __attr_readonly = None
                        if (__attr_readonly is not None):
                            __append((' readonly="%s"' % __attr_readonly))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866832272
                        __default_4866832272 = _DEFAULT_MARKER

                        # <Substitution 'view/onselect' (98:39)> -> __attr_onselect
                        __token = 3276
                        try:
                            __zt_tmp = __attrs_4866824208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_onselect = _static_4662095120('path', 'view/onselect', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_onselect is not None):
                            __append((' onselect="%s"' % __attr_onselect))
                        __append(' />')
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x123ef8e20> name=None at 12215e690> -> __attrs_4692366736
                    __attrs_4692366736 = _static_4897869344

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4692373136
                    __default_4692373136 = _DEFAULT_MARKER

                    # <Substitution 'item/id' (105:19)> -> __attr_for
                    __token = 3448
                    try:
                        __zt_tmp = __attrs_4692366736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_4662095120('path', 'item/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4866955088
                    __attrs_4866955088 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4692376208
                    __default_4692376208 = _DEFAULT_MARKER

                    # <Value 'item/label' (108:27)> -> __cache_4692371024
                    __token = 3507
                    try:
                        __zt_tmp = __attrs_4866955088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4692371024 = _static_4662095120('path', 'item/label', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/label' (108:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117afe150> -> __condition
                    __expression = __cache_4692371024

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Label')
                    else:
                        __content = __cache_4692371024
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n        ')

                    # <Static value=<ast.Dict object at 0x123ef9600> name=None at 12217d010> -> __attrs_4866964752
                    __attrs_4866964752 = _static_4897871360

                    # <Value 'item/required' (111:29)> -> __condition
                    __token = 3634
                    try:
                        __zt_tmp = __attrs_4866964752
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'item/required', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="required horizontal"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866950032
                        __default_4866950032 = _DEFAULT_MARKER

                        # <Translate msgid='title_required' node=<ast.Constant object at 0x123ef8820> at 12217d350> -> __attr_title
                        __attr_title = 'Required'
                        __attr_title = translate('title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))
                        __append(' >&nbsp;</span>')
                    __append('\n      </label>\n      ')

                    # <Static value=<ast.Dict object at 0x122df56c0> name=None at 12217c810> -> __attrs_4866962896
                    __attrs_4866962896 = _static_4880029376

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-text" >')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866957520
                    __default_4866957520 = _DEFAULT_MARKER

                    # <Value 'item/description' (116:34)> -> __cache_4866949648
                    __token = 3804
                    try:
                        __zt_tmp = __attrs_4866962896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4866949648 = _static_4662095120('path', 'item/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'item/description' (116:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 12217ca50> -> __condition
                    __expression = __cache_4866949648

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Description')
                    else:
                        __content = __cache_4866949648
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n    </div>')
                    ____index_4867309008 -= 1
                    if (____index_4867309008 > 0):
                        __append('\n    ')
                if (__backup_item_4897382528 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_4897382528
                __append('\n\n  ')
                __condition = __cache_4867297552
                if __condition:
                    __append('</div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x123ef8100> name=None at 117a6c110> -> __attrs_4691774608
            __attrs_4691774608 = _static_4897865984

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4691786640
            __default_4691786640 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (126:16)> -> __attr_name
            __token = 3988
            try:
                __zt_tmp = __attrs_4691774608
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4662095120('string', '${view/name}-empty-marker', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'field-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" value="1" />\n')
            if (__backup_single_checkbox_4897388096 is __marker):
                del econtext['single_checkbox']
            else:
                econtext['single_checkbox'] = __backup_single_checkbox_4897388096
            if (__backup_items_4878732160 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_4878732160
            if (__backup_items_4881775536 is __marker):
                del econtext['items']
            else:
                econtext['items'] = __backup_items_4881775536
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }