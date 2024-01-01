
import csv

class game_map :
    def __init__(self, map) :
        self.map_file = map
        self.map_array = []

    def read_map_to_array(self) :
        with open(self.map_file, 'r') as f :
            csvreader = csv.reader(f)
            next(csvreader)

            for row in csvreader :
                self.map_array.append(row)

        return self.map_array