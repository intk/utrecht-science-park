import React from 'react';
import loadable from '@loadable/component';
import { Message } from 'semantic-ui-react';
import { Icon, UniversalLink } from '@plone/volto/components';
import { isInternalURL, flattenToAppURL } from '@plone/volto/helpers';
import readySVG from '@plone/volto/icons/ready.svg';

import cx from 'classnames';

import 'slick-carousel/slick/slick.css';
import './less/video-carousel.less';

import { getPath } from './utils';

import { BodyClass } from '@plone/volto/helpers';

const Slider = loadable(() => import('react-slick'));

const VideoEmbed = ({ url, placeholder, height, width }) => {
  const embedId = url.match(/.be\//)
    ? url.match(/^.*\.be\/(.*)/)[1]
    : url.match(/^.*\?v=(.*)$/)[1];

  const [play, setIsPlay] = React.useState();

  return (
    <div className="video-responsive">
      {play ? (
        <iframe
          width={width}
          height={height}
          src={`https://www.youtube.com/embed/${embedId}`}
          frameBorder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
          title="Embedded youtube"
        />
      ) : (
        <div className="placeholder-image">
          <img src={placeholder} className="placeholder" alt="Placeholder" />
          <Icon
            name={readySVG}
            size={`${height / 10}px`}
            color="white"
            onClick={() => setIsPlay(true)}
          />
        </div>
      )}
    </div>
  );
};

const VideoSlide = ({ card, image_scale, height }) => {
  const preview_image = getPath(card.attachedimage);
  let placeholder = preview_image
    ? isInternalURL(preview_image)
      ? `${flattenToAppURL(preview_image)}/@@images/image`
      : preview_image
    : null;

  const embedSettings = {
    url: card.videoUrl,
    placeholder,
    height,
    width: '100%',
  };

  return (
    <div className="slider-slide">
      <VideoEmbed {...embedSettings} />
      <div className="slider-caption">
        <div className="slide-body">
          {card.linkHref?.[0] ? (
            <UniversalLink href={card.linkHref[0]['@id']}>
              <h2 className="slide-title">{card.title || ''}</h2>
            </UniversalLink>
          ) : (
            <h2 className="slide-title">{card.title || ''}</h2>
          )}
        </div>
        {!!card.linkHref?.[0] && (
          <UniversalLink href={card.linkHref[0]['@id']} className="ui button">
            {card.linkTitle || '...'}
          </UniversalLink>
        )}
      </div>
    </div>
  );
};

const VideoCarousel = ({ data }) => {
  const sliderRef = React.useRef();
  const nodeRef = React.useRef();

  const { cards = [], image_scale = 'large' } = data;

  var settings = React.useMemo(
    () => ({
      fade: true,
      speed: 800,
      infinite: true,
      autoplay: true,
      pauseOnHover: true,
      autoplaySpeed: 10000,
      slidesToShow: 1,
      slidesToScroll: 1,
      adaptiveHeight: false,
      vertical: false,
      lazyLoad: 'ondemand',
      arrows: false,
      dots: true,
    }),
    [],
  );

  const slideHeight = nodeRef.current && nodeRef.current.clientHeight;

  return (
    <div
      ref={nodeRef}
      className={cx(
        'block align imagecards-block imagecards-carousel imagecards-videocarousel',
        {
          center: !Boolean(data.align),
        },
        data.align,
      )}
    >
      <BodyClass className="has-video-carousel" />
      <div
        className={cx({
          'full-width': data.align === 'full',
        })}
      >
        <div className="slider-wrapper">
          {cards.length && slideHeight ? (
            <Slider
              {...settings}
              slideHeight={slideHeight}
              ref={sliderRef}
              listHeight="100vh"
            >
              {cards.map((card, i) => (
                <VideoSlide
                  card={card}
                  key={i}
                  image_scale={image_scale}
                  height={slideHeight}
                />
              ))}
            </Slider>
          ) : (
            <Message>No image cards</Message>
          )}
        </div>
      </div>
    </div>
  );
};

export default VideoCarousel;

export const VideoCardSchema = (args) => {
  return {
    title: 'Video Card',
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['title', 'videoUrl', 'linkHref', 'linkTitle', 'attachedimage'],
      },
    ],

    properties: {
      title: {
        type: 'string',
        title: 'Message',
      },
      videoUrl: {
        widget: 'text',
        title: 'Video URL',
      },
      linkTitle: {
        title: 'Button title',
      },
      linkHref: {
        title: 'Call to action',
        widget: 'object_browser',
        mode: 'link',
        selectedItemAttrs: ['Title', 'Description'],
        allowExternals: true,
      },
      attachedimage: {
        widget: 'attachedimage',
        title: 'Preview image',
      },
    },

    required: ['attachedimage'],
  };
};
