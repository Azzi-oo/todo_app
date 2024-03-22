import requests
# from conf import SERVICE_URL
from jsonschema import validate
# from todolist.schemas.post import POST_SCHEMA
from todolist.schemas.response import Response
# from todolist.schemas.pydantic_schema import Post


def test_equal():
    assert 1 == 1


def test_is_not_equal():
    assert 1 != 2


def test_getting_users_list():
    response = requests.get('https://gorest.co.in/public/v1/users')
    test_object = Response(response)
    test_object.assert_status_code(200)

# def test_getting_posts():
#     r = requests.get(url='https://gorest.co.in/public/v1/users')
#     response = Response(r)

#     response.assert_status_code(200).validate(Post)
