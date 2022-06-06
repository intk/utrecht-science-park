/**
 * Header component.
 * @module components/theme/Header/Header
 */

import React from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import {
  Anontools,
  LanguageSelector,
  Logo,
  Navigation,
  SearchWidget,
} from '@plone/volto/components';
import { BodyClass, isCmsUi } from '@plone/volto/helpers';
import { Container, Segment } from 'semantic-ui-react';
import { LazyLoadImage } from 'react-lazy-load-image-component';
// import { Link } from 'react-router-dom';
// import { FormattedMessage } from 'react-intl';
import { HeroSection, StickyHeader } from '@package/components';
import logoSVG from '@package/icons/logo.svg';

const Header = (props) => {
  return '';
  const {
    content,
    leadImage,
    actualPathName,
    pathname,
    navigationItems,
  } = props;

  const leadImageUrl = leadImage?.scales?.panoramic?.download;
  const contentTitle = content?.title;
  const contentImageCaption = content?.image_caption;
  const contentDescription = content?.description;
  const isHomePage = content?.['@type'] === 'Plone Site';
  const cmsView = isCmsUi(actualPathName);
  const homePageView = isHomePage && !cmsView;

  return (
    <div className="portal-top">
      {homePageView && <BodyClass className="homepage-view" />}
      {leadImageUrl && !cmsView && <BodyClass className="has-image" />}
      <Segment
        basic
        className={`header-wrapper ${
          homePageView ? 'homepage' : 'contentpage'
        }`}
        role="banner"
      >
        <StickyHeader stickyBreakpoint={1024}>
          <div className="header">
            <Container>
              <div
                className={`logo-nav-wrapper ${
                  homePageView ? 'home-nav' : 'page-nav'
                }`}
              >
                <div className="logo">
                  {homePageView ? (
                    <LazyLoadImage
                      className="home-logo"
                      src={logoSVG}
                      alt="Utrecht Science Park"
                      width="234"
                      height="56"
                    />
                  ) : (
                    <Logo />
                  )}
                </div>

                <Navigation pathname={pathname} navigation={navigationItems} />

                <div className="search">
                  <SearchWidget pathname={pathname} />
                </div>

                <div className="tools-search-wrapper">
                  <LanguageSelector />
                  {!this.props.token && (
                    <div className="tools">
                      <Anontools />
                    </div>
                  )}
                  <div className="search">
                    <SearchWidget />
                  </div>
                </div>
              </div>
            </Container>
          </div>
        </StickyHeader>
      </Segment>

      <React.Fragment>
        {!cmsView && !isHomePage && (
          <div className="header-bg">
            <div
              className={'header-container'}
              style={{ position: 'relative' }}
            >
              <HeroSection
                image_url={leadImageUrl}
                image_caption={contentImageCaption}
                content_title={contentTitle}
                content_description={contentDescription}
              />
            </div>
          </div>
        )}
      </React.Fragment>
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
  actualPathName: PropTypes.string.isRequired,
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
