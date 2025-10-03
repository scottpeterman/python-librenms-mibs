# SNMP MIB module (F3-POPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-POPM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:16:37 2025
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

(PerfCounter64,) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "PerfCounter64")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortEntry,
 cmEthernetNetPortEntry) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortEntry",
    "cmEthernetNetPortEntry")

(cmEthernetAccPortHistoryEntry,
 cmEthernetAccPortStatsEntry,
 cmEthernetNetPortHistoryEntry,
 cmEthernetNetPortStatsEntry) = mibBuilder.importSymbols(
    "CM-PERFORMANCE-MIB",
    "cmEthernetAccPortHistoryEntry",
    "cmEthernetAccPortStatsEntry",
    "cmEthernetNetPortHistoryEntry",
    "cmEthernetNetPortStatsEntry")

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
 PhysAddress,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3POPMMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16)
)
if mibBuilder.loadTexts:
    f3POPMMib.setRevisions(
        ("2011-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class POPMGlitchRejectionLevel(TextualConvention, Integer32):
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
          ("low", 2),
          ("medium", 3),
          ("high", 4))
    )



class POPMState(TextualConvention, Integer32):
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
        *(("not-applicable", 1),
          ("inoperable", 2),
          ("not-available", 3),
          ("calibrating", 4),
          ("monitoring", 5),
          ("paused", 6),
          ("inhibited-R", 7),
          ("inhibited-NR", 8))
    )



class POPMClearAlarmsAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("clear", 1))
    )



# MIB Managed Objects in the order of their OIDs

_F3POPMObjects_ObjectIdentity = ObjectIdentity
f3POPMObjects = _F3POPMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1)
)
_F3EthernetNetPortPOPMonitorTable_Object = MibTable
f3EthernetNetPortPOPMonitorTable = _F3EthernetNetPortPOPMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1)
)
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorTable.setStatus("current")
_F3EthernetNetPortPOPMonitorEntry_Object = MibTableRow
f3EthernetNetPortPOPMonitorEntry = _F3EthernetNetPortPOPMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorEntry.setStatus("current")
_F3EthernetNetPortPOPMonitorEnabled_Type = TruthValue
_F3EthernetNetPortPOPMonitorEnabled_Object = MibTableColumn
f3EthernetNetPortPOPMonitorEnabled = _F3EthernetNetPortPOPMonitorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1, 1),
    _F3EthernetNetPortPOPMonitorEnabled_Type()
)
f3EthernetNetPortPOPMonitorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorEnabled.setStatus("current")
_F3EthernetNetPortPOPMonitorOperRangeHi_Type = Integer32
_F3EthernetNetPortPOPMonitorOperRangeHi_Object = MibTableColumn
f3EthernetNetPortPOPMonitorOperRangeHi = _F3EthernetNetPortPOPMonitorOperRangeHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1, 2),
    _F3EthernetNetPortPOPMonitorOperRangeHi_Type()
)
f3EthernetNetPortPOPMonitorOperRangeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorOperRangeHi.setStatus("current")
_F3EthernetNetPortPOPMonitorOperRangeLow_Type = Integer32
_F3EthernetNetPortPOPMonitorOperRangeLow_Object = MibTableColumn
f3EthernetNetPortPOPMonitorOperRangeLow = _F3EthernetNetPortPOPMonitorOperRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1, 3),
    _F3EthernetNetPortPOPMonitorOperRangeLow_Type()
)
f3EthernetNetPortPOPMonitorOperRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorOperRangeLow.setStatus("current")
_F3EthernetNetPortPOPMonitorVariance_Type = Integer32
_F3EthernetNetPortPOPMonitorVariance_Object = MibTableColumn
f3EthernetNetPortPOPMonitorVariance = _F3EthernetNetPortPOPMonitorVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1, 4),
    _F3EthernetNetPortPOPMonitorVariance_Type()
)
f3EthernetNetPortPOPMonitorVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorVariance.setStatus("current")


