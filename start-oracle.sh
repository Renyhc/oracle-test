#!/bin/bash

VERSION=$1
case $VERSION in
  "free")
    export ORACLE_IMAGE=$ORACLE_FREE_IMAGE
    export ORACLE_PDB=$ORACLE_FREE_PDB
    ;;
  "xe21")
    export ORACLE_IMAGE=$ORACLE_XE21_IMAGE
    export ORACLE_PDB=$ORACLE_XE21_PDB
    ;;
  "xe18")
    export ORACLE_IMAGE=$ORACLE_XE18_IMAGE
    export ORACLE_PDB=$ORACLE_XE18_PDB
    ;;
  "xe11")
    export ORACLE_IMAGE=$ORACLE_XE11_IMAGE
    export ORACLE_PDB=$ORACLE_XE11_PDB
    ;;
  *)
    echo "Uso: ./start-oracle.sh [free|xe21|xe18|xe11]"
    exit 1
    ;;
esac

docker-compose --profile $VERSION up -d 