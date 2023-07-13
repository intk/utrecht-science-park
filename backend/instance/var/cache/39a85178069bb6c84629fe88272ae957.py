# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/toolbar.pt'

__tokens = {94: ('view/context_state', 4, 25), 130: (" python:context.restrictedTraverse('@@iconresolver'", 5, 16), 206: ('r python: view.get_personal_bar', 6, 22), 261: ('os view/toolbar_posit', 7, 20), 322: ('context_state/is_toolbar_visible', 9, 24), 680: ("python:icons.tag('arrow-bar-left')", 25, 41), 875: ("python:icons.tag('arrow-bar-right')", 31, 41), 1033: ('view/base_render', 37, 23), 1084: ('toolbar_main', 39, 23), 1137: ('toolbar_main', 41, 33), 1295: ('personal_bar/user_actions', 46, 24), 1191: ("personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", 45, 16), 1219: ("python:'dropend' if toolbar_pos == 'side' else ''", 45, 44), 1546: ('personal_bar/homelink_url', 55, 16), 1633: ("python:icons.tag('toolbar-action/personaltools', tag_class='')", 58, 41), 1763: ('personal_bar/user_name', 60, 27), 2000: ('${personal_bar/user_name}', 69, 38), 2002: ('personal_bar/user_name', 69, 40), 2076: ('personal_bar/user_actions', 71, 31), 2193: ('action', 74, 15), 2269: ("python:icons.tag(action.get('icon', 'dot'), tag_class='')", 77, 41), 2372: ('action/title', 78, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878932704 = set([])
_static_4878538912 = {'class': 'nav-link dropdown-item', }
_static_4878536272 = {'class': 'dropdown-header', }
_static_4873379152 = {'class': 'dropdown-menu', 'id': 'collapse-personaltools', 'aria-labelledby': 'personaltools-menulink', }
_static_4873380304 = {'class': 'toolbar-label', }
_static_4674121552 = {'class': 'nav-link dropdown-toggle', 'id': 'personaltools-menulink', 'aria-expanded': 'false', 'data-bs-offset': '0,0', 'data-bs-toggle': 'dropdown', 'href': 'personal_bar/homelink_url', }
_static_4878250096 = {'class': "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", }
_static_4878251008 = {'class': 'nav flex-column plone-toolbar-main', }
_static_4878252448 = {'class': 'toolbar-expand', 'aria-label': 'Pin', }
_static_4659865408 = {}
_static_4878251824 = {'class': 'toolbar-collapse', 'aria-label': 'Unpin', }
_static_4878243280 = {'class': 'toolbar-header nav', }
_static_4878251536 = {'class': 'pat-toolbar', 'id': 'edit-zone', 'role': 'toolbar', 'data-bs-scroll': 'true', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878247216 = {'id': 'edit-bar', 'role': 'toolbar', }

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

            # <Static value=<ast.Dict object at 0x122c42530> name=None at 11753c310> -> __attrs_4677134416
            __attrs_4677134416 = _static_4878247216
            __backup_context_state_4878928240 = get('context_state', __marker)

            # <Value 'view/context_state' (4:25)> -> __value
            __token = 94
            try:
                __zt_tmp = __attrs_4677134416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/context_state', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_icons_4878770208 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (5:16)> -> __value
            __token = 130
            try:
                __zt_tmp = __attrs_4677134416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_personal_bar_4878775872 = get('personal_bar', __marker)

            # <Value 'python: view.get_personal_bar()' (6:22)> -> __value
            __token = 206
            try:
                __zt_tmp = __attrs_4677134416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', ' view.get_personal_bar()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['personal_bar'] = __value
            __backup_toolbar_pos_4878765504 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (7:20)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_4677134416
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/toolbar_position', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'context_state/is_toolbar_visible' (9:24)> -> __condition
            __token = 322
            try:
                __zt_tmp = __attrs_4677134416
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'context_state/is_toolbar_visible', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4689703632 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="edit-bar" role="toolbar" >\n\n\n  ')

                # <Static value=<ast.Dict object at 0x122c43610> name=None at 117871bd0> -> __attrs_4689700688
                __attrs_4689700688 = _static_4878251536

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-toolbar" id="edit-zone" role="toolbar" data-bs-scroll="true" >\n\n    ')

                # <Static value=<ast.Dict object at 0x122c415d0> name=None at 11692b550> -> __attrs_4669648464
                __attrs_4669648464 = _static_4878243280

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="toolbar-header nav">\n      ')

                # <Static value=<ast.Dict object at 0x122c43730> name=None at 116a42f10> -> __attrs_4674829328
                __attrs_4674829328 = _static_4878251824

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-collapse"')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674829648
                __default_4674829648 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x122c405b0> at 116a43cd0> -> __attr_aria_label
                __attr_aria_label = 'Unpin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676095184
                __attrs_4676095184 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684439568
                __default_4684439568 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-left')" (25:41)> -> __cache_4663843984
                __token = 680
                try:
                    __zt_tmp = __attrs_4676095184
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4663843984 = _static_4662095120('python', "icons.tag('arrow-bar-left')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-left')" (25:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11542df10> -> __condition
                __expression = __cache_4663843984

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4663843984
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n      ')

                # <Static value=<ast.Dict object at 0x122c439a0> name=None at 116b7b6d0> -> __attrs_4686219600
                __attrs_4686219600 = _static_4878252448

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-expand"')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4668576592
                __default_4668576592 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x122c42650> at 11644f690> -> __attr_aria_label
                __attr_aria_label = 'Pin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686221968
                __attrs_4686221968 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686224272
                __default_4686224272 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-right')" (31:41)> -> __cache_4686220496
                __token = 875
                try:
                    __zt_tmp = __attrs_4686221968
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4686220496 = _static_4662095120('python', "icons.tag('arrow-bar-right')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-right')" (31:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117523e10> -> __condition
                __expression = __cache_4686220496

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4686220496
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n    </div>\n\n    ')

                # <Static value=<ast.Dict object at 0x122c43400> name=None at 117520d10> -> __attrs_4671362064
                __attrs_4671362064 = _static_4878251008
                __backup_toolbar_main_4878776256 = get('toolbar_main', __marker)

                # <Value 'view/base_render' (37:23)> -> __value
                __token = 1033
                try:
                    __zt_tmp = __attrs_4671362064
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/base_render', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['toolbar_main'] = __value

                # <Value 'toolbar_main' (39:23)> -> __condition
                __token = 1084
                try:
                    __zt_tmp = __attrs_4671362064
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'toolbar_main', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="nav flex-column plone-toolbar-main" >\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683616784
                    __attrs_4683616784 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4683615056
                    __default_4683615056 = _DEFAULT_MARKER

                    # <Value 'toolbar_main' (41:33)> -> __cache_4683614480
                    __token = 1137
                    try:
                        __zt_tmp = __attrs_4683616784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4683614480 = _static_4662095120('path', 'toolbar_main', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'toolbar_main' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1172a6d50> -> __condition
                    __expression = __cache_4683614480

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n      </li>')
                    else:
                        __content = __cache_4683614480
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </ul>')
                if (__backup_toolbar_main_4878776256 is __marker):
                    del econtext['toolbar_main']
                else:
                    econtext['toolbar_main'] = __backup_toolbar_main_4878776256
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x122c43070> name=None at 1172a7590> -> __attrs_4688588432
                __attrs_4688588432 = _static_4878250096

                # <Value 'personal_bar/user_actions' (46:24)> -> __condition
                __token = 1295
                try:
                    __zt_tmp = __attrs_4688588432
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'personal_bar/user_actions', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688576592
                    __default_4688576592 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}" (45:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1165c7350> -> __attr_class
                    __token = 1191
                    __token = 1219
                    try:
                        __zt_tmp = __attrs_4688588432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4662095120('python', "'dropend' if toolbar_pos == 'side' else ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('personaltools-wrapper nav ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append(' >\n\n      ')

                    # <Static value=<ast.Dict object at 0x116996f50> name=None at 117760c10> -> __attrs_4689062672
                    __attrs_4689062672 = _static_4674121552

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link dropdown-toggle" id="personaltools-menulink" aria-expanded="false" data-bs-offset="0,0" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689067536
                    __default_4689067536 = _DEFAULT_MARKER

                    # <Substitution 'personal_bar/homelink_url' (55:16)> -> __attr_href
                    __token = 1546
                    try:
                        __zt_tmp = __attrs_4689062672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('path', 'personal_bar/homelink_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686917136
                    __attrs_4686917136 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686918160
                    __default_4686918160 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> -> __cache_4686916944
                    __token = 1633
                    try:
                        __zt_tmp = __attrs_4686917136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4686916944 = _static_4662095120('python', "icons.tag('toolbar-action/personaltools', tag_class='')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1175c8350> -> __condition
                    __expression = __cache_4686916944

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4686916944
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x12279e1d0> name=None at 1175ca450> -> __attrs_4686914192
                    __attrs_4686914192 = _static_4873380304

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label" >')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686911056
                    __default_4686911056 = _DEFAULT_MARKER

                    # <Value 'personal_bar/user_name' (60:27)> -> __cache_4686919440
                    __token = 1763
                    try:
                        __zt_tmp = __attrs_4686914192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4686919440 = _static_4662095120('path', 'personal_bar/user_name', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'personal_bar/user_name' (60:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1175ca650> -> __condition
                    __expression = __cache_4686919440

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('User')
                    else:
                        __content = __cache_4686919440
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>\n\n      ')

                    # <Static value=<ast.Dict object at 0x12279dd50> name=None at 117353690> -> __attrs_4684329936
                    __attrs_4684329936 = _static_4873379152

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="dropdown-menu" id="collapse-personaltools" aria-labelledby="personaltools-menulink" >\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684318352
                    __attrs_4684318352 = _static_4659865408

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>\n          ')

                    # <Static value=<ast.Dict object at 0x122c88e50> name=None at 117549050> -> __attrs_4686384144
                    __attrs_4686384144 = _static_4878536272

                    # <h6 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h6 class="dropdown-header">')

                    # <Interpolation value=<Substitution '${personal_bar/user_name}' (69:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117549b50> -> __content_4386234736
                    __token = 2000
                    __token = 2002
                    try:
                        __zt_tmp = __attrs_4686384144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4386234736 = _static_4662095120('path', 'personal_bar/user_name', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                    __append('</h6>\n        </li>\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686384080
                    __attrs_4686384080 = _static_4659865408
                    __backup_action_4878247792 = get('action', __marker)

                    # <Value 'personal_bar/user_actions' (71:31)> -> __iterator
                    __token = 2076
                    try:
                        __zt_tmp = __attrs_4686384080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4662095120('path', 'personal_bar/user_actions', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    (__iterator, ____index_4686389904, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n          ')

                        # <Static value=<ast.Dict object at 0x122c898a0> name=None at 11754a750> -> __attrs_4686389392
                        __attrs_4686389392 = _static_4878538912

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Value 'action' (74:15)> -> __cache_4686386832
                        __token = 2193
                        try:
                            __zt_tmp = __attrs_4686389392
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4686386832 = _static_4662095120('path', 'action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if ('class' not in __chain(__cache_4686386832)):
                            __append(' class="nav-link dropdown-item"')
                        __attr_4686385424 = __cache_4686386832
                        for (name, value, ) in __attr_4686385424.items():
                            if ((name not in _static_4878932704) and (value is not None)):
                                __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                        __append(' >\n            ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4688268944
                        __attrs_4688268944 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688271632
                        __default_4688271632 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> -> __cache_4669185872
                        __token = 2269
                        try:
                            __zt_tmp = __attrs_4688268944
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4669185872 = _static_4662095120('python', "icons.tag(action.get('icon', 'dot'), tag_class='')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1170ca310> -> __condition
                        __expression = __cache_4669185872

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4669185872
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4688274512
                        __attrs_4688274512 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688277200
                        __default_4688277200 = _DEFAULT_MARKER

                        # <Value 'action/title' (78:41)> -> __cache_4684655056
                        __token = 2372
                        try:
                            __zt_tmp = __attrs_4688274512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4684655056 = _static_4662095120('path', 'action/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (78:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117717690> -> __condition
                        __expression = __cache_4684655056

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              action title\n            ')
                        else:
                            __content = __cache_4684655056
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          </a>\n        </li>')
                        ____index_4686389904 -= 1
                        if (____index_4686389904 > 0):
                            __append('\n        ')
                    if (__backup_action_4878247792 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_4878247792
                    __append('\n      </ul>\n\n    </div>')
                __append('\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_4689703632
            if (__backup_toolbar_pos_4878765504 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_4878765504
            if (__backup_personal_bar_4878775872 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_4878775872
            if (__backup_icons_4878770208 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4878770208
            if (__backup_context_state_4878928240 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_4878928240
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }