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

import { v4 as uuid } from 'uuid';

const Card = ({ title, subtitle, icon, tall, wide }) => {
  return (
    <div
      className={cx('fact-card', {
        'facts-grid-tall-cell': tall,
        'facts-grid-wide-cell': wide,
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

const icons = [suitCase, gradHat, home, people, area];

const defaultCards = () => [
  { id: uuid(), title: '130', subtitle: 'Businesses' },
  { id: uuid(), title: '51.000', subtitle: 'Students per day' },
  { id: uuid(), title: '3.000', subtitle: 'Student accomodations' },
  { id: uuid(), title: '27000', subtitle: 'Staff members per day' },
  { id: uuid(), title: '322', subtitle: 'Surface area in hectares' },
];

const FactsView = (props) => {
  const { data = {} } = props;
  const { linkHref, title = 'Facts & figures', cards = defaultCards() } = data;

  return (
    <div className="facts-grid">
      <div className="facts-grid-block-title">
        <h2>{title}</h2>
        {linkHref ? <LinkMore data={data} /> : ''}
      </div>
      {cards?.map((card, i) => (
        <Card
          key={card.id}
          icon={icons[i]}
          title={card.title}
          subtitle={card.subtitle}
          wide={i === cards.length - 1}
          tall={i === 0}
        />
      ))}
    </div>
  );
};

// <Card icon={icons[0]} size="tall" title="130" subtitle="Businesses" />
// <Card icon={icons[1]} title="51.000" subtitle="Students per day" />
// <Card icon={icons[2]} title="3.000" subtitle="Student accomodations" />
// <Card icon={icons[3]} title="27000" subtitle="Staff members per day" />
// <Card
//   icon={icons[4]}
//   title="322"
//   size="wide"
//   subtitle="Surface area in hectares"
// />

export default FactsView;
