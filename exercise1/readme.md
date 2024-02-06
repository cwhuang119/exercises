# Exercise 1


# Setup
```bash
pip3 install -r pip_requirements.txt
```

# Running
```bash
cd src
python3 app.py
# go to browser and type http://localhost:5001
```

# Run with docker
```bash
docker build . -t exercise1
docker run --rm -p 5001:5001 exercise1
# go to browser and type http://localhost:5001
```