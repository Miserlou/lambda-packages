import os
from lambda_packages import lambda_packages
from nose.tools import assert_true

def test_packages():
    for name, details in lambda_packages.items():
        assert_true(os.path.exists(details['path']))
