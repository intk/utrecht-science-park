#/bin/bash
APPNAME="utrecht-science-park-plone"
CONTAINER=$(docker ps | grep $APPNAME | cut -d " " -f1)
echo "Restarting $CONTAINER"
docker restart $CONTAINER
