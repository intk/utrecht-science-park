import React from 'react';
import { NavLink } from 'react-router-dom';
import NavItems from './NavItems';
import config from '@plone/volto/registry';
import PopupMenu from './PopupMenu';

export default function TopLevelItems(props) {
  const { items, lang } = props;
  const { settings } = config;
  const [showMenu, setShowMenu] = React.useState(false);
  const handleClick = React.useCallback((e) => {
    setShowMenu(false);
    // e.preventDefault();
    // e.stopPropagation();
  }, []);

  return (
    <>
      {items.map((item) => (
        <NavLink
          to={item.url === '' ? '/' : item.url}
          key={item.url}
          activeClassName="active"
          className="item"
          exact={
            settings.isMultilingual ? item.url === `/${lang}` : item.url === ''
          }
          onMouseOver={() => setShowMenu(true)}
          onFocus={() => setShowMenu(true)}
          onKeyDown={handleClick}
          onClick={handleClick}
        >
          {item.title}
        </NavLink>
      ))}
      <PopupMenu open={showMenu} onClose={() => setShowMenu(false)}>
        <div tabIndex="-1" role="button" className="hover-menu">
          <div className="ui container">
            <NavItems
              items={props.items?.slice(1)}
              lang={props.lang}
              onClose={() => setShowMenu(false)}
            />
          </div>
        </div>
      </PopupMenu>
    </>
  );
}
