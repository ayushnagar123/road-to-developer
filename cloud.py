import time
import math
import matplotlib.pyplot as plt

def edge_devie(ro,ed):

    thetaed = ed[0]*ed[1]
    ed.append(thetaed)

    phied = ro*ed[0]*ed[1] + ed[1]*(1-ed[0])
    ed.append(phied)

def access_point(ro,ed,ap):

    lambdaap = ed[3] * ((1-ed[0])/(1-ed[0]+ro*ed[0]))
    ap.append(lambdaap)
    betaap = ed[3] * ((ro*ed[0])/(1-ed[0]+ro*ed[0]))

    thetaap = ap[0]*ap[1]
    ap.append(thetaap)

    phiap = ro*ap[1]*ap[0] + ap[1]*(1-ap[0]) + betaap
    ap.append(round(phiap,2))

    ap.append(round(betaap,2))

def latency(ro,ed,ap,cc):
    led = 1/ed[2] + ro/ed[3] + ro/ap[3]
    ed.append(round(led,2))

    lap = 1/ed[3] + 1/ap[2] + ro/ap[3]
    ap.append(round(lap,2))

    lcc = 1/ed[3] + 1/ap[3] +1/cc[2]
    cc.append(round(lcc,2))

def latency_minimization(ed,ap,cc):
    r = ed[1]*(ed[0] * ed[4] + ap[0] * ap[5] + cc[0] * cc[3])
    # Since for all edge devices, lambda , and s is same therefore the latency will be equal for all hence minimum
    return r

def cleaning(L):
    m = L[0]
    flag = 0
    for n,i in enumerate(L):
        if(i<m):
            L[n] = m+flag
        elif(i>m):
            flag = 1
            m = i
    return L

def releasingBuffer(buff1,buff2,buff3):
    buff = []
    flag = 25
    for i in range(len(buff1)):
        buff.append(buff1[i] + buff2[i] + buff3[i])

    for n,i in enumerate(buff):
        if(n<=4):
            buff[n]-=buff[n]
        else:
            buff[n] = i/flag

    return buff

def processingAtED(ed):
    Ted = ed[1] * ed[0] / ed[2]
    ed.append(Ted)

def transmitionToAP(ro , ed,ap,buff1,buff2):
    ted = (ro*ed[0]*ed[1] + ed[1]*(1-ed[0]))/ed[3]
    ed.append(ted)
    buff1.append(math.ceil(3*ed[3] - ap[2]))
    buff2.append(math.ceil(2*ed[3] - ap[2]))

def processingAtAP(ap):
    Tap = 5*ap[1]*ap[0]/ap[2]
    ap.append(Tap)

def transmitionToCC(ro,ap,cc,buff3):
    tap = (5*ap[1]*(1-ap[0]+ro*ap[0]) + 5*ap[4])/ap[3]
    ap.append(tap)
    buff3.append(math.ceil(2*ap[3] - cc[2]))

def processingAtCC(cc):
    Tcc = 5*cc[1]/cc[2]
    cc.append(Tcc)

def recoveryTime(ed,ap,cc):
    ed1 = max(ed[5],ed[6])
    ap1 = max(ap[6],ap[7])
    m1 = max(ed1,ap1)
    Tr = max(m1,cc[4])
    return Tr

def EDLayerOptimization(ro,ed):
    phied_new = ed[2]*((1-ed[0] + ro*ed[0])/ed[0])
    phiap1_new = 3*phied_new
    phiap2_new = 2*phied_new
    return (phied_new , phiap1_new ,phiap2_new)

def APLayerOptimization(ed,ap):
    # Ted(j,i) = Ted(j' , i') is already fulfilled
    if(ap[6]!=ed[5]):
        Tap_new = ed[5]
        return Tap_new
    else:
        return 0

def CCLayerOptimization(ap,cc):
    # Ted(j,i) = Ted(j' , i') is already fulfilled
    # Also Ted(j',i') = Tap(j) is also checked
    if(ap[6]!=cc[4]):
        Tcc_new = ap[6]
        return Tcc_new
    else:
        return 0


