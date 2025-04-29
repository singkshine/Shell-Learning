#!/bin/bash
# 尝试编写安装python 图像识别虚拟环境脚本

sudo clear

ping baidu.com  || ping google.com || ! echo No internet || exit 2

! ( ! [ -f Pathcheck ] || ! echo Had install File || ! echo > Pathcheck ) || 
! echo >> Pathcheck || ! echo No install File

whereis python3 | grep '/.*bin/pyathon3' -o > Pathcheck || 
! sudo apt update ||
echo No Python3 found ,wait for install Python3 && sudo apt install python3 -y && 
whereis python3 | grep '/.*bin/python3' -o > Pathcheck

whereis pip | grep '/.*bin/pip' || 
! sudo apt update ||
echo No Pip found , wait for install Pip && sudo apt install python3-pip -y

Py=`cat Pathcheck`

echo Python load : $Py

rm -r Pathcheck

! $Py -m venv .venv || ! cd ./.venv/bin ||
./pip install torch torchvision torchaudio numpy matplotlib opencv-python || 
! echo Error to install wheel || exit 2

echo Finish Install, welcome to use python3 

exit 0


