# SNMP MIB module (MDS-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gemds\MDS-EVENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:20 2025
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

(mdsLogging,) = mibBuilder.importSymbols(
    "MDS-ORBIT-SMI-MIB",
    "mdsLogging")

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

mdsEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1)
)
if mibBuilder.loadTexts:
    mdsEventMIB.setRevisions(
        ("2018-05-16 00:00",
         "2013-04-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MdsEventMIBObjects_ObjectIdentity = ObjectIdentity
mdsEventMIBObjects = _MdsEventMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1)
)
_MdsEventVariables_ObjectIdentity = ObjectIdentity
mdsEventVariables = _MdsEventVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1)
)


class _MdsEventName_Type(OctetString):
    """Custom type mdsEventName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MdsEventName_Type.__name__ = "OctetString"
_MdsEventName_Object = MibScalar
mdsEventName = _MdsEventName_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1, 1),
    _MdsEventName_Type()
)
mdsEventName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdsEventName.setStatus("current")


class _MdsEventInfoInCee_Type(OctetString):
    """Custom type mdsEventInfoInCee based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_MdsEventInfoInCee_Type.__name__ = "OctetString"
_MdsEventInfoInCee_Object = MibScalar
mdsEventInfoInCee = _MdsEventInfoInCee_Object(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1, 2),
    _MdsEventInfoInCee_Type()
)
mdsEventInfoInCee.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdsEventInfoInCee.setStatus("current")
_MdsEventMIBNotifications_ObjectIdentity = ObjectIdentity
mdsEventMIBNotifications = _MdsEventMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2)
)
_Traps0_ObjectIdentity = ObjectIdentity
traps0 = _Traps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1, 0)
)
_MdsEventMIBConformance_ObjectIdentity = ObjectIdentity
mdsEventMIBConformance = _MdsEventMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3)
)
_MdsEventMIBCompliances_ObjectIdentity = ObjectIdentity
mdsEventMIBCompliances = _MdsEventMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 1)
)
_MdsEventMIBGroups_ObjectIdentity = ObjectIdentity
mdsEventMIBGroups = _MdsEventMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2)
)

# Managed Objects groups

mdsEventVariablesCeeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2, 2)
)
mdsEventVariablesCeeGroup.setObjects(
      *(("MDS-EVENT-MIB", "mdsEventName"),
        ("MDS-EVENT-MIB", "mdsEventInfoInCee"))
)
if mibBuilder.loadTexts:
    mdsEventVariablesCeeGroup.setStatus("current")


# Notification objects

mdsEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1, 0, 1)
)
if mibBuilder.loadTexts:
    mdsEvent.setStatus(
        "current"
    )


# Notifications groups

mdsEventNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2, 1)
)
mdsEventNotificationsGroup.setObjects(
    ("MDS-EVENT-MIB", "mdsEvent")
)
if mibBuilder.loadTexts:
    mdsEventNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mdsEventMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 1, 2)
)
mdsEventMIBCompliance.setObjects(
      *(("MDS-EVENT-MIB", "mdsEventNotificationsGroup"),
        ("MDS-EVENT-MIB", "mdsEventVariablesCeeGroup"))
)
if mibBuilder.loadTexts:
    mdsEventMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MDS-EVENT-MIB",
    **{"mdsEventMIB": mdsEventMIB,
       "mdsEventMIBObjects": mdsEventMIBObjects,
       "mdsEventVariables": mdsEventVariables,
       "mdsEventName": mdsEventName,
       "mdsEventInfoInCee": mdsEventInfoInCee,
       "mdsEventMIBNotifications": mdsEventMIBNotifications,
       "traps0": traps0,
       "traps": traps,
       "mdsEvent": mdsEvent,
       "mdsEventMIBConformance": mdsEventMIBConformance,
       "mdsEventMIBCompliances": mdsEventMIBCompliances,
       "mdsEventMIBCompliance": mdsEventMIBCompliance,
       "mdsEventMIBGroups": mdsEventMIBGroups,
       "mdsEventNotificationsGroup": mdsEventNotificationsGroup,
       "mdsEventVariablesCeeGroup": mdsEventVariablesCeeGroup}
)
