# coding: utf-8

"""
    Groupe PSA Connected Car - WEB API B2C

    *PSA B2C Connected Car API*  # Introduction This is the description of the *Groupe PSA Connected Car V2 API*. The speccification is  is based on **OpenAPI Specification version 3** and can be displayed via [ReDoc](https://github.com/Rebilly/ReDoc)a or [Swagger](http://swagger.io).   This API allows applications to fetch data from the connected Vehicles data platform. # Authentication PSA Connected Car APIs uses the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol for authentication and Authorization. any application require a valid [Access Token](https://tools.ietf.org/html/rfc6749#section-1.4) to access to user data. # Errors   Error codes returned by all REST APIs comply with the standard. Nevertheless, PSA Services (callers) need to have more complete data structures (even when the answer is not Http-OK) to better detail the type of error by providing application code, message and a debugging code(for investigation purposes). The http code of the response is managed by the protocol itself (in the header).      **Errors are  returned as a generic error response:**    * ```xError``` object model.       # noqa: E501

    OpenAPI spec version: 4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DoorsState(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'locked_state': 'list[str]',
        'opening': 'list[DoorsStateOpening]',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'locked_state': 'lockedState',
        'opening': 'opening',
        'updated_at': 'updatedAt'
    }

    def __init__(self, locked_state=None, opening=None, updated_at=None):  # noqa: E501
        """DoorsState - a model defined in Swagger"""  # noqa: E501

        self._locked_state = None
        self._opening = None
        self._updated_at = None
        self.discriminator = None

        if locked_state is not None:
            self.locked_state = locked_state
        if opening is not None:
            self.opening = opening
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def locked_state(self):
        """Gets the locked_state of this DoorsState.  # noqa: E501


        :return: The locked_state of this DoorsState.  # noqa: E501
        :rtype: list[str]
        """
        return self._locked_state

    @locked_state.setter
    def locked_state(self, locked_state):
        """Sets the locked_state of this DoorsState.


        :param locked_state: The locked_state of this DoorsState.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Unlocked", "Locked", "SuperLocked", "DriverDoorUnlocked", "CabinDoorsUnlocked", "CargoDoorsLocked", "CargoDoorsUnlocked", "RearDoorsUnlocked", "RearDoorsLocked"]  # noqa: E501
        if not set(locked_state).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `locked_state` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(locked_state) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._locked_state = locked_state

    @property
    def opening(self):
        """Gets the opening of this DoorsState.  # noqa: E501


        :return: The opening of this DoorsState.  # noqa: E501
        :rtype: list[DoorsStateOpening]
        """
        return self._opening

    @opening.setter
    def opening(self, opening):
        """Sets the opening of this DoorsState.


        :param opening: The opening of this DoorsState.  # noqa: E501
        :type: list[DoorsStateOpening]
        """

        self._opening = opening

    @property
    def updated_at(self):
        """Gets the updated_at of this DoorsState.  # noqa: E501


        :return: The updated_at of this DoorsState.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DoorsState.


        :param updated_at: The updated_at of this DoorsState.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DoorsState, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DoorsState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other