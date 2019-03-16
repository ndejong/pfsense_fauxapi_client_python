
import time
import pytest
from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi


def test_version_exist():
    fauxapi = PfsenseFauxapi(host=None, apikey=None, apisecret=None)
    assert fauxapi.version is not None

# TODO: more tests ...
