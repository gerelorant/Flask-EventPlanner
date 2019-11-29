import datetime as dt

import flask_sqlalchemy as fsa
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship, backref


class VenueMixin(fsa.Model):
    name = sa.Column(sa.String(64), nullable=False, index=True)
    description = sa.Column(sa.Text)
    address = sa.Column(sa.String(255), nullable=False, index=True)
    website = sa.Column(sa.String(80))
    limit = sa.Column(sa.Integer)

    @property
    def past_events(self):
        events = getattr(self, 'events')
        Event = getattr(type(self), 'events').property.mapper.class_
        now = dt.datetime.utcnow()

        return events\
            .filter(Event.end < now)

    @property
    def ongoing_events(self):
        events = getattr(self, 'events')
        Event = getattr(type(self), 'events').property.mapper.class_
        now = dt.datetime.utcnow()

        return events\
            .filter(Event.start <= now)\
            .filter(Event.end >= now)

    @property
    def upcoming_events(self):
        events = getattr(self, 'events')
        Event = getattr(type(self), 'events').property.mapper.class_
        now = dt.datetime.utcnow()

        return events\
            .filter(Event.start > now)


class RoomMixin(fsa.Model):
    name = sa.Column(sa.String(64), nullable=False, index=True)
    description = sa.Column(sa.Text)
    limit = sa.Column(sa.Integer)

    # noinspection PyMethodParameters
    @declared_attr
    def venue_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('venue.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def venue(cls):
        return relationship(
            'Venue',
            backref=backref('rooms', lazy='dynamic')
        )

    @property
    def past_programs(self):
        programs = getattr(self, 'programs')
        Program = getattr(type(self), 'programs').property.mapper.class_
        now = dt.datetime.utcnow()

        return programs\
            .filter(Program.end < now)

    @property
    def ongoing_programs(self):
        programs = getattr(self, 'programs')
        Program = getattr(type(self), 'programs').property.mapper.class_
        now = dt.datetime.utcnow()

        return programs\
            .filter(Program.start <= now)\
            .filter(Program.end >= now)

    @property
    def upcoming_programs(self):
        programs = getattr(self, 'programs')
        Program = getattr(type(self), 'programs').property.mapper.class_
        now = dt.datetime.utcnow()

        return programs\
            .filter(Program.start > now)


class EventMixin(fsa.Model):
    name = sa.Column(sa.String(64), nullable=False, index=True)
    description = sa.Column(sa.Text)
    start = sa.Column(sa.DateTime, index=True)
    end = sa.Column(sa.DateTime, index=True)
    public = sa.Column(sa.Boolean, default=True, nullable=False, index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def venue_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('venue.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def venue(cls):
        return relationship(
            'Venue',
            backref=backref('events', lazy='dynamic')
        )


class ProgramMixin(fsa.Model):
    name = sa.Column(sa.String(64), nullable=False, index=True)
    description = sa.Column(sa.Text)
    start = sa.Column(sa.DateTime, index=True)
    end = sa.Column(sa.DateTime, index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def room_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('room.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def room(cls):
        return relationship(
            'Room',
            backref=backref('rooms', lazy='dynamic')
        )


class OrganizerMixin(fsa.Model):
    role = sa.Column(sa.String(40), default='admin', index=True, nullable=False)

    # noinspection PyMethodParameters
    @declared_attr
    def user_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('user.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def user(cls):
        return relationship(
            'User',
            backref=backref('organized_events', lazy='dynamic')
        )

    # noinspection PyMethodParameters
    @declared_attr
    def event_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('event.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def event(cls):
        return relationship(
            'Event',
            backref=backref('organizers', lazy='dynamic')
        )


class InvitationMixin(fsa.Model):
    timestamp = sa.Column(sa.DateTime, default=dt.datetime.utcnow)

    # noinspection PyMethodParameters
    @declared_attr
    def user_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('user.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def user(cls):
        return relationship(
            'User',
            backref=backref('invitations', lazy='dynamic')
        )

    # noinspection PyMethodParameters
    @declared_attr
    def event_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('event.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def event(cls):
        return relationship(
            'Event',
            backref=backref('invitees', lazy='dynamic')
        )


class RSVPMixin(fsa.Model):
    value = sa.Column(sa.Boolean, index=True)
    timestamp = sa.Column(sa.DateTime, default=dt.datetime.utcnow)

    # noinspection PyMethodParameters
    @declared_attr
    def user_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('user.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def user(cls):
        return relationship(
            'User',
            backref=backref('invitations', lazy='dynamic')
        )

    # noinspection PyMethodParameters
    @declared_attr
    def event_id(cls):
        return sa.Column(sa.Integer, sa.ForeignKey('event.id'), index=True)

    # noinspection PyMethodParameters
    @declared_attr
    def event(cls):
        return relationship(
            'Event',
            backref=backref('invitees', lazy='dynamic')
        )
