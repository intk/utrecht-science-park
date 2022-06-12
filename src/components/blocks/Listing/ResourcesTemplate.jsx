import React from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
import { Grid } from 'semantic-ui-react';

import { flattenToAppURL } from '@plone/volto/helpers';
import { isInternalURL } from '@plone/volto/helpers/Url/Url';
import { UniversalLink } from '@plone/volto/components';

import { PreviewImage } from '@package/components';

const LinkComponent = ({ href, children }) => {
  return isInternalURL(href) ? (
    <Link to={flattenToAppURL(href)}>{children}</Link>
  ) : (
    <UniversalLink href={href}>{children}</UniversalLink>
  );
};

const ResourcesTemplate = ({ items, linkTitle, linkHref, isEditMode }) => {
  return (
    <>
      <div className="items resources-summary-template">
        <Grid stackable>
          {items.map((item) => (
            <Grid.Column mobile={12} tablet={6} computer={4}>
              <div className="listing-item" key={item['@id']}>
                <LinkComponent href={item?.['@id'] || ''}>
                  <Grid.Column width={12}>
                    <PreviewImage item={item} showFallback={false} />
                  </Grid.Column>
                  <Grid.Column width={12}>
                    <div className="listing-body">
                      <div className="resource-item-meta">
                        <div className="us_state">{item.us_state}</div>
                      </div>
                      <h3>{item.title ? item.title : item.id}</h3>
                      <p>{item.description}</p>
                    </div>
                  </Grid.Column>
                </LinkComponent>
              </div>
            </Grid.Column>
          ))}
        </Grid>
      </div>
    </>
  );
};

ResourcesTemplate.propTypes = {
  items: PropTypes.arrayOf(PropTypes.any).isRequired,
  linkMore: PropTypes.any,
  isEditMode: PropTypes.bool,
};

export default ResourcesTemplate;
