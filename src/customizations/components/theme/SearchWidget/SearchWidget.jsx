import React from 'react';
import { defineMessages, useIntl } from 'react-intl';
import { Button } from 'semantic-ui-react';
import { Icon } from '@plone/volto/components';

import PopupMenu from '@package/components/theme/Navigation/PopupMenu';
import SearchWidget from '@package/components/theme/SearchWidget/SearchWidget';

import zoomSVG from '@plone/volto/icons/zoom.svg';

const messages = defineMessages({
  search: {
    id: 'Search',
    defaultMessage: 'Search',
  },
  searchSite: {
    id: 'Search',
    defaultMessage: 'Search',
  },
});

const SearchWidgetWrapper = (props) => {
  const intl = useIntl();
  const [showPopup, setShowPopup] = React.useState();

  const { children } = props;
  return (
    <div id="global-search-widget">
      <Button
        aria-label={intl.formatMessage(messages.search)}
        onClick={() => setShowPopup(true)}
      >
        <Icon name={zoomSVG} size="24px" />
      </Button>
      <PopupMenu open={showPopup} onClose={() => setShowPopup(false)}>
        <div className="hover-menu search-widget">
          <div className="hover-menu-inner">
            {children({
              onClose: () => {
                setShowPopup(false);
              },
            })}
          </div>
        </div>
      </PopupMenu>
    </div>
  );
};

const GlobalSearchWidget = (props) => (
  <SearchWidgetWrapper>
    {({ onClose }) => <SearchWidget onClose={onClose} {...props} />}
  </SearchWidgetWrapper>
);

export default GlobalSearchWidget;
