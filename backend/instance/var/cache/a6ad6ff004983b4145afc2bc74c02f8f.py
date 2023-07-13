# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/Products/CMFPlone/browser/templates/main_template.pt'

__tokens = {71: ('string:&lt;!DOCTYPE ht', 2, 36), 344: ("python:context.restrictedTraverse('@@plone_portal_state')", 8, 31), 426: (" python:context.restrictedTraverse('@@plone_context_state'", 9, 23), 506: ("w python:context.restrictedTraverse('@@plone", 10, 19), 567: ("ns python:context.restrictedTraverse('@@iconresolve", 11, 13), 642: ("out python:context.restrictedTraverse('@@plone_layo", 12, 19), 709: ('lang python:portal_state.langu', 13, 10), 755: (' view nocall:view | nocall: plon', 14, 9), 804: (' dummy python: plone_layout.mark_vie', 15, 9), 862: ('tal_url python:portal_state.port', 16, 13), 921: ("rmission python:context.restrictedTraverse('portal_membership').checkP", 17, 17), 1018: ("roperties python:context.restrictedTraverse('portal_properties').site_", 18, 16), 1117: ("clude_head python:request.get('ajax_include_he", 19, 17), 1184: ('  ajax_load ', 20, 8), 1264: ('lang', 22, 27), 1313: ('provider:plone.httpheaders', 24, 40), 1416: ('provider:plone.htmlhead', 29, 32), 1471: ('nothing', 31, 26), 1757: ('provider:plone.scripts', 38, 32), 1882: ('provider:plone.htmlhead.links', 41, 33), 2021: ('portal_state/is_rtl', 46, 26), 2064: (" python:plone_layout.have_portlets('plone.leftcolumn', view", 47, 22), 2147: ("r python:plone_layout.have_portlets('plone.rightcolumn', vie", 48, 21), 2239: ('ss python:plone_layout.bodyClass(template, vi', 49, 28), 2415: ("  python:context.restrictedTraverse('@@plone_patterns_settings')", 52, 22), 2320: ('body_class', 50, 30), 2359: (" python:isRTL and 'rtl' or 'ltr", 51, 27), 2553: ('provider:plone.toolbar', 55, 32), 2664: ('provider:plone.portaltop', 58, 34), 2760: ('provider:plone.portalheader', 60, 36), 2880: ('provider:plone.mainnavigation', 65, 59), 3032: ('provider:plone.globalstatusmessage', 70, 42), 3211: ('provider:plone.abovecontent', 75, 59), 5052: ('sl', 130, 26), 5150: ('provider:plone.leftcolumn', 132, 38), 5325: ('sr', 138, 26), 5423: ('provider:plone.rightcolumn', 140, 38), 5586: ('provider:plone.portalfooter', 145, 34), 3606: ('provider:plone.abovecontenttitle', 91, 77), 3747: ('context/@@title', 94, 45), 3876: ('provider:plone.belowcontenttitle', 97, 77), 4028: ('context/@@description', 100, 44), 4175: ('provider:plone.belowcontentdescription', 103, 83), 4318: ('provider:plone.abovecontentbody', 107, 74), 4461: ('nothing', 110, 68), 4630: ('provider:plone.belowcontentbody', 115, 74), 4787: ('provider:plone.belowcontent', 119, 69)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4873379440 = {'id': 'viewlet-below-content', }
_static_4873083808 = {'id': 'viewlet-below-content-body', }
_static_4873513680 = {'id': 'content-core', }
_static_4873518048 = {'id': 'viewlet-above-content-body', }
_static_4873517232 = {'id': 'viewlet-below-content-description', }
_static_4873504320 = {'id': 'viewlet-below-content-title', }
_static_4873516368 = {'id': 'viewlet-above-content-title', }
_static_4873514448 = {'id': 'content', }
_static_4873515024 = {'id': 'portal-footer-wrapper', }
_static_4873509264 = {'id': 'portal-column-two', }
_static_4873513200 = {'id': 'portal-column-one', }
_static_4873510944 = {'id': 'portal-column-content', }
_static_4873509840 = {'id': 'viewlet-above-content', }
_static_4873511088 = {'id': 'global_statusmessage', }
_static_4873512000 = {'id': 'portal-mainnavigation', }
_static_4873511856 = {'id': 'portal-header', }
_static_4873503456 = {'id': 'portal-top', }
_static_4878534784 = set([])
_static_4873504752 = {'id': 'visual-portal-wrapper', 'class': 'body_class', 'dir': "python:isRTL and 'rtl' or 'ltr'", }
_static_4873503024 = {'name': 'generator', 'content': 'Plone - https://plone.org/', }
_static_4873507776 = {'charset': 'utf-8', }
_static_4873511232 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'lang', }
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

    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_javascript_head_slot = econtext['__slot_javascript_head_slot'].pop()
        except:
            __slot_javascript_head_slot = None

        try:
            __slot_column_two_slot = econtext['__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_portlets_one_slot = econtext['__slot_portlets_one_slot'].pop()
        except:
            __slot_portlets_one_slot = None

        try:
            __slot_content = econtext['__slot_content'].pop()
        except:
            __slot_content = None

        try:
            __slot_global_statusmessage = econtext['__slot_global_statusmessage'].pop()
        except:
            __slot_global_statusmessage = None

        try:
            __slot_column_one_slot = econtext['__slot_column_one_slot'].pop()
        except:
            __slot_column_one_slot = None

        try:
            __slot_portlets_two_slot = econtext['__slot_portlets_two_slot'].pop()
        except:
            __slot_portlets_two_slot = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_head_slot = econtext['__slot_head_slot'].pop()
        except:
            __slot_head_slot = None

        try:
            __slot_style_slot = econtext['__slot_style_slot'].pop()
        except:
            __slot_style_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686383440
            __attrs_4686383440 = _static_4659865408
            __append('\n')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686392720
            __attrs_4686392720 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686396176
            __default_4686396176 = _DEFAULT_MARKER

            # <Value 'string:<!DOCTYPE html>' (2:36)> -> __cache_4662523664
            __token = 71
            try:
                __zt_tmp = __attrs_4686392720
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4662523664 = _static_4662095120('string', '<!DOCTYPE html>', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'string:<!DOCTYPE html>' (2:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11754a7d0> -> __condition
            __expression = __cache_4662523664

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4662523664
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x1227be140> name=None at 11754bb90> -> __attrs_4686460176
            __attrs_4686460176 = _static_4873511232
            __backup_portal_state_4866717344 = get('portal_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_portal_state')" (8:31)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_4867717248 = get('context_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_context_state')" (9:23)> -> __value
            __token = 426
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_4866716576 = get('plone_view', __marker)

            # <Value "python:context.restrictedTraverse('@@plone')" (10:19)> -> __value
            __token = 506
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('@@plone')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_icons_4868540160 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (11:13)> -> __value
            __token = 567
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_plone_layout_4868550672 = get('plone_layout', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_layout')" (12:19)> -> __value
            __token = 642
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_4868545584 = get('lang', __marker)

            # <Value 'python:portal_state.language()' (13:10)> -> __value
            __token = 709
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'portal_state.language()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_4868545968 = get('view', __marker)

            # <Value 'nocall:view | nocall: plone_view' (14:9)> -> __value
            __token = 755
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('nocall', 'view | nocall: plone_view', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_4868539008 = get('dummy', __marker)

            # <Value 'python: plone_layout.mark_view(view)' (15:9)> -> __value
            __token = 804
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', ' plone_layout.mark_view(view)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_4868550432 = get('portal_url', __marker)

            # <Value 'python:portal_state.portal_url()' (16:13)> -> __value
            __token = 862
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'portal_state.portal_url()', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_4868551056 = get('checkPermission', __marker)

            # <Value "python:context.restrictedTraverse('portal_membership').checkPermission" (17:17)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_4868550384 = get('site_properties', __marker)

            # <Value "python:context.restrictedTraverse('portal_properties').site_properties" (18:16)> -> __value
            __token = 1018
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_4868545536 = get('ajax_include_head', __marker)

            # <Value "python:request.get('ajax_include_head', False)" (19:17)> -> __value
            __token = 1117
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "request.get('ajax_include_head', False)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_4868538768 = get('ajax_load', __marker)

            # <Value 'python:False' (20:8)> -> __value
            __token = 1184
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'False', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_4686461264 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686387024
            __default_4686387024 = _DEFAULT_MARKER

            # <Substitution 'lang' (22:27)> -> __attr_lang
            __token = 1264
            try:
                __zt_tmp = __attrs_4686460176
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_4662095120('path', 'lang', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686461136
            __attrs_4686461136 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686452752
            __default_4686452752 = _DEFAULT_MARKER

            # <Value 'provider:plone.httpheaders' (24:40)> -> __cache_4686450768
            __token = 1313
            try:
                __zt_tmp = __attrs_4686461136
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4686450768 = _static_4662095120('provider', 'plone.httpheaders', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.httpheaders' (24:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117558810> -> __condition
            __expression = __cache_4686450768

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4686450768
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686453840
            __attrs_4686453840 = _static_4659865408

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x1227bd3c0> name=None at 1173a05d0> -> __attrs_4684638736
            __attrs_4684638736 = _static_4873507776

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n\n    ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684633872
            __attrs_4684633872 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684634192
            __default_4684634192 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead' (29:32)> -> __cache_4684631760
            __token = 1416
            try:
                __zt_tmp = __attrs_4684633872
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4684631760 = _static_4662095120('provider', 'plone.htmlhead', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead' (29:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11739d4d0> -> __condition
            __expression = __cache_4684631760

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4684631760
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684638480
            __attrs_4684638480 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684643280
            __default_4684643280 = _DEFAULT_MARKER

            # <Value 'nothing' (31:26)> -> __cache_4684628688
            __token = 1471
            try:
                __zt_tmp = __attrs_4684638480
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4684628688 = _static_4662095120('path', 'nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'nothing' (31:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11739c110> -> __condition
            __expression = __cache_4684628688

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_4684628688
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_top_slot is None):

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684634960
                __attrs_4684634960 = _static_4659865408
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_head_slot is None):

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684640144
                __attrs_4684640144 = _static_4659865408
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_style_slot is None):

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684644304
                __attrs_4684644304 = _static_4659865408
            else:
                __slot_style_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684631056
            __attrs_4684631056 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684636752
            __default_4684636752 = _DEFAULT_MARKER

            # <Value 'provider:plone.scripts' (38:32)> -> __cache_4684637136
            __token = 1757
            try:
                __zt_tmp = __attrs_4684631056
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4684637136 = _static_4662095120('provider', 'plone.scripts', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.scripts' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11739dad0> -> __condition
            __expression = __cache_4684637136

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4684637136
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_javascript_head_slot is None):

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684318480
                __attrs_4684318480 = _static_4659865408
            else:
                __slot_javascript_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684317776
            __attrs_4684317776 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4684319504
            __default_4684319504 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead.links' (41:33)> -> __cache_4684318544
            __token = 1882
            try:
                __zt_tmp = __attrs_4684317776
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4684318544 = _static_4662095120('provider', 'plone.htmlhead.links', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead.links' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117353350> -> __condition
            __expression = __cache_4684318544

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link />')
            else:
                __content = __cache_4684318544
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x1227bc130> name=None at 117350dd0> -> __attrs_4653859216
            __attrs_4653859216 = _static_4873503024

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="generator" content="Plone - https://plone.org/" />\n\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x1227bc7f0> name=None at 1175f2f90> -> __attrs_4687007056
            __attrs_4687007056 = _static_4873504752
            __backup_isRTL_4693057280 = get('isRTL', __marker)

            # <Value 'portal_state/is_rtl' (46:26)> -> __value
            __token = 2021
            try:
                __zt_tmp = __attrs_4687007056
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'portal_state/is_rtl', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_4868550624 = get('sl', __marker)

            # <Value "python:plone_layout.have_portlets('plone.leftcolumn', view)" (47:22)> -> __value
            __token = 2064
            try:
                __zt_tmp = __attrs_4687007056
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_4868045552 = get('sr', __marker)

            # <Value "python:plone_layout.have_portlets('plone.rightcolumn', view)" (48:21)> -> __value
            __token = 2147
            try:
                __zt_tmp = __attrs_4687007056
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', "plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_4865178352 = get('body_class', __marker)

            # <Value 'python:plone_layout.bodyClass(template, view)' (49:28)> -> __value
            __token = 2239
            try:
                __zt_tmp = __attrs_4687007056
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')

            # <Value "python:context.restrictedTraverse('@@plone_patterns_settings')()" (52:22)> -> __cache_4687084304
            __token = 2415
            try:
                __zt_tmp = __attrs_4687007056
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4687084304 = _static_4662095120('python', "context.restrictedTraverse('@@plone_patterns_settings')()", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if ('id' not in __chain(__cache_4687084304)):
                __append(' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4687083792
            __default_4687083792 = _DEFAULT_MARKER

            # <Substitution 'body_class' (50:30)> -> __attr_class
            __token = 2320
            try:
                __zt_tmp = __attrs_4687007056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4662095120('path', 'body_class', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and ('class' not in __chain(__cache_4687084304))):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4687071120
            __default_4687071120 = _DEFAULT_MARKER

            # <Substitution "python:isRTL and 'rtl' or 'ltr'" (51:27)> -> __attr_dir
            __token = 2359
            try:
                __zt_tmp = __attrs_4687007056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_4662095120('python', "isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and ('dir' not in __chain(__cache_4687084304))):
                __append((' dir="%s"' % __attr_dir))
            __attr_4687083216 = __cache_4687084304
            for (name, value, ) in __attr_4687083216.items():
                if ((name not in _static_4878534784) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683178384
            __attrs_4683178384 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4683179088
            __default_4683179088 = _DEFAULT_MARKER

            # <Value 'provider:plone.toolbar' (55:32)> -> __cache_4683185616
            __token = 2553
            try:
                __zt_tmp = __attrs_4683178384
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4683185616 = _static_4662095120('provider', 'plone.toolbar', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.toolbar' (55:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117238210> -> __condition
            __expression = __cache_4683185616

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4683185616
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1227bc2e0> name=None at 11723b410> -> __attrs_4686225680
            __attrs_4686225680 = _static_4873503456
            __previous_i18n_domain_4686227344 = __i18n_domain
            __i18n_domain = 'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header id="portal-top">\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686524816
            __attrs_4686524816 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686219152
            __default_4686219152 = _DEFAULT_MARKER

            # <Value 'provider:plone.portaltop' (58:34)> -> __cache_4686219088
            __token = 2664
            try:
                __zt_tmp = __attrs_4686524816
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4686219088 = _static_4662095120('provider', 'plone.portaltop', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portaltop' (58:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117520e90> -> __condition
            __expression = __cache_4686219088

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4686219088
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x1227be3b0> name=None at 11756b010> -> __attrs_4686703248
            __attrs_4686703248 = _static_4873511856

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-header">\n        ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683857872
            __attrs_4683857872 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4683854352
            __default_4683854352 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalheader' (60:36)> -> __cache_4683855056
            __token = 2760
            try:
                __zt_tmp = __attrs_4683857872
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4683855056 = _static_4662095120('provider', 'plone.portalheader', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalheader' (60:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1172decd0> -> __condition
            __expression = __cache_4683855056

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4683855056
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      </div>\n\n    </header>')
            __i18n_domain = __previous_i18n_domain_4686227344
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1227be440> name=None at 1172df990> -> __attrs_4686781072
            __attrs_4686781072 = _static_4873512000

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4683853200
            __default_4683853200 = _DEFAULT_MARKER

            # <Value 'provider:plone.mainnavigation' (65:59)> -> __cache_4683847568
            __token = 2880
            try:
                __zt_tmp = __attrs_4686781072
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4683847568 = _static_4662095120('provider', 'plone.mainnavigation', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.mainnavigation' (65:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1172dc550> -> __condition
            __expression = __cache_4683847568

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n      The main navigation\n    ')
            else:
                __content = __cache_4683847568
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x1227be0b0> name=None at 1175a9b50> -> __attrs_4686776080
            __attrs_4686776080 = _static_4873511088

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="global_statusmessage">\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686854608
            __attrs_4686854608 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686844688
            __default_4686844688 = _DEFAULT_MARKER

            # <Value 'provider:plone.globalstatusmessage' (70:42)> -> __cache_4686851408
            __token = 3032
            try:
                __zt_tmp = __attrs_4686854608
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4686851408 = _static_4662095120('provider', 'plone.globalstatusmessage', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.globalstatusmessage' (70:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1175b8810> -> __condition
            __expression = __cache_4686851408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4686851408
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')
            if (__slot_global_statusmessage is None):

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686843536
                __attrs_4686843536 = _static_4659865408

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append('\n    </section>\n\n    ')

            # <Static value=<ast.Dict object at 0x1227bdbd0> name=None at 11708cf90> -> __attrs_4681429264
            __attrs_4681429264 = _static_4873509840

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686855312
            __default_4686855312 = _DEFAULT_MARKER

            # <Value 'provider:plone.abovecontent' (75:59)> -> __cache_4686855568
            __token = 3211
            try:
                __zt_tmp = __attrs_4681429264
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4686855568 = _static_4662095120('provider', 'plone.abovecontent', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.abovecontent' (75:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1175bb790> -> __condition
            __expression = __cache_4686855568

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_4686855568
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x1227be020> name=None at 11708f550> -> __attrs_4681428752
            __attrs_4681428752 = _static_4873510944

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="portal-column-content">\n\n      ')
            if (__slot_content is None):

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689318096
                __attrs_4689318096 = _static_4659865408
                __append('\n\n      ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n      ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append('\n    </article>\n\n    ')
            if (__slot_column_one_slot is None):

                # <Static value=<ast.Dict object at 0x1227be8f0> name=None at 117817290> -> __attrs_4689324560
                __attrs_4689324560 = _static_4873513200

                # <Value 'sl' (130:26)> -> __condition
                __token = 5052
                try:
                    __zt_tmp = __attrs_4689324560
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'sl', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-one">\n      ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686315216
                        __attrs_4686315216 = _static_4659865408
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686306128
                        __attrs_4686306128 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686309584
                        __default_4686309584 = _DEFAULT_MARKER

                        # <Value 'provider:plone.leftcolumn' (132:38)> -> __cache_4686306256
                        __token = 5150
                        try:
                            __zt_tmp = __attrs_4686306128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4686306256 = _static_4662095120('provider', 'plone.leftcolumn', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.leftcolumn' (132:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117535f10> -> __condition
                        __expression = __cache_4686306256

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4686306256
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_one_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_one_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')
            if (__slot_column_two_slot is None):

                # <Static value=<ast.Dict object at 0x1227bd990> name=None at 1173f5410> -> __attrs_4686314384
                __attrs_4686314384 = _static_4873509264

                # <Value 'sr' (138:26)> -> __condition
                __token = 5325
                try:
                    __zt_tmp = __attrs_4686314384
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_4662095120('path', 'sr', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-two">\n      ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4688266384
                        __attrs_4688266384 = _static_4659865408
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689064144
                        __attrs_4689064144 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4689062608
                        __default_4689062608 = _DEFAULT_MARKER

                        # <Value 'provider:plone.rightcolumn' (140:38)> -> __cache_4689056016
                        __token = 5423
                        try:
                            __zt_tmp = __attrs_4689064144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4689056016 = _static_4662095120('provider', 'plone.rightcolumn', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.rightcolumn' (140:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1177d4250> -> __condition
                        __expression = __cache_4689056016

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_4689056016
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_two_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_two_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x1227bf010> name=None at 117714e50> -> __attrs_4689066960
            __attrs_4689066960 = _static_4873515024
            __previous_i18n_domain_4689065424 = __i18n_domain
            __i18n_domain = 'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer id="portal-footer-wrapper">\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4690417872
            __attrs_4690417872 = _static_4659865408

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4690413008
            __default_4690413008 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalfooter' (145:34)> -> __cache_4690419280
            __token = 5586
            try:
                __zt_tmp = __attrs_4690417872
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_4690419280 = _static_4662095120('provider', 'plone.portalfooter', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalfooter' (145:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117920290> -> __condition
            __expression = __cache_4690419280

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_4690419280
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    </footer>')
            __i18n_domain = __previous_i18n_domain_4689065424
            __append('\n\n  </body>')
            if (__backup_body_class_4865178352 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_4865178352
            if (__backup_sr_4868045552 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_4868045552
            if (__backup_sl_4868550624 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_4868550624
            if (__backup_isRTL_4693057280 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_4693057280
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_4686461264
            if (__backup_ajax_load_4868538768 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_4868538768
            if (__backup_ajax_include_head_4868545536 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_4868545536
            if (__backup_site_properties_4868550384 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_4868550384
            if (__backup_checkPermission_4868551056 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_4868551056
            if (__backup_portal_url_4868550432 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_4868550432
            if (__backup_dummy_4868539008 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_4868539008
            if (__backup_view_4868545968 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_4868545968
            if (__backup_lang_4868545584 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_4868545584
            if (__backup_plone_layout_4868550672 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_4868550672
            if (__backup_icons_4868540160 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_4868540160
            if (__backup_plone_view_4866716576 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_4866716576
            if (__backup_context_state_4867717248 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_4867717248
            if (__backup_portal_state_4866717344 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_4866717344
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_content(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_main = econtext['__slot_main'].pop()
        except:
            __slot_main = None

        try:
            __slot_content_description = econtext['__slot_content_description'].pop()
        except:
            __slot_content_description = None

        try:
            __slot_body = econtext['__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_content_core = econtext['__slot_content_core'].pop()
        except:
            __slot_content_core = None

        try:
            __slot_content_title = econtext['__slot_content_title'].pop()
        except:
            __slot_content_title = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4689329104
            __attrs_4689329104 = _static_4659865408
            __append('\n\n        ')
            if (__slot_body is None):

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4684106128
                __attrs_4684106128 = _static_4659865408
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x1227bedd0> name=None at 11731d010> -> __attrs_4674284112
                __attrs_4674284112 = _static_4873514448

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n            ')
                if (__slot_main is None):

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674282064
                    __attrs_4674282064 = _static_4659865408
                    __append('\n\n              ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4683539728
                    __attrs_4683539728 = _static_4659865408

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header>\n\n                ')

                    # <Static value=<ast.Dict object at 0x1227bf550> name=None at 117293b90> -> __attrs_4683541712
                    __attrs_4683541712 = _static_4873516368

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4683540112
                    __default_4683540112 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontenttitle' (91:77)> -> __cache_4683534544
                    __token = 3606
                    try:
                        __zt_tmp = __attrs_4683541712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4683534544 = _static_4662095120('provider', 'plone.abovecontenttitle', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontenttitle' (91:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117292f90> -> __condition
                    __expression = __cache_4683534544

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4683534544
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_title is None):

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686963024
                        __attrs_4686963024 = _static_4659865408
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686954640
                        __attrs_4686954640 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686969232
                        __default_4686969232 = _DEFAULT_MARKER

                        # <Value 'context/@@title' (94:45)> -> __cache_4686959888
                        __token = 3747
                        try:
                            __zt_tmp = __attrs_4686954640
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4686959888 = _static_4662095120('path', 'context/@@title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@title' (94:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1175d5550> -> __condition
                        __expression = __cache_4686959888

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append('<h1 />')
                        else:
                            __content = __cache_4686959888
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x1227bc640> name=None at 1175d7a50> -> __attrs_4686341648
                    __attrs_4686341648 = _static_4873504320

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686957840
                    __default_4686957840 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontenttitle' (97:77)> -> __cache_4683541392
                    __token = 3876
                    try:
                        __zt_tmp = __attrs_4686341648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4683541392 = _static_4662095120('provider', 'plone.belowcontenttitle', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontenttitle' (97:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1173f7550> -> __condition
                    __expression = __cache_4683541392

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4683541392
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_description is None):

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686347856
                        __attrs_4686347856 = _static_4659865408
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686347664
                        __attrs_4686347664 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686337808
                        __default_4686337808 = _DEFAULT_MARKER

                        # <Value 'context/@@description' (100:44)> -> __cache_4686346576
                        __token = 4028
                        try:
                            __zt_tmp = __attrs_4686347664
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4686346576 = _static_4662095120('path', 'context/@@description', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@description' (100:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11753f350> -> __condition
                        __expression = __cache_4686346576

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append('<p />')
                        else:
                            __content = __cache_4686346576
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x1227bf8b0> name=None at 1170a4c50> -> __attrs_4681521808
                    __attrs_4681521808 = _static_4873517232

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-description">')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681517776
                    __default_4681517776 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentdescription' (103:83)> -> __cache_4686345744
                    __token = 4175
                    try:
                        __zt_tmp = __attrs_4681521808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4686345744 = _static_4662095120('provider', 'plone.belowcontentdescription', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentdescription' (103:83)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 11753de10> -> __condition
                    __expression = __cache_4686345744

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4686345744
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              </header>\n\n              ')

                    # <Static value=<ast.Dict object at 0x1227bfbe0> name=None at 1170a6890> -> __attrs_4681522000
                    __attrs_4681522000 = _static_4873518048

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4681517328
                    __default_4681517328 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontentbody' (107:74)> -> __cache_4681530384
                    __token = 4318
                    try:
                        __zt_tmp = __attrs_4681522000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4681530384 = _static_4662095120('provider', 'plone.abovecontentbody', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontentbody' (107:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1170a4610> -> __condition
                    __expression = __cache_4681530384

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4681530384
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x1227bead0> name=None at 1170a55d0> -> __attrs_4686749520
                    __attrs_4686749520 = _static_4873513680

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')
                    if (__slot_content_core is None):

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4686750672
                        __attrs_4686750672 = _static_4659865408

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686743888
                        __default_4686743888 = _DEFAULT_MARKER

                        # <Value 'nothing' (110:68)> -> __cache_4686744848
                        __token = 4461
                        try:
                            __zt_tmp = __attrs_4686750672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_4686744848 = _static_4662095120('path', 'nothing', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                        # <BinOp left=<Value 'nothing' (110:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1175a0e90> -> __condition
                        __expression = __cache_4686744848

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  Page body text\n                ')
                        else:
                            __content = __cache_4686744848
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append('\n              </div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x122755ba0> name=None at 1175a0750> -> __attrs_4686309520
                    __attrs_4686309520 = _static_4873083808

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686755472
                    __default_4686755472 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentbody' (115:74)> -> __cache_4686750928
                    __token = 4630
                    try:
                        __zt_tmp = __attrs_4686309520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_4686750928 = _static_4662095120('provider', 'plone.belowcontentbody', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentbody' (115:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 1175a1690> -> __condition
                    __expression = __cache_4686750928

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_4686750928
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n            ')
                else:
                    __slot_main(__stream, econtext.copy(), rcontext)
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4681521424
                __attrs_4681521424 = _static_4659865408

                # <footer ... (0:0)
                # --------------------------------------------------------
                __append('<footer>\n              ')

                # <Static value=<ast.Dict object at 0x12279de70> name=None at 117537590> -> __attrs_4686314768
                __attrs_4686314768 = _static_4873379440

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="viewlet-below-content">')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4686302928
                __default_4686302928 = _DEFAULT_MARKER

                # <Value 'provider:plone.belowcontent' (119:69)> -> __cache_4686311248
                __token = 4787
                try:
                    __zt_tmp = __attrs_4686314768
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_4686311248 = _static_4662095120('provider', 'plone.belowcontent', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.belowcontent' (119:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 115b98fd0> at 117535610> -> __condition
                __expression = __cache_4686311248

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_4686311248
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n            </footer>\n          </article>\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append('\n      ')
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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_master': render_master, 'render_content': render_content, 'render': render, }