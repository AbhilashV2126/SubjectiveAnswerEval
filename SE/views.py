from datetime import datetime
import Levenshtein
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from SE.models import *
from SE.test import checkans
import language_tool_python


def firsts(request):
    return render(request, 'login_index.html')

def logincode(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    try:
        ob=login_table.objects.get(username=uname,password=pswd)
        if ob.type == "admin":
            return HttpResponse('''<script>alert('Welcome');window.location='/adminpg'</script>''')
        elif ob.type == "staff":
            request.session["lid"]=ob.id
            return HttpResponse('''<script>alert('Welcome');window.location='/shme'</script>''')
        elif ob.type == "student":
            request.session["lid"] = ob.id
            ob2=students_table.objects.get(LOGIN=ob.id)
            request.session["student_course"]=ob2.COURSE.id
            request.session["student_sem"]=ob2.Sem
            return HttpResponse('''<script>alert('Welcome');window.location='/stdhme'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid Username or password');window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert('Invalid Username or password');window.location='/'</script>''')


def add_crs(request):
    return render(request, 'admin/add course.html')

def add_not(request):
    return render(request, 'admin/ADD NOTI.html')


def add_q(request):
    ob=exam_table.objects.filter(subject__STAFF__LOGIN__id=request.session['lid'])
    return render(request, 'staff/Add q.html',{'val':ob})


def editqs(request,id):
    request.session['oo']=id
    ob=assign_sub_table.objects.filter(STAFF__LOGIN__id=request.session['lid'])
    obb=question_table.objects.get(id=id)
    return render(request,"staff/edit question.html",{"val":ob,'v':obb})


def edit_question(request):
    question = request.POST['textfield']
    mark=request.POST['mark']
    asub = request.POST['select']
    ob = question_table.objects.get(id=request.session['oo'])
    ob.assign_sub=assign_sub_table.objects.get(id=asub)
    ob.question = question
    ob.mark=mark
    ob.save()
    return HttpResponse('''<script>alert('Edited succesfully');window.location='/mng_qus'</script>''')


def add_question(request):
    question = request.POST['textfield']
    mark = request.POST['mark']
    asub = request.POST['select']
    ob = question_table()
    ob.EXAMID_id=asub
    ob.question = question
    ob.mark = mark
    ob.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/mng_qus'</script>''')

def mng_anskey(request,id):
    request.session['qid']=id
    keeee=question_keys.objects.filter(QUESTION_id=id)
    return  render(request,"staff/manage_question_keys.html",{"key":keeee})
def mng_quskey_delete(request,id):
    question_keys.objects.filter(id=id).delete()
    return  mng_anskey(request,request.session['qid'])
def mng_quskey_add(request):
    if request.method=='POST':
        d=request.POST['textfield']
        qukey=question_keys()
        qukey.questionkey=d
        qukey.QUESTION_id=request.session['qid']
        qukey.save()
        return mng_anskey(request,request.session['qid'])
    return   render(request,"staff/Add_manage_keys.html")


def add_staf(request):
    return render(request, 'admin/add staff.html')

def add_std(request):
    ob=courses_table.objects.all()
    obb=students_table.objects.all()
    return render(request, 'staff/add student.html',{'val':ob,'val1':obb})

def search_std(request):
    ob = courses_table.objects.all()
    cid=request.POST['select']
    sem=request.POST['select2']
    obb = students_table.objects.filter(COURSE__id=cid,Sem=sem)
    return render(request, 'staff/add student.html', {'val': ob, 'val1': obb})

def acpt_std(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='student'
    ob.save()
    return HttpResponse('''<script>alert('Accepted');window.location='/add_std'</script>''')


def rjt_std(request,id):
    ob = login_table.objects.get(id=id)
    ob.type = 'reject'
    ob.save()
    return HttpResponse('''<script>alert('Rejected');window.location='/add_std'</script>''')

def addstaffcode(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    gender=request.POST['radio']
    qualification=request.POST['textfield3']
    experience = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    place = request.POST['textfield7']
    username = request.POST['textfield8']
    password = request.POST['textfield9']
    f = request.FILES['f']
    fs=FileSystemStorage()
    fn=fs.save(f.name,f)

    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type="staff"
    ob.save()


    obb=staff_table()
    obb.LOGIN=ob
    obb.firstname=fname
    obb.lastname=lname
    obb.qualification=qualification
    obb.experience=experience
    obb.place=place
    obb.gender=gender
    obb.phone=phone
    obb.email=email
    obb.image=fn
    obb.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/mng_staf'</script>''')


def addcoursecode(request):
    course = request.POST['textfield']
    description = request.POST['textfield2']
    ob=courses_table()
    ob.course=course
    ob.description=description
    ob.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/mng_crs'</script>''')


