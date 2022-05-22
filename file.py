def greeter(func):
    def aloha(*args):
        result = 'Aloha ' + func(*args)
        return result.title()
    return aloha


def sums_of_str_elements_are_equal(func):
    def calc(self):
        values = func(self).split()
        for i, j in enumerate(values):
            if "-" in j:
                values[i] = [-int(x) for x in j[1:]]
            else:
                values[i] = [int(x) for x in j[:]]
        summary_1 = sum(values[0])
        summary_2 = sum(values[1])

        if summary_1 == summary_2:
            return f'{summary_1} == {summary_2}'
        elif summary_1 != summary_2:
            return f'{summary_1} != {summary_2}'
    return calc


def format_output(*required_keys):
    keys = required_keys

    def dict_decorator(func):
        def in_func(*args, **kwargs):
            in_values = func(*args, **kwargs)
            out_dict = dict()
            try:
                for key in keys:
                    if '__' in key:
                        list = key.split('__')
                        value = ''
                        for element in list:
                            value += in_values[element] + ' '
                        value = value[:-1]
                    else:
                        value = in_values[key]
                    if value == '':
                        value = 'Empty value'
                    out_dict.update({key: value})
                return out_dict
            except:
                raise ValueError
        return in_func
    return dict_decorator    





def add_method_to_instance(klass):
    def out_dec(func):
        def in_dec(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, in_dec)
        return in_dec
    return out_dec

