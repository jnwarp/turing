"""
Python3 Turing Machine
Copyright (c) 2018 James Warp

github.com/jnwarp/turing
"""

class TuringMachine:
    """
    Turing Machine accepts a tape (string) and transition function.

    INPUT:
        tape = 'aaa'
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

    SPECIAL STATES:
        q0   = initial state
        qacc = Accepts the input
        qrej = Rejects the input
        
    TRANSITION FUNCTION:
        {
            state: {
                letter: (new_state, write_letter, L/R)
            }
        }
    """

    def __init__(self, tape, transition_function):
        # convert tape to list for iteration purposes
        self.tape = list(tape)

        # save inputs
        self.funct = transition_function
        self.state = 'q0'
        self.q = -1

        # print out the initial state
        print('state\ttape')
        print('='*12)
        self.printState()

        # start q at zero
        self.q = 0

        
    def printState(self, nextpos = 0):
        out = ''
        for i, q in enumerate(self.tape):
            if i == self.q:
                # optionally print direction
                if nextpos > 0:
                    out += ' ' + q + '>'
                elif nextpos < 0:
                    out += '<' + q + ' '
                else:
                    out += '[' + q + ']'
            else:
                out += ' ' + q + ' '
                    

        print(self.state + '\t' + out)


    def step(self):
        # stop if state reaches acc / rej
        if self.state == 'qacc':
            print('\nState accepted!')
            return self.state
        elif self.state == 'qrej':
            print('\nState rejected!')
            return self.state

        # select the funct to use
        funct = self.funct[self.state][self.tape[self.q]]

        # replace the tape element
        self.state = funct[0]
        self.tape[self.q] = funct[1]

        # print state before head is moved
        self.printState()
        """
        #optionally print direction
        if funct[2] == 'R':
            self.printState(1)
        else:
            self.printState(-1)
        """
        
        # move the head
        if (funct[2] == 'R'):
            self.q += 1

            # append element if q goes beyond string
            if len(self.tape) <= self.q:
                self.tape += '*'
        else:
            self.q -= 1

            # throw error if element tries to go too far
            if self.q < 0:
                raise ValueError('Out of tape, L\n' + self.tape + ' ' + self.funct)

    def stepAll(self, limit=100):
        cnt = 0
        flag = True

        while flag and cnt < limit:
            # step one, stop if result
            result = t.step()
            if (result != None):
                flag = False

            # prevent inf loop
            cnt += 1

        if flag:
            print('State limit reached!')

        return result

    def stepPause(self):
        flag = True

        while flag:
            # pause for user to press enter
            input('')

            # step one, stop if result
            result = t.step()
            if (result != None):
                flag = False

        return result


"""
# infinite problem
transition_function = {
    'q0': {
        'a': ('qr', '*', 'R'),
        '*': ('qr', '*', 'R')
    },
    'qr': {
        'a': ('qr', 'a', 'R'),
        '*': ('ql', 'a', 'L')
    },
    'ql': {
        'a': ('ql', 'a', 'L'),
        '*': ('qr', '*', 'R')
    }
}
"""

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
