import downloadSVG from '@plone/volto/icons/download.svg';

import FactsView from './Facts/FactsView';
import FactsEdit from './Facts/FactsEdit';

const installBlocks = (config) => {
  config.blocks.blocksConfig.facts = {
    id: 'facts',
    title: 'Facts',
    icon: downloadSVG,
    group: 'common',
    view: FactsView,
    edit: FactsEdit,
    restricted: false,
    mostUsed: false,
    sidebarTab: 1,
    security: {
      addPermission: [],
      view: [],
    },
  };

  return config;
};

export default installBlocks;
