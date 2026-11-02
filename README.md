# AI Gym Coach

Full stack AI fitness coaching application.

## Prerequisites
- **MySQL**: Must be running on `localhost:3306` (User: `root`, Pass: `Harish@321`).
- **Python 3.x**: With `pip`.
- **Node.js**: With `npm`.
- **Java 17+**: With Maven.

## Startup Guide

You will need **3 separate terminals** to run the full application.

### Terminal 1: AI Engine (Python)
Runs the Pose Estimation and Video Feed.
```powershell
cd ai_engine
pip install -r ..\requirements.txt
python api_server.py
```
*Port: 5000*

### Terminal 2: Backend (Spring Boot)
Runs the User and Workout persistence API.
```powershell
cd ai_engine\workouts\backend
mvn spring-boot:run
```
*Port: 8080*

### Terminal 3: Frontend (React)
Runs the User Interface.
```powershell
cd ai_engine\workouts\ai-gym-coach-frontend
npm install axios
npm start
```
*Port: 3000*

## Access
Open your browser to [http://localhost:3000](http://localhost:3000).
