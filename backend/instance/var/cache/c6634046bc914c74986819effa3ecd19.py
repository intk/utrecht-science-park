# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/locking/browser/info.pt'

__tokens = {60: ('view/info/is_locked_for_current_user', 3, 14), 114: (' view/lock_is_stealabl', 4, 16), 157: ('s view/lock_in', 5, 18), 185: ("ns python:context.restrictedTraverse('@@iconresolve", 6, 10), 299: ('locked', 10, 24), 401: ("python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", 12, 39), 574: ('lock_details/author_page', 14, 38), 819: ('lock_details/author_page', 20, 18), 750: ('lock_details/fullname', 18, 24), 929: ('lock_details/time_difference', 24, 27), 1087: ('not:lock_details/author_page', 29, 41), 1273: ('lock_details/fullname', 33, 27), 1373: ('lock_details/time_difference', 36, 27), 1546: ('stealable', 42, 27), 1607: ('string:${context/absolute_url}/@@plone_lock_operations/force_unlock', 44, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878711632 = {'type': 'submit', 'value': 'Unlock', }
_static_4878697088 = {'method': 'POST', 'action': 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', }
_static_4878712736 = {'href': 'lock_details/author_page', }
_static_4878698384 = {'class': 'portalMessage info alert alert-info', }
_static_4659865408 = {}
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878705968 = {'id': 'plone-lock-status', }

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

            # <Static value=<ast.Dict object at 0x122cb2530> name=None at 115e24190> -> __attrs_4669139984
            __attrs_4669139984 = _static_4878705968
            __backup_locked_4878325392 = get('locked', __marker)

            # <Value 'view/info/is_locked_for_current_user' (3:14)> -> __value
            __token = 60
            try:
                __zt_tmp = __attrs_4669139984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/info/is_locked_for_current_user', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_stealable_4878733600 = get('stealable', __marker)

            # <Value 'view/lock_is_stealable' (4:16)> -> __value
            __token = 114
            try:
                __zt_tmp = __attrs_4669139984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/lock_is_stealable', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['stealable'] = __value
            __backup_lock_details_4878335904 = get('lock_details', __marker)

            # <Value 'view/lock_info' (5:18)> -> __value
            __token = 157
            try:
                __zt_tmp = __attrs_4669139984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/lock_info', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['lock_details'] = __value
            __backup_icons_4878792256 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (6:10)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_4669139984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_4669141840 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="plone-lock-status" >\n  ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691694480
            __attrs_4691694480 = _static_4659865408

            # <Value 'locked' (10:24)> -> __condition
            __token = 299
            try:
                __zt_tmp = __attrs_4691694480
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'locked', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x122cb0790> name=None at 117a58a50> -> __attrs_4691704208
                __attrs_4691704208 = _static_4878698384

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portalMessage info alert alert-info">\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691692752
                __attrs_4691692752 = _static_4659865408

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4691693072
                __default_4691693072 = _DEFAULT_MARKER

                # <Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> -> __cache_4691697424
                __token = 401
                try:
                    __zt_tmp = __attrs_4691692752
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4691697424 = _static_4662095120('python', "icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117a58090> -> __condition
                __expression = __cache_4691697424

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4691697424
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4681329104
                __attrs_4681329104 = _static_4659865408

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append('<strong>')
                __stream_4691695056 = []
                __append_4691695056 = __stream_4691695056.append
                __append_4691695056('Locked')
                __msgid_4691695056 = __re_whitespace(''.join(__stream_4691695056)).strip()
                if 'label_locked':
                    __append(translate('label_locked', mapping=None, default=__msgid_4691695056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</strong>\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670541648
                __attrs_4670541648 = _static_4659865408

                # <Value 'lock_details/author_page' (14:38)> -> __condition
                __token = 574
                try:
                    __zt_tmp = __attrs_4670541648
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'lock_details/author_page', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:
                    __stream_4878918912_author = ''
                    __stream_4878918912_time = ''
                    __stream_4681331088 = []
                    __append_4681331088 = __stream_4681331088.append
                    __append_4681331088('\n          This item was locked by\n        ')
                    __stream_4878918912_author = []
                    __append_4878918912_author = __stream_4878918912_author.append

                    # <Static value=<ast.Dict object at 0x122cb3fa0> name=None at 117552c10> -> __attrs_4686420368
                    __attrs_4686420368 = _static_4878712736

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4878918912_author('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686418256
                    __default_4686418256 = _DEFAULT_MARKER

                    # <Substitution 'lock_details/author_page' (20:18)> -> __attr_href
                    __token = 819
                    try:
                        __zt_tmp = __attrs_4686420368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('path', 'lock_details/author_page', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4878918912_author((' href="%s"' % __attr_href))
                    __append_4878918912_author(' >')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686418832
                    __default_4686418832 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (18:24)> -> __cache_4686418960
                    __token = 750
                    try:
                        __zt_tmp = __attrs_4686420368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4686418960 = _static_4662095120('path', 'lock_details/fullname', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (18:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117553c50> -> __condition
                    __expression = __cache_4686418960

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4686418960
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4878918912_author(__content)
                    __append_4878918912_author('</a>')
                    __append_4681331088('${author}')
                    __stream_4878918912_author = ''.join(__stream_4878918912_author)
                    __append_4681331088('\n        ')
                    __stream_4878918912_time = []
                    __append_4878918912_time = __stream_4878918912_time.append

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686421712
                    __attrs_4686421712 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4878918912_time('<span >')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686428944
                    __default_4686428944 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (24:27)> -> __cache_4654638160
                    __token = 929
                    try:
                        __zt_tmp = __attrs_4686421712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4654638160 = _static_4662095120('path', 'lock_details/time_difference', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (24:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1179896d0> -> __condition
                    __expression = __cache_4654638160

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4654638160
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4878918912_time(__content)
                    __append_4878918912_time('</span>')
                    __append_4681331088('${time}')
                    __stream_4878918912_time = ''.join(__stream_4878918912_time)
                    __append_4681331088('\n         ago.\n      ')
                    __msgid_4681331088 = __re_whitespace(''.join(__stream_4681331088)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'time': __stream_4878918912_time, 'author': __stream_4878918912_author, }, default=__msgid_4681331088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689240336
                __attrs_4689240336 = _static_4659865408

                # <Value 'not:lock_details/author_page' (29:41)> -> __condition
                __token = 1087
                try:
                    __zt_tmp = __attrs_4689240336
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('not', 'lock_details/author_page', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:
                    __stream_4878918912_author = ''
                    __stream_4878918912_time = ''
                    __stream_4681334096 = []
                    __append_4681334096 = __stream_4681334096.append
                    __append_4681334096('\n          This item was locked by\n        ')
                    __stream_4878918912_author = []
                    __append_4878918912_author = __stream_4878918912_author.append

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689242512
                    __attrs_4689242512 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4878918912_author('<span >')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689233232
                    __default_4689233232 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (33:27)> -> __cache_4689240912
                    __token = 1273
                    try:
                        __zt_tmp = __attrs_4689242512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4689240912 = _static_4662095120('path', 'lock_details/fullname', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (33:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117803c90> -> __condition
                    __expression = __cache_4689240912

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4689240912
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4878918912_author(__content)
                    __append_4878918912_author('</span>')
                    __append_4681334096('${author}')
                    __stream_4878918912_author = ''.join(__stream_4878918912_author)
                    __append_4681334096('\n        ')
                    __stream_4878918912_time = []
                    __append_4878918912_time = __stream_4878918912_time.append

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691929936
                    __attrs_4691929936 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_4878918912_time('<span >')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689241808
                    __default_4689241808 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (36:27)> -> __cache_4689242448
                    __token = 1373
                    try:
                        __zt_tmp = __attrs_4691929936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4689242448 = _static_4662095120('path', 'lock_details/time_difference', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (36:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117803490> -> __condition
                    __expression = __cache_4689242448

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4689242448
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_4878918912_time(__content)
                    __append_4878918912_time('</span>')
                    __append_4681334096('${time}')
                    __stream_4878918912_time = ''.join(__stream_4878918912_time)
                    __append_4681334096('\n         ago.\n      ')
                    __msgid_4681334096 = __re_whitespace(''.join(__stream_4681334096)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'time': __stream_4878918912_time, 'author': __stream_4878918912_author, }, default=__msgid_4681334096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x122cb0280> name=None at 117075ad0> -> __attrs_4668579088
                __attrs_4668579088 = _static_4878697088

                # <Value 'stealable' (42:27)> -> __condition
                __token = 1546
                try:
                    __zt_tmp = __attrs_4668579088
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'stealable', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form method="POST"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4691918992
                    __default_4691918992 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock' (44:21)> -> __attr_action
                    __token = 1607
                    try:
                        __zt_tmp = __attrs_4668579088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_4662095120('string', '${context/absolute_url}/@@plone_lock_operations/force_unlock', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4688360720
                    __attrs_4688360720 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4878920032_unlock_button = ''
                    __stream_4668587472 = []
                    __append_4668587472 = __stream_4668587472.append
                    __append_4668587472('\n            If you are certain this user has abandoned the object,\n            you may\n          ')
                    __stream_4878920032_unlock_button = []
                    __append_4878920032_unlock_button = __stream_4878920032_unlock_button.append

                    # <Static value=<ast.Dict object at 0x122cb3b50> name=None at 1169a2e10> -> __attrs_4674173264
                    __attrs_4674173264 = _static_4878711632

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append_4878920032_unlock_button('<input type="submit"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670551696
                    __default_4670551696 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x122cb2020> at 1169a35d0> -> __attr_value
                    __attr_value = 'Unlock'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append_4878920032_unlock_button((' value="%s"' % __attr_value))
                    __append_4878920032_unlock_button(' />')
                    __append_4668587472('${unlock_button}')
                    __stream_4878920032_unlock_button = ''.join(__stream_4878920032_unlock_button)
                    __append_4668587472('\n            the object. You will then be able to edit it.\n        ')
                    __msgid_4668587472 = __re_whitespace(''.join(__stream_4668587472)).strip()
                    if 'description_webdav_locked_steal':
                        __append(translate('description_webdav_locked_steal', mapping={'unlock_button': __stream_4878920032_unlock_button, }, default=__msgid_4668587472, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      </form>')
                __append('\n    </div>\n  ')
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_4669141840
            if (__backup_icons_4878792256 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4878792256
            if (__backup_lock_details_4878335904 is __marker):
                del econtext['lock_details']
            else:
                econtext['lock_details'] = __backup_lock_details_4878335904
            if (__backup_stealable_4878733600 is __marker):
                del econtext['stealable']
            else:
                econtext['stealable'] = __backup_stealable_4878733600
            if (__backup_locked_4878325392 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_4878325392
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }