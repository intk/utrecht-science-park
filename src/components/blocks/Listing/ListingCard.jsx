import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Image } from 'semantic-ui-react';
import { Link } from 'react-router-dom';
import { PreviewImage } from '@plone/volto/components';

//          <Image
//            alt={item.title}
//            src={flattenToAppURL(
//              `${item['@id']}/@@images/${image_field}/${size}`,
//            )}
//          />

const Card = ({ item }) => {
  const { image_field } = item;
  const size = 'teaser';
  return (
    <section className="slider-card listing-card">
      <div className="image-container">
        <Link
          to={flattenToAppURL(item['@id'])}
          title={item.title}
          className="link-img-wrapper"
        >
          {!!image_field && <PreviewImage item={item} size={size} />}
        </Link>
      </div>
      <div className="slide-details">
        <h4 className="title">
          <Link to={flattenToAppURL(item['@id'])} title={item.title}>
            {item.title}
          </Link>
        </h4>
      </div>
    </section>
  );
};

export default Card;
