# SNMP MIB module (BCN-HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecatnetworks\BCN-HA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:26 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

bcnHaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    bcnHaMIB.setRevisions(
        ("2010-12-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BcnHa_ObjectIdentity = ObjectIdentity
bcnHa = _BcnHa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5)
)
_BcnHaObjects_ObjectIdentity = ObjectIdentity
bcnHaObjects = _BcnHaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2)
)
_BcnHaServiceStatus_ObjectIdentity = ObjectIdentity
bcnHaServiceStatus = _BcnHaServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    bcnHaServiceStatus.setStatus("current")


class _BcnHaSerOperState_Type(Integer32):
    """Custom type bcnHaSerOperState based on Integer32"""
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
        *(("standalone", 1),
          ("active", 2),
          ("passive", 3),
          ("stopped", 4),
          ("stopping", 5),
          ("becomingActive", 6),
          ("becomingPassive", 7),
          ("fault", 8))
    )


_BcnHaSerOperState_Type.__name__ = "Integer32"
_BcnHaSerOperState_Object = MibScalar
bcnHaSerOperState = _BcnHaSerOperState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 1),
    _BcnHaSerOperState_Type()
)
bcnHaSerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnHaSerOperState.setStatus("current")


class _BcnHaSerReplicationState_Type(Integer32):
    """Custom type bcnHaSerReplicationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 1),
          ("replicating", 2),
          ("synchronized", 3))
    )


_BcnHaSerReplicationState_Type.__name__ = "Integer32"
_BcnHaSerReplicationState_Object = MibScalar
bcnHaSerReplicationState = _BcnHaSerReplicationState_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 2),
    _BcnHaSerReplicationState_Type()
)
bcnHaSerReplicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnHaSerReplicationState.setStatus("current")
_BcnHaSerAddressTable_Object = MibTable
bcnHaSerAddressTable = _BcnHaSerAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    bcnHaSerAddressTable.setStatus("current")
_BcnHaSerAddressEntry_Object = MibTableRow
bcnHaSerAddressEntry = _BcnHaSerAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1)
)
bcnHaSerAddressEntry.setIndexNames(
    (0, "BCN-HA-MIB", "bcnHaSerAddrTableIndex"),
)
if mibBuilder.loadTexts:
    bcnHaSerAddressEntry.setStatus("current")
_BcnHaSerAddrTableIndex_Type = Unsigned32
_BcnHaSerAddrTableIndex_Object = MibTableColumn
bcnHaSerAddrTableIndex = _BcnHaSerAddrTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 1),
    _BcnHaSerAddrTableIndex_Type()
)
bcnHaSerAddrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcnHaSerAddrTableIndex.setStatus("current")
_BcnHaSerVirtualAddressType_Type = InetAddressType
_BcnHaSerVirtualAddressType_Object = MibTableColumn
bcnHaSerVirtualAddressType = _BcnHaSerVirtualAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 2),
    _BcnHaSerVirtualAddressType_Type()
)
bcnHaSerVirtualAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnHaSerVirtualAddressType.setStatus("current")
_BcnHaSerVirtualAddress_Type = InetAddress
_BcnHaSerVirtualAddress_Object = MibTableColumn
bcnHaSerVirtualAddress = _BcnHaSerVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 3),
    _BcnHaSerVirtualAddress_Type()
)
bcnHaSerVirtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnHaSerVirtualAddress.setStatus("current")
_BcnHaSerPhysicalAddressType_Type = InetAddressType
_BcnHaSerPhysicalAddressType_Object = MibTableColumn
bcnHaSerPhysicalAddressType = _BcnHaSerPhysicalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 4),
    _BcnHaSerPhysicalAddressType_Type()
)
bcnHaSerPhysicalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnHaSerPhysicalAddressType.setStatus("current")
_BcnHaSerPhysicalAddress_Type = InetAddress
_BcnHaSerPhysicalAddress_Object = MibTableColumn
bcnHaSerPhysicalAddress = _BcnHaSerPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 5),
    _BcnHaSerPhysicalAddress_Type()
)
bcnHaSerPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnHaSerPhysicalAddress.setStatus("current")
_BcnHaSerPeerAddressType_Type = InetAddressType
_BcnHaSerPeerAddressType_Object = MibTableColumn
bcnHaSerPeerAddressType = _BcnHaSerPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 6),
    _BcnHaSerPeerAddressType_Type()
)
bcnHaSerPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnHaSerPeerAddressType.setStatus("current")
_BcnHaSerPeerAddress_Type = InetAddress
_BcnHaSerPeerAddress_Object = MibTableColumn
bcnHaSerPeerAddress = _BcnHaSerPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 2, 1, 3, 1, 7),
    _BcnHaSerPeerAddress_Type()
)
bcnHaSerPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bcnHaSerPeerAddress.setStatus("current")
_BcnHaNotification_ObjectIdentity = ObjectIdentity
bcnHaNotification = _BcnHaNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3)
)
_BcnHaNotificationEvents_ObjectIdentity = ObjectIdentity
bcnHaNotificationEvents = _BcnHaNotificationEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 0)
)
_BcnHaNotificationData_ObjectIdentity = ObjectIdentity
bcnHaNotificationData = _BcnHaNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1)
)
_BcnHaAlarmSeverity_Type = BcnAlarmSeverity
_BcnHaAlarmSeverity_Object = MibScalar
bcnHaAlarmSeverity = _BcnHaAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1, 1),
    _BcnHaAlarmSeverity_Type()
)
bcnHaAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnHaAlarmSeverity.setStatus("current")
_BcnHaAlarmInfo_Type = DisplayString
_BcnHaAlarmInfo_Object = MibScalar
bcnHaAlarmInfo = _BcnHaAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 1, 2),
    _BcnHaAlarmInfo_Type()
)
bcnHaAlarmInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bcnHaAlarmInfo.setStatus("current")
_BcnHaConformance_ObjectIdentity = ObjectIdentity
bcnHaConformance = _BcnHaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4)
)
_BcnHaServiceCompliances_ObjectIdentity = ObjectIdentity
bcnHaServiceCompliances = _BcnHaServiceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 1)
)
_BcnHaServiceGroups_ObjectIdentity = ObjectIdentity
bcnHaServiceGroups = _BcnHaServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2)
)

# Managed Objects groups

bcnHaServiceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 1)
)
bcnHaServiceStatusGroup.setObjects(
      *(("BCN-HA-MIB", "bcnHaSerOperState"),
        ("BCN-HA-MIB", "bcnHaSerReplicationState"),
        ("BCN-HA-MIB", "bcnHaSerVirtualAddressType"),
        ("BCN-HA-MIB", "bcnHaSerVirtualAddress"),
        ("BCN-HA-MIB", "bcnHaSerPhysicalAddressType"),
        ("BCN-HA-MIB", "bcnHaSerPhysicalAddress"),
        ("BCN-HA-MIB", "bcnHaSerPeerAddressType"),
        ("BCN-HA-MIB", "bcnHaSerPeerAddress"))
)
if mibBuilder.loadTexts:
    bcnHaServiceStatusGroup.setStatus("current")

bcnHaNotificationDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 3)
)
bcnHaNotificationDataGroup.setObjects(
      *(("BCN-HA-MIB", "bcnHaAlarmSeverity"),
        ("BCN-HA-MIB", "bcnHaAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnHaNotificationDataGroup.setStatus("current")


# Notification objects

bcnHaAlarmNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 3, 0, 1)
)
bcnHaAlarmNotif.setObjects(
      *(("BCN-HA-MIB", "bcnHaSerOperState"),
        ("BCN-HA-MIB", "bcnHaAlarmSeverity"),
        ("BCN-HA-MIB", "bcnHaAlarmInfo"))
)
if mibBuilder.loadTexts:
    bcnHaAlarmNotif.setStatus(
        "current"
    )


# Notifications groups

bcnHaNotificationEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 2, 2)
)
bcnHaNotificationEventGroup.setObjects(
    ("BCN-HA-MIB", "bcnHaAlarmNotif")
)
if mibBuilder.loadTexts:
    bcnHaNotificationEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bcnHaStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13315, 3, 1, 5, 4, 1, 1)
)
bcnHaStatusCompliance.setObjects(
      *(("BCN-HA-MIB", "bcnHaServiceStatusGroup"),
        ("BCN-HA-MIB", "bcnHaNotificationEventGroup"),
        ("BCN-HA-MIB", "bcnHaNotificationDataGroup"))
)
if mibBuilder.loadTexts:
    bcnHaStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BCN-HA-MIB",
    **{"bcnHa": bcnHa,
       "bcnHaMIB": bcnHaMIB,
       "bcnHaObjects": bcnHaObjects,
       "bcnHaServiceStatus": bcnHaServiceStatus,
       "bcnHaSerOperState": bcnHaSerOperState,
       "bcnHaSerReplicationState": bcnHaSerReplicationState,
       "bcnHaSerAddressTable": bcnHaSerAddressTable,
       "bcnHaSerAddressEntry": bcnHaSerAddressEntry,
       "bcnHaSerAddrTableIndex": bcnHaSerAddrTableIndex,
       "bcnHaSerVirtualAddressType": bcnHaSerVirtualAddressType,
       "bcnHaSerVirtualAddress": bcnHaSerVirtualAddress,
       "bcnHaSerPhysicalAddressType": bcnHaSerPhysicalAddressType,
       "bcnHaSerPhysicalAddress": bcnHaSerPhysicalAddress,
       "bcnHaSerPeerAddressType": bcnHaSerPeerAddressType,
       "bcnHaSerPeerAddress": bcnHaSerPeerAddress,
       "bcnHaNotification": bcnHaNotification,
       "bcnHaNotificationEvents": bcnHaNotificationEvents,
       "bcnHaAlarmNotif": bcnHaAlarmNotif,
       "bcnHaNotificationData": bcnHaNotificationData,
       "bcnHaAlarmSeverity": bcnHaAlarmSeverity,
       "bcnHaAlarmInfo": bcnHaAlarmInfo,
       "bcnHaConformance": bcnHaConformance,
       "bcnHaServiceCompliances": bcnHaServiceCompliances,
       "bcnHaStatusCompliance": bcnHaStatusCompliance,
       "bcnHaServiceGroups": bcnHaServiceGroups,
       "bcnHaServiceStatusGroup": bcnHaServiceStatusGroup,
       "bcnHaNotificationEventGroup": bcnHaNotificationEventGroup,
       "bcnHaNotificationDataGroup": bcnHaNotificationDataGroup}
)
