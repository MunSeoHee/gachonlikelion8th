from django.shortcuts import render, redirect
from .models import Category, Detail
import requests
from xml.dom import minidom
# Create your views here.
typeList = [] #유형분류
nameList = [] #레시피 이름
levelList = [] #난이도
menuImageList = [] #대표 이미지 url

def recipeBase(request):
    api_key = "cbd0c48c7d1cfa5e14f92af7a55ede7b057ca584fdc408b5996526bc55140552"
    # URL이 인코딩된 상태로 제공된 KEY이므로 Decoding이 필요
    api_key_decode = requests.utils.unquote(api_key)
    # 위의 명령어로 URL이 제외된 디코딩 코드
    req = requests.get("http://211.237.50.150:7080/openapi/"+api_key_decode+"/xml/Grid_20150827000000000226_1/1/85")
    xmlraw = minidom.parseString(req.text) #문자열을 xml 파싱이 가능한 형식으로 변형
    clist  = xmlraw.getElementsByTagName("RECIPE_NM_KO") #레시피 이름
    blist = xmlraw.getElementsByTagName("IMG_URL") #대표 이미지 url
    elist = xmlraw.getElementsByTagName("LEVEL_NM") #난이도
    xlist = xmlraw.getElementsByTagName("NATION_NM") #유형분류
    global nameList
    nameList = []
    global menuImageList
    menuImageList = []
    global levelList
    levelList = []
    global typeList
    typeList = []
    for i in range(len(clist)):
        nameList.insert(i, clist[i].firstChild.data)
        menuImageList.insert(i, blist[i].firstChild.data)
        levelList.insert(i, elist[i].firstChild.data)
        typeList.insert(i, xlist[i].firstChild.data)
    return render(request, 'home.html', {'recipeName': nameList, 'menuImage': menuImageList, 'level': levelList , 'type': typeList})


def recipeIngredient(request):
    api_key = "cbd0c48c7d1cfa5e14f92af7a55ede7b057ca584fdc408b5996526bc55140552"
    # URL이 인코딩된 상태로 제공된 KEY이므로 Decoding이 필요
    api_key_decode = requests.utils.unquote(api_key)
    # 위의 명령어로 URL이 제외된 디코딩 코드
    req = requests.get("http://211.237.50.150:7080/openapi/"+api_key_decode+"/xml/Grid_20150827000000000227_1/1/999")
    xmlraw = minidom.parseString(req.text)
    clist = xmlraw.getElementsByTagName("IRDNT_NM") #재료명
    alist = []
    for i in range(len(clist)):
        alist.insert(i, clist[i].firstChild.data)
    return render(request, 'get.html', {'ingredient': alist})

def recipeProcess(request):
    api_key = "cbd0c48c7d1cfa5e14f92af7a55ede7b057ca584fdc408b5996526bc55140552"
    api_key_decode = requests.utils.unquote(api_key)
    req = requests.get("http://211.237.50.150:7080/openapi/"+api_key_decode+"/xml/Grid_20150827000000000228_1/1/471")
    xmlraw = minidom.parseString(req.text)
    clist = xmlraw.getElementsByTagName("COOKING_DC") #요리설명
    alist = []
    for i in range(len(clist)):
        alist.insert(i, clist[i].firstChild.data)
    return render(request, 'get.html', {'cookingProcess': alist})

def get(request):
    category = Category()
    category.level_nm = request.GET.get('level_nm') #난이도
    category.calorie = request.GET.get('calorie') #칼로리
    category.nation_nm = request.GET.get('nation_nm') #유형분류
    category.cooking_time = request.GET.get('cooking_time') #조리시간
    detail = Detail()
    detail.irdnt_nm = request.GET.get('irdnt_nm') #재료
    
    alist = []
    global typeList
    global nameList
    global levelList
    global menuImageList

    if category.nation_nm == "한식":
        for i in range(len(typeList)):
            if typeList[i] == "한식":
                alist.insert(i, i) #한식인 인덱스 값 들어있음
    elif category.nation_nm == "중국":
        for i in range(len(typeList)):
            if typeList[i] == "중국":
                alist.insert(i, i)
    elif category.nation_nm == "일본":
        for i in range(len(typeList)):
            if typeList[i] == "일본":
                alist.insert(i, i)
    elif category.nation_nm == "이탈리아":
        for i in range(len(typeList)):
            if typeList[i] == "이탈리아":
                alist.insert(i, i)
    elif category.nation_nm == "동남아시아":
        for i in range(len(typeList)):
            if typeList[i] == "동남아시아":
                alist.insert(i, i)
    elif category.nation_nm == "퓨전":
        for i in range(len(typeList)):
            if typeList[i] == "퓨전":
                alist.insert(i,i)
    else:
        for i in range(len(typeList)):
            if typeList[i] == "서양":
                alist.insert(i, i)
    
    nameLast = [] #조건에 맞는 레시피이름
    levelLast = [] #조건에 맞는 난이도
    menuImageLast = [] #조건에 맞는 레시피 대표 url
    for i in range(len(alist)):
        nameLast.insert(i, nameList[int(alist[i])])
        levelLast.insert(i, levelList[int(alist[i])])
        menuImageLast.insert(i, menuImageList[int(alist[i])])
        #유형 분류 가져오기

    if not (category.level_nm or category.calorie or category.nation_nm or category.cooking_time or detail.irdnt_nm ):
        return render(request, 'error.html')
    return render(request, 'get.html', {'nameLast': nameLast, 'levelLast': levelLast, 'menuImageLast': menuImageLast})