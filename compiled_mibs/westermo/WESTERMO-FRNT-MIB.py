# SNMP MIB module (WESTERMO-FRNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\westermo\WESTERMO-FRNT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:04 2025
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

(IfaceRefIndex,) = mibBuilder.importSymbols(
    "WESTERMO-INTERFACE-MIB",
    "IfaceRefIndex")

(common,) = mibBuilder.importSymbols(
    "WESTERMO-OID-MIB",
    "common")


# MODULE-IDENTITY

frnt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5)
)
if mibBuilder.loadTexts:
    frnt.setRevisions(
        ("2019-08-30 00:00",
         "2019-12-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrntObjects_ObjectIdentity = ObjectIdentity
frntObjects = _FrntObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1)
)
_FrntStatusTable_Object = MibTable
frntStatusTable = _FrntStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    frntStatusTable.setStatus("current")
_FrntStatusEntry_Object = MibTableRow
frntStatusEntry = _FrntStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1)
)
frntStatusEntry.setIndexNames(
    (0, "WESTERMO-FRNT-MIB", "frntStatusVersion"),
    (0, "WESTERMO-FRNT-MIB", "frntStatusInstance"),
)
if mibBuilder.loadTexts:
    frntStatusEntry.setStatus("current")


class _FrntStatusVersion_Type(Integer32):
    """Custom type frntStatusVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v0", 0),
          ("v2", 2))
    )


_FrntStatusVersion_Type.__name__ = "Integer32"
_FrntStatusVersion_Object = MibTableColumn
frntStatusVersion = _FrntStatusVersion_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 1),
    _FrntStatusVersion_Type()
)
frntStatusVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frntStatusVersion.setStatus("current")


class _FrntStatusInstance_Type(Integer32):
    """Custom type frntStatusInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FrntStatusInstance_Type.__name__ = "Integer32"
_FrntStatusInstance_Object = MibTableColumn
frntStatusInstance = _FrntStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 2),
    _FrntStatusInstance_Type()
)
frntStatusInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frntStatusInstance.setStatus("current")
_FrntStatusRingId_Type = Integer32
_FrntStatusRingId_Object = MibTableColumn
frntStatusRingId = _FrntStatusRingId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 3),
    _FrntStatusRingId_Type()
)
frntStatusRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusRingId.setStatus("current")


class _FrntStatusDeviceMode_Type(Integer32):
    """Custom type frntStatusDeviceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("member", 1),
          ("focalPoint", 2))
    )


_FrntStatusDeviceMode_Type.__name__ = "Integer32"
_FrntStatusDeviceMode_Object = MibTableColumn
frntStatusDeviceMode = _FrntStatusDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 4),
    _FrntStatusDeviceMode_Type()
)
frntStatusDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusDeviceMode.setStatus("current")


class _FrntStatusRingStatus_Type(Integer32):
    """Custom type frntStatusRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("broken", 0),
          ("ok", 1))
    )


_FrntStatusRingStatus_Type.__name__ = "Integer32"
_FrntStatusRingStatus_Object = MibTableColumn
frntStatusRingStatus = _FrntStatusRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 5),
    _FrntStatusRingStatus_Type()
)
frntStatusRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusRingStatus.setStatus("current")
_FrntStatusPort1_Type = IfaceRefIndex
_FrntStatusPort1_Object = MibTableColumn
frntStatusPort1 = _FrntStatusPort1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 6),
    _FrntStatusPort1_Type()
)
frntStatusPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusPort1.setStatus("current")
_FrntStatusPort2_Type = IfaceRefIndex
_FrntStatusPort2_Object = MibTableColumn
frntStatusPort2 = _FrntStatusPort2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 7),
    _FrntStatusPort2_Type()
)
frntStatusPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusPort2.setStatus("current")
_FrntStatusBlockingPort_Type = IfaceRefIndex
_FrntStatusBlockingPort_Object = MibTableColumn
frntStatusBlockingPort = _FrntStatusBlockingPort_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 8),
    _FrntStatusBlockingPort_Type()
)
frntStatusBlockingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusBlockingPort.setStatus("current")
_FrntStatusVid1_Type = Integer32
_FrntStatusVid1_Object = MibTableColumn
frntStatusVid1 = _FrntStatusVid1_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 9),
    _FrntStatusVid1_Type()
)
frntStatusVid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusVid1.setStatus("current")
_FrntStatusVid2_Type = Integer32
_FrntStatusVid2_Object = MibTableColumn
frntStatusVid2 = _FrntStatusVid2_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 10),
    _FrntStatusVid2_Type()
)
frntStatusVid2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusVid2.setStatus("current")
_FrntStatusTopologyChangeCount_Type = Integer32
_FrntStatusTopologyChangeCount_Object = MibTableColumn
frntStatusTopologyChangeCount = _FrntStatusTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 11),
    _FrntStatusTopologyChangeCount_Type()
)
frntStatusTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusTopologyChangeCount.setStatus("current")
_FrntStatusTimeSinceLastChange_Type = TimeTicks
_FrntStatusTimeSinceLastChange_Object = MibTableColumn
frntStatusTimeSinceLastChange = _FrntStatusTimeSinceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 1, 1, 12),
    _FrntStatusTimeSinceLastChange_Type()
)
frntStatusTimeSinceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntStatusTimeSinceLastChange.setStatus("current")
_FrntPortStatusTable_Object = MibTable
frntPortStatusTable = _FrntPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    frntPortStatusTable.setStatus("current")
_FrntPortStatusEntry_Object = MibTableRow
frntPortStatusEntry = _FrntPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 2, 1)
)
frntPortStatusEntry.setIndexNames(
    (0, "WESTERMO-FRNT-MIB", "frntPortStatusFrntRingId"),
    (0, "WESTERMO-FRNT-MIB", "frntPortStatusRefIndex"),
)
if mibBuilder.loadTexts:
    frntPortStatusEntry.setStatus("current")


