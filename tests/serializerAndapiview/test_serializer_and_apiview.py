import pytest


@pytest.mark.django_db()
def test_create_post(client):
    payload = dict(
        title="Test post",
        content="Test post content"
    )

    response = client.post("/api1/posts/", payload)
    assert response.status_code == 201
    data = response.data
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]


@pytest.mark.django_db
def test_get_list(post, client):
    response = client.get("/api1/posts/")
    assert response.status_code == 200
    data = response.data
    assert len(data) == 1
    assert data[0]["title"] == post.title
    assert data[0]["content"] == post.content


@pytest.mark.django_db
def test_get_post(post, client):
    response = client.get(f"/api1/posts/{post.id}/")
    assert response.status_code == 200
    data = response.data
    assert data["title"] == post.title
    assert data["content"] == post.content


@pytest.mark.django_db()
def test_update_post(post, client):
    payload = dict(
        title="Update post",
        content="Update post content"
    )

    response = client.put(f"/api1/posts/{post.id}/", payload)
    assert response.status_code == 200
    data = response.data
    assert data["title"] != post.title
    assert data["content"] != post.content
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]


@pytest.mark.django_db
def test_delete_post(post, client):
    response = client.delete(f"/api1/posts/{post.id}/")
    assert response.status_code == 204

    response = client.get(f"/api1/posts/{post.id}/")
    assert response.status_code == 404
