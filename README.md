# Portfolio System

A comprehensive portfolio management system built with Vue.js, FastAPI, and MongoDB, containerized with Docker.

## Architecture Overview

The system consists of three main components:

- **Frontend**: Vue.js 3 application with Chart.js for visualizations
- **Backend**: FastAPI-based Python server with data processing capabilities
- **Database**: MongoDB for data persistence

All components are containerized using Docker and orchestrated with Docker Compose.

## Prerequisites

- Docker and Docker Compose
- Node.js 20+ (for local development)
- Python 3.12+ (for local development)
- Git

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/portfolio-system.git
   cd portfolio-system
   ```

2. Create a `.env` file in the root directory:
   ```bash
   MONGO_INITDB_ROOT_USERNAME=admin
   MONGO_INITDB_ROOT_PASSWORD=secure_password
   ```

3. Start the application:
   ```bash
   docker-compose up -d
   ```

The application will be available at:
- Frontend: http://localhost:80
- Backend API: http://localhost:5000
- MongoDB: localhost:27017

## Development

### Frontend Development

```bash
cd frontend
npm install
npm run dev
```

### Backend Development

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## Testing

### Frontend Tests

```bash
cd frontend
npm run test:unit    # Run unit tests
npm run test:e2e     # Run end-to-end tests
```

### Backend Tests

```bash
cd backend
pytest
```

## Project Structure

The complete file structure of the project is organized as follows:

```
portfolio-system/
├── .env                        # Environment variables with MongoDB credentials
├── docker-compose.yml          # Docker composition configuration
│
├── frontend/
│   ├── .vscode/               
│   ├── src/
│   │   ├── assets/           
│   │   ├── components/       
│   │   ├── router/           
│   │   │   └── index.ts      # Vue Router configuration
│   │   ├── stores/          
│   │   ├── App.vue           
│   │   └── main.ts          
│   ├── index.html            
│   ├── package.json          # Frontend dependencies and scripts
│   ├── tsconfig.json         # TypeScript configuration
│   ├── vite.config.ts        # Vite bundler configuration
│   └── Dockerfile           
│
├── backend/
│   ├── requirements.txt      # Python dependencies
│   ├── main.py              # FastAPI application entry point
│   └── Dockerfile          
│
└── mongodb/
    └── mongod.conf          # MongoDB configuration file

Key technology versions:
- Node.js: 20.x (Alpine-based for production)
- Python: 3.12
- Vue.js: 3.5.x
- MongoDB: Latest
```

The project follows a containerized microservices architecture where each component (frontend, backend, and database) is isolated in its own container while maintaining clear communication channels between them.

## Features

- Real-time portfolio tracking
- Market data integration
- Cryptocurrency support
- Banking API integration
- Interactive data visualizations
- Responsive design

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
