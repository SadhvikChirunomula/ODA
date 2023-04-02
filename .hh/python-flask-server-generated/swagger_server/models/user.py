# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.user_location import UserLocation  # noqa: F401,E501
from swagger_server import util


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, first_name: str=None, last_name: str=None, email: str=None, gender: str=None, age: int=None, location: UserLocation=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        :param email: The email of this User.  # noqa: E501
        :type email: str
        :param gender: The gender of this User.  # noqa: E501
        :type gender: str
        :param age: The age of this User.  # noqa: E501
        :type age: int
        :param location: The location of this User.  # noqa: E501
        :type location: UserLocation
        """
        self.swagger_types = {
            'id': int,
            'first_name': str,
            'last_name': str,
            'email': str,
            'gender': str,
            'age': int,
            'location': UserLocation
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'gender': 'gender',
            'age': 'age',
            'location': 'location'
        }
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._gender = gender
        self._age = age
        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this User.


        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this User.


        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self) -> str:
        """Gets the email of this User.


        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this User.


        :param email: The email of this User.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def gender(self) -> str:
        """Gets the gender of this User.


        :return: The gender of this User.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this User.


        :param gender: The gender of this User.
        :type gender: str
        """
        allowed_values = ["male", "female"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def age(self) -> int:
        """Gets the age of this User.


        :return: The age of this User.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this User.


        :param age: The age of this User.
        :type age: int
        """
        if age is None:
            raise ValueError("Invalid value for `age`, must not be `None`")  # noqa: E501

        self._age = age

    @property
    def location(self) -> UserLocation:
        """Gets the location of this User.


        :return: The location of this User.
        :rtype: UserLocation
        """
        return self._location

    @location.setter
    def location(self, location: UserLocation):
        """Sets the location of this User.


        :param location: The location of this User.
        :type location: UserLocation
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location