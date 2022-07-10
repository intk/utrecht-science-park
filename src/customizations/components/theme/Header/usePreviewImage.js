import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { flattenToAppURL } from '@plone/volto/helpers';
import { getContent } from '@plone/volto/actions';

const parent = (path) => {
  if (!path) return;

  const bits = path.split('/');
  if (bits.length < 2) return;

  const parentBits = bits.slice(0, bits.length - 1);
  return parentBits.join('/');
};

const usePreviewImage = (pathname) => {
  const dispatch = useDispatch();
  const contentData = useSelector((state) => state.content.data);
  const subrequest = useSelector(
    (state) => state.content.subrequests?.preview_image_request,
  );
  const preview_image =
    contentData?.preview_image || subrequest?.data?.preview_image;

  // console.log('subrequest', subrequest);

  const parentPath = parent(
    subrequest?.data
      ? flattenToAppURL(subrequest.data['@id'])
      : flattenToAppURL(contentData?.['@id']),
  );

  // console.log(preview_image, parentPath);

  React.useEffect(() => {
    if (!preview_image && parentPath) {
      dispatch(getContent(parentPath, null, 'preview_image_request'));
    }
  }, [preview_image, parentPath, dispatch]);
  // previewImage: state?.content?.data?.preview_image,

  return preview_image;
};

export default usePreviewImage;
