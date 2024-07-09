from fastapi import FastAPI
from routes.index import testApi, createTxnApi, getTxnApi

app = FastAPI ()

app.include_router(testApi)
app.include_router(createTxnApi)
app.include_router(getTxnApi)