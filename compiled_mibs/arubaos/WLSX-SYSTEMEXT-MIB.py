# SNMP MIB module (WLSX-SYSTEMEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos\WLSX-SYSTEMEXT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:55 2025
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

(ArubaActiveState,
 ArubaCardType,
 ArubaSwitchRole) = mibBuilder.importSymbols(
    "ARUBA-TC",
    "ArubaActiveState",
    "ArubaCardType",
    "ArubaSwitchRole")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxSystemExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wlsxSystemExtMIB.setRevisions(
        ("2020-08-14 17:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxSystemExtGroup_ObjectIdentity = ObjectIdentity
wlsxSystemExtGroup = _WlsxSystemExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1)
)
_WlsxSysExtSwitchIp_Type = IpAddress
_WlsxSysExtSwitchIp_Object = MibScalar
wlsxSysExtSwitchIp = _WlsxSysExtSwitchIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 1),
    _WlsxSysExtSwitchIp_Type()
)
wlsxSysExtSwitchIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSwitchIp.setStatus("current")


class _WlsxSysExtHostname_Type(DisplayString):
    """Custom type wlsxSysExtHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlsxSysExtHostname_Type.__name__ = "DisplayString"
_WlsxSysExtHostname_Object = MibScalar
wlsxSysExtHostname = _WlsxSysExtHostname_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 2),
    _WlsxSysExtHostname_Type()
)
wlsxSysExtHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtHostname.setStatus("current")


class _WlsxSysExtModelName_Type(DisplayString):
    """Custom type wlsxSysExtModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlsxSysExtModelName_Type.__name__ = "DisplayString"
_WlsxSysExtModelName_Object = MibScalar
wlsxSysExtModelName = _WlsxSysExtModelName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 3),
    _WlsxSysExtModelName_Type()
)
wlsxSysExtModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtModelName.setStatus("current")
_WlsxSysExtSwitchRole_Type = ArubaSwitchRole
_WlsxSysExtSwitchRole_Object = MibScalar
wlsxSysExtSwitchRole = _WlsxSysExtSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 4),
    _WlsxSysExtSwitchRole_Type()
)
wlsxSysExtSwitchRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSwitchRole.setStatus("current")
_WlsxSysExtSwitchMasterIp_Type = IpAddress
_WlsxSysExtSwitchMasterIp_Object = MibScalar
wlsxSysExtSwitchMasterIp = _WlsxSysExtSwitchMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 5),
    _WlsxSysExtSwitchMasterIp_Type()
)
wlsxSysExtSwitchMasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSwitchMasterIp.setStatus("current")


class _WlsxSysExtSwitchDate_Type(DisplayString):
    """Custom type wlsxSysExtSwitchDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxSysExtSwitchDate_Type.__name__ = "DisplayString"
_WlsxSysExtSwitchDate_Object = MibScalar
wlsxSysExtSwitchDate = _WlsxSysExtSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 6),
    _WlsxSysExtSwitchDate_Type()
)
wlsxSysExtSwitchDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxSysExtSwitchDate.setStatus("current")
_WlsxSysExtSwitchBaseMacaddress_Type = MacAddress
_WlsxSysExtSwitchBaseMacaddress_Object = MibScalar
wlsxSysExtSwitchBaseMacaddress = _WlsxSysExtSwitchBaseMacaddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 7),
    _WlsxSysExtSwitchBaseMacaddress_Type()
)
wlsxSysExtSwitchBaseMacaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSwitchBaseMacaddress.setStatus("current")


class _WlsxSysExtFanTrayAssemblyNumber_Type(DisplayString):
    """Custom type wlsxSysExtFanTrayAssemblyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxSysExtFanTrayAssemblyNumber_Type.__name__ = "DisplayString"
_WlsxSysExtFanTrayAssemblyNumber_Object = MibScalar
wlsxSysExtFanTrayAssemblyNumber = _WlsxSysExtFanTrayAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 8),
    _WlsxSysExtFanTrayAssemblyNumber_Type()
)
wlsxSysExtFanTrayAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtFanTrayAssemblyNumber.setStatus("current")


class _WlsxSysExtFanTraySerialNumber_Type(DisplayString):
    """Custom type wlsxSysExtFanTraySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxSysExtFanTraySerialNumber_Type.__name__ = "DisplayString"
_WlsxSysExtFanTraySerialNumber_Object = MibScalar
wlsxSysExtFanTraySerialNumber = _WlsxSysExtFanTraySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 9),
    _WlsxSysExtFanTraySerialNumber_Type()
)
wlsxSysExtFanTraySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtFanTraySerialNumber.setStatus("current")


class _WlsxSysExtInternalTemparature_Type(DisplayString):
    """Custom type wlsxSysExtInternalTemparature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxSysExtInternalTemparature_Type.__name__ = "DisplayString"
_WlsxSysExtInternalTemparature_Object = MibScalar
wlsxSysExtInternalTemparature = _WlsxSysExtInternalTemparature_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 10),
    _WlsxSysExtInternalTemparature_Type()
)
wlsxSysExtInternalTemparature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtInternalTemparature.setStatus("current")


class _WlsxSysExtLicenseSerialNumber_Type(DisplayString):
    """Custom type wlsxSysExtLicenseSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WlsxSysExtLicenseSerialNumber_Type.__name__ = "DisplayString"
_WlsxSysExtLicenseSerialNumber_Object = MibScalar
wlsxSysExtLicenseSerialNumber = _WlsxSysExtLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 11),
    _WlsxSysExtLicenseSerialNumber_Type()
)
wlsxSysExtLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtLicenseSerialNumber.setStatus("current")
_WlsxSysExtSwitchLicenseCount_Type = Integer32
_WlsxSysExtSwitchLicenseCount_Object = MibScalar
wlsxSysExtSwitchLicenseCount = _WlsxSysExtSwitchLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 12),
    _WlsxSysExtSwitchLicenseCount_Type()
)
wlsxSysExtSwitchLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSwitchLicenseCount.setStatus("current")
_WlsxSysExtProcessorTable_Object = MibTable
wlsxSysExtProcessorTable = _WlsxSysExtProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13)
)
if mibBuilder.loadTexts:
    wlsxSysExtProcessorTable.setStatus("current")
_WlsxSysExtProcessorEntry_Object = MibTableRow
wlsxSysExtProcessorEntry = _WlsxSysExtProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1)
)
wlsxSysExtProcessorEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtProcessorID"),
)
if mibBuilder.loadTexts:
    wlsxSysExtProcessorEntry.setStatus("current")
_SysExtProcessorID_Type = Integer32
_SysExtProcessorID_Object = MibTableColumn
sysExtProcessorID = _SysExtProcessorID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 1),
    _SysExtProcessorID_Type()
)
sysExtProcessorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtProcessorID.setStatus("current")


class _SysExtProcessorDescr_Type(DisplayString):
    """Custom type sysExtProcessorDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtProcessorDescr_Type.__name__ = "DisplayString"
