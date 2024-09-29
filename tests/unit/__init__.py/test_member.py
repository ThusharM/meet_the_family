from unittest import TestCase
from family_tree.member import Member 

class TestMember(TestCase):
    
    def SetUp(self):
        self.member = Member()