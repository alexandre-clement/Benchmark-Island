import os
from main import *
from main.benchmark import Benchmark
from main.run import play_all_map


def also_print_in_file(output_file, *args):
    print(*args)
    print(*args, file=output_file)


def main():
    play_all_map()
    result = open(os.path.join(Path.source_path, "result.txt"), "w")
    for file in os.listdir(Path.source_path):
        if file.endswith('.json'):
            also_print_in_file(result, 'file "' + file + '" : ')
            with open(Path.source_path + file) as json_file:
                json_object = json.load(json_file)
                benchmark = Benchmark(json_object)
            also_print_in_file(result, "\tbudget used  : ", benchmark.budget_used())
            also_print_in_file(result, "\tcreek found  : ", benchmark.find_creek())
            also_print_in_file(result, "\tsite found   : ", benchmark.find_emergency_site())
            also_print_in_file(result, "\tcontracts    : ", benchmark.completed_contracts())
            also_print_in_file(result, "_" * 90)
            also_print_in_file(result)


if __name__ == '__main__':
    main()
