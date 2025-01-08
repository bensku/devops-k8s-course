#!/bin/bash
set -euo pipefail

# Build the image with Podman
podman build -t ping-pong:latest .

# Save the image to a tar file
rm -f ping-pong.tar
podman save -o ping-pong.tar ping-pong:latest

# Load the image into kind
sudo kind load image-archive ping-pong.tar