_SysExtProcessorDescr_Object = MibTableColumn
sysExtProcessorDescr = _SysExtProcessorDescr_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 2),
    _SysExtProcessorDescr_Type()
)
sysExtProcessorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtProcessorDescr.setStatus("current")


class _SysExtProcessorLoad_Type(Integer32):
    """Custom type sysExtProcessorLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysExtProcessorLoad_Type.__name__ = "Integer32"
_SysExtProcessorLoad_Object = MibTableColumn
sysExtProcessorLoad = _SysExtProcessorLoad_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 13, 1, 3),
    _SysExtProcessorLoad_Type()
)
sysExtProcessorLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtProcessorLoad.setStatus("current")
_WlsxSysExtStorageTable_Object = MibTable
wlsxSysExtStorageTable = _WlsxSysExtStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14)
)
if mibBuilder.loadTexts:
    wlsxSysExtStorageTable.setStatus("current")
_WlsxSysExtStorageEntry_Object = MibTableRow
wlsxSysExtStorageEntry = _WlsxSysExtStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1)
)
wlsxSysExtStorageEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtStorageIndex"),
)
if mibBuilder.loadTexts:
    wlsxSysExtStorageEntry.setStatus("current")
_SysExtStorageIndex_Type = Integer32
_SysExtStorageIndex_Object = MibTableColumn
sysExtStorageIndex = _SysExtStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 1),
    _SysExtStorageIndex_Type()
)
sysExtStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtStorageIndex.setStatus("current")


class _SysExtStorageType_Type(Integer32):
    """Custom type sysExtStorageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ram", 1),
          ("flashMemory", 2))
    )


_SysExtStorageType_Type.__name__ = "Integer32"
_SysExtStorageType_Object = MibTableColumn
sysExtStorageType = _SysExtStorageType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 2),
    _SysExtStorageType_Type()
)
sysExtStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtStorageType.setStatus("current")
_SysExtStorageSize_Type = Integer32
_SysExtStorageSize_Object = MibTableColumn
sysExtStorageSize = _SysExtStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 3),
    _SysExtStorageSize_Type()
)
sysExtStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtStorageSize.setStatus("current")
_SysExtStorageUsed_Type = Integer32
_SysExtStorageUsed_Object = MibTableColumn
sysExtStorageUsed = _SysExtStorageUsed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 4),
    _SysExtStorageUsed_Type()
)
sysExtStorageUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtStorageUsed.setStatus("current")


class _SysExtStorageName_Type(DisplayString):
    """Custom type sysExtStorageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtStorageName_Type.__name__ = "DisplayString"
_SysExtStorageName_Object = MibTableColumn
sysExtStorageName = _SysExtStorageName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 14, 1, 5),
    _SysExtStorageName_Type()
)
sysExtStorageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtStorageName.setStatus("current")
_WlsxSysExtMemoryTable_Object = MibTable
wlsxSysExtMemoryTable = _WlsxSysExtMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15)
)
if mibBuilder.loadTexts:
    wlsxSysExtMemoryTable.setStatus("current")
_WlsxSysExtMemoryEntry_Object = MibTableRow
wlsxSysExtMemoryEntry = _WlsxSysExtMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1)
)
wlsxSysExtMemoryEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtMemoryIndex"),
)
if mibBuilder.loadTexts:
    wlsxSysExtMemoryEntry.setStatus("current")
_SysExtMemoryIndex_Type = Integer32
_SysExtMemoryIndex_Object = MibTableColumn
sysExtMemoryIndex = _SysExtMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 1),
    _SysExtMemoryIndex_Type()
)
sysExtMemoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtMemoryIndex.setStatus("current")
_SysExtMemorySize_Type = Integer32
_SysExtMemorySize_Object = MibTableColumn
sysExtMemorySize = _SysExtMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 2),
    _SysExtMemorySize_Type()
)
sysExtMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtMemorySize.setStatus("current")
_SysExtMemoryUsed_Type = Integer32
_SysExtMemoryUsed_Object = MibTableColumn
sysExtMemoryUsed = _SysExtMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 3),
    _SysExtMemoryUsed_Type()
)
sysExtMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtMemoryUsed.setStatus("current")
_SysExtMemoryFree_Type = Integer32
_SysExtMemoryFree_Object = MibTableColumn
sysExtMemoryFree = _SysExtMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 15, 1, 4),
    _SysExtMemoryFree_Type()
)
sysExtMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtMemoryFree.setStatus("current")
_WlsxSysExtCardTable_Object = MibTable
wlsxSysExtCardTable = _WlsxSysExtCardTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16)
)
if mibBuilder.loadTexts:
    wlsxSysExtCardTable.setStatus("current")
_WlsxSysExtCardEntry_Object = MibTableRow
wlsxSysExtCardEntry = _WlsxSysExtCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1)
)
wlsxSysExtCardEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtCardSlot"),
)
if mibBuilder.loadTexts:
    wlsxSysExtCardEntry.setStatus("current")
_SysExtCardSlot_Type = Integer32
_SysExtCardSlot_Object = MibTableColumn
sysExtCardSlot = _SysExtCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 1),
    _SysExtCardSlot_Type()
)
sysExtCardSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtCardSlot.setStatus("current")
_SysExtCardType_Type = ArubaCardType
_SysExtCardType_Object = MibTableColumn
sysExtCardType = _SysExtCardType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 2),
    _SysExtCardType_Type()
)
sysExtCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardType.setStatus("current")
_SysExtCardNumOfPorts_Type = Integer32
_SysExtCardNumOfPorts_Object = MibTableColumn
sysExtCardNumOfPorts = _SysExtCardNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 3),
    _SysExtCardNumOfPorts_Type()
)
sysExtCardNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardNumOfPorts.setStatus("current")
_SysExtCardNumOfFastethernetPorts_Type = Integer32
_SysExtCardNumOfFastethernetPorts_Object = MibTableColumn
sysExtCardNumOfFastethernetPorts = _SysExtCardNumOfFastethernetPorts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 4),
    _SysExtCardNumOfFastethernetPorts_Type()
)
sysExtCardNumOfFastethernetPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardNumOfFastethernetPorts.setStatus("current")
_SysExtCardNumOfGigPorts_Type = Integer32
_SysExtCardNumOfGigPorts_Object = MibTableColumn
sysExtCardNumOfGigPorts = _SysExtCardNumOfGigPorts_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 5),
    _SysExtCardNumOfGigPorts_Type()
)
sysExtCardNumOfGigPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardNumOfGigPorts.setStatus("current")


class _SysExtCardSerialNo_Type(DisplayString):
    """Custom type sysExtCardSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtCardSerialNo_Type.__name__ = "DisplayString"
_SysExtCardSerialNo_Object = MibTableColumn
sysExtCardSerialNo = _SysExtCardSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 6),
    _SysExtCardSerialNo_Type()
)
sysExtCardSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardSerialNo.setStatus("current")


class _SysExtCardAssemblyNo_Type(DisplayString):
    """Custom type sysExtCardAssemblyNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtCardAssemblyNo_Type.__name__ = "DisplayString"
_SysExtCardAssemblyNo_Object = MibTableColumn
sysExtCardAssemblyNo = _SysExtCardAssemblyNo_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 7),
    _SysExtCardAssemblyNo_Type()
)
sysExtCardAssemblyNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardAssemblyNo.setStatus("current")
_SysExtCardManufacturingDate_Type = DisplayString
_SysExtCardManufacturingDate_Object = MibTableColumn
sysExtCardManufacturingDate = _SysExtCardManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 8),
    _SysExtCardManufacturingDate_Type()
)
sysExtCardManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardManufacturingDate.setStatus("current")


class _SysExtCardHwRevision_Type(DisplayString):
    """Custom type sysExtCardHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtCardHwRevision_Type.__name__ = "DisplayString"
_SysExtCardHwRevision_Object = MibTableColumn
sysExtCardHwRevision = _SysExtCardHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 9),
    _SysExtCardHwRevision_Type()
)
sysExtCardHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardHwRevision.setStatus("current")


class _SysExtCardFpgaRevision_Type(DisplayString):
    """Custom type sysExtCardFpgaRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtCardFpgaRevision_Type.__name__ = "DisplayString"
_SysExtCardFpgaRevision_Object = MibTableColumn
sysExtCardFpgaRevision = _SysExtCardFpgaRevision_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 10),
    _SysExtCardFpgaRevision_Type()
)
sysExtCardFpgaRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardFpgaRevision.setStatus("current")


class _SysExtCardSwitchChip_Type(DisplayString):
    """Custom type sysExtCardSwitchChip based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtCardSwitchChip_Type.__name__ = "DisplayString"
_SysExtCardSwitchChip_Object = MibTableColumn
sysExtCardSwitchChip = _SysExtCardSwitchChip_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 11),
    _SysExtCardSwitchChip_Type()
)
sysExtCardSwitchChip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardSwitchChip.setStatus("current")
_SysExtCardStatus_Type = ArubaActiveState
_SysExtCardStatus_Object = MibTableColumn
sysExtCardStatus = _SysExtCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 12),
    _SysExtCardStatus_Type()
)
sysExtCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardStatus.setStatus("current")
_SysExtCardUserSlot_Type = Integer32
_SysExtCardUserSlot_Object = MibTableColumn
sysExtCardUserSlot = _SysExtCardUserSlot_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 13),
    _SysExtCardUserSlot_Type()
)
sysExtCardUserSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardUserSlot.setStatus("current")


class _SysExtCardServiceTag_Type(DisplayString):
    """Custom type sysExtCardServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtCardServiceTag_Type.__name__ = "DisplayString"
_SysExtCardServiceTag_Object = MibTableColumn
sysExtCardServiceTag = _SysExtCardServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 14),
    _SysExtCardServiceTag_Type()
)
sysExtCardServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardServiceTag.setStatus("current")


class _SysExtCardPartNumber_Type(DisplayString):
    """Custom type sysExtCardPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtCardPartNumber_Type.__name__ = "DisplayString"
_SysExtCardPartNumber_Object = MibTableColumn
sysExtCardPartNumber = _SysExtCardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 16, 1, 15),
    _SysExtCardPartNumber_Type()
)
sysExtCardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtCardPartNumber.setStatus("current")
_WlsxSysExtFanTable_Object = MibTable
wlsxSysExtFanTable = _WlsxSysExtFanTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17)
)
if mibBuilder.loadTexts:
    wlsxSysExtFanTable.setStatus("current")
_WlsxSysExtFanEntry_Object = MibTableRow
wlsxSysExtFanEntry = _WlsxSysExtFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1)
)
wlsxSysExtFanEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtFanIndex"),
)
if mibBuilder.loadTexts:
    wlsxSysExtFanEntry.setStatus("current")
_SysExtFanIndex_Type = Integer32
_SysExtFanIndex_Object = MibTableColumn
sysExtFanIndex = _SysExtFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1, 1),
    _SysExtFanIndex_Type()
)
sysExtFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtFanIndex.setStatus("current")
_SysExtFanStatus_Type = ArubaActiveState
_SysExtFanStatus_Object = MibTableColumn
sysExtFanStatus = _SysExtFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 17, 1, 2),
    _SysExtFanStatus_Type()
)
sysExtFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtFanStatus.setStatus("current")
_WlsxSysExtPowerSupplyTable_Object = MibTable
wlsxSysExtPowerSupplyTable = _WlsxSysExtPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18)
)
if mibBuilder.loadTexts:
    wlsxSysExtPowerSupplyTable.setStatus("current")
