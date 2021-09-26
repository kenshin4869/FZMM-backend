from .filters import IdcFilter, IdcAreaFilter, IdcEnergyFilter, DangerFilter, JobFilter
from .models import Idc, IdcArea, IdcEnergy, Danger, Job
from .serializers import IdcSerializer, IdcCreateUpdateSerializer, ExportIdcSerializer, \
    IdcAreaSerializer, IdcAreaCreateUpdateSerializer, ExportIdcAreaSerializer, \
    IdcEnergySerializer, IdcEnergyCreateUpdateSerializer, ExportIdcEnergySerializer, \
    DangerSerializer, DangerCreateUpdateSerializer, ExportDangerSerializer, \
    JobSerializer, JobCreateUpdateSerializer, ExportJobSerializer
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.permission.permissions import CommonPermission


class IdcModelViewSet(CustomModelViewSet):
    """
    机房管理 的CRUD视图
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer  # 序列化器
    create_serializer_class = IdcCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = IdcCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = IdcFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('name',)  # 搜索
    ordering = ['create_datetime']  # 默认排序
    # 导出
    export_field_data = ['机房序号', '机房名称', '机房地址', '机房类型', '机房面积', '机架数量', '空调数量',
                         '总房长', '房长', '项目所属部门', '创建者', '修改者', '备注']  # 导出
    export_serializer_class = ExportIdcSerializer  # 导出序列化器
    # 导入
    import_field_data = {'name': '机房名称', 'address': '机房具体地址','idctype': '机房类型', 'mowner': '总房长ID',
                         'owner': '房长ID', 'department': '部门ID', 'area': '机房面积', 'rack': '机架数量', 'aircondition': '空调数量'}
    import_serializer_class = ExportIdcSerializer

class IdcAreaModelViewSet(CustomModelViewSet):
    """
    机房空间管理 的CRUD视图
    """
    queryset = IdcArea.objects.all()
    serializer_class = IdcAreaSerializer  # 序列化器
    create_serializer_class = IdcAreaCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = IdcAreaCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = IdcAreaFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('name',)  # 搜索
    ordering = ['create_datetime']  # 默认排序
    # 导出
    export_field_data = ['序号', '机房名称', '机房面积', '总机架数', '已用机架数', '空间利用率', '创建者', '修改者', '备注']  # 导出
    export_serializer_class = ExportIdcAreaSerializer  # 导出序列化器
    # 导入
    import_field_data = {'idc': '机房名称', 'area': '机房面积', 'totalRacks': '总机架数', 'usedRacks': '已用机架数',
                         'areaUsed': '空间利用率'}
    import_serializer_class = ExportIdcAreaSerializer

class IdcEnergyModelViewSet(CustomModelViewSet):
    """
    机房空间管理 的CRUD视图
    """
    queryset = IdcEnergy.objects.all()
    serializer_class = IdcEnergySerializer  # 序列化器
    create_serializer_class = IdcEnergyCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = IdcEnergyCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = IdcEnergyFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('name',)  # 搜索
    ordering = ['create_datetime']  # 默认排序
    # 导出
    export_field_data = ['序号', '机房名称', '总空调数', '在用空调数', '总功率', '空调功率', '设备功率', '机房能效利用率', '创建者', '修改者', '备注']  # 导出
    export_serializer_class = ExportIdcAreaSerializer  # 导出序列化器
    # 导入
    import_field_data = {'idc': '机房名称', 'totalAirs': '总空调数', 'usedAirs': '在用空调数', 'totalPower': '总功率',
                         'airsPower': '空调功率', 'equipPower': '设备功率', 'idcpve': '机房能效利用率'}
    import_serializer_class = ExportIdcAreaSerializer

class DangerModelViewSet(CustomModelViewSet):
    """
    隐患管理 的CRUD视图
    """
    queryset = Danger.objects.all()
    serializer_class = DangerSerializer  # 序列化器
    create_serializer_class = DangerCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = DangerCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = DangerFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('title',)  # 搜索
    ordering = ['create_datetime']  # 默认排序
    # 导出
    export_field_data = ['隐患序号', '隐患标题', '详细内容', '所属机房', '是否解决', '解决步骤', '创建者', '创建时间', '修改者', '修改时间', '备注']  # 导出
    export_serializer_class = ExportDangerSerializer  # 导出序列化器
    # 导入
    import_field_data = {'title': '隐患标题', 'context': '详细内容','idc': '所属机房', 'complete': '是否解决', 'step': '解决步骤'}
    import_serializer_class = ExportDangerSerializer

class JobModelViewSet(CustomModelViewSet):
    """
    隐患管理 的CRUD视图
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer  # 序列化器
    create_serializer_class = JobCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = JobCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = JobFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('user',)  # 搜索
    ordering = ['create_datetime']  # 默认排序
    # 导出
    export_field_data = ['任务标题', '房长', '机房类型', '起始时间', '截止时间', '是否完成', '完成时间', '所属机房', '创建者', '创建时间', '修改者', '修改时间', '备注']  # 导出
    export_serializer_class = ExportJobSerializer  # 导出序列化器
    # 导入
    import_field_data = {'title': '任务标题', 'user': '房长', 'idctype': '机房类型', 'starttime': '起始时间', 'endtime': '截止时间', 'complete': '是否完成', 'completetime': '完成时间', 'idc': '所属机房'}
    import_serializer_class = ExportJobSerializer