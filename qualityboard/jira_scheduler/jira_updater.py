from apscheduler.schedulers.background import BackgroundScheduler
from qualityboard import views

def start():
    scheduler = BackgroundScheduler()
    #jira = views()
    scheduler.add_job(views.save_jira_data,"interval",minutes=60,id="jira_001",replace_existing=True)
    scheduler.start()