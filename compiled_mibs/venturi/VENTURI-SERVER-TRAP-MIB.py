# SNMP MIB module (VENTURI-SERVER-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\venturi\VENTURI-SERVER-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:52 2025
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(vServerMgmt,) = mibBuilder.importSymbols(
    "VENTURI-SERVER-MIB",
    "vServerMgmt")


# MODULE-IDENTITY

vServerTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1)
)
if mibBuilder.loadTexts:
    vServerTraps.setRevisions(
        ("2011-01-03 00:00",
         "2010-01-06 00:00",
         "2008-06-25 00:00",
         "2008-03-19 00:00",
         "2005-07-12 00:00",
         "2005-04-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VServerTrapDef_ObjectIdentity = ObjectIdentity
vServerTrapDef = _VServerTrapDef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0)
)
if mibBuilder.loadTexts:
    vServerTrapDef.setStatus("current")
_VServerTrapInfo_ObjectIdentity = ObjectIdentity
vServerTrapInfo = _VServerTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vServerTrapInfo.setStatus("current")
_ErrorCode_Type = Integer32
_ErrorCode_Object = MibScalar
errorCode = _ErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 1),
    _ErrorCode_Type()
)
errorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorCode.setStatus("current")


class _Filename_Type(OctetString):
    """Custom type filename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Filename_Type.__name__ = "OctetString"
_Filename_Object = MibScalar
filename = _Filename_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 2),
    _Filename_Type()
)
filename.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    filename.setStatus("current")


class _Fan_Type(OctetString):
    """Custom type fan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Fan_Type.__name__ = "OctetString"
_Fan_Object = MibScalar
fan = _Fan_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 3),
    _Fan_Type()
)
fan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fan.setStatus("current")
_MCode_Type = Integer32
_MCode_Object = MibScalar
mCode = _MCode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 4),
    _MCode_Type()
)
mCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mCode.setStatus("current")


class _CurrentValue_Type(OctetString):
    """Custom type currentValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CurrentValue_Type.__name__ = "OctetString"
_CurrentValue_Object = MibScalar
currentValue = _CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 5),
    _CurrentValue_Type()
)
currentValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentValue.setStatus("current")


class _Disk_Type(OctetString):
    """Custom type disk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Disk_Type.__name__ = "OctetString"
_Disk_Object = MibScalar
disk = _Disk_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 7),
    _Disk_Type()
)
disk.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    disk.setStatus("current")


class _PowerSupplyLead_Type(OctetString):
    """Custom type powerSupplyLead based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PowerSupplyLead_Type.__name__ = "OctetString"
_PowerSupplyLead_Object = MibScalar
powerSupplyLead = _PowerSupplyLead_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 8),
    _PowerSupplyLead_Type()
)
powerSupplyLead.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    powerSupplyLead.setStatus("current")


class _SystemId_Type(OctetString):
    """Custom type systemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemId_Type.__name__ = "OctetString"
_SystemId_Object = MibScalar
systemId = _SystemId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 9),
    _SystemId_Type()
)
systemId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemId.setStatus("current")


class _TemperatureSensor_Type(OctetString):
    """Custom type temperatureSensor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TemperatureSensor_Type.__name__ = "OctetString"
_TemperatureSensor_Object = MibScalar
temperatureSensor = _TemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 10),
    _TemperatureSensor_Type()
)
temperatureSensor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    temperatureSensor.setStatus("current")


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("informational", 5))
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 11),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")


class _FtpHost_Type(OctetString):
    """Custom type ftpHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FtpHost_Type.__name__ = "OctetString"
_FtpHost_Object = MibScalar
ftpHost = _FtpHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 12),
    _FtpHost_Type()
)
ftpHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ftpHost.setStatus("current")


class _FtpUser_Type(OctetString):
    """Custom type ftpUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FtpUser_Type.__name__ = "OctetString"
_FtpUser_Object = MibScalar
ftpUser = _FtpUser_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 13),
    _FtpUser_Type()
)
ftpUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ftpUser.setStatus("current")


class _FtpDirectory_Type(OctetString):
    """Custom type ftpDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FtpDirectory_Type.__name__ = "OctetString"
