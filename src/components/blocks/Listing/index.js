// import ResourcesSummary from './ResourcesTemplate';
import CardListing from './CardListing';
// import EventListing from './EventListing';
import SimpleListing, { simpleListingSchemaEnhancer } from './SimpleListing';
import MiniCardListing, { miniCardListingSchemaEnhancer } from './MiniCard';
import CarouselSpotlight, {
  carouselSpotlightSchemaEnhancer,
} from './CarouselSpotlight';
import HorizontalCarousel, {
  horizontalCarouselSchemaEnhancer,
} from './HorizontalCarousel';
import SummaryTemplate from './SummaryTemplate';
import DetailedSummary from './DetailedSummary';
// import NewsSummary from './NewsSummaryTemplate';

export default (config) => {
  config.blocks.blocksConfig.listing.schemaEnhancer = ({ schema }) => {
    schema.properties.headline = {
      title: 'Headline',
    };
    schema.fieldsets[0].fields.push('headline');
    return schema;
  };

  config.blocks.blocksConfig.listing.variations = [
    ...config.blocks.blocksConfig.listing.variations,
    {
      id: 'simpleListing',
      title: 'Simple listing',
      template: SimpleListing,
      schemaEnhancer: simpleListingSchemaEnhancer,
    },
    {
      id: 'cardListing',
      title: 'Card listing',
      template: CardListing,
    },
    {
      id: 'miniCardListing',
      title: 'Mini card listing',
      template: MiniCardListing,
      schemaEnhancer: miniCardListingSchemaEnhancer,
    },
    {
      id: 'horizontalCarousel',
      title: 'Horizontal cards carousel',
      template: HorizontalCarousel,
      schemaEnhancer: horizontalCarouselSchemaEnhancer,
    },
    // {
    //   id: 'eventListing',
    //   title: 'Event Listing',
    //   template: EventListing,
    // },
    {
      id: 'carouselSpotlight',
      title: 'Carousel spotlight',
      template: CarouselSpotlight,
      schemaEnhancer: carouselSpotlightSchemaEnhancer,
    },
    {
      id: 'successStorySummary',
      title: 'Success Story Summary',
      template: SummaryTemplate,
    },
    {
      id: 'detailedSummary',
      title: 'Detailed Summary',
      template: DetailedSummary,
    },
    // {
    //   id: 'newsSummary',
    //   title: 'News Summary',
    //   template: NewsSummary,
    // },
    // {
    //   id: 'resourcesSummary',
    //   title: 'Resources Summary',
    //   template: ResourcesSummary,
    // },
  ];

  const addHeadline = (WrappedComponent) => (props) => {
    return props.data?.headline ? (
      <div className="headline-with-listing">
        <h5>{props.data.headline}</h5>
        <WrappedComponent {...props} />
      </div>
    ) : (
      <WrappedComponent {...props} />
    );
  };

  const { view } = config.blocks.blocksConfig.listing;
  config.blocks.blocksConfig.listing.view = addHeadline(view);

  return config;
};