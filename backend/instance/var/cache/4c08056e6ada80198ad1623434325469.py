# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/Products/CMFPlone/browser/templates/footer.pt'

__tokens = {860: ('nocall:modules/DateTime.DateTime', 20, 30), 921: (' python:DateTime(', 21, 27), 963: ('python:myTime.year()', 22, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878332592 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }
_static_4878936256 = {'href': 'http://creativecommons.org/licenses/GPL/2.0/', }
_static_4878935296 = {'href': 'http://plone.org/foundation', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878928144 = {'title': 'Copyright', }
_static_4878930304 = {'href': 'http://plone.org', }
_static_4659865408 = {}
_static_4873380160 = {'class': 'card-body', }
_static_4873382032 = {'class': 'card card-classic', 'id': 'portal-footer-signature', }

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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x12279e890> name=None at 1166e1dd0> -> __attrs_4676540688
            __attrs_4676540688 = _static_4873382032

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card card-classic" id="portal-footer-signature">\n\n    ')

            # <Static value=<ast.Dict object at 0x12279e140> name=None at 116be5950> -> __attrs_4673783120
            __attrs_4673783120 = _static_4873380160

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690953808
            __attrs_4690953808 = _static_4659865408
            __stream_4879256256_plonecms = ''
            __stream_4879256256_copyright = ''
            __stream_4879256256_current_year = ''
            __stream_4879256256_plonefoundation = ''
            __stream_4675936208 = []
            __append_4675936208 = __stream_4675936208.append
            __append_4675936208('\n      The\n      ')
            __stream_4879256256_plonecms = []
            __append_4879256256_plonecms = __stream_4879256256_plonecms.append

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676306704
            __attrs_4676306704 = _static_4659865408
            __append_4879256256_plonecms('\n           ')

            # <Static value=<ast.Dict object at 0x122ce9180> name=None at 116bae110> -> __attrs_4681516368
            __attrs_4681516368 = _static_4878930304

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4879256256_plonecms('<a href="http://plone.org">')
            __stream_4676308880 = []
            __append_4676308880 = __stream_4676308880.append
            __append_4676308880('Plone')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676773328
            __attrs_4676773328 = _static_4659865408

            # <sup ... (0:0)
            # --------------------------------------------------------
            __append_4676308880('<sup>&reg;</sup> Open Source CMS/WCM')
            __msgid_4676308880 = __re_whitespace(''.join(__stream_4676308880)).strip()
            if 'label_plone_cms':
                __append_4879256256_plonecms(translate('label_plone_cms', mapping=None, default=__msgid_4676308880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_4879256256_plonecms('</a>\n      ')
            __append_4675936208('${plonecms}')
            __stream_4879256256_plonecms = ''.join(__stream_4879256256_plonecms)
            __append_4675936208('\n      is\n      ')
            __stream_4879256256_copyright = []
            __append_4879256256_copyright = __stream_4879256256_copyright.append

            # <Static value=<ast.Dict object at 0x122ce8910> name=None at 116bad290> -> __attrs_4676074512
            __attrs_4676074512 = _static_4878928144

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_4879256256_copyright('<abbr')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4676766224
            __default_4676766224 = _DEFAULT_MARKER

            # <Translate msgid='title_copyright' node=<ast.Constant object at 0x122ce8af0> at 116bac190> -> __attr_title
            __attr_title = 'Copyright'
            __attr_title = translate('title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_4879256256_copyright((' title="%s"' % __attr_title))
            __append_4879256256_copyright('>&copy;</abbr>')
            __append_4675936208('${copyright}')
            __stream_4879256256_copyright = ''.join(__stream_4879256256_copyright)
            __append_4675936208('\n      2000-')
            __stream_4879256256_current_year = []
            __append_4879256256_current_year = __stream_4879256256_current_year.append

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689723984
            __attrs_4689723984 = _static_4659865408
            __backup_DateTime_4878539152 = get('DateTime', __marker)

            # <Value 'nocall:modules/DateTime.DateTime' (20:30)> -> __value
            __token = 860
            try:
                __zt_tmp = __attrs_4689723984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', 'modules/DateTime.DateTime', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['DateTime'] = __value
            __backup_myTime_4878534592 = get('myTime', __marker)

            # <Value 'python:DateTime()' (21:27)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_4689723984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'DateTime()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['myTime'] = __value

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4691725520
            __default_4691725520 = _DEFAULT_MARKER

            # <Value 'python:myTime.year()' (22:22)> -> __cache_4693070864
            __token = 963
            try:
                __zt_tmp = __attrs_4689723984
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4693070864 = _static_4662095120('python', 'myTime.year()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:myTime.year()' (22:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117ba9610> -> __condition
            __expression = __cache_4693070864

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4693070864
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_4879256256_current_year(__content)
            if (__backup_myTime_4878534592 is __marker):
                del econtext['myTime']
            else:
                econtext['myTime'] = __backup_myTime_4878534592
            if (__backup_DateTime_4878539152 is __marker):
                del econtext['DateTime']
            else:
                econtext['DateTime'] = __backup_DateTime_4878539152
            __append_4675936208('${current_year}')
            __stream_4879256256_current_year = ''.join(__stream_4879256256_current_year)
            __append_4675936208('\n      by the\n      ')
            __stream_4879256256_plonefoundation = []
            __append_4879256256_plonefoundation = __stream_4879256256_plonefoundation.append

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689726096
            __attrs_4689726096 = _static_4659865408
            __append_4879256256_plonefoundation('\n           ')

            # <Static value=<ast.Dict object at 0x122cea500> name=None at 116d21810> -> __attrs_4684068368
            __attrs_4684068368 = _static_4878935296

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4879256256_plonefoundation('<a href="http://plone.org/foundation">')
            __stream_4677834192 = []
            __append_4677834192 = __stream_4677834192.append
            __append_4677834192('Plone Foundation')
            __msgid_4677834192 = __re_whitespace(''.join(__stream_4677834192)).strip()
            if 'label_plone_foundation':
                __append_4879256256_plonefoundation(translate('label_plone_foundation', mapping=None, default=__msgid_4677834192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_4879256256_plonefoundation('</a>')
            __append_4675936208('${plonefoundation}')
            __stream_4879256256_plonefoundation = ''.join(__stream_4879256256_plonefoundation)
            __append_4675936208('\n      and friends.\n      ')
            __msgid_4675936208 = __re_whitespace(''.join(__stream_4675936208)).strip()
            if 'description_copyright':
                __append(translate('description_copyright', mapping={'plonefoundation': __stream_4879256256_plonefoundation, 'current_year': __stream_4879256256_current_year, 'copyright': __stream_4879256256_copyright, 'plonecms': __stream_4879256256_plonecms, }, default=__msgid_4675936208, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689727312
            __attrs_4689727312 = _static_4659865408
            __stream_4879256256_license = ''
            __stream_4683717392 = []
            __append_4683717392 = __stream_4683717392.append
            __append_4683717392('\n      Distributed under the\n           ')
            __stream_4879256256_license = []
            __append_4879256256_license = __stream_4879256256_license.append

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684057872
            __attrs_4684057872 = _static_4659865408
            __append_4879256256_license('\n                ')

            # <Static value=<ast.Dict object at 0x122cea8c0> name=None at 1173127d0> -> __attrs_4677542736
            __attrs_4677542736 = _static_4878936256

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4879256256_license('<a href="http://creativecommons.org/licenses/GPL/2.0/">')
            __stream_4684060368 = []
            __append_4684060368 = __stream_4684060368.append
            __append_4684060368('GNU GPL license')
            __msgid_4684060368 = __re_whitespace(''.join(__stream_4684060368)).strip()
            if 'label_gnu_gpl_licence':
                __append_4879256256_license(translate('label_gnu_gpl_licence', mapping=None, default=__msgid_4684060368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_4879256256_license('</a>')
            __append_4683717392('${license}')
            __stream_4879256256_license = ''.join(__stream_4879256256_license)
            __append_4683717392('.\n      ')
            __msgid_4683717392 = __re_whitespace(''.join(__stream_4683717392)).strip()
            if 'description_license':
                __append(translate('description_license', mapping={'license': __stream_4879256256_license, }, default=__msgid_4683717392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n    </div>\n\n  </div>')
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

            # <Static value=<ast.Dict object at 0x122c572b0> name=None at 1166b0c50> -> __attrs_4684238352
            __attrs_4684238352 = _static_4878332592
            __previous_i18n_domain_4684236112 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_4684236112
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_portlet': render_portlet, 'render': render, }