import pytest
from locators import StellarBurgers


@pytest.fixture
def website():
    _website = StellarBurgers()
    yield _website
    _website.quit()
