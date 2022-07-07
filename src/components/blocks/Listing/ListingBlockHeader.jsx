import { LinkMore } from '@plone/volto/components';

const ListingBlockHeader = ({ data }) => {
  const { title, headline, linkHref } = data;
  const head = title || headline;

  return head ? (
    <div className="listing-block-header">
      <h2>{head}</h2>
      {linkHref ? <LinkMore data={data} /> : ''}
    </div>
  ) : (
    ''
  );
};

export default ListingBlockHeader;
