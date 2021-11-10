class Statemachine:

    """ This class will handle the current state and also help in changing the state """

    def __init__(self, states):
        
        self.states = states

        self.current_state = None

    def change(self, state, **param):

        if state in self.states:
            if self.current_state:
                self.current_state.leave()
            
            self.current_state = self.states[state]
            self.current_state.enter(**param)
    
    def render(self):
        self.current_state.render()

    def update(self, param):
        self.current_state.update(param)