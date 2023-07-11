import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { isInternalURL } from '@plone/volto/helpers/Url/Url';
import { ConditionalLink, UniversalLink } from '@plone/volto/components';
import cx from 'classnames';

const ButtonView = ({ data, mode = 'view' }) => {
  let href = data.linkHref?.[0]?.['@id'] || '';
  const isEditMode = mode === 'edit';
  const classNames = cx('btn-block', data.btnStyle || 'primary');

  return isInternalURL(href) ? (
    isEditMode ? (
      <div className={classNames}>
        {data.linkTitle || href}
      </div>
    ) : (
      <div className={classNames}>
        <ConditionalLink to={flattenToAppURL(href)} condition={!isEditMode}>
          {data.linkTitle || href}
        </ConditionalLink>
      </div>
    )
  ) : href ? (
    <div className={classNames}>
      <UniversalLink href={href}>{data.linkTitle || href}</UniversalLink>
    </div>
  ) : isEditMode ? (
    <div className={classNames}>Button block</div>
  ) : null;
};
export default ButtonView;
