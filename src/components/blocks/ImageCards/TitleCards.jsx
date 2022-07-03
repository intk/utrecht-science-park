import { Image, Message } from 'semantic-ui-react';

import { TitleCardsSchema } from './schema';
import { getScaleUrl, getPath } from './utils';
import { serializeNodes } from 'volto-slate/editor/render';
import { UniversalLink } from '@plone/volto/components';

import { LinkMore } from '@plone/volto/components';

import './less/title-cards.less';

const LinkWrapper = ({ link, children, title }) => {
  return link ? (
    <a href={link} target="_blank" rel="noreferrer" title={title}>
      {children}
    </a>
  ) : (
    children
  );
};

const Card = ({ card = {}, image_scale }) => {
  const { link, title, text } = card;

  return (
    <div className="title-card">
      <LinkWrapper link={link} title={title}>
        <h2>{title || 'null'}</h2>
        <div className="title-card-text">
          {text ? serializeNodes(text) : ''}
        </div>
        <div className="title-card-image">
          <Image
            className="bg-image"
            src={getScaleUrl(
              getPath(card.attachedimage),
              image_scale || 'large',
            )}
          />
        </div>
      </LinkWrapper>
    </div>
  );
};

const TitleCards = (props) => {
  const { data = {}, editable = false } = props;
  const { cards = [], title, linkHref } = data;
  // {callToActionLink ? <UniversalLink href={callToActionLink} /> : ''}

  return !cards.length ? (
    editable ? (
      <Message>No cards</Message>
    ) : (
      ''
    )
  ) : (
    <div className="title-cards">
      <div className="listing-block-header">
        <h1>{title}</h1>
        {linkHref ? <LinkMore data={data} /> : ''}
      </div>
      {cards.map((card, i) => (
        <Card key={i} card={card} />
      ))}
    </div>
  );
};

TitleCards.schemaExtender = (schema, data, intl) => {
  const Custom = TitleCardsSchema({ data, schema, intl });
  schema.fieldsets[0].fields.splice(2, 0, 'linkHref');
  schema.fieldsets[0].fields.splice(3, 0, 'linkTitle');
  const out = {
    ...schema,
    ...Custom,
    properties: { ...schema.properties, ...Custom.properties },
    fieldsets: [...schema.fieldsets, ...Custom.fieldsets],
  };
  console.log('out', out);
  return out;
};

export default TitleCards;
