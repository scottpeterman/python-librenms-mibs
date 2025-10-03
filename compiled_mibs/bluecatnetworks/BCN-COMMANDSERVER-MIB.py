# SNMP MIB module (BCN-COMMANDSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-COMMANDSERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:24 2025
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

(bcnServices,) = mibBuilder.importSymbols(
    "BCN-SMI-MIB",
    "bcnServices")

(BcnAlarmSeverity,) = mibBuilder.importSymbols(
    "BCN-TC-MIB",
    "BcnAlarmSeverity")

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

bcnCommandServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    bcnCommandServerMIB.setRevisions(
        ("2011-06-30 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnCommandServer_ObjectIdentity = ObjectIdentity
bcnCommandServer = _BcnCommandServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7)
)
_BcnCommandServerObjects_ObjectIdentity = ObjectIdentity
bcnCommandServerObjects = _BcnCommandServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2)
)
_BcnCommandServerServiceStatus_ObjectIdentity = ObjectIdentity
bcnCommandServerServiceStatus = _BcnCommandServerServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    bcnCommandServerServiceStatus.setStatus("current")


class _BcnCommandServerSerOperState_Type(Integer32):
    """Custom type bcnCommandServerSerOperState based on Integer32"""
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
        *(("running", 1),
          ("notRunning", 2),
          ("starting", 3),
          ("stopping", 4),
          ("fault", 5))
    )


_BcnCommandServerSerOperState_Type.__name__ = "Integer32"
_BcnCommandServerSerOperState_Object = MibScalar
bcnCommandServerSerOperState = _BcnCommandServerSerOperState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 2, 1, 1),
    _BcnCommandServerSerOperState_Type()
)
bcnCommandServerSerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnCommandServerSerOperState.setStatus("current")
_BcnCommandServerNotification_ObjectIdentity = ObjectIdentity
bcnCommandServerNotification = _BcnCommandServerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3)
)
_BcnCommandServerNotificationEvents_ObjectIdentity = ObjectIdentity
bcnCommandServerNotificationEvents = _BcnCommandServerNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 0)
)
_BcnCommandServerNotificationData_ObjectIdentity = ObjectIdentity
bcnCommandServerNotificationData = _BcnCommandServerNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1)
)
_BcnCommandServerAlarmSeverity_Type = BcnAlarmSeverity
_BcnCommandServerAlarmSeverity_Object = MibScalar
bcnCommandServerAlarmSeverity = _BcnCommandServerAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1, 1),
    _BcnCommandServerAlarmSeverity_Type()
)
bcnCommandServerAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnCommandServerAlarmSeverity.setStatus("current")
_BcnCommandServerAlarmInfo_Type = DisplayString
_BcnCommandServerAlarmInfo_Object = MibScalar
bcnCommandServerAlarmInfo = _BcnCommandServerAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 1, 2),
    _BcnCommandServerAlarmInfo_Type()
)
bcnCommandServerAlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnCommandServerAlarmInfo.setStatus("current")
_BcnCommandServerConformance_ObjectIdentity = ObjectIdentity
bcnCommandServerConformance = _BcnCommandServerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4)
)
_BcnCommandServerServiceCompliances_ObjectIdentity = ObjectIdentity
bcnCommandServerServiceCompliances = _BcnCommandServerServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 1)
)
_BcnCommandServerServiceGroups_ObjectIdentity = ObjectIdentity
bcnCommandServerServiceGroups = _BcnCommandServerServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2)
)

# Managed Objects groups

bcnCommandServerServiceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 1)
)
bcnCommandServerServiceStatusGroup.setObjects(
    ("BCN-COMMANDSERVER-MIB", "bcnCommandServerSerOperState")
)
if mibBuilder.loadTexts:
    bcnCommandServerServiceStatusGroup.setStatus("current")

bcnCommandServerNotificationDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 3)
)
bcnCommandServerNotificationDataGroup.setObjects(
      *(("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmSeverity"),
        ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnCommandServerNotificationDataGroup.setStatus("current")


# Notification objects

bcnCommandServerAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 3, 0, 1)
)
bcnCommandServerAlarmNotif.setObjects(
      *(("BCN-COMMANDSERVER-MIB", "bcnCommandServerSerOperState"),
        ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmSeverity"),
        ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnCommandServerAlarmNotif.setStatus(
        "current"
    )


# Notifications groups

bcnCommandServerNotificationEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 2, 2)
)
bcnCommandServerNotificationEventGroup.setObjects(
    ("BCN-COMMANDSERVER-MIB", "bcnCommandServerAlarmNotif")
)
if mibBuilder.loadTexts:
    bcnCommandServerNotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcnCommandServerStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 7, 4, 1, 1)
)
bcnCommandServerStatusCompliance.setObjects(
      *(("BCN-COMMANDSERVER-MIB", "bcnCommandServerServiceStatusGroup"),
        ("BCN-COMMANDSERVER-MIB", "bcnCommandServerNotificationEventGroup"),
        ("BCN-COMMANDSERVER-MIB", "bcnCommandServerNotificationDataGroup"))
)
if mibBuilder.loadTexts:
    bcnCommandServerStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-COMMANDSERVER-MIB",
    **{"bcnCommandServer": bcnCommandServer,
       "bcnCommandServerMIB": bcnCommandServerMIB,
       "bcnCommandServerObjects": bcnCommandServerObjects,
       "bcnCommandServerServiceStatus": bcnCommandServerServiceStatus,
       "bcnCommandServerSerOperState": bcnCommandServerSerOperState,
       "bcnCommandServerNotification": bcnCommandServerNotification,
       "bcnCommandServerNotificationEvents": bcnCommandServerNotificationEvents,
       "bcnCommandServerAlarmNotif": bcnCommandServerAlarmNotif,
       "bcnCommandServerNotificationData": bcnCommandServerNotificationData,
       "bcnCommandServerAlarmSeverity": bcnCommandServerAlarmSeverity,
       "bcnCommandServerAlarmInfo": bcnCommandServerAlarmInfo,
       "bcnCommandServerConformance": bcnCommandServerConformance,
       "bcnCommandServerServiceCompliances": bcnCommandServerServiceCompliances,
       "bcnCommandServerStatusCompliance": bcnCommandServerStatusCompliance,
       "bcnCommandServerServiceGroups": bcnCommandServerServiceGroups,
       "bcnCommandServerServiceStatusGroup": bcnCommandServerServiceStatusGroup,
       "bcnCommandServerNotificationEventGroup": bcnCommandServerNotificationEventGroup,
       "bcnCommandServerNotificationDataGroup": bcnCommandServerNotificationDataGroup}
)
