#!/usr/bin/python
import cgi,sys
import time
import re
import crypt

modelfile = open("/home/rich/public_html/blog/model.html", 'r')
index = 0
model = ['','','','']
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

#sys.stderr = sys.stdout
#mydict = cgi.parse()
form = cgi.FieldStorage()
form_ok = 0
htmldir = r"/home/rich/public_html/blog/" 
#fn = time.strftime("%Y-%m-%d-%H.%M.%S") + ".html"
fn = ('%X.html' %time.time())

def teeprint(line):
   sys.stdout.write(line)
   outfile.write(line)

print "Content-Type: text/html"
#print "Content-Type: text/plain"
print                               # blank line, end of headers
#print cgi.print_form(form)
#print mydict
titletag0 = r'  <TITLE>'
titletag1 = "</TITLE>\n"
desc0='''   <meta name="description" content="'''
desc1='''" />''' + "\n"
key0='''    <meta name="keywords" content="'''
key1='''" />''' + "\n"
titletag0 = r'  <TITLE>'
titletag1 = "</TITLE>\n"
title0 = r'<hr><h2><!-- TITLESTART -->'
title1 = r'<!-- TITLEEND --></h2>' + "\n"
endcontline = "<!-- ENDCONTENT -->\n"
time0 = r'<div class="timestamp">Originally published: '
time1 = r'</div>' + "\n"
encrypt = crypt.crypt(form["pass"].value,'z0')
if encrypt != 'z06PFyHhaZ6KU':
    print(model[0] + titletag0 + form["title"].value + titletag1 + model[1])
    print('<p><STRONG>Access denied</STRONG></p>')
    print('</div></div></body></html>')
    sys.exit(-1)
outfile = open(htmldir + fn,'w')
teeprint(model[0] + titletag0 + form["title"].value + titletag1 + model[1])
teeprint(desc0 + form["description"].value + desc1)
teeprint(key0 + form["keywords"].value + key1)
teeprint(model[2])
encrypt = crypt.crypt(form["pass"].value,'z0')
teeprint(title0 + form["title"].value + title1)
teeprint(form["jabba"].value + "\n")
teeprint(endcontline)
teeprint(time0 + time.strftime("%d-%m-%Y %H:%M:%S") + time1)
teeprint(model[3])
print('<hr>')
print r'New file <a href="blog/' + fn + r'">' + fn + r'</a>'
print(r'<p>Go <a href="writetext.cgi">back</a></p>')
outfile.close()
