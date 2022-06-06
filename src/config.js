// All your imports required for the config here BEFORE this line
import '@plone/volto/config';

export default function applyConfig(config) {
  // Add here your project's configuration here by modifying `config` accordingly

  config.settings.isMultilingual = true;
  config.settings.supportedLanguages = ['en', 'nl'];
  config.settings.defaultLanguage = 'en';
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
  return config;
}
