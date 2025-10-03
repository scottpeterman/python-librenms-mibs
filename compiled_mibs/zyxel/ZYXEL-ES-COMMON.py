# SNMP MIB module (ZYXEL-ES-COMMON) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zyxel\ZYXEL-ES-COMMON
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:55 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esConformance,
 esMgmt) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esConformance",
    "esMgmt")


# MODULE-IDENTITY

esSysInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1)
)

esSysMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SwPlatform(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("zynos", 2),
          ("zld", 3))
    )



class MgmtAlarmStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("sysAlarmDetected", 0),
          ("sysTemperatureError", 1),
          ("sysFanRPMError", 2),
          ("sysVoltageRangeError", 3))
    )


# MIB Managed Objects in the order of their OIDs

_EsBasicCompliances_ObjectIdentity = ObjectIdentity
esBasicCompliances = _EsBasicCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 2, 1)
)
_EsBasicGroups_ObjectIdentity = ObjectIdentity
esBasicGroups = _EsBasicGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 2, 2)
)
_SysSwPlatform_Type = SwPlatform
_SysSwPlatform_Object = MibScalar
sysSwPlatform = _SysSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 1),
    _SysSwPlatform_Type()
)
sysSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatform.setStatus("current")
_SysSwMajorVersion_Type = Integer32
_SysSwMajorVersion_Object = MibScalar
sysSwMajorVersion = _SysSwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 2),
    _SysSwMajorVersion_Type()
)
sysSwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMajorVersion.setStatus("current")
_SysSwMinorVersion_Type = Integer32
_SysSwMinorVersion_Object = MibScalar
sysSwMinorVersion = _SysSwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 3),
    _SysSwMinorVersion_Type()
)
sysSwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMinorVersion.setStatus("current")
_SysSwModel_Type = DisplayString
_SysSwModel_Object = MibScalar
sysSwModel = _SysSwModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 4),
    _SysSwModel_Type()
)
sysSwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwModel.setStatus("current")
_SysSwPatchNumber_Type = Integer32
_SysSwPatchNumber_Object = MibScalar
sysSwPatchNumber = _SysSwPatchNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 5),
    _SysSwPatchNumber_Type()
)
sysSwPatchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPatchNumber.setStatus("current")
_SysSwVersionString_Type = DisplayString
_SysSwVersionString_Object = MibScalar
sysSwVersionString = _SysSwVersionString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 6),
    _SysSwVersionString_Type()
)
sysSwVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwVersionString.setStatus("current")
_SysSwDay_Type = Integer32
_SysSwDay_Object = MibScalar
sysSwDay = _SysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 7),
    _SysSwDay_Type()
)
sysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwDay.setStatus("current")
_SysSwMonth_Type = Integer32
_SysSwMonth_Object = MibScalar
sysSwMonth = _SysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 8),
    _SysSwMonth_Type()
)
sysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMonth.setStatus("current")
_SysSwYear_Type = Integer32
_SysSwYear_Object = MibScalar
sysSwYear = _SysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 9),
    _SysSwYear_Type()
)
sysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwYear.setStatus("current")
_SysProductFamily_Type = DisplayString
_SysProductFamily_Object = MibScalar
sysProductFamily = _SysProductFamily_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 10),
    _SysProductFamily_Type()
)
sysProductFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductFamily.setStatus("current")
_SysProductModel_Type = DisplayString
_SysProductModel_Object = MibScalar
sysProductModel = _SysProductModel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 11),
    _SysProductModel_Type()
)
sysProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductModel.setStatus("current")
_SysProductSerialNumber_Type = DisplayString
_SysProductSerialNumber_Object = MibScalar
sysProductSerialNumber = _SysProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 12),
    _SysProductSerialNumber_Type()
)
sysProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductSerialNumber.setStatus("current")
_SysHwMajorVersion_Type = Integer32
_SysHwMajorVersion_Object = MibScalar
sysHwMajorVersion = _SysHwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 13),
    _SysHwMajorVersion_Type()
)
sysHwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMajorVersion.setStatus("current")
_SysHwMinorVersion_Type = Integer32
_SysHwMinorVersion_Object = MibScalar
sysHwMinorVersion = _SysHwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 14),
    _SysHwMinorVersion_Type()
)
sysHwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMinorVersion.setStatus("current")
_SysHwVersionString_Type = DisplayString
_SysHwVersionString_Object = MibScalar
sysHwVersionString = _SysHwVersionString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 15),
    _SysHwVersionString_Type()
)
sysHwVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwVersionString.setStatus("current")
_SysCountryCode_Type = DisplayString
_SysCountryCode_Object = MibScalar
sysCountryCode = _SysCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 16),
    _SysCountryCode_Type()
)
sysCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCountryCode.setStatus("current")
_SysCurrentDateTime_Type = DisplayString
_SysCurrentDateTime_Object = MibScalar
sysCurrentDateTime = _SysCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 17),
    _SysCurrentDateTime_Type()
)
sysCurrentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurrentDateTime.setStatus("obsolete")
_SysCurrentTime_Type = DisplayString
_SysCurrentTime_Object = MibScalar
sysCurrentTime = _SysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 18),
    _SysCurrentTime_Type()
)
sysCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurrentTime.setStatus("obsolete")
_SysActiveSessionNum_Type = Integer32
_SysActiveSessionNum_Object = MibScalar
sysActiveSessionNum = _SysActiveSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 1, 19),
    _SysActiveSessionNum_Type()
)
sysActiveSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysActiveSessionNum.setStatus("current")


