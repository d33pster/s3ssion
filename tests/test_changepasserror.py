#!/usr/bin/env python3

from s3ssion import s3ssion

ctrl = s3ssion('hehe')
# create a few users
ctrl._register_(name="deep", username="d33pster", password="hehe")
ctrl._register_(name="sairam", username="simple", password="huhu")

# no user
def nouser():
    assert ctrl._change_password_('hh', 'huhuh', 'okoko') != None

# no pass
def nopass():
    assert ctrl._change_password_('d33pster', 'haha', 'hehe') != None