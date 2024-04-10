#!/usr/bin/env python3

from s3ssion import s3ssion

ctrl = s3ssion('hehe')
# create a few users
ctrl._register_(name="deep", username="d33pster", password="hehe")
ctrl._register_(name="sairam", username="simple", password="huhu")

# usercount
def test_4():
    assert ctrl._user_count_() == 2