_WlsxSysExtPowerSupplyEntry_Object = MibTableRow
wlsxSysExtPowerSupplyEntry = _WlsxSysExtPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1)
)
wlsxSysExtPowerSupplyEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    wlsxSysExtPowerSupplyEntry.setStatus("current")
_SysExtPowerSupplyIndex_Type = Integer32
_SysExtPowerSupplyIndex_Object = MibTableColumn
sysExtPowerSupplyIndex = _SysExtPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1, 1),
    _SysExtPowerSupplyIndex_Type()
)
sysExtPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtPowerSupplyIndex.setStatus("current")
_SysExtPowerSupplyStatus_Type = ArubaActiveState
_SysExtPowerSupplyStatus_Object = MibTableColumn
sysExtPowerSupplyStatus = _SysExtPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 18, 1, 2),
    _SysExtPowerSupplyStatus_Type()
)
sysExtPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtPowerSupplyStatus.setStatus("current")
_WlsxSysExtSwitchListTable_Object = MibTable
wlsxSysExtSwitchListTable = _WlsxSysExtSwitchListTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    wlsxSysExtSwitchListTable.setStatus("current")
_WlsxSysExtSwitchListEntry_Object = MibTableRow
wlsxSysExtSwitchListEntry = _WlsxSysExtSwitchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1)
)
wlsxSysExtSwitchListEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtSwitchIPAddress"),
)
if mibBuilder.loadTexts:
    wlsxSysExtSwitchListEntry.setStatus("current")
_SysExtSwitchIPAddress_Type = IpAddress
_SysExtSwitchIPAddress_Object = MibTableColumn
sysExtSwitchIPAddress = _SysExtSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 1),
    _SysExtSwitchIPAddress_Type()
)
sysExtSwitchIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtSwitchIPAddress.setStatus("current")
_SysExtSwitchRole_Type = ArubaSwitchRole
_SysExtSwitchRole_Object = MibTableColumn
sysExtSwitchRole = _SysExtSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 2),
    _SysExtSwitchRole_Type()
)
sysExtSwitchRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtSwitchRole.setStatus("current")


class _SysExtSwitchLocation_Type(DisplayString):
    """Custom type sysExtSwitchLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtSwitchLocation_Type.__name__ = "DisplayString"
_SysExtSwitchLocation_Object = MibTableColumn
sysExtSwitchLocation = _SysExtSwitchLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 3),
    _SysExtSwitchLocation_Type()
)
sysExtSwitchLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtSwitchLocation.setStatus("current")


class _SysExtSwitchSWVersion_Type(DisplayString):
    """Custom type sysExtSwitchSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtSwitchSWVersion_Type.__name__ = "DisplayString"
_SysExtSwitchSWVersion_Object = MibTableColumn
sysExtSwitchSWVersion = _SysExtSwitchSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 4),
    _SysExtSwitchSWVersion_Type()
)
sysExtSwitchSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtSwitchSWVersion.setStatus("current")
_SysExtSwitchStatus_Type = ArubaActiveState
_SysExtSwitchStatus_Object = MibTableColumn
sysExtSwitchStatus = _SysExtSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 5),
    _SysExtSwitchStatus_Type()
)
sysExtSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtSwitchStatus.setStatus("current")


class _SysExtSwitchName_Type(DisplayString):
    """Custom type sysExtSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SysExtSwitchName_Type.__name__ = "DisplayString"
_SysExtSwitchName_Object = MibTableColumn
sysExtSwitchName = _SysExtSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 6),
    _SysExtSwitchName_Type()
)
sysExtSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtSwitchName.setStatus("current")


class _SysExtSwitchSerNo_Type(DisplayString):
    """Custom type sysExtSwitchSerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysExtSwitchSerNo_Type.__name__ = "DisplayString"
_SysExtSwitchSerNo_Object = MibTableColumn
sysExtSwitchSerNo = _SysExtSwitchSerNo_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 19, 1, 7),
    _SysExtSwitchSerNo_Type()
)
sysExtSwitchSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtSwitchSerNo.setStatus("current")
_WlsxSysExtSwitchLicenseTable_Object = MibTable
wlsxSysExtSwitchLicenseTable = _WlsxSysExtSwitchLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20)
)
if mibBuilder.loadTexts:
    wlsxSysExtSwitchLicenseTable.setStatus("current")
_WlsxSysExtLicenseEntry_Object = MibTableRow
wlsxSysExtLicenseEntry = _WlsxSysExtLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1)
)
wlsxSysExtLicenseEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtLicenseIndex"),
)
if mibBuilder.loadTexts:
    wlsxSysExtLicenseEntry.setStatus("current")
_SysExtLicenseIndex_Type = Integer32
_SysExtLicenseIndex_Object = MibTableColumn
sysExtLicenseIndex = _SysExtLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 1),
    _SysExtLicenseIndex_Type()
)
sysExtLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtLicenseIndex.setStatus("current")
_SysExtLicenseKey_Type = DisplayString
_SysExtLicenseKey_Object = MibTableColumn
sysExtLicenseKey = _SysExtLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 2),
    _SysExtLicenseKey_Type()
)
sysExtLicenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtLicenseKey.setStatus("current")
_SysExtLicenseInstalled_Type = DisplayString
_SysExtLicenseInstalled_Object = MibTableColumn
sysExtLicenseInstalled = _SysExtLicenseInstalled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 3),
    _SysExtLicenseInstalled_Type()
)
sysExtLicenseInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtLicenseInstalled.setStatus("current")
_SysExtLicenseExpires_Type = DisplayString
_SysExtLicenseExpires_Object = MibTableColumn
sysExtLicenseExpires = _SysExtLicenseExpires_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 4),
    _SysExtLicenseExpires_Type()
)
sysExtLicenseExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtLicenseExpires.setStatus("current")
_SysExtLicenseFlags_Type = DisplayString
_SysExtLicenseFlags_Object = MibTableColumn
sysExtLicenseFlags = _SysExtLicenseFlags_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 5),
    _SysExtLicenseFlags_Type()
)
sysExtLicenseFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtLicenseFlags.setStatus("current")
_SysExtLicenseService_Type = DisplayString
_SysExtLicenseService_Object = MibTableColumn
sysExtLicenseService = _SysExtLicenseService_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 20, 1, 6),
    _SysExtLicenseService_Type()
)
sysExtLicenseService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtLicenseService.setStatus("current")
_WlsxSysExtMMSCompatLevel_Type = Integer32
_WlsxSysExtMMSCompatLevel_Object = MibScalar
wlsxSysExtMMSCompatLevel = _WlsxSysExtMMSCompatLevel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 21),
    _WlsxSysExtMMSCompatLevel_Type()
)
wlsxSysExtMMSCompatLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtMMSCompatLevel.setStatus("current")
_WlsxSysExtMMSConfigID_Type = Integer32
_WlsxSysExtMMSConfigID_Object = MibScalar
wlsxSysExtMMSConfigID = _WlsxSysExtMMSConfigID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 22),
    _WlsxSysExtMMSConfigID_Type()
)
wlsxSysExtMMSConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtMMSConfigID.setStatus("current")
_WlsxSysExtControllerConfigID_Type = Integer32
_WlsxSysExtControllerConfigID_Object = MibScalar
wlsxSysExtControllerConfigID = _WlsxSysExtControllerConfigID_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 23),
    _WlsxSysExtControllerConfigID_Type()
)
wlsxSysExtControllerConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtControllerConfigID.setStatus("current")
_WlsxSysExtIsMMSConfigUpdateEnabled_Type = TruthValue
_WlsxSysExtIsMMSConfigUpdateEnabled_Object = MibScalar
wlsxSysExtIsMMSConfigUpdateEnabled = _WlsxSysExtIsMMSConfigUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 24),
    _WlsxSysExtIsMMSConfigUpdateEnabled_Type()
)
wlsxSysExtIsMMSConfigUpdateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxSysExtIsMMSConfigUpdateEnabled.setStatus("current")


class _WlsxSysExtSwitchLastReload_Type(DisplayString):
    """Custom type wlsxSysExtSwitchLastReload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WlsxSysExtSwitchLastReload_Type.__name__ = "DisplayString"
_WlsxSysExtSwitchLastReload_Object = MibScalar
wlsxSysExtSwitchLastReload = _WlsxSysExtSwitchLastReload_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 25),
    _WlsxSysExtSwitchLastReload_Type()
)
wlsxSysExtSwitchLastReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSwitchLastReload.setStatus("current")
_WlsxSysExtLastStatsReset_Type = TimeTicks
_WlsxSysExtLastStatsReset_Object = MibScalar
wlsxSysExtLastStatsReset = _WlsxSysExtLastStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 26),
    _WlsxSysExtLastStatsReset_Type()
)
wlsxSysExtLastStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtLastStatsReset.setStatus("current")


class _WlsxSysExtHwVersion_Type(DisplayString):
    """Custom type wlsxSysExtHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlsxSysExtHwVersion_Type.__name__ = "DisplayString"
_WlsxSysExtHwVersion_Object = MibScalar
wlsxSysExtHwVersion = _WlsxSysExtHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 27),
    _WlsxSysExtHwVersion_Type()
)
wlsxSysExtHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtHwVersion.setStatus("current")


class _WlsxSysExtSwVersion_Type(DisplayString):
    """Custom type wlsxSysExtSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlsxSysExtSwVersion_Type.__name__ = "DisplayString"
_WlsxSysExtSwVersion_Object = MibScalar
wlsxSysExtSwVersion = _WlsxSysExtSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 28),
    _WlsxSysExtSwVersion_Type()
)
wlsxSysExtSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSwVersion.setStatus("current")


class _WlsxSysExtSerialNumber_Type(DisplayString):
    """Custom type wlsxSysExtSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlsxSysExtSerialNumber_Type.__name__ = "DisplayString"
_WlsxSysExtSerialNumber_Object = MibScalar
wlsxSysExtSerialNumber = _WlsxSysExtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 29),
    _WlsxSysExtSerialNumber_Type()
)
wlsxSysExtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSerialNumber.setStatus("current")
_WlsxSysExtCpuUsedPercent_Type = Gauge32
_WlsxSysExtCpuUsedPercent_Object = MibScalar
wlsxSysExtCpuUsedPercent = _WlsxSysExtCpuUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 30),
    _WlsxSysExtCpuUsedPercent_Type()
)
wlsxSysExtCpuUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtCpuUsedPercent.setStatus("current")
_WlsxSysExtMemoryUsedPercent_Type = Gauge32
_WlsxSysExtMemoryUsedPercent_Object = MibScalar
wlsxSysExtMemoryUsedPercent = _WlsxSysExtMemoryUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 31),
    _WlsxSysExtMemoryUsedPercent_Type()
)
wlsxSysExtMemoryUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtMemoryUsedPercent.setStatus("current")
_WlsxSysExtPacketLossPercent_Type = Integer32
_WlsxSysExtPacketLossPercent_Object = MibScalar
wlsxSysExtPacketLossPercent = _WlsxSysExtPacketLossPercent_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 32),
    _WlsxSysExtPacketLossPercent_Type()
)
wlsxSysExtPacketLossPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtPacketLossPercent.setStatus("current")
_WlsxSysExtPoweredViaPoe_Type = Integer32
_WlsxSysExtPoweredViaPoe_Object = MibScalar
wlsxSysExtPoweredViaPoe = _WlsxSysExtPoweredViaPoe_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 33),
    _WlsxSysExtPoweredViaPoe_Type()
)
wlsxSysExtPoweredViaPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtPoweredViaPoe.setStatus("current")


class _WlsxSysVMHostType_Type(DisplayString):
    """Custom type wlsxSysVMHostType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlsxSysVMHostType_Type.__name__ = "DisplayString"
_WlsxSysVMHostType_Object = MibScalar
wlsxSysVMHostType = _WlsxSysVMHostType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 34),
    _WlsxSysVMHostType_Type()
)
wlsxSysVMHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysVMHostType.setStatus("current")


class _WlsxSysExtProcessorModel_Type(DisplayString):
    """Custom type wlsxSysExtProcessorModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_WlsxSysExtProcessorModel_Type.__name__ = "DisplayString"
