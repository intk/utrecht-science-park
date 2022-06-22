/**
 * Search widget component.
 * @module components/theme/SearchWidget/SearchWidget
 */

import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Ref, Button, Popup, Form, Input } from 'semantic-ui-react';
import { compose } from 'redux';
import { PropTypes } from 'prop-types';
import { defineMessages, injectIntl } from 'react-intl';

import { Icon } from '@plone/volto/components';
import zoomSVG from '@plone/volto/icons/zoom.svg';

const messages = defineMessages({
  search: {
    id: 'Search',
    defaultMessage: 'Search',
  },
  searchSite: {
    id: 'Search Site',
    defaultMessage: 'Search Site',
  },
});

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
      <Popup
        wide
        size="huge"
        content={
          <Form action="/search" onSubmit={this.onSubmit}>
            <Form.Field className="searchbox">
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
                  placeholder={this.props.intl.formatMessage(
                    messages.searchSite,
                  )}
                  title={this.props.intl.formatMessage(messages.search)}
                />
              </Ref>
            </Form.Field>
          </Form>
        }
        on="click"
        position="bottom center"
        pinned
        trigger={
          <Button aria-label={this.props.intl.formatMessage(messages.search)}>
            <Icon name={zoomSVG} size="24px" />
          </Button>
        }
      />
    );
  }
}

export default compose(withRouter, injectIntl)(SearchWidget);

// /**
//  * Search widget component.
//  * @module components/theme/SearchWidget/SearchWidget
//  */
//
// import React, { Component } from 'react';
// import { withRouter } from 'react-router-dom';
// import { Form, Input } from 'semantic-ui-react';
// import { compose } from 'redux';
// import { PropTypes } from 'prop-types';
// import { defineMessages, injectIntl } from 'react-intl';
//
// import { Icon } from '@plone/volto/components';
// import zoomSVG from '@plone/volto/icons/zoom.svg';
//
// const messages = defineMessages({
//   search: {
//     id: 'Search',
//     defaultMessage: 'Search',
//   },
//   searchSite: {
//     id: 'Search Site',
//     defaultMessage: 'Search Site',
//   },
// });
//
// /**
//  * SearchWidget component class.
//  * @class SearchWidget
//  * @extends Component
//  */
// class SearchWidget extends Component {
//   /**
//    * Property types.
//    * @property {Object} propTypes Property types.
//    * @static
//    */
//   static propTypes = {
//     pathname: PropTypes.string,
//   };
//
//   /**
//    * Constructor
//    * @method constructor
//    * @param {Object} props Component properties
//    * @constructs WysiwygEditor
//    */
//   constructor(props) {
//     super(props);
//     this.onChangeText = this.onChangeText.bind(this);
//     this.onSubmit = this.onSubmit.bind(this);
//     this.state = {
//       text: '',
//     };
//   }
//
//   /**
//    * On change text
//    * @method onChangeText
//    * @param {object} event Event object.
//    * @param {string} value Text value.
//    * @returns {undefined}
//    */
//   onChangeText(event, { value }) {
//     this.setState({
//       text: value,
//     });
//   }
//
//   /**
//    * Submit handler
//    * @method onSubmit
//    * @param {event} event Event object.
//    * @returns {undefined}
//    */
//   onSubmit(event) {
//     const path =
//       this.props.pathname?.length > 0
//         ? `&path=${encodeURIComponent(this.props.pathname)}`
//         : '';
//     this.props.history.push(
//       `/search?SearchableText=${encodeURIComponent(this.state.text)}${path}`,
//     );
//     event.preventDefault();
//   }
//
//   /**
//    * Render method.
//    * @method render
//    * @returns {string} Markup for the component.
//    */
//   render() {
//     return (
//       <Form action="/search" onSubmit={this.onSubmit}>
//         <Form.Field className="searchbox">
//           <button aria-label={this.props.intl.formatMessage(messages.search)}>
//             <Icon name={zoomSVG} size="25px" />
//           </button>
//           <Input
//             aria-label={this.props.intl.formatMessage(messages.search)}
//             onChange={this.onChangeText}
//             name="SearchableText"
//             value={this.state.text}
//             transparent
//             autoComplete="off"
//             placeholder={this.props.intl.formatMessage(messages.search)}
//             title={this.props.intl.formatMessage(messages.search)}
//           />
//         </Form.Field>
//       </Form>
//     );
//   }
// }
//
// export default compose(withRouter, injectIntl)(SearchWidget);