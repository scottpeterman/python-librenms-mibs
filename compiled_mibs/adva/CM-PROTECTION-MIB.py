# SNMP MIB module (CM-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-PROTECTION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:20 2025
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

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

cmProtectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7)
)
if mibBuilder.loadTexts:
    cmProtectionMIB.setRevisions(
        ("2010-06-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CmProtSwitchMode(TextualConvention, Integer32):
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
        *(("oneplusone", 1),
          ("dualactiverx", 2),
          ("universalring", 3))
    )



class CmProtSwitchDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unidirectional", 1),
          ("bidirectional", 2))
    )



class CmProtSwitchAction(TextualConvention, Integer32):
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
        *(("none", 1),
          ("releaseprotswitch", 2),
          ("manualfromworking", 3),
          ("forcedfromworking", 4),
          ("manualfromprotect", 5),
          ("forcedfromprotect", 6),
          ("lockoutfromprotect", 7))
    )



class CmProtUnitType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protect", 2))
    )



class CmProtUnitState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )



class CmProtGroupStatus(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("nooutstandingreq", 1),
          ("sf-protect", 2),
          ("sf-working", 3),
          ("sd-protect", 4),
          ("sd-working", 5),
          ("manual-protect", 6),
          ("manual-working", 7),
          ("forced-protect", 8),
          ("forced-working", 9),
          ("lockout-protect", 10),
          ("waitToRestore", 11))
    )



# MIB Managed Objects in the order of their OIDs

_CmProtObjects_ObjectIdentity = ObjectIdentity
cmProtObjects = _CmProtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1)
)
_CmFacProtGroupTable_Object = MibTable
cmFacProtGroupTable = _CmFacProtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1)
)
if mibBuilder.loadTexts:
    cmFacProtGroupTable.setStatus("current")
_CmFacProtGroupEntry_Object = MibTableRow
cmFacProtGroupEntry = _CmFacProtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1)
)
cmFacProtGroupEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-PROTECTION-MIB", "cmFacProtGroupIndex"),
)
if mibBuilder.loadTexts:
    cmFacProtGroupEntry.setStatus("current")
_CmFacProtGroupIndex_Type = Integer32
_CmFacProtGroupIndex_Object = MibTableColumn
cmFacProtGroupIndex = _CmFacProtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 1),
    _CmFacProtGroupIndex_Type()
)
cmFacProtGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFacProtGroupIndex.setStatus("current")


class _CmFacProtGroupUserLabel_Type(DisplayString):
    """Custom type cmFacProtGroupUserLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmFacProtGroupUserLabel_Type.__name__ = "DisplayString"
_CmFacProtGroupUserLabel_Object = MibTableColumn
cmFacProtGroupUserLabel = _CmFacProtGroupUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 2),
    _CmFacProtGroupUserLabel_Type()
)
cmFacProtGroupUserLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupUserLabel.setStatus("current")
_CmFacProtGroupSwitchMode_Type = CmProtSwitchMode
_CmFacProtGroupSwitchMode_Object = MibTableColumn
cmFacProtGroupSwitchMode = _CmFacProtGroupSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 3),
    _CmFacProtGroupSwitchMode_Type()
)
cmFacProtGroupSwitchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupSwitchMode.setStatus("current")
_CmFacProtGroupRevertive_Type = TruthValue
_CmFacProtGroupRevertive_Object = MibTableColumn
cmFacProtGroupRevertive = _CmFacProtGroupRevertive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 4),
    _CmFacProtGroupRevertive_Type()
)
cmFacProtGroupRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupRevertive.setStatus("current")


class _CmFacProtGroupWaitToRestore_Type(Integer32):
    """Custom type cmFacProtGroupWaitToRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
        ValueRangeConstraint(0, 0),
    )


