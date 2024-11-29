data_panen= {
    'lokasi1':{
        'nama_lokasi': 'Kebun A',
        'hasil_panen':{
            'padi':1200,
            'jagung':800,
            'kedelai':500
        }
    },
    'lokasi2':{
        'nama_lokasi': 'Kebun B',
        'hasil_panen':{
            'padi':1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'lokasi3':{
        'nama_lokasi': 'Kebun C',
        'hasil_panen':{
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4':{
        'nama_lokasi': 'Kebun D',
        'hasil_panen':{
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5':{
        'nama_lokasi': 'Kebun E',
        'hasil_panen':{
            'padi':1400,
            'jagung':950,    
            'kedelai':480
        }
    }
}

panen_padi=[]
panen_kedelai=[]

print(data_panen)
print('Jumlah jagung di lokasi2 adalah',data_panen['lokasi2']['hasil_panen']['jagung'])
print('Nama lokasi3 adalah',data_panen['lokasi3']['nama_lokasi'])

for i,j in data_panen.items():
    panen_padi.append(j['hasil_panen']['padi'])
    panen_kedelai.append(j['hasil_panen']['kedelai'])

jumlah_padi=sum(panen_padi)
jumlah_kedelai=sum(panen_kedelai)

print(panen_padi)
print(panen_kedelai)

print('Jumlah padi di seluruh kebun adalah',(jumlah_padi))
print('Jumlah kedelai di seluruh kebun adalah',(jumlah_kedelai))

for i, j in data_panen.items():
    if j['hasil_panen']['padi'] > 1300 or j['hasil_panen']['jagung'] > 800:
        print(f"Lokasi {j['nama_lokasi']} memiliki hasil panen padi {j['hasil_panen']['padi']} dan jagung {j['hasil_panen']['jagung']} sehingga memerlukan perhatian khusus")
    else:
        print(f"Lokasi {j['nama_lokasi']} memiliki hasil panen padi {j['hasil_panen']['padi']} dan jagung {j['hasil_panen']['jagung']} sehingga dalam kondisi baik")