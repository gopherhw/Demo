from django.shortcuts import render, redirect
from app01 import models
def set_teachers(request):
    if request.method=='GET':
        nid=request.GET.get('nid','')

        cls_obj=models.Classes.objects.get(id=nid)
        cls_teacher_list=cls_obj.a.all()
        all_teacher_list=models.Teachers.objects.all()
        return render(request,'set_teachers.html',{
            'cls_teacher_list':cls_teacher_list,
            'all_teacher_list':all_teacher_list,
            'nid':nid,
        })
    elif request.method=='POST':
        nid = request.POST.get('nid', '')
        ids_str=request.POST.getlist('teacher_id','')
        ids_int=[]
        for i in ids_str:
            i=int(i)
            ids_int.append(i)
        obj=models.Classes.objects.get(id=nid)
        obj.a.set(ids_int)
        return redirect('/classes.html')