_CmFacProtGroupWaitToRestore_Type.__name__ = "Integer32"
_CmFacProtGroupWaitToRestore_Object = MibTableColumn
cmFacProtGroupWaitToRestore = _CmFacProtGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 5),
    _CmFacProtGroupWaitToRestore_Type()
)
cmFacProtGroupWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupWaitToRestore.setStatus("current")
_CmFacProtGroupDirection_Type = CmProtSwitchDirection
_CmFacProtGroupDirection_Object = MibTableColumn
cmFacProtGroupDirection = _CmFacProtGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 6),
    _CmFacProtGroupDirection_Type()
)
cmFacProtGroupDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupDirection.setStatus("current")
_CmFacProtGroupWorkPort_Type = VariablePointer
_CmFacProtGroupWorkPort_Object = MibTableColumn
cmFacProtGroupWorkPort = _CmFacProtGroupWorkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 7),
    _CmFacProtGroupWorkPort_Type()
)
cmFacProtGroupWorkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupWorkPort.setStatus("current")
_CmFacProtGroupProtPort_Type = VariablePointer
_CmFacProtGroupProtPort_Object = MibTableColumn
cmFacProtGroupProtPort = _CmFacProtGroupProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 8),
    _CmFacProtGroupProtPort_Type()
)
cmFacProtGroupProtPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupProtPort.setStatus("current")
_CmFacProtGroupStatus_Type = CmProtGroupStatus
_CmFacProtGroupStatus_Object = MibTableColumn
cmFacProtGroupStatus = _CmFacProtGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 9),
    _CmFacProtGroupStatus_Type()
)
cmFacProtGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFacProtGroupStatus.setStatus("current")
_CmFacProtGroupAction_Type = CmProtSwitchAction
_CmFacProtGroupAction_Object = MibTableColumn
cmFacProtGroupAction = _CmFacProtGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 10),
    _CmFacProtGroupAction_Type()
)
cmFacProtGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFacProtGroupAction.setStatus("current")
_CmFacProtGroupStorageType_Type = StorageType
_CmFacProtGroupStorageType_Object = MibTableColumn
cmFacProtGroupStorageType = _CmFacProtGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 11),
    _CmFacProtGroupStorageType_Type()
)
cmFacProtGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupStorageType.setStatus("current")
_CmFacProtGroupRowStatus_Type = RowStatus
_CmFacProtGroupRowStatus_Object = MibTableColumn
cmFacProtGroupRowStatus = _CmFacProtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 12),
    _CmFacProtGroupRowStatus_Type()
)
cmFacProtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmFacProtGroupRowStatus.setStatus("current")
_CmFacProtGroupMacAddress_Type = MacAddress
_CmFacProtGroupMacAddress_Object = MibTableColumn
cmFacProtGroupMacAddress = _CmFacProtGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 13),
    _CmFacProtGroupMacAddress_Type()
)
cmFacProtGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFacProtGroupMacAddress.setStatus("current")
_CmFacProtUnitTable_Object = MibTable
cmFacProtUnitTable = _CmFacProtUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2)
)
if mibBuilder.loadTexts:
    cmFacProtUnitTable.setStatus("current")
_CmFacProtUnitEntry_Object = MibTableRow
cmFacProtUnitEntry = _CmFacProtUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1)
)
cmFacProtUnitEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-PROTECTION-MIB", "cmFacProtGroupIndex"),
    (0, "CM-PROTECTION-MIB", "cmFacProtUnitIndex"),
)
if mibBuilder.loadTexts:
    cmFacProtUnitEntry.setStatus("current")
_CmFacProtUnitIndex_Type = Integer32
_CmFacProtUnitIndex_Object = MibTableColumn
cmFacProtUnitIndex = _CmFacProtUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 1),
    _CmFacProtUnitIndex_Type()
)
cmFacProtUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFacProtUnitIndex.setStatus("current")
_CmFacProtUnitType_Type = CmProtUnitType
_CmFacProtUnitType_Object = MibTableColumn
cmFacProtUnitType = _CmFacProtUnitType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 2),
    _CmFacProtUnitType_Type()
)
cmFacProtUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFacProtUnitType.setStatus("current")
_CmFacProtUnitState_Type = CmProtUnitState
_CmFacProtUnitState_Object = MibTableColumn
cmFacProtUnitState = _CmFacProtUnitState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 3),
    _CmFacProtUnitState_Type()
)
cmFacProtUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFacProtUnitState.setStatus("current")
_CmFacProtUnitPort_Type = VariablePointer
_CmFacProtUnitPort_Object = MibTableColumn
cmFacProtUnitPort = _CmFacProtUnitPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 4),
    _CmFacProtUnitPort_Type()
)
cmFacProtUnitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFacProtUnitPort.setStatus("current")
_CmMSPGroupTable_Object = MibTable
cmMSPGroupTable = _CmMSPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3)
)
if mibBuilder.loadTexts:
    cmMSPGroupTable.setStatus("current")
_CmMSPGroupEntry_Object = MibTableRow
cmMSPGroupEntry = _CmMSPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1)
)
cmMSPGroupEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-PROTECTION-MIB", "cmMSPGroupIndex"),
)
if mibBuilder.loadTexts:
    cmMSPGroupEntry.setStatus("current")
_CmMSPGroupIndex_Type = Integer32
_CmMSPGroupIndex_Object = MibTableColumn
cmMSPGroupIndex = _CmMSPGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 1),
    _CmMSPGroupIndex_Type()
)
cmMSPGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMSPGroupIndex.setStatus("current")


