# Flask-Events
Event organizer extension for Flask.

## Usage
Initialize extension by providing Flask and Flask-SQLAlchemy instances.
```python
from flask import Flask
from flask_eventplanner import EventPlanner
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
events = Events(app, db)


if __name__ == '__main__':
    app.run()
```
The Flask-Events uses 7 SQLAlchemy models:
- Venue: Facilities that hold events.
- Room: Smaller units of venues that hold programs.
- Event: Event model.
- Program: Scheduled programs of event.
- Organizer: Secondary table for users with organizing rights to event.
- Invitation: Secondary table for users invited to event.
- RSVP: Secondary table for users who submitted an RSVP to event.

These models can be extended using declarative mixin classes `VenueMixin`, `RoomMixin`, etc.