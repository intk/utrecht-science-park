import React from 'react';
import {
  PreviewImage,
  FormattedDate,
  UniversalLink,
} from '@plone/volto/components';

import './less/agenda-listing.less';

const SecondaryItem = ({ item }) => {
  return (
    <div className="secondary-item">
      <UniversalLink item={item}>
        {!!item.start && <FormattedDate date={item.start} format="long" />}
        <h3>{item.title}</h3>
        <strong>{item.description}</strong>
      </UniversalLink>
    </div>
  );
};

const PrimaryItem = ({ item }) => {
  return (
    <div className="primary-item">
      <div className="primary-item-header">
        <UniversalLink item={item}>
          <div className="date">
            {!!item.start && <FormattedDate date={item.start} format="long" />}
          </div>
          <h3>{item.title}</h3>
          <strong>{item.description}</strong>
        </UniversalLink>
      </div>

      <PreviewImage item={item} size="large" />
    </div>
  );
};

const AgendaListingTemplate = ({
  items,
  linkTitle,
  linkHref,
  isEditMode,
  ...rest
}) => {
  const [primaryItem, ...secondaryItems] = items;
  return (
    <div className="agenda-listing">
      <div className="column-one">
        <PrimaryItem item={primaryItem} />
      </div>
      <div className="column-two">
        {secondaryItems.map((item, i) => (
          <SecondaryItem item={item} key={i} />
        ))}
      </div>
    </div>
  );
};

export default AgendaListingTemplate;
