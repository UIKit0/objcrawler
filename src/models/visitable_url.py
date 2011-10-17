#!/usr/bin/env python
"""visitable_url.py: Contains the VisitableURL database model."""
__author__ = "Bruno Nery"
__email__  = "brunonery@brunonery.com"

from model_base import Base

import sqlalchemy

class VisitableURL(Base):
    """Database model representing a URL to be visited."""
    __tablename__ = 'visitable_urls'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    url = sqlalchemy.Column(sqlalchemy.String)
    priority = sqlalchemy.Column(sqlalchemy.Integer)

    def __init__(self, url, priority):
        """Creates a VisitableURL instance.

        Arguments:
        url -- the URL to be visited.
        priority -- an integer representing the priority (small numbers should
        be visited first).
        """
        self.url = url
        self.priority = priority