class _FrntPortStatusFrntRingId_Type(Integer32):
    """Custom type frntPortStatusFrntRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_FrntPortStatusFrntRingId_Type.__name__ = "Integer32"
_FrntPortStatusFrntRingId_Object = MibTableColumn
frntPortStatusFrntRingId = _FrntPortStatusFrntRingId_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 2, 1, 1),
    _FrntPortStatusFrntRingId_Type()
)
frntPortStatusFrntRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frntPortStatusFrntRingId.setStatus("current")
_FrntPortStatusRefIndex_Type = IfaceRefIndex
_FrntPortStatusRefIndex_Object = MibTableColumn
frntPortStatusRefIndex = _FrntPortStatusRefIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 2, 1, 2),
    _FrntPortStatusRefIndex_Type()
)
frntPortStatusRefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frntPortStatusRefIndex.setStatus("current")


class _FrntPortStatusAdminState_Type(Integer32):
    """Custom type frntPortStatusAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_FrntPortStatusAdminState_Type.__name__ = "Integer32"
_FrntPortStatusAdminState_Object = MibTableColumn
frntPortStatusAdminState = _FrntPortStatusAdminState_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 2, 1, 3),
    _FrntPortStatusAdminState_Type()
)
frntPortStatusAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntPortStatusAdminState.setStatus("current")


class _FrntPortStatusOperState_Type(Integer32):
    """Custom type frntPortStatusOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("disabled", 1),
          ("down", 2),
          ("notQualified", 3),
          ("qualified", 4),
          ("forwarding", 5))
    )


_FrntPortStatusOperState_Type.__name__ = "Integer32"
_FrntPortStatusOperState_Object = MibTableColumn
frntPortStatusOperState = _FrntPortStatusOperState_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 2, 1, 4),
    _FrntPortStatusOperState_Type()
)
frntPortStatusOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntPortStatusOperState.setStatus("current")


class _FrntPortStatusLinkState_Type(Integer32):
    """Custom type frntPortStatusLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )


_FrntPortStatusLinkState_Type.__name__ = "Integer32"
_FrntPortStatusLinkState_Object = MibTableColumn
frntPortStatusLinkState = _FrntPortStatusLinkState_Object(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 1, 2, 1, 5),
    _FrntPortStatusLinkState_Type()
)
frntPortStatusLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frntPortStatusLinkState.setStatus("current")
_FrntConformance_ObjectIdentity = ObjectIdentity
frntConformance = _FrntConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 2)
)
_FrntGroups_ObjectIdentity = ObjectIdentity
frntGroups = _FrntGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 2, 1)
)
_FrntCompliances_ObjectIdentity = ObjectIdentity
frntCompliances = _FrntCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 2, 2)
)
_FrntNotifications_ObjectIdentity = ObjectIdentity
frntNotifications = _FrntNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 3)
)
_FrntNotificationPrefix_ObjectIdentity = ObjectIdentity
frntNotificationPrefix = _FrntNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 3, 0)
)

# Managed Objects groups

frntStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 2, 1, 1)
)
frntStatusGroup.setObjects(
      *(("WESTERMO-FRNT-MIB", "frntStatusRingId"),
        ("WESTERMO-FRNT-MIB", "frntStatusDeviceMode"),
        ("WESTERMO-FRNT-MIB", "frntStatusRingStatus"),
        ("WESTERMO-FRNT-MIB", "frntStatusPort1"),
        ("WESTERMO-FRNT-MIB", "frntStatusPort2"),
        ("WESTERMO-FRNT-MIB", "frntStatusBlockingPort"),
        ("WESTERMO-FRNT-MIB", "frntStatusVid1"),
        ("WESTERMO-FRNT-MIB", "frntStatusVid2"),
        ("WESTERMO-FRNT-MIB", "frntStatusTopologyChangeCount"),
        ("WESTERMO-FRNT-MIB", "frntStatusTimeSinceLastChange"))
)
if mibBuilder.loadTexts:
    frntStatusGroup.setStatus("current")

frntPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 2, 1, 2)
)
frntPortStatusGroup.setObjects(
      *(("WESTERMO-FRNT-MIB", "frntPortStatusAdminState"),
        ("WESTERMO-FRNT-MIB", "frntPortStatusOperState"),
        ("WESTERMO-FRNT-MIB", "frntPortStatusLinkState"))
)
if mibBuilder.loadTexts:
    frntPortStatusGroup.setStatus("current")


# Notification objects

frntRingOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 3, 0, 1)
)
frntRingOK.setObjects(
      *(("WESTERMO-FRNT-MIB", "frntStatusRingId"),
        ("WESTERMO-FRNT-MIB", "frntStatusRingStatus"),
        ("WESTERMO-FRNT-MIB", "frntStatusDeviceMode"),
        ("WESTERMO-FRNT-MIB", "frntStatusPort1"),
        ("WESTERMO-FRNT-MIB", "frntStatusPort2"))
)
if mibBuilder.loadTexts:
    frntRingOK.setStatus(
        "current"
    )

frntRingBroken = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 3, 0, 2)
)
frntRingBroken.setObjects(
      *(("WESTERMO-FRNT-MIB", "frntStatusRingId"),
        ("WESTERMO-FRNT-MIB", "frntStatusRingStatus"),
        ("WESTERMO-FRNT-MIB", "frntStatusDeviceMode"),
        ("WESTERMO-FRNT-MIB", "frntStatusPort1"),
        ("WESTERMO-FRNT-MIB", "frntStatusPort2"))
)
if mibBuilder.loadTexts:
    frntRingBroken.setStatus(
        "current"
    )


# Notifications groups

frntNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 2, 1, 3)
)
frntNotificationsGroup.setObjects(
      *(("WESTERMO-FRNT-MIB", "frntRingOK"),
        ("WESTERMO-FRNT-MIB", "frntRingBroken"))
)
if mibBuilder.loadTexts:
    frntNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

frntCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 16177, 2, 5, 2, 2, 1)
)
frntCompliance.setObjects(
      *(("WESTERMO-FRNT-MIB", "frntStatusGroup"),
        ("WESTERMO-FRNT-MIB", "frntPortStatusGroup"),
        ("WESTERMO-FRNT-MIB", "frntNotificationsGroup"))
)
if mibBuilder.loadTexts:
    frntCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-FRNT-MIB",
    **{"frnt": frnt,
       "frntObjects": frntObjects,
       "frntStatusTable": frntStatusTable,
       "frntStatusEntry": frntStatusEntry,
       "frntStatusVersion": frntStatusVersion,
       "frntStatusInstance": frntStatusInstance,
       "frntStatusRingId": frntStatusRingId,
       "frntStatusDeviceMode": frntStatusDeviceMode,
       "frntStatusRingStatus": frntStatusRingStatus,
       "frntStatusPort1": frntStatusPort1,
       "frntStatusPort2": frntStatusPort2,
       "frntStatusBlockingPort": frntStatusBlockingPort,
       "frntStatusVid1": frntStatusVid1,
       "frntStatusVid2": frntStatusVid2,
       "frntStatusTopologyChangeCount": frntStatusTopologyChangeCount,
       "frntStatusTimeSinceLastChange": frntStatusTimeSinceLastChange,
       "frntPortStatusTable": frntPortStatusTable,
       "frntPortStatusEntry": frntPortStatusEntry,
       "frntPortStatusFrntRingId": frntPortStatusFrntRingId,
       "frntPortStatusRefIndex": frntPortStatusRefIndex,
       "frntPortStatusAdminState": frntPortStatusAdminState,
       "frntPortStatusOperState": frntPortStatusOperState,
       "frntPortStatusLinkState": frntPortStatusLinkState,
       "frntConformance": frntConformance,
       "frntGroups": frntGroups,
       "frntStatusGroup": frntStatusGroup,
       "frntPortStatusGroup": frntPortStatusGroup,
       "frntNotificationsGroup": frntNotificationsGroup,
       "frntCompliances": frntCompliances,
       "frntCompliance": frntCompliance,
       "frntNotifications": frntNotifications,
       "frntNotificationPrefix": frntNotificationPrefix,
       "frntRingOK": frntRingOK,
       "frntRingBroken": frntRingBroken}
)
