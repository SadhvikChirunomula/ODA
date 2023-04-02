import connexion
import six

from swagger_server.models.like import Like  # noqa: E501
from swagger_server.models.new_like import NewLike  # noqa: E501
from swagger_server.models.new_user import NewUser  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def users_get():  # noqa: E501
    """Get all users

     # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def users_id_get(id):  # noqa: E501
    """Get a user by ID

     # noqa: E501

    :param id: The ID of the user to retrieve
    :type id: int

    :rtype: User
    """
    return 'do some magic!'


def users_id_likes_get(id):  # noqa: E501
    """Get all likes for a user

     # noqa: E501

    :param id: The ID of the user to retrieve likes for
    :type id: int

    :rtype: List[Like]
    """
    return 'do some magic!'


def users_id_likes_post(body, id):  # noqa: E501
    """Add a like for a user

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: The ID of the user to add a like for
    :type id: int

    :rtype: Like
    """
    if connexion.request.is_json:
        body = NewLike.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_id_put(body, id):  # noqa: E501
    """Update a user by ID

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: The ID of the user to update
    :type id: int

    :rtype: User
    """
    if connexion.request.is_json:
        body = NewUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_post(body):  # noqa: E501
    """Create a new user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = NewUser.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
