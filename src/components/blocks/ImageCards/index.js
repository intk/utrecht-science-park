import ImageCarousel from './Carousel';

export default function install(config) {
  config.blocks.blocksConfig.imagecards.blockRenderers = {
    // ...config.blocks.blocksConfig.imagecards.blockRenderers,
    imageCarousel: {
      title: 'Image carousel',
      schema: null,
      view: ImageCarousel,
      schemaExtender: ImageCarousel.schemaExtender,
    },
  };
  return config;
}
