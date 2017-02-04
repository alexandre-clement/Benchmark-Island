from main import *


class Creek:

    def __init__(self, identity="", step=0):
        self.step = step
        self.identity = identity

    def __str__(self):
        return "{%s : %s}" % (self.identity, self.step)

    def __repr__(self):
        return self.__str__()


def get_creeks(json_object):
    creeks = []
    for answer in range(2, len(json_object), 2):
        json_creek = json_object[answer].get(JsonArguments.data).get(JsonArguments.extras).get(JsonArguments.creek)
        if json_creek is not None and len(json_creek) != 0:
            creeks.append(Creek(json_creek, int(answer / 2)))
    return creeks


if __name__ == '__main__':
    with open(Path.source_file) as source:
        print(get_creeks(json.load(source)))
