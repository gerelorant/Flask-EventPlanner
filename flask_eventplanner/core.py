from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Model

from flask_eventplanner.model import \
    EventMixin,\
    InvitationMixin,\
    OrganizerMixin,\
    RSVPMixin,\
    VenueMixin,\
    ProgramMixin,\
    RoomMixin


class EventPlanner:
    def __init__(
            self,
            app: Flask = None,
            db: SQLAlchemy = None,
            venue_class: type(Model) = None,
            room_class: type(Model) = None,
            event_class: type(Model) = None,
            program_class: type(Model) = None,
            organizer_class: type(Model) = None,
            invitation_class: type(Model) = None,
            rsvp_class: type(Model) = None
    ):
        self.app = app
        self.db = db

        self.venue_class = venue_class
        self.room_class = room_class
        self.event_class = event_class
        self.program_class = program_class
        self.organizer_class = organizer_class
        self.invitation_class = invitation_class
        self.rsvp_class = rsvp_class

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        self.app = app
        self.app.extensions['events'] = self

        if self.venue_class is None:
            class Venue(self.db.Model, VenueMixin):
                __tablename__ = "venue"

            self.venue_class = Venue

        if self.room_class is None:
            class Room(self.db.Model, RoomMixin):
                __tablename__ = "room"

            self.room_class = Room

        if self.event_class is None:
            class Event(self.db.Model, EventMixin):
                __tablename__ = "event"

            self.event_class = Event

        if self.program_class is None:
            class Program(self.db.Model, ProgramMixin):
                __tablename__ = "program"

            self.program_class = Program

        if self.organizer_class is None:
            class Organizer(self.db.Model, OrganizerMixin):
                __tablename__ = "organizer"

            self.organizer_class = Organizer

        if self.invitation_class is None:
            class Invitation(self.db.Model, InvitationMixin):
                __tablename__ = "invitation"

            self.invitation_class = Invitation

        if self.rsvp_class is None:
            class RSVP(self.db.Model, RSVPMixin):
                __tablename__ = "rsvp"

            self.rsvp_class = RSVP
