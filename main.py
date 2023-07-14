from fastapi import FastAPI
from routers.router import router 


app = FastAPI() 
 
app.include_router(router) 
 
'''Las versiones anteriores de Starlette incluían una GraphQLAppclase para integrar conGrafeno.

Quedó en desuso de Starlette, pero si tiene un código que lo usó, puede migrar 
fácilmente astarlette-graphene3, que cubre el mismo caso de uso y tiene una interfaz casi idéntica .'''