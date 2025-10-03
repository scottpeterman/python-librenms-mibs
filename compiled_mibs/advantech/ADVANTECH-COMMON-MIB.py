# SNMP MIB module (ADVANTECH-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\advantech\ADVANTECH-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:03 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(DateAndTime,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DateAndTime",
    "DisplayString")


# MODULE-IDENTITY

advantechCommonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 100)
)
if mibBuilder.loadTexts:
    advantechCommonMIB.setRevisions(
        ("2013-05-25 00:00",
         "2013-08-28 00:00",
         "2013-08-29 00:00",
         "2013-09-06 00:00",
         "2014-10-13 00:00",
         "2014-10-22 00:00",
         "2015-01-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Advantech_ObjectIdentity = ObjectIdentity
advantech = _Advantech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297)
)
_AtSystem_ObjectIdentity = ObjectIdentity
atSystem = _AtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1)
)
_SysModuleID_Type = DisplayString
_SysModuleID_Object = MibScalar
sysModuleID = _SysModuleID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1, 1),
    _SysModuleID_Type()
)
sysModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysModuleID.setStatus("mandatory")
_SysDeviceName_Type = DisplayString
_SysDeviceName_Object = MibScalar
sysDeviceName = _SysDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1, 2),
    _SysDeviceName_Type()
)
sysDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDeviceName.setStatus("current")
_SysDescr_Type = DisplayString
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1, 3),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDescr.setStatus("current")


class _SysImageVersion_Type(OctetString):
    """Custom type sysImageVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysImageVersion_Type.__name__ = "OctetString"
_SysImageVersion_Object = MibScalar
sysImageVersion = _SysImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1, 4),
    _SysImageVersion_Type()
)
sysImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysImageVersion.setStatus("mandatory")


class _SysReleaseDate_Type(OctetString):
    """Custom type sysReleaseDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysReleaseDate_Type.__name__ = "OctetString"
_SysReleaseDate_Object = MibScalar
sysReleaseDate = _SysReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1, 5),
    _SysReleaseDate_Type()
)
sysReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysReleaseDate.setStatus("mandatory")
_SysFirstBootTime_Type = DateAndTime
_SysFirstBootTime_Object = MibScalar
sysFirstBootTime = _SysFirstBootTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1, 6),
    _SysFirstBootTime_Type()
)
sysFirstBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirstBootTime.setStatus("mandatory")
_SysBootTime_Type = DateAndTime
_SysBootTime_Object = MibScalar
sysBootTime = _SysBootTime_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1, 7),
    _SysBootTime_Type()
)
sysBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootTime.setStatus("mandatory")
_SysBootCount_Type = Counter32
_SysBootCount_Object = MibScalar
sysBootCount = _SysBootCount_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 1, 8),
    _SysBootCount_Type()
)
sysBootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootCount.setStatus("mandatory")
_AtMgmt_ObjectIdentity = ObjectIdentity
atMgmt = _AtMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2)
)
_SnmpTrapSrvObj_ObjectIdentity = ObjectIdentity
snmpTrapSrvObj = _SnmpTrapSrvObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1)
)
_SnmpTrapSrvNumber_Type = Integer32
_SnmpTrapSrvNumber_Object = MibScalar
snmpTrapSrvNumber = _SnmpTrapSrvNumber_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 1),
    _SnmpTrapSrvNumber_Type()
)
snmpTrapSrvNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapSrvNumber.setStatus("mandatory")
_SnmpTrapSrvTable_Object = MibTable
snmpTrapSrvTable = _SnmpTrapSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2)
)
if mibBuilder.loadTexts:
    snmpTrapSrvTable.setStatus("mandatory")
_SnmpTrapSrvEntry_Object = MibTableRow
snmpTrapSrvEntry = _SnmpTrapSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1)
)
snmpTrapSrvEntry.setIndexNames(
    (0, "ADVANTECH-COMMON-MIB", "snmpTrapSrvIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapSrvEntry.setStatus("mandatory")


class _SnmpTrapSrvIndex_Type(Integer32):
    """Custom type snmpTrapSrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SnmpTrapSrvIndex_Type.__name__ = "Integer32"
_SnmpTrapSrvIndex_Object = MibTableColumn
snmpTrapSrvIndex = _SnmpTrapSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 1),
    _SnmpTrapSrvIndex_Type()
)
snmpTrapSrvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapSrvIndex.setStatus("mandatory")
_SnmpTrapSrvIP_Type = IpAddress
_SnmpTrapSrvIP_Object = MibTableColumn
snmpTrapSrvIP = _SnmpTrapSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 2),
    _SnmpTrapSrvIP_Type()
)
snmpTrapSrvIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSrvIP.setStatus("mandatory")


class _SnmpTrapSrvPort_Type(Integer32):
    """Custom type snmpTrapSrvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpTrapSrvPort_Type.__name__ = "Integer32"
_SnmpTrapSrvPort_Object = MibTableColumn
snmpTrapSrvPort = _SnmpTrapSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 3),
    _SnmpTrapSrvPort_Type()
)
snmpTrapSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSrvPort.setStatus("mandatory")


