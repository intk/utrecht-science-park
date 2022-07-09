// Customized to use the HeroSection

import React from 'react';
import { connect } from 'react-redux';
import {
  LanguageSelector,
  Logo,
  Navigation,
  SearchWidget,
} from '@plone/volto/components';
import { BodyClass, isCmsUi } from '@plone/volto/helpers';
import { HeroSection } from '@package/components'; // , StickyHeader

const Header = (props) => {
  const { content, previewImage, pathname, navigationItems } = props;

  const previewImageUrl = previewImage?.scales?.huge?.download;
  const contentTitle = content?.title;
  const contentImageCaption = content?.image_caption;
  const contentDescription = content?.description;
  const contentType = content?.['@type'];
  const isHomePage = contentType === 'Plone Site' || contentType === 'LRF';
  const cmsView = isCmsUi(pathname);
  const homePageView = isHomePage && !cmsView;

  return (
    <div className="portal-top">
      {homePageView && <BodyClass className="homepage-view" />}
      {previewImageUrl && !cmsView && <BodyClass className="has-image" />}
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
            </div>
          </div>
        </div>
      </div>

      {!(cmsView || isHomePage) && (
        <div className="header-bg">
          <div className={'header-container'} style={{ position: 'relative' }}>
            <HeroSection
              image_url={previewImageUrl}
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

export default connect(
  (state) => ({
    previewImage: state?.content?.data?.preview_image,
    content: state.content.data,
  }),
  {},
)(Header);
