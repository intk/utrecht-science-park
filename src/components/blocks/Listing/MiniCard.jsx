import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Grid } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';
import { PreviewImage } from '@package/components';

const MiniCardListing = ({
  items = [],
  limit = 10,
  horizontal = false,
  hideDescription = false,
  querystring = {},
  nrColumns = 2,
  isEditMode = false,
  imageStyle = 'original',
}) => {
  const hasItems = items && items.length;
  limit = parseInt(limit);
  const visibleItems = items.slice(0, limit);
  const Link = 'a';

  return !hasItems ? (
    'No results'
  ) : (
    <div className="minicardListing">
      <Grid columns={horizontal ? nrColumns : 1} stretched stackable>
        {visibleItems.map((item, k) => (
          <Grid.Column className="minicard-listing-item" key={item['@id']}>
            <div className="item-header">
              <Grid>
                <Grid.Column width={12}>
                  <PreviewImage item={item} />
                </Grid.Column>
                <Grid.Column width={12}>
                  <h5>
                    {isEditMode ? (
                      <Link>{item.title}</Link>
                    ) : (
                      <UniversalLink href={flattenToAppURL(item['@id'])}>
                        {item.title}
                      </UniversalLink>
                    )}
                  </h5>
                </Grid.Column>
              </Grid>
            </div>
            {!hideDescription &&
              (item.description ? <p>{item.description}</p> : '')}
          </Grid.Column>
        ))}
      </Grid>
    </div>
  );
};

export const MiniCardSchema = ({ formData, schema, intl }) => {
  return {
    fieldsets: [
      {
        id: 'miniCard',
        title: 'MiniCard Settings',
        fields: ['horizontal', 'hideDescription', 'imageStyle'],
      },
    ],
    properties: {
      horizontal: {
        type: 'boolean',
        title: 'Horizontal?',
      },
      nrColumns: {
        type: 'number',
        defaultValue: 2,
      },
      hideDescription: {
        type: 'boolean',
        title: 'Hide description?',
      },
      imageStyle: {
        title: 'Image style',
        choices: [
          ['original', 'Keep original size'],
          ['cover', 'Cover style'],
        ],
      },
    },
  };
};

export const miniCardListingSchemaEnhancer = ({ formData, schema, intl }) => {
  const Custom = MiniCardSchema({ formData, schema, intl });
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
export default MiniCardListing;
