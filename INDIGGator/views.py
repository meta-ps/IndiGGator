from django.shortcuts import render
from INDIGGator.models import *



def generateReferalCode():
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_chars = 30
    code = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code



# Create your views here.
def Home(request):

    if request.POST:
        WalletAddress = request.POST.get('WalletAddress')
        userName = request.POST.get('name')
        referalCode = request.POST.get('referalCode')
        print(WalletAddress)
        print(referalCode)
        print(userName)
        IsUserPresent = False
        try:
            if(User.objects.get(walletAddress=WalletAddress)):
                print('User Present')
                IsUserPresent = True
            else:
                IsUserPresent = False
        except:
            pass
        
        if(IsUserPresent==False):
            print('creating new user')
            user = User()
            user.userName = userName
            user.walletAddress = WalletAddress
            user.myRefrealCode = generateReferalCode()




    return render(request,'home.html')








