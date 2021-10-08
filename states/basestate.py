class Base:
    """
    This is the base state.
    This state contains all the necessary function which are needed in different states.
    All the other states inherits from this state
    """

    def __init__(self) -> None:
        """
        This is constructor method.
        """
        pass

    def enter(self, **params) -> None:
        """
        This is the enter method.
        During change of state via statemachine this function is called first.
        """

        pass

    def render(self) -> None:

        """
        This is the render method all the drawables are drawn using this method.
        """

        pass

    def update(self, param) -> None:
        """
        This is update function it updates the screen on each frame.
        """

        pass

    def leave(self) -> None:
        """
        This is leave method.
        When state is changing this method is used to leave the current state 
        """

        pass