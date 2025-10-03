# SNMP MIB module (TN-SYNCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-SYNCE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:32:27 2025
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

(ModuleIdentity,
 ObjectIdentity,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "ModuleIdentity",
    "ObjectIdentity",
    "entPhysicalIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnSynceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122)
)
if mibBuilder.loadTexts:
    tnSynceMIB.setRevisions(
        ("2013-05-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSynce_ObjectIdentity = ObjectIdentity
tnSynce = _TnSynce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1)
)
_TnSyncETable_Object = MibTable
tnSyncETable = _TnSyncETable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1)
)
if mibBuilder.loadTexts:
    tnSyncETable.setStatus("current")
_TnSyncEEntry_Object = MibTableRow
tnSyncEEntry = _TnSyncEEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1)
)
tnSyncEEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEEntry.setStatus("current")


class _TnSyncEStateMode_Type(Integer32):
    """Custom type tnSyncEStateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("selected", 2),
          ("nonrevertive", 3),
          ("revertive", 4),
          ("holdover", 5),
          ("freerun", 6))
    )


_TnSyncEStateMode_Type.__name__ = "Integer32"
_TnSyncEStateMode_Object = MibTableColumn
tnSyncEStateMode = _TnSyncEStateMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1, 1),
    _TnSyncEStateMode_Type()
)
tnSyncEStateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEStateMode.setStatus("current")
_TnSyncEStateWTRTime_Type = Integer32
_TnSyncEStateWTRTime_Object = MibTableColumn
tnSyncEStateWTRTime = _TnSyncEStateWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1, 2),
    _TnSyncEStateWTRTime_Type()
)
tnSyncEStateWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEStateWTRTime.setStatus("current")


class _TnSyncEStateSSMHoldOver_Type(Integer32):
    """Custom type tnSyncEStateSSMHoldOver based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("prc", 1),
          ("ssua", 2),
          ("ssub", 3),
          ("eec2", 4),
          ("eec1", 5),
          ("dnu", 6),
          ("inv", 7))
    )


_TnSyncEStateSSMHoldOver_Type.__name__ = "Integer32"
_TnSyncEStateSSMHoldOver_Object = MibTableColumn
tnSyncEStateSSMHoldOver = _TnSyncEStateSSMHoldOver_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1, 3),
    _TnSyncEStateSSMHoldOver_Type()
)
tnSyncEStateSSMHoldOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEStateSSMHoldOver.setStatus("current")


class _TnSyncEStateSSMFreeRun_Type(Integer32):
    """Custom type tnSyncEStateSSMFreeRun based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("prc", 1),
          ("ssua", 2),
          ("ssub", 3),
          ("eec2", 4),
          ("eec1", 5),
          ("dnu", 6),
          ("inv", 7))
    )


_TnSyncEStateSSMFreeRun_Type.__name__ = "Integer32"
_TnSyncEStateSSMFreeRun_Object = MibTableColumn
tnSyncEStateSSMFreeRun = _TnSyncEStateSSMFreeRun_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1, 4),
    _TnSyncEStateSSMFreeRun_Type()
)
tnSyncEStateSSMFreeRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEStateSSMFreeRun.setStatus("current")
_TnSyncEAlarmStateLOL_Type = TruthValue
_TnSyncEAlarmStateLOL_Object = MibTableColumn
tnSyncEAlarmStateLOL = _TnSyncEAlarmStateLOL_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1, 5),
    _TnSyncEAlarmStateLOL_Type()
)
tnSyncEAlarmStateLOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEAlarmStateLOL.setStatus("current")
_TnSyncEAlarmStateDHOLD_Type = TruthValue
_TnSyncEAlarmStateDHOLD_Object = MibTableColumn
tnSyncEAlarmStateDHOLD = _TnSyncEAlarmStateDHOLD_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1, 6),
    _TnSyncEAlarmStateDHOLD_Type()
)
tnSyncEAlarmStateDHOLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEAlarmStateDHOLD.setStatus("current")


class _TnSyncESelState_Type(Integer32):
    """Custom type tnSyncESelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lockedto", 1),
          ("holdover", 2),
          ("freerun", 3),
          ("prelock2", 4),
          ("prelock", 5),
          ("lossoflock", 6))
    )


