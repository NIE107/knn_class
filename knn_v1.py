class MyDataFrame:
    def __init__(self):
        self.names = []
        self.x_values = []
        self.y_values = []
        self.x_scaled = []
        self.y_scaled = []
        self.punctual: list[bool] = []
        self.k = 3

    def read_file(self, file_name: str) -> None:
        with open(file_name, "r") as raw_file:
            rows = raw_file.read().strip().splitlines()

        for row in rows:
            data = row.split(",")
            self.names.append(data[0])
            self.x_values.append(int(data[1]))
            self.y_values.append(int(data[2]))
            self.punctual.append(data[3][0] == "p")

        self.scale()

    def scale(self) -> None:
        min_x = min(self.x_values)
        range_x = max(self.x_values) - min_x
        self.x_scaled = [(x - min_x) / range_x for x in self.x_values]

        min_y = min(self.y_values)
        range_y = max(self.y_values) - min_y
        self.y_scaled = [(y - min_y) / range_y for y in self.y_values]

    def get_distances(self, reverence_point: tuple[float, float]) -> list:
        return [(reverence_point[0] - x) ** 2 + (reverence_point[1] - y) ** 2
                for x, y in zip(self.x_scaled, self.y_scaled)]

    def is_punctual(self, reverence_point: tuple[float, float]) -> bool:
        min_x = min(self.x_values)
        range_x = max(self.x_values) - min_x
        min_y = min(self.y_values)
        range_y = max(self.y_values) - min_y

        normalized_reverence_point = ((reverence_point[0] - min_x) / range_x,
                                      (reverence_point[1] - min_y) / range_y)

        punctual_count = 0
        used_indexes = set()
        distances = self.get_distances(normalized_reverence_point)

        k = self.k if self.k <= len(self.punctual) else len(self.punctual)
        for _ in range(k):
            min_distance = float("inf")
            index_of_min = None

            for index, distance in enumerate(distances):
                if index in used_indexes:
                    continue

                if distance < min_distance:
                    min_distance = distance
                    index_of_min = index

            used_indexes.add(index_of_min)
            if self.punctual[index_of_min]:
                punctual_count += 1

        return punctual_count == self.k


if __name__ == "__main__":
    test_frame = MyDataFrame()
    test_frame.read_file(r"C:\Users\Lennart\Desktop\data1.csv")
    print(test_frame.is_punctual((5, 50)))
