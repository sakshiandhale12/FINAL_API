# views.py
from rest_framework import generics
from .models import EquipmentMst,AssetMst,DepartmentMaster
from .serializers import EquipmentMstSerializer,AssetMstSerializer,DepartmentMasterSerializer,DepartmentMasterSerializer
from .models import DepreciationAssetDtl, DepreciationCalcHdr, EmployeeMaster
from .serializers import DepreciationAssetDtlSerializer, DepreciationCalcHdrSerializer, EmployeeMasterSerializer
from rest_framework import viewsets
from .models import GrnHdr, GrnItems, IssueHdr, IssueItems,ItemMaster, LocationMst, MaintenanceIncidentInfo, MaintenanceInspHdr, MaintenanceJbActivityInfo, MaintenanceJbConsumableInfo, MaintenanceJbHdr, MaintenanceJbIncidentInfo, MaintenanceJbManpowerDtl, MaintenanceJbToolsDtl
from .models import MaintenanceReportingHeader, MaintenanceRequestHeader, MaintenanceRPActivityInfo, MaintenanceRPIncidentInfo
from .serializers import MaintenanceReportingHeaderSerializer, MaintenanceRequestHeaderSerializer, MaintenanceRPActivityInfoSerializer, MaintenanceRPIncidentInfoSerializer
from .serializers import GrnHdrSerializer, GrnItemsSerializer,  ItemMasterSerializer,ItemMasterSerializer, LocationMstSerializer, LocationMstSerializer,MaintenanceIncidentInfoSerializer,MaintenanceIncidentInfoSerializer, MaintenanceInspHdrSerializer, MaintenanceInspHdrSerializer, MaintenanceJbActivityInfoSerializer, MaintenanceJbActivityInfoSerializer,MaintenanceJbConsumableInfoSerializer,MaintenanceJbConsumableInfoSerializer,MaintenanceJbHdrSerializer,MaintenanceJbHdrSerializer,MaintenanceJbIncidentInfoSerializer,MaintenanceJbIncidentInfoSerializer,MaintenanceJbManpowerDtlSerializer,MaintenanceJbManpowerDtlSerializer,MaintenanceJbToolsDtlSerializer,MaintenanceJbToolsDtlSerializer,   IssueHdrSerializer, IssueItemsSerializer
from .models import PartyMst,PurchaseReqDetail, PurchaseReqHeader, QCReqDetail, QCReqHeader
from .serializers import PartyMstSerializer,PurchaseReqDetailSerializer,PurchaseReqHeaderSerializer,QCReqDetailSerializer,QCReqHeaderSerializer


class EquipmentMstListView(generics.ListCreateAPIView):
    serializer_class = EquipmentMstSerializer

    def get_queryset(self):
        queryset = EquipmentMst.objects.all()
        isActive = self.request.query_params.get('isActive', None)
        
        if isActive is not None:
            queryset = queryset.filter(active_yn=isActive)

        return queryset

class EquipmentMstDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentMst.objects.all()
    serializer_class = EquipmentMstSerializer

#
from rest_framework import generics

# ... (import your model and serializer if not already imported)

class EquipmentMstListView(generics.ListCreateAPIView):
    queryset = EquipmentMst.objects.all()
    serializer_class = EquipmentMstSerializer

    def get_queryset(self):
        # You can keep your existing code for filtering if needed
        queryset = super().get_queryset()
        isActive = self.request.query_params.get('isActive', None)

        if isActive is not None:
            queryset = queryset.filter(active_yn=isActive)

        return queryset

class EquipmentMstDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EquipmentMst.objects.all()
    serializer_class = EquipmentMstSerializer


class AssetMstListCreateView(generics.ListCreateAPIView):
    queryset = AssetMst.objects.all()
    serializer_class = AssetMstSerializer

class AssetMstDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssetMst.objects.all()
    serializer_class = AssetMstSerializer

#

class DepartmentMasterListCreateView(generics.ListCreateAPIView):
    queryset = DepartmentMaster.objects.all()
    serializer_class = DepartmentMasterSerializer

class DepartmentMasterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepartmentMaster.objects.all()
    serializer_class = DepartmentMasterSerializer
    
#


