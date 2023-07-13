# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/Products/CMFPlone/controlpanel/browser/quickinstaller.pt'

__tokens = {1150: ('view/get_upgrades', 35, 36), 1208: (' python:len(products', 36, 39), 1386: ('not:products', 39, 30), 1667: ('products', 43, 27), 1781: ('products', 45, 44), 1822: ('product/id', 46, 30), 2084: ('pid', 50, 44), 2355: ('string:Upgrade ${pid}', 56, 44), 2451: ('product/title', 59, 33), 2648: ('product/description', 64, 39), 2682: ('product/description', 64, 73), 2809: ('pid', 65, 58), 2856: ('product/version', 65, 105), 3022: ('product/upgrade_info', 68, 43), 3237: ('not:upgrade_info/hasProfile', 72, 39), 3419: ('upgrade_info/installedVersion', 74, 77), 3533: ('upgrade_info/hasProfile', 76, 39), 3736: ('upgrade_info/installedVersion', 78, 87), 3993: ('upgrade_info/newVersion', 81, 86), 4133: ('not:upgrade_info/available', 85, 38), 4617: ('python:num_products > 1', 96, 29), 4787: ('products', 98, 51), 4953: ('product/id', 101, 44), 5522: ('view/get_available', 116, 36), 5578: (' python:len(products', 117, 36), 5829: ('products', 121, 34), 5909: ('product/id', 122, 35), 6129: ('pid', 126, 46), 6485: ('product/title', 137, 33), 6682: ('product/description', 142, 39), 6766: ('product/description', 144, 29), 6875: ('pid', 145, 58), 6922: ('product/version', 145, 105), 7091: ('not:product/uninstall_profile', 149, 31), 7389: ('view/get_installed', 158, 36), 7448: (' python:len(products', 159, 39), 7701: ('products', 163, 34), 7781: ('product/id', 164, 35), 7995: ('pid', 168, 42), 8213: ('product/uninstall_profile', 173, 37), 8405: ('product/title', 179, 35), 8612: ('product/description', 184, 41), 8700: ('product/description', 186, 31), 8811: ('pid', 187, 60), 8858: ('product/version', 187, 107), 9032: ('not:product/uninstall_profile', 191, 33), 9331: ('view/get_broken', 200, 36), 9388: (' python:len(products', 201, 40), 9443: ('num_products', 202, 31), 9685: ('products', 206, 34), 9780: ('product/product_id', 208, 33), 9976: ('product/type', 213, 33), 10087: ('product/value', 214, 61), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4878289120 = {'class': 'discreet', }
_static_4878291808 = {'class': 'configletDescription discreet', }
_static_4878367136 = {'class': 'list-group-item mt-2 pb-3', }
_static_4878366176 = {'class': 'configlets list-group list-group-flush', }
_static_4878353024 = {'class': 'card-header', }
_static_4878737008 = {'id': 'broken-products', 'class': 'card mb-4', }
_static_4878359600 = {'class': 'alert alert-info mt-2 mb-0', 'role': 'status', }
_static_4878366992 = {'class': 'discreet', }
_static_4878359648 = {'class': 'configletDescription discreet', }
_static_4878361328 = {'class': 'btn btn-sm btn-danger', 'type': 'submit', 'value': 'Uninstall', 'name': 'form.submitted', }
_static_4878365504 = {'type': 'hidden', 'name': 'uninstall_product', 'value': 'pid', }
_static_4878366896 = {'action': 'uninstall_products', 'method': 'post', 'class': 'float-end', }
_static_4878362192 = {'class': 'list-group-item mt-2 pb-3', }
_static_4878358976 = {'class': 'configlets list-group list-group-flush', }
_static_4878362480 = {'class': 'card-header', }
_static_4878739888 = {'id': 'activated-products', 'class': 'card mb-4', }
_static_4878729424 = {'class': 'alert alert-warning mt-2 mb-0', 'role': 'status', }
_static_4878734032 = {'class': 'discreet', }
_static_4878742864 = {'class': 'configletDescription discreet', }
_static_4878741472 = {'class': 'btn btn-sm btn-primary', 'type': 'submit', 'value': 'Install', 'name': 'form.submitted', }
_static_4878736432 = {'type': 'hidden', 'name': 'install_product', 'value': 'pid', }
_static_4878731776 = {'action': 'install_products', 'method': 'post', 'class': 'float-end', }
_static_4878734704 = {'class': 'list-group-item mt-2 pb-3', }
_static_4878740464 = {'class': 'configlets list-group list-group-flush', }
_static_4878739984 = {'class': 'card-header', }
_static_4878768336 = {'id': 'install-products', 'class': 'card mb-4', }
_static_4878738208 = {'class': 'btn btn-primary', 'type': 'submit', 'value': 'Upgrade them ALL!', 'name': 'form.submitted', }
_static_4878730912 = {'type': 'hidden', 'value': 'product', 'name': 'prefs_reinstallProducts:list', }
_static_4878737872 = {'action': 'upgrade_products', 'method': 'post', }
_static_4878772752 = {'class': 'list-group-item mt-2 pb-3', }
_static_4878731296 = {'class': 'list-group-item mt-2 pb-3', }
_static_4878768048 = {'class': 'configletDetails list-group list-group-flush', }
_static_4878770160 = {'class': 'discreet', }
_static_4878771264 = {'class': 'configletDescription discreet', }
_static_4878769776 = {'class': 'btn btn-secondary', 'type': 'submit', 'value': 'Upgrade ${pid}', 'name': 'form.submitted', }
_static_4878762144 = {'type': 'hidden', 'name': 'prefs_reinstallProducts:list', 'value': 'pid', }
_static_4878762096 = {'action': 'upgrade_products', 'method': 'post', 'class': 'float-end', }
_static_4878771360 = {'class': 'list-group-item mt-2 pb-3', }
_static_4878768720 = {'class': 'configlets list-group list-group-flush', }
_static_4878768816 = {'id': 'up-to-date-message', 'class': 'alert alert-info m-3 mb-0', 'role': 'status', }
_static_4878775248 = {'class': 'card-header', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878771312 = {'id': 'upgrade-products', 'class': 'card mb-4', }
_static_4878590608 = {'id': 'content-core', }
_static_4878770688 = {'href': 'http://docs.plone.org/manage/installing/installing_addons.html', }
_static_4878772896 = {'class': 'discreet', }
_static_4878764208 = {'class': 'lead', }
_static_4878583936 = {'class': 'documentFirstHeading', }
_static_4878592384 = 'master'
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4865989264
            __attrs_4865989264 = _static_4659865408
            __backup_macroname_4671260928 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x122c96980> name=None at 1221883d0> -> __value
            __value = _static_4878592384
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4867061968
                __attrs_4867061968 = _static_4659865408
                __previous_i18n_domain_4867061584 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683754576
                __attrs_4683754576 = _static_4659865408

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n    ')

                # <Static value=<ast.Dict object at 0x122c94880> name=None at 1166c8690> -> __attrs_4671366544
                __attrs_4671366544 = _static_4878583936

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_4671177744 = []
                __append_4671177744 = __stream_4671177744.append
                __append_4671177744('Add-ons')
                __msgid_4671177744 = __re_whitespace(''.join(__stream_4671177744)).strip()
                if __msgid_4671177744:
                    __append(translate(__msgid_4671177744, mapping=None, default=__msgid_4671177744, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x122cc08b0> name=None at 1175a9350> -> __attrs_4692230288
                __attrs_4692230288 = _static_4878764208

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_4686775312 = []
                __append_4686775312 = __stream_4686775312.append
                __append_4686775312('\n      This is the Add-on configuration section, you can activate and deactivate\n      add-ons in the lists below.\n    ')
                __msgid_4686775312 = __re_whitespace(''.join(__stream_4686775312)).strip()
                if __msgid_4686775312:
                    __append(translate(__msgid_4686775312, mapping=None, default=__msgid_4686775312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n    ')

                # <Static value=<ast.Dict object at 0x122cc2aa0> name=None at 117add290> -> __attrs_4689455568
                __attrs_4689455568 = _static_4878772896

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="discreet">')
                __stream_4881746400_third_party_product = ''
                __stream_4692238096 = []
                __append_4692238096 = __stream_4692238096.append
                __append_4692238096('\n      To make new add-ons show up here, add them to your buildout\n      configuration, run buildout, and restart the server process.\n      For detailed instructions see\n      ')
                __stream_4881746400_third_party_product = []
                __append_4881746400_third_party_product = __stream_4881746400_third_party_product.append

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4687005776
                __attrs_4687005776 = _static_4659865408

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_4881746400_third_party_product('<span>\n      ')

                # <Static value=<ast.Dict object at 0x122cc2200> name=None at 11753e750> -> __attrs_4686344208
                __attrs_4686344208 = _static_4878770688

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_4881746400_third_party_product('<a href="http://docs.plone.org/manage/installing/installing_addons.html">')
                __stream_4686343760 = []
                __append_4686343760 = __stream_4686343760.append
                __append_4686343760('\n        Installing a third party add-on\n      ')
                __msgid_4686343760 = __re_whitespace(''.join(__stream_4686343760)).strip()
                if __msgid_4686343760:
                    __append_4881746400_third_party_product(translate(__msgid_4686343760, mapping=None, default=__msgid_4686343760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_4881746400_third_party_product('</a>\n      </span>')
                __append_4692238096('${third_party_product}')
                __stream_4881746400_third_party_product = ''.join(__stream_4881746400_third_party_product)
                __append_4692238096('.\n    ')
                __msgid_4692238096 = __re_whitespace(''.join(__stream_4692238096)).strip()
                if __msgid_4692238096:
                    __append(translate(__msgid_4692238096, mapping={'third_party_product': __stream_4881746400_third_party_product, }, default=__msgid_4692238096, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x122c96290> name=None at 11753dd90> -> __attrs_4674352016
                __attrs_4674352016 = _static_4878590608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n\n\n      ')

                # <Static value=<ast.Dict object at 0x122cc2470> name=None at 117b0e590> -> __attrs_4692063504
                __attrs_4692063504 = _static_4878771312
                __backup_products_4878593200 = get('products', __marker)

                # <Value 'view/get_upgrades' (35:36)> -> __value
                __token = 1150
                try:
                    __zt_tmp = __attrs_4692063504
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/get_upgrades', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_4878594496 = get('num_products', __marker)

                # <Value 'python:len(products)' (36:39)> -> __value
                __token = 1208
                try:
                    __zt_tmp = __attrs_4692063504
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', 'len(products)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="upgrade-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x122cc33d0> name=None at 1179d2290> -> __attrs_4691137232
                __attrs_4691137232 = _static_4878775248

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_4692063632 = []
                __append_4692063632 = __stream_4692063632.append
                __append_4692063632('Upgrades')
                __msgid_4692063632 = __re_whitespace(''.join(__stream_4692063632)).strip()
                if __msgid_4692063632:
                    __append(translate(__msgid_4692063632, mapping=None, default=__msgid_4692063632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n          ')

                # <Static value=<ast.Dict object at 0x122cc1ab0> name=None at 1179d2a90> -> __attrs_4651670992
                __attrs_4651670992 = _static_4878768816

                # <Value 'not:products' (39:30)> -> __condition
                __token = 1386
                try:
                    __zt_tmp = __attrs_4651670992
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('not', 'products', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="up-to-date-message" class="alert alert-info m-3 mb-0" role="status">\n            ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689695248
                    __attrs_4689695248 = _static_4659865408

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4689705936 = []
                    __append_4689705936 = __stream_4689705936.append
                    __append_4689705936('No upgrades in this corner.')
                    __msgid_4689705936 = __re_whitespace(''.join(__stream_4689705936)).strip()
                    if __msgid_4689705936:
                        __append(translate(__msgid_4689705936, mapping=None, default=__msgid_4689705936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n            ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691693072
                    __attrs_4691693072 = _static_4659865408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4674448016 = []
                    __append_4674448016 = __stream_4674448016.append
                    __append_4674448016('You are up to date. High fives.')
                    __msgid_4674448016 = __re_whitespace(''.join(__stream_4674448016)).strip()
                    if __msgid_4674448016:
                        __append(translate(__msgid_4674448016, mapping=None, default=__msgid_4674448016, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n          </div>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x122cc1a50> name=None at 117a5b690> -> __attrs_4688581072
                __attrs_4688581072 = _static_4878768720

                # <Value 'products' (43:27)> -> __condition
                __token = 1667
                try:
                    __zt_tmp = __attrs_4688581072
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'products', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684785168
                    __attrs_4684785168 = _static_4659865408
                    __backup_product_4878586624 = get('product', __marker)

                    # <Value 'products' (45:44)> -> __iterator
                    __token = 1781
                    try:
                        __zt_tmp = __attrs_4684785168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4662095120('path', 'products', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    (__iterator, ____index_4691207312, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x122cc24a0> name=None at 1175b9e90> -> __attrs_4867835920
                        __attrs_4867835920 = _static_4878771360
                        __backup_pid_4878582976 = get('pid', __marker)

                        # <Value 'product/id' (46:30)> -> __value
                        __token = 1822
                        try:
                            __zt_tmp = __attrs_4867835920
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4662095120('path', 'product/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        econtext['pid'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x122cc0070> name=None at 117376010> -> __attrs_4689483216
                        __attrs_4689483216 = _static_4878762096

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post" class="float-end">\n              ')

                        # <Static value=<ast.Dict object at 0x122cc00a0> name=None at 117be8e90> -> __attrs_4675880592
                        __attrs_4675880592 = _static_4878762144

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="prefs_reinstallProducts:list"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4691147024
                        __default_4691147024 = _DEFAULT_MARKER

                        # <Substitution 'pid' (50:44)> -> __attr_value
                        __token = 2084
                        try:
                            __zt_tmp = __attrs_4675880592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4662095120('path', 'pid', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              ')

                        # <Static value=<ast.Dict object at 0x122cc1e70> name=None at 116b46ad0> -> __attrs_4674677584
                        __attrs_4674677584 = _static_4878769776

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-secondary" type="submit"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4692473808
                        __default_4692473808 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<Substitution 'string:Upgrade ${pid}' (56:44)> at 116a1d2d0> -> __attr_value

                        # <Substitution 'string:Upgrade ${pid}' (56:44)> -> __attr_value
                        __token = 2355
                        try:
                            __zt_tmp = __attrs_4674677584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_4662095120('string', 'Upgrade ${pid}', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', 'Upgrade ${pid}', _DEFAULT_MARKER)
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted"/>\n            </form>\n            ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4692760912
                        __attrs_4692760912 = _static_4659865408

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674528848
                        __attrs_4674528848 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4683502672
                        __default_4683502672 = _DEFAULT_MARKER

                        # <Value 'product/title' (59:33)> -> __cache_4683500560
                        __token = 2451
                        try:
                            __zt_tmp = __attrs_4674528848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4683500560 = _static_4662095120('path', 'product/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/title' (59:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117871050> -> __condition
                        __expression = __cache_4683500560

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_4683500560
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x122cc2440> name=None at 1169f9210> -> __attrs_4692933008
                        __attrs_4692933008 = _static_4878771264

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690422032
                        __attrs_4690422032 = _static_4659865408

                        # <Value 'product/description' (64:39)> -> __condition
                        __token = 2648
                        try:
                            __zt_tmp = __attrs_4690422032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('path', 'product/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4692931792
                            __default_4692931792 = _DEFAULT_MARKER

                            # <Value 'product/description' (64:73)> -> __cache_4692930448
                            __token = 2682
                            try:
                                __zt_tmp = __attrs_4690422032
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4692930448 = _static_4662095120('path', 'product/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                            # <BinOp left=<Value 'product/description' (64:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117b85a90> -> __condition
                            __expression = __cache_4692930448

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append('add-on description')
                            else:
                                __content = __cache_4692930448
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x122cc1ff0> name=None at 117923f50> -> __attrs_4690415888
                        __attrs_4690415888 = _static_4878770160

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> – (')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690417616
                        __attrs_4690417616 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4690423632
                        __default_4690423632 = _DEFAULT_MARKER

                        # <Value 'pid' (65:58)> -> __cache_4690421136
                        __token = 2809
                        try:
                            __zt_tmp = __attrs_4690417616
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4690421136 = _static_4662095120('path', 'pid', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pid' (65:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1179224d0> -> __condition
                        __expression = __cache_4690421136

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>plugin.app.name</span>')
                        else:
                            __content = __cache_4690421136
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(' ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674822032
                        __attrs_4674822032 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674824336
                        __default_4674824336 = _DEFAULT_MARKER

                        # <Value 'product/version' (65:105)> -> __cache_4674825616
                        __token = 2856
                        try:
                            __zt_tmp = __attrs_4674822032
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4674825616 = _static_4662095120('path', 'product/version', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/version' (65:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116a43e90> -> __condition
                        __expression = __cache_4674825616

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>1.0</span>')
                        else:
                            __content = __cache_4674825616
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(')</em>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x122cc17b0> name=None at 117849a50> -> __attrs_4866631056
                        __attrs_4866631056 = _static_4878768048

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="configletDetails list-group list-group-flush">\n              ')

                        # <Static value=<ast.Dict object at 0x122cb8820> name=None at 12212eed0> -> __attrs_4866626448
                        __attrs_4866626448 = _static_4878731296
                        __backup_upgrade_info_4878773808 = get('upgrade_info', __marker)

                        # <Value 'product/upgrade_info' (68:43)> -> __value
                        __token = 3022
                        try:
                            __zt_tmp = __attrs_4866626448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_4662095120('path', 'product/upgrade_info', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        econtext['upgrade_info'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n                  ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4866631632
                        __attrs_4866631632 = _static_4659865408

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_4866635600 = []
                        __append_4866635600 = __stream_4866635600.append
                        __append_4866635600('\n                    This addon has been upgraded.\n                  ')
                        __msgid_4866635600 = __re_whitespace(''.join(__stream_4866635600)).strip()
                        if __msgid_4866635600:
                            __append(translate(__msgid_4866635600, mapping=None, default=__msgid_4866635600, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n                  ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4866635280
                        __attrs_4866635280 = _static_4659865408

                        # <Value 'not:upgrade_info/hasProfile' (72:39)> -> __condition
                        __token = 3237
                        try:
                            __zt_tmp = __attrs_4866635280
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('not', 'upgrade_info/hasProfile', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_4881749760_version = ''
                            __stream_4866626576 = []
                            __append_4866626576 = __stream_4866626576.append
                            __append_4866626576('\n                    Old version was ')
                            __stream_4881749760_version = []
                            __append_4881749760_version = __stream_4881749760_version.append

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691458832
                            __attrs_4691458832 = _static_4659865408

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_4881749760_version('<strong>')

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4691448656
                            __default_4691448656 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (74:77)> -> __cache_4691459280
                            __token = 3419
                            try:
                                __zt_tmp = __attrs_4691458832
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4691459280 = _static_4662095120('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (74:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117a1c890> -> __condition
                            __expression = __cache_4691459280

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_4881749760_version('version')
                            else:
                                __content = __cache_4691459280
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_4881749760_version(__content)
                            __append_4881749760_version('</strong>')
                            __append_4866626576('${version}')
                            __stream_4881749760_version = ''.join(__stream_4881749760_version)
                            __append_4866626576('.\n                  ')
                            __msgid_4866626576 = __re_whitespace(''.join(__stream_4866626576)).strip()
                            if 'label_product_upgrade_old_version':
                                __append(translate('label_product_upgrade_old_version', mapping={'version': __stream_4881749760_version, }, default=__msgid_4866626576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691459856
                        __attrs_4691459856 = _static_4659865408

                        # <Value 'upgrade_info/hasProfile' (76:39)> -> __condition
                        __token = 3533
                        try:
                            __zt_tmp = __attrs_4691459856
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('path', 'upgrade_info/hasProfile', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                    ')

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690289680
                            __attrs_4690289680 = _static_4659865408
                            __stream_4881750432_version = ''
                            __stream_4690293200 = []
                            __append_4690293200 = __stream_4690293200.append
                            __append_4690293200('\n                      Old profile version was ')
                            __stream_4881750432_version = []
                            __append_4881750432_version = __stream_4881750432_version.append

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691283792
                            __attrs_4691283792 = _static_4659865408

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_4881750432_version('<strong>')

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4691285840
                            __default_4691285840 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/installedVersion' (78:87)> -> __cache_4691290064
                            __token = 3736
                            try:
                                __zt_tmp = __attrs_4691283792
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4691290064 = _static_4662095120('path', 'upgrade_info/installedVersion', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/installedVersion' (78:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1179f7510> -> __condition
                            __expression = __cache_4691290064

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_4881750432_version('version')
                            else:
                                __content = __cache_4691290064
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_4881750432_version(__content)
                            __append_4881750432_version('</strong>')
                            __append_4690293200('${version}')
                            __stream_4881750432_version = ''.join(__stream_4881750432_version)
                            __append_4690293200('.\n                    ')
                            __msgid_4690293200 = __re_whitespace(''.join(__stream_4690293200)).strip()
                            if 'label_product_upgrade_old_profile_version':
                                __append(translate('label_product_upgrade_old_profile_version', mapping={'version': __stream_4881750432_version, }, default=__msgid_4690293200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691296208
                            __attrs_4691296208 = _static_4659865408
                            __stream_4881750432_version = ''
                            __stream_4690293136 = []
                            __append_4690293136 = __stream_4690293136.append
                            __append_4690293136('\n                      New profile version is ')
                            __stream_4881750432_version = []
                            __append_4881750432_version = __stream_4881750432_version.append

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691286352
                            __attrs_4691286352 = _static_4659865408

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_4881750432_version('<strong>')

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4691289296
                            __default_4691289296 = _DEFAULT_MARKER

                            # <Value 'upgrade_info/newVersion' (81:86)> -> __cache_4691289616
                            __token = 3993
                            try:
                                __zt_tmp = __attrs_4691286352
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_4691289616 = _static_4662095120('path', 'upgrade_info/newVersion', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                            # <BinOp left=<Value 'upgrade_info/newVersion' (81:86)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1179f5450> -> __condition
                            __expression = __cache_4691289616

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_4881750432_version('version')
                            else:
                                __content = __cache_4691289616
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_4881750432_version(__content)
                            __append_4881750432_version('</strong>')
                            __append_4690293136('${version}')
                            __stream_4881750432_version = ''.join(__stream_4881750432_version)
                            __append_4690293136('.\n                    ')
                            __msgid_4690293136 = __re_whitespace(''.join(__stream_4690293136)).strip()
                            if 'label_product_upgrade_new_profile_version':
                                __append(translate('label_product_upgrade_new_profile_version', mapping={'version': __stream_4881750432_version, }, default=__msgid_4690293136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('\n                  </span>')
                        __append('\n\n                  ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689136144
                        __attrs_4689136144 = _static_4659865408

                        # <Value 'not:upgrade_info/available' (85:38)> -> __condition
                        __token = 4133
                        try:
                            __zt_tmp = __attrs_4689136144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('not', 'upgrade_info/available', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div>\n                    ')

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684283152
                            __attrs_4684283152 = _static_4659865408

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append('<strong>')
                            __stream_4689141840 = []
                            __append_4689141840 = __stream_4689141840.append
                            __append_4689141840('Warning')
                            __msgid_4689141840 = __re_whitespace(''.join(__stream_4689141840)).strip()
                            if __msgid_4689141840:
                                __append(translate(__msgid_4689141840, mapping=None, default=__msgid_4689141840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</strong>\n                    ')

                            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684273232
                            __attrs_4684273232 = _static_4659865408

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>')
                            __stream_4684279248 = []
                            __append_4684279248 = __stream_4684279248.append
                            __append_4684279248('There is no upgrade procedure defined for this\n                    addon. Please consult the addon documentation\n                    for upgrade information, or contact the addon\n                    author.')
                            __msgid_4684279248 = __re_whitespace(''.join(__stream_4684279248)).strip()
                            if __msgid_4684279248:
                                __append(translate(__msgid_4684279248, mapping=None, default=__msgid_4684279248, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</span>\n                  </div>')
                        __append('\n              </li>')
                        if (__backup_upgrade_info_4878773808 is __marker):
                            del econtext['upgrade_info']
                        else:
                            econtext['upgrade_info'] = __backup_upgrade_info_4878773808
                        __append('\n            </ul>\n          </li>')
                        if (__backup_pid_4878582976 is __marker):
                            del econtext['pid']
                        else:
                            econtext['pid'] = __backup_pid_4878582976
                        __append('\n          ')
                        ____index_4691207312 -= 1
                        if (____index_4691207312 > 0):
                            __append('')
                    if (__backup_product_4878586624 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_4878586624
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x122cc2a10> name=None at 115720a90> -> __attrs_4684271440
                    __attrs_4684271440 = _static_4878772752

                    # <Value 'python:num_products > 1' (96:29)> -> __condition
                    __token = 4617
                    try:
                        __zt_tmp = __attrs_4684271440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('python', 'num_products > 1', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x122cba1d0> name=None at 12217e290> -> __attrs_4866962256
                        __attrs_4866962256 = _static_4878737872

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form action="upgrade_products" method="post">\n                ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4866964816
                        __attrs_4866964816 = _static_4659865408
                        __backup_product_4878767184 = get('product', __marker)

                        # <Value 'products' (98:51)> -> __iterator
                        __token = 4787
                        try:
                            __zt_tmp = __attrs_4866964816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_4662095120('path', 'products', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        (__iterator, ____index_4866955408, ) = getname('repeat')('product', __iterator)
                        econtext['product'] = None
                        for __item in __iterator:
                            econtext['product'] = __item
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x122cb86a0> name=None at 12217f710> -> __attrs_4866965264
                            __attrs_4866965264 = _static_4878730912

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden"')

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4866951952
                            __default_4866951952 = _DEFAULT_MARKER

                            # <Substitution 'product/id' (101:44)> -> __attr_value
                            __token = 4953
                            try:
                                __zt_tmp = __attrs_4866965264
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_4662095120('path', 'product/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'product', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' name="prefs_reinstallProducts:list" />\n                ')
                            ____index_4866955408 -= 1
                            if (____index_4866955408 > 0):
                                __append('')
                        if (__backup_product_4878767184 is __marker):
                            del econtext['product']
                        else:
                            econtext['product'] = __backup_product_4878767184
                        __append('\n                ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4866953232
                        __attrs_4866953232 = _static_4659865408

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684063824
                        __attrs_4684063824 = _static_4659865408

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>')
                        __stream_4866957200 = []
                        __append_4866957200 = __stream_4866957200.append
                        __append_4866957200('This can be risky, are you sure you want to do this?')
                        __msgid_4866957200 = __re_whitespace(''.join(__stream_4866957200)).strip()
                        if 'label_product_upgrade_all_action':
                            __append(translate('label_product_upgrade_all_action', mapping=None, default=__msgid_4866957200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</div>\n                  ')

                        # <Static value=<ast.Dict object at 0x122cba320> name=None at 117312ed0> -> __attrs_4867223248
                        __attrs_4867223248 = _static_4878738208

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit"')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684060240
                        __default_4684060240 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<ast.Constant object at 0x122cb8430> at 117312290> -> __attr_value
                        __attr_value = 'Upgrade them ALL!'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' name="form.submitted" />\n                </span>\n            </form>\n            </li>')
                    __append('\n          </ul>')
                __append('\n      </section>')
                if (__backup_num_products_4878594496 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_4878594496
                if (__backup_products_4878593200 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_4878593200
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x122cc18d0> name=None at 1221bea10> -> __attrs_4867219024
                __attrs_4867219024 = _static_4878768336
                __backup_products_4878583984 = get('products', __marker)

                # <Value 'view/get_available' (116:36)> -> __value
                __token = 5522
                try:
                    __zt_tmp = __attrs_4867219024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/get_available', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_4878585424 = get('num_products', __marker)

                # <Value 'python:len(products)' (117:36)> -> __value
                __token = 5578
                try:
                    __zt_tmp = __attrs_4867219024
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', 'len(products)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="install-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x122cbaa10> name=None at 1221bdb10> -> __attrs_4692574288
                __attrs_4692574288 = _static_4878739984

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_4867223440 = []
                __append_4867223440 = __stream_4867223440.append
                __append_4867223440('Available add-ons')
                __msgid_4867223440 = __re_whitespace(''.join(__stream_4867223440)).strip()
                if __msgid_4867223440:
                    __append(translate(__msgid_4867223440, mapping=None, default=__msgid_4867223440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x122cbabf0> name=None at 117b30610> -> __attrs_4692577104
                __attrs_4692577104 = _static_4878740464

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x122cb9570> name=None at 117b306d0> -> __attrs_4686390928
                __attrs_4686390928 = _static_4878734704
                __backup_product_4878594976 = get('product', __marker)

                # <Value 'products' (121:34)> -> __iterator
                __token = 5829
                try:
                    __zt_tmp = __attrs_4686390928
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'products', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4686391568, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686394640
                    __attrs_4686394640 = _static_4659865408
                    __backup_pid_4878766416 = get('pid', __marker)

                    # <Value 'product/id' (122:35)> -> __value
                    __token = 5909
                    try:
                        __zt_tmp = __attrs_4686394640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'product/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x122cb8a00> name=None at 11754a290> -> __attrs_4681156496
                    __attrs_4681156496 = _static_4878731776

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="install_products" method="post" class="float-end">\n                ')

                    # <Static value=<ast.Dict object at 0x122cb9c30> name=None at 11704eb10> -> __attrs_4690366352
                    __attrs_4690366352 = _static_4878736432

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="install_product"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4690363728
                    __default_4690363728 = _DEFAULT_MARKER

                    # <Substitution 'pid' (126:46)> -> __attr_value
                    __token = 6129
                    try:
                        __zt_tmp = __attrs_4690366352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4662095120('path', 'pid', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x122cbafe0> name=None at 117915b90> -> __attrs_4674615760
                    __attrs_4674615760 = _static_4878741472

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-sm btn-primary" type="submit" value="Install" name="form.submitted">')
                    __stream_4690375824 = []
                    __append_4690375824 = __stream_4690375824.append
                    __append_4690375824('\n                    Install\n                ')
                    __msgid_4690375824 = __re_whitespace(''.join(__stream_4690375824)).strip()
                    if __msgid_4690375824:
                        __append(translate(__msgid_4690375824, mapping=None, default=__msgid_4690375824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </form>\n\n            ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674602576
                    __attrs_4674602576 = _static_4659865408

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n              ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674614288
                    __attrs_4674614288 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674605392
                    __default_4674605392 = _DEFAULT_MARKER

                    # <Value 'product/title' (137:33)> -> __cache_4674614416
                    __token = 6485
                    try:
                        __zt_tmp = __attrs_4674614288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4674614416 = _static_4662095120('path', 'product/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (137:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116a0f610> -> __condition
                    __expression = __cache_4674614416

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                Add-on Name\n              </span>')
                    else:
                        __content = __cache_4674614416
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            </h3>\n            ')

                    # <Static value=<ast.Dict object at 0x122cbb550> name=None at 116ba3290> -> __attrs_4676263632
                    __attrs_4676263632 = _static_4878742864

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n              ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676258256
                    __attrs_4676258256 = _static_4659865408

                    # <Value 'product/description' (142:39)> -> __condition
                    __token = 6682
                    try:
                        __zt_tmp = __attrs_4676258256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'product/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4676258384
                        __default_4676258384 = _DEFAULT_MARKER

                        # <Value 'product/description' (144:29)> -> __cache_4676264080
                        __token = 6766
                        try:
                            __zt_tmp = __attrs_4676258256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4676264080 = _static_4662095120('path', 'product/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (144:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116ba0c50> -> __condition
                        __expression = __cache_4676264080

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_4676264080
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x122cb92d0> name=None at 116ba2750> -> __attrs_4674220560
                    __attrs_4674220560 = _static_4878734032

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4688512592
                    __attrs_4688512592 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688516368
                    __default_4688516368 = _DEFAULT_MARKER

                    # <Value 'pid' (145:58)> -> __cache_4688519888
                    __token = 6875
                    try:
                        __zt_tmp = __attrs_4688512592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4688519888 = _static_4662095120('path', 'pid', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (145:58)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117753110> -> __condition
                    __expression = __cache_4688519888

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_4688519888
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4688525584
                    __attrs_4688525584 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4688519632
                    __default_4688519632 = _DEFAULT_MARKER

                    # <Value 'product/version' (145:105)> -> __cache_4688526160
                    __token = 6922
                    try:
                        __zt_tmp = __attrs_4688525584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4688526160 = _static_4662095120('path', 'product/version', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (145:105)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117753450> -> __condition
                    __expression = __cache_4688526160

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_4688526160
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n            </div>\n            ')

                    # <Static value=<ast.Dict object at 0x122cb80d0> name=None at 117753490> -> __attrs_4675226192
                    __attrs_4675226192 = _static_4878729424

                    # <Value 'not:product/uninstall_profile' (149:31)> -> __condition
                    __token = 7091
                    try:
                        __zt_tmp = __attrs_4675226192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('not', 'product/uninstall_profile', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-warning mt-2 mb-0" role="status">\n              ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675226256
                        __attrs_4675226256 = _static_4659865408

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_4675230032 = []
                        __append_4675230032 = __stream_4675230032.append
                        __append_4675230032('Warning')
                        __msgid_4675230032 = __re_whitespace(''.join(__stream_4675230032)).strip()
                        if __msgid_4675230032:
                            __append(translate(__msgid_4675230032, mapping=None, default=__msgid_4675230032, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n              ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675239376
                        __attrs_4675239376 = _static_4659865408

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_4675239504 = []
                        __append_4675239504 = __stream_4675239504.append
                        __append_4675239504('This product cannot be uninstalled!')
                        __msgid_4675239504 = __re_whitespace(''.join(__stream_4675239504)).strip()
                        if __msgid_4675239504:
                            __append(translate(__msgid_4675239504, mapping=None, default=__msgid_4675239504, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_4878766416 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_4878766416
                    __append('\n          </li>')
                    ____index_4686391568 -= 1
                    if (____index_4686391568 > 0):
                        __append('\n          ')
                if (__backup_product_4878594976 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_4878594976
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_4878585424 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_4878585424
                if (__backup_products_4878583984 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_4878583984
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x122cba9b0> name=None at 117549c90> -> __attrs_4675312976
                __attrs_4675312976 = _static_4878739888
                __backup_products_4878703664 = get('products', __marker)

                # <Value 'view/get_installed' (158:36)> -> __value
                __token = 7389
                try:
                    __zt_tmp = __attrs_4675312976
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/get_installed', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_4878586096 = get('num_products', __marker)

                # <Value 'python:len(products)' (159:39)> -> __value
                __token = 7448
                try:
                    __zt_tmp = __attrs_4675312976
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', 'len(products)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="activated-products" class="card mb-4">\n        ')

                # <Static value=<ast.Dict object at 0x122c5e770> name=None at 116ab9e90> -> __attrs_4675305744
                __attrs_4675305744 = _static_4878362480

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-header">')
                __stream_4675305552 = []
                __append_4675305552 = __stream_4675305552.append
                __append_4675305552('Activated add-ons')
                __msgid_4675305552 = __re_whitespace(''.join(__stream_4675305552)).strip()
                if __msgid_4675305552:
                    __append(translate(__msgid_4675305552, mapping=None, default=__msgid_4675305552, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n        ')

                # <Static value=<ast.Dict object at 0x122c5d9c0> name=None at 116ab8950> -> __attrs_4686218064
                __attrs_4686218064 = _static_4878358976

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="configlets list-group list-group-flush">\n          ')

                # <Static value=<ast.Dict object at 0x122c5e650> name=None at 117520250> -> __attrs_4686222608
                __attrs_4686222608 = _static_4878362192
                __backup_product_4878732544 = get('product', __marker)

                # <Value 'products' (163:34)> -> __iterator
                __token = 7701
                try:
                    __zt_tmp = __attrs_4686222608
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'products', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4653926928, ) = getname('repeat')('product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-group-item mt-2 pb-3">\n          ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4653929360
                    __attrs_4653929360 = _static_4659865408
                    __backup_pid_4878764400 = get('pid', __marker)

                    # <Value 'product/id' (164:35)> -> __value
                    __token = 7781
                    try:
                        __zt_tmp = __attrs_4653929360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('path', 'product/id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x122c5f8b0> name=None at 115654550> -> __attrs_4675157136
                    __attrs_4675157136 = _static_4878366896

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form action="uninstall_products" method="post" class="float-end">\n              ')

                    # <Static value=<ast.Dict object at 0x122c5f340> name=None at 116a91550> -> __attrs_4688693136
                    __attrs_4688693136 = _static_4878365504

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="uninstall_product"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4675144272
                    __default_4675144272 = _DEFAULT_MARKER

                    # <Substitution 'pid' (168:42)> -> __attr_value
                    __token = 7995
                    try:
                        __zt_tmp = __attrs_4688693136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_4662095120('path', 'pid', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n              ')

                    # <Static value=<ast.Dict object at 0x122c5e2f0> name=None at 11777d910> -> __attrs_4681664016
                    __attrs_4681664016 = _static_4878361328

                    # <Value 'product/uninstall_profile' (173:37)> -> __condition
                    __token = 8213
                    try:
                        __zt_tmp = __attrs_4681664016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'product/uninstall_profile', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button class="btn btn-sm btn-danger" type="submit" value="Uninstall" name="form.submitted">')
                        __stream_4688705616 = []
                        __append_4688705616 = __stream_4688705616.append
                        __append_4688705616('\n                Uninstall\n              ')
                        __msgid_4688705616 = __re_whitespace(''.join(__stream_4688705616)).strip()
                        if __msgid_4688705616:
                            __append(translate(__msgid_4688705616, mapping=None, default=__msgid_4688705616, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>')
                    __append('\n            </form>\n              ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689062928
                    __attrs_4689062928 = _static_4659865408

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h3>\n                ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689063248
                    __attrs_4689063248 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689064784
                    __default_4689064784 = _DEFAULT_MARKER

                    # <Value 'product/title' (179:35)> -> __cache_4689064016
                    __token = 8405
                    try:
                        __zt_tmp = __attrs_4689063248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4689064016 = _static_4662095120('path', 'product/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/title' (179:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1177d7290> -> __condition
                    __expression = __cache_4689064016

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>\n                  Add-on Name\n                </span>')
                    else:
                        __content = __cache_4689064016
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n              </h3>\n              ')

                    # <Static value=<ast.Dict object at 0x122c5dc60> name=None at 1173dea90> -> __attrs_4684897936
                    __attrs_4684897936 = _static_4878359648

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="configletDescription discreet">\n                ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4692721616
                    __attrs_4692721616 = _static_4659865408

                    # <Value 'product/description' (184:41)> -> __condition
                    __token = 8612
                    try:
                        __zt_tmp = __attrs_4692721616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'product/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684891152
                        __default_4684891152 = _DEFAULT_MARKER

                        # <Value 'product/description' (186:31)> -> __cache_4684900304
                        __token = 8700
                        try:
                            __zt_tmp = __attrs_4692721616
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4684900304 = _static_4662095120('path', 'product/description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/description' (186:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1173de050> -> __condition
                        __expression = __cache_4684900304

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('add-on description')
                        else:
                            __content = __cache_4684900304
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x122c5f910> name=None at 117b52010> -> __attrs_4691926352
                    __attrs_4691926352 = _static_4878366992

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append('<em class="discreet"> – (')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4651745232
                    __attrs_4651745232 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4651741264
                    __default_4651741264 = _DEFAULT_MARKER

                    # <Value 'pid' (187:60)> -> __cache_4691922320
                    __token = 8811
                    try:
                        __zt_tmp = __attrs_4651745232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4691922320 = _static_4662095120('path', 'pid', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'pid' (187:60)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117a92c10> -> __condition
                    __expression = __cache_4691922320

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>plugin.app.name</span>')
                    else:
                        __content = __cache_4691922320
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(' ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4681750928
                    __attrs_4681750928 = _static_4659865408

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681755600
                    __default_4681755600 = _DEFAULT_MARKER

                    # <Value 'product/version' (187:107)> -> __cache_4681746320
                    __token = 8858
                    try:
                        __zt_tmp = __attrs_4681750928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4681746320 = _static_4662095120('path', 'product/version', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'product/version' (187:107)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1170dd7d0> -> __condition
                    __expression = __cache_4681746320

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>1.0</span>')
                    else:
                        __content = __cache_4681746320
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</em>\n              </div>\n              ')

                    # <Static value=<ast.Dict object at 0x122c5dc30> name=None at 1170dd390> -> __attrs_4867370256
                    __attrs_4867370256 = _static_4878359600

                    # <Value 'not:product/uninstall_profile' (191:33)> -> __condition
                    __token = 9032
                    try:
                        __zt_tmp = __attrs_4867370256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('not', 'product/uninstall_profile', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="alert alert-info mt-2 mb-0" role="status">\n                ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4867361744
                        __attrs_4867361744 = _static_4659865408

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append('<strong>')
                        __stream_4867373264 = []
                        __append_4867373264 = __stream_4867373264.append
                        __append_4867373264('Info')
                        __msgid_4867373264 = __re_whitespace(''.join(__stream_4867373264)).strip()
                        if __msgid_4867373264:
                            __append(translate(__msgid_4867373264, mapping=None, default=__msgid_4867373264, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</strong>\n                ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4867374032
                        __attrs_4867374032 = _static_4659865408

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')
                        __stream_4867367312 = []
                        __append_4867367312 = __stream_4867367312.append
                        __append_4867367312('This product cannot be uninstalled!')
                        __msgid_4867367312 = __re_whitespace(''.join(__stream_4867367312)).strip()
                        if __msgid_4867367312:
                            __append(translate(__msgid_4867367312, mapping=None, default=__msgid_4867367312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n            </div>')
                    __append('\n          ')
                    if (__backup_pid_4878764400 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_4878764400
                    __append('\n          </li>')
                    ____index_4653926928 -= 1
                    if (____index_4653926928 > 0):
                        __append('\n          ')
                if (__backup_product_4878732544 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_4878732544
                __append('\n        </ul>\n      </section>')
                if (__backup_num_products_4878586096 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_4878586096
                if (__backup_products_4878703664 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_4878703664
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x122cb9e70> name=None at 115655d10> -> __attrs_4867368016
                __attrs_4867368016 = _static_4878737008
                __backup_products_4878582208 = get('products', __marker)

                # <Value 'view/get_broken' (200:36)> -> __value
                __token = 9331
                try:
                    __zt_tmp = __attrs_4867368016
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/get_broken', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_4878771552 = get('num_products', __marker)

                # <Value 'python:len(products)' (201:40)> -> __value
                __token = 9388
                try:
                    __zt_tmp = __attrs_4867368016
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', 'len(products)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value 'num_products' (202:31)> -> __condition
                __token = 9443
                try:
                    __zt_tmp = __attrs_4867368016
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'num_products', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append('<section id="broken-products" class="card mb-4">\n        ')

                    # <Static value=<ast.Dict object at 0x122c5c280> name=None at 116b5fb10> -> __attrs_4675980880
                    __attrs_4675980880 = _static_4878353024

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header class="card-header">')
                    __stream_4867367632 = []
                    __append_4867367632 = __stream_4867367632.append
                    __append_4867367632('Broken add-ons')
                    __msgid_4867367632 = __re_whitespace(''.join(__stream_4867367632)).strip()
                    if __msgid_4867367632:
                        __append(translate(__msgid_4867367632, mapping=None, default=__msgid_4867367632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</header>\n        ')

                    # <Static value=<ast.Dict object at 0x122c5f5e0> name=None at 116b5d990> -> __attrs_4675978640
                    __attrs_4675978640 = _static_4878366176

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="configlets list-group list-group-flush">\n          ')

                    # <Static value=<ast.Dict object at 0x122c5f9a0> name=None at 116b5d810> -> __attrs_4866216528
                    __attrs_4866216528 = _static_4878367136
                    __backup_product_4878368432 = get('product', __marker)

                    # <Value 'products' (206:34)> -> __iterator
                    __token = 9685
                    try:
                        __zt_tmp = __attrs_4866216528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_4662095120('path', 'products', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    (__iterator, ____index_4866215696, ) = getname('repeat')('product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="list-group-item mt-2 pb-3">\n            ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4866215568
                        __attrs_4866215568 = _static_4659865408

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3>\n              ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4693304976
                        __attrs_4693304976 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4669686416
                        __default_4669686416 = _DEFAULT_MARKER

                        # <Value 'product/product_id' (208:33)> -> __cache_4669691216
                        __token = 9780
                        try:
                            __zt_tmp = __attrs_4693304976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4669691216 = _static_4662095120('path', 'product/product_id', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/product_id' (208:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11655ca50> -> __condition
                        __expression = __cache_4669691216

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>\n                Add-on Name\n              </span>')
                        else:
                            __content = __cache_4669691216
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            </h3>\n            ')

                        # <Static value=<ast.Dict object at 0x122c4d360> name=None at 117be3450> -> __attrs_4693305680
                        __attrs_4693305680 = _static_4878291808

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="configletDescription discreet">\n              ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670777744
                        __attrs_4670777744 = _static_4659865408

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4693308240
                        __default_4693308240 = _DEFAULT_MARKER

                        # <Value 'product/type' (213:33)> -> __cache_4693295184
                        __token = 9976
                        try:
                            __zt_tmp = __attrs_4670777744
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4693295184 = _static_4662095120('path', 'product/type', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/type' (213:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117be3b10> -> __condition
                        __expression = __cache_4693295184

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Type')
                        else:
                            __content = __cache_4693295184
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n              ')

                        # <Static value=<ast.Dict object at 0x122c4c8e0> name=None at 1166672d0> -> __attrs_4674276112
                        __attrs_4674276112 = _static_4878289120

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append('<em class="discreet"> - ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674278480
                        __attrs_4674278480 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674285520
                        __default_4674285520 = _DEFAULT_MARKER

                        # <Value 'product/value' (214:61)> -> __cache_4674285968
                        __token = 10087
                        try:
                            __zt_tmp = __attrs_4674278480
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4674285968 = _static_4662095120('path', 'product/value', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'product/value' (214:61)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1169bce90> -> __condition
                        __expression = __cache_4674285968

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Error Reason')
                        else:
                            __content = __cache_4674285968
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</em>\n            </div>\n          </li>')
                        ____index_4866215696 -= 1
                        if (____index_4866215696 > 0):
                            __append('\n          ')
                    if (__backup_product_4878368432 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_4878368432
                    __append('\n        </ul>\n      </section>')
                if (__backup_num_products_4878771552 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_4878771552
                if (__backup_products_4878582208 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_4878582208
                __append('\n\n  </div>\n')
                __i18n_domain = __previous_i18n_domain_4867061584
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4865989264
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4662095120('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4671260928 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4671260928
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }