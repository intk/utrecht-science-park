import React from 'react';
import { Container } from 'semantic-ui-react'; // Segment,
import { BodyClass } from '@plone/volto/helpers';
import ListingTemplate from '@package/components/blocks/Listing/ListingTemplate';

const ListingView = ({ content }) => (
  <Container id="page-folder">
    <BodyClass className="multiple-content-view" />
    <section id="content-core">
      <div className="listings">
        <ListingTemplate items={content.items} />
      </div>
    </section>
  </Container>
);

export default ListingView;
