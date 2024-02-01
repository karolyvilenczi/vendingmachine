from pydantic import BaseModel

class MachineState(BaseModel):
    desired_state: str