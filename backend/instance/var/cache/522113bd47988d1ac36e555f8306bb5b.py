# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/contentmenu/contentmenu.pt'

__tokens = {64: ('view/menu', 2, 31), 106: (" python:context.restrictedTraverse('@@iconresolver'", 3, 31), 196: ('s view/toolbar_positi', 4, 36), 282: ('view/available', 6, 35), 374: ('menu', 9, 30), 426: ('menuItem/submenu', 11, 23), 469: (' menuItem/extra/i', 12, 25), 522: ("${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 14, 17), 524: ('menuItem/extra/li_class|nothing', 14, 19), 559: ("python:'dropend' if (submenu and toolbar_pos == 'side') else ''", 14, 54), 639: ('${menuItem/extra/id}', 15, 14), 641: ('menuItem/extra/id', 15, 16), 955: ('menuItem/extra/class | nothing', 24, 25), 1011: (" python:'label-%s' % state_class if state_class else '", 25, 24), 688: ("${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 18, 18), 690: ("python:'nav-link dropdown-toggle' if submenu else 'nav-link'", 18, 20), 779: ("${python:'false' if submenu else ''}", 19, 26), 781: ("python:'false' if submenu else ''", 19, 28), 1127: ("python:menuItem['action'] or 'javascript:void(0)'", 28, 18), 1196: (" python:'cursor: default;; pointer-events: none' if not menuItem['action'] else No", 29, 18), 1298: ('le menuItem/descript', 30, 16), 1426: ("python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", 35, 43), 1598: ('menuItem/title', 38, 31), 1734: ('${state_class}', 43, 25), 1736: ('state_class', 43, 27), 1781: ('menuItem/extra/stateTitle | nothing', 44, 31), 2010: ('submenu | nothing', 54, 27), 2109: ('${menuItem/title}', 58, 14), 2111: ('menuItem/title', 58, 16), 2179: ("python:toolbar_pos == 'top'", 59, 52), 2325: ('menuItem/extra/class | nothing', 62, 36), 2392: (" python:'label-%s' % state_class if state_class else '", 63, 35), 2483: ('e menuItem/extra/stateTitle|nothi', 64, 34), 2581: ('state_title', 66, 37), 2238: ('${state_class}', 60, 29), 2240: ('state_class', 60, 31), 2628: ('${state_title}', 68, 16), 2630: ('state_title', 68, 18), 2778: ('submenu', 73, 38), 2857: ('subMenuItem/extra/class | string:', 75, 37), 3002: ('subMenuItem/extra/separator|nothing', 78, 43), 3112: ('not:subMenuItem/action', 80, 43), 3231: ('is_separator', 83, 35), 3311: ('subMenuItem/title', 85, 48), 3581: ('not:is_separator', 92, 37), 3505: ('nav-link dropdown-item ${extra_class}', 91, 29), 3530: ('extra_class', 91, 54), 3668: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 94, 51), 3813: ('subMenuItem/title', 95, 48), 4131: ('subMenuItem/action', 104, 32), 4034: ('nav-link dropdown-item ${extra_class}', 102, 24), 4059: ('extra_class', 102, 49), 4209: ('subMenuItem/action', 106, 24), 4253: (' subMenuItem/descriptio', 107, 24), 4299: ('d subMenuItem/extra/id | nothi', 108, 20), 4370: ('al subMenuItem/extra/modal | noth', 109, 37), 4534: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 114, 49), 4678: ('subMenuItem/title', 116, 46), 4895: ('not:subMenuItem/action', 122, 37), 4842: ('${extra_class}', 121, 29), 4844: ('extra_class', 121, 31), 4985: ('subMenuItem/extra/id | nothing', 124, 27), 5102: ("python:'active' in extra_class", 127, 43), 5185: ("python:icons.tag('check')", 128, 51), 5280: ('subMenuItem/title', 130, 47)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878109760 = {'class': '${extra_class}', 'id': 'subMenuItem/extra/id | nothing', }
_static_4878120608 = {'class': 'nav-link dropdown-item ${extra_class}', 'href': '#', 'title': 'subMenuItem/description', 'id': 'subMenuItem/extra/id | nothing', 'data-pat-plone-modal': 'subMenuItem/extra/modal | nothing', }
_static_4878118400 = {'class': 'nav-link dropdown-item ${extra_class}', }
_static_4878113168 = {'class': 'dropdown-header', }
_static_4878242896 = {'class': '${state_class}', }
_static_4878253792 = {'class': 'dropdown-header', }
_static_4878238816 = {'class': 'dropdown-menu', }
_static_4878246928 = {'class': '${state_class}', }
_static_4878246496 = {'class': 'toolbar-label', }
_static_4878242704 = {'class': "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 'aria-expanded': "${python:'false' if submenu else ''}", 'href': '#', 'data-bs-offset': '0,0', 'data-bs-toggle': 'dropdown', 'style': "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None", 'title': 'menuItem/description', }
_static_4873387072 = {'class': "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 'id': '${menuItem/extra/id}', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4659141008
            __attrs_4659141008 = _static_4659865408
            __backup_menu_4878793408 = get('menu', __marker)

            # <Value 'view/menu' (2:31)> -> __value
            __token = 64
            try:
                __zt_tmp = __attrs_4659141008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/menu', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['menu'] = __value
            __backup_icons_4873386736 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (3:31)> -> __value
            __token = 106
            try:
                __zt_tmp = __attrs_4659141008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_toolbar_pos_4878792688 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (4:36)> -> __value
            __token = 196
            try:
                __zt_tmp = __attrs_4659141008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/toolbar_position', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'view/available' (6:35)> -> __condition
            __token = 282
            try:
                __zt_tmp = __attrs_4659141008
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'view/available', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4665586576 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675936144
                __attrs_4675936144 = _static_4659865408
                __backup_menuItem_4878322368 = get('menuItem', __marker)

                # <Value 'menu' (9:30)> -> __iterator
                __token = 374
                try:
                    __zt_tmp = __attrs_4675936144
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'menu', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4670198096, ) = getname('repeat')('menuItem', __iterator)
                econtext['menuItem'] = None
                for __item in __iterator:
                    econtext['menuItem'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675200016
                    __attrs_4675200016 = _static_4659865408
                    __backup_submenu_4878324864 = get('submenu', __marker)

                    # <Value 'menuItem/submenu' (11:23)> -> __value
                    __token = 426
                    try:
                        __zt_tmp = __attrs_4675200016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'menuItem/submenu', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['submenu'] = __value
                    __backup_identifier_4878788848 = get('identifier', __marker)

                    # <Value 'menuItem/extra/id' (12:25)> -> __value
                    __token = 469
                    try:
                        __zt_tmp = __attrs_4675200016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'menuItem/extra/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['identifier'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x12279fc40> name=None at 116a9c590> -> __attrs_4684652944
                    __attrs_4684652944 = _static_4873387072

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670512528
                    __default_4670512528 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}" (14:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11638db10> -> __attr_class
                    __token = 522
                    __token = 524
                    try:
                        __zt_tmp = __attrs_4684652944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4662095120('path', 'menuItem/extra/li_class|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 559
                    try:
                        __zt_tmp = __attrs_4684652944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_557 = _static_4662095120('python', "'dropend' if (submenu and toolbar_pos == 'side') else ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class_557 = __quote(__attr_class_557, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s%s' % ((__attr_class if (__attr_class is not None) else ''), ' ', (__attr_class_557 if (__attr_class_557 is not None) else ''), ))
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

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684446608
                    __default_4684446608 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${menuItem/extra/id}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11736e050> -> __attr_id
                    __token = 639
                    __token = 641
                    try:
                        __zt_tmp = __attrs_4684652944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_4662095120('path', 'menuItem/extra/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_id = __attr_id
                    if (__attr_id is None):
                        pass
                    else:
                        if (__attr_id is _DEFAULT_MARKER):
                            __attr_id = None
                        else:
                            __tt = type(__attr_id)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_id = str(__attr_id)
                            else:
                                if (__tt is bytes):
                                    __attr_id = decode(__attr_id)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_id = __attr_id.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_id)
                                            __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                        else:
                                            __attr_id = __attr_id()
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n\n        ')

                    # <Static value=<ast.Dict object at 0x122c41390> name=None at 1165e7e90> -> __attrs_4673620688
                    __attrs_4673620688 = _static_4878242704
                    __backup_state_class_4878333216 = get('state_class', __marker)

                    # <Value 'menuItem/extra/class | nothing' (24:25)> -> __value
                    __token = 955
                    try:
                        __zt_tmp = __attrs_4673620688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['state_class'] = __value
                    __backup_state_class_4878367616 = get('state_class', __marker)

                    # <Value "python:'label-%s' % state_class if state_class else ''" (25:24)> -> __value
                    __token = 1011
                    try:
                        __zt_tmp = __attrs_4673620688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['state_class'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4672413200
                    __default_4672413200 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116b23bd0> -> __attr_class
                    __token = 688
                    __token = 690
                    try:
                        __zt_tmp = __attrs_4673620688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4662095120('python', "'nav-link dropdown-toggle' if submenu else 'nav-link'", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = __attr_class
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

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670950800
                    __default_4670950800 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'false' if submenu else ''}" (19:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11661c910> -> __attr_aria_expanded
                    __token = 779
                    __token = 781
                    try:
                        __zt_tmp = __attrs_4673620688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_aria_expanded = _static_4662095120('python', "'false' if submenu else ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_aria_expanded = __quote(__attr_aria_expanded, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_aria_expanded = __attr_aria_expanded
                    if (__attr_aria_expanded is None):
                        pass
                    else:
                        if (__attr_aria_expanded is _DEFAULT_MARKER):
                            __attr_aria_expanded = None
                        else:
                            __tt = type(__attr_aria_expanded)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_aria_expanded = str(__attr_aria_expanded)
                            else:
                                if (__tt is bytes):
                                    __attr_aria_expanded = decode(__attr_aria_expanded)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_aria_expanded = __attr_aria_expanded.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_aria_expanded)
                                            __attr_aria_expanded = (str(__attr_aria_expanded) if (__attr_aria_expanded is __converted) else __converted)
                                        else:
                                            __attr_aria_expanded = __attr_aria_expanded()
                    if (__attr_aria_expanded is not None):
                        __append((' aria-expanded="%s"' % __attr_aria_expanded))

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681057872
                    __default_4681057872 = _DEFAULT_MARKER

                    # <Substitution "python:menuItem['action'] or 'javascript:void(0)'" (28:18)> -> __attr_href
                    __token = 1127
                    try:
                        __zt_tmp = __attrs_4673620688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('python', "menuItem['action'] or 'javascript:void(0)'", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' data-bs-offset="0,0" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670390416
                    __default_4670390416 = _DEFAULT_MARKER

                    # <Substitution "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None" (29:18)> -> __attr_style
                    __token = 1196
                    try:
                        __zt_tmp = __attrs_4673620688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_4662095120('python', "'cursor: default; pointer-events: none' if not menuItem['action'] else None", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((' style="%s"' % __attr_style))

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673634128
                    __default_4673634128 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution 'menuItem/description' (30:16)> at 11691f590> -> __attr_title

                    # <Substitution 'menuItem/description' (30:16)> -> __attr_title
                    __token = 1298
                    try:
                        __zt_tmp = __attrs_4673620688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_4662095120('path', 'menuItem/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n\n          ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684268368
                    __attrs_4684268368 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688420560
                    __default_4688420560 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (35:43)> -> __cache_4688422608
                    __token = 1426
                    try:
                        __zt_tmp = __attrs_4684268368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4688422608 = _static_4662095120('python', "icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (35:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117739650> -> __condition
                    __expression = __cache_4688422608

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4688422608
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x122c42260> name=None at 1173442d0> -> __attrs_4677722256
                    __attrs_4677722256 = _static_4878246496

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label">\n            ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686309968
                    __attrs_4686309968 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686314768
                    __default_4686314768 = _DEFAULT_MARKER

                    # <Value 'menuItem/title' (38:31)> -> __cache_4686300432
                    __token = 1598
                    try:
                        __zt_tmp = __attrs_4686309968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4686300432 = _static_4662095120('path', 'menuItem/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/title' (38:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117536710> -> __condition
                    __expression = __cache_4686300432

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n              Menu Title\n            </span>')
                    else:
                        __content = __cache_4686300432
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x122c42410> name=None at 117536f50> -> __attrs_4686313104
                    __attrs_4686313104 = _static_4878246928

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686310864
                    __default_4686310864 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${state_class}' (43:25)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1175342d0> -> __attr_class
                    __token = 1734
                    __token = 1736
                    try:
                        __zt_tmp = __attrs_4686313104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4662095120('path', 'state_class', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = __attr_class
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
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686308048
                    __default_4686308048 = _DEFAULT_MARKER

                    # <Value 'menuItem/extra/stateTitle | nothing' (44:31)> -> __cache_4686300688
                    __token = 1781
                    try:
                        __zt_tmp = __attrs_4686313104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4686300688 = _static_4662095120('path', 'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/extra/stateTitle | nothing' (44:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117536b10> -> __condition
                    __expression = __cache_4686300688

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                State title\n            ')
                    else:
                        __content = __cache_4686300688
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n          </span>\n\n        </a>')
                    if (__backup_state_class_4878367616 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_4878367616
                    if (__backup_state_class_4878333216 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_4878333216
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x122c40460> name=None at 117537390> -> __attrs_4686303248
                    __attrs_4686303248 = _static_4878238816

                    # <Value 'submenu | nothing' (54:27)> -> __condition
                    __token = 2010
                    try:
                        __zt_tmp = __attrs_4686303248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'submenu | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="dropdown-menu" >\n          ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674720912
                        __attrs_4674720912 = _static_4659865408

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n            ')

                        # <Static value=<ast.Dict object at 0x122c43ee0> name=None at 116a29750> -> __attrs_4674722768
                        __attrs_4674722768 = _static_4878253792

                        # <h6 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h6 class="dropdown-header">')

                        # <Interpolation value=<Substitution '\n              ${menuItem/title}\n              ' (57:40)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116a2a890> -> __content_4386234736
                        __token = 2109
                        __token = 2111
                        try:
                            __zt_tmp = __attrs_4674722768
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4386234736 = _static_4662095120('path', 'menuItem/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __content_4386234736 = __quote(__content_4386234736, '\x00', '&#0;', None, None)
                        __content_4386234736 = ('%s%s%s' % ('\n              ', (__content_4386234736 if (__content_4386234736 is not None) else ''), '\n              ', ))
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

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674724688
                        __attrs_4674724688 = _static_4659865408

                        # <Value "python:toolbar_pos == 'top'" (59:52)> -> __condition
                        __token = 2179
                        try:
                            __zt_tmp = __attrs_4674724688
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('python', "toolbar_pos == 'top'", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x122c41450> name=None at 1166f66d0> -> __attrs_4681425232
                            __attrs_4681425232 = _static_4878242896
                            __backup_state_class_4878247216 = get('state_class', __marker)

                            # <Value 'menuItem/extra/class | nothing' (62:36)> -> __value
                            __token = 2325
                            try:
                                __zt_tmp = __attrs_4681425232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['state_class'] = __value
                            __backup_state_class_4878242944 = get('state_class', __marker)

                            # <Value "python:'label-%s' % state_class if state_class else ''" (63:35)> -> __value
                            __token = 2392
                            try:
                                __zt_tmp = __attrs_4681425232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['state_class'] = __value
                            __backup_state_title_4878252064 = get('state_title', __marker)

                            # <Value 'menuItem/extra/stateTitle|nothing' (64:34)> -> __value
                            __token = 2483
                            try:
                                __zt_tmp = __attrs_4681425232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('path', 'menuItem/extra/stateTitle|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['state_title'] = __value

                            # <Value 'state_title' (66:37)> -> __condition
                            __token = 2581
                            try:
                                __zt_tmp = __attrs_4681425232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4662095120('path', 'state_title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span')

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681429968
                                __default_4681429968 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution '${state_class}' (60:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11708dcd0> -> __attr_class
                                __token = 2238
                                __token = 2240
                                try:
                                    __zt_tmp = __attrs_4681425232
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_4662095120('path', 'state_class', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_class = __attr_class
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
                                __append(' >')

                                # <Interpolation value=<Substitution '\n                ${state_title}\n                ' (67:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11662e110> -> __content_4386234736
                                __token = 2628
                                __token = 2630
                                try:
                                    __zt_tmp = __attrs_4681425232
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_4386234736 = _static_4662095120('path', 'state_title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                __content_4386234736 = __quote(__content_4386234736, '\x00', '&#0;', None, None)
                                __content_4386234736 = ('%s%s%s' % ('\n                ', (__content_4386234736 if (__content_4386234736 is not None) else ''), '\n                ', ))
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
                                __append('</span>')
                            if (__backup_state_title_4878252064 is __marker):
                                del econtext['state_title']
                            else:
                                econtext['state_title'] = __backup_state_title_4878252064
                            if (__backup_state_class_4878242944 is __marker):
                                del econtext['state_class']
                            else:
                                econtext['state_class'] = __backup_state_class_4878242944
                            if (__backup_state_class_4878247216 is __marker):
                                del econtext['state_class']
                            else:
                                econtext['state_class'] = __backup_state_class_4878247216
                            __append('\n              ')
                        __append('\n            </h6>\n          </li>\n          ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670539600
                        __attrs_4670539600 = _static_4659865408
                        __backup_subMenuItem_4878245440 = get('subMenuItem', __marker)

                        # <Value 'submenu' (73:38)> -> __iterator
                        __token = 2778
                        try:
                            __zt_tmp = __attrs_4670539600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4662095120('path', 'submenu', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        (__iterator, ____index_4670543184, ) = getname('repeat')('subMenuItem', __iterator)
                        econtext['subMenuItem'] = None
                        for __item in __iterator:
                            econtext['subMenuItem'] = __item

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li>\n            ')

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4669649872
                            __attrs_4669649872 = _static_4659865408
                            __backup_extra_class_4878246400 = get('extra_class', __marker)

                            # <Value 'subMenuItem/extra/class | string:' (75:37)> -> __value
                            __token = 2857
                            try:
                                __zt_tmp = __attrs_4669649872
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('path', 'subMenuItem/extra/class | string:', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['extra_class'] = __value
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676772752
                            __attrs_4676772752 = _static_4659865408
                            __backup_is_separator_4878247312 = get('is_separator', __marker)

                            # <Value 'subMenuItem/extra/separator|nothing' (78:43)> -> __value
                            __token = 3002
                            try:
                                __zt_tmp = __attrs_4676772752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('path', 'subMenuItem/extra/separator|nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['is_separator'] = __value

                            # <Value 'not:subMenuItem/action' (80:43)> -> __condition
                            __token = 3112
                            try:
                                __zt_tmp = __attrs_4676772752
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4662095120('not', 'subMenuItem/action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            if __condition:
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x122c21990> name=None at 116c1ffd0> -> __attrs_4663239760
                                __attrs_4663239760 = _static_4878113168

                                # <Value 'is_separator' (83:35)> -> __condition
                                __token = 3231
                                try:
                                    __zt_tmp = __attrs_4663239760
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4662095120('path', 'is_separator', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                if __condition:

                                    # <h6 ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<h6 class="dropdown-header" >\n                  ')

                                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674829328
                                    __attrs_4674829328 = _static_4659865408

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674821456
                                    __default_4674821456 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (85:48)> -> __cache_4674827408
                                    __token = 3311
                                    try:
                                        __zt_tmp = __attrs_4674829328
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_4674827408 = _static_4662095120('path', 'subMenuItem/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (85:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116a43650> -> __condition
                                    __expression = __cache_4674827408

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append('\n                    Title\n                  ')
                                    else:
                                        __content = __cache_4674827408
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </h6>')
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x122c22e00> name=None at 116a43e10> -> __attrs_4686520080
                                __attrs_4686520080 = _static_4878118400

                                # <Value 'not:is_separator' (92:37)> -> __condition
                                __token = 3581
                                try:
                                    __zt_tmp = __attrs_4686520080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4662095120('not', 'is_separator', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686521872
                                    __default_4686521872 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (91:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11756a250> -> __attr_class
                                    __token = 3505
                                    __token = 3530
                                    try:
                                        __zt_tmp = __attrs_4686520080
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_4662095120('path', 'extra_class', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = ('%s%s' % ('nav-link dropdown-item ', (__attr_class if (__attr_class is not None) else ''), ))
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
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686522320
                                    __attrs_4686522320 = _static_4659865408

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686524496
                                    __default_4686524496 = _DEFAULT_MARKER

                                    # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (94:51)> -> __cache_4686513936
                                    __token = 3668
                                    try:
                                        __zt_tmp = __attrs_4686522320
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_4686513936 = _static_4662095120('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                    # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (94:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117568110> -> __condition
                                    __expression = __cache_4686513936

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_4686513936
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                  ')

                                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4677832400
                                    __attrs_4677832400 = _static_4659865408

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4654189584
                                    __default_4654189584 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (95:48)> -> __cache_4654187472
                                    __token = 3813
                                    try:
                                        __zt_tmp = __attrs_4677832400
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_4654187472 = _static_4662095120('path', 'subMenuItem/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (95:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 115695ed0> -> __condition
                                    __expression = __cache_4654187472

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append('\n                    Title\n                  ')
                                    else:
                                        __content = __cache_4654187472
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </span>')
                                __append('\n              ')
                            if (__backup_is_separator_4878247312 is __marker):
                                del econtext['is_separator']
                            else:
                                econtext['is_separator'] = __backup_is_separator_4878247312
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x122c236a0> name=None at 116c1f690> -> __attrs_4676107280
                            __attrs_4676107280 = _static_4878120608

                            # <Value 'subMenuItem/action' (104:32)> -> __condition
                            __token = 4131
                            try:
                                __zt_tmp = __attrs_4676107280
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4662095120('path', 'subMenuItem/action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4677835856
                                __default_4677835856 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (102:24)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116d21a90> -> __attr_class
                                __token = 4034
                                __token = 4059
                                try:
                                    __zt_tmp = __attrs_4676107280
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_4662095120('path', 'extra_class', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_class = ('%s%s' % ('nav-link dropdown-item ', (__attr_class if (__attr_class is not None) else ''), ))
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

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4677837520
                                __default_4677837520 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/action' (106:24)> -> __attr_href
                                __token = 4209
                                try:
                                    __zt_tmp = __attrs_4676107280
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_4662095120('path', 'subMenuItem/action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673673040
                                __default_4673673040 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<Substitution 'subMenuItem/description' (107:24)> at 116d22410> -> __attr_title

                                # <Substitution 'subMenuItem/description' (107:24)> -> __attr_title
                                __token = 4253
                                try:
                                    __zt_tmp = __attrs_4676107280
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_title = _static_4662095120('path', 'subMenuItem/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_title is not None):
                                    __append((' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673677072
                                __default_4673677072 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/id | nothing' (108:20)> -> __attr_id
                                __token = 4299
                                try:
                                    __zt_tmp = __attrs_4676107280
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_4662095120('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673668560
                                __default_4673668560 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/modal | nothing' (109:37)> -> __attr_data_pat_plone_modal
                                __token = 4370
                                try:
                                    __zt_tmp = __attrs_4676107280
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_data_pat_plone_modal = _static_4662095120('path', 'subMenuItem/extra/modal | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_data_pat_plone_modal is not None):
                                    __append((' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                                __append(' >\n\n                ')

                                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4654728336
                                __attrs_4654728336 = _static_4659865408

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4654733008
                                __default_4654733008 = _DEFAULT_MARKER

                                # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (114:49)> -> __cache_4676095632
                                __token = 4534
                                try:
                                    __zt_tmp = __attrs_4654728336
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4676095632 = _static_4662095120('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (114:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116b786d0> -> __condition
                                __expression = __cache_4676095632

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_4676095632
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n\n                ')

                                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683067600
                                __attrs_4683067600 = _static_4659865408

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4683061520
                                __default_4683061520 = _DEFAULT_MARKER

                                # <Value 'subMenuItem/title' (116:46)> -> __cache_4654737040
                                __token = 4678
                                try:
                                    __zt_tmp = __attrs_4683067600
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4654737040 = _static_4662095120('path', 'subMenuItem/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                # <BinOp left=<Value 'subMenuItem/title' (116:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 115719310> -> __condition
                                __expression = __cache_4654737040

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Title\n                ')
                                else:
                                    __content = __cache_4654737040
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x122c20c40> name=None at 11721cdd0> -> __attrs_4671955792
                                __attrs_4671955792 = _static_4878109760

                                # <Value 'not:subMenuItem/action' (122:37)> -> __condition
                                __token = 4895
                                try:
                                    __zt_tmp = __attrs_4671955792
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4662095120('not', 'subMenuItem/action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671957712
                                    __default_4671957712 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution '${extra_class}' (121:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11721c650> -> __attr_class
                                    __token = 4842
                                    __token = 4844
                                    try:
                                        __zt_tmp = __attrs_4671955792
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_4662095120('path', 'extra_class', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = __attr_class
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

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671955856
                                    __default_4671955856 = _DEFAULT_MARKER

                                    # <Substitution 'subMenuItem/extra/id | nothing' (124:27)> -> __attr_id
                                    __token = 4985
                                    try:
                                        __zt_tmp = __attrs_4671955792
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_4662095120('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4653226896
                                    __attrs_4653226896 = _static_4659865408

                                    # <Value "python:'active' in extra_class" (127:43)> -> __condition
                                    __token = 5102
                                    try:
                                        __zt_tmp = __attrs_4653226896
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_4662095120('python', "'active' in extra_class", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                    if __condition:

                                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4672438480
                                        __default_4672438480 = _DEFAULT_MARKER

                                        # <Value "python:icons.tag('check')" (128:51)> -> __cache_4671952784
                                        __token = 5185
                                        try:
                                            __zt_tmp = __attrs_4653226896
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_4671952784 = _static_4662095120('python', "icons.tag('check')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                        # <BinOp left=<Value "python:icons.tag('check')" (128:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116784750> -> __condition
                                        __expression = __cache_4671952784

                                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            pass
                                        else:
                                            __content = __cache_4671952784
                                            __content = __convert(__content)
                                            if (__content is not None):
                                                __append(__content)
                                    __append('\n                  ')

                                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671184592
                                    __attrs_4671184592 = _static_4659865408

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671178256
                                    __default_4671178256 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (130:47)> -> __cache_4681801936
                                    __token = 5280
                                    try:
                                        __zt_tmp = __attrs_4671184592
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_4681801936 = _static_4662095120('path', 'subMenuItem/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (130:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1166cbb10> -> __condition
                                    __expression = __cache_4681801936

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<span >\n                    Title\n                  </span>')
                                    else:
                                        __content = __cache_4681801936
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </span>')
                                __append('\n              </a>')
                            __append('\n            ')
                            if (__backup_extra_class_4878246400 is __marker):
                                del econtext['extra_class']
                            else:
                                econtext['extra_class'] = __backup_extra_class_4878246400
                            __append('\n          </li>')
                            ____index_4670543184 -= 1
                            if (____index_4670543184 > 0):
                                __append('\n          ')
                        if (__backup_subMenuItem_4878245440 is __marker):
                            del econtext['subMenuItem']
                        else:
                            econtext['subMenuItem'] = __backup_subMenuItem_4878245440
                        __append('\n        </ul>')
                    __append('\n\n      </li>\n    ')
                    if (__backup_identifier_4878788848 is __marker):
                        del econtext['identifier']
                    else:
                        econtext['identifier'] = __backup_identifier_4878788848
                    if (__backup_submenu_4878324864 is __marker):
                        del econtext['submenu']
                    else:
                        econtext['submenu'] = __backup_submenu_4878324864
                    __append('\n  ')
                    ____index_4670198096 -= 1
                    if (____index_4670198096 > 0):
                        __append('')
                if (__backup_menuItem_4878322368 is __marker):
                    del econtext['menuItem']
                else:
                    econtext['menuItem'] = __backup_menuItem_4878322368
                __append('\n')
                __i18n_domain = __previous_i18n_domain_4665586576
            if (__backup_toolbar_pos_4878792688 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_4878792688
            if (__backup_icons_4873386736 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4873386736
            if (__backup_menu_4878793408 is __marker):
                del econtext['menu']
            else:
                econtext['menu'] = __backup_menu_4878793408
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }