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
  m: 'preview',
  s: 'mini',
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

const ViewImage = (props) => {
  const { data = {}, detached } = props;
  const { source, sourceHref, imageCaption } = data;

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
      {data.url && (
        <>
          {(() => {
            const image = (
              <img
                className={cx({
                  'full-width': data.align === 'full',
                  large: data.size === 'l',
                  medium: data.size === 'm',
                  small: data.size === 's',
                })}
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
            );
            if (data.href) {
              if (!isInternalURL(data.href)) {
                return (
                  <a
                    target={data.openLinkInNewTab ? '_blank' : null}
                    href={data.href}
                  >
                    {image}
                  </a>
                );
              } else {
                return (
                  <Link
                    to={flattenToAppURL(data.href)}
                    target={data.openLinkInNewTab ? '_blank' : null}
                  >
                    {image}
                  </Link>
                );
              }
            } else {
              return image;
            }
          })()}
        </>
      )}
      {source && <Source source={source} sourceHref={sourceHref} />}
      {imageCaption && <span className="image-caption">{imageCaption}</span>}
    </p>
  );
};

export default (props) => {
  const { data = {} } = props;
  return <ViewImage {...props} data={data} />;
};
