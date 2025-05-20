import os
import time
import requests

def main():
    os.system("echo 'Starting server at 8080' > start.log")
    while True:
        if os.system(f"curl -o /tmp/data.json http://127.0.0.1:8080"):
            with open("/tmp/data.json", "a") as f:
                f.write(f"{'-' * 49}\n")
                f.write("{" + "\n".join(["\"name\": \"data", "\"version\": \"1.0\""]) + "\n}")
                time.sleep(5)
        else:
            with open("/tmp/data.json", "a") as f:
                f.write(f"{'-' * 49}\n")
                f.write("{" + "\n".join(["\"name\": \"data", "\"version\": \"1.0\""]) + "\n}")
                time.sleep(5)

if __name__ == "__main__":
    main()
