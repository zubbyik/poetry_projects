import json
import pathlib

# print(pathlib.Path(__file__))

# print('Hello')
# print(dir(pathlib.Path()))
# print(pathlib.Path().absolute())
# print(pathlib.Path().joinpath('/src/data.json'))
with open(pathlib.Path().joinpath('src/data.json')) as json_file:
    dt = json.load(json_file)
    value_count = []
    for data in dt:
        for key, value in data.items():
            # if type(value) is dict:
            #     for key, value in value.items():
            #         print(
            #             f'The key is {key} and the value is {value}'.format(key, value))
            # else:
            #     print(
            #         f'The key is {key} and the value is {value}'.format(key, value))
            if 'email' in key:
                value_count.append(key)
    print(len(value_count))
