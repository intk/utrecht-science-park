import installStyleMenu from 'volto-slate/editor/plugins/StyleMenu';
import loadable from '@loadable/component';
import AttachedImageWidget from './components/widgets/AttachedImageWidget';
import installBlocks from './components/blocks';
import MultipleContentView from './components/theme/View/MultipleContentView';
import ListingView from './components/theme/View/ListingView';
import Layouts from '@plone/volto/constants/Layouts';
import { getContent } from '@plone/volto/actions';

// All your imports required for the config here BEFORE this line
import '@plone/volto/config';

export default function applyConfig(config) {
  // Add here your project's configuration here by modifying `config` accordingly

  installStyleMenu(config);
  const DEFAULT_LANG = 'en';

  config.settings.isMultilingual = true;
  config.settings.supportedLanguages = ['en', 'nl'];
  config.settings.defaultLanguage = DEFAULT_LANG;

  config.blocks.blocksConfig.title.view = () => null;

  config.settings = {
    ...config.settings,
    navDepth: 3,
  };

  config.settings.loadables = {
    ...config.settings.loadables,
    dateFns: loadable.lib(() => import('date-fns')),
  };

  config.settings.slate.styleMenu = {
    inlineStyles: [],
    blockStyles: [
      { cssClass: 'discreetBlock', label: 'Discreet' },
      { cssClass: 'p2', label: 'Secondary' },
      //{ cssClass: 'buttonSec', label: 'Secondary button' },
    ],
  };

  config.settings.asyncPropsExtenders = [
    ...(config.settings.asyncPropsExtenders || []),
    {
      path: '/',
      extend: (dispatchActions) => {
        const action = {
          key: 'footer',
          promise: ({ location, store }) => {
            // const currentLang = state.intl.locale;
            const bits = location.pathname.split('/');
            const currentLang =
              bits.length >= 2 ? bits[1] || DEFAULT_LANG : DEFAULT_LANG;

            const state = store.getState();
            if (state.content.subrequests?.[`footer-${currentLang}`]?.data) {
              return;
            }

            const url = `/${currentLang}/footer-links`;
            const action = getContent(url, null, `footer-${currentLang}`);
            return store.dispatch(action).catch((e) => {
              // eslint-disable-next-line
              console.log(
                `Footer links folder not found: ${url}. Please create as folder
                named footer-links in the root of your current language`,
              );
            });
          },
        };
        return [...dispatchActions, action];
      },
    },
  ];

  config.views.layoutViews.multiple_content = MultipleContentView;
  config.views.layoutViews.listing_view = ListingView;
  config.views.layoutViews.listing_view = ListingView;
  config.views.contentTypesViews.Event = config.views.defaultView;

  Layouts.multiple_content = 'Section layout';

  config.widgets.widget.attachedimage = AttachedImageWidget;
  config.settings.siteActions = [
    {
      id: 'Newsletter',
      links: {
        en: {
          title: 'Newsletter',
          path: '/en/contact',
        },
        nl: {
          title: 'Newsletter-NL',
          path: '/nl/contact',
        },
      },
    },
    {
      id: 'Disclaimer',
      links: {
        en: {
          title: 'Disclaimer',
          path: '/en/contact',
        },
        nl: {
          title: 'Disclaimer-NL',
          path: '/nl/contact',
        },
      },
    },
    {
      id: 'Privacy policy',
      links: {
        en: {
          title: 'Privacy policy',
          path: '/en/contact',
        },
        nl: {
          title: 'Privacy policy-NL',
          path: '/nl/contact',
        },
      },
    },
    {
      id: 'Login',
      links: {
        en: {
          title: 'Login',
          path: '/en/login',
        },
        nl: {
          title: 'Login',
          path: '/nl/login',
        },
      },
    },
  ];

  config.settings.footerLinks = [
    {
      id: 'Contacts',
      links: {
        en: {
          title: 'Contacts',
          path: '/en/contact',
        },
        nl: {
          title: 'Contacts-NL',
          path: '/nl/contact',
        },
      },
    },
    {
      id: 'Vacancies',
      links: {
        en: {
          title: 'Vacancies',
          path: '/en/vacancies',
        },
        nl: {
          title: 'Vacancies-NL',
          path: '/nl/vacancies',
        },
      },
    },
    {
      id: 'FAQ',
      links: {
        en: {
          title: 'FAQ',
          path: '/en/faq',
        },
        nl: {
          title: 'FAQ-NL',
          path: '/nl/faq',
        },
      },
    },
    {
      id: 'About',
      links: {
        en: {
          title: 'About',
          path: '/en/about',
        },
        nl: {
          title: 'About-NL',
          path: '/nl/about',
        },
      },
    },
  ];

  config.settings.socialLinks = [
    {
      id: 'Facebook',
      title: 'Facebook',
      href: 'https://facebook.com',
    },
    {
      id: 'Instagram',
      title: 'Instagram',
      href: 'https://Instagram.com',
    },
    {
      id: 'Twitter',
      title: 'Twitter',
      href: 'https://Twitter.com',
    },
    {
      id: 'Youtube',
      title: 'Youtube',
      href: 'https://Youtube.com',
    },
    {
      id: 'Linkedin',
      title: 'Linkedin',
      href: 'https://Linkedin.com',
    },
  ];

  return installBlocks(config);
}
