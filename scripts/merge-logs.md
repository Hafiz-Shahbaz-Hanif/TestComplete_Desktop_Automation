# Merging per-runner results

The "collect and merge" step from [`docs/DISTRIBUTED-EXECUTION.md`](../docs/DISTRIBUTED-EXECUTION.md),
written out. There is no script to run in this sample repo (it has one module and
no license in CI) — this is the shape the merge takes once `runners.yml` has more
than one runner.

## What each runner produces

Every runner finishes its slice with TestExecute and exports two things to the
shared `merge.results_dir`:

```
<results_dir>/
  runner-a/
    log.mht            # TestComplete's own log (human view)
    junit.xml          # exported JUnit summary (machine view)
  runner-b/
    log.mht
    junit.xml
  ...
```

Export the JUnit file with TestComplete's `Log.SaveResultsAs` (or the
`/ExportSummary:` command-line switch on TestExecute) so the merge only has to
read a stable format.

## The merge

1. **Wait for all runners** (or a timeout). A missing `junit.xml` after the
   deadline is itself a failure for that module — do not silently drop it.
2. **Concatenate the JUnit suites.** Each runner's `junit.xml` is one or more
   `<testsuite>` elements keyed by module. Wrap them in a single `<testsuites>`.
   Any JUnit merger works (`junit-merge`, `junitparser merge`, a 20-line XSLT).
3. **Compute the roll-up:** total / passed / failed / skipped, and per-module
   pass rate. The long pole (slowest runner's wall-clock) is the number that
   proves the 72h -> 2-3h claim.
4. **Publish:**
   - the merged `junit.xml` for CI / dashboards,
   - the per-runner `log.mht` files linked from a one-page index,
   - a per-module pass/fail line to the team channel.

## Notes

* Keep the merge **idempotent** — re-running it over the same `results_dir`
  produces the same report.
* Fail the overall run if any module is missing or red, but always publish the
  report first so the other modules are still visible.
* `runners.yml` `historical_minutes` is updated from this run's actual durations
  so the next re-balance is data-driven.
