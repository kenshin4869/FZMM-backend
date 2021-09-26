from django.conf import settings
from django.db.models import CharField, ForeignKey, CASCADE, SET_NULL, FloatField, IntegerField, BooleanField, DateTimeField

from apps.vadmin.op_drf.models import CoreModel


# 继承框架封装的 模型类 CoreModel
class Idc(CoreModel):
    name = CharField(max_length=8, verbose_name='机房名称', unique=True)
    address = CharField(max_length=32, verbose_name='机房具体地址')
    # 在普通一多一、一对多、多对多时，to='App名.模块名' 进行关联
    department = ForeignKey(to='permission.dept', on_delete=CASCADE, verbose_name="机房所属部门", related_name='idc_department', db_constraint=False)
    idctype = CharField(max_length=8, verbose_name='机房类型')
    # 在关联用户时，建议使用 to=settings.AUTH_USER_MODEL 进行关联
    mowner = ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='总房长', related_name='idc_mowner',
                        on_delete=SET_NULL, db_constraint=False)
    owner = ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='房长', related_name='idc_owner',
                            on_delete=SET_NULL, db_constraint=False)
    class Meta:
        verbose_name = '机房管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name} 机房"

# 继承框架封装的 模型类 CoreModel
class IdcArea(CoreModel):
    idc = ForeignKey(to='Idc', on_delete=CASCADE, verbose_name="机房", related_name='idcname_idcarea',db_constraint=False)
    area = FloatField(max_length=8, verbose_name='机房面积')
    totalRacks = IntegerField(verbose_name='总机架数')
    usedRacks = IntegerField(verbose_name='在用机架数')
    areaUsed = FloatField(max_length=8, verbose_name='空间效率')

    class Meta:
        verbose_name = '机房空间管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.idc} 机房空间"

# 继承框架封装的 模型类 CoreModel
class IdcEnergy(CoreModel):
    idc = ForeignKey(to='Idc', on_delete=CASCADE, verbose_name="机房", related_name='idcname_idcenergy',db_constraint=False)
    totalAirs = IntegerField(verbose_name='总空调数')
    usedAirs = IntegerField(verbose_name='在用空调数')
    totalPower = FloatField(max_length=8, verbose_name='总功率')
    airsPower = FloatField(max_length=8, verbose_name='空调功率')
    equipPower = FloatField(max_length=8, verbose_name='设备功率')
    idcpve = FloatField(max_length=8, verbose_name='能源效率')

    class Meta:
        verbose_name = '机房能源管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.idc} 机房能源"

# 继承框架封装的 模型类 CoreModel
class Danger(CoreModel):
    title = CharField(max_length=20, verbose_name='隐患标题')
    context = CharField(max_length=128, verbose_name='详细内容')
    # 在普通一多一、一对多、多对多时，to='App名.模块名' 进行关联
    idc = ForeignKey(to=Idc, on_delete=CASCADE, verbose_name="所属机房", related_name='danger_idc',db_constraint=False)
    completed = BooleanField(verbose_name='是否解决')
    completestep = CharField(max_length=128, verbose_name='解决步骤')
    completetime = DateTimeField(verbose_name='解决时间', blank=True, null=True)


    class Meta:
        verbose_name = '隐患管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title} 隐患"

# 继承框架封装的 模型类 CoreModel
class Job(CoreModel):
    title = CharField(max_length=20, verbose_name='任务标题', unique=True, default='巡检任务')
    user = ForeignKey(to=settings.AUTH_USER_MODEL, null=True, verbose_name='房长', related_name='job_user',
                        on_delete=SET_NULL, db_constraint=False)
    idctype = CharField(max_length=8, verbose_name='机房类型', blank=True, null=True)
    starttime = DateTimeField (verbose_name='起始时间',  blank=True, null=True)
    endtime = DateTimeField(verbose_name='截止时间',  blank=True, null=True)
    complete = BooleanField(verbose_name='是否完成')
    completetime = DateTimeField(verbose_name='完成时间',  blank=True, null=True)
    completeContext = CharField(max_length=128, verbose_name='完成情况', blank=True, null=True)
    completeIdc = ForeignKey(to=Idc, on_delete=CASCADE, verbose_name="所属机房", related_name='job_idc', db_constraint=False)



    class Meta:
        verbose_name = '巡检任务管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title} 巡检任务"