class DepreciationAssetDtlListCreateView(generics.ListCreateAPIView):
    queryset = DepreciationAssetDtl.objects.all()
    serializer_class = DepreciationAssetDtlSerializer

class DepreciationAssetDtlDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepreciationAssetDtl.objects.all()
    serializer_class = DepreciationAssetDtlSerializer
    

class DepreciationCalcHdrListCreateView(generics.ListCreateAPIView):
    queryset = DepreciationCalcHdr.objects.all()
    serializer_class = DepreciationCalcHdrSerializer

class DepreciationCalcHdrDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DepreciationCalcHdr.objects.all()
    serializer_class = DepreciationCalcHdrSerializer

class EmployeeMasterListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeMaster.objects.all()
    serializer_class = EmployeeMasterSerializer

class EmployeeMasterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeMaster.objects.all()
    serializer_class = EmployeeMasterSerializer

class GrnHdrList(generics.ListCreateAPIView):
    queryset = GrnHdr.objects.all()
    serializer_class = GrnHdrSerializer

class GrnHdrDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrnHdr.objects.all()
    serializer_class = GrnHdrSerializer

class GrnItemsList(generics.ListCreateAPIView):
    queryset = GrnItems.objects.all()
    serializer_class = GrnItemsSerializer

class GrnItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrnItems.objects.all()
    serializer_class = GrnItemsSerializer

class IssueHdrList(generics.ListCreateAPIView):
    queryset = IssueHdr.objects.all()
    serializer_class = IssueHdrSerializer

class IssueHdrDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssueHdr.objects.all()
    serializer_class = IssueHdrSerializer

class IssueItemsList(generics.ListCreateAPIView):
    queryset = IssueItems.objects.all()
    serializer_class = IssueItemsSerializer

class IssueItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssueItems.objects.all()
    serializer_class = IssueItemsSerializer
    
class ItemMasterList(generics.ListCreateAPIView):
    queryset = ItemMaster.objects.all()
    serializer_class = ItemMasterSerializer

class ItemMasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemMaster.objects.all()
    serializer_class = ItemMasterSerializer


# Views for LocationMst
class LocationMstList(generics.ListCreateAPIView):
    queryset = LocationMst.objects.all()
    serializer_class = LocationMstSerializer

class LocationMstDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationMst.objects.all()
    serializer_class = LocationMstSerializer
# Views for MaintenanceIncidentInfo
class MaintenanceIncidentInfoList(generics.ListCreateAPIView):
    queryset = MaintenanceIncidentInfo.objects.all()
    serializer_class = MaintenanceIncidentInfoSerializer

class MaintenanceIncidentInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceIncidentInfo.objects.all()
    serializer_class = MaintenanceIncidentInfoSerializer

# Views for MaintenanceInspHdr
class MaintenanceInspHdrList(generics.ListCreateAPIView):
    queryset = MaintenanceInspHdr.objects.all()
    serializer_class = MaintenanceInspHdrSerializer

class MaintenanceInspHdrDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceInspHdr.objects.all()
    serializer_class = MaintenanceInspHdrSerializer

# Views for MaintenanceJbActivityInfo
class MaintenanceJbActivityInfoList(generics.ListCreateAPIView):
    queryset = MaintenanceJbActivityInfo.objects.all()
    serializer_class = MaintenanceJbActivityInfoSerializer

class MaintenanceJbActivityInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceJbActivityInfo.objects.all()
    serializer_class = MaintenanceJbActivityInfoSerializer

# Views for MaintenanceJbConsumableInfo
class MaintenanceJbConsumableInfoList(generics.ListCreateAPIView):
    queryset = MaintenanceJbConsumableInfo.objects.all()
    serializer_class = MaintenanceJbConsumableInfoSerializer,

class MaintenanceJbConsumableInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceJbConsumableInfo.objects.all()
    serializer_class = MaintenanceJbConsumableInfoSerializer

# Views for MaintenanceJbHdr
class MaintenanceJbHdrList(generics.ListCreateAPIView):
    queryset = MaintenanceJbHdr.objects.all()
    serializer_class = MaintenanceJbHdrSerializer


class MaintenanceJbHdrDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceJbHdr.objects.all()
    serializer_class = MaintenanceJbHdrSerializer

