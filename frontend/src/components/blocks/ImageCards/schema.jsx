// See https://react-slick.neostack.com/docs/api
export const ImageCarouselSchema = ({ data, schema, intl }) => {
  return {
    fieldsets: [
      {
        id: 'imageCarouselSpotlight',
        title: 'Image Carousel Settings',
        fields: [
          'autoplay',
          'autoplaySpeed',
          'hideNavigationDots',
          'height',
          'itemsPerRow',
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
        defaultValue: 50,
      },
      hideNavigationDots: {
        type: 'boolean',
        title: 'Hide navigation dots',
      },
      itemsPerRow: {
        type: 'number',
        title: 'Items per row',
        defaultValue: 4,
      },
      height: {
        defaultValue: '25vh',
        title: (
          <a
            rel="noreferrer"
            target="_blank"
            href="https://developer.mozilla.org/en-US/docs/Web/CSS/height"
          >
            CSS height
          </a>
        ),
      },
    },
  };
};

export const TitleCardsSchema = ({ data, schema, intl }) => {
  return {
    fieldsets: [],
    properties: {
      linkHref: {
        title: 'Call to action Link',
        widget: 'object_browser',
        mode: 'link',
        selectedItemAttrs: ['Title', 'Description'],
        allowExternals: true,
      },
      linkTitle: {
        title: 'Link title',
      },
      imageSize: {
        title: 'Image size',
        choices: [
          ['small', 'Small'],
          ['bigger', 'Bigger'],
        ],
        default: 'small',
      },
    },
    required: [],
  };
};

export const VideoCardSchema = (args) => {
  return {
    title: 'Video Card',
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['title', 'videoUrl', 'linkHref', 'linkTitle', 'attachedimage'],
      },
    ],

    properties: {
      title: {
        type: 'string',
        title: 'Message',
      },
      videoUrl: {
        widget: 'text',
        title: 'Video URL',
        description: 'Youtube/Vimeo video URL',
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
      attachedimage: {
        widget: 'attachedimage',
        title: 'Preview image',
      },
    },

    required: ['attachedimage'],
  };
};
