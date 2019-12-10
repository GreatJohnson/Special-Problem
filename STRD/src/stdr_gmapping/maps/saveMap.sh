#!/bin/bash

# Copyright: 2016-2018 www.corvin.cn
# Author: corvin
# Description: bash file to save stdr_gmapping's map
# History:
#  20180524: initial this bash file.

rosrun map_server map_saver map:=/gmapping/map -f mymap
exit 0
