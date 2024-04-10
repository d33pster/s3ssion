#!/usr/bin/env python3

from s3ssion import s3ssion

ctrl = s3ssion('hehe')
# create a few users
ctrl._register_(name="deep", username="d33pster", password="hehe")
ctrl._register_(name="sairam", username="simple", password="huhu")

# change password check

def test_5():
    ctrl._login_('d33pster', 'hehe')
    
    assert ctrl._login_status_() == True

def test_6():
    error = ctrl._logout_()
    
    error = ctrl._change_password_('d33pster', 'hehe', 'hoho')
    
    assert error == None
    