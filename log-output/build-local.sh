#!/bin/bash
set -euo pipefail

# Build the image with Podman
rm -f log-output.tar
podman build -t log-output:latest .

# Save the image to a tar file
podman save -o log-output.tar log-output:latest

# Load the image into kind
sudo kind load image-archive log-output.tar