def addsubcode(request):
    cid=request.POST['select']
    sub=request.POST['textfield']
    sem=request.POST['select2']
    ob=subject_table()
    ob.COURSE=courses_table.objects.get(id=cid)
    ob.subject=sub
    ob.Sem=sem
    ob.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/mng_sub'</script>''')



def add_sub(request):
    ob=courses_table.objects.all()
    return render(request, 'admin/add sub.html',{'val':ob})
def adminpg(request):
    return redirect('/adminhm')

def adminhm(request):
    return render(request,'admin/adminindex.html')

def assignsub(request):
    return render(request, 'admin/ASSIGN SUB.html')
def admexm(request):
    ob = exam_table.objects.filter(subject__SUBJECT__COURSE__id=request.session["student_course"],subject__SUBJECT__Sem=request.session["student_sem"])
    return render(request, 'student/view exm.html',{'val':ob})
def cws(request):
    return render(request, 'staff/chat with student.html')
def mng_crs(request):
    ob = courses_table.objects.all()
    return render(request, 'admin/manage course.html',{'val':ob})
def mng_crs_delete(request,id):
    ob=courses_table.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/mng_crs'</script>''')
def mng_crs_edit(request,id):
    request.session['cid'] = id
    ob=courses_table.objects.get(id=id)
    return render(request,'admin/edit_course.html',{"data":ob})

def course_edit(request):
    course = request.POST['textfield']
    description = request.POST['textfield2']
    ob=courses_table.objects.get(id=request.session['cid'])
    ob.course=course
    ob.description=description
    ob.save()
    return HttpResponse('''<script>alert('updated succesfully');window.location='/mng_crs'</script>''')
def mng_ntf(request):
    return render(request, 'admin/manage notifica.html')
def mng_qus(request):
    # ob = question_table.objects.filter(assign_sub__STAFF__LOGIN=request.session["lid"])
    obb = exam_table.objects.filter(subject__STAFF__LOGIN_id=request.session['lid'])
    return render(request,'staff/manage questions.html',{'exam':obb})
def search_qus(request):
    d=[]
    search = request.POST['select']
    request.session['exam']=search
    obb1 = exam_table.objects.filter(subject__STAFF__LOGIN_id=request.session['lid'])
    obb = assign_sub_table.objects.filter(STAFF__LOGIN_id=request.session['lid'])
    d=question_table.objects.filter(EXAMID_id=search)
    return render(request, 'staff/manage questions.html', {'sub': d, 'val1':obb,'exam':obb1, 'search': int(search)})


def mng_qus_delete(request,id):
    ob=question_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/mng_qus'</script>''')

def mng_staf(request):
    ob=staff_table.objects.all()
    return render(request, 'admin/manage stff.html',{'val':ob})

def mng_staf_delete(request,id):
    ob=staff_table.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/mng_staf#about'</script>''')

def mng_staf_edit(request,id):
    request.session['sid']=id
    ob=staff_table.objects.get(id=id)
    return render(request,'admin/edit_staff.html',{"data":ob})

def edit_staf(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    gender=request.POST['radio']
    qualification=request.POST['textfield3']
    experience = request.POST['textfield4']
    phone = request.POST['textfield5']
    email = request.POST['textfield6']
    place = request.POST['textfield7']

    obb=staff_table.objects.get(id=request.session['sid'])
    obb.firstname=fname
    obb.lastname=lname
    obb.qualification=qualification
    obb.experience=experience
    obb.place=place
    obb.gender=gender
    obb.phone=phone
    obb.email=email
    obb.save()
    return HttpResponse('''<script>alert('updated succesfully');window.location='/mng_staf#about'</script>''')

def mng_stafsearch(request):
    name=request.POST['textfield']
    ob=staff_table.objects.filter(firstname__icontains=name)
    return render(request, 'admin/manage stff.html',{'val':ob})


def mng_sub(request):
    obc=courses_table.objects.all()
    ob=subject_table.objects.all()
    return render(request, 'admin/manage sub.html',{"val":ob,"obc":obc})

def mng_sub_delete(request,id):
    ob=subject_table.objects.filter(id=id).delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/mng_sub'</script>''')


