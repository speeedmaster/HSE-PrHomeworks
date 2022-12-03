"""Disjoint set union implementation and tests"""
import random

class DSU:
    """DSU abstract class"""
    def __init__(self, size: int) -> None:
        pass

    def union_sets(self, first: int, second: int) -> int:
        """Method to join two sets"""

    def get_representative(self, member: int) -> int:
        """Method to get set parent"""

    def check_equivalence(self, first: int, second: int) -> bool:
        """Method to check if two members belong to the same class"""

    def get_set_cnt(self) -> int:
        """Method to get current number of sets"""

    def get_set_size(self, member) -> int:
        """Method to get size of set member belongs to"""


class NaiveDSU(DSU):
    """DSU naive class implementation"""
    def __init__(self, size: int) -> None:
        self._set_cnt = size                      # number of disjoint sets
        self._parents = list(range(size))           # direct parent number
        self._sizes = [1] * size                    # subtree size

    def union_sets(self, first: int, second: int):
        first_set = self.get_representative(first)
        second_set = self.get_representative(second)
        if first_set == second_set:
            # already in the same set
            return first_set
        self._parents[first_set] = second_set
        self._set_cnt -= 1
        self._sizes[second_set] += self._sizes[first_set]
        return second_set

    def get_representative(self, member: int) -> int:
        if self._parents[member] == member:
            return member
        return self.get_representative(self._parents[member])

    def check_equivalence(self, first: int, second: int) -> bool:
        return self.get_representative(first) == self.get_representative(second)

    def get_set_cnt(self) -> int:
        return self._set_cnt

    def get_set_size(self, member) -> int:
        return self._sizes[self.get_representative(member)]

class OptimizedDSU(DSU):
    """DSU class implementation with rank optimization and path compression"""
    def __init__(self, size: int) -> None:
        self._set_cnt = size                      # number of disjoint sets
        self._parents = list(range(size))           # direct parent number
        self._sizes = [1] * size                    # subtree size
        self._depths = [1] * size

    def union_sets(self, first: int, second: int):
        first_set = self.get_representative(first)
        second_set = self.get_representative(second)
        if first_set == second_set:
            # already in the same set
            return first_set
        if self._depths[first_set] > self._depths[second_set]: # union by rank
            first_set, second_set = second_set, first_set
        self._parents[first_set] = second_set
        self._set_cnt -= 1
        self._sizes[second_set] += self._sizes[first_set]
        self._depths[second_set] = max(
            self._depths[second_set], self._depths[first_set] + 1)
        return second_set

    def get_representative(self, member: int) -> int:
        if self._parents[member] != member:
            # path compression
            self._parents[member] = self.get_representative(self._parents[member])
        return self._parents[member]

    def check_equivalence(self, first: int, second: int) -> bool:
        return self.get_representative(first) == self.get_representative(second)

    def get_set_cnt(self) -> int:
        return self._set_cnt

    def get_set_size(self, member) -> int:
        return self._sizes[self.get_representative(member)]


class RandomizedDSU(DSU):
    """DSU class implementation with random parent choise for join"""
    def __init__(self, size: int) -> None:
        self._set_cnt = size                      # number of disjoint sets
        self._parents = list(range(size))           # direct parent number
        self._sizes = [1] * size                    # subtree size

    def union_sets(self, first: int, second: int):
        first_set = self.get_representative(first)
        second_set = self.get_representative(second)
        if first_set == second_set:
            # already in the same set
            return first_set
        if bool(random.getrandbits(1)): # union by random
            first_set, second_set = second_set, first_set
        self._parents[first_set] = second_set
        self._set_cnt -= 1
        self._sizes[second_set] += self._sizes[first_set]
        return second_set

    def get_representative(self, member: int) -> int:
        if self._parents[member] != member:
             # path compression
            self._parents[member] = self.get_representative(self._parents[member])
        return self._parents[member]

    def check_equivalence(self, first: int, second: int) -> bool:
        return self.get_representative(first) == self.get_representative(second)

    def get_set_cnt(self) -> int:
        return self._set_cnt

    def get_set_size(self, member) -> int:
        return self._sizes[self.get_representative(member)]


def check_dsu(dsu_class):
    """Function to test DSU implementation"""
    dsu = dsu_class(10) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    assert dsu.get_set_cnt() == 10

    for i in range(10):
        assert i == dsu.get_representative(i)
        assert dsu.get_set_size(i) == 1

    dsu.union_sets(0, 1) # {0, 1} 2, 3, 4, 5, 6, 7, 8, 9, 10
    assert dsu.get_set_cnt() == 9
    assert dsu.check_equivalence(0, 1)
    assert dsu.get_set_size(0) == 2

    dsu.union_sets(0, 2) # {0, 1, 2} 3, 4, 5, 6, 7, 8, 9, 10
    assert dsu.get_set_cnt() == 8
    assert dsu.check_equivalence(0, 2)
    assert dsu.check_equivalence(1, 2)
    assert dsu.get_set_size(0) == 3

    dsu.union_sets(3, 4) # {0, 1, 2} {3, 4} 5, 6, 7, 8, 9, 10
    assert dsu.get_set_cnt() == 7
    assert dsu.check_equivalence(3, 4)
    assert dsu.get_set_size(3) == 2

    dsu.union_sets(3, 5) # {0, 1, 2} {3, 4, 5} 6, 7, 8, 9, 10
    assert dsu.get_set_cnt() == 6
    assert dsu.check_equivalence(3, 5)
    assert dsu.check_equivalence(4, 5)
    assert dsu.get_set_size(3) == 3

    dsu.union_sets(6, 5) # {0, 1, 2} {3, 4, 5, 6} 7, 8, 9, 10
    assert dsu.get_set_cnt() == 5
    assert dsu.check_equivalence(3, 6)
    assert dsu.check_equivalence(4, 6)
    assert dsu.check_equivalence(5, 6)
    assert dsu.get_set_size(6) == 4

    assert not dsu.check_equivalence(2, 3)

    dsu.union_sets(0, 6) # {0, 1, 2, 3, 4, 5, 6} {7, 8} 9, 10
    assert dsu.get_set_cnt() == 4
    assert dsu.check_equivalence(1, 6)
    assert dsu.check_equivalence(2, 6)
    assert dsu.check_equivalence(0, 3)
    assert dsu.get_set_size(0) == 7

    print('OK', dsu_class.__name__)


if __name__ == '__main__':
    check_dsu(NaiveDSU)
    check_dsu(OptimizedDSU)
    check_dsu(RandomizedDSU)
