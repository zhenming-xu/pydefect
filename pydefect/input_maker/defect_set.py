# -*- coding: utf-8 -*-
#  Copyright (c) 2020. Distributed under the terms of the MIT License.
from collections.abc import Set
from typing import Iterator, Set as typeSet

from monty.serialization import loadfn, dumpfn

from pydefect.input_maker.defect import Defect


class DefectSet(Set):
    def __init__(self, defects: typeSet[Defect]):
        self.defects = defects

    def __contains__(self, defect: object) -> bool:
        return defect in self.defects

    def __len__(self) -> int:
        return len(self.defects)

    def __iter__(self) -> Iterator:
        yield from self.defects

    def to_yaml(self, filename: str = "defect_in.yaml") -> None:
        d = {defect.name: list(defect.charges) for defect in self.defects}
        dumpfn(d, filename)

    @classmethod
    def from_yaml(cls, filename: str = "defect_in.yaml") -> "DefectSet":
        d = loadfn(filename)
        names = {Defect(name, tuple(charges)) for name, charges in d.items()}
        return cls(names)


