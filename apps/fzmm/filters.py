import django_filters

from .models import Idc, IdcArea, IdcEnergy, Danger, Job


class IdcFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Idc
        exclude = ('description', 'creator', 'modifier')


class IdcEnergyFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = IdcEnergy
        exclude = ('description', 'creator', 'modifier')


class IdcAreaFilter(django_filters.rest_framework.FilterSet):
    """
    项目管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = IdcArea
        exclude = ('description', 'creator', 'modifier')


class DangerFilter(django_filters.rest_framework.FilterSet):
    """
    隐患管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Danger
        exclude = ('description', 'creator', 'modifier')


class JobFilter(django_filters.rest_framework.FilterSet):
    """
    巡检任务管理 简单序过滤器
    """
    # 通过 lookup_expr 可进行模糊查询，其他配置可自行百度
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        exclude = ('description', 'creator', 'modifier')