_TnSyncESelState_Type.__name__ = "Integer32"
_TnSyncESelState_Object = MibTableColumn
tnSyncESelState = _TnSyncESelState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1, 7),
    _TnSyncESelState_Type()
)
tnSyncESelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncESelState.setStatus("current")
_TnSyncEClkSrc_Type = Integer32
_TnSyncEClkSrc_Object = MibTableColumn
tnSyncEClkSrc = _TnSyncEClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 1, 1, 8),
    _TnSyncEClkSrc_Type()
)
tnSyncEClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEClkSrc.setStatus("current")
_TnSyncEClkSourceTable_Object = MibTable
tnSyncEClkSourceTable = _TnSyncEClkSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2)
)
if mibBuilder.loadTexts:
    tnSyncEClkSourceTable.setStatus("current")
_TnSyncEClkSourceEntry_Object = MibTableRow
tnSyncEClkSourceEntry = _TnSyncEClkSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1)
)
tnSyncEClkSourceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-SYNCE-MIB", "tnSyncEClkSourceIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEClkSourceEntry.setStatus("current")
_TnSyncEClkSourceIndex_Type = Integer32
_TnSyncEClkSourceIndex_Object = MibTableColumn
tnSyncEClkSourceIndex = _TnSyncEClkSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 1),
    _TnSyncEClkSourceIndex_Type()
)
tnSyncEClkSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEClkSourceIndex.setStatus("current")
_TnSyncEConfPort_Type = Integer32
_TnSyncEConfPort_Object = MibTableColumn
tnSyncEConfPort = _TnSyncEConfPort_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 2),
    _TnSyncEConfPort_Type()
)
tnSyncEConfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEConfPort.setStatus("current")


