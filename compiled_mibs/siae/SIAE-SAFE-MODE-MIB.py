# SNMP MIB module (SIAE-SAFE-MODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siae\SIAE-SAFE-MODE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:27:36 2025
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

(AlarmSeverityCode,
 AlarmStatus) = mibBuilder.importSymbols(
    "SIAE-ALARM-MIB",
    "AlarmSeverityCode",
    "AlarmStatus")

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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


# MODULE-IDENTITY

safeMode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99)
)
if mibBuilder.loadTexts:
    safeMode.setRevisions(
        ("2016-03-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SafeModeMibVersion_Type = Integer32
_SafeModeMibVersion_Object = MibScalar
safeModeMibVersion = _SafeModeMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99, 1),
    _SafeModeMibVersion_Type()
)
safeModeMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safeModeMibVersion.setStatus("current")
_SafeModeAlarm_Type = AlarmStatus
_SafeModeAlarm_Object = MibScalar
safeModeAlarm = _SafeModeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99, 2),
    _SafeModeAlarm_Type()
)
safeModeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safeModeAlarm.setStatus("current")


class _SafeModeAlarmSeverityCode_Type(AlarmSeverityCode):
    """Custom type safeModeAlarmSeverityCode based on AlarmSeverityCode"""
    defaultValue = 4


_SafeModeAlarmSeverityCode_Type.__name__ = "AlarmSeverityCode"
_SafeModeAlarmSeverityCode_Object = MibScalar
safeModeAlarmSeverityCode = _SafeModeAlarmSeverityCode_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99, 3),
    _SafeModeAlarmSeverityCode_Type()
)
safeModeAlarmSeverityCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safeModeAlarmSeverityCode.setStatus("current")


class _SafeModeStatus_Type(Integer32):
    """Custom type safeModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("safeModeStatusInactive", 1),
          ("safeModeStatusNoAuxService", 2),
          ("safeModeStatusLinkMngmt", 3),
          ("safeModeStatusSiteMngmt", 4),
          ("safeModeStatusSiteDefault", 5),
          ("safeModeStatusSiteRescue", 6))
    )


_SafeModeStatus_Type.__name__ = "Integer32"
_SafeModeStatus_Object = MibScalar
safeModeStatus = _SafeModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99, 4),
    _SafeModeStatus_Type()
)
safeModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    safeModeStatus.setStatus("current")


class _SafeModeRescueAdminStatus_Type(Integer32):
    """Custom type safeModeRescueAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SafeModeRescueAdminStatus_Type.__name__ = "Integer32"
_SafeModeRescueAdminStatus_Object = MibScalar
safeModeRescueAdminStatus = _SafeModeRescueAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99, 5),
    _SafeModeRescueAdminStatus_Type()
)
safeModeRescueAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safeModeRescueAdminStatus.setStatus("current")


class _SafeModeRescuePwd_Type(DisplayString):
    """Custom type safeModeRescuePwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_SafeModeRescuePwd_Type.__name__ = "DisplayString"
_SafeModeRescuePwd_Object = MibScalar
safeModeRescuePwd = _SafeModeRescuePwd_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99, 6),
    _SafeModeRescuePwd_Type()
)
safeModeRescuePwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safeModeRescuePwd.setStatus("current")


class _SafeModeRescueIpAddress_Type(IpAddress):
    """Custom type safeModeRescueIpAddress based on IpAddress"""
    defaultHexValue = "ac14fd0d"


_SafeModeRescueIpAddress_Type.__name__ = "IpAddress"
_SafeModeRescueIpAddress_Object = MibScalar
safeModeRescueIpAddress = _SafeModeRescueIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99, 7),
    _SafeModeRescueIpAddress_Type()
)
safeModeRescueIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safeModeRescueIpAddress.setStatus("current")
_SafeModeRescueIpNetMask_Type = IpAddress
_SafeModeRescueIpNetMask_Object = MibScalar
safeModeRescueIpNetMask = _SafeModeRescueIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 99, 8),
    _SafeModeRescueIpNetMask_Type()
)
safeModeRescueIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    safeModeRescueIpNetMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-SAFE-MODE-MIB",
    **{"safeMode": safeMode,
       "safeModeMibVersion": safeModeMibVersion,
       "safeModeAlarm": safeModeAlarm,
       "safeModeAlarmSeverityCode": safeModeAlarmSeverityCode,
       "safeModeStatus": safeModeStatus,
       "safeModeRescueAdminStatus": safeModeRescueAdminStatus,
       "safeModeRescuePwd": safeModeRescuePwd,
       "safeModeRescueIpAddress": safeModeRescueIpAddress,
       "safeModeRescueIpNetMask": safeModeRescueIpNetMask}
)
