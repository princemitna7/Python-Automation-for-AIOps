from flask import Flask, request
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # IF-THEN pattern: Check alert conditions
    for alert in data.get('alerts', []):
        status = alert.get('status')
        labels = alert.get('labels', {})
        alertname = labels.get('alertname')
        instance = labels.get('instance')

        # IF this alert is firing AND it's an InstanceDown alert
        if status == 'firing' and alertname == 'InstanceDown':
            container_name = 'nginx-test'

            # THEN restart the container with error handling
            try:
                container = client.containers.get(container_name)
                container.restart()
                print(f"Remediation: Restarted container {container_name} for instance {instance}.")
            except docker.errors.NotFound:
                print(f"Remediation error: Container {container_name} not found.")
            except Exception as e:
                print(f"Remediation error: {e}")

    return {"status": "processed"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


'''
# curl -X POST -H 'Content-Type: application/json' -d '{"alerts":[{"status":"firing","labels":{"alertname":"InstanceDown","instance":"localhost:80"}}]}' http://localhost:5000/webhook

'''