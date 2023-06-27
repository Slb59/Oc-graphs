class Task:
    def __init__(self, date, subject, category, description, estimate_time, real_time):
        self.date = date
        self.subject = subject
        self.category = category
        self.description = description
        self.estimate_time = estimate_time
        self.real_time = real_time

    def __str__(self):
        str = self.date + "- (" + self.subject + ")" + self.category + "\n"
        str += self.description + "\n"
        str += "Estimé : " + self.estimate_time + " --- Réalisé : " + self.real_time
        return str
