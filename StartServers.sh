#! /bin/bash

# FONCTIONS AND VARIABLES
function checkResult
{
	if [ $? -eq 0 ]; then
    echo -e "\e[32mdone\e[0m"
	else
		echo -e "\e[31mfail\e[0m"
	fi
}

apachename="my-apache-app"
pythonname="python-app"
postgre="some-postgres"
pgadmin="some-pgadmin4"
bold=$(tput bold)
normal=$(tput sgr0)
#####################

### MAIN ###########
echo -e "${bold}Starting existing container ....${normal}" 
sudo docker start $apachename
sudo docker start $pythonname
sudo docker start $postgre
sudo docker start $pgadmin
echo -e "\n"



