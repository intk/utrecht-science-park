from utrechtsciencepark.testing import UTRECHTSCIENCEPARK_INTEGRATION_TESTING
from pytest_plone import fixtures_factory


pytest_plugins = ["pytest_plone"]


globals().update(fixtures_factory(((UTRECHTSCIENCEPARK_INTEGRATION_TESTING, "integration"),)))
