import connexion
import six

from swagger_server.models.match import Match  # noqa: E501
from swagger_server.models.match_input import MatchInput  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_input import UserInput  # noqa: E501
from swagger_server import util


def users_get():  # noqa: E501
    """List all users

    Retrieve a list of all users in the database. # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def users_post(body):  # noqa: E501
    """Create a new user

    Create a new user with the given user data. # noqa: E501

    :param body: User data to be created.
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = UserInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_user_id_get(user_id):  # noqa: E501
    """Retrieve a user by ID

    Retrieve a user with the given user ID. # noqa: E501

    :param user_id: ID of user to retrieve
    :type user_id: int

    :rtype: User
    """
    return 'do some magic!'


def users_user_id_matches_get(user_id):  # noqa: E501
    """Retrieve a user&#x27;s matches

    Retrieve a list of all matches for the user with the given user ID. # noqa: E501

    :param user_id: ID of user to retrieve matches for
    :type user_id: int

    :rtype: List[Match]
    """
    return 'do some magic!'


def users_user_id_matches_post(body, user_id):  # noqa: E501
    """Create a new match

    Create a new match between two users. # noqa: E501

    :param body: Match data to be created.
    :type body: dict | bytes
    :param user_id: ID of user creating the match
    :type user_id: int

    :rtype: Match
    """
    if connexion.request.is_json:
        body = MatchInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_user_id_put(body, user_id):  # noqa: E501
    """Update a user

    Update a user with the given user ID and data. # noqa: E501

    :param body: User data to be updated.
    :type body: dict | bytes
    :param user_id: ID of user to update
    :type user_id: int

    :rtype: User
    """
    if connexion.request.is_json:
        body = UserInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
