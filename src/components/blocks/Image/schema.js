// import { flattenToAppURL } from '@plone/volto/helpers';
//
// import clearSVG from '@plone/volto/icons/clear.svg';
// import navTreeSVG from '@plone/volto/icons/nav.svg';

const ImageSchema = ({ schema, formData, intl }) => {
  const showAlign = ['s', 'm'].includes(formData.size);

  // remove the align field, we have a fixed policy of image behavior
  schema.fieldsets[0].fields = [
    ...schema.fieldsets[0].fields.filter((n) =>
      n !== 'align' ? true : showAlign,
    ),
    'source',
    'sourceHref',
    'imageCaption',
  ];
  // schema.properties.align.description =
  //   'Available only when the size is set to Small';

  schema.properties = {
    ...schema.properties,
    source: {
      title: 'Image source',
      description: 'Write here the source/copyright of this image',
    },
    sourceHref: {
      title: 'Source website',
      widget: 'url',
    },
    imageCaption: {
      type: 'richtext',
      title: 'Image caption',
      description: 'The image caption will be shown under the image',
    },
  };

  return schema;

  // return {
  //   title: 'Image',
  //   fieldsets: [
  //     {
  //       id: 'default',
  //       title: 'Default',
  //       fields: ['source', 'sourceHref', 'imageCaption'],
  //     },
  //   ],
  //   properties: {
  //     source: {
  //       title: 'Image source',
  //       description: 'Write here the source/copyright of this image',
  //     },
  //     // sourceHref: {
  //     //   title: 'Source website',
  //     //   icon: data.sourceHref ? clearSVG : navTreeSVG,
  //     //   iconAction: data.sourceHref
  //     //     ? () => {
  //     //         onChangeBlock(block, {
  //     //           ...data,
  //     //           sourceHref: '',
  //     //           title: '',
  //     //           description: '',
  //     //           preview_image: '',
  //     //         });
  //     //       }
  //     //     : () => openObjectBrowser({ mode: 'link' }),
  //     //   value: url && flattenToAppURL(url),
  //     // },
  //     imageCaption: {
  //       type: 'richtext',
  //       title: 'Image caption',
  //       description: 'The image caption will be shown under the image',
  //     },
  //   },
  //   required: [],
  // };
};

export default ImageSchema;
