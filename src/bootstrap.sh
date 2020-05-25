export FLASK_APP=./src/main.py
source venv/bin/activate
flask run -h 0.0.0.0
curl -X POST -H 'Content-Type: application/json' -d '{
  "importance": "Extreme",
  "description": "An alarm that will wake me up"
}'
curl -X POST -H 'Content-Type: application/json' -d '{
  "importance": "Low",
  "description": "An alarm to check my emails"
}'
ng serve