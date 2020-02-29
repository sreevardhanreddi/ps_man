from starlette.responses import (
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    UJSONResponse,
)
from starlette.templating import Jinja2Templates

from utils.ps_util_code import get_process_by_cpu_percent, get_process_by_memory_percent

templates = Jinja2Templates(directory="templates")


async def homepage(request):
    return templates.TemplateResponse("index.html", {"request": request})


async def about(request):
    return PlainTextResponse("About")


async def api_ps_cpu(request):
    return UJSONResponse(get_process_by_cpu_percent())


async def api_ps_memory(request):
    return UJSONResponse(get_process_by_memory_percent())
