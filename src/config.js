import CookieBanner from 'volto-cookie-banner/CookieBannerContainer';
import { MultilingualWidget } from 'volto-multilingual-widget';

// import installStyleMenu from 'volto-slate/editor/plugins/StyleMenu';
import loadable from '@loadable/component';
import AttachedImageWidget from './components/widgets/AttachedImageWidget';
import installBlocks from './components/blocks';
import MultipleContentView from './components/theme/View/MultipleContentView';
import ListingView from './components/theme/View/ListingView';
// import Layouts from '@plone/volto/constants/Layouts';
import { getContent } from '@plone/volto/actions';
import installFooter from './footer';
import installExpressMiddleware from './express-middleware';
import { GTMTracker } from './components/hocs/useTagManager';

// All your imports required for the config here BEFORE this line
import '@plone/volto/config';

// __CLIENT__ && !__DEVELOPMENT__ && TagManager.initialize(tagManagerArgs);

export default function applyConfig(config) {
  // Add here your project's configuration here by modifying `config` accordingly

  // installStyleMenu(config);

  const DEFAULT_LANG = 'en';

  config.settings.isMultilingual = true;
  config.settings.supportedLanguages = ['en', 'nl'];
  config.settings.defaultLanguage = DEFAULT_LANG;

  config.settings.footerPageId = 'footer-content';
  config.settings.actionBlockIds = [
    ['footerLinks', 'Footer Links'],
    ['siteActions', 'Site Actions'],
  ];
  config.settings.gtmId = 'GTM-T8SF8PJ';

  config.blocks.blocksConfig.title.view = () => null;
  config.blocks.groupBlocksOrder.push({ id: 'site', title: 'Site' });

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

            const url = `/${currentLang}/${config.settings.footerPageId}`;
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
  config.views.layoutViewsNamesMapping.multiple_content = 'Section layout';

  config.widgets.widget.attachedimage = AttachedImageWidget;
  config.widgets.id.cookie_consent_configuration = MultilingualWidget();

  config.settings.appExtras = [
    ...(config.settings.appExtras || []),
    {
      match: '',
      component: CookieBanner,
    },
    {
      match: '',
      component: GTMTracker,
    },
  ];

  // config.settings.apiExpanders = [
  //   ...config.settings.apiExpanders,
  //   {
  //     match: '',
  //     GET_CONTENT: ['navigation'],
  //   },
  // ];

  return installExpressMiddleware(installFooter(installBlocks(config)));
}
