from fastapi import FastAPI
from fastmcp import FastMCP
from pydantic import BaseModel
from typing import Union
import uvicorn


class InputMulV2(BaseModel):
    a: Union[int, float]
    b: Union[int, float]


app= FastAPI(title="Simple MCP demo Using FastAPI",
             version="1.0",
            docs_url="/docs",  # Change the documentation URL
            openapi_url="/openapi.json"  )

mcp = FastMCP(name="Demo MCP Server", 
              instructions= "Server")


@app.get("/")
async def main():
    # print("Hello from mcp1!")
    return {"message": "Hello frpm mcp1!"}

#Multiplication tool
@mcp.tool()
async def multiply(a,b):
    """Multipliy (a,b), To multiply two numeric values 
    Inputs: 
        a: int or float 
        b: int or float 
    Reurns: 
         multiplication of a & b """
    return a*b


class InputMul(BaseModel):
    a: int | float 
    b: int | float

@app.post("/calc/mul")
async def call_multiply(data:InputMulV2):
    result = await multiply(data.a, data.b)
    return {"result": str(result)}
    


if __name__ == "__main__":
    # main()
    uvicorn.run(app, port= 8000, log_level="info")
