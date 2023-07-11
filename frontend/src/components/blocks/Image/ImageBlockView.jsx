import React from 'react';
import { ConditionalLink } from '@plone/volto/components';
import cx from 'classnames';
import { flattenToAppURL, isInternalURL } from '@plone/volto/helpers';
import { Link } from 'react-router-dom';

const Source = ({ source = '', sourceHref }) => (
  <div className="image-source">
    <ConditionalLink condition={sourceHref} to={sourceHref}>
      {source}
    </ConditionalLink>
  </div>
);

const sizes = {
  l: 'huge',
  m: 'huge',
  s: 'preview',
  fallback: 'huge',
};

//                      if (data.size === 'l')
//                        return `${flattenToAppURL(
//                          data.url,
//                        )}/@@images/image/large`;
//                      if (data.size === 'm')
//                        return `${flattenToAppURL(
//                          data.url,
//                        )}/@@images/image/preview`;
//                      if (data.size === 's')
//                        return `${flattenToAppURL(
//                          data.url,
//                        )}/@@images/image/mini`;
//                      return `${flattenToAppURL(
//                        data.url,
//                      )}/@@images/image/huge`;
//                    }

const Image = ({ data }) => {
  const { href } = data;
  const url = href?.[0] ? href[0]?.['@id'] : data.sourceHref;
  const { source, sourceHref, imageCaption } = data;
  // const showAlign = data.size === 's';

  const image = (
    <div
      className={cx('img-wrapper', {
        'full-width': data.align === 'full',
        large: data.size === 'l',
        medium: data.size === 'm',
        small: data.size === 's',
      })}
    >
      <img
        src={
          isInternalURL(data.url)
            ? // Backwards compat in the case that the block is storing the full server URL
              (() =>
                `${flattenToAppURL(data.url)}/@@images/image/${
                  sizes[data.size || 'fallback']
                }`)()
            : data.url
        }
        alt={data.alt || ''}
        loading="lazy"
      />
      {source && <Source source={source} sourceHref={sourceHref} />}
      {imageCaption && <span className="image-caption">{imageCaption}</span>}
    </div>
  );

  if (url) {
    if (!isInternalURL(url)) {
      return (
        <a target={data.openLinkInNewTab ? '_blank' : null} href={url}>
          {image}
        </a>
      );
    } else {
      return (
        <Link
          to={flattenToAppURL(url)}
          target={data.openLinkInNewTab ? '_blank' : null}
        >
          {image}
        </Link>
      );
    }
  } else {
    return image;
  }
};

const ViewImage = (props) => {
  const { data = {}, detached } = props;

  // className={cx('block image align', {
  //   center: !showAlign,
  //   detached,
  //   [data.align]: showAlign,
  // })}

  return (
    <p
      className={cx(
        'block image align',
        {
          center: !Boolean(data.align),
          detached,
        },
        data.align,
      )}
    >
      {!!data.url && <Image {...props} />}
    </p>
  );
};

export default (props) => {
  const { data = {} } = props;
  return <ViewImage {...props} data={data} />;
};
