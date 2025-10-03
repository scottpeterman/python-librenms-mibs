# SNMP MIB module (F3-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-PWE3-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:48 2025
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

(AdminState,
 CmPmBinAction,
 CmPmIntervalType,
 IpPriorityMapMode,
 IpVersion,
 OperationalState,
 PerfCounter64,
 SecondaryState,
 VlanId,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "CmPmIntervalType",
    "IpPriorityMapMode",
    "IpVersion",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState",
    "VlanId",
    "VlanPriority")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortIndex,
 cmEthernetNetPortIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortIndex",
    "cmEthernetNetPortIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3Pwe3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19)
)
if mibBuilder.loadTexts:
    f3Pwe3MIB.setRevisions(
        ("2012-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PWE3SatopDiscoveryType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )



class PWE3SatopEncapsulationType(TextualConvention, Integer32):
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
        *(("vlan-one-mpls-label", 1),
          ("vlan-two-mpls-label", 2),
          ("novlan-two-mpls-label", 3))
    )



class PWE3SatopRTPTSUpdateFreqType(TextualConvention, Integer32):
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
        *(("freq-8kHz", 1),
          ("freq-16kHz", 2),
          ("freq-32kHz", 3),
          ("freq-64kHz", 4),
          ("freq-128kHz", 5),
          ("freq-256kHz", 6),
          ("freq-512kHz", 7),
          ("freq-1024kHz", 8))
    )



class PWE3SatopTransportMode(TextualConvention, Integer32):
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
        *(("satop-e1", 1),
          ("satop-t1", 2),
          ("satop-octetalignt1", 3))
    )



class MplsLabel(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_F3Pwe3ConfigObjects_ObjectIdentity = ObjectIdentity
f3Pwe3ConfigObjects = _F3Pwe3ConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1)
)
_F3Pwe3IdlePatternProfileTable_Object = MibTable
f3Pwe3IdlePatternProfileTable = _F3Pwe3IdlePatternProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 1)
)
if mibBuilder.loadTexts:
    f3Pwe3IdlePatternProfileTable.setStatus("current")
_F3Pwe3IdlePatternProfileEntry_Object = MibTableRow
f3Pwe3IdlePatternProfileEntry = _F3Pwe3IdlePatternProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 1, 1)
)
f3Pwe3IdlePatternProfileEntry.setIndexNames(
    (0, "F3-PWE3-MIB", "f3Pwe3IdlePatternProfileIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3IdlePatternProfileEntry.setStatus("current")
_F3Pwe3IdlePatternProfileIndex_Type = Integer32
_F3Pwe3IdlePatternProfileIndex_Object = MibTableColumn
f3Pwe3IdlePatternProfileIndex = _F3Pwe3IdlePatternProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 1, 1, 1),
    _F3Pwe3IdlePatternProfileIndex_Type()
)
f3Pwe3IdlePatternProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3IdlePatternProfileIndex.setStatus("current")
_F3Pwe3IdlePatternProfileByte_Type = Unsigned32
_F3Pwe3IdlePatternProfileByte_Object = MibTableColumn
f3Pwe3IdlePatternProfileByte = _F3Pwe3IdlePatternProfileByte_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 1, 1, 2),
    _F3Pwe3IdlePatternProfileByte_Type()
)
f3Pwe3IdlePatternProfileByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3IdlePatternProfileByte.setStatus("current")
_F3Pwe3ResyncProfileTable_Object = MibTable
f3Pwe3ResyncProfileTable = _F3Pwe3ResyncProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 2)
)
if mibBuilder.loadTexts:
    f3Pwe3ResyncProfileTable.setStatus("current")
_F3Pwe3ResyncProfileEntry_Object = MibTableRow
f3Pwe3ResyncProfileEntry = _F3Pwe3ResyncProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 2, 1)
)
f3Pwe3ResyncProfileEntry.setIndexNames(
    (0, "F3-PWE3-MIB", "f3Pwe3ResyncProfileIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3ResyncProfileEntry.setStatus("current")
_F3Pwe3ResyncProfileIndex_Type = Integer32
_F3Pwe3ResyncProfileIndex_Object = MibTableColumn
f3Pwe3ResyncProfileIndex = _F3Pwe3ResyncProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 2, 1, 1),
    _F3Pwe3ResyncProfileIndex_Type()
)
f3Pwe3ResyncProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3ResyncProfileIndex.setStatus("current")
_F3Pwe3ResyncProfileIncreaseFactor_Type = Unsigned32
_F3Pwe3ResyncProfileIncreaseFactor_Object = MibTableColumn
f3Pwe3ResyncProfileIncreaseFactor = _F3Pwe3ResyncProfileIncreaseFactor_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 2, 1, 2),
    _F3Pwe3ResyncProfileIncreaseFactor_Type()
)
f3Pwe3ResyncProfileIncreaseFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3ResyncProfileIncreaseFactor.setStatus("current")
_F3Pwe3ResyncProfileDecreaseFactor_Type = Unsigned32
_F3Pwe3ResyncProfileDecreaseFactor_Object = MibTableColumn
f3Pwe3ResyncProfileDecreaseFactor = _F3Pwe3ResyncProfileDecreaseFactor_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 2, 1, 3),
    _F3Pwe3ResyncProfileDecreaseFactor_Type()
)
f3Pwe3ResyncProfileDecreaseFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3ResyncProfileDecreaseFactor.setStatus("current")
_F3Pwe3ResyncProfileResyncThreshold_Type = Unsigned32
_F3Pwe3ResyncProfileResyncThreshold_Object = MibTableColumn
f3Pwe3ResyncProfileResyncThreshold = _F3Pwe3ResyncProfileResyncThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 2, 1, 4),
    _F3Pwe3ResyncProfileResyncThreshold_Type()
)
f3Pwe3ResyncProfileResyncThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3ResyncProfileResyncThreshold.setStatus("current")
_F3Pwe3LoopbackProfileTable_Object = MibTable
f3Pwe3LoopbackProfileTable = _F3Pwe3LoopbackProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 3)
)
if mibBuilder.loadTexts:
    f3Pwe3LoopbackProfileTable.setStatus("current")
_F3Pwe3LoopbackProfileEntry_Object = MibTableRow
f3Pwe3LoopbackProfileEntry = _F3Pwe3LoopbackProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 3, 1)
)
f3Pwe3LoopbackProfileEntry.setIndexNames(
    (0, "F3-PWE3-MIB", "f3Pwe3LoopbackProfileIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3LoopbackProfileEntry.setStatus("current")
_F3Pwe3LoopbackProfileIndex_Type = Integer32
_F3Pwe3LoopbackProfileIndex_Object = MibTableColumn
f3Pwe3LoopbackProfileIndex = _F3Pwe3LoopbackProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 3, 1, 1),
    _F3Pwe3LoopbackProfileIndex_Type()
)
f3Pwe3LoopbackProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3LoopbackProfileIndex.setStatus("current")
_F3Pwe3LoopbackProfileLength_Type = Unsigned32
_F3Pwe3LoopbackProfileLength_Object = MibTableColumn
f3Pwe3LoopbackProfileLength = _F3Pwe3LoopbackProfileLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 3, 1, 2),
    _F3Pwe3LoopbackProfileLength_Type()
)
f3Pwe3LoopbackProfileLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3LoopbackProfileLength.setStatus("current")
_F3Pwe3LoopbackProfilePattern_Type = Unsigned32
_F3Pwe3LoopbackProfilePattern_Object = MibTableColumn
f3Pwe3LoopbackProfilePattern = _F3Pwe3LoopbackProfilePattern_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 3, 1, 3),
    _F3Pwe3LoopbackProfilePattern_Type()
)
f3Pwe3LoopbackProfilePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3LoopbackProfilePattern.setStatus("current")
_F3Pwe3LoopbackProfileRepeatTime_Type = Unsigned32
_F3Pwe3LoopbackProfileRepeatTime_Object = MibTableColumn
f3Pwe3LoopbackProfileRepeatTime = _F3Pwe3LoopbackProfileRepeatTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 3, 1, 4),
    _F3Pwe3LoopbackProfileRepeatTime_Type()
)
f3Pwe3LoopbackProfileRepeatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3LoopbackProfileRepeatTime.setStatus("current")
_F3Pwe3LoopbackProfileClearLength_Type = Unsigned32
_F3Pwe3LoopbackProfileClearLength_Object = MibTableColumn
f3Pwe3LoopbackProfileClearLength = _F3Pwe3LoopbackProfileClearLength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 3, 1, 5),
    _F3Pwe3LoopbackProfileClearLength_Type()
)
f3Pwe3LoopbackProfileClearLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3LoopbackProfileClearLength.setStatus("current")
_F3Pwe3LoopbackProfileClearPattern_Type = Unsigned32
_F3Pwe3LoopbackProfileClearPattern_Object = MibTableColumn
f3Pwe3LoopbackProfileClearPattern = _F3Pwe3LoopbackProfileClearPattern_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 3, 1, 6),
    _F3Pwe3LoopbackProfileClearPattern_Type()
)
f3Pwe3LoopbackProfileClearPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3LoopbackProfileClearPattern.setStatus("current")
_F3Pwe3LossProfileTable_Object = MibTable
f3Pwe3LossProfileTable = _F3Pwe3LossProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 4)
)
if mibBuilder.loadTexts:
    f3Pwe3LossProfileTable.setStatus("current")
