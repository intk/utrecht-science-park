import React from 'react';
import { Container } from 'semantic-ui-react';
import { When } from '@plone/volto/components/theme/View/EventDatesInfo';

function HeroSection(props) {
  const { image_url, content } = props;

  const content_title = content?.title;
  const content_description = content?.description;

  return (
    <div className="herosection">
      <div className="herosection-content-wrapper">
        {image_url ? (
          <div
            className="herosection-content-image document-image"
            style={{
              backgroundImage: `url(${image_url})`,
            }}
          />
        ) : (
          <div className="herosection-missing-image"></div>
        )}
      </div>
      <Container>
        <h1 className="content-title">{content_title}</h1>
        {!!content?.start && <When start={content.start} end={content.end} />}
        {content_description && (
          <p className={'content-description'}>{content_description}</p>
        )}
      </Container>
    </div>
  );
}

// HeroSection.displayName = 'HeroSection';
export default HeroSection;
