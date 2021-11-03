# Copyright 2021 Accioma (https://accioma.com).
# @author marcelomora <java.diablo@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import re

def is_sequence_valid(sequence):
    return bool(re.match(r"^\d{3}-\d{3}-\d{9}$", sequence))

def next_sequence(sequence):
    if not is_sequence_valid(sequence):
        return False

    vals = sequence.split("-")

    s = int(vals[2])
    s += 1
    vals[2] = "{:09d}".format(s)

    res = "-".join(vals)
    return res

def from_simple(simple):
    """
    Convert simple format ie. 1-1-1 to complete sequence format
    such as 001-001-000000001
    """
    if not re.match(r"^\d+-\d+-\d+$", simple):
        raise ValueError("Value doesn't match pattern for sequence")

    vals = simple.split("-")
    vals[0] = "{:03d}".format(int(vals[0]))
    vals[1] = "{:03d}".format(int(vals[1]))
    vals[2] = "{:09d}".format(int(vals[2]))

    res = "-".join(vals)
    return res
