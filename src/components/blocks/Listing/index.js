import AgendaListingTemplate from './AgendaListing';
import ListingsBlockTemplate from './ListingTemplate';
import SliderListingBlockTemplate from './SliderListing';

export default (config) => {
  config.blocks.blocksConfig.listing.schemaEnhancer = ({ schema }) => {
    schema.properties.headline = {
      title: 'Headline',
    };
    schema.properties = {
      ...schema.properties,
      headline: {
        title: 'Headline',
      },
      linkTitle: {
        title: 'Button title',
      },
      linkHref: {
        title: 'Call to action',
        widget: 'object_browser',
        mode: 'link',
        selectedItemAttrs: ['Title', 'Description'],
        allowExternals: true,
      },
    };

    schema.fieldsets[0].fields.splice(
      2,
      0,
      'headline',
      'linkHref',
      'linkTitle',
    );
    return schema;
  };

  config.blocks.blocksConfig.listing.variations = [
    ...config.blocks.blocksConfig.listing.variations,

    {
      id: 'agenda',
      isDefault: false,
      title: 'Agenda Listing',
      template: AgendaListingTemplate,
    },
    {
      id: 'listings',
      isDefault: false,
      title: 'Multiple Listings',
      template: ListingsBlockTemplate,
    },
    {
      id: 'slider_listing',
      isDefault: false,
      title: 'Slider (listing)',
      template: SliderListingBlockTemplate,
    },
  ];

  // const addHeadline = (WrappedComponent) => (props) => {
  //   return props.data?.headline ? (
  //     <div className="headline-with-listing">
  //       <h5>{props.data.headline}</h5>
  //       <WrappedComponent {...props} />
  //     </div>
  //   ) : (
  //     <WrappedComponent {...props} />
  //   );
  // };
  // const { view } = config.blocks.blocksConfig.listing;
  // config.blocks.blocksConfig.listing.view = addHeadline(view);

  return config;
};

// {
//   id: 'testimonials',
//   isDefault: false,
//   title: 'Testimonials',
//   template: TestimonialsListingBlockTemplate,
// },
// {
//   id: 'listings_two_columns',
//   isDefault: false,
//   title: 'Listings (Two columns)',
//   template: ListingsBlockTemplateTwoColumns,
// },
// {
//   id: 'listings_squares',
//   isDefault: false,
//   title: 'Listings (Squares)',
//   template: ListingsBlockSquaresTemplate,
// },
// {
//   id: 'listings_four_squares',
//   isDefault: false,
//   title: 'Listings (Four squares)',
//   template: ListingsBlockFourSquaresTemplate,
// },
// {
//   id: 'buttons',
//   isDefault: false,
//   title: 'Buttons',
//   template: ButtonsBlockTemplate,
// },
// {
//   id: 'slider',
//   isDefault: false,
//   title: 'Slider (ronded)',
//   template: SliderBlockTemplate,
// },
// {
//   id: 'slider_header',
//   isDefault: false,
//   title: 'Slider (Header)',
//   template: HeaderCarouselTemplate,
// },
// end museum variations

// {
//   id: 'simpleListing',
//   title: 'Simple listing',
//   template: SimpleListing,
//   schemaEnhancer: simpleListingSchemaEnhancer,
// },
// {
//   id: 'cardListing',
//   title: 'Card listing',
//   template: CardListing,
// },
// {
//   id: 'miniCardListing',
//   title: 'Mini card listing',
//   template: MiniCardListing,
//   schemaEnhancer: miniCardListingSchemaEnhancer,
// },
// {
//   id: 'horizontalCarousel',
//   title: 'Horizontal cards carousel',
//   template: HorizontalCarousel,
//   schemaEnhancer: horizontalCarouselSchemaEnhancer,
// },
// {
//   id: 'eventListing',
//   title: 'Event Listing',
//   template: EventListing,
// },
// {
//   id: 'carouselSpotlight',
//   title: 'Carousel spotlight',
//   template: CarouselSpotlight,
//   schemaEnhancer: carouselSpotlightSchemaEnhancer,
// },
// {
//   id: 'successStorySummary',
//   title: 'Success Story Summary',
//   template: SummaryTemplate,
// },
// {
//   id: 'detailedSummary',
//   title: 'Detailed Summary',
//   template: DetailedSummary,
// },
// {
//   id: 'newsListingStatic',
//   title: 'NewsListingStatic',
//   template: NewsListingStatic,
// },
// {
//   id: 'resourcesSummary',
//   title: 'Resources Summary',
//   template: ResourcesSummary,
// },

// import ResourcesSummary from './ResourcesTemplate';
// import CardListing from './CardListing';
// import EventListing from './EventListing';
// import SimpleListing, { simpleListingSchemaEnhancer } from './SimpleListing';
// import MiniCardListing, { miniCardListingSchemaEnhancer } from './MiniCard';
// import CarouselSpotlight, {
//   carouselSpotlightSchemaEnhancer,
// } from './CarouselSpotlight';
// import HorizontalCarousel, {
//   horizontalCarouselSchemaEnhancer,
// } from './HorizontalCarousel';
// import SummaryTemplate from './SummaryTemplate';
// import DetailedSummary from './DetailedSummary';
// import TestimonialsListingBlockTemplate from './TestimonialsTemplate';
// import SliderBlockTemplate from './SliderTemplate';
// import HeaderCarouselTemplate from './HeaderCarousel';
// import ListingsBlockTemplateTwoColumns from './ListingTemplateTwoColumns';
// import ListingsBlockSquaresTemplate from './ListingTemplateSquares';
// import ListingsBlockFourSquaresTemplate from './ListingTemplateFourSquares';
// import ButtonsBlockTemplate from './ButtonsTemplate';
// import NewsListingStatic from './NewsListingStatic';