def assignsub(request):
    obs=staff_table.objects.all()
    oba=assign_sub_table.objects.all()
    sub=[]
    for i in oba:
        sub.append(i.SUBJECT.id)
    ob = subject_table.objects.all()
    return render(request, 'admin/ASSIGN SUB.html',{"val":ob,"val1":obs})

def view_assng_staff(request):
    ob=assign_sub_table.objects.all()
    return render(request, 'admin/view assigned staff.html',{'val':ob})

def assign_sub_delete(request,id):
    ob=assign_sub_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/view_assng_staff#about'</script>''')


def search_sub(request):
    sem=request.POST['select2']
    crs=request.POST['select']
    obc = courses_table.objects.all()
    ob = subject_table.objects.filter(COURSE__id=crs,Sem=sem)
    return render(request, 'admin/manage sub.html', {"val": ob, "obc": obc})


def assign_sub_staff(request):
    staff = request.POST['select']
    subject = request.POST['select2']
    ob=assign_sub_table()
    ob.SUBJECT = subject_table.objects.get(id=subject)
    ob.STAFF =staff_table.objects.get(id=staff)
    ob.save()
    return HttpResponse('''<script>alert('assign succesfully');window.location='/view_assng_staff#about'</script>''')




def view_crs_search(request):
    name = request.POST['textfield']
    ob = courses_table.objects.filter(course__icontains=name)

    return render(request, 'admin/manage course.html', {'val': ob})


def sup(request):
    obc = courses_table.objects.all()
    return render(request, 'student/sign_up_index.html',{"c":obc})

def addsup(request):
    Fname=request.POST['textfield']
    Lname=request.POST['textfield2']
    Gender=request.POST['checkbox']
    Course=request.POST['select2']
    Sem=request.POST['sem']
    Place=request.POST['textfield7']
    Phone= request.POST['textfield6']
    Email=request.POST['textfield5']
    Username= request.POST['textfield4']
    Password = request.POST['textfield3']

    ob=login_table()
    ob.username = Username
    ob.password = Password
    ob.type='pending'
    ob.save()
    f = request.FILES['f']
    fs = FileSystemStorage()
    fn = fs.save(f.name, f)

    obj=students_table()
    obj.LOGIN=ob
    obj.firstname=Fname
    obj.Lname=Lname
    obj.gender=Gender
    obj.COURSE=courses_table.objects.get(id=Course)
    obj.Sem=Sem
    obj.place=Place
    obj.phone=Phone
    obj.email=Email
    obj.image = fn
    obj.save()
    return HttpResponse('''<script>alert('added succesfully');window.location='/'</script>''')





def editexam(request,id):
    request.session['pp']=id
    ob = assign_sub_table.objects.filter(STAFF=staff_table.objects.get(LOGIN=request.session["lid"]))
    obb=exam_table.objects.get(id=id)
    return render(request, "staff/edit exam.html", {'ob':ob, 'val':obb, 'date':str(obb.date), 'time':str(obb.time)})

def update_exam_post(request):
   
    date = request.POST['d1']
    time = request.POST['t1']
    ob=exam_table.objects.get(id=request.session['pp'])
   
    ob.date=date
    ob.time=time
    ob.save()
    return HttpResponse('''<script>alert('updaded');window.location='/manage_exam'</script>''')




def shme(request):
    return render(request, 'staff/newstaffindex.html')
def stdhme(request):
    return render(request, 'student/index_student.html')




#----------------------------------staff

def add_exm(request):
    ob = assign_sub_table.objects.filter(STAFF__LOGIN=request.session["lid"])
    return render(request, 'staff/Add exam.html', {'ob':ob})

