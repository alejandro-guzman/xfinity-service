# Manage Xfinity router through restful service

## Requirements

- Firefox geckodriver
- python3

## Example:

Start the Xfinity service

```bash
python server.py
```

Expose a service port

```bash
$ curl localhost:5000/service \
    --request POST \
    --header "Content-Type: application/json" \
    --date '{"service_name": "MyWebcam", "host": "10.0.0.12", "port": 10550}'
{
  "message": "Create exposed service MyWebcam on 10.0.0.12:10550", 
  "status": "OK"
}
```
