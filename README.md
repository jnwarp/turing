Turing Machine
==============
This is a python3 implementation of a [Turing Machine](https://en.wikipedia.org/wiki/Turing_machine).

Usage
-----

Set the initial `tape` state.
```python
tape = 'aba*'
```

Edit the `transition_function` with the states of the turing machine. `q0` is always the initial state and `q` (the head) will point to the first item on the tape.

If `q == b` and `state == q0`, then the transition function below would:
 - set `q = a`
 - set `state = q1`
 - move `q` to the right
```python
transition_function = {
    'q0': {
        'a': ('q0', 'a', 'R'),
        'b': ('q1', 'a', 'R'),
        '*': ('qrej', '*', 'L')
    },
    'q1': {
        'a': ('q1', 'b', 'R'),
        'b': ('qacc', 'b', 'L'),
        '*': ('qrej', '*', 'L')
    }
}
```

Create an instance of the turing machine and run it!
```python
t = TuringMachine(tape, transition_function)
t.stepAll()
```

Example
-------

### Input
```python
transition_function = {
    'q0': {
        'a': ('q0', 'a', 'R'),
        'b': ('q1', 'a', 'R'),
        '*': ('qrej', '*', 'L')
    },
    'q1': {
        'a': ('q1', 'b', 'R'),
        'b': ('qacc', 'b', 'L'),
        '*': ('qrej', '*', 'L')
    }
}

tape = 'aba*'

t = TuringMachine(tape, transition_function)
t.stepAll()
```

### Output
```
state   tape
============
q0       a  b  a  *
q0      [a] b  a  *
q1       a [a] a  *
q1       a  a [b] *
qrej     a  a  b [*]

State rejected!
```

License
-------

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
