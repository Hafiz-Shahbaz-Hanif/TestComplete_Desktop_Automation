# -*- coding: utf-8 -*-
"""Explicit, timeout-driven waits.

Screen objects use these instead of ``Delay()`` so the suite is fast when the UI
is responsive and resilient when it is not.
"""

from Support import Config


def until_visible(obj, timeout_ms=None):
    timeout_ms = timeout_ms or Config.WAIT_TIMEOUT_MS
    if not obj.WaitProperty("VisibleOnScreen", True, timeout_ms):
        raise Exception("Object did not become visible within %d ms" % timeout_ms)
    return obj


def until_enabled(obj, timeout_ms=None):
    timeout_ms = timeout_ms or Config.WAIT_TIMEOUT_MS
    if not obj.WaitProperty("Enabled", True, timeout_ms):
        raise Exception("Object did not become enabled within %d ms" % timeout_ms)
    return obj


def until(predicate, message, timeout_ms=None):
    """Poll ``predicate`` until it returns truthy or the timeout elapses."""
    timeout_ms = timeout_ms or Config.WAIT_TIMEOUT_MS
    elapsed = 0
    while elapsed < timeout_ms:
        try:
            if predicate():
                return True
        except Exception:
            pass
        Delay(Config.POLL_INTERVAL_MS)
        elapsed += Config.POLL_INTERVAL_MS
    raise Exception("Timed out after %d ms waiting for: %s" % (timeout_ms, message))


def for_ui_idle():
    """Let the WinForms message loop settle after an input event."""
    Sys.Refresh()
    Delay(Config.POLL_INTERVAL_MS)
