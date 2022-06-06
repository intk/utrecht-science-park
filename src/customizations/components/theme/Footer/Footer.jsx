import { Link } from 'react-router-dom'; // NavLink,

export function Footer(props) {
  return (
    <div className="footer">
      <div className="footer-top">
        <div className="footer-top-text">
          {props.children}
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
          <Link title="Site" to="/contact">
            Contacts
          </Link>

          <Link title="Site" to="/vacancies/">
            Vacancies
          </Link>

          <Link title="Site" to="/FAQ/">
            FAQ
          </Link>

          <Link title="Site" to="/about/">
            About
          </Link>
        </div>
        <div className="footer-top-contact-address">
          <p>
            {' '}
            Address Utrecht Science Park Foundation Heidelberglaan 11 3584 CS
            Utrecht KvK 56652488
          </p>
        </div>
        <div className="footer-top-contact-details">
          <p>Phone +31 30 800 4499 E-mail info@utrechtsciencepark.nl</p>
        </div>
        <div className="footer-top-social">
          <Link title="Site" to="#">
            Facebook
          </Link>

          <Link title="Site" to="#">
            Instagram
          </Link>

          <Link title="Site" to="#/">
            Twitter
          </Link>

          <Link title="Site" to="/about/">
            Youtube
          </Link>
        </div>
      </div>
      <div className="footer-logos"></div>
      <div className="footer-bottom"></div>
    </div>
  );
}

export default Footer;
