import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Ref, Form, Input } from 'semantic-ui-react';
import { compose } from 'redux';
import { PropTypes } from 'prop-types';
import { defineMessages, injectIntl } from 'react-intl';

const messages = defineMessages({
  search: {
    id: 'Search',
    defaultMessage: 'Search',
  },
  searchSite: {
    id: 'Search',
    defaultMessage: 'Search',
  },
});

const Lens = () => (
  <svg
    width="63"
    height="63"
    viewBox="0 0 63 63"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M42.1455 39.0928L41.8989 39.3843L42.1686 39.6545L61.9165 59.4419C62.1841 59.8061 62.3787 60.2694 62.5834 60.8754C62.5671 61.2879 62.3935 61.7049 62.0479 62.0492C61.6845 62.4114 61.2397 62.5846 60.8036 62.5846C60.3676 62.5846 59.9229 62.4115 59.5595 62.0495C59.5594 62.0494 59.5593 62.0493 59.5592 62.0492L39.7909 42.2412L39.5284 41.9782L39.2379 42.2099C34.9144 45.6572 29.7331 47.5913 24.1213 47.5913H24.0118C17.6423 47.5913 11.7089 45.1185 7.28486 40.6027L7.28305 40.6009C-1.89268 31.3503 -1.89021 16.4022 7.38917 7.26271L7.38938 7.26251C17.9679 -3.17115 35.8849 -1.66563 44.307 11.6745C45.7079 13.9291 46.6782 16.3996 47.2178 18.9798C48.7295 26.4061 46.7856 33.6086 42.1455 39.0928ZM9.87961 9.73668L10.1728 10.0309L9.87961 9.73668C2.03222 17.5565 1.91634 30.2958 9.76886 38.122C17.5079 45.9443 30.2916 46.0557 38.143 38.2328L38.143 38.2327C41.9534 34.435 44.0861 29.4052 44.0861 24.0394C44.0861 18.6787 42.0673 13.6471 38.2526 9.84593C34.329 5.93599 29.1712 3.92441 24.011 3.92441C18.9658 3.92441 13.8067 5.82347 9.87961 9.73668Z"
      fill="black"
      stroke="white"
      stroke-width="0.830769"
    />
  </svg>
);

/**
 * SearchWidget component class.
 * @class SearchWidget
 * @extends Component
 */
class SearchWidget extends Component {
  /**
   * Property types.
   * @property {Object} propTypes Property types.
   * @static
   */
  static propTypes = {
    pathname: PropTypes.string.isRequired,
  };

  /**
   * Constructor
   * @method constructor
   * @param {Object} props Component properties
   * @constructs WysiwygEditor
   */
  constructor(props) {
    super(props);
    this.onChangeText = this.onChangeText.bind(this);
    this.onChangeSection = this.onChangeSection.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
    this.state = {
      text: '',
      section: false,
      inputRef: null,
    };
  }

  /**
   * On change text
   * @method onChangeText
   * @param {object} event Event object.
   * @param {string} value Text value.
   * @returns {undefined}
   */
  onChangeText(event, { value }) {
    this.setState({
      text: value,
    });
  }

  /**
   * On change section
   * @method onChangeSection
   * @param {object} event Event object.
   * @param {bool} checked Section checked.
   * @returns {undefined}
   */
  onChangeSection(event, { checked }) {
    this.setState({
      section: checked,
    });
  }

  /**
   * Submit handler
   * @method onSubmit
   * @param {event} event Event object.
   * @returns {undefined}
   */
  onSubmit(event) {
    // const section = this.state.section ? `&path=${this.props.pathname}` : '';
    const path =
      this.props.pathname?.length > 0
        ? `&path=${encodeURIComponent(this.props.pathname)}`
        : '';
    const text = encodeURIComponent(this.state.text);
    this.props.history.push(`/search?SearchableText=${text}${path}`);
    event.preventDefault();
  }

  offset = ({ placement, popper }) => {
    if (placement === 'bottom') {
      return [0, popper.height / 2];
    }

    return [];
  };

  componentDidUpdate() {
    if (this.state.inputRef) {
      const input = this.state.inputRef.getElementsByTagName('input')[0];
      input.focus();
    }
  }

  /**
   * Render method.
   * @method render
   * @returns {string} Markup for the component.
   */
  render() {
    return (
      <Form action="/search" onSubmit={this.onSubmit}>
        <Form.Field className="searchbox">
          <div>
            <Lens />
          </div>
          <Ref
            innerRef={(ref) =>
              !this.state.inputRef && this.setState({ inputRef: ref })
            }
          >
            <Input
              aria-label={this.props.intl.formatMessage(messages.search)}
              onChange={this.onChangeText}
              name="SearchableText"
              value={this.state.text}
              transparent
              focus
              autoComplete="off"
              placeholder={this.props.intl.formatMessage(messages.searchSite)}
              title={this.props.intl.formatMessage(messages.search)}
            />
          </Ref>
        </Form.Field>
      </Form>
    );
  }
}

export default compose(withRouter, injectIntl)(SearchWidget);
