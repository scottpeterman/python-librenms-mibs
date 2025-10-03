# SNMP MIB module (ENDACE-EDA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endace\ENDACE-EDA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:54 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

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

shogunEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 9)
)
if mibBuilder.loadTexts:
    shogunEventMIB.setRevisions(
        ("2012-05-03 21:50",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ShogunVariables_ObjectIdentity = ObjectIdentity
shogunVariables = _ShogunVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1)
)


class _AgentId_Type(OctetString):
    """Custom type agentId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentId_Type.__name__ = "OctetString"
_AgentId_Object = MibScalar
agentId = _AgentId_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 1),
    _AgentId_Type()
)
agentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentId.setStatus("current")


class _EventId_Type(OctetString):
    """Custom type eventId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventId_Type.__name__ = "OctetString"
_EventId_Object = MibScalar
eventId = _EventId_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 2),
    _EventId_Type()
)
eventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventId.setStatus("current")


class _EventDescr_Type(OctetString):
    """Custom type eventDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventDescr_Type.__name__ = "OctetString"
_EventDescr_Object = MibScalar
eventDescr = _EventDescr_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 3),
    _EventDescr_Type()
)
eventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescr.setStatus("current")


class _AlarmName_Type(OctetString):
    """Custom type alarmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmName_Type.__name__ = "OctetString"
_AlarmName_Object = MibScalar
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 4),
    _AlarmName_Type()
)
alarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmName.setStatus("current")


class _AlarmDescr_Type(OctetString):
    """Custom type alarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlarmDescr_Type.__name__ = "OctetString"
_AlarmDescr_Object = MibScalar
alarmDescr = _AlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 5),
    _AlarmDescr_Type()
)
alarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescr.setStatus("current")
_AlarmTrigger_Type = Counter64
_AlarmTrigger_Object = MibScalar
alarmTrigger = _AlarmTrigger_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 6),
    _AlarmTrigger_Type()
)
alarmTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTrigger.setStatus("current")
_AlarmCriteria_Type = Unsigned32
_AlarmCriteria_Object = MibScalar
alarmCriteria = _AlarmCriteria_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 7),
    _AlarmCriteria_Type()
)
alarmCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCriteria.setStatus("current")
_AlarmType_Type = Unsigned32
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 8),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_AlarmSeverity_Type = Unsigned32
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 18418, 9, 1, 9),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_ShogunEventTraps_ObjectIdentity = ObjectIdentity
shogunEventTraps = _ShogunEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 9, 3)
)
_ShogunNotificationPrefix_ObjectIdentity = ObjectIdentity
shogunNotificationPrefix = _ShogunNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 9, 3, 0)
)
_ShogunConf_ObjectIdentity = ObjectIdentity
shogunConf = _ShogunConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 9, 4)
)
if mibBuilder.loadTexts:
    shogunConf.setStatus("current")

# Managed Objects groups

shogunObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 9, 4, 2)
)
shogunObjectGroup.setObjects(
      *(("ENDACE-EDA-MIB", "agentId"),
        ("ENDACE-EDA-MIB", "alarmCriteria"),
        ("ENDACE-EDA-MIB", "alarmDescr"),
        ("ENDACE-EDA-MIB", "alarmName"),
        ("ENDACE-EDA-MIB", "alarmSeverity"),
        ("ENDACE-EDA-MIB", "alarmTrigger"),
        ("ENDACE-EDA-MIB", "alarmType"),
        ("ENDACE-EDA-MIB", "eventDescr"),
        ("ENDACE-EDA-MIB", "eventId"))
)
if mibBuilder.loadTexts:
    shogunObjectGroup.setStatus("current")


# Notification objects

eventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 9, 3, 0, 1)
)
eventNotification.setObjects(
      *(("ENDACE-EDA-MIB", "agentId"),
        ("ENDACE-EDA-MIB", "eventId"),
        ("ENDACE-EDA-MIB", "eventDescr"))
)
if mibBuilder.loadTexts:
    eventNotification.setStatus(
        "current"
    )

alarmRaisedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 9, 3, 0, 2)
)
alarmRaisedNotification.setObjects(
      *(("ENDACE-EDA-MIB", "alarmCriteria"),
        ("ENDACE-EDA-MIB", "alarmDescr"),
        ("ENDACE-EDA-MIB", "alarmName"),
        ("ENDACE-EDA-MIB", "alarmSeverity"),
        ("ENDACE-EDA-MIB", "alarmTrigger"),
        ("ENDACE-EDA-MIB", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmRaisedNotification.setStatus(
        "current"
    )

alarmClearedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 9, 3, 0, 3)
)
alarmClearedNotification.setObjects(
      *(("ENDACE-EDA-MIB", "alarmCriteria"),
        ("ENDACE-EDA-MIB", "alarmDescr"),
        ("ENDACE-EDA-MIB", "alarmName"),
        ("ENDACE-EDA-MIB", "alarmSeverity"),
        ("ENDACE-EDA-MIB", "alarmTrigger"),
        ("ENDACE-EDA-MIB", "alarmType"))
)
if mibBuilder.loadTexts:
    alarmClearedNotification.setStatus(
        "current"
    )


# Notifications groups

shogunNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 9, 4, 1)
)
shogunNotifyGroup.setObjects(
      *(("ENDACE-EDA-MIB", "alarmClearedNotification"),
        ("ENDACE-EDA-MIB", "alarmRaisedNotification"),
        ("ENDACE-EDA-MIB", "eventNotification"))
)
if mibBuilder.loadTexts:
    shogunNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-EDA-MIB",
    **{"shogunEventMIB": shogunEventMIB,
       "shogunVariables": shogunVariables,
       "agentId": agentId,
       "eventId": eventId,
       "eventDescr": eventDescr,
       "alarmName": alarmName,
       "alarmDescr": alarmDescr,
       "alarmTrigger": alarmTrigger,
       "alarmCriteria": alarmCriteria,
       "alarmType": alarmType,
       "alarmSeverity": alarmSeverity,
       "shogunEventTraps": shogunEventTraps,
       "shogunNotificationPrefix": shogunNotificationPrefix,
       "eventNotification": eventNotification,
       "alarmRaisedNotification": alarmRaisedNotification,
       "alarmClearedNotification": alarmClearedNotification,
       "shogunConf": shogunConf,
       "shogunNotifyGroup": shogunNotifyGroup,
       "shogunObjectGroup": shogunObjectGroup}
)
