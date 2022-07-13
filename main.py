


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
    file.close()

with open(vcf, 'r') as file:

    a = file.readlines()
    print(a[block_a[0]:block_b[0]] == a[block_a[1]:block_b[1]])
    
