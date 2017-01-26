from django.http import HttpResponse

# Create your views here.


def register_view(request):
    if request.GET['hub.verify_token'] == "aide nashte":
        challenge = request.GET('hub.challenge')
        response = HttpResponse(challenge)
        response.status_code = 200

    else:
        response = HttpResponse
        response.status_code = 403

    return response
