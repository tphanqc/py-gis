#!/bin/bash
ENV_NAME=py-gis
ENVS=$(conda env list | awk '{print $1}')
if [[ $ENVS = *"$ENV_NAME"* ]]; then
  echo The environment already exists
  exit
else
  conda env create -f env_py_gis.yml
fi;
PP=$PWD
conda env config vars set PYTHONPATH=${PP} -n ${ENV_NAME}