class _CmMSPGroupUserLabel_Type(DisplayString):
    """Custom type cmMSPGroupUserLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CmMSPGroupUserLabel_Type.__name__ = "DisplayString"
_CmMSPGroupUserLabel_Object = MibTableColumn
cmMSPGroupUserLabel = _CmMSPGroupUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 2),
    _CmMSPGroupUserLabel_Type()
)
cmMSPGroupUserLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupUserLabel.setStatus("current")
_CmMSPGroupSwitchMode_Type = CmProtSwitchMode
_CmMSPGroupSwitchMode_Object = MibTableColumn
cmMSPGroupSwitchMode = _CmMSPGroupSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 3),
    _CmMSPGroupSwitchMode_Type()
)
cmMSPGroupSwitchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupSwitchMode.setStatus("current")
_CmMSPGroupRevertive_Type = TruthValue
_CmMSPGroupRevertive_Object = MibTableColumn
cmMSPGroupRevertive = _CmMSPGroupRevertive_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 4),
    _CmMSPGroupRevertive_Type()
)
cmMSPGroupRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupRevertive.setStatus("current")


class _CmMSPGroupWaitToRestore_Type(Integer32):
    """Custom type cmMSPGroupWaitToRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
        ValueRangeConstraint(0, 0),
    )


_CmMSPGroupWaitToRestore_Type.__name__ = "Integer32"
_CmMSPGroupWaitToRestore_Object = MibTableColumn
cmMSPGroupWaitToRestore = _CmMSPGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 5),
    _CmMSPGroupWaitToRestore_Type()
)
cmMSPGroupWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupWaitToRestore.setStatus("current")
_CmMSPGroupB2DEGTrigger_Type = TruthValue
_CmMSPGroupB2DEGTrigger_Object = MibTableColumn
cmMSPGroupB2DEGTrigger = _CmMSPGroupB2DEGTrigger_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 6),
    _CmMSPGroupB2DEGTrigger_Type()
)
cmMSPGroupB2DEGTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupB2DEGTrigger.setStatus("current")
_CmMSPGroupDirection_Type = CmProtSwitchDirection
_CmMSPGroupDirection_Object = MibTableColumn
cmMSPGroupDirection = _CmMSPGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 7),
    _CmMSPGroupDirection_Type()
)
cmMSPGroupDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupDirection.setStatus("current")
_CmMSPGroupWorkPort_Type = VariablePointer
_CmMSPGroupWorkPort_Object = MibTableColumn
cmMSPGroupWorkPort = _CmMSPGroupWorkPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 8),
    _CmMSPGroupWorkPort_Type()
)
cmMSPGroupWorkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupWorkPort.setStatus("current")
_CmMSPGroupProtPort_Type = VariablePointer
_CmMSPGroupProtPort_Object = MibTableColumn
cmMSPGroupProtPort = _CmMSPGroupProtPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 9),
    _CmMSPGroupProtPort_Type()
)
cmMSPGroupProtPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupProtPort.setStatus("current")
_CmMSPGroupStatus_Type = CmProtGroupStatus
_CmMSPGroupStatus_Object = MibTableColumn
cmMSPGroupStatus = _CmMSPGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 10),
    _CmMSPGroupStatus_Type()
)
cmMSPGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMSPGroupStatus.setStatus("current")
_CmMSPGroupAction_Type = CmProtSwitchAction
_CmMSPGroupAction_Object = MibTableColumn
cmMSPGroupAction = _CmMSPGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 11),
    _CmMSPGroupAction_Type()
)
cmMSPGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMSPGroupAction.setStatus("current")
_CmMSPGroupStorageType_Type = StorageType
_CmMSPGroupStorageType_Object = MibTableColumn
cmMSPGroupStorageType = _CmMSPGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 12),
    _CmMSPGroupStorageType_Type()
)
cmMSPGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupStorageType.setStatus("current")
_CmMSPGroupRowStatus_Type = RowStatus
_CmMSPGroupRowStatus_Object = MibTableColumn
cmMSPGroupRowStatus = _CmMSPGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 13),
    _CmMSPGroupRowStatus_Type()
)
cmMSPGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmMSPGroupRowStatus.setStatus("current")
_CmMSPGroupMacAddress_Type = MacAddress
_CmMSPGroupMacAddress_Object = MibTableColumn
cmMSPGroupMacAddress = _CmMSPGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 14),
    _CmMSPGroupMacAddress_Type()
)
cmMSPGroupMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMSPGroupMacAddress.setStatus("current")
_CmMSPUnitTable_Object = MibTable
cmMSPUnitTable = _CmMSPUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4)
)
if mibBuilder.loadTexts:
    cmMSPUnitTable.setStatus("current")
