import React from 'react';
import cx from 'classnames';
import { Button, Card, Ref } from 'semantic-ui-react'; // Container,
import useDeepCompareEffect from 'use-deep-compare-effect';
import useSize from '@react-hook/size';
import TextTruncate from 'react-text-truncate';

import { flattenToAppURL } from '@plone/volto/helpers';
import { UniversalLink, Icon } from '@plone/volto/components';

import galleryLeftSVG from '@plone/volto/icons/left-key.svg';
import galleryRightSVG from '@plone/volto/icons/right-key.svg';

function usePrevious(value) {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  }, [value]);
  return ref.current;
}

const ItemCard = ({ item }) => {
  return (
    <Card>
      <Card.Content>
        <Card.Header>
          <UniversalLink href={flattenToAppURL(item['@id'])} title={item.title}>
            <TextTruncate
              key={item['@id']}
              line={2}
              element="span"
              truncateText="…"
              text={item.title}
            />
          </UniversalLink>
        </Card.Header>
        <Card.Description>{item.description}</Card.Description>
      </Card.Content>
      <Card.Content extra>
        <UniversalLink href={flattenToAppURL(item['@id'])}>
          Read more
        </UniversalLink>
      </Card.Content>
    </Card>
  );
};

const getIdealSize = (width) =>
  width < 200 ? 1 : width < 400 ? 1 : width < 600 ? 2 : width < 1000 ? 3 : 6;

const HorizontalCarousel = ({ items = [], showMax = 10, ...rest }) => {
  const hasItems = items && items.length;
  const [position, setPosition] = React.useState(0);
  const oldItems = usePrevious(items);

  const containerRef = React.useRef();
  const itemRef = React.useRef();

  const [containerWidth] = useSize(containerRef, { initialWidth: 1200 });
  // const [itemWidth] = useSize(itemRef, {
  //   initialWidth: getIdealSize(containerWidth),
  // });

  useDeepCompareEffect(() => {
    if (oldItems) {
      setPosition(0);
    }
  }, [items, oldItems]);

  const limit = getIdealSize(containerWidth); // Math.floor(containerWidth / itemWidth) || 1;
  const container = React.useRef();

  // console.log('container', {
  //   containerWidth,
  //   itemWidth,
  //   limit,
  // });

  let showItems = items
    .slice(position)
    .concat(items.slice(0, position + 1))
    .slice(0, limit);

  return !hasItems ? (
    'No results'
  ) : (
    <div
      ref={containerRef}
      className={cx('horizontal-carousel', {
        'ui container': rest.isContainer,
      })}
    >
      <div className="bullets">
        {items.map((item, k) => (
          <div
            onKeyDown={() => {}}
            tabIndex="-1"
            role="button"
            key={k}
            className={`bullet ${position === k ? 'active' : ''}`}
            onClick={() => setPosition(k)}
          ></div>
        ))}
      </div>
      {showItems.length > 4 && (
        <div className="go-left">
          <Button
            className="image-gallery-icon image-gallery-left-nav primary basic"
            onClick={() => {
              setPosition(position - 1);
            }}
            disabled={position === 0}
          >
            <Icon name={galleryLeftSVG} size="48px" />
          </Button>
        </div>
      )}
      <div className="paged-content" ref={container}>
        {showItems.map((item, k) =>
          k === 0 ? (
            <Ref key={k} innerRef={itemRef}>
              <ItemCard item={item} />
            </Ref>
          ) : (
            <ItemCard key={k} item={item} />
          ),
        )}
      </div>
      {showItems.length > 4 && (
        <div className="go-right">
          <Button
            className="image-gallery-icon image-gallery-right-nav primary basic"
            onClick={() => {
              setPosition(position + 1);
            }}
            disabled={position === showItems.length - 1}
          >
            <Icon name={galleryRightSVG} size="48px" />
          </Button>
        </div>
      )}
    </div>
  );
};

export const horizontalCarouselSchemaEnhancer = ({
  formData,
  schema,
  intl,
}) => {
  schema.fieldsets[0].fields.push('isContainer');
  schema.properties.isContainer = {
    title: 'Full width?',
    type: 'boolean',
  };
  return schema;
};

export default HorizontalCarousel;
