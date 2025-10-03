# SNMP MIB module (FORTINET-FORTIVOICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTIVOICE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:57 2025
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

(FnBoolState,
 FnIndex,
 FnSessionProto,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "FnSessionProto",
    "fortinet")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

fnFortiVoiceMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 115)
)
if mibBuilder.loadTexts:
    fnFortiVoiceMib.setRevisions(
        ("2014-01-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FvSysEventCodeVal(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("systemHalt", 1),
          ("systemReboot", 2),
          ("systemReload", 3),
          ("systemUpgrade", 4),
          ("guiUpgrade", 5),
          ("logDiskFormat", 6),
          ("storageDiskFormat", 7))
    )



class FvHAEventIdVal(TextualConvention, Integer32):
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
        *(("masterUnitSwitch", 1),
          ("slaveUnitSwitch", 2),
          ("unitShutdown", 3))
    )



class FvHAModeVal(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("master", 1),
          ("slave", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FvTraps_ObjectIdentity = ObjectIdentity
fvTraps = _FvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 115, 0)
)
_FvSystem_ObjectIdentity = ObjectIdentity
fvSystem = _FvSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1)
)


class _FvSysModel_Type(DisplayString):
    """Custom type fvSysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FvSysModel_Type.__name__ = "DisplayString"
_FvSysModel_Object = MibScalar
fvSysModel = _FvSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 1),
    _FvSysModel_Type()
)
fvSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSysModel.setStatus("current")


class _FvSysSerial_Type(DisplayString):
    """Custom type fvSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FvSysSerial_Type.__name__ = "DisplayString"
_FvSysSerial_Object = MibScalar
fvSysSerial = _FvSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 2),
    _FvSysSerial_Type()
)
fvSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSysSerial.setStatus("current")


class _FvSysVersion_Type(DisplayString):
    """Custom type fvSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FvSysVersion_Type.__name__ = "DisplayString"
_FvSysVersion_Object = MibScalar
fvSysVersion = _FvSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 3),
    _FvSysVersion_Type()
)
fvSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSysVersion.setStatus("current")
_FvSysCpuUsage_Type = Gauge32
_FvSysCpuUsage_Object = MibScalar
fvSysCpuUsage = _FvSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 6),
    _FvSysCpuUsage_Type()
)
fvSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSysCpuUsage.setStatus("current")
_FvSysMemUsage_Type = Gauge32
_FvSysMemUsage_Object = MibScalar
fvSysMemUsage = _FvSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 7),
    _FvSysMemUsage_Type()
)
fvSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSysMemUsage.setStatus("current")
_FvSysLogDiskUsage_Type = Gauge32
_FvSysLogDiskUsage_Object = MibScalar
fvSysLogDiskUsage = _FvSysLogDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 8),
    _FvSysLogDiskUsage_Type()
)
fvSysLogDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSysLogDiskUsage.setStatus("current")
_FvSysStorageDiskUsage_Type = Gauge32
_FvSysStorageDiskUsage_Object = MibScalar
fvSysStorageDiskUsage = _FvSysStorageDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 9),
    _FvSysStorageDiskUsage_Type()
)
fvSysStorageDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSysStorageDiskUsage.setStatus("current")
_FvSysEventCode_Type = FvSysEventCodeVal
_FvSysEventCode_Object = MibScalar
fvSysEventCode = _FvSysEventCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 11),
    _FvSysEventCode_Type()
)
fvSysEventCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fvSysEventCode.setStatus("current")
_FvHAEventId_Type = FvHAEventIdVal
_FvHAEventId_Object = MibScalar
fvHAEventId = _FvHAEventId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 14),
    _FvHAEventId_Type()
)
fvHAEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fvHAEventId.setStatus("current")
_FvHAUnitIp_Type = IpAddress
_FvHAUnitIp_Object = MibScalar
fvHAUnitIp = _FvHAUnitIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 15),
    _FvHAUnitIp_Type()
)
fvHAUnitIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fvHAUnitIp.setStatus("current")


class _FvHAEventReason_Type(DisplayString):
    """Custom type fvHAEventReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FvHAEventReason_Type.__name__ = "DisplayString"
_FvHAEventReason_Object = MibScalar
fvHAEventReason = _FvHAEventReason_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 16),
    _FvHAEventReason_Type()
)
fvHAEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fvHAEventReason.setStatus("current")
_FvSysLoad_Type = Gauge32
_FvSysLoad_Object = MibScalar
fvSysLoad = _FvSysLoad_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 30),
    _FvSysLoad_Type()
)
fvSysLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvSysLoad.setStatus("current")
_FvSysHA_ObjectIdentity = ObjectIdentity
fvSysHA = _FvSysHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 200)
)
_FvHAMode_Type = FvHAModeVal
_FvHAMode_Object = MibScalar
fvHAMode = _FvHAMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 200, 1),
    _FvHAMode_Type()
)
fvHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvHAMode.setStatus("current")
_FvHAEffectiveMode_Type = FvHAModeVal
_FvHAEffectiveMode_Object = MibScalar
fvHAEffectiveMode = _FvHAEffectiveMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 115, 1, 200, 2),
    _FvHAEffectiveMode_Type()
)
fvHAEffectiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fvHAEffectiveMode.setStatus("current")
_FvMIBConformance_ObjectIdentity = ObjectIdentity
fvMIBConformance = _FvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 115, 600)
)

