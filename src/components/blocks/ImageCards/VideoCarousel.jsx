import React from 'react';
import loadable from '@loadable/component';
import { Message, Button } from 'semantic-ui-react';
import { Icon, UniversalLink } from '@plone/volto/components';
import { isInternalURL, flattenToAppURL } from '@plone/volto/helpers';
import YouTube from 'react-youtube';
import config from '@plone/volto/registry';

import playSVG from '@plone/volto/icons/play.svg';

import cx from 'classnames';

import 'slick-carousel/slick/slick.css';
import './less/video-carousel.less';

import { getPath } from './utils';

import { BodyClass } from '@plone/volto/helpers';

const VideoPlayer = ({ videoId, width, height }) => {
  const playerRef = React.useRef(null);

  React.useEffect(() => {
    if (playerRef.current) {
      playerRef.current.internalPlayer.playVideo();
    }
  }, [playerRef]);

  const onReady = (event) => {
    event.target.playVideo();
  };

  const opts = {
    height: height || '390',
    width: width || '640',
    playerVars: {
      autoplay: 1,
      mute: 1,
      origin: config.settings.apiPath,
      playsinline: 1,
      modestbranding: 1,
      controls: 0,
      enablejsapi: 1,
      rel: 0,
    },
  };

  return (
    <YouTube videoId={videoId} opts={opts} onReady={onReady} ref={playerRef} />
  );
};

export { VideoCardSchema } from './schema';

const Slider = loadable(() => import('react-slick'));

// <iframe src="https://player.vimeo.com/video/706175904?h=1c4118bf74" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
// <p><a href="https://vimeo.com/706175904">The Kites</a> from <a href="https://vimeo.com/user85705276">Seyed Payam Hosseini</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

const getEmbedUrl = (url) => {
  let videoId;

  if (url.match('vimeo')) {
    videoId = url.match(/^.*\.com\/(.*)/)[1];
    return {
      type: 'vimeo',
      videoId,
      url: [
        `//player.vimeo.com/video/${videoId}`,
        '?api=false',
        `&amp;dnt=1`,
        `&amp;loop=1`,
        `&amp;autopause=1`,
        `&amp;muted=1`,
        `&amp;background=1`,
        `&amp;autoplay=1`,
        '&amp;byline=false',
        '&amp;portrait=false',
        '&amp;title=false',
      ].join(''),
    };
  }
  videoId = url.match(/.be\//)
    ? url.match(/^.*\.be\/(.*)/)[1]
    : url.match(/^.*\?v=(.*)$/)[1];

  return {
    type: 'youtube',
    videoId,
    url: `https://www.youtube.com/embed/${videoId}?start=0&autoplay=1`,
  };
};

const VideoEmbed = ({ url, placeholder, height, width, sliderRef }) => {
  const autoplay = !placeholder; // if we don't have a placeholder, then we autoplay
  const [play, setIsPlay] = React.useState(autoplay);

  if (!url) return null;

  const embed = getEmbedUrl(url);

  return (
    <div className="video-responsive">
      {play ? (
        embed.type === 'youtube' ? (
          <VideoPlayer videoId={embed.videoId} width={width} height={height} />
        ) : (
          <iframe
            width={width}
            height={height}
            src={embed.url}
            frameBorder="0"
            allow="autoplay; fullscreen; picture-in-picture; encrypted-media; accelerometer; gyroscope; "
            allowFullScreen
            title="Embedded video"
          />
        )
      ) : (
        <div className="placeholder-image">
          <img src={placeholder} className="placeholder" alt="Placeholder" />
          <Button
            basic
            onClick={() => {
              sliderRef.current.slickPause();
              setIsPlay(true);
            }}
          >
            <Icon name={playSVG} size={`${height / 10}px`} color="white" />
          </Button>
        </div>
      )}
    </div>
  );
};

const VideoSlide = ({
  card,
  image_scale,
  height,
  sliderRef,
  slideIndex,
  slideCount,
}) => {
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
      <div className="slider-footer">
        <div className="video-slider-caption">
          <div className="slide-body">
            {card.linkHref?.[0] ? (
              <UniversalLink href={card.linkHref[0]['@id']}>
                <h2 className="slide-title">{card.title || ''}</h2>
              </UniversalLink>
            ) : (
              <h2 className="slide-title">{card.title || ''}</h2>
            )}
          </div>
          <div className="slide-button">
            {!!card.linkHref?.[0] && (
              <UniversalLink
                href={card.linkHref[0]['@id']}
                className="ui button"
              >
                {card.linkTitle || '...'}
              </UniversalLink>
            )}
          </div>
        </div>

        {slideCount > 1 ? (
          <Dots
            sliderRef={sliderRef}
            slideIndex={slideIndex}
            slideCount={slideCount}
          />
        ) : null}
      </div>
      <VideoEmbed {...embedSettings} sliderRef={sliderRef} />
    </div>
  );
};

const Dots = ({ sliderRef, settings, slideIndex, slideCount }) => {
  return (
    <div className="video-carousel-dots">
      <div className="inner">
        {new Array(slideCount).fill(null).map((_, k) => (
          <button
            className={cx({ 'slick-active': slideIndex === k })}
            key={k}
            onClick={(e) => {
              sliderRef.current && sliderRef.current.slickGoTo(k);
              e.preventDefault();
            }}
          >
            {slideIndex}
          </button>
        ))}
      </div>
    </div>
  );
};

const VideoCarousel = ({ data }) => {
  const sliderRef = React.useRef();
  const [slideHeight, setSlideHeight] = React.useState();
  const nodeRef = React.useRef();

  const { cards = [], image_scale = 'large' } = data;

  var settings = React.useMemo(
    () => ({
      // afterChange: (current) => setSlideIndex(current),
      fade: true,
      speed: 800,
      infinite: true,
      autoplay: true,
      pauseOnHover: true,
      autoplaySpeed: 5000,
      slidesToShow: 1,
      slidesToScroll: 1,
      adaptiveHeight: false,
      vertical: false,
      lazyLoad: 'ondemand',
      arrows: false,
      dots: false,
    }),
    [],
  );

  React.useEffect(() => {
    setSlideHeight(nodeRef.current && nodeRef.current.clientHeight);
  }, []);

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
          {cards.length ? (
            slideHeight ? (
              <>
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
                      sliderRef={sliderRef}
                      slideIndex={i}
                      slideCount={cards.length}
                    />
                  ))}
                </Slider>
              </>
            ) : (
              cards.map((card, i) => (
                <VideoSlide
                  card={card}
                  key={i}
                  image_scale={image_scale}
                  height={slideHeight}
                  sliderRef={sliderRef}
                  slideIndex={i}
                  slideCount={cards.length}
                />
              ))
            )
          ) : (
            <Message>No image cards</Message>
          )}
        </div>
      </div>
    </div>
  );
};

export default VideoCarousel;
