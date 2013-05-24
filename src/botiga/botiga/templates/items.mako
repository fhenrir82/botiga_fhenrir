<%inherit file="maqueta.mako" />

	<h1>Nº: <b>${cmd[0][0]}</b></h1>
	</br></br>
	
<table border="1">
	<tr style="background-color:lightblue;">

		<td> Codi</td><td> Producte</td><td> Stock</td><td> Quantitat</td><td> Preu €/Kg</td><td>Total</td>
	</tr>
	% for id in cmd:
	<tr>
	
		
		<td name='id'> ${id[1]}</td>
		<td name='nom'> ${id[2]}</td>
		<td name='unitats'> ${id[3]}</td>
		<td name='preu'> ${id[4]}</td>
		<td name='quantitat'> ${id[5]}</td>
		<td name='total'> ${id[6]}</td>
	</tr>
		
	% endfor

	<tr >
	</table>

