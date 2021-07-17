docker rmi docker-python -f
docker load -i sarcasm.tar
docker run docker-python
rm sarcasm.tar