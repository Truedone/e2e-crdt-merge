# SPDX-License-Identifier: BUSL-1.1
# Copyright 2026 Ryan Gillespie / Optitransfer

"""Exact dedup ignores whitespace at the ends of a value.

A CSV export often leaves a trailing space or a line break on a field, and
"hello" and "hello " were kept as two records.
"""
from crdt_merge.dedup import dedup_list


def test_exact_dedup_ignores_whitespace_at_the_ends():
    unique, dups = dedup_list(["hello", "hello ", " hello\n", "world"])
    assert unique == ["hello", "world"]
    assert dups == [1, 2]
