from pynput import mouse, keyboard
import time

class Recorder:
    def __init__(self):
        self.recording = False
        self.actions = []

        self.mouse_listener = None
        self.keyboard_listener = None

    # =========================
    # Public API
    # =========================

    def start(self, task_name=None):
        """Start recording user input"""
        
        if self.keyboard_listener:
            self.keyboard_listener.stop()

        if self.mouse_listener:
            self.mouse_listener.stop()
        
        self.recording = True
        self.actions = []

        print("[Recorder] Started recording...")

    
        self.mouse_listener = mouse.Listener(on_click = self._on_click)
        self.mouse_listener.start()

        self.keyboard_listener =  keyboard.Listener(on_press = self._on_press)
        self.keyboard_listener.start()


    def stop(self):
        """Stop recording and return actions"""

        if self.keyboard_listener:
            self.keyboard_listener.stop()

        if self.mouse_listener:
            self.mouse_listener.stop()

        
        self.recording = False

        print("[Recorder] Stopped recording.")

        self.keyboard_listener.stop()
        self.mouse_listener.stop()


        return self.actions

    # =========================
    # Mouse events
    # =========================

    def _on_click(self, x, y, button, pressed):
        if not self.recording:
            return

        # TODO: only record click when pressed == True
        if pressed:
            self.actions.append({
                "type": "mouse_click",
                "button": str(button),
                "position": [x, y],
                "time": time.time()
            })

    # =========================
    # Keyboard events
    # =========================

    def _on_press(self, key):
        if not self.recording:
            return

        try:
            self.actions.append({
                "type": "key_press",
                "key": key.char,
                "time": time.time()
            })
        except AttributeError:
            self.actions.append({
                "type": "key_press",
                "key": str(key),
                "time": time.time()
            })