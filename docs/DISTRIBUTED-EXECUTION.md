# Distributed overnight execution

How a desktop suite that takes **72+ hours** to run sequentially was brought down
to **2–3 hours**. The technique is described here generically so it can be reused;
the sample project in this repo is too small to need it.

## The problem

Desktop UI automation cannot be parallelised on one machine the way headless web
tests can — every session needs the real foreground UI. A single WinForms product
area with thousands of cases across dozens of report modules ran overnight and
often did not finish before the working day started.

## The approach: one module owner per runner

1. **Partition by module, not by case.** The suite is already organised so that
   every report / sub-module is an independent slice (independent features,
   independent NameMapping sub-tree, no shared state between modules).
2. **Assign one module to one runner.** Each QA engineer's machine (or a pool of
   dedicated VMs) owns a fixed set of modules. Ownership is explicit and version
   controlled, so a run is reproducible and a failure has a clear owner.
3. **Kick off centrally, run locally.** A scheduled job triggers every runner at
   the same time; each runner executes only its slice with TestExecute in
   headless-desktop mode against a clean VM snapshot.
4. **Collect and merge.** Every runner publishes its TestComplete log / JUnit
   summary to a shared location; a small merge step produces one consolidated
   report and posts pass/fail per module.

```
        ┌───────────── scheduler (nightly) ─────────────┐
        │                                               │
   runner A            runner B            runner C   ...runner N
  modules 1–4        modules 5–9        modules 10–14
        │                  │                  │
        └────────── shared results store ─────┘
                          │
                   merge + notify (per-module pass/fail)
```

## Why 72h → 2–3h

Sequential time ≈ Σ(module time). Distributed time ≈ max(module time on its
runner) + merge. With work spread across ~15 owners the long pole is a single
module's run, not the sum — a ~25–30× reduction in wall-clock time, with no change
to the tests themselves.

## Practical notes

* **Balance by historical duration**, not case count — modules vary widely.
* **Clean state per runner:** revert to a VM snapshot (or reinstall the SUT)
  before each nightly run so a leaked dialog never cascades.
* **Idempotent data:** each scenario creates and cleans up its own data so two
  runners never collide on shared fixtures.
* **Fail fast per module, not per suite:** one module's crash must not block the
  other 14 from reporting.
* **Keep ownership in the repo** (a `runners.yml`-style manifest) so re-balancing
  is a reviewed change.
