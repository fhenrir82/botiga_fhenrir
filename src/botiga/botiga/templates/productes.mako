<html>
	<head>
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
	</head>
   <body>
      <h1>Productes</h1>
      <table>
          <tr style="background-color:lightblue;">

              <td> ID</td><td> Producte</td><td> Unitats</td><td> Preu €/Kg</td><td> Afegeix</td><td> Treure</td><td> Quantitat</td>
          </tr>
          % for id in products:
          <tr>
              <td>${id}</td>
              <td> ${products[id]["producte"]}</td>
              <td> ${products[id]["unitats"]}</td>
              <td> ${products[id]["preu"]}</td>
              <td><input type='button' value='+' name='sumar' id='sumar' onClick="suma('${products[id]['producte']}');"/></td>
              <td><input type='button' value='-' name='restar' id='restar' onClick="resta('${products[id]['producte']}');"/></td>
              <td><input type='text' value='0' name="${products[id]['producte']}" id="${products[id]['producte']}" size='2' disabled/></td>
          </tr>
          % endfor

         <br/><br/>
         <tr >
         <td colspan="4"><input type="submit" value="Accepta" name="acabar" id="acabar"/></td></td></tr>
         </form>
      </table>
      </br>
      </br>
       <div id='comanda' name='comanda'>La seva comanda</div>
      </br>
		<a href="${request.route_url('benvinguda')}">Enrere</a>
   </body>
</html>
