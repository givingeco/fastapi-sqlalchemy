from fastapi import FastAPI
from routes.index import testApi, createTxnApi, getTxnApi, deleteTxnApi, deleteTxnsApi, \
    deleteAllApi, updateTxnApi, getAllApi

app = FastAPI ()

app.include_router(testApi)
app.include_router(createTxnApi)
app.include_router(getTxnApi)
app.include_router(deleteTxnApi)
app.include_router(deleteTxnsApi)
app.include_router(deleteAllApi)
app.include_router(updateTxnApi)
app.include_router(getAllApi)