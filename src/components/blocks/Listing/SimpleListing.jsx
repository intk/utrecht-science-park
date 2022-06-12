import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { UniversalLink } from '@plone/volto/components';

export const SimpleListingSchema = ({ formData, schema, intl }) => {
  return {
    fieldsets: [
      {
        id: 'simpleListing',
        title: 'Simple listing Settings',
        fields: ['headline'],
      },
    ],
    properties: {
      headline: {
        title: 'Block headline',
      },
    },
  };
};

export const simpleListingSchemaEnhancer = ({ formData, schema, intl }) => {
  const Custom = SimpleListingSchema({ formData, schema, intl });
  return {
    ...schema,
    ...Custom,
    properties: { ...schema.properties, ...Custom.properties },
    fieldsets: [
      // { id: 'empty', fields: [] },
      ...schema.fieldsets,
      ...Custom.fieldsets,
    ],
  };
};

const SimpleListing = ({ items = [], limit = 10, headline }) => {
  const hasItems = items && items.length;
  limit = parseInt(limit);

  return !hasItems ? (
    'No results'
  ) : (
    <div className="simpleListing">
      {headline ? <h4>{headline}</h4> : ''}
      {items.slice(0, limit).map((item, k) => (
        <div className="simpleListingItem" key={k}>
          <UniversalLink href={flattenToAppURL(item['@id'])}>
            {item.title}
          </UniversalLink>
        </div>
      ))}
    </div>
  );
};

export default SimpleListing;
