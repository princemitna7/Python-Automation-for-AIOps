import subprocess

result = subprocess.run(
    ["docker", "ps", "-a", "--format", "{{.Names}}\t{{.Status}}"],
    capture_output=True,
    text=True
)

lines = result.stdout.strip().split('\n')
for line in lines:
    name, status = line.split('\t', 1)
    print(f"{name} - {status}")

