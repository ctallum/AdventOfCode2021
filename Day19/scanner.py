from typing import List, List, Tuple, Set
import copy


class Scanner():
    def __init__(self, coordinates: List[List[int]], origin=False) -> None:
        self.coordinates = coordinates
        self.coordinates_varaitions = self.get_coord_variants()
        self.network = self.create_network()
        if origin:
            self.solved = True
            self.location = (0, 0, 0)
            self.solved_tranform = 0
            self.get_solved_coords()
        else:
            self.solved = False
            self.location = None
            self.solved_tranform = None

    def create_network(self) -> List[List[Set[Tuple[int]]]]:
        network = []
        for coordinate_variation in self.coordinates_varaitions:
            coordinate_variation_network = []
            for coord in coordinate_variation:
                coord_network = set()
                for other_coord in coordinate_variation:
                    coord_network.add(
                        tuple([a - other_coord[idx] for idx, a in enumerate(coord)]))
                coordinate_variation_network.append(coord_network)
            network.append(coordinate_variation_network)
        return network

    def get_coord_variants(self) -> List[List[List[int]]]:
        coord_variants = []
        possible_rotations = self.generate_rotations()

        for rotation in possible_rotations:
            new_variant = copy.deepcopy(self.coordinates)

            for idx, coord in enumerate(new_variant):
                new_coord = [[], [], []]
                new_coord[0] = coord[abs(rotation[0]) - 1]
                new_coord[1] = coord[abs(rotation[1]) - 1]
                new_coord[2] = coord[abs(rotation[2]) - 1]
                new_coord = [
                    a if rotation[idx] > 0 else -a for idx,
                    a in enumerate(new_coord)]
                new_variant[idx] = new_coord

            coord_variants.append(new_variant)

        return coord_variants

    def get_solved_coords(self) -> None:
        self.solved_coords = copy.deepcopy(
            self.coordinates_varaitions[self.solved_tranform])
        for idx, coord_set in enumerate(self.solved_coords):
            coord_set[0] += self.location[0]
            coord_set[1] += self.location[1]
            coord_set[2] += self.location[2]

    @staticmethod
    def generate_rotations() -> List[List[int]]:
        possible_swaps = [
            [1, 2, 3],
            [1, -2, -3],
            [-1, 2, -3],
            [-1, -2, 3],
            [1, 3, -2],
            [1, -3, 2],
            [-1, 3, 2],
            [-1, -3, -2],
            [2, 1, -3],
            [2, -1, 3],
            [-2, 1, 3],
            [-2, -1, -3],
            [2, 3, 1],
            [2, -3, -1],
            [-2, 3, -1],
            [-2, -3, 1],
            [3, 1, 2],
            [3, -1, -2],
            [-3, 1, -2],
            [-3, -1, 2],
            [3, 2, -1],
            [3, -2, 1],
            [-3, 2, 1],
            [-3, -2, -1]
        ]
        return possible_swaps
