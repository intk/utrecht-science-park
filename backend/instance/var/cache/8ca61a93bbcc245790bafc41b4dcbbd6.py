# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/Products/CMFPlone/controlpanel/browser/overview.pt'

__tokens = {421: ("python:request.set('disable_plone.leftcolumn',1)", 12, 47), 517: (" python:request.set('disable_plone.rightcolumn',1", 13, 46), 979: ('view/upgrade_warning', 26, 23), 1261: ('string:${context/portal_url}/@@plone-upgrade', 34, 35), 1644: ('view/mailhost_warning', 46, 23), 2215: ('string:${portal_url}/@@mail-controlpanel', 57, 39), 2449: ('view/timezone_warning', 66, 23), 2982: ('string:${portal_url}/@@dateandtime-controlpanel', 78, 39), 3241: ('not:view/pil', 87, 23), 3522: ('view/categories', 96, 37), 3574: ("python:view.sublists(category.get('id'))", 97, 34), 3680: ('sublist', 98, 63), 3724: ('category/title', 99, 34), 3823: ('sublist', 102, 40), 3978: ('sublist', 105, 29), 4032: ('sublist', 106, 44), 4092: ('action/visible', 107, 50), 4244: ('action/icon', 109, 37), 4297: (" python:'http' in action['icon'", 110, 40), 4372: ('action/url', 111, 41), 4466: ('icon_url', 113, 42), 4571: ('action/icon', 115, 44), 4627: (' action/titl', 116, 43), 4736: ('not: icon_url', 118, 47), 4798: ("python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", 119, 47), 4976: ('action/title', 121, 38), 5339: ('not:sublist', 133, 31), 5702: ('view/version_overview', 145, 41), 5751: ('version', 146, 25), 5842: ('view/server_info', 148, 42), 5898: (' server_info/wsg', 149, 38), 6042: ('has_wsgi', 152, 51), 6113: ('not:has_wsgi', 153, 51), 6246: ('${server_info/server_name}', 157, 18), 6248: ('server_info/server_name', 157, 20), 6298: ('${server_info/version}', 158, 18), 6300: ('server_info/version', 158, 20), 6397: ('not:view/is_dev_mode', 163, 22), 6969: ('view/is_dev_mode', 175, 22), 261: ('here/prefs_main_template/macros/master', 6, 23), 261: ('here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_4878598096 = {'class': '', }
_static_4878582256 = {'class': '', }
_static_4878582688 = {'class': 'controlPanelSectionFooter', }
_static_4878596368 = {'class': 'discreet', }
_static_4878584992 = {'class': 'text-decoration-none text-center ', }
_static_4878595936 = {'src': '', 'alt': '', 'class': 'icon', }
_static_4878594832 = {'class': 'mb-3', }
_static_4878594688 = {'href': '', 'class': 'd-block text-dark text-center py-4 rounded btn btn-light h-100', }
_static_4878588688 = {'class': 'col mb-4', }
_static_4878582736 = {'class': 'configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100', }
_static_4878592864 = {'class': 'row', }
_static_4878593680 = {'class': '', }
_static_4878585808 = {'class': 'controlPanelSection mb-4', }
_static_4878585664 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_4878584272 = {'href': '', }
_static_4878584320 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_4878592096 = {'href': '', }
_static_4878711440 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_4878707840 = {'href': '#', 'title': 'Go to the upgrade page', }
_static_4878705728 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_4878706592 = {'class': 'lead', }
_static_4878697616 = {'class': 'documentFirstHeading', }
_static_4878702608 = {'class': 'controlPanel controlPanelOverview', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4878700544 = 'master'
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

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4691705296
            __attrs_4691705296 = _static_4659865408
            __previous_i18n_domain_4691704080 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_4686775040 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x122cb1000> name=None at 117a59050> -> __value
            __value = _static_4878700544
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684245776
                __attrs_4684245776 = _static_4659865408
                __backup_disable_column_one_4878706208 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 421
                try:
                    __zt_tmp = __attrs_4684245776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_4878696704 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 517
                try:
                    __zt_tmp = __attrs_4684245776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_4878696704 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_4878696704
                if (__backup_disable_column_one_4878706208 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_4878706208
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x122cb1810> name=None at 1166ab150> -> __attrs_4686414224
                __attrs_4686414224 = _static_4878702608

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="controlPanel controlPanelOverview">\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686413904
                __attrs_4686413904 = _static_4659865408

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n    ')

                # <Static value=<ast.Dict object at 0x122cb0490> name=None at 117550b90> -> __attrs_4686908624
                __attrs_4686908624 = _static_4878697616

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_4686424912 = []
                __append_4686424912 = __stream_4686424912.append
                __append_4686424912('Site Setup')
                __msgid_4686424912 = __re_whitespace(''.join(__stream_4686424912)).strip()
                if __msgid_4686424912:
                    __append(translate(__msgid_4686424912, mapping=None, default=__msgid_4686424912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x122cb27a0> name=None at 1175c81d0> -> __attrs_4686915088
                __attrs_4686915088 = _static_4878706592

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_4686911440 = []
                __append_4686911440 = __stream_4686911440.append
                __append_4686911440('\n        Configuration area for Plone and add-on Products.\n    ')
                __msgid_4686911440 = __re_whitespace(''.join(__stream_4686911440)).strip()
                if 'description_control_panel':
                    __append(translate('description_control_panel', mapping=None, default=__msgid_4686911440, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x122cb2440> name=None at 1175cb150> -> __attrs_4671306000
                __attrs_4671306000 = _static_4878705728

                # <Value 'view/upgrade_warning' (26:23)> -> __condition
                __token = 979
                try:
                    __zt_tmp = __attrs_4671306000
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'view/upgrade_warning', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689537936
                    __attrs_4689537936 = _static_4659865408

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4689542800 = []
                    __append_4689542800 = __stream_4689542800.append
                    __append_4689542800('\n          Warning\n      ')
                    __msgid_4689542800 = __re_whitespace(''.join(__stream_4689542800)).strip()
                    if __msgid_4689542800:
                        __append(translate(__msgid_4689542800, mapping=None, default=__msgid_4689542800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689539024
                    __attrs_4689539024 = _static_4659865408
                    __stream_4879845408_link_continue_with_the_upgrade = ''
                    __stream_4689541648 = []
                    __append_4689541648 = __stream_4689541648.append
                    __append_4689541648('\n          The site configuration is outdated and needs to be\n          upgraded. Please\n          ')
                    __stream_4879845408_link_continue_with_the_upgrade = []
                    __append_4879845408_link_continue_with_the_upgrade = __stream_4879845408_link_continue_with_the_upgrade.append

                    # <Static value=<ast.Dict object at 0x122cb2c80> name=None at 11784a590> -> __attrs_4683853328
                    __attrs_4683853328 = _static_4878707840

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4879845408_link_continue_with_the_upgrade('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4669650064
                    __default_4669650064 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/portal_url}/@@plone-upgrade' (34:35)> -> __attr_href
                    __token = 1261
                    try:
                        __zt_tmp = __attrs_4683853328
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('string', '${context/portal_url}/@@plone-upgrade', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4879845408_link_continue_with_the_upgrade((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673796048
                    __default_4673796048 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x122c972b0> at 11784a2d0> -> __attr_title
                    __attr_title = 'Go to the upgrade page'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append_4879845408_link_continue_with_the_upgrade((' title="%s"' % __attr_title))
                    __append_4879845408_link_continue_with_the_upgrade('>')
                    __stream_4689541904 = []
                    __append_4689541904 = __stream_4689541904.append
                    __append_4689541904('\n            continue with the upgrade\n          ')
                    __msgid_4689541904 = __re_whitespace(''.join(__stream_4689541904)).strip()
                    if __msgid_4689541904:
                        __append_4879845408_link_continue_with_the_upgrade(translate(__msgid_4689541904, mapping=None, default=__msgid_4689541904, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_4879845408_link_continue_with_the_upgrade('</a>')
                    __append_4689541648('${link_continue_with_the_upgrade}')
                    __stream_4879845408_link_continue_with_the_upgrade = ''.join(__stream_4879845408_link_continue_with_the_upgrade)
                    __append_4689541648('.\n      ')
                    __msgid_4689541648 = __re_whitespace(''.join(__stream_4689541648)).strip()
                    if __msgid_4689541648:
                        __append(translate(__msgid_4689541648, mapping={'link_continue_with_the_upgrade': __stream_4879845408_link_continue_with_the_upgrade, }, default=__msgid_4689541648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x122cb3a90> name=None at 117849e50> -> __attrs_4683851024
                __attrs_4683851024 = _static_4878711440

                # <Value 'view/mailhost_warning' (46:23)> -> __condition
                __token = 1644
                try:
                    __zt_tmp = __attrs_4683851024
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'view/mailhost_warning', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676754768
                    __attrs_4676754768 = _static_4659865408

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4683856400 = []
                    __append_4683856400 = __stream_4683856400.append
                    __append_4683856400('\n          Warning\n      ')
                    __msgid_4683856400 = __re_whitespace(''.join(__stream_4683856400)).strip()
                    if __msgid_4683856400:
                        __append(translate(__msgid_4683856400, mapping=None, default=__msgid_4683856400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676760144
                    __attrs_4676760144 = _static_4659865408
                    __stream_4879845408_label_mail_control_panel_link = ''
                    __stream_4676757136 = []
                    __append_4676757136 = __stream_4676757136.append
                    __append_4676757136("\n          You have not configured a mail host or a site 'From'\n          address, various features including contact forms, email\n          notification and password reset will not work. Go to the\n          ")
                    __stream_4879845408_label_mail_control_panel_link = []
                    __append_4879845408_label_mail_control_panel_link = __stream_4879845408_label_mail_control_panel_link.append

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4676758288
                    __attrs_4676758288 = _static_4659865408
                    __append_4879845408_label_mail_control_panel_link('\n              ')

                    # <Static value=<ast.Dict object at 0x122c96860> name=None at 1166276d0> -> __attrs_4670515472
                    __attrs_4670515472 = _static_4878592096

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4879845408_label_mail_control_panel_link('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670515536
                    __default_4670515536 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@mail-controlpanel' (57:39)> -> __attr_href
                    __token = 2215
                    try:
                        __zt_tmp = __attrs_4670515472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('string', '${portal_url}/@@mail-controlpanel', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4879845408_label_mail_control_panel_link((' href="%s"' % __attr_href))
                    __append_4879845408_label_mail_control_panel_link(' >')
                    __stream_4670507344 = []
                    __append_4670507344 = __stream_4670507344.append
                    __append_4670507344('Mail control panel')
                    __msgid_4670507344 = __re_whitespace(''.join(__stream_4670507344)).strip()
                    if 'text_no_mailhost_configured_control_panel_link':
                        __append_4879845408_label_mail_control_panel_link(translate('text_no_mailhost_configured_control_panel_link', mapping=None, default=__msgid_4670507344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_4879845408_label_mail_control_panel_link('</a>\n          ')
                    __append_4676757136('${label_mail_control_panel_link}')
                    __stream_4879845408_label_mail_control_panel_link = ''.join(__stream_4879845408_label_mail_control_panel_link)
                    __append_4676757136('\n          to fix this.\n      ')
                    __msgid_4676757136 = __re_whitespace(''.join(__stream_4676757136)).strip()
                    if 'text_no_mailhost_configured':
                        __append(translate('text_no_mailhost_configured', mapping={'label_mail_control_panel_link': __stream_4879845408_label_mail_control_panel_link, }, default=__msgid_4676757136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x122c94a00> name=None at 116c1a610> -> __attrs_4670508176
                __attrs_4670508176 = _static_4878584320

                # <Value 'view/timezone_warning' (66:23)> -> __condition
                __token = 2449
                try:
                    __zt_tmp = __attrs_4670508176
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'view/timezone_warning', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670518288
                    __attrs_4670518288 = _static_4659865408

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4670511056 = []
                    __append_4670511056 = __stream_4670511056.append
                    __append_4670511056('\n          Warning\n      ')
                    __msgid_4670511056 = __re_whitespace(''.join(__stream_4670511056)).strip()
                    if __msgid_4670511056:
                        __append(translate(__msgid_4670511056, mapping=None, default=__msgid_4670511056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670512848
                    __attrs_4670512848 = _static_4659865408
                    __stream_4879845408_label_mail_event_settings_link = ''
                    __stream_4670516496 = []
                    __append_4670516496 = __stream_4670516496.append
                    __append_4670516496('\n\n          You have not set the portal timezone. Date/Time handling will not\n          work properly for timezone aware date/time values.\n          Go to the\n          ')
                    __stream_4879845408_label_mail_event_settings_link = []
                    __append_4879845408_label_mail_event_settings_link = __stream_4879845408_label_mail_event_settings_link.append

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689315536
                    __attrs_4689315536 = _static_4659865408
                    __append_4879845408_label_mail_event_settings_link('\n              ')

                    # <Static value=<ast.Dict object at 0x122c949d0> name=None at 1178167d0> -> __attrs_4689316368
                    __attrs_4689316368 = _static_4878584272

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_4879845408_label_mail_event_settings_link('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689329744
                    __default_4689329744 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@dateandtime-controlpanel' (78:39)> -> __attr_href
                    __token = 2982
                    try:
                        __zt_tmp = __attrs_4689316368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('string', '${portal_url}/@@dateandtime-controlpanel', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_4879845408_label_mail_event_settings_link((' href="%s"' % __attr_href))
                    __append_4879845408_label_mail_event_settings_link(' >')
                    __stream_4689327696 = []
                    __append_4689327696 = __stream_4689327696.append
                    __append_4689327696('Date and Time Settings control panel')
                    __msgid_4689327696 = __re_whitespace(''.join(__stream_4689327696)).strip()
                    if 'text_no_timezone_configured_control_panel_link':
                        __append_4879845408_label_mail_event_settings_link(translate('text_no_timezone_configured_control_panel_link', mapping=None, default=__msgid_4689327696, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_4879845408_label_mail_event_settings_link('</a>\n          ')
                    __append_4670516496('${label_mail_event_settings_link}')
                    __stream_4879845408_label_mail_event_settings_link = ''.join(__stream_4879845408_label_mail_event_settings_link)
                    __append_4670516496('\n          to fix this.\n      ')
                    __msgid_4670516496 = __re_whitespace(''.join(__stream_4670516496)).strip()
                    if 'text_no_timezone_configured':
                        __append(translate('text_no_timezone_configured', mapping={'label_mail_event_settings_link': __stream_4879845408_label_mail_event_settings_link, }, default=__msgid_4670516496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x122c94f40> name=None at 116627010> -> __attrs_4689314128
                __attrs_4689314128 = _static_4878585664

                # <Value 'not:view/pil' (87:23)> -> __condition
                __token = 3241
                try:
                    __zt_tmp = __attrs_4689314128
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('not', 'view/pil', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689321616
                    __attrs_4689321616 = _static_4659865408

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_4689319824 = []
                    __append_4689319824 = __stream_4689319824.append
                    __append_4689319824('\n          Warning\n      ')
                    __msgid_4689319824 = __re_whitespace(''.join(__stream_4689319824)).strip()
                    if __msgid_4689319824:
                        __append(translate(__msgid_4689319824, mapping=None, default=__msgid_4689319824, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689328400
                    __attrs_4689328400 = _static_4659865408
                    __stream_4689323408 = []
                    __append_4689323408 = __stream_4689323408.append
                    __append_4689323408('\n          PIL is not installed properly, image scaling will not work.\n      ')
                    __msgid_4689323408 = __re_whitespace(''.join(__stream_4689323408)).strip()
                    if 'text_no_pil_installed':
                        __append(translate('text_no_pil_installed', mapping=None, default=__msgid_4689323408, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689327440
                __attrs_4689327440 = _static_4659865408
                __backup_category_4878701648 = get('category', __marker)

                # <Value 'view/categories' (96:37)> -> __iterator
                __token = 3522
                try:
                    __zt_tmp = __attrs_4689327440
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'view/categories', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4689324432, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689325776
                    __attrs_4689325776 = _static_4659865408
                    __backup_sublist_4878699536 = get('sublist', __marker)

                    # <Value "python:view.sublists(category.get('id'))" (97:34)> -> __value
                    __token = 3574
                    try:
                        __zt_tmp = __attrs_4689325776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', "view.sublists(category.get('id'))", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['sublist'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x122c94fd0> name=None at 116ab9ed0> -> __attrs_4675319568
                    __attrs_4675319568 = _static_4878585808

                    # <Value 'sublist' (98:63)> -> __condition
                    __token = 3680
                    try:
                        __zt_tmp = __attrs_4675319568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'sublist', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append('<section class="controlPanelSection mb-4">\n        ')

                        # <Static value=<ast.Dict object at 0x122c96e90> name=None at 116ab8c10> -> __attrs_4675313104
                        __attrs_4675313104 = _static_4878593680

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3 class="">')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4675315344
                        __default_4675315344 = _DEFAULT_MARKER

                        # <Value 'category/title' (99:34)> -> __cache_4675315792
                        __token = 3724
                        try:
                            __zt_tmp = __attrs_4675313104
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4675315792 = _static_4662095120('path', 'category/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'category/title' (99:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117902090> -> __condition
                        __expression = __cache_4675315792

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Category')
                        else:
                            __content = __cache_4675315792
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</h3>\n\n        ')

                        # <Static value=<ast.Dict object at 0x122c96b60> name=None at 116a0e490> -> __attrs_4674611856
                        __attrs_4674611856 = _static_4878592864

                        # <Value 'sublist' (102:40)> -> __condition
                        __token = 3823
                        try:
                            __zt_tmp = __attrs_4674611856
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('path', 'sublist', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <nav ... (0:0)
                            # --------------------------------------------------------
                            __append('<nav class="row">\n\n          ')

                            # <Static value=<ast.Dict object at 0x122c943d0> name=None at 116a0d750> -> __attrs_4674607568
                            __attrs_4674607568 = _static_4878582736

                            # <Value 'sublist' (105:29)> -> __condition
                            __token = 3978
                            try:
                                __zt_tmp = __attrs_4674607568
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_4662095120('path', 'sublist', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            if __condition:

                                # <ul ... (0:0)
                                # --------------------------------------------------------
                                __append('<ul class="configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100">\n            ')

                                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674616272
                                __attrs_4674616272 = _static_4659865408
                                __backup_action_4878587968 = get('action', __marker)

                                # <Value 'sublist' (106:44)> -> __iterator
                                __token = 4032
                                try:
                                    __zt_tmp = __attrs_4674616272
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_4662095120('path', 'sublist', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                (__iterator, ____index_4674616592, ) = getname('repeat')('action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item
                                    __append('\n              ')

                                    # <Static value=<ast.Dict object at 0x122c95b10> name=None at 116a0e9d0> -> __attrs_4654670800
                                    __attrs_4654670800 = _static_4878588688

                                    # <Value 'action/visible' (107:50)> -> __condition
                                    __token = 4092
                                    try:
                                        __zt_tmp = __attrs_4654670800
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_4662095120('path', 'action/visible', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                    if __condition:

                                        # <li ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<li class="col mb-4">\n                ')

                                        # <Static value=<ast.Dict object at 0x122c97280> name=None at 11736ce50> -> __attrs_4671233680
                                        __attrs_4671233680 = _static_4878594688
                                        __backup_icon_4878591616 = get('icon', __marker)

                                        # <Value 'action/icon' (109:37)> -> __value
                                        __token = 4244
                                        try:
                                            __zt_tmp = __attrs_4671233680
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_4662095120('path', 'action/icon', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                        econtext['icon'] = __value
                                        __backup_icon_url_4878597040 = get('icon_url', __marker)

                                        # <Value "python:'http' in action['icon']" (110:40)> -> __value
                                        __token = 4297
                                        try:
                                            __zt_tmp = __attrs_4671233680
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_4662095120('python', "'http' in action['icon']", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                        econtext['icon_url'] = __value

                                        # <a ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<a')

                                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684438480
                                        __default_4684438480 = _DEFAULT_MARKER

                                        # <Substitution 'action/url' (111:41)> -> __attr_href
                                        __token = 4372
                                        try:
                                            __zt_tmp = __attrs_4671233680
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_href = _static_4662095120('path', 'action/url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_href is not None):
                                            __append((' href="%s"' % __attr_href))
                                        __append(' class="d-block text-dark text-center py-4 rounded btn btn-light h-100">\n                    ')

                                        # <Static value=<ast.Dict object at 0x122c97310> name=None at 1166d4710> -> __attrs_4671237328
                                        __attrs_4671237328 = _static_4878594832

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="mb-3">\n                      ')

                                        # <Static value=<ast.Dict object at 0x122c97760> name=None at 1166d7ed0> -> __attrs_4671238096
                                        __attrs_4671238096 = _static_4878595936

                                        # <Value 'icon_url' (113:42)> -> __condition
                                        __token = 4466
                                        try:
                                            __zt_tmp = __attrs_4671238096
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_4662095120('path', 'icon_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                        if __condition:

                                            # <img ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<img')

                                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671239120
                                            __default_4671239120 = _DEFAULT_MARKER

                                            # <Substitution 'action/icon' (115:44)> -> __attr_src
                                            __token = 4571
                                            try:
                                                __zt_tmp = __attrs_4671238096
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_src = _static_4662095120('path', 'action/icon', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                            __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                            if (__attr_src is not None):
                                                __append((' src="%s"' % __attr_src))

                                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671234320
                                            __default_4671234320 = _DEFAULT_MARKER

                                            # <Translate msgid=None node=<Substitution 'action/title' (116:43)> at 1166d6890> -> __attr_alt

                                            # <Substitution 'action/title' (116:43)> -> __attr_alt
                                            __token = 4627
                                            try:
                                                __zt_tmp = __attrs_4671238096
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_alt = _static_4662095120('path', 'action/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            if (__attr_alt is not None):
                                                __append((' alt="%s"' % __attr_alt))
                                            __append(' class="icon">')
                                        __append('\n                      ')

                                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675015120
                                        __attrs_4675015120 = _static_4659865408

                                        # <Value 'not: icon_url' (118:47)> -> __condition
                                        __token = 4736
                                        try:
                                            __zt_tmp = __attrs_4675015120
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_4662095120('not', ' icon_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                                        if __condition:

                                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4675011152
                                            __default_4675011152 = _DEFAULT_MARKER

                                            # <Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> -> __cache_4675025168
                                            __token = 4798
                                            try:
                                                __zt_tmp = __attrs_4675015120
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __cache_4675025168 = _static_4662095120('python', "icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                            # <BinOp left=<Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116a71f10> -> __condition
                                            __expression = __cache_4675025168

                                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                            __value = _DEFAULT_MARKER
                                            __condition = (__expression is __value)
                                            if __condition:
                                                pass
                                            else:
                                                __content = __cache_4675025168
                                                __content = __convert(__content)
                                                if (__content is not None):
                                                    __append(__content)
                                        __append('\n                    </div>\n                    ')

                                        # <Static value=<ast.Dict object at 0x122c94ca0> name=None at 116a71110> -> __attrs_4675019984
                                        __attrs_4675019984 = _static_4878584992

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="text-decoration-none text-center ">')

                                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4675021392
                                        __default_4675021392 = _DEFAULT_MARKER

                                        # <Value 'action/title' (121:38)> -> __cache_4675010704
                                        __token = 4976
                                        try:
                                            __zt_tmp = __attrs_4675019984
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_4675010704 = _static_4662095120('path', 'action/title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                                        # <BinOp left=<Value 'action/title' (121:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116a72dd0> -> __condition
                                        __expression = __cache_4675010704

                                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            __append('\n                        Title\n                    ')
                                        else:
                                            __content = __cache_4675010704
                                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            __content = __quote(__content, None, '\xad', None, None)
                                            if (__content is not None):
                                                __append(__content)
                                        __append('</div>\n                </a>')
                                        if (__backup_icon_url_4878597040 is __marker):
                                            del econtext['icon_url']
                                        else:
                                            econtext['icon_url'] = __backup_icon_url_4878597040
                                        if (__backup_icon_4878591616 is __marker):
                                            del econtext['icon']
                                        else:
                                            econtext['icon'] = __backup_icon_4878591616
                                        __append('\n              </li>')
                                    __append('\n            ')
                                    ____index_4674616592 -= 1
                                    if (____index_4674616592 > 0):
                                        __append('')
                                if (__backup_action_4878587968 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_4878587968
                                __append('\n            </ul>')
                            __append('\n          </nav>')
                        __append('\n\n          ')

                        # <Static value=<ast.Dict object at 0x122c97910> name=None at 116a0fd90> -> __attrs_4675020048
                        __attrs_4675020048 = _static_4878596368

                        # <Value 'not:sublist' (133:31)> -> __condition
                        __token = 5339
                        try:
                            __zt_tmp = __attrs_4675020048
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('not', 'sublist', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="discreet">')
                            __stream_4674614736 = []
                            __append_4674614736 = __stream_4674614736.append
                            __append_4674614736('\n              No preference panels available.\n          ')
                            __msgid_4674614736 = __re_whitespace(''.join(__stream_4674614736)).strip()
                            if 'label_no_prefs_panels_available':
                                __append(translate('label_no_prefs_panels_available', mapping=None, default=__msgid_4674614736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</div>')
                        __append('\n\n      </section>')
                    __append('\n    ')
                    if (__backup_sublist_4878699536 is __marker):
                        del econtext['sublist']
                    else:
                        econtext['sublist'] = __backup_sublist_4878699536
                    __append('\n  ')
                    ____index_4689324432 -= 1
                    if (____index_4689324432 > 0):
                        __append('')
                if (__backup_category_4878701648 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_4878701648
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x122c943a0> name=None at 117817ad0> -> __attrs_4689315920
                __attrs_4689315920 = _static_4878582688

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="controlPanelSectionFooter">\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675020560
                __attrs_4675020560 = _static_4659865408

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_4675015056 = []
                __append_4675015056 = __stream_4675015056.append
                __append_4675015056('Version Overview')
                __msgid_4675015056 = __re_whitespace(''.join(__stream_4675015056)).strip()
                if 'heading_version_overview':
                    __append(translate('heading_version_overview', mapping=None, default=__msgid_4675015056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n    ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675990864
                __attrs_4675990864 = _static_4659865408

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675991696
                __attrs_4675991696 = _static_4659865408
                __backup_version_4878700592 = get('version', __marker)

                # <Value 'view/version_overview' (145:41)> -> __iterator
                __token = 5702
                try:
                    __zt_tmp = __attrs_4675991696
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'view/version_overview', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4675986320, ) = getname('repeat')('version', __iterator)
                econtext['version'] = None
                for __item in __iterator:
                    econtext['version'] = __item
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675987728
                    __attrs_4675987728 = _static_4659865408

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4675978192
                    __default_4675978192 = _DEFAULT_MARKER

                    # <Value 'version' (146:25)> -> __cache_4675993488
                    __token = 5751
                    try:
                        __zt_tmp = __attrs_4675987728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4675993488 = _static_4662095120('path', 'version', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'version' (146:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 116b5fb10> -> __condition
                    __expression = __cache_4675993488

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Version')
                    else:
                        __content = __cache_4675993488
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</li>\n      ')
                    ____index_4675986320 -= 1
                    if (____index_4675986320 > 0):
                        __append('')
                if (__backup_version_4878700592 is __marker):
                    del econtext['version']
                else:
                    econtext['version'] = __backup_version_4878700592
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686455632
                __attrs_4686455632 = _static_4659865408
                __backup_server_info_4878705296 = get('server_info', __marker)

                # <Value 'view/server_info' (148:42)> -> __value
                __token = 5842
                try:
                    __zt_tmp = __attrs_4686455632
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'view/server_info', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['server_info'] = __value
                __backup_has_wsgi_4878586480 = get('has_wsgi', __marker)

                # <Value 'server_info/wsgi' (149:38)> -> __value
                __token = 5898
                try:
                    __zt_tmp = __attrs_4686455632
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_4662095120('path', 'server_info/wsgi', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                econtext['has_wsgi'] = __value
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686462928
                __attrs_4686462928 = _static_4659865408

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686457168
                __attrs_4686457168 = _static_4659865408
                __stream_4686454160 = []
                __append_4686454160 = __stream_4686454160.append
                __append_4686454160('WSGI:')
                __msgid_4686454160 = __re_whitespace(''.join(__stream_4686454160)).strip()
                if __msgid_4686454160:
                    __append(translate(__msgid_4686454160, mapping=None, default=__msgid_4686454160, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686461264
                __attrs_4686461264 = _static_4659865408

                # <Value 'has_wsgi' (152:51)> -> __condition
                __token = 6042
                try:
                    __zt_tmp = __attrs_4686461264
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'has_wsgi', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4686456336 = []
                    __append_4686456336 = __stream_4686456336.append
                    __append_4686456336('On')
                    __msgid_4686456336 = __re_whitespace(''.join(__stream_4686456336)).strip()
                    if __msgid_4686456336:
                        __append(translate(__msgid_4686456336, mapping=None, default=__msgid_4686456336, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683536016
                __attrs_4683536016 = _static_4659865408

                # <Value 'not:has_wsgi' (153:51)> -> __condition
                __token = 6113
                try:
                    __zt_tmp = __attrs_4683536016
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('not', 'has_wsgi', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_4686456784 = []
                    __append_4686456784 = __stream_4686456784.append
                    __append_4686456784('Off')
                    __msgid_4686456784 = __re_whitespace(''.join(__stream_4686456784)).strip()
                    if __msgid_4686456784:
                        __append(translate(__msgid_4686456784, mapping=None, default=__msgid_4686456784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n          </li>\n          ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683539664
                __attrs_4683539664 = _static_4659865408

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683543888
                __attrs_4683543888 = _static_4659865408
                __stream_4683546448 = []
                __append_4683546448 = __stream_4683546448.append
                __append_4683546448('Server:')
                __msgid_4683546448 = __re_whitespace(''.join(__stream_4683546448)).strip()
                if __msgid_4683546448:
                    __append(translate(__msgid_4683546448, mapping=None, default=__msgid_4683546448, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683537488
                __attrs_4683537488 = _static_4659865408

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/server_name}' (157:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117292f10> -> __content_4386234736
                __token = 6246
                __token = 6248
                try:
                    __zt_tmp = __attrs_4683537488
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4386234736 = _static_4662095120('path', 'server_info/server_name', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __content_4386234736 = __quote(__content_4386234736, '\x00', '&#0;', None, None)
                __content_4386234736 = __content_4386234736
                if (__content_4386234736 is None):
                    pass
                else:
                    if (__content_4386234736 is None):
                        __content_4386234736 = None
                    else:
                        __tt = type(__content_4386234736)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_4386234736 = str(__content_4386234736)
                        else:
                            if (__tt is bytes):
                                __content_4386234736 = decode(__content_4386234736)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_4386234736 = __content_4386234736.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_4386234736)
                                        __content_4386234736 = (str(__content_4386234736) if (__content_4386234736 is __converted) else __converted)
                                    else:
                                        __content_4386234736 = __content_4386234736()
                if (__content_4386234736 is not None):
                    __append(__content_4386234736)
                __append('</span>\n            ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683537808
                __attrs_4683537808 = _static_4659865408

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/version}' (158:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 117292b90> -> __content_4386234736
                __token = 6298
                __token = 6300
                try:
                    __zt_tmp = __attrs_4683537808
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_4386234736 = _static_4662095120('path', 'server_info/version', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __content_4386234736 = __quote(__content_4386234736, '\x00', '&#0;', None, None)
                __content_4386234736 = __content_4386234736
                if (__content_4386234736 is None):
                    pass
                else:
                    if (__content_4386234736 is None):
                        __content_4386234736 = None
                    else:
                        __tt = type(__content_4386234736)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_4386234736 = str(__content_4386234736)
                        else:
                            if (__tt is bytes):
                                __content_4386234736 = decode(__content_4386234736)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_4386234736 = __content_4386234736.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_4386234736)
                                        __content_4386234736 = (str(__content_4386234736) if (__content_4386234736 is __converted) else __converted)
                                    else:
                                        __content_4386234736 = __content_4386234736()
                if (__content_4386234736 is not None):
                    __append(__content_4386234736)
                __append('</span>\n          </li>\n      ')
                if (__backup_has_wsgi_4878586480 is __marker):
                    del econtext['has_wsgi']
                else:
                    econtext['has_wsgi'] = __backup_has_wsgi_4878586480
                if (__backup_server_info_4878705296 is __marker):
                    del econtext['server_info']
                else:
                    econtext['server_info'] = __backup_server_info_4878705296
                __append('\n    </ul>\n\n    ')

                # <Static value=<ast.Dict object at 0x122c941f0> name=None at 116b5d390> -> __attrs_4680978320
                __attrs_4680978320 = _static_4878582256

                # <Value 'not:view/is_dev_mode' (163:22)> -> __condition
                __token = 6397
                try:
                    __zt_tmp = __attrs_4680978320
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('not', 'view/is_dev_mode', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_4675987152 = []
                    __append_4675987152 = __stream_4675987152.append
                    __append_4675987152('\n      You are running in "production mode". This is the preferred mode of\n      operation for a live Plone site, but means that some\n      configuration changes will not take effect until your server is\n      restarted or a product refreshed. If this is a development instance,\n      and you want to enable debug mode, stop the server, set \'debug-mode=on\'\n      in your buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_4675987152 = __re_whitespace(''.join(__stream_4675987152)).strip()
                    if 'description_production_mode':
                        __append(translate('description_production_mode', mapping=None, default=__msgid_4675987152, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x122c97fd0> name=None at 117021f50> -> __attrs_4680985040
                __attrs_4680985040 = _static_4878598096

                # <Value 'view/is_dev_mode' (175:22)> -> __condition
                __token = 6969
                try:
                    __zt_tmp = __attrs_4680985040
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'view/is_dev_mode', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_4680983568 = []
                    __append_4680983568 = __stream_4680983568.append
                    __append_4680983568('\n      You are running in "debug mode". This mode is intended for sites that\n      are under development. This allows many configuration changes to be\n      immediately visible, but will make your site run more slowly. To turn\n      off debug mode, stop the server, set \'debug-mode=off\' in your\n      buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_4680983568 = __re_whitespace(''.join(__stream_4680983568)).strip()
                    if 'description_debug_mode':
                        __append(translate('description_debug_mode', mapping=None, default=__msgid_4680983568, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n  </section>\n\n</div>')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_4691705296
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_4662095120('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_4686775040 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_4686775040
            __i18n_domain = __previous_i18n_domain_4691704080
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }