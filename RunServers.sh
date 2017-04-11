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
bold=$(tput bold)
normal=$(tput sgr0)
#####################

### MAIN ###########
echo -e "${bold}Removing existing container ....${normal}" 
sudo docker rm -f $apachename
sudo docker rm -f $pythonname
echo -e "\n"

# On run le front-end Apache 
echo "${bold}Starting front-end Apache container ....${normal}" 
sudo docker run --name $apachename -d  -p 8080:8080 -v "$PWD"/www:/usr/local/apache2/htdocs/ httpd:2.4
checkResult
echo -e "\n"

echo "${bold}Starting Back-end Python container ....${normal}" 
# On run le container qui aura le serveur python
sudo docker run -d --name $pythonname -d  -p 5000:5000 -v "$PWD"/python:/usr/src/myapp -w /usr/src/myapp python:2 bash /usr/src/myapp/entrypoint.sh
checkResult
echo -e "\n"
