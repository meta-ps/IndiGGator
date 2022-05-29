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
        else:
            return redirect('userpage',WalletAddress)
    
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
    userobj  =User.objects.get(walletAddress=walletAddress)
    try:
        userCourses = courseCompleted.objects.get(user=userobj)
    except:
        userCourses = None
    context = {'walletAddress':walletAddress,'user':userobj,'coursesDoneByUser':userCourses}
    return render(request,'userpage.html',context)

def quizzPage(request,walletAddress,quizId):
    if request.method == 'POST':
        print('Hello I am Here')
        print(request.POST)
        obj = NoOfWeeks.objects.get(quizzId=quizId)
        questions = Question.objects.filter(weekId=obj)
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print("Question-> "+request.POST.get(q.question)+"  "+q.ans)
            print()
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        canIsendNFT= False
        
        print(percent)
        print(quizId)
        if(percent >= 60):
            canIsendNFT=True
            user = User.objects.get(walletAddress=walletAddress)
            course,_ = courseCompleted.objects.get_or_create(user=user)
            print('Helsdcsdcsdc  ')
            print(course)
            if(quizId=="1"):
                course.isWeek1Completed = True
            elif(quizId=="2"):
                course.isWeek2Completed = True
            elif(quizId=="3"):
                course.isWeek3Completed = True
            elif(quizId=="4"):
                course.isWeek4Completed = True
            course.save()


        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
            'canIsendNFT':canIsendNFT,
            'walletAddress':walletAddress
        }
        return render(request,'result.html',context)



    obj = NoOfWeeks.objects.get(quizzId=quizId)
    questions = Question.objects.filter(weekId=obj)
    context={'quizId':quizId,'questions':questions}
    return render(request,'quizz.html',context  )

def LogIn(request):
    WalletAddress = request.POST.get('WalletAddress')
    isUserPresent = False
    if(User.objects.get(walletAddress=WalletAddress)):
        return redirect('userpage',WalletAddress)
    else:
        context={'IsUserPresent':False}
        return render(request,'home.html',context)
    