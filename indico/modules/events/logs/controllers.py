# This file is part of Indico.
# Copyright (C) 2002 - 2017 European Organization for Nuclear Research (CERN).
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from indico.modules.events.logs.views import WPEventLogs
from indico.modules.events.logs.models.entries import EventLogEntry
from indico.legacy.webinterface.rh.conferenceModif import RHConferenceModifBase


class RHEventLogs(RHConferenceModifBase):
    """Shows the modification/action log for the event"""

    _allowClosed = True

    def _process(self):
        entries = self.event_new.log_entries.order_by(EventLogEntry.logged_dt.desc()).all()
        realms = {e.realm for e in entries}
        return WPEventLogs.render_template('logs.html', self._conf, entries=entries, realms=realms)