_F3Pwe3LossProfileEntry_Object = MibTableRow
f3Pwe3LossProfileEntry = _F3Pwe3LossProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 4, 1)
)
f3Pwe3LossProfileEntry.setIndexNames(
    (0, "F3-PWE3-MIB", "f3Pwe3LossProfileIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3LossProfileEntry.setStatus("current")
_F3Pwe3LossProfileIndex_Type = Integer32
_F3Pwe3LossProfileIndex_Object = MibTableColumn
f3Pwe3LossProfileIndex = _F3Pwe3LossProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 4, 1, 1),
    _F3Pwe3LossProfileIndex_Type()
)
f3Pwe3LossProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3LossProfileIndex.setStatus("current")
_F3Pwe3LossProfileLossStateEnterTime_Type = Unsigned32
_F3Pwe3LossProfileLossStateEnterTime_Object = MibTableColumn
f3Pwe3LossProfileLossStateEnterTime = _F3Pwe3LossProfileLossStateEnterTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 4, 1, 2),
    _F3Pwe3LossProfileLossStateEnterTime_Type()
)
f3Pwe3LossProfileLossStateEnterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3LossProfileLossStateEnterTime.setStatus("current")
_F3Pwe3LossProfileLossStateExitTime_Type = Unsigned32
_F3Pwe3LossProfileLossStateExitTime_Object = MibTableColumn
f3Pwe3LossProfileLossStateExitTime = _F3Pwe3LossProfileLossStateExitTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 4, 1, 3),
    _F3Pwe3LossProfileLossStateExitTime_Type()
)
f3Pwe3LossProfileLossStateExitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3LossProfileLossStateExitTime.setStatus("current")
_F3Pwe3AisStabilizationProfileTable_Object = MibTable
f3Pwe3AisStabilizationProfileTable = _F3Pwe3AisStabilizationProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 5)
)
if mibBuilder.loadTexts:
    f3Pwe3AisStabilizationProfileTable.setStatus("current")
_F3Pwe3AisStabilizationProfileEntry_Object = MibTableRow
f3Pwe3AisStabilizationProfileEntry = _F3Pwe3AisStabilizationProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 5, 1)
)
f3Pwe3AisStabilizationProfileEntry.setIndexNames(
    (0, "F3-PWE3-MIB", "f3Pwe3AisStabilizationProfileIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3AisStabilizationProfileEntry.setStatus("current")
_F3Pwe3AisStabilizationProfileIndex_Type = Integer32
_F3Pwe3AisStabilizationProfileIndex_Object = MibTableColumn
f3Pwe3AisStabilizationProfileIndex = _F3Pwe3AisStabilizationProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 5, 1, 1),
    _F3Pwe3AisStabilizationProfileIndex_Type()
)
f3Pwe3AisStabilizationProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3AisStabilizationProfileIndex.setStatus("current")
_F3Pwe3AisStabilizationProfileEnterTime_Type = Unsigned32
_F3Pwe3AisStabilizationProfileEnterTime_Object = MibTableColumn
f3Pwe3AisStabilizationProfileEnterTime = _F3Pwe3AisStabilizationProfileEnterTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 5, 1, 2),
    _F3Pwe3AisStabilizationProfileEnterTime_Type()
)
f3Pwe3AisStabilizationProfileEnterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3AisStabilizationProfileEnterTime.setStatus("current")
_F3Pwe3AisStabilizationProfileExitTime_Type = Unsigned32
_F3Pwe3AisStabilizationProfileExitTime_Object = MibTableColumn
f3Pwe3AisStabilizationProfileExitTime = _F3Pwe3AisStabilizationProfileExitTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 5, 1, 3),
    _F3Pwe3AisStabilizationProfileExitTime_Type()
)
f3Pwe3AisStabilizationProfileExitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3AisStabilizationProfileExitTime.setStatus("current")
_F3Pwe3SatopTable_Object = MibTable
f3Pwe3SatopTable = _F3Pwe3SatopTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6)
)
if mibBuilder.loadTexts:
    f3Pwe3SatopTable.setStatus("current")
_F3Pwe3SatopEntry_Object = MibTableRow
f3Pwe3SatopEntry = _F3Pwe3SatopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1)
)
f3Pwe3SatopEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3SatopEntry.setStatus("current")
_F3Pwe3SatopIndex_Type = Integer32
_F3Pwe3SatopIndex_Object = MibTableColumn
f3Pwe3SatopIndex = _F3Pwe3SatopIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 1),
    _F3Pwe3SatopIndex_Type()
)
f3Pwe3SatopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3SatopIndex.setStatus("current")


