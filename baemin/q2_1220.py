log1 = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
log2 = ["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]

def solution(log):
    total_study_time = 0
    formatting_study_time = ""

    for i in range(0, len(log), 2):
        start_hour, start_min = map(int, log[i].split(":"))
        end_hour, end_min = map(int, log[i+1].split(":"))
        study_time = (end_hour*60 + end_min) - (start_hour*60 + start_min)

        if study_time < 5:
            study_time = 0
        elif study_time > 105:
            study_time = 105

        total_study_time += study_time

    study_hour = (total_study_time // 60)
    study_min = (total_study_time % 60)
    formatting_study_time = ("0"+str(study_hour)) if study_hour < 10 else str(study_hour)
    formatting_study_time += ":"
    formatting_study_time += ("0"+str(study_min)) if study_min < 10 else str(study_min)

    return formatting_study_time

print(solution(log1))