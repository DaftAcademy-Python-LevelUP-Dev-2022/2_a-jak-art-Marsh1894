def greeter(func):
    def aloha(*args):
        result = 'Aloha ' + func(*args)
        return result.title()
    return aloha


def sums_of_str_elements_are_equal(func):
    def calc(self):
        values = func(self)
        values = values.split()
        for i, j in enumerate(values):
            if "-" in j:
                values[i] = [-int(x) for x in j[1:]]
            else:
                values[i] = [int(x) for x in j[:]]
        summary_1 = sum(values[0])
        summary_2 = sum(values[1])

        if summary_1 == summary_2:
            return print(f'{summary_1} == {summary_2}')
        else:
            return print(f'{summary_1} != {summary_2}')
    return calc


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass

