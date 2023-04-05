import React from 'react';
import { Image, Message } from 'semantic-ui-react';
import { ListingBlockHeader } from '@package/components';
import cx from 'classnames';
import { getScaleUrl, getPath } from './utils';
import { Placeholder } from 'semantic-ui-react';

import './less/image-gallery.less';

export const Card = ({
  card = {},
  height,
  image_scale,
  mode = 'view',
  className,
}) => {
  const { link, title } = card;

  const LinkWrapper = React.useMemo(
    () =>
      link && mode === 'view'
        ? ({ children }) => (
            <a href={link} target="_blank" rel="noreferrer" title={title}>
              {children}
            </a>
          )
        : ({ children }) => children,
    [link, mode, title],
  );

  return (
    <div className={cx('card-img', className)} style={{ height }}>
      <LinkWrapper>
        {card.attachedimage ? (
          <Image
            className="bg-image"
            src={getScaleUrl(
              getPath(card.attachedimage),
              image_scale || 'large',
            )}
          />
        ) : (
          <Placeholder />
        )}
      </LinkWrapper>
    </div>
  );
};

const Gallery = (props) => {
  const { data = {}, editable = false } = props;
  const {
    cards = [],
    height = '233px',
    itemsPerRow = 4,
    image_scale = 'large',
  } = data;

  return !cards.length ? (
    editable ? (
      <Message>No cards</Message>
    ) : (
      ''
    )
  ) : (
    <div className={cx('image-gallery')}>
      <ListingBlockHeader data={data} />
      <div className="image-gallery-cards">
        {cards.map((card, i) => (
          <Card
            key={i}
            mode={editable ? 'edit' : 'view'}
            card={card}
            height={height}
            image_scale={image_scale}
            className={`card-${itemsPerRow}x`}
          />
        ))}
      </div>
    </div>
  );
};

Gallery.schemaExtender = (schema, data, intl) => {
  schema.fieldsets[0].fields.push('itemsPerRow');
  schema.properties.itemsPerRow = {
    type: 'choice',
    title: 'Items per row',
    choices: [
      [3, '3 per row'],
      [4, '4 per row'],
    ],
  };
  return schema;
};

export default Gallery;
