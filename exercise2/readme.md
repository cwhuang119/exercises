# Exercise 2

# Setup .env
rename .env.example to .env and set the values

# Setup
```bash
pip3 install -r pip_requirements.txt
```

# Running
```bash
cd src
python3 app.py
curl -X POST -H "Content-Type: application/json" -d '{"to":"test@email.com","subject":"subject123","body":"body12323"}' http://localhost:5001/emails
```

# Run with docker
```bash
docker build . -t exercise2
docker run --rm -p 5001:5001 exercise2
curl -X POST -H "Content-Type: application/json" -d '{"to":"test@email.com","subject":"subject123","body":"body12323"}' http://localhost:5001/emails
```