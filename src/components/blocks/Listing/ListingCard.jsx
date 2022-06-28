import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Image } from 'semantic-ui-react';
import { Link } from 'react-router-dom';

const Card = ({ item }) => (
  <section className="slider-card listing-card">
    <div className="image-container">
      <Link
        to={flattenToAppURL(item['@id'])}
        title={item.title}
        className="link-img-wrapper"
      >
        <Image
          alt={item.title}
          src={flattenToAppURL(
            `${item['@id']}/@@images/${item.image_field}/teaser`,
          )}
        />
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

export default Card;
