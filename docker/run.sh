REGISTRY=jussikalliola
IMAGE=game-drl-offloading
VERSION=latest

docker run  -it \
            --rm \
            --cap-add NET_ADMIN \
            --privileged \
            -e DISPLAY=$DISP \
            -e XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
            -e PYTHONBUFFERED=1 \
            -v /etc/timezone:/etc/timezone:ro \
            -v /etc/localtime:/etc/localtime:ro \
            -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
            -v $HOME/.Xauthority:/root/.Xauthority:rw \
            -v $HOME/.tmux/:/root/.tmux \
            -v $HOME/.config/:/root/.config \
            -v /run/user/1000:/run/user/1000 \
            $IMAGE:$VERSION \
            bash
