from src.json_reader import json_reader, json_writer
import pytest


# Fixture to get expected result
@pytest.fixture
def expected_result():
    return json_reader()

# Testing the reader
def test_json_reader(expected_result):
    assert json_reader() == expected_result

# Testing the writer
def test_json_writer_1():
    json_writer({"id": 2, "name": "Alex"})
    assert  json_reader() == {"id": 2, "name": "Alex"}

# Testing the writer
def test_json_writer_2():
    json_writer({"id": 3, "name": "Alen"})
    assert  json_reader() == {"id": 3, "name": "Alen"}

# Testing the writer
def test_json_writer_3():
    json_writer({"id": 4, "name": "John"})
    assert  json_reader() == {"id": 4, "name": "John"}