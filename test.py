import pytest 
import numpy as np
from main import Memo9, Memo10

data = [2,4,6,8,10]

class TestCentralTendencyNine:
    def test_mean(self):
        assert Memo9(data=data,method="mean").calculate() == 6
    def test_median(self):
        assert Memo9(data=data,method="median").calculate() == 6
    def test_mode(self):
        assert Memo9(data=data,method="mode").calculate()["mode"] == data
    def test_sample_var(self):
        assert Memo9(data=data,method="sample_var").calculate() == 10

class TestCentralTendencyTen:
    def test_mean(self):
        assert Memo10(data=data,method="mean").calculate() == 6
    def test_median(self):
        assert Memo10(data=data,method="median").calculate() == 6
    def test_mode(self):
        assert Memo10(data=data,method="mode").calculate()["mode"] == data
    def test_sample_var(self):
        assert Memo10(data=data,method="sample_var").calculate() == 10