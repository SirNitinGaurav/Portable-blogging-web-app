#!/bin/bash
kubectl delete deploy mongodb mongo-express flask-app && \
kubectl delete service mongodb-service mongo-express-service flask-app-service

docker image rm flaskapp

docker build -f flask-app-image.dockerfile -t flaskapp .

kubectl apply -f secret.yaml && kubectl apply -f configmap.yaml

kubectl apply -f deployments.yaml && \
kubectl apply -f services.yaml

kubectl get all

echo -e '\nBash Script Execution Completed and Starting Flask Server in 5 seconds'
sleep 5

# Running flask-app server

# docker container ls # to get the list of containers. Store the id of flask-app container in variable
container_id=$(docker container ls | grep flask-app | awk '{print $1}')
# docker container exec -it <container-id> /bin/bash to execute commands in container shell
docker container exec -i $container_id /bin/bash < runFlaskServer.sh