import { UniversalLink } from '@plone/volto/components';
import { Grid } from 'semantic-ui-react';
import config from '@plone/volto/registry';
//import './less/footer.less';
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

export function Footer(props) {
  const { footerLinks, socialLinks, siteActions } = config.settings;
  return (
    <div className="footer">
      <div className="footer-top">
        <div className="footer-top-text">
          <p>
            <strong>In Short</strong>
          </p>
          <p>
            Utrecht Science Park is the beating heart of one of Europe's most
            competitive regions. We bring competence from business, industry and
            academia together in order to design and create healthier, safer and
            more sustainable cities for today and for subsequent generations.
            Utrecht Science Park provides a vibrant, dynamic and exciting place
            to work, to study and to interact
          </p>
        </div>
        <div className="footer-top-menu">
          {footerLinks.map((item) => (
            <Action key={item.id} item={item} />
          ))}
        </div>
      </div>
      {/* <div className="footer-social">
                {socialLinks.map(({ id, title, href }) => (
                    <UniversalLink key={id} href={href}>
                        {title}
                    </UniversalLink>
                ))}
            </div>
            <div className="footer-logos">
                <div className='footer-logos-partners'>
                    <h4>Partners / founders</h4>
                    <div className='logos'><img
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
                </div>
                <div className='footer-logos-supporters'>
                    <h4> Supported by</h4>
                    <div className='logos'>
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
                </div>
            </div> */}
      <div className="footer-bottom">
        <div className="footer-bottom-left">
          <div className="footer-bottom-address">
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
            <div className="footer-social">
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
            </div>
          </div>
          <div className="footer-bottom-newsletter">
            <p>
              Join our mailing list to stay up to date on everything that
              happens at the park
            </p>
            <a href="en/newsletter">Subscribe</a>
          </div>
        </div>
        <div className="footer-bottom-right">
          <div className="footer-logos">
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
          </div>
          <div className="links">
            <p>2022 © Utrecht Science Park </p>
            {siteActions.map((item) => (
              <Action key={item.id} item={item} />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Footer;
