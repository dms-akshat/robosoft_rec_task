SMS Analytics Dashboard  

This is a Django-based SMS analytics dashboard that tracks SMS delivery status, success rates, and logs SMS transactions. It runs inside a Docker container and uses PostgreSQL as the database.  

Features  
- View total SMS, success/failure rates, and pending messages  
- Display SMS logs in a table with pagination  
- Uses Bootstrap for basic styling  
- Supports database seeding for test data  
- Runs in Docker with automated migrations  

Setup Instructions  

1. Clone the repository

2. Run the Project  
Ensure Docker is installed, then run:  
docker-compose up --build -d

NOTE : The docker compose file automatically seeds the database right now. To change that, remove the python manage.py seed_logs command

4. Access the Dashboard  
Open in a browser:  
http://localhost:10000/dashboard/  

Common Issues & Fixes

Database Connection Issues  
- Ensure PostgreSQL is running inside the db container  
- Try running migrations manually:  
  docker-compose exec web python manage.py migrate

App Not Accessible
- Ensure port mappings in docker-compose.yml are correct  
- Try restarting the container:  
  docker-compose down  
  docker-compose up --build -d 