from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.parsers import  JSONParser
from myapp.models import Account
from myapp.serializers import AccountSerializers
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Reservation
from myapp.serializers import ReservationSerializer



@csrf_exempt
def data(request):
    if request.method == 'GET':
        query_set = Account.objects.all()
        serializer = AccountSerializers(query_set,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccountSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def register(request):
    if request.method == 'GET':
        query_set = Account.objects.all()
        serializer = AccountSerializers(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)


    elif request.method == 'POST':

        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        data = {'name': name,'phone' : phone, 'email': email, 'password': password}
        serializer = AccountSerializers(data=data)
        # 클라이언트에서 중복 확인
        if not Account.objects.filter(email=email).exists():
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201,content_type="application/json")
        else:
            return JsonResponse({"message": "중복된 아이디입니다."}, status=202)
        return JsonResponse({"message": f"name={name} phone = {phone} email={email} password={password}"}, status=400)  # 올바른 오류 메시지 반환



    elif request.method == 'DELETE':
        if request.method == 'DELETE':
            deleted_count, _ = Account.objects.all().delete()
            if deleted_count > 0:
                # 삭제가 성공적으로 이루어진 경우
                return JsonResponse({"message": f"{deleted_count}개의 계정이 삭제되었습니다."})
            else:
                # 삭제할 데이터가 없는 경우

                return JsonResponse({"message": "삭제할 계정이 없습니다."})
        else:
            return JsonResponse({"message": "잘못된 요청입니다."}, status=400)

@csrf_exempt
def login(request):

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if Account.objects.filter(email=email).exists():
            info = Account.objects.get(email=email)
            pwd = info.password
            if pwd==password:
                id = Account.objects.get(email=email)
                name = id.name
                print(name)
                return JsonResponse({"name":name}, status=201)
            else:
                return JsonResponse({"message": f"비밀번호 오류"}, status=202)
        else:
            return JsonResponse({"message": "정보 없음"}, status=203)
        return JsonResponse({"message": " 잘못된 요청입니다."}, status=400)


@csrf_exempt
def getName(request):
    email = request.GET.get('email','')
    info = Account.objects.get(email=email)
    name = info.name
    phone = info.phone
    email = info.email
    return JsonResponse((name,phone,email), status=201,safe=False)


@csrf_exempt
def reserved(request):
    if request.method == 'GET':
        query_set = Reservation.objects.all()
        serializer = ReservationSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method=="POST":
        day = request.POST.get('day', '')
        time = request.POST.get('time', '')
        minute = request.POST.get('minute','')
        email = request.POST.get('email', '')

        seat = request.POST.get('seat','')

        ex_name = request.POST.get('ex_name', '')
        user_name = request.POST.get('user_name', '')
        user_phone = request.POST.get('user_phone', '')
        data = {'day': day, 'time': time, 'minute': minute, 'email': email,'seat' : seat,'ex_name': ex_name,'user_name':user_name,'user_phone':user_phone}

        serializer = ReservationSerializer(data=data)
        print(serializer)
        if Reservation.objects.filter(day=day,time=time,minute=minute,seat=seat,ex_name=ex_name).exists():
            return JsonResponse({"message": "해당 기구는 이미 예약되어 있습니다."}, status=202)
        else:

            info = Reservation.objects.filter(email=email)
            if Reservation.objects.filter(day=day,time=time,minute=minute).exists():
                return JsonResponse({"message": "선택하신 시간에 다른 운동기구를 예약하셨습니다."}, status=203)
            else:
                print(serializer.is_valid())
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201, content_type="application/json")
        return JsonResponse({"message": " 잘못된 요청입니다."}, status=400)
    elif request.method == 'DELETE':

        deleted_count, _ = Reservation.objects.all().delete()
        if deleted_count > 0:
            # 삭제가 성공적으로 이루어진 경우
            return JsonResponse({"message": f"{deleted_count}개의 데이터가 삭제되었습니다."})
        else:
            # 삭제할 데이터가 없는 경우
            return JsonResponse({"message": "삭제할 계정이 없습니다."})
    else:
        return JsonResponse({"message": "잘못된 요청입니다."}, status=400)
@csrf_exempt
def reservTime(request):
    day = request.POST.get('day', '')
    time = request.POST.get('time', '')
    minute = request.POST.get('minute', '')
    email = request.POST.get('email', '')
    if Reservation.objects.filter(day=day,time=time,minute=minute,email=email).exists():
        return JsonResponse({"message":"선택하신 시간에 다른 운동기구를 예약하셨습니다."}, status=203)
    else:
        return JsonResponse({"message":"예약 가능."}, status=201)
    return JsonResponse({"message": "잘못된 요청입니다."}, status=400)
@csrf_exempt
def reserveMachine(request):
    day = request.POST.get('day', '')
    time = request.POST.get('time', '')
    minute = request.POST.get('minute', '')
    seat = request.POST.get('seat', '')
    ex_name = request.POST.get('ex_name', '')


    print(day,time,minute,seat,ex_name)
    print(Reservation.objects.filter(day=day).exists())
    print(Reservation.objects.filter(time=time).exists())
    print(Reservation.objects.filter(minute=minute).exists())
    print(Reservation.objects.filter(seat=seat).exists())
    print(Reservation.objects.filter(ex_name=ex_name).exists())
    if Reservation.objects.filter(day=day, time=time, minute=minute, seat=seat, ex_name=ex_name).exists():
        return JsonResponse({"message": "해당 기구는 이미 예약되어 있습니다."}, status=202)
    else:
        return JsonResponse({"message": "예약 가능"}, status=201)
    return JsonResponse({"message": "잘못된 요청입니다."}, status=400)

def index(request):
    print(a) #에러발생
    return render(request, 'app1/index.html')