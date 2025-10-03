# SNMP MIB module (JUNIPER-WX-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\juniper\JUNIPER-WX-COMMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:02:19 2025
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

(jnxWxCommonMib,
 jnxWxModules) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-REG",
    "jnxWxCommonMib",
    "jnxWxModules")

(TcChassisType,) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-TC",
    "TcChassisType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxWxCommonMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxWxCommonMibModule.setRevisions(
        ("2003-09-30 08:45",
         "2003-04-01 00:00",
         "2003-03-10 00:00",
         "2002-06-03 00:00",
         "2002-03-27 00:00",
         "2002-02-22 00:00",
         "2002-01-23 00:00",
         "2002-01-17 00:00",
         "2001-08-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxWxCommonConfMib_ObjectIdentity = ObjectIdentity
jnxWxCommonConfMib = _JnxWxCommonConfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxWxCommonConfMib.setStatus("current")
_JnxWxCommonObjs_ObjectIdentity = ObjectIdentity
jnxWxCommonObjs = _JnxWxCommonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2)
)
if mibBuilder.loadTexts:
    jnxWxCommonObjs.setStatus("current")
_JnxWxSys_ObjectIdentity = ObjectIdentity
jnxWxSys = _JnxWxSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxWxSys.setStatus("current")


class _JnxWxSysSwVersion_Type(DisplayString):
    """Custom type jnxWxSysSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxWxSysSwVersion_Type.__name__ = "DisplayString"
_JnxWxSysSwVersion_Object = MibScalar
jnxWxSysSwVersion = _JnxWxSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 1),
    _JnxWxSysSwVersion_Type()
)
jnxWxSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysSwVersion.setStatus("current")


class _JnxWxSysHwVersion_Type(DisplayString):
    """Custom type jnxWxSysHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxWxSysHwVersion_Type.__name__ = "DisplayString"
_JnxWxSysHwVersion_Object = MibScalar
jnxWxSysHwVersion = _JnxWxSysHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 2),
    _JnxWxSysHwVersion_Type()
)
jnxWxSysHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysHwVersion.setStatus("current")


