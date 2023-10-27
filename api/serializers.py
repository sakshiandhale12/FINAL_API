# serializers.py
from rest_framework import serializers
from .models import EquipmentMst,AssetMst,DepartmentMaster,PartyMst,MaintenanceReportingHeader, MaintenanceRequestHeader, MaintenanceRPActivityInfo, MaintenanceRPIncidentInfo,DepreciationAssetDtl, DepreciationCalcHdr, EmployeeMaster,GrnHdr, GrnItems, IssueHdr, IssueItems,   ItemMaster,LocationMst,MaintenanceIncidentInfo,MaintenanceInspHdr,MaintenanceJbActivityInfo,MaintenanceJbConsumableInfo,MaintenanceJbHdr,MaintenanceJbIncidentInfo,MaintenanceJbManpowerDtl,MaintenanceJbToolsDtl
from .models import GrnHdr, GrnItems, IssueHdr, IssueItems,RequisitionHeader, RequisitionItem, RoleMaster, UnitMaster, WarehouseMaster, QCRequestDetail, EmployeeMaster

class EquipmentMstSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentMst
        fields = '__all__'


class AssetMstSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMst
        fields = '__all__'

class DepartmentMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentMaster
        fields = '__all__'

class DepreciationAssetDtlSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepreciationAssetDtl
        fields = '__all__'

class DepreciationCalcHdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepreciationCalcHdr
        fields = '__all__'

class EmployeeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMaster
        fields = '__all__'
        

class GrnHdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnHdr
        fields = '__all__'

class GrnItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnItems
        fields = '__all__'

class IssueHdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueHdr
        fields = '__all__'

class IssueItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueItems
        fields = '__all__'
class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = '__all__'

# Serializer for LocationMst
class LocationMstSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationMst
        fields = '__all__'

# Serializer for MaintenanceIncidentInfo
class MaintenanceIncidentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceIncidentInfo
        fields = '__all__'

# Serializer for MaintenanceInspHdr
class MaintenanceInspHdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceInspHdr
        fields = '__all__'

# Serializer for MaintenanceJbActivityInfo
class MaintenanceJbActivityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceJbActivityInfo
        fields = '__all__'

# Serializer for MaintenanceJbConsumableInfo
class MaintenanceJbConsumableInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceJbConsumableInfo
        fields = '__all__'

# Serializer for MaintenanceJbHdr
class MaintenanceJbHdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceJbHdr
        fields = '__all__'

# Serializer for MaintenanceJbIncidentInfo
class MaintenanceJbIncidentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceJbIncidentInfo
        fields = '__all__'

# Serializer for MaintenanceJbManpowerDtl
class MaintenanceJbManpowerDtlSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceJbManpowerDtl
        fields = '__all__'

# Serializer for MaintenanceJbToolsDtl
class MaintenanceJbToolsDtlSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceJbToolsDtl
        fields = '__all__'

class MaintenanceReportingHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceReportingHeader
        fields = '__all__'

class MaintenanceRequestHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRequestHeader
        fields = '__all__'

class MaintenanceRPActivityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRPActivityInfo
        fields = '__all__'

class MaintenanceRPIncidentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRPIncidentInfo
        fields = '__all__'
        
from rest_framework import serializers
from .models import MaintenanceRPIncidentInfo, MaintenanceRPManpowerDetail, MaintenanceRPToolsDetail

class MaintenanceRPIncidentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRPIncidentInfo
        fields = '__all__'

class MaintenanceRPManpowerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRPManpowerDetail
        fields = '__all__'

class MaintenanceRPToolsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRPToolsDetail
        fields = '__all__'
class PartyMstSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyMst
        fields = '__all__'
        
from rest_framework import serializers
from .models import POHeader, POItem

class POHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = POHeader
        fields = '__all__'

class POItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = POItem
        fields = '__all__'

# serializers.py

from rest_framework import serializers
from .models import PurchaseReqDetail, PurchaseReqHeader, QCReqDetail, QCReqHeader

class PurchaseReqDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseReqDetail
        fields = '__all__'

class PurchaseReqHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseReqHeader
        fields = '__all__'

class QCReqDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QCReqDetail
        fields = '__all__'

class QCReqHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = QCReqHeader
        fields = '__all__'
        
class RequisitionHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitionHeader
        fields = '__all__'

class RequisitionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitionItem
        fields = '__all__'

class RoleMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleMaster
        fields = '__all__'

class UnitMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitMaster
        fields = '__all__'

class WarehouseMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseMaster
        fields = '__all__'

class QCRequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = QCRequestDetail
        fields = '__all__'


# from django.apps import apps
# from django.core.management import call_command

# # Replace 'your_app_name' with the name of your Django app
# app_name = 'your_app_name'

# # Get all models from the app
# app_models = apps.get_app_config(app_name).get_models()

# # Create serializers for each model
# for model in app_models:
#     model_name = model.__name__

#     # Define fields for the serializer
#     fields = '__all__'  # You can customize this as needed

#     # Create the serializer Python code
#     serializer_code = f"""from rest_framework import serializers
# from .models import {model_name}

# class {model_name}Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = {model_name}
#         fields = {fields}
# """

#     # Save the generated serializer code to a file
#     with open(f"{app_name}/serializers.py", "a") as serializer_file:
#         serializer_file.write(serializer_code)

# print("Serializers have been generated.")
