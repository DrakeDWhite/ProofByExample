#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, cgi

string = "i211s18_drdwhit" 		#change username to yours!!!
password = "my+sql=i211s18_drdwhit" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

html = """
<!DOCTYPE html>
<html>
<head>
	<title>Proof By Example</title>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML" async>
	</script>
</head>
<body>
	<header id= "main-header">
		<div class ="container">
			<h1> Proof By Example </h1>
			<ul>
				<li> <a class="link-style" href="home.html">Home</a></li>
				<li> <a class="link-style" href="modules.html">Modules</a></li>
				<li> <a class="link-style" href="about.html">About</a></li>
				<li> <a class="link-style" href="notes.html">Notes</a></li>
				<li> <a class="link-style" href="contact.html">Contact</a></li>
			</ul>
		</div>
	</header>
	<div class="container">
		<table border='1' width='100%'>
		<tr><th>Name</th><th>E-mail</th><th>Message</th></tr>"""


try:				#Always surround .execute with a try!
	SQL = "SELECT * FROM i310;"
	cursor.execute(SQL)
	results = cursor.fetchall()
except Exception as e:	#Here we handle the error
	html += '<p>Something went wrong with the SQL!</p>'
else:				#This runs if there was no error
	html += "Here are all of the comments given so far: <br> <br>"
	for each in results:
		html += "<tr><td align='center'>"
		html += each[1]
		html += "</td><td align='center'>"
		html += each[2]
		html += "</td><td align='center'>"
		html += each[3]
		html += "</td></tr>"

	html += """
	</div>
	</table>
    </body>
	</html>"""
				
print(html)