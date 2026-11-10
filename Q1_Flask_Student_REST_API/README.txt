QUESTION 1 - STUDENT REST API USING FLASK

WHAT YOU NEED
- Python installed
- VS Code
- Terminal / PowerShell

STEP 1: Open this Q1_Flask_Student_REST_API folder in VS Code.
STEP 2: Open Terminal > New Terminal.
STEP 3: Create and activate a virtual environment (Windows PowerShell):
    py -m venv venv
    .\venv\Scripts\Activate.ps1
If activation is blocked, run:
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    .\venv\Scripts\Activate.ps1

STEP 4: Install Flask:
    python -m pip install -r requirements.txt

STEP 5: Start the API:
    python app.py
Keep this terminal running. API address: http://127.0.0.1:5000

STEP 6: Open a SECOND terminal in VS Code and test the endpoints.
Use these PowerShell commands:

A) GET all students:
    curl.exe http://127.0.0.1:5000/students

B) GET student with ID 1:
    curl.exe http://127.0.0.1:5000/students/1

C) POST a new student:
    curl.exe -X POST http://127.0.0.1:5000/students -H "Content-Type: application/json" -d "{\"name\":\"Rahul\",\"age\":22,\"course\":\"CSE\"}"

D) PUT/update student with ID 1:
    curl.exe -X PUT http://127.0.0.1:5000/students/1 -H "Content-Type: application/json" -d "{\"name\":\"Arjun Kumar\",\"age\":21,\"course\":\"CSE\"}"

E) DELETE student with ID 2:
    curl.exe -X DELETE http://127.0.0.1:5000/students/2

F) GET all students again to verify:
    curl.exe http://127.0.0.1:5000/students

EXPECTED RESPONSE EXAMPLES
GET /students:
[
  {"age":20,"course":"CSE","id":1,"name":"Arjun"},
  {"age":21,"course":"ECE","id":2,"name":"Priya"}
]

POST response (your new ID will normally be 3):
{"age":22,"course":"CSE","id":3,"name":"Rahul"}

PUT response:
{"age":21,"course":"CSE","id":1,"name":"Arjun Kumar"}

DELETE response:
{"message":"Student deleted successfully","student":{"age":21,"course":"ECE","id":2,"name":"Priya"}}

NOTE: This is a beginner-friendly in-memory example. Data resets when you stop and restart app.py.