class _SnmpTrapSrvAuthentication_Type(Integer32):
    """Custom type snmpTrapSrvAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SnmpTrapSrvAuthentication_Type.__name__ = "Integer32"
_SnmpTrapSrvAuthentication_Object = MibTableColumn
snmpTrapSrvAuthentication = _SnmpTrapSrvAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 4),
    _SnmpTrapSrvAuthentication_Type()
)
snmpTrapSrvAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSrvAuthentication.setStatus("mandatory")


class _SnmpTrapSrvCommunity_Type(DisplayString):
    """Custom type snmpTrapSrvCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SnmpTrapSrvCommunity_Type.__name__ = "DisplayString"
_SnmpTrapSrvCommunity_Object = MibTableColumn
snmpTrapSrvCommunity = _SnmpTrapSrvCommunity_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 5),
    _SnmpTrapSrvCommunity_Type()
)
snmpTrapSrvCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapSrvCommunity.setStatus("mandatory")


class _SnmpTrapVersion_Type(Integer32):
    """Custom type snmpTrapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_SnmpTrapVersion_Type.__name__ = "Integer32"
_SnmpTrapVersion_Object = MibTableColumn
snmpTrapVersion = _SnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 6),
    _SnmpTrapVersion_Type()
)
snmpTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapVersion.setStatus("mandatory")
_AtPciConfig_ObjectIdentity = ObjectIdentity
atPciConfig = _AtPciConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3)
)
_PciConfigObj_ObjectIdentity = ObjectIdentity
pciConfigObj = _PciConfigObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1)
)
_PsNumber_Type = Integer32
_PsNumber_Object = MibScalar
psNumber = _PsNumber_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 1),
    _PsNumber_Type()
)
psNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psNumber.setStatus("current")
_PciSlotTable_Object = MibTable
pciSlotTable = _PciSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2)
)
if mibBuilder.loadTexts:
    pciSlotTable.setStatus("current")
_PciSlotEntry_Object = MibTableRow
pciSlotEntry = _PciSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1)
)
pciSlotEntry.setIndexNames(
    (0, "ADVANTECH-COMMON-MIB", "psIndex"),
)
if mibBuilder.loadTexts:
    pciSlotEntry.setStatus("current")


class _PsIndex_Type(Integer32):
    """Custom type psIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PsIndex_Type.__name__ = "Integer32"
_PsIndex_Object = MibTableColumn
psIndex = _PsIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 1),
    _PsIndex_Type()
)
psIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIndex.setStatus("mandatory")


class _PsBusIndex_Type(Integer32):
    """Custom type psBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PsBusIndex_Type.__name__ = "Integer32"
_PsBusIndex_Object = MibTableColumn
psBusIndex = _PsBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 2),
    _PsBusIndex_Type()
)
psBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBusIndex.setStatus("mandatory")


class _PsDeviceIndex_Type(Integer32):
    """Custom type psDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PsDeviceIndex_Type.__name__ = "Integer32"
_PsDeviceIndex_Object = MibTableColumn
psDeviceIndex = _PsDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 3),
    _PsDeviceIndex_Type()
)
psDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDeviceIndex.setStatus("mandatory")


class _PsFunctionIndex_Type(Integer32):
    """Custom type psFunctionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PsFunctionIndex_Type.__name__ = "Integer32"
_PsFunctionIndex_Object = MibTableColumn
psFunctionIndex = _PsFunctionIndex_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 4),
    _PsFunctionIndex_Type()
)
psFunctionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psFunctionIndex.setStatus("mandatory")
_PsDisplayName_Type = SnmpAdminString
_PsDisplayName_Object = MibTableColumn
psDisplayName = _PsDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 5),
    _PsDisplayName_Type()
)
psDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDisplayName.setStatus("mandatory")
_PsDescr_Type = SnmpAdminString
_PsDescr_Object = MibTableColumn
psDescr = _PsDescr_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 6),
    _PsDescr_Type()
)
psDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDescr.setStatus("mandatory")
_PsVendorID_Type = Integer32
_PsVendorID_Object = MibTableColumn
psVendorID = _PsVendorID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 7),
    _PsVendorID_Type()
)
psVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psVendorID.setStatus("mandatory")
_PsDeviceID_Type = Integer32
_PsDeviceID_Object = MibTableColumn
psDeviceID = _PsDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 8),
    _PsDeviceID_Type()
)
psDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psDeviceID.setStatus("mandatory")
_PsSubsysVendorID_Type = Integer32
_PsSubsysVendorID_Object = MibTableColumn
psSubsysVendorID = _PsSubsysVendorID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 9),
    _PsSubsysVendorID_Type()
)
psSubsysVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSubsysVendorID.setStatus("mandatory")
_PsSubsysDeviceID_Type = Integer32
_PsSubsysDeviceID_Object = MibTableColumn
psSubsysDeviceID = _PsSubsysDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 10),
    _PsSubsysDeviceID_Type()
)
psSubsysDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psSubsysDeviceID.setStatus("mandatory")


class _PsClassCode_Type(OctetString):
    """Custom type psClassCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_PsClassCode_Type.__name__ = "OctetString"
