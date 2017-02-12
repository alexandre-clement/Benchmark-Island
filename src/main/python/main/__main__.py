import os
from main import *
from main.benchmark import Benchmark
from main.run import play_all_map


def main():
    play_all_map()
    for file in os.listdir(Path.source_path):
        if file.endswith('.json'):
            print('file "' + file + '" : ')
            with open(Path.source_path + file) as json_file:
                json_object = json.load(json_file)
                benchmark = Benchmark(json_object)
            print("\tbudget used  : ", benchmark.budget_used())
            print("\tcreek found  : ", benchmark.find_creek())
            print("\tsite found   : ", benchmark.find_emergency_site())
            print("\tcontracts    : ", benchmark.completed_contracts())

            print("_" * 90)
            print()


if __name__ == '__main__':
    main()
