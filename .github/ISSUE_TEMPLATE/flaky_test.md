---
name: Flaky scenario
about: A scenario that passes on rerun without a code change
title: "[flaky] "
labels: flaky
---

## Which scenario

<!-- feature : scenario (or Scenario Outline + Examples row) -->

## Evidence it is flaky

- [ ] Passed on rerun with no code change
- [ ] Fails only from a non-clean SUT state / only under a certain screen resolution
- Rough failure rate: __ / 10 runs

## Failure detail

<!-- The failed assertion / the object-not-found, and the step it happened on. -->

## Suspected cause

<!-- guessed `Delay` instead of an explicit wait, NameMapping matched by index,
     leaked modal dialog, scenario not cleaning up its own data. -->

## Notes

The `scenario-triager` agent in `.claude/` is built for this.
