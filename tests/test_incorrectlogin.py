#!/usr/bin/env python3

from s3ssion import s3ssion

ctrl = s3ssion('hehe')
# create a few users
ctrl._register_(name="deep", username="d33pster", password="hehe")
ctrl._register_(name="sairam", username="simple", password="huhu")

# incorrect login
def test_inlogin():
    error = ctrl._login_('d33pster', 'hahahahahah')
    
    assert error != None

def test_inlogin2():
    error = ctrl._login_('huhaaa', 'hhhh')
    
    assert error != None