_WlsxSysExtProcessorModel_Object = MibScalar
wlsxSysExtProcessorModel = _WlsxSysExtProcessorModel_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 35),
    _WlsxSysExtProcessorModel_Type()
)
wlsxSysExtProcessorModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtProcessorModel.setStatus("current")
_WlsxSysExtTotalCpu_Type = Integer32
_WlsxSysExtTotalCpu_Object = MibScalar
wlsxSysExtTotalCpu = _WlsxSysExtTotalCpu_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 36),
    _WlsxSysExtTotalCpu_Type()
)
wlsxSysExtTotalCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtTotalCpu.setStatus("current")
_WlsxSysExtTotalSocket_Type = Integer32
_WlsxSysExtTotalSocket_Object = MibScalar
wlsxSysExtTotalSocket = _WlsxSysExtTotalSocket_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 37),
    _WlsxSysExtTotalSocket_Type()
)
wlsxSysExtTotalSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtTotalSocket.setStatus("current")
_WlsxAuthFailIp_Type = IpAddress
_WlsxAuthFailIp_Object = MibScalar
wlsxAuthFailIp = _WlsxAuthFailIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 38),
    _WlsxAuthFailIp_Type()
)
wlsxAuthFailIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxAuthFailIp.setStatus("current")
_WlsxSysExtDiskSize_Type = Integer32
_WlsxSysExtDiskSize_Object = MibScalar
wlsxSysExtDiskSize = _WlsxSysExtDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 39),
    _WlsxSysExtDiskSize_Type()
)
wlsxSysExtDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtDiskSize.setStatus("current")
_WlsxNSysExtSwitchListTable_Object = MibTable
wlsxNSysExtSwitchListTable = _WlsxNSysExtSwitchListTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40)
)
if mibBuilder.loadTexts:
    wlsxNSysExtSwitchListTable.setStatus("current")
_WlsxNSysExtSwitchListEntry_Object = MibTableRow
wlsxNSysExtSwitchListEntry = _WlsxNSysExtSwitchListEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1)
)
wlsxNSysExtSwitchListEntry.setIndexNames(
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtNSwitchIPAddressType"),
    (0, "WLSX-SYSTEMEXT-MIB", "sysExtNSwitchIPAddress"),
)
if mibBuilder.loadTexts:
    wlsxNSysExtSwitchListEntry.setStatus("current")
_SysExtNSwitchIPAddressType_Type = Integer32
_SysExtNSwitchIPAddressType_Object = MibTableColumn
sysExtNSwitchIPAddressType = _SysExtNSwitchIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1, 1),
    _SysExtNSwitchIPAddressType_Type()
)
sysExtNSwitchIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtNSwitchIPAddressType.setStatus("current")


class _SysExtNSwitchIPAddress_Type(DisplayString):
    """Custom type sysExtNSwitchIPAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_SysExtNSwitchIPAddress_Type.__name__ = "DisplayString"
_SysExtNSwitchIPAddress_Object = MibTableColumn
sysExtNSwitchIPAddress = _SysExtNSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1, 2),
    _SysExtNSwitchIPAddress_Type()
)
sysExtNSwitchIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysExtNSwitchIPAddress.setStatus("current")
_SysExtNSwitchRole_Type = ArubaSwitchRole
_SysExtNSwitchRole_Object = MibTableColumn
sysExtNSwitchRole = _SysExtNSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1, 3),
    _SysExtNSwitchRole_Type()
)
sysExtNSwitchRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtNSwitchRole.setStatus("current")


class _SysExtNSwitchLocation_Type(DisplayString):
    """Custom type sysExtNSwitchLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtNSwitchLocation_Type.__name__ = "DisplayString"
_SysExtNSwitchLocation_Object = MibTableColumn
sysExtNSwitchLocation = _SysExtNSwitchLocation_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1, 4),
    _SysExtNSwitchLocation_Type()
)
sysExtNSwitchLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtNSwitchLocation.setStatus("current")


class _SysExtNSwitchSWVersion_Type(DisplayString):
    """Custom type sysExtNSwitchSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysExtNSwitchSWVersion_Type.__name__ = "DisplayString"
_SysExtNSwitchSWVersion_Object = MibTableColumn
sysExtNSwitchSWVersion = _SysExtNSwitchSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1, 5),
    _SysExtNSwitchSWVersion_Type()
)
sysExtNSwitchSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtNSwitchSWVersion.setStatus("current")
_SysExtNSwitchStatus_Type = ArubaActiveState
_SysExtNSwitchStatus_Object = MibTableColumn
sysExtNSwitchStatus = _SysExtNSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1, 6),
    _SysExtNSwitchStatus_Type()
)
sysExtNSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtNSwitchStatus.setStatus("current")


class _SysExtNSwitchName_Type(DisplayString):
    """Custom type sysExtNSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SysExtNSwitchName_Type.__name__ = "DisplayString"
_SysExtNSwitchName_Object = MibTableColumn
sysExtNSwitchName = _SysExtNSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1, 7),
    _SysExtNSwitchName_Type()
)
sysExtNSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtNSwitchName.setStatus("current")