def add_exam_post(request):
    subject = request.POST['select']
    date = request.POST['d1']
    time = request.POST['t1']
    ob=exam_table()
    ob.subject_id =subject
    ob.date=date
    ob.time=time
    ob.save()
    return HttpResponse('''<script>alert('added');window.location='/manage_exam'</script>''')

def delete_exam_post(request,id):
    ob = exam_table.objects.filter(id=id)
    ob.delete()
    return HttpResponse('''<script>alert('deleted succesfully');window.location='/manage_exam'</script>''')


def manage_exam(request):
    ob=exam_table.objects.filter(subject__STAFF__LOGIN=request.session["lid"])
    return render(request, 'staff/manage exam.html', {'val':ob})









def vasubstf(request):
    ob=assign_sub_table.objects.filter(STAFF=staff_table.objects.get(LOGIN=request.session["lid"]))
    return render(request, 'staff/view assgn sub to stff.html',{"data":ob})

def vasub(request):
    ob = assign_sub_table.objects.filter(STAFF=staff_table.objects.get(LOGIN=request.session["lid"]))
    print("===",ob)
    print("===",request.session["lid"])
    return render(request, 'staff/view assigned subject.html',{"data":ob})



def ve(request):
    return render(request, 'student/view exm.html')



def vnoti(request):
    return render(request, 'staff/view noti.html')
def wrst(request):
    return render(request, 'staff/view reslt.html')





def viewrslt(request):
    obb = students_table.objects.get(LOGIN__id=request.session['lid'])
    cid = obb.COURSE.id
    ob = subject_table.objects.filter(COURSE__id=cid)
    return render(request, 'student/view result.html',{'val':ob})



def viewrslt_search(request):
    subid=request.POST['select']
    obbn = students_table.objects.get(LOGIN__id=request.session['lid'])
    cid = obbn.COURSE.id
    ob = subject_table.objects.filter(COURSE__id=cid)
    obb = attend_exam.objects.filter(STUDENT__LOGIN__id=request.session['lid'], QUESTION__EXAMID__subject__SUBJECT__id=subid)
    test = []
    for item in obb:
        if item.QUESTION.EXAMID not in test:
            test.append(item.QUESTION.EXAMID)
            ob2 = attend_exam.objects.filter(QUESTION__EXAMID=item.QUESTION.EXAMID)
            total_marks = 0
            for i in ob2:
                total_marks = int(total_marks) + int(i.mark)
            test.append(total_marks)
            # row={"testname":i.QUESTION__EXAMID.subject.SUBJECT.subje,"score":total_marks}
            print(test,"dddddddddddddddddddddddddd")



    return render(request, 'student/view result.html',{"t":total_marks,"val":ob})




def view_sample_question(request,id):
        from datetime import date
        today = date.today()
        print(today,"ppppppppppp")
        # qq="SELECT * FROM `test_result` WHERE DATE=CURDATE() AND `candidate_id`=%s and status='completed'"
        res=attend_exam.objects.filter(QUESTION__EXAMID__id=id,STUDENT__LOGIN__id=request.session['lid'])
        # res=selectone(qq,session['lid'])
        if len(res)==0:
            res=question_table.objects.filter(EXAMID__id=id)
            tid = id
            cid = 1
            cnt=0
            request.session['tid']=tid
            request.session['cnt']=cnt
            q=[]
            # res=selectall22("SELECT * FROM `qa` WHERE `exam_id`='"+str(tid)+"'")

            if len(res) != 0:
                s=False
                if len(res)-1 == cnt:
                    s=True
                return render(request,'student/sample.html',{'data':res[0],"s":s,'cnt':int(cnt), 'ln':len(res)})
            else:
                return HttpResponse('''<script>alert("No Questions");window.location="/admexm"</script>''')

        else:
            return HttpResponse('''<script>alert("Attended");window.location="/admexm"</script>''')




