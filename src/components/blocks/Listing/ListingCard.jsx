import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Link } from 'react-router-dom';
import { PreviewImage } from '@plone/volto/components';
import { When } from '@plone/volto/components/theme/View/EventDatesInfo';
import { FormattedDate } from '@package/components';

// see extras/listing.less for less

const Card = ({ item }) => {
  const { image_field } = item;
  const size = 'teaser';
  return (
    <section className="slider-card listing-card">
      <Link to={flattenToAppURL(item['@id'])} title={item.title}>
        <div className="card-details">
          <h4 className="title">{item.title}</h4>
        </div>
        <div className="image-container">
          <span className="link-img-wrapper">
            {!!image_field && <PreviewImage item={item} size={size} />}
          </span>
        </div>
      </Link>
    </section>
  );
};

const NewsItemCard = ({ item }) => {
  const { image_field } = item;
  const size = 'teaser';
  return (
    <section className="slider-card listing-card newsitem-card">
      <Link to={flattenToAppURL(item['@id'])} title={item.title}>
        <div className="card-details">
          <h4 className="title">{item.title}</h4>
          {!!item.effective && (
            <FormattedDate isoDate={item.effective} format="long" />
          )}
        </div>
        {!!image_field && (
          <div className="image-container">
            <span className="link-img-wrapper">
              <PreviewImage item={item} size={size} />
            </span>
          </div>
        )}
      </Link>
    </section>
  );
};

const EventCard = ({ item }) => {
  const { image_field } = item;
  const size = 'teaser';
  return (
    <section className="slider-card listing-card event-card">
      <Link to={flattenToAppURL(item['@id'])} title={item.title}>
        <div className="card-details">
          <h4 className="title">{item.title}</h4>
          <When
            start={item.start}
            end={item.end}
            whole_day={true}
            open_end={item.open_end}
          />
        </div>
        <div className="image-container">
          <span className="link-img-wrapper">
            {!!image_field && <PreviewImage item={item} size={size} />}
          </span>
        </div>
      </Link>
    </section>
  );
};

const cardTypes = {
  default: Card,
  'News Item': NewsItemCard,
  Event: EventCard,
};

const UniversalCard = ({ item }) => {
  const CardImpl = cardTypes[item['@type']] || cardTypes['default'];
  return <CardImpl item={item} />;
};

export default UniversalCard;
