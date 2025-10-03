# SNMP MIB module (BLUECOAT-SG-HEALTHCHECK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecoat\BLUECOAT-SG-HEALTHCHECK-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:39 2025
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

deviceHealthCheckMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7)
)
if mibBuilder.loadTexts:
    deviceHealthCheckMIB.setRevisions(
        ("2013-05-22 03:00",
         "2013-05-21 03:00",
         "2007-11-05 03:00",
         "2002-08-28 03:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class HealthCheckMessageString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class HealthCheckStatus(TextualConvention, Integer32):
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ok", 2),
          ("okWithErrors", 3),
          ("okForSomeIPs", 4),
          ("okButFailing", 5),
          ("checkFailed", 6),
          ("dnsFailed", 7),
          ("okOnAltServer", 8))
    )



# MIB Managed Objects in the order of their OIDs

_DeviceHealthCheckMIBObjects_ObjectIdentity = ObjectIdentity
deviceHealthCheckMIBObjects = _DeviceHealthCheckMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1)
)
_DeviceHealthCheckStringValues_ObjectIdentity = ObjectIdentity
deviceHealthCheckStringValues = _DeviceHealthCheckStringValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 1)
)
_DeviceHealthCheckMessage_Type = HealthCheckMessageString
_DeviceHealthCheckMessage_Object = MibScalar
deviceHealthCheckMessage = _DeviceHealthCheckMessage_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 1, 1),
    _DeviceHealthCheckMessage_Type()
)
deviceHealthCheckMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHealthCheckMessage.setStatus("current")
_DeviceHealthCheckValues_ObjectIdentity = ObjectIdentity
deviceHealthCheckValues = _DeviceHealthCheckValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2)
)
_DeviceHealthCheckValueTable_Object = MibTable
deviceHealthCheckValueTable = _DeviceHealthCheckValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deviceHealthCheckValueTable.setStatus("current")
_DeviceHealthCheckValueEntry_Object = MibTableRow
deviceHealthCheckValueEntry = _DeviceHealthCheckValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1)
)
deviceHealthCheckValueEntry.setIndexNames(
    (0, "BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckName"),
)
if mibBuilder.loadTexts:
    deviceHealthCheckValueEntry.setStatus("current")


class _DeviceHealthCheckName_Type(DisplayString):
    """Custom type deviceHealthCheckName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_DeviceHealthCheckName_Type.__name__ = "DisplayString"
_DeviceHealthCheckName_Object = MibTableColumn
deviceHealthCheckName = _DeviceHealthCheckName_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 1),
    _DeviceHealthCheckName_Type()
)
deviceHealthCheckName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHealthCheckName.setStatus("current")
_DeviceHealthCheckState_Type = HealthCheckStatus
_DeviceHealthCheckState_Object = MibTableColumn
deviceHealthCheckState = _DeviceHealthCheckState_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 2),
    _DeviceHealthCheckState_Type()
)
deviceHealthCheckState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHealthCheckState.setStatus("current")
_DeviceHealthCheckTime_Type = Counter64
_DeviceHealthCheckTime_Object = MibTableColumn
deviceHealthCheckTime = _DeviceHealthCheckTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 1, 2, 1, 1, 3),
    _DeviceHealthCheckTime_Type()
)
deviceHealthCheckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHealthCheckTime.setStatus("current")
_DeviceHealthCheckMIBNotifs_ObjectIdentity = ObjectIdentity
deviceHealthCheckMIBNotifs = _DeviceHealthCheckMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 2)
)
_DeviceHealthCheckMIBNotifsPrefix_ObjectIdentity = ObjectIdentity
deviceHealthCheckMIBNotifsPrefix = _DeviceHealthCheckMIBNotifsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 2, 0)
)
_DeviceHealthCheckMIBConformance_ObjectIdentity = ObjectIdentity
deviceHealthCheckMIBConformance = _DeviceHealthCheckMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 3)
)
_DeviceHealthCheckMIBCompliances_ObjectIdentity = ObjectIdentity
deviceHealthCheckMIBCompliances = _DeviceHealthCheckMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 1)
)
_DeviceHealthCheckMIBGroups_ObjectIdentity = ObjectIdentity
deviceHealthCheckMIBGroups = _DeviceHealthCheckMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 2)
)
_DeviceHealthCheckMIBNotifGroups_ObjectIdentity = ObjectIdentity
deviceHealthCheckMIBNotifGroups = _DeviceHealthCheckMIBNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 3)
)

# Managed Objects groups

deviceHealthCheckMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 2, 1)
)
deviceHealthCheckMIBGroup.setObjects(
      *(("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckName"),
        ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckState"),
        ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckTime"),
        ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMessage"))
)
if mibBuilder.loadTexts:
    deviceHealthCheckMIBGroup.setStatus("current")


# Notification objects

deviceHealthCheckTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 2, 0, 1)
)
deviceHealthCheckTrap.setObjects(
    ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMessage")
)
if mibBuilder.loadTexts:
    deviceHealthCheckTrap.setStatus(
        "current"
    )


# Notifications groups

deviceHealthCheckMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 3, 1)
)
deviceHealthCheckMIBNotifGroup.setObjects(
    ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckTrap")
)
if mibBuilder.loadTexts:
    deviceHealthCheckMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

deviceHealthCheckMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3417, 2, 7, 3, 1, 1)
)
deviceHealthCheckMIBCompliance.setObjects(
    ("BLUECOAT-SG-HEALTHCHECK-MIB", "deviceHealthCheckMIBGroup")
)
if mibBuilder.loadTexts:
    deviceHealthCheckMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-HEALTHCHECK-MIB",
    **{"HealthCheckMessageString": HealthCheckMessageString,
       "HealthCheckStatus": HealthCheckStatus,
       "deviceHealthCheckMIB": deviceHealthCheckMIB,
       "deviceHealthCheckMIBObjects": deviceHealthCheckMIBObjects,
       "deviceHealthCheckStringValues": deviceHealthCheckStringValues,
       "deviceHealthCheckMessage": deviceHealthCheckMessage,
       "deviceHealthCheckValues": deviceHealthCheckValues,
       "deviceHealthCheckValueTable": deviceHealthCheckValueTable,
       "deviceHealthCheckValueEntry": deviceHealthCheckValueEntry,
       "deviceHealthCheckName": deviceHealthCheckName,
       "deviceHealthCheckState": deviceHealthCheckState,
       "deviceHealthCheckTime": deviceHealthCheckTime,
       "deviceHealthCheckMIBNotifs": deviceHealthCheckMIBNotifs,
       "deviceHealthCheckMIBNotifsPrefix": deviceHealthCheckMIBNotifsPrefix,
       "deviceHealthCheckTrap": deviceHealthCheckTrap,
       "deviceHealthCheckMIBConformance": deviceHealthCheckMIBConformance,
       "deviceHealthCheckMIBCompliances": deviceHealthCheckMIBCompliances,
       "deviceHealthCheckMIBCompliance": deviceHealthCheckMIBCompliance,
       "deviceHealthCheckMIBGroups": deviceHealthCheckMIBGroups,
       "deviceHealthCheckMIBGroup": deviceHealthCheckMIBGroup,
       "deviceHealthCheckMIBNotifGroups": deviceHealthCheckMIBNotifGroups,
       "deviceHealthCheckMIBNotifGroup": deviceHealthCheckMIBNotifGroup}
)
