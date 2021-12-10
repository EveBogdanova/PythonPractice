import json

with open('image_info_test-dev2017.json','r') as j:
    all = json.load(j)
    l = all['images']
    b = all['categories']
    print(f'\nThis file contains {len(l)} links to images from {len(b)} categories\n')
    filenames = []
    for inf in l:
        name = inf.get('file_name')
        if name == "000000000001.jpg":
            print('URL: ',inf.get('coco_url'),'\nHeight: ',inf.get("height"),'\nWidth: ',inf.get("width"),'\nID: ',inf.get("id"))
        filenames.append(int(name.replace('.jpg','')))
        max_number = max(filenames)
        ind = filenames.index(max_number)
    print('Name of an image with the biggest number: ',l[ind].get('file_name'))
            
            
        
        