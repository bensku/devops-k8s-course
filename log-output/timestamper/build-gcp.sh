#!/bin/bash
set -euo pipefail

podman build -t europe-north1-docker.pkg.dev/benjami-lab/exercise-apps/log-output-timestamper:latest .
podman push europe-north1-docker.pkg.dev/benjami-lab/exercise-apps/log-output-timestamper:latest