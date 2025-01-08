podman build -t todo-backend .
#k3d image import todo-backend

rm -f todo-backend.tar
podman save -o todo-backend.tar todo-backend:latest

# Load the image into kind
sudo kind load image-archive todo-backend.tar