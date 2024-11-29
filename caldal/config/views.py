import json
from urllib.parse import urlencode

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def oauth_callback(request, provider):
    try:
        print("=== Request Debug Info ===")
        print(f"Method: {request.method}")
        print(f"Provider: {provider}")
        print(f"Headers: {dict(request.headers)}")
        print(f"Body: {request.body.decode('utf-8')}")
        print(f"POST: {request.POST}")

        if request.method == "POST":
            data = request.POST.dict()
            print(f"Processed data: {data}")

            # POST 데이터를 URLSearchParams 형식으로 변환
            params = urlencode(data)

            # Android 앱으로 리다이렉트하는 URI 생성
            redirect_uri = (
                f"intent://callback?{params}"
                f"#Intent;package={settings.CLIENT_APP_ID};"
                "scheme=signinwithapple;end"
            )

            print(f"Redirecting to {redirect_uri}")

            # HTML과 JavaScript를 사용하여 리다이렉트
            html_content = f"""
            <html>
            <head>
                <title>Redirecting...</title>
            </head>
            <body>
                <script>
                    window.location.replace("{redirect_uri}");
                </script>
                <p>리다이렉트 중입니다...</p>
            </body>
            </html>
            """

            return HttpResponse(html_content)

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return HttpResponse(
            f"""
            <html>
            <body>
                <p>Error: {str(e)}</p>
            </body>
            </html>
            """,
            status=400,
        )
