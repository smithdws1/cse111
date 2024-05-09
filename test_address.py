from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("489 W 200 N, Cedar City, UT 84720") == "Cedar City"
    assert extract_city("123 Any Street, Somewhere, UT 84101") == "Somewhere"

def test_extract_state():
    assert extract_state("489 W 200 N, Cedar City, UT 84720") == "UT"
    assert extract_state("123 Any Street, Somewhere, UT 84101") == "UT"

def test_extract_zipcode():
    assert extract_zipcode("489 W 200 N, Cedar City, UT 84720") == "84720"
    assert extract_zipcode("123 Any Street, Somewhere, UT 84101") == "84101"

pytest.main(["-v", "--tb=line", "-rN", __file__])