#!/usr/bin/env python3

from s3ssion import s3ssion

ctrl = s3ssion('hehe')
# create a few users
ctrl._register_(name="deep", username="d33pster", password="hehe")
ctrl._register_(name="sairam", username="simple", password="huhu")

# login
ctrl._force_login_('d33pster')

# logout
def test_3():
    ctrl._logout_()
    
    assert ctrl._login_status_() == False