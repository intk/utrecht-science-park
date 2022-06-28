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
                    <p><strong>In Short</strong></p>
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
                <Grid stackable>
                    <Grid.Column width={6}>
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
                        <br /> <strong>info @ utrechtsciencepark.nl</strong>
                    </p>
                </div>
                        2022 @ Utrecht Science Park</Grid.Column>
                    <Grid.Column width={6} className="links">
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
