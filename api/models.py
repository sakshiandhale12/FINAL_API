from django.db import models


class AssetMst(models.Model):
    ast_code = models.AutoField(primary_key=True)
    ast_name = models.CharField(max_length=255)
    ast_long_name = models.CharField(max_length=255)
    ast_unit = models.CharField(max_length=50)
    ast_type = models.CharField(max_length=50)
    active_yn = models.BooleanField()
    ast_sr_no = models.CharField(max_length=50)
    ast_manufacturer = models.CharField(max_length=255)
    ast_life = models.CharField(max_length=50)
    ast_pur_rate = models.DecimalField(max_digits=10, decimal_places=2)
    ast_pur_date = models.DateField()
    ast_mfg_date = models.DateField()
    ast_exp_date = models.DateField()
    ast_war_type = models.CharField(max_length=50)
    ast_war_start_date = models.DateField()
    ast_watr_end_date = models.DateField()
    ast_service_prov = models.CharField(max_length=255)
    ast_contact_person = models.CharField(max_length=255)
    ast_contact_no = models.CharField(max_length=20)
    parent_ast_code = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    ref_code = models.CharField(max_length=255)
    prv_main_sch = models.CharField(max_length=255)
    last_main_dt = models.DateField()
    
    def __str__(self):
        return self.ast_name

class DepartmentMaster(models.Model):
    department_code = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.department_name

class DepreciationAssetDtl(models.Model):
    depr_sr_no = models.AutoField(primary_key=True)
    depr_asst_sr_no = models.IntegerField()
    eqmt_name = models.CharField(max_length=255)
    eqmt_code = models.CharField(max_length=20)
    installation_date = models.DateField()
    life_of_asset = models.CharField(max_length=50)
    no_of_days_left = models.IntegerField()
    no_of_years_left = models.IntegerField()
    cost_as_on = models.DecimalField(max_digits=10, decimal_places=2)
    addition = models.DecimalField(max_digits=10, decimal_places=2)
    deletion = models.DecimalField(max_digits=10, decimal_places=2)
    last_depreciation = models.DateField()
    wdv = models.DecimalField(max_digits=10, decimal_places=2)
    depr_amt = models.DecimalField(max_digits=10, decimal_places=2)
    depr_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_by = models.CharField(max_length=255)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.eqmt_name

class DepreciationCalcHdr(models.Model):
    depr_sr_no = models.AutoField(primary_key=True)
    location_code = models.CharField(max_length=50)
    fin_yr = models.CharField(max_length=20)
    as_on_date = models.DateField()
    department = models.ForeignKey('DepartmentMaster', on_delete=models.CASCADE)
    dept_date = models.DateField()
    created_by = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    depr_no = models.CharField(max_length=50)
    depr_tran_date = models.DateField()
    
    def __str__(self):
        return f"Depreciation Calculation {self.depr_sr_no}"
    
class EmployeeMaster(models.Model):
    emp_code = models.CharField(max_length=20, primary_key=True)
    emp_title = models.CharField(max_length=20)
    emp_fname = models.CharField(max_length=50)
    emp_lname = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='employee_profile_images/', blank=True, null=True)
    doj = models.DateField()
    department = models.ForeignKey('DepartmentMaster', on_delete=models.CASCADE)
    active_yn = models.BooleanField()
    emp_password = models.CharField(max_length=128)
    pan_no = models.CharField(max_length=10)
    pf_no = models.CharField(max_length=20)
    esic = models.CharField(max_length=20)
    uan_no = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    emp_mail_id = models.EmailField(max_length=100)
    manpower_rate_per_hr = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.emp_code} - {self.emp_fname} {self.emp_lname}"

class EquipmentMst(models.Model):
    eqp_code = models.IntegerField(primary_key=True)
    eqp_name = models.CharField(max_length=50)
    eqp_long_name = models.CharField(max_length=50)
    eqp_unit = models.CharField(max_length=50)
    eqp_type = models.CharField(max_length=50)
    active_yn = models.CharField(max_length=1)
    eqp_sr_no = models.CharField(max_length=50)
    eqp_manufacturer = models.CharField(max_length=50)
    eqp_life = models.CharField(max_length=50)
    eqp_pur_rate = models.DecimalField(max_digits=10, decimal_places=2)
    eqp_pur_date = models.DateField()
    eqp_mfg_date = models.DateField()
    eqp_exp_date = models.DateField()
    eqp_war_type = models.CharField(max_length=50)
    eqp_war_start_date = models.DateField()
    eqp_watr_end_date = models.DateField()
    eqp_service_prov = models.CharField(max_length=50)
    eqp_contact_person = models.CharField(max_length=50)
    eqp_contact_no = models.TextField()
    parent_eqp_code = models.IntegerField(blank=True, null=True)
    ref_code = models.CharField(max_length=50)
    prv_main_sch = models.CharField(max_length=50)
    last_main_dt = models.DateField()

    def __str__(self): 
        return self.eqp_name
    
