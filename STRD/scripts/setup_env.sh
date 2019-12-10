#!/bin/bash

# Copyright: 2016-2018 ROS小课堂 www.corvin.cn
# Author: corvin
# Description:该脚本是为了安装一些必要软件包,这样才能正常运行软件包中的
#   各个实例代码.该脚本只需要执行一次即可.
# History:
#   20181220:Initial this bash file.
#   20190102:在安装upgrade时,增加一个判断,必须等命令执行成功才继续往下运行.

red="\e[31m"
normal="\e[0m"
CURRENT_PATH=$(dirname $(readlink -f "$0"))
STDR_WS_PATH=${CURRENT_PATH%scripts}

# first install necessary packages
sudo apt update
while [ $? -ne 0 ]
do
    echo -e "${red}Can't update source list, will retry...${noraml}\n"
    sleep 10
    sudo apt update
done

sudo apt -y upgrade
while [ $? -ne 0 ]
do
    echo -e "${red}Can't install upgrade packages, will retry...${noraml}\n"
    sleep 10
    sudo apt -y upgrade
done

sudo apt install -y ros-$ROS_DISTRO-move-base ros-$ROS_DISTRO-amcl
sudo apt install -y ros-$ROS_DISTRO-dwa-local-planner ros-$ROS_DISTRO-global-planner
sudo apt install -y ros-$ROS_DISTRO-gmapping ros-$ROS_DISTRO-hector-mapping
sudo apt install -y ros-$ROS_DISTRO-costmap-2d ros-$ROS_DISTRO-hector-nav-msgs
sudo apt install -y ros-$ROS_DISTRO-map-server ros-$ROS_DISTRO-nav-core
sudo apt-get -y autoremove

# second catkin_make worksapce
cd $STDR_WS_PATH
catkin_make

# third set workspace env to .bashrc
source devel/setup.bash
echo "#config stdr_ws env by corvin" >>~/.bashrc
echo "source ${STDR_WS_PATH}devel/setup.bash" >> ~/.bashrc

exit 0
