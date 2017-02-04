from main import *
from main.site import get_site
from main.creek import get_creeks
from main.contract import completed_contract


def not_verbose(callback):
    def wrapper(*args):
        return [element[-1] for element in callback(*args)]
    return wrapper


def beautiful_print(callback):
    def wrapper(*args):
        beautiful = ""
        for contract in callback(*args):
            beautiful += " \n\t\tContracts {:>10} is completed at {:>5} with consuming {:>3} of the budget".format(*contract)
        return beautiful
    return wrapper


class Benchmark:

    def __init__(self, json_object):
        self.json_object = json_object
        self.step_cost_table = self.get_step_cost_table()
        self.budget = json_object[0].get(JsonArguments.data).get(JsonArguments.budget)

    def get_step_cost_table(self):
        cost = 0
        step_cost_table = [cost]
        for answer in range(2, len(self.json_object), 2):
            cost += self.json_object[answer].get(JsonArguments.data).get(JsonArguments.cost)
            step_cost_table.append(cost)
        return step_cost_table

    def budget_used(self):
        return self.step_cost_table[-1]

    def get_percentage_budget_used(self):
        return "%d%%" % (self.budget_used() * 100 / self.budget)

    @not_verbose
    def find_creek(self):
        return [(creek.identity, self.step_cost_table[creek.step]) for creek in get_creeks(self.json_object)]

    @not_verbose
    def find_emergency_site(self):
        return [(site.identity, self.step_cost_table[site.step]) for site in get_site(self.json_object)]

    def find_land(self):
        pass

    @beautiful_print
    def completed_contracts(self):
        return [(exploited, contract.get_percentage(), self._get_step_percentage(contract.terminated)) for (exploited, contract) in completed_contract(self.json_object).items()]

    def _get_step_percentage(self, step):
        return "%d%%" % (self.step_cost_table[step] * 100 / self.budget)

if __name__ == '__main__':
    with open(Path.source_file) as source:
        json_test = json.load(source)
        benchmark = Benchmark(json_test)
        print(benchmark.completed_contracts())
