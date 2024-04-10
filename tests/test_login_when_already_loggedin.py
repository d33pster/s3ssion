#!/usr/bin/env python3

from s3ssion import s3ssion

ctrl = s3ssion('hehe')
# create a few users
ctrl._register_(name="deep", username="d33pster", password="hehe")
ctrl._register_(name="sairam", username="simple", password="huhu")

ctrl._force_login_('d33pster')

# login when already logged in

def test_relogin():
    error = ctrl._login_('sairam', 'huhu')
    
    assert error != None
