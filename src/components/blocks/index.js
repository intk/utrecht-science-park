import installImageBlock from './Image';
import installFactsBlock from './Facts';
import installListingBlock from './Listing';
import { compose } from 'redux';

const installBlocks = (config) => {
  return compose(
    installListingBlock,
    installImageBlock,
    installFactsBlock,
  )(config);
};

export default installBlocks;
