import React from 'react';
import PropTypes from 'prop-types';

import { ConditionalLink } from '@plone/volto/components';
import { flattenToAppURL } from '@plone/volto/helpers';
import { isInternalURL } from '@plone/volto/helpers/Url/Url';
import { UniversalLink } from '@plone/volto/components';

import { PreviewImage, FormattedDate } from '@package/components';

import { Grid, Button } from 'semantic-ui-react';

const SummaryTemplate = ({ items, linkTitle, linkHref, isEditMode }) => {
  let link = null;
  let href = linkHref?.[0]?.['@id'] || '';

  if (isInternalURL(href)) {
    link = (
      <ConditionalLink to={flattenToAppURL(href)} condition={!isEditMode}>
        {linkTitle || href}
      </ConditionalLink>
    );
  } else if (href) {
    link = <UniversalLink href={href}>{linkTitle || href}</UniversalLink>;
  }

  return (
    <>
      <div className="items news-summary-template">
        {items.map((item) => (
          <div className="listing-item" key={item['@id']}>
            <ConditionalLink item={item} condition={!isEditMode}>
              <Grid stackable>
                <Grid.Column width={2}>
                  <PreviewImage item={item} />
                </Grid.Column>
                <Grid.Column width={10}>
                  <div className="listing-body">
                    <div className="newsitem-meta">
                      <FormattedDate isoDate={item.effective} format="DD" />
                      <div className="us_state">
                        {false && item.us_state ? item.us_state.join(', ') : ''}
                      </div>
                    </div>
                    <h3>{item.title ? item.title : item.id}</h3>
                    <p>{item.description}</p>
                  </div>
                  <div className="extra-footer">
                    <Button
                      compact
                      secondary
                      className="news"
                      as={UniversalLink}
                      href={flattenToAppURL(item['@id'])}
                    >
                      Read more
                    </Button>
                  </div>
                </Grid.Column>
              </Grid>
            </ConditionalLink>
          </div>
        ))}
      </div>

      {link && <div className="footer">{link}</div>}
    </>
  );
};

SummaryTemplate.propTypes = {
  items: PropTypes.arrayOf(PropTypes.any).isRequired,
  linkMore: PropTypes.any,
  isEditMode: PropTypes.bool,
};

export default SummaryTemplate;
