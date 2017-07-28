#!/bin/bash

FAIL=0

python test/test_raise.py
if [ $? -ne 139 ]; then
    echo "test_raise.py did not segfault"
    FAIL=1
else
    echo "test_raise.py: PASS"
fi

python test/test_call.py
if [ $? -ne 139 ]; then
    echo "test_raise.py did not segfault"
    FAIL=1
else
    echo "test_raise.py: PASS"
fi

if [ $FAIL -eq 1 ]; then
    echo FAIL
    exit 1
else
    echo PASS
fi
