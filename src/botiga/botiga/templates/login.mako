<%inherit file="maqueta.mako" />
  <div id="wrap">
    <div id="top-small">
      <div class="top-small align-center">
      </div>
    </div>
    <div id="middle">
      <div class="middle align-right">
        <div id="left" class="app-welcome align-left">
          <b>Login</b> | <a href="${request.route_url('benvinguda')}">Anar a casa</a><br/>
          % if message:
            ${message}
          % endif
        </div>
        <div id="right" class="app-welcome align-right"></div>
      </div>
    </div>
    <div id="bottom">
      <div class="bottom">
        <form action="${url}" method="post">
          <input type="hidden" name="came_from" value="${came_from}"/>
          <input type="text" name="login" value="${login}"/><br/>
          <input type="password" name="password" value="${password}"/><br/>
          <input type="submit" name="form.submitted" value="Log In"/>
        </form>
      </div>
    </div>
  </div>
  <div id="footer">
    <div class="footer">Copyleft aleix 2013.</div>
  </div>
