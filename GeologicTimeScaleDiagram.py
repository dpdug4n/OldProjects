import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

data = [['Eon', 'Era', 'Period', 'Epoch', ' X millions of Years Ago'],
        ['Phanerozoic', 'Cenozoic', 'Quaternary', 'Holocene', 0.01],
        ['Phanerozoic', 'Cenozoic', 'Quaternary', 'Pliestocene', 1.8],
        ['Phanerozoic', 'Cenozoic', 'Tertiary; Neogene','Pliocene', 5.3],
        ['Phanerozoic', 'Cenozoic', 'Tertiary; Neogene','Miocene', 23],
        ['Phanerozoic', 'Cenozoic', 'Tertiary; Paleogene','Oligocene', 33.9],
        ['Phanerozoic', 'Cenozoic', 'Tertiary; Paleogene','Eoocene', 55.8],
        ['Phanerozoic', 'Cenozoic', 'Tertiary; Paleogene','Paleocene', 65.5],
        ['Phanerozoic', 'Mesozoic', 'Cretaceous','', 146],
        ['Phanerozoic', 'Mesozoic', 'Jurassic','', 200],
        ['Phanerozoic', 'Mesozoic', 'Triassic','', 251],
        ['Phanerozoic', 'Paleozoic', 'Permian','', 299],
        ['Phanerozoic', 'Paleozoic', 'Carboniferous; Pennsylvanian','', 318],
        ['Phanerozoic', 'Paleozoic', 'Carboniferous; Mississippian','', 359],
        ['Phanerozoic', 'Paleozoic', 'Devonian','', 416],
        ['Phanerozoic', 'Paleozoic', 'Silurian','', 444],
        ['Phanerozoic', 'Paleozoic', 'Ordovician','', 488],
        ['Phanerozoic', 'Paleozoic', 'Cambrian','', 542],
        ['Proterozoic', '', '','', 2500],
        ['Archean', '', '','', 4000],
        ['Hadean', '', '','', 4560]]
        
diagram = pd.DataFrame(data)
print(diagram)

#set colors and font size
mpl.rcParams['font.size'] = 7
a,b,c,d,e=[plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Oranges,plt.cm.Greys]

eons =['Phanerozoic','Proterozoic - 2500','Archean - 4000', 'Hadean - 4560']
eons_size=[1000,1500,1900,500]
era = ['Cenozoic ','Mesozoic','Paleozoic','']
era_size = [200, 300, 500, 3900]
period = ['Quaternary','Tertiary; Neogene','Tertiary; Paleogene','Cretaceous - 146','Jurassic - 200','Triassic - 251','Permian - 299',
           'Carboniferous; Pennsylvanian - 318','Carboniferous; Mississippian - 359','Devonian - 416','Silurian - 44','Ordovician - 488',
           'Cambrian - 542','']
period_size= [40,60,100, 150,75,75, 91,41,71,71,46,74,106,3900]
period_colors =[a(.5),a(.4),a(.3),a(.5),a(.4),a(.3),a(.5),a(.4),a(.3),a(.5),a(.4),a(.3),a(.5),e(2)]

epoch=['Holocene - .01','Pliestocene - 1.8', 'Pliocene - 5.3','Miocene - 23', 'Oligocene - 33.9','Eoocene - 55.8','Paleocene - 65.5','']
epoch_size=[5,35, 15,45, 25,50,25,4700]
epoch_colors=[a(.7),a(.6),a(.5),a(.7),a(.6),a(.5),a(.7),e(2)]

#chart settings
fig, ax =plt.subplots()
ax.axis('equal')
ax.set_title("Geologic Time Scale Diagram\n" + "Sized and labeled by Millions of years ago")

#eons ring
mypie, _ =ax.pie(eons_size, radius=1.7, labels=eons, labeldistance=1, colors=[a(.8),b(.5),c(.5),d(.5)], rotatelabels=False)
plt.setp( mypie, width=0.3, edgecolor='white')

#era ring
mypie2, _ =ax.pie(era_size, radius=1.6, labels=era, labeldistance=.9, colors=[a(.7),a(.6),a(.5),e(2)],rotatelabels=False)
plt.setp( mypie2, width=0.3, edgecolor='white')

#periods ring
mypie3, _ =ax.pie(period_size, radius=1.4, labels=period, labeldistance=.85, colors=period_colors, rotatelabels=True)
plt.setp( mypie3, width=0.3, edgecolor='white')

#epoch ring
mypie4, _ =ax.pie(epoch_size, radius=1.2, labels=epoch, labeldistance=.6, colors=epoch_colors, rotatelabels=True)
plt.setp( mypie4, width=0.3, edgecolor='white')

plt.show()