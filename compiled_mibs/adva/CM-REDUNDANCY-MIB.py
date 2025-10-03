# SNMP MIB module (CM-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-REDUNDANCY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:04 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(CardType,
 neIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "CardType",
    "neIndex")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

cmRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15)
)
if mibBuilder.loadTexts:
    cmRedundancyMIB.setRevisions(
        ("2009-02-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CmRedundancyArch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadbalance", 1),
          ("activestandby", 2))
    )



class CmRedundancyStandbyMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("warm", 2),
          ("hot", 3))
    )



class CmRedundancyState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class CmRedundancySyncStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("out-of-synchronize", 2),
          ("bulk-synchronize", 3),
          ("incremental-synchronize", 4))
    )



class CmRedundancySwitchOverReason(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("latestUpdatedData", 2),
          ("userTrigger", 3),
          ("cardReset", 4),
          ("cardRemoval", 5),
          ("softwareFailure", 6),
          ("hardwareFailure", 7))
    )



class CmRedundancySyncMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatically", 1),
          ("manually", 2))
    )



class CmRedundancyAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("force", 1),
          ("manual", 2),
          ("releaseforce", 3))
    )



class CmRedundancyUnitState(TextualConvention, Integer32):
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
        *(("none", 1),
          ("normal", 2),
          ("maintenance", 3),
          ("faultisolation", 4),
          ("lock", 5),
          ("extracted", 6),
          ("init", 7),
          ("stanbdby", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CmRedundancyObjects_ObjectIdentity = ObjectIdentity
cmRedundancyObjects = _CmRedundancyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1)
)
_CmRedundancyGroupTable_Object = MibTable
cmRedundancyGroupTable = _CmRedundancyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1)
)
if mibBuilder.loadTexts:
    cmRedundancyGroupTable.setStatus("current")
_CmRedundancyGroupEntry_Object = MibTableRow
cmRedundancyGroupEntry = _CmRedundancyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1)
)
cmRedundancyGroupEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-REDUNDANCY-MIB", "cmRedundancyGroupIndex"),
)
if mibBuilder.loadTexts:
    cmRedundancyGroupEntry.setStatus("current")
_CmRedundancyGroupIndex_Type = Integer32
_CmRedundancyGroupIndex_Object = MibTableColumn
cmRedundancyGroupIndex = _CmRedundancyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 1),
    _CmRedundancyGroupIndex_Type()
)
cmRedundancyGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupIndex.setStatus("current")


class _CmRedundancyGroupUserLabel_Type(DisplayString):
    """Custom type cmRedundancyGroupUserLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmRedundancyGroupUserLabel_Type.__name__ = "DisplayString"
_CmRedundancyGroupUserLabel_Object = MibTableColumn
cmRedundancyGroupUserLabel = _CmRedundancyGroupUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 2),
    _CmRedundancyGroupUserLabel_Type()
)
cmRedundancyGroupUserLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmRedundancyGroupUserLabel.setStatus("current")
_CmRedundancyGroupType_Type = CardType
_CmRedundancyGroupType_Object = MibTableColumn
cmRedundancyGroupType = _CmRedundancyGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 3),
    _CmRedundancyGroupType_Type()
)
cmRedundancyGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupType.setStatus("current")
_CmRedundancyGroupSyncEnabled_Type = TruthValue
_CmRedundancyGroupSyncEnabled_Object = MibTableColumn
cmRedundancyGroupSyncEnabled = _CmRedundancyGroupSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 4),
    _CmRedundancyGroupSyncEnabled_Type()
)
cmRedundancyGroupSyncEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRedundancyGroupSyncEnabled.setStatus("current")
_CmRedundancyGroupActiveCard_Type = VariablePointer
_CmRedundancyGroupActiveCard_Object = MibTableColumn
cmRedundancyGroupActiveCard = _CmRedundancyGroupActiveCard_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 5),
    _CmRedundancyGroupActiveCard_Type()
)
cmRedundancyGroupActiveCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupActiveCard.setStatus("current")
_CmRedundancyGroupActiveCardState_Type = CmRedundancyUnitState
_CmRedundancyGroupActiveCardState_Object = MibTableColumn
cmRedundancyGroupActiveCardState = _CmRedundancyGroupActiveCardState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 6),
    _CmRedundancyGroupActiveCardState_Type()
)
cmRedundancyGroupActiveCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupActiveCardState.setStatus("current")
_CmRedundancyGroupStandbyCard_Type = VariablePointer
_CmRedundancyGroupStandbyCard_Object = MibTableColumn
cmRedundancyGroupStandbyCard = _CmRedundancyGroupStandbyCard_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 7),
    _CmRedundancyGroupStandbyCard_Type()
)
cmRedundancyGroupStandbyCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupStandbyCard.setStatus("current")
_CmRedundancyGroupStandbyCardState_Type = CmRedundancyUnitState
_CmRedundancyGroupStandbyCardState_Object = MibTableColumn
cmRedundancyGroupStandbyCardState = _CmRedundancyGroupStandbyCardState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 8),
    _CmRedundancyGroupStandbyCardState_Type()
)
cmRedundancyGroupStandbyCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupStandbyCardState.setStatus("current")
_CmRedundancyGroupLastSwitchOverTime_Type = TimeTicks
_CmRedundancyGroupLastSwitchOverTime_Object = MibTableColumn
cmRedundancyGroupLastSwitchOverTime = _CmRedundancyGroupLastSwitchOverTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 9),
    _CmRedundancyGroupLastSwitchOverTime_Type()
)
cmRedundancyGroupLastSwitchOverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupLastSwitchOverTime.setStatus("current")
_CmRedundancyGroupLastSwitchOverReason_Type = CmRedundancySwitchOverReason
_CmRedundancyGroupLastSwitchOverReason_Object = MibTableColumn
cmRedundancyGroupLastSwitchOverReason = _CmRedundancyGroupLastSwitchOverReason_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 10),
    _CmRedundancyGroupLastSwitchOverReason_Type()
)
cmRedundancyGroupLastSwitchOverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupLastSwitchOverReason.setStatus("current")
_CmRedundancyGroupState_Type = CmRedundancyState
_CmRedundancyGroupState_Object = MibTableColumn
cmRedundancyGroupState = _CmRedundancyGroupState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 11),
    _CmRedundancyGroupState_Type()
)
cmRedundancyGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupState.setStatus("current")
_CmRedundancyGroupSyncStatus_Type = CmRedundancySyncStatus
_CmRedundancyGroupSyncStatus_Object = MibTableColumn
cmRedundancyGroupSyncStatus = _CmRedundancyGroupSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 12),
    _CmRedundancyGroupSyncStatus_Type()
)
cmRedundancyGroupSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRedundancyGroupSyncStatus.setStatus("current")
_CmRedundancyGroupAction_Type = CmRedundancyAction
_CmRedundancyGroupAction_Object = MibTableColumn
cmRedundancyGroupAction = _CmRedundancyGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 1, 1, 1, 13),
    _CmRedundancyGroupAction_Type()
)
cmRedundancyGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRedundancyGroupAction.setStatus("current")
_CmRedundancyNotifications_ObjectIdentity = ObjectIdentity
cmRedundancyNotifications = _CmRedundancyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 2)
)
_CmRedundancyConformance_ObjectIdentity = ObjectIdentity
cmRedundancyConformance = _CmRedundancyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3)
)
_CmRedundancyCompliances_ObjectIdentity = ObjectIdentity
cmRedundancyCompliances = _CmRedundancyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 1)
)
_CmRedundancyGroups_ObjectIdentity = ObjectIdentity
cmRedundancyGroups = _CmRedundancyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 2)
)

# Managed Objects groups

cmRedundancyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 2, 1)
)
cmRedundancyObjectGroup.setObjects(
      *(("CM-REDUNDANCY-MIB", "cmRedundancyGroupIndex"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupUserLabel"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupType"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupSyncEnabled"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupActiveCard"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupActiveCardState"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupStandbyCard"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupStandbyCardState"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupLastSwitchOverTime"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupLastSwitchOverReason"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupState"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupSyncStatus"),
        ("CM-REDUNDANCY-MIB", "cmRedundancyGroupAction"))
)
if mibBuilder.loadTexts:
    cmRedundancyObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmRedundancyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 15, 3, 1, 1)
)
cmRedundancyCompliance.setObjects(
    ("CM-REDUNDANCY-MIB", "cmRedundancyObjectGroup")
)
if mibBuilder.loadTexts:
    cmRedundancyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-REDUNDANCY-MIB",
    **{"CmRedundancyArch": CmRedundancyArch,
       "CmRedundancyStandbyMode": CmRedundancyStandbyMode,
       "CmRedundancyState": CmRedundancyState,
       "CmRedundancySyncStatus": CmRedundancySyncStatus,
       "CmRedundancySwitchOverReason": CmRedundancySwitchOverReason,
       "CmRedundancySyncMode": CmRedundancySyncMode,
       "CmRedundancyAction": CmRedundancyAction,
       "CmRedundancyUnitState": CmRedundancyUnitState,
       "cmRedundancyMIB": cmRedundancyMIB,
       "cmRedundancyObjects": cmRedundancyObjects,
       "cmRedundancyGroupTable": cmRedundancyGroupTable,
       "cmRedundancyGroupEntry": cmRedundancyGroupEntry,
       "cmRedundancyGroupIndex": cmRedundancyGroupIndex,
       "cmRedundancyGroupUserLabel": cmRedundancyGroupUserLabel,
       "cmRedundancyGroupType": cmRedundancyGroupType,
       "cmRedundancyGroupSyncEnabled": cmRedundancyGroupSyncEnabled,
       "cmRedundancyGroupActiveCard": cmRedundancyGroupActiveCard,
       "cmRedundancyGroupActiveCardState": cmRedundancyGroupActiveCardState,
       "cmRedundancyGroupStandbyCard": cmRedundancyGroupStandbyCard,
       "cmRedundancyGroupStandbyCardState": cmRedundancyGroupStandbyCardState,
       "cmRedundancyGroupLastSwitchOverTime": cmRedundancyGroupLastSwitchOverTime,
       "cmRedundancyGroupLastSwitchOverReason": cmRedundancyGroupLastSwitchOverReason,
       "cmRedundancyGroupState": cmRedundancyGroupState,
       "cmRedundancyGroupSyncStatus": cmRedundancyGroupSyncStatus,
       "cmRedundancyGroupAction": cmRedundancyGroupAction,
       "cmRedundancyNotifications": cmRedundancyNotifications,
       "cmRedundancyConformance": cmRedundancyConformance,
       "cmRedundancyCompliances": cmRedundancyCompliances,
       "cmRedundancyCompliance": cmRedundancyCompliance,
       "cmRedundancyGroups": cmRedundancyGroups,
       "cmRedundancyObjectGroup": cmRedundancyObjectGroup}
)
