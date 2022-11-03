class Range:
    def __init__(self, begin = 0, end = 0):
        assert isinstance(begin, int)
        assert isinstance(end, int)
        assert begin <= end
        self.begin = begin
        self.end = end

    def intersection(self, other):
        assert self.intersects_with(other)
        return Range(max(self.begin, other.begin), min(self.end, other.end))

    def union(self, other):
        assert self.intersects_with(other)
        return Range(min(self.begin, other.begin), max(self.end, other.end))

    def empty(self):
        return self.begin == self.end

    def contains(self, point):
        if isinstance(point, int):
            return self.begin <= point and self.end >= point
        if isinstance(point, Range):
            return self.begin <= point.begin and self.end >= point.end

    def is_equal_to(self, other):
        return self.begin == other.begin and self.end == other.end

    def intersects_with(self, other):
        max_left = max(self.begin, other.begin)
        min_right = min(self.end, other.end)
        return max_left <= min_right

    def points(self):
        return list(range(self.begin, self.end + 1))

    def min(self):
        return self.begin
    
    def max(self):
        return self.end

    def to_string(self):
        return f'[{self.begin}; {self.end}]'
