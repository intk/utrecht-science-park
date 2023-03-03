import React from 'react';
import PropTypes from 'prop-types';
import { Grid } from 'semantic-ui-react';
import { ListingBlockHeader } from '@package/components';

import Card from './ListingCard';

const ListingTemplate = (data) => {
  const { items, isEditMode } = data;
  return (
    <>
      {!isEditMode && <ListingBlockHeader data={data} />}
      <Grid stackable columns={2} className="listings two-columns">
        {items.map((item, i) => (
          <Grid.Column
            mobile={12}
            tablet={6}
            computer={4}
            className="listing-column"
          >
            <Card item={item} key={i} />
          </Grid.Column>
        ))}
      </Grid>
    </>
  );
};

ListingTemplate.propTypes = {
  items: PropTypes.arrayOf(PropTypes.any).isRequired,
  linkMore: PropTypes.any,
  isEditMode: PropTypes.bool,
};

export default ListingTemplate;
