from StaticPriorityPattern import StaticPriorityPattern


class Task:
    def __init__(self, id, period, priority):
        self.id = id
        self.period = period
        self.priority = priority

    def task_property_print(self):
        print("Priority:" + str(self.priority) + " Task id:" + str(self.id) + " Period:" + str(self.period))


static_priority_pattern = StaticPriorityPattern()
period_list = [10, 5, 20, 3]
counter = 1
task_List = []
for period in period_list:
    task = Task(counter, period, -1)
    counter += 1
    task_List.append(task)

priority_task_list = static_priority_pattern.schedule(task_List)

for task in priority_task_list:
    task.task_property_print()