class _TnSyncEConfSSMOverwrite_Type(Integer32):
    """Custom type tnSyncEConfSSMOverwrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("prc", 1),
          ("ssua", 2),
          ("ssub", 3),
          ("eec2", 4),
          ("eec1", 5),
          ("dnu", 6))
    )


_TnSyncEConfSSMOverwrite_Type.__name__ = "Integer32"
_TnSyncEConfSSMOverwrite_Object = MibTableColumn
tnSyncEConfSSMOverwrite = _TnSyncEConfSSMOverwrite_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 3),
    _TnSyncEConfSSMOverwrite_Type()
)
tnSyncEConfSSMOverwrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEConfSSMOverwrite.setStatus("current")
_TnSyncEConfHoldOff_Type = Integer32
_TnSyncEConfHoldOff_Object = MibTableColumn
tnSyncEConfHoldOff = _TnSyncEConfHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 4),
    _TnSyncEConfHoldOff_Type()
)
tnSyncEConfHoldOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEConfHoldOff.setStatus("current")


class _TnSyncEConfANEG_Type(Integer32):
    """Custom type tnSyncEConfANEG based on Integer32"""
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
        *(("none", 0),
          ("slave", 1),
          ("master", 2),
          ("forced", 3))
    )


_TnSyncEConfANEG_Type.__name__ = "Integer32"
_TnSyncEConfANEG_Object = MibTableColumn
tnSyncEConfANEG = _TnSyncEConfANEG_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 5),
    _TnSyncEConfANEG_Type()
)
tnSyncEConfANEG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEConfANEG.setStatus("current")
_TnSyncEPriority_Type = Integer32
_TnSyncEPriority_Object = MibTableColumn
tnSyncEPriority = _TnSyncEPriority_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 6),
    _TnSyncEPriority_Type()
)
tnSyncEPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEPriority.setStatus("current")
_TnSyncEClear_Type = TruthValue
_TnSyncEClear_Object = MibTableColumn
tnSyncEClear = _TnSyncEClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 7),
    _TnSyncEClear_Type()
)
tnSyncEClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEClear.setStatus("current")
_TnSyncEAlarmStateLOCS_Type = TruthValue
_TnSyncEAlarmStateLOCS_Object = MibTableColumn
tnSyncEAlarmStateLOCS = _TnSyncEAlarmStateLOCS_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 8),
    _TnSyncEAlarmStateLOCS_Type()
)
tnSyncEAlarmStateLOCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEAlarmStateLOCS.setStatus("current")
_TnSyncEAlarmStateSSM_Type = TruthValue
_TnSyncEAlarmStateSSM_Object = MibTableColumn
tnSyncEAlarmStateSSM = _TnSyncEAlarmStateSSM_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 9),
    _TnSyncEAlarmStateSSM_Type()
)
tnSyncEAlarmStateSSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEAlarmStateSSM.setStatus("current")
_TnSyncEAlarmStateWTR_Type = TruthValue
_TnSyncEAlarmStateWTR_Object = MibTableColumn
tnSyncEAlarmStateWTR = _TnSyncEAlarmStateWTR_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 10),
    _TnSyncEAlarmStateWTR_Type()
)
tnSyncEAlarmStateWTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEAlarmStateWTR.setStatus("current")
_TnSyncENominated_Type = TruthValue
_TnSyncENominated_Object = MibTableColumn
tnSyncENominated = _TnSyncENominated_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 2, 1, 11),
    _TnSyncENominated_Type()
)
tnSyncENominated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncENominated.setStatus("current")
_TnSyncEPortTable_Object = MibTable
tnSyncEPortTable = _TnSyncEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 3)
)
if mibBuilder.loadTexts:
    tnSyncEPortTable.setStatus("current")
_TnSyncEPortEntry_Object = MibTableRow
tnSyncEPortEntry = _TnSyncEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 3, 1)
)
tnSyncEPortEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TN-SYNCE-MIB", "tnSyncEStatePortIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEPortEntry.setStatus("current")
_TnSyncEStatePortIndex_Type = Integer32
_TnSyncEStatePortIndex_Object = MibTableColumn
tnSyncEStatePortIndex = _TnSyncEStatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 3, 1, 1),
    _TnSyncEStatePortIndex_Type()
)
tnSyncEStatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEStatePortIndex.setStatus("current")


class _TnSyncEStateTxSSM_Type(Integer32):
    """Custom type tnSyncEStateTxSSM based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("prc", 1),
          ("ssua", 2),
          ("ssub", 3),
          ("dnu", 4),
          ("eec2", 5),
          ("eec1", 6),
          ("inv", 7),
          ("fail", 8),
          ("link", 9))
    )


_TnSyncEStateTxSSM_Type.__name__ = "Integer32"
_TnSyncEStateTxSSM_Object = MibTableColumn
tnSyncEStateTxSSM = _TnSyncEStateTxSSM_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 3, 1, 2),
    _TnSyncEStateTxSSM_Type()
)
tnSyncEStateTxSSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEStateTxSSM.setStatus("current")


class _TnSyncEStateRxSSM_Type(Integer32):
    """Custom type tnSyncEStateRxSSM based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("prc", 1),
          ("ssua", 2),
          ("ssub", 3),
          ("dnu", 4),
          ("eec2", 5),
          ("eec1", 6),
          ("inv", 7),
          ("fail", 8),
          ("link", 9))
    )


_TnSyncEStateRxSSM_Type.__name__ = "Integer32"
_TnSyncEStateRxSSM_Object = MibTableColumn
tnSyncEStateRxSSM = _TnSyncEStateRxSSM_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 3, 1, 3),
    _TnSyncEStateRxSSM_Type()
)
tnSyncEStateRxSSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEStateRxSSM.setStatus("current")


class _TnSyncEStateSSMMode_Type(Integer32):
    """Custom type tnSyncEStateSSMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_TnSyncEStateSSMMode_Type.__name__ = "Integer32"
