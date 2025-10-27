class PointsForPlace:
    points = 0

    @staticmethod
    def get_points_for_place(place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            PointsForPlace.points = 101 - place
        return PointsForPlace.points

class PointsForMeters:
    points = 0

    @staticmethod
    def get_points_for_meters(meters):
        if meters > 0:
            PointsForMeters.points = meters // 2
        else:
            print('Количество метров не может быть отрицательным')
        return PointsForMeters.points

class TotalPoints(PointsForPlace, PointsForMeters):
    total = 0

    @staticmethod
    def get_total_points(place, meters):
        TotalPoints.total += PointsForPlace.get_points_for_place(place) + PointsForMeters.get_points_for_meters(meters)
        return TotalPoints.total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))