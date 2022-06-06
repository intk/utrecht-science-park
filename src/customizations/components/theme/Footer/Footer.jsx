import { UniversalLink } from '@plone/volto/components';
import { Grid } from 'semantic-ui-react';

import config from '@plone/volto/registry';

import './less/footer.less';

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
        <div className="footer-top-contact-address">
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
            KvK <br />
            <strong>56652488 </strong>
          </p>
        </div>
        <div className="footer-top-contact-details">
          <p>
            Phone
            <br />
            <strong> +31 30 800 4499</strong>{' '}
          </p>
          <p>
            E-mail
            <br /> <strong>info@utrechtsciencepark.nl</strong>
          </p>
        </div>
      </div>
      <div className="footer-social">
        {socialLinks.map(({ id, title, href }) => (
          <UniversalLink key={id} href={href}>
            {title}
          </UniversalLink>
        ))}
      </div>
      <div className="footer-logos">logos here</div>
      <div className="footer-bottom">
        <Grid>
          <Grid.Column>2022 @ Utrecht Science Park</Grid.Column>
          <Grid.Column>
            {siteActions.map((item) => (
              <Action key={item.id} item={item} />
            ))}
          </Grid.Column>
        </Grid>
      </div>
    </div>
  );
}

export default Footer;
