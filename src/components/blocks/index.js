import installImageBlock from './Image';
import installFactsBlock from './Facts';
import installListingBlock from './Listing';
import installQuoteBlock from './Quote';
import { compose } from 'redux';

const installBlocks = (config) => {
  return compose(
    installListingBlock,
    installImageBlock,
    installFactsBlock,
    installQuoteBlock,
  )(config);
};

export default installBlocks;
