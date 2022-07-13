import React from 'react';
import { Container } from 'semantic-ui-react'; // Segment,
import { BodyClass } from '@plone/volto/helpers';
// import ListingTemplate from '@package/components/blocks/Listing/ListingTemplate';
import ListingBody from '@plone/volto/components/manage/Blocks/Listing/ListingBody';

const ListingView = ({ content, location: { pathname } }) => {
  return (
    <Container id="page-folder">
      <BodyClass className="multiple-content-view" />
      <section id="content-core">
        <div className="listings">
          <ListingBody properties={content} data={{}} path={pathname} />
        </div>
      </section>
    </Container>
  );
};

export default ListingView;
