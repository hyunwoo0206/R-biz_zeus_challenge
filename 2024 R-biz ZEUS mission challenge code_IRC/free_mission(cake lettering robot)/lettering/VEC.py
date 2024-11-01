import math


class VECTOR:
    def __init__(self, scale=1):
        self.scale = scale

    def _scale_vector(self, vector):
        return [v * self.scale for v in vector]

    def draw_Horizontal(self, x, y, length):
        start = [x, y]
        end = [start[0] + self._scale_vector([length, 0])[0], start[1]]
        return start, end

    def draw_Vertical(self, x, y, length):
        start = [x, y]
        end = [start[0], start[1] + self._scale_vector([0, -length])[1]]
        return start, end

    def draw_diagonal_forward(self, x, y, len_x, len_y):
        start = [x, y]
        scaled = self._scale_vector([len_x, -len_y])
        end = [start[0] + scaled[0], start[1] + scaled[1]]
        return start, end

    def draw_diagonal_backward(self, x, y, len_x, len_y):
        start = [x, y]
        scaled = self._scale_vector([-len_x, -len_y])
        end = [start[0] + scaled[0], start[1] + scaled[1]]
        return start, end
    
    def draw_curve(self, x, y, radius, angle_start, angle_end, segments=10):
        points = []
        for i in range(segments + 1):
            theta = math.radians(
                angle_start + i * (angle_end - angle_start) / segments)
            point = [x + radius *
                     math.cos(theta), y + radius * math.sin(theta)]
            points.append([point[0], point[1]])
        return points