class _F3EthernetNetPortPOPMonitorWindowSize_Type(Integer32):
    """Custom type f3EthernetNetPortPOPMonitorWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_F3EthernetNetPortPOPMonitorWindowSize_Type.__name__ = "Integer32"
_F3EthernetNetPortPOPMonitorWindowSize_Object = MibTableColumn
f3EthernetNetPortPOPMonitorWindowSize = _F3EthernetNetPortPOPMonitorWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1, 5),
    _F3EthernetNetPortPOPMonitorWindowSize_Type()
)
f3EthernetNetPortPOPMonitorWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorWindowSize.setStatus("current")
_F3EthernetNetPortPOPMonitorGlitchRejectionLevel_Type = POPMGlitchRejectionLevel
_F3EthernetNetPortPOPMonitorGlitchRejectionLevel_Object = MibTableColumn
f3EthernetNetPortPOPMonitorGlitchRejectionLevel = _F3EthernetNetPortPOPMonitorGlitchRejectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1, 6),
    _F3EthernetNetPortPOPMonitorGlitchRejectionLevel_Type()
)
f3EthernetNetPortPOPMonitorGlitchRejectionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorGlitchRejectionLevel.setStatus("current")
_F3EthernetNetPortPOPMonitorState_Type = POPMState
_F3EthernetNetPortPOPMonitorState_Object = MibTableColumn
f3EthernetNetPortPOPMonitorState = _F3EthernetNetPortPOPMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1, 7),
    _F3EthernetNetPortPOPMonitorState_Type()
)
f3EthernetNetPortPOPMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorState.setStatus("current")
_F3EthernetNetPortPOPMonitorClearAction_Type = POPMClearAlarmsAction
_F3EthernetNetPortPOPMonitorClearAction_Object = MibTableColumn
f3EthernetNetPortPOPMonitorClearAction = _F3EthernetNetPortPOPMonitorClearAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 1, 1, 8),
    _F3EthernetNetPortPOPMonitorClearAction_Type()
)
f3EthernetNetPortPOPMonitorClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMonitorClearAction.setStatus("current")
_F3EthernetAccPortPOPMonitorTable_Object = MibTable
f3EthernetAccPortPOPMonitorTable = _F3EthernetAccPortPOPMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2)
)
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorTable.setStatus("current")
_F3EthernetAccPortPOPMonitorEntry_Object = MibTableRow
f3EthernetAccPortPOPMonitorEntry = _F3EthernetAccPortPOPMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorEntry.setStatus("current")
_F3EthernetAccPortPOPMonitorEnabled_Type = TruthValue
_F3EthernetAccPortPOPMonitorEnabled_Object = MibTableColumn
f3EthernetAccPortPOPMonitorEnabled = _F3EthernetAccPortPOPMonitorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1, 1),
    _F3EthernetAccPortPOPMonitorEnabled_Type()
)
f3EthernetAccPortPOPMonitorEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorEnabled.setStatus("current")
_F3EthernetAccPortPOPMonitorOperRangeHi_Type = Integer32
_F3EthernetAccPortPOPMonitorOperRangeHi_Object = MibTableColumn
f3EthernetAccPortPOPMonitorOperRangeHi = _F3EthernetAccPortPOPMonitorOperRangeHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1, 2),
    _F3EthernetAccPortPOPMonitorOperRangeHi_Type()
)
f3EthernetAccPortPOPMonitorOperRangeHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorOperRangeHi.setStatus("current")
_F3EthernetAccPortPOPMonitorOperRangeLow_Type = Integer32
_F3EthernetAccPortPOPMonitorOperRangeLow_Object = MibTableColumn
f3EthernetAccPortPOPMonitorOperRangeLow = _F3EthernetAccPortPOPMonitorOperRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1, 3),
    _F3EthernetAccPortPOPMonitorOperRangeLow_Type()
)
f3EthernetAccPortPOPMonitorOperRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorOperRangeLow.setStatus("current")
_F3EthernetAccPortPOPMonitorVariance_Type = Integer32
_F3EthernetAccPortPOPMonitorVariance_Object = MibTableColumn
f3EthernetAccPortPOPMonitorVariance = _F3EthernetAccPortPOPMonitorVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1, 4),
    _F3EthernetAccPortPOPMonitorVariance_Type()
)
f3EthernetAccPortPOPMonitorVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorVariance.setStatus("current")


class _F3EthernetAccPortPOPMonitorWindowSize_Type(Integer32):
    """Custom type f3EthernetAccPortPOPMonitorWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_F3EthernetAccPortPOPMonitorWindowSize_Type.__name__ = "Integer32"
