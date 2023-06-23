import os
from beets.plugins import BeetsPlugin

class SomePlugin(BeetsPlugin):
  def __init__(self):
    super(SomePlugin, self).__init__()
    self.register_listener('pluginload', self.loaded)
    self.register_listener('album_imported', self.album_imported)

  def loaded(self):
    self._log.info('Clearbeet plugin loaded.')

  def album_imported(self):
    os.system('cls' if os.name=='nt' else 'clear')