class _F3Pwe3SatopAlias_Type(DisplayString):
    """Custom type f3Pwe3SatopAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_F3Pwe3SatopAlias_Type.__name__ = "DisplayString"
_F3Pwe3SatopAlias_Object = MibTableColumn
f3Pwe3SatopAlias = _F3Pwe3SatopAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 2),
    _F3Pwe3SatopAlias_Type()
)
f3Pwe3SatopAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopAlias.setStatus("current")
_F3Pwe3SatopAdminState_Type = AdminState
_F3Pwe3SatopAdminState_Object = MibTableColumn
f3Pwe3SatopAdminState = _F3Pwe3SatopAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 3),
    _F3Pwe3SatopAdminState_Type()
)
f3Pwe3SatopAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3SatopAdminState.setStatus("current")
_F3Pwe3SatopOperationalState_Type = OperationalState
_F3Pwe3SatopOperationalState_Object = MibTableColumn
f3Pwe3SatopOperationalState = _F3Pwe3SatopOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 4),
    _F3Pwe3SatopOperationalState_Type()
)
f3Pwe3SatopOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopOperationalState.setStatus("current")
_F3Pwe3SatopSecondaryState_Type = SecondaryState
_F3Pwe3SatopSecondaryState_Object = MibTableColumn
f3Pwe3SatopSecondaryState = _F3Pwe3SatopSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 5),
    _F3Pwe3SatopSecondaryState_Type()
)
f3Pwe3SatopSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopSecondaryState.setStatus("current")
_F3Pwe3SatopTDMEntity_Type = VariablePointer
_F3Pwe3SatopTDMEntity_Object = MibTableColumn
f3Pwe3SatopTDMEntity = _F3Pwe3SatopTDMEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 6),
    _F3Pwe3SatopTDMEntity_Type()
)
f3Pwe3SatopTDMEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopTDMEntity.setStatus("current")
_F3Pwe3SatopDiscoveryType_Type = PWE3SatopDiscoveryType
_F3Pwe3SatopDiscoveryType_Object = MibTableColumn
f3Pwe3SatopDiscoveryType = _F3Pwe3SatopDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 7),
    _F3Pwe3SatopDiscoveryType_Type()
)
f3Pwe3SatopDiscoveryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopDiscoveryType.setStatus("current")
_F3Pwe3SatopRemoteIpAddress_Type = IpAddress
_F3Pwe3SatopRemoteIpAddress_Object = MibTableColumn
f3Pwe3SatopRemoteIpAddress = _F3Pwe3SatopRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 8),
    _F3Pwe3SatopRemoteIpAddress_Type()
)
f3Pwe3SatopRemoteIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopRemoteIpAddress.setStatus("current")
_F3Pwe3SatopRemoteMacAddress_Type = MacAddress
_F3Pwe3SatopRemoteMacAddress_Object = MibTableColumn
f3Pwe3SatopRemoteMacAddress = _F3Pwe3SatopRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 9),
    _F3Pwe3SatopRemoteMacAddress_Type()
)
f3Pwe3SatopRemoteMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopRemoteMacAddress.setStatus("current")
_F3Pwe3SatopEncapsulationType_Type = PWE3SatopEncapsulationType
_F3Pwe3SatopEncapsulationType_Object = MibTableColumn
f3Pwe3SatopEncapsulationType = _F3Pwe3SatopEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 10),
    _F3Pwe3SatopEncapsulationType_Type()
)
f3Pwe3SatopEncapsulationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopEncapsulationType.setStatus("current")
_F3Pwe3SatopRTPEnabled_Type = TruthValue
_F3Pwe3SatopRTPEnabled_Object = MibTableColumn
f3Pwe3SatopRTPEnabled = _F3Pwe3SatopRTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 11),
    _F3Pwe3SatopRTPEnabled_Type()
)
f3Pwe3SatopRTPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopRTPEnabled.setStatus("current")
_F3Pwe3SatopRTPUpdateFrequency_Type = PWE3SatopRTPTSUpdateFreqType
_F3Pwe3SatopRTPUpdateFrequency_Object = MibTableColumn
f3Pwe3SatopRTPUpdateFrequency = _F3Pwe3SatopRTPUpdateFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 12),
    _F3Pwe3SatopRTPUpdateFrequency_Type()
)
f3Pwe3SatopRTPUpdateFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopRTPUpdateFrequency.setStatus("current")
_F3Pwe3SatopControlWordEnabled_Type = TruthValue
_F3Pwe3SatopControlWordEnabled_Object = MibTableColumn
f3Pwe3SatopControlWordEnabled = _F3Pwe3SatopControlWordEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 13),
    _F3Pwe3SatopControlWordEnabled_Type()
)
f3Pwe3SatopControlWordEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopControlWordEnabled.setStatus("current")
_F3Pwe3SatopJitterBufferSize_Type = Unsigned32
_F3Pwe3SatopJitterBufferSize_Object = MibTableColumn
f3Pwe3SatopJitterBufferSize = _F3Pwe3SatopJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 14),
    _F3Pwe3SatopJitterBufferSize_Type()
)
f3Pwe3SatopJitterBufferSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopJitterBufferSize.setStatus("current")
_F3Pwe3SatopPayloadSize_Type = Unsigned32
_F3Pwe3SatopPayloadSize_Object = MibTableColumn
f3Pwe3SatopPayloadSize = _F3Pwe3SatopPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 15),
    _F3Pwe3SatopPayloadSize_Type()
)
f3Pwe3SatopPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopPayloadSize.setStatus("current")
_F3Pwe3SatopVlanId_Type = VlanId
_F3Pwe3SatopVlanId_Object = MibTableColumn
f3Pwe3SatopVlanId = _F3Pwe3SatopVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 16),
    _F3Pwe3SatopVlanId_Type()
)
f3Pwe3SatopVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopVlanId.setStatus("current")
_F3Pwe3SatopVlanPriority_Type = VlanPriority
_F3Pwe3SatopVlanPriority_Object = MibTableColumn
f3Pwe3SatopVlanPriority = _F3Pwe3SatopVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 17),
    _F3Pwe3SatopVlanPriority_Type()
)
f3Pwe3SatopVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopVlanPriority.setStatus("current")
_F3Pwe3SatopRxMplsLabel1_Type = MplsLabel
_F3Pwe3SatopRxMplsLabel1_Object = MibTableColumn
f3Pwe3SatopRxMplsLabel1 = _F3Pwe3SatopRxMplsLabel1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 18),
    _F3Pwe3SatopRxMplsLabel1_Type()
)
f3Pwe3SatopRxMplsLabel1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopRxMplsLabel1.setStatus("current")
_F3Pwe3SatopRxMplsLabel2_Type = MplsLabel
_F3Pwe3SatopRxMplsLabel2_Object = MibTableColumn
f3Pwe3SatopRxMplsLabel2 = _F3Pwe3SatopRxMplsLabel2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 19),
    _F3Pwe3SatopRxMplsLabel2_Type()
)
f3Pwe3SatopRxMplsLabel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopRxMplsLabel2.setStatus("current")
_F3Pwe3SatopTxMplsLabel1_Type = MplsLabel
_F3Pwe3SatopTxMplsLabel1_Object = MibTableColumn
f3Pwe3SatopTxMplsLabel1 = _F3Pwe3SatopTxMplsLabel1_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 20),
    _F3Pwe3SatopTxMplsLabel1_Type()
)
f3Pwe3SatopTxMplsLabel1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopTxMplsLabel1.setStatus("current")
_F3Pwe3SatopTxMplsLabel2_Type = MplsLabel
_F3Pwe3SatopTxMplsLabel2_Object = MibTableColumn
f3Pwe3SatopTxMplsLabel2 = _F3Pwe3SatopTxMplsLabel2_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 21),
    _F3Pwe3SatopTxMplsLabel2_Type()
)
f3Pwe3SatopTxMplsLabel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopTxMplsLabel2.setStatus("current")
_F3Pwe3SatopAisStabilizationProfile_Type = VariablePointer
_F3Pwe3SatopAisStabilizationProfile_Object = MibTableColumn
f3Pwe3SatopAisStabilizationProfile = _F3Pwe3SatopAisStabilizationProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 22),
    _F3Pwe3SatopAisStabilizationProfile_Type()
)
f3Pwe3SatopAisStabilizationProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopAisStabilizationProfile.setStatus("current")
_F3Pwe3SatopResyncProfile_Type = VariablePointer
_F3Pwe3SatopResyncProfile_Object = MibTableColumn
f3Pwe3SatopResyncProfile = _F3Pwe3SatopResyncProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 23),
    _F3Pwe3SatopResyncProfile_Type()
)
f3Pwe3SatopResyncProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopResyncProfile.setStatus("current")
_F3Pwe3SatopLossProfile_Type = VariablePointer
_F3Pwe3SatopLossProfile_Object = MibTableColumn
f3Pwe3SatopLossProfile = _F3Pwe3SatopLossProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 24),
    _F3Pwe3SatopLossProfile_Type()
)
f3Pwe3SatopLossProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopLossProfile.setStatus("current")
_F3Pwe3SatopTransportMode_Type = PWE3SatopTransportMode
_F3Pwe3SatopTransportMode_Object = MibTableColumn
f3Pwe3SatopTransportMode = _F3Pwe3SatopTransportMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 25),
    _F3Pwe3SatopTransportMode_Type()
)
f3Pwe3SatopTransportMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopTransportMode.setStatus("current")
_F3Pwe3SatopStorageType_Type = StorageType
_F3Pwe3SatopStorageType_Object = MibTableColumn
f3Pwe3SatopStorageType = _F3Pwe3SatopStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 26),
    _F3Pwe3SatopStorageType_Type()
)
f3Pwe3SatopStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopStorageType.setStatus("current")
_F3Pwe3SatopRowStatus_Type = RowStatus
_F3Pwe3SatopRowStatus_Object = MibTableColumn
f3Pwe3SatopRowStatus = _F3Pwe3SatopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 6, 1, 27),
    _F3Pwe3SatopRowStatus_Type()
)
f3Pwe3SatopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopRowStatus.setStatus("current")
_F3Pwe3SatopTDMEntitiesTable_Object = MibTable
f3Pwe3SatopTDMEntitiesTable = _F3Pwe3SatopTDMEntitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 7)
)
if mibBuilder.loadTexts:
    f3Pwe3SatopTDMEntitiesTable.setStatus("current")
_F3Pwe3SatopTDMEntitiesEntry_Object = MibTableRow
f3Pwe3SatopTDMEntitiesEntry = _F3Pwe3SatopTDMEntitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 7, 1)
)
f3Pwe3SatopTDMEntitiesEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopTDMEntityIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3SatopTDMEntitiesEntry.setStatus("current")
_F3Pwe3SatopTDMEntityIndex_Type = Integer32
_F3Pwe3SatopTDMEntityIndex_Object = MibTableColumn
f3Pwe3SatopTDMEntityIndex = _F3Pwe3SatopTDMEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 7, 1, 1),
    _F3Pwe3SatopTDMEntityIndex_Type()
)
f3Pwe3SatopTDMEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3SatopTDMEntityIndex.setStatus("current")
_F3Pwe3SatopTDMEntityObject_Type = VariablePointer
_F3Pwe3SatopTDMEntityObject_Object = MibTableColumn
f3Pwe3SatopTDMEntityObject = _F3Pwe3SatopTDMEntityObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 7, 1, 2),
    _F3Pwe3SatopTDMEntityObject_Type()
)
f3Pwe3SatopTDMEntityObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3SatopTDMEntityObject.setStatus("current")
_F3Pwe3SatopTDMEntityStorageType_Type = StorageType
_F3Pwe3SatopTDMEntityStorageType_Object = MibTableColumn
f3Pwe3SatopTDMEntityStorageType = _F3Pwe3SatopTDMEntityStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 7, 1, 3),
    _F3Pwe3SatopTDMEntityStorageType_Type()
)
f3Pwe3SatopTDMEntityStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopTDMEntityStorageType.setStatus("current")
_F3Pwe3SatopTDMEntityRowStatus_Type = RowStatus
_F3Pwe3SatopTDMEntityRowStatus_Object = MibTableColumn
f3Pwe3SatopTDMEntityRowStatus = _F3Pwe3SatopTDMEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 1, 7, 1, 4),
    _F3Pwe3SatopTDMEntityRowStatus_Type()
)
f3Pwe3SatopTDMEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3Pwe3SatopTDMEntityRowStatus.setStatus("current")
_F3Pwe3PerformanceObjects_ObjectIdentity = ObjectIdentity
f3Pwe3PerformanceObjects = _F3Pwe3PerformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2)
)
_F3Pwe3SatopStatsTable_Object = MibTable
f3Pwe3SatopStatsTable = _F3Pwe3SatopStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1)
)
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsTable.setStatus("current")
_F3Pwe3SatopStatsEntry_Object = MibTableRow
f3Pwe3SatopStatsEntry = _F3Pwe3SatopStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1)
)
f3Pwe3SatopStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopStatsIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsEntry.setStatus("current")


class _F3Pwe3SatopStatsIndex_Type(Integer32):
    """Custom type f3Pwe3SatopStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3Pwe3SatopStatsIndex_Type.__name__ = "Integer32"
