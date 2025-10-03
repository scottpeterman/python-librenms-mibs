# SNMP MIB module (VMWARE-ENV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\vmware\VMWARE-ENV-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:16 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(vmwESX,) = mibBuilder.importSymbols(
    "VMWARE-PRODUCTS-MIB",
    "vmwESX")

(vmwNotifications,
 vmwProductSpecific) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwNotifications",
    "vmwProductSpecific")

(VmwCIMAlertFormat,
 VmwCIMAlertTypes,
 VmwCIMSeverity,
 VmwCimName,
 VmwLongSnmpAdminString,
 VmwSubsystemStatus,
 VmwSubsystemTypes) = mibBuilder.importSymbols(
    "VMWARE-TC-MIB",
    "VmwCIMAlertFormat",
    "VmwCIMAlertTypes",
    "VmwCIMSeverity",
    "VmwCimName",
    "VmwLongSnmpAdminString",
    "VmwSubsystemStatus",
    "VmwSubsystemTypes")


# MODULE-IDENTITY

vmwEnvironmentalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10)
)
if mibBuilder.loadTexts:
    vmwEnvironmentalMIB.setRevisions(
        ("2017-06-05 00:00",
         "2010-05-12 00:00",
         "2008-10-30 00:00",
         "2007-12-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwESXNotifications_ObjectIdentity = ObjectIdentity
vmwESXNotifications = _VmwESXNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0)
)
if mibBuilder.loadTexts:
    vmwESXNotifications.setStatus("current")
_VmwEnv_ObjectIdentity = ObjectIdentity
vmwEnv = _VmwEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20)
)
_VmwEnvNumber_Type = Integer32
_VmwEnvNumber_Object = MibScalar
vmwEnvNumber = _VmwEnvNumber_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 1),
    _VmwEnvNumber_Type()
)
vmwEnvNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvNumber.setStatus("current")
_VmwEnvLastChange_Type = TimeTicks
_VmwEnvLastChange_Object = MibScalar
vmwEnvLastChange = _VmwEnvLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 2),
    _VmwEnvLastChange_Type()
)
vmwEnvLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvLastChange.setStatus("current")
_VmwEnvTable_Object = MibTable
vmwEnvTable = _VmwEnvTable_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3)
)
if mibBuilder.loadTexts:
    vmwEnvTable.setStatus("current")
_VmwEnvEntry_Object = MibTableRow
vmwEnvEntry = _VmwEnvEntry_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1)
)
vmwEnvEntry.setIndexNames(
    (0, "VMWARE-ENV-MIB", "vmwEnvIndex"),
)
if mibBuilder.loadTexts:
    vmwEnvEntry.setStatus("current")


class _VmwEnvIndex_Type(Integer32):
    """Custom type vmwEnvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VmwEnvIndex_Type.__name__ = "Integer32"
_VmwEnvIndex_Object = MibTableColumn
vmwEnvIndex = _VmwEnvIndex_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 1),
    _VmwEnvIndex_Type()
)
vmwEnvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vmwEnvIndex.setStatus("current")
_VmwSubsystemType_Type = VmwSubsystemTypes
_VmwSubsystemType_Object = MibTableColumn
vmwSubsystemType = _VmwSubsystemType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 2),
    _VmwSubsystemType_Type()
)
vmwSubsystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwSubsystemType.setStatus("current")
_VmwHardwareStatus_Type = VmwSubsystemStatus
_VmwHardwareStatus_Object = MibTableColumn
vmwHardwareStatus = _VmwHardwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 3),
    _VmwHardwareStatus_Type()
)
vmwHardwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwHardwareStatus.setStatus("current")
_VmwEventDescription_Type = DisplayString
_VmwEventDescription_Object = MibTableColumn
vmwEventDescription = _VmwEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 4),
    _VmwEventDescription_Type()
)
vmwEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEventDescription.setStatus("current")
_VmwEnvHardwareTime_Type = DateAndTime
_VmwEnvHardwareTime_Object = MibTableColumn
vmwEnvHardwareTime = _VmwEnvHardwareTime_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 5),
    _VmwEnvHardwareTime_Type()
)
vmwEnvHardwareTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvHardwareTime.setStatus("current")


class _VmwEnvHrDeviceIndex_Type(Integer32):
    """Custom type vmwEnvHrDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_VmwEnvHrDeviceIndex_Type.__name__ = "Integer32"
