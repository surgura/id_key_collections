import pytest
from id_key_collections import IdKeyDict


@pytest.fixture
def test_dict() -> IdKeyDict[str, float]:
    """
    Create an empty IdKeyDict[str, float] before each test case.

    :returns: The initialized valueect.
    """
    return IdKeyDict[str, float]()


def test_set_and_get(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the __setitem__ and __getitem__ methods.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    key = "key"
    value = 0.1234
    test_dict[key] = value
    assert test_dict[key] == value


def test_contains(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the __contains__ method.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    key = "key"
    value = 0.1234
    assert key not in test_dict
    test_dict[key] = value
    assert key in test_dict


def test_del(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the __delitem__ method.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    key = "key"
    value = 0.1234
    test_dict[key] = value
    del test_dict[key]
    assert key not in test_dict


def test_len(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the __len__ method.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    key1 = "key1"
    value1 = 0.1
    key2 = "key2"
    value2 = 0.2

    assert len(test_dict) == 0
    test_dict[key1] = value1
    test_dict[key2] = value2
    assert len(test_dict) == 2


def test_iter(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the __iter__ method.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    keys = ["key1", "key2", "key3"]
    values = [0.1, 0.2, 0.3]
    for key, value in zip(keys, values):
        test_dict[key] = value
    assert set(test_dict) == set(keys)


def test_keys(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the keys method.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    keys = ["key1", "key2", "key3"]
    values = [0.1, 0.2, 0.3]
    for key, value in zip(keys, values):
        test_dict[key] = value
    assert set(test_dict.keys()) == set(keys)


def test_values(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the values method.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    keys = ["key1", "key2", "key3"]
    values = [0.1, 0.2, 0.3]
    for key, value in zip(keys, values):
        test_dict[key] = value
    assert set(test_dict.values()) == set(values)


def test_items(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the items method.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    keys = ["key1", "key2", "key3"]
    values = [0.1, 0.2, 0.3]
    for key, value in zip(keys, values):
        test_dict[key] = value
    assert set(test_dict.items()) == set(zip(keys, values))


def test_get(test_dict: IdKeyDict[str, float]) -> None:
    """
    Test the get method.

    :param test_dict: An empty IdKeyDict[str, float].
    """
    key1 = "key1"
    value1 = 0.1

    assert test_dict.get(key1) is None
    test_dict[key1] = value1
    assert test_dict.get(key1) == value1
