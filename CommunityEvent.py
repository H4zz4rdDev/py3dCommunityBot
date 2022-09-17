

class CommunityEvent:
    eventName = None
    timeInMinutes = 60

    def __init__(self, eventName, timeInMinutes):
        self.eventName = eventName
        self.timeInMinutes = timeInMinutes