if __name__ == "__main__":

    plt.title("Representation of 1 CC , 2 AP's & 5 ED's (Top-Bottom)")

    plt.scatter(5,10,s=300,)
    plt.scatter(3, 8,s=150)
    plt.plot([3,5],[8,10])
    plt.scatter(7, 8,s=150)
    plt.plot([7,5],[8,10])

    plt.scatter(2,6)
    plt.plot([2,3],[6,8])
    plt.scatter(3,6)
    plt.plot([3,3],[6,8])
    plt.scatter(4, 6)
    plt.plot([4,3],[6,8])

    plt.scatter(6,6)
    plt.plot([6,7],[6,8])
    plt.scatter(8,6)
    plt.plot([8,7],[6,8])
    plt.axis('off')

    plt.show()

    sed = 0.05
    sap = 0.3
    scc = 0.65
    ro = 0.1
    x = []
    for i in range(1,481,60):
        x.append(i)

    print("Lambda for ED's are:- ",x)
    L = []
    Tprocess = []
    T = []
    buff = []
    buff1 = []
    buff2 = []
    buff3 = []

    for lambdaed in x:
        ed = []
        ed.append(sed)
        ed.append(lambdaed)
        edge_devie(ro,ed)
        # ed  = [ s , lambda , theta , phi , Latency , T , t]

        ap = []
        ap.append(sap)
        access_point(ro,ed,ap = ap)
        # ap = [s , lambda , theta , phi , beta , Latency , T , t ]

        cc = []
        cc.append(scc)
        r = ro * ed[0] / (1-ed[0])
        lambdacc = ed[3]*(1-ap[0])/(1-ap[0] + ro*ap[0]+r)
        cc.append(round(lambdacc,2))
        cc.append(round(lambdacc, 2))
        # cc = [s , lambda , theta , Latency , T ]

        latency(ro,ed=ed , ap=ap , cc=cc)
        # print("ED:- ",ed)
        # print("AP:- ", ap)
        # print("CC:- ", cc)

        L.append(math.trunc(latency_minimization(ed=ed , ap = ap , cc=cc)))
        L = cleaning(L)

        processingAtED(ed)
        transmitionToAP(ro,ed = ed,ap=ap,buff1=buff1,buff2=buff2)
        processingAtAP(ap)
        transmitionToCC(ro,ap = ap,cc=cc,buff3=buff3)
        processingAtCC(cc)

        T.append(round(recoveryTime(ed=ed , ap=ap , cc=cc),3))
        Tprocess.append(round((ed[5] + ap[6] + cc[4]) , 3))

        time.sleep(0.7)
        print('\n\n ED LAYER OPTIMIZATION \n')
        a1,a2,a3 = EDLayerOptimization(ro,ed=ed)

        if(a1!=ed[3]):
            print("The phi at ED should be:- %.2f"%(a1)," Instead of:- %.2f"%(ed[3]))
        elif(ap[3]!=a2):
            print("The phi at AP1 should be:- %.2f"%(a2), " Instead of:- %.2f"%(ap[3]))
        elif(ap[3]!=a3):
            print("The phi at AP2 should be:- %.2f"%(a3), " Instead of:- %.2f"%(ap[3]))
        else:
            print("Same")


        time.sleep(0.7)
        print('\n\n AP LAYER OPTIMIZATION\n')
        tap_new = APLayerOptimization(ed=ed,ap=ap)
        if(tap_new!=0 and tap_new != ap[6]):
            print("The T (processing time) at AP's should be:- %.2f"%(tap_new)," instead of :-%.2f"%(ap[6]))
        else:
            print("The T (processing time) at AP's should be same:- %.2f"%(ap[6]))

        time.sleep(0.7)
        print('\n\n CC LAYER OPTIMIZATION \n')
        tcc_new = CCLayerOptimization(ap=ap,cc=cc)
        if(tcc_new !=0 and tcc_new != cc[4]):
            print("The T (processing time) at CC should be:- %.2f "%(tcc_new), " instead of:- %.2f"%(cc[4]))
        else:
            print("The T (processing time) at CC should be same :- %.2f"%(cc[4]))


    print("Latencies are:- ",L)
    m = max(L)
    plt.title('Graph 1 (Non-Blocking)')
    plt.xlabel("Data Generation")
    plt.ylabel("System Latency")
    plt.plot(x , L ,marker='*',markerfacecolor='red',linestyle='--',color='yellow',linewidth=2,markersize=10)
    plt.axis([-2,500,3,m+2])
    plt.show()

    print("Processing Time:- ",Tprocess)
    m = max(Tprocess)
    plt.title('Graph 2 (Blocking)')
    plt.xlabel("Data Generation")
    plt.ylabel("Processing Time")
    plt.plot(x,Tprocess,marker='o',markerfacecolor='yellow',linestyle='-',color='blue',linewidth=1,markersize=5)
    plt.axis([-2, 500, 5, m + 2])
    plt.show()

    print("Recovery Time:- ",T)
    m = max(T)
    plt.title('Graph 3 (Blocking)')
    plt.xlabel("Data Generation")
    plt.ylabel("Recovery Time")
    plt.plot(x, T, marker='o', markerfacecolor='magenta', linestyle='-', color='black', linewidth=1, markersize=5)
    plt.axis([-2, 500, 0, m + 2])
    plt.show()

    print("Packets waiting in the buffers:-\n",buff1,"\n",buff2,"\n",buff3)
    plt.title('Graph 4 (Blocking)')
    plt.xlabel("Data Generation")
    plt.ylabel("Packets in Buffer")
    buff = releasingBuffer(buff1=buff1,buff2=buff2,buff3=buff3)
    plt.plot(x, buff1, marker='o', markerfacecolor='magenta', linestyle='-', color='black', linewidth=1, markersize=5,label="B/w ED's & AP1")
    plt.plot(x, buff2, marker='s', markerfacecolor='yellow', linestyle='-', color='black', linewidth=1, markersize=5,label="B/w ED's & AP2")
    plt.plot(x, buff3, marker='*', markerfacecolor='red', linestyle='-', color='black', linewidth=1, markersize=7,label="B/w AP's & CC")
    plt.plot(x,buff,marker='D',markerfacecolor='green',linestyle='-',color='black',linewidth=2,markersize=5,label='Final buffer after releasing pkts')
    plt.legend()
    plt.axis([-2, 500, -3, 1500])
    plt.show()