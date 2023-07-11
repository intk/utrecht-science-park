"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "utrechtsciencepark"

_ = MessageFactory("utrechtsciencepark")

logger = logging.getLogger("utrechtsciencepark")
