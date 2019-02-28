from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.

#FBV
def userPanel(request):
	usernames = User.objects.all().values("username")
	return render(request, "user.html", {"usernames": usernames})

def getUserInfo(request):
	if request.method == "GET" and request.is_ajax():
		username = request.GET.get("username")
		try:
			user = User.objects.get(username = username)
		except:
			return JsonResponse({"success":False}, status=400)
		user_info = {
			"first_name": user.first_name,
			"last_name": user.last_name,
			"email": user.email,
			"is_active": user.is_active,
			"joined": user.date_joined
		}
		return JsonResponse({"user_info":user_info}, status=200)
	return JsonResponse({"success":False}, status=400)