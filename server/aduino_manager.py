import socket

class ArduinoManager:
    def __init__(self):
        self.devices = {}  # device_id → (ip, port)

    def pair(self, device_id, ip="127.0.0.1", port=9000):
        self.devices[device_id] = (ip, port)
        return {"status": "paired", "device": device_id}

    def list_devices(self):
        return self.devices

    def send_command(self, command):
        results = {}
        for device_id, (ip, port) in self.devices.items():
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((ip, port))
                    s.sendall(str(command).encode())
                    results[device_id] = "sent"
            except Exception as e:
                results[device_id] = str(e)
        return results
