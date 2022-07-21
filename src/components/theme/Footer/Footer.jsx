import React from 'react';
import { RenderBlocks } from '@plone/volto/components';
import { useSelector } from 'react-redux';
import config from '@plone/volto/registry';
import { FormattedMessage, defineMessages, injectIntl } from 'react-intl';

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

const messages = defineMessages({
  UniversityOfAppliedSciences: {
    id: 'University of Applied Sciences Utrecht',
    defaultMessage: 'University of Applied Sciences Utrecht',
  },
});

const FooterLogos = ({ intl }) => {
  return (
    <>
      <h4>
        <FormattedMessage
          id="partners/founders"
          defaultMessage="Partners / founders"
        />
      </h4>
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
          title={intl.formatMessage(messages.UniversityOfAppliedSciences)}
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
      <h4>
        <FormattedMessage id="supportedBy" defaultMessage="Supported by" />
      </h4>
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
};

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

const Address = () => (
  <>
    <p>
      <FormattedMessage id="Address" defaultMessage="Address" /> <br />
      <strong>
        Utrecht Science Park Foundation <br />
        Heidelberglaan 11 <br />
        3584 CS Utrecht
      </strong>
    </p>
    <p>
      <FormattedMessage id="E-mail" defaultMessage="E-mail" />
      <br /> <strong>info @ utrechtsciencepark.nl</strong>
    </p>
    <p>
      <FormattedMessage id="Phone" defaultMessage="Phone" />
      <br />
      <strong> +31 30 800 4499</strong>{' '}
    </p>
    <p>
      <FormattedMessage id="KvK" defaultMessage="KvK" /> <br />
      <strong>56652488 </strong>
    </p>
  </>
);

const NewsletterDetails = () => (
  <>
    <p>
      <FormattedMessage
        id="joinOurMailing"
        defaultMessage="Join our mailing list to stay up to date on everything that happens at the park"
      />
    </p>
    <a href="en/newsletter">
      <FormattedMessage id="Subscribe" defaultMessage="Subscribe" />
    </a>
  </>
);

const Copyright = () => (
  <p>{new Date().getFullYear()} © Utrecht Science Park </p>
);

const useFooter = () => {
  const currentLang = useSelector((state) => state.intl.locale);
  const content = useSelector(
    (state) => state.content.subrequests?.[`footer-${currentLang}`]?.data || {},
  );

  return content;
};

const useFooterBlock = (globalId) => {
  const footer = useFooter();
  const { blocks = {} } = footer;
  // blocks[id]['@type'] === 'actionLinks' &&
  const blockId = Object.keys(blocks).find(
    (id) => blocks[id].globalId === globalId,
  );
  return blockId ? [blockId, blocks[blockId]] : [];
};

const FooterLinks = ({ globalId }) => {
  const [blockId, block] = useFooterBlock(globalId);
  const properties = {
    blocks: { [blockId]: block },
    blocks_layout: { items: [blockId] },
  };

  return blockId ? <RenderBlocks content={properties} /> : null;
};

const FooterBlocks = ({
  excludeIds = [],
  excludeTypes = ['title', 'actionLinks'],
}) => {
  const footer = useFooter();
  const { blocks = {}, blocks_layout } = footer;
  const filtered = blocks_layout?.items?.filter(
    // TODO: filter by excludeIds
    (id) => !excludeTypes.includes(blocks[id]?.['@type']),
  );
  const properties = {
    blocks,
    blocks_layout: {
      ...blocks_layout,
      items: filtered,
    },
  };
  return <RenderBlocks content={properties} />;
};

export function Footer(props) {
  return (
    <div className="footer">
      <div className="footer-top-left footer-top-text">
        <FooterBlocks
          excludeIds={config.settings.actionBlockIds}
          excludeTypes={['title', 'actionLinks']}
        />
      </div>
      <div className="footer-top-right footer-top-menu">
        <FooterLinks globalId="footerLinks" />
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
          <FooterLogos {...props} />
        </div>
        <div className="links">
          <Copyright />
          <FooterLinks globalId="siteActions" />
        </div>
      </div>
    </div>
  );
}

export default injectIntl(Footer);
