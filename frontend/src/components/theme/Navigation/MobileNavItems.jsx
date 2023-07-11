import React from 'react';
import { Menu, Dropdown, Button } from 'semantic-ui-react';
import cx from 'classnames';
import { Icon, LanguageSelector } from '@plone/volto/components';

import { CSSTransition } from 'react-transition-group';
import { BodyClass } from '@plone/volto/helpers';

import { NavLink } from 'react-router-dom';
import { isInternalURL } from '@plone/volto/helpers';
import config from '@plone/volto/registry';

import closeSVG from '@plone/volto/icons/clear.svg';
import SiteLogo from '@package/static/logo.svg';
import { FormattedMessage } from 'react-intl';

const NavItem = ({ item, lang, level, closeMobileMenu }) => {
  const { settings } = config;
  // The item.url in the root is ''
  // TODO: make more consistent it everywhere (eg. reducers to return '/' instead of '')
  if (isInternalURL(item.url) || item.url === '') {
    return (
      <NavLink
        to={item.url === '' ? '/' : item.url}
        key={item.url}
        className={cx('item', `level-${level}`, {
          home: level === 0 && ['/', '/en', '/nl'].includes(item.url),
        })}
        activeClassName="active"
        exact={
          settings.isMultilingual ? item.url === `/${lang}` : item.url === ''
        }
        onClick={closeMobileMenu}
      >
        {item.title}
      </NavLink>
    );
  } else {
    return (
      <a
        href={item.url}
        key={item.url}
        className="item"
        rel="noopener noreferrer"
      >
        {item.title}
      </a>
    );
  }
};

const MenuItem = ({ item, lang, level = 0, closeMobileMenu }) => {
  const [isOpened, setIsOpened] = React.useState(false);
  return item.items?.length > 0 ? (
    <Dropdown
      text={item.title}
      className={cx('item', `level-${level}`)}
      onClick={() => setIsOpened(!isOpened)}
      open={isOpened}
    >
      <Dropdown.Menu>
        <NavItems
          items={item.items}
          lang={lang}
          level={level + 1}
          closeMobileMenu={closeMobileMenu}
        />
      </Dropdown.Menu>
    </Dropdown>
  ) : (
    <NavItem
      item={item}
      lang={lang}
      key={item.url}
      level={level}
      closeMobileMenu={closeMobileMenu}
    />
  );
};

const NavItems = ({ items, lang, level = 0, closeMobileMenu }) => {
  return items.map((item, key) => (
    <MenuItem
      key={key}
      level={level}
      lang={lang}
      item={item}
      closeMobileMenu={closeMobileMenu}
    />
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
        <div className="mobile-menu-top">
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
        <div className="tools-search-wrapper-mobile">
          <div className="language-selector-wrapper">
            <LanguageSelector />
          </div>
          <div className="search-wrapper">
            <a href="/search" rel="noopener noreferrer">
              <FormattedMessage id="Search" defaultMessage="Search" />
            </a>
          </div>
        </div>
        <div className="mobile-menu-nav">
          <Menu stackable pointing secondary>
            <NavItems
              items={items}
              lang={lang}
              closeMobileMenu={closeMobileMenu}
            />
          </Menu>
        </div>
      </div>
    </CSSTransition>
  );
};

export default MobileNavItems;
