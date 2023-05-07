from pydantic import BaseModel


class StandardResponse(BaseModel):
    status: bool = True
    description: str = "Operation completed successfully"