_F3Pwe3SatopStatsIndex_Object = MibTableColumn
f3Pwe3SatopStatsIndex = _F3Pwe3SatopStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 1),
    _F3Pwe3SatopStatsIndex_Type()
)
f3Pwe3SatopStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsIndex.setStatus("current")
_F3Pwe3SatopStatsIntervalType_Type = CmPmIntervalType
_F3Pwe3SatopStatsIntervalType_Object = MibTableColumn
f3Pwe3SatopStatsIntervalType = _F3Pwe3SatopStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 2),
    _F3Pwe3SatopStatsIntervalType_Type()
)
f3Pwe3SatopStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsIntervalType.setStatus("current")
_F3Pwe3SatopStatsValid_Type = TruthValue
_F3Pwe3SatopStatsValid_Object = MibTableColumn
f3Pwe3SatopStatsValid = _F3Pwe3SatopStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 3),
    _F3Pwe3SatopStatsValid_Type()
)
f3Pwe3SatopStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsValid.setStatus("current")
_F3Pwe3SatopStatsAction_Type = CmPmBinAction
_F3Pwe3SatopStatsAction_Object = MibTableColumn
f3Pwe3SatopStatsAction = _F3Pwe3SatopStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 4),
    _F3Pwe3SatopStatsAction_Type()
)
f3Pwe3SatopStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsAction.setStatus("current")
_F3Pwe3SatopStatsESs_Type = PerfCounter64
_F3Pwe3SatopStatsESs_Object = MibTableColumn
f3Pwe3SatopStatsESs = _F3Pwe3SatopStatsESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 5),
    _F3Pwe3SatopStatsESs_Type()
)
f3Pwe3SatopStatsESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsESs.setStatus("current")
_F3Pwe3SatopStatsSESs_Type = PerfCounter64
_F3Pwe3SatopStatsSESs_Object = MibTableColumn
f3Pwe3SatopStatsSESs = _F3Pwe3SatopStatsSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 6),
    _F3Pwe3SatopStatsSESs_Type()
)
f3Pwe3SatopStatsSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsSESs.setStatus("current")
_F3Pwe3SatopStatsEBs_Type = PerfCounter64
_F3Pwe3SatopStatsEBs_Object = MibTableColumn
f3Pwe3SatopStatsEBs = _F3Pwe3SatopStatsEBs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 7),
    _F3Pwe3SatopStatsEBs_Type()
)
f3Pwe3SatopStatsEBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsEBs.setStatus("current")
_F3Pwe3SatopStatsResyncs_Type = PerfCounter64
_F3Pwe3SatopStatsResyncs_Object = MibTableColumn
f3Pwe3SatopStatsResyncs = _F3Pwe3SatopStatsResyncs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 8),
    _F3Pwe3SatopStatsResyncs_Type()
)
f3Pwe3SatopStatsResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsResyncs.setStatus("current")
_F3Pwe3SatopStatsMaxJitter_Type = Unsigned32
_F3Pwe3SatopStatsMaxJitter_Object = MibTableColumn
f3Pwe3SatopStatsMaxJitter = _F3Pwe3SatopStatsMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 9),
    _F3Pwe3SatopStatsMaxJitter_Type()
)
f3Pwe3SatopStatsMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsMaxJitter.setStatus("current")
_F3Pwe3SatopStatsFramesTx_Type = PerfCounter64
_F3Pwe3SatopStatsFramesTx_Object = MibTableColumn
f3Pwe3SatopStatsFramesTx = _F3Pwe3SatopStatsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 10),
    _F3Pwe3SatopStatsFramesTx_Type()
)
f3Pwe3SatopStatsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsFramesTx.setStatus("current")
_F3Pwe3SatopStatsPayloadOctetsTx_Type = PerfCounter64
_F3Pwe3SatopStatsPayloadOctetsTx_Object = MibTableColumn
f3Pwe3SatopStatsPayloadOctetsTx = _F3Pwe3SatopStatsPayloadOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 11),
    _F3Pwe3SatopStatsPayloadOctetsTx_Type()
)
f3Pwe3SatopStatsPayloadOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsPayloadOctetsTx.setStatus("current")
_F3Pwe3SatopStatsFramesRx_Type = PerfCounter64
_F3Pwe3SatopStatsFramesRx_Object = MibTableColumn
f3Pwe3SatopStatsFramesRx = _F3Pwe3SatopStatsFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 12),
    _F3Pwe3SatopStatsFramesRx_Type()
)
f3Pwe3SatopStatsFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsFramesRx.setStatus("current")
_F3Pwe3SatopStatsPayloadOctetsRx_Type = PerfCounter64
_F3Pwe3SatopStatsPayloadOctetsRx_Object = MibTableColumn
f3Pwe3SatopStatsPayloadOctetsRx = _F3Pwe3SatopStatsPayloadOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 13),
    _F3Pwe3SatopStatsPayloadOctetsRx_Type()
)
f3Pwe3SatopStatsPayloadOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsPayloadOctetsRx.setStatus("current")
_F3Pwe3SatopStatsOutOfSeqFramesRx_Type = PerfCounter64
_F3Pwe3SatopStatsOutOfSeqFramesRx_Object = MibTableColumn
f3Pwe3SatopStatsOutOfSeqFramesRx = _F3Pwe3SatopStatsOutOfSeqFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 14),
    _F3Pwe3SatopStatsOutOfSeqFramesRx_Type()
)
f3Pwe3SatopStatsOutOfSeqFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsOutOfSeqFramesRx.setStatus("current")
_F3Pwe3SatopStatsLostFrames_Type = PerfCounter64
_F3Pwe3SatopStatsLostFrames_Object = MibTableColumn
f3Pwe3SatopStatsLostFrames = _F3Pwe3SatopStatsLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 15),
    _F3Pwe3SatopStatsLostFrames_Type()
)
f3Pwe3SatopStatsLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsLostFrames.setStatus("current")
_F3Pwe3SatopStatsLostFramesStateTrans_Type = PerfCounter64
_F3Pwe3SatopStatsLostFramesStateTrans_Object = MibTableColumn
f3Pwe3SatopStatsLostFramesStateTrans = _F3Pwe3SatopStatsLostFramesStateTrans_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 16),
    _F3Pwe3SatopStatsLostFramesStateTrans_Type()
)
f3Pwe3SatopStatsLostFramesStateTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsLostFramesStateTrans.setStatus("current")
_F3Pwe3SatopStatsMalformedFramesRx_Type = PerfCounter64
_F3Pwe3SatopStatsMalformedFramesRx_Object = MibTableColumn
f3Pwe3SatopStatsMalformedFramesRx = _F3Pwe3SatopStatsMalformedFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 17),
    _F3Pwe3SatopStatsMalformedFramesRx_Type()
)
f3Pwe3SatopStatsMalformedFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsMalformedFramesRx.setStatus("current")
_F3Pwe3SatopStatsJitterBufferLateFrames_Type = PerfCounter64
_F3Pwe3SatopStatsJitterBufferLateFrames_Object = MibTableColumn
f3Pwe3SatopStatsJitterBufferLateFrames = _F3Pwe3SatopStatsJitterBufferLateFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 1, 1, 18),
    _F3Pwe3SatopStatsJitterBufferLateFrames_Type()
)
f3Pwe3SatopStatsJitterBufferLateFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopStatsJitterBufferLateFrames.setStatus("current")
_F3Pwe3SatopHistoryTable_Object = MibTable
f3Pwe3SatopHistoryTable = _F3Pwe3SatopHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2)
)
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryTable.setStatus("current")
_F3Pwe3SatopHistoryEntry_Object = MibTableRow
f3Pwe3SatopHistoryEntry = _F3Pwe3SatopHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1)
)
f3Pwe3SatopHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopStatsIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryEntry.setStatus("current")


class _F3Pwe3SatopHistoryIndex_Type(Integer32):
    """Custom type f3Pwe3SatopHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3Pwe3SatopHistoryIndex_Type.__name__ = "Integer32"
_F3Pwe3SatopHistoryIndex_Object = MibTableColumn
f3Pwe3SatopHistoryIndex = _F3Pwe3SatopHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 1),
    _F3Pwe3SatopHistoryIndex_Type()
)
f3Pwe3SatopHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryIndex.setStatus("current")
_F3Pwe3SatopHistoryTime_Type = DateAndTime
_F3Pwe3SatopHistoryTime_Object = MibTableColumn
f3Pwe3SatopHistoryTime = _F3Pwe3SatopHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 2),
    _F3Pwe3SatopHistoryTime_Type()
)
f3Pwe3SatopHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryTime.setStatus("current")
_F3Pwe3SatopHistoryValid_Type = TruthValue
_F3Pwe3SatopHistoryValid_Object = MibTableColumn
f3Pwe3SatopHistoryValid = _F3Pwe3SatopHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 3),
    _F3Pwe3SatopHistoryValid_Type()
)
f3Pwe3SatopHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryValid.setStatus("current")
_F3Pwe3SatopHistoryAction_Type = CmPmBinAction
_F3Pwe3SatopHistoryAction_Object = MibTableColumn
f3Pwe3SatopHistoryAction = _F3Pwe3SatopHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 4),
    _F3Pwe3SatopHistoryAction_Type()
)
f3Pwe3SatopHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryAction.setStatus("current")
_F3Pwe3SatopHistoryESs_Type = PerfCounter64
_F3Pwe3SatopHistoryESs_Object = MibTableColumn
f3Pwe3SatopHistoryESs = _F3Pwe3SatopHistoryESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 5),
    _F3Pwe3SatopHistoryESs_Type()
)
f3Pwe3SatopHistoryESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryESs.setStatus("current")
_F3Pwe3SatopHistorySESs_Type = PerfCounter64
_F3Pwe3SatopHistorySESs_Object = MibTableColumn
f3Pwe3SatopHistorySESs = _F3Pwe3SatopHistorySESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 6),
    _F3Pwe3SatopHistorySESs_Type()
)
f3Pwe3SatopHistorySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistorySESs.setStatus("current")
_F3Pwe3SatopHistoryEBs_Type = PerfCounter64
_F3Pwe3SatopHistoryEBs_Object = MibTableColumn
f3Pwe3SatopHistoryEBs = _F3Pwe3SatopHistoryEBs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 7),
    _F3Pwe3SatopHistoryEBs_Type()
)
f3Pwe3SatopHistoryEBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryEBs.setStatus("current")
_F3Pwe3SatopHistoryResyncs_Type = PerfCounter64
_F3Pwe3SatopHistoryResyncs_Object = MibTableColumn
f3Pwe3SatopHistoryResyncs = _F3Pwe3SatopHistoryResyncs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 8),
    _F3Pwe3SatopHistoryResyncs_Type()
)
f3Pwe3SatopHistoryResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryResyncs.setStatus("current")
_F3Pwe3SatopHistoryMaxJitter_Type = Unsigned32
_F3Pwe3SatopHistoryMaxJitter_Object = MibTableColumn
f3Pwe3SatopHistoryMaxJitter = _F3Pwe3SatopHistoryMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 9),
    _F3Pwe3SatopHistoryMaxJitter_Type()
)
f3Pwe3SatopHistoryMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryMaxJitter.setStatus("current")
_F3Pwe3SatopHistoryFramesTx_Type = PerfCounter64
_F3Pwe3SatopHistoryFramesTx_Object = MibTableColumn
f3Pwe3SatopHistoryFramesTx = _F3Pwe3SatopHistoryFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 10),
    _F3Pwe3SatopHistoryFramesTx_Type()
)
f3Pwe3SatopHistoryFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryFramesTx.setStatus("current")
_F3Pwe3SatopHistoryPayloadOctetsTx_Type = PerfCounter64
_F3Pwe3SatopHistoryPayloadOctetsTx_Object = MibTableColumn
f3Pwe3SatopHistoryPayloadOctetsTx = _F3Pwe3SatopHistoryPayloadOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 11),
    _F3Pwe3SatopHistoryPayloadOctetsTx_Type()
)
f3Pwe3SatopHistoryPayloadOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryPayloadOctetsTx.setStatus("current")
_F3Pwe3SatopHistoryFramesRx_Type = PerfCounter64
_F3Pwe3SatopHistoryFramesRx_Object = MibTableColumn
f3Pwe3SatopHistoryFramesRx = _F3Pwe3SatopHistoryFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 12),
    _F3Pwe3SatopHistoryFramesRx_Type()
)
f3Pwe3SatopHistoryFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryFramesRx.setStatus("current")
_F3Pwe3SatopHistoryPayloadOctetsRx_Type = PerfCounter64
_F3Pwe3SatopHistoryPayloadOctetsRx_Object = MibTableColumn
f3Pwe3SatopHistoryPayloadOctetsRx = _F3Pwe3SatopHistoryPayloadOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 13),
    _F3Pwe3SatopHistoryPayloadOctetsRx_Type()
)
f3Pwe3SatopHistoryPayloadOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryPayloadOctetsRx.setStatus("current")
_F3Pwe3SatopHistoryOutOfSeqFramesRx_Type = PerfCounter64
_F3Pwe3SatopHistoryOutOfSeqFramesRx_Object = MibTableColumn
f3Pwe3SatopHistoryOutOfSeqFramesRx = _F3Pwe3SatopHistoryOutOfSeqFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 14),
    _F3Pwe3SatopHistoryOutOfSeqFramesRx_Type()
)
f3Pwe3SatopHistoryOutOfSeqFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryOutOfSeqFramesRx.setStatus("current")
_F3Pwe3SatopHistoryLostFrames_Type = PerfCounter64
_F3Pwe3SatopHistoryLostFrames_Object = MibTableColumn
f3Pwe3SatopHistoryLostFrames = _F3Pwe3SatopHistoryLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 15),
    _F3Pwe3SatopHistoryLostFrames_Type()
)
f3Pwe3SatopHistoryLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryLostFrames.setStatus("current")
_F3Pwe3SatopHistoryLostFramesStateTrans_Type = PerfCounter64
_F3Pwe3SatopHistoryLostFramesStateTrans_Object = MibTableColumn
f3Pwe3SatopHistoryLostFramesStateTrans = _F3Pwe3SatopHistoryLostFramesStateTrans_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 16),
    _F3Pwe3SatopHistoryLostFramesStateTrans_Type()
)
f3Pwe3SatopHistoryLostFramesStateTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryLostFramesStateTrans.setStatus("current")
_F3Pwe3SatopHistoryMalformedFramesRx_Type = PerfCounter64
_F3Pwe3SatopHistoryMalformedFramesRx_Object = MibTableColumn
f3Pwe3SatopHistoryMalformedFramesRx = _F3Pwe3SatopHistoryMalformedFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 17),
    _F3Pwe3SatopHistoryMalformedFramesRx_Type()
)
f3Pwe3SatopHistoryMalformedFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryMalformedFramesRx.setStatus("current")
_F3Pwe3SatopHistoryJitterBufferLateFrames_Type = PerfCounter64
_F3Pwe3SatopHistoryJitterBufferLateFrames_Object = MibTableColumn
f3Pwe3SatopHistoryJitterBufferLateFrames = _F3Pwe3SatopHistoryJitterBufferLateFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 2, 1, 18),
    _F3Pwe3SatopHistoryJitterBufferLateFrames_Type()
)
f3Pwe3SatopHistoryJitterBufferLateFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopHistoryJitterBufferLateFrames.setStatus("current")
_F3Pwe3SatopThresholdTable_Object = MibTable
f3Pwe3SatopThresholdTable = _F3Pwe3SatopThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 3)
)
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdTable.setStatus("current")
_F3Pwe3SatopThresholdEntry_Object = MibTableRow
f3Pwe3SatopThresholdEntry = _F3Pwe3SatopThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 3, 1)
)
f3Pwe3SatopThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopStatsIndex"),
    (0, "F3-PWE3-MIB", "f3Pwe3SatopThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdEntry.setStatus("current")


class _F3Pwe3SatopThresholdIndex_Type(Integer32):
    """Custom type f3Pwe3SatopThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3Pwe3SatopThresholdIndex_Type.__name__ = "Integer32"
