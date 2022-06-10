/**
 * Header component.
 * @module components/theme/Header/Header
 */

import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import {
//  Anontools,
  LanguageSelector,
  Logo,
  Navigation,
  SearchWidget,
} from '@plone/volto/components';
import { BodyClass, isCmsUi } from '@plone/volto/helpers';
// import { Container, Segment } from 'semantic-ui-react';
import { HeroSection } from '@package/components'; // , StickyHeader
import logoSVG from '@package/static/logo.svg';

import { LazyLoadImage } from 'react-lazy-load-image-component';

const Header = (props) => {
  const { content, leadImage, pathname, navigationItems } = props;

  const leadImageUrl = leadImage?.scales?.huge?.download;
  const contentTitle = content?.title;
  const contentImageCaption = content?.image_caption;
  const contentDescription = content?.description;
  const isHomePage = content?.['@type'] === 'Plone Site';
  const cmsView = isCmsUi(pathname);
  const homePageView = isHomePage && !cmsView;

  // <StickyHeader stickyBreakpoint={1024}>
  // </StickyHeader>

  return (
    <div className="portal-top">
      {homePageView && <BodyClass className="homepage-view" />}
      {leadImageUrl && !cmsView && <BodyClass className="has-image" />}
      <div
        className={`header-wrapper ${
          homePageView ? 'homepage' : 'contentpage'
        }`}
        role="banner"
      >
        <div className="header">
          <div
            className={`logo-nav-wrapper ${
              homePageView ? 'home-nav' : 'page-nav'
            }`}
          >
            <div className="logo">
              <Logo />
            </div>

            <Navigation pathname={pathname} navigation={navigationItems} />

            <div className="tools-search-wrapper">
              <div className="search-wrapper">
                <SearchWidget pathname={pathname} />
              </div>

              <div className="language-selector-wrapper">
                <LanguageSelector />
              </div>

              {/* {!props.token && (
                <div className="tools">
                  <Anontools />
                </div>
              )} */}
            </div>
          </div>
        </div>
      </div>

      {!(cmsView || isHomePage) && (
        <div className="header-bg">
          <div className={'header-container'} style={{ position: 'relative' }}>
            <HeroSection
              image_url={leadImageUrl}
              image_caption={contentImageCaption}
              content_title={contentTitle}
              content_description={contentDescription}
            />
          </div>
        </div>
      )}
    </div>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
Header.propTypes = {
  pathname: PropTypes.string.isRequired,
  // actualPathName: PropTypes.string.isRequired,
  leadImage: PropTypes.object,
  content: PropTypes.object,
};

export default connect(
  (state) => ({
    leadImage: state?.content?.data?.image,
    content: state.content.data,
  }),
  {},
)(Header);
