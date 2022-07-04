import { LinkMore } from '@plone/volto/components';

const ListingBlockHeader = ({ data }) => {
  console.log('data', data);
  const { title, headline, linkHref } = data;
  const head = title || headline;

  return head ? (
    <div className="listing-block-header">
      <h1>{head}</h1>
      {linkHref ? <LinkMore data={data} /> : ''}
    </div>
  ) : (
    ''
  );
};

export default ListingBlockHeader;
