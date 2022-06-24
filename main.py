# DELETE DUPLICATE CONTACTS


line_number = 0
vcf = """vCards de iCloud.vcf"""
    
with open(vcf, 'r', encoding='utf8') as read_obj:
    block_b = []
    block_e = []
    
    for line in read_obj:
        
        line_number += 1
        
        if 'BEGIN:VCARD' in line:
            block_b.append(str(line_number))
        
        for i in range(int(block_b[-1]) + 100):
            print('a')

            
                 
    print(block_b) 
