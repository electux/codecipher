#!/bin/bash
#
# @brief   codecipher
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2022
# @company None, free software to use 2022
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov codecipher_coverage.xml codecipher_coverage.json .coverage
python3 -m coverage run -m --source=../codecipher unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o codecipher_coverage.xml 
python3 -m coverage json -o codecipher_coverage.json
python3 -m coverage report --format=markdown -m
python3 ats_coverage.py -n codecipher
echo "Done"
