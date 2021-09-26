from rest_framework import serializers

from .models.fzmm import Idc, IdcArea, IdcEnergy, Danger, Job
from apps.vadmin.op_drf.serializers import CustomModelSerializer


# ================================================= #
# ************** 机房管理 序列化器  ************** #
# ================================================= #
class IdcSerializer(CustomModelSerializer):
    """
    机房管理 简单序列化器
    """

    class Meta:
        model = Idc
        fields = '__all__'


class IdcCreateUpdateSerializer(CustomModelSerializer):
    """
    机房管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Idc
        fields = '__all__'


class ExportIdcSerializer(CustomModelSerializer):
    """
    导出 机房管理 简单序列化器
    """
    mowner__username = serializers.SerializerMethodField(read_only=False)
    owner__username = serializers.SerializerMethodField(read_only=False)
    dept__deptName = serializers.SerializerMethodField(read_only=False)

    def get_mowner__username(self, obj):
        return "" if not hasattr(obj, 'majorOwner') else obj.person.username

    def get_owner__username(self, obj):
        return "" if not hasattr(obj, 'owner') else obj.person.username

    def get_dept__deptName(self, obj):
        return "" if not hasattr(obj, 'department') else obj.dept.deptName

    class Meta:
        model = Idc
        fields = ('id', 'name', 'address', 'idctype', 'area', 'rack', 'aircondition', 'mowner', 'mowner__username',
                  'owner', 'owner__username', 'department', 'dept__deptName', 'creator', 'modifier', 'description')


# ================================================= #
# ************** 机房空间管理 序列化器  ************** #
# ================================================= #
class IdcAreaSerializer(CustomModelSerializer):
    """
    机房空间管理 简单序列化器
    """

    class Meta:
        model = IdcArea
        fields = '__all__'


class IdcAreaCreateUpdateSerializer(CustomModelSerializer):
    """
    机房空间管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = IdcArea
        fields = '__all__'


class ExportIdcAreaSerializer(CustomModelSerializer):
    """
    导出 机房管理 简单序列化器
    """
    idc__name = serializers.SerializerMethodField(read_only=False)

    def get_idc__name(self, obj):
        return "" if not hasattr(obj, 'idc') else obj.Idc.name


    class Meta:
        model = IdcArea
        fields = ('id', 'idc', 'idc__name', 'area', 'totalRacks', 'usedRacks', 'areaUsed', 'creator', 'modifier', 'description')


# ================================================= #
# ************** 机房能源管理 序列化器  ************** #
# ================================================= #
class IdcEnergySerializer(CustomModelSerializer):
    """
    机房空间管理 简单序列化器
    """

    class Meta:
        model = IdcEnergy
        fields = '__all__'


class IdcEnergyCreateUpdateSerializer(CustomModelSerializer):
    """
    机房空间管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = IdcEnergy
        fields = '__all__'


class ExportIdcEnergySerializer(CustomModelSerializer):
    """
    导出 机房管理 简单序列化器
    """
    idc__name = serializers.SerializerMethodField(read_only=False)

    def get_idc__name(self, obj):
        return "" if not hasattr(obj, 'idc') else obj.Idc.name


    class Meta:
        model = IdcEnergy
        fields = ('id', 'idc', 'idc__name', 'totalAirs', 'usedAirs', 'totalPower', 'airsPower', 'equipPower', 'idcpve', 'creator', 'modifier', 'description')

# ================================================= #
# ************** 隐患管理 序列化器  ************** #
# ================================================= #
class DangerSerializer(CustomModelSerializer):
    """
    隐患管理 简单序列化器
    """

    class Meta:
        model = Danger
        fields = '__all__'


class DangerCreateUpdateSerializer(CustomModelSerializer):
    """
    隐患管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Danger
        fields = '__all__'


class ExportDangerSerializer(CustomModelSerializer):
    """
    导出 隐患管理 简单序列化器
    """
    idc__name = serializers.SerializerMethodField(read_only=False)

    def get_idc__name(self, obj):
        return "" if not hasattr(obj, 'name') else obj.idc.name


    class Meta:
        model = Danger
        fields = ('id', 'title', 'context', 'idc', 'idc__name', 'complete', 'step', 'creator', 'create_datetime', 'modifier', 'update_datetime','description')

# ================================================= #
# ************** 巡检任务管理 序列化器  ************** #
# ================================================= #
class JobSerializer(CustomModelSerializer):
    """
    巡检任务管理 简单序列化器
    """

    class Meta:
        model = Job
        fields = '__all__'


class JobCreateUpdateSerializer(CustomModelSerializer):
    """
    巡检任务管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Job
        fields = '__all__'


class ExportJobSerializer(CustomModelSerializer):
    """
    导出 巡检任务管理 简单序列化器
    """
    job__user = serializers.SerializerMethodField(read_only=False)
    idc__name = serializers.SerializerMethodField(read_only=False)

    def get_job__user(self, obj):
        return "" if not hasattr(obj, 'name') else obj.person.username

    def get_idc__name(self, obj):
        return "" if not hasattr(obj, 'name') else obj.idc.name


    class Meta:
        model = Danger
        fields = ('id', 'title', 'user', 'job__user', 'idctype', 'starttime', 'endtime', 'complete', 'completetime', 'idc', 'idc__name', 'creator', 'modifier', 'description')