# class demo(models.Model):
#     name= models.CharField(max_length=100)
#     roll= models.IntegerField()
#     mob_no= models.CharField(max_length=50)
#     sallary=models.IntegerField()
    
    

class GrnHdr(models.Model):
    grn_hdr_no = models.IntegerField(primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    grn_no = models.CharField(max_length=20)
    grn_date = models.DateField()
    remark = models.TextField()
    po_no = models.CharField(max_length=20)
    po_date = models.DateField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.grn_hdr_no

class GrnItems(models.Model):
    grn_hdr_no = models.ForeignKey(GrnHdr, on_delete=models.CASCADE)
    grn_item_no = models.IntegerField()
    item_code = models.CharField(max_length=50)
    item_qty = models.DecimalField(max_digits=10, decimal_places=2)
    item_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_val = models.DecimalField(max_digits=10, decimal_places=2)
    mfg_date = models.DateField()
    exp_date = models.DateField()
    igst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    igst_val = models.DecimalField(max_digits=10, decimal_places=2)
    sgst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    sgst_val = models.DecimalField(max_digits=10, decimal_places=2)
    cgst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    cgst_val = models.DecimalField(max_digits=10, decimal_places=2)
    ut_gst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    ut_gst_val = models.DecimalField(max_digits=10, decimal_places=2)
    wh_cd = models.CharField(max_length=10)
    code_head = models.CharField(max_length=20)
    major_head = models.CharField(max_length=20)
    minor_head = models.CharField(max_length=20)
    batch_id = models.CharField(max_length=20)

    def __str__(self):
        return self.item_code
from django.db import models

class IssueHdr(models.Model):
    iss_hdr_no = models.IntegerField(primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    iss_no = models.CharField(max_length=20)
    iss_date = models.DateField()
    remark = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    req_no = models.CharField(max_length=20)
    req_date = models.DateField()
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.iss_no

class IssueItems(models.Model):
    iss_hdr_no = models.ForeignKey(IssueHdr, on_delete=models.CASCADE)
    iss_item_no = models.IntegerField()
    item_code = models.CharField(max_length=50)
    item_qty = models.DecimalField(max_digits=10, decimal_places=2)
    item_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_val = models.DecimalField(max_digits=10, decimal_places=2)
    wh_cd = models.CharField(max_length=10)
    code_head = models.CharField(max_length=20)
    major_head = models.CharField(max_length=20)
    minor_head = models.CharField(max_length=20)
    batch_id = models.CharField(max_length=20)
    ref_grn_item_no = models.IntegerField()
    unit = models.CharField(max_length=10)
    mfg_date = models.DateField()
    exp_date = models.DateField()
    req_qty = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_code

class ItemMaster(models.Model):
    item_code = models.CharField(max_length=50, primary_key=True)
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=20)
    item_unit = models.CharField(max_length=10)
    item_rate = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField()
    gst_applicable_yn = models.CharField(max_length=1)
    hsn_code = models.CharField(max_length=20)
    igst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    sgst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    cgst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    ut_gst_rate = models.DecimalField(max_digits=5, decimal_places=2)
    safety_stock = models.DecimalField(max_digits=10, decimal_places=2)
    min_stock_level = models.DecimalField(max_digits=10, decimal_places=2)
    max_stock = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.DecimalField(max_digits=10, decimal_places=2)
    ref_code = models.CharField(max_length=20)
    trade_number = models.CharField(max_length=20)

    def __str__(self):
        return self.item_name

class LocationMst(models.Model):
    location_code = models.CharField(max_length=20, primary_key=True)
    location_name = models.CharField(max_length=100)

    def __str__(self):
        return self.location_name

class MaintenanceIncidentInfo(models.Model):
    mntc_req_hdr = models.IntegerField()
    mntc_incd_info_dtl = models.TextField()
    incd_info = models.CharField(max_length=20)
    incd_date = models.DateField()
    incd_report_time = models.TimeField()
    expected_res_date = models.DateField()
    instructions = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class MaintenanceInspHdr(models.Model):
    mntc_insp_hdr = models.CharField(max_length=20, primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    mr_no = models.CharField(max_length=20)
    mntc_insp_no = models.CharField(max_length=20)
    mntc_insp_date = models.DateField()
    mntc_rep_no = models.CharField(max_length=20)
    mntc_rep_date = models.DateField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class MaintenanceJbActivityInfo(models.Model):
    mntc_jbc_hdr = models.IntegerField()
    mntc_jbc_act_dtl = models.TextField()
    mntc_act_seq = models.IntegerField()
    mntc_act_desc = models.CharField(max_length=100)
    act_instructions = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
   
from django.db import models

class MaintenanceJbConsumableInfo(models.Model):
    mntc_jbc_hdr = models.ForeignKey('MaintenanceJbHdr', on_delete=models.CASCADE)
    mntc_jbc_cons_dtl = models.TextField()
    item_code = models.CharField(max_length=50)
    mntc_cons_req_qty = models.DecimalField(max_digits=10, decimal_places=2)
    cons_instructions = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class MaintenanceJbHdr(models.Model):
    mntc_jbc_hdr = models.CharField(max_length=20, primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    mntc_jbc_no = models.CharField(max_length=20)
    mntc_jbc_date = models.DateField()
    mntc_req_no = models.CharField(max_length=20)
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    parent_eqp_name = models.CharField(max_length=50)

class MaintenanceJbIncidentInfo(models.Model):
    mntc_jbc_hdr = models.ForeignKey(MaintenanceJbHdr, on_delete=models.CASCADE)
    mntc_jbc_inc_dtl = models.TextField()
    incd_info = models.CharField(max_length=20)
    incd_date = models.DateField()
    incd_report_time = models.TimeField()
    expected_res_date = models.DateField()
    inc_instructions = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class MaintenanceJbManpowerDtl(models.Model):
    mntc_jbc_hdr = models.ForeignKey(MaintenanceJbHdr, on_delete=models.CASCADE)
    mntc_jbc_mp_dtl = models.TextField()
    mntc_emp_cd = models.CharField(max_length=20)
    mntc_req_time = models.TimeField()
    manpower_instructions = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class MaintenanceJbToolsDtl(models.Model):
    mntc_jbc_hdr = models.ForeignKey(MaintenanceJbHdr, on_delete=models.CASCADE)
    mntc_jbc_tool_dtl = models.TextField()
    item_code = models.CharField(max_length=50)
    mntc_tool_req_qty = models.DecimalField(max_digits=10, decimal_places=2)
    tool_instructions = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class MaintenanceReportingHeader(models.Model):
    mntc_rp_hdr = models.CharField(max_length=20, primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    mr_no = models.CharField(max_length=20)
    mntc_rp_no = models.CharField(max_length=20)
    mntc_rp_date = models.DateField()
    mntc_job_no = models.CharField(max_length=20)
    mntc_job_date = models.DateField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.mntc_rp_hdr
from django.db import models

class MaintenanceRequestHeader(models.Model):
    mntc_req_hdr = models.CharField(max_length=20, primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    mntc_req_no = models.CharField(max_length=20)
    mntc_req_date = models.DateField()
    mntc_req_type = models.CharField(max_length=20)
    mntc_eqpmt_name = models.CharField(max_length=50)
    mntc_problem = models.TextField()
    mntc_severity = models.CharField(max_length=20)
    mntc_dept = models.CharField(max_length=20)
    mntc_eqpmt_loc = models.CharField(max_length=20)
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    parent_eqp_name = models.CharField(max_length=50)

    def __str__(self):
        return self.mntc_req_hdr
from django.db import models

class MaintenanceRPActivityInfo(models.Model):
    mntc_rp_hdr = models.ForeignKey(MaintenanceReportingHeader, on_delete=models.CASCADE)
    mntc_rp_act_dtl = models.TextField()
    mntc_jbc_act_dtl = models.TextField()
    mntc_action_taken = models.TextField()
    mntc_act_status = models.CharField(max_length=20)
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
from django.db import models

class MaintenanceRPIncidentInfo(models.Model):
    mntc_rp_hdr = models.ForeignKey(MaintenanceReportingHeader, on_delete=models.CASCADE)
    mntc_rp_inc_dtl = models.TextField()
    mntc_jbc_inc_dtl = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

from django.db import models

# class MaintenanceRPManpowerDetail(models.Model):
#     mntc_rp_hdr = models.ForeignKey(MaintenanceReportingHeader, on_delete=models.CASCADE)
#     mntc_mp_cons_dtl = models.ForeignKey('MaintenanceJBCManpowerDtl', on_delete=models.CASCADE)
#     mntc_rp_mp_dtl = models.TextField()
#     mntc_rp_act_time = models.TimeField()
#     mntc_rp_remarks = models.TextField()
#     created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
#     created_date = models.DateTimeField()

# from django.db import models

# class MaintenanceRPToolsDetail(models.Model):
#     mntc_jbc_tool_dtl = models.ForeignKey('MaintenanceJBCToolDtl', on_delete=models.CASCADE)
#     mntc_rp_hdr = models.ForeignKey(MaintenanceReportingHeader, on_delete=models.CASCADE)
#     tool_rp_remarks = models.TextField()
#     created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
#     created_date = models.DateTimeField()

# from django.db import models

class MaintenanceRPIncidentInfo(models.Model):
    mntc_rp_hdr = models.ForeignKey(MaintenanceReportingHeader, on_delete=models.CASCADE)
    mntc_rp_inc_dtl = models.TextField()
    mntc_jbc_inc_dtl = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    # def __str__(self):
    #     return f'MaintenanceRPIncidentInfo - ID: {self.id}'

class MaintenanceRPManpowerDetail(models.Model):
    mntc_rp_hdr = models.ForeignKey(MaintenanceReportingHeader, on_delete=models.CASCADE)
    mntc_mp_cons_dtl = models.ForeignKey('MaintenanceJbManpowerDtl', on_delete=models.CASCADE)
    mntc_rp_mp_dtl = models.TextField()
    mntc_rp_act_time = models.TimeField()
    mntc_rp_remarks = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    # def __str__(self):
    #     return f'MaintenanceRPManpowerDetail - ID: {self.id}'

class MaintenanceRPToolsDetail(models.Model):
    mntc_rp_hdr = models.ForeignKey(MaintenanceReportingHeader, on_delete=models.CASCADE)
    mntc_jbc_tool_dtl = models.TextField()
    mntc_rp_tool_dtl = models.TextField()
    tool_rp_remarks = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    # def __str__(self):
    #     return f'MaintenanceRPToolsDetail - ID: {self.id}'



from django.db import models

class PartyMst(models.Model):
    party_name = models.CharField(max_length=100)
    party_code = models.CharField(max_length=20, unique=True)
    party_website = models.URLField(max_length=200, blank=True, null=True)
    party_type = models.CharField(max_length=20)
    party_mail_id = models.EmailField(max_length=100, blank=True, null=True)
    party_contact_no = models.CharField(max_length=15, blank=True, null=True)
    active = models.BooleanField(default=True)
    ofc_add1 = models.TextField()
    ofc_country = models.CharField(max_length=50)
    ofc_state = models.CharField(max_length=50)
    ofc_district = models.CharField(max_length=50)
    ofc_city = models.CharField(max_length=50)
    ofc_pin = models.CharField(max_length=10)
    pan_no = models.CharField(max_length=10)
    gstin_no = models.CharField(max_length=15, blank=True, null=True)
    msme_yn = models.BooleanField(default=False)
    msme_type = models.CharField(max_length=20, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    bank_acno = models.CharField(max_length=20, blank=True, null=True)
    ifsc_code = models.CharField(max_length=15, blank=True, null=True)
    swift_code = models.CharField(max_length=15, blank=True, null=True)
    micr_code = models.CharField(max_length=15, blank=True, null=True)
    ac_type = models.CharField(max_length=20, blank=True, null=True)
    beneficiary_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.party_name
from django.db import models

class POHeader(models.Model):
    po_hdr_no = models.AutoField(primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    po_no = models.CharField(max_length=20)
    po_date = models.DateField()
    party_code = models.CharField(max_length=20)
    contract_no = models.CharField(max_length=20)
    contract_date = models.DateField()
    remark = models.TextField()
    po_purpose = models.TextField()
    approve_yn = models.CharField(max_length=1)
    doc_upload = models.FileField(upload_to='documents/')
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    purc_req_no = models.CharField(max_length=20)
    purc_req_date = models.DateField()

    def __str__(self):
        return self.po_no

class POItem(models.Model):
    po_hdr_no = models.ForeignKey(POHeader, on_delete=models.CASCADE)
    po_item_no = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=20)
    item_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    item_qty = models.DecimalField(max_digits=10, decimal_places=2)
    item_value = models.DecimalField(max_digits=10, decimal_places=2)
    item_rate = models.DecimalField(max_digits=10, decimal_places=2)
    igst_value = models.DecimalField(max_digits=10, decimal_places=2)
    disc_value = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    req_on = models.DateField()
    item_remarks = models.TextField()
    code_head = models.CharField(max_length=20)
    major_head = models.CharField(max_length=20)
    minor_head = models.CharField(max_length=20)
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    igst_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.item_name
    
from django.db import models
from django.contrib.auth.models import User

# Your other models...

class PurchaseReqDetail(models.Model):
    purc_req_hdr_no = models.CharField(max_length=20)
    purc_req_dtl_no = models.CharField(max_length=20)
    item_code = models.CharField(max_length=50)
    item_name = models.CharField(max_length=100)
    item_ref_no = models.CharField(max_length=20)
    unit = models.CharField(max_length=20)
    item_qty = models.DecimalField(max_digits=10, decimal_places=2)
    req_on = models.DateField()
    code_head = models.CharField(max_length=20)
    major_head = models.CharField(max_length=20)
    minor_head = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    
class PurchaseReqHeader(models.Model):
    purc_req_hdr_no = models.CharField(max_length=20, primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    purc_req_no = models.CharField(max_length=20)
    purc_req_date = models.DateField()
    purc_department = models.CharField(max_length=50)
    purc_req_by = models.CharField(max_length=50)
    doc_ref_no = models.CharField(max_length=20)
    purc_purpose = models.TextField()
    doc_upload = models.FileField(upload_to='documents/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class QCReqDetail(models.Model):
    qc_req_hdr_no = models.CharField(max_length=20)
    qc_req_dtl_no = models.CharField(max_length=20)
    qc_parameter = models.CharField(max_length=100)
    standard = models.TextField()
    accept_criteria = models.TextField()
    tolerance = models.DecimalField(max_digits=5, decimal_places=2)
    remark = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class QCReqHeader(models.Model):
    qc_req_hdr_no = models.CharField(max_length=20)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    qc_req_no = models.CharField(max_length=20)
    qc_req_date = models.DateField()
    mntc_jbc_no = models.CharField(max_length=20)
    mntc_jbc_date = models.DateField()
    parent_eqp_name = models.CharField(max_length=50)
    eqp_name = models.CharField(max_length=100)
    req_type = models.CharField(max_length=20)
    severity = models.CharField(max_length=20)
    qc_department = models.CharField(max_length=50)
    problem_st = models.TextField()
    eqp_location = models.CharField(max_length=50)
    doc_upload = models.FileField(upload_to='documents/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    
class RequisitionHeader(models.Model):
    req_hdr_no = models.CharField(max_length=20, primary_key=True)
    location_code = models.CharField(max_length=20)
    fin_yr = models.CharField(max_length=10)
    req_no = models.CharField(max_length=20)
    req_date = models.DateField()
    remark = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    department = models.CharField(max_length=50)
    main_req_no = models.CharField(max_length=20)
    main_req_dt = models.DateField()
    eqp_name = models.CharField(max_length=50)
    approve_yn = models.CharField(max_length=1)

class RequisitionItem(models.Model):
    req_hdr_no = models.ForeignKey(RequisitionHeader, on_delete=models.CASCADE)
    req_item_no = models.AutoField(primary_key=True)
    item_code = models.CharField(max_length=20)
    item_qty = models.DecimalField(max_digits=10, decimal_places=2)
    item_remarks = models.TextField()
    code_head = models.CharField(max_length=20)
    major_head = models.CharField(max_length=20)
    minor_head = models.CharField(max_length=20)
    unit = models.ForeignKey('UnitMaster', on_delete=models.CASCADE)
    req_on = models.CharField(max_length=20)

class RoleMaster(models.Model):
    role_code = models.CharField(max_length=20, primary_key=True)
    role_name = models.CharField(max_length=50)
    role_parent = models.CharField(max_length=20)

class UnitMaster(models.Model):
    unit_code = models.CharField(max_length=20, primary_key=True)
    unit_name = models.CharField(max_length=50)

class WarehouseMaster(models.Model):
    wh_cd = models.CharField(max_length=20, primary_key=True)
    wh_disp_name = models.CharField(max_length=50)

class QCRequestDetail(models.Model):
    qc_req_hdr_no = models.ForeignKey(RequisitionHeader, on_delete=models.CASCADE)
    qc_req_dtl_no = models.AutoField(primary_key=True)
    qc_parameter = models.CharField(max_length=50)
    standard = models.CharField(max_length=50)
    accept_criteria = models.CharField(max_length=50)
    tollerence = models.CharField(max_length=50)
    remark = models.TextField()
    created_by = models.ForeignKey('EmployeeMaster', on_delete=models.CASCADE)
    created_date = models.DateTimeField()