#!/bin/bash
set -Eeuo pipefail
set -x
python3 generate.py
BASE_PATH=$(pwd)
for OUTPUT in output/*/*; do
  cd $BASE_PATH
  TAG=${OUTPUT/output\//}
  IMAGE="kudaliar032/php:${TAG/\//-}"

  cd $OUTPUT
  docker build -t $IMAGE .
  docker push $IMAGE
done
