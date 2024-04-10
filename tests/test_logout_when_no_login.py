#!/usr/bin/env python3

from s3ssion import s3ssion

ctrl = s3ssion('hehu',['username', 'password'], 'haha', 'default')
# create a few users
ctrl._register_(username="d33pster", password="hehe")
ctrl._register_(username="simple", password="huhu")

# logout
def test_blanklogout():
    error = ctrl._logout_()
    
    assert error != None
