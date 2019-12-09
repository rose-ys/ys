from django.db import models



class Application(models.Model):
    name = models.CharField('姓名', max_length=32)
    cause = models.CharField('请假原因', max_length=64)
    start_time = models.DateField('请假开始时间', help_text="格式yyyy-mm-dd")
    end_time = models.DateField('请假结束时间', help_text="格式yyyy-mm-dd")
    case = models.CharField('是否通过', choices=((True, '通过'), (False, '未通过')), default='not', max_length=16)
