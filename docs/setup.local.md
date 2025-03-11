# Guide to Setting Up the Environment (for dummies)

Simple guide... Don't worry, it's super easy and doesn't require advanced knowledge of anything.

---

### **What do we have?**
This project consists of:
1. **Frontend:** A simple web interface that interacts with the backend.
2. **Backend:** A FastAPI application that serves data to the frontend.
3. **Nginx:** A web server used to serve the frontend and forward API requests to the backend.

In short, Nginx handles serving the web pages, and the backend (FastAPI) handles the business logic and API requests.

---

### **Steps to Set Up**


1. **Build and Run Containers with Docker Compose**

   In the project directory (which i suppose you already know how to clone), run:
   ```bash
   docker-compose up --build
   ```

3. **Access the Project Locally**

   Once the containers are running, open your browser and go to:
   - **Frontend:** `http://localhost/`
   - **Backend API (for testing):** `http://localhost/api/`

   You should see the website up and running!

---

### **How It Works**

- **Frontend**: The frontend files (HTML, CSS, JS) are served by **Nginx**, which is a web server.

- **Backend**: The **backend** is a FastAPI application that provides the API (e.g., `/api/`) that the frontend can interact with. Nginx forwards any request starting with `/api/` to the backend container.

- **Nginx**: This is the magic behind everything. It takes care of:
  - Serving static files (like your frontend HTML) to visitors.
  - Forwarding API requests to the backend server.

---

### **Some files:**

Here's a quick overview of the project files:

- `docker-compose.yml`: Contains all the service definitions for the frontend, backend, and Nginx.
- `Dockerfile`: Defines how the containers are built and how the frontend is served.
- `nginx/benchai.conf`: The Nginx configuration file that tells Nginx how to route traffic (e.g., serve static files or forward API requests).

---

### **How to Stop Everything**

To stop the Docker containers and shut down the project, run:
```bash
docker-compose down
```
This will stop all the containers and remove any associated resources (everything).

---

### **Updating**
- This setup uses Docker to ensure that everyone has the same environment, making it easier to run the project without worrying about local dependencies.
- If you're making changes to the code, remember to rebuild the containers:
  ```bash
  docker-compose up --build -d
  ```