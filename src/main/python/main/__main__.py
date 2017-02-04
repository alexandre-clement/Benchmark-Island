import os
from main import *
from main.benchmark import Benchmark


def main():
    for file in os.listdir(Path.source_path):
        if file.endswith('.json'):
            with open(Path.source_path + file) as json_file:
                json_object = json.load(json_file)
                benchmark = Benchmark(json_object)
            print('file "' + file + '" : ')
            print("\tcreek found  : ", benchmark.find_creek())
            print("\tsite found   : ", benchmark.find_emergency_site())
            print("\tcontracts    : ", benchmark.completed_contracts())
            print("\tbudget used  : ", benchmark.get_percentage_budget_used())
            print("_" * 90)
            print()


if __name__ == '__main__':
    main()