_F3EthernetAccPortPOPMonitorWindowSize_Object = MibTableColumn
f3EthernetAccPortPOPMonitorWindowSize = _F3EthernetAccPortPOPMonitorWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1, 5),
    _F3EthernetAccPortPOPMonitorWindowSize_Type()
)
f3EthernetAccPortPOPMonitorWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorWindowSize.setStatus("current")
_F3EthernetAccPortPOPMonitorGlitchRejectionLevel_Type = POPMGlitchRejectionLevel
_F3EthernetAccPortPOPMonitorGlitchRejectionLevel_Object = MibTableColumn
f3EthernetAccPortPOPMonitorGlitchRejectionLevel = _F3EthernetAccPortPOPMonitorGlitchRejectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1, 6),
    _F3EthernetAccPortPOPMonitorGlitchRejectionLevel_Type()
)
f3EthernetAccPortPOPMonitorGlitchRejectionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorGlitchRejectionLevel.setStatus("current")
_F3EthernetAccPortPOPMonitorState_Type = POPMState
_F3EthernetAccPortPOPMonitorState_Object = MibTableColumn
f3EthernetAccPortPOPMonitorState = _F3EthernetAccPortPOPMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1, 7),
    _F3EthernetAccPortPOPMonitorState_Type()
)
f3EthernetAccPortPOPMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorState.setStatus("current")
_F3EthernetAccPortPOPMonitorClearAction_Type = POPMClearAlarmsAction
_F3EthernetAccPortPOPMonitorClearAction_Object = MibTableColumn
f3EthernetAccPortPOPMonitorClearAction = _F3EthernetAccPortPOPMonitorClearAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 1, 2, 1, 8),
    _F3EthernetAccPortPOPMonitorClearAction_Type()
)
f3EthernetAccPortPOPMonitorClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMonitorClearAction.setStatus("current")
_F3POPMPerfObjects_ObjectIdentity = ObjectIdentity
f3POPMPerfObjects = _F3POPMPerfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2)
)
_F3EthernetAccPortPOPMStatsTable_Object = MibTable
f3EthernetAccPortPOPMStatsTable = _F3EthernetAccPortPOPMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1)
)
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsTable.setStatus("current")
_F3EthernetAccPortPOPMStatsEntry_Object = MibTableRow
f3EthernetAccPortPOPMStatsEntry = _F3EthernetAccPortPOPMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsEntry.setStatus("current")
_F3EthernetAccPortPOPMStatsOPR_Type = Integer32
_F3EthernetAccPortPOPMStatsOPR_Object = MibTableColumn
f3EthernetAccPortPOPMStatsOPR = _F3EthernetAccPortPOPMStatsOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1, 1),
    _F3EthernetAccPortPOPMStatsOPR_Type()
)
f3EthernetAccPortPOPMStatsOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsOPR.setStatus("current")
_F3EthernetAccPortPOPMStatsAOPR_Type = Integer32
_F3EthernetAccPortPOPMStatsAOPR_Object = MibTableColumn
f3EthernetAccPortPOPMStatsAOPR = _F3EthernetAccPortPOPMStatsAOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1, 2),
    _F3EthernetAccPortPOPMStatsAOPR_Type()
)
f3EthernetAccPortPOPMStatsAOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsAOPR.setStatus("current")
_F3EthernetAccPortPOPMStatsOPRVar_Type = Integer32
_F3EthernetAccPortPOPMStatsOPRVar_Object = MibTableColumn
f3EthernetAccPortPOPMStatsOPRVar = _F3EthernetAccPortPOPMStatsOPRVar_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1, 3),
    _F3EthernetAccPortPOPMStatsOPRVar_Type()
)
f3EthernetAccPortPOPMStatsOPRVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsOPRVar.setStatus("current")
_F3EthernetAccPortPOPMStatsOPRMaxVar_Type = Integer32
_F3EthernetAccPortPOPMStatsOPRMaxVar_Object = MibTableColumn
f3EthernetAccPortPOPMStatsOPRMaxVar = _F3EthernetAccPortPOPMStatsOPRMaxVar_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1, 4),
    _F3EthernetAccPortPOPMStatsOPRMaxVar_Type()
)
f3EthernetAccPortPOPMStatsOPRMaxVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsOPRMaxVar.setStatus("current")
_F3EthernetAccPortPOPMStatsOPRGlitchRejects_Type = Unsigned32
_F3EthernetAccPortPOPMStatsOPRGlitchRejects_Object = MibTableColumn
f3EthernetAccPortPOPMStatsOPRGlitchRejects = _F3EthernetAccPortPOPMStatsOPRGlitchRejects_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1, 5),
    _F3EthernetAccPortPOPMStatsOPRGlitchRejects_Type()
)
f3EthernetAccPortPOPMStatsOPRGlitchRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsOPRGlitchRejects.setStatus("current")
_F3EthernetAccPortPOPMStatsOPRRTR_Type = Unsigned32
_F3EthernetAccPortPOPMStatsOPRRTR_Object = MibTableColumn
f3EthernetAccPortPOPMStatsOPRRTR = _F3EthernetAccPortPOPMStatsOPRRTR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1, 6),
    _F3EthernetAccPortPOPMStatsOPRRTR_Type()
)
f3EthernetAccPortPOPMStatsOPRRTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsOPRRTR.setStatus("current")
_F3EthernetAccPortPOPMStatsOPROOR_Type = Unsigned32
_F3EthernetAccPortPOPMStatsOPROOR_Object = MibTableColumn
f3EthernetAccPortPOPMStatsOPROOR = _F3EthernetAccPortPOPMStatsOPROOR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1, 7),
    _F3EthernetAccPortPOPMStatsOPROOR_Type()
)
f3EthernetAccPortPOPMStatsOPROOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsOPROOR.setStatus("current")
_F3EthernetAccPortPOPMStatsOPROOV_Type = Unsigned32
_F3EthernetAccPortPOPMStatsOPROOV_Object = MibTableColumn
f3EthernetAccPortPOPMStatsOPROOV = _F3EthernetAccPortPOPMStatsOPROOV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 1, 1, 8),
    _F3EthernetAccPortPOPMStatsOPROOV_Type()
)
f3EthernetAccPortPOPMStatsOPROOV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMStatsOPROOV.setStatus("current")
_F3EthernetAccPortPOPMHistoryTable_Object = MibTable
f3EthernetAccPortPOPMHistoryTable = _F3EthernetAccPortPOPMHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2)
)
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryTable.setStatus("current")
_F3EthernetAccPortPOPMHistoryEntry_Object = MibTableRow
f3EthernetAccPortPOPMHistoryEntry = _F3EthernetAccPortPOPMHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1)
)
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryEntry.setStatus("current")
_F3EthernetAccPortPOPMHistoryOPR_Type = Integer32
_F3EthernetAccPortPOPMHistoryOPR_Object = MibTableColumn
f3EthernetAccPortPOPMHistoryOPR = _F3EthernetAccPortPOPMHistoryOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1, 1),
    _F3EthernetAccPortPOPMHistoryOPR_Type()
)
f3EthernetAccPortPOPMHistoryOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryOPR.setStatus("current")
_F3EthernetAccPortPOPMHistoryAOPR_Type = Integer32
_F3EthernetAccPortPOPMHistoryAOPR_Object = MibTableColumn
f3EthernetAccPortPOPMHistoryAOPR = _F3EthernetAccPortPOPMHistoryAOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1, 2),
    _F3EthernetAccPortPOPMHistoryAOPR_Type()
)
f3EthernetAccPortPOPMHistoryAOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryAOPR.setStatus("current")
_F3EthernetAccPortPOPMHistoryOPRVar_Type = Integer32
_F3EthernetAccPortPOPMHistoryOPRVar_Object = MibTableColumn
f3EthernetAccPortPOPMHistoryOPRVar = _F3EthernetAccPortPOPMHistoryOPRVar_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1, 3),
    _F3EthernetAccPortPOPMHistoryOPRVar_Type()
)
f3EthernetAccPortPOPMHistoryOPRVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryOPRVar.setStatus("current")
_F3EthernetAccPortPOPMHistoryOPRMaxVar_Type = Integer32
_F3EthernetAccPortPOPMHistoryOPRMaxVar_Object = MibTableColumn
f3EthernetAccPortPOPMHistoryOPRMaxVar = _F3EthernetAccPortPOPMHistoryOPRMaxVar_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1, 4),
    _F3EthernetAccPortPOPMHistoryOPRMaxVar_Type()
)
f3EthernetAccPortPOPMHistoryOPRMaxVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryOPRMaxVar.setStatus("current")
_F3EthernetAccPortPOPMHistoryOPRGlitchRejects_Type = Unsigned32
_F3EthernetAccPortPOPMHistoryOPRGlitchRejects_Object = MibTableColumn
f3EthernetAccPortPOPMHistoryOPRGlitchRejects = _F3EthernetAccPortPOPMHistoryOPRGlitchRejects_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1, 5),
    _F3EthernetAccPortPOPMHistoryOPRGlitchRejects_Type()
)
f3EthernetAccPortPOPMHistoryOPRGlitchRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryOPRGlitchRejects.setStatus("current")
_F3EthernetAccPortPOPMHistoryOPRRTR_Type = Unsigned32
_F3EthernetAccPortPOPMHistoryOPRRTR_Object = MibTableColumn
f3EthernetAccPortPOPMHistoryOPRRTR = _F3EthernetAccPortPOPMHistoryOPRRTR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1, 6),
    _F3EthernetAccPortPOPMHistoryOPRRTR_Type()
)
f3EthernetAccPortPOPMHistoryOPRRTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryOPRRTR.setStatus("current")
_F3EthernetAccPortPOPMHistoryOPROOR_Type = Unsigned32
_F3EthernetAccPortPOPMHistoryOPROOR_Object = MibTableColumn
f3EthernetAccPortPOPMHistoryOPROOR = _F3EthernetAccPortPOPMHistoryOPROOR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1, 7),
    _F3EthernetAccPortPOPMHistoryOPROOR_Type()
)
f3EthernetAccPortPOPMHistoryOPROOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryOPROOR.setStatus("current")
_F3EthernetAccPortPOPMHistoryOPROOV_Type = Unsigned32
_F3EthernetAccPortPOPMHistoryOPROOV_Object = MibTableColumn
f3EthernetAccPortPOPMHistoryOPROOV = _F3EthernetAccPortPOPMHistoryOPROOV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 2, 1, 8),
    _F3EthernetAccPortPOPMHistoryOPROOV_Type()
)
f3EthernetAccPortPOPMHistoryOPROOV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetAccPortPOPMHistoryOPROOV.setStatus("current")
_F3EthernetNetPortPOPMStatsTable_Object = MibTable
f3EthernetNetPortPOPMStatsTable = _F3EthernetNetPortPOPMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3)
)
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsTable.setStatus("current")
_F3EthernetNetPortPOPMStatsEntry_Object = MibTableRow
f3EthernetNetPortPOPMStatsEntry = _F3EthernetNetPortPOPMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1)
)
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsEntry.setStatus("current")
_F3EthernetNetPortPOPMStatsOPR_Type = Integer32
_F3EthernetNetPortPOPMStatsOPR_Object = MibTableColumn
f3EthernetNetPortPOPMStatsOPR = _F3EthernetNetPortPOPMStatsOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1, 1),
    _F3EthernetNetPortPOPMStatsOPR_Type()
)
f3EthernetNetPortPOPMStatsOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsOPR.setStatus("current")
_F3EthernetNetPortPOPMStatsAOPR_Type = Integer32
_F3EthernetNetPortPOPMStatsAOPR_Object = MibTableColumn
f3EthernetNetPortPOPMStatsAOPR = _F3EthernetNetPortPOPMStatsAOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1, 2),
    _F3EthernetNetPortPOPMStatsAOPR_Type()
)
f3EthernetNetPortPOPMStatsAOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsAOPR.setStatus("current")
_F3EthernetNetPortPOPMStatsOPRVar_Type = Integer32
_F3EthernetNetPortPOPMStatsOPRVar_Object = MibTableColumn
f3EthernetNetPortPOPMStatsOPRVar = _F3EthernetNetPortPOPMStatsOPRVar_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1, 3),
    _F3EthernetNetPortPOPMStatsOPRVar_Type()
)
f3EthernetNetPortPOPMStatsOPRVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsOPRVar.setStatus("current")
_F3EthernetNetPortPOPMStatsOPRMaxVar_Type = Integer32
_F3EthernetNetPortPOPMStatsOPRMaxVar_Object = MibTableColumn
f3EthernetNetPortPOPMStatsOPRMaxVar = _F3EthernetNetPortPOPMStatsOPRMaxVar_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1, 4),
    _F3EthernetNetPortPOPMStatsOPRMaxVar_Type()
)
f3EthernetNetPortPOPMStatsOPRMaxVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsOPRMaxVar.setStatus("current")
_F3EthernetNetPortPOPMStatsOPRGlitchRejects_Type = Unsigned32
_F3EthernetNetPortPOPMStatsOPRGlitchRejects_Object = MibTableColumn
f3EthernetNetPortPOPMStatsOPRGlitchRejects = _F3EthernetNetPortPOPMStatsOPRGlitchRejects_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1, 5),
    _F3EthernetNetPortPOPMStatsOPRGlitchRejects_Type()
)
f3EthernetNetPortPOPMStatsOPRGlitchRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsOPRGlitchRejects.setStatus("current")
_F3EthernetNetPortPOPMStatsOPRRTR_Type = Unsigned32
_F3EthernetNetPortPOPMStatsOPRRTR_Object = MibTableColumn
f3EthernetNetPortPOPMStatsOPRRTR = _F3EthernetNetPortPOPMStatsOPRRTR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1, 6),
    _F3EthernetNetPortPOPMStatsOPRRTR_Type()
)
f3EthernetNetPortPOPMStatsOPRRTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsOPRRTR.setStatus("current")
_F3EthernetNetPortPOPMStatsOPROOR_Type = Unsigned32
_F3EthernetNetPortPOPMStatsOPROOR_Object = MibTableColumn
f3EthernetNetPortPOPMStatsOPROOR = _F3EthernetNetPortPOPMStatsOPROOR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1, 7),
    _F3EthernetNetPortPOPMStatsOPROOR_Type()
)
f3EthernetNetPortPOPMStatsOPROOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsOPROOR.setStatus("current")
_F3EthernetNetPortPOPMStatsOPROOV_Type = Unsigned32
_F3EthernetNetPortPOPMStatsOPROOV_Object = MibTableColumn
f3EthernetNetPortPOPMStatsOPROOV = _F3EthernetNetPortPOPMStatsOPROOV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 3, 1, 8),
    _F3EthernetNetPortPOPMStatsOPROOV_Type()
)
f3EthernetNetPortPOPMStatsOPROOV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMStatsOPROOV.setStatus("current")
_F3EthernetNetPortPOPMHistoryTable_Object = MibTable
f3EthernetNetPortPOPMHistoryTable = _F3EthernetNetPortPOPMHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4)
)
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryTable.setStatus("current")
_F3EthernetNetPortPOPMHistoryEntry_Object = MibTableRow
f3EthernetNetPortPOPMHistoryEntry = _F3EthernetNetPortPOPMHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1)
)
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryEntry.setStatus("current")
_F3EthernetNetPortPOPMHistoryOPR_Type = Integer32
_F3EthernetNetPortPOPMHistoryOPR_Object = MibTableColumn
f3EthernetNetPortPOPMHistoryOPR = _F3EthernetNetPortPOPMHistoryOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1, 1),
    _F3EthernetNetPortPOPMHistoryOPR_Type()
)
f3EthernetNetPortPOPMHistoryOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryOPR.setStatus("current")
_F3EthernetNetPortPOPMHistoryAOPR_Type = Integer32
_F3EthernetNetPortPOPMHistoryAOPR_Object = MibTableColumn
f3EthernetNetPortPOPMHistoryAOPR = _F3EthernetNetPortPOPMHistoryAOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1, 2),
    _F3EthernetNetPortPOPMHistoryAOPR_Type()
)
f3EthernetNetPortPOPMHistoryAOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryAOPR.setStatus("current")
_F3EthernetNetPortPOPMHistoryOPRVar_Type = Integer32
_F3EthernetNetPortPOPMHistoryOPRVar_Object = MibTableColumn
f3EthernetNetPortPOPMHistoryOPRVar = _F3EthernetNetPortPOPMHistoryOPRVar_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1, 3),
    _F3EthernetNetPortPOPMHistoryOPRVar_Type()
)
f3EthernetNetPortPOPMHistoryOPRVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryOPRVar.setStatus("current")
_F3EthernetNetPortPOPMHistoryOPRMaxVar_Type = Integer32
_F3EthernetNetPortPOPMHistoryOPRMaxVar_Object = MibTableColumn
f3EthernetNetPortPOPMHistoryOPRMaxVar = _F3EthernetNetPortPOPMHistoryOPRMaxVar_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1, 4),
    _F3EthernetNetPortPOPMHistoryOPRMaxVar_Type()
)
f3EthernetNetPortPOPMHistoryOPRMaxVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryOPRMaxVar.setStatus("current")
_F3EthernetNetPortPOPMHistoryOPRGlitchRejects_Type = Unsigned32
_F3EthernetNetPortPOPMHistoryOPRGlitchRejects_Object = MibTableColumn
f3EthernetNetPortPOPMHistoryOPRGlitchRejects = _F3EthernetNetPortPOPMHistoryOPRGlitchRejects_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1, 5),
    _F3EthernetNetPortPOPMHistoryOPRGlitchRejects_Type()
)
f3EthernetNetPortPOPMHistoryOPRGlitchRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryOPRGlitchRejects.setStatus("current")
_F3EthernetNetPortPOPMHistoryOPRRTR_Type = Unsigned32
_F3EthernetNetPortPOPMHistoryOPRRTR_Object = MibTableColumn
f3EthernetNetPortPOPMHistoryOPRRTR = _F3EthernetNetPortPOPMHistoryOPRRTR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1, 6),
    _F3EthernetNetPortPOPMHistoryOPRRTR_Type()
)
f3EthernetNetPortPOPMHistoryOPRRTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryOPRRTR.setStatus("current")
_F3EthernetNetPortPOPMHistoryOPROOR_Type = Unsigned32
_F3EthernetNetPortPOPMHistoryOPROOR_Object = MibTableColumn
f3EthernetNetPortPOPMHistoryOPROOR = _F3EthernetNetPortPOPMHistoryOPROOR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1, 7),
    _F3EthernetNetPortPOPMHistoryOPROOR_Type()
)
f3EthernetNetPortPOPMHistoryOPROOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryOPROOR.setStatus("current")
_F3EthernetNetPortPOPMHistoryOPROOV_Type = Unsigned32
_F3EthernetNetPortPOPMHistoryOPROOV_Object = MibTableColumn
f3EthernetNetPortPOPMHistoryOPROOV = _F3EthernetNetPortPOPMHistoryOPROOV_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 2, 4, 1, 8),
    _F3EthernetNetPortPOPMHistoryOPROOV_Type()
)
f3EthernetNetPortPOPMHistoryOPROOV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3EthernetNetPortPOPMHistoryOPROOV.setStatus("current")
_F3POPMConformance_ObjectIdentity = ObjectIdentity
f3POPMConformance = _F3POPMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 3)
)
_F3POPMCompliances_ObjectIdentity = ObjectIdentity
f3POPMCompliances = _F3POPMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 3, 1)
)
_F3POPMGroups_ObjectIdentity = ObjectIdentity
f3POPMGroups = _F3POPMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 3, 2)
)
cmEthernetNetPortEntry.registerAugmentions(
    ("F3-POPM-MIB",
     "f3EthernetNetPortPOPMonitorEntry")
)
f3EthernetNetPortPOPMonitorEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
cmEthernetAccPortEntry.registerAugmentions(
    ("F3-POPM-MIB",
     "f3EthernetAccPortPOPMonitorEntry")
)
f3EthernetAccPortPOPMonitorEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())
cmEthernetAccPortStatsEntry.registerAugmentions(
    ("F3-POPM-MIB",
     "f3EthernetAccPortPOPMStatsEntry")
)
f3EthernetAccPortPOPMStatsEntry.setIndexNames(*cmEthernetAccPortStatsEntry.getIndexNames())
cmEthernetAccPortHistoryEntry.registerAugmentions(
    ("F3-POPM-MIB",
     "f3EthernetAccPortPOPMHistoryEntry")
)
f3EthernetAccPortPOPMHistoryEntry.setIndexNames(*cmEthernetAccPortHistoryEntry.getIndexNames())
cmEthernetNetPortStatsEntry.registerAugmentions(
    ("F3-POPM-MIB",
     "f3EthernetNetPortPOPMStatsEntry")
)
f3EthernetNetPortPOPMStatsEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
cmEthernetNetPortHistoryEntry.registerAugmentions(
    ("F3-POPM-MIB",
     "f3EthernetNetPortPOPMHistoryEntry")
)
f3EthernetNetPortPOPMHistoryEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())

