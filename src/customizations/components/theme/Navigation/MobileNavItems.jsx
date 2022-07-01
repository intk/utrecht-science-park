import React from 'react';
import { Link } from 'react-router-dom';
import { Menu, Dropdown, Button } from 'semantic-ui-react';
import cx from 'classnames';
import { flattenToAppURL } from '@plone/volto/helpers';
import { Icon } from '@plone/volto/components';

import clearSVG from '@plone/volto/icons/clear.svg';

const MobileNavItems = ({ items, closeMobileMenu, isActive }) => {
  const isMobileMenuOpen = true;

  return (
    <Menu
      stackable
      pointing
      secondary
      className={
        isMobileMenuOpen
          ? 'open'
          : 'tablet computer large screen widescreen only'
      }
      // onClick={this.closeMobileMenu}
      // onBlur={() => this.closeMobileMenu}
    >
      <Button
        icon
        basic
        title="Close menu"
        className="close-button"
        onClick={closeMobileMenu}
      >
        <Icon name={clearSVG} size="37px" />
      </Button>

      {items.map((item) => {
        const flatUrl = flattenToAppURL(item.url);
        const draftItem = item.review_state === 'draft';
        return item.items && item.items.length ? (
          <Dropdown
            item
            simple
            className={
              isActive(flatUrl)
                ? 'item firstLevel menuActive'
                : 'item firstLevel'
            }
            key={flatUrl}
            closeOnBlur={isMobileMenuOpen ? false : true}
            trigger={
              <Link
                className={draftItem ? 'disabled' : ''}
                to={flatUrl === '' ? '/' : flatUrl}
                key={flatUrl}
                onClick={(e) => {
                  if (draftItem) e.preventDefault();
                }}
              >
                {item.title}
              </Link>
            }
          >
            <Dropdown.Menu>
              {item.items.map((subitem) => {
                const flatSubUrl = flattenToAppURL(subitem.url);
                const subDraftItem = subitem.review_state === 'draft';
                return (
                  <Dropdown.Item key={flatSubUrl}>
                    {subitem.title
                      .toLowerCase()
                      .includes('country profiles') ? (
                      <>
                        <div className="secondLevel-wrapper">
                          <Link
                            to={flatSubUrl === '' ? '/' : flatSubUrl}
                            key={flatSubUrl}
                            className={cx('item secondLevel', {
                              menuActive: isActive(flatSubUrl),
                              disabled: subDraftItem,
                            })}
                            onClick={(e) => {
                              if (subDraftItem) e.preventDefault();
                            }}
                          >
                            {subitem.title}
                          </Link>
                        </div>
                        {subitem.items && subitem.items.length > 0 && (
                          <div className="submenu-wrapper">
                            <div className="submenu countries-submenu">
                              {subitem.items.map((subsubitem) => {
                                const flatSubSubUrl = flattenToAppURL(
                                  subsubitem.url,
                                );
                                const subSubDraftItem =
                                  subsubitem.review_state === 'draft';
                                return (
                                  <Link
                                    to={
                                      flatSubSubUrl === '' ? '/' : flatSubSubUrl
                                    }
                                    title={subsubitem.title}
                                    key={flatSubSubUrl}
                                    className={cx('item thirdLevel', {
                                      menuActive: isActive(flatSubUrl),
                                      disabled: subSubDraftItem,
                                    })}
                                    onClick={(e) => {
                                      if (subSubDraftItem) e.preventDefault();
                                    }}
                                  >
                                    {subsubitem.title}
                                  </Link>
                                );
                              })}
                            </div>
                          </div>
                        )}
                      </>
                    ) : (
                      <>
                        <div className="secondLevel-wrapper">
                          <Link
                            to={flatSubUrl === '' ? '/' : flatSubUrl}
                            key={flatSubUrl}
                            className={cx('item secondLevel', {
                              menuActive: isActive(flatSubUrl),
                              disabled: subDraftItem,
                            })}
                            onClick={(e) => {
                              if (subDraftItem) e.preventDefault();
                            }}
                          >
                            {subitem.title}
                          </Link>
                        </div>
                        {subitem.items && subitem.items.length > 0 && (
                          <div className="submenu-wrapper">
                            <div className="submenu">
                              {subitem.items.map((subsubitem) => {
                                const flatSubSubUrl = flattenToAppURL(
                                  subsubitem.url,
                                );
                                const subSubDraftItem =
                                  subsubitem.review_state === 'draft';
                                return (
                                  <Link
                                    to={
                                      flatSubSubUrl === '' ? '/' : flatSubSubUrl
                                    }
                                    title={subsubitem.title}
                                    key={flatSubSubUrl}
                                    className={cx('item thirdLevel', {
                                      menuActive: isActive(flatSubUrl),
                                      disabled: subSubDraftItem,
                                    })}
                                    onClick={(e) => {
                                      if (subSubDraftItem) e.preventDefault();
                                    }}
                                  >
                                    {subsubitem.title}
                                  </Link>
                                );
                              })}
                            </div>
                          </div>
                        )}
                      </>
                    )}
                  </Dropdown.Item>
                );
              })}
            </Dropdown.Menu>
          </Dropdown>
        ) : (
          <Link
            to={flatUrl === '' ? '/' : flatUrl}
            key={flatUrl}
            className={
              isActive(flatUrl)
                ? 'item menuActive firstLevel'
                : 'item firstLevel'
            }
          >
            {item.title}
          </Link>
        );
      })}
    </Menu>
  );
};

export default MobileNavItems;
