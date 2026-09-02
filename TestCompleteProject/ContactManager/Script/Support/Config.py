# -*- coding: utf-8 -*-
"""Central configuration for the Contact Manager automation project.

Values can be overridden per run via TestComplete Project Variables of the same
name (Project.Variables.<NAME>); the file provides the defaults.
"""


def _project_var(name, default):
    try:
        if Project.Variables.VariableExists(name):
            return Project.Variables.VariableByName(name)
    except Exception:
        pass
    return default


# Path to the built SUT. Relative paths are resolved from the project folder.
APP_PATH = _project_var(
    "AppPath",
    "..\\..\\sut\\ContactManager\\bin\\Release\\net8.0-windows\\ContactManager.exe",
)
APP_PROCESS = "ContactManager"

# Default explicit-wait budget (milliseconds).
WAIT_TIMEOUT_MS = int(_project_var("WaitTimeoutMs", 10000))

# Polling interval used by the custom waiters.
POLL_INTERVAL_MS = 200

# Fallback scratch folder for artefacts a scenario writes (e.g. the CSV export),
# used only when the TEMP environment variable is not set on the agent.
PROJECT_TEMP = _project_var("ProjectTemp", "C:\\Temp")
