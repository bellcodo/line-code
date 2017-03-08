# From the user '(3,5)' and '(10,9)'

end_point = '(100,200)'

print end_point

no_parens_start_point = end_point.replace("(","").replace(")", "")
split_start_point = no_parens_start_point.split(',')

print type(split_start_point)

end_point = []
for el in split_start_point:
    print type(el)
    end_point.append(int(el))
   

for el in end_point:
    print type(el)
    
print end_point

