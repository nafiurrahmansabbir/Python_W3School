class Time:
    def init(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def add_time(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours, minutes = divmod(total_minutes, 60)
        total_hours = self.hours + other.hours + extra_hours
        return Time(total_hours, minutes)

    def display_minute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minutes")

    def str(self):
        return f"{self.hours} hr and {self.minutes} min"

if __name__ == "main":
    time1 = Time(2, 50)
    time2 = Time(1, 20)
    
    result = time1.add_time(time2)
    print(f"Resultant Time: {result}")
    
    time3 = Time(1, 2)
    time3.display_minute()