class _SysMgmtReboot_Type(Integer32):
    """Custom type sysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("reboot", 1))
    )


_SysMgmtReboot_Type.__name__ = "Integer32"
_SysMgmtReboot_Object = MibScalar
sysMgmtReboot = _SysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 1),
    _SysMgmtReboot_Type()
)
sysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtReboot.setStatus("current")


class _SysMgmtConfigSave_Type(Integer32):
    """Custom type sysMgmtConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("save", 1))
    )


_SysMgmtConfigSave_Type.__name__ = "Integer32"
_SysMgmtConfigSave_Object = MibScalar
sysMgmtConfigSave = _SysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 2),
    _SysMgmtConfigSave_Type()
)
sysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSave.setStatus("current")


class _SysMgmtRestoreDefaultConfig_Type(Integer32):
    """Custom type sysMgmtRestoreDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("restore", 1))
    )


_SysMgmtRestoreDefaultConfig_Type.__name__ = "Integer32"
_SysMgmtRestoreDefaultConfig_Object = MibScalar
sysMgmtRestoreDefaultConfig = _SysMgmtRestoreDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 3),
    _SysMgmtRestoreDefaultConfig_Type()
)
sysMgmtRestoreDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtRestoreDefaultConfig.setStatus("current")


class _SysMgmtCPUUsage_Type(Integer32):
    """Custom type sysMgmtCPUUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtCPUUsage_Type.__name__ = "Integer32"
_SysMgmtCPUUsage_Object = MibScalar
sysMgmtCPUUsage = _SysMgmtCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 4),
    _SysMgmtCPUUsage_Type()
)
sysMgmtCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPUUsage.setStatus("current")


class _SysMgmtMemUsage_Type(Integer32):
    """Custom type sysMgmtMemUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtMemUsage_Type.__name__ = "Integer32"
_SysMgmtMemUsage_Object = MibScalar
sysMgmtMemUsage = _SysMgmtMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 5),
    _SysMgmtMemUsage_Type()
)
sysMgmtMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtMemUsage.setStatus("current")


class _SysMgmtFlashUsage_Type(Integer32):
    """Custom type sysMgmtFlashUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtFlashUsage_Type.__name__ = "Integer32"
_SysMgmtFlashUsage_Object = MibScalar
sysMgmtFlashUsage = _SysMgmtFlashUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 6),
    _SysMgmtFlashUsage_Type()
)
sysMgmtFlashUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtFlashUsage.setStatus("current")