_VmwEnvHrDeviceIndex_Object = MibTableColumn
vmwEnvHrDeviceIndex = _VmwEnvHrDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 6),
    _VmwEnvHrDeviceIndex_Type()
)
vmwEnvHrDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvHrDeviceIndex.setStatus("current")


class _VmwEnvSelSensorNumber_Type(Integer32):
    """Custom type vmwEnvSelSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VmwEnvSelSensorNumber_Type.__name__ = "Integer32"
_VmwEnvSelSensorNumber_Object = MibTableColumn
vmwEnvSelSensorNumber = _VmwEnvSelSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 3, 1, 7),
    _VmwEnvSelSensorNumber_Type()
)
vmwEnvSelSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvSelSensorNumber.setStatus("current")
_VmwEnvironmentalMIBConformance_ObjectIdentity = ObjectIdentity
vmwEnvironmentalMIBConformance = _VmwEnvironmentalMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2)
)
_VmwEnvironmentMIBCompliances_ObjectIdentity = ObjectIdentity
vmwEnvironmentMIBCompliances = _VmwEnvironmentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1)
)
_VmwEnvMIBGroups_ObjectIdentity = ObjectIdentity
vmwEnvMIBGroups = _VmwEnvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2)
)


class _VmwSELCapacity_Type(Integer32):
    """Custom type vmwSELCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VmwSELCapacity_Type.__name__ = "Integer32"
_VmwSELCapacity_Object = MibScalar
vmwSELCapacity = _VmwSELCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 30),
    _VmwSELCapacity_Type()
)
vmwSELCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwSELCapacity.setStatus("current")


