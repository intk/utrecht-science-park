import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Placeholder, Image } from 'semantic-ui-react';
import cx from 'classnames';

const empty =
  'data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==';

export default function PreviewImage({
  item,
  size = 'medium',
  showFallback = true,
}) {
  const url = flattenToAppURL(
    `${item['@id']}/@@images/${item.image_field}/large`,
  );
  return (
    <>
      {item.image_field ? (
        <Image
          src={empty}
          style={{ backgroundImage: `url("${url}")` }}
          size={size}
          alt={item.title}
          className={cx('preview-image', size)}
        />
      ) : showFallback ? (
        <Placeholder>
          <Placeholder.Image square></Placeholder.Image>
        </Placeholder>
      ) : (
        ''
      )}
    </>
  );
}
