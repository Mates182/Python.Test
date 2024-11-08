from fasthtml.common import *

app, rt = fast_app()

@rt('/change')
def get(): return P('Nice to be here!')

@rt("/")
def get():
    return Div(P("ola"), hx_get="/change")


serve()
