from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = f"Received alert: {data}"
    print(message)           
    return message           

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# python3 webhook_app.py
# curl -X POST -H "Content-Type: application/json" -d '{"test":"alert"}' http://localhost:5000/webhook
# Received alert: {'test': 'alert'}

"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    for alert in data.get('alerts', []):
        labels = alert.get('labels', {})
        annotations = alert.get('annotations', {})
        status = alert.get('status', '').upper()
        alertname = labels.get('alertname', 'Unknown')
        job = labels.get('job', 'Unknown')
        instance = labels.get('instance', 'Unknown')
        summary = annotations.get('summary', '')
        print(f"ALERT {status}: {alertname} for job {job} on instance {instance}. Summary: {summary}")
    return "Alerts processed", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# curl -X POST -H "Content-Type: application/json" -d '{
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "alertname": "InstanceDown",
        "job": "node_exporter",
        "instance": "node-exporter:9100",
        "severity": "critical"
      },
      "annotations": {
        "summary": "Instance has been down for more than 1 minute."
      }
    }
  ]
}' http://localhost:5000/webhook

# python3 webhook_app.py
* Running on http://0.0.0.0:5000
ALERT FIRING: InstanceDown for job node_exporter on instance node-exporter:9100. Summary: Instance has been down for more than 1 minute.

"""