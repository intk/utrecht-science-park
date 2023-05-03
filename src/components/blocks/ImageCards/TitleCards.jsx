import { Image, Message } from 'semantic-ui-react';
import cx from 'classnames';

import { TitleCardsSchema } from './schema';
import { getScaleUrl, getPath } from './utils';
import { serializeNodes } from '@plone/volto-slate/editor/render';
import { ListingBlockHeader } from '@package/components';

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

const Card = ({ card = {}, image_scale, imageSize }) => {
  const { link, title, text } = card;

  return (
    <LinkWrapper link={link} title={title}>
      <div className="title-card">
        <h3>{title || 'null'}</h3>
        <div className="title-card-text">
          {text ? serializeNodes(text) : ''}
        </div>
        <div className="title-card-image">
          <Image
            className={cx('bg-image', imageSize || 'small')}
            src={getScaleUrl(
              getPath(card.attachedimage),
              image_scale || 'large',
            )}
          />
        </div>
      </div>
    </LinkWrapper>
  );
};

const TitleCards = (props) => {
  const { data = {}, editable = false } = props;
  const { cards = [] } = data;

  return !cards.length ? (
    editable ? (
      <Message>No cards</Message>
    ) : (
      ''
    )
  ) : (
    <div className="title-cards">
      <ListingBlockHeader data={data} />
      {cards.map((card, i) => (
        <Card key={i} card={card} imageSize={data.imageSize} />
      ))}
    </div>
  );
};

TitleCards.schemaExtender = (schema, data, intl) => {
  const Custom = TitleCardsSchema({ data, schema, intl });

  schema.fieldsets[0].fields.splice(2, 0, 'linkHref');
  schema.fieldsets[0].fields.splice(3, 0, 'linkTitle');
  schema.fieldsets[0].fields.splice(3, 0, 'imageSize');

  // if (!schema.properties.cards.schema.properties.imageSize) {
  //   schema.properties.cards.schema.properties.imageSize = {
  //     title: 'Image size',
  //     choices: [
  //       ['small', 'Small'],
  //       ['bigger', 'Bigger'],
  //     ],
  //     default: 'small',
  //   };
  //   schema.properties.cards.schema.fieldsets[0].fields.push('imageSize');
  // }

  // console.log('schema', schema);

  const out = {
    ...schema,
    ...Custom,
    properties: { ...schema.properties, ...Custom.properties },
    fieldsets: [...schema.fieldsets, ...Custom.fieldsets],
  };
  return out;
};

export default TitleCards;
