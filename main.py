from fasthtml.common import *

app, rt = fast_app()

@rt('/change')
def get(): return P('Nice to be here!')

@rt("/")
def get():
    return Titled(P("ola"), hx_get="/change")


serve()