_CmMSPUnitEntry_Object = MibTableRow
cmMSPUnitEntry = _CmMSPUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1)
)
cmMSPUnitEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-PROTECTION-MIB", "cmMSPGroupIndex"),
    (0, "CM-PROTECTION-MIB", "cmMSPUnitIndex"),
)
if mibBuilder.loadTexts:
    cmMSPUnitEntry.setStatus("current")
_CmMSPUnitIndex_Type = Integer32
_CmMSPUnitIndex_Object = MibTableColumn
cmMSPUnitIndex = _CmMSPUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 1),
    _CmMSPUnitIndex_Type()
)
cmMSPUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMSPUnitIndex.setStatus("current")
_CmMSPUnitType_Type = CmProtUnitType
_CmMSPUnitType_Object = MibTableColumn
cmMSPUnitType = _CmMSPUnitType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 2),
    _CmMSPUnitType_Type()
)
cmMSPUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMSPUnitType.setStatus("current")
_CmMSPUnitState_Type = CmProtUnitState
_CmMSPUnitState_Object = MibTableColumn
cmMSPUnitState = _CmMSPUnitState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 3),
    _CmMSPUnitState_Type()
)
cmMSPUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMSPUnitState.setStatus("current")
_CmMSPUnitPort_Type = VariablePointer
_CmMSPUnitPort_Object = MibTableColumn
cmMSPUnitPort = _CmMSPUnitPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 4),
    _CmMSPUnitPort_Type()
)
cmMSPUnitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMSPUnitPort.setStatus("current")
_CmProtNotifications_ObjectIdentity = ObjectIdentity
cmProtNotifications = _CmProtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 2)
)
_CmProtConformance_ObjectIdentity = ObjectIdentity
cmProtConformance = _CmProtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3)
)
_CmProtCompliances_ObjectIdentity = ObjectIdentity
cmProtCompliances = _CmProtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 1)
)
_CmProtGroups_ObjectIdentity = ObjectIdentity
cmProtGroups = _CmProtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2)
)

# Managed Objects groups

cmProtObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2, 1)
)
cmProtObjectGroup.setObjects(
      *(("CM-PROTECTION-MIB", "cmFacProtGroupIndex"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupUserLabel"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupSwitchMode"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupRevertive"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupWaitToRestore"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupDirection"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupWorkPort"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupProtPort"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupStatus"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupAction"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupStorageType"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupRowStatus"),
        ("CM-PROTECTION-MIB", "cmFacProtGroupMacAddress"),
        ("CM-PROTECTION-MIB", "cmFacProtUnitIndex"),
        ("CM-PROTECTION-MIB", "cmFacProtUnitType"),
        ("CM-PROTECTION-MIB", "cmFacProtUnitState"),
        ("CM-PROTECTION-MIB", "cmFacProtUnitPort"))
)
if mibBuilder.loadTexts:
    cmProtObjectGroup.setStatus("current")

cmMSProtObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2, 2)
)
cmMSProtObjectGroup.setObjects(
      *(("CM-PROTECTION-MIB", "cmMSPGroupIndex"),
        ("CM-PROTECTION-MIB", "cmMSPGroupUserLabel"),
        ("CM-PROTECTION-MIB", "cmMSPGroupSwitchMode"),
        ("CM-PROTECTION-MIB", "cmMSPGroupRevertive"),
        ("CM-PROTECTION-MIB", "cmMSPGroupWaitToRestore"),
        ("CM-PROTECTION-MIB", "cmMSPGroupB2DEGTrigger"),
        ("CM-PROTECTION-MIB", "cmMSPGroupDirection"),
        ("CM-PROTECTION-MIB", "cmMSPGroupWorkPort"),
        ("CM-PROTECTION-MIB", "cmMSPGroupProtPort"),
        ("CM-PROTECTION-MIB", "cmMSPGroupStatus"),
        ("CM-PROTECTION-MIB", "cmMSPGroupAction"),
        ("CM-PROTECTION-MIB", "cmMSPGroupStorageType"),
        ("CM-PROTECTION-MIB", "cmMSPGroupRowStatus"),
        ("CM-PROTECTION-MIB", "cmMSPGroupMacAddress"),
        ("CM-PROTECTION-MIB", "cmMSPUnitIndex"),
        ("CM-PROTECTION-MIB", "cmMSPUnitType"),
        ("CM-PROTECTION-MIB", "cmMSPUnitState"),
        ("CM-PROTECTION-MIB", "cmMSPUnitPort"))
)
if mibBuilder.loadTexts:
    cmMSProtObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmProtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 1, 1)
)
cmProtCompliance.setObjects(
      *(("CM-PROTECTION-MIB", "cmProtObjectGroup"),
        ("CM-PROTECTION-MIB", "cmMSProtObjectGroup"))
)
if mibBuilder.loadTexts:
    cmProtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-PROTECTION-MIB",
    **{"CmProtSwitchMode": CmProtSwitchMode,
       "CmProtSwitchDirection": CmProtSwitchDirection,
       "CmProtSwitchAction": CmProtSwitchAction,
       "CmProtUnitType": CmProtUnitType,
       "CmProtUnitState": CmProtUnitState,
       "CmProtGroupStatus": CmProtGroupStatus,
       "cmProtectionMIB": cmProtectionMIB,
       "cmProtObjects": cmProtObjects,
       "cmFacProtGroupTable": cmFacProtGroupTable,
       "cmFacProtGroupEntry": cmFacProtGroupEntry,
       "cmFacProtGroupIndex": cmFacProtGroupIndex,
       "cmFacProtGroupUserLabel": cmFacProtGroupUserLabel,
       "cmFacProtGroupSwitchMode": cmFacProtGroupSwitchMode,
       "cmFacProtGroupRevertive": cmFacProtGroupRevertive,
       "cmFacProtGroupWaitToRestore": cmFacProtGroupWaitToRestore,
       "cmFacProtGroupDirection": cmFacProtGroupDirection,
       "cmFacProtGroupWorkPort": cmFacProtGroupWorkPort,
       "cmFacProtGroupProtPort": cmFacProtGroupProtPort,
       "cmFacProtGroupStatus": cmFacProtGroupStatus,
       "cmFacProtGroupAction": cmFacProtGroupAction,
       "cmFacProtGroupStorageType": cmFacProtGroupStorageType,
       "cmFacProtGroupRowStatus": cmFacProtGroupRowStatus,
       "cmFacProtGroupMacAddress": cmFacProtGroupMacAddress,
       "cmFacProtUnitTable": cmFacProtUnitTable,
       "cmFacProtUnitEntry": cmFacProtUnitEntry,
       "cmFacProtUnitIndex": cmFacProtUnitIndex,
       "cmFacProtUnitType": cmFacProtUnitType,
       "cmFacProtUnitState": cmFacProtUnitState,
       "cmFacProtUnitPort": cmFacProtUnitPort,
       "cmMSPGroupTable": cmMSPGroupTable,
       "cmMSPGroupEntry": cmMSPGroupEntry,
       "cmMSPGroupIndex": cmMSPGroupIndex,
       "cmMSPGroupUserLabel": cmMSPGroupUserLabel,
       "cmMSPGroupSwitchMode": cmMSPGroupSwitchMode,
       "cmMSPGroupRevertive": cmMSPGroupRevertive,
       "cmMSPGroupWaitToRestore": cmMSPGroupWaitToRestore,
       "cmMSPGroupB2DEGTrigger": cmMSPGroupB2DEGTrigger,
       "cmMSPGroupDirection": cmMSPGroupDirection,
       "cmMSPGroupWorkPort": cmMSPGroupWorkPort,
       "cmMSPGroupProtPort": cmMSPGroupProtPort,
       "cmMSPGroupStatus": cmMSPGroupStatus,
       "cmMSPGroupAction": cmMSPGroupAction,
       "cmMSPGroupStorageType": cmMSPGroupStorageType,
       "cmMSPGroupRowStatus": cmMSPGroupRowStatus,
       "cmMSPGroupMacAddress": cmMSPGroupMacAddress,
       "cmMSPUnitTable": cmMSPUnitTable,
       "cmMSPUnitEntry": cmMSPUnitEntry,
       "cmMSPUnitIndex": cmMSPUnitIndex,
       "cmMSPUnitType": cmMSPUnitType,
       "cmMSPUnitState": cmMSPUnitState,
       "cmMSPUnitPort": cmMSPUnitPort,
       "cmProtNotifications": cmProtNotifications,
       "cmProtConformance": cmProtConformance,
       "cmProtCompliances": cmProtCompliances,
       "cmProtCompliance": cmProtCompliance,
       "cmProtGroups": cmProtGroups,
       "cmProtObjectGroup": cmProtObjectGroup,
       "cmMSProtObjectGroup": cmMSProtObjectGroup}
)
