#!/bin/bash

pip install jaxlib==0.3.2 -f https://storage.googleapis.com/jax-releases/jax_releases.html

exec "$@"
