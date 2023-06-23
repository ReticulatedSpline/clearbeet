import os
from beets.plugins import BeetsPlugin

class ClearBeet(BeetsPlugin):
  def __init__(self):
    super(ClearBeet, self).__init__()
    self.register_listener('pluginload', self.loaded)
    self.register_listener('import_task_start', self.import_task_start)

  def loaded(self):
    self._log.info('Clearbeet plugin loaded.')

  def import_task_start(self):
    os.system('cls' if os.name=='nt' else 'clear')