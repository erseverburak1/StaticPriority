
class StaticPriorityPattern:

    def schedule(self, task_list):
        task_priority_list = []
        period_list = []
        tmp_task_list = []

        for task in task_list:
            period_list.append(task.period)
            tmp_task_list.append(task)

        period_list.sort()
        for period in period_list:
            for task in tmp_task_list:
                if period == task.period:
                    task_priority_list.append(task)
                    tmp_task_list.remove(task)
                    break

        counter = 1
        for task in task_priority_list:
            task.priority = counter
            counter += 1

        print("Tasks scheduled")
        return task_priority_list
