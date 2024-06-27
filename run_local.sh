#!/bin/sh

docker stop think-prompt-ass1;
docker rm think-prompt-ass1;
docker build --tag think-prompt-ass1 .;
docker run --name think-prompt-ass1 \
    -v "$(pwd)"/logs:/app/logs \
    -v "$(pwd)"/output \
    --restart always \
    think-prompt-ass1;
exit;