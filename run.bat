set APP=rest-api-demo
docker image rm %APP%
docker build -t %APP% .
docker run --rm -p 5101:5000 --name="%APP%" %APP%