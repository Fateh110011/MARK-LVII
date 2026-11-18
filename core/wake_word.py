"""
Temporary safe fallback: wake-word detection is disabled to stop the spam loop.
The rest of the app will run normally, and manual activation still works.
"""
from __future__ import annotations
from typing import Callable

DEFAULT_THRESHOLD = 0.5
SAMPLE_RATE = 16000

def is_installed() -> bool:
    return False

def is_ready() -> bool:
    return False

def install_and_download(logger: Callable[[str], None] = print,
                         notify: Callable[[str], None] | None = None) -> tuple[bool, str]:
    return False, "Wake word temporarily disabled."

class WakeWordDetector:
    def __init__(self, on_detect: Callable[[], None],
                 threshold: float = DEFAULT_THRESHOLD,
                 logger: Callable[[str], None] = print,
                 notify: Callable[[str], None] | None = None):
        self._on_detect = on_detect
        self._threshold = threshold
        self._logger = logger
        self._notify = notify or (lambda _msg: None)
        self._ready = False
        self._running = False

    def start(self) -> bool:
        # Intentionally returns False silently so it never runs the loop
        self._running = False
        self._ready = False
        return False

    def stop(self) -> None:
        self._running = False
        self._ready = False

    @property
    def ready(self) -> bool:
        return False

    def reset(self) -> None:
        pass

    def feed(self, frame_int16) -> None:
        # Instantly discard audio frames without running any models or triggering callbacks
        pass
