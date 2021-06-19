from threading import Timer
import logging

class FileMonitor:

  def __init__(self, filename, interval):
    self._pollingInterval = interval
    self._text = ''
    self._filename = filename
    self._observers = []
    self._counter = 0
    self._init = False

  def onChange(self, observer):
    self._observers.append(observer)

  def start(self):
    t = Timer(self._pollingInterval, self._readFile, (self._filename, self._loopAndNotify))
    t.start()

  def _loopAndNotify(self, text):
    self.start()

    notifyObservers = False
    if (self._init and text != self._text):
      notifyObservers = True

    self._text = text
    self._counter += 1
    self._init = True

    if (notifyObservers):
      for observer in self._observers:
        try:
          observer(text)
        except Exception as ex:
          log(ex)



  def _readFile(self, text, callback):
    handler = open(self._filename, 'r')
    file = handler.read()
    handler.close()
    callback(file)