# Managed Objects groups

fvSystemConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 115, 600, 1)
)
fvSystemConformanceGroup.setObjects(
      *(("FORTINET-FORTIVOICE-MIB", "fvSysModel"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysSerial"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysVersion"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysCpuUsage"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysMemUsage"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysLogDiskUsage"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysStorageDiskUsage"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysEventCode"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysLoad"))
)
if mibBuilder.loadTexts:
    fvSystemConformanceGroup.setStatus("current")

fvHAModeConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 115, 600, 6)
)
fvHAModeConformanceGroup.setObjects(
      *(("FORTINET-FORTIVOICE-MIB", "fvHAMode"),
        ("FORTINET-FORTIVOICE-MIB", "fvHAEffectiveMode"))
)
if mibBuilder.loadTexts:
    fvHAModeConformanceGroup.setStatus("current")


# Notification objects

fvTrapStorageDiskHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 115, 0, 104)
)
fvTrapStorageDiskHighThreshold.setObjects(
    ("FORTINET-FORTIVOICE-MIB", "fvSysSerial")
)
if mibBuilder.loadTexts:
    fvTrapStorageDiskHighThreshold.setStatus(
        "current"
    )

fvTrapSystemEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 115, 0, 201)
)
fvTrapSystemEvent.setObjects(
      *(("FORTINET-FORTIVOICE-MIB", "fvSysSerial"),
        ("FORTINET-FORTIVOICE-MIB", "fvSysEventCode"))
)
if mibBuilder.loadTexts:
    fvTrapSystemEvent.setStatus(
        "current"
    )

fvTrapHAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 115, 0, 203)
)
fvTrapHAEvent.setObjects(
      *(("FORTINET-FORTIVOICE-MIB", "fvSysSerial"),
        ("FORTINET-FORTIVOICE-MIB", "fvHAEventId"),
        ("FORTINET-FORTIVOICE-MIB", "fvHAUnitIp"),
        ("FORTINET-FORTIVOICE-MIB", "fvHAEventReason"))
)
if mibBuilder.loadTexts:
    fvTrapHAEvent.setStatus(
        "current"
    )


# Notifications groups

fvTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 115, 600, 7)
)
fvTrapsComplianceGroup.setObjects(
      *(("FORTINET-FORTIVOICE-MIB", "fvTrapStorageDiskHighThreshold"),
        ("FORTINET-FORTIVOICE-MIB", "fvTrapSystemEvent"),
        ("FORTINET-FORTIVOICE-MIB", "fvTrapHAEvent"))
)
if mibBuilder.loadTexts:
    fvTrapsComplianceGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 115, 600, 100)
)
fvMIBCompliance.setObjects(
      *(("FORTINET-FORTIVOICE-MIB", "fvSystemConformanceGroup"),
        ("FORTINET-FORTIVOICE-MIB", "fvHAModeConformanceGroup"),
        ("FORTINET-FORTIVOICE-MIB", "fvTrapsComplianceGroup"))
)
if mibBuilder.loadTexts:
    fvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIVOICE-MIB",
    **{"FvSysEventCodeVal": FvSysEventCodeVal,
       "FvHAEventIdVal": FvHAEventIdVal,
       "FvHAModeVal": FvHAModeVal,
       "fnFortiVoiceMib": fnFortiVoiceMib,
       "fvTraps": fvTraps,
       "fvTrapStorageDiskHighThreshold": fvTrapStorageDiskHighThreshold,
       "fvTrapSystemEvent": fvTrapSystemEvent,
       "fvTrapHAEvent": fvTrapHAEvent,
       "fvSystem": fvSystem,
       "fvSysModel": fvSysModel,
       "fvSysSerial": fvSysSerial,
       "fvSysVersion": fvSysVersion,
       "fvSysCpuUsage": fvSysCpuUsage,
       "fvSysMemUsage": fvSysMemUsage,
       "fvSysLogDiskUsage": fvSysLogDiskUsage,
       "fvSysStorageDiskUsage": fvSysStorageDiskUsage,
       "fvSysEventCode": fvSysEventCode,
       "fvHAEventId": fvHAEventId,
       "fvHAUnitIp": fvHAUnitIp,
       "fvHAEventReason": fvHAEventReason,
       "fvSysLoad": fvSysLoad,
       "fvSysHA": fvSysHA,
       "fvHAMode": fvHAMode,
       "fvHAEffectiveMode": fvHAEffectiveMode,
       "fvMIBConformance": fvMIBConformance,
       "fvSystemConformanceGroup": fvSystemConformanceGroup,
       "fvHAModeConformanceGroup": fvHAModeConformanceGroup,
       "fvTrapsComplianceGroup": fvTrapsComplianceGroup,
       "fvMIBCompliance": fvMIBCompliance}
)
