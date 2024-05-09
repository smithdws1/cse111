from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("David", "Smith") == "Smith; David"
    assert make_full_name("Samuel", "Adams") == "Adams; Samuel"
    assert make_full_name("John-son", "Abe") == "Abe; John-son"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Smith; David") == "Smith"
    assert extract_family_name("Adams; Samuel") == "Adams"
    assert extract_family_name("Abe; John-son") == "Abe"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("Smith; David") == "David"
    assert extract_given_name("Adams; Samuel") == "Samuel"
    assert extract_given_name("Abe; John-son") == "John-son"
    assert extract_given_name("; ") == ""
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])