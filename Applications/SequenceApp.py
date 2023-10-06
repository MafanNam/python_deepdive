import math


class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError("Polygon must have at least three sides")
        self._n = n
        self._R = R

    def __repr__(self):
        return f"Polygon(n={self._n}, R={self._R})"

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self._n == other._n and self._R == other._R

    @property
    def count_vertices(self):
        return self._n

    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)

    @property
    def area(self):
        return 1 / 2 * self._n * self.side_length * self.apothem

    @property
    def perimeter(self):
        return self._n * self.side_length


p = Polygon(4, 4)

# class Polygons:
#     def __init__(self, m, R):
#         if m < 3:
#             raise ValueError("Polygons must have at least three sides")
#         self._m = m
#         self._R = R
#         self._polygons = [Polygon(i, R) for i in range(3, m + 1)]
#
#     def __len__(self):
#         return self._m - 2
#
#     def __repr__(self):
#         return f"Polygons(m={self._m}, R={self._R})"
#
#     def __getitem__(self, item):
#         return self._polygons[item]
#
#     @property
#     def max_efficiency_polygon(self):
#         sorted_polygons = sorted(
#             self._polygons, key=lambda p: p.area / p.perimeter,
#             reverse=True)
#         return sorted_polygons[0]


# pol = Polygons(10, 1)
# print(pol.max_efficiency_polygon)

class PolygonsIter:
    def __init__(self, length, *, m, R):
        if m < 3:
            raise ValueError("PolygonsIter must have at least three sides")
        self._m = m
        self._R = R
        self.length = length
        # self._polygons = [Polygon(i, R) for i in range(3, m + 1)]
        self._i = 2

    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f"PolygonsIter(m={self._m}, R={self._R})"

    # def __getitem__(self, item):
    #     return self._polygons[item]

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self.length:
            raise StopIteration
        else:
            self._i += 1
            return Polygon(self._i, self._R)


    # @property
    # def max_efficiency_polygon(self):
    #     sorted_polygons = sorted(
    #         self._polygons, key=lambda p: p.area / p.perimeter,
    #         reverse=True)
    #     return sorted_polygons[0]


p = PolygonsIter(8, m=10, R=10)

for i in p:
    print(i)




