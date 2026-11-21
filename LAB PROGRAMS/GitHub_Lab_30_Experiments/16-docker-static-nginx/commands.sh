docker build -t lab-static:1.0 .
docker run --rm -d --name lab-static -p 8080:80 lab-static:1.0
curl -I http://localhost:8080
