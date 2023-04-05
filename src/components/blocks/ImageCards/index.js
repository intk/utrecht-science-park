import ImageCarousel from './Carousel';
import LogoCardsCarousel from './LogoCarousel';
import TitleCards from './TitleCards';
import Gallery from './Gallery';
import VideoCarousel, { VideoCardSchema } from './VideoCarousel';

export default function install(config) {
  config.blocks.blocksConfig.imagecards.defaultRendererName = 'imageCards';
  // config.blocks.blocksConfig.imagecards.tocEntry = (block, data) => {
  //   const title = data.title || data.headline;
  //   return title ? [1, title] : null;
  // };
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
      view: LogoCardsCarousel,
      schemaExtender: LogoCardsCarousel.schemaExtender,
    },
    gallery: {
      title: 'Gallery',
      schema: null,
      view: Gallery,
      schemaExtender: Gallery.schemaExtender,
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
