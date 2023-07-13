# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/content/browser/contents/templates/workflow.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_4881138304 = {'class': 'form-text', }
_static_4881141952 = {'class': 'form-check-label', 'for': 'fcWorkflowRecurse', }
_static_4881143584 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'recurse', 'value': 'yes', 'id': 'fcWorkflowRecurse', }
_static_4881140464 = {'class': 'form-check', }
_static_4881152416 = {'class': 'form-text', }
_static_4881151024 = {'value': '<%= transition.id %>', }
_static_4881143392 = {'class': 'form-select', 'name': 'transition', }
_static_4881153568 = {'class': 'form-label', }
_static_4881138112 = {'class': 'mb-2', }
_static_4881140128 = {'class': 'form-control', 'rows': '2', 'name': 'comments', }
_static_4881147136 = {'class': 'form-label', }
_static_4881140320 = {'class': 'mb-2', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683842896
            __attrs_4683842896 = _static_4659865408
            __previous_i18n_domain_4683847440 = __i18n_domain
            __i18n_domain = 'plone'

            # <fieldset ... (0:0)
            # --------------------------------------------------------
            __append('<fieldset>\n  ')

            # <Static value=<ast.Dict object at 0x122f04a60> name=None at 1166f5350> -> __attrs_4687083344
            __attrs_4687083344 = _static_4881140320

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f06500> name=None at 1169a2fd0> -> __attrs_4890783696
            __attrs_4890783696 = _static_4881147136

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4674170128 = []
            __append_4674170128 = __stream_4674170128.append
            __append_4674170128('Comments')
            __msgid_4674170128 = __re_whitespace(''.join(__stream_4674170128)).strip()
            if 'label_comments':
                __append(translate('label_comments', mapping=None, default=__msgid_4674170128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f049a0> name=None at 123835710> -> __attrs_4653929296
            __attrs_4653929296 = _static_4881140128

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea class="form-control" rows="2" name="comments"></textarea>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x122f041c0> name=None at 115657250> -> __attrs_4650887632
            __attrs_4650887632 = _static_4881138112

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f07e20> name=None at 117be8d90> -> __attrs_4869248528
            __attrs_4869248528 = _static_4881153568

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4684471440 = []
            __append_4684471440 = __stream_4684471440.append
            __append_4684471440('Change State')
            __msgid_4684471440 = __re_whitespace(''.join(__stream_4684471440)).strip()
            if 'label_change_status':
                __append(translate('label_change_status', mapping=None, default=__msgid_4684471440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f05660> name=None at 122342910> -> __attrs_4890575440
            __attrs_4890575440 = _static_4881143392

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select class="form-select" name="transition">\n      <% if(data.transitions){\n        _.each(data.transitions, function(transition){\n          %>')

            # <Static value=<ast.Dict object at 0x122f07430> name=None at 1223f7b10> -> __attrs_4869546896
            __attrs_4869546896 = _static_4881151024

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= transition.id %>"><%= transition.title %></option>\n          <%\n        });\n      } %>\n    </select>\n    ')

            # <Static value=<ast.Dict object at 0x122f079a0> name=None at 1223f5ad0> -> __attrs_4890609552
            __attrs_4890609552 = _static_4881152416

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_4869549968 = []
            __append_4869549968 = __stream_4869549968.append
            __append_4869549968('Select the transition to be used for modifying the items state.')
            __msgid_4869549968 = __re_whitespace(''.join(__stream_4869549968)).strip()
            if 'help_change_status_action':
                __append(translate('help_change_status_action', mapping=None, default=__msgid_4869549968, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n  ')

            # <Static value=<ast.Dict object at 0x122f04af0> name=None at 12380f950> -> __attrs_4691288848
            __attrs_4691288848 = _static_4881140464

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n    ')

            # <Static value=<ast.Dict object at 0x122f05720> name=None at 1179f5a50> -> __attrs_4693308560
            __attrs_4693308560 = _static_4881143584

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="recurse" value="yes" id="fcWorkflowRecurse" />\n    ')

            # <Static value=<ast.Dict object at 0x122f050c0> name=None at 117be03d0> -> __attrs_4693306576
            __attrs_4693306576 = _static_4881141952

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcWorkflowRecurse">')
            __stream_4693298448 = []
            __append_4693298448 = __stream_4693298448.append
            __append_4693298448('Include contained items')
            __msgid_4693298448 = __re_whitespace(''.join(__stream_4693298448)).strip()
            if 'label_include_contained_objects':
                __append(translate('label_include_contained_objects', mapping=None, default=__msgid_4693298448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f04280> name=None at 1221bf6d0> -> __attrs_4890701264
            __attrs_4890701264 = _static_4881138304

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_4867212816 = []
            __append_4867212816 = __stream_4867212816.append
            __append_4867212816('\n    If checked, this will attempt to modify the status of all content in any selected folders and their subfolders.\n    ')
            __msgid_4867212816 = __re_whitespace(''.join(__stream_4867212816)).strip()
            if 'help_include_contained_objects':
                __append(translate('help_include_contained_objects', mapping=None, default=__msgid_4867212816, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n</fieldset>')
            __i18n_domain = __previous_i18n_domain_4683847440
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }