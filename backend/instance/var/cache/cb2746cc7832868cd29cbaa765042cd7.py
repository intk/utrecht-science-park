# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/volto/browser/voltobackendwarning.pt'

__tokens = {33: ('nocall: context/@@iconresolver', 1, 33), 253: ("python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", 6, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878819600 = {'href': 'https://6.docs.plone.org/volto/index.html', }
_static_4878323328 = {'href': 'https://6.docs.plone.org/install/install-from-packages.html', }
_static_4878322704 = {'class': 'content', }
_static_4878334464 = {'class': 'portalMessage statusmessage statusmessage-warning alert alert-warning', 'role': 'alert', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674344528
            __attrs_4674344528 = _static_4659865408
            __backup_icons_4878333312 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_4674344528
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', ' context/@@iconresolver', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_4674354640 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x122c57a00> name=None at 1169cd1d0> -> __attrs_4674350224
            __attrs_4674350224 = _static_4878334464

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="portalMessage statusmessage statusmessage-warning alert alert-warning" role="alert">\n        ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674174672
            __attrs_4674174672 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674170832
            __default_4674170832 = _DEFAULT_MARKER

            # <Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> -> __cache_4674170384
            __token = 253
            try:
                __zt_tmp = __attrs_4674174672
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4674170384 = _static_4662095120('python', "icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1169a1a90> -> __condition
            __expression = __cache_4674170384

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4674170384
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4673877840
            __attrs_4673877840 = _static_4659865408

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_4674159696 = []
            __append_4674159696 = __stream_4674159696.append
            __append_4674159696('Warning')
            __msgid_4674159696 = __re_whitespace(''.join(__stream_4674159696)).strip()
            if __msgid_4674159696:
                __append(translate(__msgid_4674159696, mapping=None, default=__msgid_4674159696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>:\n        ')

            # <Static value=<ast.Dict object at 0x122c54c10> name=None at 11695b850> -> __attrs_4683595024
            __attrs_4683595024 = _static_4878322704

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="content">\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690466384
            __attrs_4690466384 = _static_4659865408
            __stream_4683587216 = []
            __append_4683587216 = __stream_4683587216.append
            __append_4683587216('You have accessed the Plone backend through its Classic UI frontend.')
            __msgid_4683587216 = __re_whitespace(''.join(__stream_4683587216)).strip()
            if 'volto_backend_warning':
                __append(translate('volto_backend_warning', mapping=None, default=__msgid_4683587216, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690469392
            __attrs_4690469392 = _static_4659865408

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670551312
            __attrs_4670551312 = _static_4659865408

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686708368
            __attrs_4686708368 = _static_4659865408
            __stream_4670541904 = []
            __append_4670541904 = __stream_4670541904.append
            __append_4670541904("If you want to use Plone's new frontend Volto instead:\n              ")

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674881744
            __attrs_4674881744 = _static_4659865408

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_4670541904('<ul>\n                ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689451792
            __attrs_4689451792 = _static_4659865408

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_4670541904('<li>Install Volto, if not already installed.</li>\n                ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4664381328
            __attrs_4664381328 = _static_4659865408

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_4670541904('<li>Start Volto, if not already started.</li>\n                ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4390669520
            __attrs_4390669520 = _static_4659865408

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_4670541904('<li>Visit the Volto frontend.</li>\n              </ul>\n              For more information, please read the documentation for how to\n              ')

            # <Static value=<ast.Dict object at 0x122c54e80> name=None at 105b44c10> -> __attrs_4691722448
            __attrs_4691722448 = _static_4878323328

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4670541904('<a href="https://6.docs.plone.org/install/install-from-packages.html">Install Plone from its packages</a>\n              and refer to the full Volto documentation\n              ')

            # <Static value=<ast.Dict object at 0x122cce110> name=None at 117a61e10> -> __attrs_4675884560
            __attrs_4675884560 = _static_4878819600

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4670541904('<a href="https://6.docs.plone.org/volto/index.html">Frontend</a>.')
            __msgid_4670541904 = __re_whitespace(''.join(__stream_4670541904)).strip()
            if 'volto_backend_warning_link':
                __append(translate('volto_backend_warning_link', mapping=None, default=__msgid_4670541904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n        </span>\n    </div>\n\n')
            __i18n_domain = __previous_i18n_domain_4674354640
            if (__backup_icons_4878333312 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4878333312
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }