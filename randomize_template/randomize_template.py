from applyrecursive import ApplyRecursive
from random import choice, choices, randint, random
import json
import string

class RandomizeTemplate():
    """
    Randomize values in a JSON / dict template

    @Version: 1.0
    @Author: Rob (analyticsdept)
    @GitHub: https://github.com/analyticsdept/py-randomizetemplate

    """

    def __init__(self) -> None:
        pass

    def copy_and_randomize_template(self, copies=1, template={}, random_map={}):
        """
        Create multiple copies of the template, randomizing fields in each copy based on the map

        `copies`: the number of randomized payloads to generate

        `template`: the template dictionary

        `random_map`: the random map
        """

        _copies = [self.randomize_template(template, random_map, x) for x in range(0, copies)]
        return _copies

    def randomize_template(self, template, random_map, seed=0):
        """
        Create a copy of the template, randomizing fields based on the map

        `template`: the template dictionary

        `random_map`: the random map
        """

        def random_field(field_type, _options={}):
            if field_type == "string":
                _length = _options.get('length', 16)
                return "".join(choices(string.ascii_uppercase + string.digits, k = randint(_length, _length)))
            
            if field_type == "integer":
                _min = _options.get('min', 0)
                _max = _options.get('max', 9999999999)
                return randint(_min, _max)
            
            if field_type == "float":
                _round = _options.get('round', None)
                return round(random(), _round) if _round else random()
            
            if field_type == "boolean":
                return choice([True, False])

        def make_random(*args, **kwargs):

            _data = kwargs.get('data')
            _type = kwargs.get('__type')
            _options = kwargs.get('__options', {})

            return choice(_type) if isinstance(_type, list) else random_field(_type, _options)

        _template = json.loads(json.dumps(template))

        _applyrecursive = ApplyRecursive(make_random, None, {'data': _template}, 'data')
        result = _applyrecursive.apply(random_map, "__modify", _template)
        return result
