#!/bin/bash

export RESOURCE_GROUP=cochlea-rg
export ACR=cochleaacr.azurecr.io
export APP=once-upon-an-app
az group create -g $RESOURCE_GROUP -l westeurope
az deployment group create --name Deployment -f ../bicep/main.bicep -g $RESOURCE_GROUP

az acr login -n $ACR

docker build -t $ACR/$APP --platform linux/amd64 ../nginx/.
docker scan $ACR/$APP
docker push $ACR/$APP

echo ""
echo "Enjoy the app!"