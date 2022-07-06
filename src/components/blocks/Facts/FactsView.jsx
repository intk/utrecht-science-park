import React from 'react';
import cx from 'classnames';
import { Image } from 'semantic-ui-react';
import { LinkMore } from '@plone/volto/components';

import suitCase from '@package/static/suitcase.svg';
import area from '@package/static/area.svg';
import people from '@package/static/people.svg';
import gradHat from '@package/static/gradhat.svg';
import home from '@package/static/home.svg';

import './facts.less';

const Card = ({ title, subtitle, icon, size }) => {
  return (
    <div
      className={cx('fact-card', {
        'facts-grid-tall-cell': size === 'tall',
        'facts-grid-wide-cell': size === 'wide',
      })}
    >
      <div>
        <div className="title">{title}</div>
        <div className="subtitle">{subtitle}</div>
      </div>
      <Image src={icon} size="small" />
    </div>
  );
};

const FactsView = (props) => {
  const { data = {} } = props;
  const { linkHref, title = 'Facts & figures' } = data;

  return (
    <div className="facts-grid">
      <div className="facts-grid-block-title">
        <h1>{title}</h1>

        {linkHref ? <LinkMore data={data} /> : ''}
      </div>
      <Card icon={suitCase} size="tall" title="130" subtitle="Businesses" />
      <Card icon={gradHat} title="51.000" subtitle="Students per day" />
      <Card icon={home} title="3.000" subtitle="Student accomodations" />
      <Card icon={people} title="27000" subtitle="Staff members per day" />
      <Card
        icon={area}
        title="322"
        size="wide"
        subtitle="Surface area in hectares"
      />
    </div>
  );
};

export default FactsView;
