from re import X
from randomize_template import RandomizeTemplate
import json

# Config

TEMPLATE = {
    'mode_of_transport': 'mystery machine',
    'fake_license_plate': None,
    'miles_to_the_mansion': 10,
    'are_you_scared': None,
    'probability_of_catching_the_ghost': 0.089,
    'which_door_is_the_ghost_behind': 'door #1'
}

RANDOM_MAP = {
    'fake_license_plate': {
        '__modify': True, 
        '__type': 'string', 
        '__options': {'length': 6}
    },
    'miles_to_the_mansion': {
        '__modify': True, 
        '__type': 'integer', 
        '__options': {'min': 1, 'max': 50}
    },
    'are_you_scared': {
        '__modify': True, 
        '__type': 'boolean'
    },
    'probability_of_catching_the_ghost': {
        '__modify': True, 
        '__type': 'float', 
        '__options': {'round': 10}
    },
    'which_door_is_the_ghost_behind': {
        '__modify': True, 
        '__type': ['door #2', 'door #3', 'door #4', 'RUH ROH RAGGY']
    }
}

TRIGGER = "__modify"

# Randomize a template

_random = RandomizeTemplate().randomize_template(
    template=TEMPLATE,
    random_map=RANDOM_MAP,
    trigger=TRIGGER
)

print(json.dumps(_random, indent=4), '\n\n')

# Randomize a template n times

_random_copies = RandomizeTemplate().copy_and_randomize_template(
    copies=10,
    template=TEMPLATE,
    random_map=RANDOM_MAP,
    trigger=TRIGGER
)

print(f'{len(_random_copies)} copies\n\n')

print(json.dumps(_random_copies, indent=4), '\n\n')