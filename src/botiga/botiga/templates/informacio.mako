<%inherit file="maqueta.mako" />
	<tr style="background-color:lightblue;">
	
		<td> Codi</td><td> Producte</td><td> Stock</td><td> Quantitat</td><td> Preu €/Kg</td><td>Total</td>
	</tr>
	% for id in llistat:
	<tr>
	
		
		<td name='id'> ${llistat[id]["idprod"]}</td>
		<td name='nom'> ${llistat[id]["idprod"]}</td>
		<td name='unitats'> ${llistat[id]["idprod"]}</td>
		<td name='preu'> ${llistat[id]["idprod"]}</td>
		<td name='quantitat'> ${llistat[id]["idprod"]}</td>
		<td name='total'> ${llistat[id]["idprod"]}</td>
	</tr>
		
	% endfor

	<tr >
	</table>
