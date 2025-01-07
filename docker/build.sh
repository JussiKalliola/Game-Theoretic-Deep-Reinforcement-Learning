REGISTRY=jussikalliola
IMAGE=game-drl-offloading
VERSION=latest


  docker build \
    --force-rm \
    --progress=plain \
    -t ${IMAGE}:${VERSION} \
    ..
