# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/plone/app/content/browser/contents/templates/properties.pt'

__tokens = {795: ("multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", 22, 29), 857: ("python: options['vocabulary_url']", 23, 46), 1119: ("multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", 30, 29), 1181: ("python: options['vocabulary_url']", 31, 46)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4881829024 = {'class': 'form-text', }
_static_4881836896 = {'class': 'form-check-label', 'for': 'fcCheckRecurse', }
_static_4881838384 = {'class': 'form-check-input', 'type': 'checkbox', 'name': 'recurse', 'value': 'yes', 'id': 'fcCheckRecurse', }
_static_4881841648 = {'class': 'form-check', }
_static_4881828880 = {'value': '<%= lang.value %>', }
_static_4881829408 = {'class': 'form-select', 'name': 'language', }
_static_4881835600 = {'class': 'form-label', }
_static_4881772224 = {'class': 'mb-2', }
_static_4881838096 = {'class': 'form-check-label', 'for': 'fcSwitchExcludeFromNavNo', }
_static_4881840544 = {'class': 'form-check-input', 'type': 'radio', 'name': 'exclude-from-nav', 'id': 'fcSwitchExcludeFromNavNo', 'value': 'no', }
_static_4881827104 = {'class': 'form-check', }
_static_4881829456 = {'class': 'form-check-label', 'for': 'fcSwitchExcludeFromNavYes', }
_static_4881838192 = {'class': 'form-check-input', 'type': 'radio', 'name': 'exclude-from-nav', 'id': 'fcSwitchExcludeFromNavYes', 'value': 'yes', }
_static_4881767856 = {'class': 'form-check', }
_static_4881772368 = {'class': 'form-label', 'for': 'fcSwitchExcludeFromNav', }
_static_4881764880 = {'class': 'mb-2', }
_static_4881764112 = {'name': 'contributors', 'class': 'pat-select2', 'data-pat-select2': "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_4881769008 = {'class': 'form-label', }
_static_4881760944 = {'class': 'mb-2', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4881764688 = {'name': 'creators', 'class': 'pat-select2', 'data-pat-select2': "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}", }
_static_4881771696 = {'class': 'form-label', }
_static_4881769728 = {'class': 'mb-2', }
_static_4881773232 = {'class': 'form-control', 'name': 'copyright', }
_static_4881769920 = {'class': 'form-label', }
_static_4881770160 = {'class': 'mb-2', }
_static_4881774768 = {'class': 'form-control', 'name': 'expirationDate', 'type': 'datetime-local', }
_static_4881766128 = {'class': 'form-label', }
_static_4881770784 = {'class': 'mb-2', }
_static_4881769872 = {'class': 'form-control', 'name': 'effectiveDate', 'type': 'datetime-local', }
_static_4881772176 = {'class': 'form-label', }
_static_4881767424 = {'class': 'mb-2', }
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4894298192
            __attrs_4894298192 = _static_4659865408
            __previous_i18n_domain_4894298320 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div>\n\n  ')

            # <Static value=<ast.Dict object at 0x122f9dc00> name=None at 116be4a10> -> __attrs_4894300880
            __attrs_4894300880 = _static_4881767424

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f9ee90> name=None at 123b91f90> -> __attrs_4894303952
            __attrs_4894303952 = _static_4881772176

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4894301776 = []
            __append_4894301776 = __stream_4894301776.append
            __append_4894301776('Publication Date')
            __msgid_4894301776 = __re_whitespace(''.join(__stream_4894301776)).strip()
            if 'publiciation_date':
                __append(translate('publiciation_date', mapping=None, default=__msgid_4894301776, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f9e590> name=None at 123b92b90> -> __attrs_4894307664
            __attrs_4894307664 = _static_4881769872

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="effectiveDate" type="datetime-local" />\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x122f9e920> name=None at 123b93750> -> __attrs_4894310032
            __attrs_4894310032 = _static_4881770784

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f9d6f0> name=None at 123b98410> -> __attrs_4894329680
            __attrs_4894329680 = _static_4881766128

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4894327376 = []
            __append_4894327376 = __stream_4894327376.append
            __append_4894327376('Expiration Date')
            __msgid_4894327376 = __re_whitespace(''.join(__stream_4894327376)).strip()
            if 'expiration_date':
                __append(translate('expiration_date', mapping=None, default=__msgid_4894327376, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f9f8b0> name=None at 123b98f90> -> __attrs_4894333328
            __attrs_4894333328 = _static_4881774768

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control" name="expirationDate" type="datetime-local" />\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x122f9e6b0> name=None at 123b99b50> -> __attrs_4894335632
            __attrs_4894335632 = _static_4881770160

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f9e5c0> name=None at 123b9a810> -> __attrs_4894338896
            __attrs_4894338896 = _static_4881769920

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4894336592 = []
            __append_4894336592 = __stream_4894336592.append
            __append_4894336592('Copyright')
            __msgid_4894336592 = __re_whitespace(''.join(__stream_4894336592)).strip()
            if 'copyright':
                __append(translate('copyright', mapping=None, default=__msgid_4894336592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f9f2b0> name=None at 123b9b5d0> -> __attrs_4894342288
            __attrs_4894342288 = _static_4881773232

            # <textarea ... (0:0)
            # --------------------------------------------------------
            __append('<textarea class="form-control" name="copyright"></textarea>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x122f9e500> name=None at 123b9be50> -> __attrs_4894344656
            __attrs_4894344656 = _static_4881769728

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f9ecb0> name=None at 123b9cb10> -> __attrs_4894347856
            __attrs_4894347856 = _static_4881771696

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4894345552 = []
            __append_4894345552 = __stream_4894345552.append
            __append_4894345552('Creators')
            __msgid_4894345552 = __re_whitespace(''.join(__stream_4894345552)).strip()
            if 'creators':
                __append(translate('creators', mapping=None, default=__msgid_4894345552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f9d150> name=None at 123b9d690> -> __attrs_4894351952
            __attrs_4894351952 = _static_4881764688

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="creators" class="form-control" class="pat-select2"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894350928
            __default_4894350928 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}" (22:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116ba1ed0> -> __attr_data_pat_select2
            __token = 795
            __token = 857
            try:
                __zt_tmp = __attrs_4894351952
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_4662095120('python', " options['vocabulary_url']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_data_pat_select2 = __quote(__attr_data_pat_select2, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_pat_select2 = ('%s%s' % ('multiple: true;\n                             vocabularyUrl: ', (__attr_data_pat_select2 if (__attr_data_pat_select2 is not None) else ''), ))
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
            __append('/>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x122f9c2b0> name=None at 123b9d390> -> __attrs_4894354128
            __attrs_4894354128 = _static_4881760944

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f9e230> name=None at 123b9efd0> -> __attrs_4894357264
            __attrs_4894357264 = _static_4881769008

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4894354960 = []
            __append_4894354960 = __stream_4894354960.append
            __append_4894354960('Contributors')
            __msgid_4894354960 = __re_whitespace(''.join(__stream_4894354960)).strip()
            if 'contributors':
                __append(translate('contributors', mapping=None, default=__msgid_4894354960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f9cf10> name=None at 123b9fb10> -> __attrs_4894361488
            __attrs_4894361488 = _static_4881764112

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input name="contributors" class="form-control" class="pat-select2"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4894360528
            __default_4894360528 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "multiple: true;\n                             vocabularyUrl: ${python: options['vocabulary_url']}" (30:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 123ba0310> -> __attr_data_pat_select2
            __token = 1119
            __token = 1181
            try:
                __zt_tmp = __attrs_4894361488
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_select2 = _static_4662095120('python', " options['vocabulary_url']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_data_pat_select2 = __quote(__attr_data_pat_select2, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_pat_select2 = ('%s%s' % ('multiple: true;\n                             vocabularyUrl: ', (__attr_data_pat_select2 if (__attr_data_pat_select2 is not None) else ''), ))
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
            __append('/>\n  </div>\n\n  ')

            # <Static value=<ast.Dict object at 0x122f9d210> name=None at 123ba0950> -> __attrs_4894363664
            __attrs_4894363664 = _static_4881764880

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122f9ef50> name=None at 123ba1650> -> __attrs_4894367376
            __attrs_4894367376 = _static_4881772368

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label" for="fcSwitchExcludeFromNav">')
            __stream_4894364560 = []
            __append_4894364560 = __stream_4894364560.append
            __append_4894364560('Exclude from navigation')
            __msgid_4894364560 = __re_whitespace(''.join(__stream_4894364560)).strip()
            if 'exclude_from_nav':
                __append(translate('exclude_from_nav', mapping=None, default=__msgid_4894364560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122f9ddb0> name=None at 123ba2210> -> __attrs_4894370192
            __attrs_4894370192 = _static_4881767856

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n      ')

            # <Static value=<ast.Dict object at 0x122faf070> name=None at 123ba2ed0> -> __attrs_4894375376
            __attrs_4894375376 = _static_4881838192

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="radio" name="exclude-from-nav" id="fcSwitchExcludeFromNavYes" value="yes">\n      ')

            # <Static value=<ast.Dict object at 0x122face50> name=None at 123ba80d0> -> __attrs_4894394896
            __attrs_4894394896 = _static_4881829456

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcSwitchExcludeFromNavYes">')
            __stream_4894375824 = []
            __append_4894375824 = __stream_4894375824.append
            __append_4894375824('Yes')
            __msgid_4894375824 = __re_whitespace(''.join(__stream_4894375824)).strip()
            if 'yes':
                __append(translate('yes', mapping=None, default=__msgid_4894375824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    </div>\n    ')

            # <Static value=<ast.Dict object at 0x122fac520> name=None at 123ba8c90> -> __attrs_4894397328
            __attrs_4894397328 = _static_4881827104

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n      ')

            # <Static value=<ast.Dict object at 0x122faf9a0> name=None at 123ba98d0> -> __attrs_4894402512
            __attrs_4894402512 = _static_4881840544

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="radio" name="exclude-from-nav" id="fcSwitchExcludeFromNavNo" value="no">\n      ')

            # <Static value=<ast.Dict object at 0x122faf010> name=None at 123baaa90> -> __attrs_4894405584
            __attrs_4894405584 = _static_4881838096

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcSwitchExcludeFromNavNo">')
            __stream_4894402960 = []
            __append_4894402960 = __stream_4894402960.append
            __append_4894402960('No')
            __msgid_4894402960 = __re_whitespace(''.join(__stream_4894402960)).strip()
            if 'no':
                __append(translate('no', mapping=None, default=__msgid_4894402960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    </div>\n  </div>\n\n  <% if (data.languages) { %>\n  ')

            # <Static value=<ast.Dict object at 0x122f9eec0> name=None at 123bab6d0> -> __attrs_4894407888
            __attrs_4894407888 = _static_4881772224

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="mb-2">\n    ')

            # <Static value=<ast.Dict object at 0x122fae650> name=None at 123bac210> -> __attrs_4894411088
            __attrs_4894411088 = _static_4881835600

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-label">')
            __stream_4894408784 = []
            __append_4894408784 = __stream_4894408784.append
            __append_4894408784('Language')
            __msgid_4894408784 = __re_whitespace(''.join(__stream_4894408784)).strip()
            if 'label_language':
                __append(translate('label_language', mapping=None, default=__msgid_4894408784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122face20> name=None at 123bacf90> -> __attrs_4894414416
            __attrs_4894414416 = _static_4881829408

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select class="form-select" name="language">\n      <% _.each(data.languages, function (lang) { %>\n        ')

            # <Static value=<ast.Dict object at 0x122facc10> name=None at 123badc90> -> __attrs_4894417744
            __attrs_4894417744 = _static_4881828880

            # <option ... (0:0)
            # --------------------------------------------------------
            __append('<option value="<%= lang.value %>"><%= lang.title %></option>\n      <% }); %>\n    </select>\n  </div>\n  <% } %>\n\n  ')

            # <Static value=<ast.Dict object at 0x122fafdf0> name=None at 123bae810> -> __attrs_4894420496
            __attrs_4894420496 = _static_4881841648

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-check">\n    ')

            # <Static value=<ast.Dict object at 0x122faf130> name=None at 123baf290> -> __attrs_4894442064
            __attrs_4894442064 = _static_4881838384

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-check-input" type="checkbox" name="recurse" value="yes" id="fcCheckRecurse" />\n    ')

            # <Static value=<ast.Dict object at 0x122faeb60> name=None at 123bb4550> -> __attrs_4894445136
            __attrs_4894445136 = _static_4881836896

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label class="form-check-label" for="fcCheckRecurse">')
            __stream_4894442384 = []
            __append_4894442384 = __stream_4894442384.append
            __append_4894442384('Include contained items')
            __msgid_4894442384 = __re_whitespace(''.join(__stream_4894442384)).strip()
            if 'label_include_contained_objects':
                __append(translate('label_include_contained_objects', mapping=None, default=__msgid_4894442384, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n    ')

            # <Static value=<ast.Dict object at 0x122facca0> name=None at 123bb5210> -> __attrs_4894447952
            __attrs_4894447952 = _static_4881829024

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-text">')
            __stream_4894445840 = []
            __append_4894445840 = __stream_4894445840.append
            __append_4894445840('\n    If checked, this will attempt to modify the status of all content in any selected folders and their subfolders.\n    ')
            __msgid_4894445840 = __re_whitespace(''.join(__stream_4894445840)).strip()
            if 'help_include_contained_objects':
                __append(translate('help_include_contained_objects', mapping=None, default=__msgid_4894445840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n  </div>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_4894298320
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }