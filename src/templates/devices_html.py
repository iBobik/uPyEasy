# Autogenerated file
def render(info,devices, plugins, controllers):
    yield """
    <table cellpadding='4' border='1' frame='box' rules='all'>
       <TH>
       <TH>ID
       <TH>Name
       <TH>Device
       <TH>Dx Pin
       <TH>Controller
       <TH>Cntr.ID
       <TH>Values
       <TH>Enabled
       <TH>
       """
    for device in devices:
        yield """
           """
        if device['id'] != 0:
            yield """ 
           <TR>
              <TD><a class=\"button link\" href=\"/device_setting?id="""
            yield str(device['id'])
            yield """\">Edit</a>
              <TD>"""
            yield str(device['id'])
            yield """
              <TD>"""
            yield str(device['name'])
            yield """
              <TD>"""
            for plugin in plugins:
                yield """
                       """
                if plugin['id'] == device['pluginid']:
                    yield """ """
                    yield str(plugin['name'])
                    yield """ """
                yield """
                  """
            yield """
              <TD>"""
            if device['dxpin'] != '':
                yield """ """
                yield str(device['dxpin'])
                yield """ 
                  """
            elif device['i2c'] > 0:
                yield """ I2C("""
                yield str(device['i2c'])
                yield """) 
                  """
            elif device['spi'] > 0:
                yield """ SPI("""
                yield str(device['spi'])
                yield """) 
                  """
            elif device['uart'] > 0:
                yield """ UART("""
                yield str(device['uart'])
                yield """) """
            yield """
              <TD>"""
            for controller in controllers:
                yield """
                       """
                if controller['id'] == device['controller']:
                    yield """ """
                    yield str(controller['protocol'])
                    yield """ """
                yield """
                  """
            yield """
              <TD>"""
            yield str(device['controllerid'])
            yield """
              <TD>"""
            yield str(device['values'])
            yield """
              <TD><span style=\"color:"""
            if device['enable'] == 'on':
                yield """Green"""
            else:
                yield """Red"""
            yield """\">"""
            if device['enable'] == 'on':
                yield """Yes"""
            else:
                yield """No"""
            yield """</span>
              <TD><a class=\"button link\" href=\"/device_setting?id="""
            yield str(device['id'])
            yield """&oper=del\">Del</a>
           """
        yield """
       """
    yield """
       <TR>
          <TD><a class=\"button link\" href=\"/device_setting?id=0\">Add</a>
          <TD colspan=\"9\">
    </table>
"""
