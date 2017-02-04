from main import *


class Site:

    def __init__(self, identity="", step=0):
        self.step = step
        self.identity = identity

    def __str__(self):
        return "{%s : %s}" % (self.identity, self.step)

    def __repr__(self):
        return self.__str__()


def get_site(json_object):
    for answer in range(2, len(json_object), 2):
        json_site = json_object[answer].get(JsonArguments.data).get(JsonArguments.extras).get(JsonArguments.site)
        if json_site is not None and len(json_site) != 0:
            yield Site(json_site, int(answer / 2))


if __name__ == '__main__':
    with open(Path.source_file) as source:
        json_test = json.load(source)
        print(get_site(json_test))
