import numpy as np
import math

def contas_media(): #encontra a media anual de consumo energetico
    print('Insira o valor das ultimas 12 contas:')
    contas=[0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range(len(contas)):
        num = str(x+1)
        contas[x]= int(input(num+'a: '))
    media = sum(contas)/len(contas)
    return media

#def tamanho_sistema(media):

def hsp():
    L=int(input('Digite a latitude do local:'))
    print('Digite o desvio do norte da placa em relação ao norte magnetico')
    AZ=float(input('(desvio à esquerda -, à direita +):'))
    DM=float(input('Digite a declinação magnetica local(ex:-22.53):'))
    d=1
    DI=0
    while d<=365:
        DM=23.45*np.sin((284+d)/365)
        DI=DI+DM
        d=d+1
    D=math.floor(DI/365)
    W=np.cos(-1*np.tan(L)*np.tan(D))
    N=(2/15)*W
    NM=(N/2)+12
    NN=-(N/2)+12
    NI=math.ceil(NN)
    NX=math.ceil(NM)
    H=NN
    MI=0
    while H>=NI and H<=NX:
        MN=(-1*H+12)*15
        MI=MI+MN
        H=H+1
    M=MI/(NN-NM)
    ZI=np.sin(D)*np.sin(L)+np.cos(D)*np.cos(L)*np.cos(M)
    Z=np.arccos(ZI)
    A=Z-90
    print(AZ,type(AZ))
    print(DM,type(DM))
    AR=AZ-DM
    NDA=1
    IR=0
    while NDA<=365:
        DS=1+0.033*np.cos(360*NDA/365)
        DP=23.45*np.sin((284+NDA)/365)
        print(L,type(L))
        print(DP,type(DP))
        WH=np.arccos(-1*np.tan(L)*np.tan(DP))
        NH=(2/15)*WH
        NL=(NH/2)+12
        NP=-(NH/2)+12
        NS=math.ceil(NL)
        NO=math.ceil(NP)
        HS=NO
        while HS<=NS:
            MS=(-HS+12)*15
            ZH=np.sin(DP)*np.sin(L)+np.cos(DP)*np.cos(L)*np.cos(MS)
            ZS=np.arccos(ZH)
            IRR=1367*DS*np.cos(ZS)
            IH=IRR*0.5
            IR=IR+IH
            HS=HS+1
        NDA=NDA+1
    Iz=IR/365
    HSP=Iz/1000
    B=0
    OI=361
    X=0
    while B<=90:
        OZ=(np.sin(D)*np.sin(L)*np.cos(B))-(np.sin(D)*np.cos(L)*np.sin(B)*np.cos(AR))+(np.cos(D)*np.cos(L)*np.cos(B)*np.cos(M))+(np.cos(D)*np.sin(L)*np.sin(B)*np.cos(AR)*np.cos(M))+(np.cos(D)*np.sin(B)*np.sin(AR)*np.sin(M))
        OM=np.arccos(OZ)
        if OI>OM:
            OI=OM
            X=B
        B=B+1
    print('Hora do Nascer do Sol: \n',NN)
    print('Hora do por do sol: \n',NM)
    print('Angulo Horario: \n', M)
    print('Angulo Zenital: \n',Z)
    print('Angulo de altitude solar: \n',A)
    print('Angulo de incidencia da radiação direta: \n',OI)
    print('Angulo ideal da placa: \n',X)
    print('Irradiancia na terra: \n',Iz)
    print('horas de sol pleno: \n',HSP)

def contas_PreKivy():
    print ("A media e ",contas_media())

#contas_PreKivy()

hsp()
