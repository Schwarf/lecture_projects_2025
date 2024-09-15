# Redis 
Acts like post office:
- Role: Acts as the message broker and result backend.
- Functionality:
    - Message broker: Queues and stores the tasks that need to be done. It manages the incoming tasks and maintains the queue, ensuring that tasks are ready to be fetched and processed by (Celery) workers.
    - Result backend: Stores the results of completed tasks, allowing other parts of the application or other applications to retrieve these results later.

# Celery 
Acts like postal workers, picks up mail and delivers (aka executes tasks) it:
* Role: Distributed task queue and worker management system.
* Functionality:
    - Task distribution: Responsible for distributing these tasks across available workers. When scaling up by adding more workers, Celery efficiently distributes tasks among them based on their availability and capability.
    - Task execution: Workers pick up tasks from the Redis queue and execute them. This is where the actual task code (the functions you define and decorate with @app.task) is run.
    - Worker management: Celery manages the lifecycle of these workers, including their creation, the work they do, handling failures, and their graceful shutdown.


 Docker commands:
 - `docker ps -a`:  Shows --all container's. 
 - `docker logs container_name`: Shows logs of container with name 'container_name'. With option '-f' it monitors and follows log-output.
 - `docker rm container_name`: Remove the container. Use `-f` if the container is running.
 - `docker rmi container_image`: Remove the container-image or a list of images.
 - `dcoker network ls/rm`: `ls` Show networks. `rm` deletes a network.

# Ideas:
 - First step projects:
   - Analyze the Hacker News dataset. Split data cleaning and analysis over two different workers?
     - Questions:
       - How many comments do "Ask HN" entries receive on average?
       - How many comments do "Show HN" entries receive on average?
       - What is the percentage of https-url's in the dataset?
       - Which of the following websites has been visited most
         - https://www.facebook.com
         - https://www.washingtonpost.com
         - https://www.theguardian.com/
         - http://www.theguardian.com/
 -