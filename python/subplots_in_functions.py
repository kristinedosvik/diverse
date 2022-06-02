import matplotlib.pyplot as plt

def f1(i, a):
    data = [0,2,i]
    
    a[i].plot(data)

def f_all():
   
    fig,axes = plt.subplots(1,2)
    
    f1(1, axes)
    f1(0, axes)

    plt.show()

f_all()


