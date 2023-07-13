# -*- coding: utf-8 -*-
__filename = '/Users/cihanandac/Documents/utrechtsciencepark/utrechtsciencepark/backend/lib/python3.11/site-packages/Products/CMFPlone/browser/templates/plone-overview.pt'

__tokens = {581: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 16, 14), 583: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 16, 16), 727: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 19, 14), 729: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 19, 16), 830: ('view/sites', 23, 24), 864: (' python:len(sites) > ', 24, 22), 1087: ('string:${context/absolute_url}/++resource++plone-logo.svg', 29, 36), 1755: ('sites', 44, 28), 1802: ('sites', 45, 39), 1852: ('python: view.outdated(site)', 46, 42), 1910: ("mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", 47, 28), 1917: ("python: 'p-3 alert alert-warning' if outdated else ''", 47, 35), 2012: ('outdated', 48, 38), 2285: ('site/absolute_url', 50, 45), 2166: ("btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 49, 60), 2184: ("python:'btn-lg' if not many and not outdated  else ''", 49, 78), 2450: ('not: many', 53, 44), 2555: ('many', 54, 45), 2561: ('${python:site.title}', 54, 51), 2563: ('python:site.title', 54, 53), 2589: ('(${python:"/".join(site.getPhysicalPath())})', 54, 79), 2592: ('python:"/".join(site.getPhysicalPath())', 54, 82), 2851: ('outdated', 59, 43), 2912: ('python:view.upgrade_url(site)', 60, 51), 2990: ('not:view/can_manage', 61, 46), 3128: ('python:view.upgrade_url(site, can_manage=True)', 63, 54), 3620: ('sites', 74, 30), 3770: ('not:sites', 78, 30), 4017: ("python: '' if not sites else len(sites) + 1", 84, 44), 4100: (' string:${context/absolute_url}/@@plone-addsit', 85, 38), 4177: ('${action}', 86, 28), 4179: ('action', 86, 30), 4248: ('Plone${site_number}', 87, 59), 4255: ('site_number', 87, 66), 4341: ("btn btn-${python:'success' if sites else 'primary'}", 89, 31), 4351: ("python:'success' if sites else 'primary'", 89, 41), 4582: ('view/has_volto', 93, 35), 4624: ('${action}?site_id=Plone${site_number}&amp;classic=1', 94, 26), 4626: ('action', 94, 28), 4649: ('site_number', 94, 51), 4837: ('${action}?site_id=Plone${site_number}&amp;advanced=1', 98, 26), 4839: ('action', 98, 28), 4862: ('site_number', 98, 51), 6194: ('string:${context/absolute_url}/manage_main', 126, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_4873518432 = {'href': '#', 'title': 'Go to the ZMI', }
_static_4873514064 = {'class': 'row', }
_static_4873517184 = {'href': 'https://6.docs.plone.org/', 'title': 'Plone 6 developer documentation', }
_static_4873516320 = {'class': 'btn btn-secondary', 'href': '${action}?site_id=Plone${site_number}&amp;advanced=1', }
_static_4873515840 = {'class': 'btn btn-info', 'href': '${action}?site_id=Plone${site_number}&amp;classic=1', }
_static_4873515312 = {'type': 'submit', 'class': "btn btn-${python:'success' if sites else 'primary'}", }
_static_4873514736 = {'type': 'hidden', 'name': 'site_id', 'value': 'Plone${site_number}', }
_static_4873513728 = {'id': 'add-plone-site', 'method': 'get', 'action': '${action}', }
_static_4873511328 = {'class': 'alert alert-warning p-1', }
_static_4873505040 = {'class': 'col-md-12', }
_static_4873510224 = {'type': 'submit', 'class': 'btn btn-warning me-3', }
_static_4873504896 = {'type': 'hidden', 'name': 'came_from', 'value': 'python:view.upgrade_url(site, can_manage=True)', }
_static_4873508928 = {'action': '', 'style': 'display: inline;', 'method': 'get', }
_static_4873507728 = {'href': '#', 'id': 'go-to-site-link', 'class': "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 'title': 'Go to your instance', }
_static_4873506576 = {'class': "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", }
_static_4873504128 = {'class': 'col-md-12 mb-4', }
_static_4873504848 = {'class': 'row mb-5', }
_static_4873511760 = {'href': 'http://plone.org', 'title': 'Plone Community Home', }
_static_4873507296 = {'class': 'lead', }
_static_4873508208 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_4873511616 = {'class': 'row', }
_static_4873502784 = {'class': 'container admin mt-5 mb-5 p-4', }
_static_4873387072 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_4662088080 = __C2ZContextWrapper
_static_4662095120 = __compile_zt_expr
_static_4873373728 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_4873380064 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_4873380496 = {'charset': 'utf-8', }
_static_4659865408 = {}
_static_4873083808 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')

            # <Static value=<ast.Dict object at 0x122755ba0> name=None at 11667ac10> -> __attrs_4655496016
            __attrs_4655496016 = _static_4873083808
            __previous_i18n_domain_4670119376 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671184464
            __attrs_4671184464 = _static_4659865408

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x12279e290> name=None at 1166cb650> -> __attrs_4669648528
            __attrs_4669648528 = _static_4873380496

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8"/>\n  ')

            # <Static value=<ast.Dict object at 0x12279e0e0> name=None at 116552010> -> __attrs_4671122640
            __attrs_4671122640 = _static_4873380064

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1"/>\n  ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671125840
            __attrs_4671125840 = _static_4659865408

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>Plone</title>\n  ')

            # <Static value=<ast.Dict object at 0x12279c820> name=None at 1166f6c10> -> __attrs_4671263056
            __attrs_4671263056 = _static_4873373728

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671365072
            __default_4671365072 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (16:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1166ef350> -> __attr_href
            __token = 581
            __token = 583
            try:
                __zt_tmp = __attrs_4671263056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4662095120('string', '${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x12279fc40> name=None at 1166dd090> -> __attrs_4674398608
            __attrs_4674398608 = _static_4873387072

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4662136528
            __default_4662136528 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (19:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 115e2b890> -> __attr_href
            __token = 727
            __token = 729
            try:
                __zt_tmp = __attrs_4674398608
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4662095120('string', '${context/absolute_url}/++resource++plone-admin-ui.css', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = __attr_href
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n</head>\n\n\n')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674390096
            __attrs_4674390096 = _static_4659865408
            __backup_sites_4866717248 = get('sites', __marker)

            # <Value 'view/sites' (23:24)> -> __value
            __token = 830
            try:
                __zt_tmp = __attrs_4674390096
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('path', 'view/sites', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['sites'] = __value
            __backup_many_4866717392 = get('many', __marker)

            # <Value 'python:len(sites) > 1' (24:22)> -> __value
            __token = 864
            try:
                __zt_tmp = __attrs_4674390096
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', 'len(sites) > 1', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['many'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n  ')

            # <Static value=<ast.Dict object at 0x1227bc040> name=None at 1169d8e90> -> __attrs_4674391952
            __attrs_4674391952 = _static_4873502784

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4">\n    ')

            # <Static value=<ast.Dict object at 0x1227be2c0> name=None at 1169dbad0> -> __attrs_4674401552
            __attrs_4674401552 = _static_4873511616

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n        ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4664517008
            __attrs_4664517008 = _static_4659865408

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x1227bd570> name=None at 115719550> -> __attrs_4671236560
            __attrs_4671236560 = _static_4873508208

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671230544
            __default_4671230544 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (29:36)> -> __attr_src
            __token = 1087
            try:
                __zt_tmp = __attrs_4671236560
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_4662095120('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670126032
            __default_4670126032 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x1227be3b0> at 1166d7510> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n        ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4671231376
            __attrs_4671231376 = _static_4659865408

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_4654741520 = []
            __append_4654741520 = __stream_4654741520.append
            __append_4654741520('Plone is up and running.')
            __msgid_4654741520 = __re_whitespace(''.join(__stream_4654741520)).strip()
            if __msgid_4654741520:
                __append(translate(__msgid_4654741520, mapping=None, default=__msgid_4654741520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n        ')

            # <Static value=<ast.Dict object at 0x1227bd1e0> name=None at 1166d7a50> -> __attrs_4674349264
            __attrs_4674349264 = _static_4873507296

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674350416
            __attrs_4674350416 = _static_4659865408

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_4674339408 = []
            __append_4674339408 = __stream_4674339408.append
            __append_4674339408(' For an introduction to Plone, documentation, demos, add-ons, support, and community, visit')
            __msgid_4674339408 = __re_whitespace(''.join(__stream_4674339408)).strip()
            if 'label_plone_org_description':
                __append(translate('label_plone_org_description', mapping=None, default=__msgid_4674339408, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n            ')

            # <Static value=<ast.Dict object at 0x1227be350> name=None at 1169cfdd0> -> __attrs_4674344720
            __attrs_4674344720 = _static_4873511760

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="http://plone.org"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674346320
            __default_4674346320 = _DEFAULT_MARKER

            # <Translate msgid='label_plone_org_title' node=<ast.Constant object at 0x1227bdff0> at 1169ccb10> -> __attr_title
            __attr_title = 'Plone Community Home'
            __attr_title = translate('label_plone_org_title', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>plone.org</a>.\n          </p>\n\n    </header>\n\n    ')

            # <Static value=<ast.Dict object at 0x1227bc850> name=None at 1169cc650> -> __attrs_4674340560
            __attrs_4674340560 = _static_4873504848

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row mb-5">\n        ')

            # <Static value=<ast.Dict object at 0x1227bc580> name=None at 116967210> -> __attrs_4670392656
            __attrs_4670392656 = _static_4873504128

            # <Value 'sites' (44:28)> -> __condition
            __token = 1755
            try:
                __zt_tmp = __attrs_4670392656
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'sites', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-4">\n            ')

                # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4670393360
                __attrs_4670393360 = _static_4659865408
                __backup_site_4866717968 = get('site', __marker)

                # <Value 'sites' (45:39)> -> __iterator
                __token = 1802
                try:
                    __zt_tmp = __attrs_4670393360
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_4662095120('path', 'sites', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                (__iterator, ____index_4670396880, ) = getname('repeat')('site', __iterator)
                econtext['site'] = None
                for __item in __iterator:
                    econtext['site'] = __item
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x1227bcf10> name=None at 116928790> -> __attrs_4673672464
                    __attrs_4673672464 = _static_4873506576
                    __backup_outdated_4866718016 = get('outdated', __marker)

                    # <Value 'python: view.outdated(site)' (46:42)> -> __value
                    __token = 1852
                    try:
                        __zt_tmp = __attrs_4673672464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_4662095120('python', ' view.outdated(site)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    econtext['outdated'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673672016
                    __default_4673672016 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}" (47:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116928d90> -> __attr_class
                    __token = 1910
                    __token = 1917
                    try:
                        __zt_tmp = __attrs_4673672464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4662095120('python', " 'p-3 alert alert-warning' if outdated else ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('mb-3 ', (__attr_class if (__attr_class is not None) else ''), ))
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                    ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674605456
                    __attrs_4674605456 = _static_4659865408

                    # <Value 'outdated' (48:38)> -> __condition
                    __token = 2012
                    try:
                        __zt_tmp = __attrs_4674605456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'outdated', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_4673671056 = []
                        __append_4673671056 = __stream_4673671056.append
                        __append_4673671056('This site configuration is outdated and needs to be upgraded:')
                        __msgid_4673671056 = __re_whitespace(''.join(__stream_4673671056)).strip()
                        if __msgid_4673671056:
                            __append(translate(__msgid_4673671056, mapping=None, default=__msgid_4673671056, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>')
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x1227bd390> name=None at 116a0da10> -> __attrs_4674609232
                    __attrs_4674609232 = _static_4873507728

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674609296
                    __default_4674609296 = _DEFAULT_MARKER

                    # <Substitution 'site/absolute_url' (50:45)> -> __attr_href
                    __token = 2285
                    try:
                        __zt_tmp = __attrs_4674609232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_4662095120('path', 'site/absolute_url', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' id="go-to-site-link"')

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674611216
                    __default_4674611216 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}" (49:60)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116a0e710> -> __attr_class
                    __token = 2166
                    __token = 2184
                    try:
                        __zt_tmp = __attrs_4674609232
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_4662095120('python', "'btn-lg' if not many and not outdated  else ''", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('btn btn-primary ', (__attr_class if (__attr_class is not None) else ''), ))
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674612048
                    __default_4674612048 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x1227bd5d0> at 116a0ea90> -> __attr_title
                    __attr_title = 'Go to your instance'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>\n                        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674615696
                    __attrs_4674615696 = _static_4659865408

                    # <Value 'not: many' (53:44)> -> __condition
                    __token = 2450
                    try:
                        __zt_tmp = __attrs_4674615696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('not', ' many', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:
                        __stream_4674614480 = []
                        __append_4674614480 = __stream_4674614480.append
                        __append_4674614480('View your Plone site')
                        __msgid_4674614480 = __re_whitespace(''.join(__stream_4674614480)).strip()
                        if __msgid_4674614480:
                            __append(translate(__msgid_4674614480, mapping=None, default=__msgid_4674614480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674613008
                    __attrs_4674613008 = _static_4659865408

                    # <Value 'many' (54:45)> -> __condition
                    __token = 2555
                    try:
                        __zt_tmp = __attrs_4674613008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'many', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <Interpolation value=<Substitution '${python:site.title} ' (54:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116a0c110> -> __content_4386234736
                        __token = 2561
                        __token = 2563
                        try:
                            __zt_tmp = __attrs_4674613008
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4386234736 = _static_4662095120('python', 'site.title', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __content_4386234736 = __quote(__content_4386234736, '\x00', '&#0;', None, None)
                        __content_4386234736 = ('%s%s' % ((__content_4386234736 if (__content_4386234736 is not None) else ''), ' ', ))
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

                        # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4673976336
                        __attrs_4673976336 = _static_4659865408

                        # <small ... (0:0)
                        # --------------------------------------------------------
                        __append('<small>')

                        # <Interpolation value=<Substitution '(${python:"/".join(site.getPhysicalPath())})' (54:79)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116972310> -> __content_4386234736
                        __token = 2589
                        __token = 2592
                        try:
                            __zt_tmp = __attrs_4673976336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_4386234736 = _static_4662095120('python', '"/".join(site.getPhysicalPath())', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __content_4386234736 = __quote(__content_4386234736, '\x00', '&#0;', None, None)
                        __content_4386234736 = ('%s%s%s' % ('(', (__content_4386234736 if (__content_4386234736 is not None) else ''), ')', ))
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
                        __append('</small>')
                    __append('\n                    </a>\n                    ')

                    # <Static value=<ast.Dict object at 0x1227bd840> name=None at 116973ed0> -> __attrs_4674440656
                    __attrs_4674440656 = _static_4873508928

                    # <Value 'outdated' (59:43)> -> __condition
                    __token = 2851
                    try:
                        __zt_tmp = __attrs_4674440656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_4662095120('path', 'outdated', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                    if __condition:

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form')

                        # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674437456
                        __default_4674437456 = _DEFAULT_MARKER

                        # <Substitution 'python:view.upgrade_url(site)' (60:51)> -> __attr_action
                        __token = 2912
                        try:
                            __zt_tmp = __attrs_4674440656
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_action = _static_4662095120('python', 'view.upgrade_url(site)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_action is not None):
                            __append((' action="%s"' % __attr_action))
                        __append(' style="display: inline;" method="get">\n                        ')

                        # <Static value=<ast.Dict object at 0x1227bc880> name=None at 1169e6990> -> __attrs_4674277136
                        __attrs_4674277136 = _static_4873504896

                        # <Value 'not:view/can_manage' (61:46)> -> __condition
                        __token = 2990
                        try:
                            __zt_tmp = __attrs_4674277136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_4662095120('not', 'view/can_manage', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="came_from"')

                            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674273680
                            __default_4674273680 = _DEFAULT_MARKER

                            # <Substitution 'python:view.upgrade_url(site, can_manage=True)' (63:54)> -> __attr_value
                            __token = 3128
                            try:
                                __zt_tmp = __attrs_4674277136
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_4662095120('python', 'view.upgrade_url(site, can_manage=True)', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append('/>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x1227bdd50> name=None at 1169bd310> -> __attrs_4674280208
                        __attrs_4674280208 = _static_4873510224

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" class="btn btn-warning me-3">')
                        __stream_4674277648 = []
                        __append_4674277648 = __stream_4674277648.append
                        __append_4674277648('Upgrade&hellip;')
                        __msgid_4674277648 = __re_whitespace(''.join(__stream_4674277648)).strip()
                        if 'label_upgrade_hellip':
                            __append(translate('label_upgrade_hellip', mapping=None, default=__msgid_4674277648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>\n                    </form>')
                    __append('\n                </div>')
                    if (__backup_outdated_4866718016 is __marker):
                        del econtext['outdated']
                    else:
                        econtext['outdated'] = __backup_outdated_4866718016
                    __append('\n            ')
                    ____index_4670396880 -= 1
                    if (____index_4670396880 > 0):
                        __append('')
                if (__backup_site_4866717968 is __marker):
                    del econtext['site']
                else:
                    econtext['site'] = __backup_site_4866717968
                __append('\n        </div>')
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x1227bc910> name=None at 11660a150> -> __attrs_4674281744
            __attrs_4674281744 = _static_4873505040

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674283600
            __attrs_4674283600 = _static_4659865408

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2 >')
            __stream_4674282576 = []
            __append_4674282576 = __stream_4674282576.append
            __append_4674282576('Add Plone site')
            __msgid_4674282576 = __re_whitespace(''.join(__stream_4674282576)).strip()
            if __msgid_4674282576:
                __append(translate(__msgid_4674282576, mapping=None, default=__msgid_4674282576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h2>\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674285456
            __attrs_4674285456 = _static_4659865408

            # <Value 'sites' (74:30)> -> __condition
            __token = 3620
            try:
                __zt_tmp = __attrs_4674285456
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'sites', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_4674284048 = []
                __append_4674284048 = __stream_4674284048.append
                __append_4674284048('\n                You can add another Plone site to the server.\n            ')
                __msgid_4674284048 = __re_whitespace(''.join(__stream_4674284048)).strip()
                if __msgid_4674284048:
                    __append(translate(__msgid_4674284048, mapping=None, default=__msgid_4674284048, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x1227be1a0> name=None at 1169bf510> -> __attrs_4674289552
            __attrs_4674289552 = _static_4873511328

            # <Value 'not:sites' (78:30)> -> __condition
            __token = 3770
            try:
                __zt_tmp = __attrs_4674289552
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('not', 'sites', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="alert alert-warning p-1">')
                __stream_4674286544 = []
                __append_4674286544 = __stream_4674286544.append
                __append_4674286544('\n                Your Plone site has not been added yet.\n            ')
                __msgid_4674286544 = __re_whitespace(''.join(__stream_4674286544)).strip()
                if __msgid_4674286544:
                    __append(translate(__msgid_4674286544, mapping=None, default=__msgid_4674286544, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x1227beb00> name=None at 1167a9150> -> __attrs_4667530256
            __attrs_4667530256 = _static_4873513728
            __backup_site_number_4866717632 = get('site_number', __marker)

            # <Value "python: '' if not sites else len(sites) + 1" (84:44)> -> __value
            __token = 4017
            try:
                __zt_tmp = __attrs_4667530256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('python', " '' if not sites else len(sites) + 1", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['site_number'] = __value
            __backup_action_4866717728 = get('action', __marker)

            # <Value 'string:${context/absolute_url}/@@plone-addsite' (85:38)> -> __value
            __token = 4100
            try:
                __zt_tmp = __attrs_4667530256
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_4662095120('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            econtext['action'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="add-plone-site" method="get"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671813264
            __default_4671813264 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}' (86:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116763410> -> __attr_action
            __token = 4177
            __token = 4179
            try:
                __zt_tmp = __attrs_4667530256
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_4662095120('path', 'action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_action = __attr_action
            if (__attr_action is None):
                pass
            else:
                if (__attr_action is _DEFAULT_MARKER):
                    __attr_action = None
                else:
                    __tt = type(__attr_action)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_action = str(__attr_action)
                    else:
                        if (__tt is bytes):
                            __attr_action = decode(__attr_action)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_action = __attr_action.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_action)
                                    __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                else:
                                    __attr_action = __attr_action()
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n                ')

            # <Static value=<ast.Dict object at 0x1227beef0> name=None at 116685a10> -> __attrs_4671160976
            __attrs_4671160976 = _static_4873514736

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="site_id"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4670905680
            __default_4670905680 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'Plone${site_number}' (87:59)> braces_required=True translation=False default='"?"' default_marker='"?"' at 116686910> -> __attr_value
            __token = 4248
            __token = 4255
            try:
                __zt_tmp = __attrs_4671160976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_4662095120('path', 'site_number', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_value = ('%s%s' % ('Plone', (__attr_value if (__attr_value is not None) else ''), ))
            if (__attr_value is None):
                pass
            else:
                if (__attr_value is _DEFAULT_MARKER):
                    __attr_value = None
                else:
                    __tt = type(__attr_value)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_value = str(__attr_value)
                    else:
                        if (__tt is bytes):
                            __attr_value = decode(__attr_value)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_value = __attr_value.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_value)
                                    __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                else:
                                    __attr_value = __attr_value()
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n                ')

            # <Static value=<ast.Dict object at 0x1227bf130> name=None at 1166c5710> -> __attrs_4671495312
            __attrs_4671495312 = _static_4873515312

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4671173328
            __default_4671173328 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "btn btn-${python:'success' if sites else 'primary'}" (89:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1166c6510> -> __attr_class
            __token = 4341
            __token = 4351
            try:
                __zt_tmp = __attrs_4671495312
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_4662095120('python', "'success' if sites else 'primary'", econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s' % ('btn btn-', (__attr_class if (__attr_class is not None) else ''), ))
            if (__attr_class is None):
                pass
            else:
                if (__attr_class is _DEFAULT_MARKER):
                    __attr_class = None
                else:
                    __tt = type(__attr_class)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_class = str(__attr_class)
                    else:
                        if (__tt is bytes):
                            __attr_class = decode(__attr_class)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_class = __attr_class.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_class)
                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                else:
                                    __attr_class = __attr_class()
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))
            __append('>')
            __stream_4671163344 = []
            __append_4671163344 = __stream_4671163344.append
            __append_4671163344('Create a new Plone site')
            __msgid_4671163344 = __re_whitespace(''.join(__stream_4671163344)).strip()
            if __msgid_4671163344:
                __append(translate(__msgid_4671163344, mapping=None, default=__msgid_4671163344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n                ')

            # <Static value=<ast.Dict object at 0x1227bf340> name=None at 1167177d0> -> __attrs_4673816784
            __attrs_4673816784 = _static_4873515840

            # <Value 'view/has_volto' (93:35)> -> __condition
            __token = 4582
            try:
                __zt_tmp = __attrs_4673816784
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_4662095120('path', 'view/has_volto', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="btn btn-info"')

                # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673815312
                __default_4673815312 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;classic=1' (94:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11694c2d0> -> __attr_href
                __token = 4624
                __token = 4626
                try:
                    __zt_tmp = __attrs_4673816784
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_4662095120('path', 'action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __token = 4649
                try:
                    __zt_tmp = __attrs_4673816784
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href_4647 = _static_4662095120('path', 'site_number', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
                __attr_href_4647 = __quote(__attr_href_4647, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4647 if (__attr_href_4647 is not None) else ''), '&amp;classic=1', ))
                if (__attr_href is None):
                    pass
                else:
                    if (__attr_href is _DEFAULT_MARKER):
                        __attr_href = None
                    else:
                        __tt = type(__attr_href)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_href = str(__attr_href)
                        else:
                            if (__tt is bytes):
                                __attr_href = decode(__attr_href)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_href = __attr_href.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_href)
                                        __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                    else:
                                        __attr_href = __attr_href()
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')
                __stream_4671496720 = []
                __append_4671496720 = __stream_4671496720.append
                __append_4671496720('Create Classic Plone site')
                __msgid_4671496720 = __re_whitespace(''.join(__stream_4671496720)).strip()
                if __msgid_4671496720:
                    __append(translate(__msgid_4671496720, mapping=None, default=__msgid_4671496720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            __append('\n                ')

            # <Static value=<ast.Dict object at 0x1227bf520> name=None at 11694c490> -> __attrs_4672408976
            __attrs_4672408976 = _static_4873516320

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-secondary"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673828752
            __default_4673828752 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;advanced=1' (98:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 11694d050> -> __attr_href
            __token = 4837
            __token = 4839
            try:
                __zt_tmp = __attrs_4672408976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4662095120('path', 'action', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 4862
            try:
                __zt_tmp = __attrs_4672408976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href_4860 = _static_4662095120('path', 'site_number', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_href_4860 = __quote(__attr_href_4860, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4860 if (__attr_href_4860 is not None) else ''), '&amp;advanced=1', ))
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')
            __stream_4673819728 = []
            __append_4673819728 = __stream_4673819728.append
            __append_4673819728('Advanced')
            __msgid_4673819728 = __re_whitespace(''.join(__stream_4673819728)).strip()
            if __msgid_4673819728:
                __append(translate(__msgid_4673819728, mapping=None, default=__msgid_4673819728, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            </form>')
            if (__backup_action_4866717728 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_4866717728
            if (__backup_site_number_4866717632 is __marker):
                del econtext['site_number']
            else:
                econtext['site_number'] = __backup_site_number_4866717632
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4672413264
            __attrs_4672413264 = _static_4659865408

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br/>\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4672421776
            __attrs_4672421776 = _static_4659865408

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4672415952 = []
            __append_4672415952 = __stream_4672415952.append
            __append_4672415952("\n                Starting with Plone 6, 'Create a new Plone site' applies a\n                profile and creates default content for the new React based\n                default frontend Volto. You are however required to set up and run\n                an additional frontend service to use this setup.\n            ")
            __msgid_4672415952 = __re_whitespace(''.join(__stream_4672415952)).strip()
            if 'help_create_plone_site_buttons_1':
                __append(translate('help_create_plone_site_buttons_1', mapping=None, default=__msgid_4672415952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n            ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4673782032
            __attrs_4673782032 = _static_4659865408

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_4873678272_docs_link = ''
            __stream_4672421392 = []
            __append_4672421392 = __stream_4672421392.append
            __append_4672421392("\n                The 'Create Classic Plone site' button creates a Plone site configured\n                for HTML based output, as was already supported by previous Plone versions.\n                Please consult our\n                ")
            __stream_4873678272_docs_link = []
            __append_4873678272_docs_link = __stream_4873678272_docs_link.append

            # <Static value=<ast.Dict object at 0x1227bf880> name=None at 116944a50> -> __attrs_4673793232
            __attrs_4673793232 = _static_4873517184

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_4873678272_docs_link('<a href="https://6.docs.plone.org/"')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4673791632
            __default_4673791632 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x1227bf760> at 116945790> -> __attr_title
            __attr_title = 'Plone 6 developer documentation'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_4873678272_docs_link((' title="%s"' % __attr_title))
            __append_4873678272_docs_link('>')
            __stream_4673784144 = []
            __append_4673784144 = __stream_4673784144.append
            __append_4673784144('developer documentation overview ')
            __msgid_4673784144 = __re_whitespace(''.join(__stream_4673784144)).strip()
            if __msgid_4673784144:
                __append_4873678272_docs_link(translate(__msgid_4673784144, mapping=None, default=__msgid_4673784144, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_4873678272_docs_link('</a>')
            __append_4672421392('${docs_link}')
            __stream_4873678272_docs_link = ''.join(__stream_4873678272_docs_link)
            __append_4672421392('\n                for more information about differences and requirements for\n                these frontends and possible upgrade paths from older Plone versions\n                to Plone 6.\n            ')
            __msgid_4672421392 = __re_whitespace(''.join(__stream_4672421392)).strip()
            if 'help_create_plone_site_buttons_2':
                __append(translate('help_create_plone_site_buttons_2', mapping={'docs_link': __stream_4873678272_docs_link, }, default=__msgid_4672421392, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n    </article>\n\n    ')

            # <Static value=<ast.Dict object at 0x1227bec50> name=None at 116944290> -> __attrs_4673796240
            __attrs_4673796240 = _static_4873514064

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer class="row">\n    ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4674521680
            __attrs_4674521680 = _static_4659865408

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      ')

            # <Static value=<ast.Dict object at 0x1227bfd60> name=None at 1169f9b90> -> __attrs_4674532368
            __attrs_4674532368 = _static_4873518432

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674529168
            __default_4674529168 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/manage_main' (126:29)> -> __attr_href
            __token = 6194
            try:
                __zt_tmp = __attrs_4674532368
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_4662095120('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_4662088080(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 115b98fd0> -> __default_4674531088
            __default_4674531088 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x1227bfbe0> at 1169fa750> -> __attr_title
            __attr_title = 'Go to the ZMI'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')
            __stream_4674528592 = []
            __append_4674528592 = __stream_4674528592.append
            __append_4674528592('Management Interface')
            __msgid_4674528592 = __re_whitespace(''.join(__stream_4674528592)).strip()
            if 'label_zmi_link':
                __append(translate('label_zmi_link', mapping=None, default=__msgid_4674528592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n      ')

            # <Static value=<ast.Dict object at 0x115bfe740> name=None at 115b6d050> -> __attrs_4675224912
            __attrs_4675224912 = _static_4659865408

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_4674519888 = []
            __append_4674519888 = __stream_4674519888.append
            __append_4674519888(' &#151; low-level technical configuration.')
            __msgid_4674519888 = __re_whitespace(''.join(__stream_4674519888)).strip()
            if 'label_zmi_link_description':
                __append(translate('label_zmi_link_description', mapping=None, default=__msgid_4674519888, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n    </p>\n  </footer>\n</div>\n</body>')
            if (__backup_many_4866717392 is __marker):
                del econtext['many']
            else:
                econtext['many'] = __backup_many_4866717392
            if (__backup_sites_4866717248 is __marker):
                del econtext['sites']
            else:
                econtext['sites'] = __backup_sites_4866717248
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_4670119376
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }