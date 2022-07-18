import React from 'react';
import { UniversalLink } from '@plone/volto/components';
import { useSelector, useDispatch } from 'react-redux';
import config from '@plone/volto/registry';
import { getContent } from '@plone/volto/actions';
// import { useLocation } from 'react-router';

import UtrechtUnivLogo from '@package/static/Utrecht University.png';
import CityUtrechtLogo from '@package/static/City of Utrecht.png';
import UMCUtrechtLogo from '@package/static/UMC Utrecht.png';
import UnivApplScienceLogo from '@package/static/University of Applied Sciences Utrecht.png';
import ProvUtrechtLogo from '@package/static/Provincie Utrecht.png';
import OnderFondsLogo from '@package/static/Ondernemers fonds Utrecht.png';
import EuroRegDevLogo from '@package/static/European Fund for regional Development.png';
import FacebookLogo from '@package/static/facebook.svg';
import InstagramLogo from '@package/static/instagram.svg';
import TwitterLogo from '@package/static/twiter.svg';
import YouTubeLogo from '@package/static/youtube.svg';
import LinkedInLogo from '@package/static/linkedin.svg';

const Action = ({ item }) => {
  return (
    <UniversalLink href={item.links.en.path}>
      {item.links.en.title}
    </UniversalLink>
  );
};

const FooterLogos = () => (
  <>
    <h4>Partners / founders</h4>
    <div className="logos">
      <img
        height="auto"
        title="Utrecht University"
        src={UtrechtUnivLogo}
        alt="Utrecht University"
        className="logo-partner"
      />
      <img
        height="auto"
        title="City of Utrecht"
        src={CityUtrechtLogo}
        alt="City of Utrecht"
        className="logo-partner"
      />
      <img
        height="auto"
        title="UMC Utrecht"
        src={UMCUtrechtLogo}
        alt="UMC Utrecht"
        className="logo-partner"
      />
      <img
        height="auto"
        title="University of Applied Sciences Utrecht"
        src={UnivApplScienceLogo}
        alt="University of Applied Sciences Utrecht"
        className="logo-partner"
      />
      <img
        height="auto"
        title="Provincie Utrecht"
        src={ProvUtrechtLogo}
        alt="Provincie Utrecht"
        className="logo-partner"
      />
    </div>
    <h4> Supported by</h4>
    <div className="logos">
      <img
        height="auto"
        title="Ondernemers fonds Utrecht"
        src={OnderFondsLogo}
        alt="Ondernemers fonds Utrecht"
        className="logo-partner"
      />
      <img
        height="auto"
        title="European Fund for regional Development"
        src={EuroRegDevLogo}
        alt="European Fund for regional Development"
        className="logo-partner"
      />
    </div>
  </>
);

const SocialLinks = () => (
  <>
    <a href="https://facebook.com">
      <img
        height="auto"
        title="Facebook"
        src={FacebookLogo}
        alt="Facebook"
        className="logo-social"
      />
    </a>
    <a href="https://instagram.com">
      <img
        height="auto"
        title="Instagram"
        src={InstagramLogo}
        alt="Instagram"
        className="logo-social"
      />
    </a>
    <a href="https://youtube.com">
      <img
        height="auto"
        title="YouTube"
        src={YouTubeLogo}
        alt="YouTube"
        className="logo-social"
      />
    </a>
    <a href="https://twitter.com">
      <img
        height="auto"
        title="Twitter"
        src={TwitterLogo}
        alt="Twitter"
        className="logo-social"
      />
    </a>
    <a href="https://linkedin.com">
      <img
        height="auto"
        title="LinkedIn"
        src={LinkedInLogo}
        alt="LinkedIn"
        className="logo-social"
      />
    </a>
  </>
);

const InShort = () => (
  <>
    <p>
      <strong>In Short</strong>
    </p>
    <p>
      Utrecht Science Park is the beating heart of one of Europe's most
      competitive regions. We bring competence from business, industry and
      academia together in order to design and create healthier, safer and more
      sustainable cities for today and for subsequent generations. Utrecht
      Science Park provides a vibrant, dynamic and exciting place to work, to
      study and to interact
    </p>
  </>
);

const Address = () => (
  <>
    <p>
      Address <br />
      <strong>
        Utrecht Science Park Foundation <br />
        Heidelberglaan 11 <br />
        3584 CS Utrecht
      </strong>{' '}
      <br />
    </p>
    <p>
      E-mail
      <br /> <strong>info @ utrechtsciencepark.nl</strong>
    </p>
    <p>
      Phone
      <br />
      <strong> +31 30 800 4499</strong>{' '}
    </p>
    <p>
      KvK <br />
      <strong>56652488 </strong>
    </p>
  </>
);

const NewsletterDetails = () => (
  <>
    <p>
      Join our mailing list to stay up to date on everything that happens at the
      park
    </p>
    <a href="en/newsletter">Subscribe</a>
  </>
);

const Copyright = () => <p>2022 © Utrecht Science Park </p>;

function FooterLinks(props) {
  const dispatch = useDispatch();
  const footerLinks = useSelector(
    (state) => state.content.subrequests?.footer?.data?.items || [],
  );

  const currentLang = useSelector((state) => state.intl.locale);

  const footerUrl = `/${currentLang}/footer-links`;

  React.useEffect(() => {
    dispatch(getContent(footerUrl, null, 'footer')).catch((e) => {
      // eslint-disable-next-line
      console.log(
        `Footer page not found: ${footerUrl}. Please create as folder`,
      );
    });
  }, [dispatch, footerUrl]);

  return footerLinks.map((item) => (
    <UniversalLink key={item.id} item={item}>
      {item.title}
    </UniversalLink>
  ));
}

export function Footer(props) {
  const { siteActions } = config.settings;

  return (
    <div className="footer">
      <div className="footer-top-left footer-top-text">
        <InShort />
      </div>
      <div className="footer-top-right footer-top-menu">
        <FooterLinks />
      </div>
      <div className="footer-bottom-left">
        <div className="footer-bottom-address">
          <Address />
          <div className="footer-social">
            <SocialLinks />
          </div>
        </div>
        <div className="footer-bottom-newsletter">
          <NewsletterDetails />
        </div>
      </div>

      <div className="footer-bottom-right footer-bottom">
        <div className="footer-logos">
          <FooterLogos />
        </div>
        <div className="links">
          <Copyright />
          {siteActions.map((item) => (
            <Action key={item.id} item={item} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Footer;
