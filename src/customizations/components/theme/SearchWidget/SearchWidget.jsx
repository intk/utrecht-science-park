/**
 * Search widget component.
 * @module components/theme/SearchWidget/SearchWidget
 */

import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import { Ref, Button, Form, Input } from 'semantic-ui-react';
import { compose } from 'redux';
import { PropTypes } from 'prop-types';
import { defineMessages, injectIntl } from 'react-intl';
import PopupMenu from '@package/components/theme/Navigation/PopupMenu';

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
      <>
        <Button
          aria-label={this.props.intl.formatMessage(messages.search)}
          onClick={() => this.setState({ showPopup: true })}
        >
          <Icon name={zoomSVG} size="24px" />
        </Button>
        <PopupMenu
          open={this.state.showPopup}
          onClose={() => this.setState({ showPopup: false })}
        >
          <div className="hover-menu search-widget">
            <div className="hover-menu-inner">
              <Form action="/search" onSubmit={this.onSubmit}>
                <Form.Field className="searchbox">
                  <Ref
                    innerRef={(ref) =>
                      !this.state.inputRef && this.setState({ inputRef: ref })
                    }
                  >
                    <Input
                      aria-label={this.props.intl.formatMessage(
                        messages.search,
                      )}
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
            </div>
          </div>
        </PopupMenu>
      </>
    );
  }
}

export default compose(withRouter, injectIntl)(SearchWidget);
