#!/usr/bin/env python3

from s3ssion import s3ssion

ctrl = s3ssion('hehe')
# create a few users
ctrl._register_(name="deep", username="d33pster", password="hehe")
ctrl._register_(name="sairam", username="simple", password="huhu")

# test login
def test_1():
    ctrl._login_('d33pster', 'hehe')
    
    assert ctrl._login_status_() == True
    assert ctrl._login_who_() == 'd33pster'

def test_2():
    ctrl._force_login_('sairam')
    
    assert ctrl._login_who_() == 'sairam'