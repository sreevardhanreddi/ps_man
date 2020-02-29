from starlette.applications import Starlette
from ps_man import routes


app = Starlette(debug=True, routes=routes)

