import emotions
import file_monitor

def main():
  repo = emotions.Repository()
  parser = emotions.Parser()

  def processFileChange(text):
    emotions_found = parseEmotions(text)
    repo.save(emotions_found)

  def parseEmotions(text):
    phrases = parser.parsePhrases(text)
    return map(lambda phrase: parser.detectEmotion(phrase), phrases)

  POLLING_INTERVAL_SECONDS = 0.05

  watchFile = file_monitor.FileMonitor('test-file.log', POLLING_INTERVAL_SECONDS)
  watchFile.onChange(processFileChange)
  watchFile.start()

main()
