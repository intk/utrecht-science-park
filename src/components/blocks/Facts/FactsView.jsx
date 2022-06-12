import React from 'react';
import { Image } from 'semantic-ui-react';
import { UniversalLink } from '@plone/volto/components';
import lightBulb from '@package/static/logo.svg';
import cx from 'classnames';

import './facts.less';

const Card = ({ title, subtitle, icon, size }) => {
  return (
    <div className={cx('fact-card', { big: size === 'big' })}>
      <div>
        <div className="title">{title}</div>
        <div className="subtitle">{subtitle}</div>
      </div>
      <Image src={icon} size="small" />
    </div>
  );
};

const FactsView = (props) => {
  return (
    <div className="facts-grid">
      <div className="facts-row">
        <div className="fact-header">
          <h2>Facts & figures</h2>
          <UniversalLink as="button" href="/">
            View all
          </UniversalLink>
        </div>
        <Card icon={lightBulb} size="big" title="130" subtitle="Businesses" />
        <div className="facts-grid">
          <Card icon={lightBulb} title="51.000" subtitle="Students per day" />
          <Card
            icon={lightBulb}
            title="3.000"
            subtitle="Student accomodations"
          />
        </div>
      </div>
      <div className="facts-row">
        <Card icon={lightBulb} title="27000" subtitle="Staff members per day" />
        <Card
          icon={lightBulb}
          title="322"
          subtitle="Surface area in hectares"
        />
      </div>
    </div>
  );
};

export default FactsView;
