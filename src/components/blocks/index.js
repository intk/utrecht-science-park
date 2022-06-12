// import installImageBlock from './Image';
import installFactsBlock from './Facts';

const installImageBlock = (config) => config;

const installBlocks = (config) => {
  return installImageBlock(installFactsBlock(config));
};

export default installBlocks;