_FtpDirectory_Object = MibScalar
ftpDirectory = _FtpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 14),
    _FtpDirectory_Type()
)
ftpDirectory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ftpDirectory.setStatus("current")
_Timeout_Type = Integer32
_Timeout_Object = MibScalar
timeout = _Timeout_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 15),
    _Timeout_Type()
)
timeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timeout.setStatus("current")
_Retries_Type = Integer32
_Retries_Object = MibScalar
retries = _Retries_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 16),
    _Retries_Type()
)
retries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    retries.setStatus("current")


class _RadiusServer_Type(OctetString):
    """Custom type radiusServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RadiusServer_Type.__name__ = "OctetString"
_RadiusServer_Object = MibScalar
radiusServer = _RadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 17),
    _RadiusServer_Type()
)
radiusServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    radiusServer.setStatus("current")


class _SetThreshold_Type(OctetString):
    """Custom type setThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SetThreshold_Type.__name__ = "OctetString"
_SetThreshold_Object = MibScalar
setThreshold = _SetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 18),
    _SetThreshold_Type()
)
setThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    setThreshold.setStatus("current")


class _ClearThreshold_Type(OctetString):
    """Custom type clearThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ClearThreshold_Type.__name__ = "OctetString"
_ClearThreshold_Object = MibScalar
clearThreshold = _ClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 19),
    _ClearThreshold_Type()
)
clearThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clearThreshold.setStatus("current")


class _HighThreshold_Type(OctetString):
    """Custom type highThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HighThreshold_Type.__name__ = "OctetString"
_HighThreshold_Object = MibScalar
highThreshold = _HighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 20),
    _HighThreshold_Type()
)
highThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    highThreshold.setStatus("current")


