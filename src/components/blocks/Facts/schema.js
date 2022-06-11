import { defineMessages } from 'react-intl';
// import { flattenToAppURL } from '@plone/volto/helpers';

import clearSVG from '@plone/volto/icons/clear.svg';
import navTreeSVG from '@plone/volto/icons/nav.svg';

const messages = defineMessages({
  icon: {
    id: 'icon',
    defaultMessage: 'Icon',
  },
  title: {
    id: 'title',
    defaultMessage: 'Title',
  },
  subtitle: {
    id: 'subtitle',
    defaultMessage: 'SubTitle',
  },
  LinkTo: {
    id: 'LinkTo',
    defaultMessage: 'Call to action link',
  },
});

const CardSchema = ({ onChangeBlock, intl, data, openObjectBrowser }) => ({
  fieldsets: [
    {
      id: 'default',
      fields: ['title', 'subtitle', 'url'],
    },
  ],

  properties: {
    title: {
      title: messages.title,
    },
    subtitle: {
      title: messages.subtitle,
    },
    url: {
      title: 'Image',
      widget: 'attachedimage',
    },
  },
  required: [],
});

const schema = ({ onChangeBlock, intl, data, openObjectBrowser }) => ({
  fieldsets: [
    {
      id: 'default',
      fields: ['href', 'cards'],
    },
  ],

  properties: {
    cards: {
      widget: 'object_list',
      schema: CardSchema({ onChangeBlock, intl, data, openObjectBrowser }),
    },

    href: {
      title: intl.formatMessage(messages.LinkTo),
      icon: data.href ? clearSVG : navTreeSVG,
      iconAction: data.href
        ? () => {
            onChangeBlock(data.block, {
              ...data,
              href: '',
            });
          }
        : () => openObjectBrowser({ mode: 'link' }),
    },
  },
  required: [],
});

export default schema;
