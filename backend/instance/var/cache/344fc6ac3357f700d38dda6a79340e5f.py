# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/document_relateditems.pt'

__tokens = {71: ('view/related_items', 3, 19), 112: (' nocall:context/@@plon', 4, 21), 159: ('t nocall:context/@@plone_layo', 5, 22), 216: ('ng nocall:plone_view/normalizeStr', 6, 24), 275: ('ate nocall:context/@@plone_context_s', 7, 21), 339: ("tion python:context.portal_registry.get('types_use_view_action_in_listings'", 8, 22), 456: ('related', 10, 24), 678: ('related', 21, 30), 767: ('item/Description', 24, 16), 805: (' item/portal_typ', 25, 20), 849: ("s python:'contenttype-' + normalizeString(item_typ", 26, 25), 925: ('te item/review_state|python: context_state.workflow_stat', 27, 22), 1013: ("ass python: 'state-' + normalizeString(item_wf_st", 28, 27), 1083: ('_url item/getURL|item/absolut', 29, 15), 1133: ("m_url python:(item_type in use_view_action) and item_url+'/view' or it", 30, 14), 1230: ('_image python:item.', 31, 19), 1368: ('${item_url}', 37, 19), 1370: ('item_url', 37, 21), 1392: ('${item/pretty_title_or_id}', 38, 11), 1394: ('item/pretty_title_or_id', 38, 13), 1444: ('${item/Description}', 39, 15), 1446: ('item/Description', 39, 17), 1573: ("python:item.getURL() +'/@@images/image/thumb'", 45, 21), 1659: ('item_has_image', 47, 26), 1720: ('string:$getIcon', 49, 17), 1753: (' item/Descriptio', 50, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878541648 = {'class': 'ms-3', 'src': '', 'alt': 'item/Description', }
_static_4878541072 = {'class': 'h6 stretched-link', 'href': '${item_url}', }
_static_4878537136 = {'class': 'media-body', }
_static_4878537520 = {'class': 'media position-relative', }
_static_4659865408 = {}
_static_4878534208 = {'class': 'section-heading', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878533632 = {'id': 'section-related', }

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

            # <Static value=<ast.Dict object at 0x122c88400> name=None at 11604c410> -> __attrs_4675389200
            __attrs_4675389200 = _static_4878533632
            __backup_related_4878938656 = get('related', __marker)

            # <Value 'view/related_items' (3:19)> -> __value
            __token = 71
            try:
                __zt_tmp = __attrs_4675389200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/related_items', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['related'] = __value
            __backup_plone_view_4878444112 = get('plone_view', __marker)

            # <Value 'nocall:context/@@plone' (4:21)> -> __value
            __token = 112
            try:
                __zt_tmp = __attrs_4675389200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', 'context/@@plone', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_plone_layout_4878360032 = get('plone_layout', __marker)

            # <Value 'nocall:context/@@plone_layout' (5:22)> -> __value
            __token = 159
            try:
                __zt_tmp = __attrs_4675389200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', 'context/@@plone_layout', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_normalizeString_4878355856 = get('normalizeString', __marker)

            # <Value 'nocall:plone_view/normalizeString' (6:24)> -> __value
            __token = 216
            try:
                __zt_tmp = __attrs_4675389200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', 'plone_view/normalizeString', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['normalizeString'] = __value
            __backup_context_state_4878762384 = get('context_state', __marker)

            # <Value 'nocall:context/@@plone_context_state' (7:21)> -> __value
            __token = 275
            try:
                __zt_tmp = __attrs_4675389200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', 'context/@@plone_context_state', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_use_view_action_4878450064 = get('use_view_action', __marker)

            # <Value "python:context.portal_registry.get('types_use_view_action_in_listings', [])" (8:22)> -> __value
            __token = 339
            try:
                __zt_tmp = __attrs_4675389200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.portal_registry.get('types_use_view_action_in_listings', [])", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['use_view_action'] = __value

            # <Value 'related' (10:24)> -> __condition
            __token = 456
            try:
                __zt_tmp = __attrs_4675389200
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'related', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4675400208 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-related" >\n\n  ')

                # <Static value=<ast.Dict object at 0x122c88640> name=None at 116acf410> -> __attrs_4390672016
                __attrs_4390672016 = _static_4878534208

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="section-heading" >')
                __stream_4675400016 = []
                __append_4675400016 = __stream_4675400016.append
                __append_4675400016('\n      Related content\n  ')
                __msgid_4675400016 = __re_whitespace(''.join(__stream_4675400016)).strip()
                if 'section_related_heading':
                    __append(translate('section_related_heading', mapping=None, default=__msgid_4675400016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n  <!-- section content -->\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683622160
                __attrs_4683622160 = _static_4659865408
                __backup_item_4878603008 = get('item', __marker)

                # <Value 'related' (21:30)> -> __iterator
                __token = 678
                try:
                    __zt_tmp = __attrs_4683622160
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'related', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4690953168, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x122c89330> name=None at 11542c890> -> __attrs_4675435856
                    __attrs_4675435856 = _static_4878537520
                    __backup_desc_4878611792 = get('desc', __marker)

                    # <Value 'item/Description' (24:16)> -> __value
                    __token = 767
                    try:
                        __zt_tmp = __attrs_4675435856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'item/Description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['desc'] = __value
                    __backup_item_type_4878445456 = get('item_type', __marker)

                    # <Value 'item/portal_type' (25:20)> -> __value
                    __token = 805
                    try:
                        __zt_tmp = __attrs_4675435856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'item/portal_type', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['item_type'] = __value
                    __backup_item_type_class_4878610064 = get('item_type_class', __marker)

                    # <Value "python:'contenttype-' + normalizeString(item_type)" (26:25)> -> __value
                    __token = 849
                    try:
                        __zt_tmp = __attrs_4675435856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "'contenttype-' + normalizeString(item_type)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_wf_state_4878601568 = get('item_wf_state', __marker)

                    # <Value 'item/review_state|python: context_state.workflow_state()' (27:22)> -> __value
                    __token = 925
                    try:
                        __zt_tmp = __attrs_4675435856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'item/review_state|python: context_state.workflow_state()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['item_wf_state'] = __value
                    __backup_item_wf_state_class_4878598352 = get('item_wf_state_class', __marker)

                    # <Value "python: 'state-' + normalizeString(item_wf_state)" (28:27)> -> __value
                    __token = 1013
                    try:
                        __zt_tmp = __attrs_4675435856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', " 'state-' + normalizeString(item_wf_state)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['item_wf_state_class'] = __value
                    __backup_item_url_4878222384 = get('item_url', __marker)

                    # <Value 'item/getURL|item/absolute_url' (29:15)> -> __value
                    __token = 1083
                    try:
                        __zt_tmp = __attrs_4675435856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'item/getURL|item/absolute_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_url_4878605168 = get('item_url', __marker)

                    # <Value "python:(item_type in use_view_action) and item_url+'/view' or item_url" (30:14)> -> __value
                    __token = 1133
                    try:
                        __zt_tmp = __attrs_4675435856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "(item_type in use_view_action) and item_url+'/view' or item_url", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_has_image_4878784144 = get('item_has_image', __marker)

                    # <Value 'python:item.getIcon' (31:19)> -> __value
                    __token = 1230
                    try:
                        __zt_tmp = __attrs_4675435856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', 'item.getIcon', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['item_has_image'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="media position-relative" >\n\n      ')

                    # <Static value=<ast.Dict object at 0x122c891b0> name=None at 116ad7f50> -> __attrs_4677721680
                    __attrs_4677721680 = _static_4878537136

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="media-body">\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671191952
                    __attrs_4671191952 = _static_4659865408

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')

                    # <Static value=<ast.Dict object at 0x122c8a110> name=None at 1178354d0> -> __attrs_4670122000
                    __attrs_4670122000 = _static_4878541072

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="h6 stretched-link"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4667576912
                    __default_4667576912 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${item_url}' (37:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117729d50> -> __attr_href
                    __token = 1368
                    __token = 1370
                    try:
                        __zt_tmp = __attrs_4670122000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('path', 'item_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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

                    # <Interpolation value=<Substitution '${item/pretty_title_or_id}' (38:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1157c4850> -> __content_4386234736
                    __token = 1392
                    __token = 1394
                    try:
                        __zt_tmp = __attrs_4670122000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4386234736 = _static_4662095120('path', 'item/pretty_title_or_id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                    __append('</a></div>\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4668482000
                    __attrs_4668482000 = _static_4659865408

                    # <small ... (0:0)
                    # --------------------------------------------------------
                    __append('<small>')

                    # <Interpolation value=<Substitution '${item/Description}' (39:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116434f90> -> __content_4386234736
                    __token = 1444
                    __token = 1446
                    try:
                        __zt_tmp = __attrs_4668482000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_4386234736 = _static_4662095120('path', 'item/Description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                    __append('</small>\n      </div>\n\n      ')

                    # <Static value=<ast.Dict object at 0x122c8a350> name=None at 11783edd0> -> __attrs_4688589840
                    __attrs_4688589840 = _static_4878541648
                    __backup_getIcon_4878335856 = get('getIcon', __marker)

                    # <Value "python:item.getURL() +'/@@images/image/thumb'" (45:21)> -> __value
                    __token = 1573
                    try:
                        __zt_tmp = __attrs_4688589840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "item.getURL() +'/@@images/image/thumb'", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['getIcon'] = __value

                    # <Value 'item_has_image' (47:26)> -> __condition
                    __token = 1659
                    try:
                        __zt_tmp = __attrs_4688589840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'item_has_image', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append('<img class="ms-3"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689479248
                        __default_4689479248 = _DEFAULT_MARKER

                        # <Substitution 'string:$getIcon' (49:17)> -> __attr_src
                        __token = 1720
                        try:
                            __zt_tmp = __attrs_4688589840
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_4662095120('string', '$getIcon', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((' src="%s"' % __attr_src))

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688587472
                        __default_4688587472 = _DEFAULT_MARKER

                        # <Substitution 'item/Description' (50:16)> -> __attr_alt
                        __token = 1753
                        try:
                            __zt_tmp = __attrs_4688589840
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_4662095120('path', 'item/Description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))
                        __append(' />')
                    if (__backup_getIcon_4878335856 is __marker):
                        del econtext['getIcon']
                    else:
                        econtext['getIcon'] = __backup_getIcon_4878335856
                    __append('\n\n    </div>')
                    if (__backup_item_has_image_4878784144 is __marker):
                        del econtext['item_has_image']
                    else:
                        econtext['item_has_image'] = __backup_item_has_image_4878784144
                    if (__backup_item_url_4878605168 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_4878605168
                    if (__backup_item_url_4878222384 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_4878222384
                    if (__backup_item_wf_state_class_4878598352 is __marker):
                        del econtext['item_wf_state_class']
                    else:
                        econtext['item_wf_state_class'] = __backup_item_wf_state_class_4878598352
                    if (__backup_item_wf_state_4878601568 is __marker):
                        del econtext['item_wf_state']
                    else:
                        econtext['item_wf_state'] = __backup_item_wf_state_4878601568
                    if (__backup_item_type_class_4878610064 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_4878610064
                    if (__backup_item_type_4878445456 is __marker):
                        del econtext['item_type']
                    else:
                        econtext['item_type'] = __backup_item_type_4878445456
                    if (__backup_desc_4878611792 is __marker):
                        del econtext['desc']
                    else:
                        econtext['desc'] = __backup_desc_4878611792
                    __append('\n  ')
                    ____index_4690953168 -= 1
                    if (____index_4690953168 > 0):
                        __append('')
                if (__backup_item_4878603008 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_4878603008
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4675400208
            if (__backup_use_view_action_4878450064 is __marker):
                del econtext['use_view_action']
            else:
                econtext['use_view_action'] = __backup_use_view_action_4878450064
            if (__backup_context_state_4878762384 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_4878762384
            if (__backup_normalizeString_4878355856 is __marker):
                del econtext['normalizeString']
            else:
                econtext['normalizeString'] = __backup_normalizeString_4878355856
            if (__backup_plone_layout_4878360032 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_4878360032
            if (__backup_plone_view_4878444112 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_4878444112
            if (__backup_related_4878938656 is __marker):
                del econtext['related']
            else:
                econtext['related'] = __backup_related_4878938656
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }