# SNMP MIB module (BLUECOAT-SEGMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bluecoat\BLUECOAT-SEGMENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:35 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

segmentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17)
)
if mibBuilder.loadTexts:
    segmentMIB.setRevisions(
        ("2016-02-24 03:00",
         "2015-01-13 03:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SegmentMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("activeInlineFailToAppliance", 1),
          ("asymActiveInlineFailToAppliance", 2),
          ("activeInlineFailToNetwork", 3),
          ("asymActiveInlineFailToNetwork", 4),
          ("passiveInline", 5),
          ("asymPassiveInline", 6),
          ("passiveTap", 7),
          ("asymPassiveTap", 8),
          ("passiveTap2xAggrInputs", 9),
          ("passiveTap3xAggrInputs", 10))
    )



class SegmentState(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("softwareFailure", 0),
          ("manualFailure", 1),
          ("linkFailure", 2),
          ("activationFailure", 3))
    )


# MIB Managed Objects in the order of their OIDs

_SegmentMIBObjects_ObjectIdentity = ObjectIdentity
segmentMIBObjects = _SegmentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1)
)
_Segments_ObjectIdentity = ObjectIdentity
segments = _Segments_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1)
)
_SegmentStatusTable_Object = MibTable
segmentStatusTable = _SegmentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    segmentStatusTable.setStatus("current")
_SegmentStatusEntry_Object = MibTableRow
segmentStatusEntry = _SegmentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1)
)
segmentStatusEntry.setIndexNames(
    (0, "BLUECOAT-SEGMENT-MIB", "segmentStatusIndex"),
)
if mibBuilder.loadTexts:
    segmentStatusEntry.setStatus("current")


class _SegmentStatusIndex_Type(Integer32):
    """Custom type segmentStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SegmentStatusIndex_Type.__name__ = "Integer32"
_SegmentStatusIndex_Object = MibTableColumn
segmentStatusIndex = _SegmentStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 1),
    _SegmentStatusIndex_Type()
)
segmentStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    segmentStatusIndex.setStatus("current")
_SegmentStatusIdentifier_Type = DisplayString
_SegmentStatusIdentifier_Object = MibTableColumn
segmentStatusIdentifier = _SegmentStatusIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 2),
    _SegmentStatusIdentifier_Type()
)
segmentStatusIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentStatusIdentifier.setStatus("current")
_SegmentStatusMode_Type = SegmentMode
_SegmentStatusMode_Object = MibTableColumn
segmentStatusMode = _SegmentStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 3),
    _SegmentStatusMode_Type()
)
segmentStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentStatusMode.setStatus("current")


class _SegmentStatusIfList_Type(PortList):
    """Custom type segmentStatusIfList based on PortList"""
    subtypeSpec = PortList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SegmentStatusIfList_Type.__name__ = "PortList"
_SegmentStatusIfList_Object = MibTableColumn
segmentStatusIfList = _SegmentStatusIfList_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 4),
    _SegmentStatusIfList_Type()
)
segmentStatusIfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentStatusIfList.setStatus("current")


class _SegmentStatusDownIfList_Type(PortList):
    """Custom type segmentStatusDownIfList based on PortList"""
    subtypeSpec = PortList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SegmentStatusDownIfList_Type.__name__ = "PortList"
_SegmentStatusDownIfList_Object = MibTableColumn
segmentStatusDownIfList = _SegmentStatusDownIfList_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 5),
    _SegmentStatusDownIfList_Type()
)
segmentStatusDownIfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentStatusDownIfList.setStatus("current")


class _SegmentStatusCopyIfList_Type(PortList):
    """Custom type segmentStatusCopyIfList based on PortList"""
    subtypeSpec = PortList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SegmentStatusCopyIfList_Type.__name__ = "PortList"
_SegmentStatusCopyIfList_Object = MibTableColumn
segmentStatusCopyIfList = _SegmentStatusCopyIfList_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 6),
    _SegmentStatusCopyIfList_Type()
)
segmentStatusCopyIfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentStatusCopyIfList.setStatus("current")
_SegmentStatusState_Type = SegmentState
_SegmentStatusState_Object = MibTableColumn
segmentStatusState = _SegmentStatusState_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 7),
    _SegmentStatusState_Type()
)
segmentStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentStatusState.setStatus("current")
_SegmentStatusComment_Type = DisplayString
_SegmentStatusComment_Object = MibTableColumn
segmentStatusComment = _SegmentStatusComment_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 1, 1, 1, 1, 8),
    _SegmentStatusComment_Type()
)
segmentStatusComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segmentStatusComment.setStatus("current")
_SegmentMIBNotifications_ObjectIdentity = ObjectIdentity
segmentMIBNotifications = _SegmentMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 2)
)
_SegmentMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
segmentMIBNotificationsPrefix = _SegmentMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 2, 0)
)
_SegmentMIBConformance_ObjectIdentity = ObjectIdentity
segmentMIBConformance = _SegmentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 3)
)
_SegmentMIBCompliances_ObjectIdentity = ObjectIdentity
segmentMIBCompliances = _SegmentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 1)
)
_SegmentMIBGroups_ObjectIdentity = ObjectIdentity
segmentMIBGroups = _SegmentMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 2)
)
_SegmentMIBNotifGroups_ObjectIdentity = ObjectIdentity
segmentMIBNotifGroups = _SegmentMIBNotifGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 3)
)

# Managed Objects groups

segmentMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 2, 1)
)
segmentMIBGroup.setObjects(
      *(("BLUECOAT-SEGMENT-MIB", "segmentStatusIdentifier"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusMode"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusIfList"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusDownIfList"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusCopyIfList"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusState"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusComment"))
)
if mibBuilder.loadTexts:
    segmentMIBGroup.setStatus("current")


# Notification objects

segmentStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 2, 0, 1)
)
segmentStateTrap.setObjects(
      *(("BLUECOAT-SEGMENT-MIB", "segmentStatusIdentifier"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusMode"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusIfList"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusDownIfList"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusCopyIfList"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusState"),
        ("BLUECOAT-SEGMENT-MIB", "segmentStatusComment"))
)
if mibBuilder.loadTexts:
    segmentStateTrap.setStatus(
        "current"
    )


# Notifications groups

segmentMIBNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 3, 1)
)
segmentMIBNotifGroup.setObjects(
    ("BLUECOAT-SEGMENT-MIB", "segmentStateTrap")
)
if mibBuilder.loadTexts:
    segmentMIBNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

segmentMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3417, 2, 17, 3, 1, 1)
)
segmentMIBCompliance.setObjects(
    ("BLUECOAT-SEGMENT-MIB", "segmentMIBGroup")
)
if mibBuilder.loadTexts:
    segmentMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SEGMENT-MIB",
    **{"SegmentMode": SegmentMode,
       "SegmentState": SegmentState,
       "segmentMIB": segmentMIB,
       "segmentMIBObjects": segmentMIBObjects,
       "segments": segments,
       "segmentStatusTable": segmentStatusTable,
       "segmentStatusEntry": segmentStatusEntry,
       "segmentStatusIndex": segmentStatusIndex,
       "segmentStatusIdentifier": segmentStatusIdentifier,
       "segmentStatusMode": segmentStatusMode,
       "segmentStatusIfList": segmentStatusIfList,
       "segmentStatusDownIfList": segmentStatusDownIfList,
       "segmentStatusCopyIfList": segmentStatusCopyIfList,
       "segmentStatusState": segmentStatusState,
       "segmentStatusComment": segmentStatusComment,
       "segmentMIBNotifications": segmentMIBNotifications,
       "segmentMIBNotificationsPrefix": segmentMIBNotificationsPrefix,
       "segmentStateTrap": segmentStateTrap,
       "segmentMIBConformance": segmentMIBConformance,
       "segmentMIBCompliances": segmentMIBCompliances,
       "segmentMIBCompliance": segmentMIBCompliance,
       "segmentMIBGroups": segmentMIBGroups,
       "segmentMIBGroup": segmentMIBGroup,
       "segmentMIBNotifGroups": segmentMIBNotifGroups,
       "segmentMIBNotifGroup": segmentMIBNotifGroup}
)
