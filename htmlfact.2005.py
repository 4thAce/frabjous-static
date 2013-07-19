import sys,os
import re
import time
import string

model = ['','','','']

def setup(modelfilename):
   modelfile = open(modelfilename, 'r')
   index = 0
   for line in modelfile.readlines():
     if (re.search("<title>",line) or re.search("<TITLE>",line)):
       index = 1
       continue
     if (re.search(r'="[dD]escription"',line) or re.search(r'="[Kk]ey[Ww]ords"',line)):
       index = 2
       continue
     if re.search("!-- INSERTCONTENT --",line):
       index = 3
       continue
     model[index] = model[index] + line

def head(headarg):
    desc0='''   <meta name="description" content="'''
    desc1='''" />''' + "\n"
    key0='''    <meta name="keywords" content="'''
    key1='''" />''' + "\n"
    title0 = "\n" + r'<hr><h2><!-- TITLESTART -->'
    title1 = r'<!-- TITLEEND --></h2>' + "\n\n"
    titletag0 = r'  <TITLE>'
    titletag1 = "</TITLE>\n"
    dellink0 = r'<a href="http://del.icio.us/milkfish/'
    dellink1 = r'">'
    dellink2 = "</a>\n"
    techno0 = r'<span class="technoratitag"><a href="http://technorati.com/tag/'
    techno1 = r'" rel="tag">'
    techno2 = "</a></span>\n"
    outfile.write(model[0] + titletag0 + headarg[0] + titletag1 + model[1] + "\n")
    outfile.write(desc0 + headarg[1] + desc1)
    outfile.write(key0 + headarg[2] + key1)
    outfile.write(model[2])
    # Loop over keywords and generate del.icio.us links
    keywords=[eachword.rstrip(",") for eachword in string.split(headarg[2])]
    for word in keywords:
      outfile.write(dellink0 + word + dellink1 + word + dellink2)
    outfile.write("<br>\n")
    # And Technorati tags
    for word in keywords:
      outfile.write(techno0 + word + techno1 + word + techno2)
    outfile.write(title0 + headarg[0] + title1)

def ku3(ku3argv):
    ku0='''<div class="kufirst">
'''
    ku1='''</div>
<div class="kumid">
'''
    ku2='''</div>
<div class="kulast">
'''
    ku3='''</div>
'''
    form0 = r'<div class="form">'
    form1 = r'</div>'
    if len(ku3argv[3]) > 0:
        outfile.write(form0 + ku3argv[3] + form1 + "\n")
    outfile.write(ku0 + ku3argv[0] + ku1 + ku3argv[1] + ku2 + ku3argv[2] + ku3 + "\n")

def ku2(ku2argv):
    zip0='''<div class="split"><span class="lefthalf">
'''
    zip1='''
</span>
<span class="righthalf">
'''
    zip2='''
</span></div>
'''
    form0 = r'<div class="form">'
    form1 = r'</div>'
    if len(ku2argv[2]) > 0:
        outfile.write(form0 + ku2argv[2] + form1 + "\n")
    outfile.write(zip0 + ku2argv[0] + zip1 + ku2argv[1] + zip2 + "\n")

def lim(limarg):
   l12pre = r'<div class="limtop">' + "\n"
   l12post = r'</div>' + "\n"
   l34pre = r'<div class="lim34">' + "\n"
   l34post = r'</div>' + "\n"
   l5pre = r'<div class="limbot">' + "\n"
   l5post = r'</div>' + "\n"
   form0 = r'<div class="form">' + "\n"
   form1 = r'</div>'
   outfile.write(form0 + 'limerick' + form1)
   outfile.write(l12pre + limarg[0] + l12post)
   outfile.write(l12pre + limarg[1] + l12post)
   outfile.write(l34pre + limarg[2] + l34post)
   outfile.write(l34pre + limarg[3] + l34post)
   outfile.write(l5pre + limarg[4] + l5post)