class _SysMgmtCPU5SecUsage_Type(Integer32):
    """Custom type sysMgmtCPU5SecUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtCPU5SecUsage_Type.__name__ = "Integer32"
_SysMgmtCPU5SecUsage_Object = MibScalar
sysMgmtCPU5SecUsage = _SysMgmtCPU5SecUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 7),
    _SysMgmtCPU5SecUsage_Type()
)
sysMgmtCPU5SecUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPU5SecUsage.setStatus("current")


class _SysMgmtCPU1MinUsage_Type(Integer32):
    """Custom type sysMgmtCPU1MinUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtCPU1MinUsage_Type.__name__ = "Integer32"
_SysMgmtCPU1MinUsage_Object = MibScalar
sysMgmtCPU1MinUsage = _SysMgmtCPU1MinUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 8),
    _SysMgmtCPU1MinUsage_Type()
)
sysMgmtCPU1MinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPU1MinUsage.setStatus("current")


class _SysMgmtCPU5MinUsage_Type(Integer32):
    """Custom type sysMgmtCPU5MinUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtCPU5MinUsage_Type.__name__ = "Integer32"
_SysMgmtCPU5MinUsage_Object = MibScalar
sysMgmtCPU5MinUsage = _SysMgmtCPU5MinUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 9),
    _SysMgmtCPU5MinUsage_Type()
)
sysMgmtCPU5MinUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtCPU5MinUsage.setStatus("current")


class _SysMgmtBootupConfigIndex_Type(Integer32):
    """Custom type sysMgmtBootupConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtBootupConfigIndex_Type.__name__ = "Integer32"
_SysMgmtBootupConfigIndex_Object = MibScalar
sysMgmtBootupConfigIndex = _SysMgmtBootupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 10),
    _SysMgmtBootupConfigIndex_Type()
)
sysMgmtBootupConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupConfigIndex.setStatus("current")


class _SysMgmtBootupImageIndex_Type(Integer32):
    """Custom type sysMgmtBootupImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMgmtBootupImageIndex_Type.__name__ = "Integer32"
_SysMgmtBootupImageIndex_Object = MibScalar
sysMgmtBootupImageIndex = _SysMgmtBootupImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 11),
    _SysMgmtBootupImageIndex_Type()
)
sysMgmtBootupImageIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupImageIndex.setStatus("current")
_SysMgmtAlarmStatus_Type = MgmtAlarmStatus
_SysMgmtAlarmStatus_Object = MibScalar
sysMgmtAlarmStatus = _SysMgmtAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 12),
    _SysMgmtAlarmStatus_Type()
)
sysMgmtAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtAlarmStatus.setStatus("obsolete")
_SysMgmtVLANControl_Type = EnabledStatus
_SysMgmtVLANControl_Object = MibScalar
sysMgmtVLANControl = _SysMgmtVLANControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 13),
    _SysMgmtVLANControl_Type()
)
sysMgmtVLANControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtVLANControl.setStatus("deprecated")


class _SysMgmtVLANID_Type(Integer32):
    """Custom type sysMgmtVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SysMgmtVLANID_Type.__name__ = "Integer32"
_SysMgmtVLANID_Object = MibScalar
sysMgmtVLANID = _SysMgmtVLANID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 14),
    _SysMgmtVLANID_Type()
)
sysMgmtVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtVLANID.setStatus("deprecated")
_Sys8021QControl_Type = EnabledStatus
_Sys8021QControl_Object = MibScalar
sys8021QControl = _Sys8021QControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 2, 15),
    _Sys8021QControl_Type()
)
sys8021QControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sys8021QControl.setStatus("deprecated")

# Managed Objects groups

esSysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 2, 2, 1)
)
esSysInfoGroup.setObjects(
      *(("ZYXEL-ES-COMMON", "sysSwPlatform"),
        ("ZYXEL-ES-COMMON", "sysSwMajorVersion"),
        ("ZYXEL-ES-COMMON", "sysSwMinorVersion"),
        ("ZYXEL-ES-COMMON", "sysSwModel"),
        ("ZYXEL-ES-COMMON", "sysSwPatchNumber"),
        ("ZYXEL-ES-COMMON", "sysSwVersionString"),
        ("ZYXEL-ES-COMMON", "sysSwDay"),
        ("ZYXEL-ES-COMMON", "sysSwMonth"),
        ("ZYXEL-ES-COMMON", "sysSwYear"),
        ("ZYXEL-ES-COMMON", "sysProductFamily"),
        ("ZYXEL-ES-COMMON", "sysProductModel"),
        ("ZYXEL-ES-COMMON", "sysProductSerialNumber"))
)
if mibBuilder.loadTexts:
    esSysInfoGroup.setStatus("current")

esSysMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 2, 2, 2)
)
esSysMgmtGroup.setObjects(
      *(("ZYXEL-ES-COMMON", "sysMgmtReboot"),
        ("ZYXEL-ES-COMMON", "sysMgmtConfigSave"),
        ("ZYXEL-ES-COMMON", "sysMgmtRestoreDefaultConfig"),
        ("ZYXEL-ES-COMMON", "sysMgmtCPUUsage"),
        ("ZYXEL-ES-COMMON", "sysMgmtMemUsage"))
)
if mibBuilder.loadTexts:
    esSysMgmtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

esBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 2, 1, 1)
)
esBasicCompliance.setObjects(
      *(("ZYXEL-ES-COMMON", "esSysInfoGroup"),
        ("ZYXEL-ES-COMMON", "esSysMgmtGroup"))
)
if mibBuilder.loadTexts:
    esBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES-COMMON",
    **{"SwPlatform": SwPlatform,
       "MgmtAlarmStatus": MgmtAlarmStatus,
       "esBasicCompliances": esBasicCompliances,
       "esBasicCompliance": esBasicCompliance,
       "esBasicGroups": esBasicGroups,
       "esSysInfoGroup": esSysInfoGroup,
       "esSysMgmtGroup": esSysMgmtGroup,
       "esSysInfo": esSysInfo,
       "sysSwPlatform": sysSwPlatform,
       "sysSwMajorVersion": sysSwMajorVersion,
       "sysSwMinorVersion": sysSwMinorVersion,
       "sysSwModel": sysSwModel,
       "sysSwPatchNumber": sysSwPatchNumber,
       "sysSwVersionString": sysSwVersionString,
       "sysSwDay": sysSwDay,
       "sysSwMonth": sysSwMonth,
       "sysSwYear": sysSwYear,
       "sysProductFamily": sysProductFamily,
       "sysProductModel": sysProductModel,
       "sysProductSerialNumber": sysProductSerialNumber,
       "sysHwMajorVersion": sysHwMajorVersion,
       "sysHwMinorVersion": sysHwMinorVersion,
       "sysHwVersionString": sysHwVersionString,
       "sysCountryCode": sysCountryCode,
       "sysCurrentDateTime": sysCurrentDateTime,
       "sysCurrentTime": sysCurrentTime,
       "sysActiveSessionNum": sysActiveSessionNum,
       "esSysMgmt": esSysMgmt,
       "sysMgmtReboot": sysMgmtReboot,
       "sysMgmtConfigSave": sysMgmtConfigSave,
       "sysMgmtRestoreDefaultConfig": sysMgmtRestoreDefaultConfig,
       "sysMgmtCPUUsage": sysMgmtCPUUsage,
       "sysMgmtMemUsage": sysMgmtMemUsage,
       "sysMgmtFlashUsage": sysMgmtFlashUsage,
       "sysMgmtCPU5SecUsage": sysMgmtCPU5SecUsage,
       "sysMgmtCPU1MinUsage": sysMgmtCPU1MinUsage,
       "sysMgmtCPU5MinUsage": sysMgmtCPU5MinUsage,
       "sysMgmtBootupConfigIndex": sysMgmtBootupConfigIndex,
       "sysMgmtBootupImageIndex": sysMgmtBootupImageIndex,
       "sysMgmtAlarmStatus": sysMgmtAlarmStatus,
       "sysMgmtVLANControl": sysMgmtVLANControl,
       "sysMgmtVLANID": sysMgmtVLANID,
       "sys8021QControl": sys8021QControl}
)
