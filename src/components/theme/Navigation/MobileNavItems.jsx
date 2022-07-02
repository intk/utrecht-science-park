import React from 'react';
import { Menu, Dropdown, Button } from 'semantic-ui-react';
import cx from 'classnames';
import { Icon } from '@plone/volto/components';

import { CSSTransition } from 'react-transition-group';
import { BodyClass } from '@plone/volto/helpers';
import NavItem from '@plone/volto/components/theme/Navigation/NavItem';
import closeSVG from '@plone/volto/icons/clear.svg';
import SiteLogo from '@package/static/logo.svg';

const MenuItem = ({ item, lang, level = 0 }) => {
  return item.items?.length > 0 ? (
    <Dropdown text={item.title} className={cx('item', `level-${level}`)}>
      <Dropdown.Menu>
        <NavItems items={item.items} lang={lang} level={level + 1} />
      </Dropdown.Menu>
    </Dropdown>
  ) : (
    <NavItem item={item} lang={lang} key={item.url} />
  );
};

const NavItems = ({ items, lang, level = 0 }) => {
  return items.map((item, key) => (
    <MenuItem key={key} level={level} lang={lang} item={item} />
  ));
};

const MobileNavItems = ({
  items,
  lang,
  closeMobileMenu,
  isActive,
  pathname,
  open,
}) => {
  return (
    <CSSTransition
      in={open}
      timeout={500}
      classNames="mobile-menu"
      unmountOnExit
    >
      <div key="mobile-menu-key" className="mobile-menu">
        <div className='mobile-menu-top'>
          <img
            height="auto"
            title="Utrecht Science Park"
            src={SiteLogo}
            alt="Utrecht Science Park"
            className="logo-mobile-nav"
          />
          <BodyClass className="has-mobile-menu-open" />
          <Button basic className="close-button" onClick={closeMobileMenu}>
            <Icon name={closeSVG} />
          </Button>
        </div>
        <div className="mobile-menu-nav">
          <Menu stackable pointing secondary>
            <NavItems items={items} lang={lang} />
          </Menu>
        </div>
      </div>
    </CSSTransition>
  );
};

export default MobileNavItems;
