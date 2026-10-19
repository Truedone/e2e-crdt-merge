# SPDX-License-Identifier: BUSL-1.1
# Copyright 2026 Ryan Gillespie / Optitransfer

"""merge_json_lines(key=...) keeps the records that have no value for the key.

They were dropped: a record without an id in either dataset vanished from the
merge, and merging a dataset with itself lost every such record.
"""
from crdt_merge.json_merge import merge_json_lines


def test_records_without_the_key_are_kept_once_after_the_matched_ones():
    a = [{"id": 1, "v": "a"}, {"v": "no id"}]
    b = [{"id": 1, "v": "b"}, {"id": None, "v": "null id"}, {"v": "no id"}]
    result = merge_json_lines(a, b, key="id")
    assert result == [{"id": 1, "v": "b"}, {"v": "no id"}, {"id": None, "v": "null id"}]


def test_merging_a_dataset_with_itself_returns_it_whole():
    a = [{"id": 1, "v": "a"}, {"note": "header row"}]
    assert merge_json_lines(a, a, key="id") == a