class _LowThreshold_Type(OctetString):
    """Custom type lowThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_LowThreshold_Type.__name__ = "OctetString"
_LowThreshold_Object = MibScalar
lowThreshold = _LowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 21),
    _LowThreshold_Type()
)
lowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    lowThreshold.setStatus("current")
_EntityId_Type = Integer32
_EntityId_Object = MibScalar
entityId = _EntityId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 1, 22),
    _EntityId_Type()
)
entityId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    entityId.setStatus("current")

# Managed Objects groups


# Notification objects

vServerStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 1)
)
vServerStopped.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerStopped.setStatus(
        "current"
    )

vServerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 2)
)
vServerStarted.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerStarted.setStatus(
        "current"
    )

vServerSwapOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 3)
)
vServerSwapOverload.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "currentValue"),
        ("VENTURI-SERVER-TRAP-MIB", "setThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "clearThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerSwapOverload.setStatus(
        "current"
    )

vServerSwapOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 4)
)
vServerSwapOverloadClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerSwapOverloadClear.setStatus(
        "current"
    )

vServerNetworkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 5)
)
vServerNetworkError.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerNetworkError.setStatus(
        "current"
    )

vServerNetworkErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 6)
)
vServerNetworkErrorClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerNetworkErrorClear.setStatus(
        "current"
    )

vServerKernelError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 7)
)
vServerKernelError.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerKernelError.setStatus(
        "current"
    )

vServerKernelErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 8)
)
vServerKernelErrorClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerKernelErrorClear.setStatus(
        "current"
    )

vServerLicenseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 9)
)
vServerLicenseError.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLicenseError.setStatus(
        "current"
    )

vServerLicenseErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 10)
)
vServerLicenseErrorClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLicenseErrorClear.setStatus(
        "current"
    )

vServerSharedMemoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 11)
)
vServerSharedMemoryError.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerSharedMemoryError.setStatus(
        "current"
    )

vServerSharedMemoryErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 12)
)
vServerSharedMemoryErrorClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerSharedMemoryErrorClear.setStatus(
        "current"
    )

vServerFileSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 13)
)
vServerFileSystemError.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerFileSystemError.setStatus(
        "current"
    )

vServerFileSystemErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 14)
)
vServerFileSystemErrorClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerFileSystemErrorClear.setStatus(
        "current"
    )

vServerTCPOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 15)
)
vServerTCPOverload.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "currentValue"),
        ("VENTURI-SERVER-TRAP-MIB", "setThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "clearThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerTCPOverload.setStatus(
        "current"
    )

vServerTCPOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 16)
)
vServerTCPOverloadClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerTCPOverloadClear.setStatus(
        "current"
    )

vServerCacheOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 17)
)
vServerCacheOverload.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "disk"),
        ("VENTURI-SERVER-TRAP-MIB", "currentValue"),
        ("VENTURI-SERVER-TRAP-MIB", "setThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "clearThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerCacheOverload.setStatus(
        "current"
    )

vServerCacheOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 18)
)
vServerCacheOverloadClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerCacheOverloadClear.setStatus(
        "current"
    )

vServerLogOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 19)
)
vServerLogOverload.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "disk"),
        ("VENTURI-SERVER-TRAP-MIB", "currentValue"),
        ("VENTURI-SERVER-TRAP-MIB", "setThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "clearThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLogOverload.setStatus(
        "current"
    )

vServerLogOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 20)
)
vServerLogOverloadClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLogOverloadClear.setStatus(
        "current"
    )

vServerFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 21)
)
vServerFanFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "fan"),
        ("VENTURI-SERVER-TRAP-MIB", "currentValue"),
        ("VENTURI-SERVER-TRAP-MIB", "setThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "clearThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerFanFailure.setStatus(
        "current"
    )

vServerFanFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 22)
)
vServerFanFailureClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerFanFailureClear.setStatus(
        "current"
    )

vServerPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 23)
)
vServerPowerSupplyFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "powerSupplyLead"),
        ("VENTURI-SERVER-TRAP-MIB", "currentValue"),
        ("VENTURI-SERVER-TRAP-MIB", "lowThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "highThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerPowerSupplyFailure.setStatus(
        "current"
    )

vServerPowerSupplyFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 24)
)
vServerPowerSupplyFailureClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerPowerSupplyFailureClear.setStatus(
        "current"
    )

vServerTemperatureExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 25)
)
vServerTemperatureExceeded.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "temperatureSensor"),
        ("VENTURI-SERVER-TRAP-MIB", "currentValue"),
        ("VENTURI-SERVER-TRAP-MIB", "setThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "clearThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerTemperatureExceeded.setStatus(
        "current"
    )

vServerTemperatureExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 26)
)
vServerTemperatureExceededClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerTemperatureExceededClear.setStatus(
        "current"
    )

vServerStatsDeliveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 27)
)
vServerStatsDeliveryFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "filename"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpHost"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpUser"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpDirectory"),
        ("VENTURI-SERVER-TRAP-MIB", "timeout"),
        ("VENTURI-SERVER-TRAP-MIB", "retries"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerStatsDeliveryFailure.setStatus(
        "current"
    )

vServerStatsDeliveryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 28)
)
vServerStatsDeliveryClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerStatsDeliveryClear.setStatus(
        "current"
    )

vServerLogDeliveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 29)
)
vServerLogDeliveryFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "filename"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpHost"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpUser"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpDirectory"),
        ("VENTURI-SERVER-TRAP-MIB", "timeout"),
        ("VENTURI-SERVER-TRAP-MIB", "retries"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLogDeliveryFailure.setStatus(
        "current"
    )

vServerLogDeliveryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 30)
)
vServerLogDeliveryClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLogDeliveryClear.setStatus(
        "current"
    )

vServerURLDeliveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 31)
)
vServerURLDeliveryFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "filename"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpHost"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpUser"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpDirectory"),
        ("VENTURI-SERVER-TRAP-MIB", "timeout"),
        ("VENTURI-SERVER-TRAP-MIB", "retries"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerURLDeliveryFailure.setStatus(
        "current"
    )

vServerURLDeliveryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 32)
)
vServerURLDeliveryClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerURLDeliveryClear.setStatus(
        "current"
    )

vServerModuleInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 33)
)
vServerModuleInitFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerModuleInitFailure.setStatus(
        "current"
    )

vServerModuleInitFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 34)
)
vServerModuleInitFailureClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerModuleInitFailureClear.setStatus(
        "current"
    )

vServerDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 35)
)
vServerDiskFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "disk"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerDiskFailure.setStatus(
        "current"
    )

vServerTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 37)
)
vServerTestTrap.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerTestTrap.setStatus(
        "current"
    )

vServerLicensesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 39)
)
vServerLicensesExceeded.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLicensesExceeded.setStatus(
        "current"
    )

vServerRadiusServerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 41)
)
vServerRadiusServerError.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "radiusServer"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerRadiusServerError.setStatus(
        "current"
    )

vServerRadiusServerErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 42)
)
vServerRadiusServerErrorClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerRadiusServerErrorClear.setStatus(
        "current"
    )

vServerLowCriticalBuffers = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 43)
)
vServerLowCriticalBuffers.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "currentValue"),
        ("VENTURI-SERVER-TRAP-MIB", "setThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "clearThreshold"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLowCriticalBuffers.setStatus(
        "current"
    )

vServerLowCriticalBuffersClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 44)
)
vServerLowCriticalBuffersClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerLowCriticalBuffersClear.setStatus(
        "current"
    )

vServerClientStatsDeliveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 45)
)
vServerClientStatsDeliveryFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "filename"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpHost"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpUser"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpDirectory"),
        ("VENTURI-SERVER-TRAP-MIB", "timeout"),
        ("VENTURI-SERVER-TRAP-MIB", "retries"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerClientStatsDeliveryFailure.setStatus(
        "current"
    )

vServerClientStatsDeliveryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 46)
)
vServerClientStatsDeliveryClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerClientStatsDeliveryClear.setStatus(
        "current"
    )

vServerClientUpgradeDeliveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 47)
)
vServerClientUpgradeDeliveryFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "filename"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpHost"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpUser"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpDirectory"),
        ("VENTURI-SERVER-TRAP-MIB", "timeout"),
        ("VENTURI-SERVER-TRAP-MIB", "retries"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerClientUpgradeDeliveryFailure.setStatus(
        "current"
    )

vServerClientUpgradeDeliveryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 48)
)
vServerClientUpgradeDeliveryClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerClientUpgradeDeliveryClear.setStatus(
        "current"
    )

vServerDCDeliveryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 49)
)
vServerDCDeliveryFailure.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "filename"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpHost"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpUser"),
        ("VENTURI-SERVER-TRAP-MIB", "ftpDirectory"),
        ("VENTURI-SERVER-TRAP-MIB", "timeout"),
        ("VENTURI-SERVER-TRAP-MIB", "retries"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerDCDeliveryFailure.setStatus(
        "current"
    )

vServerDCDeliveryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 1, 0, 50)
)
vServerDCDeliveryClear.setObjects(
      *(("VENTURI-SERVER-TRAP-MIB", "mCode"),
        ("VENTURI-SERVER-TRAP-MIB", "errorCode"),
        ("VENTURI-SERVER-TRAP-MIB", "systemId"),
        ("VENTURI-SERVER-TRAP-MIB", "trapSeverity"),
        ("VENTURI-SERVER-TRAP-MIB", "entityId"))
)
if mibBuilder.loadTexts:
    vServerDCDeliveryClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VENTURI-SERVER-TRAP-MIB",
    **{"vServerTraps": vServerTraps,
       "vServerTrapDef": vServerTrapDef,
       "vServerStopped": vServerStopped,
       "vServerStarted": vServerStarted,
       "vServerSwapOverload": vServerSwapOverload,
       "vServerSwapOverloadClear": vServerSwapOverloadClear,
       "vServerNetworkError": vServerNetworkError,
       "vServerNetworkErrorClear": vServerNetworkErrorClear,
       "vServerKernelError": vServerKernelError,
       "vServerKernelErrorClear": vServerKernelErrorClear,
       "vServerLicenseError": vServerLicenseError,
       "vServerLicenseErrorClear": vServerLicenseErrorClear,
       "vServerSharedMemoryError": vServerSharedMemoryError,
       "vServerSharedMemoryErrorClear": vServerSharedMemoryErrorClear,
       "vServerFileSystemError": vServerFileSystemError,
       "vServerFileSystemErrorClear": vServerFileSystemErrorClear,
       "vServerTCPOverload": vServerTCPOverload,
       "vServerTCPOverloadClear": vServerTCPOverloadClear,
       "vServerCacheOverload": vServerCacheOverload,
       "vServerCacheOverloadClear": vServerCacheOverloadClear,
       "vServerLogOverload": vServerLogOverload,
       "vServerLogOverloadClear": vServerLogOverloadClear,
       "vServerFanFailure": vServerFanFailure,
       "vServerFanFailureClear": vServerFanFailureClear,
       "vServerPowerSupplyFailure": vServerPowerSupplyFailure,
       "vServerPowerSupplyFailureClear": vServerPowerSupplyFailureClear,
       "vServerTemperatureExceeded": vServerTemperatureExceeded,
       "vServerTemperatureExceededClear": vServerTemperatureExceededClear,
       "vServerStatsDeliveryFailure": vServerStatsDeliveryFailure,
       "vServerStatsDeliveryClear": vServerStatsDeliveryClear,
       "vServerLogDeliveryFailure": vServerLogDeliveryFailure,
       "vServerLogDeliveryClear": vServerLogDeliveryClear,
       "vServerURLDeliveryFailure": vServerURLDeliveryFailure,
       "vServerURLDeliveryClear": vServerURLDeliveryClear,
       "vServerModuleInitFailure": vServerModuleInitFailure,
       "vServerModuleInitFailureClear": vServerModuleInitFailureClear,
       "vServerDiskFailure": vServerDiskFailure,
       "vServerTestTrap": vServerTestTrap,
       "vServerLicensesExceeded": vServerLicensesExceeded,
       "vServerRadiusServerError": vServerRadiusServerError,
       "vServerRadiusServerErrorClear": vServerRadiusServerErrorClear,
       "vServerLowCriticalBuffers": vServerLowCriticalBuffers,
       "vServerLowCriticalBuffersClear": vServerLowCriticalBuffersClear,
       "vServerClientStatsDeliveryFailure": vServerClientStatsDeliveryFailure,
       "vServerClientStatsDeliveryClear": vServerClientStatsDeliveryClear,
       "vServerClientUpgradeDeliveryFailure": vServerClientUpgradeDeliveryFailure,
       "vServerClientUpgradeDeliveryClear": vServerClientUpgradeDeliveryClear,
       "vServerDCDeliveryFailure": vServerDCDeliveryFailure,
       "vServerDCDeliveryClear": vServerDCDeliveryClear,
       "vServerTrapInfo": vServerTrapInfo,
       "errorCode": errorCode,
       "filename": filename,
       "fan": fan,
       "mCode": mCode,
       "currentValue": currentValue,
       "disk": disk,
       "powerSupplyLead": powerSupplyLead,
       "systemId": systemId,
       "temperatureSensor": temperatureSensor,
       "trapSeverity": trapSeverity,
       "ftpHost": ftpHost,
       "ftpUser": ftpUser,
       "ftpDirectory": ftpDirectory,
       "timeout": timeout,
       "retries": retries,
       "radiusServer": radiusServer,
       "setThreshold": setThreshold,
       "clearThreshold": clearThreshold,
       "highThreshold": highThreshold,
       "lowThreshold": lowThreshold,
       "entityId": entityId}
)
