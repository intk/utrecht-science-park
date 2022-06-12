import React from 'react';
import PropTypes from 'prop-types';
import { ConditionalLink } from '@plone/volto/components';
import { flattenToAppURL } from '@plone/volto/helpers';

import { isInternalURL } from '@plone/volto/helpers/Url/Url';
import { Grid, Button } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';
import { PreviewImage } from '@package/components';

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
    link = <a href={href}>{linkTitle || href}</a>;
  }

  return (
    <>
      <div className="items success-story-summary-template">
        {items.map((item) => (
          <div className="listing-item" key={item['@id']}>
            <ConditionalLink item={item} condition={!isEditMode}>
              <Grid>
                <Grid.Column width={4}>
                  <PreviewImage item={item} />
                </Grid.Column>
                <Grid.Column width={8}>
                  <div className="listing-body">
                    <h3>{item.title ? item.title : item.id}</h3>
                    <p>{item.description}</p>
                  </div>
                  <div className="extra-footer">
                    <Button
                      compact
                      secondary
                      className="stories"
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