class _VmwEnvSource_Type(Integer32):
    """Custom type vmwEnvSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("sensors", 2),
          ("indications", 3),
          ("ipmi", 4))
    )


_VmwEnvSource_Type.__name__ = "Integer32"
_VmwEnvSource_Object = MibScalar
vmwEnvSource = _VmwEnvSource_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 100),
    _VmwEnvSource_Type()
)
vmwEnvSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvSource.setStatus("current")
_VmwEnvInIndications_Type = Counter32
_VmwEnvInIndications_Object = MibScalar
vmwEnvInIndications = _VmwEnvInIndications_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 101),
    _VmwEnvInIndications_Type()
)
vmwEnvInIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvInIndications.setStatus("current")
_VmwEnvLastIn_Type = TimeTicks
_VmwEnvLastIn_Object = MibScalar
vmwEnvLastIn = _VmwEnvLastIn_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 102),
    _VmwEnvLastIn_Type()
)
vmwEnvLastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvLastIn.setStatus("current")
_VmwEnvOutNotifications_Type = Counter32
_VmwEnvOutNotifications_Object = MibScalar
vmwEnvOutNotifications = _VmwEnvOutNotifications_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 103),
    _VmwEnvOutNotifications_Type()
)
vmwEnvOutNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvOutNotifications.setStatus("current")
_VmwEnvInErrs_Type = Counter32
_VmwEnvInErrs_Object = MibScalar
vmwEnvInErrs = _VmwEnvInErrs_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 104),
    _VmwEnvInErrs_Type()
)
vmwEnvInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvInErrs.setStatus("current")
_VmwEnvIndOidErrs_Type = Counter32
_VmwEnvIndOidErrs_Object = MibScalar
vmwEnvIndOidErrs = _VmwEnvIndOidErrs_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 105),
    _VmwEnvIndOidErrs_Type()
)
vmwEnvIndOidErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvIndOidErrs.setStatus("current")
_VmwEnvCvtValueErrs_Type = Counter32
_VmwEnvCvtValueErrs_Object = MibScalar
vmwEnvCvtValueErrs = _VmwEnvCvtValueErrs_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 106),
    _VmwEnvCvtValueErrs_Type()
)
vmwEnvCvtValueErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvCvtValueErrs.setStatus("current")
_VmwEnvCvtSyntaxErrs_Type = Counter32
_VmwEnvCvtSyntaxErrs_Object = MibScalar
vmwEnvCvtSyntaxErrs = _VmwEnvCvtSyntaxErrs_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 107),
    _VmwEnvCvtSyntaxErrs_Type()
)
vmwEnvCvtSyntaxErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvCvtSyntaxErrs.setStatus("current")
_VmwEnvCvtOidErrs_Type = Counter32
_VmwEnvCvtOidErrs_Object = MibScalar
vmwEnvCvtOidErrs = _VmwEnvCvtOidErrs_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 108),
    _VmwEnvCvtOidErrs_Type()
)
vmwEnvCvtOidErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvCvtOidErrs.setStatus("current")
_VmwEnvGetClassErrs_Type = Counter32
_VmwEnvGetClassErrs_Object = MibScalar
vmwEnvGetClassErrs = _VmwEnvGetClassErrs_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 109),
    _VmwEnvGetClassErrs_Type()
)
vmwEnvGetClassErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvGetClassErrs.setStatus("current")
_VmwEnvPropertySkips_Type = Counter32
_VmwEnvPropertySkips_Object = MibScalar
vmwEnvPropertySkips = _VmwEnvPropertySkips_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 110),
    _VmwEnvPropertySkips_Type()
)
vmwEnvPropertySkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvPropertySkips.setStatus("current")
_VmwEnvIndicationSkips_Type = Counter32
_VmwEnvIndicationSkips_Object = MibScalar
vmwEnvIndicationSkips = _VmwEnvIndicationSkips_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 111),
    _VmwEnvIndicationSkips_Type()
)
vmwEnvIndicationSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmwEnvIndicationSkips.setStatus("current")
_VmwEnvIPMI_ObjectIdentity = ObjectIdentity
vmwEnvIPMI = _VmwEnvIPMI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 25)
)
_VmwEnvCIM_ObjectIdentity = ObjectIdentity
vmwEnvCIM = _VmwEnvCIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30)
)
_VmwEnvDescription_Type = VmwLongSnmpAdminString
_VmwEnvDescription_Object = MibScalar
vmwEnvDescription = _VmwEnvDescription_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 1),
    _VmwEnvDescription_Type()
)
vmwEnvDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvDescription.setStatus("deprecated")
_VmwEnvEventTime_Type = DateAndTime
_VmwEnvEventTime_Object = MibScalar
vmwEnvEventTime = _VmwEnvEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 2),
    _VmwEnvEventTime_Type()
)
vmwEnvEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvEventTime.setStatus("deprecated")
_VmwEnvIndicationTime_Type = DateAndTime
_VmwEnvIndicationTime_Object = MibScalar
vmwEnvIndicationTime = _VmwEnvIndicationTime_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 3),
    _VmwEnvIndicationTime_Type()
)
vmwEnvIndicationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvIndicationTime.setStatus("deprecated")
_VmwEnvPerceivedSeverity_Type = VmwCIMSeverity
_VmwEnvPerceivedSeverity_Object = MibScalar
vmwEnvPerceivedSeverity = _VmwEnvPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 4),
    _VmwEnvPerceivedSeverity_Type()
)
vmwEnvPerceivedSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvPerceivedSeverity.setStatus("deprecated")
_VmwEnvAlertType_Type = VmwCIMAlertTypes
_VmwEnvAlertType_Object = MibScalar
vmwEnvAlertType = _VmwEnvAlertType_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 5),
    _VmwEnvAlertType_Type()
)
vmwEnvAlertType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvAlertType.setStatus("deprecated")
_VmwEnvSysCreationClassName_Type = VmwCimName
_VmwEnvSysCreationClassName_Object = MibScalar
vmwEnvSysCreationClassName = _VmwEnvSysCreationClassName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 6),
    _VmwEnvSysCreationClassName_Type()
)
vmwEnvSysCreationClassName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvSysCreationClassName.setStatus("deprecated")
_VmwEnvAlertingElement_Type = VmwCimName
_VmwEnvAlertingElement_Object = MibScalar
vmwEnvAlertingElement = _VmwEnvAlertingElement_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 7),
    _VmwEnvAlertingElement_Type()
)
vmwEnvAlertingElement.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvAlertingElement.setStatus("deprecated")
_VmwEnvAlertingFormat_Type = VmwCIMAlertFormat
_VmwEnvAlertingFormat_Object = MibScalar
vmwEnvAlertingFormat = _VmwEnvAlertingFormat_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 8),
    _VmwEnvAlertingFormat_Type()
)
vmwEnvAlertingFormat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvAlertingFormat.setStatus("deprecated")
_VmwEnvSystemName_Type = VmwCimName
_VmwEnvSystemName_Object = MibScalar
vmwEnvSystemName = _VmwEnvSystemName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 9),
    _VmwEnvSystemName_Type()
)
vmwEnvSystemName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvSystemName.setStatus("deprecated")
_VmwEnvProviderName_Type = VmwCimName
_VmwEnvProviderName_Object = MibScalar
vmwEnvProviderName = _VmwEnvProviderName_Object(
    (1, 3, 6, 1, 4, 1, 6876, 4, 30, 10),
    _VmwEnvProviderName_Type()
)
vmwEnvProviderName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vmwEnvProviderName.setStatus("deprecated")

# Managed Objects groups

vmwEnvironmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 1)
)
vmwEnvironmentGroup.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvLastChange"),
        ("VMWARE-ENV-MIB", "vmwSubsystemType"),
        ("VMWARE-ENV-MIB", "vmwHardwareStatus"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"))
)
if mibBuilder.loadTexts:
    vmwEnvironmentGroup.setStatus("deprecated")

vmwEnvAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 5)
)
vmwEnvAlertGroup.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSource"),
        ("VMWARE-ENV-MIB", "vmwEnvInIndications"),
        ("VMWARE-ENV-MIB", "vmwEnvLastIn"),
        ("VMWARE-ENV-MIB", "vmwEnvOutNotifications"),
        ("VMWARE-ENV-MIB", "vmwEnvInErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvIndOidErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvCvtValueErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvCvtSyntaxErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvCvtOidErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvGetClassErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvPropertySkips"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationSkips"),
        ("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwEnvAlertGroup.setStatus("obsolete")

vmwEnvironmentGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 6)
)
vmwEnvironmentGroup2.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvLastChange"),
        ("VMWARE-ENV-MIB", "vmwSELCapacity"),
        ("VMWARE-ENV-MIB", "vmwSubsystemType"),
        ("VMWARE-ENV-MIB", "vmwHardwareStatus"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEnvHrDeviceIndex"),
        ("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"))
)
if mibBuilder.loadTexts:
    vmwEnvironmentGroup2.setStatus("current")

vmwEnvCIMToSNMP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 20)
)
vmwEnvCIMToSNMP.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSource"),
        ("VMWARE-ENV-MIB", "vmwEnvInIndications"),
        ("VMWARE-ENV-MIB", "vmwEnvLastIn"),
        ("VMWARE-ENV-MIB", "vmwEnvOutNotifications"),
        ("VMWARE-ENV-MIB", "vmwEnvInErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvIndOidErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvCvtValueErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvCvtSyntaxErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvCvtOidErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvGetClassErrs"),
        ("VMWARE-ENV-MIB", "vmwEnvPropertySkips"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationSkips"))
)
if mibBuilder.loadTexts:
    vmwEnvCIMToSNMP.setStatus("current")


# Notification objects

vmwEnvHardwareEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 0, 301)
)
vmwEnvHardwareEvent.setObjects(
      *(("VMWARE-ENV-MIB", "vmwSubsystemType"),
        ("VMWARE-ENV-MIB", "vmwHardwareStatus"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"))
)
if mibBuilder.loadTexts:
    vmwEnvHardwareEvent.setStatus(
        "deprecated"
    )

vmwESXEnvHardwareEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 301)
)
vmwESXEnvHardwareEvent.setObjects(
      *(("VMWARE-ENV-MIB", "vmwSubsystemType"),
        ("VMWARE-ENV-MIB", "vmwHardwareStatus"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"))
)
if mibBuilder.loadTexts:
    vmwESXEnvHardwareEvent.setStatus(
        "deprecated"
    )

vmwESXEnvHardwareAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 302)
)
vmwESXEnvHardwareAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvHardwareAlert.setStatus(
        "deprecated"
    )

vmwESXEnvBatteryAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 303)
)
vmwESXEnvBatteryAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvBatteryAlert.setStatus(
        "deprecated"
    )

vmwESXEnvChassisAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 304)
)
vmwESXEnvChassisAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvChassisAlert.setStatus(
        "deprecated"
    )

vmwESXEnvThermalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 305)
)
vmwESXEnvThermalAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvThermalAlert.setStatus(
        "deprecated"
    )

vmwESXEnvDiskAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 306)
)
vmwESXEnvDiskAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvDiskAlert.setStatus(
        "deprecated"
    )

vmwESXEnvPowerAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 307)
)
vmwESXEnvPowerAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvPowerAlert.setStatus(
        "deprecated"
    )

vmwESXEnvProcessorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 308)
)
vmwESXEnvProcessorAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvProcessorAlert.setStatus(
        "deprecated"
    )

vmwESXEnvMemoryAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 309)
)
vmwESXEnvMemoryAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvMemoryAlert.setStatus(
        "deprecated"
    )

vmwESXEnvBIOSAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 310)
)
vmwESXEnvBIOSAlert.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvDescription"),
        ("VMWARE-ENV-MIB", "vmwEnvEventTime"),
        ("VMWARE-ENV-MIB", "vmwEnvIndicationTime"),
        ("VMWARE-ENV-MIB", "vmwEnvPerceivedSeverity"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertType"),
        ("VMWARE-ENV-MIB", "vmwEnvSysCreationClassName"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingElement"),
        ("VMWARE-ENV-MIB", "vmwEnvAlertingFormat"),
        ("VMWARE-ENV-MIB", "vmwEnvSystemName"),
        ("VMWARE-ENV-MIB", "vmwEnvProviderName"))
)
if mibBuilder.loadTexts:
    vmwESXEnvBIOSAlert.setStatus(
        "deprecated"
    )

vmwEnvIpmiSelFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 390)
)
vmwEnvIpmiSelFull.setObjects(
    ("VMWARE-ENV-MIB", "vmwSELCapacity")
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelFull.setStatus(
        "current"
    )

vmwEnvIpmiSelMemoryRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 400)
)
vmwEnvIpmiSelMemoryRaised.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"))
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelMemoryRaised.setStatus(
        "current"
    )

vmwEnvIpmiSelMemoryCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 401)
)
vmwEnvIpmiSelMemoryCleared.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"))
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelMemoryCleared.setStatus(
        "current"
    )

vmwEnvIpmiSelPowerSupplyRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 410)
)
vmwEnvIpmiSelPowerSupplyRaised.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"))
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelPowerSupplyRaised.setStatus(
        "current"
    )

vmwEnvIpmiSelPowerSupplyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 411)
)
vmwEnvIpmiSelPowerSupplyCleared.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"))
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelPowerSupplyCleared.setStatus(
        "current"
    )

vmwEnvIpmiSelFanRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 420)
)
vmwEnvIpmiSelFanRaised.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"))
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelFanRaised.setStatus(
        "current"
    )

vmwEnvIpmiSelFanCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 421)
)
vmwEnvIpmiSelFanCleared.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"))
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelFanCleared.setStatus(
        "current"
    )

vmwEnvIpmiSelCpuRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 430)
)
vmwEnvIpmiSelCpuRaised.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"))
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelCpuRaised.setStatus(
        "current"
    )

vmwEnvIpmiSelCpuCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6876, 4, 1, 0, 431)
)
vmwEnvIpmiSelCpuCleared.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvSelSensorNumber"),
        ("VMWARE-ENV-MIB", "vmwEnvHardwareTime"),
        ("VMWARE-ENV-MIB", "vmwEventDescription"))
)
if mibBuilder.loadTexts:
    vmwEnvIpmiSelCpuCleared.setStatus(
        "current"
    )


# Notifications groups

vmwEnvNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 2)
)
vmwEnvNotificationGroup.setObjects(
    ("VMWARE-ENV-MIB", "vmwEnvHardwareEvent")
)
if mibBuilder.loadTexts:
    vmwEnvNotificationGroup.setStatus(
        "deprecated"
    )

vmwESXEnvNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 3)
)
vmwESXEnvNotificationGroup.setObjects(
    ("VMWARE-ENV-MIB", "vmwESXEnvHardwareEvent")
)
if mibBuilder.loadTexts:
    vmwESXEnvNotificationGroup.setStatus(
        "deprecated"
    )

vmwESXEnvNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 4)
)
vmwESXEnvNotificationGroup2.setObjects(
      *(("VMWARE-ENV-MIB", "vmwESXEnvHardwareAlert"),
        ("VMWARE-ENV-MIB", "vmwESXEnvBatteryAlert"),
        ("VMWARE-ENV-MIB", "vmwESXEnvChassisAlert"),
        ("VMWARE-ENV-MIB", "vmwESXEnvThermalAlert"),
        ("VMWARE-ENV-MIB", "vmwESXEnvDiskAlert"),
        ("VMWARE-ENV-MIB", "vmwESXEnvPowerAlert"),
        ("VMWARE-ENV-MIB", "vmwESXEnvProcessorAlert"),
        ("VMWARE-ENV-MIB", "vmwESXEnvMemoryAlert"),
        ("VMWARE-ENV-MIB", "vmwESXEnvBIOSAlert"))
)
if mibBuilder.loadTexts:
    vmwESXEnvNotificationGroup2.setStatus(
        "deprecated"
    )

vmwESXEnvNotificationGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 2, 10)
)
vmwESXEnvNotificationGroup3.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvIpmiSelFull"),
        ("VMWARE-ENV-MIB", "vmwEnvIpmiSelMemoryRaised"),
        ("VMWARE-ENV-MIB", "vmwEnvIpmiSelMemoryCleared"),
        ("VMWARE-ENV-MIB", "vmwEnvIpmiSelPowerSupplyRaised"),
        ("VMWARE-ENV-MIB", "vmwEnvIpmiSelPowerSupplyCleared"),
        ("VMWARE-ENV-MIB", "vmwEnvIpmiSelFanRaised"),
        ("VMWARE-ENV-MIB", "vmwEnvIpmiSelFanCleared"),
        ("VMWARE-ENV-MIB", "vmwEnvIpmiSelCpuRaised"),
        ("VMWARE-ENV-MIB", "vmwEnvIpmiSelCpuCleared"))
)
if mibBuilder.loadTexts:
    vmwESXEnvNotificationGroup3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vmwEnvMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1, 2)
)
vmwEnvMIBBasicCompliance.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvironmentGroup"),
        ("VMWARE-ENV-MIB", "vmwEnvNotificationGroup"))
)
if mibBuilder.loadTexts:
    vmwEnvMIBBasicCompliance.setStatus(
        "obsolete"
    )

vmwEnvMIBBasicCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1, 3)
)
vmwEnvMIBBasicCompliance2.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvironmentGroup"),
        ("VMWARE-ENV-MIB", "vmwESXEnvNotificationGroup"),
        ("VMWARE-ENV-MIB", "vmwEnvNotificationGroup"))
)
if mibBuilder.loadTexts:
    vmwEnvMIBBasicCompliance2.setStatus(
        "deprecated"
    )

vmwEnvMIBBasicCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1, 4)
)
vmwEnvMIBBasicCompliance3.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvAlertGroup"),
        ("VMWARE-ENV-MIB", "vmwESXEnvNotificationGroup2"),
        ("VMWARE-ENV-MIB", "vmwESXEnvNotificationGroup2"))
)
if mibBuilder.loadTexts:
    vmwEnvMIBBasicCompliance3.setStatus(
        "obsolete"
    )

vmwEnvMIBBasicCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6876, 4, 20, 10, 2, 1, 5)
)
vmwEnvMIBBasicCompliance4.setObjects(
      *(("VMWARE-ENV-MIB", "vmwEnvCIMToSNMP"),
        ("VMWARE-ENV-MIB", "vmwEnvironmentGroup2"),
        ("VMWARE-ENV-MIB", "vmwESXEnvNotificationGroup3"),
        ("VMWARE-ENV-MIB", "vmwESXEnvNotificationGroup3"))
)
if mibBuilder.loadTexts:
    vmwEnvMIBBasicCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-ENV-MIB",
    **{"vmwEnvHardwareEvent": vmwEnvHardwareEvent,
       "vmwESXNotifications": vmwESXNotifications,
       "vmwESXEnvHardwareEvent": vmwESXEnvHardwareEvent,
       "vmwESXEnvHardwareAlert": vmwESXEnvHardwareAlert,
       "vmwESXEnvBatteryAlert": vmwESXEnvBatteryAlert,
       "vmwESXEnvChassisAlert": vmwESXEnvChassisAlert,
       "vmwESXEnvThermalAlert": vmwESXEnvThermalAlert,
       "vmwESXEnvDiskAlert": vmwESXEnvDiskAlert,
       "vmwESXEnvPowerAlert": vmwESXEnvPowerAlert,
       "vmwESXEnvProcessorAlert": vmwESXEnvProcessorAlert,
       "vmwESXEnvMemoryAlert": vmwESXEnvMemoryAlert,
       "vmwESXEnvBIOSAlert": vmwESXEnvBIOSAlert,
       "vmwEnvIpmiSelFull": vmwEnvIpmiSelFull,
       "vmwEnvIpmiSelMemoryRaised": vmwEnvIpmiSelMemoryRaised,
       "vmwEnvIpmiSelMemoryCleared": vmwEnvIpmiSelMemoryCleared,
       "vmwEnvIpmiSelPowerSupplyRaised": vmwEnvIpmiSelPowerSupplyRaised,
       "vmwEnvIpmiSelPowerSupplyCleared": vmwEnvIpmiSelPowerSupplyCleared,
       "vmwEnvIpmiSelFanRaised": vmwEnvIpmiSelFanRaised,
       "vmwEnvIpmiSelFanCleared": vmwEnvIpmiSelFanCleared,
       "vmwEnvIpmiSelCpuRaised": vmwEnvIpmiSelCpuRaised,
       "vmwEnvIpmiSelCpuCleared": vmwEnvIpmiSelCpuCleared,
       "vmwEnv": vmwEnv,
       "vmwEnvNumber": vmwEnvNumber,
       "vmwEnvLastChange": vmwEnvLastChange,
       "vmwEnvTable": vmwEnvTable,
       "vmwEnvEntry": vmwEnvEntry,
       "vmwEnvIndex": vmwEnvIndex,
       "vmwSubsystemType": vmwSubsystemType,
       "vmwHardwareStatus": vmwHardwareStatus,
       "vmwEventDescription": vmwEventDescription,
       "vmwEnvHardwareTime": vmwEnvHardwareTime,
       "vmwEnvHrDeviceIndex": vmwEnvHrDeviceIndex,
       "vmwEnvSelSensorNumber": vmwEnvSelSensorNumber,
       "vmwEnvironmentalMIB": vmwEnvironmentalMIB,
       "vmwEnvironmentalMIBConformance": vmwEnvironmentalMIBConformance,
       "vmwEnvironmentMIBCompliances": vmwEnvironmentMIBCompliances,
       "vmwEnvMIBBasicCompliance": vmwEnvMIBBasicCompliance,
       "vmwEnvMIBBasicCompliance2": vmwEnvMIBBasicCompliance2,
       "vmwEnvMIBBasicCompliance3": vmwEnvMIBBasicCompliance3,
       "vmwEnvMIBBasicCompliance4": vmwEnvMIBBasicCompliance4,
       "vmwEnvMIBGroups": vmwEnvMIBGroups,
       "vmwEnvironmentGroup": vmwEnvironmentGroup,
       "vmwEnvNotificationGroup": vmwEnvNotificationGroup,
       "vmwESXEnvNotificationGroup": vmwESXEnvNotificationGroup,
       "vmwESXEnvNotificationGroup2": vmwESXEnvNotificationGroup2,
       "vmwEnvAlertGroup": vmwEnvAlertGroup,
       "vmwEnvironmentGroup2": vmwEnvironmentGroup2,
       "vmwESXEnvNotificationGroup3": vmwESXEnvNotificationGroup3,
       "vmwEnvCIMToSNMP": vmwEnvCIMToSNMP,
       "vmwSELCapacity": vmwSELCapacity,
       "vmwEnvSource": vmwEnvSource,
       "vmwEnvInIndications": vmwEnvInIndications,
       "vmwEnvLastIn": vmwEnvLastIn,
       "vmwEnvOutNotifications": vmwEnvOutNotifications,
       "vmwEnvInErrs": vmwEnvInErrs,
       "vmwEnvIndOidErrs": vmwEnvIndOidErrs,
       "vmwEnvCvtValueErrs": vmwEnvCvtValueErrs,
       "vmwEnvCvtSyntaxErrs": vmwEnvCvtSyntaxErrs,
       "vmwEnvCvtOidErrs": vmwEnvCvtOidErrs,
       "vmwEnvGetClassErrs": vmwEnvGetClassErrs,
       "vmwEnvPropertySkips": vmwEnvPropertySkips,
       "vmwEnvIndicationSkips": vmwEnvIndicationSkips,
       "vmwEnvIPMI": vmwEnvIPMI,
       "vmwEnvCIM": vmwEnvCIM,
       "vmwEnvDescription": vmwEnvDescription,
       "vmwEnvEventTime": vmwEnvEventTime,
       "vmwEnvIndicationTime": vmwEnvIndicationTime,
       "vmwEnvPerceivedSeverity": vmwEnvPerceivedSeverity,
       "vmwEnvAlertType": vmwEnvAlertType,
       "vmwEnvSysCreationClassName": vmwEnvSysCreationClassName,
       "vmwEnvAlertingElement": vmwEnvAlertingElement,
       "vmwEnvAlertingFormat": vmwEnvAlertingFormat,
       "vmwEnvSystemName": vmwEnvSystemName,
       "vmwEnvProviderName": vmwEnvProviderName}
)
