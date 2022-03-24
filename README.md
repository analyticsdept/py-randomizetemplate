# py-randomizetemplate

Randomize the values of target keys in a JSON template

&nbsp;

---

&nbsp;

## Usage

&nbsp;

---

&nbsp;

### **Template**

&nbsp;

Create a template dictionary - this should be modelled after your desired payload.

&nbsp;

```python
TEMPLATE = {
    'mode_of_transport': 'mystery machine',
    'fake_license_plate': None,
    'miles_to_the_mansion': 10,
    'are_you_scared': False,
    'probability_of_catching_the_ghost': 0.089,
    'which_door_is_the_ghost_behind': 'door #1'
}
```

&nbsp;

---

&nbsp;

### **Random Map**

&nbsp;

Create another dictionary that only contains the fields to be randomized.

Decide on a key to trigger a modification of a value - the example belows uses `__modify` and sets its value to `True`

&nbsp;

```python
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
```

&nbsp;

---

&nbsp;

#### **Types**

The `__type` field indicates a specific class to create a random value in.

&nbsp;

Supported types are:

- boolean
- float
- integer
- string

&nbsp;

_Note:_ A special use-case is passing a `list` into the `__type` field to force the randomizer to choose from the given list.

&nbsp;

---

&nbsp;

#### **Options**

The `__options` field can be used to pass in constraints for randomizing, though this is optional.

&nbsp;

Supported options are:

_Float_

```python
{
    'round': 6 # decimal precision of floating point
}
```

&nbsp;

_Integer_

```python
{
    'min': 0 # floor of random range
    'max': 10 # ceiling of random range
}
```

&nbsp;

_String_

```python
{
    'length': 16 # length of the random string
}
```

&nbsp;

---

&nbsp;

### **Methods**

&nbsp;

---

&nbsp;

#### **`randomize_template(template, random_map)`**

&nbsp;

**_Arguments_**:

`template`: the template dictionary

`random_map`: the random map

&nbsp;

---

&nbsp;

#### **`copy_and_randomize_template(copies, template, random_map)`**

&nbsp;

**_Arguments_**:

`copies`: the number of randomized payloads to generate

`template`: the template dictionary

`random_map`: the random map
