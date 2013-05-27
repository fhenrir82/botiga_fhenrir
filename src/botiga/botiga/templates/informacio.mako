<%inherit file="maqueta.mako" />
	<tr style="background-color:lightblue;">
	
		<td> Codi</td><td> Producte</td><td> Stock</td><td> Quantitat</td><td> Preu €/Kg</td><td>Total</td>
	</tr>
	% for i in llistat:
	<tr>
	
		
		<td name='id'> ${i}</td></br>
		<td name='nom'> ${llistat}</td>
		<td name='unitats'> ${llistat[i]}</td>
		<td name='preu'> ${llistat[i]}</td>
		<td name='quantitat'> ${llistat[i]}</td>
		<td name='total'> ${llistat[i]}</td>
	</tr>
		
	% endfor

	<tr >
	</table>
