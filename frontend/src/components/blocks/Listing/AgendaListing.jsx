import React from 'react';
import { PreviewImage, UniversalLink } from '@plone/volto/components';
import { ListingBlockHeader, FormattedDate } from '@package/components';
import './less/agenda-listing.less';

const SecondaryItem = ({ item }) => {
  return (
    <div className="secondary-item">
      <div className="inner">
        <UniversalLink item={item}>
          {!!item.start && <FormattedDate isoDate={item.start} format="long" />}
          <h3>{item.title}</h3>
          {/* <strong>{item.description}</strong> */}
        </UniversalLink>
      </div>
    </div>
  );
};

const PrimaryItem = ({ item }) => {
  return (
    <div className="primary-item">
      <div className="primary-item-header">
        <UniversalLink item={item}>
          <div className="date">
            {!!item.start && (
              <FormattedDate isoDate={item.start} format="long" />
            )}
          </div>
          <h3>{item.title}</h3>
          {/* <strong>{item.description}</strong> */}
        </UniversalLink>
      </div>

      <div className="image-container">
        <PreviewImage item={item} size="large" />
      </div>
    </div>
  );
};

const AgendaListingTemplate = (data) => {
  const { items } = data;
  const [primaryItem, ...secondaryItems] = items;
  return (
    <div className="agenda-listing">
      <ListingBlockHeader data={data} />
      <div className="agenda-listing-content">
        <div className="column-one">
          <PrimaryItem item={primaryItem} />
        </div>
        <div className="column-two">
          {secondaryItems.map((item, i) => (
            <SecondaryItem item={item} key={i} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default AgendaListingTemplate;
