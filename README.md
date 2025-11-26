# Livepeer BYOC Pulse Service

This project implements a pulse/health check capability for Livepeer BYOC (Bring Your Own Compute).

## Project Structure

- `pulse/` - Pulse service container (Flask app that returns health status)
- `register-capability/` - Container that registers the pulse capability with the orchestrator
- `docker-compose.yml` - Orchestrates all services (orchestrator, gateway, pulse, register_capability)

## Testing the Pulse Service Standalone

Test the pulse service independently without the full BYOC stack:

### Build the Pulse Container

```bash
docker build -t byoc_pulse ./pulse
```

### Run the Pulse Container

```bash
docker run --rm -p 5000:5000 byoc_pulse
```

### Test the Pulse Endpoint

Send a POST request to:
- **URL:** `http://localhost:5000/pulse`
- **Method:** POST
- **Headers:** 
  - `Content-Type: application/json`
- **Body:** `{}` (empty JSON object or omit body)

**Expected Response:**
```json
{
  "status": "OK",
  "code": 200
}
```

### Using cURL

```bash
curl -X POST http://localhost:5000/pulse \
  -H "Content-Type: application/json" \
  -d "{}"
```

### Using Postman

1. Method: **POST**
2. URL: `http://localhost:5000/pulse`
3. Headers:
   - `Content-Type: application/json`
4. Body: Select **raw** → **JSON**, enter: `{}`

## Testing the Full Project

Test the complete BYOC stack with orchestrator, gateway, and pulse service:

### Build All Containers

```bash
docker-compose build
```

### Run All Services

```bash
docker-compose up -d
```

### Test Through the Gateway

Send a POST request to the gateway endpoint:

- **URL:** `http://localhost:9935/process/request/pulse`
- **Method:** POST
- **Headers:**
  - `Content-Type: application/json`
  - `Livepeer: eyJyZXF1ZXN0IjogIntcInJ1blwiOiBcImVjaG9cIn0iLCAiY2FwYWJpbGl0eSI6ICJwdWxzZSIsICJ0aW1lb3V0X3NlY29uZHMiOiAzMCwgInBhcmFtZXRlcnMiOiAie30ifQ==`
- **Body:** `{}` (empty JSON object or omit body)

**Expected Response:**
```json
{
  "status": "OK",
  "code": 200
}
```

### Using cURL

```bash
curl -X POST http://localhost:9935/process/request/pulse \
  -H "Content-Type: application/json" \
  -H "Livepeer: eyJyZXF1ZXN0IjogIntcInJ1blwiOiBcImVjaG9cIn0iLCAiY2FwYWJpbGl0eSI6ICJwdWxzZSIsICJ0aW1lb3V0X3NlY29uZHMiOiAzMCwgInBhcmFtZXRlcnMiOiAie30ifQ==" \
  -d "{}"
```

### Using Postman

1. Method: **POST**
2. URL: `http://localhost:9935/process/request/pulse`
3. Headers:
   - `Content-Type: application/json`
   - `Livepeer: eyJyZXF1ZXN0IjogIntcInJ1blwiOiBcImVjaG9cIn0iLCAiY2FwYWJpbGl0eSI6ICJwdWxzZSIsICJ0aW1lb3V0X3NlY29uZHMiOiAzMCwgInBhcmFtZXRlcnMiOiAie30ifQ==`
4. Body: Select **raw** → **JSON**, enter: `{}`

## Useful Commands

### Check Container Status

```bash
docker-compose ps
```

### View Logs

```bash
# All services
docker-compose logs

# Specific service
docker-compose logs pulse
docker-compose logs register_capability
docker-compose logs gateway
docker-compose logs orchestrator

# Follow logs in real-time
docker-compose logs -f
```

### Stop All Services

```bash
docker-compose down
```

### Rebuild and Restart

```bash
docker-compose down
docker-compose build
docker-compose up -d
```

## Troubleshooting

### Port 5000 Already in Use

If you get an error that port 5000 is already allocated:

1. Find what's using the port:
   ```bash
   netstat -ano | findstr :5000
   ```

2. Stop the process or change the port mapping in `docker-compose.yml`

### Capability Not Registered

If you get "No orchestrators found for capability pulse":

1. Check if the register_capability container is running:
   ```bash
   docker-compose ps register_capability
   ```

2. Check registration logs:
   ```bash
   docker-compose logs register_capability
   ```

3. Restart the registration container:
   ```bash
   docker-compose restart register_capability
   ```

### Gateway Connection Issues

If the gateway endpoint doesn't respond:

1. Verify the gateway is running:
   ```bash
   docker-compose ps gateway
   ```

2. Check gateway logs for errors:
   ```bash
   docker-compose logs gateway
   ```

3. Ensure the orchestrator is running and accessible:
   ```bash
   docker-compose ps orchestrator
   ```

