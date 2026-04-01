from flask import Flask, request
import docker

app  = Flask(__name__)
client =  docker.from_env()

@app.route('/webhook',methods=['POST'])
def webhook():
    containers = client.containers.list(all=True)

    print(f"Found {len(containers)} container(s):")
    for container in containers:
        print(f"- {container.name}: {container.status}")

    return {"status": "success","containers_found": len(containers)}, 200

if __name__ == "__main__":
    print("Flask webhook listening on port 5000....")
    app.run(host="0.0.0.0", port=5000)

'''
# python3 webhook_app.py
Flask webhook listening on port 5000...
Found X container(s):
- nginx-exporter: running
- nginx-test: running

# curl -X POST http://localhost:5000/webhook
{"containers_found":2,"status":"success"}

# curl -X POST -H 'Content-Type: application/json' -d '{"alerts":[{"status":"firing","labels":{"alertname":"InstanceDown","instance":"localhost:80"}}]}' http://localhost:5000/webhook

'''