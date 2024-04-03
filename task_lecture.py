from datetime import datetime, timedelta
import re

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start = datetime.strptime(start_time, '%H:%M')
        hour, minute = map(int, re.findall('\d+', duration))
        self.duration = timedelta(hours = hour, minutes = minute)
        self.end = self.start + self.duration
        
class Conference:
    def __init__(self):
        self.all = []
        
    @staticmethod
    def check(lect):
        def wrapper(cur):
            if cur.start<=lect.start<cur.end or cur.start<lect.end<=cur.end or (lect.start<=cur.start and lect.end>=cur.end):
                return True
            return False
        return wrapper
        
    def add(self, lect):
        foo = self.check(lect)
        if any(filter(lambda cur: foo(cur), self.all)):
            raise ValueError('Провести выступление в это время невозможно')
        self.all.append(lect)
        self.all.sort(key=lambda lect: lect.start)
        
    def total(self):
        sum_time = sum([lect.duration.seconds for lect in self.all])
        return f'{sum_time // 3600:>02}:{sum_time % 3600 // 60:>02}'
        
    def longest_lecture(self):
        max_time = max([lect.duration.seconds for lect in self.all])
        return f'{max_time // 3600:>02}:{max_time % 3600 // 60:>02}'
        
    def longest_break(self):
        longest_break = max([self.all[n + 1].start - self.all[n].end for n in range(len(self.all) - 1)]).seconds
        return f'{longest_break // 3600:>02}:{longest_break % 3600 // 60:>02}'