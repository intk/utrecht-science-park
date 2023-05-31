import { flattenToAppURL } from '@plone/volto/helpers';

import clearSVG from '@plone/volto/icons/clear.svg';
import navTreeSVG from '@plone/volto/icons/nav.svg';

const ImageSchema = (props) => {
  const { block, data = {}, onChangeBlock, openObjectBrowser } = props;
  const url = data?.sourceHref?.[0]
    ? data?.sourceHref?.[0]?.['@id']
    : data.sourceHref;

  return {
    title: 'Image',
    fieldsets: [
      {
        id: 'default',
        title: 'Default',
        fields: ['source', 'sourceHref', 'imageCaption'],
      },
    ],
    properties: {
      source: {
        title: 'Image source',
        description: 'Write here the source/copyright of this image',
      },
      sourceHref: {
        title: 'Source website',
        icon: data.sourceHref ? clearSVG : navTreeSVG,
        iconAction: data.sourceHref
          ? () => {
              onChangeBlock(block, {
                ...data,
                sourceHref: '',
                title: '',
                description: '',
                preview_image: '',
              });
            }
          : () => openObjectBrowser({ mode: 'link' }),
        value: url && flattenToAppURL(url),
      },
      imageCaption: {
        type: 'richtext',
        title: 'Image caption',
        description: 'The image caption will be shown under the image',
      },
    },
    required: [],
  };
};

export default ImageSchema;
