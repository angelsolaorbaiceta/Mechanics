class OpenInterval:
    def __init__(self, start, end):
        if start > end:
            raise ValueError('start should be smaller than end')
        self.start = start
        self.end = end

    def length(self):
        return self.end - self.start

    def contains(self, value):
        return self.start < value < self.end

    def overlaps_interval(self, other):
        return self.contains(other.start) \
               or self.contains(other.end) \
               or other.contains(self.start) \
               or other.contains(self.end)

    def compute_overlap_with(self, other):
        if not self.overlaps_interval(other):
            return None

        return OpenInterval(
            max(self.start, other.start),
            min(self.end, other.end)
        )
