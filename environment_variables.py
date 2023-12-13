import os
from configparser import ConfigParser
import yaml


with open("config.yaml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
        user = config['USERNAME']
        print(user)

    except yaml.YAMLError as exc:
        print(exc)


# cars = {
#     'BMW': 40000,
#     'Dacia': 18000,
#     'Toyota': 24000
# }
#
# # print(cars['asdasda'])
# # print(cars.get('Toyota', 'Not a valid key'))
# # # print(dir(cars))
# #
# #
# # print(os.environ.get('USERNAME', 'not a variable'))
# var = input('enter var: ')
#
# while True:
#     try:
#         print(os.environ[var])
#         break
#     except KeyError as e:
#         print(f'key does not exist - {e}')
#         var = input('enter var: ')