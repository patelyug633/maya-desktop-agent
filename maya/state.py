class State:
    def __init__(self, mode="idle", current_task=None):
        self.mode = mode  # idle | recording | executing
        self.current_task = current_task