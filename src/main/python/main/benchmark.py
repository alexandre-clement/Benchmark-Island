from main import *
from main.site import get_site
from main.creek import get_creeks
from main.contract import completed_contract


class Benchmark:

    def __init__(self, json_object):
        self.json_object = json_object
        self.step_cost_table = self.get_step_cost_table()

    def get_step_cost_table(self):
        cost = 0
        step_cost_table = [cost]
        for answer in range(2, len(self.json_object), 2):
            cost += self.json_object[answer].get(JsonArguments.data).get(JsonArguments.cost)
            step_cost_table.append(cost)
        return step_cost_table

    def find_creek(self):
        return [self.step_cost_table[creek.step] for creek in get_creeks(self.json_object)]

    def find_emergency_site(self):
        return [self.step_cost_table[site.step] for site in get_site(self.json_object)]

    def find_land(self):
        pass

    def completed_contracts(self):
        return [(exploited, self.step_cost_table[step]) for (exploited, step) in completed_contract(self.json_object).items()]


if __name__ == '__main__':
    with open(Path.source_file) as source:
        json_test = json.load(source)
        benchmark = Benchmark(json_test)
        print(benchmark.completed_contracts())
