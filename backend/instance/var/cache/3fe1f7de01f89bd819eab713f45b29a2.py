# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/content/browser/contents/templates/rename.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_4881786976 = {'class': 'thumb-thumb', 'src': '<%= item.getURL %>/@@images/image/thumb', }
_static_4881783616 = {'class': 'form-control', 'name': 'newid_<%= index %>', 'value': '<%= item.id %>', }
_static_4881783088 = {'class': 'form-label', }
_static_4881780928 = {'class': 'mb-2', }
_static_4881779392 = {'class': 'form-control', 'name': 'newtitle_<%= index %>', 'value': '<%= item.Title %>', }
_static_4881780592 = {'class': 'form-label', }
_static_4881778912 = {'class': 'mb-2', }
_static_4881782080 = {'name': 'UID_<%= index %>', 'type': 'hidden', 'value': '<%- item.UID %>', }
_static_4881777040 = {'class': 'mb-3 pb-3 <% if (items.length > 1){%>border-bottom<% } %>', }
_static_4881777664 = {'class': 'itemstoremove row row-cols-1', }

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

            # <Static value=<ast.Dict object at 0x122fa0400> name=None at 1179f4a50> -> __attrs_4681665680
            __attrs_4681665680 = _static_4881777664
            __previous_i18n_domain_4663694032 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="itemstoremove row row-cols-1">\n<% _.each(items, function(item, index) { %>\n  ')

            # <Static value=<ast.Dict object at 0x122fa0190> name=None at 115f01610> -> __attrs_4664214608
            __attrs_4664214608 = _static_4881777040

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-3 pb-3 <% if (items.length > 1){%>border-bottom<% } %>">\n    ')

            # <Static value=<ast.Dict object at 0x122fa1540> name=None at 123831e10> -> __attrs_4650886544
            __attrs_4650886544 = _static_4881782080

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="UID_<%= index %>" type="hidden" value="<%- item.UID %>" />\n\n    ')

            # <Static value=<ast.Dict object at 0x122fa08e0> name=None at 11536db90> -> __attrs_4690294736
            __attrs_4690294736 = _static_4881778912

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x122fa0f70> name=None at 116a81a90> -> __attrs_4664336400
            __attrs_4664336400 = _static_4881780592

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4675077136 = []
            __append_4675077136 = __stream_4675077136.append
            __append_4675077136('Title')
            __msgid_4675077136 = __re_whitespace(''.join(__stream_4675077136)).strip()
            if 'label_title':
                __append(translate('label_title', mapping=None, default=__msgid_4675077136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n      ')

            # <Static value=<ast.Dict object at 0x122fa0ac0> name=None at 115f74890> -> __attrs_4663499664
            __attrs_4663499664 = _static_4881779392

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="newtitle_<%= index %>" value="<%= item.Title %>" />\n    </div>\n\n    ')

            # <Static value=<ast.Dict object at 0x122fa10c0> name=None at 116a43e10> -> __attrs_4659077776
            __attrs_4659077776 = _static_4881780928

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n      ')

            # <Static value=<ast.Dict object at 0x122fa1930> name=None at 123826650> -> __attrs_4890648464
            __attrs_4890648464 = _static_4881783088

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4890721168 = []
            __append_4890721168 = __stream_4890721168.append
            __append_4890721168('Short name')
            __msgid_4890721168 = __re_whitespace(''.join(__stream_4890721168)).strip()
            if 'label_short_name':
                __append(translate('label_short_name', mapping=None, default=__msgid_4890721168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n      ')

            # <Static value=<ast.Dict object at 0x122fa1b40> name=None at 115f58bd0> -> __attrs_4890772624
            __attrs_4890772624 = _static_4881783616

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="newid_<%= index %>" value="<%= item.id %>" />\n    </div>\n\n    <% if(item.getIcon ){ %>')

            # <Static value=<ast.Dict object at 0x122fa2860> name=None at 1225c6750> -> __attrs_4871449936
            __attrs_4871449936 = _static_4881786976

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img class="thumb-thumb" src="<%= item.getURL %>/@@images/image/thumb"><% } %>\n\n  </div>\n<% }) %>\n</div>')
            __i18n_domain = __previous_i18n_domain_4663694032
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }