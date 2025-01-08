podman build -t todo-app .
#k3d image import todo-app

rm -f todo-app.tar
podman save -o todo-app.tar todo-app:latest

# Load the image into kind
sudo kind load image-archive todo-app.tar