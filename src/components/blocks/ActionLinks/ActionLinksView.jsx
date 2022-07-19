import { UniversalLink } from '@plone/volto/components';

const ActionLinksView = (props) => {
  const { data = {}, mode = 'view' } = props;
  const { id, actions } = data;

  return (
    <>
      {mode === 'edit' ? <h5>Action links block {data.globalId}</h5> : ''}
      <ul className="action-links-block" id={id}>
        {actions?.map((action, i) => (
          <li key={i}>
            <UniversalLink item={action.linkHref?.[0] || {}}>
              {action.title}
            </UniversalLink>
          </li>
        ))}
      </ul>
      {(mode === 'edit') & !actions?.length ? (
        <div>No actions defined</div>
      ) : null}
    </>
  );
};

export default ActionLinksView;
