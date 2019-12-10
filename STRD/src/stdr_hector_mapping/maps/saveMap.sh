#!/bin/bash

# Copyright: 2016-2018 www.corvin.cn
# Author: corvin
# Description: bash file to save stdr_hector_mapping's map
# History:
#  20180601: initial this bash file.

rosrun map_server map_saver map:=/hector_map -f hector_map
exit 0

