import uvicorn

if __name__=='__main__':
    uvicorn.run("main:app", host="0.0.0.0", reload = True, port = 5006, log_level= "info")

