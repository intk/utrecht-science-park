# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/Products/CMFPlone/controlpanel/browser/prefsmaintemplate.pt'

__tokens = {256: ("python:request.set('disable_border',1)", 6, 43), 345: (" python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel'", 7, 49), 485: ("e python:request.set('disable_plone.leftcolumn', ", 8, 54), 591: ("wo python:request.set('disable_plone.rightcolumn'", 9, 53), 1074: ("python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", 21, 46), 1198: (" python:controlPanel.getGroups('site'", 22, 39), 1278: ('l controlPanel/site_u', 23, 40), 1345: ('rl request/', 24, 42), 1496: ('string:$portal_url/@@overview-controlpanel', 27, 49), 1573: ("nav-link ${python:'active' if overview_url in current_url else ''}", 28, 32), 1584: ("python:'active' if overview_url in current_url else ''", 28, 43), 1667: ('${overview_url}', 28, 126), 1669: ('overview_url', 28, 128), 1792: ('groups', 30, 49), 1850: ("python:controlPanel.enumConfiglets(group=group['id'])", 31, 49), 1949: (" python:'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive", 32, 44), 2093: ('python:configlets and controlPanel.maySeeSomeConfiglets', 33, 41), 2237: ('nav-link dropdown-toggle ${active}', 35, 34), 2264: ('active', 35, 61), 2344: ('${group/title}', 35, 141), 2346: ('group/title', 35, 143), 2474: ('configlets', 37, 58), 2534: ('configlet/visible', 38, 47), 2608: ("python:'http' in configlet['icon']", 39, 54), 2738: ('${configlet/url}', 41, 39), 2740: ('configlet/url', 41, 41), 2809: ('icon_url', 42, 52), 2938: ('configlet/icon', 44, 56), 3009: (' configlet/titl', 45, 55), 3143: ('not: icon_url', 47, 57), 3223: ("python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])", 48, 65), 3347: ('${configlet/title}', 49, 32), 3349: ('configlet/title', 49, 34), 3694: ('nothing', 59, 82), 898: ('context/@@main_template/macros/content', 17, 42), 898: ('context/@@main_template/macros/content', 17, 42), 85: ('context/@@main_template/macros/master', 2, 30), 85: ('context/@@main_template/macros/master', 2, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_4881144640 = {'src': '', 'alt': '', 'class': 'icon', }
_static_4881138976 = {'class': 'dropdown-item', 'href': '${configlet/url}', }
_static_4881142096 = {'class': 'dropdown-menu', }
_static_4881138592 = {'class': 'nav-link dropdown-toggle ${active}', 'data-bs-toggle': 'dropdown', 'href': '#', 'role': 'button', 'aria-expanded': 'false', }
_static_4881141040 = {'class': 'nav-item dropdown', }
_static_4881141376 = {'class': "nav-link ${python:'active' if overview_url in current_url else ''}", 'aria-current': 'page', 'href': '${overview_url}', }
_static_4881140224 = {'class': 'nav-item', }
_static_4881150160 = {'class': 'nav nav-tabs', }
_static_4881148336 = {'class': 'mb-3', }
_static_4881142912 = 'content'
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4881149968 = 'master'
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

    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_prefs_configlet_wrapper = econtext['__slot_prefs_configlet_wrapper'].pop()
        except:
            __slot_prefs_configlet_wrapper = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_prefs_configlet_main = econtext['__slot_prefs_configlet_main'].pop()
        except:
            __slot_prefs_configlet_main = None

        try:
            __slot_prefs_configlet_content = econtext['__slot_prefs_configlet_content'].pop()
        except:
            __slot_prefs_configlet_content = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671231824
            __attrs_4671231824 = _static_4659865408
            __previous_i18n_domain_4671242000 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671231568
            __attrs_4671231568 = _static_4659865408
            __backup_macroname_4683855424 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x122f07010> name=None at 1166d7790> -> __value
            __value = _static_4881149968
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671241232
                __attrs_4671241232 = _static_4659865408
                __append('\n        ')
                if (__slot_top_slot is None):

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671226128
                    __attrs_4671226128 = _static_4659865408
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671238608
                    __attrs_4671238608 = _static_4659865408
                    __backup_dummy_4878699488 = get('dummy', __marker)

                    # <Value "python:request.set('disable_border',1)" (6:43)> -> __value
                    __token = 256
                    try:
                        __zt_tmp = __attrs_4671238608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "request.set('disable_border',1)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['dummy'] = __value
                    __backup_controlPanel_4878702128 = get('controlPanel', __marker)

                    # <Value "python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (7:49)> -> __value
                    __token = 345
                    try:
                        __zt_tmp = __attrs_4671238608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['controlPanel'] = __value
                    __backup_disable_column_one_4878711632 = get('disable_column_one', __marker)

                    # <Value "python:request.set('disable_plone.leftcolumn', 1)" (8:54)> -> __value
                    __token = 485
                    try:
                        __zt_tmp = __attrs_4671238608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['disable_column_one'] = __value
                    __backup_disable_column_two_4878698192 = get('disable_column_two', __marker)

                    # <Value "python:request.set('disable_plone.rightcolumn',1)" (9:53)> -> __value
                    __token = 591
                    try:
                        __zt_tmp = __attrs_4671238608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['disable_column_two'] = __value
                    if (__backup_disable_column_two_4878698192 is __marker):
                        del econtext['disable_column_two']
                    else:
                        econtext['disable_column_two'] = __backup_disable_column_two_4878698192
                    if (__backup_disable_column_one_4878711632 is __marker):
                        del econtext['disable_column_one']
                    else:
                        econtext['disable_column_one'] = __backup_disable_column_one_4878711632
                    if (__backup_controlPanel_4878702128 is __marker):
                        del econtext['controlPanel']
                    else:
                        econtext['controlPanel'] = __backup_controlPanel_4878702128
                    if (__backup_dummy_4878699488 is __marker):
                        del econtext['dummy']
                    else:
                        econtext['dummy'] = __backup_dummy_4878699488
                    __append('\n        ')
                else:
                    __slot_top_slot(__stream, econtext.copy(), rcontext)
                __append('\n    ')
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671233744
                __attrs_4671233744 = _static_4659865408
                __append('\n        ')
                if (__slot_prefs_configlet_wrapper is None):

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671239632
                    __attrs_4671239632 = _static_4659865408
                    __append('\n          ')
                    if (__slot_prefs_configlet_content is None):

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683583888
                        __attrs_4683583888 = _static_4659865408
                        __append('\n\n            ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675020112
                        __attrs_4675020112 = _static_4659865408
                        __backup_macroname_4683136128 = get('macroname', __marker)

                        # <Static value=<ast.Constant object at 0x122f05480> name=None at 116c30210> -> __value
                        __value = _static_4881142912
                        econtext['macroname'] = __value

                        def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                            getname = econtext.get_name
                            get = econtext.get

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675013584
                            __attrs_4675013584 = _static_4659865408
                            __append('\n\n                ')

                            # <Static value=<ast.Dict object at 0x122f069b0> name=None at 116a72090> -> __attrs_4675018448
                            __attrs_4675018448 = _static_4881148336
                            __backup_controlPanel_4878701072 = get('controlPanel', __marker)

                            # <Value "python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (21:46)> -> __value
                            __token = 1074
                            try:
                                __zt_tmp = __attrs_4675018448
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('python', "modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['controlPanel'] = __value
                            __backup_groups_4878710672 = get('groups', __marker)

                            # <Value "python:controlPanel.getGroups('site')" (22:39)> -> __value
                            __token = 1198
                            try:
                                __zt_tmp = __attrs_4675018448
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('python', "controlPanel.getGroups('site')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['groups'] = __value
                            __backup_site_url_4878708656 = get('site_url', __marker)

                            # <Value 'controlPanel/site_url' (23:40)> -> __value
                            __token = 1278
                            try:
                                __zt_tmp = __attrs_4675018448
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('path', 'controlPanel/site_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['site_url'] = __value
                            __backup_current_url_4878707888 = get('current_url', __marker)

                            # <Value 'request/URL' (24:42)> -> __value
                            __token = 1345
                            try:
                                __zt_tmp = __attrs_4675018448
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('path', 'request/URL', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['current_url'] = __value

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="mb-3">\n                  ')

                            # <Static value=<ast.Dict object at 0x122f070d0> name=None at 116a72350> -> __attrs_4653859600
                            __attrs_4653859600 = _static_4881150160

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append('<ul class="nav nav-tabs">\n                    ')

                            # <Static value=<ast.Dict object at 0x122f04a00> name=None at 116553010> -> __attrs_4691201040
                            __attrs_4691201040 = _static_4881140224
                            __backup_overview_url_4878704048 = get('overview_url', __marker)

                            # <Value 'string:$portal_url/@@overview-controlpanel' (27:49)> -> __value
                            __token = 1496
                            try:
                                __zt_tmp = __attrs_4691201040
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_4662095120('string', '$portal_url/@@overview-controlpanel', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            econtext['overview_url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li class="nav-item">\n                      ')

                            # <Static value=<ast.Dict object at 0x122f04e80> name=None at 1165daf10> -> __attrs_4693340944
                            __attrs_4693340944 = _static_4881141376

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4693329872
                            __default_4693329872 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution "nav-link ${python:'active' if overview_url in current_url else ''}" (28:32)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117be8690> -> __attr_class
                            __token = 1573
                            __token = 1584
                            try:
                                __zt_tmp = __attrs_4693340944
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_4662095120('python', "'active' if overview_url in current_url else ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_class = ('%s%s' % ('nav-link ', (__attr_class if (__attr_class is not None) else ''), ))
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
                            __append(' aria-current="page"')

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4693338000
                            __default_4693338000 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${overview_url}' (28:126)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117bea490> -> __attr_href
                            __token = 1667
                            __token = 1669
                            try:
                                __zt_tmp = __attrs_4693340944
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_4662095120('path', 'overview_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                            __stream_4684654544 = []
                            __append_4684654544 = __stream_4684654544.append
                            __append_4684654544('Site Setup')
                            __msgid_4684654544 = __re_whitespace(''.join(__stream_4684654544)).strip()
                            if __msgid_4684654544:
                                __append(translate(__msgid_4684654544, mapping=None, default=__msgid_4684654544, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</a>\n                    </li>')
                            if (__backup_overview_url_4878704048 is __marker):
                                del econtext['overview_url']
                            else:
                                econtext['overview_url'] = __backup_overview_url_4878704048
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4862948944
                            __attrs_4862948944 = _static_4659865408
                            __backup_group_4878582880 = get('group', __marker)

                            # <Value 'groups' (30:49)> -> __iterator
                            __token = 1792
                            try:
                                __zt_tmp = __attrs_4862948944
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __iterator = _static_4662095120('path', 'groups', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            (__iterator, ____index_4691284624, ) = getname('repeat')('group', __iterator)
                            econtext['group'] = None
                            for __item in __iterator:
                                econtext['group'] = __item
                                __append('\n                      ')

                                # <Static value=<ast.Dict object at 0x122f04d30> name=None at 1179f53d0> -> __attrs_4691287056
                                __attrs_4691287056 = _static_4881141040
                                __backup_configlets_4878697520 = get('configlets', __marker)

                                # <Value "python:controlPanel.enumConfiglets(group=group['id'])" (31:49)> -> __value
                                __token = 1850
                                try:
                                    __zt_tmp = __attrs_4691287056
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_4662095120('python', "controlPanel.enumConfiglets(group=group['id'])", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                econtext['configlets'] = __value
                                __backup_active_4878699296 = get('active', __marker)

                                # <Value "python:'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive'" (32:44)> -> __value
                                __token = 1949
                                try:
                                    __zt_tmp = __attrs_4691287056
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_4662095120('python', "'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive'", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                econtext['active'] = __value

                                # <Value 'python:configlets and controlPanel.maySeeSomeConfiglets' (33:41)> -> __condition
                                __token = 2093
                                try:
                                    __zt_tmp = __attrs_4691287056
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_4662095120('python', 'configlets and controlPanel.maySeeSomeConfiglets', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                if __condition:

                                    # <li ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<li class="nav-item dropdown">\n                        ')

                                    # <Static value=<ast.Dict object at 0x122f043a0> name=None at 1179f5e50> -> __attrs_4692514448
                                    __attrs_4692514448 = _static_4881138592

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a')

                                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866352528
                                    __default_4866352528 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution 'nav-link dropdown-toggle ${active}' (35:34)> braces_required=True translation=False default='"?"' default_marker='"?"' at 121e63b10> -> __attr_class
                                    __token = 2237
                                    __token = 2264
                                    try:
                                        __zt_tmp = __attrs_4692514448
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_4662095120('path', 'active', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = ('%s%s' % ('nav-link dropdown-toggle ', (__attr_class if (__attr_class is not None) else ''), ))
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
                                    __append(' data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">')

                                    # <Interpolation value=<Substitution '${group/title}' (35:141)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117b20790> -> __content_4386234736
                                    __token = 2344
                                    __token = 2346
                                    try:
                                        __zt_tmp = __attrs_4692514448
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __content_4386234736 = _static_4662095120('path', 'group/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                                    __append('</a>\n                          ')

                                    # <Static value=<ast.Dict object at 0x122f05150> name=None at 122195c90> -> __attrs_4867061968
                                    __attrs_4867061968 = _static_4881142096

                                    # <ul ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<ul class="dropdown-menu">\n                          ')

                                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4867063120
                                    __attrs_4867063120 = _static_4659865408
                                    __backup_configlet_4881151216 = get('configlet', __marker)

                                    # <Value 'configlets' (37:58)> -> __iterator
                                    __token = 2474
                                    try:
                                        __zt_tmp = __attrs_4867063120
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __iterator = _static_4662095120('path', 'configlets', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                    (__iterator, ____index_4684895952, ) = getname('repeat')('configlet', __iterator)
                                    econtext['configlet'] = None
                                    for __item in __iterator:
                                        econtext['configlet'] = __item
                                        __append('\n                            ')

                                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4867365136
                                        __attrs_4867365136 = _static_4659865408

                                        # <Value 'configlet/visible' (38:47)> -> __condition
                                        __token = 2534
                                        try:
                                            __zt_tmp = __attrs_4867365136
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_4662095120('path', 'configlet/visible', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                        if __condition:

                                            # <li ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<li>\n                              ')

                                            # <Static value=<ast.Dict object at 0x122f04520> name=None at 1221e1690> -> __attrs_4867366416
                                            __attrs_4867366416 = _static_4881138976
                                            __backup_icon_url_4878700928 = get('icon_url', __marker)

                                            # <Value "python:'http' in configlet['icon']" (39:54)> -> __value
                                            __token = 2608
                                            try:
                                                __zt_tmp = __attrs_4867366416
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __value = _static_4662095120('python', "'http' in configlet['icon']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                            econtext['icon_url'] = __value

                                            # <a ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<a class="dropdown-item"')

                                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4867363728
                                            __default_4867363728 = _DEFAULT_MARKER

                                            # <Interpolation value=<Substitution '${configlet/url}' (41:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1221e2cd0> -> __attr_href
                                            __token = 2738
                                            __token = 2740
                                            try:
                                                __zt_tmp = __attrs_4867366416
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_href = _static_4662095120('path', 'configlet/url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                                            __append('>\n                                ')

                                            # <Static value=<ast.Dict object at 0x122f05b40> name=None at 1221e0d90> -> __attrs_4688526288
                                            __attrs_4688526288 = _static_4881144640

                                            # <Value 'icon_url' (42:52)> -> __condition
                                            __token = 2809
                                            try:
                                                __zt_tmp = __attrs_4688526288
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __condition = _static_4662095120('path', 'icon_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                            if __condition:

                                                # <img ... (0:0)
                                                # --------------------------------------------------------
                                                __append('<img')

                                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688515600
                                                __default_4688515600 = _DEFAULT_MARKER

                                                # <Substitution 'configlet/icon' (44:56)> -> __attr_src
                                                __token = 2938
                                                try:
                                                    __zt_tmp = __attrs_4688526288
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __attr_src = _static_4662095120('path', 'configlet/icon', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                                __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                                if (__attr_src is not None):
                                                    __append((' src="%s"' % __attr_src))

                                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688524816
                                                __default_4688524816 = _DEFAULT_MARKER

                                                # <Translate msgid=None node=<Substitution 'configlet/title' (45:55)> at 117753050> -> __attr_alt

                                                # <Substitution 'configlet/title' (45:55)> -> __attr_alt
                                                __token = 3009
                                                try:
                                                    __zt_tmp = __attrs_4688526288
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __attr_alt = _static_4662095120('path', 'configlet/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                                __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                                __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                                if (__attr_alt is not None):
                                                    __append((' alt="%s"' % __attr_alt))
                                                __append(' class="icon">')
                                            __append('\n                                ')

                                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4688523920
                                            __attrs_4688523920 = _static_4659865408

                                            # <Value 'not: icon_url' (47:57)> -> __condition
                                            __token = 3143
                                            try:
                                                __zt_tmp = __attrs_4688523920
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __condition = _static_4662095120('not', ' icon_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                            if __condition:

                                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686918672
                                                __default_4686918672 = _DEFAULT_MARKER

                                                # <Value "python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])" (48:65)> -> __cache_4688523024
                                                __token = 3223
                                                try:
                                                    __zt_tmp = __attrs_4688523920
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __cache_4688523024 = _static_4662095120('python', "icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                                # <BinOp left=<Value "python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])" (48:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1177514d0> -> __condition
                                                __expression = __cache_4688523024

                                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                                __value = _DEFAULT_MARKER
                                                __condition = (__expression is __value)
                                                if __condition:
                                                    pass
                                                else:
                                                    __content = __cache_4688523024
                                                    __content = __convert(__content)
                                                    if (__content is not None):
                                                        __append(__content)

                                            # <Interpolation value=<Substitution '\n                                ${configlet/title}\n                              ' (48:156)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117752fd0> -> __content_4386234736
                                            __token = 3347
                                            __token = 3349
                                            try:
                                                __zt_tmp = __attrs_4867366416
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __content_4386234736 = _static_4662095120('path', 'configlet/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                            __content_4386234736 = __quote(__content_4386234736, '\x00', '&#0;', None, None)
                                            __content_4386234736 = ('%s%s%s' % ('\n                                ', (__content_4386234736 if (__content_4386234736 is not None) else ''), '\n                              ', ))
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
                                            __append('</a>')
                                            if (__backup_icon_url_4878700928 is __marker):
                                                del econtext['icon_url']
                                            else:
                                                econtext['icon_url'] = __backup_icon_url_4878700928
                                            __append('\n                            </li>')
                                        __append('\n                          ')
                                        ____index_4684895952 -= 1
                                        if (____index_4684895952 > 0):
                                            __append('')
                                    if (__backup_configlet_4881151216 is __marker):
                                        del econtext['configlet']
                                    else:
                                        econtext['configlet'] = __backup_configlet_4881151216
                                    __append('\n                        </ul>\n                      </li>')
                                if (__backup_active_4878699296 is __marker):
                                    del econtext['active']
                                else:
                                    econtext['active'] = __backup_active_4878699296
                                if (__backup_configlets_4878697520 is __marker):
                                    del econtext['configlets']
                                else:
                                    econtext['configlets'] = __backup_configlets_4878697520
                                __append('\n                    ')
                                ____index_4691284624 -= 1
                                if (____index_4691284624 > 0):
                                    __append('')
                            if (__backup_group_4878582880 is __marker):
                                del econtext['group']
                            else:
                                econtext['group'] = __backup_group_4878582880
                            __append('\n                  </ul>\n                </div>')
                            if (__backup_current_url_4878707888 is __marker):
                                del econtext['current_url']
                            else:
                                econtext['current_url'] = __backup_current_url_4878707888
                            if (__backup_site_url_4878708656 is __marker):
                                del econtext['site_url']
                            else:
                                econtext['site_url'] = __backup_site_url_4878708656
                            if (__backup_groups_4878710672 is __marker):
                                del econtext['groups']
                            else:
                                econtext['groups'] = __backup_groups_4878710672
                            if (__backup_controlPanel_4878701072 is __marker):
                                del econtext['controlPanel']
                            else:
                                econtext['controlPanel'] = __backup_controlPanel_4878701072
                            __append('\n\n                ')
                            if (__slot_prefs_configlet_main is None):

                                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4688512976
                                __attrs_4688512976 = _static_4659865408

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4867062864
                                __default_4867062864 = _DEFAULT_MARKER

                                # <Value 'nothing' (59:82)> -> __cache_4670253840
                                __token = 3694
                                try:
                                    __zt_tmp = __attrs_4688512976
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_4670253840 = _static_4662095120('path', 'nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                # <BinOp left=<Value 'nothing' (59:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1179f4050> -> __condition
                                __expression = __cache_4670253840

                                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Page body text\n                ')
                                else:
                                    __content = __cache_4670253840
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            else:
                                __slot_prefs_configlet_main(__stream, econtext.copy(), rcontext)
                            __append('\n\n              ')
                        _slots = econtext['__slot_main'] = _deque((__fill_main, ))

                        # <Value 'context/@@main_template/macros/content' (17:42)> -> __macro
                        __token = 898
                        try:
                            __zt_tmp = __attrs_4675020112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_4662095120('path', 'context/@@main_template/macros/content', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __token = 898
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_4683136128 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_4683136128
                        __append('\n\n          ')
                    else:
                        __slot_prefs_configlet_content(__stream, econtext.copy(), rcontext)
                    __append('\n        ')
                else:
                    __slot_prefs_configlet_wrapper(__stream, econtext.copy(), rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content'] = _deque((__fill_content, ))

            # <Value 'context/@@main_template/macros/master' (2:30)> -> __macro
            __token = 85
            try:
                __zt_tmp = __attrs_4671231568
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4662095120('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __token = 85
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4683855424 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4683855424
            __append('\n')
            __i18n_domain = __previous_i18n_domain_4671242000
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_master': render_master, 'render': render, }