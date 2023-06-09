# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Match(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, user_id: int=None, match_id: int=None, match_score: float=None, created_at: datetime=None, updated_at: datetime=None):  # noqa: E501
        """Match - a model defined in Swagger

        :param id: The id of this Match.  # noqa: E501
        :type id: int
        :param user_id: The user_id of this Match.  # noqa: E501
        :type user_id: int
        :param match_id: The match_id of this Match.  # noqa: E501
        :type match_id: int
        :param match_score: The match_score of this Match.  # noqa: E501
        :type match_score: float
        :param created_at: The created_at of this Match.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this Match.  # noqa: E501
        :type updated_at: datetime
        """
        self.swagger_types = {
            'id': int,
            'user_id': int,
            'match_id': int,
            'match_score': float,
            'created_at': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'user_id',
            'match_id': 'match_id',
            'match_score': 'match_score',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }
        self._id = id
        self._user_id = user_id
        self._match_id = match_id
        self._match_score = match_score
        self._created_at = created_at
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'Match':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Match of this Match.  # noqa: E501
        :rtype: Match
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Match.


        :return: The id of this Match.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Match.


        :param id: The id of this Match.
        :type id: int
        """

        self._id = id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Match.


        :return: The user_id of this Match.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Match.


        :param user_id: The user_id of this Match.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def match_id(self) -> int:
        """Gets the match_id of this Match.


        :return: The match_id of this Match.
        :rtype: int
        """
        return self._match_id

    @match_id.setter
    def match_id(self, match_id: int):
        """Sets the match_id of this Match.


        :param match_id: The match_id of this Match.
        :type match_id: int
        """

        self._match_id = match_id

    @property
    def match_score(self) -> float:
        """Gets the match_score of this Match.


        :return: The match_score of this Match.
        :rtype: float
        """
        return self._match_score

    @match_score.setter
    def match_score(self, match_score: float):
        """Sets the match_score of this Match.


        :param match_score: The match_score of this Match.
        :type match_score: float
        """

        self._match_score = match_score

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this Match.


        :return: The created_at of this Match.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this Match.


        :param created_at: The created_at of this Match.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self) -> datetime:
        """Gets the updated_at of this Match.


        :return: The updated_at of this Match.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """Sets the updated_at of this Match.


        :param updated_at: The updated_at of this Match.
        :type updated_at: datetime
        """

        self._updated_at = updated_at
