import os, datetime
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from .models import Usage, User, Device
from .forms import UsageEditForm, DeviceNewForm


# home.html 페이지를 부르는 index 함수
def home(request):
    return render(request, 'app_equipments/base/home.html')


def check_total(request):

    info_list = []
    device_list = Device.objects.all()

    search_key = request.GET.get('search_key')  # 검색어 가져오기
    #print(search_key)
    if search_key:  # 만약 검색어가 존재하면
        device_list = device_list.filter(Q(category__icontains=search_key) | Q(brand__icontains=search_key) | Q(spec__icontains=search_key) | Q(is_assets__icontains=search_key)).distinct()  # 해당 검색어를 포함한 queryset 가져오기

    for i in device_list:
        usage_amount = Usage.objects.filter(device_id=i.device_id)

        info_dic = {
         'device_id': i.device_id,
         'category': i.category,
         'brand': i.brand,
         'purchase_date': i.purchase_date,
         'spec': i.spec,
         'is_assets': i.is_assets,
         'etc': i.etc,
         'total': i.amount,
         'amounts': len(usage_amount),
         'remains': i.amount - len(usage_amount),
        }
        #print(info_dic)

        info_list.append(info_dic)
        #print(info_list)

    return render(request, 'app_equipments/menu/check_total.html', {'info_list': info_list,})


def check_total_new(request):

    # new device
    if request.method == "POST":
        form = DeviceNewForm(request.POST)
        if form.is_valid():
            new_device = form.save()

        return redirect('check_total')
    else:
        form = DeviceNewForm()

    return render(request, 'app_equipments/menu/check_total_new.html', {'form': form, })


def check_total_update(request, device_id):
    device = Device.objects.get(device_id=device_id)
    if request.method == "POST":
        form = DeviceNewForm(request.POST)
        if form.is_valid():
            device.category = form.cleaned_data['category']
            device.brand = form.cleaned_data['brand']
            device.spec = form.cleaned_data['spec']
            device.amount = form.cleaned_data['amount']
            device.purchase_date = form.cleaned_data['purchase_date']
            device.is_assets = form.cleaned_data['is_assets']
            device.etc = form.cleaned_data['etc']
            device.save()

        return redirect('check_total')
    else:
        form = DeviceNewForm(instance=device)

    return render(request, 'app_equipments/menu/check_total_update.html', {'form': form, 'device_id': device_id,})


def check_total_delete(request, device_id):
    device = Device.objects.filter(device_id=device_id)
    device[0].delete()

    return redirect('/check_total/')


