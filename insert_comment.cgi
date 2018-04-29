#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, cgi

string = "i211s18_drdwhit" 		#change username to yours!!!
password = "my+sql=i211s18_drdwhit" 	#change username to yours!!!

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

form = cgi.FieldStorage()

name = form.getfirst('name', None)
email = form.getfirst('email', None)
comment = form.getfirst('message', None)

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
	<div class="container">"""

try:				#Always surround .execute with a try!
		SQL = """INSERT INTO i310 (name, email, message) 
		VALUES ('"""
		SQL += name
		SQL += "', '"
		SQL += email
		SQL += "', '"
		SQL += comment
		SQL += "');"
		cursor.execute(SQL)
		db_con.commit()
except Exception as e:	#Here we handle the error
		html += '<p>Something went wrong with the SQL!</p>'
else:				#This runs if there was no error
		html += "<h2> New Comment Added! </h2> <p> You may now go back to the homepage. </p> <br><br>" 

html += """
	<div class="clr"></div>
		<div style="margin-top:300px;"></div>
		<footer id="main-footer">
			<p> Copyright &copy; 2018 Proof By Example </p>
		</footer>
	</div>
</body>
</html>"""
				
print(html)