_F3Pwe3SatopThresholdIndex_Object = MibTableColumn
f3Pwe3SatopThresholdIndex = _F3Pwe3SatopThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 3, 1, 1),
    _F3Pwe3SatopThresholdIndex_Type()
)
f3Pwe3SatopThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdIndex.setStatus("current")
_F3Pwe3SatopThresholdInterval_Type = CmPmIntervalType
_F3Pwe3SatopThresholdInterval_Object = MibTableColumn
f3Pwe3SatopThresholdInterval = _F3Pwe3SatopThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 3, 1, 2),
    _F3Pwe3SatopThresholdInterval_Type()
)
f3Pwe3SatopThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdInterval.setStatus("current")
_F3Pwe3SatopThresholdVariable_Type = VariablePointer
_F3Pwe3SatopThresholdVariable_Object = MibTableColumn
f3Pwe3SatopThresholdVariable = _F3Pwe3SatopThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 3, 1, 3),
    _F3Pwe3SatopThresholdVariable_Type()
)
f3Pwe3SatopThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdVariable.setStatus("current")
_F3Pwe3SatopThresholdValueLo_Type = Unsigned32
_F3Pwe3SatopThresholdValueLo_Object = MibTableColumn
f3Pwe3SatopThresholdValueLo = _F3Pwe3SatopThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 3, 1, 4),
    _F3Pwe3SatopThresholdValueLo_Type()
)
f3Pwe3SatopThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdValueLo.setStatus("current")
_F3Pwe3SatopThresholdValueHi_Type = Unsigned32
_F3Pwe3SatopThresholdValueHi_Object = MibTableColumn
f3Pwe3SatopThresholdValueHi = _F3Pwe3SatopThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 3, 1, 5),
    _F3Pwe3SatopThresholdValueHi_Type()
)
f3Pwe3SatopThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdValueHi.setStatus("current")
_F3Pwe3SatopThresholdMonValue_Type = Counter64
_F3Pwe3SatopThresholdMonValue_Object = MibTableColumn
f3Pwe3SatopThresholdMonValue = _F3Pwe3SatopThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 2, 3, 1, 6),
    _F3Pwe3SatopThresholdMonValue_Type()
)
f3Pwe3SatopThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdMonValue.setStatus("current")
_F3Pwe3PerformanceNotifications_ObjectIdentity = ObjectIdentity
f3Pwe3PerformanceNotifications = _F3Pwe3PerformanceNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 3)
)
_F3Pwe3Conformance_ObjectIdentity = ObjectIdentity
f3Pwe3Conformance = _F3Pwe3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 4)
)
_F3Pwe3Compliances_ObjectIdentity = ObjectIdentity
f3Pwe3Compliances = _F3Pwe3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 4, 1)
)
_F3Pwe3Groups_ObjectIdentity = ObjectIdentity
f3Pwe3Groups = _F3Pwe3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 4, 2)
)

# Managed Objects groups

