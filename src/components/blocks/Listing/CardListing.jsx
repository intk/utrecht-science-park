import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Card } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';

const CardListing = ({ items = [], limit = 10 }) => {
  const hasItems = items && items.length;
  limit = parseInt(limit);

  return !hasItems ? (
    'No results'
  ) : (
    <div className="cardListing">
      {items.slice(0, limit).map((item, k) => (
        <Card key={k}>
          <Card.Content>
            <Card.Header>
              <UniversalLink href={flattenToAppURL(item['@id'])}>
                {item.title}
              </UniversalLink>
            </Card.Header>
            <Card.Description>{item.description}</Card.Description>
          </Card.Content>
          <Card.Content extra>
            <UniversalLink href={flattenToAppURL(item['@id'])}>
              Read more
            </UniversalLink>
          </Card.Content>
        </Card>
      ))}
    </div>
  );
};

export default CardListing;