class _SysExtNSwitchSerNo_Type(DisplayString):
    """Custom type sysExtNSwitchSerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysExtNSwitchSerNo_Type.__name__ = "DisplayString"
_SysExtNSwitchSerNo_Object = MibTableColumn
sysExtNSwitchSerNo = _SysExtNSwitchSerNo_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 1, 40, 1, 8),
    _SysExtNSwitchSerNo_Type()
)
sysExtNSwitchSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysExtNSwitchSerNo.setStatus("current")
_WlsxSystemExtTableGenNumberGroup_ObjectIdentity = ObjectIdentity
wlsxSystemExtTableGenNumberGroup = _WlsxSystemExtTableGenNumberGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2)
)
_WlsxSysExtUserTableGenNumber_Type = Integer32
_WlsxSysExtUserTableGenNumber_Object = MibScalar
wlsxSysExtUserTableGenNumber = _WlsxSysExtUserTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 1),
    _WlsxSysExtUserTableGenNumber_Type()
)
wlsxSysExtUserTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtUserTableGenNumber.setStatus("deprecated")
_WlsxSysExtAPBssidTableGenNumber_Type = Integer32
_WlsxSysExtAPBssidTableGenNumber_Object = MibScalar
wlsxSysExtAPBssidTableGenNumber = _WlsxSysExtAPBssidTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 2),
    _WlsxSysExtAPBssidTableGenNumber_Type()
)
wlsxSysExtAPBssidTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtAPBssidTableGenNumber.setStatus("deprecated")
_WlsxSysExtAPRadioTableGenNumber_Type = Integer32
_WlsxSysExtAPRadioTableGenNumber_Object = MibScalar
wlsxSysExtAPRadioTableGenNumber = _WlsxSysExtAPRadioTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 3),
    _WlsxSysExtAPRadioTableGenNumber_Type()
)
wlsxSysExtAPRadioTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtAPRadioTableGenNumber.setStatus("deprecated")
_WlsxSysExtAPTableGenNumber_Type = Integer32
_WlsxSysExtAPTableGenNumber_Object = MibScalar
wlsxSysExtAPTableGenNumber = _WlsxSysExtAPTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 4),
    _WlsxSysExtAPTableGenNumber_Type()
)
wlsxSysExtAPTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtAPTableGenNumber.setStatus("deprecated")
_WlsxSysExtSwitchListTableGenNumber_Type = Integer32
_WlsxSysExtSwitchListTableGenNumber_Object = MibScalar
wlsxSysExtSwitchListTableGenNumber = _WlsxSysExtSwitchListTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 5),
    _WlsxSysExtSwitchListTableGenNumber_Type()
)
wlsxSysExtSwitchListTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtSwitchListTableGenNumber.setStatus("deprecated")
_WlsxSysExtPortTableGenNumber_Type = Integer32
_WlsxSysExtPortTableGenNumber_Object = MibScalar
wlsxSysExtPortTableGenNumber = _WlsxSysExtPortTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 6),
    _WlsxSysExtPortTableGenNumber_Type()
)
wlsxSysExtPortTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtPortTableGenNumber.setStatus("deprecated")
_WlsxSysExtVlanTableGenNumber_Type = Integer32
_WlsxSysExtVlanTableGenNumber_Object = MibScalar
wlsxSysExtVlanTableGenNumber = _WlsxSysExtVlanTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 7),
    _WlsxSysExtVlanTableGenNumber_Type()
)
wlsxSysExtVlanTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtVlanTableGenNumber.setStatus("deprecated")
_WlsxSysExtVlanInterfaceTableGenNumber_Type = Integer32
_WlsxSysExtVlanInterfaceTableGenNumber_Object = MibScalar
wlsxSysExtVlanInterfaceTableGenNumber = _WlsxSysExtVlanInterfaceTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 8),
    _WlsxSysExtVlanInterfaceTableGenNumber_Type()
)
wlsxSysExtVlanInterfaceTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtVlanInterfaceTableGenNumber.setStatus("deprecated")
_WlsxSysExtLicenseTableGenNumber_Type = Integer32
_WlsxSysExtLicenseTableGenNumber_Object = MibScalar
wlsxSysExtLicenseTableGenNumber = _WlsxSysExtLicenseTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 9),
    _WlsxSysExtLicenseTableGenNumber_Type()
)
wlsxSysExtLicenseTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtLicenseTableGenNumber.setStatus("deprecated")
_WlsxSysExtMonAPTableGenNumber_Type = Integer32
_WlsxSysExtMonAPTableGenNumber_Object = MibScalar
wlsxSysExtMonAPTableGenNumber = _WlsxSysExtMonAPTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 10),
    _WlsxSysExtMonAPTableGenNumber_Type()
)
wlsxSysExtMonAPTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtMonAPTableGenNumber.setStatus("deprecated")
_WlsxSysExtMonStationTableGenNumber_Type = Integer32
_WlsxSysExtMonStationTableGenNumber_Object = MibScalar
wlsxSysExtMonStationTableGenNumber = _WlsxSysExtMonStationTableGenNumber_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 2, 2, 11),
    _WlsxSysExtMonStationTableGenNumber_Type()
)
wlsxSysExtMonStationTableGenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxSysExtMonStationTableGenNumber.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-SYSTEMEXT-MIB",
    **{"wlsxSystemExtMIB": wlsxSystemExtMIB,
       "wlsxSystemExtGroup": wlsxSystemExtGroup,
       "wlsxSysExtSwitchIp": wlsxSysExtSwitchIp,
       "wlsxSysExtHostname": wlsxSysExtHostname,
       "wlsxSysExtModelName": wlsxSysExtModelName,
       "wlsxSysExtSwitchRole": wlsxSysExtSwitchRole,
       "wlsxSysExtSwitchMasterIp": wlsxSysExtSwitchMasterIp,
       "wlsxSysExtSwitchDate": wlsxSysExtSwitchDate,
       "wlsxSysExtSwitchBaseMacaddress": wlsxSysExtSwitchBaseMacaddress,
       "wlsxSysExtFanTrayAssemblyNumber": wlsxSysExtFanTrayAssemblyNumber,
       "wlsxSysExtFanTraySerialNumber": wlsxSysExtFanTraySerialNumber,
       "wlsxSysExtInternalTemparature": wlsxSysExtInternalTemparature,
       "wlsxSysExtLicenseSerialNumber": wlsxSysExtLicenseSerialNumber,
       "wlsxSysExtSwitchLicenseCount": wlsxSysExtSwitchLicenseCount,
       "wlsxSysExtProcessorTable": wlsxSysExtProcessorTable,
       "wlsxSysExtProcessorEntry": wlsxSysExtProcessorEntry,
       "sysExtProcessorID": sysExtProcessorID,
       "sysExtProcessorDescr": sysExtProcessorDescr,
       "sysExtProcessorLoad": sysExtProcessorLoad,
       "wlsxSysExtStorageTable": wlsxSysExtStorageTable,
       "wlsxSysExtStorageEntry": wlsxSysExtStorageEntry,
       "sysExtStorageIndex": sysExtStorageIndex,
       "sysExtStorageType": sysExtStorageType,
       "sysExtStorageSize": sysExtStorageSize,
       "sysExtStorageUsed": sysExtStorageUsed,
       "sysExtStorageName": sysExtStorageName,
       "wlsxSysExtMemoryTable": wlsxSysExtMemoryTable,
       "wlsxSysExtMemoryEntry": wlsxSysExtMemoryEntry,
       "sysExtMemoryIndex": sysExtMemoryIndex,
       "sysExtMemorySize": sysExtMemorySize,
       "sysExtMemoryUsed": sysExtMemoryUsed,
       "sysExtMemoryFree": sysExtMemoryFree,
       "wlsxSysExtCardTable": wlsxSysExtCardTable,
       "wlsxSysExtCardEntry": wlsxSysExtCardEntry,
       "sysExtCardSlot": sysExtCardSlot,
       "sysExtCardType": sysExtCardType,
       "sysExtCardNumOfPorts": sysExtCardNumOfPorts,
       "sysExtCardNumOfFastethernetPorts": sysExtCardNumOfFastethernetPorts,
       "sysExtCardNumOfGigPorts": sysExtCardNumOfGigPorts,
       "sysExtCardSerialNo": sysExtCardSerialNo,
       "sysExtCardAssemblyNo": sysExtCardAssemblyNo,
       "sysExtCardManufacturingDate": sysExtCardManufacturingDate,
       "sysExtCardHwRevision": sysExtCardHwRevision,
       "sysExtCardFpgaRevision": sysExtCardFpgaRevision,
       "sysExtCardSwitchChip": sysExtCardSwitchChip,
       "sysExtCardStatus": sysExtCardStatus,
       "sysExtCardUserSlot": sysExtCardUserSlot,
       "sysExtCardServiceTag": sysExtCardServiceTag,
       "sysExtCardPartNumber": sysExtCardPartNumber,
       "wlsxSysExtFanTable": wlsxSysExtFanTable,
       "wlsxSysExtFanEntry": wlsxSysExtFanEntry,
       "sysExtFanIndex": sysExtFanIndex,
       "sysExtFanStatus": sysExtFanStatus,
       "wlsxSysExtPowerSupplyTable": wlsxSysExtPowerSupplyTable,
       "wlsxSysExtPowerSupplyEntry": wlsxSysExtPowerSupplyEntry,
       "sysExtPowerSupplyIndex": sysExtPowerSupplyIndex,
       "sysExtPowerSupplyStatus": sysExtPowerSupplyStatus,
       "wlsxSysExtSwitchListTable": wlsxSysExtSwitchListTable,
       "wlsxSysExtSwitchListEntry": wlsxSysExtSwitchListEntry,
       "sysExtSwitchIPAddress": sysExtSwitchIPAddress,
       "sysExtSwitchRole": sysExtSwitchRole,
       "sysExtSwitchLocation": sysExtSwitchLocation,
       "sysExtSwitchSWVersion": sysExtSwitchSWVersion,
       "sysExtSwitchStatus": sysExtSwitchStatus,
       "sysExtSwitchName": sysExtSwitchName,
       "sysExtSwitchSerNo": sysExtSwitchSerNo,
       "wlsxSysExtSwitchLicenseTable": wlsxSysExtSwitchLicenseTable,
       "wlsxSysExtLicenseEntry": wlsxSysExtLicenseEntry,
       "sysExtLicenseIndex": sysExtLicenseIndex,
       "sysExtLicenseKey": sysExtLicenseKey,
       "sysExtLicenseInstalled": sysExtLicenseInstalled,
       "sysExtLicenseExpires": sysExtLicenseExpires,
       "sysExtLicenseFlags": sysExtLicenseFlags,
       "sysExtLicenseService": sysExtLicenseService,
       "wlsxSysExtMMSCompatLevel": wlsxSysExtMMSCompatLevel,
       "wlsxSysExtMMSConfigID": wlsxSysExtMMSConfigID,
       "wlsxSysExtControllerConfigID": wlsxSysExtControllerConfigID,
       "wlsxSysExtIsMMSConfigUpdateEnabled": wlsxSysExtIsMMSConfigUpdateEnabled,
       "wlsxSysExtSwitchLastReload": wlsxSysExtSwitchLastReload,
       "wlsxSysExtLastStatsReset": wlsxSysExtLastStatsReset,
       "wlsxSysExtHwVersion": wlsxSysExtHwVersion,
       "wlsxSysExtSwVersion": wlsxSysExtSwVersion,
       "wlsxSysExtSerialNumber": wlsxSysExtSerialNumber,
       "wlsxSysExtCpuUsedPercent": wlsxSysExtCpuUsedPercent,
       "wlsxSysExtMemoryUsedPercent": wlsxSysExtMemoryUsedPercent,
       "wlsxSysExtPacketLossPercent": wlsxSysExtPacketLossPercent,
       "wlsxSysExtPoweredViaPoe": wlsxSysExtPoweredViaPoe,
       "wlsxSysVMHostType": wlsxSysVMHostType,
       "wlsxSysExtProcessorModel": wlsxSysExtProcessorModel,
       "wlsxSysExtTotalCpu": wlsxSysExtTotalCpu,
       "wlsxSysExtTotalSocket": wlsxSysExtTotalSocket,
       "wlsxAuthFailIp": wlsxAuthFailIp,
       "wlsxSysExtDiskSize": wlsxSysExtDiskSize,
       "wlsxNSysExtSwitchListTable": wlsxNSysExtSwitchListTable,
       "wlsxNSysExtSwitchListEntry": wlsxNSysExtSwitchListEntry,
       "sysExtNSwitchIPAddressType": sysExtNSwitchIPAddressType,
       "sysExtNSwitchIPAddress": sysExtNSwitchIPAddress,
       "sysExtNSwitchRole": sysExtNSwitchRole,
       "sysExtNSwitchLocation": sysExtNSwitchLocation,
       "sysExtNSwitchSWVersion": sysExtNSwitchSWVersion,
       "sysExtNSwitchStatus": sysExtNSwitchStatus,
       "sysExtNSwitchName": sysExtNSwitchName,
       "sysExtNSwitchSerNo": sysExtNSwitchSerNo,
       "wlsxSystemExtTableGenNumberGroup": wlsxSystemExtTableGenNumberGroup,
       "wlsxSysExtUserTableGenNumber": wlsxSysExtUserTableGenNumber,
       "wlsxSysExtAPBssidTableGenNumber": wlsxSysExtAPBssidTableGenNumber,
       "wlsxSysExtAPRadioTableGenNumber": wlsxSysExtAPRadioTableGenNumber,
       "wlsxSysExtAPTableGenNumber": wlsxSysExtAPTableGenNumber,
       "wlsxSysExtSwitchListTableGenNumber": wlsxSysExtSwitchListTableGenNumber,
       "wlsxSysExtPortTableGenNumber": wlsxSysExtPortTableGenNumber,
       "wlsxSysExtVlanTableGenNumber": wlsxSysExtVlanTableGenNumber,
       "wlsxSysExtVlanInterfaceTableGenNumber": wlsxSysExtVlanInterfaceTableGenNumber,
       "wlsxSysExtLicenseTableGenNumber": wlsxSysExtLicenseTableGenNumber,
       "wlsxSysExtMonAPTableGenNumber": wlsxSysExtMonAPTableGenNumber,
       "wlsxSysExtMonStationTableGenNumber": wlsxSysExtMonStationTableGenNumber}
)
