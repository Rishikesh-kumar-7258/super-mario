class Statemachine:
    """
    This is class whose object will help in changing the states.
    With its help we can also pass some variables to the next state.

    USAGE:
        gstatemachine = Statemachine(states)
        gstatemachine.change(state, param1=val1,
                                    params2=val2)
    """

    def __init__(self, states={}) -> None:
        """
        It acts as a constructor for python class
        """
        
        self.current = None
        self.states = states
    
    def change(self, state) -> None:
        """
        This is the function to change the change the state.
        """

        # checking if the given state exists in self.states
        # if not present it will raise exception
        assert state in self.states
        
        # leaving the current state. Only if the current state is not None
        if self.current != None : self.current.leave()

        # current state is changed to the new state provided
        self.current = self.states[state]

        # Entering into the new current state
        self.current.enter()
    
    def update(self, params) -> None:
        """
        This function will constantly update the state in each game loop.
        It takes on extra parameter as an argument which is events
        """

        #updating the current state
        self.current.update(params)