#!/bin/bash
set -euo pipefail

# Build the image with Podman
rm -f log-output-timestamper.tar
podman build -t log-output-timestamper:latest .

# Save the image to a tar file
podman save -o log-output-timestamper.tar log-output-timestamper:latest

# Load the image into kind
sudo kind load image-archive log-output-timestamper.tar