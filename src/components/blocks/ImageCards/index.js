import ImageCarousel from './Carousel';
import TitleCards from './TitleCards';

export default function install(config) {
  config.blocks.blocksConfig.imagecards.blockRenderers = {
    ...config.blocks.blocksConfig.imagecards.blockRenderers,
    imageCarousel: {
      title: 'Image carousel',
      schema: null,
      view: ImageCarousel,
      schemaExtender: ImageCarousel.schemaExtender,
    },
    titleCards: {
      title: 'Title Cards',
      schema: null,
      view: TitleCards,
      schemaExtender: TitleCards.schemaExtender,
    },
  };

  return config;
}
