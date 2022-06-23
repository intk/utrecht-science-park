import React from 'react';
import PropTypes from 'prop-types';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Grid, Image, Segment, Icon } from 'semantic-ui-react';
import { Link } from 'react-router-dom';
import SharingButtons from './SharingButtons';
import { FormattedDate } from '@package/components';
import {
  When,
  Recurrence,
} from '@plone/volto/components/theme/View/EventDatesInfo';

const ListingTemplate = ({ items, linkTitle, linkHref, isEditMode }) => {
  return (
    <>
      <Grid stackable columns={2} className="newsListingStatic two-columns">
        {items.map((item) => (
          <Grid.Column
            mobile={12}
            tablet={6}
            computer={4}
            className="listing-column"
          >
            <Segment basic className="listing-item-content">
              <h2>
                <Link to={flattenToAppURL(item['@id'])} title={item.title}>
                  {item.title ? item.title : item.id}
                </Link>
              </h2>
              <FormattedDate isoDate={item.effective} format="DD" />
              {['Event'].includes(item['@type']) ? (
                <When
                  start={item.start}
                  end={item.end}
                  whole_day={true}
                  open_end={item.open_end}
                />
              ) : (
                ''
              )}
              {item.image_field && (
                <Link to={flattenToAppURL(item['@id'])}>
                  <Image
                    alt={item.title}
                    src={flattenToAppURL(
                      `${item['@id']}/@@images/${item.image_field}/teaser`,
                    )}
                    loading="lazy"
                  />

                  {item.youtube_id && (
                    <Icon name="play" size="huge" color="white" />
                  )}
                </Link>
              )}
            </Segment>
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
