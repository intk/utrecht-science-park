# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/document_byline.pt'

__tokens = {53: ('view/show', 2, 24), 154: ('here/creators', 6, 30), 206: (' context/@@plone_portal_state/navigation_root_ur', 7, 37), 306: ('python:creator_ids and view.show_about()', 9, 31), 427: ('creator_ids', 12, 29), 493: ('python: view.get_url_path(user_id)', 14, 27), 555: (' python:view.get_fullname(user_id', 15, 26), 761: ('url_path', 19, 26), 699: ('${navigation_root_url}/${url_path}', 18, 17), 701: ('navigation_root_url', 18, 19), 724: ('url_path', 18, 42), 780: ('${fullname}', 20, 9), 782: ('fullname', 20, 11), 900: ('not:url_path', 22, 29), 923: ('${fullname}', 23, 9), 925: ('fullname', 23, 11), 1053: ('view/pub_date', 30, 25), 1091: (' context/ModificationDat', 31, 23), 1154: ('e python:view.show_modification_date', 32, 36), 1271: ('published', 35, 25), 1373: ('python:context.toLocalizedTime(published)', 38, 25), 1452: ('show_modification_date', 38, 104), 1561: ('show_modification_date', 42, 25), 1698: ('python:context.toLocalizedTime(modified)', 47, 25), 1828: ('view/isExpired', 53, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878443200 = {'class': 'state-expired', }
_static_4878438400 = {'class': 'documentModified', }
_static_4878448624 = {'class': 'documentPublished', }
_static_4878442336 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', }
_static_4878448480 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', 'href': '${navigation_root_url}/${url_path}', }
_static_4659865408 = {}
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878448528 = {'id': 'section-byline', }

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

            # <Static value=<ast.Dict object at 0x122c73790> name=None at 1164e1e90> -> __attrs_4674450704
            __attrs_4674450704 = _static_4878448528

            # <Value 'view/show' (2:24)> -> __condition
            __token = 53
            try:
                __zt_tmp = __attrs_4674450704
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'view/show', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4673669648 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-byline" >\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4693126032
                __attrs_4693126032 = _static_4659865408
                __backup_creator_ids_4878450352 = get('creator_ids', __marker)

                # <Value 'here/creators' (6:30)> -> __value
                __token = 154
                try:
                    __zt_tmp = __attrs_4693126032
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'here/creators', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['creator_ids'] = __value
                __backup_navigation_root_url_4878439888 = get('navigation_root_url', __marker)

                # <Value 'context/@@plone_portal_state/navigation_root_url' (7:37)> -> __value
                __token = 206
                try:
                    __zt_tmp = __attrs_4693126032
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['navigation_root_url'] = __value

                # <Value 'python:creator_ids and view.show_about()' (9:31)> -> __condition
                __token = 306
                try:
                    __zt_tmp = __attrs_4693126032
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('python', 'creator_ids and view.show_about()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691725840
                    __attrs_4691725840 = _static_4659865408
                    __stream_4691727376 = []
                    __append_4691727376 = __stream_4691727376.append
                    __append_4691727376('by')
                    __msgid_4691727376 = __re_whitespace(''.join(__stream_4691727376)).strip()
                    if __msgid_4691727376:
                        __append(translate(__msgid_4691727376, mapping=None, default=__msgid_4691727376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691723984
                    __attrs_4691723984 = _static_4659865408
                    __backup_user_id_4878446080 = get('user_id', __marker)

                    # <Value 'creator_ids' (12:29)> -> __iterator
                    __token = 427
                    try:
                        __zt_tmp = __attrs_4691723984
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4662095120('path', 'creator_ids', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    (__iterator, ____index_4691736336, ) = getname('repeat')('user_id', __iterator)
                    econtext['user_id'] = None
                    for __item in __iterator:
                        econtext['user_id'] = __item
                        __append('\n      ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683758800
                        __attrs_4683758800 = _static_4659865408
                        __backup_url_path_4878446848 = get('url_path', __marker)

                        # <Value 'python: view.get_url_path(user_id)' (14:27)> -> __value
                        __token = 493
                        try:
                            __zt_tmp = __attrs_4683758800
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4662095120('python', ' view.get_url_path(user_id)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        econtext['url_path'] = __value
                        __backup_fullname_4878436096 = get('fullname', __marker)

                        # <Value 'python:view.get_fullname(user_id)' (15:26)> -> __value
                        __token = 555
                        try:
                            __zt_tmp = __attrs_4683758800
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4662095120('python', 'view.get_fullname(user_id)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        econtext['fullname'] = __value
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x122c73760> name=None at 1167f6350> -> __attrs_4665583568
                        __attrs_4665583568 = _static_4878448480

                        # <Value 'url_path' (19:26)> -> __condition
                        __token = 761
                        try:
                            __zt_tmp = __attrs_4665583568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('path', 'url_path', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a class="badge rounded-pill bg-light text-dark fw-normal fs-6"')

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686959312
                            __default_4686959312 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${navigation_root_url}/${url_path}' (18:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117878d50> -> __attr_href
                            __token = 699
                            __token = 701
                            try:
                                __zt_tmp = __attrs_4665583568
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_4662095120('path', 'navigation_root_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __token = 724
                            try:
                                __zt_tmp = __attrs_4665583568
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href_722 = _static_4662095120('path', 'url_path', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            __attr_href_722 = __quote(__attr_href_722, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/', (__attr_href_722 if (__attr_href_722 is not None) else ''), ))
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

                            # <Interpolation value=<Substitution '${fullname}' (20:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117707650> -> __content_4386234736
                            __token = 780
                            __token = 782
                            try:
                                __zt_tmp = __attrs_4665583568
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_4386234736 = _static_4662095120('path', 'fullname', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                            __append('</a>')
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x122c71f60> name=None at 117704f50> -> __attrs_4688204240
                        __attrs_4688204240 = _static_4878442336

                        # <Value 'not:url_path' (22:29)> -> __condition
                        __token = 900
                        try:
                            __zt_tmp = __attrs_4688204240
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('not', 'url_path', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge rounded-pill bg-light text-dark fw-normal fs-6" >')

                            # <Interpolation value=<Substitution '${fullname}' (23:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117707390> -> __content_4386234736
                            __token = 923
                            __token = 925
                            try:
                                __zt_tmp = __attrs_4688204240
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_4386234736 = _static_4662095120('path', 'fullname', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
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
                            __append('</span>')
                        __append('\n      ')
                        if (__backup_fullname_4878436096 is __marker):
                            del econtext['fullname']
                        else:
                            econtext['fullname'] = __backup_fullname_4878436096
                        if (__backup_url_path_4878446848 is __marker):
                            del econtext['url_path']
                        else:
                            econtext['url_path'] = __backup_url_path_4878446848
                        __append('\n    ')
                        ____index_4691736336 -= 1
                        if (____index_4691736336 > 0):
                            __append('')
                    if (__backup_user_id_4878446080 is __marker):
                        del econtext['user_id']
                    else:
                        econtext['user_id'] = __backup_user_id_4878446080
                    __append('\n    &mdash;\n  ')
                if (__backup_navigation_root_url_4878439888 is __marker):
                    del econtext['navigation_root_url']
                else:
                    econtext['navigation_root_url'] = __backup_navigation_root_url_4878439888
                if (__backup_creator_ids_4878450352 is __marker):
                    del econtext['creator_ids']
                else:
                    econtext['creator_ids'] = __backup_creator_ids_4878450352
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670122512
                __attrs_4670122512 = _static_4659865408
                __backup_published_4878444784 = get('published', __marker)

                # <Value 'view/pub_date' (30:25)> -> __value
                __token = 1053
                try:
                    __zt_tmp = __attrs_4670122512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/pub_date', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['published'] = __value
                __backup_modified_4878436048 = get('modified', __marker)

                # <Value 'context/ModificationDate' (31:23)> -> __value
                __token = 1091
                try:
                    __zt_tmp = __attrs_4670122512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'context/ModificationDate', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['modified'] = __value
                __backup_show_modification_date_4878445408 = get('show_modification_date', __marker)

                # <Value 'python:view.show_modification_date()' (32:36)> -> __value
                __token = 1154
                try:
                    __zt_tmp = __attrs_4670122512
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', 'view.show_modification_date()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['show_modification_date'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x122c737f0> name=None at 1177065d0> -> __attrs_4684248336
                __attrs_4684248336 = _static_4878448624

                # <Value 'published' (35:25)> -> __condition
                __token = 1271
                try:
                    __zt_tmp = __attrs_4684248336
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'published', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentPublished" >\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4687080720
                    __attrs_4687080720 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4671283984 = []
                    __append_4671283984 = __stream_4671283984.append
                    __append_4671283984('published')
                    __msgid_4671283984 = __re_whitespace(''.join(__stream_4671283984)).strip()
                    if 'box_published':
                        __append(translate('box_published', mapping=None, default=__msgid_4671283984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4687069264
                    __attrs_4687069264 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4687070736
                    __default_4687070736 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(published)' (38:25)> -> __cache_4687081360
                    __token = 1373
                    try:
                        __zt_tmp = __attrs_4687069264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4687081360 = _static_4662095120('python', 'context.toLocalizedTime(published)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(published)' (38:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1175f3150> -> __condition
                    __expression = __cache_4687081360

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Published')
                    else:
                        __content = __cache_4687081360
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684111888
                    __attrs_4684111888 = _static_4659865408

                    # <Value 'show_modification_date' (38:104)> -> __condition
                    __token = 1452
                    try:
                        __zt_tmp = __attrs_4684111888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'show_modification_date', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:
                        __append(',')
                    __append('\n    </span>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x122c71000> name=None at 11731c550> -> __attrs_4669142416
                __attrs_4669142416 = _static_4878438400

                # <Value 'show_modification_date' (42:25)> -> __condition
                __token = 1561
                try:
                    __zt_tmp = __attrs_4669142416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'show_modification_date', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentModified" >\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674534288
                    __attrs_4674534288 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4390671952 = []
                    __append_4390671952 = __stream_4390671952.append
                    __append_4390671952('\n      last modified\n      ')
                    __msgid_4390671952 = __re_whitespace(''.join(__stream_4390671952)).strip()
                    if 'box_last_modified':
                        __append(translate('box_last_modified', mapping=None, default=__msgid_4390671952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674160720
                    __attrs_4674160720 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674163152
                    __default_4674163152 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(modified)' (47:25)> -> __cache_4674530768
                    __token = 1698
                    try:
                        __zt_tmp = __attrs_4674160720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4674530768 = _static_4662095120('python', 'context.toLocalizedTime(modified)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(modified)' (47:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1169a2e10> -> __condition
                    __expression = __cache_4674530768

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n      Modified\n      ')
                    else:
                        __content = __cache_4674530768
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n    </span>')
                __append('\n  ')
                if (__backup_show_modification_date_4878445408 is __marker):
                    del econtext['show_modification_date']
                else:
                    econtext['show_modification_date'] = __backup_show_modification_date_4878445408
                if (__backup_modified_4878436048 is __marker):
                    del econtext['modified']
                else:
                    econtext['modified'] = __backup_modified_4878436048
                if (__backup_published_4878444784 is __marker):
                    del econtext['published']
                else:
                    econtext['published'] = __backup_published_4878444784
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684649680
                __attrs_4684649680 = _static_4659865408

                # <Value 'view/isExpired' (53:30)> -> __condition
                __token = 1828
                try:
                    __zt_tmp = __attrs_4684649680
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'view/isExpired', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:
                    __append('\n    &mdash;\n    ')

                    # <Static value=<ast.Dict object at 0x122c722c0> name=None at 1165517d0> -> __attrs_4686907472
                    __attrs_4686907472 = _static_4878443200

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="state-expired" >')
                    __stream_4669642832 = []
                    __append_4669642832 = __stream_4669642832.append
                    __append_4669642832('expired')
                    __msgid_4669642832 = __re_whitespace(''.join(__stream_4669642832)).strip()
                    if 'time_expired':
                        __append(translate('time_expired', mapping=None, default=__msgid_4669642832, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n  ')
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_4673669648
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }