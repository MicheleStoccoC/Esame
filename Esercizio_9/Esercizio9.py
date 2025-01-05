"""
Created on Fri Dec 27 10:03:40 2024

@author: Michele
"""



#import math
import numpy as np
import matplotlib.pyplot as plt



#       Inserimento dati in un unico grande array per gestire i contenuti direttamente senza lavorare sul file

Dati = np.loadtxt('file2_Groups_AGN-wWU_500Mpc_Data.txt') 
# 0:TOTMass, 1:GASMass, 2:DMMass, 3:*Mass, 4:BHMass, 5:PosX, 6:PosY, 7:PosZ


#           PUNTO 1

#       DM_Mass su BM_mass
plt.figure(1)
plt.title("DM_Mass over BM_Mass")
DM_BM = plt.plot(Dati[:,1]+Dati[:,3], Dati[:,2], '.')
plt.xscale('log') #Le 5 strutture più massicce sono fuori scala rispetto alle altre,
plt.yscale('log') #Per poterle includere nel grafico serve la scala log.
plt.xlabel("Massa Barionica (10^10 M_sun/h)")
plt.ylabel("Massa Oscura (10^10 M_sun/h)")
plt.grid(True)


x1=np.arange(0.00003,15,0.00003)
y1=3.0*x1+0.01
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Linear Fit")

ax1.plot(Dati[:,1]+Dati[:,3], Dati[:,2], '.')
ax1.plot(x1, y1, '-')
ax1.set_xlabel("M_Bar (10^10 M_sun/h)")
ax1.set_ylabel("M_Dark (10^10 M_sun/h)")
ax1.grid(True)

ax2.plot(Dati[:,1]+Dati[:,3], Dati[:,2], '.')
ax2.plot(x1, y1, '-')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel("M_Bar (10^10 M_sun/h)")

ax2.grid(True)
plt.show()

#La Most Massive Galaxy (MMG) è fuori scala, si prova il fit lineare senza di essa (è la prima struttura del file)
#prova di fit lineare

m=np.polyfit(Dati[1:455,1]+Dati[1:455,3], Dati[1:455,2], 1)

x2=np.arange(0.00003,2,0.00003)
y2=m[0]*x2+m[1] # m=[4;0.01] sembra meglio...
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Linear Fit - MMG")

ax1.plot(Dati[1:455,1]+Dati[1:455,3], Dati[1:455,2], '.')
ax1.plot(x2, y2, '-')
ax1.set_xlabel("M_Bar (10^10 M_sun/h)")
ax1.set_ylabel("M_Dark (10^10 M_sun/h)")
ax1.grid(True)

ax2.plot(Dati[1:455,1]+Dati[1:455,3], Dati[1:455,2], '.')
ax2.plot(x2, y2, '-')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_xlabel("M_Bar (10^10 M_sun/h)")

ax2.grid(True)
plt.show()



#           PUNTO 2

#      Distanze dalla più massiccia
Maximo = np.zeros(8)
massimo = Dati[:,0].max()
mask = (Dati[:,0]==massimo)
Maximo = Dati[mask,:]
Distanze = np.zeros((len(Dati[:,0]),4))
for i in range(len(Dati[:,0])):
    Distanze[i,0] = Dati[i,5] - Maximo[0,5]
    Distanze[i,1] = Dati[i,6] - Maximo[0,6]
    Distanze[i,2] = Dati[i,7] - Maximo[0,7]
    Distanze[i,3] = np.sqrt(Distanze[i,0]**2 + Distanze[i,1]**2 + Distanze[i,2]**2)
    
#      M_TOT su Distanza
plt.figure(4)
plt.title("M_TOT over Distance")
plt.plot(Distanze[:,3], Dati[:,0], '.', color='red')
plt.ticklabel_format(axis='x', style='sci', scilimits=(0,4))
#plt.xscale('log') 
plt.yscale('log') 
plt.xlabel("Distance from MMG (hkpc/h)")
plt.ylabel("Total Mass (10^10 M_sun/h)")
plt.grid(True)



#           PUNTO 3
Mbins1 = np.geomspace(0.002, 10, 30)

plt.figure(10)
plt.title("DM Halo Distribution")
HistoM = plt.hist(Dati[:, 2], bins=Mbins1, range=[0, 10], rwidth=0.9)  #, histtype='step'
#Media
Media1 = np.mean(Dati[:, 2])
plt.axvline(Media1, color='k', linestyle='dashed', linewidth=1, label=f'Mean: {Media1:.2f}')
#Mediana
Mediana1 = np.median(Dati[:, 2])
plt.axvline(Mediana1, color='k', linestyle='dashdot', linewidth=1, label=f'Median: {Mediana1:.2f}')

plt.text(Media1, plt.ylim()[1] * 0.9, f'{Media1:.2f}', rotation=0, color='k', va='bottom')
plt.text(Mediana1, plt.ylim()[1] * 0.8, f'{Mediana1:.2f}', rotation=0, color='k', va='bottom')

plt.xscale('log')
plt.xlabel("DM Mass (10^10 M_sun/h)")
plt.ylabel("Counts")
plt.grid(True)
plt.legend()
plt.show()


#           PUNTO 4
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Spatial Distributions")

#plt.title("X over Y")
ax1.plot(Distanze[:,0], Distanze[:,1], '.')
ax1.set_xlabel("X from MMG (hkpc/h)")
ax1.set_ylabel("Y from MMG (hkpc/h)")
ax1.grid(True)

#plt.title("Z over Y")
ax2.plot(Distanze[:,2], Distanze[:,1], '.')
ax2.set_xlabel("Z from MMG (hkpc/h)")

ax2.set_yticklabels([])
ax2.grid(True)
plt.subplots_adjust(wspace=0.05)


#   Prova 3 in uno
fig, axis = plt.subplots(2, 2)
fig.suptitle("3 Spatial Distributions")

#plt.title("X over Y")
axis[0,0].plot(Distanze[:,0], Distanze[:,1], '.')
axis[0,0].set_xlabel("X from MMG (hkpc/h)")
axis[0,0].set_ylabel("Y from MMG (hkpc/h)")
axis[0,0].grid(True)

#plt.title("Z over Y")
axis[0,1].plot(Distanze[:,2], Distanze[:,1], '.')
#axis[0,1].set_xlabel("Z from MMG (hkpc/h)")

axis[0,1].set_yticklabels([])
axis[0,1].grid(True)

#plt.title("X over Z")
axis[1,0].plot(Distanze[:,0], Distanze[:,2], '.')
axis[1,0].set_xlabel("X from MMG (hkpc/h)")
axis[1,0].set_ylabel("Z from MMG (hkpc/h)")
axis[1,0].grid(True)

axis[1,1].set_xticks([])
axis[1,1].set_yticks([])
axis[1,1].set_xlabel("Z from MMG (hkpc/h)")

plt.show()




#Prova di uno scatter 3D delle posizioni
'''
fig=plt.figure(21)#Griglia
ax = fig.add_subplot(projection ='3d')
x = Distanze[1:,0]
y = Distanze[1:,1]
z = Distanze[1:,2]
ax.scatter(x, y, z, marker='o', c=Dati[1:,1], alpha=0.4)
plt.tight_layout()
plt.xlabel("Y (hkpc/h)")
plt.ylabel("X (hkpc/h)")
#plt.zlabel("Z (hkpc/h)")
plt.show()
'''

#   Area:(StarMass) & Colore:(GasMass)

plt.figure(6)
plt.title("X-Y Spatial distribution")
plt.scatter(Distanze[:,0], Distanze[:,1], s=Dati[:,3]*1000, c=Dati[:,1], alpha=0.5)
plt.xlabel("X from MMG (hkpc/h)")
plt.ylabel("Y from MMG (hkpc/h)")
plt.colorbar(label="Gas Mass")
plt.figure(7)
plt.title("Z-Y Spatial distribution")
plt.scatter(Distanze[:,2], Distanze[:,1], s=Dati[:,3]*1000, c=Dati[:,1], alpha=0.5)
plt.xlabel("Z from MMG (hkpc/h)")
plt.ylabel("Y from MMG (hkpc/h)")
plt.colorbar(label="Gas Mass")
#La MMG continua ad essere fuori scala, provo a toglierla
plt.figure(8)
plt.title("X-Y Spatial distribution, not MMG")
plt.scatter(Distanze[1:,0], Distanze[1:,1], s=Dati[1:,3]*5000, c=Dati[1:,1], alpha=0.5)
plt.xlabel("X from MMG (hkpc/h)")
plt.ylabel("Y from MMG (hkpc/h)")
plt.colorbar(label="Gas Mass")
plt.figure(9)
plt.title("Z-Y Spatial distribution, not MMG")
plt.scatter(Distanze[1:,2], Distanze[1:,1], s=Dati[1:,3]*5000, c=Dati[1:,1], alpha=0.5)
plt.xlabel("Z from MMG (hkpc/h)")
plt.ylabel("Y from MMG (hkpc/h)")
plt.colorbar(label="Gas Mass")



#           PUNTO 5

BH_min=8*1e-5
mask = ( Dati[:,4] > BH_min )
BH_Dati = Dati[mask]
#Continuo ad escludere la MMG per i soliti motivi di scala
m1=np.polyfit(BH_Dati[1:,3], BH_Dati[1:,4], 1) 
x=np.arange(0,0.9,0.06)
y=m1[0]*x+m1[1]

