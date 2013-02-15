<html>
   <body>
      <h1>Productes</h1>
      <table>
          <tr style="background-color:lightblue;">

              <td> ID</td><td> Producte</td><td> Unitats</td><td> Preu</td>
          </tr>
          % for id in products:
          <tr>
              <td>${id}</td><td> ${products[id]["producte"]}</td><td> ${products[id]["unitats"]}</td><td> ${products[id]["preu"]}</td>
          </tr>
          % endfor
      </table>
		<a href="${request.route_url('benvinguts')}">Enrere</a>
   </body>
</html>
