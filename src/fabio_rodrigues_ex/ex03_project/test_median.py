# -*- coding: utf-8 -*-
import pytest

__author__ = 'FABIO RODRIGUES PEREIRA'
__email__ = 'faro@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sdata = sorted(data)
    n = len(sdata)

    if not data:
        raise ValueError('Cannot empty list')

    return (sdata[n // 2] if n % 2 == 1

            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_median_one_element_list():
    """A test that the median function returns the correct value for
    a one-element list
    """
    one_element_list = [8]
    assert median(one_element_list) == 8


@pytest.mark.parametrize('odd_list, even_list, list_ordered, '
                         'list_rev_ordered, list_unordered, result',
                         [
                             [
                                 (1, 3, 5),
                                 (1, 2, 4, 5),
                                 (1, 2, 3, 4, 5),
                                 (5, 4, 3, 2, 1),
                                 (2, 1, 5, 4, 3),
                                 3
                             ]
                         ]
                         )
def test_several(odd_list, even_list, list_ordered,
                 list_rev_ordered, list_unordered, result):
    """Several tests that check that the correct median is returned for
    - Lists with odd numbers of elements
    - Lists with even numbers of elements
    - Ordered list,
    - List with reverse-ordered
    - List with unordered elements
    """
    assert median(odd_list) == median(even_list) == median(
        list_ordered) == median(list_rev_ordered) == median(
        list_unordered) == result


def test_empty_list_exception():
    """A test checking that requesting the median of an empty list
    raises a ValueError exception
    """
    with pytest.raises(ValueError) as e:
        median([])

    assert str(e.value) == 'Cannot empty list'


def test_original_data_unchanged():
    """A test that ensures that the median function leaves
    the original data unchanged.
    """
    data = [5, 3, 4, 1, 2]
    assert median(data) == 3 != data == [5, 3, 4, 1, 2]


def test_median_works_for_tuples_and_lists():
    """A test that ensures that the median function works for
    tuples as well as lists
    """
    data_list = [5, 3, 4, 1, 2]
    data_tuples = (5, 3, 4, 1, 2)
    assert median(data_list) == median(data_tuples) == 3
