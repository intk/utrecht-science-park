import React from 'react';
import { NavLink } from 'react-router-dom';
import { Icon } from '@plone/volto/components';
import config from '@plone/volto/registry';

import _ from 'lodash';

import NavItems from './NavItems';
import PopupMenu from './PopupMenu';

import downKeySVG from '@plone/volto/icons/down-key.svg';

const HOME = ['', '/', '/en', '/nl'];

const isMouseOver = (node, e) => {
  // const contains = node && node.contains(e.target);
  // console.log('mouse out', contains, e);

  const { clientX, clientY } = e;
  if (_.some([clientX, clientY], _.isNil)) return false;

  // false if the node is not visible
  const clientRects = node.getClientRects();
  // Heads Up!
  // getClientRects returns a DOMRectList, not an array nor a plain object
  // We explicitly avoid _.isEmpty and check .length to cover all possible shapes
  if (
    !node.offsetWidth ||
    !node.offsetHeight ||
    !clientRects ||
    !clientRects.length
  )
    return false;

  // false if the node doesn't have a valid bounding rect
  const { top, bottom, left, right } = _.first(clientRects);
  if (_.some([top, bottom, left, right], _.isNil)) return false;

  // we add a small decimal to the upper bound just to make it inclusive
  // don't add an whole pixel (1) as the event/node values may be decimal sensitive
  return (
    _.inRange(clientY, top, bottom + 0.001) &&
    _.inRange(clientX, left, right + 0.001)
  );
};

export default function TopLevelItems(props) {
  const { items, lang } = props;
  const { settings } = config;

  const handleClick = React.useCallback((e) => {
    setTopItem(null);
    // e.preventDefault();
    // e.stopPropagation();
  }, []);

  const handleMouseOut = React.useCallback((e) => {
    const over = isMouseOver(nodeRef.current, e);

    if (!over) {
      console.log('out', over);
      setTopItem(null);
    }
  }, []);

  const [topItem, setTopItem] = React.useState();
  const nodeRef = React.useRef();

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
            onMouseOver={() => setTopItem(item)}
            onFocus={() => setTopItem(item)}
            onKeyDown={handleClick}
            onClick={handleClick}
          >
            {item.title}
            <Icon name={downKeySVG} size="24px" />
          </NavLink>
        ))}
      <PopupMenu open={!!topItem} onClose={() => setTopItem(null)}>
        <div className="hover-menu" ref={nodeRef} onMouseOut={handleMouseOut}>
          <div tabIndex="-1" role="button" className="hover-menu-inner">
            <div className="ui container">
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
