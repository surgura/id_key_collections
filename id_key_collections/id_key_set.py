"""Contains the IdKeySet class."""

from __future__ import annotations

from typing import AbstractSet, Dict, Generic, Iterator, MutableSet, TypeVar

_TValue = TypeVar("_TValue")


class IdKeySet(MutableSet[_TValue], Generic[_TValue]):
    """
    A set that uses the id of objects as keys.

    Otherwise, behaves exactly like a standard set.
    Object are explicitly stored to prevent garbage collection.
    """

    _inner_mapping: Dict[int, _TValue]
    """The internal mapping of object IDs to values."""

    def __init__(self) -> None:
        """Initialize an empty IdKeyDict instance."""
        self._inner_mapping = {}

    def __contains__(self, item: object) -> bool:
        """
        Check if the item is in the set.

        :param item: The item to check.
        :returns: True if item is in the set, False otherwise.
        """
        return id(item) in self._inner_mapping

    def __iter__(self) -> Iterator[_TValue]:
        """
        Return an iterator over the elements in the set.

        :returns: An iterator over the keys.
        """
        return (v for v in self._inner_mapping.values())

    def __len__(self) -> int:
        """
        Return the number of elements in the set.

        :returns: The number of items.
        """
        return len(self._inner_mapping)

    def add(self, item: _TValue) -> None:
        """
        Add an item to the set.

        :param item: The item to add.
        """
        self._inner_mapping[id(item)] = item

    def discard(self, item: _TValue) -> None:
        """
        Remove an item from the set.

        Does nothing if item is not in the set.

        :param item: The item to remove.
        """
        self._inner_mapping.pop(id(item), None)  # type: ignore[arg-type] # None is actually valid, but this is not properly typed.

    def __le__(self, other: AbstractSet[_TValue]) -> bool:
        """
        Check if this set is a subset of another set.

        :param other: The set to compare against.
        :returns: True if this set is a subset, False otherwise.
        :raises TypeError: If the other set is not an IdKeySet.
        """
        if not isinstance(other, IdKeySet):
            raise TypeError("Can only compare with another IdKeySet.")
        return all(k in other._inner_mapping for k in self._inner_mapping.keys())

    def __lt__(self, other: AbstractSet[_TValue]) -> bool:
        """
        Check if this set is a proper subset of another set.

        :param other: The set to compare against.
        :returns: True if this set is a proper subset, False otherwise.
        :raises TypeError: If the other set is not an IdKeySet.
        """
        if not isinstance(other, IdKeySet):
            raise TypeError("Can only compare with another IdKeySet.")
        return (
            all(k in other._inner_mapping for k in self._inner_mapping.keys())
            and self._inner_mapping != other._inner_mapping
        )

    def __eq__(self, other: object) -> bool:
        """
        Check if this set is equal to another set.

        :param other: The set to compare against.
        :returns: True if the sets are equal, False otherwise.
        :raises TypeError: If the other set is not an IdKeySet.
        """
        if not isinstance(other, IdKeySet):
            raise TypeError("Can only compare with another IdKeySet.")
        return self._inner_mapping.keys() == other._inner_mapping.keys()

    def __gt__(self, other: AbstractSet[_TValue]) -> bool:
        """
        Check if this set is a proper superset of another set.

        :param other: The set to compare against.
        :returns: True if this set is a proper superset, False otherwise.
        :raises TypeError: If the other set is not an IdKeySet.
        """
        if not isinstance(other, IdKeySet):
            raise TypeError("Can only compare with another IdKeySet.")
        return (
            all(k in self._inner_mapping for k in other._inner_mapping.keys())
            and self._inner_mapping != other._inner_mapping
        )

    def __ge__(self, other: AbstractSet[_TValue]) -> bool:
        """
        Check if this set is a superset of another set.

        :param other: The set to compare against.
        :returns: True if this set is a superset, False otherwise.
        :raises TypeError: If the other set is not an IdKeySet.
        """
        if not isinstance(other, IdKeySet):
            raise TypeError("Can only compare with another IdKeySet.")
        return all(k in self._inner_mapping for k in other._inner_mapping.keys())

    def __or__(  # type:ignore[override] # Mypy complains, but I'm pretty sure my signature is correct. Maybe a bug?
        self, other: AbstractSet[_TValue]
    ) -> IdKeySet[_TValue]:
        """
        Return the union of two sets as a new set.

        :param other: Another IdKeySet instance.
        :returns: A new IdKeySet instance containing all elements from both sets.
        :raises TypeError: If the other set is not an IdKeySet.
        """
        if not isinstance(other, IdKeySet):
            raise TypeError("Can only operate with another IdKeySet.")
        new_set = IdKeySet[_TValue]()
        new_set._inner_mapping.update(self._inner_mapping)
        new_set._inner_mapping.update(other._inner_mapping)
        return new_set

    def __and__(self, other: AbstractSet[_TValue]) -> IdKeySet[_TValue]:
        """
        Return the intersection of two sets as a new set.

        :param other: Another IdKeySet instance.
        :returns: A new IdKeySet instance containing only the elements present in both sets.
        :raises TypeError: If the other set is not an IdKeySet.
        """
        if not isinstance(other, IdKeySet):
            raise TypeError("Can only operate with another IdKeySet.")
        new_set = IdKeySet[_TValue]()
        for k, v in self._inner_mapping.items():
            if k in other._inner_mapping:
                new_set.add(v)
        return new_set

    def __sub__(self, other: AbstractSet[_TValue]) -> IdKeySet[_TValue]:
        """
        Return the difference of two sets as a new set.

        :param other: Another IdKeySet instance.
        :returns: A new IdKeySet instance containing only the elements present in the first set and not in the second.
        :raises TypeError: If the other set is not an IdKeySet.
        """
        if not isinstance(other, IdKeySet):
            raise TypeError("Can only operate with another IdKeySet.")
        new_set = IdKeySet[_TValue]()
        for k, v in self._inner_mapping.items():
            if k not in other._inner_mapping:
                new_set.add(v)
        return new_set
