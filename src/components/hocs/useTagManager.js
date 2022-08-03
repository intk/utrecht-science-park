import React from 'react';
import TagManager from 'react-gtm-module';
import config from '@plone/volto/registry';

const useTagManager = ({ gtmId }) => {
  React.useEffect(() => {
    TagManager.initialize({ gtmId });
  }, [gtmId]);
};

export const GTMTracker = () => {
  useTagManager({ gtmId: config.settings.gtmId });
  return null;
};

export default useTagManager;
