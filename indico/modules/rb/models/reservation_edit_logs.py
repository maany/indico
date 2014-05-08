# -*- coding: utf-8 -*-
##
##
## This file is part of Indico.
## Copyright (C) 2002 - 2013 European Organization for Nuclear Research (CERN).
##
## Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or (at your option) any later version.
##
## Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Indico;if not, see <http://www.gnu.org/licenses/>.

"""
Schema of modifications done on a reservation
"""

from indico.core.db import db
from indico.core.db.sqlalchemy.custom.utcdatetime import UTCDateTime
from indico.util.date_time import now_utc
from indico.util.string import return_ascii


class ReservationEditLog(db.Model):
    __tablename__ = 'reservation_edit_logs'

    timestamp = db.Column(
        UTCDateTime,
        primary_key=True,
        nullable=False,
        default=now_utc
    )
    info = db.Column(
        db.String,
        nullable=False
    )
    avatar_id = db.Column(
        db.String,
        primary_key=True,
        nullable=False
    )
    reservation_id = db.Column(
        db.Integer,
        db.ForeignKey('reservations.id'),
        primary_key=True,
        nullable=False
    )

    @return_ascii
    def __repr__(self):
        return u'<ReservationEditLog({0}, {1}, {2}, {3})>'.format(
            self.avatar_id,
            self.reservation_id,
            self.timestamp,
            self.info
        )
