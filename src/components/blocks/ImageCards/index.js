import ImageCarousel from './Carousel';
import TitleCards from './TitleCards';
import VideoCarousel, { VideoCardSchema } from './VideoCarousel';

export default function install(config) {
  config.blocks.blocksConfig.imagecards.defaultRendererName = 'imageCards';
  config.blocks.blocksConfig.imagecards.blockRenderers = {
    ...config.blocks.blocksConfig.imagecards.blockRenderers,
    titleCards: {
      title: 'Title Cards',
      schema: null,
      view: TitleCards,
      schemaExtender: TitleCards.schemaExtender,
    },
    imageCards: {
      title: 'Logo Cards',
      schema: null,
      view: ImageCarousel,
      schemaExtender: ImageCarousel.schemaExtender,
    },
    imageCarousel: {
      title: 'Image Carousel',
      schema: null,
      view: ImageCarousel,
      schemaExtender: ImageCarousel.schemaExtender,
    },
    videoCarousel: {
      title: 'Video Carousel',
      view: VideoCarousel,
      schema: VideoCardSchema,
      // schemaExtender: VideoCarousel.schemaExtender,
    },
  };

  delete config.blocks.blocksConfig.imagecards.blockRenderers.carousel;
  delete config.blocks.blocksConfig.imagecards.blockRenderers.discreetCarousel;
  delete config.blocks.blocksConfig.imagecards.blockRenderers.round_tiled;

  return config;
}
