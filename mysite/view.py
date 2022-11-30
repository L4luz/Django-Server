from django.shortcucuts import render,redirect

def inicio(request):
    return render(request,"index.html")
    
def modelo(request)
    loaded_model =pickle.load(open("finalized_model.sav",'rb'))
    y_pred=loaded_model.predict(x_test_bow)