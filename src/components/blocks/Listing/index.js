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

  return config;
};
