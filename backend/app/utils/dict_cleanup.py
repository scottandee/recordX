#!/usr/bin/python3
"""This script contains a method that
cleans up an objects dictionary
representation
"""


def dict_cleanup(obj):
    """This function takes in an obj/
    a resource and returns the cleaned up
    dictionary representation
    """

    dic = obj.__dict__.copy()
    if "_sa_instance_state" in dic.keys():
        del dic["_sa_instance_state"]
    return dic