_TnSyncEStateSSMMode_Object = MibTableColumn
tnSyncEStateSSMMode = _TnSyncEStateSSMMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 3, 1, 4),
    _TnSyncEStateSSMMode_Type()
)
tnSyncEStateSSMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEStateSSMMode.setStatus("current")


class _TnSyncESSMEnabled_Type(Integer32):
    """Custom type tnSyncESSMEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnSyncESSMEnabled_Type.__name__ = "Integer32"
_TnSyncESSMEnabled_Object = MibTableColumn
tnSyncESSMEnabled = _TnSyncESSMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 3, 1, 5),
    _TnSyncESSMEnabled_Type()
)
tnSyncESSMEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncESSMEnabled.setStatus("current")
_TnSyncEExtTable_Object = MibTable
tnSyncEExtTable = _TnSyncEExtTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4)
)
if mibBuilder.loadTexts:
    tnSyncEExtTable.setStatus("current")
_TnSyncEExtEntry_Object = MibTableRow
tnSyncEExtEntry = _TnSyncEExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4, 1)
)
tnSyncEExtEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnSyncEExtEntry.setStatus("current")


class _TnSyncEExtInState_Type(Integer32):
    """Custom type tnSyncEExtInState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnSyncEExtInState_Type.__name__ = "Integer32"
_TnSyncEExtInState_Object = MibTableColumn
tnSyncEExtInState = _TnSyncEExtInState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4, 1, 1),
    _TnSyncEExtInState_Type()
)
tnSyncEExtInState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEExtInState.setStatus("current")


class _TnSyncEExtOutState_Type(Integer32):
    """Custom type tnSyncEExtOutState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_TnSyncEExtOutState_Type.__name__ = "Integer32"
_TnSyncEExtOutState_Object = MibTableColumn
tnSyncEExtOutState = _TnSyncEExtOutState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4, 1, 2),
    _TnSyncEExtOutState_Type()
)
tnSyncEExtOutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEExtOutState.setStatus("current")


class _TnSyncEExtInFreq_Type(Integer32):
    """Custom type tnSyncEExtInFreq based on Integer32"""
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
        *(("f8kHz", 1),
          ("f64kHz", 2),
          ("f1544kHz", 3),
          ("f2048kHz", 4),
          ("f10000kHz", 5),
          ("f19440kHz", 6),
          ("f25Mhz", 7))
    )


_TnSyncEExtInFreq_Type.__name__ = "Integer32"
_TnSyncEExtInFreq_Object = MibTableColumn
tnSyncEExtInFreq = _TnSyncEExtInFreq_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4, 1, 3),
    _TnSyncEExtInFreq_Type()
)
tnSyncEExtInFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEExtInFreq.setStatus("current")


class _TnSyncEExtOutFreq_Type(Integer32):
    """Custom type tnSyncEExtOutFreq based on Integer32"""
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
        *(("f8kHz", 1),
          ("f64kHz", 2),
          ("f1544kHz", 3),
          ("f2048kHz", 4),
          ("f10000kHz", 5),
          ("f19440kHz", 6),
          ("f25Mhz", 7))
    )


_TnSyncEExtOutFreq_Type.__name__ = "Integer32"
_TnSyncEExtOutFreq_Object = MibTableColumn
tnSyncEExtOutFreq = _TnSyncEExtOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4, 1, 4),
    _TnSyncEExtOutFreq_Type()
)
tnSyncEExtOutFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEExtOutFreq.setStatus("current")


class _TnSyncEExtImpedance_Type(Integer32):
    """Custom type tnSyncEExtImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("imp50", 1),
          ("imp75", 2),
          ("hi-Z", 3))
    )


