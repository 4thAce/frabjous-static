#!/usr/bin/python
import cgi
import sys
#import cgitb; cgitb.enable()
import crypt

#sys.stderr = sys.stdout
#print "Content-Type: text/plain"    #
print "Content-Type: text/html"    # 
print                               # blank line, end of headers
print "<HTML><HEAD>"
print "<TITLE>CGI script output</TITLE>"
print '  <style type="text/css">'
print ' td {color: #330000; font-size: 80%}'
print '</style>'
print '  <link rel="SHORTCUT ICON" href="/frabjous/frabjous.ico">'
print "</HEAD><BODY>"
print "<H2>This creates html files in the corral</H1>"
#print r'<FORM METHOD="POST" ACTION="corral/writejabba.cgi">'
print r'<FORM METHOD="POST" ACTION="writejabba.cgi">'
print r'<STRONG>Title: </STRONG><INPUT TYPE="text" NAME="title" SIZE="48"><br />'
print r'<STRONG>Description: </STRONG><INPUT TYPE="text" NAME="description" SIZE="128"><br />'
print r'<STRONG>Keywords: </STRONG><INPUT TYPE="text" NAME="keywords" SIZE="128"><br />'
print r'<STRONG>Text: </STRONG>'
print r'<textarea rows="22" cols="80" name="jabba">'
print r'</textarea><br />'
#<INPUT TYPE="textarea" NAME="oneline" SIZE="48"><br />'
print r'<INPUT TYPE="submit" VALUE="Submit!"><br />'
print r'<STRONG>Passphrase: </STRONG><INPUT TYPE="text" NAME="pass" SIZE="48"><BR>'
print r'</FORM>'
print r'<div class="c2"><table summary="cut-n-paste"><tr><td>'
print r'<table summary="exemplars" border="2">'
print '<tr><td>&lt;div class="kufirst"&gt;</td><td>First line of haiku</td></tr>'
print '<tr><td>&lt;div class="kumid"&gt;</td><td>Middle line of haiku</td></tr>'
print '<tr><td>&lt;div class="kulast"&gt;</td><td>Last line of haiku (additional margin)</td></tr>'
print '<tr><td>&lt;table summary="short0" align="center"&gt;&lt;tr&gt;&lt;td&gt;<br>'
print '&lt;span class="zipel"&gt;</td><td>First half-line</td></tr>'
print '<tr><td>&lt;/span&gt;&lt;/td&gt;&lt;td width="10%"&gt;<br>' + "\n"
print '&lt;span class="zipel"&gt;&amp;nbsp;&lt;/span&gt;&lt;/td&gt;&lt;td&gt;&amp;nbsp;&lt;/td&gt;<br>'
print '&lt;td&gt;&lt;span class="zipel"&gt;</td><td>Between half-lines</td></tr>'
print '<tr><td>&lt;/span&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;</td><td>After second half-line</td></tr>'
print '<tr><td>&lt;div class="storybody"&gt;</td><td>Paragraph of text</td></tr>'
print '<tr><td>&lt;div class="brickfirst"&gt;</td><td>First line of a brick</td></tr>'
print '<tr><td>&lt;div class="brickmid"&gt;</td><td>Second or third line of a brick</td></tr>'
print '<tr><td>&lt;div class="bricklast"&gt;</td><td>Fourth line of a brick</td></tr>'
print '<tr><td>&lt;div class="limtop"&gt;</td><td>First or second line of a limerick</td></tr>'
print '<tr><td>&lt;div class="lim34"&gt;</td><td>Third or fourth line of a limerick</td></tr>'
print '<tr><td>&lt;div class="limbot"&gt;</td><td>Last line of a limerick (additional margin)</td></tr>'
print '<tr><td>&lt;div class="note"&gt;</td><td>Additional note</td></tr>'
print '<tr><td>&lt;div class="form"&gt;</td><td>Description of a form</td></tr>'
print '<tr><td>&lt;div class="timestamp"&gt;</td><td>Time stamp line (Originally published:)</td></tr>'
print '<tr><td>&lt;div class="revision"&gt;</td><td>Revision: line</td></tr>'
print '<tr><td>&lt;div class="kubody"&gt;</td><td>Line of haiku</td></tr>'
print '<tr><td>&lt;h2&gt;</td><td>Heading</td></tr>'
print '<tr><td>&lt;h3&gt;</td><td>Heading</td></tr>'
print '<tr><td>&lt;div class="keyword"&gt;</td><td>Small line of keywords</td></tr>'
print '<tr><td>&lt;div class="c1"&gt;</td><td>Big, dark, centered</td></tr>'
print '<tr><td>&lt;div class="c2"&gt;</td><td>Small, very dark</td></tr>'
print '<tr><td>&lt;div class="c3"&gt;</td><td>Dark green, centered</td></tr>'
#<td><span class="zipel">
print '</table>'
print '</td><td><table summary="keywords" border="2">'
print '<tr><td>scifaiku</td></tr>'
print '<tr><td>space scifaiku</td></tr>'
print '<tr><td>social scifaiku</td></tr>'
print '<tr><td>technology scifaiku</td></tr>'
print '<tr><td>physics scifaiku</td></tr>'
print '<tr><td>biology scifaiku</td></tr>'
print '<tr><td>earth science scifaiku</td></tr>'
print '<tr><td>art scifaiku</td></tr>'
print '<tr><td>limerick</td></tr>'
print '<tr><td>scifaisenryu</td></tr>'
print '<tr><td>brick</td></tr>'
print '<tr><td>zip</td></tr>'
print '<tr><td>tanka</td></tr>'
print '<tr><td>review</td></tr>'
print '<tr><td>essay</td></tr>'
print '<tr><td>family</td></tr>'
print '<tr><td>cinquain</td></tr>'
print '<tr><td>googlewhack</td></tr>'
print '<tr><td>opinion</td></tr>'
print '<tr><td>tip</td></tr>'
print '<tr><td>link</td></tr>'
print '</table></table></div>'
print "</BODY></HTML>"