def cinq(cinqarg):
   c1pre = r'<div class="brickfirst">' + "\n"
   cpost = r'</div>' + "\n"
   cmid = r'<div class="brickmid">' + "\n"
   c34post = r'</div>' + "\n"
   c5pre = r'<div class="bricklast">' + "\n"
   form0 = r'<div class="form">' + "\n"
   form1 = "</div>\n"
   outfile.write(form0 + 'cinquain' + form1)
   outfile.write(c1pre + cinqarg[0] + cpost)
   outfile.write(cmid + cinqarg[1] + cpost)
   outfile.write(cmid + cinqarg[2] + cpost)
   outfile.write(cmid + cinqarg[3] + cpost)
   outfile.write(c5pre + cinqarg[4] + cpost)

def esctag(escarg):
    temp = re.sub('&lt;','<',escarg)
    temp = re.sub('&gt;','>',temp)
    outfile.write(temp + "\n")

def plaintxt(plainarg):
    outfile.write(plainarg + "\n")

def tail():
    time0 = r'<div class="timestamp">Originally published: '
    time1 = r'</div>' + "\n"
    endcontline = "<!-- ENDCONTENT -->\n"
    outfile.write(endcontline)
    outfile.write(time0 + time.strftime("%Y/%m/%d %H:%M:%S")  + time1)
    outfile.write(model[3])
    outfile.close()

def grabfile(file2):
    for line in file2.readlines():
        outfile.write(line)
    outfile.write("\n")   # insert a blank line afterwards
    
if __name__ == '__main__':
    if len(sys.argv) < 1:
        sys.stderr.write("Specify the path to the model.html on the command line.")
    setup(sys.argv[1])
    menu = '''
1.  Set up file with header
2.  3 line haiku
3.  1 line haiku with two parts
4.  Limerick
5.  Cinquain
6.  Insert text file
7.  Insert text lines.
8.  Trailer.
x.  Exit.
'''
    #  Keep reading until they hit x.
    while 1:
      # Get input
      sys.stdout.write(menu)
      character = raw_input("Choice: ")
      if(character == '1'):
        filename = ('%X.html' % int(time.time()))
        prompt = "File name (default " + filename + ")="
        response = raw_input(prompt)
        if len(response) > 0:
            filename = response
        outfile = open(filename,'w')
        title = []
        title[0:0] = [raw_input("Title=")]
        title[1:1] = [raw_input("Description=")]
        title[2:1] = [raw_input("Keywords=")]
        head(title)
      elif(character == '2'):
        h3 = []
        h3[0:0] = [raw_input("Line 1=")]
        h3[1:1] = [raw_input("Line 2=")]
        h3[2:2] = [raw_input("Line 3=")]
        h3[3:3] = [raw_input("Form (optional)=")]
        ku3(h3)
      elif(character == '3'):
        h2 = []
        h2[0:0] = [raw_input("Part 1=")]
        h2[1:1] = [raw_input("Part 2=")]
        h2[2:2] = [raw_input("Form (optional)=")]
        ku2(h2)
      elif(character == '4'):
         l = []
         l[1:1] = [raw_input("First line=")]
         l[2:2] = [raw_input("Second line=")]
         l[3:3] = [raw_input("Third line=")]
         l[4:4] = [raw_input("Fourth line=")]
         l[5:5] = [raw_input("Fifth line=")]
         lim(l)
      elif(character == '5'):
         l = []
         l[1:1] = [raw_input("First line=")]
         l[2:2] = [raw_input("Second line=")]
         l[3:3] = [raw_input("Third line=")]
         l[4:4] = [raw_input("Fourth line=")]
         l[5:5] = [raw_input("Fifth line=")]
         cinq(l)
      elif(character == '6'):
       insfilename = raw_input("File name=")
       try:
        insfile = open(insfilename,'r')
        grabfile(insfile)
        insfile.close()
       except IOError:
        sys.stderr.write("Cannot open " + insfilename + ", continue.\n")
      elif(character == '7'):
        sys.stdout.write("Begin inputting text, end with a line containing only a period.\n")
        plain = raw_input()
        while(plain != "."):
            plaintxt(plain)
            plain = raw_input()
      elif(character == '8'):
        tail()
        sys.stdout.write("Wrote to file " + filename)
      elif(character == 'x'):
        outfile.close()
        sys.exit(0)
      else:
        sys.stderr.write("Invalid input <" + character + ">, exiting.\n")
