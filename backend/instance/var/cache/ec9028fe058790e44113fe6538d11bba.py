# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/z3cform/templates/orderedselect_input.pt'

__tokens = {374: ('view/id', 13, 14), 671: ('s string:form-control ${view/klas', 25, 22), 576: ('string:${view/id}-from', 23, 21), 622: (' string:${view/name}.fro', 24, 22), 1511: ('         ', 45, 1), 729: ('le view/st', 26, 21), 764: ('tle view/t', 27, 20), 798: ('lang view', 28, 18), 834: ('click view/o', 29, 20), 876: ('lclick view/ond', 30, 22), 922: ('usedown view/onm', 31, 22), 967: ('nmouseup view/', 32, 19), 1012: ('mouseover view/o', 33, 20), 1059: ('nmousemove view/', 34, 19), 1105: (' onmouseout vie', 35, 17), 1150: ('  onkeypress vi', 36, 16), 1194: ('    onkeydown ', 37, 14), 1235: ('       onkey', 38, 11), 1275: ('       disabl', 39, 11), 1316: ('        tabin', 40, 10), 1356: ('          on', 41, 8), 1394: ('           ', 42, 6), 1433: ('           on', 43, 7), 1474: ('            m', 44, 6), 1608: ('view/notselectedItems', 48, 36), 1745: ('entry/value', 51, 26), 1662: ('nocall:entry/content', 49, 31), 2137: ("string:javascript:from2to('${view/id}')", 64, 26), 2497: ("string:javascript:to2from('${view/id}')", 74, 26), 2849: ('s string:form-control ${view/klas', 86, 22), 2758: ('string:${view/id}-to', 84, 21), 2802: (' string:${view/name}.t', 85, 22), 3689: ('         ', 106, 1), 2907: ('le view/st', 87, 21), 2942: ('tle view/t', 88, 20), 2976: ('lang view', 89, 18), 3012: ('click view/o', 90, 20), 3054: ('lclick view/ond', 91, 22), 3100: ('usedown view/onm', 92, 22), 3145: ('nmouseup view/', 93, 19), 3190: ('mouseover view/o', 94, 20), 3237: ('nmousemove view/', 95, 19), 3283: (' onmouseout vie', 96, 17), 3328: ('  onkeypress vi', 97, 16), 3372: ('    onkeydown ', 98, 14), 3413: ('       onkey', 99, 11), 3453: ('       disabl', 100, 11), 3494: ('        tabin', 101, 10), 3534: ('          on', 102, 8), 3572: ('           ', 103, 6), 3611: ('           on', 104, 7), 3652: ('            m', 105, 6), 3726: ('              required python:view.required', 107, 4), 3858: ('view/selectedItems', 110, 36), 3992: ('entry/value', 113, 26), 3909: ('nocall:entry/content', 111, 31), 4222: ('string:${view/name}-empty-marker', 121, 22), 4405: ('string:${view/id}-toDataContainer', 127, 19), 4538: ("string:copyDataForSubmit('${view/id}');", 131, 31), 4605: ('<![CDATA[ */\n          // initial copying of field "field.to" --> "field"\n          copyDataForSubmit("<i tal:replace="${view/id}"/>");\n          /* ]]>', 133, 14), 4726: ('view/id', 135, 47), 5075: ("string:javascript:moveUp('${view/id}')", 147, 26), 5432: ("string:javascript:moveDown('${view/id}')", 157, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4898240304 = {'class': 'btn btn-sm btn-outline-secondary', 'name': 'downButton', 'onClick': 'javascript:moveDown()', 'type': 'button', 'value': '&darr;', }
_static_4898227440 = {'class': 'btn btn-sm btn-outline-secondary', 'name': 'upButton', 'onClick': 'javascript:moveUp()', 'type': 'button', 'value': '&uarr;', }
_static_4898237952 = {'type': 'text/javascript', }
_static_4898233728 = {'id': 'toDataContainer', 'style': 'display: none', }
_static_4898236752 = {'name': 'foo-empty-marker', 'type': 'hidden', }
_static_4898231712 = {'value': 'entry/value', }
_static_4898232720 = {'class': '', 'id': 'to', 'name': 'to', 'size': '5', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'tabindex': 'view/tabindex', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'multiple': 'view/multiple', 'required': "python:view.required and 'required' or None", }
_static_4898237664 = {'class': 'btn btn-sm btn-outline-secondary', 'name': 'to2fromButton', 'onClick': 'javascript:to2from()', 'type': 'button', 'value': '&larr;', }
_static_4897207872 = {'class': 'btn btn-sm btn-outline-secondary', 'name': 'from2toButton', 'onClick': 'javascript:from2to()', 'type': 'button', 'value': '&rarr;', }
_static_4897209696 = {'value': 'entry/value', }
_static_4897204992 = {'class': '', 'id': 'from', 'name': 'from', 'size': '5', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'disabled': 'view/disabled', 'tabindex': 'view/tabindex', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'multiple': 'view/multiple', }
_static_4659865408 = {}
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4897208688 = {'class': 'ordered-selection-field', 'border': '0', 'id': 'view/id', }
_static_4897208160 = {'src': '++resource++orderedselect_input.js', 'type': 'text/javascript', }
_static_4897208064 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x123e57700> name=None at 123e6bf50> -> __attrs_4897280848
            __attrs_4897280848 = _static_4897208064
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x123e57760> name=None at 123e6a9d0> -> __attrs_4897286096
            __attrs_4897286096 = _static_4897208160

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script src="++resource++orderedselect_input.js" type="text/javascript" ></script>\n\n  ')

            # <Static value=<ast.Dict object at 0x123e57970> name=None at 123e6b450> -> __attrs_4896810896
            __attrs_4896810896 = _static_4897208688

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table class="ordered-selection-field" border="0"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894722512
            __default_4894722512 = _DEFAULT_MARKER

            # <Substitution 'view/id' (13:14)> -> __attr_id
            __token = 374
            try:
                __zt_tmp = __attrs_4896810896
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4662095120('path', 'view/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))
            __append(' >\n    ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4896806160
            __attrs_4896806160 = _static_4659865408

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4896810384
            __attrs_4896810384 = _static_4659865408

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n        ')

            # <Static value=<ast.Dict object at 0x123e56b00> name=None at 123df6d90> -> __attrs_4896629648
            __attrs_4896629648 = _static_4897204992

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897633360
            __default_4897633360 = _DEFAULT_MARKER

            # <Substitution 'string:form-control ${view/klass}' (25:22)> -> __attr_class
            __token = 671
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4662095120('string', 'form-control ${view/klass}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897620048
            __default_4897620048 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-from' (23:21)> -> __attr_id
            __token = 576
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4662095120('string', '${view/id}-from', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', 'from', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897633488
            __default_4897633488 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}.from' (24:22)> -> __attr_name
            __token = 622
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4662095120('string', '${view/name}.from', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'from', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897622736
            __default_4897622736 = _DEFAULT_MARKER

            # <Substitution 'view/size' (45:1)> -> __attr_size
            __token = 1511
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_4662095120('path', 'view/size', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '5', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897629392
            __default_4897629392 = _DEFAULT_MARKER

            # <Substitution 'view/style' (26:21)> -> __attr_style
            __token = 729
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4662095120('path', 'view/style', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897628112
            __default_4897628112 = _DEFAULT_MARKER

            # <Substitution 'view/title' (27:20)> -> __attr_title
            __token = 764
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4662095120('path', 'view/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897633424
            __default_4897633424 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (28:18)> -> __attr_lang
            __token = 798
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4662095120('path', 'view/lang', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897628560
            __default_4897628560 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (29:20)> -> __attr_onclick
            __token = 834
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4662095120('path', 'view/onclick', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897620304
            __default_4897620304 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (30:22)> -> __attr_ondblclick
            __token = 876
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4662095120('path', 'view/ondblclick', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897634832
            __default_4897634832 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (31:22)> -> __attr_onmousedown
            __token = 922
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4662095120('path', 'view/onmousedown', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896797072
            __default_4896797072 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (32:19)> -> __attr_onmouseup
            __token = 967
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4662095120('path', 'view/onmouseup', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896789776
            __default_4896789776 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (33:20)> -> __attr_onmouseover
            __token = 1012
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4662095120('path', 'view/onmouseover', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896793808
            __default_4896793808 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (34:19)> -> __attr_onmousemove
            __token = 1059
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4662095120('path', 'view/onmousemove', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896796368
            __default_4896796368 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (35:17)> -> __attr_onmouseout
            __token = 1105
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4662095120('path', 'view/onmouseout', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896797968
            __default_4896797968 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (36:16)> -> __attr_onkeypress
            __token = 1150
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4662095120('path', 'view/onkeypress', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896791504
            __default_4896791504 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (37:14)> -> __attr_onkeydown
            __token = 1194
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4662095120('path', 'view/onkeydown', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896794960
            __default_4896794960 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (38:11)> -> __attr_onkeyup
            __token = 1235
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4662095120('path', 'view/onkeyup', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896788176
            __default_4896788176 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (39:11)> -> __attr_disabled
            __token = 1275
            try:
                __zt_tmp = __attrs_4896629648
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

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896789904
            __default_4896789904 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (40:10)> -> __attr_tabindex
            __token = 1316
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4662095120('path', 'view/tabindex', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896790864
            __default_4896790864 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (41:8)> -> __attr_onfocus
            __token = 1356
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4662095120('path', 'view/onfocus', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896786960
            __default_4896786960 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (42:6)> -> __attr_onblur
            __token = 1394
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4662095120('path', 'view/onblur', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894603472
            __default_4894603472 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (43:7)> -> __attr_onchange
            __token = 1433
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4662095120('path', 'view/onchange', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894594896
            __default_4894594896 = _DEFAULT_MARKER

            # <Boolean 'view/multiple' (44:6)> -> __attr_multiple
            __token = 1474
            try:
                __zt_tmp = __attrs_4896629648
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_multiple = _static_4662095120('path', 'view/multiple', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if (__attr_multiple is _DEFAULT_MARKER):
                __attr_multiple = None
            else:
                if __attr_multiple:
                    __attr_multiple = 'multiple'
                else:
                    __attr_multiple = None
            if (__attr_multiple is not None):
                __append((' multiple="%s"' % __attr_multiple))
            __append(' >\n          ')

            # <Static value=<ast.Dict object at 0x123e57d60> name=None at 123dc91d0> -> __attrs_4896632720
            __attrs_4896632720 = _static_4897209696
            __backup_entry_4898113760 = get('entry', __marker)

            # <Value 'view/notselectedItems' (48:36)> -> __iterator
            __token = 1608
            try:
                __zt_tmp = __attrs_4896632720
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4662095120('path', 'view/notselectedItems', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            (__iterator, ____index_4896634704, ) = getname('repeat')('entry', __iterator)
            econtext['entry'] = None
            for __item in __iterator:
                econtext['entry'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896629584
                __default_4896629584 = _DEFAULT_MARKER

                # <Substitution 'entry/value' (51:26)> -> __attr_value
                __token = 1745
                try:
                    __zt_tmp = __attrs_4896632720
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4662095120('path', 'entry/value', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' >')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896624272
                __default_4896624272 = _DEFAULT_MARKER

                # <Value 'nocall:entry/content' (49:31)> -> __cache_4896629840
                __token = 1662
                try:
                    __zt_tmp = __attrs_4896632720
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4896629840 = _static_4662095120('nocall', 'entry/content', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'nocall:entry/content' (49:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 123e3ea10> -> __condition
                __expression = __cache_4896629840

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4896629840
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</option>')
                ____index_4896634704 -= 1
                if (____index_4896634704 > 0):
                    __append('\n          ')
            if (__backup_entry_4898113760 is __marker):
                del econtext['entry']
            else:
                econtext['entry'] = __backup_entry_4898113760
            __append('\n        </select>\n      </td>\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4896626512
            __attrs_4896626512 = _static_4659865408

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n        ')

            # <Static value=<ast.Dict object at 0x123e57640> name=None at 123dc9150> -> __attrs_4896291600
            __attrs_4896291600 = _static_4897207872

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-sm btn-outline-secondary" name="from2toButton"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896290512
            __default_4896290512 = _DEFAULT_MARKER

            # <Substitution "string:javascript:from2to('${view/id}')" (64:26)> -> __attr_onClick
            __token = 2137
            try:
                __zt_tmp = __attrs_4896291600
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onClick = _static_4662095120('string', "javascript:from2to('${view/id}')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onClick = __quote(__attr_onClick, '"', '&quot;', 'javascript:from2to()', _DEFAULT_MARKER)
            if (__attr_onClick is not None):
                __append((' onClick="%s"' % __attr_onClick))
            __append(' type="button" value="&rarr;" >&rarr;</button>\n        ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4896278288
            __attrs_4896278288 = _static_4659865408

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n        ')

            # <Static value=<ast.Dict object at 0x123f52ce0> name=None at 123d768d0> -> __attrs_4897472592
            __attrs_4897472592 = _static_4898237664

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-sm btn-outline-secondary" name="to2fromButton"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897484368
            __default_4897484368 = _DEFAULT_MARKER

            # <Substitution "string:javascript:to2from('${view/id}')" (74:26)> -> __attr_onClick
            __token = 2497
            try:
                __zt_tmp = __attrs_4897472592
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onClick = _static_4662095120('string', "javascript:to2from('${view/id}')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onClick = __quote(__attr_onClick, '"', '&quot;', 'javascript:to2from()', _DEFAULT_MARKER)
            if (__attr_onClick is not None):
                __append((' onClick="%s"' % __attr_onClick))
            __append(' type="button" value="&larr;" >&larr;</button>\n      </td>\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4897475152
            __attrs_4897475152 = _static_4659865408

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n        ')

            # <Static value=<ast.Dict object at 0x123f51990> name=None at 123e9b610> -> __attrs_4897857168
            __attrs_4897857168 = _static_4898232720

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898451472
            __default_4898451472 = _DEFAULT_MARKER

            # <Substitution 'string:form-control ${view/klass}' (86:22)> -> __attr_class
            __token = 2849
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4662095120('string', 'form-control ${view/klass}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898447632
            __default_4898447632 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-to' (84:21)> -> __attr_id
            __token = 2758
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4662095120('string', '${view/id}-to', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', 'to', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898449488
            __default_4898449488 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}.to' (85:22)> -> __attr_name
            __token = 2802
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4662095120('string', '${view/name}.to', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'to', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898451920
            __default_4898451920 = _DEFAULT_MARKER

            # <Substitution 'view/size' (106:1)> -> __attr_size
            __token = 3689
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_4662095120('path', 'view/size', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', '5', _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898449808
            __default_4898449808 = _DEFAULT_MARKER

            # <Substitution 'view/style' (87:21)> -> __attr_style
            __token = 2907
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_4662095120('path', 'view/style', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898454928
            __default_4898454928 = _DEFAULT_MARKER

            # <Substitution 'view/title' (88:20)> -> __attr_title
            __token = 2942
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_4662095120('path', 'view/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898453200
            __default_4898453200 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (89:18)> -> __attr_lang
            __token = 2976
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4662095120('path', 'view/lang', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898451088
            __default_4898451088 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (90:20)> -> __attr_onclick
            __token = 3012
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_4662095120('path', 'view/onclick', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898444240
            __default_4898444240 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (91:22)> -> __attr_ondblclick
            __token = 3054
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_4662095120('path', 'view/ondblclick', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898442192
            __default_4898442192 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (92:22)> -> __attr_onmousedown
            __token = 3100
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_4662095120('path', 'view/onmousedown', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898452560
            __default_4898452560 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (93:19)> -> __attr_onmouseup
            __token = 3145
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_4662095120('path', 'view/onmouseup', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898443600
            __default_4898443600 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (94:20)> -> __attr_onmouseover
            __token = 3190
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_4662095120('path', 'view/onmouseover', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898449296
            __default_4898449296 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (95:19)> -> __attr_onmousemove
            __token = 3237
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_4662095120('path', 'view/onmousemove', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898441680
            __default_4898441680 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (96:17)> -> __attr_onmouseout
            __token = 3283
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_4662095120('path', 'view/onmouseout', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4898446544
            __default_4898446544 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (97:16)> -> __attr_onkeypress
            __token = 3328
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_4662095120('path', 'view/onkeypress', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894787024
            __default_4894787024 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (98:14)> -> __attr_onkeydown
            __token = 3372
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_4662095120('path', 'view/onkeydown', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894789072
            __default_4894789072 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (99:11)> -> __attr_onkeyup
            __token = 3413
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_4662095120('path', 'view/onkeyup', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894794640
            __default_4894794640 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (100:11)> -> __attr_disabled
            __token = 3453
            try:
                __zt_tmp = __attrs_4897857168
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

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894450320
            __default_4894450320 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (101:10)> -> __attr_tabindex
            __token = 3494
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_4662095120('path', 'view/tabindex', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897853584
            __default_4897853584 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (102:8)> -> __attr_onfocus
            __token = 3534
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_4662095120('path', 'view/onfocus', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897857424
            __default_4897857424 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (103:6)> -> __attr_onblur
            __token = 3572
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_4662095120('path', 'view/onblur', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897857936
            __default_4897857936 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (104:7)> -> __attr_onchange
            __token = 3611
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_4662095120('path', 'view/onchange', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897854992
            __default_4897854992 = _DEFAULT_MARKER

            # <Boolean 'view/multiple' (105:6)> -> __attr_multiple
            __token = 3652
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_multiple = _static_4662095120('path', 'view/multiple', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if (__attr_multiple is _DEFAULT_MARKER):
                __attr_multiple = None
            else:
                if __attr_multiple:
                    __attr_multiple = 'multiple'
                else:
                    __attr_multiple = None
            if (__attr_multiple is not None):
                __append((' multiple="%s"' % __attr_multiple))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897864848
            __default_4897864848 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (107:4)> -> __attr_required
            __token = 3726
            try:
                __zt_tmp = __attrs_4897857168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_4662095120('python', "view.required and 'required' or None", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))
            __append(' >\n          ')

            # <Static value=<ast.Dict object at 0x123f515a0> name=None at 123ef6cd0> -> __attrs_4897857808
            __attrs_4897857808 = _static_4898231712
            __backup_entry_4881927568 = get('entry', __marker)

            # <Value 'view/selectedItems' (110:36)> -> __iterator
            __token = 3858
            try:
                __zt_tmp = __attrs_4897857808
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_4662095120('path', 'view/selectedItems', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            (__iterator, ____index_4897855312, ) = getname('repeat')('entry', __iterator)
            econtext['entry'] = None
            for __item in __iterator:
                econtext['entry'] = __item

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897861840
                __default_4897861840 = _DEFAULT_MARKER

                # <Substitution 'entry/value' (113:26)> -> __attr_value
                __token = 3992
                try:
                    __zt_tmp = __attrs_4897857808
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_4662095120('path', 'entry/value', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' >')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897862608
                __default_4897862608 = _DEFAULT_MARKER

                # <Value 'nocall:entry/content' (111:31)> -> __cache_4897863056
                __token = 3909
                try:
                    __zt_tmp = __attrs_4897857808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4897863056 = _static_4662095120('nocall', 'entry/content', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'nocall:entry/content' (111:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 123ef6f50> -> __condition
                __expression = __cache_4897863056

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4897863056
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</option>')
                ____index_4897855312 -= 1
                if (____index_4897855312 > 0):
                    __append('\n          ')
            if (__backup_entry_4881927568 is __marker):
                del econtext['entry']
            else:
                econtext['entry'] = __backup_entry_4881927568
            __append('\n        </select>\n        ')

            # <Static value=<ast.Dict object at 0x123f52950> name=None at 123e49590> -> __attrs_4897148688
            __attrs_4897148688 = _static_4898236752

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897160016
            __default_4897160016 = _DEFAULT_MARKER

            # <Substitution 'string:${view/name}-empty-marker' (121:22)> -> __attr_name
            __token = 4222
            try:
                __zt_tmp = __attrs_4897148688
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_4662095120('string', '${view/name}-empty-marker', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', 'foo-empty-marker', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))
            __append(' type="hidden" />\n        ')

            # <Static value=<ast.Dict object at 0x123f51d80> name=None at 123e486d0> -> __attrs_4897145552
            __attrs_4897145552 = _static_4898233728

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897144912
            __default_4897144912 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-toDataContainer' (127:19)> -> __attr_id
            __token = 4405
            try:
                __zt_tmp = __attrs_4897145552
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_4662095120('string', '${view/id}-toDataContainer', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', 'toDataContainer', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))
            __append(' style="display: none" >\n          ')

            # <Static value=<ast.Dict object at 0x123f52e00> name=None at 123e4a510> -> __attrs_4897885200
            __attrs_4897885200 = _static_4898237952

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script type="text/javascript" >')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897155792
            __default_4897155792 = _DEFAULT_MARKER

            # <Value "string:copyDataForSubmit('${view/id}');" (131:31)> -> __cache_4897153040
            __token = 4538
            try:
                __zt_tmp = __attrs_4897885200
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4897153040 = _static_4662095120('string', "copyDataForSubmit('${view/id}');", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value "string:copyDataForSubmit('${view/id}');" (131:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 123e4bed0> -> __condition
            __expression = __cache_4897153040

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n          /*  ')

                # <Interpolation value=<Substitution '<![CDATA[ */\n          // initial copying of field "field.to" --> "field"\n          copyDataForSubmit("<i tal:replace="${view/id}"/>");\n          /* ]]>' (133:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 123effbd0> -> __content_4386234736
                __token = 4605
                __token = 4726
                try:
                    __zt_tmp = __attrs_4897885200
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4386234736 = _static_4662095120('path', 'view/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                __content_4386234736 = ('%s%s%s' % ('<![CDATA[ */\n          // initial copying of field "field.to" --> "field"\n          copyDataForSubmit("<i tal:replace="', (__content_4386234736 if (__content_4386234736 is not None) else ''), '"/>");\n          /* ]]>', ))
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
                __append(' */\n          ')
            else:
                __content = __cache_4897153040
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</script>\n        </span>\n      </td>\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4897895888
            __attrs_4897895888 = _static_4659865408

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n        ')

            # <Static value=<ast.Dict object at 0x123f504f0> name=None at 123efc910> -> __attrs_4896715152
            __attrs_4896715152 = _static_4898227440

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-sm btn-outline-secondary" name="upButton"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4897889040
            __default_4897889040 = _DEFAULT_MARKER

            # <Substitution "string:javascript:moveUp('${view/id}')" (147:26)> -> __attr_onClick
            __token = 5075
            try:
                __zt_tmp = __attrs_4896715152
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onClick = _static_4662095120('string', "javascript:moveUp('${view/id}')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onClick = __quote(__attr_onClick, '"', '&quot;', 'javascript:moveUp()', _DEFAULT_MARKER)
            if (__attr_onClick is not None):
                __append((' onClick="%s"' % __attr_onClick))
            __append(' type="button" value="&uarr;" >&uarr;</button>\n        ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4896708048
            __attrs_4896708048 = _static_4659865408

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n        ')

            # <Static value=<ast.Dict object at 0x123f53730> name=None at 123ddded0> -> __attrs_4896714320
            __attrs_4896714320 = _static_4898240304

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-sm btn-outline-secondary" name="downButton"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4896703248
            __default_4896703248 = _DEFAULT_MARKER

            # <Substitution "string:javascript:moveDown('${view/id}')" (157:26)> -> __attr_onClick
            __token = 5432
            try:
                __zt_tmp = __attrs_4896714320
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onClick = _static_4662095120('string', "javascript:moveDown('${view/id}')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_onClick = __quote(__attr_onClick, '"', '&quot;', 'javascript:moveDown()', _DEFAULT_MARKER)
            if (__attr_onClick is not None):
                __append((' onClick="%s"' % __attr_onClick))
            __append(' type="button" value="&darr;" >&darr;</button>\n      </td>\n    </tr>\n  </table>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }