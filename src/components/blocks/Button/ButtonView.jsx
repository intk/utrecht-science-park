import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { isInternalURL } from '@plone/volto/helpers/Url/Url';
import { ConditionalLink, UniversalLink } from '@plone/volto/components';

const ButtonView = ({ data, mode = 'view' }) => {
  let href = data.linkHref?.[0]?.['@id'] || '';
  const isEditMode = mode === 'edit';

  return isInternalURL(href) ? (
    <ConditionalLink
      to={flattenToAppURL(href)}
      condition={!isEditMode}
      className="ui button btn-block"
    >
      {data.linkTitle || href}
    </ConditionalLink>
  ) : href ? (
    <UniversalLink href={href} className="ui button btn-block">
      {data.linkTitle || href}
    </UniversalLink>
  ) : isEditMode ? (
    'Button block'
  ) : null;
};
export default ButtonView;
// {/* <Button as={}></Button> */}