# Managed Objects groups

f3POPMFacilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 3, 2, 1)
)
f3POPMFacilityGroup.setObjects(
      *(("F3-POPM-MIB", "f3EthernetAccPortPOPMonitorEnabled"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMonitorOperRangeHi"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMonitorOperRangeLow"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMonitorVariance"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMonitorWindowSize"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMonitorGlitchRejectionLevel"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMonitorState"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMonitorClearAction"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMonitorEnabled"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMonitorOperRangeHi"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMonitorOperRangeLow"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMonitorVariance"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMonitorWindowSize"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMonitorGlitchRejectionLevel"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMonitorState"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMonitorClearAction"))
)
if mibBuilder.loadTexts:
    f3POPMFacilityGroup.setStatus("current")

f3POPMStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 3, 2, 2)
)
f3POPMStatsGroup.setObjects(
      *(("F3-POPM-MIB", "f3EthernetAccPortPOPMStatsOPR"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMStatsAOPR"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMStatsOPRVar"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMStatsOPRMaxVar"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMStatsOPRGlitchRejects"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMStatsOPRRTR"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMStatsOPROOR"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMStatsOPROOV"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMHistoryOPR"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMHistoryAOPR"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMHistoryOPRVar"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMHistoryOPRMaxVar"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMHistoryOPRGlitchRejects"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMHistoryOPRRTR"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMHistoryOPROOR"),
        ("F3-POPM-MIB", "f3EthernetAccPortPOPMHistoryOPROOV"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMStatsOPR"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMStatsAOPR"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMStatsOPRVar"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMStatsOPRMaxVar"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMStatsOPRGlitchRejects"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMStatsOPRRTR"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMStatsOPROOR"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMStatsOPROOV"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMHistoryOPR"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMHistoryAOPR"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMHistoryOPRVar"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMHistoryOPRMaxVar"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMHistoryOPRGlitchRejects"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMHistoryOPRRTR"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMHistoryOPROOR"),
        ("F3-POPM-MIB", "f3EthernetNetPortPOPMHistoryOPROOV"))
)
if mibBuilder.loadTexts:
    f3POPMStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3POPMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 16, 3, 1, 1)
)
f3POPMCompliance.setObjects(
      *(("F3-POPM-MIB", "f3POPMFacilityGroup"),
        ("F3-POPM-MIB", "f3POPMStatsGroup"))
)
if mibBuilder.loadTexts:
    f3POPMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-POPM-MIB",
    **{"POPMGlitchRejectionLevel": POPMGlitchRejectionLevel,
       "POPMState": POPMState,
       "POPMClearAlarmsAction": POPMClearAlarmsAction,
       "f3POPMMib": f3POPMMib,
       "f3POPMObjects": f3POPMObjects,
       "f3EthernetNetPortPOPMonitorTable": f3EthernetNetPortPOPMonitorTable,
       "f3EthernetNetPortPOPMonitorEntry": f3EthernetNetPortPOPMonitorEntry,
       "f3EthernetNetPortPOPMonitorEnabled": f3EthernetNetPortPOPMonitorEnabled,
       "f3EthernetNetPortPOPMonitorOperRangeHi": f3EthernetNetPortPOPMonitorOperRangeHi,
       "f3EthernetNetPortPOPMonitorOperRangeLow": f3EthernetNetPortPOPMonitorOperRangeLow,
       "f3EthernetNetPortPOPMonitorVariance": f3EthernetNetPortPOPMonitorVariance,
       "f3EthernetNetPortPOPMonitorWindowSize": f3EthernetNetPortPOPMonitorWindowSize,
       "f3EthernetNetPortPOPMonitorGlitchRejectionLevel": f3EthernetNetPortPOPMonitorGlitchRejectionLevel,
       "f3EthernetNetPortPOPMonitorState": f3EthernetNetPortPOPMonitorState,
       "f3EthernetNetPortPOPMonitorClearAction": f3EthernetNetPortPOPMonitorClearAction,
       "f3EthernetAccPortPOPMonitorTable": f3EthernetAccPortPOPMonitorTable,
       "f3EthernetAccPortPOPMonitorEntry": f3EthernetAccPortPOPMonitorEntry,
       "f3EthernetAccPortPOPMonitorEnabled": f3EthernetAccPortPOPMonitorEnabled,
       "f3EthernetAccPortPOPMonitorOperRangeHi": f3EthernetAccPortPOPMonitorOperRangeHi,
       "f3EthernetAccPortPOPMonitorOperRangeLow": f3EthernetAccPortPOPMonitorOperRangeLow,
       "f3EthernetAccPortPOPMonitorVariance": f3EthernetAccPortPOPMonitorVariance,
       "f3EthernetAccPortPOPMonitorWindowSize": f3EthernetAccPortPOPMonitorWindowSize,
       "f3EthernetAccPortPOPMonitorGlitchRejectionLevel": f3EthernetAccPortPOPMonitorGlitchRejectionLevel,
       "f3EthernetAccPortPOPMonitorState": f3EthernetAccPortPOPMonitorState,
       "f3EthernetAccPortPOPMonitorClearAction": f3EthernetAccPortPOPMonitorClearAction,
       "f3POPMPerfObjects": f3POPMPerfObjects,
       "f3EthernetAccPortPOPMStatsTable": f3EthernetAccPortPOPMStatsTable,
       "f3EthernetAccPortPOPMStatsEntry": f3EthernetAccPortPOPMStatsEntry,
       "f3EthernetAccPortPOPMStatsOPR": f3EthernetAccPortPOPMStatsOPR,
       "f3EthernetAccPortPOPMStatsAOPR": f3EthernetAccPortPOPMStatsAOPR,
       "f3EthernetAccPortPOPMStatsOPRVar": f3EthernetAccPortPOPMStatsOPRVar,
       "f3EthernetAccPortPOPMStatsOPRMaxVar": f3EthernetAccPortPOPMStatsOPRMaxVar,
       "f3EthernetAccPortPOPMStatsOPRGlitchRejects": f3EthernetAccPortPOPMStatsOPRGlitchRejects,
       "f3EthernetAccPortPOPMStatsOPRRTR": f3EthernetAccPortPOPMStatsOPRRTR,
       "f3EthernetAccPortPOPMStatsOPROOR": f3EthernetAccPortPOPMStatsOPROOR,
       "f3EthernetAccPortPOPMStatsOPROOV": f3EthernetAccPortPOPMStatsOPROOV,
       "f3EthernetAccPortPOPMHistoryTable": f3EthernetAccPortPOPMHistoryTable,
       "f3EthernetAccPortPOPMHistoryEntry": f3EthernetAccPortPOPMHistoryEntry,
       "f3EthernetAccPortPOPMHistoryOPR": f3EthernetAccPortPOPMHistoryOPR,
       "f3EthernetAccPortPOPMHistoryAOPR": f3EthernetAccPortPOPMHistoryAOPR,
       "f3EthernetAccPortPOPMHistoryOPRVar": f3EthernetAccPortPOPMHistoryOPRVar,
       "f3EthernetAccPortPOPMHistoryOPRMaxVar": f3EthernetAccPortPOPMHistoryOPRMaxVar,
       "f3EthernetAccPortPOPMHistoryOPRGlitchRejects": f3EthernetAccPortPOPMHistoryOPRGlitchRejects,
       "f3EthernetAccPortPOPMHistoryOPRRTR": f3EthernetAccPortPOPMHistoryOPRRTR,
       "f3EthernetAccPortPOPMHistoryOPROOR": f3EthernetAccPortPOPMHistoryOPROOR,
       "f3EthernetAccPortPOPMHistoryOPROOV": f3EthernetAccPortPOPMHistoryOPROOV,
       "f3EthernetNetPortPOPMStatsTable": f3EthernetNetPortPOPMStatsTable,
       "f3EthernetNetPortPOPMStatsEntry": f3EthernetNetPortPOPMStatsEntry,
       "f3EthernetNetPortPOPMStatsOPR": f3EthernetNetPortPOPMStatsOPR,
       "f3EthernetNetPortPOPMStatsAOPR": f3EthernetNetPortPOPMStatsAOPR,
       "f3EthernetNetPortPOPMStatsOPRVar": f3EthernetNetPortPOPMStatsOPRVar,
       "f3EthernetNetPortPOPMStatsOPRMaxVar": f3EthernetNetPortPOPMStatsOPRMaxVar,
       "f3EthernetNetPortPOPMStatsOPRGlitchRejects": f3EthernetNetPortPOPMStatsOPRGlitchRejects,
       "f3EthernetNetPortPOPMStatsOPRRTR": f3EthernetNetPortPOPMStatsOPRRTR,
       "f3EthernetNetPortPOPMStatsOPROOR": f3EthernetNetPortPOPMStatsOPROOR,
       "f3EthernetNetPortPOPMStatsOPROOV": f3EthernetNetPortPOPMStatsOPROOV,
       "f3EthernetNetPortPOPMHistoryTable": f3EthernetNetPortPOPMHistoryTable,
       "f3EthernetNetPortPOPMHistoryEntry": f3EthernetNetPortPOPMHistoryEntry,
       "f3EthernetNetPortPOPMHistoryOPR": f3EthernetNetPortPOPMHistoryOPR,
       "f3EthernetNetPortPOPMHistoryAOPR": f3EthernetNetPortPOPMHistoryAOPR,
       "f3EthernetNetPortPOPMHistoryOPRVar": f3EthernetNetPortPOPMHistoryOPRVar,
       "f3EthernetNetPortPOPMHistoryOPRMaxVar": f3EthernetNetPortPOPMHistoryOPRMaxVar,
       "f3EthernetNetPortPOPMHistoryOPRGlitchRejects": f3EthernetNetPortPOPMHistoryOPRGlitchRejects,
       "f3EthernetNetPortPOPMHistoryOPRRTR": f3EthernetNetPortPOPMHistoryOPRRTR,
       "f3EthernetNetPortPOPMHistoryOPROOR": f3EthernetNetPortPOPMHistoryOPROOR,
       "f3EthernetNetPortPOPMHistoryOPROOV": f3EthernetNetPortPOPMHistoryOPROOV,
       "f3POPMConformance": f3POPMConformance,
       "f3POPMCompliances": f3POPMCompliances,
       "f3POPMCompliance": f3POPMCompliance,
       "f3POPMGroups": f3POPMGroups,
       "f3POPMFacilityGroup": f3POPMFacilityGroup,
       "f3POPMStatsGroup": f3POPMStatsGroup}
)
