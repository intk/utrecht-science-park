// Customized to use the HeroSection

import React from 'react';
import { useSelector } from 'react-redux';
import {
  LanguageSelector,
  Logo,
  Navigation,
  SearchWidget,
} from '@plone/volto/components';
import { BodyClass, isCmsUi } from '@plone/volto/helpers';
import { HeroSection } from '@package/components'; // , StickyHeader
import usePreviewImage from './usePreviewImage';

const Header = (props) => {
  const { pathname, navigationItems } = props;

  const content = useSelector((state) => state.content.data);

  const previewImage = usePreviewImage(pathname);

  const previewImageUrl = previewImage?.scales?.huge?.download;
  // const contentImageCaption = content?.image_caption;

  const contentType = content?.['@type'];
  const isHomePage = contentType === 'Plone Site' || contentType === 'LRF';
  const cmsView = isCmsUi(pathname);
  const homePageView = isHomePage && !cmsView;

  return (
    <div className="portal-top">
      {homePageView && <BodyClass className="homepage-view" />}
      {!cmsView && <BodyClass className="has-image" />}
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
            <HeroSection image_url={previewImageUrl} content={content} />
          </div>
        </div>
      )}
    </div>
  );
};

export default Header;
