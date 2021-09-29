from .models import Job
from apps.vadmin.utils.decorators import BaseCeleryApp
import  datetime


@BaseCeleryApp(name='apps.fzmm.tasks.create_job')
def create_job():
    """
    自动创建任务
    :return:
    """
    cre_job=Job()
    cre_job.title = "自动巡检任务" + str(datetime.datetime.now())