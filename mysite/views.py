from django.http import HttpResponse

def index(request):
    httpString = """
    <head>
    <meta http-equiv="refresh" content="5;url=polls/">
    </head>
    <body>
    Hi there, welcome to my site.<br/>You will be redirected to <font color="blue">polls</font> page.
    <ul>
    <li><a href="polls/">polls</a></li>
    <li><a href="admin/">admin</a></li>
    </ul>
    </body>
    """
    return HttpResponse(httpString)