plt.figure(12)
plt.title("BH_mass over Star_mass")
#plt.plot([0,0.9],[-7e-4,0.009], '-') # Questo funziona meglio se si esclude anche la seconda MMG
plt.plot(x, y, '-')
plt.plot(BH_Dati[1:,3], BH_Dati[1:,4], '.')
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel("Star_mass (10^10 M_sun/h)")
plt.ylabel("BH_mass (10^10 M_sun/h)")
plt.grid(True)




#           PUNTO 6

Massa_min = 0.307

# Seleziona gli aloni più massicci che superano la soglia
Massicci = Dati[Dati[:,1] > Massa_min]

Dist = np.zeros((len(Dati[:,0]),len(Massicci[:,0])))

for j in range(len(Massicci[:,0])):
    for i in range(len(Dati[:,0])):
        X = Massicci[j,5]-Dati[i,5]
        Y = Massicci[j,6]-Dati[i,6]
        Z = Massicci[j,7]-Dati[i,7]
        Dist[i,j] = np.sqrt(X**2+Y**2+Z**2)

# Binning per massa e distanza
Mbins = np.geomspace(min(Dati[:,0]), 10, 45)  # Massa
Dbins0 = np.linspace(0, 2750, 45)  # Distanza

fig1, ax = plt.subplots(tight_layout=True)
plt.title("Distance-M_TOT histogram for M="+str(Massicci[0,0]))
Histo_0 = ax.hist2d(Dati[1:,0], Dist[1:,0], bins=(Mbins, Dbins0)) #, norm=colors.LogNorm() ; aggiungere se si preferisce lo sfondo bianco
plt.xscale('log')
plt.xlabel("Total Mass (10^10 M_sun/h)")
plt.ylabel("Distance (hkpc/h)")
fig.colorbar(Histo_0[3], ax=ax)
#
fig2, ax = plt.subplots(tight_layout=True)
plt.title("Distance-M_TOT histogram for M="+str(Massicci[1,0]))
Histo_1 = ax.hist2d(Dati[1:,0], Dist[1:,1], bins=(Mbins, Dbins0)) #, norm=colors.LogNorm()
plt.xscale('log')
plt.xlabel("Total Mass (10^10 M_sun/h)")
plt.ylabel("Distance (hkpc/h)")
fig.colorbar(Histo_1[3], ax=ax)
#
fig3, ax = plt.subplots(tight_layout=True)
plt.title("Distance-M_TOT histogram for M="+str(Massicci[2,0]))
Histo_2 = ax.hist2d(Dati[1:,0], Dist[1:,2], bins=(Mbins, Dbins0)) #, norm=colors.LogNorm()
plt.xscale('log')
plt.xlabel("Total Mass (10^10 M_sun/h)")
plt.ylabel("Distance (hkpc/h)")
fig.colorbar(Histo_2[3], ax=ax)
#
fig4, ax = plt.subplots(tight_layout=True)
plt.title("Distance-M_TOT histogram for M="+str(Massicci[3,0]))
Histo_3 = ax.hist2d(Dati[1:,0], Dist[1:,3], bins=(Mbins, Dbins0)) #, norm=colors.LogNorm()
plt.xscale('log')
plt.xlabel("Total Mass (10^10 M_sun/h)")
plt.ylabel("Distance (hkpc/h)")
fig.colorbar(Histo_3[3], ax=ax)
#
fig5, ax = plt.subplots(tight_layout=True)
plt.title("Distance-M_TOT histogram for M="+str(Massicci[4,0]))
Histo_4 = ax.hist2d(Dati[1:,0], Dist[1:,4], bins=(Mbins, Dbins0)) #, norm=colors.LogNorm()
plt.xscale('log')
plt.xlabel("Total Mass (10^10 M_sun/h)")
plt.ylabel("Distance (hkpc/h)")
fig.colorbar(Histo_4[3], ax=ax)


M_tot = Dati[1:,0]
D_tot = Dist[1:,0]
for i in range(4):
    M_tot = np.concatenate((M_tot, Dati[1:,0]))
    D_tot = np.concatenate((D_tot, Dist[1:,i+1]))


fig6, ax = plt.subplots(tight_layout=True)
plt.title("Cumulative Distance-M_TOT histogram")
Histo_tot = ax.hist2d(M_tot, D_tot, bins=(Mbins, Dbins0)) #, norm=colors.LogNorm()
plt.xscale('log')
plt.xlabel("Total Mass (10^10 M_sun/h)")
plt.ylabel("Distance (hkpc/h)")
fig.colorbar(Histo_tot[3], ax=ax)
    






