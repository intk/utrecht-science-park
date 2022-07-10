import installImageBlock from './Image';
import installFactsBlock from './Facts';
import installListingBlock from './Listing';
import installQuoteBlock from './Quote';
import installImageCards from './ImageCards';
import installButtonBlock from './Button';

import { compose } from 'redux';

const installBlocks = (config) => {
  return compose(
    installListingBlock,
    installImageBlock,
    installFactsBlock,
    installQuoteBlock,
    installImageCards,
    installButtonBlock,
  )(config);
};

export default installBlocks;