def download_tsv(request):
    # 장비 정보를 리스트 담기
    device_id = []
    category = []
    brand = []
    purchase_date = []
    spec = []
    is_assets = []
    etc = []
    total = []
    amounts = []
    remains = []
    device_list = Device.objects.all()
    for i in device_list:
        device_id.append(i.device_id)
        category.append(i.category)
        brand.append(i.brand)
        purchase_date.append(i.purchase_date)
        spec.append(i.spec)
        is_assets.append(i.is_assets)
        etc.append(i.etc)
        total.append(i.amount)

        usage_amount = Usage.objects.filter(device_id=i.device_id)
        amounts.append(len(usage_amount))
        remains.append(i.amount - len(usage_amount))

    user_seat = []
    user_name = []
    user_category = []
    user_brand = []
    user_purchase_date = []
    user_spec = []
    user_is_assets = []
    user_etc = []
    # 직원 정보를 리스트 담기
    user_list = User.objects.all()
    #print(user_list)
    for i in user_list:
        usage_list = Usage.objects.filter(user_id=i.user_id)
        #print(usage_list)
        for j in usage_list:
            split_list = str(j).split('|')
            #print(split_list)
            user_seat.append(split_list[0].strip())
            user_name.append(split_list[1].strip())

            user_category.append(split_list[2].strip())
            user_brand.append(split_list[3].strip())
            user_purchase_date.append(split_list[4].strip())
            user_device = Device.objects.filter(category=split_list[2].strip(), brand=split_list[3].strip(),
                                                purchase_date=split_list[4].strip())
            user_spec.append(user_device[0].spec)
            user_is_assets.append(user_device[0].is_assets)
            user_etc.append(user_device[0].etc)

    users_folder_path = os.path.expanduser('~')
    downloads_path = os.path.join(users_folder_path, 'Downloads', 'GJAC_Equipments')
    file_name = 'GJAC_Equipments_' + datetime.datetime.now().strftime('%Y%m%d') + '.tsv'
    output_path = os.path.join(downloads_path, file_name)
    try:
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)
    except OSError:
        print('Error: Creating directory. ' + downloads_path)

    f = open(output_path, 'w')

    f.write('\n' + '장비 총계 및 사용량' + '\n')
    f.write('구분' + '\t' + '브랜드' + '\t' + '구매일자' + '\t' + '스펙' + '\t' + '자산여부' + '\t' + '기타' + '\t' + '전체량' + '\t' + '사용량' + '\t' + '잔여량' + '\n')
    for i in range(len(device_id)):
        f.write(str(category[i]) + '\t' + str(brand[i]) + '\t' + str(purchase_date[i]) + '\t' +
                str(spec[i]) + '\t' + str(is_assets[i]) + '\t' + str(etc[i]) + '\t' +
                str(total[i]) + '\t' + str(amounts[i]) + '\t' + str(remains[i]) + '\n')

    f.write('\n' + '직원 장비목록' + '\n')
    f.write('자리' + '\t' + '성함' + '\t' + '구분' + '\t' + '브랜드' + '\t' + '구매일자' + '\t' + '스펙' + '\t' + '자산여부' + '\t' + '기타' + '\n')
    for i in range(len(user_seat)):
        f.write(str(user_seat[i]) + '\t' + str(user_name[i]) + '\t' + str(user_category[i]) + '\t' +
                str(user_brand[i]) + '\t' + str(user_purchase_date[i]) + '\t' + str(user_spec[i]) + '\t' +
                str(user_is_assets[i]) + '\t' + str(user_etc[i]) + '\n')

    f.close()

    return render(request, 'app_equipments/menu/download_tsv.html', {})


def check_seat(request, office, seat):

    # get seat list
    seat_all = User.objects.all()

    # get user info
    user = User.objects.get(seat=seat)
    #print('3 :', user)

    # get usage info
    usage = Usage.objects.filter(user_id=user.user_id).order_by('device_id')
    #print('4 :', usage)

    # make usage list
    device_usage_info = []
    for i in usage:
        device = str(i.device_id).split('|')
        #print('5 :', device)
        #print('6 :', device[0])
        #print('7 :', device[1])
        device_spec = Device.objects.filter(category=device[0].strip(), brand=device[1].strip())
        #print('8 :', device_usage)
        #print('9 :', device_usage[0].spec)
        device_info = {
            'device_id': device_spec[0].device_id,
            'category': device[0],
            'brand': device[1],
            'spec': device_spec[0].spec,
            'is_assets': device_spec[0].is_assets
        }
        device_usage_info.append(device_info)
        #print('10 :', device_usage_info)

    # new usage
    if request.method == "POST":
        form = UsageEditForm(request.POST)
        if form.is_valid():
            new_usage = form.save(commit=False)
            new_usage.user_id = user
            new_usage.save()

            seat = user.seat
            get_page = '/check_seat/' + str(office) + '/' + str(seat)

        return redirect(get_page)
    else:
        form = UsageEditForm()

    return render(request, 'app_equipments/menu/check_seat.html', {'seat_all': seat_all, 'user': user, 'device_usage_info': device_usage_info, 'form': form, 'office': office})


def check_seat_delete(request, user_id, device_id, office):
    usage = Usage.objects.filter(user_id=user_id, device_id=device_id)
    #print(usage)
    usage[0].delete()

    user = User.objects.get(user_id=user_id)
    seat = user.seat
    get_page = '/check_seat/' + str(office) + '/' + str(seat)

    return redirect(get_page)


def notification(request):
    return render(request, 'app_equipments/menu/notification.html')