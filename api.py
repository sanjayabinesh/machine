from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class MachineRequest(BaseModel):
    thread: str
    machineId: int


@app.post("/api/run-machine")
def run_machine(data: MachineRequest):

    machine_id = data.machineId
    thread_name = data.thread

    print(
        f"API received → {thread_name} → Machine {machine_id}"
    )

    return {
        "success": True,
        "thread": thread_name,
        "machineId": machine_id,
        "message": f"Machine {machine_id} completed"
    }
