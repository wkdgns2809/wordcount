from django.shortcuts import render

# Create your views here.
def main(request):
    
    
    
    return render(request,'main.html')

def result(request):
    text = request.GET['text']
    word_list = text.split(' ')
    word_dic = {}
    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    
    text = request.GET['text']
    word_list2 = text.split('.')
    word_dic2 = {}
    for word in word_list2:
        if word == '\n':
            pass
        elif word == '':
            pass
        elif word in word_dic2:
            word_dic2[word] += 1
        else:
            word_dic2[word] =1

    text = request.GET['text']
    word_list3 = text.split(' ')
    word_dic3 = {}
    for word in word_list3:
        if word == '\n':
            pass
        elif word == '':
            pass
        elif word in word_dic3:
            word_dic3[word] += 1
        else:
            word_dic3[word] = 1



    
    context = {
        "word_dic" : word_dic,
        "word_dic2" : word_dic2,
        "word_dic3" : word_dic3,
        "text" : text,
        
        
    }

    
    
    
    return render(request,'result.html',context)

def info(request):

    return render(request,'info.html')