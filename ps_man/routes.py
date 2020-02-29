from starlette.routing import Route
from ps_man.views import homepage, about, api_ps_cpu, api_ps_memory

routes = [
    Route("/", endpoint=homepage),
    Route("/about", endpoint=about),
    Route("/api/cpu/", endpoint=api_ps_cpu),
    Route("/api/memory/", endpoint=api_ps_memory),
]
