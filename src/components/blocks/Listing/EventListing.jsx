import React from 'react';
import { Button, Image } from 'semantic-ui-react';
import { UniversalLink, Icon } from '@plone/volto/components';
import { DateTime } from 'luxon';
import { Grid } from 'semantic-ui-react';
import { FormattedDateRange } from '@package/components';
import calendarSVG from '@plone/volto/icons/calendar.svg';
import { getAuthToken } from '@plone/volto/helpers';
// import externalSVG from '@package/icons/arrow-up-right-from-square-solid.svg';

// , PreviewImage
// import globeSVG from '@plone/volto/icons/globe.svg';
// import enterpriseSVG from '@plone/volto/icons/enterprise.svg';

const ICONS = {
  webinar:
    'https://gptrac.pixelblaster.ro/events/webinar_icon_pms-7721.svg/@@images/2d2c159c-ed6d-43b9-8f51-9c8aec230f25.svg',
  conference:
    'https://img.icons8.com/external-kiranshastry-lineal-kiranshastry/64/000000/external-conference-communication-kiranshastry-lineal-kiranshastry-2.png',
  training: 'https://img.icons8.com/material-outlined/24/000000/training.png',
  meeting: 'https://img.icons8.com/ios/50/000000/meeting.png',
  workshop: 'https://img.icons8.com/ios/50/000000/people-working-together.png',
};

const EventTypeIcon = ({ event_type }) => {
  return event_type ? (
    <Image title={event_type} src={ICONS[event_type]} size="small" />
  ) : null;
};

const ItemLocation = ({ location, event_url }) => {
  return (
    <span className="location">
      {location ? (
        event_url ? (
          <>
            {' at'} <UniversalLink href={event_url}>{location}</UniversalLink>
          </>
        ) : (
          `at ${location}`
        )
      ) : (
        ''
      )}
    </span>
  );
};

const PastEventsDivider = ({ index, base, item, groups, groupIndex = 0 }) => {
  // because of batching we can never be sure if we haven't already displayed
  // the past events indicator. For this we only show it if it's in between
  // actual events.
  if (index === 0 && groupIndex === 0) return null;

  let previous;
  if (groupIndex === 0) {
    previous = groups[groupIndex][index - 1];
  } else {
    if (index === 0) {
      const prevGroup = groups[groupIndex - 1].entries;
      previous = prevGroup[prevGroup.length - 1];
    } else {
      previous = groups[groupIndex][index - 1];
    }
  }

  if (!previous?.start) return null;
  if (!item?.start) return null;

  if (
    DateTime.fromISO(previous.start) < base &&
    DateTime.fromISO(item.start) > base
  ) {
    return <h4 className="pastevents-divider">Past events</h4>;
  }

  if (
    DateTime.fromISO(previous.start) > base &&
    DateTime.fromISO(item.start) < base
  ) {
    return (
      <Grid.Row>
        <h4 className="pastevents-divider">Past events</h4>
      </Grid.Row>
    );
  }

  return null;
};

const EventListingTemplate = ({ items, linkTitle, linkHref, isEditMode }) => {
  // console.log('item', items);

  const groups = [];
  items.forEach((item) => {
    const date = DateTime.fromISO(item.start);
    if (
      groups.length &&
      groups[groups.length - 1].month === `${date.monthLong} - ${date.year}`
    ) {
      groups[groups.length - 1].entries.push(item);
    } else {
      groups.push({
        month: `${date.monthLong} - ${date.year}`,
        entries: [item],
      });
    }
  });
  const now = DateTime.fromJSDate(new Date());

  const isAuthenticated = getAuthToken();

  return (
    <Grid className="items event-listing-items" stackable>
      {groups.map(({ month, entries }, gi) => (
        <>
          {gi > 0 && (
            <Grid.Row className="month-divider">
              <div>{month}</div>
            </Grid.Row>
          )}
          <Grid.Row key={gi} className="items-month">
            <Grid.Column width={12}>
              {entries.map((item, i) => {
                return (
                  <Grid stackable key={i}>
                    <PastEventsDivider
                      item={item}
                      groups={groups}
                      groupIndex={gi}
                      index={i}
                      base={now}
                    />
                    <Grid.Column width={12}>
                      <div className="listing-item" key={item['@id']}>
                        <div>
                          <div className="metadata">
                            {item.event_type === 'webinar' ? (
                              <>
                                {/* <Icon name={globeSVG} size="18px" /> */}
                                <EventTypeIcon event_type={item.event_type} />
                              </>
                            ) : (
                              <>
                                {/* <Icon name={enterpriseSVG} size="18px" /> */}
                                <EventTypeIcon event_type={item.event_type} />
                              </>
                            )}
                            <FormattedDateRange
                              start={item.start}
                              end={item.end}
                            />

                            <ItemLocation {...item} />

                            {item.start && DateTime.fromISO(item.start) > now && (
                              <Button
                                basic
                                compact
                                size="tiny"
                                as="a"
                                href={`${item['@id']}/@@ics_view`}
                                target="_blank"
                                rel="noopener noreferrer"
                                className="calendar"
                              >
                                <Icon name={calendarSVG} size="14px" />
                                Add to calendar
                              </Button>
                            )}
                          </div>
                          <div className="listing-body">
                            <h4>
                              <UniversalLink
                                href={item.event_url || item['@id']}
                              >
                                {item.title ? item.title : item.id}
                                <span className="external"></span>
                              </UniversalLink>
                            </h4>
                          </div>
                          <p>
                            {item.description}
                            {isAuthenticated && (
                              <p>
                                <UniversalLink item={item}>
                                  GPTRAC page for this event
                                </UniversalLink>
                              </p>
                            )}
                          </p>
                        </div>
                      </div>
                    </Grid.Column>
                  </Grid>
                );
              })}
            </Grid.Column>
          </Grid.Row>
        </>
      ))}
    </Grid>
  );
};

export default EventListingTemplate;
