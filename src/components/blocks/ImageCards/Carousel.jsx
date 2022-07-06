import React from 'react';
import { Popup, Image, Message } from 'semantic-ui-react';
import ResponsiveContainer from '@eeacms/volto-block-image-cards/ImageCards/ResponsiveContainer';
import { ListingBlockHeader } from '@package/components';
import { Placeholder } from 'semantic-ui-react';
import { serializeNodes } from 'volto-slate/editor/render';
import cx from 'classnames';

import loadable from '@loadable/component';

import 'slick-carousel/slick/slick.css';
import './less/image-carousel.less';
import 'slick-carousel/slick/slick-theme.css';

import { ImageCarouselSchema } from './schema';
import { getScaleUrl, getPath } from './utils';

const Slider = loadable(() => import('react-slick'));

const Caption = ({ card }) => {
  const { title, text } = card;

  return (
    <div className="slide-caption">
      {!!title && <h4>{title}</h4>}
      {!!text && serializeNodes(text)}
    </div>
  );
};

const Card = ({ card = {}, height, image_scale, mode = 'view' }) => {
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
    <div className="slide-img" style={{ height }}>
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

const ImageCarousel = (props) => {
  const { data = {}, editable = false } = props;
  const sliderRef = React.useRef();
  const [slideIndex, setSlideIndex] = React.useState(0);
  const [isClient, setIsClient] = React.useState(false);

  React.useEffect(() => setIsClient(true), []);
  const {
    cards = [],
    height = '120px',
    itemsPerRow = 4,
    hideNavigationDots = false,
    autoplay = false,
    autoplaySpeed = 3000,
    image_scale = 'large',
    display = '',
  } = data;

  const carouselSettings = React.useMemo(
    () => ({
      afterChange: (current) => setSlideIndex(current),
      // speed: 800,
      infinite: true,
      slidesToShow: Math.min(cards.length, itemsPerRow),
      slidesToScroll: 1,
      dots: itemsPerRow > 1 && !hideNavigationDots,
      autoplay: itemsPerRow > 1 && autoplay && !editable,
      autoplaySpeed,
      fade: false,
      useTransform: false,
      lazyLoad: 'ondemand',

      responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
            infinite: true,
            dots: true,
          },
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
            initialSlide: 2,
          },
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          },
        },
      ],
    }),
    [
      autoplay,
      autoplaySpeed,
      cards.length,
      editable,
      hideNavigationDots,
      itemsPerRow,
    ],
  );

  return !cards.length ? (
    editable ? (
      <Message>No cards</Message>
    ) : (
      ''
    )
  ) : (
    <div className={cx('image-carousel', `image-carousel-${display}`)}>
      <ListingBlockHeader data={data} />
      <Slider {...carouselSettings} ref={sliderRef}>
        {cards.map((card, i) => (
          <Card
            key={i}
            mode={editable ? 'edit' : 'view'}
            card={card}
            height={height}
            image_scale={image_scale}
          />
        ))}
      </Slider>
      {!!sliderRef.current && carouselSettings.slidesToShow === 1 && (
        <Caption card={cards[slideIndex]} />
      )}
    </div>
  );
};

ImageCarousel.schemaExtender = (schema, data, intl) => {
  const Custom = ImageCarouselSchema({ data, schema, intl });
  return {
    ...schema,
    ...Custom,
    properties: { ...schema.properties, ...Custom.properties },
    fieldsets: [
      // { id: 'empty', fields: [] },
      ...schema.fieldsets,
      ...Custom.fieldsets,
    ],
  };
};

export default ImageCarousel;
