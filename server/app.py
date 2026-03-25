from fastapi import FastAPI
from pydantic import BaseModel
from arduino_manager import ArduinoManager
from command_parser import parse_command

app = FastAPI()
manager = ArduinoManager()

class CommandRequest(BaseModel):
    text: str

@app.post("/pair")
def pair_device(device_id: str):
    return manager.pair(device_id)

@app.post("/command")
def send_command(req: CommandRequest):
    structured = parse_command(req.text)
    return manager.send_command(structured)

@app.get("/devices")
def devices():
    return manager.list_devices()
