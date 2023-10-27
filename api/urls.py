# urls.py
from django.urls import path
from . import views
from .views import AssetMstListCreateView, AssetMstDetailView,DepartmentMasterListCreateView,DepartmentMasterDetailView,DepreciationAssetDtlListCreateView,DepreciationCalcHdrListCreateView,DepreciationCalcHdrDetailView,DepreciationAssetDtlDetailView,EmployeeMasterListCreateView,EmployeeMasterDetailView

urlpatterns = [
    path('master/equipment/v1/', views.EquipmentMstListView.as_view(), name='equipment-list'),
    path('master/equipment/v1/<int:pk>/', views.EquipmentMstDetailView.as_view(), name='equipment-detail'),
    path('assets/', AssetMstListCreateView.as_view(), name='asset-list-create'),
    path('assets/<int:pk>/', AssetMstDetailView.as_view(), name='asset-detail'),
    path('DepartmentMaster/', DepartmentMasterListCreateView.as_view(), name='asset-list-create'),
    path('DepartmentMaster/<int:pk>/', DepartmentMasterDetailView.as_view(), name='asset-detail'),
    path('depreciation_asset/', DepreciationAssetDtlListCreateView.as_view(), name='depreciation-asset-list-create'),
    path('depreciation_asset/<int:pk>/', DepreciationAssetDtlDetailView.as_view(), name='depreciation-asset-detail'),
    path('depreciation_calc_hdr/', DepreciationCalcHdrListCreateView.as_view(), name='depreciation-calc-hdr-list-create'),
    path('depreciation_calc_hdr/<int:pk>/', DepreciationCalcHdrDetailView.as_view(), name='depreciation-calc-hdr-detail'),
    path('employees/', EmployeeMasterListCreateView.as_view(), name='employee-list-create'),
    path('employees/<str:pk>/', EmployeeMasterDetailView.as_view(), name='employee-detail'),
    path('grn_hdr/', views.GrnHdrList.as_view(), name='grn_hdr-list'),
    path('grn_hdr/<int:pk>/', views.GrnHdrDetail.as_view(), name='grn_hdr-detail'),
    path('grn_items/', views.GrnItemsList.as_view(), name='grn_items-list'),
    path('grn_items/<int:pk>/', views.GrnItemsDetail.as_view(), name='grn_items-detail'),
    path('issue_hdr/', views.IssueHdrList.as_view(), name='issue_hdr-list'),
    path('issue_hdr/<int:pk>/', views.IssueHdrDetail.as_view(), name='issue_hdr-detail'),
    path('issue_items/', views.IssueItemsList.as_view(), name='issue_items-list'),
    path('issue_items/<int:pk>/', views.IssueItemsDetail.as_view(), name='issue_items-detail'),
    path('itemmaster/', views.ItemMasterList.as_view(), name='itemmaster-list'),
    path('itemmaster/<str:pk>/', views.ItemMasterDetail.as_view(), name='itemmaster-detail'),

    # LocationMst URLs
    path('locationmst/', views.LocationMstList.as_view(), name='locationmst-list'),
    path('locationmst/<str:pk>/', views.LocationMstDetail.as_view(), name='locationmst-detail'),

    # MaintenanceIncidentInfo URLs
    path('maintenanceincidentinfo/', views.MaintenanceIncidentInfoList.as_view(), name='maintenanceincidentinfo-list'),
    path('maintenanceincidentinfo/<int:pk>/', views.MaintenanceIncidentInfoDetail.as_view(), name='maintenanceincidentinfo-detail'),

    # MaintenanceInspHdr URLs
    path('maintenanceinsphdr/', views.MaintenanceInspHdrList.as_view(), name='maintenanceinsphdr-list'),
    path('maintenanceinsphdr/<str:pk>/', views.MaintenanceInspHdrDetail.as_view(), name='maintenanceinsphdr-detail'),

    # MaintenanceJbActivityInfo URLs
    path('maintenancejbactivityinfo/', views.MaintenanceJbActivityInfoList.as_view(), name='maintenancejbactivityinfo-list'),
    path('maintenancejbactivityinfo/<int:pk>/', views.MaintenanceJbActivityInfoDetail.as_view(), name='maintenancejbactivityinfo-detail'),

    # MaintenanceJbConsumableInfo URLs
    path('maintenancejbconsumableinfo/', views.MaintenanceJbConsumableInfoList.as_view(), name='maintenancejbconsumableinfo-list'),
    path('maintenancejbconsumableinfo/<int:pk>/', views.MaintenanceJbConsumableInfoDetail.as_view(), name='maintenancejbconsumableinfo-detail'),

    # MaintenanceJbHdr URLs
    path('maintenancejbhdr/', views.MaintenanceJbHdrList.as_view(), name='maintenancejbhdr-list'),
    path('maintenancejbhdr/<str:pk>/', views.MaintenanceJbHdrDetail.as_view(), name='maintenancejbhdr-detail'),

    # MaintenanceJbIncidentInfo URLs
    path('maintenancejbincidentinfo/', views.MaintenanceJbIncidentInfoList.as_view(), name='maintenancejbincidentinfo-list'),
    path('maintenancejbincidentinfo/<int:pk>/', views.MaintenanceJbIncidentInfoDetail.as_view(), name='maintenancejbincidentinfo-detail'),
    
    path('maintenancerequestheader/', views.MaintenanceRequestHeaderList.as_view(), name='maintenancerequestheader-list'),
    path('maintenancerequestheader/<str:pk>/', views.MaintenanceRequestHeaderDetail.as_view(), name='maintenancerequestheader-detail'),

    # MaintenanceReportingHeader URLs
    path('maintenancereportingheader/', views.MaintenanceReportingHeaderList.as_view(), name='maintenancereportingheader-list'),
    path('maintenancereportingheader/<str:pk>/', views.MaintenanceReportingHeaderDetail.as_view(), name='maintenancereportingheader-detail'),

    # MaintenanceRPActivityInfo URLs
    path('maintenancerpactivityinfo/', views.MaintenanceRPActivityInfoList.as_view(), name='maintenancerpactivityinfo-list'),
    path('maintenancerpactivityinfo/<int:pk>/', views.MaintenanceRPActivityInfoDetail.as_view(), name='maintenancerpactivityinfo-detail'),

    # MaintenanceRPIncidentInfo URLs
    path('maintenancerpincidentinfo/', views.MaintenanceRPIncidentInfoList.as_view(), name='maintenancerpincidentinfo-list'),
    path('maintenancerpincidentinfo/<int:pk>/', views.MaintenanceRPIncidentInfoDetail.as_view(), name='maintenancerpincidentinfo-detail'),
     path('maintenancerpincidentinfo/', views.MaintenanceRPIncidentInfoList.as_view(), name='maintenancerpincidentinfo-list'),
    path('maintenancerpincidentinfo/<int:pk>/', views.MaintenanceRPIncidentInfoDetail.as_view(), name='maintenancerpincidentinfo-detail'),

    # MaintenanceRPManpowerDetail URLs
    path('maintenancerpmanpowerdetail/', views.MaintenanceRPManpowerDetailList.as_view(), name='maintenancerpmanpowerdetail-list'),
    path('maintenancerpmanpowerdetail/<int:pk>/', views.MaintenanceRPManpowerDetailDetail.as_view(), name='maintenancerpmanpowerdetail-detail'),

    # MaintenanceRPToolsDetail URLs
    path('maintenancerptoolsdetail/', views.MaintenanceRPToolsDetailList.as_view(), name='maintenancerptoolsdetail-list'),
    path('maintenancerptoolsdetail/<int:pk>/', views.MaintenanceRPToolsDetailDetail.as_view(), name='maintenancerptoolsdetail-detail'),
    path('party_mst/', views.PartyMstList.as_view(), name='party_mst-list'),
    path('party_mst/<int:pk>/', views.PartyMstDetail.as_view(), name='party_mst-detail'),
    path('poheaders/', views.POHeaderList.as_view(), name='poheader-list'),
    path('poheaders/<int:pk>/', views.POHeaderDetail.as_view(), name='poheader-detail'),
    path('poitems/', views.POItemList.as_view(), name='poitem-list'),
    path('poitems/<int:pk>/', views.POItemDetail.as_view(), name='poitem-detail'),
    path('purchasereqdetail/', views.PurchaseReqDetailList.as_view(), name='purchasereqdetail-list'),
    path('purchasereqdetail/<int:pk>/', views.PurchaseReqDetailDetail.as_view(), name='purchasereqdetail-detail'),
    path('purchasereqheader/', views.PurchaseReqHeaderList.as_view(), name='purchasereqheader-list'),
    path('purchasereqheader/<str:pk>/', views.PurchaseReqHeaderDetail.as_view(), name='purchasereqheader-detail'),
    path('qcreqdetail/', views.QCReqDetailList.as_view(), name='qcreqdetail-list'),
    path('qcreqdetail/<int:pk>/', views.QCReqDetailDetail.as_view(), name='qcreqdetail-detail'),
    path('qcreqheader/', views.QCReqHeaderList.as_view(), name='qcreqheader-list'),
    path('qcreqheader/<str:pk>/', views.QCReqHeaderDetail.as_view(), name='qcreqheader-detail'),
    path('requisitionheader/', views.RequisitionHeaderList.as_view(), name='requisitionheader-list'),
    path('requisitionheader/<str:pk>/', views.RequisitionHeaderDetail.as_view(), name='requisitionheader-detail'),

    # Requisition Item URLs
    path('requisitionitem/', views.RequisitionItemList.as_view(), name='requisitionitem-list'),
    path('requisitionitem/<int:pk>/', views.RequisitionItemDetail.as_view(), name='requisitionitem-detail'),

    # Role Master URLs
    path('rolemaster/', views.RoleMasterList.as_view(), name='rolemaster-list'),
    path('rolemaster/<str:pk>/', views.RoleMasterDetail.as_view(), name='rolemaster-detail'),

    # Unit Master URLs
    path('unitmaster/', views.UnitMasterList.as_view(), name='unitmaster-list'),
    path('unitmaster/<str:pk>/', views.UnitMasterDetail.as_view(), name='unitmaster-detail'),

    # Warehouse Master URLs
    path('warehousemaster/', views.WarehouseMasterList.as_view(), name='warehousemaster-list'),
    path('warehousemaster/<str:pk>/', views.WarehouseMasterDetail.as_view(), name='warehousemaster-detail'),

    # QC Request Detail URLs
    path('qcrequestdetail/', views.QCRequestDetailList.as_view(), name='qcrequestdetail-list'),
    path('qcrequestdetail/<int:pk>/', views.QCRequestDetailDetail.as_view(), name='qcrequestdetail-detail'),

]