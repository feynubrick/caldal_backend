import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def oauth_callback(request, provider):
    if request.method == "POST":
        try:
            payload = json.loads(request.POST.get("payload", "{}"))
            print(f"provider: {provider}")
            print(f"payload: \n{json.dumps(payload, indent=4)}")
        except json.JSONDecodeError:
            print("Invalid JSON payload")

    html_content = """
    <html>
    <head>
        <title>Authentication Complete</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f5f5f5;
            }
            .message {
                text-align: center;
                padding: 20px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="message">
            <p>인증이 완료되었습니다. 잠시 후 창이 자동으로 닫힙니다.</p>
        </div>
        <script>
            window.onload = function() {
                setTimeout(function() {
                    window.close();
                }, 1000);
            }
        </script>
    </body>
    </html>
    """

    return HttpResponse(
        content=html_content, content_type="text/html; charset=utf-8", status=200
    )
