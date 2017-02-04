from main import *


class Contract:

    def __init__(self, contract_amount=0, contract_resource=Resource.wood, is_useful=True):
        self.is_useful = is_useful
        self.resource = contract_resource
        self.amount = contract_amount
        self.collected = 0
        self.terminated = False

    def __str__(self):
        return "{%s : %s}" % (self.resource, self.amount)

    def __repr__(self):
        return self.__str__()

    def collect(self, collected, step):
        if self.collected < self.amount <= self.collected + collected:
            self.terminated = step
        self.collected += collected

    def is_complete(self):
        return self.collected >= self.amount

    def get_percentage(self):
        return "%d%%" % (self.collected * 100 / self.amount)


def create_contract(contract):
    resource_amount = contract.get(JsonArguments.amount)
    resource_type = contract.get(JsonArguments.resource)
    return Contract(resource_amount, resource_type)


def get_contracts(json_object):
    header = json_object[0].get(JsonArguments.data)
    return [create_contract(contract) for contract in header.get(JsonArguments.contracts)]


def get_contracts_dict(contracts):
    return {contract.resource: contract for contract in contracts}


def completed_contract(json_object):
    contracts = get_contracts_dict(get_contracts(json_object))

    for answer in range(1, len(json_object), 2):
        action = json_object[answer].get(JsonArguments.data)
        result = json_object[answer+1].get(JsonArguments.data)

        if action.get(JsonArguments.action) == JsonArguments.exploit:
            exploited = action.get(JsonArguments.parameters).get(JsonArguments.resource)
            amount = result.get(JsonArguments.extras).get(JsonArguments.amount)

            if exploited in contracts:
                contracts[exploited].collect(amount, int(answer / 2))

    return contracts


if __name__ == '__main__':
    with open(Path.source_file) as source:
        print(get_contracts(json.load(source)))
