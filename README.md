# Introduction

An once-upon-an-app is a sample application for GitHub experiments.

Folder's structure: 

```bash 

.
├── README.md
├── app
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── bicep
    └── main.bicep

```

## How to run

To run application: 

```bash

cd app
pip install -r requirements.txt
flask run

```

To run iac (make sure az login`ed) and do:

```bash

cd bicep
az group create -g myapp-rg -l westeurope
az deployment group create -g myapp-rg -f main.bicep

```

Dockerfile is provided. Build image, push to the regisry (the one being build with bicep). Run app on Web App.
