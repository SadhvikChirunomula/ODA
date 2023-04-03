# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.user_location import UserLocation  # noqa: F401,E501
from swagger_server import util


class UserInput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, email: str=None, password: str=None, age: int=None, gender: str=None, bio: str=None, location: UserLocation=None):  # noqa: E501
        """UserInput - a model defined in Swagger

        :param name: The name of this UserInput.  # noqa: E501
        :type name: str
        :param email: The email of this UserInput.  # noqa: E501
        :type email: str
        :param password: The password of this UserInput.  # noqa: E501
        :type password: str
        :param age: The age of this UserInput.  # noqa: E501
        :type age: int
        :param gender: The gender of this UserInput.  # noqa: E501
        :type gender: str
        :param bio: The bio of this UserInput.  # noqa: E501
        :type bio: str
        :param location: The location of this UserInput.  # noqa: E501
        :type location: UserLocation
        """
        self.swagger_types = {
            'name': str,
            'email': str,
            'password': str,
            'age': int,
            'gender': str,
            'bio': str,
            'location': UserLocation
        }

        self.attribute_map = {
            'name': 'name',
            'email': 'email',
            'password': 'password',
            'age': 'age',
            'gender': 'gender',
            'bio': 'bio',
            'location': 'location'
        }
        self._name = name
        self._email = email
        self._password = password
        self._age = age
        self._gender = gender
        self._bio = bio
        self._location = location

    @classmethod
    def from_dict(cls, dikt) -> 'UserInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserInput of this UserInput.  # noqa: E501
        :rtype: UserInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this UserInput.


        :return: The name of this UserInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this UserInput.


        :param name: The name of this UserInput.
        :type name: str
        """

        self._name = name

    @property
    def email(self) -> str:
        """Gets the email of this UserInput.


        :return: The email of this UserInput.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UserInput.


        :param email: The email of this UserInput.
        :type email: str
        """

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this UserInput.


        :return: The password of this UserInput.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this UserInput.


        :param password: The password of this UserInput.
        :type password: str
        """

        self._password = password

    @property
    def age(self) -> int:
        """Gets the age of this UserInput.


        :return: The age of this UserInput.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this UserInput.


        :param age: The age of this UserInput.
        :type age: int
        """

        self._age = age

    @property
    def gender(self) -> str:
        """Gets the gender of this UserInput.


        :return: The gender of this UserInput.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this UserInput.


        :param gender: The gender of this UserInput.
        :type gender: str
        """
        allowed_values = ["male", "female", "other"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def bio(self) -> str:
        """Gets the bio of this UserInput.


        :return: The bio of this UserInput.
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio: str):
        """Sets the bio of this UserInput.


        :param bio: The bio of this UserInput.
        :type bio: str
        """

        self._bio = bio

    @property
    def location(self) -> UserLocation:
        """Gets the location of this UserInput.


        :return: The location of this UserInput.
        :rtype: UserLocation
        """
        return self._location

    @location.setter
    def location(self, location: UserLocation):
        """Sets the location of this UserInput.


        :param location: The location of this UserInput.
        :type location: UserLocation
        """

        self._location = location