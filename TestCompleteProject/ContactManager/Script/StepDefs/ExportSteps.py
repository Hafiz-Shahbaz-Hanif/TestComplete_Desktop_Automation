# -*- coding: utf-8 -*-
"""Step definitions for File -> Export to CSV."""

from ScreenObjects.MainScreen import MainScreen
from Support import Config

# The path used by the most recent export step, so later Then-steps can read it back.
_last_export_path = [None]


def _export_path():
    folder = aqEnvironment.GetEnvironmentVariable("TEMP") or Config.PROJECT_TEMP
    return aqFileSystem.CleanPathName(folder + "\\contactmanager_export.csv")


def _read_lines():
    path = _last_export_path[0]
    if not path or not aqFile.Exists(path):
        Log.Error("No exported CSV file at '%s'" % path)
        return []
    content = aqFile.ReadWholeTextFile(path, aqFile.ctUTF8)
    return [line for line in content.splitlines() if line.strip()]


# @step(r"^I export the contacts to a CSV file$")
def export_contacts():
    path = _export_path()
    if aqFile.Exists(path):
        aqFile.Delete(path)
    _last_export_path[0] = path
    MainScreen().export().save_as(path)


# @step(r"^I cancel the export$")
def cancel_export():
    MainScreen().export().cancel()


# @step(r"^the exported file has (\d+) data rows$")
def csv_row_count(expected):
    lines = _read_lines()
    data_rows = max(len(lines) - 1, 0)  # minus the header
    if data_rows == int(expected):
        Log.Checkpoint("Exported CSV has %s data rows" % expected)
    else:
        Log.Error("Exported CSV has %d data rows, expected %s" % (data_rows, expected))


# @step(r"^the exported file contains \"([^\"]*)\"$")
def csv_contains(fragment):
    body = "\n".join(_read_lines())
    if fragment.lower() in body.lower():
        Log.Checkpoint("Exported CSV contains '%s'" % fragment)
    else:
        Log.Error("Exported CSV does not contain '%s'" % fragment)


# @step(r"^the exported file header is \"([^\"]*)\"$")
def csv_header_is(expected):
    lines = _read_lines()
    header = lines[0] if lines else ""
    if header == expected:
        Log.Checkpoint("Exported CSV header is correct")
    else:
        Log.Error("Exported CSV header is '%s', expected '%s'" % (header, expected))
