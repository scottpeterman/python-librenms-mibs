# SNMP MIB module (DELL-NETWORKING-MAC-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\DELL-NETWORKING-MAC-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:35:45 2025
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dellNetMacNotifMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28)
)
if mibBuilder.loadTexts:
    dellNetMacNotifMib.setRevisions(
        ("2017-01-01 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetMacNotificationObjects_ObjectIdentity = ObjectIdentity
dellNetMacNotificationObjects = _DellNetMacNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1)
)
_DellNetMacNotificationTraps_ObjectIdentity = ObjectIdentity
dellNetMacNotificationTraps = _DellNetMacNotificationTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 1)
)
_MacAddress_Type = MacAddress
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 2),
    _MacAddress_Type()
)
macAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_VlanId_Type = VlanId
_VlanId_Object = MibScalar
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 3),
    _VlanId_Type()
)
vlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")


class _PortId_Type(Integer32):
    """Custom type portId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortId_Type.__name__ = "Integer32"
_PortId_Object = MibScalar
portId = _PortId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 4),
    _PortId_Type()
)
portId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portId.setStatus("current")


class _NewPortId_Type(Integer32):
    """Custom type newPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NewPortId_Type.__name__ = "Integer32"
_NewPortId_Object = MibScalar
newPortId = _NewPortId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 5),
    _NewPortId_Type()
)
newPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    newPortId.setStatus("current")
_TimeStamp_Type = TimeTicks
_TimeStamp_Object = MibScalar
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 6),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timeStamp.setStatus("current")
_Message_Type = OctetString
_Message_Object = MibScalar
message = _Message_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 7),
    _Message_Type()
)
message.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    message.setStatus("current")
_DellNetMacMibConformance_ObjectIdentity = ObjectIdentity
dellNetMacMibConformance = _DellNetMacMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 2)
)
_DellNetMacMibCompliances_ObjectIdentity = ObjectIdentity
dellNetMacMibCompliances = _DellNetMacMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 2, 1)
)
_DellNetMacMibGroups_ObjectIdentity = ObjectIdentity
dellNetMacMibGroups = _DellNetMacMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 2, 2)
)

# Managed Objects groups


# Notification objects

macLearnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 1, 1)
)
macLearnNotification.setObjects(
      *(("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "macAddress"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "vlanId"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "portId"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "timeStamp"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "message"))
)
if mibBuilder.loadTexts:
    macLearnNotification.setStatus(
        "current"
    )

macMoveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 1, 1, 2)
)
macMoveNotification.setObjects(
      *(("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "macAddress"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "vlanId"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "portId"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "newPortId"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "timeStamp"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "message"))
)
if mibBuilder.loadTexts:
    macMoveNotification.setStatus(
        "current"
    )


# Notifications groups

dellNetMacNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 2, 2, 1)
)
dellNetMacNotificationGroup.setObjects(
      *(("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "macLearnNotification"),
        ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "macMoveNotification"))
)
if mibBuilder.loadTexts:
    dellNetMacNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetMacMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 28, 2, 1, 1)
)
dellNetMacMibCompliance.setObjects(
    ("DELL-NETWORKING-MAC-NOTIFICATION-MIB", "dellNetMacNotificationGroup")
)
if mibBuilder.loadTexts:
    dellNetMacMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-MAC-NOTIFICATION-MIB",
    **{"dellNetMacNotifMib": dellNetMacNotifMib,
       "dellNetMacNotificationObjects": dellNetMacNotificationObjects,
       "dellNetMacNotificationTraps": dellNetMacNotificationTraps,
       "macLearnNotification": macLearnNotification,
       "macMoveNotification": macMoveNotification,
       "macAddress": macAddress,
       "vlanId": vlanId,
       "portId": portId,
       "newPortId": newPortId,
       "timeStamp": timeStamp,
       "message": message,
       "dellNetMacMibConformance": dellNetMacMibConformance,
       "dellNetMacMibCompliances": dellNetMacMibCompliances,
       "dellNetMacMibCompliance": dellNetMacMibCompliance,
       "dellNetMacMibGroups": dellNetMacMibGroups,
       "dellNetMacNotificationGroup": dellNetMacNotificationGroup}
)