def finishexm(request):
    btnv=request.POST['btn']
    if btnv == "next":
        from datetime import date

        tid=request.session['tid']
        cnt=request.session['cnt']
        uans=request.POST['ans']
        ans=request.POST['rans']
        mark=request.POST['mark']
        res = question_table.objects.filter(EXAMID__id=tid)
        # ob=attend_exam()
        # ob.STUDENT = students_table.objects.get(LOGIN__id=request.session['lid'])
        # ob.QUESTION = res[cnt]
        # ob.answer=ans
        #
        # ob.save()
        my_tool = language_tool_python.LanguageTool('en-US')

        my_matches = my_tool.check(uans)
        print(len(my_matches),"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        print(uans)
        print("uaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(ans)
        print("anssssssssssssss")
        mm = checkans(uans, ans)
        
        print(mm,"-----------mm")
       
        totalmark = (mm * (int(mark)*2))
        print(totalmark, "ttttotal")
        if totalmark<0:
            totalmark=0
        dl=[]
        dd=question_keys.objects.filter(QUESTION=res[cnt])
        for i in dd:
            dl.append(i.questionkey)
        
        kk=calculate_similarity(uans,ans)

        # KKark=len(my_matches)//5
        totalmark2 = (kk * (int(mark)*2))
        print(totalmark,totalmark2,"maaarks")
        if totalmark2<0:
            totalmark2=0
        if totalmark2==0 and totalmark==0:

            totalmarks=0
        else:
            totalmarks=(totalmark+totalmark2)/2
        if totalmarks <int(mark)/2:
            j=totalmarks*int(mark)
        else:
            j=totalmarks
        j=round(j,1)
        ob = attend_exam()
        ob.STUDENT=students_table.objects.get(LOGIN__id=request.session['lid'])
        ob.QUESTION=res[cnt]
        ob.mark=j
        ob.answer=uans
        ob.status="pending"
        ob.save()
        request.session['cnt'] = cnt + 1
        
        cnt=cnt+1
        if len(res)==cnt:
            return HttpResponse('''<script>alert("Exam Completed");window.location="/admexm"</script>''')

        else:
            s=False
            if len(res)-1 == cnt:
                s=True
            return render(request,'student/sample.html',{'data':res[cnt],"s":s})
    else:
        from datetime import date

        tid = request.session['tid']
        cnt = request.session['cnt']
        ans = request.POST['ans']
        mm = checkans(uans, ans)
        
        # mmark=len(my_matches)//5
        totalmark = (mm * int(mark))
        print(totalmark, "ttttotal")
        if totalmark<0:
            totalmark=0
        dl=[]
        dd=question_keys.objects.filter(QUESTION=res[cnt])
        for i in dd:
            dl.append(i.questionkey)
        kk=calculate_similarity(uans,ans)

        # KKark=len(my_matches)//5
        totalmark2 = (kk * int(mark))
        print(totalmark,totalmark2,"maaarks")
        if totalmark2<0:
            totalmark2=0
        if totalmark2==0 and totalmark==0:

            totalmarks=0
        else:
            totalmarks=(totalmark+totalmark2)/2
        if totalmarks <int(mark)/2:
            j=totalmarks*int(mark)
        else:
            j=totalmarks
        
        j=round(j,1)
        res = question_table.objects.filter(EXAMID__id=tid)
        ob = attend_exam()
        ob.STUDENT = students_table.objects.get(LOGIN__id=request.session['lid'])
        ob.QUESTION = res[cnt]
        ob.answer = ans
        ob.mark = j
        ob.save()


        request.session['cnt'] = cnt

        if cnt ==0:
            cnt=cnt
        else:
            cnt=cnt-1

                
        return render(request, 'student/sample.html', {'data': res[cnt]})

from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
# Load the pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')


def ss(text1,text2):
    # Tokenize and encode the texts
    inputs1 = tokenizer(text1, return_tensors='pt', padding=True, truncation=True)
    inputs2 = tokenizer(text2, return_tensors='pt', padding=True, truncation=True)

    # Get BERT embeddings
    with torch.no_grad():
        outputs1 = model(**inputs1)
        outputs2 = model(**inputs2)

    # Extract the embeddings
    embeddings1 = outputs1.last_hidden_state[:, 0, :].numpy()
    embeddings2 = outputs2.last_hidden_state[:, 0, :].numpy()

    # Calculate cosine similarity
    similarity_score = cosine_similarity(embeddings1, embeddings2)[0][0]
    print(f"Cosine Similarity: {similarity_score}")
    return similarity_score


def calculate_similarity(text1, text2):
    distance = Levenshtein.distance(text1, text2)
    similarity_score = 1 - (distance / max(len(text1), len(text2)))
    return similarity_score




