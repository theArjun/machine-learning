from IPython.display import display, HTML
with open('variables.css') as f:
    css = f.read().replace(';', ' !important;')
display(HTML('<style type="text/css">%s</style>Customized changes loaded.'%css))