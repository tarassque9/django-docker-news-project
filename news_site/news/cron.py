from django_cron import CronJobBase, Schedule
from .services import _null_votes


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1440

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'news.my_cron_job'

    def do(self):
        _null_votes()
