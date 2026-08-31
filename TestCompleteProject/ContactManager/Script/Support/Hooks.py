# -*- coding: utf-8 -*-
"""Scenario lifecycle hooks.

TestComplete's BDD plugin calls ``on_scenario_start`` / ``on_scenario_end``
(wired in Project ▸ Properties ▸ Events). Each scenario gets a fresh application
instance so runs are isolated and order-independent.
"""

from Support import Config
from ScreenObjects.MainScreen import MainScreen


def start_application():
    """Launch the SUT (registered as a Tested Application) and wait for the main window."""
    TestedApps.ContactManager.Run()
    return MainScreen().wait_shown()


def stop_application():
    proc = Sys.WaitProcess(Config.APP_PROCESS, 1000)
    if proc.Exists:
        proc.Close()
        if Sys.WaitProcess(Config.APP_PROCESS, 3000).Exists:
            Sys.Process(Config.APP_PROCESS).Terminate()


def on_scenario_start(scenario):
    Log.AppendFolder("Scenario: " + scenario.Name)
    start_application()


def on_scenario_end(scenario):
    if scenario.Status != 0:  # 0 == passed
        Log.Picture(Sys.Desktop.Picture(), "Desktop at failure")
    stop_application()
    Log.PopLogFolder()
