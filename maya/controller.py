from . import recorder as rec
from . import state as st
from . import storage as mem
from . import actions as act
from . import executor as exe 

class Maya:
    def __init__(self):
        self.state = st.State(
            mode = "idle",  # idle | recording | executing
            current_task = None
        )

        # system components
        self.recorder = rec.Recorder()
        self.storage = mem.Storage()
        self.executor = exe.Executor()
        self.actions = act.Actions()
    
    def start_recoring():
        pass