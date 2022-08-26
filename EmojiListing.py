import re
f =  open("emojis.txt")
g = open("emoji_list2.txt" ,'w')
for line in f.readlines():
    emoji_name = str(re.findall(r':\w*:', line)).strip("[]':")
    emoji_id = str(re.findall(r':\d*>' , line)).strip("[]':>")
    print(emoji_id)
    text = '"' + emoji_name + '":[ "' + line.replace('\n' , '') + '",'+ f"{emoji_id}" + '],' + '\n'
    print(text)
    g.write(text)
f.close
g.close

    
