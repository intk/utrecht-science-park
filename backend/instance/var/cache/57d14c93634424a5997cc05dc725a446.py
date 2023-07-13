# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/content/browser/contents/templates/tags.pt'

__tokens = {721: ("multiple: true; vocabularyUrl: ${python: options['vocabulary_url']}", 21, 29), 754: ("python: options['vocabulary_url']", 21, 62)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4881761472 = {'class': 'toadd pat-select2', 'name': 'toadd', 'style': 'width:100%', 'data-pat-select2': "multiple: true; vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_4881765888 = {'class': 'form-label', }
_static_4881763728 = {'value': '<%= tag %>', }
_static_4881765744 = {'multiple': '', 'class': 'toremove pat-select2', 'name': 'toremove', 'style': 'width:100%', }
_static_4881761376 = {'class': 'form-label', }
_static_4881763968 = {'class': 'mb-2', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676777744
            __attrs_4676777744 = _static_4659865408
            __previous_i18n_domain_4674719568 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n  ')

            # <Static value=<ast.Dict object at 0x122f9ce80> name=None at 116a80a50> -> __attrs_4650889168
            __attrs_4650889168 = _static_4881763968

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f9c460> name=None at 11536fbd0> -> __attrs_4663026128
            __attrs_4663026128 = _static_4881761376

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4650886928 = []
            __append_4650886928 = __stream_4650886928.append
            __append_4650886928('Tags to remove')
            __msgid_4650886928 = __re_whitespace(''.join(__stream_4650886928)).strip()
            if 'tags_to_remove':
                __append(translate('tags_to_remove', mapping=None, default=__msgid_4650886928, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f9d570> name=None at 116043410> -> __attrs_4663494800
            __attrs_4663494800 = _static_4881765744

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select multiple class="toremove pat-select2" name="toremove" style="width:100%">\n      <% var tags = [];\n      _.each(items, function(item, index) {\n        _.each(item.Subject, function(tag) {\n          if(tags.indexOf(tag) === -1){\n            tags.push(tag);\n            %>')

            # <Static value=<ast.Dict object at 0x122f9cd90> name=None at 1173dd1d0> -> __attrs_4890656400
            __attrs_4890656400 = _static_4881763728

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= tag %>"><%= tag %></option>\n            <%\n          }\n        });\n      }); %>\n    </select>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674829968
            __attrs_4674829968 = _static_4659865408

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n    ')

            # <Static value=<ast.Dict object at 0x122f9d600> name=None at 115fc9610> -> __attrs_4890612368
            __attrs_4890612368 = _static_4881765888

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4663843856 = []
            __append_4663843856 = __stream_4663843856.append
            __append_4663843856('Tags to add')
            __msgid_4663843856 = __re_whitespace(''.join(__stream_4663843856)).strip()
            if 'tags_to_add':
                __append(translate('tags_to_add', mapping=None, default=__msgid_4663843856, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f9c4c0> name=None at 123835910> -> __attrs_4890782288
            __attrs_4890782288 = _static_4881761472

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="toadd pat-select2" name="toadd" style="width:100%"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4890783312
            __default_4890783312 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true; vocabularyUrl: ${python: options['vocabulary_url']}" (21:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117b51910> -> __attr_data_pat_select2
            __token = 721
            __token = 754
            try:
                __zt_tmp = __attrs_4890782288
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_4662095120('python', " options['vocabulary_url']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_data_pat_select2 = __quote(__attr_data_pat_select2, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_pat_select2 = ('%s%s' % ('multiple: true; vocabularyUrl: ', (__attr_data_pat_select2 if (__attr_data_pat_select2 is not None) else ''), ))
            if (__attr_data_pat_select2 is None):
                pass
            else:
                if (__attr_data_pat_select2 is _DEFAULT_MARKER):
                    __attr_data_pat_select2 = None
                else:
                    __tt = type(__attr_data_pat_select2)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_data_pat_select2 = str(__attr_data_pat_select2)
                    else:
                        if (__tt is bytes):
                            __attr_data_pat_select2 = decode(__attr_data_pat_select2)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_data_pat_select2 = __attr_data_pat_select2.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_pat_select2)
                                    __attr_data_pat_select2 = (str(__attr_data_pat_select2) if (__attr_data_pat_select2 is __converted) else __converted)
                                else:
                                    __attr_data_pat_select2 = __attr_data_pat_select2()
            if (__attr_data_pat_select2 is not None):
                __append((' data-pat-select2="%s"' % __attr_data_pat_select2))
            __append('/>\n\n  </div>\n</div>')
            __i18n_domain = __previous_i18n_domain_4674719568
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }