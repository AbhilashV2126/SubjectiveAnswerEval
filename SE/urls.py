from django.urls import path

from SE import views

urlpatterns =[
    path('',views.firsts,name='first'),
    path('logincode',views.logincode,name='logincode'),
    path('add_crs',views.add_crs,name='add_crs'),
    path('add_exm',views.add_exm,name='add_exam'),
    path('editexam/<int:id>',views.editexam,name='editexam'),
    path('update_exam_post',views.update_exam_post,name='update_exam_post'),
    path('add_exam_post',views.add_exam_post,name='add_exam_post'),
    path('delete_exam_post/<int:id>',views.delete_exam_post,name='delete_exam_post'),
    path('add_not',views.add_not,name='add_note'),
    path('add_q',views.add_q,name='add_q'),
    path('editqs/<int:id>',views.editqs,name='editqs'),
    path('edit_question',views.edit_question,name='edit_question'),
    path('search_qus',views.search_qus,name='search_qus'),
    path('add_question',views.add_question,name='add_question'),
    path('add_staf',views.add_staf,name='add_staf'),
    path('add_std',views.add_std,name='add_std'),
    path('search_std',views.search_std,name='search_std'),
    path('acpt_std/<int:id>',views.acpt_std,name='acpt_std'),
    path('rjt_std/<int:id>',views.rjt_std,name='rjt_std'),
    # path('addstudentcode',views.addstudentcode,name='addstudentcode'),
    path('add_sub',views.add_sub,name='add_sub'),
    path('adminpg',views.adminpg,name='adminpg'),
    path('assignsub',views.assignsub,name='assignsub'),
    path('assign_sub_delete/<int:id>',views.assign_sub_delete,name='assign_sub_delete'),
    path('admexm',views.admexm,name='admexm'),
    path('cws',views.cws,name='cws'),
    path('mng_crs',views.mng_crs,name='mng_crs'),
    path('mng_crs_delete/<id>',views.mng_crs_delete,name='mng_crs_delete'),
    path('mng_crs_edit/<id>',views.mng_crs_edit,name='mng_crs_edit'),
    path('mng_ntf',views.mng_ntf,name='mng_ntf'),
    path('mng_qus',views.mng_qus,name='mng_qus'),
    path('mng_qus_delete/<id>',views.mng_qus_delete,name='mng_qus_delete'),
    path('mng_staf',views.mng_staf,name='mng_staf'),
    path('mng_staf_delete/<id>',views.mng_staf_delete,name='mng_staf_delete'),
    path('mng_sub',views.mng_sub,name='mng_sub'),
    path('mng_sub_delete/<id>',views.mng_sub_delete,name='mng_sub_delete'),
    
   
    
   
    
    path('sup',views.sup,name='sup'),
    path('shme',views.shme,name='shme'),
    path('stdhme',views.stdhme,name='stdhme'),
    path('vasubstf',views.vasubstf,name='vasubstf'),
    path('vasub',views.vasub,name='vasub'),
    
    
    path('ve',views.ve,name='ve'),
    
    
    
    path('vnoti',views.vnoti,name='vnoti'),
    path('wrst',views.wrst,name='wrst'),
    # path('vstd',views.vstd,name='vstd'),
    path("mng_anskey/<id>",views.mng_anskey),
    path("mng_quskey_delete/<id>",views.mng_quskey_delete),
    path("mng_quskey_add",views.mng_quskey_add),
    path('manage_exam',views.manage_exam,name='manage_exam'),
    
    
    path('viewrslt',views.viewrslt,name='viewrslt'),
    path('addstaffcode',views.addstaffcode,name='addstaffcode'),
    path('addcoursecode',views.addcoursecode,name='addcoursecode'),
    path('addsubcode',views.addsubcode,name='addsubcode'),
    path('search_sub',views.search_sub,name='search_sub'),
    path('assignsub',views.assignsub,name='assignsub'),
    path('assign_sub_staff',views.assign_sub_staff,name='assign_sub_staff'),
    path('view_assng_staff',views.view_assng_staff,name='view_assng_staff'),
    path('mng_stafsearch',views.mng_stafsearch,name='mng_stafsearch'),
    path('view_crs_search',views.view_crs_search,name='view_crs_search'),
    path('course_edit',views.course_edit,name='course_edit'),
    path('edit_staf',views.edit_staf,name='edit_staf'),
    path('mng_staf_edit/<id>',views.mng_staf_edit,name='mng_staf_edit'),
    path('sup', views.sup, name='sup'),
    path('addsup', views.addsup, name='addsup'),
    path('adminhm', views.adminhm, name='adminhm'),


    


    
    path('view_sample_question/<int:id>',views.view_sample_question),
   
    path('finishexm',views.finishexm),
    path('viewrslt_search',views.viewrslt_search)
]