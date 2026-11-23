"""HW2 · errors.py: the club's own exceptions. Practises Session 6: custom exception classes
that share one parent and carry the details for whoever catches them."""


class SignupError(Exception):
    """Provided: the parent of every sign-up problem, so one except can catch them all."""


class NotSignedUpError(SignupError):
    """Provided: the member has no seat and is not on the waitlist."""

    def __init__(self, member: str, event: str):
        """Provided: give the parent the message, then keep member and event."""
        super().__init__(f"{member} is not signed up for {event}")
        self.member = member
        self.event = event


class AlreadySignedUpError(SignupError):
    def __init__(self, member: str, event: str):
        super().__init__(f"{member} is already signed up for {event}")
        self.member=member
        self.event=event

class UnknownEventError(SignupError):
    def __init__(self, title: str):
        super().__init__(f"there is no event called {title}")
        self.title=title
