# Autogenerated file
def render(info):
    yield """
<form name = 'frmselect' method=\"post\">
    <table cellpadding='4' border='1' frame='box' rules='all'>
       """
    if info['message'] != '':
        yield """ 
       <TR>
            <TD colspan=\"2\" class=\"off\">"""
        yield str(info['message'])
        yield """
       """
    yield """
       <TR>
            <TD>Please enter administrator password:
            <TD><input type='password' name='password' maxlength='30' value=''>
       <TR>
          <TD><a class=\"button link\" href=\"scripts\">Close</a>
          <TD><input class=\"button link\" type='submit' value='Submit'>
   </table>
</form>"""