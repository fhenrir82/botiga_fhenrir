<%inherit file="maqueta.mako" />
		<script language="Javascript">
			function suma(objecte){
				var valor=document.getElementById(objecte).value;
				valor++;
				document.getElementById(objecte).value=valor; 
				
			}
			function resta(objecte){
				var valor=document.getElementById(objecte).value;
				valor--;
				document.getElementById(objecte).value=valor; 
				
			}
        </script>
      <table>
		<form id="comanda" method="POST" action="${request.route_url('comanda')}">
          <tr style="background-color:lightblue;">

              <td> ID</td><td> Producte</td><td> Unitats</td><td> Preu €/Kg</td><td> Afegeix</td><td> Treure</td><td> Quantitat</td>
          </tr>
          % for id in products:
          <tr>
              <td name='idprod' id='idprod'>${id}</td>
              <td name='nom'> ${products[id]["producte"]}</td>
              <td name='unitats'> ${products[id]["unitats"]}</td>
              <td name='preu'> ${products[id]["preu"]}</td>
              <td><input type='button' value='+' name='sumar' id='sumar' onClick="suma('${id}');"/></td>
              <td><input type='button' value='-' name='restar' id='restar' onClick="resta('${id}');"/></td>
              <td><input type='text' value='0' name="${id}" id="${id}" size='2'></td>
          </tr>
          % endfor

         <br/><br/>
         <tr >
         <td colspan="4"><input type="submit" value="Accepta" name="acceptar" id="acceptar" /></td></td></tr>
         </form>
      </table>
      </br>
      </br>
      </br>
<a href="${request.route_url('benvinguda')}">Enrere</a>