_TnSyncEExtImpedance_Type.__name__ = "Integer32"
_TnSyncEExtImpedance_Object = MibTableColumn
tnSyncEExtImpedance = _TnSyncEExtImpedance_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4, 1, 5),
    _TnSyncEExtImpedance_Type()
)
tnSyncEExtImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnSyncEExtImpedance.setStatus("current")
_TnSyncEActualInFreq_Type = Integer32
_TnSyncEActualInFreq_Object = MibTableColumn
tnSyncEActualInFreq = _TnSyncEActualInFreq_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4, 1, 6),
    _TnSyncEActualInFreq_Type()
)
tnSyncEActualInFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEActualInFreq.setStatus("current")
_TnSyncEActualOutFreq_Type = Integer32
_TnSyncEActualOutFreq_Object = MibTableColumn
tnSyncEActualOutFreq = _TnSyncEActualOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 122, 1, 4, 1, 7),
    _TnSyncEActualOutFreq_Type()
)
tnSyncEActualOutFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSyncEActualOutFreq.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SYNCE-MIB",
    **{"tnSynceMIB": tnSynceMIB,
       "tnSynce": tnSynce,
       "tnSyncETable": tnSyncETable,
       "tnSyncEEntry": tnSyncEEntry,
       "tnSyncEStateMode": tnSyncEStateMode,
       "tnSyncEStateWTRTime": tnSyncEStateWTRTime,
       "tnSyncEStateSSMHoldOver": tnSyncEStateSSMHoldOver,
       "tnSyncEStateSSMFreeRun": tnSyncEStateSSMFreeRun,
       "tnSyncEAlarmStateLOL": tnSyncEAlarmStateLOL,
       "tnSyncEAlarmStateDHOLD": tnSyncEAlarmStateDHOLD,
       "tnSyncESelState": tnSyncESelState,
       "tnSyncEClkSrc": tnSyncEClkSrc,
       "tnSyncEClkSourceTable": tnSyncEClkSourceTable,
       "tnSyncEClkSourceEntry": tnSyncEClkSourceEntry,
       "tnSyncEClkSourceIndex": tnSyncEClkSourceIndex,
       "tnSyncEConfPort": tnSyncEConfPort,
       "tnSyncEConfSSMOverwrite": tnSyncEConfSSMOverwrite,
       "tnSyncEConfHoldOff": tnSyncEConfHoldOff,
       "tnSyncEConfANEG": tnSyncEConfANEG,
       "tnSyncEPriority": tnSyncEPriority,
       "tnSyncEClear": tnSyncEClear,
       "tnSyncEAlarmStateLOCS": tnSyncEAlarmStateLOCS,
       "tnSyncEAlarmStateSSM": tnSyncEAlarmStateSSM,
       "tnSyncEAlarmStateWTR": tnSyncEAlarmStateWTR,
       "tnSyncENominated": tnSyncENominated,
       "tnSyncEPortTable": tnSyncEPortTable,
       "tnSyncEPortEntry": tnSyncEPortEntry,
       "tnSyncEStatePortIndex": tnSyncEStatePortIndex,
       "tnSyncEStateTxSSM": tnSyncEStateTxSSM,
       "tnSyncEStateRxSSM": tnSyncEStateRxSSM,
       "tnSyncEStateSSMMode": tnSyncEStateSSMMode,
       "tnSyncESSMEnabled": tnSyncESSMEnabled,
       "tnSyncEExtTable": tnSyncEExtTable,
       "tnSyncEExtEntry": tnSyncEExtEntry,
       "tnSyncEExtInState": tnSyncEExtInState,
       "tnSyncEExtOutState": tnSyncEExtOutState,
       "tnSyncEExtInFreq": tnSyncEExtInFreq,
       "tnSyncEExtOutFreq": tnSyncEExtOutFreq,
       "tnSyncEExtImpedance": tnSyncEExtImpedance,
       "tnSyncEActualInFreq": tnSyncEActualInFreq,
       "tnSyncEActualOutFreq": tnSyncEActualOutFreq}
)
