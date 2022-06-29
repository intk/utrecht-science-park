import React from 'react';
import { NavLink } from 'react-router-dom';
import { Icon } from '@plone/volto/components';
import config from '@plone/volto/registry';

import NavItems from './NavItems';
import PopupMenu from './PopupMenu';

import downKeySVG from '@plone/volto/icons/down-key.svg';

const HOME = ['', '/', '/en', '/nl'];

export default function TopLevelItems(props) {
  const { items, lang } = props;
  const { settings } = config;

  const handleClick = (item) => (e) => {
    setTopItem(item);
    e.preventDefault();
    e.stopPropagation();
  };

  const [topItem, setTopItem] = React.useState();

  return (
    <>
      {items
        .filter((item) => HOME.indexOf(item.url) === -1)
        .map((item) => (
          <NavLink
            to={item.url === '' ? '/' : item.url}
            key={item.url}
            activeClassName="active"
            className="item"
            exact={
              settings.isMultilingual
                ? item.url === `/${lang}`
                : item.url === ''
            }
            onClick={handleClick(item)}
            onKeyDown={handleClick(item)}
          >
            {item.title}
            <Icon name={downKeySVG} size="24px" />
          </NavLink>
        ))}
      <PopupMenu open={!!topItem} onClose={() => setTopItem(null)}>
        <div className="hover-menu">
          <div tabIndex="-1" role="button" className="hover-menu-inner">
            <div className="">
              {!!topItem && (
                <NavItems
                  items={topItem.items || []}
                  lang={props.lang}
                  onClose={() => setTopItem(null)}
                />
              )}
            </div>
          </div>
        </div>
      </PopupMenu>
    </>
  );
}

// import { isMouseOver } from './utils';
// const nodeRef = React.useRef();
// ref={nodeRef} onMouseOut={handleMouseOut}
// const handleMouseOut = React.useCallback((e) => {
//   const over = isMouseOver(nodeRef.current, e);
//
//   if (!over) {
//     console.log('out', over);
//     setTopItem(null);
//   }
// }, []);
