import React from 'react';
import loadable from '@loadable/component';
import { Message } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';
// import readySVG from '@plone/volto/icons/ready.svg';
import VideoBody from '@plone/volto/components/manage/Blocks/Video/Body';

import cx from 'classnames';

import 'slick-carousel/slick/slick.css';
import './less/video-carousel.less';

import { getPath } from './utils';

import { BodyClass } from '@plone/volto/helpers';

const Slider = loadable(() => import('react-slick'));

const VideoSlide = ({ card, image_scale }) => {
  return (
    <div className="slider-slide">
      <VideoBody
        data={{
          url: card.videoUrl,
          preview_image: getPath(card.attachedimage),
        }}
      />

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
      adaptiveHeight: true,
      vertical: false,
      lazyLoad: 'ondemand',
      arrows: false,
      dots: true,
    }),
    [],
  );

  return (
    <div
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
          {cards.length ? (
            <Slider {...settings} ref={sliderRef} listHeight="100vh">
              {cards.map((card, i) => (
                <VideoSlide card={card} key={i} image_scale={image_scale} />
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
