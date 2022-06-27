
line_number = 0
vcf = """vCards de iCloud.vcf"""
block_a = []
block_b = [] 
    

with open(vcf, 'r') as file:
    for line in file:
        if line == 'BEGIN:VCARD\n':
            block_a.append(line_number)
        if line == 'END:VCARD\n':
            block_b.append(line_number)
        line_number+=1
    
    
