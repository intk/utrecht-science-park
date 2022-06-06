import React from 'react';
import { Container } from 'semantic-ui-react';

function HeroSection(props) {
  const { image_url, content_description, content_title } = props;
  return (
    <>
      {image_url && (
        <div className="herosection">
          <div className="herosection-content-wrapper">
            <div
              className="herosection-content-image document-image"
              style={{
                backgroundImage: `url(${image_url})`,
              }}
            />
          </div>
          <Container>
            <h1 className="content-title">{content_title}</h1>
            {content_description && (
              <p className={'content-description'}>{content_description}</p>
            )}
          </Container>
        </div>
      )}
    </>
  );
}

// HeroSection.displayName = 'HeroSection';
export default HeroSection;
