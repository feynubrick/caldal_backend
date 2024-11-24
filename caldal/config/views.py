import json
from urllib.parse import urlencode

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def oauth_callback(request, provider):
    if request.method == "POST":
        # POST 데이터를 URLSearchParams 형식으로 변환
        params = urlencode(request.POST.dict())

        # Android 앱으로 리다이렉트하는 URI 생성
        redirect_uri = (
            f"intent://callback?{params}"
            f"#Intent;package={settings.CLIENT_APP_ID};"
            "scheme=signinwithapple;end"
        )

        print(f"Redirecting to {redirect_uri}")

        # 307 Temporary Redirect로 리다이렉트
        return HttpResponseRedirect(redirect_uri, status=307)
