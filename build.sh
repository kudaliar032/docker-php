#!/bin/bash
set -Eeuo pipefail
set -x
python generate.py
BASE_PATH=$(pwd)
for OUTPUT in output/*/*; do
  cd $BASE_PATH
  TAG=${OUTPUT/output\//}
  IMAGE="kudaliar032/php:${VERSION}${TAG/\//-}"

  cd $OUTPUT
  docker build -t $TAG .
  docker push $IMAGE
done
