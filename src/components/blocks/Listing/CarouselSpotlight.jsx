import React from 'react';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Grid, Button, Message, Placeholder } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';
import { ResponsiveContainer, PreviewImage } from '@package/components';

import loadable from '@loadable/component';

import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const Slider = loadable(() => import('react-slick'));

// See https://react-slick.neostack.com/docs/api
export const CarouselSpotlightSchema = ({ formData, schema, intl }) => {
  return {
    fieldsets: [
      {
        id: 'carouselSpotlight',
        title: 'Carousel Spotlight Settings',
        fields: [
          'autoplay',
          'autoplaySpeed',
          'hideNavigationDots',
          'showReadMore',
        ],
      },
    ],
    properties: {
      autoplay: {
        type: 'boolean',
        title: 'Autoplay',
      },
      autoplaySpeed: {
        type: 'number',
        title: 'Autoplay delay',
        defaultValue: 1000,
      },
      hideNavigationDots: {
        type: 'boolean',
        title: 'Hide navigation dots',
      },
      showReadMore: {
        type: 'boolean',
        title: 'Show read more button?',
        description: "A 'Read more' button will be displayed under each item",
      },
    },
  };
};

export const carouselSpotlightSchemaEnhancer = ({ formData, schema, intl }) => {
  const Custom = CarouselSpotlightSchema({ formData, schema, intl });
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

const shuffle = (arr) => arr.sort(() => (Math.random() > 0.5 ? 1 : -1));

const CarouselSpotlight = ({
  items = [],
  limit = 10,
  hideNavigationDots = false,
  isEditMode = false,
  autoplay = true,
  autoplaySpeed = 1000,
  showReadMore = false,
  ...rest
}) => {
  items = shuffle(items);
  const hasItems = items && items.length;
  limit = parseInt(limit);
  const visibleItems = items.slice(0, limit);

  const carouselSettings = {
    dots: limit > 1 && !hideNavigationDots,
    autoplay: limit > 1 && autoplay && !isEditMode,
    autoplaySpeed,
  };

  return !hasItems ? (
    <Message>No results</Message>
  ) : (
    <div className="carousel-spotlight">
      <ResponsiveContainer>
        {({ parentWidth }) => (
          <div style={{ width: `${parentWidth}px` }}>
            <Slider {...carouselSettings}>
              {visibleItems.map((item) => (
                <div className="carousel-spotlight-item" key={item['@id']}>
                  <Grid stackable>
                    <Grid.Column width={6}>
                      <PreviewImage item={item} size="medium" />
                    </Grid.Column>
                    <Grid.Column width={6} className="description">
                      <h5>
                        <UniversalLink href={flattenToAppURL(item['@id'])}>
                          {item.title}
                        </UniversalLink>
                      </h5>
                      {item.description ? (
                        <p>{item.description}</p>
                      ) : (
                        <Placeholder>
                          <Placeholder.Paragraph>
                            <Placeholder.Line />
                            <Placeholder.Line />
                            <Placeholder.Line />
                            <Placeholder.Line />
                          </Placeholder.Paragraph>
                        </Placeholder>
                      )}
                      {showReadMore && (
                        <div className="extra-footer">
                          <Button
                            compact
                            secondary
                            as={UniversalLink}
                            href={flattenToAppURL(item['@id'])}
                          >
                            Read more
                          </Button>
                        </div>
                      )}
                    </Grid.Column>
                  </Grid>
                </div>
              ))}
            </Slider>
          </div>
        )}
      </ResponsiveContainer>
    </div>
  );
};

export default CarouselSpotlight;
