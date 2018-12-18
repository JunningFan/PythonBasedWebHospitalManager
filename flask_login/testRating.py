import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import pytest

from HASUser import *
from health_centre import *

class TestRating(object):
    
    def setup_method(self):
        self.sample_pat_0 = Patient('pat0','pass','pat0')
        self.sample_pat_0.assign_ID(0)
        self.sample_pat_1 = Patient('pat1','pass','pat1')
        self.sample_pat_1.assign_ID(1)
        self.sample_doc_0 = HealthProvider('doc0', 'pass', 'doc0', 'just a doc')
        self.sample_doc_0.assign_ID(2)
        self.sample_hc_0 = HealthCentre('hos0','Sydney','Hospital','Just a hosptital')

    def test_succ_make_hc(self):
        self.setup_method()
        self.sample_hc_0.record_rating(self.sample_pat_0, 10)
        assert self.sample_hc_0.get_average_rating() == 10

    def test_succ_replace_hc(self):
        self.setup_method()
        self.sample_hc_0.record_rating(self.sample_pat_0, 10)
        self.sample_hc_0.record_rating(self.sample_pat_0, 3)
        assert self.sample_hc_0.get_average_rating() == 3

    def test_succ_mult_hc(self):
        self.setup_method()
        self.sample_hc_0.record_rating(self.sample_pat_0, 10)
        self.sample_hc_0.record_rating(self.sample_pat_1, 8)
        assert self.sample_hc_0.get_average_rating() == 9

    def test_empty_input_make_hc(self):
        self.setup_method()
        try:
            self.sample_hc_0.record_rating(self.sample_pat_0, None)
        except ValueError:
            assert(True)
        else:
            assert(False)
        

    
    
