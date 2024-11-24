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
            # 요청 본문이 JSON인 경우
            if request.headers.get("content-type") == "application/json":
                try:
                    data = json.loads(request.body)
                except json.JSONDecodeError:
                    print("Failed to parse JSON body")
                    data = {}
            # 일반 POST 데이터인 경우
            else:
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

            # 307 Temporary Redirect로 리다이렉트
            return HttpResponseRedirect(redirect_uri, status=307)

        # GET 요청 처리 (디버깅용)
        elif request.method == "GET":
            return HttpResponse(
                "OAuth callback endpoint is working. "
                "This endpoint expects POST requests.",
                content_type="text/plain",
            )

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return HttpResponseBadRequest(f"Error processing request: {str(e)}")
