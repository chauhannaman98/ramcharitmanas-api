from fastapi.testclient import TestClient
from mock import (
    root_response, chapter_response, chapter_num_response, all_verses, verse
    )

from app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == root_response


def test_get_all_chapters():
    response = client.get("/chapters")
    assert response.status_code == 200
    assert response.json() == chapter_response


def test_get_chapter_by_number():
    response = client.get("/chapters/1")
    assert response.status_code == 200
    assert response.json() == chapter_num_response


def test_get_all_verses_of_chapter():
    response = client.get("/chapters/1/verses")
    assert response.status_code == 200
    assert response.json() == all_verses


def test_get_a_verse_of_chapter():
    response = client.get("/chapters/1/verses/1")
    assert response.status_code == 200
    assert response.json() == verse