from email import contentmanager
from django.shortcuts import render,redirect
from INDIGGator.models import *



def generateReferalCode():
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn'
    num_chars = 30
    code = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code



# Create your views here.
def Home(request):
    IsUserPresent = False


    if request.POST:
        WalletAddress = request.POST.get('WalletAddress')
        request.session['WalletAddress'] = WalletAddress
        userName = request.POST.get('name')
        whoReferedMe = request.POST.get('referalCode')
        print(WalletAddress)
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
            if whoReferedMe:
                print(whoReferedMe)
                user.whoReferedMe=whoReferedMe
            user.save()
            print('user saved')
            return redirect('checkKyc',user.walletAddress)
    
    context={'IsUserPresent':IsUserPresent}
    return render(request,'home.html',context)

def isKycVerified_1(request,walletAddresss):
    request.session['WalletAddress'] = walletAddresss
    print('Kyc User address ='+walletAddresss)
    user =User.objects.get(walletAddress =walletAddresss )
    isVerifiedUser = user.isKycVerified
    context = {'walletAddresss':walletAddresss}
    if(isVerifiedUser=="False"):
        return render(request,'kycForm.html',context)
    else:
        return redirect('userpage',walletAddresss)


def kycFileUploadDone(request,walletAddress):
    request.session['WalletAddress'] = walletAddress
    user = User.objects.get(walletAddress=walletAddress)
    documentFile = request.FILES['documentFile']    
    User.objects.filter(walletAddress=walletAddress).update(isKycVerified='docuploaded')
    print(request.POST.get('fullname'))
    kycdata  = KYCData.objects.get_or_create(user=user,FullName=request.POST.get('fullname'),
        IdNumber=request.POST.get('IdNumber'),documentFile=documentFile
    )

    print('Hello World user verfid and doc uploaded')
    context = {'walletAddresss':walletAddress}

    return redirect('userpage',walletAddress)
    
def UserPage(request,walletAddress):
    request.session['WalletAddress'] = walletAddress
    context = {'walletAddress':walletAddress}
    return render(request,'userpage.html',context)




def quizzPage(request,walletAddress,quizId):

    questions = Question.objects.all()
    context={'quizId':quizId,'questions':questions}
    return render(request,'quizz.html',context  )