from range import Range

import pytest

def test_init():
    r0 = Range()
    assert r0.begin == 0
    assert r0.end == 0
    r1 = Range(3, 19)
    assert r1.begin == 3
    assert r1.end == 19

def test_intersection():
    a = Range(1, 10)
    b = Range(5, 20)
    intersection = a.intersection(b)
    assert intersection.begin == 5
    assert intersection.end == 10

    a = Range(10, 15)
    b = Range(5, 20)
    intersection = a.intersection(b)
    assert intersection.begin == 10
    assert intersection.end == 15

def test_union():
    a = Range(1, 10)
    b = Range(5, 20)
    union = a.union(b)
    assert union.begin == 1
    assert union.end == 20

    a = Range(10, 15)
    b = Range(5, 20)
    union = a.union(b)
    assert union.begin == 5
    assert union.end == 20

def test_empty():
    a = Range()
    assert a.empty()

    b = Range(9, 9)
    assert b.empty()

    c = Range(1, 10)
    assert not c.empty()

def test_contains_point():
    a = Range(9, 9)
    assert a.contains(9)
    assert not a.contains(10)

    b = Range(1, 10)
    assert b.contains(9)
    assert b.contains(10)
    assert not b.contains(11)

def test_equals():
    a = Range()
    b = Range()
    assert a.is_equal_to(b)
    assert b.is_equal_to(a)

    a = Range(1, 1)
    b = Range(1, 1)
    assert a.is_equal_to(b)
    assert b.is_equal_to(a)

    a = Range(1, 10)
    b = Range(1, 10)
    assert a.is_equal_to(b)
    assert b.is_equal_to(a)

    a = Range(1, 1)
    b = Range(3, 3)
    assert not a.is_equal_to(b)
    assert not b.is_equal_to(a)

    a = Range(1, 10)
    b = Range(3, 3)
    assert not a.is_equal_to(b)
    assert not b.is_equal_to(a)

    a = Range(1, 10)
    b = Range(15, 20)
    assert not a.is_equal_to(b)
    assert not b.is_equal_to(a)

def test_intersects():
    a = Range()
    b = Range()
    assert a.intersects_with(b)
    assert b.intersects_with(a)

    a = Range(1, 1)
    b = Range(1, 1)
    assert a.intersects_with(b)
    assert b.intersects_with(a)

    a = Range(1, 10)
    b = Range(1, 10)
    assert a.intersects_with(b)
    assert b.intersects_with(a)

    a = Range(1, 1)
    b = Range(3, 3)
    assert not a.intersects_with(b)
    assert not b.intersects_with(a)

    a = Range(1, 10)
    b = Range(3, 3)
    assert a.intersects_with(b)
    assert b.intersects_with(a)

    a = Range(1, 15)
    b = Range(10, 20)
    assert a.intersects_with(b)
    assert b.intersects_with(a)

    a = Range(1, 20)
    b = Range(10, 15)
    assert a.intersects_with(b)
    assert b.intersects_with(a)

    a = Range(1, 5)
    b = Range(5, 10)
    assert a.intersects_with(b)
    assert b.intersects_with(a)

    a = Range(1, 5)
    b = Range(6, 10)
    assert not a.intersects_with(b)
    assert not b.intersects_with(a)

def test_contains_range():
    a = Range(9, 9)
    assert a.contains(Range(9, 9))
    assert not a.contains(Range(10, 10))
    assert not a.contains(Range(1, 10))
    assert not a.contains(Range(8, 9))
    assert not a.contains(Range(9, 15))
    assert not a.contains(Range(10, 15))

    b = Range(5, 10)
    assert b.contains(Range(9, 9))
    assert b.contains(Range(5, 5))
    assert b.contains(Range(10, 10))
    assert not b.contains(Range(11, 11))
    assert b.contains(Range(6, 9))
    assert b.contains(Range(5, 9))
    assert b.contains(Range(6, 10))
    assert not b.contains(Range(4, 9))
    assert not b.contains(Range(6, 11))
    assert not b.contains(Range(4, 10))
    assert not b.contains(Range(5, 11))
    assert not b.contains(Range(4, 5))
    assert not b.contains(Range(10, 11))
    assert not b.contains(Range(15, 20))
    assert not b.contains(Range(1, 2))

def test_range():
    a = Range()
    assert a.points() == [0]

    a = Range(10, 10)
    assert a.points() == [10]

    a = Range(5, 10)
    assert a.points() == [5, 6, 7, 8, 9, 10]

def test_min_max():
    a = Range()
    assert a.min() == 0
    assert a.max() == 0

    a = Range(10, 10)
    assert a.min() == 10
    assert a.max() == 10

    a = Range(5, 10)
    assert a.min() == 5
    assert a.max() == 10

def test_to_string():
    a = Range()
    assert a.to_string() == '[0; 0]'

    a = Range(10, 10)
    assert a.to_string() == '[10; 10]'

    a = Range(-1, 10)
    assert a.to_string() == '[-1; 10]'