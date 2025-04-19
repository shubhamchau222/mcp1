import requests

def call_server(a,b):
    response= requests.post(url= "http://127.0.0.1:8000/calc/mul", 
                            json={"a":a, "b":b})

    if response.status_code == 200:
        return {"result": str(response.json())}
    else:
        return {'Error': "There is some Error"}
        
    

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(prog='Client',)

    parser.add_argument("--a", type= lambda x: float(x), default= 2)
    parser.add_argument("--b", type= lambda x: float(x), default= 2)

    args = parser.parse_args()
    input_data= {"a": args.a, "b": args.b}

    reply= call_server(a=input_data.get("a", 0), 
                       b= input_data.get("b", 0))
    print(reply)