<!-- Create Docker Image -->
docker build -t [image_name] .

<!-- run Image -->
# บน Linux / macOS
docker run -it --rm -v $(pwd):/app [image_name]

# บน Windows (PowerShell)
docker run -it --rm -v ${PWD}:/app [image_name]

<!-- Check Container Id -->
docker ps

<!-- Open Image -->
# (1)
docker run -it --rm -v $(pwd):/app [image_name] bash

# (2)
docker run -it --rm -v ${PWD}:/app [image_name] sh

<!-- Close Container -->
exit