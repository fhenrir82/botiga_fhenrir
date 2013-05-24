<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
	<head>
	  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
	  <link rel="stylesheet" type="text/css" href="${request.static_url('botiga:static/aleix.css')}"/>
	</head>
	<body> 
	<div id="header">
					
		<div><center><h1>${pagina}</h1></center></div>
	</div>
				
	<div id="wrapper">	   
		<div id="mig">	
			<div id="leftcolumn">
				<a href="${request.route_url('benvinguda')}">Pagina principal</a></br>
				<a href="${request.route_url('productes')}">Realitzar comanda</a></br>
				<a href="${request.route_url('informacio')}">Informacio</a></br>
			</div>
			<div id="rightcolumn">${next.body()}</div>
		</div>		
	</div>	
	<div id="footer">
	% if logged_in:
		<p id="usuari-box">Benvingut: <b>${logged_in}</b>  [<a href="${request.route_url('logout')}">Sortir</a>]</p>
	% endif
	</div>
	</body>
</html>
