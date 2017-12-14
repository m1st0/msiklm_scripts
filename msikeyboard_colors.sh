#!/bin/bash
# 
# MSI GS63VR keyboard colorizing script.
MY_USERNAME=${USER}
WORK_DIR=${HOME}/my_builds/msi_keyboard
PM2=${HOME}/.nvm/versions/node/v7.10.0/bin/pm2

case "$1,$2" in
  resume,suspend,*) 
    sudo -H -u ${MY_USERNAME} ${PM2} kill
    sudo -H -u ${MY_USERNAME} ${PM2} start ${WORK_DIR}/examples/breathe3.js
    #resume,suspend) msiklm blue breathe
    ;;   
esac

#msiklm blue,blue,blue breathe
sudo ${PM2} kill
sudo -H -u ${MY_USERNAME} ${PM2} start ${WORK_DIR}/examples/breathe3.js
#msi-keyboard -m breathe -c left,blue,high -c middle,purple,high -c right,red,high
#msi-keyboard -m breathe -c left,red,high -c middle,green,high -c right,sky,high
#msiklm yellow,blue,orange high breathe
#msiklm red,green,blue high breathe
#sleep 3
#msiklm blue,orange,yellow high wave
#msiklm blue,green,red high wave
#msiklm red,green,blue high wave
