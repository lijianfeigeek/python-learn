import time
import os
class Clock(object):
  def __init__(self,hour=0,minute=0,second=0):
    self._hour = hour
    self._minute = minute
    self._second = second

  def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
  def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)

if __name__ == '__main__':
	# clock = Clock(hour=10, minute=5, second=58)
	clock = Clock()
	while True:
		os.system('clear')
		print(clock.show())
		time.sleep(1)
		clock.run()
