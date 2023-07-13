# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/layout/viewlets/toc.pt'

__tokens = {135: ('view/enabled', 5, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info

_static_4878586768 = {'class': 'portletItem', }
_static_4878583024 = {'class': 'portletContent', }
_static_4878593776 = {'class': 'portletHeader', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878584416 = {'class': 'portlet toc', 'id': 'document-toc', 'role': 'section', 'style': 'display: none', }

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

            # <Static value=<ast.Dict object at 0x122c94a60> name=None at 116b71b90> -> __attrs_4674822480
            __attrs_4674822480 = _static_4878584416

            # <Value 'view/enabled' (5:24)> -> __condition
            __token = 135
            try:
                __zt_tmp = __attrs_4674822480
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'view/enabled', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_4676064912 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="portlet toc" id="document-toc" role="section" style="display: none" >\n  ')

                # <Static value=<ast.Dict object at 0x122c96ef0> name=None at 116b726d0> -> __attrs_4676075472
                __attrs_4676075472 = _static_4878593776

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="portletHeader" >')
                __stream_4676074064 = []
                __append_4676074064 = __stream_4676074064.append
                __append_4676074064('Contents')
                __msgid_4676074064 = __re_whitespace(''.join(__stream_4676074064)).strip()
                if 'label_tableofcontents':
                    __append(translate('label_tableofcontents', mapping=None, default=__msgid_4676074064, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n  ')

                # <Static value=<ast.Dict object at 0x122c944f0> name=None at 1170e8290> -> __attrs_4674163600
                __attrs_4674163600 = _static_4878583024

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="portletContent">\n    ')

                # <Static value=<ast.Dict object at 0x122c95390> name=None at 1169a3b50> -> __attrs_4674162000
                __attrs_4674162000 = _static_4878586768

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portletItem">\n    </div>\n  </section>\n</section>')
                __i18n_domain = __previous_i18n_domain_4676064912
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }