sche = ['เรียนคณิตศาสตร์online','เรียนอังกฤษonline','เรียนไทยonline','เรียนวิทย์online',
        'อ่านเตรียมสอบ o-net','ทำงานบ้าน','เรียนวาดรูป','เรียนร้องเพลง']
l = list(map(str,input().split(',')))

for i in l:
    for j in sche:
        if i==j:
            sche.remove(i)
print('ยังเหลือสิ่งที่ต้องทำอีก {} อย่าง'.format(len(sche)))
for i in sche:
    print('- {}'.format(i))