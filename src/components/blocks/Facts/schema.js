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
  image: {
    id: 'image',
    defaultMessage: 'Image',
  },
  subtitle: {
    id: 'subtitle',
    defaultMessage: 'SubTitle',
  },
  LinkTo: {
    id: 'LinkTo',
    defaultMessage: 'Action link',
  },
  Cards: {
    id: 'Cards',
    defaultMessage: 'Cards',
  },
  Card: {
    id: 'Card',
    defaultMessage: 'Card',
  },
  linkToDescription: {
    id: 'linkToDescription',
    defaultMessage: 'Destination for the call to action button',
  },
});

const CardSchema = ({ onChangeBlock, intl, data, openObjectBrowser }) => ({
  title: intl.formatMessage(messages.Card),
  fieldsets: [
    {
      id: 'default',
      fields: ['title', 'subtitle', 'url'],
      title: 'Default',
    },
  ],

  properties: {
    title: {
      title: intl.formatMessage(messages.title),
    },
    subtitle: {
      title: intl.formatMessage(messages.subtitle),
    },
    url: {
      title: intl.formatMessage(messages.image),
      widget: 'attachedimage',
    },
  },
  required: [],
});

const schema = ({ onChangeBlock, intl, data, openObjectBrowser }) => ({
  fieldsets: [
    {
      id: 'default',
      fields: ['title', 'href', 'cards'],
      title: 'Basics',
    },
  ],

  properties: {
    title: {
      title: intl.formatMessage(messages.title),
      description: 'Main block title',
    },
    cards: {
      title: intl.formatMessage(messages.Cards),
      widget: 'object_list',
      schema: CardSchema({ onChangeBlock, intl, data, openObjectBrowser }),
    },

    href: {
      title: intl.formatMessage(messages.LinkTo),
      description: intl.formatMessage(messages.linkToDescription),
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
    callToAction: {
      title: 'Link title',
      description: 'Text for the call to action button',
    },
  },
  required: [],
});

export default schema;