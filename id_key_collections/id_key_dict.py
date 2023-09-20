"""Contains the IdKeyDict class."""

from typing import Dict, Generic, Iterator, MutableMapping, Optional, Tuple, TypeVar

_TKey = TypeVar("_TKey")
_TValue = TypeVar("_TValue")


class IdKeyDict(MutableMapping[_TKey, _TValue], Generic[_TKey, _TValue]):
    """
    A dictionary that uses the id of objects as keys.

    Otherwise, behaves exactly like a standard set.
    Key objects are explicitly stored to prevent garbage collection.
    """

    _inner_mapping: Dict[int, _TValue]
    """The internal mapping of object IDs to values."""

    _id_to_obj: Dict[int, _TKey]
    """A mapping from object IDs to the original keys."""

    def __init__(self) -> None:
        """Initialize an empty IdKeyDict instance."""
        self._inner_mapping = {}
        self._id_to_obj = {}

    def __setitem__(self, key: _TKey, value: _TValue) -> None:
        """
        Set the value for a given key.

        :param key: The key for which to set the value.
        :param value: The value to set.
        """
        obj_id = id(key)
        self._inner_mapping[obj_id] = value
        self._id_to_obj[obj_id] = key

    def __getitem__(self, key: _TKey) -> _TValue:
        """
        Retrieve the value for a given key.

        :param key: The key to look up.
        :returns: The value associated with the key.
        """
        return self._inner_mapping[id(key)]

    def __delitem__(self, key: _TKey) -> None:
        """
        Delete the item with the given key.

        :param key: The key of the item to delete.
        """
        obj_id = id(key)
        del self._inner_mapping[obj_id]
        del self._id_to_obj[obj_id]

    def __contains__(self, key: object) -> bool:
        """
        Check if the key is in the dictionary.

        :param key: The key to check.
        :returns: True if key is in the dictionary, False otherwise.
        """
        return id(key) in self._inner_mapping

    def __len__(self) -> int:
        """
        Get the number of items in the dictionary.

        :returns: The number of items.
        """
        return len(self._inner_mapping)

    def __iter__(self) -> Iterator[_TKey]:
        """
        Get an iterator over the keys.

        :returns: An iterator over the keys.
        """
        return iter(self._id_to_obj.values())

    def keys(  # type:ignore # According to MutableMapping this should return KeysView[_TKey], but I currently don't understand how I would implement that.
        self,
    ) -> Iterator[_TKey]:
        """
        Get an iterator over the keys.

        :returns: An iterator over the keys.
        """
        return iter(self._id_to_obj.values())

    def values(self) -> Iterator[_TValue]:  # type: ignore # Same as `keys`
        """
        Get an iterator over the values.

        :returns: An iterator over the values.
        """
        return (v for v in self._inner_mapping.values())

    def items(self) -> Iterator[Tuple[_TKey, _TValue]]:  # type: ignore # Same as `keys`.
        """
        Get an iterator over the items.

        Items are key-value pairs.

        :returns: An iterator over the items.
        """
        return ((self._id_to_obj[k], v) for k, v in self._inner_mapping.items())

    def get(self, key: _TKey) -> Optional[_TValue]:  # type: ignore # I don't fully understand the mypy error, but I think the problem is that I don't override all function signatures.
        """
        Retrieve the value for a given key without raising an exception if the key is not found.

        :param key: The key to look up.
        :returns: The value associated with the key or None if the key is not found.
        """
        return self._inner_mapping.get(id(key))