f3Pwe3ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 4, 2, 1)
)
f3Pwe3ObjectGroup.setObjects(
      *(("F3-PWE3-MIB", "f3Pwe3IdlePatternProfileIndex"),
        ("F3-PWE3-MIB", "f3Pwe3IdlePatternProfileByte"),
        ("F3-PWE3-MIB", "f3Pwe3ResyncProfileIndex"),
        ("F3-PWE3-MIB", "f3Pwe3ResyncProfileIncreaseFactor"),
        ("F3-PWE3-MIB", "f3Pwe3ResyncProfileDecreaseFactor"),
        ("F3-PWE3-MIB", "f3Pwe3ResyncProfileResyncThreshold"),
        ("F3-PWE3-MIB", "f3Pwe3LoopbackProfileIndex"),
        ("F3-PWE3-MIB", "f3Pwe3LoopbackProfileLength"),
        ("F3-PWE3-MIB", "f3Pwe3LoopbackProfilePattern"),
        ("F3-PWE3-MIB", "f3Pwe3LoopbackProfileRepeatTime"),
        ("F3-PWE3-MIB", "f3Pwe3LoopbackProfileClearLength"),
        ("F3-PWE3-MIB", "f3Pwe3LoopbackProfileClearPattern"),
        ("F3-PWE3-MIB", "f3Pwe3LossProfileIndex"),
        ("F3-PWE3-MIB", "f3Pwe3LossProfileLossStateEnterTime"),
        ("F3-PWE3-MIB", "f3Pwe3LossProfileLossStateExitTime"),
        ("F3-PWE3-MIB", "f3Pwe3AisStabilizationProfileIndex"),
        ("F3-PWE3-MIB", "f3Pwe3AisStabilizationProfileEnterTime"),
        ("F3-PWE3-MIB", "f3Pwe3AisStabilizationProfileExitTime"),
        ("F3-PWE3-MIB", "f3Pwe3SatopIndex"),
        ("F3-PWE3-MIB", "f3Pwe3SatopAlias"),
        ("F3-PWE3-MIB", "f3Pwe3SatopAdminState"),
        ("F3-PWE3-MIB", "f3Pwe3SatopOperationalState"),
        ("F3-PWE3-MIB", "f3Pwe3SatopSecondaryState"),
        ("F3-PWE3-MIB", "f3Pwe3SatopTDMEntity"),
        ("F3-PWE3-MIB", "f3Pwe3SatopDiscoveryType"),
        ("F3-PWE3-MIB", "f3Pwe3SatopRemoteIpAddress"),
        ("F3-PWE3-MIB", "f3Pwe3SatopRemoteMacAddress"),
        ("F3-PWE3-MIB", "f3Pwe3SatopEncapsulationType"),
        ("F3-PWE3-MIB", "f3Pwe3SatopRTPEnabled"),
        ("F3-PWE3-MIB", "f3Pwe3SatopRTPUpdateFrequency"),
        ("F3-PWE3-MIB", "f3Pwe3SatopControlWordEnabled"),
        ("F3-PWE3-MIB", "f3Pwe3SatopJitterBufferSize"),
        ("F3-PWE3-MIB", "f3Pwe3SatopPayloadSize"),
        ("F3-PWE3-MIB", "f3Pwe3SatopVlanId"),
        ("F3-PWE3-MIB", "f3Pwe3SatopVlanPriority"),
        ("F3-PWE3-MIB", "f3Pwe3SatopRxMplsLabel1"),
        ("F3-PWE3-MIB", "f3Pwe3SatopRxMplsLabel2"),
        ("F3-PWE3-MIB", "f3Pwe3SatopTxMplsLabel1"),
        ("F3-PWE3-MIB", "f3Pwe3SatopTxMplsLabel2"),
        ("F3-PWE3-MIB", "f3Pwe3SatopAisStabilizationProfile"),
        ("F3-PWE3-MIB", "f3Pwe3SatopResyncProfile"),
        ("F3-PWE3-MIB", "f3Pwe3SatopLossProfile"),
        ("F3-PWE3-MIB", "f3Pwe3SatopTransportMode"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStorageType"),
        ("F3-PWE3-MIB", "f3Pwe3SatopRowStatus"),
        ("F3-PWE3-MIB", "f3Pwe3SatopTDMEntityIndex"),
        ("F3-PWE3-MIB", "f3Pwe3SatopTDMEntityObject"),
        ("F3-PWE3-MIB", "f3Pwe3SatopTDMEntityStorageType"),
        ("F3-PWE3-MIB", "f3Pwe3SatopTDMEntityRowStatus"))
)
if mibBuilder.loadTexts:
    f3Pwe3ObjectGroup.setStatus("current")

f3Pwe3PerfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 4, 2, 2)
)
f3Pwe3PerfObjectGroup.setObjects(
      *(("F3-PWE3-MIB", "f3Pwe3SatopStatsIndex"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsIntervalType"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsValid"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsAction"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsESs"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsSESs"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsEBs"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsResyncs"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsMaxJitter"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsFramesTx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsPayloadOctetsTx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsFramesRx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsPayloadOctetsRx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsOutOfSeqFramesRx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsLostFrames"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsLostFramesStateTrans"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsMalformedFramesRx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopStatsJitterBufferLateFrames"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryIndex"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryTime"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryValid"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryAction"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryESs"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistorySESs"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryEBs"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryResyncs"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryMaxJitter"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryFramesTx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryPayloadOctetsTx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryFramesRx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryPayloadOctetsRx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryOutOfSeqFramesRx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryLostFrames"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryLostFramesStateTrans"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryMalformedFramesRx"),
        ("F3-PWE3-MIB", "f3Pwe3SatopHistoryJitterBufferLateFrames"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdIndex"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdInterval"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdVariable"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdValueLo"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdValueHi"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3Pwe3PerfObjectGroup.setStatus("current")


# Notification objects

f3Pwe3SatopThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 3, 1)
)
f3Pwe3SatopThresholdCrossingAlert.setObjects(
      *(("F3-PWE3-MIB", "f3Pwe3SatopThresholdIndex"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdInterval"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdVariable"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdValueLo"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdValueHi"),
        ("F3-PWE3-MIB", "f3Pwe3SatopThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3Pwe3SatopThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups

f3Pwe3PerfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 4, 2, 3)
)
f3Pwe3PerfNotifGroup.setObjects(
    ("F3-PWE3-MIB", "f3Pwe3SatopThresholdCrossingAlert")
)
if mibBuilder.loadTexts:
    f3Pwe3PerfNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f3Pwe3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 19, 4, 1, 1)
)
f3Pwe3Compliance.setObjects(
      *(("F3-PWE3-MIB", "f3Pwe3ObjectGroup"),
        ("F3-PWE3-MIB", "f3Pwe3PerfObjectGroup"),
        ("F3-PWE3-MIB", "f3Pwe3PerfNotifGroup"))
)
if mibBuilder.loadTexts:
    f3Pwe3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-PWE3-MIB",
    **{"PWE3SatopDiscoveryType": PWE3SatopDiscoveryType,
       "PWE3SatopEncapsulationType": PWE3SatopEncapsulationType,
       "PWE3SatopRTPTSUpdateFreqType": PWE3SatopRTPTSUpdateFreqType,
       "PWE3SatopTransportMode": PWE3SatopTransportMode,
       "MplsLabel": MplsLabel,
       "f3Pwe3MIB": f3Pwe3MIB,
       "f3Pwe3ConfigObjects": f3Pwe3ConfigObjects,
       "f3Pwe3IdlePatternProfileTable": f3Pwe3IdlePatternProfileTable,
       "f3Pwe3IdlePatternProfileEntry": f3Pwe3IdlePatternProfileEntry,
       "f3Pwe3IdlePatternProfileIndex": f3Pwe3IdlePatternProfileIndex,
       "f3Pwe3IdlePatternProfileByte": f3Pwe3IdlePatternProfileByte,
       "f3Pwe3ResyncProfileTable": f3Pwe3ResyncProfileTable,
       "f3Pwe3ResyncProfileEntry": f3Pwe3ResyncProfileEntry,
       "f3Pwe3ResyncProfileIndex": f3Pwe3ResyncProfileIndex,
       "f3Pwe3ResyncProfileIncreaseFactor": f3Pwe3ResyncProfileIncreaseFactor,
       "f3Pwe3ResyncProfileDecreaseFactor": f3Pwe3ResyncProfileDecreaseFactor,
       "f3Pwe3ResyncProfileResyncThreshold": f3Pwe3ResyncProfileResyncThreshold,
       "f3Pwe3LoopbackProfileTable": f3Pwe3LoopbackProfileTable,
       "f3Pwe3LoopbackProfileEntry": f3Pwe3LoopbackProfileEntry,
       "f3Pwe3LoopbackProfileIndex": f3Pwe3LoopbackProfileIndex,
       "f3Pwe3LoopbackProfileLength": f3Pwe3LoopbackProfileLength,
       "f3Pwe3LoopbackProfilePattern": f3Pwe3LoopbackProfilePattern,
       "f3Pwe3LoopbackProfileRepeatTime": f3Pwe3LoopbackProfileRepeatTime,
       "f3Pwe3LoopbackProfileClearLength": f3Pwe3LoopbackProfileClearLength,
       "f3Pwe3LoopbackProfileClearPattern": f3Pwe3LoopbackProfileClearPattern,
       "f3Pwe3LossProfileTable": f3Pwe3LossProfileTable,
       "f3Pwe3LossProfileEntry": f3Pwe3LossProfileEntry,
       "f3Pwe3LossProfileIndex": f3Pwe3LossProfileIndex,
       "f3Pwe3LossProfileLossStateEnterTime": f3Pwe3LossProfileLossStateEnterTime,
       "f3Pwe3LossProfileLossStateExitTime": f3Pwe3LossProfileLossStateExitTime,
       "f3Pwe3AisStabilizationProfileTable": f3Pwe3AisStabilizationProfileTable,
       "f3Pwe3AisStabilizationProfileEntry": f3Pwe3AisStabilizationProfileEntry,
       "f3Pwe3AisStabilizationProfileIndex": f3Pwe3AisStabilizationProfileIndex,
       "f3Pwe3AisStabilizationProfileEnterTime": f3Pwe3AisStabilizationProfileEnterTime,
       "f3Pwe3AisStabilizationProfileExitTime": f3Pwe3AisStabilizationProfileExitTime,
       "f3Pwe3SatopTable": f3Pwe3SatopTable,
       "f3Pwe3SatopEntry": f3Pwe3SatopEntry,
       "f3Pwe3SatopIndex": f3Pwe3SatopIndex,
       "f3Pwe3SatopAlias": f3Pwe3SatopAlias,
       "f3Pwe3SatopAdminState": f3Pwe3SatopAdminState,
       "f3Pwe3SatopOperationalState": f3Pwe3SatopOperationalState,
       "f3Pwe3SatopSecondaryState": f3Pwe3SatopSecondaryState,
       "f3Pwe3SatopTDMEntity": f3Pwe3SatopTDMEntity,
       "f3Pwe3SatopDiscoveryType": f3Pwe3SatopDiscoveryType,
       "f3Pwe3SatopRemoteIpAddress": f3Pwe3SatopRemoteIpAddress,
       "f3Pwe3SatopRemoteMacAddress": f3Pwe3SatopRemoteMacAddress,
       "f3Pwe3SatopEncapsulationType": f3Pwe3SatopEncapsulationType,
       "f3Pwe3SatopRTPEnabled": f3Pwe3SatopRTPEnabled,
       "f3Pwe3SatopRTPUpdateFrequency": f3Pwe3SatopRTPUpdateFrequency,
       "f3Pwe3SatopControlWordEnabled": f3Pwe3SatopControlWordEnabled,
       "f3Pwe3SatopJitterBufferSize": f3Pwe3SatopJitterBufferSize,
       "f3Pwe3SatopPayloadSize": f3Pwe3SatopPayloadSize,
       "f3Pwe3SatopVlanId": f3Pwe3SatopVlanId,
       "f3Pwe3SatopVlanPriority": f3Pwe3SatopVlanPriority,
       "f3Pwe3SatopRxMplsLabel1": f3Pwe3SatopRxMplsLabel1,
       "f3Pwe3SatopRxMplsLabel2": f3Pwe3SatopRxMplsLabel2,
       "f3Pwe3SatopTxMplsLabel1": f3Pwe3SatopTxMplsLabel1,
       "f3Pwe3SatopTxMplsLabel2": f3Pwe3SatopTxMplsLabel2,
       "f3Pwe3SatopAisStabilizationProfile": f3Pwe3SatopAisStabilizationProfile,
       "f3Pwe3SatopResyncProfile": f3Pwe3SatopResyncProfile,
       "f3Pwe3SatopLossProfile": f3Pwe3SatopLossProfile,
       "f3Pwe3SatopTransportMode": f3Pwe3SatopTransportMode,
       "f3Pwe3SatopStorageType": f3Pwe3SatopStorageType,
       "f3Pwe3SatopRowStatus": f3Pwe3SatopRowStatus,
       "f3Pwe3SatopTDMEntitiesTable": f3Pwe3SatopTDMEntitiesTable,
       "f3Pwe3SatopTDMEntitiesEntry": f3Pwe3SatopTDMEntitiesEntry,
       "f3Pwe3SatopTDMEntityIndex": f3Pwe3SatopTDMEntityIndex,
       "f3Pwe3SatopTDMEntityObject": f3Pwe3SatopTDMEntityObject,
       "f3Pwe3SatopTDMEntityStorageType": f3Pwe3SatopTDMEntityStorageType,
       "f3Pwe3SatopTDMEntityRowStatus": f3Pwe3SatopTDMEntityRowStatus,
       "f3Pwe3PerformanceObjects": f3Pwe3PerformanceObjects,
       "f3Pwe3SatopStatsTable": f3Pwe3SatopStatsTable,
       "f3Pwe3SatopStatsEntry": f3Pwe3SatopStatsEntry,
       "f3Pwe3SatopStatsIndex": f3Pwe3SatopStatsIndex,
       "f3Pwe3SatopStatsIntervalType": f3Pwe3SatopStatsIntervalType,
       "f3Pwe3SatopStatsValid": f3Pwe3SatopStatsValid,
       "f3Pwe3SatopStatsAction": f3Pwe3SatopStatsAction,
       "f3Pwe3SatopStatsESs": f3Pwe3SatopStatsESs,
       "f3Pwe3SatopStatsSESs": f3Pwe3SatopStatsSESs,
       "f3Pwe3SatopStatsEBs": f3Pwe3SatopStatsEBs,
       "f3Pwe3SatopStatsResyncs": f3Pwe3SatopStatsResyncs,
       "f3Pwe3SatopStatsMaxJitter": f3Pwe3SatopStatsMaxJitter,
       "f3Pwe3SatopStatsFramesTx": f3Pwe3SatopStatsFramesTx,
       "f3Pwe3SatopStatsPayloadOctetsTx": f3Pwe3SatopStatsPayloadOctetsTx,
       "f3Pwe3SatopStatsFramesRx": f3Pwe3SatopStatsFramesRx,
       "f3Pwe3SatopStatsPayloadOctetsRx": f3Pwe3SatopStatsPayloadOctetsRx,
       "f3Pwe3SatopStatsOutOfSeqFramesRx": f3Pwe3SatopStatsOutOfSeqFramesRx,
       "f3Pwe3SatopStatsLostFrames": f3Pwe3SatopStatsLostFrames,
       "f3Pwe3SatopStatsLostFramesStateTrans": f3Pwe3SatopStatsLostFramesStateTrans,
       "f3Pwe3SatopStatsMalformedFramesRx": f3Pwe3SatopStatsMalformedFramesRx,
       "f3Pwe3SatopStatsJitterBufferLateFrames": f3Pwe3SatopStatsJitterBufferLateFrames,
       "f3Pwe3SatopHistoryTable": f3Pwe3SatopHistoryTable,
       "f3Pwe3SatopHistoryEntry": f3Pwe3SatopHistoryEntry,
       "f3Pwe3SatopHistoryIndex": f3Pwe3SatopHistoryIndex,
       "f3Pwe3SatopHistoryTime": f3Pwe3SatopHistoryTime,
       "f3Pwe3SatopHistoryValid": f3Pwe3SatopHistoryValid,
       "f3Pwe3SatopHistoryAction": f3Pwe3SatopHistoryAction,
       "f3Pwe3SatopHistoryESs": f3Pwe3SatopHistoryESs,
       "f3Pwe3SatopHistorySESs": f3Pwe3SatopHistorySESs,
       "f3Pwe3SatopHistoryEBs": f3Pwe3SatopHistoryEBs,
       "f3Pwe3SatopHistoryResyncs": f3Pwe3SatopHistoryResyncs,
       "f3Pwe3SatopHistoryMaxJitter": f3Pwe3SatopHistoryMaxJitter,
       "f3Pwe3SatopHistoryFramesTx": f3Pwe3SatopHistoryFramesTx,
       "f3Pwe3SatopHistoryPayloadOctetsTx": f3Pwe3SatopHistoryPayloadOctetsTx,
       "f3Pwe3SatopHistoryFramesRx": f3Pwe3SatopHistoryFramesRx,
       "f3Pwe3SatopHistoryPayloadOctetsRx": f3Pwe3SatopHistoryPayloadOctetsRx,
       "f3Pwe3SatopHistoryOutOfSeqFramesRx": f3Pwe3SatopHistoryOutOfSeqFramesRx,
       "f3Pwe3SatopHistoryLostFrames": f3Pwe3SatopHistoryLostFrames,
       "f3Pwe3SatopHistoryLostFramesStateTrans": f3Pwe3SatopHistoryLostFramesStateTrans,
       "f3Pwe3SatopHistoryMalformedFramesRx": f3Pwe3SatopHistoryMalformedFramesRx,
       "f3Pwe3SatopHistoryJitterBufferLateFrames": f3Pwe3SatopHistoryJitterBufferLateFrames,
       "f3Pwe3SatopThresholdTable": f3Pwe3SatopThresholdTable,
       "f3Pwe3SatopThresholdEntry": f3Pwe3SatopThresholdEntry,
       "f3Pwe3SatopThresholdIndex": f3Pwe3SatopThresholdIndex,
       "f3Pwe3SatopThresholdInterval": f3Pwe3SatopThresholdInterval,
       "f3Pwe3SatopThresholdVariable": f3Pwe3SatopThresholdVariable,
       "f3Pwe3SatopThresholdValueLo": f3Pwe3SatopThresholdValueLo,
       "f3Pwe3SatopThresholdValueHi": f3Pwe3SatopThresholdValueHi,
       "f3Pwe3SatopThresholdMonValue": f3Pwe3SatopThresholdMonValue,
       "f3Pwe3PerformanceNotifications": f3Pwe3PerformanceNotifications,
       "f3Pwe3SatopThresholdCrossingAlert": f3Pwe3SatopThresholdCrossingAlert,
       "f3Pwe3Conformance": f3Pwe3Conformance,
       "f3Pwe3Compliances": f3Pwe3Compliances,
       "f3Pwe3Compliance": f3Pwe3Compliance,
       "f3Pwe3Groups": f3Pwe3Groups,
       "f3Pwe3ObjectGroup": f3Pwe3ObjectGroup,
       "f3Pwe3PerfObjectGroup": f3Pwe3PerfObjectGroup,
       "f3Pwe3PerfNotifGroup": f3Pwe3PerfNotifGroup}
)
