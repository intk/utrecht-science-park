# -*- coding: utf-8 -*-
__filename = 'login_form'

__tokens = {166: ('string:${here/absolute_url}/login', 11, 33), 291: ('request/came_from | string:', 14, 35)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_5010921296 = {'type': 'submit', 'value': ' Log In ', }
_static_5010918512 = {'colspan': '2', }
_static_5010919904 = {'type': 'password', 'name': '__ac_password', 'size': '30', }
_static_5010919088 = {'type': 'text', 'name': '__ac_name', 'size': '30', }
_static_5010915920 = {'cellpadding': '2', }
_static_5010917264 = {'type': 'hidden', 'name': 'came_from', 'value': '', }
_static_4795593872 = __C2ZContextWrapper
_static_4795594640 = __compile_zt_expr
_static_5010916640 = {'method': 'post', 'action': '', }
_static_4795505040 = {}

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

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4827824208
            __attrs_4827824208 = _static_4795505040

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html>\n  ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970415376
            __attrs_4970415376 = _static_4795505040

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970423504
            __attrs_4970423504 = _static_4795505040

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title> Login Form </title>\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970425680
            __attrs_4970425680 = _static_4795505040

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n    ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970427600
            __attrs_4970427600 = _static_4795505040

            # <h3 ... (0:0)
            # --------------------------------------------------------
            __append('<h3> Please log in </h3>\n\n    ')

            # <Static value=<ast.Dict object at 0x12aac8520> name=None at 12842bd10> -> __attrs_4970497168
            __attrs_4970497168 = _static_5010916640

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form method="post"')

            # <Symbol value=<DEFAULT> at 11dc7b090> -> __default_4787902160
            __default_4787902160 = _DEFAULT_MARKER

            # <Substitution 'string:${here/absolute_url}/login' (11:33)> -> __attr_action
            __token = 166
            try:
                __zt_tmp = __attrs_4970497168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4795594640('string', '${here/absolute_url}/login', econtext=econtext)(_static_4795593872(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n      ')

            # <Static value=<ast.Dict object at 0x12aac8790> name=None at 12843d050> -> __attrs_4970502160
            __attrs_4970502160 = _static_5010917264

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="came_from"')

            # <Symbol value=<DEFAULT> at 11dc7b090> -> __default_4970501200
            __default_4970501200 = _DEFAULT_MARKER

            # <Substitution 'request/came_from | string:' (14:35)> -> __attr_value
            __token = 291
            try:
                __zt_tmp = __attrs_4970502160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4795594640('path', 'request/came_from | string:', econtext=econtext)(_static_4795593872(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append('/>\n      ')

            # <Static value=<ast.Dict object at 0x12aac8250> name=None at 12843db10> -> __attrs_4970504272
            __attrs_4970504272 = _static_5010915920

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table cellpadding="2">\n        ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970508432
            __attrs_4970508432 = _static_4795505040

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970511440
            __attrs_4970511440 = _static_4795505040

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4828319504
            __attrs_4828319504 = _static_4795505040

            # <b ... (0:0)
            # --------------------------------------------------------
            __append('<b>Login:</b> </td>\n          ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4828317776
            __attrs_4828317776 = _static_4795505040

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x12aac8eb0> name=None at 11fca5750> -> __attrs_4828327824
            __attrs_4828327824 = _static_5010919088

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="__ac_name" size="30" /></td>\n        </tr>\n        ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4828319376
            __attrs_4828319376 = _static_4795505040

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4828320464
            __attrs_4828320464 = _static_4795505040

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970448272
            __attrs_4970448272 = _static_4795505040

            # <b ... (0:0)
            # --------------------------------------------------------
            __append('<b>Password:</b></td>\n          ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970449616
            __attrs_4970449616 = _static_4795505040

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>')

            # <Static value=<ast.Dict object at 0x12aac91e0> name=None at 128430cd0> -> __attrs_4970454928
            __attrs_4970454928 = _static_5010919904

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="password" name="__ac_password" size="30" /></td>\n        </tr>\n        ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4970457104
            __attrs_4970457104 = _static_4795505040

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n          ')

            # <Static value=<ast.Dict object at 0x12aac8c70> name=None at 128433bd0> -> __attrs_4969873872
            __attrs_4969873872 = _static_5010918512

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td colspan="2">\n            ')

            # <Static value=<ast.Dict object at 0x11dd59990> name=None at 11dd6a590> -> __attrs_4969885968
            __attrs_4969885968 = _static_4795505040

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x12aac9750> name=None at 1283a6a90> -> __attrs_4969882064
            __attrs_4969882064 = _static_5010921296

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="submit" value=" Log In " />\n          </td>\n        </tr>\n      </table>\n\n    </form>\n\n  </body>\n\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }