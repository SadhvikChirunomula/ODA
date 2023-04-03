# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.match import Match  # noqa: E501
from swagger_server.models.match_input import MatchInput  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_input import UserInput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_users_get(self):
        """Test case for users_get

        List all users
        """
        response = self.client.open(
            '//users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Create a new user
        """
        body = UserInput()
        response = self.client.open(
            '//users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        Retrieve a user by ID
        """
        response = self.client.open(
            '//users/{user_id}'.format(user_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_matches_get(self):
        """Test case for users_user_id_matches_get

        Retrieve a user's matches
        """
        response = self.client.open(
            '//users/{user_id}/matches'.format(user_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_matches_post(self):
        """Test case for users_user_id_matches_post

        Create a new match
        """
        body = MatchInput()
        response = self.client.open(
            '//users/{user_id}/matches'.format(user_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_put(self):
        """Test case for users_user_id_put

        Update a user
        """
        body = UserInput()
        response = self.client.open(
            '//users/{user_id}'.format(user_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