# Views for MaintenanceJbIncidentInfo
class MaintenanceJbIncidentInfoList(generics.ListCreateAPIView):
    queryset = MaintenanceJbIncidentInfo.objects.all()
    serializer_class = MaintenanceJbIncidentInfoSerializer

class MaintenanceJbIncidentInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceJbIncidentInfo.objects.all()
    serializer_class = MaintenanceJbIncidentInfoSerializer


# Views for MaintenanceJbManpowerDtl
class MaintenanceJbManpowerDtlList(generics.ListCreateAPIView):
    queryset = MaintenanceJbManpowerDtl.objects.all()
    serializer_class = MaintenanceJbManpowerDtlSerializer


class MaintenanceJbManpowerDtlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceJbManpowerDtl.objects.all()
    serializer_class = MaintenanceJbManpowerDtlSerializer

# Views for MaintenanceJbToolsDtl
class MaintenanceJbToolsDtlList(generics.ListCreateAPIView):
    queryset = MaintenanceJbToolsDtl.objects.all()
    serializer_class = MaintenanceJbToolsDtlSerializer

class MaintenanceJbToolsDtlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceJbToolsDtl.objects.all()
    serializer_class = MaintenanceJbToolsDtlSerializer
    
from rest_framework import generics
from .models import MaintenanceReportingHeader, MaintenanceRequestHeader, MaintenanceRPActivityInfo, MaintenanceRPIncidentInfo
from .serializers import MaintenanceReportingHeaderSerializer, MaintenanceRequestHeaderSerializer, MaintenanceRPActivityInfoSerializer, MaintenanceRPIncidentInfoSerializer

class MaintenanceReportingHeaderList(generics.ListCreateAPIView):
    queryset = MaintenanceReportingHeader.objects.all()
    serializer_class = MaintenanceReportingHeaderSerializer

class MaintenanceReportingHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceReportingHeader.objects.all()
    serializer_class = MaintenanceReportingHeaderSerializer

class MaintenanceRequestHeaderList(generics.ListCreateAPIView):
    queryset = MaintenanceRequestHeader.objects.all()
    serializer_class = MaintenanceRequestHeaderSerializer

class MaintenanceRequestHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRequestHeader.objects.all()
    serializer_class = MaintenanceRequestHeaderSerializer

class MaintenanceRPActivityInfoList(generics.ListCreateAPIView):
    queryset = MaintenanceRPActivityInfo.objects.all()
    serializer_class = MaintenanceRPActivityInfoSerializer

class MaintenanceRPActivityInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRPActivityInfo.objects.all()
    serializer_class = MaintenanceRPActivityInfoSerializer

class MaintenanceRPIncidentInfoList(generics.ListCreateAPIView):
    queryset = MaintenanceRPIncidentInfo.objects.all()
    serializer_class = MaintenanceRPIncidentInfoSerializer

class MaintenanceRPIncidentInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRPIncidentInfo.objects.all()
    serializer_class = MaintenanceRPIncidentInfoSerializer
    
from rest_framework import generics
from .models import MaintenanceRPIncidentInfo, MaintenanceRPManpowerDetail, MaintenanceRPToolsDetail
from .serializers import MaintenanceRPIncidentInfoSerializer, MaintenanceRPManpowerDetailSerializer, MaintenanceRPToolsDetailSerializer

class MaintenanceRPIncidentInfoList(generics.ListCreateAPIView):
    queryset = MaintenanceRPIncidentInfo.objects.all()
    serializer_class = MaintenanceRPIncidentInfoSerializer

class MaintenanceRPIncidentInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRPIncidentInfo.objects.all()
    serializer_class = MaintenanceRPIncidentInfoSerializer

class MaintenanceRPManpowerDetailList(generics.ListCreateAPIView):
    queryset = MaintenanceRPManpowerDetail.objects.all()
    serializer_class = MaintenanceRPManpowerDetailSerializer

class MaintenanceRPManpowerDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRPManpowerDetail.objects.all()
    serializer_class = MaintenanceRPManpowerDetailSerializer

class MaintenanceRPToolsDetailList(generics.ListCreateAPIView):
    queryset = MaintenanceRPToolsDetail.objects.all()
    serializer_class = MaintenanceRPToolsDetailSerializer

class MaintenanceRPToolsDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintenanceRPToolsDetail.objects.all()
    serializer_class = MaintenanceRPToolsDetailSerializer

class PartyMstList(generics.ListCreateAPIView):
    queryset = PartyMst.objects.all()
    serializer_class = PartyMstSerializer

class PartyMstDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartyMst.objects.all()
    serializer_class = PartyMstSerializer
    
from rest_framework import generics
from .models import POHeader, POItem
from .serializers import POHeaderSerializer, POItemSerializer

class POHeaderList(generics.ListCreateAPIView):
    queryset = POHeader.objects.all()
    serializer_class = POHeaderSerializer

class POHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = POHeader.objects.all()
    serializer_class = POHeaderSerializer

class POItemList(generics.ListCreateAPIView):
    queryset = POItem.objects.all()
    serializer_class = POItemSerializer

class POItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = POItem.objects.all()
    serializer_class = POItemSerializer
class PurchaseReqDetailList(generics.ListCreateAPIView):
    queryset = PurchaseReqDetail.objects.all()
    serializer_class = PurchaseReqDetailSerializer

class PurchaseReqDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseReqDetail.objects.all()
    serializer_class = PurchaseReqDetailSerializer

class PurchaseReqHeaderList(generics.ListCreateAPIView):
    queryset = PurchaseReqHeader.objects.all()
    serializer_class = PurchaseReqHeaderSerializer

class PurchaseReqHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseReqHeader.objects.all()
    serializer_class = PurchaseReqHeaderSerializer

class QCReqDetailList(generics.ListCreateAPIView):
    queryset = QCReqDetail.objects.all()
    serializer_class = QCReqDetailSerializer

class QCReqDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QCReqDetail.objects.all()
    serializer_class = QCReqDetailSerializer

class QCReqHeaderList(generics.ListCreateAPIView):
    queryset = QCReqHeader.objects.all()
    serializer_class = QCReqHeaderSerializer

class QCReqHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QCReqHeader.objects.all()
    serializer_class = QCReqHeaderSerializer
    
from rest_framework import generics
from .models import RequisitionHeader, RequisitionItem, RoleMaster, UnitMaster, WarehouseMaster, QCRequestDetail, EmployeeMaster
from .serializers import RequisitionHeaderSerializer, RequisitionItemSerializer, RoleMasterSerializer, UnitMasterSerializer, WarehouseMasterSerializer, QCRequestDetailSerializer, EmployeeMasterSerializer

class RequisitionHeaderList(generics.ListCreateAPIView):
    queryset = RequisitionHeader.objects.all()
    serializer_class = RequisitionHeaderSerializer

class RequisitionHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequisitionHeader.objects.all()
    serializer_class = RequisitionHeaderSerializer

class RequisitionItemList(generics.ListCreateAPIView):
    queryset = RequisitionItem.objects.all()
    serializer_class = RequisitionItemSerializer

class RequisitionItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequisitionItem.objects.all()
    serializer_class = RequisitionItemSerializer

class RoleMasterList(generics.ListCreateAPIView):
    queryset = RoleMaster.objects.all()
    serializer_class = RoleMasterSerializer

class RoleMasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoleMaster.objects.all()
    serializer_class = RoleMasterSerializer

class UnitMasterList(generics.ListCreateAPIView):
    queryset = UnitMaster.objects.all()
    serializer_class = UnitMasterSerializer

class UnitMasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnitMaster.objects.all()
    serializer_class = UnitMasterSerializer

class WarehouseMasterList(generics.ListCreateAPIView):
    queryset = WarehouseMaster.objects.all()
    serializer_class = WarehouseMasterSerializer

class WarehouseMasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WarehouseMaster.objects.all()
    serializer_class = WarehouseMasterSerializer

class QCRequestDetailList(generics.ListCreateAPIView):
    queryset = QCRequestDetail.objects.all()
    serializer_class = QCRequestDetailSerializer

class QCRequestDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QCRequestDetail.objects.all()
    serializer_class = QCRequestDetailSerializer

class EmployeeMasterList(generics.ListCreateAPIView):
    queryset = EmployeeMaster.objects.all()
    serializer_class = EmployeeMasterSerializer

class EmployeeMasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeMaster.objects.all()
    serializer_class = EmployeeMasterSerializer