_PsClassCode_Object = MibTableColumn
psClassCode = _PsClassCode_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 11),
    _PsClassCode_Type()
)
psClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psClassCode.setStatus("mandatory")
_PsManufacturer_Type = SnmpAdminString
_PsManufacturer_Object = MibTableColumn
psManufacturer = _PsManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 12),
    _PsManufacturer_Type()
)
psManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psManufacturer.setStatus("current")
_PsLocation_Type = SnmpAdminString
_PsLocation_Object = MibTableColumn
psLocation = _PsLocation_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 13),
    _PsLocation_Type()
)
psLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psLocation.setStatus("current")


class _PsBaseAddress_Type(OctetString):
    """Custom type psBaseAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_PsBaseAddress_Type.__name__ = "OctetString"
_PsBaseAddress_Object = MibTableColumn
psBaseAddress = _PsBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 14),
    _PsBaseAddress_Type()
)
psBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psBaseAddress.setStatus("mandatory")


class _PsLength_Type(OctetString):
    """Custom type psLength based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_PsLength_Type.__name__ = "OctetString"
_PsLength_Object = MibTableColumn
psLength = _PsLength_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 15),
    _PsLength_Type()
)
psLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psLength.setStatus("mandatory")
_PsIRQ_Type = Integer32
_PsIRQ_Object = MibTableColumn
psIRQ = _PsIRQ_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 16),
    _PsIRQ_Type()
)
psIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psIRQ.setStatus("mandatory")


class _PsState_Type(Integer32):
    """Custom type psState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PsState_Type.__name__ = "Integer32"
_PsState_Object = MibTableColumn
psState = _PsState_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 17),
    _PsState_Type()
)
psState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psState.setStatus("current")


class _PsModuleType_Type(Integer32):
    """Custom type psModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("com", 1),
          ("can", 2),
          ("amonet", 3),
          ("motion", 4),
          ("wireless", 5))
    )


_PsModuleType_Type.__name__ = "Integer32"
_PsModuleType_Object = MibTableColumn
psModuleType = _PsModuleType_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 18),
    _PsModuleType_Type()
)
psModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psModuleType.setStatus("current")
_PsModulePorts_Type = Integer32
_PsModulePorts_Object = MibTableColumn
psModulePorts = _PsModulePorts_Object(
    (1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 19),
    _PsModulePorts_Type()
)
psModulePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psModulePorts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADVANTECH-COMMON-MIB",
    **{"advantech": advantech,
       "advantechCommonMIB": advantechCommonMIB,
       "atSystem": atSystem,
       "sysModuleID": sysModuleID,
       "sysDeviceName": sysDeviceName,
       "sysDescr": sysDescr,
       "sysImageVersion": sysImageVersion,
       "sysReleaseDate": sysReleaseDate,
       "sysFirstBootTime": sysFirstBootTime,
       "sysBootTime": sysBootTime,
       "sysBootCount": sysBootCount,
       "atMgmt": atMgmt,
       "snmpTrapSrvObj": snmpTrapSrvObj,
       "snmpTrapSrvNumber": snmpTrapSrvNumber,
       "snmpTrapSrvTable": snmpTrapSrvTable,
       "snmpTrapSrvEntry": snmpTrapSrvEntry,
       "snmpTrapSrvIndex": snmpTrapSrvIndex,
       "snmpTrapSrvIP": snmpTrapSrvIP,
       "snmpTrapSrvPort": snmpTrapSrvPort,
       "snmpTrapSrvAuthentication": snmpTrapSrvAuthentication,
       "snmpTrapSrvCommunity": snmpTrapSrvCommunity,
       "snmpTrapVersion": snmpTrapVersion,
       "atPciConfig": atPciConfig,
       "pciConfigObj": pciConfigObj,
       "psNumber": psNumber,
       "pciSlotTable": pciSlotTable,
       "pciSlotEntry": pciSlotEntry,
       "psIndex": psIndex,
       "psBusIndex": psBusIndex,
       "psDeviceIndex": psDeviceIndex,
       "psFunctionIndex": psFunctionIndex,
       "psDisplayName": psDisplayName,
       "psDescr": psDescr,
       "psVendorID": psVendorID,
       "psDeviceID": psDeviceID,
       "psSubsysVendorID": psSubsysVendorID,
       "psSubsysDeviceID": psSubsysDeviceID,
       "psClassCode": psClassCode,
       "psManufacturer": psManufacturer,
       "psLocation": psLocation,
       "psBaseAddress": psBaseAddress,
       "psLength": psLength,
       "psIRQ": psIRQ,
       "psState": psState,
       "psModuleType": psModuleType,
       "psModulePorts": psModulePorts}
)