class _JnxWxSysSerialNumber_Type(DisplayString):
    """Custom type jnxWxSysSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxWxSysSerialNumber_Type.__name__ = "DisplayString"
_JnxWxSysSerialNumber_Object = MibScalar
jnxWxSysSerialNumber = _JnxWxSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 3),
    _JnxWxSysSerialNumber_Type()
)
jnxWxSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysSerialNumber.setStatus("current")
_JnxWxSysTimeZoneOffset_Type = Integer32
_JnxWxSysTimeZoneOffset_Object = MibScalar
jnxWxSysTimeZoneOffset = _JnxWxSysTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 4),
    _JnxWxSysTimeZoneOffset_Type()
)
jnxWxSysTimeZoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysTimeZoneOffset.setStatus("current")
_JnxWxSysDaylightSaving_Type = TruthValue
_JnxWxSysDaylightSaving_Object = MibScalar
jnxWxSysDaylightSaving = _JnxWxSysDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 5),
    _JnxWxSysDaylightSaving_Type()
)
jnxWxSysDaylightSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysDaylightSaving.setStatus("current")
_JnxWxChassis_ObjectIdentity = ObjectIdentity
jnxWxChassis = _JnxWxChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxWxChassis.setStatus("current")
_JnxWxChassisType_Type = TcChassisType
_JnxWxChassisType_Object = MibScalar
jnxWxChassisType = _JnxWxChassisType_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 2, 1),
    _JnxWxChassisType_Type()
)
jnxWxChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxChassisType.setStatus("current")
_JnxWxCommonEvents_ObjectIdentity = ObjectIdentity
jnxWxCommonEvents = _JnxWxCommonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3)
)
if mibBuilder.loadTexts:
    jnxWxCommonEvents.setStatus("current")
_JnxWxCommonEventObjs_ObjectIdentity = ObjectIdentity
jnxWxCommonEventObjs = _JnxWxCommonEventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxWxCommonEventObjs.setStatus("current")
_JnxWxCommonEventDescr_Type = DisplayString
_JnxWxCommonEventDescr_Object = MibScalar
jnxWxCommonEventDescr = _JnxWxCommonEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 1, 1),
    _JnxWxCommonEventDescr_Type()
)
jnxWxCommonEventDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxWxCommonEventDescr.setStatus("current")
_JnxWxCommonEventEvents_ObjectIdentity = ObjectIdentity
jnxWxCommonEventEvents = _JnxWxCommonEventEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxWxCommonEventEvents.setStatus("current")
_JnxWxCommonEventEventsV2_ObjectIdentity = ObjectIdentity
jnxWxCommonEventEventsV2 = _JnxWxCommonEventEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0)
)
if mibBuilder.loadTexts:
    jnxWxCommonEventEventsV2.setStatus("current")

# Managed Objects groups


# Notification objects

jnxWxCommonEventInFailSafeMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 1)
)
if mibBuilder.loadTexts:
    jnxWxCommonEventInFailSafeMode.setStatus(
        "current"
    )

jnxWxCommonEventPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 2)
)
if mibBuilder.loadTexts:
    jnxWxCommonEventPowerSupplyFailure.setStatus(
        "current"
    )

jnxWxCommonEventPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 3)
)
if mibBuilder.loadTexts:
    jnxWxCommonEventPowerSupplyOk.setStatus(
        "current"
    )

jnxWxCommonEventLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 4)
)
jnxWxCommonEventLicenseExpired.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventLicenseExpired.setStatus(
        "current"
    )

jnxWxCommonEventThruputLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 5)
)
jnxWxCommonEventThruputLimitExceeded.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventThruputLimitExceeded.setStatus(
        "current"
    )

jnxWxCommonEventLicenseWillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 6)
)
jnxWxCommonEventLicenseWillExpire.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventLicenseWillExpire.setStatus(
        "current"
    )

jnxWxCommonEventLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 7)
)
jnxWxCommonEventLoginFailure.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventLoginFailure.setStatus(
        "current"
    )

jnxWxCommonEventFaultTolerantPassThrough = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 8)
)
jnxWxCommonEventFaultTolerantPassThrough.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventFaultTolerantPassThrough.setStatus(
        "current"
    )

jnxWxCommonEventFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 9)
)
jnxWxCommonEventFanFailure.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventFanFailure.setStatus(
        "current"
    )

jnxWxCommonEventFanSpeedVariation = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 10)
)
jnxWxCommonEventFanSpeedVariation.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventFanSpeedVariation.setStatus(
        "current"
    )

jnxWxCommonEventFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 11)
)
jnxWxCommonEventFanOk.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventFanOk.setStatus(
        "current"
    )

jnxWxCommonEventInterfaceSpeedMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 12)
)
jnxWxCommonEventInterfaceSpeedMismatch.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventInterfaceSpeedMismatch.setStatus(
        "current"
    )

jnxWxCommonEventInterfaceSpeedOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 13)
)
jnxWxCommonEventInterfaceSpeedOk.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventInterfaceSpeedOk.setStatus(
        "current"
    )

jnxWxCommonEventInterfaceDuplexMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 14)
)
jnxWxCommonEventInterfaceDuplexMismatch.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventInterfaceDuplexMismatch.setStatus(
        "current"
    )

jnxWxCommonEventIpsecSecurityAssociationAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 15)
)
jnxWxCommonEventIpsecSecurityAssociationAdded.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventIpsecSecurityAssociationAdded.setStatus(
        "current"
    )

jnxWxCommonEventIpsecSecurityAssociationExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 16)
)
jnxWxCommonEventIpsecSecurityAssociationExpired.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventIpsecSecurityAssociationExpired.setStatus(
        "current"
    )

jnxWxCommonEventIpsecSecurityAssociationDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 17)
)
jnxWxCommonEventIpsecSecurityAssociationDeleted.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxCommonEventIpsecSecurityAssociationDeleted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WX-COMMON-MIB",
    **{"jnxWxCommonMibModule": jnxWxCommonMibModule,
       "jnxWxCommonConfMib": jnxWxCommonConfMib,
       "jnxWxCommonObjs": jnxWxCommonObjs,
       "jnxWxSys": jnxWxSys,
       "jnxWxSysSwVersion": jnxWxSysSwVersion,
       "jnxWxSysHwVersion": jnxWxSysHwVersion,
       "jnxWxSysSerialNumber": jnxWxSysSerialNumber,
       "jnxWxSysTimeZoneOffset": jnxWxSysTimeZoneOffset,
       "jnxWxSysDaylightSaving": jnxWxSysDaylightSaving,
       "jnxWxChassis": jnxWxChassis,
       "jnxWxChassisType": jnxWxChassisType,
       "jnxWxCommonEvents": jnxWxCommonEvents,
       "jnxWxCommonEventObjs": jnxWxCommonEventObjs,
       "jnxWxCommonEventDescr": jnxWxCommonEventDescr,
       "jnxWxCommonEventEvents": jnxWxCommonEventEvents,
       "jnxWxCommonEventEventsV2": jnxWxCommonEventEventsV2,
       "jnxWxCommonEventInFailSafeMode": jnxWxCommonEventInFailSafeMode,
       "jnxWxCommonEventPowerSupplyFailure": jnxWxCommonEventPowerSupplyFailure,
       "jnxWxCommonEventPowerSupplyOk": jnxWxCommonEventPowerSupplyOk,
       "jnxWxCommonEventLicenseExpired": jnxWxCommonEventLicenseExpired,
       "jnxWxCommonEventThruputLimitExceeded": jnxWxCommonEventThruputLimitExceeded,
       "jnxWxCommonEventLicenseWillExpire": jnxWxCommonEventLicenseWillExpire,
       "jnxWxCommonEventLoginFailure": jnxWxCommonEventLoginFailure,
       "jnxWxCommonEventFaultTolerantPassThrough": jnxWxCommonEventFaultTolerantPassThrough,
       "jnxWxCommonEventFanFailure": jnxWxCommonEventFanFailure,
       "jnxWxCommonEventFanSpeedVariation": jnxWxCommonEventFanSpeedVariation,
       "jnxWxCommonEventFanOk": jnxWxCommonEventFanOk,
       "jnxWxCommonEventInterfaceSpeedMismatch": jnxWxCommonEventInterfaceSpeedMismatch,
       "jnxWxCommonEventInterfaceSpeedOk": jnxWxCommonEventInterfaceSpeedOk,
       "jnxWxCommonEventInterfaceDuplexMismatch": jnxWxCommonEventInterfaceDuplexMismatch,
       "jnxWxCommonEventIpsecSecurityAssociationAdded": jnxWxCommonEventIpsecSecurityAssociationAdded,
       "jnxWxCommonEventIpsecSecurityAssociationExpired": jnxWxCommonEventIpsecSecurityAssociationExpired,
       "jnxWxCommonEventIpsecSecurityAssociationDeleted": jnxWxCommonEventIpsecSecurityAssociationDeleted}
)
