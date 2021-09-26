from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.fzmm.views import IdcModelViewSet, IdcAreaModelViewSet, \
    IdcEnergyModelViewSet, DangerModelViewSet, JobModelViewSet

router = DefaultRouter()
router.register(r'idc', IdcModelViewSet)
router.register(r'idcarea', IdcAreaModelViewSet)
router.register(r'idcenergy', IdcEnergyModelViewSet)
router.register(r'danger', DangerModelViewSet)
router.register(r'job', JobModelViewSet)

urlpatterns = [
    # 导出项目
    re_path('fzmm/idc/export/', IdcModelViewSet.as_view({'get': 'export', })),
    re_path('fzmm/idcarea/export/', IdcAreaModelViewSet.as_view({'get': 'export', })),
    re_path('fzmm/idcenergy/export/', IdcEnergyModelViewSet.as_view({'get': 'export', })),
    re_path('fzmm/danger/export/', DangerModelViewSet.as_view({'get': 'export', })),
    re_path('fzmm/job/export/', JobModelViewSet.as_view({'get': 'export', })),
    # 项目导入模板下载及导入
    re_path('fzmm/idc/importTemplate/',IdcModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
    re_path('fzmm/idcarea/importTemplate/',IdcAreaModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
    re_path('fzmm/idcenergy/importTemplate/',IdcEnergyModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
    re_path('fzmm/danger/importTemplate/',DangerModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
    re_path('fzmm/job/importTemplate/',JobModelViewSet.as_view({'get': 'importTemplate', 'post': 'importTemplate'})),
]

urlpatterns += router.urls