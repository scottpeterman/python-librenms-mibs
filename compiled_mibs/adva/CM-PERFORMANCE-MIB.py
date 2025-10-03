# SNMP MIB module (CM-PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\CM-PERFORMANCE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:17 2025
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

(CmPmBinAction,
 CmPmIntervalType,
 PerfCounter64) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "CmPmBinAction",
    "CmPmIntervalType",
    "PerfCounter64")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmAccPortQosShaperIndex,
 cmEthernetAccPortIndex,
 cmEthernetNetPortIndex,
 cmEthernetTrafficPortIndex,
 cmFlowEntry,
 cmFlowIndex,
 cmFlowPointIndex,
 cmOAMFlowPointIndex,
 cmQosFlowPolicerIndex,
 cmQosFlowPolicerTypeIndex,
 cmQosPolicerV2Index,
 cmQosShaperIndex,
 cmQosShaperTypeIndex,
 cmQosShaperV2Index,
 cmTrafficPortQosShaperIndex,
 e1t1Index,
 e1t1ParentIfIndex,
 e3t3Index,
 e3t3ParentIfIndex,
 f3AclRuleIndex,
 f3FpQosPolicerIndex,
 f3FpQosShaperIndex,
 f3NetPortQosShaperIndex,
 ocnStmIndex,
 stsVcPathIndex,
 stsVcPathParentIfIndex,
 vtVcPathIndex,
 vtVcPathParentIfIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmAccPortQosShaperIndex",
    "cmEthernetAccPortIndex",
    "cmEthernetNetPortIndex",
    "cmEthernetTrafficPortIndex",
    "cmFlowEntry",
    "cmFlowIndex",
    "cmFlowPointIndex",
    "cmOAMFlowPointIndex",
    "cmQosFlowPolicerIndex",
    "cmQosFlowPolicerTypeIndex",
    "cmQosPolicerV2Index",
    "cmQosShaperIndex",
    "cmQosShaperTypeIndex",
    "cmQosShaperV2Index",
    "cmTrafficPortQosShaperIndex",
    "e1t1Index",
    "e1t1ParentIfIndex",
    "e3t3Index",
    "e3t3ParentIfIndex",
    "f3AclRuleIndex",
    "f3FpQosPolicerIndex",
    "f3FpQosShaperIndex",
    "f3NetPortQosShaperIndex",
    "ocnStmIndex",
    "stsVcPathIndex",
    "stsVcPathParentIfIndex",
    "vtVcPathIndex",
    "vtVcPathParentIfIndex")

(f3LagIndex,) = mibBuilder.importSymbols(
    "F3-LAG-MIB",
    "f3LagIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(dot3adAggIndex,) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

cmPerformanceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5)
)
if mibBuilder.loadTexts:
    cmPerformanceMIB.setRevisions(
        ("2021-01-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmPerfObjects_ObjectIdentity = ObjectIdentity
cmPerfObjects = _CmPerfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1)
)
_CmEthernetAccPortStatsTable_Object = MibTable
cmEthernetAccPortStatsTable = _CmEthernetAccPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1)
)
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsTable.setStatus("current")
_CmEthernetAccPortStatsEntry_Object = MibTableRow
cmEthernetAccPortStatsEntry = _CmEthernetAccPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1)
)
cmEthernetAccPortStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsEntry.setStatus("current")


class _CmEthernetAccPortStatsIndex_Type(Integer32):
    """Custom type cmEthernetAccPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmEthernetAccPortStatsIndex_Type.__name__ = "Integer32"
_CmEthernetAccPortStatsIndex_Object = MibTableColumn
cmEthernetAccPortStatsIndex = _CmEthernetAccPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 1),
    _CmEthernetAccPortStatsIndex_Type()
)
cmEthernetAccPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsIndex.setStatus("current")
_CmEthernetAccPortStatsIntervalType_Type = CmPmIntervalType
_CmEthernetAccPortStatsIntervalType_Object = MibTableColumn
cmEthernetAccPortStatsIntervalType = _CmEthernetAccPortStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 2),
    _CmEthernetAccPortStatsIntervalType_Type()
)
cmEthernetAccPortStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsIntervalType.setStatus("current")
_CmEthernetAccPortStatsValid_Type = TruthValue
_CmEthernetAccPortStatsValid_Object = MibTableColumn
cmEthernetAccPortStatsValid = _CmEthernetAccPortStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 3),
    _CmEthernetAccPortStatsValid_Type()
)
cmEthernetAccPortStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsValid.setStatus("current")
_CmEthernetAccPortStatsAction_Type = CmPmBinAction
_CmEthernetAccPortStatsAction_Object = MibTableColumn
cmEthernetAccPortStatsAction = _CmEthernetAccPortStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 4),
    _CmEthernetAccPortStatsAction_Type()
)
cmEthernetAccPortStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsAction.setStatus("current")
_CmEthernetAccPortStatsESBF_Type = PerfCounter64
_CmEthernetAccPortStatsESBF_Object = MibTableColumn
cmEthernetAccPortStatsESBF = _CmEthernetAccPortStatsESBF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 5),
    _CmEthernetAccPortStatsESBF_Type()
)
cmEthernetAccPortStatsESBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESBF.setStatus("current")
_CmEthernetAccPortStatsESBP_Type = PerfCounter64
_CmEthernetAccPortStatsESBP_Object = MibTableColumn
cmEthernetAccPortStatsESBP = _CmEthernetAccPortStatsESBP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 6),
    _CmEthernetAccPortStatsESBP_Type()
)
cmEthernetAccPortStatsESBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESBP.setStatus("current")
_CmEthernetAccPortStatsESBS_Type = PerfCounter64
_CmEthernetAccPortStatsESBS_Object = MibTableColumn
cmEthernetAccPortStatsESBS = _CmEthernetAccPortStatsESBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 7),
    _CmEthernetAccPortStatsESBS_Type()
)
cmEthernetAccPortStatsESBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESBS.setStatus("current")
_CmEthernetAccPortStatsESC_Type = PerfCounter64
_CmEthernetAccPortStatsESC_Object = MibTableColumn
cmEthernetAccPortStatsESC = _CmEthernetAccPortStatsESC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 8),
    _CmEthernetAccPortStatsESC_Type()
)
cmEthernetAccPortStatsESC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESC.setStatus("current")
_CmEthernetAccPortStatsESCAE_Type = PerfCounter64
_CmEthernetAccPortStatsESCAE_Object = MibTableColumn
cmEthernetAccPortStatsESCAE = _CmEthernetAccPortStatsESCAE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 9),
    _CmEthernetAccPortStatsESCAE_Type()
)
cmEthernetAccPortStatsESCAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESCAE.setStatus("current")
_CmEthernetAccPortStatsESDE_Type = PerfCounter64
_CmEthernetAccPortStatsESDE_Object = MibTableColumn
cmEthernetAccPortStatsESDE = _CmEthernetAccPortStatsESDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 10),
    _CmEthernetAccPortStatsESDE_Type()
)
cmEthernetAccPortStatsESDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESDE.setStatus("current")
_CmEthernetAccPortStatsESF_Type = PerfCounter64
_CmEthernetAccPortStatsESF_Object = MibTableColumn
cmEthernetAccPortStatsESF = _CmEthernetAccPortStatsESF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 11),
    _CmEthernetAccPortStatsESF_Type()
)
cmEthernetAccPortStatsESF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESF.setStatus("current")
_CmEthernetAccPortStatsESFS_Type = PerfCounter64
_CmEthernetAccPortStatsESFS_Object = MibTableColumn
cmEthernetAccPortStatsESFS = _CmEthernetAccPortStatsESFS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 12),
    _CmEthernetAccPortStatsESFS_Type()
)
cmEthernetAccPortStatsESFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESFS.setStatus("current")
_CmEthernetAccPortStatsESJ_Type = PerfCounter64
_CmEthernetAccPortStatsESJ_Object = MibTableColumn
cmEthernetAccPortStatsESJ = _CmEthernetAccPortStatsESJ_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 13),
    _CmEthernetAccPortStatsESJ_Type()
)
cmEthernetAccPortStatsESJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESJ.setStatus("current")
_CmEthernetAccPortStatsESMF_Type = PerfCounter64
_CmEthernetAccPortStatsESMF_Object = MibTableColumn
cmEthernetAccPortStatsESMF = _CmEthernetAccPortStatsESMF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 14),
    _CmEthernetAccPortStatsESMF_Type()
)
cmEthernetAccPortStatsESMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESMF.setStatus("current")
_CmEthernetAccPortStatsESMP_Type = PerfCounter64
_CmEthernetAccPortStatsESMP_Object = MibTableColumn
cmEthernetAccPortStatsESMP = _CmEthernetAccPortStatsESMP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 15),
    _CmEthernetAccPortStatsESMP_Type()
)
cmEthernetAccPortStatsESMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESMP.setStatus("current")
_CmEthernetAccPortStatsESO_Type = PerfCounter64
_CmEthernetAccPortStatsESO_Object = MibTableColumn
cmEthernetAccPortStatsESO = _CmEthernetAccPortStatsESO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 16),
    _CmEthernetAccPortStatsESO_Type()
)
cmEthernetAccPortStatsESO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESO.setStatus("current")
_CmEthernetAccPortStatsESOF_Type = PerfCounter64
_CmEthernetAccPortStatsESOF_Object = MibTableColumn
cmEthernetAccPortStatsESOF = _CmEthernetAccPortStatsESOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 17),
    _CmEthernetAccPortStatsESOF_Type()
)
cmEthernetAccPortStatsESOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESOF.setStatus("current")
_CmEthernetAccPortStatsESOP_Type = PerfCounter64
_CmEthernetAccPortStatsESOP_Object = MibTableColumn
cmEthernetAccPortStatsESOP = _CmEthernetAccPortStatsESOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 18),
    _CmEthernetAccPortStatsESOP_Type()
)
cmEthernetAccPortStatsESOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESOP.setStatus("current")
_CmEthernetAccPortStatsESP_Type = PerfCounter64
_CmEthernetAccPortStatsESP_Object = MibTableColumn
cmEthernetAccPortStatsESP = _CmEthernetAccPortStatsESP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 19),
    _CmEthernetAccPortStatsESP_Type()
)
cmEthernetAccPortStatsESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESP.setStatus("current")
_CmEthernetAccPortStatsESP64_Type = PerfCounter64
_CmEthernetAccPortStatsESP64_Object = MibTableColumn
cmEthernetAccPortStatsESP64 = _CmEthernetAccPortStatsESP64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 20),
    _CmEthernetAccPortStatsESP64_Type()
)
cmEthernetAccPortStatsESP64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESP64.setStatus("current")
_CmEthernetAccPortStatsESP65_Type = PerfCounter64
_CmEthernetAccPortStatsESP65_Object = MibTableColumn
cmEthernetAccPortStatsESP65 = _CmEthernetAccPortStatsESP65_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 21),
    _CmEthernetAccPortStatsESP65_Type()
)
cmEthernetAccPortStatsESP65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESP65.setStatus("current")
_CmEthernetAccPortStatsESP128_Type = PerfCounter64
_CmEthernetAccPortStatsESP128_Object = MibTableColumn
cmEthernetAccPortStatsESP128 = _CmEthernetAccPortStatsESP128_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 22),
    _CmEthernetAccPortStatsESP128_Type()
)
cmEthernetAccPortStatsESP128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESP128.setStatus("current")
_CmEthernetAccPortStatsESP256_Type = PerfCounter64
_CmEthernetAccPortStatsESP256_Object = MibTableColumn
cmEthernetAccPortStatsESP256 = _CmEthernetAccPortStatsESP256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 23),
    _CmEthernetAccPortStatsESP256_Type()
)
cmEthernetAccPortStatsESP256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESP256.setStatus("current")
_CmEthernetAccPortStatsESP512_Type = PerfCounter64
_CmEthernetAccPortStatsESP512_Object = MibTableColumn
cmEthernetAccPortStatsESP512 = _CmEthernetAccPortStatsESP512_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 24),
    _CmEthernetAccPortStatsESP512_Type()
)
cmEthernetAccPortStatsESP512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESP512.setStatus("current")
_CmEthernetAccPortStatsESP1024_Type = PerfCounter64
_CmEthernetAccPortStatsESP1024_Object = MibTableColumn
cmEthernetAccPortStatsESP1024 = _CmEthernetAccPortStatsESP1024_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 25),
    _CmEthernetAccPortStatsESP1024_Type()
)
cmEthernetAccPortStatsESP1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESP1024.setStatus("current")
_CmEthernetAccPortStatsESP1519_Type = PerfCounter64
_CmEthernetAccPortStatsESP1519_Object = MibTableColumn
cmEthernetAccPortStatsESP1519 = _CmEthernetAccPortStatsESP1519_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 26),
    _CmEthernetAccPortStatsESP1519_Type()
)
cmEthernetAccPortStatsESP1519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESP1519.setStatus("current")
_CmEthernetAccPortStatsESUF_Type = PerfCounter64
_CmEthernetAccPortStatsESUF_Object = MibTableColumn
cmEthernetAccPortStatsESUF = _CmEthernetAccPortStatsESUF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 27),
    _CmEthernetAccPortStatsESUF_Type()
)
cmEthernetAccPortStatsESUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESUF.setStatus("current")
_CmEthernetAccPortStatsESUP_Type = PerfCounter64
_CmEthernetAccPortStatsESUP_Object = MibTableColumn
cmEthernetAccPortStatsESUP = _CmEthernetAccPortStatsESUP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 28),
    _CmEthernetAccPortStatsESUP_Type()
)
cmEthernetAccPortStatsESUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsESUP.setStatus("current")
_CmEthernetAccPortStatsL2CPFD_Type = PerfCounter64
_CmEthernetAccPortStatsL2CPFD_Object = MibTableColumn
cmEthernetAccPortStatsL2CPFD = _CmEthernetAccPortStatsL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 29),
    _CmEthernetAccPortStatsL2CPFD_Type()
)
cmEthernetAccPortStatsL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsL2CPFD.setStatus("current")
_CmEthernetAccPortStatsL2CPFP_Type = PerfCounter64
_CmEthernetAccPortStatsL2CPFP_Object = MibTableColumn
cmEthernetAccPortStatsL2CPFP = _CmEthernetAccPortStatsL2CPFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 30),
    _CmEthernetAccPortStatsL2CPFP_Type()
)
cmEthernetAccPortStatsL2CPFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsL2CPFP.setStatus("current")
_CmEthernetAccPortStatsLES_Type = PerfCounter64
_CmEthernetAccPortStatsLES_Object = MibTableColumn
cmEthernetAccPortStatsLES = _CmEthernetAccPortStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 31),
    _CmEthernetAccPortStatsLES_Type()
)
cmEthernetAccPortStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsLES.setStatus("deprecated")
_CmEthernetAccPortStatsLBC_Type = Integer32
_CmEthernetAccPortStatsLBC_Object = MibTableColumn
cmEthernetAccPortStatsLBC = _CmEthernetAccPortStatsLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 32),
    _CmEthernetAccPortStatsLBC_Type()
)
cmEthernetAccPortStatsLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsLBC.setStatus("current")
_CmEthernetAccPortStatsOPT_Type = Integer32
_CmEthernetAccPortStatsOPT_Object = MibTableColumn
cmEthernetAccPortStatsOPT = _CmEthernetAccPortStatsOPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 33),
    _CmEthernetAccPortStatsOPT_Type()
)
cmEthernetAccPortStatsOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsOPT.setStatus("current")
_CmEthernetAccPortStatsOPR_Type = Integer32
_CmEthernetAccPortStatsOPR_Object = MibTableColumn
cmEthernetAccPortStatsOPR = _CmEthernetAccPortStatsOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 34),
    _CmEthernetAccPortStatsOPR_Type()
)
cmEthernetAccPortStatsOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsOPR.setStatus("current")
_CmEthernetAccPortStatsAUFD_Type = PerfCounter64
_CmEthernetAccPortStatsAUFD_Object = MibTableColumn
cmEthernetAccPortStatsAUFD = _CmEthernetAccPortStatsAUFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 35),
    _CmEthernetAccPortStatsAUFD_Type()
)
cmEthernetAccPortStatsAUFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsAUFD.setStatus("current")
_CmEthernetAccPortStatsAPFD_Type = PerfCounter64
_CmEthernetAccPortStatsAPFD_Object = MibTableColumn
cmEthernetAccPortStatsAPFD = _CmEthernetAccPortStatsAPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 36),
    _CmEthernetAccPortStatsAPFD_Type()
)
cmEthernetAccPortStatsAPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsAPFD.setStatus("current")
_CmEthernetAccPortStatsABRRx_Type = PerfCounter64
_CmEthernetAccPortStatsABRRx_Object = MibTableColumn
cmEthernetAccPortStatsABRRx = _CmEthernetAccPortStatsABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 37),
    _CmEthernetAccPortStatsABRRx_Type()
)
cmEthernetAccPortStatsABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsABRRx.setStatus("current")
_CmEthernetAccPortStatsABRTx_Type = PerfCounter64
_CmEthernetAccPortStatsABRTx_Object = MibTableColumn
cmEthernetAccPortStatsABRTx = _CmEthernetAccPortStatsABRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 38),
    _CmEthernetAccPortStatsABRTx_Type()
)
cmEthernetAccPortStatsABRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsABRTx.setStatus("current")
_CmEthernetAccPortStatsTemp_Type = Integer32
_CmEthernetAccPortStatsTemp_Object = MibTableColumn
cmEthernetAccPortStatsTemp = _CmEthernetAccPortStatsTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 39),
    _CmEthernetAccPortStatsTemp_Type()
)
cmEthernetAccPortStatsTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsTemp.setStatus("current")
_CmEthernetAccPortStatsUAS_Type = PerfCounter64
_CmEthernetAccPortStatsUAS_Object = MibTableColumn
cmEthernetAccPortStatsUAS = _CmEthernetAccPortStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 40),
    _CmEthernetAccPortStatsUAS_Type()
)
cmEthernetAccPortStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsUAS.setStatus("current")
_CmEthernetAccPortStatsL2PTRxFramesEncap_Type = PerfCounter64
_CmEthernetAccPortStatsL2PTRxFramesEncap_Object = MibTableColumn
cmEthernetAccPortStatsL2PTRxFramesEncap = _CmEthernetAccPortStatsL2PTRxFramesEncap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 41),
    _CmEthernetAccPortStatsL2PTRxFramesEncap_Type()
)
cmEthernetAccPortStatsL2PTRxFramesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsL2PTRxFramesEncap.setStatus("current")
_CmEthernetAccPortStatsL2PTTxFramesDecap_Type = PerfCounter64
_CmEthernetAccPortStatsL2PTTxFramesDecap_Object = MibTableColumn
cmEthernetAccPortStatsL2PTTxFramesDecap = _CmEthernetAccPortStatsL2PTTxFramesDecap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 42),
    _CmEthernetAccPortStatsL2PTTxFramesDecap_Type()
)
cmEthernetAccPortStatsL2PTTxFramesDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsL2PTTxFramesDecap.setStatus("current")
_CmEthernetAccPortStatsIBRMaxRx_Type = PerfCounter64
_CmEthernetAccPortStatsIBRMaxRx_Object = MibTableColumn
cmEthernetAccPortStatsIBRMaxRx = _CmEthernetAccPortStatsIBRMaxRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 43),
    _CmEthernetAccPortStatsIBRMaxRx_Type()
)
cmEthernetAccPortStatsIBRMaxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsIBRMaxRx.setStatus("current")
_CmEthernetAccPortStatsIBRMaxTx_Type = PerfCounter64
_CmEthernetAccPortStatsIBRMaxTx_Object = MibTableColumn
cmEthernetAccPortStatsIBRMaxTx = _CmEthernetAccPortStatsIBRMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 44),
    _CmEthernetAccPortStatsIBRMaxTx_Type()
)
cmEthernetAccPortStatsIBRMaxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsIBRMaxTx.setStatus("current")
_CmEthernetAccPortStatsIBRMinRx_Type = PerfCounter64
_CmEthernetAccPortStatsIBRMinRx_Object = MibTableColumn
cmEthernetAccPortStatsIBRMinRx = _CmEthernetAccPortStatsIBRMinRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 45),
    _CmEthernetAccPortStatsIBRMinRx_Type()
)
cmEthernetAccPortStatsIBRMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsIBRMinRx.setStatus("current")
_CmEthernetAccPortStatsIBRMinTx_Type = PerfCounter64
_CmEthernetAccPortStatsIBRMinTx_Object = MibTableColumn
cmEthernetAccPortStatsIBRMinTx = _CmEthernetAccPortStatsIBRMinTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 46),
    _CmEthernetAccPortStatsIBRMinTx_Type()
)
cmEthernetAccPortStatsIBRMinTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsIBRMinTx.setStatus("current")
_CmEthernetAccPortStatsIBRRx_Type = PerfCounter64
_CmEthernetAccPortStatsIBRRx_Object = MibTableColumn
cmEthernetAccPortStatsIBRRx = _CmEthernetAccPortStatsIBRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 47),
    _CmEthernetAccPortStatsIBRRx_Type()
)
cmEthernetAccPortStatsIBRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsIBRRx.setStatus("current")
_CmEthernetAccPortStatsIBRTx_Type = PerfCounter64
_CmEthernetAccPortStatsIBRTx_Object = MibTableColumn
cmEthernetAccPortStatsIBRTx = _CmEthernetAccPortStatsIBRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 48),
    _CmEthernetAccPortStatsIBRTx_Type()
)
cmEthernetAccPortStatsIBRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsIBRTx.setStatus("current")
_CmEthernetAccPortStatsFmcd_Type = PerfCounter64
_CmEthernetAccPortStatsFmcd_Object = MibTableColumn
cmEthernetAccPortStatsFmcd = _CmEthernetAccPortStatsFmcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 49),
    _CmEthernetAccPortStatsFmcd_Type()
)
cmEthernetAccPortStatsFmcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsFmcd.setStatus("current")
_CmEthernetAccPortStatsFbcd_Type = PerfCounter64
_CmEthernetAccPortStatsFbcd_Object = MibTableColumn
cmEthernetAccPortStatsFbcd = _CmEthernetAccPortStatsFbcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 50),
    _CmEthernetAccPortStatsFbcd_Type()
)
cmEthernetAccPortStatsFbcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsFbcd.setStatus("current")
_CmEthernetAccPortStatsAclDropNoMatch_Type = PerfCounter64
_CmEthernetAccPortStatsAclDropNoMatch_Object = MibTableColumn
cmEthernetAccPortStatsAclDropNoMatch = _CmEthernetAccPortStatsAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 51),
    _CmEthernetAccPortStatsAclDropNoMatch_Type()
)
cmEthernetAccPortStatsAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsAclDropNoMatch.setStatus("current")
_CmEthernetAccPortStatsAclFwd2Cpu_Type = PerfCounter64
_CmEthernetAccPortStatsAclFwd2Cpu_Object = MibTableColumn
cmEthernetAccPortStatsAclFwd2Cpu = _CmEthernetAccPortStatsAclFwd2Cpu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 52),
    _CmEthernetAccPortStatsAclFwd2Cpu_Type()
)
cmEthernetAccPortStatsAclFwd2Cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsAclFwd2Cpu.setStatus("current")
_CmEthernetAccPortStatsDhcpDropNoAssocIf_Type = PerfCounter64
_CmEthernetAccPortStatsDhcpDropNoAssocIf_Object = MibTableColumn
cmEthernetAccPortStatsDhcpDropNoAssocIf = _CmEthernetAccPortStatsDhcpDropNoAssocIf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 53),
    _CmEthernetAccPortStatsDhcpDropNoAssocIf_Type()
)
cmEthernetAccPortStatsDhcpDropNoAssocIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsDhcpDropNoAssocIf.setStatus("current")
_CmEthernetAccPortStatsLkupFails_Type = PerfCounter64
_CmEthernetAccPortStatsLkupFails_Object = MibTableColumn
cmEthernetAccPortStatsLkupFails = _CmEthernetAccPortStatsLkupFails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 1, 1, 54),
    _CmEthernetAccPortStatsLkupFails_Type()
)
cmEthernetAccPortStatsLkupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortStatsLkupFails.setStatus("current")
_CmEthernetAccPortHistoryTable_Object = MibTable
cmEthernetAccPortHistoryTable = _CmEthernetAccPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2)
)
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryTable.setStatus("current")
_CmEthernetAccPortHistoryEntry_Object = MibTableRow
cmEthernetAccPortHistoryEntry = _CmEthernetAccPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1)
)
cmEthernetAccPortHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryEntry.setStatus("current")


class _CmEthernetAccPortHistoryIndex_Type(Integer32):
    """Custom type cmEthernetAccPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CmEthernetAccPortHistoryIndex_Type.__name__ = "Integer32"
_CmEthernetAccPortHistoryIndex_Object = MibTableColumn
cmEthernetAccPortHistoryIndex = _CmEthernetAccPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 1),
    _CmEthernetAccPortHistoryIndex_Type()
)
cmEthernetAccPortHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryIndex.setStatus("current")
_CmEthernetAccPortHistoryTime_Type = DateAndTime
_CmEthernetAccPortHistoryTime_Object = MibTableColumn
cmEthernetAccPortHistoryTime = _CmEthernetAccPortHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 2),
    _CmEthernetAccPortHistoryTime_Type()
)
cmEthernetAccPortHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryTime.setStatus("current")
_CmEthernetAccPortHistoryValid_Type = TruthValue
_CmEthernetAccPortHistoryValid_Object = MibTableColumn
cmEthernetAccPortHistoryValid = _CmEthernetAccPortHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 3),
    _CmEthernetAccPortHistoryValid_Type()
)
cmEthernetAccPortHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryValid.setStatus("current")
_CmEthernetAccPortHistoryAction_Type = CmPmBinAction
_CmEthernetAccPortHistoryAction_Object = MibTableColumn
cmEthernetAccPortHistoryAction = _CmEthernetAccPortHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 4),
    _CmEthernetAccPortHistoryAction_Type()
)
cmEthernetAccPortHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryAction.setStatus("current")
_CmEthernetAccPortHistoryESBF_Type = PerfCounter64
_CmEthernetAccPortHistoryESBF_Object = MibTableColumn
cmEthernetAccPortHistoryESBF = _CmEthernetAccPortHistoryESBF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 5),
    _CmEthernetAccPortHistoryESBF_Type()
)
cmEthernetAccPortHistoryESBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESBF.setStatus("current")
_CmEthernetAccPortHistoryESBP_Type = PerfCounter64
_CmEthernetAccPortHistoryESBP_Object = MibTableColumn
cmEthernetAccPortHistoryESBP = _CmEthernetAccPortHistoryESBP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 6),
    _CmEthernetAccPortHistoryESBP_Type()
)
cmEthernetAccPortHistoryESBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESBP.setStatus("current")
_CmEthernetAccPortHistoryESBS_Type = PerfCounter64
_CmEthernetAccPortHistoryESBS_Object = MibTableColumn
cmEthernetAccPortHistoryESBS = _CmEthernetAccPortHistoryESBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 7),
    _CmEthernetAccPortHistoryESBS_Type()
)
cmEthernetAccPortHistoryESBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESBS.setStatus("current")
_CmEthernetAccPortHistoryESC_Type = PerfCounter64
_CmEthernetAccPortHistoryESC_Object = MibTableColumn
cmEthernetAccPortHistoryESC = _CmEthernetAccPortHistoryESC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 8),
    _CmEthernetAccPortHistoryESC_Type()
)
cmEthernetAccPortHistoryESC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESC.setStatus("current")
_CmEthernetAccPortHistoryESCAE_Type = PerfCounter64
_CmEthernetAccPortHistoryESCAE_Object = MibTableColumn
cmEthernetAccPortHistoryESCAE = _CmEthernetAccPortHistoryESCAE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 9),
    _CmEthernetAccPortHistoryESCAE_Type()
)
cmEthernetAccPortHistoryESCAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESCAE.setStatus("current")
_CmEthernetAccPortHistoryESDE_Type = PerfCounter64
_CmEthernetAccPortHistoryESDE_Object = MibTableColumn
cmEthernetAccPortHistoryESDE = _CmEthernetAccPortHistoryESDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 10),
    _CmEthernetAccPortHistoryESDE_Type()
)
cmEthernetAccPortHistoryESDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESDE.setStatus("current")
_CmEthernetAccPortHistoryESF_Type = PerfCounter64
_CmEthernetAccPortHistoryESF_Object = MibTableColumn
cmEthernetAccPortHistoryESF = _CmEthernetAccPortHistoryESF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 11),
    _CmEthernetAccPortHistoryESF_Type()
)
cmEthernetAccPortHistoryESF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESF.setStatus("current")
_CmEthernetAccPortHistoryESFS_Type = PerfCounter64
_CmEthernetAccPortHistoryESFS_Object = MibTableColumn
cmEthernetAccPortHistoryESFS = _CmEthernetAccPortHistoryESFS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 12),
    _CmEthernetAccPortHistoryESFS_Type()
)
cmEthernetAccPortHistoryESFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESFS.setStatus("current")
_CmEthernetAccPortHistoryESJ_Type = PerfCounter64
_CmEthernetAccPortHistoryESJ_Object = MibTableColumn
cmEthernetAccPortHistoryESJ = _CmEthernetAccPortHistoryESJ_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 13),
    _CmEthernetAccPortHistoryESJ_Type()
)
cmEthernetAccPortHistoryESJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESJ.setStatus("current")
_CmEthernetAccPortHistoryESMF_Type = PerfCounter64
_CmEthernetAccPortHistoryESMF_Object = MibTableColumn
cmEthernetAccPortHistoryESMF = _CmEthernetAccPortHistoryESMF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 14),
    _CmEthernetAccPortHistoryESMF_Type()
)
cmEthernetAccPortHistoryESMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESMF.setStatus("current")
_CmEthernetAccPortHistoryESMP_Type = PerfCounter64
_CmEthernetAccPortHistoryESMP_Object = MibTableColumn
cmEthernetAccPortHistoryESMP = _CmEthernetAccPortHistoryESMP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 15),
    _CmEthernetAccPortHistoryESMP_Type()
)
cmEthernetAccPortHistoryESMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESMP.setStatus("current")
_CmEthernetAccPortHistoryESO_Type = PerfCounter64
_CmEthernetAccPortHistoryESO_Object = MibTableColumn
cmEthernetAccPortHistoryESO = _CmEthernetAccPortHistoryESO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 16),
    _CmEthernetAccPortHistoryESO_Type()
)
cmEthernetAccPortHistoryESO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESO.setStatus("current")
_CmEthernetAccPortHistoryESOF_Type = PerfCounter64
_CmEthernetAccPortHistoryESOF_Object = MibTableColumn
cmEthernetAccPortHistoryESOF = _CmEthernetAccPortHistoryESOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 17),
    _CmEthernetAccPortHistoryESOF_Type()
)
cmEthernetAccPortHistoryESOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESOF.setStatus("current")
_CmEthernetAccPortHistoryESOP_Type = PerfCounter64
_CmEthernetAccPortHistoryESOP_Object = MibTableColumn
cmEthernetAccPortHistoryESOP = _CmEthernetAccPortHistoryESOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 18),
    _CmEthernetAccPortHistoryESOP_Type()
)
cmEthernetAccPortHistoryESOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESOP.setStatus("current")
_CmEthernetAccPortHistoryESP_Type = PerfCounter64
_CmEthernetAccPortHistoryESP_Object = MibTableColumn
cmEthernetAccPortHistoryESP = _CmEthernetAccPortHistoryESP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 19),
    _CmEthernetAccPortHistoryESP_Type()
)
cmEthernetAccPortHistoryESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESP.setStatus("current")
_CmEthernetAccPortHistoryESP64_Type = PerfCounter64
_CmEthernetAccPortHistoryESP64_Object = MibTableColumn
cmEthernetAccPortHistoryESP64 = _CmEthernetAccPortHistoryESP64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 20),
    _CmEthernetAccPortHistoryESP64_Type()
)
cmEthernetAccPortHistoryESP64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESP64.setStatus("current")
_CmEthernetAccPortHistoryESP65_Type = PerfCounter64
_CmEthernetAccPortHistoryESP65_Object = MibTableColumn
cmEthernetAccPortHistoryESP65 = _CmEthernetAccPortHistoryESP65_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 21),
    _CmEthernetAccPortHistoryESP65_Type()
)
cmEthernetAccPortHistoryESP65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESP65.setStatus("current")
_CmEthernetAccPortHistoryESP128_Type = PerfCounter64
_CmEthernetAccPortHistoryESP128_Object = MibTableColumn
cmEthernetAccPortHistoryESP128 = _CmEthernetAccPortHistoryESP128_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 22),
    _CmEthernetAccPortHistoryESP128_Type()
)
cmEthernetAccPortHistoryESP128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESP128.setStatus("current")
_CmEthernetAccPortHistoryESP256_Type = PerfCounter64
_CmEthernetAccPortHistoryESP256_Object = MibTableColumn
cmEthernetAccPortHistoryESP256 = _CmEthernetAccPortHistoryESP256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 23),
    _CmEthernetAccPortHistoryESP256_Type()
)
cmEthernetAccPortHistoryESP256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESP256.setStatus("current")
_CmEthernetAccPortHistoryESP512_Type = PerfCounter64
_CmEthernetAccPortHistoryESP512_Object = MibTableColumn
cmEthernetAccPortHistoryESP512 = _CmEthernetAccPortHistoryESP512_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 24),
    _CmEthernetAccPortHistoryESP512_Type()
)
cmEthernetAccPortHistoryESP512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESP512.setStatus("current")
_CmEthernetAccPortHistoryESP1024_Type = PerfCounter64
_CmEthernetAccPortHistoryESP1024_Object = MibTableColumn
cmEthernetAccPortHistoryESP1024 = _CmEthernetAccPortHistoryESP1024_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 25),
    _CmEthernetAccPortHistoryESP1024_Type()
)
cmEthernetAccPortHistoryESP1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESP1024.setStatus("current")
_CmEthernetAccPortHistoryESP1519_Type = PerfCounter64
_CmEthernetAccPortHistoryESP1519_Object = MibTableColumn
cmEthernetAccPortHistoryESP1519 = _CmEthernetAccPortHistoryESP1519_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 26),
    _CmEthernetAccPortHistoryESP1519_Type()
)
cmEthernetAccPortHistoryESP1519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESP1519.setStatus("current")
_CmEthernetAccPortHistoryESUF_Type = PerfCounter64
_CmEthernetAccPortHistoryESUF_Object = MibTableColumn
cmEthernetAccPortHistoryESUF = _CmEthernetAccPortHistoryESUF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 27),
    _CmEthernetAccPortHistoryESUF_Type()
)
cmEthernetAccPortHistoryESUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESUF.setStatus("current")
_CmEthernetAccPortHistoryESUP_Type = PerfCounter64
_CmEthernetAccPortHistoryESUP_Object = MibTableColumn
cmEthernetAccPortHistoryESUP = _CmEthernetAccPortHistoryESUP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 28),
    _CmEthernetAccPortHistoryESUP_Type()
)
cmEthernetAccPortHistoryESUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryESUP.setStatus("current")
_CmEthernetAccPortHistoryL2CPFD_Type = PerfCounter64
_CmEthernetAccPortHistoryL2CPFD_Object = MibTableColumn
cmEthernetAccPortHistoryL2CPFD = _CmEthernetAccPortHistoryL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 29),
    _CmEthernetAccPortHistoryL2CPFD_Type()
)
cmEthernetAccPortHistoryL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryL2CPFD.setStatus("current")
_CmEthernetAccPortHistoryL2CPFP_Type = PerfCounter64
_CmEthernetAccPortHistoryL2CPFP_Object = MibTableColumn
cmEthernetAccPortHistoryL2CPFP = _CmEthernetAccPortHistoryL2CPFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 30),
    _CmEthernetAccPortHistoryL2CPFP_Type()
)
cmEthernetAccPortHistoryL2CPFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryL2CPFP.setStatus("current")
_CmEthernetAccPortHistoryLES_Type = PerfCounter64
_CmEthernetAccPortHistoryLES_Object = MibTableColumn
cmEthernetAccPortHistoryLES = _CmEthernetAccPortHistoryLES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 31),
    _CmEthernetAccPortHistoryLES_Type()
)
cmEthernetAccPortHistoryLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryLES.setStatus("deprecated")
_CmEthernetAccPortHistoryLBC_Type = Integer32
_CmEthernetAccPortHistoryLBC_Object = MibTableColumn
cmEthernetAccPortHistoryLBC = _CmEthernetAccPortHistoryLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 32),
    _CmEthernetAccPortHistoryLBC_Type()
)
cmEthernetAccPortHistoryLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryLBC.setStatus("current")
_CmEthernetAccPortHistoryOPT_Type = Integer32
_CmEthernetAccPortHistoryOPT_Object = MibTableColumn
cmEthernetAccPortHistoryOPT = _CmEthernetAccPortHistoryOPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 33),
    _CmEthernetAccPortHistoryOPT_Type()
)
cmEthernetAccPortHistoryOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryOPT.setStatus("current")
_CmEthernetAccPortHistoryOPR_Type = Integer32
_CmEthernetAccPortHistoryOPR_Object = MibTableColumn
cmEthernetAccPortHistoryOPR = _CmEthernetAccPortHistoryOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 34),
    _CmEthernetAccPortHistoryOPR_Type()
)
cmEthernetAccPortHistoryOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryOPR.setStatus("current")
_CmEthernetAccPortHistoryAUFD_Type = PerfCounter64
_CmEthernetAccPortHistoryAUFD_Object = MibTableColumn
cmEthernetAccPortHistoryAUFD = _CmEthernetAccPortHistoryAUFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 35),
    _CmEthernetAccPortHistoryAUFD_Type()
)
cmEthernetAccPortHistoryAUFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryAUFD.setStatus("current")
_CmEthernetAccPortHistoryAPFD_Type = PerfCounter64
_CmEthernetAccPortHistoryAPFD_Object = MibTableColumn
cmEthernetAccPortHistoryAPFD = _CmEthernetAccPortHistoryAPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 36),
    _CmEthernetAccPortHistoryAPFD_Type()
)
cmEthernetAccPortHistoryAPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryAPFD.setStatus("current")
_CmEthernetAccPortHistoryABRRx_Type = PerfCounter64
_CmEthernetAccPortHistoryABRRx_Object = MibTableColumn
cmEthernetAccPortHistoryABRRx = _CmEthernetAccPortHistoryABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 37),
    _CmEthernetAccPortHistoryABRRx_Type()
)
cmEthernetAccPortHistoryABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryABRRx.setStatus("current")
_CmEthernetAccPortHistoryABRTx_Type = PerfCounter64
_CmEthernetAccPortHistoryABRTx_Object = MibTableColumn
cmEthernetAccPortHistoryABRTx = _CmEthernetAccPortHistoryABRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 38),
    _CmEthernetAccPortHistoryABRTx_Type()
)
cmEthernetAccPortHistoryABRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryABRTx.setStatus("current")
_CmEthernetAccPortHistoryTemp_Type = Integer32
_CmEthernetAccPortHistoryTemp_Object = MibTableColumn
cmEthernetAccPortHistoryTemp = _CmEthernetAccPortHistoryTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 39),
    _CmEthernetAccPortHistoryTemp_Type()
)
cmEthernetAccPortHistoryTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryTemp.setStatus("current")
_CmEthernetAccPortHistoryUAS_Type = PerfCounter64
_CmEthernetAccPortHistoryUAS_Object = MibTableColumn
cmEthernetAccPortHistoryUAS = _CmEthernetAccPortHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 40),
    _CmEthernetAccPortHistoryUAS_Type()
)
cmEthernetAccPortHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryUAS.setStatus("current")
_CmEthernetAccPortHistoryL2PTRxFramesEncap_Type = PerfCounter64
_CmEthernetAccPortHistoryL2PTRxFramesEncap_Object = MibTableColumn
cmEthernetAccPortHistoryL2PTRxFramesEncap = _CmEthernetAccPortHistoryL2PTRxFramesEncap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 41),
    _CmEthernetAccPortHistoryL2PTRxFramesEncap_Type()
)
cmEthernetAccPortHistoryL2PTRxFramesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryL2PTRxFramesEncap.setStatus("current")
_CmEthernetAccPortHistoryL2PTTxFramesDecap_Type = PerfCounter64
_CmEthernetAccPortHistoryL2PTTxFramesDecap_Object = MibTableColumn
cmEthernetAccPortHistoryL2PTTxFramesDecap = _CmEthernetAccPortHistoryL2PTTxFramesDecap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 42),
    _CmEthernetAccPortHistoryL2PTTxFramesDecap_Type()
)
cmEthernetAccPortHistoryL2PTTxFramesDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryL2PTTxFramesDecap.setStatus("current")
_CmEthernetAccPortHistoryIBRMaxRx_Type = PerfCounter64
_CmEthernetAccPortHistoryIBRMaxRx_Object = MibTableColumn
cmEthernetAccPortHistoryIBRMaxRx = _CmEthernetAccPortHistoryIBRMaxRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 43),
    _CmEthernetAccPortHistoryIBRMaxRx_Type()
)
cmEthernetAccPortHistoryIBRMaxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryIBRMaxRx.setStatus("current")
_CmEthernetAccPortHistoryIBRMaxTx_Type = PerfCounter64
_CmEthernetAccPortHistoryIBRMaxTx_Object = MibTableColumn
cmEthernetAccPortHistoryIBRMaxTx = _CmEthernetAccPortHistoryIBRMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 44),
    _CmEthernetAccPortHistoryIBRMaxTx_Type()
)
cmEthernetAccPortHistoryIBRMaxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryIBRMaxTx.setStatus("current")
_CmEthernetAccPortHistoryIBRMinRx_Type = PerfCounter64
_CmEthernetAccPortHistoryIBRMinRx_Object = MibTableColumn
cmEthernetAccPortHistoryIBRMinRx = _CmEthernetAccPortHistoryIBRMinRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 45),
    _CmEthernetAccPortHistoryIBRMinRx_Type()
)
cmEthernetAccPortHistoryIBRMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryIBRMinRx.setStatus("current")
_CmEthernetAccPortHistoryIBRMinTx_Type = PerfCounter64
_CmEthernetAccPortHistoryIBRMinTx_Object = MibTableColumn
cmEthernetAccPortHistoryIBRMinTx = _CmEthernetAccPortHistoryIBRMinTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 46),
    _CmEthernetAccPortHistoryIBRMinTx_Type()
)
cmEthernetAccPortHistoryIBRMinTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryIBRMinTx.setStatus("current")
_CmEthernetAccPortHistoryIBRRx_Type = PerfCounter64
_CmEthernetAccPortHistoryIBRRx_Object = MibTableColumn
cmEthernetAccPortHistoryIBRRx = _CmEthernetAccPortHistoryIBRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 47),
    _CmEthernetAccPortHistoryIBRRx_Type()
)
cmEthernetAccPortHistoryIBRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryIBRRx.setStatus("current")
_CmEthernetAccPortHistoryIBRTx_Type = PerfCounter64
_CmEthernetAccPortHistoryIBRTx_Object = MibTableColumn
cmEthernetAccPortHistoryIBRTx = _CmEthernetAccPortHistoryIBRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 48),
    _CmEthernetAccPortHistoryIBRTx_Type()
)
cmEthernetAccPortHistoryIBRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryIBRTx.setStatus("current")
_CmEthernetAccPortHistoryFmcd_Type = PerfCounter64
_CmEthernetAccPortHistoryFmcd_Object = MibTableColumn
cmEthernetAccPortHistoryFmcd = _CmEthernetAccPortHistoryFmcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 49),
    _CmEthernetAccPortHistoryFmcd_Type()
)
cmEthernetAccPortHistoryFmcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryFmcd.setStatus("current")
_CmEthernetAccPortHistoryFbcd_Type = PerfCounter64
_CmEthernetAccPortHistoryFbcd_Object = MibTableColumn
cmEthernetAccPortHistoryFbcd = _CmEthernetAccPortHistoryFbcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 50),
    _CmEthernetAccPortHistoryFbcd_Type()
)
cmEthernetAccPortHistoryFbcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryFbcd.setStatus("current")
_CmEthernetAccPortHistoryAclDropNoMatch_Type = PerfCounter64
_CmEthernetAccPortHistoryAclDropNoMatch_Object = MibTableColumn
cmEthernetAccPortHistoryAclDropNoMatch = _CmEthernetAccPortHistoryAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 51),
    _CmEthernetAccPortHistoryAclDropNoMatch_Type()
)
cmEthernetAccPortHistoryAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryAclDropNoMatch.setStatus("current")
_CmEthernetAccPortHistoryAclFwd2Cpu_Type = PerfCounter64
_CmEthernetAccPortHistoryAclFwd2Cpu_Object = MibTableColumn
cmEthernetAccPortHistoryAclFwd2Cpu = _CmEthernetAccPortHistoryAclFwd2Cpu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 52),
    _CmEthernetAccPortHistoryAclFwd2Cpu_Type()
)
cmEthernetAccPortHistoryAclFwd2Cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryAclFwd2Cpu.setStatus("current")
_CmEthernetAccPortHistoryDhcpDropNoAssocIf_Type = PerfCounter64
_CmEthernetAccPortHistoryDhcpDropNoAssocIf_Object = MibTableColumn
cmEthernetAccPortHistoryDhcpDropNoAssocIf = _CmEthernetAccPortHistoryDhcpDropNoAssocIf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 53),
    _CmEthernetAccPortHistoryDhcpDropNoAssocIf_Type()
)
cmEthernetAccPortHistoryDhcpDropNoAssocIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryDhcpDropNoAssocIf.setStatus("current")
_CmEthernetAccPortHistoryLkupFails_Type = PerfCounter64
_CmEthernetAccPortHistoryLkupFails_Object = MibTableColumn
cmEthernetAccPortHistoryLkupFails = _CmEthernetAccPortHistoryLkupFails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 2, 1, 54),
    _CmEthernetAccPortHistoryLkupFails_Type()
)
cmEthernetAccPortHistoryLkupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortHistoryLkupFails.setStatus("current")
_CmEthernetAccPortThresholdTable_Object = MibTable
cmEthernetAccPortThresholdTable = _CmEthernetAccPortThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 3)
)
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdTable.setStatus("current")
_CmEthernetAccPortThresholdEntry_Object = MibTableRow
cmEthernetAccPortThresholdEntry = _CmEthernetAccPortThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 3, 1)
)
cmEthernetAccPortThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdEntry.setStatus("current")


class _CmEthernetAccPortThresholdIndex_Type(Integer32):
    """Custom type cmEthernetAccPortThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmEthernetAccPortThresholdIndex_Type.__name__ = "Integer32"
_CmEthernetAccPortThresholdIndex_Object = MibTableColumn
cmEthernetAccPortThresholdIndex = _CmEthernetAccPortThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 3, 1, 1),
    _CmEthernetAccPortThresholdIndex_Type()
)
cmEthernetAccPortThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdIndex.setStatus("current")
_CmEthernetAccPortThresholdInterval_Type = CmPmIntervalType
_CmEthernetAccPortThresholdInterval_Object = MibTableColumn
cmEthernetAccPortThresholdInterval = _CmEthernetAccPortThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 3, 1, 2),
    _CmEthernetAccPortThresholdInterval_Type()
)
cmEthernetAccPortThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdInterval.setStatus("current")
_CmEthernetAccPortThresholdVariable_Type = VariablePointer
_CmEthernetAccPortThresholdVariable_Object = MibTableColumn
cmEthernetAccPortThresholdVariable = _CmEthernetAccPortThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 3, 1, 3),
    _CmEthernetAccPortThresholdVariable_Type()
)
cmEthernetAccPortThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdVariable.setStatus("current")
_CmEthernetAccPortThresholdValueLo_Type = Unsigned32
_CmEthernetAccPortThresholdValueLo_Object = MibTableColumn
cmEthernetAccPortThresholdValueLo = _CmEthernetAccPortThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 3, 1, 4),
    _CmEthernetAccPortThresholdValueLo_Type()
)
cmEthernetAccPortThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdValueLo.setStatus("current")
_CmEthernetAccPortThresholdValueHi_Type = Unsigned32
_CmEthernetAccPortThresholdValueHi_Object = MibTableColumn
cmEthernetAccPortThresholdValueHi = _CmEthernetAccPortThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 3, 1, 5),
    _CmEthernetAccPortThresholdValueHi_Type()
)
cmEthernetAccPortThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdValueHi.setStatus("current")
_CmEthernetAccPortThresholdMonValue_Type = Counter64
_CmEthernetAccPortThresholdMonValue_Object = MibTableColumn
cmEthernetAccPortThresholdMonValue = _CmEthernetAccPortThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 3, 1, 6),
    _CmEthernetAccPortThresholdMonValue_Type()
)
cmEthernetAccPortThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdMonValue.setStatus("current")
_CmEthernetAccPortThresholdVarTable_Object = MibTable
cmEthernetAccPortThresholdVarTable = _CmEthernetAccPortThresholdVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 4)
)
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdVarTable.setStatus("current")
_CmEthernetAccPortThresholdVarEntry_Object = MibTableRow
cmEthernetAccPortThresholdVarEntry = _CmEthernetAccPortThresholdVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 4, 1)
)
cmEthernetAccPortThresholdVarEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdVarEntry.setStatus("current")
_CmEthernetAccPortThresholdVarOprVariance_Type = Integer32
_CmEthernetAccPortThresholdVarOprVariance_Object = MibTableColumn
cmEthernetAccPortThresholdVarOprVariance = _CmEthernetAccPortThresholdVarOprVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 4, 1, 1),
    _CmEthernetAccPortThresholdVarOprVariance_Type()
)
cmEthernetAccPortThresholdVarOprVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdVarOprVariance.setStatus("current")
_CmEthernetAccPortThresholdVarOptVariance_Type = Integer32
_CmEthernetAccPortThresholdVarOptVariance_Object = MibTableColumn
cmEthernetAccPortThresholdVarOptVariance = _CmEthernetAccPortThresholdVarOptVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 4, 1, 2),
    _CmEthernetAccPortThresholdVarOptVariance_Type()
)
cmEthernetAccPortThresholdVarOptVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdVarOptVariance.setStatus("current")
_CmEthernetNetPortStatsTable_Object = MibTable
cmEthernetNetPortStatsTable = _CmEthernetNetPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5)
)
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsTable.setStatus("current")
_CmEthernetNetPortStatsEntry_Object = MibTableRow
cmEthernetNetPortStatsEntry = _CmEthernetNetPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1)
)
cmEthernetNetPortStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsEntry.setStatus("current")


class _CmEthernetNetPortStatsIndex_Type(Integer32):
    """Custom type cmEthernetNetPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmEthernetNetPortStatsIndex_Type.__name__ = "Integer32"
_CmEthernetNetPortStatsIndex_Object = MibTableColumn
cmEthernetNetPortStatsIndex = _CmEthernetNetPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 1),
    _CmEthernetNetPortStatsIndex_Type()
)
cmEthernetNetPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsIndex.setStatus("current")
_CmEthernetNetPortStatsIntervalType_Type = CmPmIntervalType
_CmEthernetNetPortStatsIntervalType_Object = MibTableColumn
cmEthernetNetPortStatsIntervalType = _CmEthernetNetPortStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 2),
    _CmEthernetNetPortStatsIntervalType_Type()
)
cmEthernetNetPortStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsIntervalType.setStatus("current")
_CmEthernetNetPortStatsValid_Type = TruthValue
_CmEthernetNetPortStatsValid_Object = MibTableColumn
cmEthernetNetPortStatsValid = _CmEthernetNetPortStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 3),
    _CmEthernetNetPortStatsValid_Type()
)
cmEthernetNetPortStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsValid.setStatus("current")
_CmEthernetNetPortStatsAction_Type = CmPmBinAction
_CmEthernetNetPortStatsAction_Object = MibTableColumn
cmEthernetNetPortStatsAction = _CmEthernetNetPortStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 4),
    _CmEthernetNetPortStatsAction_Type()
)
cmEthernetNetPortStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsAction.setStatus("current")
_CmEthernetNetPortStatsESBF_Type = PerfCounter64
_CmEthernetNetPortStatsESBF_Object = MibTableColumn
cmEthernetNetPortStatsESBF = _CmEthernetNetPortStatsESBF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 5),
    _CmEthernetNetPortStatsESBF_Type()
)
cmEthernetNetPortStatsESBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESBF.setStatus("current")
_CmEthernetNetPortStatsESBP_Type = PerfCounter64
_CmEthernetNetPortStatsESBP_Object = MibTableColumn
cmEthernetNetPortStatsESBP = _CmEthernetNetPortStatsESBP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 6),
    _CmEthernetNetPortStatsESBP_Type()
)
cmEthernetNetPortStatsESBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESBP.setStatus("current")
_CmEthernetNetPortStatsESBS_Type = PerfCounter64
_CmEthernetNetPortStatsESBS_Object = MibTableColumn
cmEthernetNetPortStatsESBS = _CmEthernetNetPortStatsESBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 7),
    _CmEthernetNetPortStatsESBS_Type()
)
cmEthernetNetPortStatsESBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESBS.setStatus("current")
_CmEthernetNetPortStatsESC_Type = PerfCounter64
_CmEthernetNetPortStatsESC_Object = MibTableColumn
cmEthernetNetPortStatsESC = _CmEthernetNetPortStatsESC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 8),
    _CmEthernetNetPortStatsESC_Type()
)
cmEthernetNetPortStatsESC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESC.setStatus("current")
_CmEthernetNetPortStatsESCAE_Type = PerfCounter64
_CmEthernetNetPortStatsESCAE_Object = MibTableColumn
cmEthernetNetPortStatsESCAE = _CmEthernetNetPortStatsESCAE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 9),
    _CmEthernetNetPortStatsESCAE_Type()
)
cmEthernetNetPortStatsESCAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESCAE.setStatus("current")
_CmEthernetNetPortStatsESDE_Type = PerfCounter64
_CmEthernetNetPortStatsESDE_Object = MibTableColumn
cmEthernetNetPortStatsESDE = _CmEthernetNetPortStatsESDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 10),
    _CmEthernetNetPortStatsESDE_Type()
)
cmEthernetNetPortStatsESDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESDE.setStatus("current")
_CmEthernetNetPortStatsESF_Type = PerfCounter64
_CmEthernetNetPortStatsESF_Object = MibTableColumn
cmEthernetNetPortStatsESF = _CmEthernetNetPortStatsESF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 11),
    _CmEthernetNetPortStatsESF_Type()
)
cmEthernetNetPortStatsESF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESF.setStatus("current")
_CmEthernetNetPortStatsESFS_Type = PerfCounter64
_CmEthernetNetPortStatsESFS_Object = MibTableColumn
cmEthernetNetPortStatsESFS = _CmEthernetNetPortStatsESFS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 12),
    _CmEthernetNetPortStatsESFS_Type()
)
cmEthernetNetPortStatsESFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESFS.setStatus("current")
_CmEthernetNetPortStatsESJ_Type = PerfCounter64
_CmEthernetNetPortStatsESJ_Object = MibTableColumn
cmEthernetNetPortStatsESJ = _CmEthernetNetPortStatsESJ_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 13),
    _CmEthernetNetPortStatsESJ_Type()
)
cmEthernetNetPortStatsESJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESJ.setStatus("current")
_CmEthernetNetPortStatsESMF_Type = PerfCounter64
_CmEthernetNetPortStatsESMF_Object = MibTableColumn
cmEthernetNetPortStatsESMF = _CmEthernetNetPortStatsESMF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 14),
    _CmEthernetNetPortStatsESMF_Type()
)
cmEthernetNetPortStatsESMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESMF.setStatus("current")
_CmEthernetNetPortStatsESMP_Type = PerfCounter64
_CmEthernetNetPortStatsESMP_Object = MibTableColumn
cmEthernetNetPortStatsESMP = _CmEthernetNetPortStatsESMP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 15),
    _CmEthernetNetPortStatsESMP_Type()
)
cmEthernetNetPortStatsESMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESMP.setStatus("current")
_CmEthernetNetPortStatsESO_Type = PerfCounter64
_CmEthernetNetPortStatsESO_Object = MibTableColumn
cmEthernetNetPortStatsESO = _CmEthernetNetPortStatsESO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 16),
    _CmEthernetNetPortStatsESO_Type()
)
cmEthernetNetPortStatsESO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESO.setStatus("current")
_CmEthernetNetPortStatsESOF_Type = PerfCounter64
_CmEthernetNetPortStatsESOF_Object = MibTableColumn
cmEthernetNetPortStatsESOF = _CmEthernetNetPortStatsESOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 17),
    _CmEthernetNetPortStatsESOF_Type()
)
cmEthernetNetPortStatsESOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESOF.setStatus("current")
_CmEthernetNetPortStatsESOP_Type = PerfCounter64
_CmEthernetNetPortStatsESOP_Object = MibTableColumn
cmEthernetNetPortStatsESOP = _CmEthernetNetPortStatsESOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 18),
    _CmEthernetNetPortStatsESOP_Type()
)
cmEthernetNetPortStatsESOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESOP.setStatus("current")
_CmEthernetNetPortStatsESP_Type = PerfCounter64
_CmEthernetNetPortStatsESP_Object = MibTableColumn
cmEthernetNetPortStatsESP = _CmEthernetNetPortStatsESP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 19),
    _CmEthernetNetPortStatsESP_Type()
)
cmEthernetNetPortStatsESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESP.setStatus("current")
_CmEthernetNetPortStatsESP64_Type = PerfCounter64
_CmEthernetNetPortStatsESP64_Object = MibTableColumn
cmEthernetNetPortStatsESP64 = _CmEthernetNetPortStatsESP64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 20),
    _CmEthernetNetPortStatsESP64_Type()
)
cmEthernetNetPortStatsESP64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESP64.setStatus("current")
_CmEthernetNetPortStatsESP65_Type = PerfCounter64
_CmEthernetNetPortStatsESP65_Object = MibTableColumn
cmEthernetNetPortStatsESP65 = _CmEthernetNetPortStatsESP65_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 21),
    _CmEthernetNetPortStatsESP65_Type()
)
cmEthernetNetPortStatsESP65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESP65.setStatus("current")
_CmEthernetNetPortStatsESP128_Type = PerfCounter64
_CmEthernetNetPortStatsESP128_Object = MibTableColumn
cmEthernetNetPortStatsESP128 = _CmEthernetNetPortStatsESP128_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 22),
    _CmEthernetNetPortStatsESP128_Type()
)
cmEthernetNetPortStatsESP128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESP128.setStatus("current")
_CmEthernetNetPortStatsESP256_Type = PerfCounter64
_CmEthernetNetPortStatsESP256_Object = MibTableColumn
cmEthernetNetPortStatsESP256 = _CmEthernetNetPortStatsESP256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 23),
    _CmEthernetNetPortStatsESP256_Type()
)
cmEthernetNetPortStatsESP256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESP256.setStatus("current")
_CmEthernetNetPortStatsESP512_Type = PerfCounter64
_CmEthernetNetPortStatsESP512_Object = MibTableColumn
cmEthernetNetPortStatsESP512 = _CmEthernetNetPortStatsESP512_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 24),
    _CmEthernetNetPortStatsESP512_Type()
)
cmEthernetNetPortStatsESP512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESP512.setStatus("current")
_CmEthernetNetPortStatsESP1024_Type = PerfCounter64
_CmEthernetNetPortStatsESP1024_Object = MibTableColumn
cmEthernetNetPortStatsESP1024 = _CmEthernetNetPortStatsESP1024_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 25),
    _CmEthernetNetPortStatsESP1024_Type()
)
cmEthernetNetPortStatsESP1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESP1024.setStatus("current")
_CmEthernetNetPortStatsESP1519_Type = PerfCounter64
_CmEthernetNetPortStatsESP1519_Object = MibTableColumn
cmEthernetNetPortStatsESP1519 = _CmEthernetNetPortStatsESP1519_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 26),
    _CmEthernetNetPortStatsESP1519_Type()
)
cmEthernetNetPortStatsESP1519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESP1519.setStatus("current")
_CmEthernetNetPortStatsESUF_Type = PerfCounter64
_CmEthernetNetPortStatsESUF_Object = MibTableColumn
cmEthernetNetPortStatsESUF = _CmEthernetNetPortStatsESUF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 27),
    _CmEthernetNetPortStatsESUF_Type()
)
cmEthernetNetPortStatsESUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESUF.setStatus("current")
_CmEthernetNetPortStatsESUP_Type = PerfCounter64
_CmEthernetNetPortStatsESUP_Object = MibTableColumn
cmEthernetNetPortStatsESUP = _CmEthernetNetPortStatsESUP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 28),
    _CmEthernetNetPortStatsESUP_Type()
)
cmEthernetNetPortStatsESUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsESUP.setStatus("current")
_CmEthernetNetPortStatsL2CPFD_Type = PerfCounter64
_CmEthernetNetPortStatsL2CPFD_Object = MibTableColumn
cmEthernetNetPortStatsL2CPFD = _CmEthernetNetPortStatsL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 29),
    _CmEthernetNetPortStatsL2CPFD_Type()
)
cmEthernetNetPortStatsL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsL2CPFD.setStatus("current")
_CmEthernetNetPortStatsL2CPFP_Type = PerfCounter64
_CmEthernetNetPortStatsL2CPFP_Object = MibTableColumn
cmEthernetNetPortStatsL2CPFP = _CmEthernetNetPortStatsL2CPFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 30),
    _CmEthernetNetPortStatsL2CPFP_Type()
)
cmEthernetNetPortStatsL2CPFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsL2CPFP.setStatus("current")
_CmEthernetNetPortStatsLES_Type = PerfCounter64
_CmEthernetNetPortStatsLES_Object = MibTableColumn
cmEthernetNetPortStatsLES = _CmEthernetNetPortStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 31),
    _CmEthernetNetPortStatsLES_Type()
)
cmEthernetNetPortStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsLES.setStatus("deprecated")
_CmEthernetNetPortStatsLBC_Type = Integer32
_CmEthernetNetPortStatsLBC_Object = MibTableColumn
cmEthernetNetPortStatsLBC = _CmEthernetNetPortStatsLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 32),
    _CmEthernetNetPortStatsLBC_Type()
)
cmEthernetNetPortStatsLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsLBC.setStatus("current")
_CmEthernetNetPortStatsOPT_Type = Integer32
_CmEthernetNetPortStatsOPT_Object = MibTableColumn
cmEthernetNetPortStatsOPT = _CmEthernetNetPortStatsOPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 33),
    _CmEthernetNetPortStatsOPT_Type()
)
cmEthernetNetPortStatsOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsOPT.setStatus("current")
_CmEthernetNetPortStatsOPR_Type = Integer32
_CmEthernetNetPortStatsOPR_Object = MibTableColumn
cmEthernetNetPortStatsOPR = _CmEthernetNetPortStatsOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 34),
    _CmEthernetNetPortStatsOPR_Type()
)
cmEthernetNetPortStatsOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsOPR.setStatus("current")
_CmEthernetNetPortStatsAUFD_Type = PerfCounter64
_CmEthernetNetPortStatsAUFD_Object = MibTableColumn
cmEthernetNetPortStatsAUFD = _CmEthernetNetPortStatsAUFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 35),
    _CmEthernetNetPortStatsAUFD_Type()
)
cmEthernetNetPortStatsAUFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsAUFD.setStatus("current")
_CmEthernetNetPortStatsAPFD_Type = PerfCounter64
_CmEthernetNetPortStatsAPFD_Object = MibTableColumn
cmEthernetNetPortStatsAPFD = _CmEthernetNetPortStatsAPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 36),
    _CmEthernetNetPortStatsAPFD_Type()
)
cmEthernetNetPortStatsAPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsAPFD.setStatus("current")
_CmEthernetNetPortStatsABRRx_Type = PerfCounter64
_CmEthernetNetPortStatsABRRx_Object = MibTableColumn
cmEthernetNetPortStatsABRRx = _CmEthernetNetPortStatsABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 37),
    _CmEthernetNetPortStatsABRRx_Type()
)
cmEthernetNetPortStatsABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsABRRx.setStatus("current")
_CmEthernetNetPortStatsABRTx_Type = PerfCounter64
_CmEthernetNetPortStatsABRTx_Object = MibTableColumn
cmEthernetNetPortStatsABRTx = _CmEthernetNetPortStatsABRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 38),
    _CmEthernetNetPortStatsABRTx_Type()
)
cmEthernetNetPortStatsABRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsABRTx.setStatus("current")
_CmEthernetNetPortStatsPSC_Type = PerfCounter64
_CmEthernetNetPortStatsPSC_Object = MibTableColumn
cmEthernetNetPortStatsPSC = _CmEthernetNetPortStatsPSC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 39),
    _CmEthernetNetPortStatsPSC_Type()
)
cmEthernetNetPortStatsPSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsPSC.setStatus("current")
_CmEthernetNetPortStatsTemp_Type = Integer32
_CmEthernetNetPortStatsTemp_Object = MibTableColumn
cmEthernetNetPortStatsTemp = _CmEthernetNetPortStatsTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 40),
    _CmEthernetNetPortStatsTemp_Type()
)
cmEthernetNetPortStatsTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsTemp.setStatus("current")
_CmEthernetNetPortStatsUAS_Type = PerfCounter64
_CmEthernetNetPortStatsUAS_Object = MibTableColumn
cmEthernetNetPortStatsUAS = _CmEthernetNetPortStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 41),
    _CmEthernetNetPortStatsUAS_Type()
)
cmEthernetNetPortStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsUAS.setStatus("current")
_CmEthernetNetPortStatsL2PTRxFramesEncap_Type = PerfCounter64
_CmEthernetNetPortStatsL2PTRxFramesEncap_Object = MibTableColumn
cmEthernetNetPortStatsL2PTRxFramesEncap = _CmEthernetNetPortStatsL2PTRxFramesEncap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 42),
    _CmEthernetNetPortStatsL2PTRxFramesEncap_Type()
)
cmEthernetNetPortStatsL2PTRxFramesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsL2PTRxFramesEncap.setStatus("current")
_CmEthernetNetPortStatsL2PTTxFramesDecap_Type = PerfCounter64
_CmEthernetNetPortStatsL2PTTxFramesDecap_Object = MibTableColumn
cmEthernetNetPortStatsL2PTTxFramesDecap = _CmEthernetNetPortStatsL2PTTxFramesDecap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 43),
    _CmEthernetNetPortStatsL2PTTxFramesDecap_Type()
)
cmEthernetNetPortStatsL2PTTxFramesDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsL2PTTxFramesDecap.setStatus("current")
_CmEthernetNetPortStatsIBRMaxRx_Type = PerfCounter64
_CmEthernetNetPortStatsIBRMaxRx_Object = MibTableColumn
cmEthernetNetPortStatsIBRMaxRx = _CmEthernetNetPortStatsIBRMaxRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 44),
    _CmEthernetNetPortStatsIBRMaxRx_Type()
)
cmEthernetNetPortStatsIBRMaxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsIBRMaxRx.setStatus("current")
_CmEthernetNetPortStatsIBRMaxTx_Type = PerfCounter64
_CmEthernetNetPortStatsIBRMaxTx_Object = MibTableColumn
cmEthernetNetPortStatsIBRMaxTx = _CmEthernetNetPortStatsIBRMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 45),
    _CmEthernetNetPortStatsIBRMaxTx_Type()
)
cmEthernetNetPortStatsIBRMaxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsIBRMaxTx.setStatus("current")
_CmEthernetNetPortStatsIBRMinRx_Type = PerfCounter64
_CmEthernetNetPortStatsIBRMinRx_Object = MibTableColumn
cmEthernetNetPortStatsIBRMinRx = _CmEthernetNetPortStatsIBRMinRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 46),
    _CmEthernetNetPortStatsIBRMinRx_Type()
)
cmEthernetNetPortStatsIBRMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsIBRMinRx.setStatus("current")
_CmEthernetNetPortStatsIBRMinTx_Type = PerfCounter64
_CmEthernetNetPortStatsIBRMinTx_Object = MibTableColumn
cmEthernetNetPortStatsIBRMinTx = _CmEthernetNetPortStatsIBRMinTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 47),
    _CmEthernetNetPortStatsIBRMinTx_Type()
)
cmEthernetNetPortStatsIBRMinTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsIBRMinTx.setStatus("current")
_CmEthernetNetPortStatsIBRRx_Type = PerfCounter64
_CmEthernetNetPortStatsIBRRx_Object = MibTableColumn
cmEthernetNetPortStatsIBRRx = _CmEthernetNetPortStatsIBRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 48),
    _CmEthernetNetPortStatsIBRRx_Type()
)
cmEthernetNetPortStatsIBRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsIBRRx.setStatus("current")
_CmEthernetNetPortStatsIBRTx_Type = PerfCounter64
_CmEthernetNetPortStatsIBRTx_Object = MibTableColumn
cmEthernetNetPortStatsIBRTx = _CmEthernetNetPortStatsIBRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 49),
    _CmEthernetNetPortStatsIBRTx_Type()
)
cmEthernetNetPortStatsIBRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsIBRTx.setStatus("current")
_CmEthernetNetPortStatsFmcd_Type = PerfCounter64
_CmEthernetNetPortStatsFmcd_Object = MibTableColumn
cmEthernetNetPortStatsFmcd = _CmEthernetNetPortStatsFmcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 50),
    _CmEthernetNetPortStatsFmcd_Type()
)
cmEthernetNetPortStatsFmcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsFmcd.setStatus("current")
_CmEthernetNetPortStatsFbcd_Type = PerfCounter64
_CmEthernetNetPortStatsFbcd_Object = MibTableColumn
cmEthernetNetPortStatsFbcd = _CmEthernetNetPortStatsFbcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 51),
    _CmEthernetNetPortStatsFbcd_Type()
)
cmEthernetNetPortStatsFbcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsFbcd.setStatus("current")
_CmEthernetNetPortStatsAclDropNoMatch_Type = PerfCounter64
_CmEthernetNetPortStatsAclDropNoMatch_Object = MibTableColumn
cmEthernetNetPortStatsAclDropNoMatch = _CmEthernetNetPortStatsAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 52),
    _CmEthernetNetPortStatsAclDropNoMatch_Type()
)
cmEthernetNetPortStatsAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsAclDropNoMatch.setStatus("current")
_CmEthernetNetPortStatsAclFwd2Cpu_Type = PerfCounter64
_CmEthernetNetPortStatsAclFwd2Cpu_Object = MibTableColumn
cmEthernetNetPortStatsAclFwd2Cpu = _CmEthernetNetPortStatsAclFwd2Cpu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 53),
    _CmEthernetNetPortStatsAclFwd2Cpu_Type()
)
cmEthernetNetPortStatsAclFwd2Cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsAclFwd2Cpu.setStatus("current")
_CmEthernetNetPortStatsDhcpDropNoAssocIf_Type = PerfCounter64
_CmEthernetNetPortStatsDhcpDropNoAssocIf_Object = MibTableColumn
cmEthernetNetPortStatsDhcpDropNoAssocIf = _CmEthernetNetPortStatsDhcpDropNoAssocIf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 54),
    _CmEthernetNetPortStatsDhcpDropNoAssocIf_Type()
)
cmEthernetNetPortStatsDhcpDropNoAssocIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsDhcpDropNoAssocIf.setStatus("current")
_CmEthernetNetPortStatsLkupFails_Type = PerfCounter64
_CmEthernetNetPortStatsLkupFails_Object = MibTableColumn
cmEthernetNetPortStatsLkupFails = _CmEthernetNetPortStatsLkupFails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 5, 1, 55),
    _CmEthernetNetPortStatsLkupFails_Type()
)
cmEthernetNetPortStatsLkupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsLkupFails.setStatus("current")
_CmEthernetNetPortHistoryTable_Object = MibTable
cmEthernetNetPortHistoryTable = _CmEthernetNetPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6)
)
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryTable.setStatus("current")
_CmEthernetNetPortHistoryEntry_Object = MibTableRow
cmEthernetNetPortHistoryEntry = _CmEthernetNetPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1)
)
cmEthernetNetPortHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryEntry.setStatus("current")


class _CmEthernetNetPortHistoryIndex_Type(Integer32):
    """Custom type cmEthernetNetPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmEthernetNetPortHistoryIndex_Type.__name__ = "Integer32"
_CmEthernetNetPortHistoryIndex_Object = MibTableColumn
cmEthernetNetPortHistoryIndex = _CmEthernetNetPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 1),
    _CmEthernetNetPortHistoryIndex_Type()
)
cmEthernetNetPortHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryIndex.setStatus("current")
_CmEthernetNetPortHistoryTime_Type = DateAndTime
_CmEthernetNetPortHistoryTime_Object = MibTableColumn
cmEthernetNetPortHistoryTime = _CmEthernetNetPortHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 2),
    _CmEthernetNetPortHistoryTime_Type()
)
cmEthernetNetPortHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryTime.setStatus("current")
_CmEthernetNetPortHistoryValid_Type = TruthValue
_CmEthernetNetPortHistoryValid_Object = MibTableColumn
cmEthernetNetPortHistoryValid = _CmEthernetNetPortHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 3),
    _CmEthernetNetPortHistoryValid_Type()
)
cmEthernetNetPortHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryValid.setStatus("current")
_CmEthernetNetPortHistoryAction_Type = CmPmBinAction
_CmEthernetNetPortHistoryAction_Object = MibTableColumn
cmEthernetNetPortHistoryAction = _CmEthernetNetPortHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 4),
    _CmEthernetNetPortHistoryAction_Type()
)
cmEthernetNetPortHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryAction.setStatus("current")
_CmEthernetNetPortHistoryESBF_Type = PerfCounter64
_CmEthernetNetPortHistoryESBF_Object = MibTableColumn
cmEthernetNetPortHistoryESBF = _CmEthernetNetPortHistoryESBF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 5),
    _CmEthernetNetPortHistoryESBF_Type()
)
cmEthernetNetPortHistoryESBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESBF.setStatus("current")
_CmEthernetNetPortHistoryESBP_Type = PerfCounter64
_CmEthernetNetPortHistoryESBP_Object = MibTableColumn
cmEthernetNetPortHistoryESBP = _CmEthernetNetPortHistoryESBP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 6),
    _CmEthernetNetPortHistoryESBP_Type()
)
cmEthernetNetPortHistoryESBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESBP.setStatus("current")
_CmEthernetNetPortHistoryESBS_Type = PerfCounter64
_CmEthernetNetPortHistoryESBS_Object = MibTableColumn
cmEthernetNetPortHistoryESBS = _CmEthernetNetPortHistoryESBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 7),
    _CmEthernetNetPortHistoryESBS_Type()
)
cmEthernetNetPortHistoryESBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESBS.setStatus("current")
_CmEthernetNetPortHistoryESC_Type = PerfCounter64
_CmEthernetNetPortHistoryESC_Object = MibTableColumn
cmEthernetNetPortHistoryESC = _CmEthernetNetPortHistoryESC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 8),
    _CmEthernetNetPortHistoryESC_Type()
)
cmEthernetNetPortHistoryESC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESC.setStatus("current")
_CmEthernetNetPortHistoryESCAE_Type = PerfCounter64
_CmEthernetNetPortHistoryESCAE_Object = MibTableColumn
cmEthernetNetPortHistoryESCAE = _CmEthernetNetPortHistoryESCAE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 9),
    _CmEthernetNetPortHistoryESCAE_Type()
)
cmEthernetNetPortHistoryESCAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESCAE.setStatus("current")
_CmEthernetNetPortHistoryESDE_Type = PerfCounter64
_CmEthernetNetPortHistoryESDE_Object = MibTableColumn
cmEthernetNetPortHistoryESDE = _CmEthernetNetPortHistoryESDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 10),
    _CmEthernetNetPortHistoryESDE_Type()
)
cmEthernetNetPortHistoryESDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESDE.setStatus("current")
_CmEthernetNetPortHistoryESF_Type = PerfCounter64
_CmEthernetNetPortHistoryESF_Object = MibTableColumn
cmEthernetNetPortHistoryESF = _CmEthernetNetPortHistoryESF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 11),
    _CmEthernetNetPortHistoryESF_Type()
)
cmEthernetNetPortHistoryESF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESF.setStatus("current")
_CmEthernetNetPortHistoryESFS_Type = PerfCounter64
_CmEthernetNetPortHistoryESFS_Object = MibTableColumn
cmEthernetNetPortHistoryESFS = _CmEthernetNetPortHistoryESFS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 12),
    _CmEthernetNetPortHistoryESFS_Type()
)
cmEthernetNetPortHistoryESFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESFS.setStatus("current")
_CmEthernetNetPortHistoryESJ_Type = PerfCounter64
_CmEthernetNetPortHistoryESJ_Object = MibTableColumn
cmEthernetNetPortHistoryESJ = _CmEthernetNetPortHistoryESJ_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 13),
    _CmEthernetNetPortHistoryESJ_Type()
)
cmEthernetNetPortHistoryESJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESJ.setStatus("current")
_CmEthernetNetPortHistoryESMF_Type = PerfCounter64
_CmEthernetNetPortHistoryESMF_Object = MibTableColumn
cmEthernetNetPortHistoryESMF = _CmEthernetNetPortHistoryESMF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 14),
    _CmEthernetNetPortHistoryESMF_Type()
)
cmEthernetNetPortHistoryESMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESMF.setStatus("current")
_CmEthernetNetPortHistoryESMP_Type = PerfCounter64
_CmEthernetNetPortHistoryESMP_Object = MibTableColumn
cmEthernetNetPortHistoryESMP = _CmEthernetNetPortHistoryESMP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 15),
    _CmEthernetNetPortHistoryESMP_Type()
)
cmEthernetNetPortHistoryESMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESMP.setStatus("current")
_CmEthernetNetPortHistoryESO_Type = PerfCounter64
_CmEthernetNetPortHistoryESO_Object = MibTableColumn
cmEthernetNetPortHistoryESO = _CmEthernetNetPortHistoryESO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 16),
    _CmEthernetNetPortHistoryESO_Type()
)
cmEthernetNetPortHistoryESO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESO.setStatus("current")
_CmEthernetNetPortHistoryESOF_Type = PerfCounter64
_CmEthernetNetPortHistoryESOF_Object = MibTableColumn
cmEthernetNetPortHistoryESOF = _CmEthernetNetPortHistoryESOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 17),
    _CmEthernetNetPortHistoryESOF_Type()
)
cmEthernetNetPortHistoryESOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESOF.setStatus("current")
_CmEthernetNetPortHistoryESOP_Type = PerfCounter64
_CmEthernetNetPortHistoryESOP_Object = MibTableColumn
cmEthernetNetPortHistoryESOP = _CmEthernetNetPortHistoryESOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 18),
    _CmEthernetNetPortHistoryESOP_Type()
)
cmEthernetNetPortHistoryESOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESOP.setStatus("current")
_CmEthernetNetPortHistoryESP_Type = PerfCounter64
_CmEthernetNetPortHistoryESP_Object = MibTableColumn
cmEthernetNetPortHistoryESP = _CmEthernetNetPortHistoryESP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 19),
    _CmEthernetNetPortHistoryESP_Type()
)
cmEthernetNetPortHistoryESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESP.setStatus("current")
_CmEthernetNetPortHistoryESP64_Type = PerfCounter64
_CmEthernetNetPortHistoryESP64_Object = MibTableColumn
cmEthernetNetPortHistoryESP64 = _CmEthernetNetPortHistoryESP64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 20),
    _CmEthernetNetPortHistoryESP64_Type()
)
cmEthernetNetPortHistoryESP64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESP64.setStatus("current")
_CmEthernetNetPortHistoryESP65_Type = PerfCounter64
_CmEthernetNetPortHistoryESP65_Object = MibTableColumn
cmEthernetNetPortHistoryESP65 = _CmEthernetNetPortHistoryESP65_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 21),
    _CmEthernetNetPortHistoryESP65_Type()
)
cmEthernetNetPortHistoryESP65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESP65.setStatus("current")
_CmEthernetNetPortHistoryESP128_Type = PerfCounter64
_CmEthernetNetPortHistoryESP128_Object = MibTableColumn
cmEthernetNetPortHistoryESP128 = _CmEthernetNetPortHistoryESP128_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 22),
    _CmEthernetNetPortHistoryESP128_Type()
)
cmEthernetNetPortHistoryESP128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESP128.setStatus("current")
_CmEthernetNetPortHistoryESP256_Type = PerfCounter64
_CmEthernetNetPortHistoryESP256_Object = MibTableColumn
cmEthernetNetPortHistoryESP256 = _CmEthernetNetPortHistoryESP256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 23),
    _CmEthernetNetPortHistoryESP256_Type()
)
cmEthernetNetPortHistoryESP256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESP256.setStatus("current")
_CmEthernetNetPortHistoryESP512_Type = PerfCounter64
_CmEthernetNetPortHistoryESP512_Object = MibTableColumn
cmEthernetNetPortHistoryESP512 = _CmEthernetNetPortHistoryESP512_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 24),
    _CmEthernetNetPortHistoryESP512_Type()
)
cmEthernetNetPortHistoryESP512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESP512.setStatus("current")
_CmEthernetNetPortHistoryESP1024_Type = PerfCounter64
_CmEthernetNetPortHistoryESP1024_Object = MibTableColumn
cmEthernetNetPortHistoryESP1024 = _CmEthernetNetPortHistoryESP1024_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 25),
    _CmEthernetNetPortHistoryESP1024_Type()
)
cmEthernetNetPortHistoryESP1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESP1024.setStatus("current")
_CmEthernetNetPortHistoryESP1519_Type = PerfCounter64
_CmEthernetNetPortHistoryESP1519_Object = MibTableColumn
cmEthernetNetPortHistoryESP1519 = _CmEthernetNetPortHistoryESP1519_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 26),
    _CmEthernetNetPortHistoryESP1519_Type()
)
cmEthernetNetPortHistoryESP1519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESP1519.setStatus("current")
_CmEthernetNetPortHistoryESUF_Type = PerfCounter64
_CmEthernetNetPortHistoryESUF_Object = MibTableColumn
cmEthernetNetPortHistoryESUF = _CmEthernetNetPortHistoryESUF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 27),
    _CmEthernetNetPortHistoryESUF_Type()
)
cmEthernetNetPortHistoryESUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESUF.setStatus("current")
_CmEthernetNetPortHistoryESUP_Type = PerfCounter64
_CmEthernetNetPortHistoryESUP_Object = MibTableColumn
cmEthernetNetPortHistoryESUP = _CmEthernetNetPortHistoryESUP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 28),
    _CmEthernetNetPortHistoryESUP_Type()
)
cmEthernetNetPortHistoryESUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryESUP.setStatus("current")
_CmEthernetNetPortHistoryL2CPFD_Type = PerfCounter64
_CmEthernetNetPortHistoryL2CPFD_Object = MibTableColumn
cmEthernetNetPortHistoryL2CPFD = _CmEthernetNetPortHistoryL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 29),
    _CmEthernetNetPortHistoryL2CPFD_Type()
)
cmEthernetNetPortHistoryL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryL2CPFD.setStatus("current")
_CmEthernetNetPortHistoryL2CPFP_Type = PerfCounter64
_CmEthernetNetPortHistoryL2CPFP_Object = MibTableColumn
cmEthernetNetPortHistoryL2CPFP = _CmEthernetNetPortHistoryL2CPFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 30),
    _CmEthernetNetPortHistoryL2CPFP_Type()
)
cmEthernetNetPortHistoryL2CPFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryL2CPFP.setStatus("current")
_CmEthernetNetPortHistoryLES_Type = PerfCounter64
_CmEthernetNetPortHistoryLES_Object = MibTableColumn
cmEthernetNetPortHistoryLES = _CmEthernetNetPortHistoryLES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 31),
    _CmEthernetNetPortHistoryLES_Type()
)
cmEthernetNetPortHistoryLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryLES.setStatus("deprecated")
_CmEthernetNetPortHistoryLBC_Type = Integer32
_CmEthernetNetPortHistoryLBC_Object = MibTableColumn
cmEthernetNetPortHistoryLBC = _CmEthernetNetPortHistoryLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 32),
    _CmEthernetNetPortHistoryLBC_Type()
)
cmEthernetNetPortHistoryLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryLBC.setStatus("current")
_CmEthernetNetPortHistoryOPT_Type = Integer32
_CmEthernetNetPortHistoryOPT_Object = MibTableColumn
cmEthernetNetPortHistoryOPT = _CmEthernetNetPortHistoryOPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 33),
    _CmEthernetNetPortHistoryOPT_Type()
)
cmEthernetNetPortHistoryOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryOPT.setStatus("current")
_CmEthernetNetPortHistoryOPR_Type = Integer32
_CmEthernetNetPortHistoryOPR_Object = MibTableColumn
cmEthernetNetPortHistoryOPR = _CmEthernetNetPortHistoryOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 34),
    _CmEthernetNetPortHistoryOPR_Type()
)
cmEthernetNetPortHistoryOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryOPR.setStatus("current")
_CmEthernetNetPortHistoryAUFD_Type = PerfCounter64
_CmEthernetNetPortHistoryAUFD_Object = MibTableColumn
cmEthernetNetPortHistoryAUFD = _CmEthernetNetPortHistoryAUFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 35),
    _CmEthernetNetPortHistoryAUFD_Type()
)
cmEthernetNetPortHistoryAUFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryAUFD.setStatus("current")
_CmEthernetNetPortHistoryAPFD_Type = PerfCounter64
_CmEthernetNetPortHistoryAPFD_Object = MibTableColumn
cmEthernetNetPortHistoryAPFD = _CmEthernetNetPortHistoryAPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 36),
    _CmEthernetNetPortHistoryAPFD_Type()
)
cmEthernetNetPortHistoryAPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryAPFD.setStatus("current")
_CmEthernetNetPortHistoryABRRx_Type = PerfCounter64
_CmEthernetNetPortHistoryABRRx_Object = MibTableColumn
cmEthernetNetPortHistoryABRRx = _CmEthernetNetPortHistoryABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 37),
    _CmEthernetNetPortHistoryABRRx_Type()
)
cmEthernetNetPortHistoryABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryABRRx.setStatus("current")
_CmEthernetNetPortHistoryABRTx_Type = PerfCounter64
_CmEthernetNetPortHistoryABRTx_Object = MibTableColumn
cmEthernetNetPortHistoryABRTx = _CmEthernetNetPortHistoryABRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 38),
    _CmEthernetNetPortHistoryABRTx_Type()
)
cmEthernetNetPortHistoryABRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryABRTx.setStatus("current")
_CmEthernetNetPortHistoryPSC_Type = PerfCounter64
_CmEthernetNetPortHistoryPSC_Object = MibTableColumn
cmEthernetNetPortHistoryPSC = _CmEthernetNetPortHistoryPSC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 39),
    _CmEthernetNetPortHistoryPSC_Type()
)
cmEthernetNetPortHistoryPSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryPSC.setStatus("current")
_CmEthernetNetPortHistoryTemp_Type = Integer32
_CmEthernetNetPortHistoryTemp_Object = MibTableColumn
cmEthernetNetPortHistoryTemp = _CmEthernetNetPortHistoryTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 40),
    _CmEthernetNetPortHistoryTemp_Type()
)
cmEthernetNetPortHistoryTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryTemp.setStatus("current")
_CmEthernetNetPortHistoryUAS_Type = PerfCounter64
_CmEthernetNetPortHistoryUAS_Object = MibTableColumn
cmEthernetNetPortHistoryUAS = _CmEthernetNetPortHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 41),
    _CmEthernetNetPortHistoryUAS_Type()
)
cmEthernetNetPortHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryUAS.setStatus("current")
_CmEthernetNetPortHistoryL2PTRxFramesEncap_Type = PerfCounter64
_CmEthernetNetPortHistoryL2PTRxFramesEncap_Object = MibTableColumn
cmEthernetNetPortHistoryL2PTRxFramesEncap = _CmEthernetNetPortHistoryL2PTRxFramesEncap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 42),
    _CmEthernetNetPortHistoryL2PTRxFramesEncap_Type()
)
cmEthernetNetPortHistoryL2PTRxFramesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryL2PTRxFramesEncap.setStatus("current")
_CmEthernetNetPortHistoryL2PTTxFramesDecap_Type = PerfCounter64
_CmEthernetNetPortHistoryL2PTTxFramesDecap_Object = MibTableColumn
cmEthernetNetPortHistoryL2PTTxFramesDecap = _CmEthernetNetPortHistoryL2PTTxFramesDecap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 43),
    _CmEthernetNetPortHistoryL2PTTxFramesDecap_Type()
)
cmEthernetNetPortHistoryL2PTTxFramesDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryL2PTTxFramesDecap.setStatus("current")
_CmEthernetNetPortHistoryIBRMaxRx_Type = PerfCounter64
_CmEthernetNetPortHistoryIBRMaxRx_Object = MibTableColumn
cmEthernetNetPortHistoryIBRMaxRx = _CmEthernetNetPortHistoryIBRMaxRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 44),
    _CmEthernetNetPortHistoryIBRMaxRx_Type()
)
cmEthernetNetPortHistoryIBRMaxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryIBRMaxRx.setStatus("current")
_CmEthernetNetPortHistoryIBRMaxTx_Type = PerfCounter64
_CmEthernetNetPortHistoryIBRMaxTx_Object = MibTableColumn
cmEthernetNetPortHistoryIBRMaxTx = _CmEthernetNetPortHistoryIBRMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 45),
    _CmEthernetNetPortHistoryIBRMaxTx_Type()
)
cmEthernetNetPortHistoryIBRMaxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryIBRMaxTx.setStatus("current")
_CmEthernetNetPortHistoryIBRMinRx_Type = PerfCounter64
_CmEthernetNetPortHistoryIBRMinRx_Object = MibTableColumn
cmEthernetNetPortHistoryIBRMinRx = _CmEthernetNetPortHistoryIBRMinRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 46),
    _CmEthernetNetPortHistoryIBRMinRx_Type()
)
cmEthernetNetPortHistoryIBRMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryIBRMinRx.setStatus("current")
_CmEthernetNetPortHistoryIBRMinTx_Type = PerfCounter64
_CmEthernetNetPortHistoryIBRMinTx_Object = MibTableColumn
cmEthernetNetPortHistoryIBRMinTx = _CmEthernetNetPortHistoryIBRMinTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 47),
    _CmEthernetNetPortHistoryIBRMinTx_Type()
)
cmEthernetNetPortHistoryIBRMinTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryIBRMinTx.setStatus("current")
_CmEthernetNetPortHistoryIBRRx_Type = PerfCounter64
_CmEthernetNetPortHistoryIBRRx_Object = MibTableColumn
cmEthernetNetPortHistoryIBRRx = _CmEthernetNetPortHistoryIBRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 48),
    _CmEthernetNetPortHistoryIBRRx_Type()
)
cmEthernetNetPortHistoryIBRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryIBRRx.setStatus("current")
_CmEthernetNetPortHistoryIBRTx_Type = PerfCounter64
_CmEthernetNetPortHistoryIBRTx_Object = MibTableColumn
cmEthernetNetPortHistoryIBRTx = _CmEthernetNetPortHistoryIBRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 49),
    _CmEthernetNetPortHistoryIBRTx_Type()
)
cmEthernetNetPortHistoryIBRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryIBRTx.setStatus("current")
_CmEthernetNetPortHistoryFmcd_Type = PerfCounter64
_CmEthernetNetPortHistoryFmcd_Object = MibTableColumn
cmEthernetNetPortHistoryFmcd = _CmEthernetNetPortHistoryFmcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 50),
    _CmEthernetNetPortHistoryFmcd_Type()
)
cmEthernetNetPortHistoryFmcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryFmcd.setStatus("current")
_CmEthernetNetPortHistoryFbcd_Type = PerfCounter64
_CmEthernetNetPortHistoryFbcd_Object = MibTableColumn
cmEthernetNetPortHistoryFbcd = _CmEthernetNetPortHistoryFbcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 51),
    _CmEthernetNetPortHistoryFbcd_Type()
)
cmEthernetNetPortHistoryFbcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryFbcd.setStatus("current")
_CmEthernetNetPortHistoryAclDropNoMatch_Type = PerfCounter64
_CmEthernetNetPortHistoryAclDropNoMatch_Object = MibTableColumn
cmEthernetNetPortHistoryAclDropNoMatch = _CmEthernetNetPortHistoryAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 52),
    _CmEthernetNetPortHistoryAclDropNoMatch_Type()
)
cmEthernetNetPortHistoryAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryAclDropNoMatch.setStatus("current")
_CmEthernetNetPortHistoryAclFwd2Cpu_Type = PerfCounter64
_CmEthernetNetPortHistoryAclFwd2Cpu_Object = MibTableColumn
cmEthernetNetPortHistoryAclFwd2Cpu = _CmEthernetNetPortHistoryAclFwd2Cpu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 53),
    _CmEthernetNetPortHistoryAclFwd2Cpu_Type()
)
cmEthernetNetPortHistoryAclFwd2Cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryAclFwd2Cpu.setStatus("current")
_CmEthernetNetPortHistoryDhcpDropNoAssocIf_Type = PerfCounter64
_CmEthernetNetPortHistoryDhcpDropNoAssocIf_Object = MibTableColumn
cmEthernetNetPortHistoryDhcpDropNoAssocIf = _CmEthernetNetPortHistoryDhcpDropNoAssocIf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 54),
    _CmEthernetNetPortHistoryDhcpDropNoAssocIf_Type()
)
cmEthernetNetPortHistoryDhcpDropNoAssocIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryDhcpDropNoAssocIf.setStatus("current")
_CmEthernetNetPortHistoryLkupFails_Type = PerfCounter64
_CmEthernetNetPortHistoryLkupFails_Object = MibTableColumn
cmEthernetNetPortHistoryLkupFails = _CmEthernetNetPortHistoryLkupFails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 6, 1, 55),
    _CmEthernetNetPortHistoryLkupFails_Type()
)
cmEthernetNetPortHistoryLkupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryLkupFails.setStatus("current")
_CmEthernetNetPortThresholdTable_Object = MibTable
cmEthernetNetPortThresholdTable = _CmEthernetNetPortThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 7)
)
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdTable.setStatus("current")
_CmEthernetNetPortThresholdEntry_Object = MibTableRow
cmEthernetNetPortThresholdEntry = _CmEthernetNetPortThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 7, 1)
)
cmEthernetNetPortThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdEntry.setStatus("current")


class _CmEthernetNetPortThresholdIndex_Type(Integer32):
    """Custom type cmEthernetNetPortThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmEthernetNetPortThresholdIndex_Type.__name__ = "Integer32"
_CmEthernetNetPortThresholdIndex_Object = MibTableColumn
cmEthernetNetPortThresholdIndex = _CmEthernetNetPortThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 7, 1, 1),
    _CmEthernetNetPortThresholdIndex_Type()
)
cmEthernetNetPortThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdIndex.setStatus("current")
_CmEthernetNetPortThresholdInterval_Type = CmPmIntervalType
_CmEthernetNetPortThresholdInterval_Object = MibTableColumn
cmEthernetNetPortThresholdInterval = _CmEthernetNetPortThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 7, 1, 2),
    _CmEthernetNetPortThresholdInterval_Type()
)
cmEthernetNetPortThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdInterval.setStatus("current")
_CmEthernetNetPortThresholdVariable_Type = VariablePointer
_CmEthernetNetPortThresholdVariable_Object = MibTableColumn
cmEthernetNetPortThresholdVariable = _CmEthernetNetPortThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 7, 1, 3),
    _CmEthernetNetPortThresholdVariable_Type()
)
cmEthernetNetPortThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdVariable.setStatus("current")
_CmEthernetNetPortThresholdValueLo_Type = Unsigned32
_CmEthernetNetPortThresholdValueLo_Object = MibTableColumn
cmEthernetNetPortThresholdValueLo = _CmEthernetNetPortThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 7, 1, 4),
    _CmEthernetNetPortThresholdValueLo_Type()
)
cmEthernetNetPortThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdValueLo.setStatus("current")
_CmEthernetNetPortThresholdValueHi_Type = Unsigned32
_CmEthernetNetPortThresholdValueHi_Object = MibTableColumn
cmEthernetNetPortThresholdValueHi = _CmEthernetNetPortThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 7, 1, 5),
    _CmEthernetNetPortThresholdValueHi_Type()
)
cmEthernetNetPortThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdValueHi.setStatus("current")
_CmEthernetNetPortThresholdMonValue_Type = Counter64
_CmEthernetNetPortThresholdMonValue_Object = MibTableColumn
cmEthernetNetPortThresholdMonValue = _CmEthernetNetPortThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 7, 1, 6),
    _CmEthernetNetPortThresholdMonValue_Type()
)
cmEthernetNetPortThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdMonValue.setStatus("current")
_CmEthernetNetPortThresholdVarTable_Object = MibTable
cmEthernetNetPortThresholdVarTable = _CmEthernetNetPortThresholdVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 8)
)
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdVarTable.setStatus("current")
_CmEthernetNetPortThresholdVarEntry_Object = MibTableRow
cmEthernetNetPortThresholdVarEntry = _CmEthernetNetPortThresholdVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 8, 1)
)
cmEthernetNetPortThresholdVarEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdVarEntry.setStatus("current")
_CmEthernetNetPortThresholdVarOprVariance_Type = Integer32
_CmEthernetNetPortThresholdVarOprVariance_Object = MibTableColumn
cmEthernetNetPortThresholdVarOprVariance = _CmEthernetNetPortThresholdVarOprVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 8, 1, 1),
    _CmEthernetNetPortThresholdVarOprVariance_Type()
)
cmEthernetNetPortThresholdVarOprVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdVarOprVariance.setStatus("current")
_CmEthernetNetPortThresholdVarOptVariance_Type = Integer32
_CmEthernetNetPortThresholdVarOptVariance_Object = MibTableColumn
cmEthernetNetPortThresholdVarOptVariance = _CmEthernetNetPortThresholdVarOptVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 8, 1, 2),
    _CmEthernetNetPortThresholdVarOptVariance_Type()
)
cmEthernetNetPortThresholdVarOptVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdVarOptVariance.setStatus("current")
_CmFlowStatsTable_Object = MibTable
cmFlowStatsTable = _CmFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9)
)
if mibBuilder.loadTexts:
    cmFlowStatsTable.setStatus("current")
_CmFlowStatsEntry_Object = MibTableRow
cmFlowStatsEntry = _CmFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1)
)
cmFlowStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowStatsIndex"),
)
if mibBuilder.loadTexts:
    cmFlowStatsEntry.setStatus("current")


class _CmFlowStatsIndex_Type(Integer32):
    """Custom type cmFlowStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmFlowStatsIndex_Type.__name__ = "Integer32"
_CmFlowStatsIndex_Object = MibTableColumn
cmFlowStatsIndex = _CmFlowStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 1),
    _CmFlowStatsIndex_Type()
)
cmFlowStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIndex.setStatus("current")
_CmFlowStatsIntervalType_Type = CmPmIntervalType
_CmFlowStatsIntervalType_Object = MibTableColumn
cmFlowStatsIntervalType = _CmFlowStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 2),
    _CmFlowStatsIntervalType_Type()
)
cmFlowStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIntervalType.setStatus("current")
_CmFlowStatsValid_Type = TruthValue
_CmFlowStatsValid_Object = MibTableColumn
cmFlowStatsValid = _CmFlowStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 3),
    _CmFlowStatsValid_Type()
)
cmFlowStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsValid.setStatus("current")
_CmFlowStatsAction_Type = CmPmBinAction
_CmFlowStatsAction_Object = MibTableColumn
cmFlowStatsAction = _CmFlowStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 4),
    _CmFlowStatsAction_Type()
)
cmFlowStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlowStatsAction.setStatus("current")
_CmFlowStatsL2CPFD_Type = PerfCounter64
_CmFlowStatsL2CPFD_Object = MibTableColumn
cmFlowStatsL2CPFD = _CmFlowStatsL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 5),
    _CmFlowStatsL2CPFD_Type()
)
cmFlowStatsL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsL2CPFD.setStatus("current")
_CmFlowStatsABRA2N_Type = PerfCounter64
_CmFlowStatsABRA2N_Object = MibTableColumn
cmFlowStatsABRA2N = _CmFlowStatsABRA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 6),
    _CmFlowStatsABRA2N_Type()
)
cmFlowStatsABRA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsABRA2N.setStatus("current")
_CmFlowStatsABRRLA2N_Type = PerfCounter64
_CmFlowStatsABRRLA2N_Object = MibTableColumn
cmFlowStatsABRRLA2N = _CmFlowStatsABRRLA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 7),
    _CmFlowStatsABRRLA2N_Type()
)
cmFlowStatsABRRLA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsABRRLA2N.setStatus("current")
_CmFlowStatsABRRLRA2N_Type = PerfCounter64
_CmFlowStatsABRRLRA2N_Object = MibTableColumn
cmFlowStatsABRRLRA2N = _CmFlowStatsABRRLRA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 8),
    _CmFlowStatsABRRLRA2N_Type()
)
cmFlowStatsABRRLRA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsABRRLRA2N.setStatus("current")
_CmFlowStatsABRN2A_Type = PerfCounter64
_CmFlowStatsABRN2A_Object = MibTableColumn
cmFlowStatsABRN2A = _CmFlowStatsABRN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 9),
    _CmFlowStatsABRN2A_Type()
)
cmFlowStatsABRN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsABRN2A.setStatus("current")
_CmFlowStatsABRRLN2A_Type = PerfCounter64
_CmFlowStatsABRRLN2A_Object = MibTableColumn
cmFlowStatsABRRLN2A = _CmFlowStatsABRRLN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 10),
    _CmFlowStatsABRRLN2A_Type()
)
cmFlowStatsABRRLN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsABRRLN2A.setStatus("current")
_CmFlowStatsUAS_Type = PerfCounter64
_CmFlowStatsUAS_Object = MibTableColumn
cmFlowStatsUAS = _CmFlowStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 11),
    _CmFlowStatsUAS_Type()
)
cmFlowStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsUAS.setStatus("current")
_CmFlowStatsES_Type = PerfCounter64
_CmFlowStatsES_Object = MibTableColumn
cmFlowStatsES = _CmFlowStatsES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 12),
    _CmFlowStatsES_Type()
)
cmFlowStatsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsES.setStatus("current")
_CmFlowStatsSES_Type = PerfCounter64
_CmFlowStatsSES_Object = MibTableColumn
cmFlowStatsSES = _CmFlowStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 13),
    _CmFlowStatsSES_Type()
)
cmFlowStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsSES.setStatus("current")
_CmFlowStatsFMGA2N_Type = PerfCounter64
_CmFlowStatsFMGA2N_Object = MibTableColumn
cmFlowStatsFMGA2N = _CmFlowStatsFMGA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 14),
    _CmFlowStatsFMGA2N_Type()
)
cmFlowStatsFMGA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMGA2N.setStatus("current")
_CmFlowStatsFMYA2N_Type = PerfCounter64
_CmFlowStatsFMYA2N_Object = MibTableColumn
cmFlowStatsFMYA2N = _CmFlowStatsFMYA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 15),
    _CmFlowStatsFMYA2N_Type()
)
cmFlowStatsFMYA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMYA2N.setStatus("current")
_CmFlowStatsFMYDA2N_Type = PerfCounter64
_CmFlowStatsFMYDA2N_Object = MibTableColumn
cmFlowStatsFMYDA2N = _CmFlowStatsFMYDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 16),
    _CmFlowStatsFMYDA2N_Type()
)
cmFlowStatsFMYDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMYDA2N.setStatus("deprecated")
_CmFlowStatsFMRDA2N_Type = PerfCounter64
_CmFlowStatsFMRDA2N_Object = MibTableColumn
cmFlowStatsFMRDA2N = _CmFlowStatsFMRDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 17),
    _CmFlowStatsFMRDA2N_Type()
)
cmFlowStatsFMRDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMRDA2N.setStatus("current")
_CmFlowStatsBytesInA2N_Type = PerfCounter64
_CmFlowStatsBytesInA2N_Object = MibTableColumn
cmFlowStatsBytesInA2N = _CmFlowStatsBytesInA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 18),
    _CmFlowStatsBytesInA2N_Type()
)
cmFlowStatsBytesInA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsBytesInA2N.setStatus("current")
_CmFlowStatsBytesOutA2N_Type = PerfCounter64
_CmFlowStatsBytesOutA2N_Object = MibTableColumn
cmFlowStatsBytesOutA2N = _CmFlowStatsBytesOutA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 19),
    _CmFlowStatsBytesOutA2N_Type()
)
cmFlowStatsBytesOutA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsBytesOutA2N.setStatus("current")
_CmFlowStatsFMGN2A_Type = PerfCounter64
_CmFlowStatsFMGN2A_Object = MibTableColumn
cmFlowStatsFMGN2A = _CmFlowStatsFMGN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 20),
    _CmFlowStatsFMGN2A_Type()
)
cmFlowStatsFMGN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMGN2A.setStatus("current")
_CmFlowStatsFMYN2A_Type = PerfCounter64
_CmFlowStatsFMYN2A_Object = MibTableColumn
cmFlowStatsFMYN2A = _CmFlowStatsFMYN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 21),
    _CmFlowStatsFMYN2A_Type()
)
cmFlowStatsFMYN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMYN2A.setStatus("current")
_CmFlowStatsFMYDN2A_Type = PerfCounter64
_CmFlowStatsFMYDN2A_Object = MibTableColumn
cmFlowStatsFMYDN2A = _CmFlowStatsFMYDN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 22),
    _CmFlowStatsFMYDN2A_Type()
)
cmFlowStatsFMYDN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMYDN2A.setStatus("deprecated")
_CmFlowStatsFMRDN2A_Type = PerfCounter64
_CmFlowStatsFMRDN2A_Object = MibTableColumn
cmFlowStatsFMRDN2A = _CmFlowStatsFMRDN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 23),
    _CmFlowStatsFMRDN2A_Type()
)
cmFlowStatsFMRDN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMRDN2A.setStatus("current")
_CmFlowStatsBytesInN2A_Type = PerfCounter64
_CmFlowStatsBytesInN2A_Object = MibTableColumn
cmFlowStatsBytesInN2A = _CmFlowStatsBytesInN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 24),
    _CmFlowStatsBytesInN2A_Type()
)
cmFlowStatsBytesInN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsBytesInN2A.setStatus("current")
_CmFlowStatsBytesOutN2A_Type = PerfCounter64
_CmFlowStatsBytesOutN2A_Object = MibTableColumn
cmFlowStatsBytesOutN2A = _CmFlowStatsBytesOutN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 25),
    _CmFlowStatsBytesOutN2A_Type()
)
cmFlowStatsBytesOutN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsBytesOutN2A.setStatus("current")
_CmFlowStatsFTDA2N_Type = PerfCounter64
_CmFlowStatsFTDA2N_Object = MibTableColumn
cmFlowStatsFTDA2N = _CmFlowStatsFTDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 26),
    _CmFlowStatsFTDA2N_Type()
)
cmFlowStatsFTDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFTDA2N.setStatus("current")
_CmFlowStatsIBRA2NMax_Type = PerfCounter64
_CmFlowStatsIBRA2NMax_Object = MibTableColumn
cmFlowStatsIBRA2NMax = _CmFlowStatsIBRA2NMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 27),
    _CmFlowStatsIBRA2NMax_Type()
)
cmFlowStatsIBRA2NMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRA2NMax.setStatus("current")
_CmFlowStatsIBRRlA2NMax_Type = PerfCounter64
_CmFlowStatsIBRRlA2NMax_Object = MibTableColumn
cmFlowStatsIBRRlA2NMax = _CmFlowStatsIBRRlA2NMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 28),
    _CmFlowStatsIBRRlA2NMax_Type()
)
cmFlowStatsIBRRlA2NMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRRlA2NMax.setStatus("current")
_CmFlowStatsIBRA2NMin_Type = PerfCounter64
_CmFlowStatsIBRA2NMin_Object = MibTableColumn
cmFlowStatsIBRA2NMin = _CmFlowStatsIBRA2NMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 29),
    _CmFlowStatsIBRA2NMin_Type()
)
cmFlowStatsIBRA2NMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRA2NMin.setStatus("current")
_CmFlowStatsIBRRlA2NMin_Type = PerfCounter64
_CmFlowStatsIBRRlA2NMin_Object = MibTableColumn
cmFlowStatsIBRRlA2NMin = _CmFlowStatsIBRRlA2NMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 30),
    _CmFlowStatsIBRRlA2NMin_Type()
)
cmFlowStatsIBRRlA2NMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRRlA2NMin.setStatus("current")
_CmFlowStatsIBRA2N_Type = PerfCounter64
_CmFlowStatsIBRA2N_Object = MibTableColumn
cmFlowStatsIBRA2N = _CmFlowStatsIBRA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 31),
    _CmFlowStatsIBRA2N_Type()
)
cmFlowStatsIBRA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRA2N.setStatus("current")
_CmFlowStatsIBRRlA2N_Type = PerfCounter64
_CmFlowStatsIBRRlA2N_Object = MibTableColumn
cmFlowStatsIBRRlA2N = _CmFlowStatsIBRRlA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 32),
    _CmFlowStatsIBRRlA2N_Type()
)
cmFlowStatsIBRRlA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRRlA2N.setStatus("current")
_CmFlowStatsIBRN2AMax_Type = PerfCounter64
_CmFlowStatsIBRN2AMax_Object = MibTableColumn
cmFlowStatsIBRN2AMax = _CmFlowStatsIBRN2AMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 33),
    _CmFlowStatsIBRN2AMax_Type()
)
cmFlowStatsIBRN2AMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRN2AMax.setStatus("current")
_CmFlowStatsIBRRlN2AMax_Type = PerfCounter64
_CmFlowStatsIBRRlN2AMax_Object = MibTableColumn
cmFlowStatsIBRRlN2AMax = _CmFlowStatsIBRRlN2AMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 34),
    _CmFlowStatsIBRRlN2AMax_Type()
)
cmFlowStatsIBRRlN2AMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRRlN2AMax.setStatus("current")
_CmFlowStatsIBRN2AMin_Type = PerfCounter64
_CmFlowStatsIBRN2AMin_Object = MibTableColumn
cmFlowStatsIBRN2AMin = _CmFlowStatsIBRN2AMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 35),
    _CmFlowStatsIBRN2AMin_Type()
)
cmFlowStatsIBRN2AMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRN2AMin.setStatus("current")
_CmFlowStatsIBRRlN2AMin_Type = PerfCounter64
_CmFlowStatsIBRRlN2AMin_Object = MibTableColumn
cmFlowStatsIBRRlN2AMin = _CmFlowStatsIBRRlN2AMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 36),
    _CmFlowStatsIBRRlN2AMin_Type()
)
cmFlowStatsIBRRlN2AMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRRlN2AMin.setStatus("current")
_CmFlowStatsIBRN2A_Type = PerfCounter64
_CmFlowStatsIBRN2A_Object = MibTableColumn
cmFlowStatsIBRN2A = _CmFlowStatsIBRN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 37),
    _CmFlowStatsIBRN2A_Type()
)
cmFlowStatsIBRN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRN2A.setStatus("current")
_CmFlowStatsIBRRlN2A_Type = PerfCounter64
_CmFlowStatsIBRRlN2A_Object = MibTableColumn
cmFlowStatsIBRRlN2A = _CmFlowStatsIBRRlN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 38),
    _CmFlowStatsIBRRlN2A_Type()
)
cmFlowStatsIBRRlN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsIBRRlN2A.setStatus("current")
_CmFlowStatsFMCDA2N_Type = PerfCounter64
_CmFlowStatsFMCDA2N_Object = MibTableColumn
cmFlowStatsFMCDA2N = _CmFlowStatsFMCDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 39),
    _CmFlowStatsFMCDA2N_Type()
)
cmFlowStatsFMCDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFMCDA2N.setStatus("current")
_CmFlowStatsFBCDA2N_Type = PerfCounter64
_CmFlowStatsFBCDA2N_Object = MibTableColumn
cmFlowStatsFBCDA2N = _CmFlowStatsFBCDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 40),
    _CmFlowStatsFBCDA2N_Type()
)
cmFlowStatsFBCDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsFBCDA2N.setStatus("current")
_CmFlowStatsACLN2ADrop_Type = PerfCounter64
_CmFlowStatsACLN2ADrop_Object = MibTableColumn
cmFlowStatsACLN2ADrop = _CmFlowStatsACLN2ADrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 41),
    _CmFlowStatsACLN2ADrop_Type()
)
cmFlowStatsACLN2ADrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsACLN2ADrop.setStatus("current")
_CmFlowStatsACLA2NDrop_Type = PerfCounter64
_CmFlowStatsACLA2NDrop_Object = MibTableColumn
cmFlowStatsACLA2NDrop = _CmFlowStatsACLA2NDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 9, 1, 42),
    _CmFlowStatsACLA2NDrop_Type()
)
cmFlowStatsACLA2NDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowStatsACLA2NDrop.setStatus("current")
_CmFlowHistoryTable_Object = MibTable
cmFlowHistoryTable = _CmFlowHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10)
)
if mibBuilder.loadTexts:
    cmFlowHistoryTable.setStatus("current")
_CmFlowHistoryEntry_Object = MibTableRow
cmFlowHistoryEntry = _CmFlowHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1)
)
cmFlowHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmFlowHistoryEntry.setStatus("current")


class _CmFlowHistoryIndex_Type(Integer32):
    """Custom type cmFlowHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmFlowHistoryIndex_Type.__name__ = "Integer32"
_CmFlowHistoryIndex_Object = MibTableColumn
cmFlowHistoryIndex = _CmFlowHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 1),
    _CmFlowHistoryIndex_Type()
)
cmFlowHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIndex.setStatus("current")
_CmFlowHistoryTime_Type = DateAndTime
_CmFlowHistoryTime_Object = MibTableColumn
cmFlowHistoryTime = _CmFlowHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 2),
    _CmFlowHistoryTime_Type()
)
cmFlowHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryTime.setStatus("current")
_CmFlowHistoryValid_Type = TruthValue
_CmFlowHistoryValid_Object = MibTableColumn
cmFlowHistoryValid = _CmFlowHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 3),
    _CmFlowHistoryValid_Type()
)
cmFlowHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryValid.setStatus("current")
_CmFlowHistoryAction_Type = CmPmBinAction
_CmFlowHistoryAction_Object = MibTableColumn
cmFlowHistoryAction = _CmFlowHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 4),
    _CmFlowHistoryAction_Type()
)
cmFlowHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlowHistoryAction.setStatus("current")
_CmFlowHistoryL2CPFD_Type = PerfCounter64
_CmFlowHistoryL2CPFD_Object = MibTableColumn
cmFlowHistoryL2CPFD = _CmFlowHistoryL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 5),
    _CmFlowHistoryL2CPFD_Type()
)
cmFlowHistoryL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryL2CPFD.setStatus("current")
_CmFlowHistoryABRA2N_Type = PerfCounter64
_CmFlowHistoryABRA2N_Object = MibTableColumn
cmFlowHistoryABRA2N = _CmFlowHistoryABRA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 6),
    _CmFlowHistoryABRA2N_Type()
)
cmFlowHistoryABRA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryABRA2N.setStatus("current")
_CmFlowHistoryABRRLA2N_Type = PerfCounter64
_CmFlowHistoryABRRLA2N_Object = MibTableColumn
cmFlowHistoryABRRLA2N = _CmFlowHistoryABRRLA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 7),
    _CmFlowHistoryABRRLA2N_Type()
)
cmFlowHistoryABRRLA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryABRRLA2N.setStatus("current")
_CmFlowHistoryABRRLRA2N_Type = PerfCounter64
_CmFlowHistoryABRRLRA2N_Object = MibTableColumn
cmFlowHistoryABRRLRA2N = _CmFlowHistoryABRRLRA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 8),
    _CmFlowHistoryABRRLRA2N_Type()
)
cmFlowHistoryABRRLRA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryABRRLRA2N.setStatus("current")
_CmFlowHistoryABRN2A_Type = PerfCounter64
_CmFlowHistoryABRN2A_Object = MibTableColumn
cmFlowHistoryABRN2A = _CmFlowHistoryABRN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 9),
    _CmFlowHistoryABRN2A_Type()
)
cmFlowHistoryABRN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryABRN2A.setStatus("current")
_CmFlowHistoryABRRLN2A_Type = PerfCounter64
_CmFlowHistoryABRRLN2A_Object = MibTableColumn
cmFlowHistoryABRRLN2A = _CmFlowHistoryABRRLN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 10),
    _CmFlowHistoryABRRLN2A_Type()
)
cmFlowHistoryABRRLN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryABRRLN2A.setStatus("current")
_CmFlowHistoryUAS_Type = PerfCounter64
_CmFlowHistoryUAS_Object = MibTableColumn
cmFlowHistoryUAS = _CmFlowHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 11),
    _CmFlowHistoryUAS_Type()
)
cmFlowHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryUAS.setStatus("current")
_CmFlowHistoryES_Type = PerfCounter64
_CmFlowHistoryES_Object = MibTableColumn
cmFlowHistoryES = _CmFlowHistoryES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 12),
    _CmFlowHistoryES_Type()
)
cmFlowHistoryES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryES.setStatus("current")
_CmFlowHistorySES_Type = PerfCounter64
_CmFlowHistorySES_Object = MibTableColumn
cmFlowHistorySES = _CmFlowHistorySES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 13),
    _CmFlowHistorySES_Type()
)
cmFlowHistorySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistorySES.setStatus("current")
_CmFlowHistoryFMGA2N_Type = PerfCounter64
_CmFlowHistoryFMGA2N_Object = MibTableColumn
cmFlowHistoryFMGA2N = _CmFlowHistoryFMGA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 14),
    _CmFlowHistoryFMGA2N_Type()
)
cmFlowHistoryFMGA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMGA2N.setStatus("current")
_CmFlowHistoryFMYA2N_Type = PerfCounter64
_CmFlowHistoryFMYA2N_Object = MibTableColumn
cmFlowHistoryFMYA2N = _CmFlowHistoryFMYA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 15),
    _CmFlowHistoryFMYA2N_Type()
)
cmFlowHistoryFMYA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMYA2N.setStatus("current")
_CmFlowHistoryFMYDA2N_Type = PerfCounter64
_CmFlowHistoryFMYDA2N_Object = MibTableColumn
cmFlowHistoryFMYDA2N = _CmFlowHistoryFMYDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 16),
    _CmFlowHistoryFMYDA2N_Type()
)
cmFlowHistoryFMYDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMYDA2N.setStatus("deprecated")
_CmFlowHistoryFMRDA2N_Type = PerfCounter64
_CmFlowHistoryFMRDA2N_Object = MibTableColumn
cmFlowHistoryFMRDA2N = _CmFlowHistoryFMRDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 17),
    _CmFlowHistoryFMRDA2N_Type()
)
cmFlowHistoryFMRDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMRDA2N.setStatus("current")
_CmFlowHistoryBytesInA2N_Type = PerfCounter64
_CmFlowHistoryBytesInA2N_Object = MibTableColumn
cmFlowHistoryBytesInA2N = _CmFlowHistoryBytesInA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 18),
    _CmFlowHistoryBytesInA2N_Type()
)
cmFlowHistoryBytesInA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryBytesInA2N.setStatus("current")
_CmFlowHistoryBytesOutA2N_Type = PerfCounter64
_CmFlowHistoryBytesOutA2N_Object = MibTableColumn
cmFlowHistoryBytesOutA2N = _CmFlowHistoryBytesOutA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 19),
    _CmFlowHistoryBytesOutA2N_Type()
)
cmFlowHistoryBytesOutA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryBytesOutA2N.setStatus("current")
_CmFlowHistoryFMGN2A_Type = PerfCounter64
_CmFlowHistoryFMGN2A_Object = MibTableColumn
cmFlowHistoryFMGN2A = _CmFlowHistoryFMGN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 20),
    _CmFlowHistoryFMGN2A_Type()
)
cmFlowHistoryFMGN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMGN2A.setStatus("current")
_CmFlowHistoryFMYN2A_Type = PerfCounter64
_CmFlowHistoryFMYN2A_Object = MibTableColumn
cmFlowHistoryFMYN2A = _CmFlowHistoryFMYN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 21),
    _CmFlowHistoryFMYN2A_Type()
)
cmFlowHistoryFMYN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMYN2A.setStatus("current")
_CmFlowHistoryFMYDN2A_Type = PerfCounter64
_CmFlowHistoryFMYDN2A_Object = MibTableColumn
cmFlowHistoryFMYDN2A = _CmFlowHistoryFMYDN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 22),
    _CmFlowHistoryFMYDN2A_Type()
)
cmFlowHistoryFMYDN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMYDN2A.setStatus("deprecated")
_CmFlowHistoryFMRDN2A_Type = PerfCounter64
_CmFlowHistoryFMRDN2A_Object = MibTableColumn
cmFlowHistoryFMRDN2A = _CmFlowHistoryFMRDN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 23),
    _CmFlowHistoryFMRDN2A_Type()
)
cmFlowHistoryFMRDN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMRDN2A.setStatus("current")
_CmFlowHistoryBytesInN2A_Type = PerfCounter64
_CmFlowHistoryBytesInN2A_Object = MibTableColumn
cmFlowHistoryBytesInN2A = _CmFlowHistoryBytesInN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 24),
    _CmFlowHistoryBytesInN2A_Type()
)
cmFlowHistoryBytesInN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryBytesInN2A.setStatus("current")
_CmFlowHistoryBytesOutN2A_Type = PerfCounter64
_CmFlowHistoryBytesOutN2A_Object = MibTableColumn
cmFlowHistoryBytesOutN2A = _CmFlowHistoryBytesOutN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 25),
    _CmFlowHistoryBytesOutN2A_Type()
)
cmFlowHistoryBytesOutN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryBytesOutN2A.setStatus("current")
_CmFlowHistoryFTDA2N_Type = PerfCounter64
_CmFlowHistoryFTDA2N_Object = MibTableColumn
cmFlowHistoryFTDA2N = _CmFlowHistoryFTDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 26),
    _CmFlowHistoryFTDA2N_Type()
)
cmFlowHistoryFTDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFTDA2N.setStatus("current")
_CmFlowHistoryIBRA2NMax_Type = PerfCounter64
_CmFlowHistoryIBRA2NMax_Object = MibTableColumn
cmFlowHistoryIBRA2NMax = _CmFlowHistoryIBRA2NMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 27),
    _CmFlowHistoryIBRA2NMax_Type()
)
cmFlowHistoryIBRA2NMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRA2NMax.setStatus("current")
_CmFlowHistoryIBRRlA2NMax_Type = PerfCounter64
_CmFlowHistoryIBRRlA2NMax_Object = MibTableColumn
cmFlowHistoryIBRRlA2NMax = _CmFlowHistoryIBRRlA2NMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 28),
    _CmFlowHistoryIBRRlA2NMax_Type()
)
cmFlowHistoryIBRRlA2NMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRRlA2NMax.setStatus("current")
_CmFlowHistoryIBRA2NMin_Type = PerfCounter64
_CmFlowHistoryIBRA2NMin_Object = MibTableColumn
cmFlowHistoryIBRA2NMin = _CmFlowHistoryIBRA2NMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 29),
    _CmFlowHistoryIBRA2NMin_Type()
)
cmFlowHistoryIBRA2NMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRA2NMin.setStatus("current")
_CmFlowHistoryIBRRlA2NMin_Type = PerfCounter64
_CmFlowHistoryIBRRlA2NMin_Object = MibTableColumn
cmFlowHistoryIBRRlA2NMin = _CmFlowHistoryIBRRlA2NMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 30),
    _CmFlowHistoryIBRRlA2NMin_Type()
)
cmFlowHistoryIBRRlA2NMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRRlA2NMin.setStatus("current")
_CmFlowHistoryIBRA2N_Type = PerfCounter64
_CmFlowHistoryIBRA2N_Object = MibTableColumn
cmFlowHistoryIBRA2N = _CmFlowHistoryIBRA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 31),
    _CmFlowHistoryIBRA2N_Type()
)
cmFlowHistoryIBRA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRA2N.setStatus("current")
_CmFlowHistoryIBRRlA2N_Type = PerfCounter64
_CmFlowHistoryIBRRlA2N_Object = MibTableColumn
cmFlowHistoryIBRRlA2N = _CmFlowHistoryIBRRlA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 32),
    _CmFlowHistoryIBRRlA2N_Type()
)
cmFlowHistoryIBRRlA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRRlA2N.setStatus("current")
_CmFlowHistoryIBRN2AMax_Type = PerfCounter64
_CmFlowHistoryIBRN2AMax_Object = MibTableColumn
cmFlowHistoryIBRN2AMax = _CmFlowHistoryIBRN2AMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 33),
    _CmFlowHistoryIBRN2AMax_Type()
)
cmFlowHistoryIBRN2AMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRN2AMax.setStatus("current")
_CmFlowHistoryIBRRlN2AMax_Type = PerfCounter64
_CmFlowHistoryIBRRlN2AMax_Object = MibTableColumn
cmFlowHistoryIBRRlN2AMax = _CmFlowHistoryIBRRlN2AMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 34),
    _CmFlowHistoryIBRRlN2AMax_Type()
)
cmFlowHistoryIBRRlN2AMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRRlN2AMax.setStatus("current")
_CmFlowHistoryIBRN2AMin_Type = PerfCounter64
_CmFlowHistoryIBRN2AMin_Object = MibTableColumn
cmFlowHistoryIBRN2AMin = _CmFlowHistoryIBRN2AMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 35),
    _CmFlowHistoryIBRN2AMin_Type()
)
cmFlowHistoryIBRN2AMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRN2AMin.setStatus("current")
_CmFlowHistoryIBRRlN2AMin_Type = PerfCounter64
_CmFlowHistoryIBRRlN2AMin_Object = MibTableColumn
cmFlowHistoryIBRRlN2AMin = _CmFlowHistoryIBRRlN2AMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 36),
    _CmFlowHistoryIBRRlN2AMin_Type()
)
cmFlowHistoryIBRRlN2AMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRRlN2AMin.setStatus("current")
_CmFlowHistoryIBRN2A_Type = PerfCounter64
_CmFlowHistoryIBRN2A_Object = MibTableColumn
cmFlowHistoryIBRN2A = _CmFlowHistoryIBRN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 37),
    _CmFlowHistoryIBRN2A_Type()
)
cmFlowHistoryIBRN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRN2A.setStatus("current")
_CmFlowHistoryIBRRlN2A_Type = PerfCounter64
_CmFlowHistoryIBRRlN2A_Object = MibTableColumn
cmFlowHistoryIBRRlN2A = _CmFlowHistoryIBRRlN2A_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 38),
    _CmFlowHistoryIBRRlN2A_Type()
)
cmFlowHistoryIBRRlN2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryIBRRlN2A.setStatus("current")
_CmFlowHistoryFMCDA2N_Type = PerfCounter64
_CmFlowHistoryFMCDA2N_Object = MibTableColumn
cmFlowHistoryFMCDA2N = _CmFlowHistoryFMCDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 39),
    _CmFlowHistoryFMCDA2N_Type()
)
cmFlowHistoryFMCDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFMCDA2N.setStatus("current")
_CmFlowHistoryFBCDA2N_Type = PerfCounter64
_CmFlowHistoryFBCDA2N_Object = MibTableColumn
cmFlowHistoryFBCDA2N = _CmFlowHistoryFBCDA2N_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 40),
    _CmFlowHistoryFBCDA2N_Type()
)
cmFlowHistoryFBCDA2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryFBCDA2N.setStatus("current")
_CmFlowHistoryACLN2ADrop_Type = PerfCounter64
_CmFlowHistoryACLN2ADrop_Object = MibTableColumn
cmFlowHistoryACLN2ADrop = _CmFlowHistoryACLN2ADrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 41),
    _CmFlowHistoryACLN2ADrop_Type()
)
cmFlowHistoryACLN2ADrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryACLN2ADrop.setStatus("current")
_CmFlowHistoryACLA2NDrop_Type = PerfCounter64
_CmFlowHistoryACLA2NDrop_Object = MibTableColumn
cmFlowHistoryACLA2NDrop = _CmFlowHistoryACLA2NDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 10, 1, 42),
    _CmFlowHistoryACLA2NDrop_Type()
)
cmFlowHistoryACLA2NDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowHistoryACLA2NDrop.setStatus("current")
_CmFlowThresholdTable_Object = MibTable
cmFlowThresholdTable = _CmFlowThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 11)
)
if mibBuilder.loadTexts:
    cmFlowThresholdTable.setStatus("current")
_CmFlowThresholdEntry_Object = MibTableRow
cmFlowThresholdEntry = _CmFlowThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 11, 1)
)
cmFlowThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmFlowThresholdEntry.setStatus("current")


class _CmFlowThresholdIndex_Type(Integer32):
    """Custom type cmFlowThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmFlowThresholdIndex_Type.__name__ = "Integer32"
_CmFlowThresholdIndex_Object = MibTableColumn
cmFlowThresholdIndex = _CmFlowThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 11, 1, 1),
    _CmFlowThresholdIndex_Type()
)
cmFlowThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowThresholdIndex.setStatus("current")
_CmFlowThresholdInterval_Type = CmPmIntervalType
_CmFlowThresholdInterval_Object = MibTableColumn
cmFlowThresholdInterval = _CmFlowThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 11, 1, 2),
    _CmFlowThresholdInterval_Type()
)
cmFlowThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowThresholdInterval.setStatus("current")
_CmFlowThresholdVariable_Type = VariablePointer
_CmFlowThresholdVariable_Object = MibTableColumn
cmFlowThresholdVariable = _CmFlowThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 11, 1, 3),
    _CmFlowThresholdVariable_Type()
)
cmFlowThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowThresholdVariable.setStatus("current")
_CmFlowThresholdValueLo_Type = Unsigned32
_CmFlowThresholdValueLo_Object = MibTableColumn
cmFlowThresholdValueLo = _CmFlowThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 11, 1, 4),
    _CmFlowThresholdValueLo_Type()
)
cmFlowThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlowThresholdValueLo.setStatus("current")
_CmFlowThresholdValueHi_Type = Unsigned32
_CmFlowThresholdValueHi_Object = MibTableColumn
cmFlowThresholdValueHi = _CmFlowThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 11, 1, 5),
    _CmFlowThresholdValueHi_Type()
)
cmFlowThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlowThresholdValueHi.setStatus("current")
_CmFlowThresholdMonValue_Type = Counter64
_CmFlowThresholdMonValue_Object = MibTableColumn
cmFlowThresholdMonValue = _CmFlowThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 11, 1, 6),
    _CmFlowThresholdMonValue_Type()
)
cmFlowThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowThresholdMonValue.setStatus("current")
_CmQosShaperStatsTable_Object = MibTable
cmQosShaperStatsTable = _CmQosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12)
)
if mibBuilder.loadTexts:
    cmQosShaperStatsTable.setStatus("current")
_CmQosShaperStatsEntry_Object = MibTableRow
cmQosShaperStatsEntry = _CmQosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1)
)
cmQosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperTypeIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    cmQosShaperStatsEntry.setStatus("current")


class _CmQosShaperStatsIndex_Type(Integer32):
    """Custom type cmQosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosShaperStatsIndex_Type.__name__ = "Integer32"
_CmQosShaperStatsIndex_Object = MibTableColumn
cmQosShaperStatsIndex = _CmQosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 1),
    _CmQosShaperStatsIndex_Type()
)
cmQosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsIndex.setStatus("current")
_CmQosShaperStatsIntervalType_Type = CmPmIntervalType
_CmQosShaperStatsIntervalType_Object = MibTableColumn
cmQosShaperStatsIntervalType = _CmQosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 2),
    _CmQosShaperStatsIntervalType_Type()
)
cmQosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsIntervalType.setStatus("current")
_CmQosShaperStatsValid_Type = TruthValue
_CmQosShaperStatsValid_Object = MibTableColumn
cmQosShaperStatsValid = _CmQosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 3),
    _CmQosShaperStatsValid_Type()
)
cmQosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsValid.setStatus("current")
_CmQosShaperStatsAction_Type = CmPmBinAction
_CmQosShaperStatsAction_Object = MibTableColumn
cmQosShaperStatsAction = _CmQosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 4),
    _CmQosShaperStatsAction_Type()
)
cmQosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosShaperStatsAction.setStatus("current")
_CmQosShaperStatsBT_Type = PerfCounter64
_CmQosShaperStatsBT_Object = MibTableColumn
cmQosShaperStatsBT = _CmQosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 5),
    _CmQosShaperStatsBT_Type()
)
cmQosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsBT.setStatus("current")
_CmQosShaperStatsBTD_Type = PerfCounter64
_CmQosShaperStatsBTD_Object = MibTableColumn
cmQosShaperStatsBTD = _CmQosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 6),
    _CmQosShaperStatsBTD_Type()
)
cmQosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsBTD.setStatus("current")
_CmQosShaperStatsFD_Type = PerfCounter64
_CmQosShaperStatsFD_Object = MibTableColumn
cmQosShaperStatsFD = _CmQosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 7),
    _CmQosShaperStatsFD_Type()
)
cmQosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsFD.setStatus("current")
_CmQosShaperStatsFTD_Type = PerfCounter64
_CmQosShaperStatsFTD_Object = MibTableColumn
cmQosShaperStatsFTD = _CmQosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 8),
    _CmQosShaperStatsFTD_Type()
)
cmQosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsFTD.setStatus("current")
_CmQosShaperStatsBR_Type = PerfCounter64
_CmQosShaperStatsBR_Object = MibTableColumn
cmQosShaperStatsBR = _CmQosShaperStatsBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 9),
    _CmQosShaperStatsBR_Type()
)
cmQosShaperStatsBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsBR.setStatus("current")
_CmQosShaperStatsFR_Type = PerfCounter64
_CmQosShaperStatsFR_Object = MibTableColumn
cmQosShaperStatsFR = _CmQosShaperStatsFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 10),
    _CmQosShaperStatsFR_Type()
)
cmQosShaperStatsFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsFR.setStatus("current")
_CmQosShaperStatsABRRL_Type = PerfCounter64
_CmQosShaperStatsABRRL_Object = MibTableColumn
cmQosShaperStatsABRRL = _CmQosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 11),
    _CmQosShaperStatsABRRL_Type()
)
cmQosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsABRRL.setStatus("current")
_CmQosShaperStatsABRRLR_Type = PerfCounter64
_CmQosShaperStatsABRRLR_Object = MibTableColumn
cmQosShaperStatsABRRLR = _CmQosShaperStatsABRRLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 12),
    _CmQosShaperStatsABRRLR_Type()
)
cmQosShaperStatsABRRLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsABRRLR.setStatus("current")
_CmQosShaperStatsBREDD_Type = PerfCounter64
_CmQosShaperStatsBREDD_Object = MibTableColumn
cmQosShaperStatsBREDD = _CmQosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 13),
    _CmQosShaperStatsBREDD_Type()
)
cmQosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsBREDD.setStatus("current")
_CmQosShaperStatsFREDD_Type = PerfCounter64
_CmQosShaperStatsFREDD_Object = MibTableColumn
cmQosShaperStatsFREDD = _CmQosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 12, 1, 14),
    _CmQosShaperStatsFREDD_Type()
)
cmQosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperStatsFREDD.setStatus("current")
_CmQosShaperHistoryTable_Object = MibTable
cmQosShaperHistoryTable = _CmQosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13)
)
if mibBuilder.loadTexts:
    cmQosShaperHistoryTable.setStatus("current")
_CmQosShaperHistoryEntry_Object = MibTableRow
cmQosShaperHistoryEntry = _CmQosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1)
)
cmQosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperTypeIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmQosShaperHistoryEntry.setStatus("current")


class _CmQosShaperHistoryIndex_Type(Integer32):
    """Custom type cmQosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosShaperHistoryIndex_Type.__name__ = "Integer32"
_CmQosShaperHistoryIndex_Object = MibTableColumn
cmQosShaperHistoryIndex = _CmQosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 1),
    _CmQosShaperHistoryIndex_Type()
)
cmQosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryIndex.setStatus("current")
_CmQosShaperHistoryTime_Type = DateAndTime
_CmQosShaperHistoryTime_Object = MibTableColumn
cmQosShaperHistoryTime = _CmQosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 2),
    _CmQosShaperHistoryTime_Type()
)
cmQosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryTime.setStatus("current")
_CmQosShaperHistoryValid_Type = TruthValue
_CmQosShaperHistoryValid_Object = MibTableColumn
cmQosShaperHistoryValid = _CmQosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 3),
    _CmQosShaperHistoryValid_Type()
)
cmQosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryValid.setStatus("current")
_CmQosShaperHistoryAction_Type = CmPmBinAction
_CmQosShaperHistoryAction_Object = MibTableColumn
cmQosShaperHistoryAction = _CmQosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 4),
    _CmQosShaperHistoryAction_Type()
)
cmQosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosShaperHistoryAction.setStatus("current")
_CmQosShaperHistoryBT_Type = PerfCounter64
_CmQosShaperHistoryBT_Object = MibTableColumn
cmQosShaperHistoryBT = _CmQosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 5),
    _CmQosShaperHistoryBT_Type()
)
cmQosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryBT.setStatus("current")
_CmQosShaperHistoryBTD_Type = PerfCounter64
_CmQosShaperHistoryBTD_Object = MibTableColumn
cmQosShaperHistoryBTD = _CmQosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 6),
    _CmQosShaperHistoryBTD_Type()
)
cmQosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryBTD.setStatus("current")
_CmQosShaperHistoryFD_Type = PerfCounter64
_CmQosShaperHistoryFD_Object = MibTableColumn
cmQosShaperHistoryFD = _CmQosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 7),
    _CmQosShaperHistoryFD_Type()
)
cmQosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryFD.setStatus("current")
_CmQosShaperHistoryFTD_Type = PerfCounter64
_CmQosShaperHistoryFTD_Object = MibTableColumn
cmQosShaperHistoryFTD = _CmQosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 8),
    _CmQosShaperHistoryFTD_Type()
)
cmQosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryFTD.setStatus("current")
_CmQosShaperHistoryBR_Type = PerfCounter64
_CmQosShaperHistoryBR_Object = MibTableColumn
cmQosShaperHistoryBR = _CmQosShaperHistoryBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 9),
    _CmQosShaperHistoryBR_Type()
)
cmQosShaperHistoryBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryBR.setStatus("current")
_CmQosShaperHistoryFR_Type = PerfCounter64
_CmQosShaperHistoryFR_Object = MibTableColumn
cmQosShaperHistoryFR = _CmQosShaperHistoryFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 10),
    _CmQosShaperHistoryFR_Type()
)
cmQosShaperHistoryFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryFR.setStatus("current")
_CmQosShaperHistoryABRRL_Type = PerfCounter64
_CmQosShaperHistoryABRRL_Object = MibTableColumn
cmQosShaperHistoryABRRL = _CmQosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 11),
    _CmQosShaperHistoryABRRL_Type()
)
cmQosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryABRRL.setStatus("current")
_CmQosShaperHistoryABRRLR_Type = PerfCounter64
_CmQosShaperHistoryABRRLR_Object = MibTableColumn
cmQosShaperHistoryABRRLR = _CmQosShaperHistoryABRRLR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 12),
    _CmQosShaperHistoryABRRLR_Type()
)
cmQosShaperHistoryABRRLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryABRRLR.setStatus("current")
_CmQosShaperHistoryBREDD_Type = PerfCounter64
_CmQosShaperHistoryBREDD_Object = MibTableColumn
cmQosShaperHistoryBREDD = _CmQosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 13),
    _CmQosShaperHistoryBREDD_Type()
)
cmQosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryBREDD.setStatus("current")
_CmQosShaperHistoryFREDD_Type = PerfCounter64
_CmQosShaperHistoryFREDD_Object = MibTableColumn
cmQosShaperHistoryFREDD = _CmQosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 13, 1, 14),
    _CmQosShaperHistoryFREDD_Type()
)
cmQosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperHistoryFREDD.setStatus("current")
_CmQosShaperThresholdTable_Object = MibTable
cmQosShaperThresholdTable = _CmQosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 14)
)
if mibBuilder.loadTexts:
    cmQosShaperThresholdTable.setStatus("current")
_CmQosShaperThresholdEntry_Object = MibTableRow
cmQosShaperThresholdEntry = _CmQosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 14, 1)
)
cmQosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperTypeIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmQosShaperThresholdEntry.setStatus("current")


class _CmQosShaperThresholdIndex_Type(Integer32):
    """Custom type cmQosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosShaperThresholdIndex_Type.__name__ = "Integer32"
_CmQosShaperThresholdIndex_Object = MibTableColumn
cmQosShaperThresholdIndex = _CmQosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 14, 1, 1),
    _CmQosShaperThresholdIndex_Type()
)
cmQosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperThresholdIndex.setStatus("current")
_CmQosShaperThresholdInterval_Type = CmPmIntervalType
_CmQosShaperThresholdInterval_Object = MibTableColumn
cmQosShaperThresholdInterval = _CmQosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 14, 1, 2),
    _CmQosShaperThresholdInterval_Type()
)
cmQosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperThresholdInterval.setStatus("current")
_CmQosShaperThresholdVariable_Type = VariablePointer
_CmQosShaperThresholdVariable_Object = MibTableColumn
cmQosShaperThresholdVariable = _CmQosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 14, 1, 3),
    _CmQosShaperThresholdVariable_Type()
)
cmQosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperThresholdVariable.setStatus("current")
_CmQosShaperThresholdValueLo_Type = Unsigned32
_CmQosShaperThresholdValueLo_Object = MibTableColumn
cmQosShaperThresholdValueLo = _CmQosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 14, 1, 4),
    _CmQosShaperThresholdValueLo_Type()
)
cmQosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosShaperThresholdValueLo.setStatus("current")
_CmQosShaperThresholdValueHi_Type = Unsigned32
_CmQosShaperThresholdValueHi_Object = MibTableColumn
cmQosShaperThresholdValueHi = _CmQosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 14, 1, 5),
    _CmQosShaperThresholdValueHi_Type()
)
cmQosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosShaperThresholdValueHi.setStatus("current")
_CmQosShaperThresholdMonValue_Type = Counter64
_CmQosShaperThresholdMonValue_Object = MibTableColumn
cmQosShaperThresholdMonValue = _CmQosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 14, 1, 6),
    _CmQosShaperThresholdMonValue_Type()
)
cmQosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperThresholdMonValue.setStatus("current")
_CmQosFlowPolicerStatsTable_Object = MibTable
cmQosFlowPolicerStatsTable = _CmQosFlowPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15)
)
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsTable.setStatus("current")
_CmQosFlowPolicerStatsEntry_Object = MibTableRow
cmQosFlowPolicerStatsEntry = _CmQosFlowPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1)
)
cmQosFlowPolicerStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-FACILITY-MIB", "cmQosFlowPolicerTypeIndex"),
    (0, "CM-FACILITY-MIB", "cmQosFlowPolicerIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsIndex"),
)
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsEntry.setStatus("current")


class _CmQosFlowPolicerStatsIndex_Type(Integer32):
    """Custom type cmQosFlowPolicerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosFlowPolicerStatsIndex_Type.__name__ = "Integer32"
_CmQosFlowPolicerStatsIndex_Object = MibTableColumn
cmQosFlowPolicerStatsIndex = _CmQosFlowPolicerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 1),
    _CmQosFlowPolicerStatsIndex_Type()
)
cmQosFlowPolicerStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsIndex.setStatus("current")
_CmQosFlowPolicerStatsIntervalType_Type = CmPmIntervalType
_CmQosFlowPolicerStatsIntervalType_Object = MibTableColumn
cmQosFlowPolicerStatsIntervalType = _CmQosFlowPolicerStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 2),
    _CmQosFlowPolicerStatsIntervalType_Type()
)
cmQosFlowPolicerStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsIntervalType.setStatus("current")
_CmQosFlowPolicerStatsValid_Type = TruthValue
_CmQosFlowPolicerStatsValid_Object = MibTableColumn
cmQosFlowPolicerStatsValid = _CmQosFlowPolicerStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 3),
    _CmQosFlowPolicerStatsValid_Type()
)
cmQosFlowPolicerStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsValid.setStatus("current")
_CmQosFlowPolicerStatsAction_Type = CmPmBinAction
_CmQosFlowPolicerStatsAction_Object = MibTableColumn
cmQosFlowPolicerStatsAction = _CmQosFlowPolicerStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 4),
    _CmQosFlowPolicerStatsAction_Type()
)
cmQosFlowPolicerStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsAction.setStatus("current")
_CmQosFlowPolicerStatsFMG_Type = PerfCounter64
_CmQosFlowPolicerStatsFMG_Object = MibTableColumn
cmQosFlowPolicerStatsFMG = _CmQosFlowPolicerStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 5),
    _CmQosFlowPolicerStatsFMG_Type()
)
cmQosFlowPolicerStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsFMG.setStatus("current")
_CmQosFlowPolicerStatsFMY_Type = PerfCounter64
_CmQosFlowPolicerStatsFMY_Object = MibTableColumn
cmQosFlowPolicerStatsFMY = _CmQosFlowPolicerStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 6),
    _CmQosFlowPolicerStatsFMY_Type()
)
cmQosFlowPolicerStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsFMY.setStatus("current")
_CmQosFlowPolicerStatsFMYD_Type = PerfCounter64
_CmQosFlowPolicerStatsFMYD_Object = MibTableColumn
cmQosFlowPolicerStatsFMYD = _CmQosFlowPolicerStatsFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 7),
    _CmQosFlowPolicerStatsFMYD_Type()
)
cmQosFlowPolicerStatsFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsFMYD.setStatus("deprecated")
_CmQosFlowPolicerStatsFMRD_Type = PerfCounter64
_CmQosFlowPolicerStatsFMRD_Object = MibTableColumn
cmQosFlowPolicerStatsFMRD = _CmQosFlowPolicerStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 8),
    _CmQosFlowPolicerStatsFMRD_Type()
)
cmQosFlowPolicerStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsFMRD.setStatus("current")
_CmQosFlowPolicerStatsBytesIn_Type = PerfCounter64
_CmQosFlowPolicerStatsBytesIn_Object = MibTableColumn
cmQosFlowPolicerStatsBytesIn = _CmQosFlowPolicerStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 9),
    _CmQosFlowPolicerStatsBytesIn_Type()
)
cmQosFlowPolicerStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsBytesIn.setStatus("current")
_CmQosFlowPolicerStatsBytesOut_Type = PerfCounter64
_CmQosFlowPolicerStatsBytesOut_Object = MibTableColumn
cmQosFlowPolicerStatsBytesOut = _CmQosFlowPolicerStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 10),
    _CmQosFlowPolicerStatsBytesOut_Type()
)
cmQosFlowPolicerStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsBytesOut.setStatus("current")
_CmQosFlowPolicerStatsABR_Type = PerfCounter64
_CmQosFlowPolicerStatsABR_Object = MibTableColumn
cmQosFlowPolicerStatsABR = _CmQosFlowPolicerStatsABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 15, 1, 11),
    _CmQosFlowPolicerStatsABR_Type()
)
cmQosFlowPolicerStatsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerStatsABR.setStatus("current")
_CmQosFlowPolicerHistoryTable_Object = MibTable
cmQosFlowPolicerHistoryTable = _CmQosFlowPolicerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16)
)
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryTable.setStatus("current")
_CmQosFlowPolicerHistoryEntry_Object = MibTableRow
cmQosFlowPolicerHistoryEntry = _CmQosFlowPolicerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1)
)
cmQosFlowPolicerHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-FACILITY-MIB", "cmQosFlowPolicerTypeIndex"),
    (0, "CM-FACILITY-MIB", "cmQosFlowPolicerIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryEntry.setStatus("current")


class _CmQosFlowPolicerHistoryIndex_Type(Integer32):
    """Custom type cmQosFlowPolicerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosFlowPolicerHistoryIndex_Type.__name__ = "Integer32"
_CmQosFlowPolicerHistoryIndex_Object = MibTableColumn
cmQosFlowPolicerHistoryIndex = _CmQosFlowPolicerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 1),
    _CmQosFlowPolicerHistoryIndex_Type()
)
cmQosFlowPolicerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryIndex.setStatus("current")
_CmQosFlowPolicerHistoryTime_Type = DateAndTime
_CmQosFlowPolicerHistoryTime_Object = MibTableColumn
cmQosFlowPolicerHistoryTime = _CmQosFlowPolicerHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 2),
    _CmQosFlowPolicerHistoryTime_Type()
)
cmQosFlowPolicerHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryTime.setStatus("current")
_CmQosFlowPolicerHistoryValid_Type = TruthValue
_CmQosFlowPolicerHistoryValid_Object = MibTableColumn
cmQosFlowPolicerHistoryValid = _CmQosFlowPolicerHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 3),
    _CmQosFlowPolicerHistoryValid_Type()
)
cmQosFlowPolicerHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryValid.setStatus("current")
_CmQosFlowPolicerHistoryAction_Type = CmPmBinAction
_CmQosFlowPolicerHistoryAction_Object = MibTableColumn
cmQosFlowPolicerHistoryAction = _CmQosFlowPolicerHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 4),
    _CmQosFlowPolicerHistoryAction_Type()
)
cmQosFlowPolicerHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryAction.setStatus("current")
_CmQosFlowPolicerHistoryFMG_Type = PerfCounter64
_CmQosFlowPolicerHistoryFMG_Object = MibTableColumn
cmQosFlowPolicerHistoryFMG = _CmQosFlowPolicerHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 5),
    _CmQosFlowPolicerHistoryFMG_Type()
)
cmQosFlowPolicerHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryFMG.setStatus("current")
_CmQosFlowPolicerHistoryFMY_Type = PerfCounter64
_CmQosFlowPolicerHistoryFMY_Object = MibTableColumn
cmQosFlowPolicerHistoryFMY = _CmQosFlowPolicerHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 6),
    _CmQosFlowPolicerHistoryFMY_Type()
)
cmQosFlowPolicerHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryFMY.setStatus("current")
_CmQosFlowPolicerHistoryFMYD_Type = PerfCounter64
_CmQosFlowPolicerHistoryFMYD_Object = MibTableColumn
cmQosFlowPolicerHistoryFMYD = _CmQosFlowPolicerHistoryFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 7),
    _CmQosFlowPolicerHistoryFMYD_Type()
)
cmQosFlowPolicerHistoryFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryFMYD.setStatus("deprecated")
_CmQosFlowPolicerHistoryFMRD_Type = PerfCounter64
_CmQosFlowPolicerHistoryFMRD_Object = MibTableColumn
cmQosFlowPolicerHistoryFMRD = _CmQosFlowPolicerHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 8),
    _CmQosFlowPolicerHistoryFMRD_Type()
)
cmQosFlowPolicerHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryFMRD.setStatus("current")
_CmQosFlowPolicerHistoryBytesIn_Type = PerfCounter64
_CmQosFlowPolicerHistoryBytesIn_Object = MibTableColumn
cmQosFlowPolicerHistoryBytesIn = _CmQosFlowPolicerHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 9),
    _CmQosFlowPolicerHistoryBytesIn_Type()
)
cmQosFlowPolicerHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryBytesIn.setStatus("current")
_CmQosFlowPolicerHistoryBytesOut_Type = PerfCounter64
_CmQosFlowPolicerHistoryBytesOut_Object = MibTableColumn
cmQosFlowPolicerHistoryBytesOut = _CmQosFlowPolicerHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 10),
    _CmQosFlowPolicerHistoryBytesOut_Type()
)
cmQosFlowPolicerHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryBytesOut.setStatus("current")
_CmQosFlowPolicerHistoryABR_Type = PerfCounter64
_CmQosFlowPolicerHistoryABR_Object = MibTableColumn
cmQosFlowPolicerHistoryABR = _CmQosFlowPolicerHistoryABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 16, 1, 11),
    _CmQosFlowPolicerHistoryABR_Type()
)
cmQosFlowPolicerHistoryABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerHistoryABR.setStatus("current")
_CmQosFlowPolicerThresholdTable_Object = MibTable
cmQosFlowPolicerThresholdTable = _CmQosFlowPolicerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 17)
)
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdTable.setStatus("current")
_CmQosFlowPolicerThresholdEntry_Object = MibTableRow
cmQosFlowPolicerThresholdEntry = _CmQosFlowPolicerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 17, 1)
)
cmQosFlowPolicerThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
    (0, "CM-FACILITY-MIB", "cmQosFlowPolicerTypeIndex"),
    (0, "CM-FACILITY-MIB", "cmQosFlowPolicerIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdEntry.setStatus("current")


class _CmQosFlowPolicerThresholdIndex_Type(Integer32):
    """Custom type cmQosFlowPolicerThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosFlowPolicerThresholdIndex_Type.__name__ = "Integer32"
_CmQosFlowPolicerThresholdIndex_Object = MibTableColumn
cmQosFlowPolicerThresholdIndex = _CmQosFlowPolicerThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 17, 1, 1),
    _CmQosFlowPolicerThresholdIndex_Type()
)
cmQosFlowPolicerThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdIndex.setStatus("current")
_CmQosFlowPolicerThresholdInterval_Type = CmPmIntervalType
_CmQosFlowPolicerThresholdInterval_Object = MibTableColumn
cmQosFlowPolicerThresholdInterval = _CmQosFlowPolicerThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 17, 1, 2),
    _CmQosFlowPolicerThresholdInterval_Type()
)
cmQosFlowPolicerThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdInterval.setStatus("current")
_CmQosFlowPolicerThresholdVariable_Type = VariablePointer
_CmQosFlowPolicerThresholdVariable_Object = MibTableColumn
cmQosFlowPolicerThresholdVariable = _CmQosFlowPolicerThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 17, 1, 3),
    _CmQosFlowPolicerThresholdVariable_Type()
)
cmQosFlowPolicerThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdVariable.setStatus("current")
_CmQosFlowPolicerThresholdValueLo_Type = Unsigned32
_CmQosFlowPolicerThresholdValueLo_Object = MibTableColumn
cmQosFlowPolicerThresholdValueLo = _CmQosFlowPolicerThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 17, 1, 4),
    _CmQosFlowPolicerThresholdValueLo_Type()
)
cmQosFlowPolicerThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdValueLo.setStatus("current")
_CmQosFlowPolicerThresholdValueHi_Type = Unsigned32
_CmQosFlowPolicerThresholdValueHi_Object = MibTableColumn
cmQosFlowPolicerThresholdValueHi = _CmQosFlowPolicerThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 17, 1, 5),
    _CmQosFlowPolicerThresholdValueHi_Type()
)
cmQosFlowPolicerThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdValueHi.setStatus("current")
_CmQosFlowPolicerThresholdMonValue_Type = Counter64
_CmQosFlowPolicerThresholdMonValue_Object = MibTableColumn
cmQosFlowPolicerThresholdMonValue = _CmQosFlowPolicerThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 17, 1, 6),
    _CmQosFlowPolicerThresholdMonValue_Type()
)
cmQosFlowPolicerThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdMonValue.setStatus("current")
_CmAccPortQosShaperStatsTable_Object = MibTable
cmAccPortQosShaperStatsTable = _CmAccPortQosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18)
)
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsTable.setStatus("current")
_CmAccPortQosShaperStatsEntry_Object = MibTableRow
cmAccPortQosShaperStatsEntry = _CmAccPortQosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1)
)
cmAccPortQosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmAccPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsEntry.setStatus("current")


class _CmAccPortQosShaperStatsIndex_Type(Integer32):
    """Custom type cmAccPortQosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmAccPortQosShaperStatsIndex_Type.__name__ = "Integer32"
_CmAccPortQosShaperStatsIndex_Object = MibTableColumn
cmAccPortQosShaperStatsIndex = _CmAccPortQosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 1),
    _CmAccPortQosShaperStatsIndex_Type()
)
cmAccPortQosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsIndex.setStatus("current")
_CmAccPortQosShaperStatsIntervalType_Type = CmPmIntervalType
_CmAccPortQosShaperStatsIntervalType_Object = MibTableColumn
cmAccPortQosShaperStatsIntervalType = _CmAccPortQosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 2),
    _CmAccPortQosShaperStatsIntervalType_Type()
)
cmAccPortQosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsIntervalType.setStatus("current")
_CmAccPortQosShaperStatsValid_Type = TruthValue
_CmAccPortQosShaperStatsValid_Object = MibTableColumn
cmAccPortQosShaperStatsValid = _CmAccPortQosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 3),
    _CmAccPortQosShaperStatsValid_Type()
)
cmAccPortQosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsValid.setStatus("current")
_CmAccPortQosShaperStatsAction_Type = CmPmBinAction
_CmAccPortQosShaperStatsAction_Object = MibTableColumn
cmAccPortQosShaperStatsAction = _CmAccPortQosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 4),
    _CmAccPortQosShaperStatsAction_Type()
)
cmAccPortQosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsAction.setStatus("current")
_CmAccPortQosShaperStatsBT_Type = PerfCounter64
_CmAccPortQosShaperStatsBT_Object = MibTableColumn
cmAccPortQosShaperStatsBT = _CmAccPortQosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 5),
    _CmAccPortQosShaperStatsBT_Type()
)
cmAccPortQosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsBT.setStatus("current")
_CmAccPortQosShaperStatsBTD_Type = PerfCounter64
_CmAccPortQosShaperStatsBTD_Object = MibTableColumn
cmAccPortQosShaperStatsBTD = _CmAccPortQosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 6),
    _CmAccPortQosShaperStatsBTD_Type()
)
cmAccPortQosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsBTD.setStatus("current")
_CmAccPortQosShaperStatsFD_Type = PerfCounter64
_CmAccPortQosShaperStatsFD_Object = MibTableColumn
cmAccPortQosShaperStatsFD = _CmAccPortQosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 7),
    _CmAccPortQosShaperStatsFD_Type()
)
cmAccPortQosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsFD.setStatus("current")
_CmAccPortQosShaperStatsFTD_Type = PerfCounter64
_CmAccPortQosShaperStatsFTD_Object = MibTableColumn
cmAccPortQosShaperStatsFTD = _CmAccPortQosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 8),
    _CmAccPortQosShaperStatsFTD_Type()
)
cmAccPortQosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsFTD.setStatus("current")
_CmAccPortQosShaperStatsBR_Type = PerfCounter64
_CmAccPortQosShaperStatsBR_Object = MibTableColumn
cmAccPortQosShaperStatsBR = _CmAccPortQosShaperStatsBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 9),
    _CmAccPortQosShaperStatsBR_Type()
)
cmAccPortQosShaperStatsBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsBR.setStatus("current")
_CmAccPortQosShaperStatsFR_Type = PerfCounter64
_CmAccPortQosShaperStatsFR_Object = MibTableColumn
cmAccPortQosShaperStatsFR = _CmAccPortQosShaperStatsFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 10),
    _CmAccPortQosShaperStatsFR_Type()
)
cmAccPortQosShaperStatsFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsFR.setStatus("current")
_CmAccPortQosShaperStatsABRRL_Type = PerfCounter64
_CmAccPortQosShaperStatsABRRL_Object = MibTableColumn
cmAccPortQosShaperStatsABRRL = _CmAccPortQosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 11),
    _CmAccPortQosShaperStatsABRRL_Type()
)
cmAccPortQosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsABRRL.setStatus("current")
_CmAccPortQosShaperStatsBREDD_Type = PerfCounter64
_CmAccPortQosShaperStatsBREDD_Object = MibTableColumn
cmAccPortQosShaperStatsBREDD = _CmAccPortQosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 12),
    _CmAccPortQosShaperStatsBREDD_Type()
)
cmAccPortQosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsBREDD.setStatus("current")
_CmAccPortQosShaperStatsFREDD_Type = PerfCounter64
_CmAccPortQosShaperStatsFREDD_Object = MibTableColumn
cmAccPortQosShaperStatsFREDD = _CmAccPortQosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 18, 1, 13),
    _CmAccPortQosShaperStatsFREDD_Type()
)
cmAccPortQosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperStatsFREDD.setStatus("current")
_CmAccPortQosShaperHistoryTable_Object = MibTable
cmAccPortQosShaperHistoryTable = _CmAccPortQosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19)
)
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryTable.setStatus("current")
_CmAccPortQosShaperHistoryEntry_Object = MibTableRow
cmAccPortQosShaperHistoryEntry = _CmAccPortQosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1)
)
cmAccPortQosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmAccPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryEntry.setStatus("current")


class _CmAccPortQosShaperHistoryIndex_Type(Integer32):
    """Custom type cmAccPortQosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmAccPortQosShaperHistoryIndex_Type.__name__ = "Integer32"
_CmAccPortQosShaperHistoryIndex_Object = MibTableColumn
cmAccPortQosShaperHistoryIndex = _CmAccPortQosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 1),
    _CmAccPortQosShaperHistoryIndex_Type()
)
cmAccPortQosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryIndex.setStatus("current")
_CmAccPortQosShaperHistoryTime_Type = DateAndTime
_CmAccPortQosShaperHistoryTime_Object = MibTableColumn
cmAccPortQosShaperHistoryTime = _CmAccPortQosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 2),
    _CmAccPortQosShaperHistoryTime_Type()
)
cmAccPortQosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryTime.setStatus("current")
_CmAccPortQosShaperHistoryValid_Type = TruthValue
_CmAccPortQosShaperHistoryValid_Object = MibTableColumn
cmAccPortQosShaperHistoryValid = _CmAccPortQosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 3),
    _CmAccPortQosShaperHistoryValid_Type()
)
cmAccPortQosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryValid.setStatus("current")
_CmAccPortQosShaperHistoryAction_Type = CmPmBinAction
_CmAccPortQosShaperHistoryAction_Object = MibTableColumn
cmAccPortQosShaperHistoryAction = _CmAccPortQosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 4),
    _CmAccPortQosShaperHistoryAction_Type()
)
cmAccPortQosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryAction.setStatus("current")
_CmAccPortQosShaperHistoryBT_Type = PerfCounter64
_CmAccPortQosShaperHistoryBT_Object = MibTableColumn
cmAccPortQosShaperHistoryBT = _CmAccPortQosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 5),
    _CmAccPortQosShaperHistoryBT_Type()
)
cmAccPortQosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryBT.setStatus("current")
_CmAccPortQosShaperHistoryBTD_Type = PerfCounter64
_CmAccPortQosShaperHistoryBTD_Object = MibTableColumn
cmAccPortQosShaperHistoryBTD = _CmAccPortQosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 6),
    _CmAccPortQosShaperHistoryBTD_Type()
)
cmAccPortQosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryBTD.setStatus("current")
_CmAccPortQosShaperHistoryFD_Type = PerfCounter64
_CmAccPortQosShaperHistoryFD_Object = MibTableColumn
cmAccPortQosShaperHistoryFD = _CmAccPortQosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 7),
    _CmAccPortQosShaperHistoryFD_Type()
)
cmAccPortQosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryFD.setStatus("current")
_CmAccPortQosShaperHistoryFTD_Type = PerfCounter64
_CmAccPortQosShaperHistoryFTD_Object = MibTableColumn
cmAccPortQosShaperHistoryFTD = _CmAccPortQosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 8),
    _CmAccPortQosShaperHistoryFTD_Type()
)
cmAccPortQosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryFTD.setStatus("current")
_CmAccPortQosShaperHistoryBR_Type = PerfCounter64
_CmAccPortQosShaperHistoryBR_Object = MibTableColumn
cmAccPortQosShaperHistoryBR = _CmAccPortQosShaperHistoryBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 9),
    _CmAccPortQosShaperHistoryBR_Type()
)
cmAccPortQosShaperHistoryBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryBR.setStatus("current")
_CmAccPortQosShaperHistoryFR_Type = PerfCounter64
_CmAccPortQosShaperHistoryFR_Object = MibTableColumn
cmAccPortQosShaperHistoryFR = _CmAccPortQosShaperHistoryFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 10),
    _CmAccPortQosShaperHistoryFR_Type()
)
cmAccPortQosShaperHistoryFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryFR.setStatus("current")
_CmAccPortQosShaperHistoryABRRL_Type = PerfCounter64
_CmAccPortQosShaperHistoryABRRL_Object = MibTableColumn
cmAccPortQosShaperHistoryABRRL = _CmAccPortQosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 11),
    _CmAccPortQosShaperHistoryABRRL_Type()
)
cmAccPortQosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryABRRL.setStatus("current")
_CmAccPortQosShaperHistoryBREDD_Type = PerfCounter64
_CmAccPortQosShaperHistoryBREDD_Object = MibTableColumn
cmAccPortQosShaperHistoryBREDD = _CmAccPortQosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 12),
    _CmAccPortQosShaperHistoryBREDD_Type()
)
cmAccPortQosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryBREDD.setStatus("current")
_CmAccPortQosShaperHistoryFREDD_Type = PerfCounter64
_CmAccPortQosShaperHistoryFREDD_Object = MibTableColumn
cmAccPortQosShaperHistoryFREDD = _CmAccPortQosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 19, 1, 13),
    _CmAccPortQosShaperHistoryFREDD_Type()
)
cmAccPortQosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperHistoryFREDD.setStatus("current")
_CmAccPortQosShaperThresholdTable_Object = MibTable
cmAccPortQosShaperThresholdTable = _CmAccPortQosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 20)
)
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdTable.setStatus("current")
_CmAccPortQosShaperThresholdEntry_Object = MibTableRow
cmAccPortQosShaperThresholdEntry = _CmAccPortQosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 20, 1)
)
cmAccPortQosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmAccPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdEntry.setStatus("current")


class _CmAccPortQosShaperThresholdIndex_Type(Integer32):
    """Custom type cmAccPortQosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmAccPortQosShaperThresholdIndex_Type.__name__ = "Integer32"
_CmAccPortQosShaperThresholdIndex_Object = MibTableColumn
cmAccPortQosShaperThresholdIndex = _CmAccPortQosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 20, 1, 1),
    _CmAccPortQosShaperThresholdIndex_Type()
)
cmAccPortQosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdIndex.setStatus("current")
_CmAccPortQosShaperThresholdInterval_Type = CmPmIntervalType
_CmAccPortQosShaperThresholdInterval_Object = MibTableColumn
cmAccPortQosShaperThresholdInterval = _CmAccPortQosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 20, 1, 2),
    _CmAccPortQosShaperThresholdInterval_Type()
)
cmAccPortQosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdInterval.setStatus("current")
_CmAccPortQosShaperThresholdVariable_Type = VariablePointer
_CmAccPortQosShaperThresholdVariable_Object = MibTableColumn
cmAccPortQosShaperThresholdVariable = _CmAccPortQosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 20, 1, 3),
    _CmAccPortQosShaperThresholdVariable_Type()
)
cmAccPortQosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdVariable.setStatus("current")
_CmAccPortQosShaperThresholdValueLo_Type = Unsigned32
_CmAccPortQosShaperThresholdValueLo_Object = MibTableColumn
cmAccPortQosShaperThresholdValueLo = _CmAccPortQosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 20, 1, 4),
    _CmAccPortQosShaperThresholdValueLo_Type()
)
cmAccPortQosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdValueLo.setStatus("current")
_CmAccPortQosShaperThresholdValueHi_Type = Unsigned32
_CmAccPortQosShaperThresholdValueHi_Object = MibTableColumn
cmAccPortQosShaperThresholdValueHi = _CmAccPortQosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 20, 1, 5),
    _CmAccPortQosShaperThresholdValueHi_Type()
)
cmAccPortQosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdValueHi.setStatus("current")
_CmAccPortQosShaperThresholdMonValue_Type = Counter64
_CmAccPortQosShaperThresholdMonValue_Object = MibTableColumn
cmAccPortQosShaperThresholdMonValue = _CmAccPortQosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 20, 1, 6),
    _CmAccPortQosShaperThresholdMonValue_Type()
)
cmAccPortQosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdMonValue.setStatus("current")
_CmEthernetTrafficPortStatsTable_Object = MibTable
cmEthernetTrafficPortStatsTable = _CmEthernetTrafficPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21)
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsTable.setStatus("current")
_CmEthernetTrafficPortStatsEntry_Object = MibTableRow
cmEthernetTrafficPortStatsEntry = _CmEthernetTrafficPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1)
)
cmEthernetTrafficPortStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsEntry.setStatus("current")


class _CmEthernetTrafficPortStatsIndex_Type(Integer32):
    """Custom type cmEthernetTrafficPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmEthernetTrafficPortStatsIndex_Type.__name__ = "Integer32"
_CmEthernetTrafficPortStatsIndex_Object = MibTableColumn
cmEthernetTrafficPortStatsIndex = _CmEthernetTrafficPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 1),
    _CmEthernetTrafficPortStatsIndex_Type()
)
cmEthernetTrafficPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsIndex.setStatus("current")
_CmEthernetTrafficPortStatsIntervalType_Type = CmPmIntervalType
_CmEthernetTrafficPortStatsIntervalType_Object = MibTableColumn
cmEthernetTrafficPortStatsIntervalType = _CmEthernetTrafficPortStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 2),
    _CmEthernetTrafficPortStatsIntervalType_Type()
)
cmEthernetTrafficPortStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsIntervalType.setStatus("current")
_CmEthernetTrafficPortStatsValid_Type = TruthValue
_CmEthernetTrafficPortStatsValid_Object = MibTableColumn
cmEthernetTrafficPortStatsValid = _CmEthernetTrafficPortStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 3),
    _CmEthernetTrafficPortStatsValid_Type()
)
cmEthernetTrafficPortStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsValid.setStatus("current")
_CmEthernetTrafficPortStatsAction_Type = CmPmBinAction
_CmEthernetTrafficPortStatsAction_Object = MibTableColumn
cmEthernetTrafficPortStatsAction = _CmEthernetTrafficPortStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 4),
    _CmEthernetTrafficPortStatsAction_Type()
)
cmEthernetTrafficPortStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsAction.setStatus("current")
_CmEthernetTrafficPortStatsESBF_Type = PerfCounter64
_CmEthernetTrafficPortStatsESBF_Object = MibTableColumn
cmEthernetTrafficPortStatsESBF = _CmEthernetTrafficPortStatsESBF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 5),
    _CmEthernetTrafficPortStatsESBF_Type()
)
cmEthernetTrafficPortStatsESBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESBF.setStatus("current")
_CmEthernetTrafficPortStatsESBP_Type = PerfCounter64
_CmEthernetTrafficPortStatsESBP_Object = MibTableColumn
cmEthernetTrafficPortStatsESBP = _CmEthernetTrafficPortStatsESBP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 6),
    _CmEthernetTrafficPortStatsESBP_Type()
)
cmEthernetTrafficPortStatsESBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESBP.setStatus("current")
_CmEthernetTrafficPortStatsESBS_Type = PerfCounter64
_CmEthernetTrafficPortStatsESBS_Object = MibTableColumn
cmEthernetTrafficPortStatsESBS = _CmEthernetTrafficPortStatsESBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 7),
    _CmEthernetTrafficPortStatsESBS_Type()
)
cmEthernetTrafficPortStatsESBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESBS.setStatus("current")
_CmEthernetTrafficPortStatsESC_Type = PerfCounter64
_CmEthernetTrafficPortStatsESC_Object = MibTableColumn
cmEthernetTrafficPortStatsESC = _CmEthernetTrafficPortStatsESC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 8),
    _CmEthernetTrafficPortStatsESC_Type()
)
cmEthernetTrafficPortStatsESC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESC.setStatus("current")
_CmEthernetTrafficPortStatsESCAE_Type = PerfCounter64
_CmEthernetTrafficPortStatsESCAE_Object = MibTableColumn
cmEthernetTrafficPortStatsESCAE = _CmEthernetTrafficPortStatsESCAE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 9),
    _CmEthernetTrafficPortStatsESCAE_Type()
)
cmEthernetTrafficPortStatsESCAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESCAE.setStatus("current")
_CmEthernetTrafficPortStatsESDE_Type = PerfCounter64
_CmEthernetTrafficPortStatsESDE_Object = MibTableColumn
cmEthernetTrafficPortStatsESDE = _CmEthernetTrafficPortStatsESDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 10),
    _CmEthernetTrafficPortStatsESDE_Type()
)
cmEthernetTrafficPortStatsESDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESDE.setStatus("current")
_CmEthernetTrafficPortStatsESF_Type = PerfCounter64
_CmEthernetTrafficPortStatsESF_Object = MibTableColumn
cmEthernetTrafficPortStatsESF = _CmEthernetTrafficPortStatsESF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 11),
    _CmEthernetTrafficPortStatsESF_Type()
)
cmEthernetTrafficPortStatsESF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESF.setStatus("current")
_CmEthernetTrafficPortStatsESFS_Type = PerfCounter64
_CmEthernetTrafficPortStatsESFS_Object = MibTableColumn
cmEthernetTrafficPortStatsESFS = _CmEthernetTrafficPortStatsESFS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 12),
    _CmEthernetTrafficPortStatsESFS_Type()
)
cmEthernetTrafficPortStatsESFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESFS.setStatus("current")
_CmEthernetTrafficPortStatsESJ_Type = PerfCounter64
_CmEthernetTrafficPortStatsESJ_Object = MibTableColumn
cmEthernetTrafficPortStatsESJ = _CmEthernetTrafficPortStatsESJ_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 13),
    _CmEthernetTrafficPortStatsESJ_Type()
)
cmEthernetTrafficPortStatsESJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESJ.setStatus("current")
_CmEthernetTrafficPortStatsESMF_Type = PerfCounter64
_CmEthernetTrafficPortStatsESMF_Object = MibTableColumn
cmEthernetTrafficPortStatsESMF = _CmEthernetTrafficPortStatsESMF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 14),
    _CmEthernetTrafficPortStatsESMF_Type()
)
cmEthernetTrafficPortStatsESMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESMF.setStatus("current")
_CmEthernetTrafficPortStatsESMP_Type = PerfCounter64
_CmEthernetTrafficPortStatsESMP_Object = MibTableColumn
cmEthernetTrafficPortStatsESMP = _CmEthernetTrafficPortStatsESMP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 15),
    _CmEthernetTrafficPortStatsESMP_Type()
)
cmEthernetTrafficPortStatsESMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESMP.setStatus("current")
_CmEthernetTrafficPortStatsESO_Type = PerfCounter64
_CmEthernetTrafficPortStatsESO_Object = MibTableColumn
cmEthernetTrafficPortStatsESO = _CmEthernetTrafficPortStatsESO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 16),
    _CmEthernetTrafficPortStatsESO_Type()
)
cmEthernetTrafficPortStatsESO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESO.setStatus("current")
_CmEthernetTrafficPortStatsESOF_Type = PerfCounter64
_CmEthernetTrafficPortStatsESOF_Object = MibTableColumn
cmEthernetTrafficPortStatsESOF = _CmEthernetTrafficPortStatsESOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 17),
    _CmEthernetTrafficPortStatsESOF_Type()
)
cmEthernetTrafficPortStatsESOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESOF.setStatus("current")
_CmEthernetTrafficPortStatsESOP_Type = PerfCounter64
_CmEthernetTrafficPortStatsESOP_Object = MibTableColumn
cmEthernetTrafficPortStatsESOP = _CmEthernetTrafficPortStatsESOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 18),
    _CmEthernetTrafficPortStatsESOP_Type()
)
cmEthernetTrafficPortStatsESOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESOP.setStatus("current")
_CmEthernetTrafficPortStatsESP_Type = PerfCounter64
_CmEthernetTrafficPortStatsESP_Object = MibTableColumn
cmEthernetTrafficPortStatsESP = _CmEthernetTrafficPortStatsESP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 19),
    _CmEthernetTrafficPortStatsESP_Type()
)
cmEthernetTrafficPortStatsESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESP.setStatus("current")
_CmEthernetTrafficPortStatsESP64_Type = PerfCounter64
_CmEthernetTrafficPortStatsESP64_Object = MibTableColumn
cmEthernetTrafficPortStatsESP64 = _CmEthernetTrafficPortStatsESP64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 20),
    _CmEthernetTrafficPortStatsESP64_Type()
)
cmEthernetTrafficPortStatsESP64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESP64.setStatus("current")
_CmEthernetTrafficPortStatsESP65_Type = PerfCounter64
_CmEthernetTrafficPortStatsESP65_Object = MibTableColumn
cmEthernetTrafficPortStatsESP65 = _CmEthernetTrafficPortStatsESP65_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 21),
    _CmEthernetTrafficPortStatsESP65_Type()
)
cmEthernetTrafficPortStatsESP65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESP65.setStatus("current")
_CmEthernetTrafficPortStatsESP128_Type = PerfCounter64
_CmEthernetTrafficPortStatsESP128_Object = MibTableColumn
cmEthernetTrafficPortStatsESP128 = _CmEthernetTrafficPortStatsESP128_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 22),
    _CmEthernetTrafficPortStatsESP128_Type()
)
cmEthernetTrafficPortStatsESP128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESP128.setStatus("current")
_CmEthernetTrafficPortStatsESP256_Type = PerfCounter64
_CmEthernetTrafficPortStatsESP256_Object = MibTableColumn
cmEthernetTrafficPortStatsESP256 = _CmEthernetTrafficPortStatsESP256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 23),
    _CmEthernetTrafficPortStatsESP256_Type()
)
cmEthernetTrafficPortStatsESP256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESP256.setStatus("current")
_CmEthernetTrafficPortStatsESP512_Type = PerfCounter64
_CmEthernetTrafficPortStatsESP512_Object = MibTableColumn
cmEthernetTrafficPortStatsESP512 = _CmEthernetTrafficPortStatsESP512_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 24),
    _CmEthernetTrafficPortStatsESP512_Type()
)
cmEthernetTrafficPortStatsESP512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESP512.setStatus("current")
_CmEthernetTrafficPortStatsESP1024_Type = PerfCounter64
_CmEthernetTrafficPortStatsESP1024_Object = MibTableColumn
cmEthernetTrafficPortStatsESP1024 = _CmEthernetTrafficPortStatsESP1024_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 25),
    _CmEthernetTrafficPortStatsESP1024_Type()
)
cmEthernetTrafficPortStatsESP1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESP1024.setStatus("current")
_CmEthernetTrafficPortStatsESP1519_Type = PerfCounter64
_CmEthernetTrafficPortStatsESP1519_Object = MibTableColumn
cmEthernetTrafficPortStatsESP1519 = _CmEthernetTrafficPortStatsESP1519_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 26),
    _CmEthernetTrafficPortStatsESP1519_Type()
)
cmEthernetTrafficPortStatsESP1519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESP1519.setStatus("current")
_CmEthernetTrafficPortStatsESUF_Type = PerfCounter64
_CmEthernetTrafficPortStatsESUF_Object = MibTableColumn
cmEthernetTrafficPortStatsESUF = _CmEthernetTrafficPortStatsESUF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 27),
    _CmEthernetTrafficPortStatsESUF_Type()
)
cmEthernetTrafficPortStatsESUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESUF.setStatus("current")
_CmEthernetTrafficPortStatsESUP_Type = PerfCounter64
_CmEthernetTrafficPortStatsESUP_Object = MibTableColumn
cmEthernetTrafficPortStatsESUP = _CmEthernetTrafficPortStatsESUP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 28),
    _CmEthernetTrafficPortStatsESUP_Type()
)
cmEthernetTrafficPortStatsESUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsESUP.setStatus("current")
_CmEthernetTrafficPortStatsL2CPFD_Type = PerfCounter64
_CmEthernetTrafficPortStatsL2CPFD_Object = MibTableColumn
cmEthernetTrafficPortStatsL2CPFD = _CmEthernetTrafficPortStatsL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 29),
    _CmEthernetTrafficPortStatsL2CPFD_Type()
)
cmEthernetTrafficPortStatsL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsL2CPFD.setStatus("current")
_CmEthernetTrafficPortStatsL2CPFP_Type = PerfCounter64
_CmEthernetTrafficPortStatsL2CPFP_Object = MibTableColumn
cmEthernetTrafficPortStatsL2CPFP = _CmEthernetTrafficPortStatsL2CPFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 30),
    _CmEthernetTrafficPortStatsL2CPFP_Type()
)
cmEthernetTrafficPortStatsL2CPFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsL2CPFP.setStatus("current")
_CmEthernetTrafficPortStatsLES_Type = PerfCounter64
_CmEthernetTrafficPortStatsLES_Object = MibTableColumn
cmEthernetTrafficPortStatsLES = _CmEthernetTrafficPortStatsLES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 31),
    _CmEthernetTrafficPortStatsLES_Type()
)
cmEthernetTrafficPortStatsLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsLES.setStatus("deprecated")
_CmEthernetTrafficPortStatsLBC_Type = Integer32
_CmEthernetTrafficPortStatsLBC_Object = MibTableColumn
cmEthernetTrafficPortStatsLBC = _CmEthernetTrafficPortStatsLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 32),
    _CmEthernetTrafficPortStatsLBC_Type()
)
cmEthernetTrafficPortStatsLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsLBC.setStatus("current")
_CmEthernetTrafficPortStatsOPT_Type = Integer32
_CmEthernetTrafficPortStatsOPT_Object = MibTableColumn
cmEthernetTrafficPortStatsOPT = _CmEthernetTrafficPortStatsOPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 33),
    _CmEthernetTrafficPortStatsOPT_Type()
)
cmEthernetTrafficPortStatsOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsOPT.setStatus("current")
_CmEthernetTrafficPortStatsOPR_Type = Integer32
_CmEthernetTrafficPortStatsOPR_Object = MibTableColumn
cmEthernetTrafficPortStatsOPR = _CmEthernetTrafficPortStatsOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 34),
    _CmEthernetTrafficPortStatsOPR_Type()
)
cmEthernetTrafficPortStatsOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsOPR.setStatus("current")
_CmEthernetTrafficPortStatsAUFD_Type = PerfCounter64
_CmEthernetTrafficPortStatsAUFD_Object = MibTableColumn
cmEthernetTrafficPortStatsAUFD = _CmEthernetTrafficPortStatsAUFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 35),
    _CmEthernetTrafficPortStatsAUFD_Type()
)
cmEthernetTrafficPortStatsAUFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsAUFD.setStatus("current")
_CmEthernetTrafficPortStatsAPFD_Type = PerfCounter64
_CmEthernetTrafficPortStatsAPFD_Object = MibTableColumn
cmEthernetTrafficPortStatsAPFD = _CmEthernetTrafficPortStatsAPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 36),
    _CmEthernetTrafficPortStatsAPFD_Type()
)
cmEthernetTrafficPortStatsAPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsAPFD.setStatus("current")
_CmEthernetTrafficPortStatsABRRx_Type = PerfCounter64
_CmEthernetTrafficPortStatsABRRx_Object = MibTableColumn
cmEthernetTrafficPortStatsABRRx = _CmEthernetTrafficPortStatsABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 37),
    _CmEthernetTrafficPortStatsABRRx_Type()
)
cmEthernetTrafficPortStatsABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsABRRx.setStatus("current")
_CmEthernetTrafficPortStatsABRTx_Type = PerfCounter64
_CmEthernetTrafficPortStatsABRTx_Object = MibTableColumn
cmEthernetTrafficPortStatsABRTx = _CmEthernetTrafficPortStatsABRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 38),
    _CmEthernetTrafficPortStatsABRTx_Type()
)
cmEthernetTrafficPortStatsABRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsABRTx.setStatus("current")
_CmEthernetTrafficPortStatsATFD_Type = PerfCounter64
_CmEthernetTrafficPortStatsATFD_Object = MibTableColumn
cmEthernetTrafficPortStatsATFD = _CmEthernetTrafficPortStatsATFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 39),
    _CmEthernetTrafficPortStatsATFD_Type()
)
cmEthernetTrafficPortStatsATFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsATFD.setStatus("current")
_CmEthernetTrafficPortStatsUAS_Type = PerfCounter64
_CmEthernetTrafficPortStatsUAS_Object = MibTableColumn
cmEthernetTrafficPortStatsUAS = _CmEthernetTrafficPortStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 40),
    _CmEthernetTrafficPortStatsUAS_Type()
)
cmEthernetTrafficPortStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsUAS.setStatus("current")
_CmEthernetTrafficPortStatsTemp_Type = Integer32
_CmEthernetTrafficPortStatsTemp_Object = MibTableColumn
cmEthernetTrafficPortStatsTemp = _CmEthernetTrafficPortStatsTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 41),
    _CmEthernetTrafficPortStatsTemp_Type()
)
cmEthernetTrafficPortStatsTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsTemp.setStatus("current")
_CmEthernetTrafficPortStatsLkupFails_Type = PerfCounter64
_CmEthernetTrafficPortStatsLkupFails_Object = MibTableColumn
cmEthernetTrafficPortStatsLkupFails = _CmEthernetTrafficPortStatsLkupFails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 42),
    _CmEthernetTrafficPortStatsLkupFails_Type()
)
cmEthernetTrafficPortStatsLkupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsLkupFails.setStatus("current")
_CmEthernetTrafficPortStatsPSC_Type = PerfCounter64
_CmEthernetTrafficPortStatsPSC_Object = MibTableColumn
cmEthernetTrafficPortStatsPSC = _CmEthernetTrafficPortStatsPSC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 43),
    _CmEthernetTrafficPortStatsPSC_Type()
)
cmEthernetTrafficPortStatsPSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsPSC.setStatus("current")
_CmEthernetTrafficPortStatsL2PTRxFramesEncap_Type = PerfCounter64
_CmEthernetTrafficPortStatsL2PTRxFramesEncap_Object = MibTableColumn
cmEthernetTrafficPortStatsL2PTRxFramesEncap = _CmEthernetTrafficPortStatsL2PTRxFramesEncap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 44),
    _CmEthernetTrafficPortStatsL2PTRxFramesEncap_Type()
)
cmEthernetTrafficPortStatsL2PTRxFramesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsL2PTRxFramesEncap.setStatus("current")
_CmEthernetTrafficPortStatsL2PTTxFramesDecap_Type = PerfCounter64
_CmEthernetTrafficPortStatsL2PTTxFramesDecap_Object = MibTableColumn
cmEthernetTrafficPortStatsL2PTTxFramesDecap = _CmEthernetTrafficPortStatsL2PTTxFramesDecap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 45),
    _CmEthernetTrafficPortStatsL2PTTxFramesDecap_Type()
)
cmEthernetTrafficPortStatsL2PTTxFramesDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsL2PTTxFramesDecap.setStatus("current")
_CmEthernetTrafficPortStatsIBRMaxRx_Type = PerfCounter64
_CmEthernetTrafficPortStatsIBRMaxRx_Object = MibTableColumn
cmEthernetTrafficPortStatsIBRMaxRx = _CmEthernetTrafficPortStatsIBRMaxRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 46),
    _CmEthernetTrafficPortStatsIBRMaxRx_Type()
)
cmEthernetTrafficPortStatsIBRMaxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsIBRMaxRx.setStatus("current")
_CmEthernetTrafficPortStatsIBRMaxTx_Type = PerfCounter64
_CmEthernetTrafficPortStatsIBRMaxTx_Object = MibTableColumn
cmEthernetTrafficPortStatsIBRMaxTx = _CmEthernetTrafficPortStatsIBRMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 47),
    _CmEthernetTrafficPortStatsIBRMaxTx_Type()
)
cmEthernetTrafficPortStatsIBRMaxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsIBRMaxTx.setStatus("current")
_CmEthernetTrafficPortStatsIBRMinRx_Type = PerfCounter64
_CmEthernetTrafficPortStatsIBRMinRx_Object = MibTableColumn
cmEthernetTrafficPortStatsIBRMinRx = _CmEthernetTrafficPortStatsIBRMinRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 48),
    _CmEthernetTrafficPortStatsIBRMinRx_Type()
)
cmEthernetTrafficPortStatsIBRMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsIBRMinRx.setStatus("current")
_CmEthernetTrafficPortStatsIBRMinTx_Type = PerfCounter64
_CmEthernetTrafficPortStatsIBRMinTx_Object = MibTableColumn
cmEthernetTrafficPortStatsIBRMinTx = _CmEthernetTrafficPortStatsIBRMinTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 49),
    _CmEthernetTrafficPortStatsIBRMinTx_Type()
)
cmEthernetTrafficPortStatsIBRMinTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsIBRMinTx.setStatus("current")
_CmEthernetTrafficPortStatsIBRRx_Type = PerfCounter64
_CmEthernetTrafficPortStatsIBRRx_Object = MibTableColumn
cmEthernetTrafficPortStatsIBRRx = _CmEthernetTrafficPortStatsIBRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 50),
    _CmEthernetTrafficPortStatsIBRRx_Type()
)
cmEthernetTrafficPortStatsIBRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsIBRRx.setStatus("current")
_CmEthernetTrafficPortStatsIBRTx_Type = PerfCounter64
_CmEthernetTrafficPortStatsIBRTx_Object = MibTableColumn
cmEthernetTrafficPortStatsIBRTx = _CmEthernetTrafficPortStatsIBRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 51),
    _CmEthernetTrafficPortStatsIBRTx_Type()
)
cmEthernetTrafficPortStatsIBRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsIBRTx.setStatus("current")
_CmEthernetTrafficPortStatsFmcd_Type = PerfCounter64
_CmEthernetTrafficPortStatsFmcd_Object = MibTableColumn
cmEthernetTrafficPortStatsFmcd = _CmEthernetTrafficPortStatsFmcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 52),
    _CmEthernetTrafficPortStatsFmcd_Type()
)
cmEthernetTrafficPortStatsFmcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsFmcd.setStatus("current")
_CmEthernetTrafficPortStatsFbcd_Type = PerfCounter64
_CmEthernetTrafficPortStatsFbcd_Object = MibTableColumn
cmEthernetTrafficPortStatsFbcd = _CmEthernetTrafficPortStatsFbcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 53),
    _CmEthernetTrafficPortStatsFbcd_Type()
)
cmEthernetTrafficPortStatsFbcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsFbcd.setStatus("current")
_CmEthernetTrafficPortStatsAclDropNoMatch_Type = PerfCounter64
_CmEthernetTrafficPortStatsAclDropNoMatch_Object = MibTableColumn
cmEthernetTrafficPortStatsAclDropNoMatch = _CmEthernetTrafficPortStatsAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 54),
    _CmEthernetTrafficPortStatsAclDropNoMatch_Type()
)
cmEthernetTrafficPortStatsAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsAclDropNoMatch.setStatus("current")
_CmEthernetTrafficPortStatsAclFwd2Cpu_Type = PerfCounter64
_CmEthernetTrafficPortStatsAclFwd2Cpu_Object = MibTableColumn
cmEthernetTrafficPortStatsAclFwd2Cpu = _CmEthernetTrafficPortStatsAclFwd2Cpu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 55),
    _CmEthernetTrafficPortStatsAclFwd2Cpu_Type()
)
cmEthernetTrafficPortStatsAclFwd2Cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsAclFwd2Cpu.setStatus("current")
_CmEthernetTrafficPortStatsDhcpDropNoAssocIf_Type = PerfCounter64
_CmEthernetTrafficPortStatsDhcpDropNoAssocIf_Object = MibTableColumn
cmEthernetTrafficPortStatsDhcpDropNoAssocIf = _CmEthernetTrafficPortStatsDhcpDropNoAssocIf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 56),
    _CmEthernetTrafficPortStatsDhcpDropNoAssocIf_Type()
)
cmEthernetTrafficPortStatsDhcpDropNoAssocIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsDhcpDropNoAssocIf.setStatus("current")
_CmEthernetTrafficPortStatsDroppedFragmented_Type = PerfCounter64
_CmEthernetTrafficPortStatsDroppedFragmented_Object = MibTableColumn
cmEthernetTrafficPortStatsDroppedFragmented = _CmEthernetTrafficPortStatsDroppedFragmented_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 57),
    _CmEthernetTrafficPortStatsDroppedFragmented_Type()
)
cmEthernetTrafficPortStatsDroppedFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsDroppedFragmented.setStatus("current")
_CmEthernetTrafficPortStatsRLBC_Type = Integer32
_CmEthernetTrafficPortStatsRLBC_Object = MibTableColumn
cmEthernetTrafficPortStatsRLBC = _CmEthernetTrafficPortStatsRLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 58),
    _CmEthernetTrafficPortStatsRLBC_Type()
)
cmEthernetTrafficPortStatsRLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsRLBC.setStatus("current")
_CmEthernetTrafficPortStatsROPT_Type = Integer32
_CmEthernetTrafficPortStatsROPT_Object = MibTableColumn
cmEthernetTrafficPortStatsROPT = _CmEthernetTrafficPortStatsROPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 59),
    _CmEthernetTrafficPortStatsROPT_Type()
)
cmEthernetTrafficPortStatsROPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsROPT.setStatus("current")
_CmEthernetTrafficPortStatsROPR_Type = Integer32
_CmEthernetTrafficPortStatsROPR_Object = MibTableColumn
cmEthernetTrafficPortStatsROPR = _CmEthernetTrafficPortStatsROPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 60),
    _CmEthernetTrafficPortStatsROPR_Type()
)
cmEthernetTrafficPortStatsROPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsROPR.setStatus("current")
_CmEthernetTrafficPortStatsRTemp_Type = Integer32
_CmEthernetTrafficPortStatsRTemp_Object = MibTableColumn
cmEthernetTrafficPortStatsRTemp = _CmEthernetTrafficPortStatsRTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 21, 1, 61),
    _CmEthernetTrafficPortStatsRTemp_Type()
)
cmEthernetTrafficPortStatsRTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortStatsRTemp.setStatus("current")
_CmEthernetTrafficPortHistoryTable_Object = MibTable
cmEthernetTrafficPortHistoryTable = _CmEthernetTrafficPortHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22)
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryTable.setStatus("current")
_CmEthernetTrafficPortHistoryEntry_Object = MibTableRow
cmEthernetTrafficPortHistoryEntry = _CmEthernetTrafficPortHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1)
)
cmEthernetTrafficPortHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryEntry.setStatus("current")


class _CmEthernetTrafficPortHistoryIndex_Type(Integer32):
    """Custom type cmEthernetTrafficPortHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CmEthernetTrafficPortHistoryIndex_Type.__name__ = "Integer32"
_CmEthernetTrafficPortHistoryIndex_Object = MibTableColumn
cmEthernetTrafficPortHistoryIndex = _CmEthernetTrafficPortHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 1),
    _CmEthernetTrafficPortHistoryIndex_Type()
)
cmEthernetTrafficPortHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryIndex.setStatus("current")
_CmEthernetTrafficPortHistoryTime_Type = DateAndTime
_CmEthernetTrafficPortHistoryTime_Object = MibTableColumn
cmEthernetTrafficPortHistoryTime = _CmEthernetTrafficPortHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 2),
    _CmEthernetTrafficPortHistoryTime_Type()
)
cmEthernetTrafficPortHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryTime.setStatus("current")
_CmEthernetTrafficPortHistoryValid_Type = TruthValue
_CmEthernetTrafficPortHistoryValid_Object = MibTableColumn
cmEthernetTrafficPortHistoryValid = _CmEthernetTrafficPortHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 3),
    _CmEthernetTrafficPortHistoryValid_Type()
)
cmEthernetTrafficPortHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryValid.setStatus("current")
_CmEthernetTrafficPortHistoryAction_Type = CmPmBinAction
_CmEthernetTrafficPortHistoryAction_Object = MibTableColumn
cmEthernetTrafficPortHistoryAction = _CmEthernetTrafficPortHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 4),
    _CmEthernetTrafficPortHistoryAction_Type()
)
cmEthernetTrafficPortHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryAction.setStatus("current")
_CmEthernetTrafficPortHistoryESBF_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESBF_Object = MibTableColumn
cmEthernetTrafficPortHistoryESBF = _CmEthernetTrafficPortHistoryESBF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 5),
    _CmEthernetTrafficPortHistoryESBF_Type()
)
cmEthernetTrafficPortHistoryESBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESBF.setStatus("current")
_CmEthernetTrafficPortHistoryESBP_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESBP_Object = MibTableColumn
cmEthernetTrafficPortHistoryESBP = _CmEthernetTrafficPortHistoryESBP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 6),
    _CmEthernetTrafficPortHistoryESBP_Type()
)
cmEthernetTrafficPortHistoryESBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESBP.setStatus("current")
_CmEthernetTrafficPortHistoryESBS_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESBS_Object = MibTableColumn
cmEthernetTrafficPortHistoryESBS = _CmEthernetTrafficPortHistoryESBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 7),
    _CmEthernetTrafficPortHistoryESBS_Type()
)
cmEthernetTrafficPortHistoryESBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESBS.setStatus("current")
_CmEthernetTrafficPortHistoryESC_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESC_Object = MibTableColumn
cmEthernetTrafficPortHistoryESC = _CmEthernetTrafficPortHistoryESC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 8),
    _CmEthernetTrafficPortHistoryESC_Type()
)
cmEthernetTrafficPortHistoryESC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESC.setStatus("current")
_CmEthernetTrafficPortHistoryESCAE_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESCAE_Object = MibTableColumn
cmEthernetTrafficPortHistoryESCAE = _CmEthernetTrafficPortHistoryESCAE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 9),
    _CmEthernetTrafficPortHistoryESCAE_Type()
)
cmEthernetTrafficPortHistoryESCAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESCAE.setStatus("current")
_CmEthernetTrafficPortHistoryESDE_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESDE_Object = MibTableColumn
cmEthernetTrafficPortHistoryESDE = _CmEthernetTrafficPortHistoryESDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 10),
    _CmEthernetTrafficPortHistoryESDE_Type()
)
cmEthernetTrafficPortHistoryESDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESDE.setStatus("current")
_CmEthernetTrafficPortHistoryESF_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESF_Object = MibTableColumn
cmEthernetTrafficPortHistoryESF = _CmEthernetTrafficPortHistoryESF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 11),
    _CmEthernetTrafficPortHistoryESF_Type()
)
cmEthernetTrafficPortHistoryESF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESF.setStatus("current")
_CmEthernetTrafficPortHistoryESFS_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESFS_Object = MibTableColumn
cmEthernetTrafficPortHistoryESFS = _CmEthernetTrafficPortHistoryESFS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 12),
    _CmEthernetTrafficPortHistoryESFS_Type()
)
cmEthernetTrafficPortHistoryESFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESFS.setStatus("current")
_CmEthernetTrafficPortHistoryESJ_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESJ_Object = MibTableColumn
cmEthernetTrafficPortHistoryESJ = _CmEthernetTrafficPortHistoryESJ_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 13),
    _CmEthernetTrafficPortHistoryESJ_Type()
)
cmEthernetTrafficPortHistoryESJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESJ.setStatus("current")
_CmEthernetTrafficPortHistoryESMF_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESMF_Object = MibTableColumn
cmEthernetTrafficPortHistoryESMF = _CmEthernetTrafficPortHistoryESMF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 14),
    _CmEthernetTrafficPortHistoryESMF_Type()
)
cmEthernetTrafficPortHistoryESMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESMF.setStatus("current")
_CmEthernetTrafficPortHistoryESMP_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESMP_Object = MibTableColumn
cmEthernetTrafficPortHistoryESMP = _CmEthernetTrafficPortHistoryESMP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 15),
    _CmEthernetTrafficPortHistoryESMP_Type()
)
cmEthernetTrafficPortHistoryESMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESMP.setStatus("current")
_CmEthernetTrafficPortHistoryESO_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESO_Object = MibTableColumn
cmEthernetTrafficPortHistoryESO = _CmEthernetTrafficPortHistoryESO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 16),
    _CmEthernetTrafficPortHistoryESO_Type()
)
cmEthernetTrafficPortHistoryESO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESO.setStatus("current")
_CmEthernetTrafficPortHistoryESOF_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESOF_Object = MibTableColumn
cmEthernetTrafficPortHistoryESOF = _CmEthernetTrafficPortHistoryESOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 17),
    _CmEthernetTrafficPortHistoryESOF_Type()
)
cmEthernetTrafficPortHistoryESOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESOF.setStatus("current")
_CmEthernetTrafficPortHistoryESOP_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESOP_Object = MibTableColumn
cmEthernetTrafficPortHistoryESOP = _CmEthernetTrafficPortHistoryESOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 18),
    _CmEthernetTrafficPortHistoryESOP_Type()
)
cmEthernetTrafficPortHistoryESOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESOP.setStatus("current")
_CmEthernetTrafficPortHistoryESP_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESP_Object = MibTableColumn
cmEthernetTrafficPortHistoryESP = _CmEthernetTrafficPortHistoryESP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 19),
    _CmEthernetTrafficPortHistoryESP_Type()
)
cmEthernetTrafficPortHistoryESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESP.setStatus("current")
_CmEthernetTrafficPortHistoryESP64_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESP64_Object = MibTableColumn
cmEthernetTrafficPortHistoryESP64 = _CmEthernetTrafficPortHistoryESP64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 20),
    _CmEthernetTrafficPortHistoryESP64_Type()
)
cmEthernetTrafficPortHistoryESP64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESP64.setStatus("current")
_CmEthernetTrafficPortHistoryESP65_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESP65_Object = MibTableColumn
cmEthernetTrafficPortHistoryESP65 = _CmEthernetTrafficPortHistoryESP65_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 21),
    _CmEthernetTrafficPortHistoryESP65_Type()
)
cmEthernetTrafficPortHistoryESP65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESP65.setStatus("current")
_CmEthernetTrafficPortHistoryESP128_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESP128_Object = MibTableColumn
cmEthernetTrafficPortHistoryESP128 = _CmEthernetTrafficPortHistoryESP128_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 22),
    _CmEthernetTrafficPortHistoryESP128_Type()
)
cmEthernetTrafficPortHistoryESP128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESP128.setStatus("current")
_CmEthernetTrafficPortHistoryESP256_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESP256_Object = MibTableColumn
cmEthernetTrafficPortHistoryESP256 = _CmEthernetTrafficPortHistoryESP256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 23),
    _CmEthernetTrafficPortHistoryESP256_Type()
)
cmEthernetTrafficPortHistoryESP256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESP256.setStatus("current")
_CmEthernetTrafficPortHistoryESP512_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESP512_Object = MibTableColumn
cmEthernetTrafficPortHistoryESP512 = _CmEthernetTrafficPortHistoryESP512_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 24),
    _CmEthernetTrafficPortHistoryESP512_Type()
)
cmEthernetTrafficPortHistoryESP512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESP512.setStatus("current")
_CmEthernetTrafficPortHistoryESP1024_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESP1024_Object = MibTableColumn
cmEthernetTrafficPortHistoryESP1024 = _CmEthernetTrafficPortHistoryESP1024_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 25),
    _CmEthernetTrafficPortHistoryESP1024_Type()
)
cmEthernetTrafficPortHistoryESP1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESP1024.setStatus("current")
_CmEthernetTrafficPortHistoryESP1519_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESP1519_Object = MibTableColumn
cmEthernetTrafficPortHistoryESP1519 = _CmEthernetTrafficPortHistoryESP1519_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 26),
    _CmEthernetTrafficPortHistoryESP1519_Type()
)
cmEthernetTrafficPortHistoryESP1519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESP1519.setStatus("current")
_CmEthernetTrafficPortHistoryESUF_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESUF_Object = MibTableColumn
cmEthernetTrafficPortHistoryESUF = _CmEthernetTrafficPortHistoryESUF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 27),
    _CmEthernetTrafficPortHistoryESUF_Type()
)
cmEthernetTrafficPortHistoryESUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESUF.setStatus("current")
_CmEthernetTrafficPortHistoryESUP_Type = PerfCounter64
_CmEthernetTrafficPortHistoryESUP_Object = MibTableColumn
cmEthernetTrafficPortHistoryESUP = _CmEthernetTrafficPortHistoryESUP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 28),
    _CmEthernetTrafficPortHistoryESUP_Type()
)
cmEthernetTrafficPortHistoryESUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryESUP.setStatus("current")
_CmEthernetTrafficPortHistoryL2CPFD_Type = PerfCounter64
_CmEthernetTrafficPortHistoryL2CPFD_Object = MibTableColumn
cmEthernetTrafficPortHistoryL2CPFD = _CmEthernetTrafficPortHistoryL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 29),
    _CmEthernetTrafficPortHistoryL2CPFD_Type()
)
cmEthernetTrafficPortHistoryL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryL2CPFD.setStatus("current")
_CmEthernetTrafficPortHistoryL2CPFP_Type = PerfCounter64
_CmEthernetTrafficPortHistoryL2CPFP_Object = MibTableColumn
cmEthernetTrafficPortHistoryL2CPFP = _CmEthernetTrafficPortHistoryL2CPFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 30),
    _CmEthernetTrafficPortHistoryL2CPFP_Type()
)
cmEthernetTrafficPortHistoryL2CPFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryL2CPFP.setStatus("current")
_CmEthernetTrafficPortHistoryLES_Type = PerfCounter64
_CmEthernetTrafficPortHistoryLES_Object = MibTableColumn
cmEthernetTrafficPortHistoryLES = _CmEthernetTrafficPortHistoryLES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 31),
    _CmEthernetTrafficPortHistoryLES_Type()
)
cmEthernetTrafficPortHistoryLES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryLES.setStatus("deprecated")
_CmEthernetTrafficPortHistoryLBC_Type = Integer32
_CmEthernetTrafficPortHistoryLBC_Object = MibTableColumn
cmEthernetTrafficPortHistoryLBC = _CmEthernetTrafficPortHistoryLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 32),
    _CmEthernetTrafficPortHistoryLBC_Type()
)
cmEthernetTrafficPortHistoryLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryLBC.setStatus("current")
_CmEthernetTrafficPortHistoryOPT_Type = Integer32
_CmEthernetTrafficPortHistoryOPT_Object = MibTableColumn
cmEthernetTrafficPortHistoryOPT = _CmEthernetTrafficPortHistoryOPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 33),
    _CmEthernetTrafficPortHistoryOPT_Type()
)
cmEthernetTrafficPortHistoryOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryOPT.setStatus("current")
_CmEthernetTrafficPortHistoryOPR_Type = Integer32
_CmEthernetTrafficPortHistoryOPR_Object = MibTableColumn
cmEthernetTrafficPortHistoryOPR = _CmEthernetTrafficPortHistoryOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 34),
    _CmEthernetTrafficPortHistoryOPR_Type()
)
cmEthernetTrafficPortHistoryOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryOPR.setStatus("current")
_CmEthernetTrafficPortHistoryAUFD_Type = PerfCounter64
_CmEthernetTrafficPortHistoryAUFD_Object = MibTableColumn
cmEthernetTrafficPortHistoryAUFD = _CmEthernetTrafficPortHistoryAUFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 35),
    _CmEthernetTrafficPortHistoryAUFD_Type()
)
cmEthernetTrafficPortHistoryAUFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryAUFD.setStatus("current")
_CmEthernetTrafficPortHistoryAPFD_Type = PerfCounter64
_CmEthernetTrafficPortHistoryAPFD_Object = MibTableColumn
cmEthernetTrafficPortHistoryAPFD = _CmEthernetTrafficPortHistoryAPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 36),
    _CmEthernetTrafficPortHistoryAPFD_Type()
)
cmEthernetTrafficPortHistoryAPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryAPFD.setStatus("current")
_CmEthernetTrafficPortHistoryABRRx_Type = PerfCounter64
_CmEthernetTrafficPortHistoryABRRx_Object = MibTableColumn
cmEthernetTrafficPortHistoryABRRx = _CmEthernetTrafficPortHistoryABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 37),
    _CmEthernetTrafficPortHistoryABRRx_Type()
)
cmEthernetTrafficPortHistoryABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryABRRx.setStatus("current")
_CmEthernetTrafficPortHistoryABRTx_Type = PerfCounter64
_CmEthernetTrafficPortHistoryABRTx_Object = MibTableColumn
cmEthernetTrafficPortHistoryABRTx = _CmEthernetTrafficPortHistoryABRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 38),
    _CmEthernetTrafficPortHistoryABRTx_Type()
)
cmEthernetTrafficPortHistoryABRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryABRTx.setStatus("current")
_CmEthernetTrafficPortHistoryATFD_Type = PerfCounter64
_CmEthernetTrafficPortHistoryATFD_Object = MibTableColumn
cmEthernetTrafficPortHistoryATFD = _CmEthernetTrafficPortHistoryATFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 39),
    _CmEthernetTrafficPortHistoryATFD_Type()
)
cmEthernetTrafficPortHistoryATFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryATFD.setStatus("current")
_CmEthernetTrafficPortHistoryUAS_Type = PerfCounter64
_CmEthernetTrafficPortHistoryUAS_Object = MibTableColumn
cmEthernetTrafficPortHistoryUAS = _CmEthernetTrafficPortHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 40),
    _CmEthernetTrafficPortHistoryUAS_Type()
)
cmEthernetTrafficPortHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryUAS.setStatus("current")
_CmEthernetTrafficPortHistoryTemp_Type = Integer32
_CmEthernetTrafficPortHistoryTemp_Object = MibTableColumn
cmEthernetTrafficPortHistoryTemp = _CmEthernetTrafficPortHistoryTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 41),
    _CmEthernetTrafficPortHistoryTemp_Type()
)
cmEthernetTrafficPortHistoryTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryTemp.setStatus("current")
_CmEthernetTrafficPortHistoryLkupFails_Type = PerfCounter64
_CmEthernetTrafficPortHistoryLkupFails_Object = MibTableColumn
cmEthernetTrafficPortHistoryLkupFails = _CmEthernetTrafficPortHistoryLkupFails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 42),
    _CmEthernetTrafficPortHistoryLkupFails_Type()
)
cmEthernetTrafficPortHistoryLkupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryLkupFails.setStatus("current")
_CmEthernetTrafficPortHistoryPSC_Type = PerfCounter64
_CmEthernetTrafficPortHistoryPSC_Object = MibTableColumn
cmEthernetTrafficPortHistoryPSC = _CmEthernetTrafficPortHistoryPSC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 43),
    _CmEthernetTrafficPortHistoryPSC_Type()
)
cmEthernetTrafficPortHistoryPSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryPSC.setStatus("current")
_CmEthernetTrafficPortHistoryL2PTRxFramesEncap_Type = PerfCounter64
_CmEthernetTrafficPortHistoryL2PTRxFramesEncap_Object = MibTableColumn
cmEthernetTrafficPortHistoryL2PTRxFramesEncap = _CmEthernetTrafficPortHistoryL2PTRxFramesEncap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 44),
    _CmEthernetTrafficPortHistoryL2PTRxFramesEncap_Type()
)
cmEthernetTrafficPortHistoryL2PTRxFramesEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryL2PTRxFramesEncap.setStatus("current")
_CmEthernetTrafficPortHistoryL2PTTxFramesDecap_Type = PerfCounter64
_CmEthernetTrafficPortHistoryL2PTTxFramesDecap_Object = MibTableColumn
cmEthernetTrafficPortHistoryL2PTTxFramesDecap = _CmEthernetTrafficPortHistoryL2PTTxFramesDecap_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 45),
    _CmEthernetTrafficPortHistoryL2PTTxFramesDecap_Type()
)
cmEthernetTrafficPortHistoryL2PTTxFramesDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryL2PTTxFramesDecap.setStatus("current")
_CmEthernetTrafficPortHistoryIBRMaxRx_Type = PerfCounter64
_CmEthernetTrafficPortHistoryIBRMaxRx_Object = MibTableColumn
cmEthernetTrafficPortHistoryIBRMaxRx = _CmEthernetTrafficPortHistoryIBRMaxRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 46),
    _CmEthernetTrafficPortHistoryIBRMaxRx_Type()
)
cmEthernetTrafficPortHistoryIBRMaxRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryIBRMaxRx.setStatus("current")
_CmEthernetTrafficPortHistoryIBRMaxTx_Type = PerfCounter64
_CmEthernetTrafficPortHistoryIBRMaxTx_Object = MibTableColumn
cmEthernetTrafficPortHistoryIBRMaxTx = _CmEthernetTrafficPortHistoryIBRMaxTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 47),
    _CmEthernetTrafficPortHistoryIBRMaxTx_Type()
)
cmEthernetTrafficPortHistoryIBRMaxTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryIBRMaxTx.setStatus("current")
_CmEthernetTrafficPortHistoryIBRMinRx_Type = PerfCounter64
_CmEthernetTrafficPortHistoryIBRMinRx_Object = MibTableColumn
cmEthernetTrafficPortHistoryIBRMinRx = _CmEthernetTrafficPortHistoryIBRMinRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 48),
    _CmEthernetTrafficPortHistoryIBRMinRx_Type()
)
cmEthernetTrafficPortHistoryIBRMinRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryIBRMinRx.setStatus("current")
_CmEthernetTrafficPortHistoryIBRMinTx_Type = PerfCounter64
_CmEthernetTrafficPortHistoryIBRMinTx_Object = MibTableColumn
cmEthernetTrafficPortHistoryIBRMinTx = _CmEthernetTrafficPortHistoryIBRMinTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 49),
    _CmEthernetTrafficPortHistoryIBRMinTx_Type()
)
cmEthernetTrafficPortHistoryIBRMinTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryIBRMinTx.setStatus("current")
_CmEthernetTrafficPortHistoryIBRRx_Type = PerfCounter64
_CmEthernetTrafficPortHistoryIBRRx_Object = MibTableColumn
cmEthernetTrafficPortHistoryIBRRx = _CmEthernetTrafficPortHistoryIBRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 50),
    _CmEthernetTrafficPortHistoryIBRRx_Type()
)
cmEthernetTrafficPortHistoryIBRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryIBRRx.setStatus("current")
_CmEthernetTrafficPortHistoryIBRTx_Type = PerfCounter64
_CmEthernetTrafficPortHistoryIBRTx_Object = MibTableColumn
cmEthernetTrafficPortHistoryIBRTx = _CmEthernetTrafficPortHistoryIBRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 51),
    _CmEthernetTrafficPortHistoryIBRTx_Type()
)
cmEthernetTrafficPortHistoryIBRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryIBRTx.setStatus("current")
_CmEthernetTrafficPortHistoryFmcd_Type = PerfCounter64
_CmEthernetTrafficPortHistoryFmcd_Object = MibTableColumn
cmEthernetTrafficPortHistoryFmcd = _CmEthernetTrafficPortHistoryFmcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 52),
    _CmEthernetTrafficPortHistoryFmcd_Type()
)
cmEthernetTrafficPortHistoryFmcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryFmcd.setStatus("current")
_CmEthernetTrafficPortHistoryFbcd_Type = PerfCounter64
_CmEthernetTrafficPortHistoryFbcd_Object = MibTableColumn
cmEthernetTrafficPortHistoryFbcd = _CmEthernetTrafficPortHistoryFbcd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 53),
    _CmEthernetTrafficPortHistoryFbcd_Type()
)
cmEthernetTrafficPortHistoryFbcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryFbcd.setStatus("current")
_CmEthernetTrafficPortHistoryAclDropNoMatch_Type = PerfCounter64
_CmEthernetTrafficPortHistoryAclDropNoMatch_Object = MibTableColumn
cmEthernetTrafficPortHistoryAclDropNoMatch = _CmEthernetTrafficPortHistoryAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 54),
    _CmEthernetTrafficPortHistoryAclDropNoMatch_Type()
)
cmEthernetTrafficPortHistoryAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryAclDropNoMatch.setStatus("current")
_CmEthernetTrafficPortHistoryAclFwd2Cpu_Type = PerfCounter64
_CmEthernetTrafficPortHistoryAclFwd2Cpu_Object = MibTableColumn
cmEthernetTrafficPortHistoryAclFwd2Cpu = _CmEthernetTrafficPortHistoryAclFwd2Cpu_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 55),
    _CmEthernetTrafficPortHistoryAclFwd2Cpu_Type()
)
cmEthernetTrafficPortHistoryAclFwd2Cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryAclFwd2Cpu.setStatus("current")
_CmEthernetTrafficPortHistoryDhcpDropNoAssocIf_Type = PerfCounter64
_CmEthernetTrafficPortHistoryDhcpDropNoAssocIf_Object = MibTableColumn
cmEthernetTrafficPortHistoryDhcpDropNoAssocIf = _CmEthernetTrafficPortHistoryDhcpDropNoAssocIf_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 56),
    _CmEthernetTrafficPortHistoryDhcpDropNoAssocIf_Type()
)
cmEthernetTrafficPortHistoryDhcpDropNoAssocIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryDhcpDropNoAssocIf.setStatus("current")
_CmEthernetTrafficPortHistoryDroppedFragmented_Type = PerfCounter64
_CmEthernetTrafficPortHistoryDroppedFragmented_Object = MibTableColumn
cmEthernetTrafficPortHistoryDroppedFragmented = _CmEthernetTrafficPortHistoryDroppedFragmented_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 57),
    _CmEthernetTrafficPortHistoryDroppedFragmented_Type()
)
cmEthernetTrafficPortHistoryDroppedFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryDroppedFragmented.setStatus("current")
_CmEthernetTrafficPortHistoryRLBC_Type = Integer32
_CmEthernetTrafficPortHistoryRLBC_Object = MibTableColumn
cmEthernetTrafficPortHistoryRLBC = _CmEthernetTrafficPortHistoryRLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 58),
    _CmEthernetTrafficPortHistoryRLBC_Type()
)
cmEthernetTrafficPortHistoryRLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryRLBC.setStatus("current")
_CmEthernetTrafficPortHistoryROPT_Type = Integer32
_CmEthernetTrafficPortHistoryROPT_Object = MibTableColumn
cmEthernetTrafficPortHistoryROPT = _CmEthernetTrafficPortHistoryROPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 59),
    _CmEthernetTrafficPortHistoryROPT_Type()
)
cmEthernetTrafficPortHistoryROPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryROPT.setStatus("current")
_CmEthernetTrafficPortHistoryROPR_Type = Integer32
_CmEthernetTrafficPortHistoryROPR_Object = MibTableColumn
cmEthernetTrafficPortHistoryROPR = _CmEthernetTrafficPortHistoryROPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 60),
    _CmEthernetTrafficPortHistoryROPR_Type()
)
cmEthernetTrafficPortHistoryROPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryROPR.setStatus("current")
_CmEthernetTrafficPortHistoryRTemp_Type = Integer32
_CmEthernetTrafficPortHistoryRTemp_Object = MibTableColumn
cmEthernetTrafficPortHistoryRTemp = _CmEthernetTrafficPortHistoryRTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 22, 1, 61),
    _CmEthernetTrafficPortHistoryRTemp_Type()
)
cmEthernetTrafficPortHistoryRTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortHistoryRTemp.setStatus("current")
_CmEthernetTrafficPortThresholdTable_Object = MibTable
cmEthernetTrafficPortThresholdTable = _CmEthernetTrafficPortThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 23)
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdTable.setStatus("current")
_CmEthernetTrafficPortThresholdEntry_Object = MibTableRow
cmEthernetTrafficPortThresholdEntry = _CmEthernetTrafficPortThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 23, 1)
)
cmEthernetTrafficPortThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdEntry.setStatus("current")


class _CmEthernetTrafficPortThresholdIndex_Type(Integer32):
    """Custom type cmEthernetTrafficPortThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmEthernetTrafficPortThresholdIndex_Type.__name__ = "Integer32"
_CmEthernetTrafficPortThresholdIndex_Object = MibTableColumn
cmEthernetTrafficPortThresholdIndex = _CmEthernetTrafficPortThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 23, 1, 1),
    _CmEthernetTrafficPortThresholdIndex_Type()
)
cmEthernetTrafficPortThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdIndex.setStatus("current")
_CmEthernetTrafficPortThresholdInterval_Type = CmPmIntervalType
_CmEthernetTrafficPortThresholdInterval_Object = MibTableColumn
cmEthernetTrafficPortThresholdInterval = _CmEthernetTrafficPortThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 23, 1, 2),
    _CmEthernetTrafficPortThresholdInterval_Type()
)
cmEthernetTrafficPortThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdInterval.setStatus("current")
_CmEthernetTrafficPortThresholdVariable_Type = VariablePointer
_CmEthernetTrafficPortThresholdVariable_Object = MibTableColumn
cmEthernetTrafficPortThresholdVariable = _CmEthernetTrafficPortThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 23, 1, 3),
    _CmEthernetTrafficPortThresholdVariable_Type()
)
cmEthernetTrafficPortThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdVariable.setStatus("current")
_CmEthernetTrafficPortThresholdValueLo_Type = Unsigned32
_CmEthernetTrafficPortThresholdValueLo_Object = MibTableColumn
cmEthernetTrafficPortThresholdValueLo = _CmEthernetTrafficPortThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 23, 1, 4),
    _CmEthernetTrafficPortThresholdValueLo_Type()
)
cmEthernetTrafficPortThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdValueLo.setStatus("current")
_CmEthernetTrafficPortThresholdValueHi_Type = Unsigned32
_CmEthernetTrafficPortThresholdValueHi_Object = MibTableColumn
cmEthernetTrafficPortThresholdValueHi = _CmEthernetTrafficPortThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 23, 1, 5),
    _CmEthernetTrafficPortThresholdValueHi_Type()
)
cmEthernetTrafficPortThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdValueHi.setStatus("current")
_CmEthernetTrafficPortThresholdMonValue_Type = Counter64
_CmEthernetTrafficPortThresholdMonValue_Object = MibTableColumn
cmEthernetTrafficPortThresholdMonValue = _CmEthernetTrafficPortThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 23, 1, 6),
    _CmEthernetTrafficPortThresholdMonValue_Type()
)
cmEthernetTrafficPortThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdMonValue.setStatus("current")
_CmEthernetTrafficPortThresholdVarTable_Object = MibTable
cmEthernetTrafficPortThresholdVarTable = _CmEthernetTrafficPortThresholdVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 24)
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdVarTable.setStatus("current")
_CmEthernetTrafficPortThresholdVarEntry_Object = MibTableRow
cmEthernetTrafficPortThresholdVarEntry = _CmEthernetTrafficPortThresholdVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 24, 1)
)
cmEthernetTrafficPortThresholdVarEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIndex"),
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdVarEntry.setStatus("current")
_CmEthernetTrafficPortThresholdVarOprVariance_Type = Integer32
_CmEthernetTrafficPortThresholdVarOprVariance_Object = MibTableColumn
cmEthernetTrafficPortThresholdVarOprVariance = _CmEthernetTrafficPortThresholdVarOprVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 24, 1, 1),
    _CmEthernetTrafficPortThresholdVarOprVariance_Type()
)
cmEthernetTrafficPortThresholdVarOprVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdVarOprVariance.setStatus("current")
_CmEthernetTrafficPortThresholdVarOptVariance_Type = Integer32
_CmEthernetTrafficPortThresholdVarOptVariance_Object = MibTableColumn
cmEthernetTrafficPortThresholdVarOptVariance = _CmEthernetTrafficPortThresholdVarOptVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 24, 1, 2),
    _CmEthernetTrafficPortThresholdVarOptVariance_Type()
)
cmEthernetTrafficPortThresholdVarOptVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdVarOptVariance.setStatus("current")
_CmFlowPointStatsTable_Object = MibTable
cmFlowPointStatsTable = _CmFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25)
)
if mibBuilder.loadTexts:
    cmFlowPointStatsTable.setStatus("current")
_CmFlowPointStatsEntry_Object = MibTableRow
cmFlowPointStatsEntry = _CmFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1)
)
cmFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    cmFlowPointStatsEntry.setStatus("current")


class _CmFlowPointStatsIndex_Type(Integer32):
    """Custom type cmFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmFlowPointStatsIndex_Type.__name__ = "Integer32"
_CmFlowPointStatsIndex_Object = MibTableColumn
cmFlowPointStatsIndex = _CmFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 1),
    _CmFlowPointStatsIndex_Type()
)
cmFlowPointStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsIndex.setStatus("current")
_CmFlowPointStatsIntervalType_Type = CmPmIntervalType
_CmFlowPointStatsIntervalType_Object = MibTableColumn
cmFlowPointStatsIntervalType = _CmFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 2),
    _CmFlowPointStatsIntervalType_Type()
)
cmFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsIntervalType.setStatus("current")
_CmFlowPointStatsValid_Type = TruthValue
_CmFlowPointStatsValid_Object = MibTableColumn
cmFlowPointStatsValid = _CmFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 3),
    _CmFlowPointStatsValid_Type()
)
cmFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsValid.setStatus("current")
_CmFlowPointStatsAction_Type = CmPmBinAction
_CmFlowPointStatsAction_Object = MibTableColumn
cmFlowPointStatsAction = _CmFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 4),
    _CmFlowPointStatsAction_Type()
)
cmFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlowPointStatsAction.setStatus("current")
_CmFlowPointStatsL2CPFD_Type = PerfCounter64
_CmFlowPointStatsL2CPFD_Object = MibTableColumn
cmFlowPointStatsL2CPFD = _CmFlowPointStatsL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 5),
    _CmFlowPointStatsL2CPFD_Type()
)
cmFlowPointStatsL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsL2CPFD.setStatus("current")
_CmFlowPointStatsABRRx_Type = PerfCounter64
_CmFlowPointStatsABRRx_Object = MibTableColumn
cmFlowPointStatsABRRx = _CmFlowPointStatsABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 6),
    _CmFlowPointStatsABRRx_Type()
)
cmFlowPointStatsABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsABRRx.setStatus("current")
_CmFlowPointStatsABRRLRx_Type = PerfCounter64
_CmFlowPointStatsABRRLRx_Object = MibTableColumn
cmFlowPointStatsABRRLRx = _CmFlowPointStatsABRRLRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 7),
    _CmFlowPointStatsABRRLRx_Type()
)
cmFlowPointStatsABRRLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsABRRLRx.setStatus("current")
_CmFlowPointStatsUAS_Type = PerfCounter64
_CmFlowPointStatsUAS_Object = MibTableColumn
cmFlowPointStatsUAS = _CmFlowPointStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 8),
    _CmFlowPointStatsUAS_Type()
)
cmFlowPointStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsUAS.setStatus("current")
_CmFlowPointStatsSES_Type = PerfCounter64
_CmFlowPointStatsSES_Object = MibTableColumn
cmFlowPointStatsSES = _CmFlowPointStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 9),
    _CmFlowPointStatsSES_Type()
)
cmFlowPointStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsSES.setStatus("current")
_CmFlowPointStatsFMG_Type = PerfCounter64
_CmFlowPointStatsFMG_Object = MibTableColumn
cmFlowPointStatsFMG = _CmFlowPointStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 10),
    _CmFlowPointStatsFMG_Type()
)
cmFlowPointStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFMG.setStatus("current")
_CmFlowPointStatsFMY_Type = PerfCounter64
_CmFlowPointStatsFMY_Object = MibTableColumn
cmFlowPointStatsFMY = _CmFlowPointStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 11),
    _CmFlowPointStatsFMY_Type()
)
cmFlowPointStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFMY.setStatus("current")
_CmFlowPointStatsFMRD_Type = PerfCounter64
_CmFlowPointStatsFMRD_Object = MibTableColumn
cmFlowPointStatsFMRD = _CmFlowPointStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 12),
    _CmFlowPointStatsFMRD_Type()
)
cmFlowPointStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFMRD.setStatus("current")
_CmFlowPointStatsFTD_Type = PerfCounter64
_CmFlowPointStatsFTD_Object = MibTableColumn
cmFlowPointStatsFTD = _CmFlowPointStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 13),
    _CmFlowPointStatsFTD_Type()
)
cmFlowPointStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFTD.setStatus("current")
_CmFlowPointStatsBytesIn_Type = PerfCounter64
_CmFlowPointStatsBytesIn_Object = MibTableColumn
cmFlowPointStatsBytesIn = _CmFlowPointStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 14),
    _CmFlowPointStatsBytesIn_Type()
)
cmFlowPointStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsBytesIn.setStatus("current")
_CmFlowPointStatsBytesOut_Type = PerfCounter64
_CmFlowPointStatsBytesOut_Object = MibTableColumn
cmFlowPointStatsBytesOut = _CmFlowPointStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 15),
    _CmFlowPointStatsBytesOut_Type()
)
cmFlowPointStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsBytesOut.setStatus("current")
_CmFlowPointStatsFREDD_Type = PerfCounter64
_CmFlowPointStatsFREDD_Object = MibTableColumn
cmFlowPointStatsFREDD = _CmFlowPointStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 16),
    _CmFlowPointStatsFREDD_Type()
)
cmFlowPointStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFREDD.setStatus("current")
_CmFlowPointStatsFACLD_Type = PerfCounter64
_CmFlowPointStatsFACLD_Object = MibTableColumn
cmFlowPointStatsFACLD = _CmFlowPointStatsFACLD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 17),
    _CmFlowPointStatsFACLD_Type()
)
cmFlowPointStatsFACLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFACLD.setStatus("current")
_CmFlowPointStatsFMYD_Type = PerfCounter64
_CmFlowPointStatsFMYD_Object = MibTableColumn
cmFlowPointStatsFMYD = _CmFlowPointStatsFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 18),
    _CmFlowPointStatsFMYD_Type()
)
cmFlowPointStatsFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFMYD.setStatus("current")
_CmFlowPointStatsFMGD_Type = PerfCounter64
_CmFlowPointStatsFMGD_Object = MibTableColumn
cmFlowPointStatsFMGD = _CmFlowPointStatsFMGD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 19),
    _CmFlowPointStatsFMGD_Type()
)
cmFlowPointStatsFMGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFMGD.setStatus("current")
_CmFlowPointStatsFD_Type = PerfCounter64
_CmFlowPointStatsFD_Object = MibTableColumn
cmFlowPointStatsFD = _CmFlowPointStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 20),
    _CmFlowPointStatsFD_Type()
)
cmFlowPointStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFD.setStatus("current")
_CmFlowPointStatsFMCD_Type = PerfCounter64
_CmFlowPointStatsFMCD_Object = MibTableColumn
cmFlowPointStatsFMCD = _CmFlowPointStatsFMCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 21),
    _CmFlowPointStatsFMCD_Type()
)
cmFlowPointStatsFMCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFMCD.setStatus("current")
_CmFlowPointStatsFBCD_Type = PerfCounter64
_CmFlowPointStatsFBCD_Object = MibTableColumn
cmFlowPointStatsFBCD = _CmFlowPointStatsFBCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 22),
    _CmFlowPointStatsFBCD_Type()
)
cmFlowPointStatsFBCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFBCD.setStatus("current")
_CmFlowPointStatsBT_Type = PerfCounter64
_CmFlowPointStatsBT_Object = MibTableColumn
cmFlowPointStatsBT = _CmFlowPointStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 23),
    _CmFlowPointStatsBT_Type()
)
cmFlowPointStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsBT.setStatus("current")
_CmFlowPointStatsFLD_Type = PerfCounter64
_CmFlowPointStatsFLD_Object = MibTableColumn
cmFlowPointStatsFLD = _CmFlowPointStatsFLD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 24),
    _CmFlowPointStatsFLD_Type()
)
cmFlowPointStatsFLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFLD.setStatus("current")
_CmFlowPointStatsIBRMax_Type = PerfCounter64
_CmFlowPointStatsIBRMax_Object = MibTableColumn
cmFlowPointStatsIBRMax = _CmFlowPointStatsIBRMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 25),
    _CmFlowPointStatsIBRMax_Type()
)
cmFlowPointStatsIBRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsIBRMax.setStatus("current")
_CmFlowPointStatsIBRRlMax_Type = PerfCounter64
_CmFlowPointStatsIBRRlMax_Object = MibTableColumn
cmFlowPointStatsIBRRlMax = _CmFlowPointStatsIBRRlMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 26),
    _CmFlowPointStatsIBRRlMax_Type()
)
cmFlowPointStatsIBRRlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsIBRRlMax.setStatus("current")
_CmFlowPointStatsIBRMin_Type = PerfCounter64
_CmFlowPointStatsIBRMin_Object = MibTableColumn
cmFlowPointStatsIBRMin = _CmFlowPointStatsIBRMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 27),
    _CmFlowPointStatsIBRMin_Type()
)
cmFlowPointStatsIBRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsIBRMin.setStatus("current")
_CmFlowPointStatsIBRRlMin_Type = PerfCounter64
_CmFlowPointStatsIBRRlMin_Object = MibTableColumn
cmFlowPointStatsIBRRlMin = _CmFlowPointStatsIBRRlMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 28),
    _CmFlowPointStatsIBRRlMin_Type()
)
cmFlowPointStatsIBRRlMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsIBRRlMin.setStatus("current")
_CmFlowPointStatsIBR_Type = PerfCounter64
_CmFlowPointStatsIBR_Object = MibTableColumn
cmFlowPointStatsIBR = _CmFlowPointStatsIBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 29),
    _CmFlowPointStatsIBR_Type()
)
cmFlowPointStatsIBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsIBR.setStatus("current")
_CmFlowPointStatsIBRRl_Type = PerfCounter64
_CmFlowPointStatsIBRRl_Object = MibTableColumn
cmFlowPointStatsIBRRl = _CmFlowPointStatsIBRRl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 30),
    _CmFlowPointStatsIBRRl_Type()
)
cmFlowPointStatsIBRRl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsIBRRl.setStatus("current")
_CmFlowPointStatsFdRxFb_Type = PerfCounter64
_CmFlowPointStatsFdRxFb_Object = MibTableColumn
cmFlowPointStatsFdRxFb = _CmFlowPointStatsFdRxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 31),
    _CmFlowPointStatsFdRxFb_Type()
)
cmFlowPointStatsFdRxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFdRxFb.setStatus("current")
_CmFlowPointStatsFdTxFb_Type = PerfCounter64
_CmFlowPointStatsFdTxFb_Object = MibTableColumn
cmFlowPointStatsFdTxFb = _CmFlowPointStatsFdTxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 32),
    _CmFlowPointStatsFdTxFb_Type()
)
cmFlowPointStatsFdTxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFdTxFb.setStatus("current")
_CmFlowPointStatsFdicd_Type = PerfCounter64
_CmFlowPointStatsFdicd_Object = MibTableColumn
cmFlowPointStatsFdicd = _CmFlowPointStatsFdicd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 33),
    _CmFlowPointStatsFdicd_Type()
)
cmFlowPointStatsFdicd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsFdicd.setStatus("current")
_CmFlowPointStatsNumLearnTableFlushes_Type = PerfCounter64
_CmFlowPointStatsNumLearnTableFlushes_Object = MibTableColumn
cmFlowPointStatsNumLearnTableFlushes = _CmFlowPointStatsNumLearnTableFlushes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 34),
    _CmFlowPointStatsNumLearnTableFlushes_Type()
)
cmFlowPointStatsNumLearnTableFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsNumLearnTableFlushes.setStatus("current")
_CmFlowPointStatsEfFramesDiscarded_Type = PerfCounter64
_CmFlowPointStatsEfFramesDiscarded_Object = MibTableColumn
cmFlowPointStatsEfFramesDiscarded = _CmFlowPointStatsEfFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 35),
    _CmFlowPointStatsEfFramesDiscarded_Type()
)
cmFlowPointStatsEfFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsEfFramesDiscarded.setStatus("current")
_CmFlowPointStatsEfBytesDiscarded_Type = PerfCounter64
_CmFlowPointStatsEfBytesDiscarded_Object = MibTableColumn
cmFlowPointStatsEfBytesDiscarded = _CmFlowPointStatsEfBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 36),
    _CmFlowPointStatsEfBytesDiscarded_Type()
)
cmFlowPointStatsEfBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsEfBytesDiscarded.setStatus("current")
_CmFlowPointStatsAclDropNoMatch_Type = PerfCounter64
_CmFlowPointStatsAclDropNoMatch_Object = MibTableColumn
cmFlowPointStatsAclDropNoMatch = _CmFlowPointStatsAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 37),
    _CmFlowPointStatsAclDropNoMatch_Type()
)
cmFlowPointStatsAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsAclDropNoMatch.setStatus("current")
_CmFlowPointStatsAclRuleDrop_Type = PerfCounter64
_CmFlowPointStatsAclRuleDrop_Object = MibTableColumn
cmFlowPointStatsAclRuleDrop = _CmFlowPointStatsAclRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 25, 1, 38),
    _CmFlowPointStatsAclRuleDrop_Type()
)
cmFlowPointStatsAclRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointStatsAclRuleDrop.setStatus("current")
_CmFlowPointHistoryTable_Object = MibTable
cmFlowPointHistoryTable = _CmFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26)
)
if mibBuilder.loadTexts:
    cmFlowPointHistoryTable.setStatus("current")
_CmFlowPointHistoryEntry_Object = MibTableRow
cmFlowPointHistoryEntry = _CmFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1)
)
cmFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowPointStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmFlowPointHistoryEntry.setStatus("current")


class _CmFlowPointHistoryIndex_Type(Integer32):
    """Custom type cmFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmFlowPointHistoryIndex_Type.__name__ = "Integer32"
_CmFlowPointHistoryIndex_Object = MibTableColumn
cmFlowPointHistoryIndex = _CmFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 1),
    _CmFlowPointHistoryIndex_Type()
)
cmFlowPointHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryIndex.setStatus("current")
_CmFlowPointHistoryTime_Type = DateAndTime
_CmFlowPointHistoryTime_Object = MibTableColumn
cmFlowPointHistoryTime = _CmFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 2),
    _CmFlowPointHistoryTime_Type()
)
cmFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryTime.setStatus("current")
_CmFlowPointHistoryValid_Type = TruthValue
_CmFlowPointHistoryValid_Object = MibTableColumn
cmFlowPointHistoryValid = _CmFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 3),
    _CmFlowPointHistoryValid_Type()
)
cmFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryValid.setStatus("current")
_CmFlowPointHistoryAction_Type = CmPmBinAction
_CmFlowPointHistoryAction_Object = MibTableColumn
cmFlowPointHistoryAction = _CmFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 4),
    _CmFlowPointHistoryAction_Type()
)
cmFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlowPointHistoryAction.setStatus("current")
_CmFlowPointHistoryL2CPFD_Type = PerfCounter64
_CmFlowPointHistoryL2CPFD_Object = MibTableColumn
cmFlowPointHistoryL2CPFD = _CmFlowPointHistoryL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 5),
    _CmFlowPointHistoryL2CPFD_Type()
)
cmFlowPointHistoryL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryL2CPFD.setStatus("current")
_CmFlowPointHistoryABRRx_Type = PerfCounter64
_CmFlowPointHistoryABRRx_Object = MibTableColumn
cmFlowPointHistoryABRRx = _CmFlowPointHistoryABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 6),
    _CmFlowPointHistoryABRRx_Type()
)
cmFlowPointHistoryABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryABRRx.setStatus("current")
_CmFlowPointHistoryABRRLRx_Type = PerfCounter64
_CmFlowPointHistoryABRRLRx_Object = MibTableColumn
cmFlowPointHistoryABRRLRx = _CmFlowPointHistoryABRRLRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 7),
    _CmFlowPointHistoryABRRLRx_Type()
)
cmFlowPointHistoryABRRLRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryABRRLRx.setStatus("current")
_CmFlowPointHistoryUAS_Type = PerfCounter64
_CmFlowPointHistoryUAS_Object = MibTableColumn
cmFlowPointHistoryUAS = _CmFlowPointHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 8),
    _CmFlowPointHistoryUAS_Type()
)
cmFlowPointHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryUAS.setStatus("current")
_CmFlowPointHistorySES_Type = PerfCounter64
_CmFlowPointHistorySES_Object = MibTableColumn
cmFlowPointHistorySES = _CmFlowPointHistorySES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 9),
    _CmFlowPointHistorySES_Type()
)
cmFlowPointHistorySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistorySES.setStatus("current")
_CmFlowPointHistoryFMG_Type = PerfCounter64
_CmFlowPointHistoryFMG_Object = MibTableColumn
cmFlowPointHistoryFMG = _CmFlowPointHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 10),
    _CmFlowPointHistoryFMG_Type()
)
cmFlowPointHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFMG.setStatus("current")
_CmFlowPointHistoryFMY_Type = PerfCounter64
_CmFlowPointHistoryFMY_Object = MibTableColumn
cmFlowPointHistoryFMY = _CmFlowPointHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 11),
    _CmFlowPointHistoryFMY_Type()
)
cmFlowPointHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFMY.setStatus("current")
_CmFlowPointHistoryFMRD_Type = PerfCounter64
_CmFlowPointHistoryFMRD_Object = MibTableColumn
cmFlowPointHistoryFMRD = _CmFlowPointHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 12),
    _CmFlowPointHistoryFMRD_Type()
)
cmFlowPointHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFMRD.setStatus("current")
_CmFlowPointHistoryFTD_Type = PerfCounter64
_CmFlowPointHistoryFTD_Object = MibTableColumn
cmFlowPointHistoryFTD = _CmFlowPointHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 13),
    _CmFlowPointHistoryFTD_Type()
)
cmFlowPointHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFTD.setStatus("current")
_CmFlowPointHistoryBytesIn_Type = PerfCounter64
_CmFlowPointHistoryBytesIn_Object = MibTableColumn
cmFlowPointHistoryBytesIn = _CmFlowPointHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 14),
    _CmFlowPointHistoryBytesIn_Type()
)
cmFlowPointHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryBytesIn.setStatus("current")
_CmFlowPointHistoryBytesOut_Type = PerfCounter64
_CmFlowPointHistoryBytesOut_Object = MibTableColumn
cmFlowPointHistoryBytesOut = _CmFlowPointHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 15),
    _CmFlowPointHistoryBytesOut_Type()
)
cmFlowPointHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryBytesOut.setStatus("current")
_CmFlowPointHistoryFREDD_Type = PerfCounter64
_CmFlowPointHistoryFREDD_Object = MibTableColumn
cmFlowPointHistoryFREDD = _CmFlowPointHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 16),
    _CmFlowPointHistoryFREDD_Type()
)
cmFlowPointHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFREDD.setStatus("current")
_CmFlowPointHistoryFACLD_Type = PerfCounter64
_CmFlowPointHistoryFACLD_Object = MibTableColumn
cmFlowPointHistoryFACLD = _CmFlowPointHistoryFACLD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 17),
    _CmFlowPointHistoryFACLD_Type()
)
cmFlowPointHistoryFACLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFACLD.setStatus("current")
_CmFlowPointHistoryFMYD_Type = PerfCounter64
_CmFlowPointHistoryFMYD_Object = MibTableColumn
cmFlowPointHistoryFMYD = _CmFlowPointHistoryFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 18),
    _CmFlowPointHistoryFMYD_Type()
)
cmFlowPointHistoryFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFMYD.setStatus("current")
_CmFlowPointHistoryFMGD_Type = PerfCounter64
_CmFlowPointHistoryFMGD_Object = MibTableColumn
cmFlowPointHistoryFMGD = _CmFlowPointHistoryFMGD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 19),
    _CmFlowPointHistoryFMGD_Type()
)
cmFlowPointHistoryFMGD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFMGD.setStatus("current")
_CmFlowPointHistoryFD_Type = PerfCounter64
_CmFlowPointHistoryFD_Object = MibTableColumn
cmFlowPointHistoryFD = _CmFlowPointHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 20),
    _CmFlowPointHistoryFD_Type()
)
cmFlowPointHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFD.setStatus("current")
_CmFlowPointHistoryFMCD_Type = PerfCounter64
_CmFlowPointHistoryFMCD_Object = MibTableColumn
cmFlowPointHistoryFMCD = _CmFlowPointHistoryFMCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 21),
    _CmFlowPointHistoryFMCD_Type()
)
cmFlowPointHistoryFMCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFMCD.setStatus("current")
_CmFlowPointHistoryFBCD_Type = PerfCounter64
_CmFlowPointHistoryFBCD_Object = MibTableColumn
cmFlowPointHistoryFBCD = _CmFlowPointHistoryFBCD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 22),
    _CmFlowPointHistoryFBCD_Type()
)
cmFlowPointHistoryFBCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFBCD.setStatus("current")
_CmFlowPointHistoryBT_Type = PerfCounter64
_CmFlowPointHistoryBT_Object = MibTableColumn
cmFlowPointHistoryBT = _CmFlowPointHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 23),
    _CmFlowPointHistoryBT_Type()
)
cmFlowPointHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryBT.setStatus("current")
_CmFlowPointHistoryFLD_Type = PerfCounter64
_CmFlowPointHistoryFLD_Object = MibTableColumn
cmFlowPointHistoryFLD = _CmFlowPointHistoryFLD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 24),
    _CmFlowPointHistoryFLD_Type()
)
cmFlowPointHistoryFLD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFLD.setStatus("current")
_CmFlowPointHistoryIBRMax_Type = PerfCounter64
_CmFlowPointHistoryIBRMax_Object = MibTableColumn
cmFlowPointHistoryIBRMax = _CmFlowPointHistoryIBRMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 25),
    _CmFlowPointHistoryIBRMax_Type()
)
cmFlowPointHistoryIBRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryIBRMax.setStatus("current")
_CmFlowPointHistoryIBRRlMax_Type = PerfCounter64
_CmFlowPointHistoryIBRRlMax_Object = MibTableColumn
cmFlowPointHistoryIBRRlMax = _CmFlowPointHistoryIBRRlMax_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 26),
    _CmFlowPointHistoryIBRRlMax_Type()
)
cmFlowPointHistoryIBRRlMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryIBRRlMax.setStatus("current")
_CmFlowPointHistoryIBRMin_Type = PerfCounter64
_CmFlowPointHistoryIBRMin_Object = MibTableColumn
cmFlowPointHistoryIBRMin = _CmFlowPointHistoryIBRMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 27),
    _CmFlowPointHistoryIBRMin_Type()
)
cmFlowPointHistoryIBRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryIBRMin.setStatus("current")
_CmFlowPointHistoryIBRRlMin_Type = PerfCounter64
_CmFlowPointHistoryIBRRlMin_Object = MibTableColumn
cmFlowPointHistoryIBRRlMin = _CmFlowPointHistoryIBRRlMin_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 28),
    _CmFlowPointHistoryIBRRlMin_Type()
)
cmFlowPointHistoryIBRRlMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryIBRRlMin.setStatus("current")
_CmFlowPointHistoryIBR_Type = PerfCounter64
_CmFlowPointHistoryIBR_Object = MibTableColumn
cmFlowPointHistoryIBR = _CmFlowPointHistoryIBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 29),
    _CmFlowPointHistoryIBR_Type()
)
cmFlowPointHistoryIBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryIBR.setStatus("current")
_CmFlowPointHistoryIBRRl_Type = PerfCounter64
_CmFlowPointHistoryIBRRl_Object = MibTableColumn
cmFlowPointHistoryIBRRl = _CmFlowPointHistoryIBRRl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 30),
    _CmFlowPointHistoryIBRRl_Type()
)
cmFlowPointHistoryIBRRl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryIBRRl.setStatus("current")
_CmFlowPointHistoryFdRxFb_Type = PerfCounter64
_CmFlowPointHistoryFdRxFb_Object = MibTableColumn
cmFlowPointHistoryFdRxFb = _CmFlowPointHistoryFdRxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 31),
    _CmFlowPointHistoryFdRxFb_Type()
)
cmFlowPointHistoryFdRxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFdRxFb.setStatus("current")
_CmFlowPointHistoryFdTxFb_Type = PerfCounter64
_CmFlowPointHistoryFdTxFb_Object = MibTableColumn
cmFlowPointHistoryFdTxFb = _CmFlowPointHistoryFdTxFb_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 32),
    _CmFlowPointHistoryFdTxFb_Type()
)
cmFlowPointHistoryFdTxFb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFdTxFb.setStatus("current")
_CmFlowPointHistoryFdicd_Type = PerfCounter64
_CmFlowPointHistoryFdicd_Object = MibTableColumn
cmFlowPointHistoryFdicd = _CmFlowPointHistoryFdicd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 33),
    _CmFlowPointHistoryFdicd_Type()
)
cmFlowPointHistoryFdicd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryFdicd.setStatus("current")
_CmFlowPointHistoryNumLearnTableFlushes_Type = PerfCounter64
_CmFlowPointHistoryNumLearnTableFlushes_Object = MibTableColumn
cmFlowPointHistoryNumLearnTableFlushes = _CmFlowPointHistoryNumLearnTableFlushes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 34),
    _CmFlowPointHistoryNumLearnTableFlushes_Type()
)
cmFlowPointHistoryNumLearnTableFlushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryNumLearnTableFlushes.setStatus("current")
_CmFlowPointHistoryEfFramesDiscarded_Type = PerfCounter64
_CmFlowPointHistoryEfFramesDiscarded_Object = MibTableColumn
cmFlowPointHistoryEfFramesDiscarded = _CmFlowPointHistoryEfFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 35),
    _CmFlowPointHistoryEfFramesDiscarded_Type()
)
cmFlowPointHistoryEfFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryEfFramesDiscarded.setStatus("current")
_CmFlowPointHistoryEfBytesDiscarded_Type = PerfCounter64
_CmFlowPointHistoryEfBytesDiscarded_Object = MibTableColumn
cmFlowPointHistoryEfBytesDiscarded = _CmFlowPointHistoryEfBytesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 36),
    _CmFlowPointHistoryEfBytesDiscarded_Type()
)
cmFlowPointHistoryEfBytesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryEfBytesDiscarded.setStatus("current")
_CmFlowPointHistoryAclDropNoMatch_Type = PerfCounter64
_CmFlowPointHistoryAclDropNoMatch_Object = MibTableColumn
cmFlowPointHistoryAclDropNoMatch = _CmFlowPointHistoryAclDropNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 37),
    _CmFlowPointHistoryAclDropNoMatch_Type()
)
cmFlowPointHistoryAclDropNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryAclDropNoMatch.setStatus("current")
_CmFlowPointHistoryAclRuleDrop_Type = PerfCounter64
_CmFlowPointHistoryAclRuleDrop_Object = MibTableColumn
cmFlowPointHistoryAclRuleDrop = _CmFlowPointHistoryAclRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 26, 1, 38),
    _CmFlowPointHistoryAclRuleDrop_Type()
)
cmFlowPointHistoryAclRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointHistoryAclRuleDrop.setStatus("current")
_CmFlowPointThresholdTable_Object = MibTable
cmFlowPointThresholdTable = _CmFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 27)
)
if mibBuilder.loadTexts:
    cmFlowPointThresholdTable.setStatus("current")
_CmFlowPointThresholdEntry_Object = MibTableRow
cmFlowPointThresholdEntry = _CmFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 27, 1)
)
cmFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowPointStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmFlowPointThresholdEntry.setStatus("current")


class _CmFlowPointThresholdIndex_Type(Integer32):
    """Custom type cmFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmFlowPointThresholdIndex_Type.__name__ = "Integer32"
_CmFlowPointThresholdIndex_Object = MibTableColumn
cmFlowPointThresholdIndex = _CmFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 27, 1, 1),
    _CmFlowPointThresholdIndex_Type()
)
cmFlowPointThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointThresholdIndex.setStatus("current")
_CmFlowPointThresholdInterval_Type = CmPmIntervalType
_CmFlowPointThresholdInterval_Object = MibTableColumn
cmFlowPointThresholdInterval = _CmFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 27, 1, 2),
    _CmFlowPointThresholdInterval_Type()
)
cmFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointThresholdInterval.setStatus("current")
_CmFlowPointThresholdVariable_Type = VariablePointer
_CmFlowPointThresholdVariable_Object = MibTableColumn
cmFlowPointThresholdVariable = _CmFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 27, 1, 3),
    _CmFlowPointThresholdVariable_Type()
)
cmFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointThresholdVariable.setStatus("current")
_CmFlowPointThresholdValueLo_Type = Unsigned32
_CmFlowPointThresholdValueLo_Object = MibTableColumn
cmFlowPointThresholdValueLo = _CmFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 27, 1, 4),
    _CmFlowPointThresholdValueLo_Type()
)
cmFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlowPointThresholdValueLo.setStatus("current")
_CmFlowPointThresholdValueHi_Type = Unsigned32
_CmFlowPointThresholdValueHi_Object = MibTableColumn
cmFlowPointThresholdValueHi = _CmFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 27, 1, 5),
    _CmFlowPointThresholdValueHi_Type()
)
cmFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFlowPointThresholdValueHi.setStatus("current")
_CmFlowPointThresholdMonValue_Type = Counter64
_CmFlowPointThresholdMonValue_Object = MibTableColumn
cmFlowPointThresholdMonValue = _CmFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 27, 1, 6),
    _CmFlowPointThresholdMonValue_Type()
)
cmFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowPointThresholdMonValue.setStatus("current")
_CmOAMFlowPointStatsTable_Object = MibTable
cmOAMFlowPointStatsTable = _CmOAMFlowPointStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 28)
)
if mibBuilder.loadTexts:
    cmOAMFlowPointStatsTable.setStatus("current")
_CmOAMFlowPointStatsEntry_Object = MibTableRow
cmOAMFlowPointStatsEntry = _CmOAMFlowPointStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 28, 1)
)
cmOAMFlowPointStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmOAMFlowPointIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsIndex"),
)
if mibBuilder.loadTexts:
    cmOAMFlowPointStatsEntry.setStatus("current")


class _CmOAMFlowPointStatsIndex_Type(Integer32):
    """Custom type cmOAMFlowPointStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmOAMFlowPointStatsIndex_Type.__name__ = "Integer32"
_CmOAMFlowPointStatsIndex_Object = MibTableColumn
cmOAMFlowPointStatsIndex = _CmOAMFlowPointStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 28, 1, 1),
    _CmOAMFlowPointStatsIndex_Type()
)
cmOAMFlowPointStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointStatsIndex.setStatus("current")
_CmOAMFlowPointStatsIntervalType_Type = CmPmIntervalType
_CmOAMFlowPointStatsIntervalType_Object = MibTableColumn
cmOAMFlowPointStatsIntervalType = _CmOAMFlowPointStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 28, 1, 2),
    _CmOAMFlowPointStatsIntervalType_Type()
)
cmOAMFlowPointStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointStatsIntervalType.setStatus("current")
_CmOAMFlowPointStatsValid_Type = TruthValue
_CmOAMFlowPointStatsValid_Object = MibTableColumn
cmOAMFlowPointStatsValid = _CmOAMFlowPointStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 28, 1, 3),
    _CmOAMFlowPointStatsValid_Type()
)
cmOAMFlowPointStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointStatsValid.setStatus("current")
_CmOAMFlowPointStatsAction_Type = CmPmBinAction
_CmOAMFlowPointStatsAction_Object = MibTableColumn
cmOAMFlowPointStatsAction = _CmOAMFlowPointStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 28, 1, 4),
    _CmOAMFlowPointStatsAction_Type()
)
cmOAMFlowPointStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOAMFlowPointStatsAction.setStatus("current")
_CmOAMFlowPointStatsUAS_Type = PerfCounter64
_CmOAMFlowPointStatsUAS_Object = MibTableColumn
cmOAMFlowPointStatsUAS = _CmOAMFlowPointStatsUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 28, 1, 5),
    _CmOAMFlowPointStatsUAS_Type()
)
cmOAMFlowPointStatsUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointStatsUAS.setStatus("current")
_CmOAMFlowPointStatsSES_Type = PerfCounter64
_CmOAMFlowPointStatsSES_Object = MibTableColumn
cmOAMFlowPointStatsSES = _CmOAMFlowPointStatsSES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 28, 1, 6),
    _CmOAMFlowPointStatsSES_Type()
)
cmOAMFlowPointStatsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointStatsSES.setStatus("current")
_CmOAMFlowPointHistoryTable_Object = MibTable
cmOAMFlowPointHistoryTable = _CmOAMFlowPointHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 29)
)
if mibBuilder.loadTexts:
    cmOAMFlowPointHistoryTable.setStatus("current")
_CmOAMFlowPointHistoryEntry_Object = MibTableRow
cmOAMFlowPointHistoryEntry = _CmOAMFlowPointHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 29, 1)
)
cmOAMFlowPointHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmOAMFlowPointIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmOAMFlowPointHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmOAMFlowPointHistoryEntry.setStatus("current")


class _CmOAMFlowPointHistoryIndex_Type(Integer32):
    """Custom type cmOAMFlowPointHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmOAMFlowPointHistoryIndex_Type.__name__ = "Integer32"
_CmOAMFlowPointHistoryIndex_Object = MibTableColumn
cmOAMFlowPointHistoryIndex = _CmOAMFlowPointHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 29, 1, 1),
    _CmOAMFlowPointHistoryIndex_Type()
)
cmOAMFlowPointHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointHistoryIndex.setStatus("current")
_CmOAMFlowPointHistoryTime_Type = DateAndTime
_CmOAMFlowPointHistoryTime_Object = MibTableColumn
cmOAMFlowPointHistoryTime = _CmOAMFlowPointHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 29, 1, 2),
    _CmOAMFlowPointHistoryTime_Type()
)
cmOAMFlowPointHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointHistoryTime.setStatus("current")
_CmOAMFlowPointHistoryValid_Type = TruthValue
_CmOAMFlowPointHistoryValid_Object = MibTableColumn
cmOAMFlowPointHistoryValid = _CmOAMFlowPointHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 29, 1, 3),
    _CmOAMFlowPointHistoryValid_Type()
)
cmOAMFlowPointHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointHistoryValid.setStatus("current")
_CmOAMFlowPointHistoryAction_Type = CmPmBinAction
_CmOAMFlowPointHistoryAction_Object = MibTableColumn
cmOAMFlowPointHistoryAction = _CmOAMFlowPointHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 29, 1, 4),
    _CmOAMFlowPointHistoryAction_Type()
)
cmOAMFlowPointHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOAMFlowPointHistoryAction.setStatus("current")
_CmOAMFlowPointHistoryUAS_Type = PerfCounter64
_CmOAMFlowPointHistoryUAS_Object = MibTableColumn
cmOAMFlowPointHistoryUAS = _CmOAMFlowPointHistoryUAS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 29, 1, 5),
    _CmOAMFlowPointHistoryUAS_Type()
)
cmOAMFlowPointHistoryUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointHistoryUAS.setStatus("current")
_CmOAMFlowPointHistorySES_Type = PerfCounter64
_CmOAMFlowPointHistorySES_Object = MibTableColumn
cmOAMFlowPointHistorySES = _CmOAMFlowPointHistorySES_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 29, 1, 6),
    _CmOAMFlowPointHistorySES_Type()
)
cmOAMFlowPointHistorySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointHistorySES.setStatus("current")
_CmOAMFlowPointThresholdTable_Object = MibTable
cmOAMFlowPointThresholdTable = _CmOAMFlowPointThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 30)
)
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdTable.setStatus("current")
_CmOAMFlowPointThresholdEntry_Object = MibTableRow
cmOAMFlowPointThresholdEntry = _CmOAMFlowPointThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 30, 1)
)
cmOAMFlowPointThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmOAMFlowPointIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdEntry.setStatus("current")


class _CmOAMFlowPointThresholdIndex_Type(Integer32):
    """Custom type cmOAMFlowPointThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmOAMFlowPointThresholdIndex_Type.__name__ = "Integer32"
_CmOAMFlowPointThresholdIndex_Object = MibTableColumn
cmOAMFlowPointThresholdIndex = _CmOAMFlowPointThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 30, 1, 1),
    _CmOAMFlowPointThresholdIndex_Type()
)
cmOAMFlowPointThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdIndex.setStatus("current")
_CmOAMFlowPointThresholdInterval_Type = CmPmIntervalType
_CmOAMFlowPointThresholdInterval_Object = MibTableColumn
cmOAMFlowPointThresholdInterval = _CmOAMFlowPointThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 30, 1, 2),
    _CmOAMFlowPointThresholdInterval_Type()
)
cmOAMFlowPointThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdInterval.setStatus("current")
_CmOAMFlowPointThresholdVariable_Type = VariablePointer
_CmOAMFlowPointThresholdVariable_Object = MibTableColumn
cmOAMFlowPointThresholdVariable = _CmOAMFlowPointThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 30, 1, 3),
    _CmOAMFlowPointThresholdVariable_Type()
)
cmOAMFlowPointThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdVariable.setStatus("current")
_CmOAMFlowPointThresholdValueLo_Type = Unsigned32
_CmOAMFlowPointThresholdValueLo_Object = MibTableColumn
cmOAMFlowPointThresholdValueLo = _CmOAMFlowPointThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 30, 1, 4),
    _CmOAMFlowPointThresholdValueLo_Type()
)
cmOAMFlowPointThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdValueLo.setStatus("current")
_CmOAMFlowPointThresholdValueHi_Type = Unsigned32
_CmOAMFlowPointThresholdValueHi_Object = MibTableColumn
cmOAMFlowPointThresholdValueHi = _CmOAMFlowPointThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 30, 1, 5),
    _CmOAMFlowPointThresholdValueHi_Type()
)
cmOAMFlowPointThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdValueHi.setStatus("current")
_CmOAMFlowPointThresholdMonValue_Type = Counter64
_CmOAMFlowPointThresholdMonValue_Object = MibTableColumn
cmOAMFlowPointThresholdMonValue = _CmOAMFlowPointThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 30, 1, 6),
    _CmOAMFlowPointThresholdMonValue_Type()
)
cmOAMFlowPointThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdMonValue.setStatus("current")
_CmQosPolicerV2StatsTable_Object = MibTable
cmQosPolicerV2StatsTable = _CmQosPolicerV2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31)
)
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsTable.setStatus("current")
_CmQosPolicerV2StatsEntry_Object = MibTableRow
cmQosPolicerV2StatsEntry = _CmQosPolicerV2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1)
)
cmQosPolicerV2StatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "cmQosPolicerV2Index"),
    (0, "CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsIndex"),
)
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsEntry.setStatus("current")


class _CmQosPolicerV2StatsIndex_Type(Integer32):
    """Custom type cmQosPolicerV2StatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosPolicerV2StatsIndex_Type.__name__ = "Integer32"
_CmQosPolicerV2StatsIndex_Object = MibTableColumn
cmQosPolicerV2StatsIndex = _CmQosPolicerV2StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 1),
    _CmQosPolicerV2StatsIndex_Type()
)
cmQosPolicerV2StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsIndex.setStatus("current")
_CmQosPolicerV2StatsIntervalType_Type = CmPmIntervalType
_CmQosPolicerV2StatsIntervalType_Object = MibTableColumn
cmQosPolicerV2StatsIntervalType = _CmQosPolicerV2StatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 2),
    _CmQosPolicerV2StatsIntervalType_Type()
)
cmQosPolicerV2StatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsIntervalType.setStatus("current")
_CmQosPolicerV2StatsValid_Type = TruthValue
_CmQosPolicerV2StatsValid_Object = MibTableColumn
cmQosPolicerV2StatsValid = _CmQosPolicerV2StatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 3),
    _CmQosPolicerV2StatsValid_Type()
)
cmQosPolicerV2StatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsValid.setStatus("current")
_CmQosPolicerV2StatsAction_Type = CmPmBinAction
_CmQosPolicerV2StatsAction_Object = MibTableColumn
cmQosPolicerV2StatsAction = _CmQosPolicerV2StatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 4),
    _CmQosPolicerV2StatsAction_Type()
)
cmQosPolicerV2StatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsAction.setStatus("current")
_CmQosPolicerV2StatsFMG_Type = PerfCounter64
_CmQosPolicerV2StatsFMG_Object = MibTableColumn
cmQosPolicerV2StatsFMG = _CmQosPolicerV2StatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 5),
    _CmQosPolicerV2StatsFMG_Type()
)
cmQosPolicerV2StatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsFMG.setStatus("current")
_CmQosPolicerV2StatsFMY_Type = PerfCounter64
_CmQosPolicerV2StatsFMY_Object = MibTableColumn
cmQosPolicerV2StatsFMY = _CmQosPolicerV2StatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 6),
    _CmQosPolicerV2StatsFMY_Type()
)
cmQosPolicerV2StatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsFMY.setStatus("current")
_CmQosPolicerV2StatsFMYD_Type = PerfCounter64
_CmQosPolicerV2StatsFMYD_Object = MibTableColumn
cmQosPolicerV2StatsFMYD = _CmQosPolicerV2StatsFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 7),
    _CmQosPolicerV2StatsFMYD_Type()
)
cmQosPolicerV2StatsFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsFMYD.setStatus("current")
_CmQosPolicerV2StatsFMRD_Type = PerfCounter64
_CmQosPolicerV2StatsFMRD_Object = MibTableColumn
cmQosPolicerV2StatsFMRD = _CmQosPolicerV2StatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 8),
    _CmQosPolicerV2StatsFMRD_Type()
)
cmQosPolicerV2StatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsFMRD.setStatus("current")
_CmQosPolicerV2StatsBytesIn_Type = PerfCounter64
_CmQosPolicerV2StatsBytesIn_Object = MibTableColumn
cmQosPolicerV2StatsBytesIn = _CmQosPolicerV2StatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 9),
    _CmQosPolicerV2StatsBytesIn_Type()
)
cmQosPolicerV2StatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsBytesIn.setStatus("current")
_CmQosPolicerV2StatsBytesOut_Type = PerfCounter64
_CmQosPolicerV2StatsBytesOut_Object = MibTableColumn
cmQosPolicerV2StatsBytesOut = _CmQosPolicerV2StatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 10),
    _CmQosPolicerV2StatsBytesOut_Type()
)
cmQosPolicerV2StatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsBytesOut.setStatus("current")
_CmQosPolicerV2StatsABR_Type = PerfCounter64
_CmQosPolicerV2StatsABR_Object = MibTableColumn
cmQosPolicerV2StatsABR = _CmQosPolicerV2StatsABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 31, 1, 11),
    _CmQosPolicerV2StatsABR_Type()
)
cmQosPolicerV2StatsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2StatsABR.setStatus("current")
_CmQosPolicerV2HistoryTable_Object = MibTable
cmQosPolicerV2HistoryTable = _CmQosPolicerV2HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32)
)
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryTable.setStatus("current")
_CmQosPolicerV2HistoryEntry_Object = MibTableRow
cmQosPolicerV2HistoryEntry = _CmQosPolicerV2HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1)
)
cmQosPolicerV2HistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "cmQosPolicerV2Index"),
    (0, "CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryIndex"),
)
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryEntry.setStatus("current")


class _CmQosPolicerV2HistoryIndex_Type(Integer32):
    """Custom type cmQosPolicerV2HistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosPolicerV2HistoryIndex_Type.__name__ = "Integer32"
_CmQosPolicerV2HistoryIndex_Object = MibTableColumn
cmQosPolicerV2HistoryIndex = _CmQosPolicerV2HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 1),
    _CmQosPolicerV2HistoryIndex_Type()
)
cmQosPolicerV2HistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryIndex.setStatus("current")
_CmQosPolicerV2HistoryTime_Type = DateAndTime
_CmQosPolicerV2HistoryTime_Object = MibTableColumn
cmQosPolicerV2HistoryTime = _CmQosPolicerV2HistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 2),
    _CmQosPolicerV2HistoryTime_Type()
)
cmQosPolicerV2HistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryTime.setStatus("current")
_CmQosPolicerV2HistoryValid_Type = TruthValue
_CmQosPolicerV2HistoryValid_Object = MibTableColumn
cmQosPolicerV2HistoryValid = _CmQosPolicerV2HistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 3),
    _CmQosPolicerV2HistoryValid_Type()
)
cmQosPolicerV2HistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryValid.setStatus("current")
_CmQosPolicerV2HistoryAction_Type = CmPmBinAction
_CmQosPolicerV2HistoryAction_Object = MibTableColumn
cmQosPolicerV2HistoryAction = _CmQosPolicerV2HistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 4),
    _CmQosPolicerV2HistoryAction_Type()
)
cmQosPolicerV2HistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryAction.setStatus("current")
_CmQosPolicerV2HistoryFMG_Type = PerfCounter64
_CmQosPolicerV2HistoryFMG_Object = MibTableColumn
cmQosPolicerV2HistoryFMG = _CmQosPolicerV2HistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 5),
    _CmQosPolicerV2HistoryFMG_Type()
)
cmQosPolicerV2HistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryFMG.setStatus("current")
_CmQosPolicerV2HistoryFMY_Type = PerfCounter64
_CmQosPolicerV2HistoryFMY_Object = MibTableColumn
cmQosPolicerV2HistoryFMY = _CmQosPolicerV2HistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 6),
    _CmQosPolicerV2HistoryFMY_Type()
)
cmQosPolicerV2HistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryFMY.setStatus("current")
_CmQosPolicerV2HistoryFMYD_Type = PerfCounter64
_CmQosPolicerV2HistoryFMYD_Object = MibTableColumn
cmQosPolicerV2HistoryFMYD = _CmQosPolicerV2HistoryFMYD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 7),
    _CmQosPolicerV2HistoryFMYD_Type()
)
cmQosPolicerV2HistoryFMYD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryFMYD.setStatus("current")
_CmQosPolicerV2HistoryFMRD_Type = PerfCounter64
_CmQosPolicerV2HistoryFMRD_Object = MibTableColumn
cmQosPolicerV2HistoryFMRD = _CmQosPolicerV2HistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 8),
    _CmQosPolicerV2HistoryFMRD_Type()
)
cmQosPolicerV2HistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryFMRD.setStatus("current")
_CmQosPolicerV2HistoryBytesIn_Type = PerfCounter64
_CmQosPolicerV2HistoryBytesIn_Object = MibTableColumn
cmQosPolicerV2HistoryBytesIn = _CmQosPolicerV2HistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 9),
    _CmQosPolicerV2HistoryBytesIn_Type()
)
cmQosPolicerV2HistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryBytesIn.setStatus("current")
_CmQosPolicerV2HistoryBytesOut_Type = PerfCounter64
_CmQosPolicerV2HistoryBytesOut_Object = MibTableColumn
cmQosPolicerV2HistoryBytesOut = _CmQosPolicerV2HistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 10),
    _CmQosPolicerV2HistoryBytesOut_Type()
)
cmQosPolicerV2HistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryBytesOut.setStatus("current")
_CmQosPolicerV2HistoryABR_Type = PerfCounter64
_CmQosPolicerV2HistoryABR_Object = MibTableColumn
cmQosPolicerV2HistoryABR = _CmQosPolicerV2HistoryABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 32, 1, 11),
    _CmQosPolicerV2HistoryABR_Type()
)
cmQosPolicerV2HistoryABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2HistoryABR.setStatus("current")
_CmQosPolicerV2ThresholdTable_Object = MibTable
cmQosPolicerV2ThresholdTable = _CmQosPolicerV2ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 33)
)
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdTable.setStatus("current")
_CmQosPolicerV2ThresholdEntry_Object = MibTableRow
cmQosPolicerV2ThresholdEntry = _CmQosPolicerV2ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 33, 1)
)
cmQosPolicerV2ThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "cmQosPolicerV2Index"),
    (0, "CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdEntry.setStatus("current")


class _CmQosPolicerV2ThresholdIndex_Type(Integer32):
    """Custom type cmQosPolicerV2ThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosPolicerV2ThresholdIndex_Type.__name__ = "Integer32"
_CmQosPolicerV2ThresholdIndex_Object = MibTableColumn
cmQosPolicerV2ThresholdIndex = _CmQosPolicerV2ThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 33, 1, 1),
    _CmQosPolicerV2ThresholdIndex_Type()
)
cmQosPolicerV2ThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdIndex.setStatus("current")
_CmQosPolicerV2ThresholdInterval_Type = CmPmIntervalType
_CmQosPolicerV2ThresholdInterval_Object = MibTableColumn
cmQosPolicerV2ThresholdInterval = _CmQosPolicerV2ThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 33, 1, 2),
    _CmQosPolicerV2ThresholdInterval_Type()
)
cmQosPolicerV2ThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdInterval.setStatus("current")
_CmQosPolicerV2ThresholdVariable_Type = VariablePointer
_CmQosPolicerV2ThresholdVariable_Object = MibTableColumn
cmQosPolicerV2ThresholdVariable = _CmQosPolicerV2ThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 33, 1, 3),
    _CmQosPolicerV2ThresholdVariable_Type()
)
cmQosPolicerV2ThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdVariable.setStatus("current")
_CmQosPolicerV2ThresholdValueLo_Type = Unsigned32
_CmQosPolicerV2ThresholdValueLo_Object = MibTableColumn
cmQosPolicerV2ThresholdValueLo = _CmQosPolicerV2ThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 33, 1, 4),
    _CmQosPolicerV2ThresholdValueLo_Type()
)
cmQosPolicerV2ThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdValueLo.setStatus("current")
_CmQosPolicerV2ThresholdValueHi_Type = Unsigned32
_CmQosPolicerV2ThresholdValueHi_Object = MibTableColumn
cmQosPolicerV2ThresholdValueHi = _CmQosPolicerV2ThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 33, 1, 5),
    _CmQosPolicerV2ThresholdValueHi_Type()
)
cmQosPolicerV2ThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdValueHi.setStatus("current")
_CmQosPolicerV2ThresholdMonValue_Type = Counter64
_CmQosPolicerV2ThresholdMonValue_Object = MibTableColumn
cmQosPolicerV2ThresholdMonValue = _CmQosPolicerV2ThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 33, 1, 6),
    _CmQosPolicerV2ThresholdMonValue_Type()
)
cmQosPolicerV2ThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdMonValue.setStatus("current")
_CmQosShaperV2StatsTable_Object = MibTable
cmQosShaperV2StatsTable = _CmQosShaperV2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34)
)
if mibBuilder.loadTexts:
    cmQosShaperV2StatsTable.setStatus("current")
_CmQosShaperV2StatsEntry_Object = MibTableRow
cmQosShaperV2StatsEntry = _CmQosShaperV2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1)
)
cmQosShaperV2StatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperV2Index"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperV2StatsIndex"),
)
if mibBuilder.loadTexts:
    cmQosShaperV2StatsEntry.setStatus("current")


class _CmQosShaperV2StatsIndex_Type(Integer32):
    """Custom type cmQosShaperV2StatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosShaperV2StatsIndex_Type.__name__ = "Integer32"
_CmQosShaperV2StatsIndex_Object = MibTableColumn
cmQosShaperV2StatsIndex = _CmQosShaperV2StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 1),
    _CmQosShaperV2StatsIndex_Type()
)
cmQosShaperV2StatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsIndex.setStatus("current")
_CmQosShaperV2StatsIntervalType_Type = CmPmIntervalType
_CmQosShaperV2StatsIntervalType_Object = MibTableColumn
cmQosShaperV2StatsIntervalType = _CmQosShaperV2StatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 2),
    _CmQosShaperV2StatsIntervalType_Type()
)
cmQosShaperV2StatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsIntervalType.setStatus("current")
_CmQosShaperV2StatsValid_Type = TruthValue
_CmQosShaperV2StatsValid_Object = MibTableColumn
cmQosShaperV2StatsValid = _CmQosShaperV2StatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 3),
    _CmQosShaperV2StatsValid_Type()
)
cmQosShaperV2StatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsValid.setStatus("current")
_CmQosShaperV2StatsAction_Type = CmPmBinAction
_CmQosShaperV2StatsAction_Object = MibTableColumn
cmQosShaperV2StatsAction = _CmQosShaperV2StatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 4),
    _CmQosShaperV2StatsAction_Type()
)
cmQosShaperV2StatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsAction.setStatus("current")
_CmQosShaperV2StatsBT_Type = PerfCounter64
_CmQosShaperV2StatsBT_Object = MibTableColumn
cmQosShaperV2StatsBT = _CmQosShaperV2StatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 5),
    _CmQosShaperV2StatsBT_Type()
)
cmQosShaperV2StatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsBT.setStatus("current")
_CmQosShaperV2StatsBTD_Type = PerfCounter64
_CmQosShaperV2StatsBTD_Object = MibTableColumn
cmQosShaperV2StatsBTD = _CmQosShaperV2StatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 6),
    _CmQosShaperV2StatsBTD_Type()
)
cmQosShaperV2StatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsBTD.setStatus("current")
_CmQosShaperV2StatsFD_Type = PerfCounter64
_CmQosShaperV2StatsFD_Object = MibTableColumn
cmQosShaperV2StatsFD = _CmQosShaperV2StatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 7),
    _CmQosShaperV2StatsFD_Type()
)
cmQosShaperV2StatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsFD.setStatus("current")
_CmQosShaperV2StatsFTD_Type = PerfCounter64
_CmQosShaperV2StatsFTD_Object = MibTableColumn
cmQosShaperV2StatsFTD = _CmQosShaperV2StatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 8),
    _CmQosShaperV2StatsFTD_Type()
)
cmQosShaperV2StatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsFTD.setStatus("current")
_CmQosShaperV2StatsABRRL_Type = PerfCounter64
_CmQosShaperV2StatsABRRL_Object = MibTableColumn
cmQosShaperV2StatsABRRL = _CmQosShaperV2StatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 9),
    _CmQosShaperV2StatsABRRL_Type()
)
cmQosShaperV2StatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsABRRL.setStatus("current")
_CmQosShaperV2StatsBREDD_Type = PerfCounter64
_CmQosShaperV2StatsBREDD_Object = MibTableColumn
cmQosShaperV2StatsBREDD = _CmQosShaperV2StatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 10),
    _CmQosShaperV2StatsBREDD_Type()
)
cmQosShaperV2StatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsBREDD.setStatus("current")
_CmQosShaperV2StatsFREDD_Type = PerfCounter64
_CmQosShaperV2StatsFREDD_Object = MibTableColumn
cmQosShaperV2StatsFREDD = _CmQosShaperV2StatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 34, 1, 11),
    _CmQosShaperV2StatsFREDD_Type()
)
cmQosShaperV2StatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2StatsFREDD.setStatus("current")
_CmQosShaperV2HistoryTable_Object = MibTable
cmQosShaperV2HistoryTable = _CmQosShaperV2HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35)
)
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryTable.setStatus("current")
_CmQosShaperV2HistoryEntry_Object = MibTableRow
cmQosShaperV2HistoryEntry = _CmQosShaperV2HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1)
)
cmQosShaperV2HistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperV2Index"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperV2StatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryIndex"),
)
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryEntry.setStatus("current")


class _CmQosShaperV2HistoryIndex_Type(Integer32):
    """Custom type cmQosShaperV2HistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosShaperV2HistoryIndex_Type.__name__ = "Integer32"
_CmQosShaperV2HistoryIndex_Object = MibTableColumn
cmQosShaperV2HistoryIndex = _CmQosShaperV2HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 1),
    _CmQosShaperV2HistoryIndex_Type()
)
cmQosShaperV2HistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryIndex.setStatus("current")
_CmQosShaperV2HistoryTime_Type = DateAndTime
_CmQosShaperV2HistoryTime_Object = MibTableColumn
cmQosShaperV2HistoryTime = _CmQosShaperV2HistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 2),
    _CmQosShaperV2HistoryTime_Type()
)
cmQosShaperV2HistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryTime.setStatus("current")
_CmQosShaperV2HistoryValid_Type = TruthValue
_CmQosShaperV2HistoryValid_Object = MibTableColumn
cmQosShaperV2HistoryValid = _CmQosShaperV2HistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 3),
    _CmQosShaperV2HistoryValid_Type()
)
cmQosShaperV2HistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryValid.setStatus("current")
_CmQosShaperV2HistoryAction_Type = CmPmBinAction
_CmQosShaperV2HistoryAction_Object = MibTableColumn
cmQosShaperV2HistoryAction = _CmQosShaperV2HistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 4),
    _CmQosShaperV2HistoryAction_Type()
)
cmQosShaperV2HistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryAction.setStatus("current")
_CmQosShaperV2HistoryBT_Type = PerfCounter64
_CmQosShaperV2HistoryBT_Object = MibTableColumn
cmQosShaperV2HistoryBT = _CmQosShaperV2HistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 5),
    _CmQosShaperV2HistoryBT_Type()
)
cmQosShaperV2HistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryBT.setStatus("current")
_CmQosShaperV2HistoryBTD_Type = PerfCounter64
_CmQosShaperV2HistoryBTD_Object = MibTableColumn
cmQosShaperV2HistoryBTD = _CmQosShaperV2HistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 6),
    _CmQosShaperV2HistoryBTD_Type()
)
cmQosShaperV2HistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryBTD.setStatus("current")
_CmQosShaperV2HistoryFD_Type = PerfCounter64
_CmQosShaperV2HistoryFD_Object = MibTableColumn
cmQosShaperV2HistoryFD = _CmQosShaperV2HistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 7),
    _CmQosShaperV2HistoryFD_Type()
)
cmQosShaperV2HistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryFD.setStatus("current")
_CmQosShaperV2HistoryFTD_Type = PerfCounter64
_CmQosShaperV2HistoryFTD_Object = MibTableColumn
cmQosShaperV2HistoryFTD = _CmQosShaperV2HistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 8),
    _CmQosShaperV2HistoryFTD_Type()
)
cmQosShaperV2HistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryFTD.setStatus("current")
_CmQosShaperV2HistoryABRRL_Type = PerfCounter64
_CmQosShaperV2HistoryABRRL_Object = MibTableColumn
cmQosShaperV2HistoryABRRL = _CmQosShaperV2HistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 9),
    _CmQosShaperV2HistoryABRRL_Type()
)
cmQosShaperV2HistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryABRRL.setStatus("current")
_CmQosShaperV2HistoryBREDD_Type = PerfCounter64
_CmQosShaperV2HistoryBREDD_Object = MibTableColumn
cmQosShaperV2HistoryBREDD = _CmQosShaperV2HistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 10),
    _CmQosShaperV2HistoryBREDD_Type()
)
cmQosShaperV2HistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryBREDD.setStatus("current")
_CmQosShaperV2HistoryFREDD_Type = PerfCounter64
_CmQosShaperV2HistoryFREDD_Object = MibTableColumn
cmQosShaperV2HistoryFREDD = _CmQosShaperV2HistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 35, 1, 11),
    _CmQosShaperV2HistoryFREDD_Type()
)
cmQosShaperV2HistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2HistoryFREDD.setStatus("current")
_CmQosShaperV2ThresholdTable_Object = MibTable
cmQosShaperV2ThresholdTable = _CmQosShaperV2ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 36)
)
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdTable.setStatus("current")
_CmQosShaperV2ThresholdEntry_Object = MibTableRow
cmQosShaperV2ThresholdEntry = _CmQosShaperV2ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 36, 1)
)
cmQosShaperV2ThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "cmQosShaperV2Index"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperV2StatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdEntry.setStatus("current")


class _CmQosShaperV2ThresholdIndex_Type(Integer32):
    """Custom type cmQosShaperV2ThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmQosShaperV2ThresholdIndex_Type.__name__ = "Integer32"
_CmQosShaperV2ThresholdIndex_Object = MibTableColumn
cmQosShaperV2ThresholdIndex = _CmQosShaperV2ThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 36, 1, 1),
    _CmQosShaperV2ThresholdIndex_Type()
)
cmQosShaperV2ThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdIndex.setStatus("current")
_CmQosShaperV2ThresholdInterval_Type = CmPmIntervalType
_CmQosShaperV2ThresholdInterval_Object = MibTableColumn
cmQosShaperV2ThresholdInterval = _CmQosShaperV2ThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 36, 1, 2),
    _CmQosShaperV2ThresholdInterval_Type()
)
cmQosShaperV2ThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdInterval.setStatus("current")
_CmQosShaperV2ThresholdVariable_Type = VariablePointer
_CmQosShaperV2ThresholdVariable_Object = MibTableColumn
cmQosShaperV2ThresholdVariable = _CmQosShaperV2ThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 36, 1, 3),
    _CmQosShaperV2ThresholdVariable_Type()
)
cmQosShaperV2ThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdVariable.setStatus("current")
_CmQosShaperV2ThresholdValueLo_Type = Unsigned32
_CmQosShaperV2ThresholdValueLo_Object = MibTableColumn
cmQosShaperV2ThresholdValueLo = _CmQosShaperV2ThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 36, 1, 4),
    _CmQosShaperV2ThresholdValueLo_Type()
)
cmQosShaperV2ThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdValueLo.setStatus("current")
_CmQosShaperV2ThresholdValueHi_Type = Unsigned32
_CmQosShaperV2ThresholdValueHi_Object = MibTableColumn
cmQosShaperV2ThresholdValueHi = _CmQosShaperV2ThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 36, 1, 5),
    _CmQosShaperV2ThresholdValueHi_Type()
)
cmQosShaperV2ThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdValueHi.setStatus("current")
_CmQosShaperV2ThresholdMonValue_Type = Counter64
_CmQosShaperV2ThresholdMonValue_Object = MibTableColumn
cmQosShaperV2ThresholdMonValue = _CmQosShaperV2ThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 36, 1, 6),
    _CmQosShaperV2ThresholdMonValue_Type()
)
cmQosShaperV2ThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdMonValue.setStatus("current")
_CmLagStatsTable_Object = MibTable
cmLagStatsTable = _CmLagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37)
)
if mibBuilder.loadTexts:
    cmLagStatsTable.setStatus("current")
_CmLagStatsEntry_Object = MibTableRow
cmLagStatsEntry = _CmLagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1)
)
cmLagStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-LAG-MIB", "f3LagIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmLagStatsIndex"),
)
if mibBuilder.loadTexts:
    cmLagStatsEntry.setStatus("current")


class _CmLagStatsIndex_Type(Integer32):
    """Custom type cmLagStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmLagStatsIndex_Type.__name__ = "Integer32"
_CmLagStatsIndex_Object = MibTableColumn
cmLagStatsIndex = _CmLagStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 1),
    _CmLagStatsIndex_Type()
)
cmLagStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsIndex.setStatus("current")
_CmLagStatsIntervalType_Type = CmPmIntervalType
_CmLagStatsIntervalType_Object = MibTableColumn
cmLagStatsIntervalType = _CmLagStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 2),
    _CmLagStatsIntervalType_Type()
)
cmLagStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsIntervalType.setStatus("current")
_CmLagStatsValid_Type = TruthValue
_CmLagStatsValid_Object = MibTableColumn
cmLagStatsValid = _CmLagStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 3),
    _CmLagStatsValid_Type()
)
cmLagStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsValid.setStatus("current")
_CmLagStatsAction_Type = CmPmBinAction
_CmLagStatsAction_Object = MibTableColumn
cmLagStatsAction = _CmLagStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 4),
    _CmLagStatsAction_Type()
)
cmLagStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLagStatsAction.setStatus("current")
_CmLagStatsESBF_Type = PerfCounter64
_CmLagStatsESBF_Object = MibTableColumn
cmLagStatsESBF = _CmLagStatsESBF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 5),
    _CmLagStatsESBF_Type()
)
cmLagStatsESBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESBF.setStatus("current")
_CmLagStatsESBP_Type = PerfCounter64
_CmLagStatsESBP_Object = MibTableColumn
cmLagStatsESBP = _CmLagStatsESBP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 6),
    _CmLagStatsESBP_Type()
)
cmLagStatsESBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESBP.setStatus("current")
_CmLagStatsESBS_Type = PerfCounter64
_CmLagStatsESBS_Object = MibTableColumn
cmLagStatsESBS = _CmLagStatsESBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 7),
    _CmLagStatsESBS_Type()
)
cmLagStatsESBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESBS.setStatus("current")
_CmLagStatsESC_Type = PerfCounter64
_CmLagStatsESC_Object = MibTableColumn
cmLagStatsESC = _CmLagStatsESC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 8),
    _CmLagStatsESC_Type()
)
cmLagStatsESC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESC.setStatus("current")
_CmLagStatsESCAE_Type = PerfCounter64
_CmLagStatsESCAE_Object = MibTableColumn
cmLagStatsESCAE = _CmLagStatsESCAE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 9),
    _CmLagStatsESCAE_Type()
)
cmLagStatsESCAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESCAE.setStatus("current")
_CmLagStatsESDE_Type = PerfCounter64
_CmLagStatsESDE_Object = MibTableColumn
cmLagStatsESDE = _CmLagStatsESDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 10),
    _CmLagStatsESDE_Type()
)
cmLagStatsESDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESDE.setStatus("current")
_CmLagStatsESF_Type = PerfCounter64
_CmLagStatsESF_Object = MibTableColumn
cmLagStatsESF = _CmLagStatsESF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 11),
    _CmLagStatsESF_Type()
)
cmLagStatsESF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESF.setStatus("current")
_CmLagStatsESFS_Type = PerfCounter64
_CmLagStatsESFS_Object = MibTableColumn
cmLagStatsESFS = _CmLagStatsESFS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 12),
    _CmLagStatsESFS_Type()
)
cmLagStatsESFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESFS.setStatus("current")
_CmLagStatsESJ_Type = PerfCounter64
_CmLagStatsESJ_Object = MibTableColumn
cmLagStatsESJ = _CmLagStatsESJ_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 13),
    _CmLagStatsESJ_Type()
)
cmLagStatsESJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESJ.setStatus("current")
_CmLagStatsESMF_Type = PerfCounter64
_CmLagStatsESMF_Object = MibTableColumn
cmLagStatsESMF = _CmLagStatsESMF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 14),
    _CmLagStatsESMF_Type()
)
cmLagStatsESMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESMF.setStatus("current")
_CmLagStatsESMP_Type = PerfCounter64
_CmLagStatsESMP_Object = MibTableColumn
cmLagStatsESMP = _CmLagStatsESMP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 15),
    _CmLagStatsESMP_Type()
)
cmLagStatsESMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESMP.setStatus("current")
_CmLagStatsESO_Type = PerfCounter64
_CmLagStatsESO_Object = MibTableColumn
cmLagStatsESO = _CmLagStatsESO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 16),
    _CmLagStatsESO_Type()
)
cmLagStatsESO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESO.setStatus("current")
_CmLagStatsESOF_Type = PerfCounter64
_CmLagStatsESOF_Object = MibTableColumn
cmLagStatsESOF = _CmLagStatsESOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 17),
    _CmLagStatsESOF_Type()
)
cmLagStatsESOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESOF.setStatus("current")
_CmLagStatsESOP_Type = PerfCounter64
_CmLagStatsESOP_Object = MibTableColumn
cmLagStatsESOP = _CmLagStatsESOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 18),
    _CmLagStatsESOP_Type()
)
cmLagStatsESOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESOP.setStatus("current")
_CmLagStatsESP_Type = PerfCounter64
_CmLagStatsESP_Object = MibTableColumn
cmLagStatsESP = _CmLagStatsESP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 19),
    _CmLagStatsESP_Type()
)
cmLagStatsESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESP.setStatus("current")
_CmLagStatsESP64_Type = PerfCounter64
_CmLagStatsESP64_Object = MibTableColumn
cmLagStatsESP64 = _CmLagStatsESP64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 20),
    _CmLagStatsESP64_Type()
)
cmLagStatsESP64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESP64.setStatus("current")
_CmLagStatsESP65_Type = PerfCounter64
_CmLagStatsESP65_Object = MibTableColumn
cmLagStatsESP65 = _CmLagStatsESP65_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 21),
    _CmLagStatsESP65_Type()
)
cmLagStatsESP65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESP65.setStatus("current")
_CmLagStatsESP128_Type = PerfCounter64
_CmLagStatsESP128_Object = MibTableColumn
cmLagStatsESP128 = _CmLagStatsESP128_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 22),
    _CmLagStatsESP128_Type()
)
cmLagStatsESP128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESP128.setStatus("current")
_CmLagStatsESP256_Type = PerfCounter64
_CmLagStatsESP256_Object = MibTableColumn
cmLagStatsESP256 = _CmLagStatsESP256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 23),
    _CmLagStatsESP256_Type()
)
cmLagStatsESP256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESP256.setStatus("current")
_CmLagStatsESP512_Type = PerfCounter64
_CmLagStatsESP512_Object = MibTableColumn
cmLagStatsESP512 = _CmLagStatsESP512_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 24),
    _CmLagStatsESP512_Type()
)
cmLagStatsESP512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESP512.setStatus("current")
_CmLagStatsESP1024_Type = PerfCounter64
_CmLagStatsESP1024_Object = MibTableColumn
cmLagStatsESP1024 = _CmLagStatsESP1024_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 25),
    _CmLagStatsESP1024_Type()
)
cmLagStatsESP1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESP1024.setStatus("current")
_CmLagStatsESP1519_Type = PerfCounter64
_CmLagStatsESP1519_Object = MibTableColumn
cmLagStatsESP1519 = _CmLagStatsESP1519_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 26),
    _CmLagStatsESP1519_Type()
)
cmLagStatsESP1519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESP1519.setStatus("current")
_CmLagStatsESUF_Type = PerfCounter64
_CmLagStatsESUF_Object = MibTableColumn
cmLagStatsESUF = _CmLagStatsESUF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 27),
    _CmLagStatsESUF_Type()
)
cmLagStatsESUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESUF.setStatus("current")
_CmLagStatsESUP_Type = PerfCounter64
_CmLagStatsESUP_Object = MibTableColumn
cmLagStatsESUP = _CmLagStatsESUP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 28),
    _CmLagStatsESUP_Type()
)
cmLagStatsESUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsESUP.setStatus("current")
_CmLagStatsL2CPFD_Type = PerfCounter64
_CmLagStatsL2CPFD_Object = MibTableColumn
cmLagStatsL2CPFD = _CmLagStatsL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 29),
    _CmLagStatsL2CPFD_Type()
)
cmLagStatsL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsL2CPFD.setStatus("current")
_CmLagStatsL2CPFP_Type = PerfCounter64
_CmLagStatsL2CPFP_Object = MibTableColumn
cmLagStatsL2CPFP = _CmLagStatsL2CPFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 30),
    _CmLagStatsL2CPFP_Type()
)
cmLagStatsL2CPFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsL2CPFP.setStatus("current")
_CmLagStatsAUFD_Type = PerfCounter64
_CmLagStatsAUFD_Object = MibTableColumn
cmLagStatsAUFD = _CmLagStatsAUFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 31),
    _CmLagStatsAUFD_Type()
)
cmLagStatsAUFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsAUFD.setStatus("current")
_CmLagStatsAPFD_Type = PerfCounter64
_CmLagStatsAPFD_Object = MibTableColumn
cmLagStatsAPFD = _CmLagStatsAPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 32),
    _CmLagStatsAPFD_Type()
)
cmLagStatsAPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsAPFD.setStatus("current")
_CmLagStatsABRRx_Type = PerfCounter64
_CmLagStatsABRRx_Object = MibTableColumn
cmLagStatsABRRx = _CmLagStatsABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 33),
    _CmLagStatsABRRx_Type()
)
cmLagStatsABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsABRRx.setStatus("current")
_CmLagStatsABRTx_Type = PerfCounter64
_CmLagStatsABRTx_Object = MibTableColumn
cmLagStatsABRTx = _CmLagStatsABRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 34),
    _CmLagStatsABRTx_Type()
)
cmLagStatsABRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsABRTx.setStatus("current")
_CmLagStatsATFD_Type = PerfCounter64
_CmLagStatsATFD_Object = MibTableColumn
cmLagStatsATFD = _CmLagStatsATFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 35),
    _CmLagStatsATFD_Type()
)
cmLagStatsATFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsATFD.setStatus("current")
_CmLagStatsLkupFails_Type = PerfCounter64
_CmLagStatsLkupFails_Object = MibTableColumn
cmLagStatsLkupFails = _CmLagStatsLkupFails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 37, 1, 36),
    _CmLagStatsLkupFails_Type()
)
cmLagStatsLkupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagStatsLkupFails.setStatus("current")
_CmLagHistoryTable_Object = MibTable
cmLagHistoryTable = _CmLagHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38)
)
if mibBuilder.loadTexts:
    cmLagHistoryTable.setStatus("current")
_CmLagHistoryEntry_Object = MibTableRow
cmLagHistoryEntry = _CmLagHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1)
)
cmLagHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-LAG-MIB", "f3LagIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmLagStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmLagHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmLagHistoryEntry.setStatus("current")


class _CmLagHistoryIndex_Type(Integer32):
    """Custom type cmLagHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CmLagHistoryIndex_Type.__name__ = "Integer32"
_CmLagHistoryIndex_Object = MibTableColumn
cmLagHistoryIndex = _CmLagHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 1),
    _CmLagHistoryIndex_Type()
)
cmLagHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryIndex.setStatus("current")
_CmLagHistoryTime_Type = DateAndTime
_CmLagHistoryTime_Object = MibTableColumn
cmLagHistoryTime = _CmLagHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 2),
    _CmLagHistoryTime_Type()
)
cmLagHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryTime.setStatus("current")
_CmLagHistoryValid_Type = TruthValue
_CmLagHistoryValid_Object = MibTableColumn
cmLagHistoryValid = _CmLagHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 3),
    _CmLagHistoryValid_Type()
)
cmLagHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryValid.setStatus("current")
_CmLagHistoryAction_Type = CmPmBinAction
_CmLagHistoryAction_Object = MibTableColumn
cmLagHistoryAction = _CmLagHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 4),
    _CmLagHistoryAction_Type()
)
cmLagHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLagHistoryAction.setStatus("current")
_CmLagHistoryESBF_Type = PerfCounter64
_CmLagHistoryESBF_Object = MibTableColumn
cmLagHistoryESBF = _CmLagHistoryESBF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 5),
    _CmLagHistoryESBF_Type()
)
cmLagHistoryESBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESBF.setStatus("current")
_CmLagHistoryESBP_Type = PerfCounter64
_CmLagHistoryESBP_Object = MibTableColumn
cmLagHistoryESBP = _CmLagHistoryESBP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 6),
    _CmLagHistoryESBP_Type()
)
cmLagHistoryESBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESBP.setStatus("current")
_CmLagHistoryESBS_Type = PerfCounter64
_CmLagHistoryESBS_Object = MibTableColumn
cmLagHistoryESBS = _CmLagHistoryESBS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 7),
    _CmLagHistoryESBS_Type()
)
cmLagHistoryESBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESBS.setStatus("current")
_CmLagHistoryESC_Type = PerfCounter64
_CmLagHistoryESC_Object = MibTableColumn
cmLagHistoryESC = _CmLagHistoryESC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 8),
    _CmLagHistoryESC_Type()
)
cmLagHistoryESC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESC.setStatus("current")
_CmLagHistoryESCAE_Type = PerfCounter64
_CmLagHistoryESCAE_Object = MibTableColumn
cmLagHistoryESCAE = _CmLagHistoryESCAE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 9),
    _CmLagHistoryESCAE_Type()
)
cmLagHistoryESCAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESCAE.setStatus("current")
_CmLagHistoryESDE_Type = PerfCounter64
_CmLagHistoryESDE_Object = MibTableColumn
cmLagHistoryESDE = _CmLagHistoryESDE_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 10),
    _CmLagHistoryESDE_Type()
)
cmLagHistoryESDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESDE.setStatus("current")
_CmLagHistoryESF_Type = PerfCounter64
_CmLagHistoryESF_Object = MibTableColumn
cmLagHistoryESF = _CmLagHistoryESF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 11),
    _CmLagHistoryESF_Type()
)
cmLagHistoryESF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESF.setStatus("current")
_CmLagHistoryESFS_Type = PerfCounter64
_CmLagHistoryESFS_Object = MibTableColumn
cmLagHistoryESFS = _CmLagHistoryESFS_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 12),
    _CmLagHistoryESFS_Type()
)
cmLagHistoryESFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESFS.setStatus("current")
_CmLagHistoryESJ_Type = PerfCounter64
_CmLagHistoryESJ_Object = MibTableColumn
cmLagHistoryESJ = _CmLagHistoryESJ_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 13),
    _CmLagHistoryESJ_Type()
)
cmLagHistoryESJ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESJ.setStatus("current")
_CmLagHistoryESMF_Type = PerfCounter64
_CmLagHistoryESMF_Object = MibTableColumn
cmLagHistoryESMF = _CmLagHistoryESMF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 14),
    _CmLagHistoryESMF_Type()
)
cmLagHistoryESMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESMF.setStatus("current")
_CmLagHistoryESMP_Type = PerfCounter64
_CmLagHistoryESMP_Object = MibTableColumn
cmLagHistoryESMP = _CmLagHistoryESMP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 15),
    _CmLagHistoryESMP_Type()
)
cmLagHistoryESMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESMP.setStatus("current")
_CmLagHistoryESO_Type = PerfCounter64
_CmLagHistoryESO_Object = MibTableColumn
cmLagHistoryESO = _CmLagHistoryESO_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 16),
    _CmLagHistoryESO_Type()
)
cmLagHistoryESO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESO.setStatus("current")
_CmLagHistoryESOF_Type = PerfCounter64
_CmLagHistoryESOF_Object = MibTableColumn
cmLagHistoryESOF = _CmLagHistoryESOF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 17),
    _CmLagHistoryESOF_Type()
)
cmLagHistoryESOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESOF.setStatus("current")
_CmLagHistoryESOP_Type = PerfCounter64
_CmLagHistoryESOP_Object = MibTableColumn
cmLagHistoryESOP = _CmLagHistoryESOP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 18),
    _CmLagHistoryESOP_Type()
)
cmLagHistoryESOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESOP.setStatus("current")
_CmLagHistoryESP_Type = PerfCounter64
_CmLagHistoryESP_Object = MibTableColumn
cmLagHistoryESP = _CmLagHistoryESP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 19),
    _CmLagHistoryESP_Type()
)
cmLagHistoryESP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESP.setStatus("current")
_CmLagHistoryESP64_Type = PerfCounter64
_CmLagHistoryESP64_Object = MibTableColumn
cmLagHistoryESP64 = _CmLagHistoryESP64_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 20),
    _CmLagHistoryESP64_Type()
)
cmLagHistoryESP64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESP64.setStatus("current")
_CmLagHistoryESP65_Type = PerfCounter64
_CmLagHistoryESP65_Object = MibTableColumn
cmLagHistoryESP65 = _CmLagHistoryESP65_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 21),
    _CmLagHistoryESP65_Type()
)
cmLagHistoryESP65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESP65.setStatus("current")
_CmLagHistoryESP128_Type = PerfCounter64
_CmLagHistoryESP128_Object = MibTableColumn
cmLagHistoryESP128 = _CmLagHistoryESP128_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 22),
    _CmLagHistoryESP128_Type()
)
cmLagHistoryESP128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESP128.setStatus("current")
_CmLagHistoryESP256_Type = PerfCounter64
_CmLagHistoryESP256_Object = MibTableColumn
cmLagHistoryESP256 = _CmLagHistoryESP256_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 23),
    _CmLagHistoryESP256_Type()
)
cmLagHistoryESP256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESP256.setStatus("current")
_CmLagHistoryESP512_Type = PerfCounter64
_CmLagHistoryESP512_Object = MibTableColumn
cmLagHistoryESP512 = _CmLagHistoryESP512_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 24),
    _CmLagHistoryESP512_Type()
)
cmLagHistoryESP512.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESP512.setStatus("current")
_CmLagHistoryESP1024_Type = PerfCounter64
_CmLagHistoryESP1024_Object = MibTableColumn
cmLagHistoryESP1024 = _CmLagHistoryESP1024_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 25),
    _CmLagHistoryESP1024_Type()
)
cmLagHistoryESP1024.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESP1024.setStatus("current")
_CmLagHistoryESP1519_Type = PerfCounter64
_CmLagHistoryESP1519_Object = MibTableColumn
cmLagHistoryESP1519 = _CmLagHistoryESP1519_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 26),
    _CmLagHistoryESP1519_Type()
)
cmLagHistoryESP1519.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESP1519.setStatus("current")
_CmLagHistoryESUF_Type = PerfCounter64
_CmLagHistoryESUF_Object = MibTableColumn
cmLagHistoryESUF = _CmLagHistoryESUF_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 27),
    _CmLagHistoryESUF_Type()
)
cmLagHistoryESUF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESUF.setStatus("current")
_CmLagHistoryESUP_Type = PerfCounter64
_CmLagHistoryESUP_Object = MibTableColumn
cmLagHistoryESUP = _CmLagHistoryESUP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 28),
    _CmLagHistoryESUP_Type()
)
cmLagHistoryESUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryESUP.setStatus("current")
_CmLagHistoryL2CPFD_Type = PerfCounter64
_CmLagHistoryL2CPFD_Object = MibTableColumn
cmLagHistoryL2CPFD = _CmLagHistoryL2CPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 29),
    _CmLagHistoryL2CPFD_Type()
)
cmLagHistoryL2CPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryL2CPFD.setStatus("current")
_CmLagHistoryL2CPFP_Type = PerfCounter64
_CmLagHistoryL2CPFP_Object = MibTableColumn
cmLagHistoryL2CPFP = _CmLagHistoryL2CPFP_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 30),
    _CmLagHistoryL2CPFP_Type()
)
cmLagHistoryL2CPFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryL2CPFP.setStatus("current")
_CmLagHistoryAUFD_Type = PerfCounter64
_CmLagHistoryAUFD_Object = MibTableColumn
cmLagHistoryAUFD = _CmLagHistoryAUFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 31),
    _CmLagHistoryAUFD_Type()
)
cmLagHistoryAUFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryAUFD.setStatus("current")
_CmLagHistoryAPFD_Type = PerfCounter64
_CmLagHistoryAPFD_Object = MibTableColumn
cmLagHistoryAPFD = _CmLagHistoryAPFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 32),
    _CmLagHistoryAPFD_Type()
)
cmLagHistoryAPFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryAPFD.setStatus("current")
_CmLagHistoryABRRx_Type = PerfCounter64
_CmLagHistoryABRRx_Object = MibTableColumn
cmLagHistoryABRRx = _CmLagHistoryABRRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 33),
    _CmLagHistoryABRRx_Type()
)
cmLagHistoryABRRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryABRRx.setStatus("current")
_CmLagHistoryABRTx_Type = PerfCounter64
_CmLagHistoryABRTx_Object = MibTableColumn
cmLagHistoryABRTx = _CmLagHistoryABRTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 34),
    _CmLagHistoryABRTx_Type()
)
cmLagHistoryABRTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryABRTx.setStatus("current")
_CmLagHistoryATFD_Type = PerfCounter64
_CmLagHistoryATFD_Object = MibTableColumn
cmLagHistoryATFD = _CmLagHistoryATFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 35),
    _CmLagHistoryATFD_Type()
)
cmLagHistoryATFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryATFD.setStatus("current")
_CmLagHistoryLkupFails_Type = PerfCounter64
_CmLagHistoryLkupFails_Object = MibTableColumn
cmLagHistoryLkupFails = _CmLagHistoryLkupFails_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 38, 1, 36),
    _CmLagHistoryLkupFails_Type()
)
cmLagHistoryLkupFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagHistoryLkupFails.setStatus("current")
_CmLagThresholdTable_Object = MibTable
cmLagThresholdTable = _CmLagThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 39)
)
if mibBuilder.loadTexts:
    cmLagThresholdTable.setStatus("current")
_CmLagThresholdEntry_Object = MibTableRow
cmLagThresholdEntry = _CmLagThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 39, 1)
)
cmLagThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-LAG-MIB", "f3LagIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmLagStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmLagThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmLagThresholdEntry.setStatus("current")


class _CmLagThresholdIndex_Type(Integer32):
    """Custom type cmLagThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmLagThresholdIndex_Type.__name__ = "Integer32"
_CmLagThresholdIndex_Object = MibTableColumn
cmLagThresholdIndex = _CmLagThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 39, 1, 1),
    _CmLagThresholdIndex_Type()
)
cmLagThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagThresholdIndex.setStatus("current")
_CmLagThresholdInterval_Type = CmPmIntervalType
_CmLagThresholdInterval_Object = MibTableColumn
cmLagThresholdInterval = _CmLagThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 39, 1, 2),
    _CmLagThresholdInterval_Type()
)
cmLagThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagThresholdInterval.setStatus("current")
_CmLagThresholdVariable_Type = VariablePointer
_CmLagThresholdVariable_Object = MibTableColumn
cmLagThresholdVariable = _CmLagThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 39, 1, 3),
    _CmLagThresholdVariable_Type()
)
cmLagThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagThresholdVariable.setStatus("current")
_CmLagThresholdValueLo_Type = Unsigned32
_CmLagThresholdValueLo_Object = MibTableColumn
cmLagThresholdValueLo = _CmLagThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 39, 1, 4),
    _CmLagThresholdValueLo_Type()
)
cmLagThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLagThresholdValueLo.setStatus("current")
_CmLagThresholdValueHi_Type = Unsigned32
_CmLagThresholdValueHi_Object = MibTableColumn
cmLagThresholdValueHi = _CmLagThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 39, 1, 5),
    _CmLagThresholdValueHi_Type()
)
cmLagThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLagThresholdValueHi.setStatus("current")
_CmLagThresholdMonValue_Type = Counter64
_CmLagThresholdMonValue_Object = MibTableColumn
cmLagThresholdMonValue = _CmLagThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 39, 1, 6),
    _CmLagThresholdMonValue_Type()
)
cmLagThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLagThresholdMonValue.setStatus("current")
_CmTrafficPortQosShaperStatsTable_Object = MibTable
cmTrafficPortQosShaperStatsTable = _CmTrafficPortQosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40)
)
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsTable.setStatus("current")
_CmTrafficPortQosShaperStatsEntry_Object = MibTableRow
cmTrafficPortQosShaperStatsEntry = _CmTrafficPortQosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1)
)
cmTrafficPortQosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmTrafficPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsEntry.setStatus("current")


class _CmTrafficPortQosShaperStatsIndex_Type(Integer32):
    """Custom type cmTrafficPortQosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmTrafficPortQosShaperStatsIndex_Type.__name__ = "Integer32"
_CmTrafficPortQosShaperStatsIndex_Object = MibTableColumn
cmTrafficPortQosShaperStatsIndex = _CmTrafficPortQosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 1),
    _CmTrafficPortQosShaperStatsIndex_Type()
)
cmTrafficPortQosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsIndex.setStatus("current")
_CmTrafficPortQosShaperStatsIntervalType_Type = CmPmIntervalType
_CmTrafficPortQosShaperStatsIntervalType_Object = MibTableColumn
cmTrafficPortQosShaperStatsIntervalType = _CmTrafficPortQosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 2),
    _CmTrafficPortQosShaperStatsIntervalType_Type()
)
cmTrafficPortQosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsIntervalType.setStatus("current")
_CmTrafficPortQosShaperStatsValid_Type = TruthValue
_CmTrafficPortQosShaperStatsValid_Object = MibTableColumn
cmTrafficPortQosShaperStatsValid = _CmTrafficPortQosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 3),
    _CmTrafficPortQosShaperStatsValid_Type()
)
cmTrafficPortQosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsValid.setStatus("current")
_CmTrafficPortQosShaperStatsAction_Type = CmPmBinAction
_CmTrafficPortQosShaperStatsAction_Object = MibTableColumn
cmTrafficPortQosShaperStatsAction = _CmTrafficPortQosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 4),
    _CmTrafficPortQosShaperStatsAction_Type()
)
cmTrafficPortQosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsAction.setStatus("current")
_CmTrafficPortQosShaperStatsBT_Type = PerfCounter64
_CmTrafficPortQosShaperStatsBT_Object = MibTableColumn
cmTrafficPortQosShaperStatsBT = _CmTrafficPortQosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 5),
    _CmTrafficPortQosShaperStatsBT_Type()
)
cmTrafficPortQosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsBT.setStatus("current")
_CmTrafficPortQosShaperStatsBTD_Type = PerfCounter64
_CmTrafficPortQosShaperStatsBTD_Object = MibTableColumn
cmTrafficPortQosShaperStatsBTD = _CmTrafficPortQosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 6),
    _CmTrafficPortQosShaperStatsBTD_Type()
)
cmTrafficPortQosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsBTD.setStatus("current")
_CmTrafficPortQosShaperStatsFD_Type = PerfCounter64
_CmTrafficPortQosShaperStatsFD_Object = MibTableColumn
cmTrafficPortQosShaperStatsFD = _CmTrafficPortQosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 7),
    _CmTrafficPortQosShaperStatsFD_Type()
)
cmTrafficPortQosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsFD.setStatus("current")
_CmTrafficPortQosShaperStatsFTD_Type = PerfCounter64
_CmTrafficPortQosShaperStatsFTD_Object = MibTableColumn
cmTrafficPortQosShaperStatsFTD = _CmTrafficPortQosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 8),
    _CmTrafficPortQosShaperStatsFTD_Type()
)
cmTrafficPortQosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsFTD.setStatus("current")
_CmTrafficPortQosShaperStatsABRRL_Type = PerfCounter64
_CmTrafficPortQosShaperStatsABRRL_Object = MibTableColumn
cmTrafficPortQosShaperStatsABRRL = _CmTrafficPortQosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 9),
    _CmTrafficPortQosShaperStatsABRRL_Type()
)
cmTrafficPortQosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsABRRL.setStatus("current")
_CmTrafficPortQosShaperStatsBREDD_Type = PerfCounter64
_CmTrafficPortQosShaperStatsBREDD_Object = MibTableColumn
cmTrafficPortQosShaperStatsBREDD = _CmTrafficPortQosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 10),
    _CmTrafficPortQosShaperStatsBREDD_Type()
)
cmTrafficPortQosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsBREDD.setStatus("current")
_CmTrafficPortQosShaperStatsFREDD_Type = PerfCounter64
_CmTrafficPortQosShaperStatsFREDD_Object = MibTableColumn
cmTrafficPortQosShaperStatsFREDD = _CmTrafficPortQosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 40, 1, 11),
    _CmTrafficPortQosShaperStatsFREDD_Type()
)
cmTrafficPortQosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperStatsFREDD.setStatus("current")
_CmTrafficPortQosShaperHistoryTable_Object = MibTable
cmTrafficPortQosShaperHistoryTable = _CmTrafficPortQosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41)
)
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryTable.setStatus("current")
_CmTrafficPortQosShaperHistoryEntry_Object = MibTableRow
cmTrafficPortQosShaperHistoryEntry = _CmTrafficPortQosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1)
)
cmTrafficPortQosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmTrafficPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryEntry.setStatus("current")


class _CmTrafficPortQosShaperHistoryIndex_Type(Integer32):
    """Custom type cmTrafficPortQosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmTrafficPortQosShaperHistoryIndex_Type.__name__ = "Integer32"
_CmTrafficPortQosShaperHistoryIndex_Object = MibTableColumn
cmTrafficPortQosShaperHistoryIndex = _CmTrafficPortQosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 1),
    _CmTrafficPortQosShaperHistoryIndex_Type()
)
cmTrafficPortQosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryIndex.setStatus("current")
_CmTrafficPortQosShaperHistoryTime_Type = DateAndTime
_CmTrafficPortQosShaperHistoryTime_Object = MibTableColumn
cmTrafficPortQosShaperHistoryTime = _CmTrafficPortQosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 2),
    _CmTrafficPortQosShaperHistoryTime_Type()
)
cmTrafficPortQosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryTime.setStatus("current")
_CmTrafficPortQosShaperHistoryValid_Type = TruthValue
_CmTrafficPortQosShaperHistoryValid_Object = MibTableColumn
cmTrafficPortQosShaperHistoryValid = _CmTrafficPortQosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 3),
    _CmTrafficPortQosShaperHistoryValid_Type()
)
cmTrafficPortQosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryValid.setStatus("current")
_CmTrafficPortQosShaperHistoryAction_Type = CmPmBinAction
_CmTrafficPortQosShaperHistoryAction_Object = MibTableColumn
cmTrafficPortQosShaperHistoryAction = _CmTrafficPortQosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 4),
    _CmTrafficPortQosShaperHistoryAction_Type()
)
cmTrafficPortQosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryAction.setStatus("current")
_CmTrafficPortQosShaperHistoryBT_Type = PerfCounter64
_CmTrafficPortQosShaperHistoryBT_Object = MibTableColumn
cmTrafficPortQosShaperHistoryBT = _CmTrafficPortQosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 5),
    _CmTrafficPortQosShaperHistoryBT_Type()
)
cmTrafficPortQosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryBT.setStatus("current")
_CmTrafficPortQosShaperHistoryBTD_Type = PerfCounter64
_CmTrafficPortQosShaperHistoryBTD_Object = MibTableColumn
cmTrafficPortQosShaperHistoryBTD = _CmTrafficPortQosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 6),
    _CmTrafficPortQosShaperHistoryBTD_Type()
)
cmTrafficPortQosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryBTD.setStatus("current")
_CmTrafficPortQosShaperHistoryFD_Type = PerfCounter64
_CmTrafficPortQosShaperHistoryFD_Object = MibTableColumn
cmTrafficPortQosShaperHistoryFD = _CmTrafficPortQosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 7),
    _CmTrafficPortQosShaperHistoryFD_Type()
)
cmTrafficPortQosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryFD.setStatus("current")
_CmTrafficPortQosShaperHistoryFTD_Type = PerfCounter64
_CmTrafficPortQosShaperHistoryFTD_Object = MibTableColumn
cmTrafficPortQosShaperHistoryFTD = _CmTrafficPortQosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 8),
    _CmTrafficPortQosShaperHistoryFTD_Type()
)
cmTrafficPortQosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryFTD.setStatus("current")
_CmTrafficPortQosShaperHistoryABRRL_Type = PerfCounter64
_CmTrafficPortQosShaperHistoryABRRL_Object = MibTableColumn
cmTrafficPortQosShaperHistoryABRRL = _CmTrafficPortQosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 9),
    _CmTrafficPortQosShaperHistoryABRRL_Type()
)
cmTrafficPortQosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryABRRL.setStatus("current")
_CmTrafficPortQosShaperHistoryBREDD_Type = PerfCounter64
_CmTrafficPortQosShaperHistoryBREDD_Object = MibTableColumn
cmTrafficPortQosShaperHistoryBREDD = _CmTrafficPortQosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 10),
    _CmTrafficPortQosShaperHistoryBREDD_Type()
)
cmTrafficPortQosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryBREDD.setStatus("current")
_CmTrafficPortQosShaperHistoryFREDD_Type = PerfCounter64
_CmTrafficPortQosShaperHistoryFREDD_Object = MibTableColumn
cmTrafficPortQosShaperHistoryFREDD = _CmTrafficPortQosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 41, 1, 11),
    _CmTrafficPortQosShaperHistoryFREDD_Type()
)
cmTrafficPortQosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperHistoryFREDD.setStatus("current")
_CmTrafficPortQosShaperThresholdTable_Object = MibTable
cmTrafficPortQosShaperThresholdTable = _CmTrafficPortQosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 42)
)
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdTable.setStatus("current")
_CmTrafficPortQosShaperThresholdEntry_Object = MibTableRow
cmTrafficPortQosShaperThresholdEntry = _CmTrafficPortQosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 42, 1)
)
cmTrafficPortQosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmTrafficPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdEntry.setStatus("current")


class _CmTrafficPortQosShaperThresholdIndex_Type(Integer32):
    """Custom type cmTrafficPortQosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmTrafficPortQosShaperThresholdIndex_Type.__name__ = "Integer32"
_CmTrafficPortQosShaperThresholdIndex_Object = MibTableColumn
cmTrafficPortQosShaperThresholdIndex = _CmTrafficPortQosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 42, 1, 1),
    _CmTrafficPortQosShaperThresholdIndex_Type()
)
cmTrafficPortQosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdIndex.setStatus("current")
_CmTrafficPortQosShaperThresholdInterval_Type = CmPmIntervalType
_CmTrafficPortQosShaperThresholdInterval_Object = MibTableColumn
cmTrafficPortQosShaperThresholdInterval = _CmTrafficPortQosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 42, 1, 2),
    _CmTrafficPortQosShaperThresholdInterval_Type()
)
cmTrafficPortQosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdInterval.setStatus("current")
_CmTrafficPortQosShaperThresholdVariable_Type = VariablePointer
_CmTrafficPortQosShaperThresholdVariable_Object = MibTableColumn
cmTrafficPortQosShaperThresholdVariable = _CmTrafficPortQosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 42, 1, 3),
    _CmTrafficPortQosShaperThresholdVariable_Type()
)
cmTrafficPortQosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdVariable.setStatus("current")
_CmTrafficPortQosShaperThresholdValueLo_Type = Unsigned32
_CmTrafficPortQosShaperThresholdValueLo_Object = MibTableColumn
cmTrafficPortQosShaperThresholdValueLo = _CmTrafficPortQosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 42, 1, 4),
    _CmTrafficPortQosShaperThresholdValueLo_Type()
)
cmTrafficPortQosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdValueLo.setStatus("current")
_CmTrafficPortQosShaperThresholdValueHi_Type = Unsigned32
_CmTrafficPortQosShaperThresholdValueHi_Object = MibTableColumn
cmTrafficPortQosShaperThresholdValueHi = _CmTrafficPortQosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 42, 1, 5),
    _CmTrafficPortQosShaperThresholdValueHi_Type()
)
cmTrafficPortQosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdValueHi.setStatus("current")
_CmTrafficPortQosShaperThresholdMonValue_Type = Counter64
_CmTrafficPortQosShaperThresholdMonValue_Object = MibTableColumn
cmTrafficPortQosShaperThresholdMonValue = _CmTrafficPortQosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 42, 1, 6),
    _CmTrafficPortQosShaperThresholdMonValue_Type()
)
cmTrafficPortQosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdMonValue.setStatus("current")
_F3NetPortQosShaperStatsTable_Object = MibTable
f3NetPortQosShaperStatsTable = _F3NetPortQosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43)
)
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsTable.setStatus("current")
_F3NetPortQosShaperStatsEntry_Object = MibTableRow
f3NetPortQosShaperStatsEntry = _F3NetPortQosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1)
)
f3NetPortQosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "CM-FACILITY-MIB", "f3NetPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsEntry.setStatus("current")


class _F3NetPortQosShaperStatsIndex_Type(Integer32):
    """Custom type f3NetPortQosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetPortQosShaperStatsIndex_Type.__name__ = "Integer32"
_F3NetPortQosShaperStatsIndex_Object = MibTableColumn
f3NetPortQosShaperStatsIndex = _F3NetPortQosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 1),
    _F3NetPortQosShaperStatsIndex_Type()
)
f3NetPortQosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsIndex.setStatus("current")
_F3NetPortQosShaperStatsIntervalType_Type = CmPmIntervalType
_F3NetPortQosShaperStatsIntervalType_Object = MibTableColumn
f3NetPortQosShaperStatsIntervalType = _F3NetPortQosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 2),
    _F3NetPortQosShaperStatsIntervalType_Type()
)
f3NetPortQosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsIntervalType.setStatus("current")
_F3NetPortQosShaperStatsValid_Type = TruthValue
_F3NetPortQosShaperStatsValid_Object = MibTableColumn
f3NetPortQosShaperStatsValid = _F3NetPortQosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 3),
    _F3NetPortQosShaperStatsValid_Type()
)
f3NetPortQosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsValid.setStatus("current")
_F3NetPortQosShaperStatsAction_Type = CmPmBinAction
_F3NetPortQosShaperStatsAction_Object = MibTableColumn
f3NetPortQosShaperStatsAction = _F3NetPortQosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 4),
    _F3NetPortQosShaperStatsAction_Type()
)
f3NetPortQosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsAction.setStatus("current")
_F3NetPortQosShaperStatsBT_Type = PerfCounter64
_F3NetPortQosShaperStatsBT_Object = MibTableColumn
f3NetPortQosShaperStatsBT = _F3NetPortQosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 5),
    _F3NetPortQosShaperStatsBT_Type()
)
f3NetPortQosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsBT.setStatus("current")
_F3NetPortQosShaperStatsBTD_Type = PerfCounter64
_F3NetPortQosShaperStatsBTD_Object = MibTableColumn
f3NetPortQosShaperStatsBTD = _F3NetPortQosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 6),
    _F3NetPortQosShaperStatsBTD_Type()
)
f3NetPortQosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsBTD.setStatus("current")
_F3NetPortQosShaperStatsFD_Type = PerfCounter64
_F3NetPortQosShaperStatsFD_Object = MibTableColumn
f3NetPortQosShaperStatsFD = _F3NetPortQosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 7),
    _F3NetPortQosShaperStatsFD_Type()
)
f3NetPortQosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsFD.setStatus("current")
_F3NetPortQosShaperStatsFTD_Type = PerfCounter64
_F3NetPortQosShaperStatsFTD_Object = MibTableColumn
f3NetPortQosShaperStatsFTD = _F3NetPortQosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 8),
    _F3NetPortQosShaperStatsFTD_Type()
)
f3NetPortQosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsFTD.setStatus("current")
_F3NetPortQosShaperStatsBR_Type = PerfCounter64
_F3NetPortQosShaperStatsBR_Object = MibTableColumn
f3NetPortQosShaperStatsBR = _F3NetPortQosShaperStatsBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 9),
    _F3NetPortQosShaperStatsBR_Type()
)
f3NetPortQosShaperStatsBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsBR.setStatus("current")
_F3NetPortQosShaperStatsFR_Type = PerfCounter64
_F3NetPortQosShaperStatsFR_Object = MibTableColumn
f3NetPortQosShaperStatsFR = _F3NetPortQosShaperStatsFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 10),
    _F3NetPortQosShaperStatsFR_Type()
)
f3NetPortQosShaperStatsFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsFR.setStatus("current")
_F3NetPortQosShaperStatsABRRL_Type = PerfCounter64
_F3NetPortQosShaperStatsABRRL_Object = MibTableColumn
f3NetPortQosShaperStatsABRRL = _F3NetPortQosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 11),
    _F3NetPortQosShaperStatsABRRL_Type()
)
f3NetPortQosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsABRRL.setStatus("current")
_F3NetPortQosShaperStatsBREDD_Type = PerfCounter64
_F3NetPortQosShaperStatsBREDD_Object = MibTableColumn
f3NetPortQosShaperStatsBREDD = _F3NetPortQosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 12),
    _F3NetPortQosShaperStatsBREDD_Type()
)
f3NetPortQosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsBREDD.setStatus("current")
_F3NetPortQosShaperStatsFREDD_Type = PerfCounter64
_F3NetPortQosShaperStatsFREDD_Object = MibTableColumn
f3NetPortQosShaperStatsFREDD = _F3NetPortQosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 43, 1, 13),
    _F3NetPortQosShaperStatsFREDD_Type()
)
f3NetPortQosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperStatsFREDD.setStatus("current")
_F3NetPortQosShaperHistoryTable_Object = MibTable
f3NetPortQosShaperHistoryTable = _F3NetPortQosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44)
)
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryTable.setStatus("current")
_F3NetPortQosShaperHistoryEntry_Object = MibTableRow
f3NetPortQosShaperHistoryEntry = _F3NetPortQosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1)
)
f3NetPortQosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "CM-FACILITY-MIB", "f3NetPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryEntry.setStatus("current")


class _F3NetPortQosShaperHistoryIndex_Type(Integer32):
    """Custom type f3NetPortQosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetPortQosShaperHistoryIndex_Type.__name__ = "Integer32"
_F3NetPortQosShaperHistoryIndex_Object = MibTableColumn
f3NetPortQosShaperHistoryIndex = _F3NetPortQosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 1),
    _F3NetPortQosShaperHistoryIndex_Type()
)
f3NetPortQosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryIndex.setStatus("current")
_F3NetPortQosShaperHistoryTime_Type = DateAndTime
_F3NetPortQosShaperHistoryTime_Object = MibTableColumn
f3NetPortQosShaperHistoryTime = _F3NetPortQosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 2),
    _F3NetPortQosShaperHistoryTime_Type()
)
f3NetPortQosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryTime.setStatus("current")
_F3NetPortQosShaperHistoryValid_Type = TruthValue
_F3NetPortQosShaperHistoryValid_Object = MibTableColumn
f3NetPortQosShaperHistoryValid = _F3NetPortQosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 3),
    _F3NetPortQosShaperHistoryValid_Type()
)
f3NetPortQosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryValid.setStatus("current")
_F3NetPortQosShaperHistoryAction_Type = CmPmBinAction
_F3NetPortQosShaperHistoryAction_Object = MibTableColumn
f3NetPortQosShaperHistoryAction = _F3NetPortQosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 4),
    _F3NetPortQosShaperHistoryAction_Type()
)
f3NetPortQosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryAction.setStatus("current")
_F3NetPortQosShaperHistoryBT_Type = PerfCounter64
_F3NetPortQosShaperHistoryBT_Object = MibTableColumn
f3NetPortQosShaperHistoryBT = _F3NetPortQosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 5),
    _F3NetPortQosShaperHistoryBT_Type()
)
f3NetPortQosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryBT.setStatus("current")
_F3NetPortQosShaperHistoryBTD_Type = PerfCounter64
_F3NetPortQosShaperHistoryBTD_Object = MibTableColumn
f3NetPortQosShaperHistoryBTD = _F3NetPortQosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 6),
    _F3NetPortQosShaperHistoryBTD_Type()
)
f3NetPortQosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryBTD.setStatus("current")
_F3NetPortQosShaperHistoryFD_Type = PerfCounter64
_F3NetPortQosShaperHistoryFD_Object = MibTableColumn
f3NetPortQosShaperHistoryFD = _F3NetPortQosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 7),
    _F3NetPortQosShaperHistoryFD_Type()
)
f3NetPortQosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryFD.setStatus("current")
_F3NetPortQosShaperHistoryFTD_Type = PerfCounter64
_F3NetPortQosShaperHistoryFTD_Object = MibTableColumn
f3NetPortQosShaperHistoryFTD = _F3NetPortQosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 8),
    _F3NetPortQosShaperHistoryFTD_Type()
)
f3NetPortQosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryFTD.setStatus("current")
_F3NetPortQosShaperHistoryBR_Type = PerfCounter64
_F3NetPortQosShaperHistoryBR_Object = MibTableColumn
f3NetPortQosShaperHistoryBR = _F3NetPortQosShaperHistoryBR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 9),
    _F3NetPortQosShaperHistoryBR_Type()
)
f3NetPortQosShaperHistoryBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryBR.setStatus("current")
_F3NetPortQosShaperHistoryFR_Type = PerfCounter64
_F3NetPortQosShaperHistoryFR_Object = MibTableColumn
f3NetPortQosShaperHistoryFR = _F3NetPortQosShaperHistoryFR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 10),
    _F3NetPortQosShaperHistoryFR_Type()
)
f3NetPortQosShaperHistoryFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryFR.setStatus("current")
_F3NetPortQosShaperHistoryABRRL_Type = PerfCounter64
_F3NetPortQosShaperHistoryABRRL_Object = MibTableColumn
f3NetPortQosShaperHistoryABRRL = _F3NetPortQosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 11),
    _F3NetPortQosShaperHistoryABRRL_Type()
)
f3NetPortQosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryABRRL.setStatus("current")
_F3NetPortQosShaperHistoryBREDD_Type = PerfCounter64
_F3NetPortQosShaperHistoryBREDD_Object = MibTableColumn
f3NetPortQosShaperHistoryBREDD = _F3NetPortQosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 12),
    _F3NetPortQosShaperHistoryBREDD_Type()
)
f3NetPortQosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryBREDD.setStatus("current")
_F3NetPortQosShaperHistoryFREDD_Type = PerfCounter64
_F3NetPortQosShaperHistoryFREDD_Object = MibTableColumn
f3NetPortQosShaperHistoryFREDD = _F3NetPortQosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 44, 1, 13),
    _F3NetPortQosShaperHistoryFREDD_Type()
)
f3NetPortQosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperHistoryFREDD.setStatus("current")
_F3NetPortQosShaperThresholdTable_Object = MibTable
f3NetPortQosShaperThresholdTable = _F3NetPortQosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 45)
)
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdTable.setStatus("current")
_F3NetPortQosShaperThresholdEntry_Object = MibTableRow
f3NetPortQosShaperThresholdEntry = _F3NetPortQosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 45, 1)
)
f3NetPortQosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "CM-FACILITY-MIB", "f3NetPortQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdEntry.setStatus("current")


class _F3NetPortQosShaperThresholdIndex_Type(Integer32):
    """Custom type f3NetPortQosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3NetPortQosShaperThresholdIndex_Type.__name__ = "Integer32"
_F3NetPortQosShaperThresholdIndex_Object = MibTableColumn
f3NetPortQosShaperThresholdIndex = _F3NetPortQosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 45, 1, 1),
    _F3NetPortQosShaperThresholdIndex_Type()
)
f3NetPortQosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdIndex.setStatus("current")
_F3NetPortQosShaperThresholdInterval_Type = CmPmIntervalType
_F3NetPortQosShaperThresholdInterval_Object = MibTableColumn
f3NetPortQosShaperThresholdInterval = _F3NetPortQosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 45, 1, 2),
    _F3NetPortQosShaperThresholdInterval_Type()
)
f3NetPortQosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdInterval.setStatus("current")
_F3NetPortQosShaperThresholdVariable_Type = VariablePointer
_F3NetPortQosShaperThresholdVariable_Object = MibTableColumn
f3NetPortQosShaperThresholdVariable = _F3NetPortQosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 45, 1, 3),
    _F3NetPortQosShaperThresholdVariable_Type()
)
f3NetPortQosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdVariable.setStatus("current")
_F3NetPortQosShaperThresholdValueLo_Type = Unsigned32
_F3NetPortQosShaperThresholdValueLo_Object = MibTableColumn
f3NetPortQosShaperThresholdValueLo = _F3NetPortQosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 45, 1, 4),
    _F3NetPortQosShaperThresholdValueLo_Type()
)
f3NetPortQosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdValueLo.setStatus("current")
_F3NetPortQosShaperThresholdValueHi_Type = Unsigned32
_F3NetPortQosShaperThresholdValueHi_Object = MibTableColumn
f3NetPortQosShaperThresholdValueHi = _F3NetPortQosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 45, 1, 5),
    _F3NetPortQosShaperThresholdValueHi_Type()
)
f3NetPortQosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdValueHi.setStatus("current")
_F3NetPortQosShaperThresholdMonValue_Type = Counter64
_F3NetPortQosShaperThresholdMonValue_Object = MibTableColumn
f3NetPortQosShaperThresholdMonValue = _F3NetPortQosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 45, 1, 6),
    _F3NetPortQosShaperThresholdMonValue_Type()
)
f3NetPortQosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdMonValue.setStatus("current")
_OcnStmStatsTable_Object = MibTable
ocnStmStatsTable = _OcnStmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46)
)
if mibBuilder.loadTexts:
    ocnStmStatsTable.setStatus("current")
_OcnStmStatsEntry_Object = MibTableRow
ocnStmStatsEntry = _OcnStmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1)
)
ocnStmStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-PERFORMANCE-MIB", "ocnStmStatsIndex"),
)
if mibBuilder.loadTexts:
    ocnStmStatsEntry.setStatus("current")


class _OcnStmStatsIndex_Type(Integer32):
    """Custom type ocnStmStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OcnStmStatsIndex_Type.__name__ = "Integer32"
_OcnStmStatsIndex_Object = MibTableColumn
ocnStmStatsIndex = _OcnStmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 1),
    _OcnStmStatsIndex_Type()
)
ocnStmStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocnStmStatsIndex.setStatus("current")
_OcnStmStatsIntervalType_Type = CmPmIntervalType
_OcnStmStatsIntervalType_Object = MibTableColumn
ocnStmStatsIntervalType = _OcnStmStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 2),
    _OcnStmStatsIntervalType_Type()
)
ocnStmStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsIntervalType.setStatus("current")
_OcnStmStatsValid_Type = TruthValue
_OcnStmStatsValid_Object = MibTableColumn
ocnStmStatsValid = _OcnStmStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 3),
    _OcnStmStatsValid_Type()
)
ocnStmStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsValid.setStatus("current")
_OcnStmStatsAction_Type = CmPmBinAction
_OcnStmStatsAction_Object = MibTableColumn
ocnStmStatsAction = _OcnStmStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 4),
    _OcnStmStatsAction_Type()
)
ocnStmStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnStmStatsAction.setStatus("current")
_OcnStmStatsLineLBC_Type = Integer32
_OcnStmStatsLineLBC_Object = MibTableColumn
ocnStmStatsLineLBC = _OcnStmStatsLineLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 5),
    _OcnStmStatsLineLBC_Type()
)
ocnStmStatsLineLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineLBC.setStatus("current")
_OcnStmStatsLineOPT_Type = Integer32
_OcnStmStatsLineOPT_Object = MibTableColumn
ocnStmStatsLineOPT = _OcnStmStatsLineOPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 6),
    _OcnStmStatsLineOPT_Type()
)
ocnStmStatsLineOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineOPT.setStatus("current")
_OcnStmStatsLineOPR_Type = Integer32
_OcnStmStatsLineOPR_Object = MibTableColumn
ocnStmStatsLineOPR = _OcnStmStatsLineOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 7),
    _OcnStmStatsLineOPR_Type()
)
ocnStmStatsLineOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineOPR.setStatus("current")
_OcnStmStatsLineTemp_Type = Integer32
_OcnStmStatsLineTemp_Object = MibTableColumn
ocnStmStatsLineTemp = _OcnStmStatsLineTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 8),
    _OcnStmStatsLineTemp_Type()
)
ocnStmStatsLineTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineTemp.setStatus("current")
_OcnStmStatsLinePSC_Type = PerfCounter64
_OcnStmStatsLinePSC_Object = MibTableColumn
ocnStmStatsLinePSC = _OcnStmStatsLinePSC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 9),
    _OcnStmStatsLinePSC_Type()
)
ocnStmStatsLinePSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLinePSC.setStatus("current")
_OcnStmStatsLineESs_Type = PerfCounter64
_OcnStmStatsLineESs_Object = MibTableColumn
ocnStmStatsLineESs = _OcnStmStatsLineESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 10),
    _OcnStmStatsLineESs_Type()
)
ocnStmStatsLineESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineESs.setStatus("current")
_OcnStmStatsLineSESs_Type = PerfCounter64
_OcnStmStatsLineSESs_Object = MibTableColumn
ocnStmStatsLineSESs = _OcnStmStatsLineSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 11),
    _OcnStmStatsLineSESs_Type()
)
ocnStmStatsLineSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineSESs.setStatus("current")
_OcnStmStatsLineCVs_Type = PerfCounter64
_OcnStmStatsLineCVs_Object = MibTableColumn
ocnStmStatsLineCVs = _OcnStmStatsLineCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 12),
    _OcnStmStatsLineCVs_Type()
)
ocnStmStatsLineCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineCVs.setStatus("current")
_OcnStmStatsLineUASs_Type = PerfCounter64
_OcnStmStatsLineUASs_Object = MibTableColumn
ocnStmStatsLineUASs = _OcnStmStatsLineUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 13),
    _OcnStmStatsLineUASs_Type()
)
ocnStmStatsLineUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineUASs.setStatus("current")
_OcnStmStatsLineFCs_Type = PerfCounter64
_OcnStmStatsLineFCs_Object = MibTableColumn
ocnStmStatsLineFCs = _OcnStmStatsLineFCs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 14),
    _OcnStmStatsLineFCs_Type()
)
ocnStmStatsLineFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineFCs.setStatus("current")
_OcnStmStatsLineFarEndESs_Type = PerfCounter64
_OcnStmStatsLineFarEndESs_Object = MibTableColumn
ocnStmStatsLineFarEndESs = _OcnStmStatsLineFarEndESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 15),
    _OcnStmStatsLineFarEndESs_Type()
)
ocnStmStatsLineFarEndESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineFarEndESs.setStatus("current")
_OcnStmStatsLineFarEndSESs_Type = PerfCounter64
_OcnStmStatsLineFarEndSESs_Object = MibTableColumn
ocnStmStatsLineFarEndSESs = _OcnStmStatsLineFarEndSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 16),
    _OcnStmStatsLineFarEndSESs_Type()
)
ocnStmStatsLineFarEndSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineFarEndSESs.setStatus("current")
_OcnStmStatsLineFarEndCVs_Type = PerfCounter64
_OcnStmStatsLineFarEndCVs_Object = MibTableColumn
ocnStmStatsLineFarEndCVs = _OcnStmStatsLineFarEndCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 17),
    _OcnStmStatsLineFarEndCVs_Type()
)
ocnStmStatsLineFarEndCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineFarEndCVs.setStatus("current")
_OcnStmStatsLineFarEndUASs_Type = PerfCounter64
_OcnStmStatsLineFarEndUASs_Object = MibTableColumn
ocnStmStatsLineFarEndUASs = _OcnStmStatsLineFarEndUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 18),
    _OcnStmStatsLineFarEndUASs_Type()
)
ocnStmStatsLineFarEndUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsLineFarEndUASs.setStatus("current")
_OcnStmStatsSectionESs_Type = PerfCounter64
_OcnStmStatsSectionESs_Object = MibTableColumn
ocnStmStatsSectionESs = _OcnStmStatsSectionESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 19),
    _OcnStmStatsSectionESs_Type()
)
ocnStmStatsSectionESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsSectionESs.setStatus("current")
_OcnStmStatsSectionSESs_Type = PerfCounter64
_OcnStmStatsSectionSESs_Object = MibTableColumn
ocnStmStatsSectionSESs = _OcnStmStatsSectionSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 20),
    _OcnStmStatsSectionSESs_Type()
)
ocnStmStatsSectionSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsSectionSESs.setStatus("current")
_OcnStmStatsSectionCVs_Type = PerfCounter64
_OcnStmStatsSectionCVs_Object = MibTableColumn
ocnStmStatsSectionCVs = _OcnStmStatsSectionCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 21),
    _OcnStmStatsSectionCVs_Type()
)
ocnStmStatsSectionCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsSectionCVs.setStatus("current")
_OcnStmStatsSectionSEFs_Type = PerfCounter64
_OcnStmStatsSectionSEFs_Object = MibTableColumn
ocnStmStatsSectionSEFs = _OcnStmStatsSectionSEFs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 22),
    _OcnStmStatsSectionSEFs_Type()
)
ocnStmStatsSectionSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsSectionSEFs.setStatus("current")
_OcnStmStatsSectionUASs_Type = PerfCounter64
_OcnStmStatsSectionUASs_Object = MibTableColumn
ocnStmStatsSectionUASs = _OcnStmStatsSectionUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 46, 1, 23),
    _OcnStmStatsSectionUASs_Type()
)
ocnStmStatsSectionUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmStatsSectionUASs.setStatus("current")
_OcnStmHistoryTable_Object = MibTable
ocnStmHistoryTable = _OcnStmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47)
)
if mibBuilder.loadTexts:
    ocnStmHistoryTable.setStatus("current")
_OcnStmHistoryEntry_Object = MibTableRow
ocnStmHistoryEntry = _OcnStmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1)
)
ocnStmHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-PERFORMANCE-MIB", "ocnStmStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "ocnStmHistoryIndex"),
)
if mibBuilder.loadTexts:
    ocnStmHistoryEntry.setStatus("current")


class _OcnStmHistoryIndex_Type(Integer32):
    """Custom type ocnStmHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OcnStmHistoryIndex_Type.__name__ = "Integer32"
_OcnStmHistoryIndex_Object = MibTableColumn
ocnStmHistoryIndex = _OcnStmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 1),
    _OcnStmHistoryIndex_Type()
)
ocnStmHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocnStmHistoryIndex.setStatus("current")
_OcnStmHistoryTime_Type = DateAndTime
_OcnStmHistoryTime_Object = MibTableColumn
ocnStmHistoryTime = _OcnStmHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 2),
    _OcnStmHistoryTime_Type()
)
ocnStmHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryTime.setStatus("current")
_OcnStmHistoryValid_Type = TruthValue
_OcnStmHistoryValid_Object = MibTableColumn
ocnStmHistoryValid = _OcnStmHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 3),
    _OcnStmHistoryValid_Type()
)
ocnStmHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryValid.setStatus("current")
_OcnStmHistoryAction_Type = CmPmBinAction
_OcnStmHistoryAction_Object = MibTableColumn
ocnStmHistoryAction = _OcnStmHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 4),
    _OcnStmHistoryAction_Type()
)
ocnStmHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnStmHistoryAction.setStatus("current")
_OcnStmHistoryLineLBC_Type = Integer32
_OcnStmHistoryLineLBC_Object = MibTableColumn
ocnStmHistoryLineLBC = _OcnStmHistoryLineLBC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 5),
    _OcnStmHistoryLineLBC_Type()
)
ocnStmHistoryLineLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineLBC.setStatus("current")
_OcnStmHistoryLineOPT_Type = Integer32
_OcnStmHistoryLineOPT_Object = MibTableColumn
ocnStmHistoryLineOPT = _OcnStmHistoryLineOPT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 6),
    _OcnStmHistoryLineOPT_Type()
)
ocnStmHistoryLineOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineOPT.setStatus("current")
_OcnStmHistoryLineOPR_Type = Integer32
_OcnStmHistoryLineOPR_Object = MibTableColumn
ocnStmHistoryLineOPR = _OcnStmHistoryLineOPR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 7),
    _OcnStmHistoryLineOPR_Type()
)
ocnStmHistoryLineOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineOPR.setStatus("current")
_OcnStmHistoryLineTemp_Type = Integer32
_OcnStmHistoryLineTemp_Object = MibTableColumn
ocnStmHistoryLineTemp = _OcnStmHistoryLineTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 8),
    _OcnStmHistoryLineTemp_Type()
)
ocnStmHistoryLineTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineTemp.setStatus("current")
_OcnStmHistoryLinePSC_Type = PerfCounter64
_OcnStmHistoryLinePSC_Object = MibTableColumn
ocnStmHistoryLinePSC = _OcnStmHistoryLinePSC_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 9),
    _OcnStmHistoryLinePSC_Type()
)
ocnStmHistoryLinePSC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLinePSC.setStatus("current")
_OcnStmHistoryLineESs_Type = PerfCounter64
_OcnStmHistoryLineESs_Object = MibTableColumn
ocnStmHistoryLineESs = _OcnStmHistoryLineESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 10),
    _OcnStmHistoryLineESs_Type()
)
ocnStmHistoryLineESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineESs.setStatus("current")
_OcnStmHistoryLineSESs_Type = PerfCounter64
_OcnStmHistoryLineSESs_Object = MibTableColumn
ocnStmHistoryLineSESs = _OcnStmHistoryLineSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 11),
    _OcnStmHistoryLineSESs_Type()
)
ocnStmHistoryLineSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineSESs.setStatus("current")
_OcnStmHistoryLineCVs_Type = PerfCounter64
_OcnStmHistoryLineCVs_Object = MibTableColumn
ocnStmHistoryLineCVs = _OcnStmHistoryLineCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 12),
    _OcnStmHistoryLineCVs_Type()
)
ocnStmHistoryLineCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineCVs.setStatus("current")
_OcnStmHistoryLineUASs_Type = PerfCounter64
_OcnStmHistoryLineUASs_Object = MibTableColumn
ocnStmHistoryLineUASs = _OcnStmHistoryLineUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 13),
    _OcnStmHistoryLineUASs_Type()
)
ocnStmHistoryLineUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineUASs.setStatus("current")
_OcnStmHistoryLineFCs_Type = PerfCounter64
_OcnStmHistoryLineFCs_Object = MibTableColumn
ocnStmHistoryLineFCs = _OcnStmHistoryLineFCs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 14),
    _OcnStmHistoryLineFCs_Type()
)
ocnStmHistoryLineFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineFCs.setStatus("current")
_OcnStmHistoryLineFarEndESs_Type = PerfCounter64
_OcnStmHistoryLineFarEndESs_Object = MibTableColumn
ocnStmHistoryLineFarEndESs = _OcnStmHistoryLineFarEndESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 15),
    _OcnStmHistoryLineFarEndESs_Type()
)
ocnStmHistoryLineFarEndESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineFarEndESs.setStatus("current")
_OcnStmHistoryLineFarEndSESs_Type = PerfCounter64
_OcnStmHistoryLineFarEndSESs_Object = MibTableColumn
ocnStmHistoryLineFarEndSESs = _OcnStmHistoryLineFarEndSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 16),
    _OcnStmHistoryLineFarEndSESs_Type()
)
ocnStmHistoryLineFarEndSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineFarEndSESs.setStatus("current")
_OcnStmHistoryLineFarEndCVs_Type = PerfCounter64
_OcnStmHistoryLineFarEndCVs_Object = MibTableColumn
ocnStmHistoryLineFarEndCVs = _OcnStmHistoryLineFarEndCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 17),
    _OcnStmHistoryLineFarEndCVs_Type()
)
ocnStmHistoryLineFarEndCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineFarEndCVs.setStatus("current")
_OcnStmHistoryLineFarEndUASs_Type = PerfCounter64
_OcnStmHistoryLineFarEndUASs_Object = MibTableColumn
ocnStmHistoryLineFarEndUASs = _OcnStmHistoryLineFarEndUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 18),
    _OcnStmHistoryLineFarEndUASs_Type()
)
ocnStmHistoryLineFarEndUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistoryLineFarEndUASs.setStatus("current")
_OcnStmHistorySectionESs_Type = PerfCounter64
_OcnStmHistorySectionESs_Object = MibTableColumn
ocnStmHistorySectionESs = _OcnStmHistorySectionESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 19),
    _OcnStmHistorySectionESs_Type()
)
ocnStmHistorySectionESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistorySectionESs.setStatus("current")
_OcnStmHistorySectionSESs_Type = PerfCounter64
_OcnStmHistorySectionSESs_Object = MibTableColumn
ocnStmHistorySectionSESs = _OcnStmHistorySectionSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 20),
    _OcnStmHistorySectionSESs_Type()
)
ocnStmHistorySectionSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistorySectionSESs.setStatus("current")
_OcnStmHistorySectionCVs_Type = PerfCounter64
_OcnStmHistorySectionCVs_Object = MibTableColumn
ocnStmHistorySectionCVs = _OcnStmHistorySectionCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 21),
    _OcnStmHistorySectionCVs_Type()
)
ocnStmHistorySectionCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistorySectionCVs.setStatus("current")
_OcnStmHistorySectionSEFs_Type = PerfCounter64
_OcnStmHistorySectionSEFs_Object = MibTableColumn
ocnStmHistorySectionSEFs = _OcnStmHistorySectionSEFs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 22),
    _OcnStmHistorySectionSEFs_Type()
)
ocnStmHistorySectionSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistorySectionSEFs.setStatus("current")
_OcnStmHistorySectionUASs_Type = PerfCounter64
_OcnStmHistorySectionUASs_Object = MibTableColumn
ocnStmHistorySectionUASs = _OcnStmHistorySectionUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 47, 1, 23),
    _OcnStmHistorySectionUASs_Type()
)
ocnStmHistorySectionUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmHistorySectionUASs.setStatus("current")
_OcnStmThresholdTable_Object = MibTable
ocnStmThresholdTable = _OcnStmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 48)
)
if mibBuilder.loadTexts:
    ocnStmThresholdTable.setStatus("current")
_OcnStmThresholdEntry_Object = MibTableRow
ocnStmThresholdEntry = _OcnStmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 48, 1)
)
ocnStmThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-PERFORMANCE-MIB", "ocnStmStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "ocnStmThresholdIndex"),
)
if mibBuilder.loadTexts:
    ocnStmThresholdEntry.setStatus("current")


class _OcnStmThresholdIndex_Type(Integer32):
    """Custom type ocnStmThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OcnStmThresholdIndex_Type.__name__ = "Integer32"
_OcnStmThresholdIndex_Object = MibTableColumn
ocnStmThresholdIndex = _OcnStmThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 48, 1, 1),
    _OcnStmThresholdIndex_Type()
)
ocnStmThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocnStmThresholdIndex.setStatus("current")
_OcnStmThresholdInterval_Type = CmPmIntervalType
_OcnStmThresholdInterval_Object = MibTableColumn
ocnStmThresholdInterval = _OcnStmThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 48, 1, 2),
    _OcnStmThresholdInterval_Type()
)
ocnStmThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmThresholdInterval.setStatus("current")
_OcnStmThresholdVariable_Type = VariablePointer
_OcnStmThresholdVariable_Object = MibTableColumn
ocnStmThresholdVariable = _OcnStmThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 48, 1, 3),
    _OcnStmThresholdVariable_Type()
)
ocnStmThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmThresholdVariable.setStatus("current")
_OcnStmThresholdValueLo_Type = Unsigned32
_OcnStmThresholdValueLo_Object = MibTableColumn
ocnStmThresholdValueLo = _OcnStmThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 48, 1, 4),
    _OcnStmThresholdValueLo_Type()
)
ocnStmThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnStmThresholdValueLo.setStatus("current")
_OcnStmThresholdValueHi_Type = Unsigned32
_OcnStmThresholdValueHi_Object = MibTableColumn
ocnStmThresholdValueHi = _OcnStmThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 48, 1, 5),
    _OcnStmThresholdValueHi_Type()
)
ocnStmThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnStmThresholdValueHi.setStatus("current")
_OcnStmThresholdMonValue_Type = Counter64
_OcnStmThresholdMonValue_Object = MibTableColumn
ocnStmThresholdMonValue = _OcnStmThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 48, 1, 6),
    _OcnStmThresholdMonValue_Type()
)
ocnStmThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocnStmThresholdMonValue.setStatus("current")
_StsVcPathStatsTable_Object = MibTable
stsVcPathStatsTable = _StsVcPathStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49)
)
if mibBuilder.loadTexts:
    stsVcPathStatsTable.setStatus("current")
_StsVcPathStatsEntry_Object = MibTableRow
stsVcPathStatsEntry = _StsVcPathStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1)
)
stsVcPathStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-FACILITY-MIB", "stsVcPathParentIfIndex"),
    (0, "CM-FACILITY-MIB", "stsVcPathIndex"),
    (0, "CM-PERFORMANCE-MIB", "stsVcPathStatsIndex"),
)
if mibBuilder.loadTexts:
    stsVcPathStatsEntry.setStatus("current")


class _StsVcPathStatsIndex_Type(Integer32):
    """Custom type stsVcPathStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StsVcPathStatsIndex_Type.__name__ = "Integer32"
_StsVcPathStatsIndex_Object = MibTableColumn
stsVcPathStatsIndex = _StsVcPathStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 1),
    _StsVcPathStatsIndex_Type()
)
stsVcPathStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stsVcPathStatsIndex.setStatus("current")
_StsVcPathStatsIntervalType_Type = CmPmIntervalType
_StsVcPathStatsIntervalType_Object = MibTableColumn
stsVcPathStatsIntervalType = _StsVcPathStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 2),
    _StsVcPathStatsIntervalType_Type()
)
stsVcPathStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathStatsIntervalType.setStatus("current")
_StsVcPathStatsValid_Type = TruthValue
_StsVcPathStatsValid_Object = MibTableColumn
stsVcPathStatsValid = _StsVcPathStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 3),
    _StsVcPathStatsValid_Type()
)
stsVcPathStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathStatsValid.setStatus("current")
_StsVcPathStatsAction_Type = CmPmBinAction
_StsVcPathStatsAction_Object = MibTableColumn
stsVcPathStatsAction = _StsVcPathStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 4),
    _StsVcPathStatsAction_Type()
)
stsVcPathStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsVcPathStatsAction.setStatus("current")
_StsVcPathStatsESs_Type = PerfCounter64
_StsVcPathStatsESs_Object = MibTableColumn
stsVcPathStatsESs = _StsVcPathStatsESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 5),
    _StsVcPathStatsESs_Type()
)
stsVcPathStatsESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathStatsESs.setStatus("current")
_StsVcPathStatsSESs_Type = PerfCounter64
_StsVcPathStatsSESs_Object = MibTableColumn
stsVcPathStatsSESs = _StsVcPathStatsSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 6),
    _StsVcPathStatsSESs_Type()
)
stsVcPathStatsSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathStatsSESs.setStatus("current")
_StsVcPathStatsCVs_Type = PerfCounter64
_StsVcPathStatsCVs_Object = MibTableColumn
stsVcPathStatsCVs = _StsVcPathStatsCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 7),
    _StsVcPathStatsCVs_Type()
)
stsVcPathStatsCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathStatsCVs.setStatus("current")
_StsVcPathStatsUASs_Type = PerfCounter64
_StsVcPathStatsUASs_Object = MibTableColumn
stsVcPathStatsUASs = _StsVcPathStatsUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 8),
    _StsVcPathStatsUASs_Type()
)
stsVcPathStatsUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathStatsUASs.setStatus("current")
_StsVcPathFarEndStatsESs_Type = PerfCounter64
_StsVcPathFarEndStatsESs_Object = MibTableColumn
stsVcPathFarEndStatsESs = _StsVcPathFarEndStatsESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 9),
    _StsVcPathFarEndStatsESs_Type()
)
stsVcPathFarEndStatsESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathFarEndStatsESs.setStatus("current")
_StsVcPathFarEndStatsSESs_Type = PerfCounter64
_StsVcPathFarEndStatsSESs_Object = MibTableColumn
stsVcPathFarEndStatsSESs = _StsVcPathFarEndStatsSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 10),
    _StsVcPathFarEndStatsSESs_Type()
)
stsVcPathFarEndStatsSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathFarEndStatsSESs.setStatus("current")
_StsVcPathFarEndStatsCVs_Type = PerfCounter64
_StsVcPathFarEndStatsCVs_Object = MibTableColumn
stsVcPathFarEndStatsCVs = _StsVcPathFarEndStatsCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 11),
    _StsVcPathFarEndStatsCVs_Type()
)
stsVcPathFarEndStatsCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathFarEndStatsCVs.setStatus("current")
_StsVcPathFarEndStatsUASs_Type = PerfCounter64
_StsVcPathFarEndStatsUASs_Object = MibTableColumn
stsVcPathFarEndStatsUASs = _StsVcPathFarEndStatsUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 49, 1, 12),
    _StsVcPathFarEndStatsUASs_Type()
)
stsVcPathFarEndStatsUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathFarEndStatsUASs.setStatus("current")
_StsVcPathHistoryTable_Object = MibTable
stsVcPathHistoryTable = _StsVcPathHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50)
)
if mibBuilder.loadTexts:
    stsVcPathHistoryTable.setStatus("current")
_StsVcPathHistoryEntry_Object = MibTableRow
stsVcPathHistoryEntry = _StsVcPathHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1)
)
stsVcPathHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-FACILITY-MIB", "stsVcPathParentIfIndex"),
    (0, "CM-FACILITY-MIB", "stsVcPathIndex"),
    (0, "CM-PERFORMANCE-MIB", "stsVcPathStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "stsVcPathHistoryIndex"),
)
if mibBuilder.loadTexts:
    stsVcPathHistoryEntry.setStatus("current")


class _StsVcPathHistoryIndex_Type(Integer32):
    """Custom type stsVcPathHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StsVcPathHistoryIndex_Type.__name__ = "Integer32"
_StsVcPathHistoryIndex_Object = MibTableColumn
stsVcPathHistoryIndex = _StsVcPathHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 1),
    _StsVcPathHistoryIndex_Type()
)
stsVcPathHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stsVcPathHistoryIndex.setStatus("current")
_StsVcPathHistoryTime_Type = DateAndTime
_StsVcPathHistoryTime_Object = MibTableColumn
stsVcPathHistoryTime = _StsVcPathHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 2),
    _StsVcPathHistoryTime_Type()
)
stsVcPathHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathHistoryTime.setStatus("current")
_StsVcPathHistoryValid_Type = TruthValue
_StsVcPathHistoryValid_Object = MibTableColumn
stsVcPathHistoryValid = _StsVcPathHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 3),
    _StsVcPathHistoryValid_Type()
)
stsVcPathHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathHistoryValid.setStatus("current")
_StsVcPathHistoryAction_Type = CmPmBinAction
_StsVcPathHistoryAction_Object = MibTableColumn
stsVcPathHistoryAction = _StsVcPathHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 4),
    _StsVcPathHistoryAction_Type()
)
stsVcPathHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsVcPathHistoryAction.setStatus("current")
_StsVcPathHistoryESs_Type = PerfCounter64
_StsVcPathHistoryESs_Object = MibTableColumn
stsVcPathHistoryESs = _StsVcPathHistoryESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 5),
    _StsVcPathHistoryESs_Type()
)
stsVcPathHistoryESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathHistoryESs.setStatus("current")
_StsVcPathHistorySESs_Type = PerfCounter64
_StsVcPathHistorySESs_Object = MibTableColumn
stsVcPathHistorySESs = _StsVcPathHistorySESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 6),
    _StsVcPathHistorySESs_Type()
)
stsVcPathHistorySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathHistorySESs.setStatus("current")
_StsVcPathHistoryCVs_Type = PerfCounter64
_StsVcPathHistoryCVs_Object = MibTableColumn
stsVcPathHistoryCVs = _StsVcPathHistoryCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 7),
    _StsVcPathHistoryCVs_Type()
)
stsVcPathHistoryCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathHistoryCVs.setStatus("current")
_StsVcPathHistoryUASs_Type = PerfCounter64
_StsVcPathHistoryUASs_Object = MibTableColumn
stsVcPathHistoryUASs = _StsVcPathHistoryUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 8),
    _StsVcPathHistoryUASs_Type()
)
stsVcPathHistoryUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathHistoryUASs.setStatus("current")
_StsVcPathFarEndHistoryESs_Type = PerfCounter64
_StsVcPathFarEndHistoryESs_Object = MibTableColumn
stsVcPathFarEndHistoryESs = _StsVcPathFarEndHistoryESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 9),
    _StsVcPathFarEndHistoryESs_Type()
)
stsVcPathFarEndHistoryESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathFarEndHistoryESs.setStatus("current")
_StsVcPathFarEndHistorySESs_Type = PerfCounter64
_StsVcPathFarEndHistorySESs_Object = MibTableColumn
stsVcPathFarEndHistorySESs = _StsVcPathFarEndHistorySESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 10),
    _StsVcPathFarEndHistorySESs_Type()
)
stsVcPathFarEndHistorySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathFarEndHistorySESs.setStatus("current")
_StsVcPathFarEndHistoryCVs_Type = PerfCounter64
_StsVcPathFarEndHistoryCVs_Object = MibTableColumn
stsVcPathFarEndHistoryCVs = _StsVcPathFarEndHistoryCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 11),
    _StsVcPathFarEndHistoryCVs_Type()
)
stsVcPathFarEndHistoryCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathFarEndHistoryCVs.setStatus("current")
_StsVcPathFarEndHistoryUASs_Type = PerfCounter64
_StsVcPathFarEndHistoryUASs_Object = MibTableColumn
stsVcPathFarEndHistoryUASs = _StsVcPathFarEndHistoryUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 50, 1, 12),
    _StsVcPathFarEndHistoryUASs_Type()
)
stsVcPathFarEndHistoryUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathFarEndHistoryUASs.setStatus("current")
_StsVcPathThresholdTable_Object = MibTable
stsVcPathThresholdTable = _StsVcPathThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 51)
)
if mibBuilder.loadTexts:
    stsVcPathThresholdTable.setStatus("current")
_StsVcPathThresholdEntry_Object = MibTableRow
stsVcPathThresholdEntry = _StsVcPathThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 51, 1)
)
stsVcPathThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-FACILITY-MIB", "stsVcPathParentIfIndex"),
    (0, "CM-FACILITY-MIB", "stsVcPathIndex"),
    (0, "CM-PERFORMANCE-MIB", "stsVcPathStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "stsVcPathThresholdIndex"),
)
if mibBuilder.loadTexts:
    stsVcPathThresholdEntry.setStatus("current")


class _StsVcPathThresholdIndex_Type(Integer32):
    """Custom type stsVcPathThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StsVcPathThresholdIndex_Type.__name__ = "Integer32"
_StsVcPathThresholdIndex_Object = MibTableColumn
stsVcPathThresholdIndex = _StsVcPathThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 51, 1, 1),
    _StsVcPathThresholdIndex_Type()
)
stsVcPathThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stsVcPathThresholdIndex.setStatus("current")
_StsVcPathThresholdInterval_Type = CmPmIntervalType
_StsVcPathThresholdInterval_Object = MibTableColumn
stsVcPathThresholdInterval = _StsVcPathThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 51, 1, 2),
    _StsVcPathThresholdInterval_Type()
)
stsVcPathThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathThresholdInterval.setStatus("current")
_StsVcPathThresholdVariable_Type = VariablePointer
_StsVcPathThresholdVariable_Object = MibTableColumn
stsVcPathThresholdVariable = _StsVcPathThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 51, 1, 3),
    _StsVcPathThresholdVariable_Type()
)
stsVcPathThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathThresholdVariable.setStatus("current")
_StsVcPathThresholdValueLo_Type = Unsigned32
_StsVcPathThresholdValueLo_Object = MibTableColumn
stsVcPathThresholdValueLo = _StsVcPathThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 51, 1, 4),
    _StsVcPathThresholdValueLo_Type()
)
stsVcPathThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsVcPathThresholdValueLo.setStatus("current")
_StsVcPathThresholdValueHi_Type = Unsigned32
_StsVcPathThresholdValueHi_Object = MibTableColumn
stsVcPathThresholdValueHi = _StsVcPathThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 51, 1, 5),
    _StsVcPathThresholdValueHi_Type()
)
stsVcPathThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stsVcPathThresholdValueHi.setStatus("current")
_StsVcPathThresholdMonValue_Type = Counter64
_StsVcPathThresholdMonValue_Object = MibTableColumn
stsVcPathThresholdMonValue = _StsVcPathThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 51, 1, 6),
    _StsVcPathThresholdMonValue_Type()
)
stsVcPathThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stsVcPathThresholdMonValue.setStatus("current")
_VtVcPathStatsTable_Object = MibTable
vtVcPathStatsTable = _VtVcPathStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52)
)
if mibBuilder.loadTexts:
    vtVcPathStatsTable.setStatus("current")
_VtVcPathStatsEntry_Object = MibTableRow
vtVcPathStatsEntry = _VtVcPathStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1)
)
vtVcPathStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-FACILITY-MIB", "vtVcPathParentIfIndex"),
    (0, "CM-FACILITY-MIB", "vtVcPathIndex"),
    (0, "CM-PERFORMANCE-MIB", "vtVcPathStatsIndex"),
)
if mibBuilder.loadTexts:
    vtVcPathStatsEntry.setStatus("current")


class _VtVcPathStatsIndex_Type(Integer32):
    """Custom type vtVcPathStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VtVcPathStatsIndex_Type.__name__ = "Integer32"
_VtVcPathStatsIndex_Object = MibTableColumn
vtVcPathStatsIndex = _VtVcPathStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 1),
    _VtVcPathStatsIndex_Type()
)
vtVcPathStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtVcPathStatsIndex.setStatus("current")
_VtVcPathStatsIntervalType_Type = CmPmIntervalType
_VtVcPathStatsIntervalType_Object = MibTableColumn
vtVcPathStatsIntervalType = _VtVcPathStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 2),
    _VtVcPathStatsIntervalType_Type()
)
vtVcPathStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathStatsIntervalType.setStatus("current")
_VtVcPathStatsValid_Type = TruthValue
_VtVcPathStatsValid_Object = MibTableColumn
vtVcPathStatsValid = _VtVcPathStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 3),
    _VtVcPathStatsValid_Type()
)
vtVcPathStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathStatsValid.setStatus("current")
_VtVcPathStatsAction_Type = CmPmBinAction
_VtVcPathStatsAction_Object = MibTableColumn
vtVcPathStatsAction = _VtVcPathStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 4),
    _VtVcPathStatsAction_Type()
)
vtVcPathStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtVcPathStatsAction.setStatus("current")
_VtVcPathStatsESs_Type = PerfCounter64
_VtVcPathStatsESs_Object = MibTableColumn
vtVcPathStatsESs = _VtVcPathStatsESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 5),
    _VtVcPathStatsESs_Type()
)
vtVcPathStatsESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathStatsESs.setStatus("current")
_VtVcPathStatsSESs_Type = PerfCounter64
_VtVcPathStatsSESs_Object = MibTableColumn
vtVcPathStatsSESs = _VtVcPathStatsSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 6),
    _VtVcPathStatsSESs_Type()
)
vtVcPathStatsSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathStatsSESs.setStatus("current")
_VtVcPathStatsCVs_Type = PerfCounter64
_VtVcPathStatsCVs_Object = MibTableColumn
vtVcPathStatsCVs = _VtVcPathStatsCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 7),
    _VtVcPathStatsCVs_Type()
)
vtVcPathStatsCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathStatsCVs.setStatus("current")
_VtVcPathStatsUASs_Type = PerfCounter64
_VtVcPathStatsUASs_Object = MibTableColumn
vtVcPathStatsUASs = _VtVcPathStatsUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 8),
    _VtVcPathStatsUASs_Type()
)
vtVcPathStatsUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathStatsUASs.setStatus("current")
_VtVcPathFarEndStatsESs_Type = PerfCounter64
_VtVcPathFarEndStatsESs_Object = MibTableColumn
vtVcPathFarEndStatsESs = _VtVcPathFarEndStatsESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 9),
    _VtVcPathFarEndStatsESs_Type()
)
vtVcPathFarEndStatsESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathFarEndStatsESs.setStatus("current")
_VtVcPathFarEndStatsSESs_Type = PerfCounter64
_VtVcPathFarEndStatsSESs_Object = MibTableColumn
vtVcPathFarEndStatsSESs = _VtVcPathFarEndStatsSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 10),
    _VtVcPathFarEndStatsSESs_Type()
)
vtVcPathFarEndStatsSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathFarEndStatsSESs.setStatus("current")
_VtVcPathFarEndStatsCVs_Type = PerfCounter64
_VtVcPathFarEndStatsCVs_Object = MibTableColumn
vtVcPathFarEndStatsCVs = _VtVcPathFarEndStatsCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 11),
    _VtVcPathFarEndStatsCVs_Type()
)
vtVcPathFarEndStatsCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathFarEndStatsCVs.setStatus("current")
_VtVcPathFarEndStatsUASs_Type = PerfCounter64
_VtVcPathFarEndStatsUASs_Object = MibTableColumn
vtVcPathFarEndStatsUASs = _VtVcPathFarEndStatsUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 52, 1, 12),
    _VtVcPathFarEndStatsUASs_Type()
)
vtVcPathFarEndStatsUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathFarEndStatsUASs.setStatus("current")
_VtVcPathHistoryTable_Object = MibTable
vtVcPathHistoryTable = _VtVcPathHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53)
)
if mibBuilder.loadTexts:
    vtVcPathHistoryTable.setStatus("current")
_VtVcPathHistoryEntry_Object = MibTableRow
vtVcPathHistoryEntry = _VtVcPathHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1)
)
vtVcPathHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-FACILITY-MIB", "vtVcPathParentIfIndex"),
    (0, "CM-FACILITY-MIB", "vtVcPathIndex"),
    (0, "CM-PERFORMANCE-MIB", "vtVcPathStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "vtVcPathHistoryIndex"),
)
if mibBuilder.loadTexts:
    vtVcPathHistoryEntry.setStatus("current")


class _VtVcPathHistoryIndex_Type(Integer32):
    """Custom type vtVcPathHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VtVcPathHistoryIndex_Type.__name__ = "Integer32"
_VtVcPathHistoryIndex_Object = MibTableColumn
vtVcPathHistoryIndex = _VtVcPathHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 1),
    _VtVcPathHistoryIndex_Type()
)
vtVcPathHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtVcPathHistoryIndex.setStatus("current")
_VtVcPathHistoryTime_Type = DateAndTime
_VtVcPathHistoryTime_Object = MibTableColumn
vtVcPathHistoryTime = _VtVcPathHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 2),
    _VtVcPathHistoryTime_Type()
)
vtVcPathHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathHistoryTime.setStatus("current")
_VtVcPathHistoryValid_Type = TruthValue
_VtVcPathHistoryValid_Object = MibTableColumn
vtVcPathHistoryValid = _VtVcPathHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 3),
    _VtVcPathHistoryValid_Type()
)
vtVcPathHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathHistoryValid.setStatus("current")
_VtVcPathHistoryAction_Type = CmPmBinAction
_VtVcPathHistoryAction_Object = MibTableColumn
vtVcPathHistoryAction = _VtVcPathHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 4),
    _VtVcPathHistoryAction_Type()
)
vtVcPathHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtVcPathHistoryAction.setStatus("current")
_VtVcPathHistoryESs_Type = PerfCounter64
_VtVcPathHistoryESs_Object = MibTableColumn
vtVcPathHistoryESs = _VtVcPathHistoryESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 5),
    _VtVcPathHistoryESs_Type()
)
vtVcPathHistoryESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathHistoryESs.setStatus("current")
_VtVcPathHistorySESs_Type = PerfCounter64
_VtVcPathHistorySESs_Object = MibTableColumn
vtVcPathHistorySESs = _VtVcPathHistorySESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 6),
    _VtVcPathHistorySESs_Type()
)
vtVcPathHistorySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathHistorySESs.setStatus("current")
_VtVcPathHistoryCVs_Type = PerfCounter64
_VtVcPathHistoryCVs_Object = MibTableColumn
vtVcPathHistoryCVs = _VtVcPathHistoryCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 7),
    _VtVcPathHistoryCVs_Type()
)
vtVcPathHistoryCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathHistoryCVs.setStatus("current")
_VtVcPathHistoryUASs_Type = PerfCounter64
_VtVcPathHistoryUASs_Object = MibTableColumn
vtVcPathHistoryUASs = _VtVcPathHistoryUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 8),
    _VtVcPathHistoryUASs_Type()
)
vtVcPathHistoryUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathHistoryUASs.setStatus("current")
_VtVcPathFarEndHistoryESs_Type = PerfCounter64
_VtVcPathFarEndHistoryESs_Object = MibTableColumn
vtVcPathFarEndHistoryESs = _VtVcPathFarEndHistoryESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 9),
    _VtVcPathFarEndHistoryESs_Type()
)
vtVcPathFarEndHistoryESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathFarEndHistoryESs.setStatus("current")
_VtVcPathFarEndHistorySESs_Type = PerfCounter64
_VtVcPathFarEndHistorySESs_Object = MibTableColumn
vtVcPathFarEndHistorySESs = _VtVcPathFarEndHistorySESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 10),
    _VtVcPathFarEndHistorySESs_Type()
)
vtVcPathFarEndHistorySESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathFarEndHistorySESs.setStatus("current")
_VtVcPathFarEndHistoryCVs_Type = PerfCounter64
_VtVcPathFarEndHistoryCVs_Object = MibTableColumn
vtVcPathFarEndHistoryCVs = _VtVcPathFarEndHistoryCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 11),
    _VtVcPathFarEndHistoryCVs_Type()
)
vtVcPathFarEndHistoryCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathFarEndHistoryCVs.setStatus("current")
_VtVcPathFarEndHistoryUASs_Type = PerfCounter64
_VtVcPathFarEndHistoryUASs_Object = MibTableColumn
vtVcPathFarEndHistoryUASs = _VtVcPathFarEndHistoryUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 53, 1, 12),
    _VtVcPathFarEndHistoryUASs_Type()
)
vtVcPathFarEndHistoryUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathFarEndHistoryUASs.setStatus("current")
_VtVcPathThresholdTable_Object = MibTable
vtVcPathThresholdTable = _VtVcPathThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 54)
)
if mibBuilder.loadTexts:
    vtVcPathThresholdTable.setStatus("current")
_VtVcPathThresholdEntry_Object = MibTableRow
vtVcPathThresholdEntry = _VtVcPathThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 54, 1)
)
vtVcPathThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-FACILITY-MIB", "vtVcPathParentIfIndex"),
    (0, "CM-FACILITY-MIB", "vtVcPathIndex"),
    (0, "CM-PERFORMANCE-MIB", "vtVcPathStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "vtVcPathThresholdIndex"),
)
if mibBuilder.loadTexts:
    vtVcPathThresholdEntry.setStatus("current")
_VtVcPathThresholdIndex_Type = Integer32
_VtVcPathThresholdIndex_Object = MibTableColumn
vtVcPathThresholdIndex = _VtVcPathThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 54, 1, 1),
    _VtVcPathThresholdIndex_Type()
)
vtVcPathThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtVcPathThresholdIndex.setStatus("current")
_VtVcPathThresholdInterval_Type = CmPmIntervalType
_VtVcPathThresholdInterval_Object = MibTableColumn
vtVcPathThresholdInterval = _VtVcPathThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 54, 1, 2),
    _VtVcPathThresholdInterval_Type()
)
vtVcPathThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathThresholdInterval.setStatus("current")
_VtVcPathThresholdVariable_Type = VariablePointer
_VtVcPathThresholdVariable_Object = MibTableColumn
vtVcPathThresholdVariable = _VtVcPathThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 54, 1, 3),
    _VtVcPathThresholdVariable_Type()
)
vtVcPathThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathThresholdVariable.setStatus("current")
_VtVcPathThresholdValueLo_Type = Unsigned32
_VtVcPathThresholdValueLo_Object = MibTableColumn
vtVcPathThresholdValueLo = _VtVcPathThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 54, 1, 4),
    _VtVcPathThresholdValueLo_Type()
)
vtVcPathThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtVcPathThresholdValueLo.setStatus("current")
_VtVcPathThresholdValueHi_Type = Unsigned32
_VtVcPathThresholdValueHi_Object = MibTableColumn
vtVcPathThresholdValueHi = _VtVcPathThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 54, 1, 5),
    _VtVcPathThresholdValueHi_Type()
)
vtVcPathThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtVcPathThresholdValueHi.setStatus("current")
_VtVcPathThresholdMonValue_Type = Counter64
_VtVcPathThresholdMonValue_Object = MibTableColumn
vtVcPathThresholdMonValue = _VtVcPathThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 54, 1, 6),
    _VtVcPathThresholdMonValue_Type()
)
vtVcPathThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtVcPathThresholdMonValue.setStatus("current")
_E1t1StatsTable_Object = MibTable
e1t1StatsTable = _E1t1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55)
)
if mibBuilder.loadTexts:
    e1t1StatsTable.setStatus("current")
_E1t1StatsEntry_Object = MibTableRow
e1t1StatsEntry = _E1t1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1)
)
e1t1StatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "e1t1ParentIfIndex"),
    (0, "CM-FACILITY-MIB", "e1t1Index"),
    (0, "CM-PERFORMANCE-MIB", "e1t1StatsIndex"),
)
if mibBuilder.loadTexts:
    e1t1StatsEntry.setStatus("current")


class _E1t1StatsIndex_Type(Integer32):
    """Custom type e1t1StatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_E1t1StatsIndex_Type.__name__ = "Integer32"
_E1t1StatsIndex_Object = MibTableColumn
e1t1StatsIndex = _E1t1StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 1),
    _E1t1StatsIndex_Type()
)
e1t1StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1t1StatsIndex.setStatus("current")
_E1t1StatsIntervalType_Type = CmPmIntervalType
_E1t1StatsIntervalType_Object = MibTableColumn
e1t1StatsIntervalType = _E1t1StatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 2),
    _E1t1StatsIntervalType_Type()
)
e1t1StatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsIntervalType.setStatus("current")
_E1t1StatsValid_Type = TruthValue
_E1t1StatsValid_Object = MibTableColumn
e1t1StatsValid = _E1t1StatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 3),
    _E1t1StatsValid_Type()
)
e1t1StatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsValid.setStatus("current")
_E1t1StatsAction_Type = CmPmBinAction
_E1t1StatsAction_Object = MibTableColumn
e1t1StatsAction = _E1t1StatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 4),
    _E1t1StatsAction_Type()
)
e1t1StatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1t1StatsAction.setStatus("current")
_E1t1StatsLineCVs_Type = PerfCounter64
_E1t1StatsLineCVs_Object = MibTableColumn
e1t1StatsLineCVs = _E1t1StatsLineCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 5),
    _E1t1StatsLineCVs_Type()
)
e1t1StatsLineCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsLineCVs.setStatus("current")
_E1t1StatsLineESs_Type = PerfCounter64
_E1t1StatsLineESs_Object = MibTableColumn
e1t1StatsLineESs = _E1t1StatsLineESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 6),
    _E1t1StatsLineESs_Type()
)
e1t1StatsLineESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsLineESs.setStatus("current")
_E1t1StatsLineSESs_Type = PerfCounter64
_E1t1StatsLineSESs_Object = MibTableColumn
e1t1StatsLineSESs = _E1t1StatsLineSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 7),
    _E1t1StatsLineSESs_Type()
)
e1t1StatsLineSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsLineSESs.setStatus("current")
_E1t1StatsLineESsFarEnd_Type = PerfCounter64
_E1t1StatsLineESsFarEnd_Object = MibTableColumn
e1t1StatsLineESsFarEnd = _E1t1StatsLineESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 8),
    _E1t1StatsLineESsFarEnd_Type()
)
e1t1StatsLineESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsLineESsFarEnd.setStatus("current")
_E1t1StatsLineUASs_Type = PerfCounter64
_E1t1StatsLineUASs_Object = MibTableColumn
e1t1StatsLineUASs = _E1t1StatsLineUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 9),
    _E1t1StatsLineUASs_Type()
)
e1t1StatsLineUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsLineUASs.setStatus("current")
_E1t1StatsLineLOSSs_Type = PerfCounter64
_E1t1StatsLineLOSSs_Object = MibTableColumn
e1t1StatsLineLOSSs = _E1t1StatsLineLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 10),
    _E1t1StatsLineLOSSs_Type()
)
e1t1StatsLineLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsLineLOSSs.setStatus("current")
_E1t1StatsPathCVs_Type = PerfCounter64
_E1t1StatsPathCVs_Object = MibTableColumn
e1t1StatsPathCVs = _E1t1StatsPathCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 11),
    _E1t1StatsPathCVs_Type()
)
e1t1StatsPathCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathCVs.setStatus("current")
_E1t1StatsPathESs_Type = PerfCounter64
_E1t1StatsPathESs_Object = MibTableColumn
e1t1StatsPathESs = _E1t1StatsPathESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 12),
    _E1t1StatsPathESs_Type()
)
e1t1StatsPathESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathESs.setStatus("current")
_E1t1StatsPathSESs_Type = PerfCounter64
_E1t1StatsPathSESs_Object = MibTableColumn
e1t1StatsPathSESs = _E1t1StatsPathSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 13),
    _E1t1StatsPathSESs_Type()
)
e1t1StatsPathSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathSESs.setStatus("current")
_E1t1StatsPathUASs_Type = PerfCounter64
_E1t1StatsPathUASs_Object = MibTableColumn
e1t1StatsPathUASs = _E1t1StatsPathUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 14),
    _E1t1StatsPathUASs_Type()
)
e1t1StatsPathUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathUASs.setStatus("current")
_E1t1StatsPathCVsFarEnd_Type = PerfCounter64
_E1t1StatsPathCVsFarEnd_Object = MibTableColumn
e1t1StatsPathCVsFarEnd = _E1t1StatsPathCVsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 15),
    _E1t1StatsPathCVsFarEnd_Type()
)
e1t1StatsPathCVsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathCVsFarEnd.setStatus("current")
_E1t1StatsPathESsFarEnd_Type = PerfCounter64
_E1t1StatsPathESsFarEnd_Object = MibTableColumn
e1t1StatsPathESsFarEnd = _E1t1StatsPathESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 16),
    _E1t1StatsPathESsFarEnd_Type()
)
e1t1StatsPathESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathESsFarEnd.setStatus("current")
_E1t1StatsPathSESsFarEnd_Type = PerfCounter64
_E1t1StatsPathSESsFarEnd_Object = MibTableColumn
e1t1StatsPathSESsFarEnd = _E1t1StatsPathSESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 17),
    _E1t1StatsPathSESsFarEnd_Type()
)
e1t1StatsPathSESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathSESsFarEnd.setStatus("current")
_E1t1StatsPathSEFsFarEnd_Type = PerfCounter64
_E1t1StatsPathSEFsFarEnd_Object = MibTableColumn
e1t1StatsPathSEFsFarEnd = _E1t1StatsPathSEFsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 18),
    _E1t1StatsPathSEFsFarEnd_Type()
)
e1t1StatsPathSEFsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathSEFsFarEnd.setStatus("current")
_E1t1StatsPathUASsFarEnd_Type = PerfCounter64
_E1t1StatsPathUASsFarEnd_Object = MibTableColumn
e1t1StatsPathUASsFarEnd = _E1t1StatsPathUASsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 19),
    _E1t1StatsPathUASsFarEnd_Type()
)
e1t1StatsPathUASsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathUASsFarEnd.setStatus("current")
_E1t1StatsPathFCs_Type = PerfCounter64
_E1t1StatsPathFCs_Object = MibTableColumn
e1t1StatsPathFCs = _E1t1StatsPathFCs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 20),
    _E1t1StatsPathFCs_Type()
)
e1t1StatsPathFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathFCs.setStatus("current")
_E1t1StatsPathFCsFarEnd_Type = PerfCounter64
_E1t1StatsPathFCsFarEnd_Object = MibTableColumn
e1t1StatsPathFCsFarEnd = _E1t1StatsPathFCsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 21),
    _E1t1StatsPathFCsFarEnd_Type()
)
e1t1StatsPathFCsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathFCsFarEnd.setStatus("current")
_E1t1StatsPathAISs_Type = PerfCounter64
_E1t1StatsPathAISs_Object = MibTableColumn
e1t1StatsPathAISs = _E1t1StatsPathAISs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 22),
    _E1t1StatsPathAISs_Type()
)
e1t1StatsPathAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathAISs.setStatus("current")
_E1t1StatsPathSASs_Type = PerfCounter64
_E1t1StatsPathSASs_Object = MibTableColumn
e1t1StatsPathSASs = _E1t1StatsPathSASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 55, 1, 23),
    _E1t1StatsPathSASs_Type()
)
e1t1StatsPathSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1StatsPathSASs.setStatus("current")
_E1t1HistoryTable_Object = MibTable
e1t1HistoryTable = _E1t1HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56)
)
if mibBuilder.loadTexts:
    e1t1HistoryTable.setStatus("current")
_E1t1HistoryEntry_Object = MibTableRow
e1t1HistoryEntry = _E1t1HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1)
)
e1t1HistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "e1t1ParentIfIndex"),
    (0, "CM-FACILITY-MIB", "e1t1Index"),
    (0, "CM-PERFORMANCE-MIB", "e1t1StatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "e1t1HistoryIndex"),
)
if mibBuilder.loadTexts:
    e1t1HistoryEntry.setStatus("current")


class _E1t1HistoryIndex_Type(Integer32):
    """Custom type e1t1HistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_E1t1HistoryIndex_Type.__name__ = "Integer32"
_E1t1HistoryIndex_Object = MibTableColumn
e1t1HistoryIndex = _E1t1HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 1),
    _E1t1HistoryIndex_Type()
)
e1t1HistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1t1HistoryIndex.setStatus("current")
_E1t1HistoryTime_Type = DateAndTime
_E1t1HistoryTime_Object = MibTableColumn
e1t1HistoryTime = _E1t1HistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 2),
    _E1t1HistoryTime_Type()
)
e1t1HistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryTime.setStatus("current")
_E1t1HistoryValid_Type = TruthValue
_E1t1HistoryValid_Object = MibTableColumn
e1t1HistoryValid = _E1t1HistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 3),
    _E1t1HistoryValid_Type()
)
e1t1HistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryValid.setStatus("current")
_E1t1HistoryAction_Type = CmPmBinAction
_E1t1HistoryAction_Object = MibTableColumn
e1t1HistoryAction = _E1t1HistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 4),
    _E1t1HistoryAction_Type()
)
e1t1HistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1t1HistoryAction.setStatus("current")
_E1t1HistoryLineCVs_Type = PerfCounter64
_E1t1HistoryLineCVs_Object = MibTableColumn
e1t1HistoryLineCVs = _E1t1HistoryLineCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 5),
    _E1t1HistoryLineCVs_Type()
)
e1t1HistoryLineCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryLineCVs.setStatus("current")
_E1t1HistoryLineESs_Type = PerfCounter64
_E1t1HistoryLineESs_Object = MibTableColumn
e1t1HistoryLineESs = _E1t1HistoryLineESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 6),
    _E1t1HistoryLineESs_Type()
)
e1t1HistoryLineESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryLineESs.setStatus("current")
_E1t1HistoryLineSESs_Type = PerfCounter64
_E1t1HistoryLineSESs_Object = MibTableColumn
e1t1HistoryLineSESs = _E1t1HistoryLineSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 7),
    _E1t1HistoryLineSESs_Type()
)
e1t1HistoryLineSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryLineSESs.setStatus("current")
_E1t1HistoryLineESsFarEnd_Type = PerfCounter64
_E1t1HistoryLineESsFarEnd_Object = MibTableColumn
e1t1HistoryLineESsFarEnd = _E1t1HistoryLineESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 8),
    _E1t1HistoryLineESsFarEnd_Type()
)
e1t1HistoryLineESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryLineESsFarEnd.setStatus("current")
_E1t1HistoryLineUASs_Type = PerfCounter64
_E1t1HistoryLineUASs_Object = MibTableColumn
e1t1HistoryLineUASs = _E1t1HistoryLineUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 9),
    _E1t1HistoryLineUASs_Type()
)
e1t1HistoryLineUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryLineUASs.setStatus("current")
_E1t1HistoryLineLOSSs_Type = PerfCounter64
_E1t1HistoryLineLOSSs_Object = MibTableColumn
e1t1HistoryLineLOSSs = _E1t1HistoryLineLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 10),
    _E1t1HistoryLineLOSSs_Type()
)
e1t1HistoryLineLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryLineLOSSs.setStatus("current")
_E1t1HistoryPathCVs_Type = PerfCounter64
_E1t1HistoryPathCVs_Object = MibTableColumn
e1t1HistoryPathCVs = _E1t1HistoryPathCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 11),
    _E1t1HistoryPathCVs_Type()
)
e1t1HistoryPathCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathCVs.setStatus("current")
_E1t1HistoryPathESs_Type = PerfCounter64
_E1t1HistoryPathESs_Object = MibTableColumn
e1t1HistoryPathESs = _E1t1HistoryPathESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 12),
    _E1t1HistoryPathESs_Type()
)
e1t1HistoryPathESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathESs.setStatus("current")
_E1t1HistoryPathSESs_Type = PerfCounter64
_E1t1HistoryPathSESs_Object = MibTableColumn
e1t1HistoryPathSESs = _E1t1HistoryPathSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 13),
    _E1t1HistoryPathSESs_Type()
)
e1t1HistoryPathSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathSESs.setStatus("current")
_E1t1HistoryPathUASs_Type = PerfCounter64
_E1t1HistoryPathUASs_Object = MibTableColumn
e1t1HistoryPathUASs = _E1t1HistoryPathUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 14),
    _E1t1HistoryPathUASs_Type()
)
e1t1HistoryPathUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathUASs.setStatus("current")
_E1t1HistoryPathCVsFarEnd_Type = PerfCounter64
_E1t1HistoryPathCVsFarEnd_Object = MibTableColumn
e1t1HistoryPathCVsFarEnd = _E1t1HistoryPathCVsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 15),
    _E1t1HistoryPathCVsFarEnd_Type()
)
e1t1HistoryPathCVsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathCVsFarEnd.setStatus("current")
_E1t1HistoryPathESsFarEnd_Type = PerfCounter64
_E1t1HistoryPathESsFarEnd_Object = MibTableColumn
e1t1HistoryPathESsFarEnd = _E1t1HistoryPathESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 16),
    _E1t1HistoryPathESsFarEnd_Type()
)
e1t1HistoryPathESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathESsFarEnd.setStatus("current")
_E1t1HistoryPathSESsFarEnd_Type = PerfCounter64
_E1t1HistoryPathSESsFarEnd_Object = MibTableColumn
e1t1HistoryPathSESsFarEnd = _E1t1HistoryPathSESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 17),
    _E1t1HistoryPathSESsFarEnd_Type()
)
e1t1HistoryPathSESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathSESsFarEnd.setStatus("current")
_E1t1HistoryPathSEFsFarEnd_Type = PerfCounter64
_E1t1HistoryPathSEFsFarEnd_Object = MibTableColumn
e1t1HistoryPathSEFsFarEnd = _E1t1HistoryPathSEFsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 18),
    _E1t1HistoryPathSEFsFarEnd_Type()
)
e1t1HistoryPathSEFsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathSEFsFarEnd.setStatus("current")
_E1t1HistoryPathUASsFarEnd_Type = PerfCounter64
_E1t1HistoryPathUASsFarEnd_Object = MibTableColumn
e1t1HistoryPathUASsFarEnd = _E1t1HistoryPathUASsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 19),
    _E1t1HistoryPathUASsFarEnd_Type()
)
e1t1HistoryPathUASsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathUASsFarEnd.setStatus("current")
_E1t1HistoryPathFCs_Type = PerfCounter64
_E1t1HistoryPathFCs_Object = MibTableColumn
e1t1HistoryPathFCs = _E1t1HistoryPathFCs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 20),
    _E1t1HistoryPathFCs_Type()
)
e1t1HistoryPathFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathFCs.setStatus("current")
_E1t1HistoryPathFCsFarEnd_Type = PerfCounter64
_E1t1HistoryPathFCsFarEnd_Object = MibTableColumn
e1t1HistoryPathFCsFarEnd = _E1t1HistoryPathFCsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 21),
    _E1t1HistoryPathFCsFarEnd_Type()
)
e1t1HistoryPathFCsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathFCsFarEnd.setStatus("current")
_E1t1HistoryPathAISs_Type = PerfCounter64
_E1t1HistoryPathAISs_Object = MibTableColumn
e1t1HistoryPathAISs = _E1t1HistoryPathAISs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 22),
    _E1t1HistoryPathAISs_Type()
)
e1t1HistoryPathAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathAISs.setStatus("current")
_E1t1HistoryPathSASs_Type = PerfCounter64
_E1t1HistoryPathSASs_Object = MibTableColumn
e1t1HistoryPathSASs = _E1t1HistoryPathSASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 56, 1, 23),
    _E1t1HistoryPathSASs_Type()
)
e1t1HistoryPathSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1HistoryPathSASs.setStatus("current")
_E1t1ThresholdTable_Object = MibTable
e1t1ThresholdTable = _E1t1ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 57)
)
if mibBuilder.loadTexts:
    e1t1ThresholdTable.setStatus("current")
_E1t1ThresholdEntry_Object = MibTableRow
e1t1ThresholdEntry = _E1t1ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 57, 1)
)
e1t1ThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "e1t1ParentIfIndex"),
    (0, "CM-FACILITY-MIB", "e1t1Index"),
    (0, "CM-PERFORMANCE-MIB", "e1t1StatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "e1t1ThresholdIndex"),
)
if mibBuilder.loadTexts:
    e1t1ThresholdEntry.setStatus("current")


class _E1t1ThresholdIndex_Type(Integer32):
    """Custom type e1t1ThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_E1t1ThresholdIndex_Type.__name__ = "Integer32"
_E1t1ThresholdIndex_Object = MibTableColumn
e1t1ThresholdIndex = _E1t1ThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 57, 1, 1),
    _E1t1ThresholdIndex_Type()
)
e1t1ThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e1t1ThresholdIndex.setStatus("current")
_E1t1ThresholdInterval_Type = CmPmIntervalType
_E1t1ThresholdInterval_Object = MibTableColumn
e1t1ThresholdInterval = _E1t1ThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 57, 1, 2),
    _E1t1ThresholdInterval_Type()
)
e1t1ThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1ThresholdInterval.setStatus("current")
_E1t1ThresholdVariable_Type = VariablePointer
_E1t1ThresholdVariable_Object = MibTableColumn
e1t1ThresholdVariable = _E1t1ThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 57, 1, 3),
    _E1t1ThresholdVariable_Type()
)
e1t1ThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1ThresholdVariable.setStatus("current")
_E1t1ThresholdValueLo_Type = Unsigned32
_E1t1ThresholdValueLo_Object = MibTableColumn
e1t1ThresholdValueLo = _E1t1ThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 57, 1, 4),
    _E1t1ThresholdValueLo_Type()
)
e1t1ThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1t1ThresholdValueLo.setStatus("current")
_E1t1ThresholdValueHi_Type = Unsigned32
_E1t1ThresholdValueHi_Object = MibTableColumn
e1t1ThresholdValueHi = _E1t1ThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 57, 1, 5),
    _E1t1ThresholdValueHi_Type()
)
e1t1ThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e1t1ThresholdValueHi.setStatus("current")
_E1t1ThresholdMonValue_Type = Counter64
_E1t1ThresholdMonValue_Object = MibTableColumn
e1t1ThresholdMonValue = _E1t1ThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 57, 1, 6),
    _E1t1ThresholdMonValue_Type()
)
e1t1ThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e1t1ThresholdMonValue.setStatus("current")
_E3t3StatsTable_Object = MibTable
e3t3StatsTable = _E3t3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58)
)
if mibBuilder.loadTexts:
    e3t3StatsTable.setStatus("current")
_E3t3StatsEntry_Object = MibTableRow
e3t3StatsEntry = _E3t3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1)
)
e3t3StatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "e3t3ParentIfIndex"),
    (0, "CM-FACILITY-MIB", "e3t3Index"),
    (0, "CM-PERFORMANCE-MIB", "e3t3StatsIndex"),
)
if mibBuilder.loadTexts:
    e3t3StatsEntry.setStatus("current")


class _E3t3StatsIndex_Type(Integer32):
    """Custom type e3t3StatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_E3t3StatsIndex_Type.__name__ = "Integer32"
_E3t3StatsIndex_Object = MibTableColumn
e3t3StatsIndex = _E3t3StatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 1),
    _E3t3StatsIndex_Type()
)
e3t3StatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e3t3StatsIndex.setStatus("current")
_E3t3StatsIntervalType_Type = CmPmIntervalType
_E3t3StatsIntervalType_Object = MibTableColumn
e3t3StatsIntervalType = _E3t3StatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 2),
    _E3t3StatsIntervalType_Type()
)
e3t3StatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsIntervalType.setStatus("current")
_E3t3StatsValid_Type = TruthValue
_E3t3StatsValid_Object = MibTableColumn
e3t3StatsValid = _E3t3StatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 3),
    _E3t3StatsValid_Type()
)
e3t3StatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsValid.setStatus("current")
_E3t3StatsAction_Type = CmPmBinAction
_E3t3StatsAction_Object = MibTableColumn
e3t3StatsAction = _E3t3StatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 4),
    _E3t3StatsAction_Type()
)
e3t3StatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3t3StatsAction.setStatus("current")
_E3t3StatsLineCVs_Type = PerfCounter64
_E3t3StatsLineCVs_Object = MibTableColumn
e3t3StatsLineCVs = _E3t3StatsLineCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 5),
    _E3t3StatsLineCVs_Type()
)
e3t3StatsLineCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsLineCVs.setStatus("current")
_E3t3StatsLineESs_Type = PerfCounter64
_E3t3StatsLineESs_Object = MibTableColumn
e3t3StatsLineESs = _E3t3StatsLineESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 6),
    _E3t3StatsLineESs_Type()
)
e3t3StatsLineESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsLineESs.setStatus("current")
_E3t3StatsLineSESs_Type = PerfCounter64
_E3t3StatsLineSESs_Object = MibTableColumn
e3t3StatsLineSESs = _E3t3StatsLineSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 7),
    _E3t3StatsLineSESs_Type()
)
e3t3StatsLineSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsLineSESs.setStatus("current")
_E3t3StatsLineLOSSs_Type = PerfCounter64
_E3t3StatsLineLOSSs_Object = MibTableColumn
e3t3StatsLineLOSSs = _E3t3StatsLineLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 8),
    _E3t3StatsLineLOSSs_Type()
)
e3t3StatsLineLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsLineLOSSs.setStatus("current")
_E3t3StatsPathPCVs_Type = PerfCounter64
_E3t3StatsPathPCVs_Object = MibTableColumn
e3t3StatsPathPCVs = _E3t3StatsPathPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 9),
    _E3t3StatsPathPCVs_Type()
)
e3t3StatsPathPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathPCVs.setStatus("current")
_E3t3StatsPathCCVs_Type = PerfCounter64
_E3t3StatsPathCCVs_Object = MibTableColumn
e3t3StatsPathCCVs = _E3t3StatsPathCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 10),
    _E3t3StatsPathCCVs_Type()
)
e3t3StatsPathCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCCVs.setStatus("current")
_E3t3StatsPathAISs_Type = PerfCounter64
_E3t3StatsPathAISs_Object = MibTableColumn
e3t3StatsPathAISs = _E3t3StatsPathAISs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 11),
    _E3t3StatsPathAISs_Type()
)
e3t3StatsPathAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathAISs.setStatus("current")
_E3t3StatsPathPESs_Type = PerfCounter64
_E3t3StatsPathPESs_Object = MibTableColumn
e3t3StatsPathPESs = _E3t3StatsPathPESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 12),
    _E3t3StatsPathPESs_Type()
)
e3t3StatsPathPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathPESs.setStatus("current")
_E3t3StatsPathCESs_Type = PerfCounter64
_E3t3StatsPathCESs_Object = MibTableColumn
e3t3StatsPathCESs = _E3t3StatsPathCESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 13),
    _E3t3StatsPathCESs_Type()
)
e3t3StatsPathCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCESs.setStatus("current")
_E3t3StatsPathFCs_Type = PerfCounter64
_E3t3StatsPathFCs_Object = MibTableColumn
e3t3StatsPathFCs = _E3t3StatsPathFCs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 14),
    _E3t3StatsPathFCs_Type()
)
e3t3StatsPathFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathFCs.setStatus("current")
_E3t3StatsPathSEFs_Type = PerfCounter64
_E3t3StatsPathSEFs_Object = MibTableColumn
e3t3StatsPathSEFs = _E3t3StatsPathSEFs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 15),
    _E3t3StatsPathSEFs_Type()
)
e3t3StatsPathSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathSEFs.setStatus("current")
_E3t3StatsPathPSESs_Type = PerfCounter64
_E3t3StatsPathPSESs_Object = MibTableColumn
e3t3StatsPathPSESs = _E3t3StatsPathPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 16),
    _E3t3StatsPathPSESs_Type()
)
e3t3StatsPathPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathPSESs.setStatus("current")
_E3t3StatsPathCSESs_Type = PerfCounter64
_E3t3StatsPathCSESs_Object = MibTableColumn
e3t3StatsPathCSESs = _E3t3StatsPathCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 17),
    _E3t3StatsPathCSESs_Type()
)
e3t3StatsPathCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCSESs.setStatus("current")
_E3t3StatsPathPUASs_Type = PerfCounter64
_E3t3StatsPathPUASs_Object = MibTableColumn
e3t3StatsPathPUASs = _E3t3StatsPathPUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 18),
    _E3t3StatsPathPUASs_Type()
)
e3t3StatsPathPUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathPUASs.setStatus("current")
_E3t3StatsPathCUASs_Type = PerfCounter64
_E3t3StatsPathCUASs_Object = MibTableColumn
e3t3StatsPathCUASs = _E3t3StatsPathCUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 19),
    _E3t3StatsPathCUASs_Type()
)
e3t3StatsPathCUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCUASs.setStatus("current")
_E3t3StatsPathCCVsFarEnd_Type = PerfCounter64
_E3t3StatsPathCCVsFarEnd_Object = MibTableColumn
e3t3StatsPathCCVsFarEnd = _E3t3StatsPathCCVsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 20),
    _E3t3StatsPathCCVsFarEnd_Type()
)
e3t3StatsPathCCVsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCCVsFarEnd.setStatus("current")
_E3t3StatsPathCESsFarEnd_Type = PerfCounter64
_E3t3StatsPathCESsFarEnd_Object = MibTableColumn
e3t3StatsPathCESsFarEnd = _E3t3StatsPathCESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 21),
    _E3t3StatsPathCESsFarEnd_Type()
)
e3t3StatsPathCESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCESsFarEnd.setStatus("current")
_E3t3StatsPathCSESsFarEnd_Type = PerfCounter64
_E3t3StatsPathCSESsFarEnd_Object = MibTableColumn
e3t3StatsPathCSESsFarEnd = _E3t3StatsPathCSESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 22),
    _E3t3StatsPathCSESsFarEnd_Type()
)
e3t3StatsPathCSESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCSESsFarEnd.setStatus("current")
_E3t3StatsPathCFCsFarEnd_Type = PerfCounter64
_E3t3StatsPathCFCsFarEnd_Object = MibTableColumn
e3t3StatsPathCFCsFarEnd = _E3t3StatsPathCFCsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 23),
    _E3t3StatsPathCFCsFarEnd_Type()
)
e3t3StatsPathCFCsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCFCsFarEnd.setStatus("current")
_E3t3StatsPathCUASsFarEnd_Type = PerfCounter64
_E3t3StatsPathCUASsFarEnd_Object = MibTableColumn
e3t3StatsPathCUASsFarEnd = _E3t3StatsPathCUASsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 58, 1, 24),
    _E3t3StatsPathCUASsFarEnd_Type()
)
e3t3StatsPathCUASsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3StatsPathCUASsFarEnd.setStatus("current")
_E3t3HistoryTable_Object = MibTable
e3t3HistoryTable = _E3t3HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59)
)
if mibBuilder.loadTexts:
    e3t3HistoryTable.setStatus("current")
_E3t3HistoryEntry_Object = MibTableRow
e3t3HistoryEntry = _E3t3HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1)
)
e3t3HistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "e3t3ParentIfIndex"),
    (0, "CM-FACILITY-MIB", "e3t3Index"),
    (0, "CM-PERFORMANCE-MIB", "e3t3StatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "e3t3HistoryIndex"),
)
if mibBuilder.loadTexts:
    e3t3HistoryEntry.setStatus("current")


class _E3t3HistoryIndex_Type(Integer32):
    """Custom type e3t3HistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_E3t3HistoryIndex_Type.__name__ = "Integer32"
_E3t3HistoryIndex_Object = MibTableColumn
e3t3HistoryIndex = _E3t3HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 1),
    _E3t3HistoryIndex_Type()
)
e3t3HistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e3t3HistoryIndex.setStatus("current")
_E3t3HistoryTime_Type = DateAndTime
_E3t3HistoryTime_Object = MibTableColumn
e3t3HistoryTime = _E3t3HistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 2),
    _E3t3HistoryTime_Type()
)
e3t3HistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryTime.setStatus("current")
_E3t3HistoryValid_Type = TruthValue
_E3t3HistoryValid_Object = MibTableColumn
e3t3HistoryValid = _E3t3HistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 3),
    _E3t3HistoryValid_Type()
)
e3t3HistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryValid.setStatus("current")
_E3t3HistoryAction_Type = CmPmBinAction
_E3t3HistoryAction_Object = MibTableColumn
e3t3HistoryAction = _E3t3HistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 4),
    _E3t3HistoryAction_Type()
)
e3t3HistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3t3HistoryAction.setStatus("current")
_E3t3HistoryLineCVs_Type = PerfCounter64
_E3t3HistoryLineCVs_Object = MibTableColumn
e3t3HistoryLineCVs = _E3t3HistoryLineCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 5),
    _E3t3HistoryLineCVs_Type()
)
e3t3HistoryLineCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryLineCVs.setStatus("current")
_E3t3HistoryLineESs_Type = PerfCounter64
_E3t3HistoryLineESs_Object = MibTableColumn
e3t3HistoryLineESs = _E3t3HistoryLineESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 6),
    _E3t3HistoryLineESs_Type()
)
e3t3HistoryLineESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryLineESs.setStatus("current")
_E3t3HistoryLineSESs_Type = PerfCounter64
_E3t3HistoryLineSESs_Object = MibTableColumn
e3t3HistoryLineSESs = _E3t3HistoryLineSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 7),
    _E3t3HistoryLineSESs_Type()
)
e3t3HistoryLineSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryLineSESs.setStatus("current")
_E3t3HistoryLineLOSSs_Type = PerfCounter64
_E3t3HistoryLineLOSSs_Object = MibTableColumn
e3t3HistoryLineLOSSs = _E3t3HistoryLineLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 8),
    _E3t3HistoryLineLOSSs_Type()
)
e3t3HistoryLineLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryLineLOSSs.setStatus("current")
_E3t3HistoryPathPCVs_Type = PerfCounter64
_E3t3HistoryPathPCVs_Object = MibTableColumn
e3t3HistoryPathPCVs = _E3t3HistoryPathPCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 9),
    _E3t3HistoryPathPCVs_Type()
)
e3t3HistoryPathPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathPCVs.setStatus("current")
_E3t3HistoryPathCCVs_Type = PerfCounter64
_E3t3HistoryPathCCVs_Object = MibTableColumn
e3t3HistoryPathCCVs = _E3t3HistoryPathCCVs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 10),
    _E3t3HistoryPathCCVs_Type()
)
e3t3HistoryPathCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCCVs.setStatus("current")
_E3t3HistoryPathAISs_Type = PerfCounter64
_E3t3HistoryPathAISs_Object = MibTableColumn
e3t3HistoryPathAISs = _E3t3HistoryPathAISs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 11),
    _E3t3HistoryPathAISs_Type()
)
e3t3HistoryPathAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathAISs.setStatus("current")
_E3t3HistoryPathPESs_Type = PerfCounter64
_E3t3HistoryPathPESs_Object = MibTableColumn
e3t3HistoryPathPESs = _E3t3HistoryPathPESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 12),
    _E3t3HistoryPathPESs_Type()
)
e3t3HistoryPathPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathPESs.setStatus("current")
_E3t3HistoryPathCESs_Type = PerfCounter64
_E3t3HistoryPathCESs_Object = MibTableColumn
e3t3HistoryPathCESs = _E3t3HistoryPathCESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 13),
    _E3t3HistoryPathCESs_Type()
)
e3t3HistoryPathCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCESs.setStatus("current")
_E3t3HistoryPathFCs_Type = PerfCounter64
_E3t3HistoryPathFCs_Object = MibTableColumn
e3t3HistoryPathFCs = _E3t3HistoryPathFCs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 14),
    _E3t3HistoryPathFCs_Type()
)
e3t3HistoryPathFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathFCs.setStatus("current")
_E3t3HistoryPathSEFs_Type = PerfCounter64
_E3t3HistoryPathSEFs_Object = MibTableColumn
e3t3HistoryPathSEFs = _E3t3HistoryPathSEFs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 15),
    _E3t3HistoryPathSEFs_Type()
)
e3t3HistoryPathSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathSEFs.setStatus("current")
_E3t3HistoryPathPSESs_Type = PerfCounter64
_E3t3HistoryPathPSESs_Object = MibTableColumn
e3t3HistoryPathPSESs = _E3t3HistoryPathPSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 16),
    _E3t3HistoryPathPSESs_Type()
)
e3t3HistoryPathPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathPSESs.setStatus("current")
_E3t3HistoryPathCSESs_Type = PerfCounter64
_E3t3HistoryPathCSESs_Object = MibTableColumn
e3t3HistoryPathCSESs = _E3t3HistoryPathCSESs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 17),
    _E3t3HistoryPathCSESs_Type()
)
e3t3HistoryPathCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCSESs.setStatus("current")
_E3t3HistoryPathPUASs_Type = PerfCounter64
_E3t3HistoryPathPUASs_Object = MibTableColumn
e3t3HistoryPathPUASs = _E3t3HistoryPathPUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 18),
    _E3t3HistoryPathPUASs_Type()
)
e3t3HistoryPathPUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathPUASs.setStatus("current")
_E3t3HistoryPathCUASs_Type = PerfCounter64
_E3t3HistoryPathCUASs_Object = MibTableColumn
e3t3HistoryPathCUASs = _E3t3HistoryPathCUASs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 19),
    _E3t3HistoryPathCUASs_Type()
)
e3t3HistoryPathCUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCUASs.setStatus("current")
_E3t3HistoryPathCCVsFarEnd_Type = PerfCounter64
_E3t3HistoryPathCCVsFarEnd_Object = MibTableColumn
e3t3HistoryPathCCVsFarEnd = _E3t3HistoryPathCCVsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 20),
    _E3t3HistoryPathCCVsFarEnd_Type()
)
e3t3HistoryPathCCVsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCCVsFarEnd.setStatus("current")
_E3t3HistoryPathCESsFarEnd_Type = PerfCounter64
_E3t3HistoryPathCESsFarEnd_Object = MibTableColumn
e3t3HistoryPathCESsFarEnd = _E3t3HistoryPathCESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 21),
    _E3t3HistoryPathCESsFarEnd_Type()
)
e3t3HistoryPathCESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCESsFarEnd.setStatus("current")
_E3t3HistoryPathCSESsFarEnd_Type = PerfCounter64
_E3t3HistoryPathCSESsFarEnd_Object = MibTableColumn
e3t3HistoryPathCSESsFarEnd = _E3t3HistoryPathCSESsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 22),
    _E3t3HistoryPathCSESsFarEnd_Type()
)
e3t3HistoryPathCSESsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCSESsFarEnd.setStatus("current")
_E3t3HistoryPathCFCsFarEnd_Type = PerfCounter64
_E3t3HistoryPathCFCsFarEnd_Object = MibTableColumn
e3t3HistoryPathCFCsFarEnd = _E3t3HistoryPathCFCsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 23),
    _E3t3HistoryPathCFCsFarEnd_Type()
)
e3t3HistoryPathCFCsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCFCsFarEnd.setStatus("current")
_E3t3HistoryPathCUASsFarEnd_Type = PerfCounter64
_E3t3HistoryPathCUASsFarEnd_Object = MibTableColumn
e3t3HistoryPathCUASsFarEnd = _E3t3HistoryPathCUASsFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 59, 1, 24),
    _E3t3HistoryPathCUASsFarEnd_Type()
)
e3t3HistoryPathCUASsFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3HistoryPathCUASsFarEnd.setStatus("current")
_E3t3ThresholdTable_Object = MibTable
e3t3ThresholdTable = _E3t3ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 60)
)
if mibBuilder.loadTexts:
    e3t3ThresholdTable.setStatus("current")
_E3t3ThresholdEntry_Object = MibTableRow
e3t3ThresholdEntry = _E3t3ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 60, 1)
)
e3t3ThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "e3t3ParentIfIndex"),
    (0, "CM-FACILITY-MIB", "e3t3Index"),
    (0, "CM-PERFORMANCE-MIB", "e3t3StatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "e3t3ThresholdIndex"),
)
if mibBuilder.loadTexts:
    e3t3ThresholdEntry.setStatus("current")


class _E3t3ThresholdIndex_Type(Integer32):
    """Custom type e3t3ThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_E3t3ThresholdIndex_Type.__name__ = "Integer32"
_E3t3ThresholdIndex_Object = MibTableColumn
e3t3ThresholdIndex = _E3t3ThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 60, 1, 1),
    _E3t3ThresholdIndex_Type()
)
e3t3ThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    e3t3ThresholdIndex.setStatus("current")
_E3t3ThresholdInterval_Type = CmPmIntervalType
_E3t3ThresholdInterval_Object = MibTableColumn
e3t3ThresholdInterval = _E3t3ThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 60, 1, 2),
    _E3t3ThresholdInterval_Type()
)
e3t3ThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3ThresholdInterval.setStatus("current")
_E3t3ThresholdVariable_Type = VariablePointer
_E3t3ThresholdVariable_Object = MibTableColumn
e3t3ThresholdVariable = _E3t3ThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 60, 1, 3),
    _E3t3ThresholdVariable_Type()
)
e3t3ThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3ThresholdVariable.setStatus("current")
_E3t3ThresholdValueLo_Type = Unsigned32
_E3t3ThresholdValueLo_Object = MibTableColumn
e3t3ThresholdValueLo = _E3t3ThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 60, 1, 4),
    _E3t3ThresholdValueLo_Type()
)
e3t3ThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3t3ThresholdValueLo.setStatus("current")
_E3t3ThresholdValueHi_Type = Unsigned32
_E3t3ThresholdValueHi_Object = MibTableColumn
e3t3ThresholdValueHi = _E3t3ThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 60, 1, 5),
    _E3t3ThresholdValueHi_Type()
)
e3t3ThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    e3t3ThresholdValueHi.setStatus("current")
_E3t3ThresholdMonValue_Type = Counter64
_E3t3ThresholdMonValue_Object = MibTableColumn
e3t3ThresholdMonValue = _E3t3ThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 60, 1, 6),
    _E3t3ThresholdMonValue_Type()
)
e3t3ThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3t3ThresholdMonValue.setStatus("current")
_CmFlowBWExtTable_Object = MibTable
cmFlowBWExtTable = _CmFlowBWExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 61)
)
if mibBuilder.loadTexts:
    cmFlowBWExtTable.setStatus("current")
_CmFlowBWExtEntry_Object = MibTableRow
cmFlowBWExtEntry = _CmFlowBWExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 61, 1)
)
if mibBuilder.loadTexts:
    cmFlowBWExtEntry.setStatus("current")
_CmFlowBWA2NCIR_Type = CounterBasedGauge64
_CmFlowBWA2NCIR_Object = MibTableColumn
cmFlowBWA2NCIR = _CmFlowBWA2NCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 61, 1, 1),
    _CmFlowBWA2NCIR_Type()
)
cmFlowBWA2NCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowBWA2NCIR.setStatus("current")
_CmFlowBWA2NEIR_Type = CounterBasedGauge64
_CmFlowBWA2NEIR_Object = MibTableColumn
cmFlowBWA2NEIR = _CmFlowBWA2NEIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 61, 1, 2),
    _CmFlowBWA2NEIR_Type()
)
cmFlowBWA2NEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowBWA2NEIR.setStatus("current")
_CmFlowBWN2ACIR_Type = CounterBasedGauge64
_CmFlowBWN2ACIR_Object = MibTableColumn
cmFlowBWN2ACIR = _CmFlowBWN2ACIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 61, 1, 3),
    _CmFlowBWN2ACIR_Type()
)
cmFlowBWN2ACIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowBWN2ACIR.setStatus("current")
_CmFlowBWN2AEIR_Type = CounterBasedGauge64
_CmFlowBWN2AEIR_Object = MibTableColumn
cmFlowBWN2AEIR = _CmFlowBWN2AEIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 61, 1, 4),
    _CmFlowBWN2AEIR_Type()
)
cmFlowBWN2AEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowBWN2AEIR.setStatus("current")
_CmFlowBWA2NGFB_Type = CounterBasedGauge64
_CmFlowBWA2NGFB_Object = MibTableColumn
cmFlowBWA2NGFB = _CmFlowBWA2NGFB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 61, 1, 5),
    _CmFlowBWA2NGFB_Type()
)
cmFlowBWA2NGFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowBWA2NGFB.setStatus("current")
_CmFlowBWA2NMFB_Type = CounterBasedGauge64
_CmFlowBWA2NMFB_Object = MibTableColumn
cmFlowBWA2NMFB = _CmFlowBWA2NMFB_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 61, 1, 6),
    _CmFlowBWA2NMFB_Type()
)
cmFlowBWA2NMFB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFlowBWA2NMFB.setStatus("current")
_OcnStmThresholdVarTable_Object = MibTable
ocnStmThresholdVarTable = _OcnStmThresholdVarTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 62)
)
if mibBuilder.loadTexts:
    ocnStmThresholdVarTable.setStatus("current")
_OcnStmThresholdVarEntry_Object = MibTableRow
ocnStmThresholdVarEntry = _OcnStmThresholdVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 62, 1)
)
ocnStmThresholdVarEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "ocnStmIndex"),
    (0, "CM-PERFORMANCE-MIB", "ocnStmStatsIndex"),
)
if mibBuilder.loadTexts:
    ocnStmThresholdVarEntry.setStatus("current")
_OcnStmThresholdVarOprVariance_Type = Integer32
_OcnStmThresholdVarOprVariance_Object = MibTableColumn
ocnStmThresholdVarOprVariance = _OcnStmThresholdVarOprVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 62, 1, 1),
    _OcnStmThresholdVarOprVariance_Type()
)
ocnStmThresholdVarOprVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnStmThresholdVarOprVariance.setStatus("current")
_OcnStmThresholdVarOptVariance_Type = Integer32
_OcnStmThresholdVarOptVariance_Object = MibTableColumn
ocnStmThresholdVarOptVariance = _OcnStmThresholdVarOptVariance_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 62, 1, 2),
    _OcnStmThresholdVarOptVariance_Type()
)
ocnStmThresholdVarOptVariance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ocnStmThresholdVarOptVariance.setStatus("current")
_CmPerfScalarObjects_ObjectIdentity = ObjectIdentity
cmPerfScalarObjects = _CmPerfScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 63)
)
_CmPerQueryGenControl_Type = TruthValue
_CmPerQueryGenControl_Object = MibScalar
cmPerQueryGenControl = _CmPerQueryGenControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 63, 1),
    _CmPerQueryGenControl_Type()
)
cmPerQueryGenControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPerQueryGenControl.setStatus("current")
_F3FpQosShaperStatsTable_Object = MibTable
f3FpQosShaperStatsTable = _F3FpQosShaperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64)
)
if mibBuilder.loadTexts:
    f3FpQosShaperStatsTable.setStatus("current")
_F3FpQosShaperStatsEntry_Object = MibTableRow
f3FpQosShaperStatsEntry = _F3FpQosShaperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1)
)
f3FpQosShaperStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3FpQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosShaperStatsIndex"),
)
if mibBuilder.loadTexts:
    f3FpQosShaperStatsEntry.setStatus("current")


class _F3FpQosShaperStatsIndex_Type(Integer32):
    """Custom type f3FpQosShaperStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3FpQosShaperStatsIndex_Type.__name__ = "Integer32"
_F3FpQosShaperStatsIndex_Object = MibTableColumn
f3FpQosShaperStatsIndex = _F3FpQosShaperStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 1),
    _F3FpQosShaperStatsIndex_Type()
)
f3FpQosShaperStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsIndex.setStatus("current")
_F3FpQosShaperStatsIntervalType_Type = CmPmIntervalType
_F3FpQosShaperStatsIntervalType_Object = MibTableColumn
f3FpQosShaperStatsIntervalType = _F3FpQosShaperStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 2),
    _F3FpQosShaperStatsIntervalType_Type()
)
f3FpQosShaperStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsIntervalType.setStatus("current")
_F3FpQosShaperStatsValid_Type = TruthValue
_F3FpQosShaperStatsValid_Object = MibTableColumn
f3FpQosShaperStatsValid = _F3FpQosShaperStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 3),
    _F3FpQosShaperStatsValid_Type()
)
f3FpQosShaperStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsValid.setStatus("current")
_F3FpQosShaperStatsAction_Type = CmPmBinAction
_F3FpQosShaperStatsAction_Object = MibTableColumn
f3FpQosShaperStatsAction = _F3FpQosShaperStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 4),
    _F3FpQosShaperStatsAction_Type()
)
f3FpQosShaperStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsAction.setStatus("current")
_F3FpQosShaperStatsBT_Type = PerfCounter64
_F3FpQosShaperStatsBT_Object = MibTableColumn
f3FpQosShaperStatsBT = _F3FpQosShaperStatsBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 5),
    _F3FpQosShaperStatsBT_Type()
)
f3FpQosShaperStatsBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsBT.setStatus("current")
_F3FpQosShaperStatsBTD_Type = PerfCounter64
_F3FpQosShaperStatsBTD_Object = MibTableColumn
f3FpQosShaperStatsBTD = _F3FpQosShaperStatsBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 6),
    _F3FpQosShaperStatsBTD_Type()
)
f3FpQosShaperStatsBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsBTD.setStatus("current")
_F3FpQosShaperStatsFD_Type = PerfCounter64
_F3FpQosShaperStatsFD_Object = MibTableColumn
f3FpQosShaperStatsFD = _F3FpQosShaperStatsFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 7),
    _F3FpQosShaperStatsFD_Type()
)
f3FpQosShaperStatsFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsFD.setStatus("current")
_F3FpQosShaperStatsFTD_Type = PerfCounter64
_F3FpQosShaperStatsFTD_Object = MibTableColumn
f3FpQosShaperStatsFTD = _F3FpQosShaperStatsFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 8),
    _F3FpQosShaperStatsFTD_Type()
)
f3FpQosShaperStatsFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsFTD.setStatus("current")
_F3FpQosShaperStatsABRRL_Type = PerfCounter64
_F3FpQosShaperStatsABRRL_Object = MibTableColumn
f3FpQosShaperStatsABRRL = _F3FpQosShaperStatsABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 9),
    _F3FpQosShaperStatsABRRL_Type()
)
f3FpQosShaperStatsABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsABRRL.setStatus("current")
_F3FpQosShaperStatsBREDD_Type = PerfCounter64
_F3FpQosShaperStatsBREDD_Object = MibTableColumn
f3FpQosShaperStatsBREDD = _F3FpQosShaperStatsBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 10),
    _F3FpQosShaperStatsBREDD_Type()
)
f3FpQosShaperStatsBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsBREDD.setStatus("current")
_F3FpQosShaperStatsFREDD_Type = PerfCounter64
_F3FpQosShaperStatsFREDD_Object = MibTableColumn
f3FpQosShaperStatsFREDD = _F3FpQosShaperStatsFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 64, 1, 11),
    _F3FpQosShaperStatsFREDD_Type()
)
f3FpQosShaperStatsFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperStatsFREDD.setStatus("current")
_F3FpQosShaperHistoryTable_Object = MibTable
f3FpQosShaperHistoryTable = _F3FpQosShaperHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65)
)
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryTable.setStatus("current")
_F3FpQosShaperHistoryEntry_Object = MibTableRow
f3FpQosShaperHistoryEntry = _F3FpQosShaperHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1)
)
f3FpQosShaperHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3FpQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryEntry.setStatus("current")


class _F3FpQosShaperHistoryIndex_Type(Integer32):
    """Custom type f3FpQosShaperHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3FpQosShaperHistoryIndex_Type.__name__ = "Integer32"
_F3FpQosShaperHistoryIndex_Object = MibTableColumn
f3FpQosShaperHistoryIndex = _F3FpQosShaperHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 1),
    _F3FpQosShaperHistoryIndex_Type()
)
f3FpQosShaperHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryIndex.setStatus("current")
_F3FpQosShaperHistoryTime_Type = DateAndTime
_F3FpQosShaperHistoryTime_Object = MibTableColumn
f3FpQosShaperHistoryTime = _F3FpQosShaperHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 2),
    _F3FpQosShaperHistoryTime_Type()
)
f3FpQosShaperHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryTime.setStatus("current")
_F3FpQosShaperHistoryValid_Type = TruthValue
_F3FpQosShaperHistoryValid_Object = MibTableColumn
f3FpQosShaperHistoryValid = _F3FpQosShaperHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 3),
    _F3FpQosShaperHistoryValid_Type()
)
f3FpQosShaperHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryValid.setStatus("current")
_F3FpQosShaperHistoryAction_Type = CmPmBinAction
_F3FpQosShaperHistoryAction_Object = MibTableColumn
f3FpQosShaperHistoryAction = _F3FpQosShaperHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 4),
    _F3FpQosShaperHistoryAction_Type()
)
f3FpQosShaperHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryAction.setStatus("current")
_F3FpQosShaperHistoryBT_Type = PerfCounter64
_F3FpQosShaperHistoryBT_Object = MibTableColumn
f3FpQosShaperHistoryBT = _F3FpQosShaperHistoryBT_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 5),
    _F3FpQosShaperHistoryBT_Type()
)
f3FpQosShaperHistoryBT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryBT.setStatus("current")
_F3FpQosShaperHistoryBTD_Type = PerfCounter64
_F3FpQosShaperHistoryBTD_Object = MibTableColumn
f3FpQosShaperHistoryBTD = _F3FpQosShaperHistoryBTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 6),
    _F3FpQosShaperHistoryBTD_Type()
)
f3FpQosShaperHistoryBTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryBTD.setStatus("current")
_F3FpQosShaperHistoryFD_Type = PerfCounter64
_F3FpQosShaperHistoryFD_Object = MibTableColumn
f3FpQosShaperHistoryFD = _F3FpQosShaperHistoryFD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 7),
    _F3FpQosShaperHistoryFD_Type()
)
f3FpQosShaperHistoryFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryFD.setStatus("current")
_F3FpQosShaperHistoryFTD_Type = PerfCounter64
_F3FpQosShaperHistoryFTD_Object = MibTableColumn
f3FpQosShaperHistoryFTD = _F3FpQosShaperHistoryFTD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 8),
    _F3FpQosShaperHistoryFTD_Type()
)
f3FpQosShaperHistoryFTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryFTD.setStatus("current")
_F3FpQosShaperHistoryABRRL_Type = PerfCounter64
_F3FpQosShaperHistoryABRRL_Object = MibTableColumn
f3FpQosShaperHistoryABRRL = _F3FpQosShaperHistoryABRRL_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 9),
    _F3FpQosShaperHistoryABRRL_Type()
)
f3FpQosShaperHistoryABRRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryABRRL.setStatus("current")
_F3FpQosShaperHistoryBREDD_Type = PerfCounter64
_F3FpQosShaperHistoryBREDD_Object = MibTableColumn
f3FpQosShaperHistoryBREDD = _F3FpQosShaperHistoryBREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 10),
    _F3FpQosShaperHistoryBREDD_Type()
)
f3FpQosShaperHistoryBREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryBREDD.setStatus("current")
_F3FpQosShaperHistoryFREDD_Type = PerfCounter64
_F3FpQosShaperHistoryFREDD_Object = MibTableColumn
f3FpQosShaperHistoryFREDD = _F3FpQosShaperHistoryFREDD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 65, 1, 11),
    _F3FpQosShaperHistoryFREDD_Type()
)
f3FpQosShaperHistoryFREDD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperHistoryFREDD.setStatus("current")
_F3FpQosShaperThresholdTable_Object = MibTable
f3FpQosShaperThresholdTable = _F3FpQosShaperThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 66)
)
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdTable.setStatus("current")
_F3FpQosShaperThresholdEntry_Object = MibTableRow
f3FpQosShaperThresholdEntry = _F3FpQosShaperThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 66, 1)
)
f3FpQosShaperThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3FpQosShaperIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosShaperStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdEntry.setStatus("current")


class _F3FpQosShaperThresholdIndex_Type(Integer32):
    """Custom type f3FpQosShaperThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3FpQosShaperThresholdIndex_Type.__name__ = "Integer32"
_F3FpQosShaperThresholdIndex_Object = MibTableColumn
f3FpQosShaperThresholdIndex = _F3FpQosShaperThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 66, 1, 1),
    _F3FpQosShaperThresholdIndex_Type()
)
f3FpQosShaperThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdIndex.setStatus("current")
_F3FpQosShaperThresholdInterval_Type = CmPmIntervalType
_F3FpQosShaperThresholdInterval_Object = MibTableColumn
f3FpQosShaperThresholdInterval = _F3FpQosShaperThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 66, 1, 2),
    _F3FpQosShaperThresholdInterval_Type()
)
f3FpQosShaperThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdInterval.setStatus("current")
_F3FpQosShaperThresholdVariable_Type = VariablePointer
_F3FpQosShaperThresholdVariable_Object = MibTableColumn
f3FpQosShaperThresholdVariable = _F3FpQosShaperThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 66, 1, 3),
    _F3FpQosShaperThresholdVariable_Type()
)
f3FpQosShaperThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdVariable.setStatus("current")
_F3FpQosShaperThresholdValueLo_Type = Unsigned32
_F3FpQosShaperThresholdValueLo_Object = MibTableColumn
f3FpQosShaperThresholdValueLo = _F3FpQosShaperThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 66, 1, 4),
    _F3FpQosShaperThresholdValueLo_Type()
)
f3FpQosShaperThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdValueLo.setStatus("current")
_F3FpQosShaperThresholdValueHi_Type = Unsigned32
_F3FpQosShaperThresholdValueHi_Object = MibTableColumn
f3FpQosShaperThresholdValueHi = _F3FpQosShaperThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 66, 1, 5),
    _F3FpQosShaperThresholdValueHi_Type()
)
f3FpQosShaperThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdValueHi.setStatus("current")
_F3FpQosShaperThresholdMonValue_Type = Counter64
_F3FpQosShaperThresholdMonValue_Object = MibTableColumn
f3FpQosShaperThresholdMonValue = _F3FpQosShaperThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 66, 1, 6),
    _F3FpQosShaperThresholdMonValue_Type()
)
f3FpQosShaperThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdMonValue.setStatus("current")
_F3FpQosPolicerStatsTable_Object = MibTable
f3FpQosPolicerStatsTable = _F3FpQosPolicerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67)
)
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsTable.setStatus("current")
_F3FpQosPolicerStatsEntry_Object = MibTableRow
f3FpQosPolicerStatsEntry = _F3FpQosPolicerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1)
)
f3FpQosPolicerStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3FpQosPolicerIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsIndex"),
)
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsEntry.setStatus("current")


class _F3FpQosPolicerStatsIndex_Type(Integer32):
    """Custom type f3FpQosPolicerStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3FpQosPolicerStatsIndex_Type.__name__ = "Integer32"
_F3FpQosPolicerStatsIndex_Object = MibTableColumn
f3FpQosPolicerStatsIndex = _F3FpQosPolicerStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 1),
    _F3FpQosPolicerStatsIndex_Type()
)
f3FpQosPolicerStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsIndex.setStatus("current")
_F3FpQosPolicerStatsIntervalType_Type = CmPmIntervalType
_F3FpQosPolicerStatsIntervalType_Object = MibTableColumn
f3FpQosPolicerStatsIntervalType = _F3FpQosPolicerStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 2),
    _F3FpQosPolicerStatsIntervalType_Type()
)
f3FpQosPolicerStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsIntervalType.setStatus("current")
_F3FpQosPolicerStatsValid_Type = TruthValue
_F3FpQosPolicerStatsValid_Object = MibTableColumn
f3FpQosPolicerStatsValid = _F3FpQosPolicerStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 3),
    _F3FpQosPolicerStatsValid_Type()
)
f3FpQosPolicerStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsValid.setStatus("current")
_F3FpQosPolicerStatsAction_Type = CmPmBinAction
_F3FpQosPolicerStatsAction_Object = MibTableColumn
f3FpQosPolicerStatsAction = _F3FpQosPolicerStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 4),
    _F3FpQosPolicerStatsAction_Type()
)
f3FpQosPolicerStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsAction.setStatus("current")
_F3FpQosPolicerStatsFMG_Type = PerfCounter64
_F3FpQosPolicerStatsFMG_Object = MibTableColumn
f3FpQosPolicerStatsFMG = _F3FpQosPolicerStatsFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 5),
    _F3FpQosPolicerStatsFMG_Type()
)
f3FpQosPolicerStatsFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsFMG.setStatus("current")
_F3FpQosPolicerStatsFMY_Type = PerfCounter64
_F3FpQosPolicerStatsFMY_Object = MibTableColumn
f3FpQosPolicerStatsFMY = _F3FpQosPolicerStatsFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 6),
    _F3FpQosPolicerStatsFMY_Type()
)
f3FpQosPolicerStatsFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsFMY.setStatus("current")
_F3FpQosPolicerStatsFMRD_Type = PerfCounter64
_F3FpQosPolicerStatsFMRD_Object = MibTableColumn
f3FpQosPolicerStatsFMRD = _F3FpQosPolicerStatsFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 7),
    _F3FpQosPolicerStatsFMRD_Type()
)
f3FpQosPolicerStatsFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsFMRD.setStatus("current")
_F3FpQosPolicerStatsBytesIn_Type = PerfCounter64
_F3FpQosPolicerStatsBytesIn_Object = MibTableColumn
f3FpQosPolicerStatsBytesIn = _F3FpQosPolicerStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 8),
    _F3FpQosPolicerStatsBytesIn_Type()
)
f3FpQosPolicerStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsBytesIn.setStatus("current")
_F3FpQosPolicerStatsBytesOut_Type = PerfCounter64
_F3FpQosPolicerStatsBytesOut_Object = MibTableColumn
f3FpQosPolicerStatsBytesOut = _F3FpQosPolicerStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 9),
    _F3FpQosPolicerStatsBytesOut_Type()
)
f3FpQosPolicerStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsBytesOut.setStatus("current")
_F3FpQosPolicerStatsABR_Type = PerfCounter64
_F3FpQosPolicerStatsABR_Object = MibTableColumn
f3FpQosPolicerStatsABR = _F3FpQosPolicerStatsABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 67, 1, 10),
    _F3FpQosPolicerStatsABR_Type()
)
f3FpQosPolicerStatsABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerStatsABR.setStatus("current")
_F3FpQosPolicerHistoryTable_Object = MibTable
f3FpQosPolicerHistoryTable = _F3FpQosPolicerHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68)
)
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryTable.setStatus("current")
_F3FpQosPolicerHistoryEntry_Object = MibTableRow
f3FpQosPolicerHistoryEntry = _F3FpQosPolicerHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1)
)
f3FpQosPolicerHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3FpQosPolicerIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryEntry.setStatus("current")


class _F3FpQosPolicerHistoryIndex_Type(Integer32):
    """Custom type f3FpQosPolicerHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3FpQosPolicerHistoryIndex_Type.__name__ = "Integer32"
_F3FpQosPolicerHistoryIndex_Object = MibTableColumn
f3FpQosPolicerHistoryIndex = _F3FpQosPolicerHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 1),
    _F3FpQosPolicerHistoryIndex_Type()
)
f3FpQosPolicerHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryIndex.setStatus("current")
_F3FpQosPolicerHistoryTime_Type = DateAndTime
_F3FpQosPolicerHistoryTime_Object = MibTableColumn
f3FpQosPolicerHistoryTime = _F3FpQosPolicerHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 2),
    _F3FpQosPolicerHistoryTime_Type()
)
f3FpQosPolicerHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryTime.setStatus("current")
_F3FpQosPolicerHistoryValid_Type = TruthValue
_F3FpQosPolicerHistoryValid_Object = MibTableColumn
f3FpQosPolicerHistoryValid = _F3FpQosPolicerHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 3),
    _F3FpQosPolicerHistoryValid_Type()
)
f3FpQosPolicerHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryValid.setStatus("current")
_F3FpQosPolicerHistoryAction_Type = CmPmBinAction
_F3FpQosPolicerHistoryAction_Object = MibTableColumn
f3FpQosPolicerHistoryAction = _F3FpQosPolicerHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 4),
    _F3FpQosPolicerHistoryAction_Type()
)
f3FpQosPolicerHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryAction.setStatus("current")
_F3FpQosPolicerHistoryFMG_Type = PerfCounter64
_F3FpQosPolicerHistoryFMG_Object = MibTableColumn
f3FpQosPolicerHistoryFMG = _F3FpQosPolicerHistoryFMG_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 5),
    _F3FpQosPolicerHistoryFMG_Type()
)
f3FpQosPolicerHistoryFMG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryFMG.setStatus("current")
_F3FpQosPolicerHistoryFMY_Type = PerfCounter64
_F3FpQosPolicerHistoryFMY_Object = MibTableColumn
f3FpQosPolicerHistoryFMY = _F3FpQosPolicerHistoryFMY_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 6),
    _F3FpQosPolicerHistoryFMY_Type()
)
f3FpQosPolicerHistoryFMY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryFMY.setStatus("current")
_F3FpQosPolicerHistoryFMRD_Type = PerfCounter64
_F3FpQosPolicerHistoryFMRD_Object = MibTableColumn
f3FpQosPolicerHistoryFMRD = _F3FpQosPolicerHistoryFMRD_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 7),
    _F3FpQosPolicerHistoryFMRD_Type()
)
f3FpQosPolicerHistoryFMRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryFMRD.setStatus("current")
_F3FpQosPolicerHistoryBytesIn_Type = PerfCounter64
_F3FpQosPolicerHistoryBytesIn_Object = MibTableColumn
f3FpQosPolicerHistoryBytesIn = _F3FpQosPolicerHistoryBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 8),
    _F3FpQosPolicerHistoryBytesIn_Type()
)
f3FpQosPolicerHistoryBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryBytesIn.setStatus("current")
_F3FpQosPolicerHistoryBytesOut_Type = PerfCounter64
_F3FpQosPolicerHistoryBytesOut_Object = MibTableColumn
f3FpQosPolicerHistoryBytesOut = _F3FpQosPolicerHistoryBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 9),
    _F3FpQosPolicerHistoryBytesOut_Type()
)
f3FpQosPolicerHistoryBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryBytesOut.setStatus("current")
_F3FpQosPolicerHistoryABR_Type = PerfCounter64
_F3FpQosPolicerHistoryABR_Object = MibTableColumn
f3FpQosPolicerHistoryABR = _F3FpQosPolicerHistoryABR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 68, 1, 10),
    _F3FpQosPolicerHistoryABR_Type()
)
f3FpQosPolicerHistoryABR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerHistoryABR.setStatus("current")
_F3FpQosPolicerThresholdTable_Object = MibTable
f3FpQosPolicerThresholdTable = _F3FpQosPolicerThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 69)
)
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdTable.setStatus("current")
_F3FpQosPolicerThresholdEntry_Object = MibTableRow
f3FpQosPolicerThresholdEntry = _F3FpQosPolicerThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 69, 1)
)
f3FpQosPolicerThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3FpQosPolicerIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdEntry.setStatus("current")


class _F3FpQosPolicerThresholdIndex_Type(Integer32):
    """Custom type f3FpQosPolicerThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3FpQosPolicerThresholdIndex_Type.__name__ = "Integer32"
_F3FpQosPolicerThresholdIndex_Object = MibTableColumn
f3FpQosPolicerThresholdIndex = _F3FpQosPolicerThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 69, 1, 1),
    _F3FpQosPolicerThresholdIndex_Type()
)
f3FpQosPolicerThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdIndex.setStatus("current")
_F3FpQosPolicerThresholdInterval_Type = CmPmIntervalType
_F3FpQosPolicerThresholdInterval_Object = MibTableColumn
f3FpQosPolicerThresholdInterval = _F3FpQosPolicerThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 69, 1, 2),
    _F3FpQosPolicerThresholdInterval_Type()
)
f3FpQosPolicerThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdInterval.setStatus("current")
_F3FpQosPolicerThresholdVariable_Type = VariablePointer
_F3FpQosPolicerThresholdVariable_Object = MibTableColumn
f3FpQosPolicerThresholdVariable = _F3FpQosPolicerThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 69, 1, 3),
    _F3FpQosPolicerThresholdVariable_Type()
)
f3FpQosPolicerThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdVariable.setStatus("current")
_F3FpQosPolicerThresholdValueLo_Type = Unsigned32
_F3FpQosPolicerThresholdValueLo_Object = MibTableColumn
f3FpQosPolicerThresholdValueLo = _F3FpQosPolicerThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 69, 1, 4),
    _F3FpQosPolicerThresholdValueLo_Type()
)
f3FpQosPolicerThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdValueLo.setStatus("current")
_F3FpQosPolicerThresholdValueHi_Type = Unsigned32
_F3FpQosPolicerThresholdValueHi_Object = MibTableColumn
f3FpQosPolicerThresholdValueHi = _F3FpQosPolicerThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 69, 1, 5),
    _F3FpQosPolicerThresholdValueHi_Type()
)
f3FpQosPolicerThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdValueHi.setStatus("current")
_F3FpQosPolicerThresholdMonValue_Type = Counter64
_F3FpQosPolicerThresholdMonValue_Object = MibTableColumn
f3FpQosPolicerThresholdMonValue = _F3FpQosPolicerThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 69, 1, 6),
    _F3FpQosPolicerThresholdMonValue_Type()
)
f3FpQosPolicerThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdMonValue.setStatus("current")
_F3AclRuleStatsTable_Object = MibTable
f3AclRuleStatsTable = _F3AclRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 70)
)
if mibBuilder.loadTexts:
    f3AclRuleStatsTable.setStatus("current")
_F3AclRuleStatsEntry_Object = MibTableRow
f3AclRuleStatsEntry = _F3AclRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 70, 1)
)
f3AclRuleStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3AclRuleIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3AclRuleStatsIndex"),
)
if mibBuilder.loadTexts:
    f3AclRuleStatsEntry.setStatus("current")


class _F3AclRuleStatsIndex_Type(Integer32):
    """Custom type f3AclRuleStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3AclRuleStatsIndex_Type.__name__ = "Integer32"
_F3AclRuleStatsIndex_Object = MibTableColumn
f3AclRuleStatsIndex = _F3AclRuleStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 70, 1, 1),
    _F3AclRuleStatsIndex_Type()
)
f3AclRuleStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AclRuleStatsIndex.setStatus("current")
_F3AclRuleStatsIntervalType_Type = CmPmIntervalType
_F3AclRuleStatsIntervalType_Object = MibTableColumn
f3AclRuleStatsIntervalType = _F3AclRuleStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 70, 1, 2),
    _F3AclRuleStatsIntervalType_Type()
)
f3AclRuleStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleStatsIntervalType.setStatus("current")
_F3AclRuleStatsValid_Type = TruthValue
_F3AclRuleStatsValid_Object = MibTableColumn
f3AclRuleStatsValid = _F3AclRuleStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 70, 1, 3),
    _F3AclRuleStatsValid_Type()
)
f3AclRuleStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleStatsValid.setStatus("current")
_F3AclRuleStatsAction_Type = CmPmBinAction
_F3AclRuleStatsAction_Object = MibTableColumn
f3AclRuleStatsAction = _F3AclRuleStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 70, 1, 4),
    _F3AclRuleStatsAction_Type()
)
f3AclRuleStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AclRuleStatsAction.setStatus("current")
_F3AclRuleStatsRuleMatch_Type = PerfCounter64
_F3AclRuleStatsRuleMatch_Object = MibTableColumn
f3AclRuleStatsRuleMatch = _F3AclRuleStatsRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 70, 1, 5),
    _F3AclRuleStatsRuleMatch_Type()
)
f3AclRuleStatsRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleStatsRuleMatch.setStatus("current")
_F3AclRuleHistoryTable_Object = MibTable
f3AclRuleHistoryTable = _F3AclRuleHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 71)
)
if mibBuilder.loadTexts:
    f3AclRuleHistoryTable.setStatus("current")
_F3AclRuleHistoryEntry_Object = MibTableRow
f3AclRuleHistoryEntry = _F3AclRuleHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 71, 1)
)
f3AclRuleHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3AclRuleIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3AclRuleStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3AclRuleHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3AclRuleHistoryEntry.setStatus("current")


class _F3AclRuleHistoryIndex_Type(Integer32):
    """Custom type f3AclRuleHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3AclRuleHistoryIndex_Type.__name__ = "Integer32"
_F3AclRuleHistoryIndex_Object = MibTableColumn
f3AclRuleHistoryIndex = _F3AclRuleHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 71, 1, 1),
    _F3AclRuleHistoryIndex_Type()
)
f3AclRuleHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AclRuleHistoryIndex.setStatus("current")
_F3AclRuleHistoryTime_Type = DateAndTime
_F3AclRuleHistoryTime_Object = MibTableColumn
f3AclRuleHistoryTime = _F3AclRuleHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 71, 1, 2),
    _F3AclRuleHistoryTime_Type()
)
f3AclRuleHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleHistoryTime.setStatus("current")
_F3AclRuleHistoryValid_Type = TruthValue
_F3AclRuleHistoryValid_Object = MibTableColumn
f3AclRuleHistoryValid = _F3AclRuleHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 71, 1, 3),
    _F3AclRuleHistoryValid_Type()
)
f3AclRuleHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleHistoryValid.setStatus("current")
_F3AclRuleHistoryAction_Type = CmPmBinAction
_F3AclRuleHistoryAction_Object = MibTableColumn
f3AclRuleHistoryAction = _F3AclRuleHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 71, 1, 4),
    _F3AclRuleHistoryAction_Type()
)
f3AclRuleHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AclRuleHistoryAction.setStatus("current")
_F3AclRuleHistoryRuleMatch_Type = PerfCounter64
_F3AclRuleHistoryRuleMatch_Object = MibTableColumn
f3AclRuleHistoryRuleMatch = _F3AclRuleHistoryRuleMatch_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 71, 1, 5),
    _F3AclRuleHistoryRuleMatch_Type()
)
f3AclRuleHistoryRuleMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleHistoryRuleMatch.setStatus("current")
_F3AclRuleThresholdTable_Object = MibTable
f3AclRuleThresholdTable = _F3AclRuleThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 72)
)
if mibBuilder.loadTexts:
    f3AclRuleThresholdTable.setStatus("current")
_F3AclRuleThresholdEntry_Object = MibTableRow
f3AclRuleThresholdEntry = _F3AclRuleThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 72, 1)
)
f3AclRuleThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowPointIndex"),
    (0, "CM-FACILITY-MIB", "f3AclRuleIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3AclRuleStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3AclRuleThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3AclRuleThresholdEntry.setStatus("current")


class _F3AclRuleThresholdIndex_Type(Integer32):
    """Custom type f3AclRuleThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3AclRuleThresholdIndex_Type.__name__ = "Integer32"
_F3AclRuleThresholdIndex_Object = MibTableColumn
f3AclRuleThresholdIndex = _F3AclRuleThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 72, 1, 1),
    _F3AclRuleThresholdIndex_Type()
)
f3AclRuleThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AclRuleThresholdIndex.setStatus("current")
_F3AclRuleThresholdInterval_Type = CmPmIntervalType
_F3AclRuleThresholdInterval_Object = MibTableColumn
f3AclRuleThresholdInterval = _F3AclRuleThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 72, 1, 2),
    _F3AclRuleThresholdInterval_Type()
)
f3AclRuleThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleThresholdInterval.setStatus("current")
_F3AclRuleThresholdVariable_Type = VariablePointer
_F3AclRuleThresholdVariable_Object = MibTableColumn
f3AclRuleThresholdVariable = _F3AclRuleThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 72, 1, 3),
    _F3AclRuleThresholdVariable_Type()
)
f3AclRuleThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleThresholdVariable.setStatus("current")
_F3AclRuleThresholdValueLo_Type = Unsigned32
_F3AclRuleThresholdValueLo_Object = MibTableColumn
f3AclRuleThresholdValueLo = _F3AclRuleThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 72, 1, 4),
    _F3AclRuleThresholdValueLo_Type()
)
f3AclRuleThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AclRuleThresholdValueLo.setStatus("current")
_F3AclRuleThresholdValueHi_Type = Unsigned32
_F3AclRuleThresholdValueHi_Object = MibTableColumn
f3AclRuleThresholdValueHi = _F3AclRuleThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 72, 1, 5),
    _F3AclRuleThresholdValueHi_Type()
)
f3AclRuleThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AclRuleThresholdValueHi.setStatus("current")
_F3AclRuleThresholdMonValue_Type = Counter64
_F3AclRuleThresholdMonValue_Object = MibTableColumn
f3AclRuleThresholdMonValue = _F3AclRuleThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 72, 1, 6),
    _F3AclRuleThresholdMonValue_Type()
)
f3AclRuleThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AclRuleThresholdMonValue.setStatus("current")
_CmEthernetNetPortXdslStatsTable_Object = MibTable
cmEthernetNetPortXdslStatsTable = _CmEthernetNetPortXdslStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73)
)
if mibBuilder.loadTexts:
    cmEthernetNetPortXdslStatsTable.setStatus("current")
_CmEthernetNetPortXdslStatsEntry_Object = MibTableRow
cmEthernetNetPortXdslStatsEntry = _CmEthernetNetPortXdslStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1)
)
if mibBuilder.loadTexts:
    cmEthernetNetPortXdslStatsEntry.setStatus("current")
_CmEthernetNetPortStatsXdslUsPkt_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsPkt_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsPkt = _CmEthernetNetPortStatsXdslUsPkt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 1),
    _CmEthernetNetPortStatsXdslUsPkt_Type()
)
cmEthernetNetPortStatsXdslUsPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsPkt.setStatus("current")
_CmEthernetNetPortStatsXdslUsCrcError_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsCrcError_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsCrcError = _CmEthernetNetPortStatsXdslUsCrcError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 2),
    _CmEthernetNetPortStatsXdslUsCrcError_Type()
)
cmEthernetNetPortStatsXdslUsCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsCrcError.setStatus("current")
_CmEthernetNetPortStatsXdslDsPkt_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsPkt_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsPkt = _CmEthernetNetPortStatsXdslDsPkt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 3),
    _CmEthernetNetPortStatsXdslDsPkt_Type()
)
cmEthernetNetPortStatsXdslDsPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsPkt.setStatus("current")
_CmEthernetNetPortStatsXdslUsFecs_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsFecs_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsFecs = _CmEthernetNetPortStatsXdslUsFecs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 4),
    _CmEthernetNetPortStatsXdslUsFecs_Type()
)
cmEthernetNetPortStatsXdslUsFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsFecs.setStatus("current")
_CmEthernetNetPortStatsXdslDsFecs_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsFecs_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsFecs = _CmEthernetNetPortStatsXdslDsFecs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 5),
    _CmEthernetNetPortStatsXdslDsFecs_Type()
)
cmEthernetNetPortStatsXdslDsFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsFecs.setStatus("current")
_CmEthernetNetPortStatsXdslUsEs_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsEs_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsEs = _CmEthernetNetPortStatsXdslUsEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 6),
    _CmEthernetNetPortStatsXdslUsEs_Type()
)
cmEthernetNetPortStatsXdslUsEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsEs.setStatus("current")
_CmEthernetNetPortStatsXdslDsEs_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsEs_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsEs = _CmEthernetNetPortStatsXdslDsEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 7),
    _CmEthernetNetPortStatsXdslDsEs_Type()
)
cmEthernetNetPortStatsXdslDsEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsEs.setStatus("current")
_CmEthernetNetPortStatsXdslUsSes_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsSes_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsSes = _CmEthernetNetPortStatsXdslUsSes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 8),
    _CmEthernetNetPortStatsXdslUsSes_Type()
)
cmEthernetNetPortStatsXdslUsSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsSes.setStatus("current")
_CmEthernetNetPortStatsXdslDsSes_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsSes_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsSes = _CmEthernetNetPortStatsXdslDsSes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 9),
    _CmEthernetNetPortStatsXdslDsSes_Type()
)
cmEthernetNetPortStatsXdslDsSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsSes.setStatus("current")
_CmEthernetNetPortStatsXdslUsLoss_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsLoss_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsLoss = _CmEthernetNetPortStatsXdslUsLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 10),
    _CmEthernetNetPortStatsXdslUsLoss_Type()
)
cmEthernetNetPortStatsXdslUsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsLoss.setStatus("current")
_CmEthernetNetPortStatsXdslDsLoss_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsLoss_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsLoss = _CmEthernetNetPortStatsXdslDsLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 11),
    _CmEthernetNetPortStatsXdslDsLoss_Type()
)
cmEthernetNetPortStatsXdslDsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsLoss.setStatus("current")
_CmEthernetNetPortStatsXdslDsUas_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsUas_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsUas = _CmEthernetNetPortStatsXdslDsUas_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 12),
    _CmEthernetNetPortStatsXdslDsUas_Type()
)
cmEthernetNetPortStatsXdslDsUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsUas.setStatus("current")
_CmEthernetNetPortStatsXdslUsCv_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsCv_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsCv = _CmEthernetNetPortStatsXdslUsCv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 13),
    _CmEthernetNetPortStatsXdslUsCv_Type()
)
cmEthernetNetPortStatsXdslUsCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsCv.setStatus("current")
_CmEthernetNetPortStatsXdslDsCv_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsCv_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsCv = _CmEthernetNetPortStatsXdslDsCv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 14),
    _CmEthernetNetPortStatsXdslDsCv_Type()
)
cmEthernetNetPortStatsXdslDsCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsCv.setStatus("current")
_CmEthernetNetPortStatsXdslUsFec_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsFec_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsFec = _CmEthernetNetPortStatsXdslUsFec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 15),
    _CmEthernetNetPortStatsXdslUsFec_Type()
)
cmEthernetNetPortStatsXdslUsFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsFec.setStatus("current")
_CmEthernetNetPortStatsXdslDsFec_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsFec_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsFec = _CmEthernetNetPortStatsXdslDsFec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 16),
    _CmEthernetNetPortStatsXdslDsFec_Type()
)
cmEthernetNetPortStatsXdslDsFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsFec.setStatus("current")
_CmEthernetNetPortStatsXdslDsFullInits_Type = PerfCounter64
_CmEthernetNetPortStatsXdslDsFullInits_Object = MibTableColumn
cmEthernetNetPortStatsXdslDsFullInits = _CmEthernetNetPortStatsXdslDsFullInits_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 17),
    _CmEthernetNetPortStatsXdslDsFullInits_Type()
)
cmEthernetNetPortStatsXdslDsFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslDsFullInits.setStatus("current")
_CmEthernetNetPortStatsXdslUsFullInits_Type = PerfCounter64
_CmEthernetNetPortStatsXdslUsFullInits_Object = MibTableColumn
cmEthernetNetPortStatsXdslUsFullInits = _CmEthernetNetPortStatsXdslUsFullInits_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 73, 1, 18),
    _CmEthernetNetPortStatsXdslUsFullInits_Type()
)
cmEthernetNetPortStatsXdslUsFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortStatsXdslUsFullInits.setStatus("current")
_CmEthernetNetPortXdslHistoryTable_Object = MibTable
cmEthernetNetPortXdslHistoryTable = _CmEthernetNetPortXdslHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74)
)
if mibBuilder.loadTexts:
    cmEthernetNetPortXdslHistoryTable.setStatus("current")
_CmEthernetNetPortXdslHistoryEntry_Object = MibTableRow
cmEthernetNetPortXdslHistoryEntry = _CmEthernetNetPortXdslHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1)
)
if mibBuilder.loadTexts:
    cmEthernetNetPortXdslHistoryEntry.setStatus("current")
_CmEthernetNetPortHistoryXdslUsPkt_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsPkt_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsPkt = _CmEthernetNetPortHistoryXdslUsPkt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 1),
    _CmEthernetNetPortHistoryXdslUsPkt_Type()
)
cmEthernetNetPortHistoryXdslUsPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsPkt.setStatus("current")
_CmEthernetNetPortHistoryXdslUsCrcError_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsCrcError_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsCrcError = _CmEthernetNetPortHistoryXdslUsCrcError_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 2),
    _CmEthernetNetPortHistoryXdslUsCrcError_Type()
)
cmEthernetNetPortHistoryXdslUsCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsCrcError.setStatus("current")
_CmEthernetNetPortHistoryXdslDsPkt_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsPkt_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsPkt = _CmEthernetNetPortHistoryXdslDsPkt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 3),
    _CmEthernetNetPortHistoryXdslDsPkt_Type()
)
cmEthernetNetPortHistoryXdslDsPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsPkt.setStatus("current")
_CmEthernetNetPortHistoryXdslUsFecs_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsFecs_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsFecs = _CmEthernetNetPortHistoryXdslUsFecs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 4),
    _CmEthernetNetPortHistoryXdslUsFecs_Type()
)
cmEthernetNetPortHistoryXdslUsFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsFecs.setStatus("current")
_CmEthernetNetPortHistoryXdslDsFecs_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsFecs_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsFecs = _CmEthernetNetPortHistoryXdslDsFecs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 5),
    _CmEthernetNetPortHistoryXdslDsFecs_Type()
)
cmEthernetNetPortHistoryXdslDsFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsFecs.setStatus("current")
_CmEthernetNetPortHistoryXdslUsEs_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsEs_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsEs = _CmEthernetNetPortHistoryXdslUsEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 6),
    _CmEthernetNetPortHistoryXdslUsEs_Type()
)
cmEthernetNetPortHistoryXdslUsEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsEs.setStatus("current")
_CmEthernetNetPortHistoryXdslDsEs_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsEs_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsEs = _CmEthernetNetPortHistoryXdslDsEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 7),
    _CmEthernetNetPortHistoryXdslDsEs_Type()
)
cmEthernetNetPortHistoryXdslDsEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsEs.setStatus("current")
_CmEthernetNetPortHistoryXdslUsSes_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsSes_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsSes = _CmEthernetNetPortHistoryXdslUsSes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 8),
    _CmEthernetNetPortHistoryXdslUsSes_Type()
)
cmEthernetNetPortHistoryXdslUsSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsSes.setStatus("current")
_CmEthernetNetPortHistoryXdslDsSes_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsSes_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsSes = _CmEthernetNetPortHistoryXdslDsSes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 9),
    _CmEthernetNetPortHistoryXdslDsSes_Type()
)
cmEthernetNetPortHistoryXdslDsSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsSes.setStatus("current")
_CmEthernetNetPortHistoryXdslUsLoss_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsLoss_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsLoss = _CmEthernetNetPortHistoryXdslUsLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 10),
    _CmEthernetNetPortHistoryXdslUsLoss_Type()
)
cmEthernetNetPortHistoryXdslUsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsLoss.setStatus("current")
_CmEthernetNetPortHistoryXdslDsLoss_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsLoss_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsLoss = _CmEthernetNetPortHistoryXdslDsLoss_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 11),
    _CmEthernetNetPortHistoryXdslDsLoss_Type()
)
cmEthernetNetPortHistoryXdslDsLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsLoss.setStatus("current")
_CmEthernetNetPortHistoryXdslDsUas_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsUas_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsUas = _CmEthernetNetPortHistoryXdslDsUas_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 12),
    _CmEthernetNetPortHistoryXdslDsUas_Type()
)
cmEthernetNetPortHistoryXdslDsUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsUas.setStatus("current")
_CmEthernetNetPortHistoryXdslUsCv_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsCv_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsCv = _CmEthernetNetPortHistoryXdslUsCv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 13),
    _CmEthernetNetPortHistoryXdslUsCv_Type()
)
cmEthernetNetPortHistoryXdslUsCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsCv.setStatus("current")
_CmEthernetNetPortHistoryXdslDsCv_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsCv_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsCv = _CmEthernetNetPortHistoryXdslDsCv_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 14),
    _CmEthernetNetPortHistoryXdslDsCv_Type()
)
cmEthernetNetPortHistoryXdslDsCv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsCv.setStatus("current")
_CmEthernetNetPortHistoryXdslUsFec_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsFec_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsFec = _CmEthernetNetPortHistoryXdslUsFec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 15),
    _CmEthernetNetPortHistoryXdslUsFec_Type()
)
cmEthernetNetPortHistoryXdslUsFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsFec.setStatus("current")
_CmEthernetNetPortHistoryXdslDsFec_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsFec_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsFec = _CmEthernetNetPortHistoryXdslDsFec_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 16),
    _CmEthernetNetPortHistoryXdslDsFec_Type()
)
cmEthernetNetPortHistoryXdslDsFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsFec.setStatus("current")
_CmEthernetNetPortHistoryXdslDsFullInits_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslDsFullInits_Object = MibTableColumn
cmEthernetNetPortHistoryXdslDsFullInits = _CmEthernetNetPortHistoryXdslDsFullInits_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 17),
    _CmEthernetNetPortHistoryXdslDsFullInits_Type()
)
cmEthernetNetPortHistoryXdslDsFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslDsFullInits.setStatus("current")
_CmEthernetNetPortHistoryXdslUsFullInits_Type = PerfCounter64
_CmEthernetNetPortHistoryXdslUsFullInits_Object = MibTableColumn
cmEthernetNetPortHistoryXdslUsFullInits = _CmEthernetNetPortHistoryXdslUsFullInits_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 74, 1, 18),
    _CmEthernetNetPortHistoryXdslUsFullInits_Type()
)
cmEthernetNetPortHistoryXdslUsFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEthernetNetPortHistoryXdslUsFullInits.setStatus("current")
_F3CardStatsTable_Object = MibTable
f3CardStatsTable = _F3CardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75)
)
if mibBuilder.loadTexts:
    f3CardStatsTable.setStatus("current")
_F3CardStatsEntry_Object = MibTableRow
f3CardStatsEntry = _F3CardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1)
)
f3CardStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3CardStatsIndex"),
)
if mibBuilder.loadTexts:
    f3CardStatsEntry.setStatus("current")


class _F3CardStatsIndex_Type(Integer32):
    """Custom type f3CardStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_F3CardStatsIndex_Type.__name__ = "Integer32"
_F3CardStatsIndex_Object = MibTableColumn
f3CardStatsIndex = _F3CardStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 1),
    _F3CardStatsIndex_Type()
)
f3CardStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3CardStatsIndex.setStatus("current")
_F3CardStatsIntervalType_Type = CmPmIntervalType
_F3CardStatsIntervalType_Object = MibTableColumn
f3CardStatsIntervalType = _F3CardStatsIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 2),
    _F3CardStatsIntervalType_Type()
)
f3CardStatsIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardStatsIntervalType.setStatus("current")
_F3CardStatsValid_Type = TruthValue
_F3CardStatsValid_Object = MibTableColumn
f3CardStatsValid = _F3CardStatsValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 3),
    _F3CardStatsValid_Type()
)
f3CardStatsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardStatsValid.setStatus("current")
_F3CardStatsAction_Type = CmPmBinAction
_F3CardStatsAction_Object = MibTableColumn
f3CardStatsAction = _F3CardStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 4),
    _F3CardStatsAction_Type()
)
f3CardStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CardStatsAction.setStatus("current")
_F3CardStatsACU_Type = Integer32
_F3CardStatsACU_Object = MibTableColumn
f3CardStatsACU = _F3CardStatsACU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 5),
    _F3CardStatsACU_Type()
)
f3CardStatsACU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardStatsACU.setStatus("current")
_F3CardStatsMCU_Type = Integer32
_F3CardStatsMCU_Object = MibTableColumn
f3CardStatsMCU = _F3CardStatsMCU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 6),
    _F3CardStatsMCU_Type()
)
f3CardStatsMCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardStatsMCU.setStatus("current")
_F3CardStatsICU_Type = Integer32
_F3CardStatsICU_Object = MibTableColumn
f3CardStatsICU = _F3CardStatsICU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 7),
    _F3CardStatsICU_Type()
)
f3CardStatsICU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardStatsICU.setStatus("current")
_F3CardStatsAMU_Type = Integer32
_F3CardStatsAMU_Object = MibTableColumn
f3CardStatsAMU = _F3CardStatsAMU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 8),
    _F3CardStatsAMU_Type()
)
f3CardStatsAMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardStatsAMU.setStatus("current")
_F3CardStatsMMU_Type = Integer32
_F3CardStatsMMU_Object = MibTableColumn
f3CardStatsMMU = _F3CardStatsMMU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 9),
    _F3CardStatsMMU_Type()
)
f3CardStatsMMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardStatsMMU.setStatus("current")
_F3CardStatsIMU_Type = Integer32
_F3CardStatsIMU_Object = MibTableColumn
f3CardStatsIMU = _F3CardStatsIMU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 75, 1, 10),
    _F3CardStatsIMU_Type()
)
f3CardStatsIMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardStatsIMU.setStatus("current")
_F3CardHistoryTable_Object = MibTable
f3CardHistoryTable = _F3CardHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76)
)
if mibBuilder.loadTexts:
    f3CardHistoryTable.setStatus("current")
_F3CardHistoryEntry_Object = MibTableRow
f3CardHistoryEntry = _F3CardHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1)
)
f3CardHistoryEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3CardStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3CardHistoryIndex"),
)
if mibBuilder.loadTexts:
    f3CardHistoryEntry.setStatus("current")


class _F3CardHistoryIndex_Type(Integer32):
    """Custom type f3CardHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_F3CardHistoryIndex_Type.__name__ = "Integer32"
_F3CardHistoryIndex_Object = MibTableColumn
f3CardHistoryIndex = _F3CardHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 1),
    _F3CardHistoryIndex_Type()
)
f3CardHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3CardHistoryIndex.setStatus("current")
_F3CardHistoryTime_Type = DateAndTime
_F3CardHistoryTime_Object = MibTableColumn
f3CardHistoryTime = _F3CardHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 2),
    _F3CardHistoryTime_Type()
)
f3CardHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardHistoryTime.setStatus("current")
_F3CardHistoryValid_Type = TruthValue
_F3CardHistoryValid_Object = MibTableColumn
f3CardHistoryValid = _F3CardHistoryValid_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 3),
    _F3CardHistoryValid_Type()
)
f3CardHistoryValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardHistoryValid.setStatus("current")
_F3CardHistoryAction_Type = CmPmBinAction
_F3CardHistoryAction_Object = MibTableColumn
f3CardHistoryAction = _F3CardHistoryAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 4),
    _F3CardHistoryAction_Type()
)
f3CardHistoryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CardHistoryAction.setStatus("current")
_F3CardHistoryACU_Type = Integer32
_F3CardHistoryACU_Object = MibTableColumn
f3CardHistoryACU = _F3CardHistoryACU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 5),
    _F3CardHistoryACU_Type()
)
f3CardHistoryACU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardHistoryACU.setStatus("current")
_F3CardHistoryMCU_Type = Integer32
_F3CardHistoryMCU_Object = MibTableColumn
f3CardHistoryMCU = _F3CardHistoryMCU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 6),
    _F3CardHistoryMCU_Type()
)
f3CardHistoryMCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardHistoryMCU.setStatus("current")
_F3CardHistoryICU_Type = Integer32
_F3CardHistoryICU_Object = MibTableColumn
f3CardHistoryICU = _F3CardHistoryICU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 7),
    _F3CardHistoryICU_Type()
)
f3CardHistoryICU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardHistoryICU.setStatus("current")
_F3CardHistoryAMU_Type = Integer32
_F3CardHistoryAMU_Object = MibTableColumn
f3CardHistoryAMU = _F3CardHistoryAMU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 8),
    _F3CardHistoryAMU_Type()
)
f3CardHistoryAMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardHistoryAMU.setStatus("current")
_F3CardHistoryMMU_Type = Integer32
_F3CardHistoryMMU_Object = MibTableColumn
f3CardHistoryMMU = _F3CardHistoryMMU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 9),
    _F3CardHistoryMMU_Type()
)
f3CardHistoryMMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardHistoryMMU.setStatus("current")
_F3CardHistoryIMU_Type = Integer32
_F3CardHistoryIMU_Object = MibTableColumn
f3CardHistoryIMU = _F3CardHistoryIMU_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 76, 1, 10),
    _F3CardHistoryIMU_Type()
)
f3CardHistoryIMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardHistoryIMU.setStatus("current")
_F3CardThresholdTable_Object = MibTable
f3CardThresholdTable = _F3CardThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 77)
)
if mibBuilder.loadTexts:
    f3CardThresholdTable.setStatus("current")
_F3CardThresholdEntry_Object = MibTableRow
f3CardThresholdEntry = _F3CardThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 77, 1)
)
f3CardThresholdEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3CardStatsIndex"),
    (0, "CM-PERFORMANCE-MIB", "f3CardThresholdIndex"),
)
if mibBuilder.loadTexts:
    f3CardThresholdEntry.setStatus("current")


class _F3CardThresholdIndex_Type(Integer32):
    """Custom type f3CardThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_F3CardThresholdIndex_Type.__name__ = "Integer32"
_F3CardThresholdIndex_Object = MibTableColumn
f3CardThresholdIndex = _F3CardThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 77, 1, 1),
    _F3CardThresholdIndex_Type()
)
f3CardThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3CardThresholdIndex.setStatus("current")
_F3CardThresholdInterval_Type = CmPmIntervalType
_F3CardThresholdInterval_Object = MibTableColumn
f3CardThresholdInterval = _F3CardThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 77, 1, 2),
    _F3CardThresholdInterval_Type()
)
f3CardThresholdInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardThresholdInterval.setStatus("current")
_F3CardThresholdVariable_Type = VariablePointer
_F3CardThresholdVariable_Object = MibTableColumn
f3CardThresholdVariable = _F3CardThresholdVariable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 77, 1, 3),
    _F3CardThresholdVariable_Type()
)
f3CardThresholdVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardThresholdVariable.setStatus("current")
_F3CardThresholdValueLo_Type = Unsigned32
_F3CardThresholdValueLo_Object = MibTableColumn
f3CardThresholdValueLo = _F3CardThresholdValueLo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 77, 1, 4),
    _F3CardThresholdValueLo_Type()
)
f3CardThresholdValueLo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CardThresholdValueLo.setStatus("current")
_F3CardThresholdValueHi_Type = Unsigned32
_F3CardThresholdValueHi_Object = MibTableColumn
f3CardThresholdValueHi = _F3CardThresholdValueHi_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 77, 1, 5),
    _F3CardThresholdValueHi_Type()
)
f3CardThresholdValueHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3CardThresholdValueHi.setStatus("current")
_F3CardThresholdMonValue_Type = Counter64
_F3CardThresholdMonValue_Object = MibTableColumn
f3CardThresholdMonValue = _F3CardThresholdMonValue_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 1, 77, 1, 6),
    _F3CardThresholdMonValue_Type()
)
f3CardThresholdMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3CardThresholdMonValue.setStatus("current")
_CmPerfNotifications_ObjectIdentity = ObjectIdentity
cmPerfNotifications = _CmPerfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2)
)
_CmPerfConformance_ObjectIdentity = ObjectIdentity
cmPerfConformance = _CmPerfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3)
)
_CmPerfCompliances_ObjectIdentity = ObjectIdentity
cmPerfCompliances = _CmPerfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 1)
)
_CmPerfGroups_ObjectIdentity = ObjectIdentity
cmPerfGroups = _CmPerfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2)
)
cmFlowEntry.registerAugmentions(
    ("CM-PERFORMANCE-MIB",
     "cmFlowBWExtEntry")
)
cmFlowBWExtEntry.setIndexNames(*cmFlowEntry.getIndexNames())
cmEthernetNetPortStatsEntry.registerAugmentions(
    ("CM-PERFORMANCE-MIB",
     "cmEthernetNetPortXdslStatsEntry")
)
cmEthernetNetPortXdslStatsEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
cmEthernetNetPortHistoryEntry.registerAugmentions(
    ("CM-PERFORMANCE-MIB",
     "cmEthernetNetPortXdslHistoryEntry")
)
cmEthernetNetPortXdslHistoryEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())

# Managed Objects groups

cmPerfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 1)
)
cmPerfObjectGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdVarOprVariance"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdVarOptVariance"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsPSC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryPSC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdVarOprVariance"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdVarOptVariance"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsES"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsSES"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMGA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMRDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesInA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesOutA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMGN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMRDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesInN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesOutN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFTDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMCDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFBCDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryES"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistorySES"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMGA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMRDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesInA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesOutA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMGN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMRDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesInN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesOutN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFTDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMCDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFBCDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsABRRLR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryABRRLR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsFMG"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsFMY"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsFMYD"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsFMRD"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsABR"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryFMG"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryFMY"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryFMYD"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryFMRD"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryABR"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsBR"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsFR"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryBR"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryFR"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsATFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsL2PTRxFramesEncap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsL2PTTxFramesDecap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsFmcd"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsFbcd"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAclDropNoMatch"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAclFwd2Cpu"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsDhcpDropNoAssocIf"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsDroppedFragmented"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsRLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsROPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsROPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsRTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryATFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryL2PTRxFramesEncap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryL2PTTxFramesDecap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryFmcd"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryFbcd"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAclDropNoMatch"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAclFwd2Cpu"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryDhcpDropNoAssocIf"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryRLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryROPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryROPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryRTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdVarOprVariance"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdVarOptVariance"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsABRRLRx"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsSES"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMG"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMY"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMRD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFACLD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryABRRLRx"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistorySES"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMG"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMY"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMRD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFACLD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointStatsSES"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointHistorySES"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsValid"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsAction"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsFMG"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsFMY"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsFMYD"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsFMRD"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2StatsABR"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryFMG"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryFMY"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryFMYD"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryFMRD"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2HistoryABR"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsValid"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsAction"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsBT"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsBTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsFD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsABRRL"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsBREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2StatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryBT"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryBTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryFD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2HistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESBF"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESBP"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESBS"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESC"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESCAE"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESDE"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESF"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESFS"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESJ"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESMF"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESMP"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESO"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESOF"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESOP"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESP"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESP64"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESP65"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESP128"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESP256"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESP512"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESP1024"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESP1519"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESUF"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsESUP"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsAUFD"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsAPFD"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsABRTx"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsATFD"),
        ("CM-PERFORMANCE-MIB", "cmLagStatsLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESBF"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESBP"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESBS"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESC"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESCAE"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESDE"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESF"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESFS"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESJ"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESMF"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESMP"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESO"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESOF"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESOP"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESP"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESP64"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESP65"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESP128"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESP256"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESP512"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESP1024"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESP1519"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESUF"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryESUP"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryAUFD"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryAPFD"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryABRTx"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryATFD"),
        ("CM-PERFORMANCE-MIB", "cmLagHistoryLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsBR"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsFR"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryBR"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryFR"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsIndex"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsValid"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsAction"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineLBC"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineOPT"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineOPR"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineTemp"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLinePSC"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFCs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFarEndESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFarEndSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFarEndCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFarEndUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionSEFs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryTime"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryValid"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryAction"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineLBC"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineOPT"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineOPR"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineTemp"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLinePSC"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFCs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFarEndESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFarEndSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFarEndCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFarEndUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionSEFs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsIndex"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsValid"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsAction"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsSESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsCVs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsUASs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndStatsESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndStatsSESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndStatsCVs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndStatsUASs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryTime"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryValid"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryAction"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistorySESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryCVs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryUASs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndHistoryESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndHistorySESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndHistoryCVs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndHistoryUASs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsIndex"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsValid"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsAction"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsSESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsCVs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsUASs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndStatsESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndStatsSESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndStatsCVs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndStatsUASs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryTime"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryValid"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryAction"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistorySESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryCVs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryUASs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndHistoryESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndHistorySESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndHistoryCVs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndHistoryUASs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsIndex"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsValid"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsAction"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineCVs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineESs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineSESs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineUASs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineLOSSs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathCVs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathESs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathSESs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathUASs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathCVsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathSESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathSEFsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathUASsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathFCs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathFCsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathAISs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathSASs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryIndex"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryTime"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryValid"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryAction"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineCVs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineESs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineSESs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineUASs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineLOSSs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathCVs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathESs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathSESs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathUASs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathCVsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathSESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathSEFsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathUASsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathFCs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathFCsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathAISs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathSASs"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsIndex"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsValid"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsAction"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsLineCVs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsLineESs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsLineSESs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsLineLOSSs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathPCVs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCCVs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathAISs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathPESs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCESs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathFCs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathSEFs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathPSESs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCSESs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathPUASs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCUASs"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCCVsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCSESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCFCsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3StatsPathCUASsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryIndex"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryTime"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryValid"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryAction"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryLineCVs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryLineESs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryLineSESs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryLineLOSSs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathPCVs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCCVs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathAISs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathPESs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCESs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathFCs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathSEFs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathPSESs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCSESs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathPUASs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCUASs"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCCVsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCSESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCFCsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3HistoryPathCUASsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmPerfObjectGroup.setStatus("deprecated")

ethernetAccessPortPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 3)
)
ethernetAccessPortPMGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsL2PTRxFramesEncap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsL2PTTxFramesDecap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortStatsLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryL2PTRxFramesEncap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryL2PTTxFramesDecap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortHistoryLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdVarOprVariance"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdVarOptVariance"))
)
if mibBuilder.loadTexts:
    ethernetAccessPortPMGroup.setStatus("current")

ethernetNetworkPortPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 4)
)
ethernetNetworkPortPMGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsPSC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsL2PTRxFramesEncap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsL2PTTxFramesDecap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryPSC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryL2PTRxFramesEncap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryL2PTTxFramesDecap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdVarOprVariance"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdVarOptVariance"))
)
if mibBuilder.loadTexts:
    ethernetNetworkPortPMGroup.setStatus("current")

trafficPMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 5)
)
trafficPMGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmFlowStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsES"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsSES"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMGA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMRDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesInA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesOutA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMGN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMRDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesInN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesOutN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFTDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMCDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFBCDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryES"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistorySES"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMGA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMRDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesInA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesOutA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMGN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMRDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesInN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesOutN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFTDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMCDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFBCDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsABRRLR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryABRRLR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsFMG"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsFMY"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsFMYD"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsFMRD"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerStatsABR"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryFMG"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryFMY"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryFMYD"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryFMRD"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerHistoryABR"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsBR"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsFR"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryBR"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryFR"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsBR"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsFR"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryBR"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryFR"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    trafficPMGroup.setStatus("current")

trafficPMGroupCmHub = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 7)
)
trafficPMGroupCmHub.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmFlowStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsABRRLN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsES"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsSES"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMGA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMRDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesInA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesOutA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMGN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMYDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFMRDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesInN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsBytesOutN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsFTDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowStatsIBRRlN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryABRRLN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryES"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistorySES"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMGA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMRDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesInA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesOutA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMGN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMYDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFMRDN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesInN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryBytesOutN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryFTDA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2NMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2NMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlA2N"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2AMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2AMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowHistoryIBRRlN2A"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdMonValue"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsABRRLR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryABRRLR"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    trafficPMGroupCmHub.setStatus("current")

ocnStmPortPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 9)
)
ocnStmPortPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "ocnStmStatsIndex"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsValid"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsAction"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineLBC"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineOPT"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineOPR"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineTemp"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLinePSC"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFCs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFarEndESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFarEndSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFarEndCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsLineFarEndUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionSEFs"),
        ("CM-PERFORMANCE-MIB", "ocnStmStatsSectionUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryTime"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryValid"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryAction"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineLBC"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineOPT"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineOPR"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineTemp"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLinePSC"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFCs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFarEndESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFarEndSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFarEndCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistoryLineFarEndUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionSESs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionCVs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionSEFs"),
        ("CM-PERFORMANCE-MIB", "ocnStmHistorySectionUASs"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdMonValue"))
)
if mibBuilder.loadTexts:
    ocnStmPortPerfGroup.setStatus("current")

stsVcPathPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 10)
)
stsVcPathPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "stsVcPathStatsIndex"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsValid"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsAction"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsSESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsCVs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathStatsUASs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndStatsESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndStatsSESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndStatsCVs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndStatsUASs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryTime"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryValid"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryAction"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistorySESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryCVs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathHistoryUASs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndHistoryESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndHistorySESs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndHistoryCVs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathFarEndHistoryUASs"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdMonValue"))
)
if mibBuilder.loadTexts:
    stsVcPathPerfGroup.setStatus("current")

vtVcPathPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 11)
)
vtVcPathPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "vtVcPathStatsIndex"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsValid"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsAction"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsSESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsCVs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathStatsUASs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndStatsESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndStatsSESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndStatsCVs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndStatsUASs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryTime"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryValid"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryAction"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistorySESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryCVs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathHistoryUASs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndHistoryESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndHistorySESs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndHistoryCVs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathFarEndHistoryUASs"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdMonValue"))
)
if mibBuilder.loadTexts:
    vtVcPathPerfGroup.setStatus("current")

e1T1PerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 12)
)
e1T1PerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "e1t1StatsIndex"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsValid"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsAction"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineCVs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineESs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineSESs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineUASs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsLineLOSSs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathCVs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathESs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathSESs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathUASs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathCVsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathSESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathSEFsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathUASsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathFCs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathFCsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathAISs"),
        ("CM-PERFORMANCE-MIB", "e1t1StatsPathSASs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryIndex"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryTime"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryValid"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryAction"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineCVs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineESs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineSESs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineUASs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryLineLOSSs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathCVs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathESs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathSESs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathUASs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathCVsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathSESsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathSEFsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathUASsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathFCs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathFCsFarEnd"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathAISs"),
        ("CM-PERFORMANCE-MIB", "e1t1HistoryPathSASs"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdMonValue"))
)
if mibBuilder.loadTexts:
    e1T1PerfGroup.setStatus("current")

flowPointPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 13)
)
flowPointPmGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmFlowPointStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsABRRLRx"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsSES"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMG"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMY"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMRD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFTD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFACLD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMYD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMGD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFMCD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFBCD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsBT"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFLD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIBRMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIBRRlMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIBRMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIBRRlMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIBR"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsIBRRl"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFdRxFb"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFdTxFb"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsFdicd"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsNumLearnTableFlushes"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsEfFramesDiscarded"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsEfBytesDiscarded"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsAclDropNoMatch"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointStatsAclRuleDrop"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryABRRLRx"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistorySES"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMG"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMY"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMRD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryBytesIn"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryBytesOut"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFACLD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMYD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMGD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFMCD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFBCD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryBT"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFLD"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryIBRMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryIBRRlMax"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryIBRMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryIBRRlMin"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryIBR"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryIBRRl"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFdRxFb"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFdTxFb"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryFdicd"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryNumLearnTableFlushes"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryEfFramesDiscarded"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryEfBytesDiscarded"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryAclDropNoMatch"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointHistoryAclRuleDrop"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    flowPointPmGroup.setStatus("current")

cmFlowBWPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 14)
)
cmFlowBWPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmFlowBWA2NCIR"),
        ("CM-PERFORMANCE-MIB", "cmFlowBWA2NEIR"),
        ("CM-PERFORMANCE-MIB", "cmFlowBWN2ACIR"),
        ("CM-PERFORMANCE-MIB", "cmFlowBWN2AEIR"),
        ("CM-PERFORMANCE-MIB", "cmFlowBWA2NGFB"),
        ("CM-PERFORMANCE-MIB", "cmFlowBWA2NMFB"))
)
if mibBuilder.loadTexts:
    cmFlowBWPerfGroup.setStatus("current")

ocnStmThresholdVarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 15)
)
ocnStmThresholdVarGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "ocnStmThresholdVarOprVariance"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdVarOptVariance"))
)
if mibBuilder.loadTexts:
    ocnStmThresholdVarGroup.setStatus("current")

f3FpQosShaperPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 16)
)
f3FpQosShaperPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsIndex"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsValid"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsAction"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsBT"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsBTD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsFD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsFTD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsABRRL"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsBREDD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperStatsFREDD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryTime"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryValid"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryAction"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryBT"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryBTD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryFD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryFTD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryABRRL"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryBREDD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperHistoryFREDD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3FpQosShaperPerfGroup.setStatus("current")

f3FpQosPolicerPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 17)
)
f3FpQosPolicerPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsIndex"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsValid"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsAction"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsFMG"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsFMY"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsFMRD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsBytesIn"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsBytesOut"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerStatsABR"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryTime"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryValid"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryAction"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryFMG"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryFMY"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryFMRD"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryBytesIn"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryBytesOut"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerHistoryABR"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3FpQosPolicerPerfGroup.setStatus("current")

cmEthernetTrafficPortPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 18)
)
cmEthernetTrafficPortPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsATFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsL2PTRxFramesEncap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsL2PTTxFramesDecap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsFmcd"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsFbcd"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAclDropNoMatch"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsAclFwd2Cpu"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsDhcpDropNoAssocIf"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsDroppedFragmented"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsRLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsROPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsROPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortStatsRTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryTime"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryValid"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAction"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESBF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESBP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESBS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESCAE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESDE"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESFS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESJ"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESMF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESMP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESO"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESOF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESOP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP64"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP65"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP128"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP256"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP512"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP1024"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESP1519"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESUF"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryESUP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryL2CPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryL2CPFP"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryLES"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryOPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryOPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAUFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAPFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryABRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryABRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryATFD"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryUAS"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryLkupFails"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryL2PTRxFramesEncap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryL2PTTxFramesDecap"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRMaxRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRMaxTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRMinRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRMinTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRRx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryIBRTx"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryFmcd"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryFbcd"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAclDropNoMatch"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryAclFwd2Cpu"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryDhcpDropNoAssocIf"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryDroppedFragmented"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryRLBC"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryROPT"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryROPR"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortHistoryRTemp"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortPerfGroup.setStatus("current")

f3AclRulePerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 19)
)
f3AclRulePerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3AclRuleStatsIndex"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleStatsValid"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleStatsAction"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleStatsRuleMatch"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleHistoryTime"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleHistoryValid"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleHistoryAction"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleHistoryRuleMatch"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3AclRulePerfGroup.setStatus("current")

cmEthernetNetPortXdslPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 21)
)
cmEthernetNetPortXdslPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsPkt"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsCrcError"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsPkt"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsFecs"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsFecs"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsEs"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsEs"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsSes"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsSes"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsLoss"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsLoss"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsUas"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsCv"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsCv"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsFec"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsFec"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslDsFullInits"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsXdslUsFullInits"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsPkt"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsCrcError"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsPkt"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsFecs"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsFecs"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsEs"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsEs"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsSes"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsSes"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsLoss"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsLoss"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsUas"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsCv"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsCv"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsFec"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsFec"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslDsFullInits"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryXdslUsFullInits"))
)
if mibBuilder.loadTexts:
    cmEthernetNetPortXdslPerfGroup.setStatus("current")

f3CardPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 22)
)
f3CardPerfGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3CardStatsIndex"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsIntervalType"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsValid"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsAction"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsACU"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsMCU"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsICU"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsAMU"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsMMU"),
        ("CM-PERFORMANCE-MIB", "f3CardStatsIMU"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryIndex"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryTime"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryValid"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryAction"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryACU"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryMCU"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryICU"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryAMU"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryMMU"),
        ("CM-PERFORMANCE-MIB", "f3CardHistoryIMU"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3CardPerfGroup.setStatus("current")


# Notification objects

cmEthernetAccPortThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 1)
)
cmEthernetAccPortThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmEthernetAccPortThresholdCrossingAlert.setStatus(
        "current"
    )

cmEthernetNetPortThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 2)
)
cmEthernetNetPortThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmEthernetNetPortThresholdCrossingAlert.setStatus(
        "current"
    )

cmFlowThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 3)
)
cmFlowThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmFlowThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmFlowThresholdCrossingAlert.setStatus(
        "current"
    )

cmQosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 4)
)
cmQosShaperThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmQosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

cmQosFlowPolicerThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 5)
)
cmQosFlowPolicerThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmQosFlowPolicerThresholdCrossingAlert.setStatus(
        "current"
    )

cmAccPortQosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 6)
)
cmAccPortQosShaperThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmAccPortQosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

cmEthernetTrafficPortThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 7)
)
cmEthernetTrafficPortThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmEthernetTrafficPortThresholdCrossingAlert.setStatus(
        "current"
    )

cmFlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 8)
)
cmFlowPointThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmFlowPointThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmFlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

cmOAMFlowPointThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 9)
)
cmOAMFlowPointThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmOAMFlowPointThresholdCrossingAlert.setStatus(
        "current"
    )

cmQosPolicerV2ThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 10)
)
cmQosPolicerV2ThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmQosPolicerV2ThresholdCrossingAlert.setStatus(
        "current"
    )

cmQosShaperV2ThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 11)
)
cmQosShaperV2ThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmQosShaperV2ThresholdCrossingAlert.setStatus(
        "current"
    )

cmLagThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 12)
)
cmLagThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmLagThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmLagThresholdCrossingAlert.setStatus(
        "current"
    )

cmTrafficPortQosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 13)
)
cmTrafficPortQosShaperThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    cmTrafficPortQosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

f3NetPortQosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 14)
)
f3NetPortQosShaperThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3NetPortQosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

ocnStmThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 15)
)
ocnStmThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "ocnStmThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdMonValue"))
)
if mibBuilder.loadTexts:
    ocnStmThresholdCrossingAlert.setStatus(
        "current"
    )

stsVcPathThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 16)
)
stsVcPathThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "stsVcPathThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdMonValue"))
)
if mibBuilder.loadTexts:
    stsVcPathThresholdCrossingAlert.setStatus(
        "current"
    )

vtVcPathThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 17)
)
vtVcPathThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "vtVcPathThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdMonValue"))
)
if mibBuilder.loadTexts:
    vtVcPathThresholdCrossingAlert.setStatus(
        "current"
    )

e1t1ThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 18)
)
e1t1ThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "e1t1ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdMonValue"))
)
if mibBuilder.loadTexts:
    e1t1ThresholdCrossingAlert.setStatus(
        "current"
    )

e3t3ThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 19)
)
e3t3ThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "e3t3ThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdMonValue"))
)
if mibBuilder.loadTexts:
    e3t3ThresholdCrossingAlert.setStatus(
        "current"
    )

cmPerQueryGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 20)
)
if mibBuilder.loadTexts:
    cmPerQueryGenTrap.setStatus(
        "current"
    )

f3FpQosShaperThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 21)
)
f3FpQosShaperThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3FpQosShaperThresholdCrossingAlert.setStatus(
        "current"
    )

f3FpQosPolicerThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 22)
)
f3FpQosPolicerThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3FpQosPolicerThresholdCrossingAlert.setStatus(
        "current"
    )

f3AclRuleThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 23)
)
f3AclRuleThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3AclRuleThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3AclRuleThresholdCrossingAlert.setStatus(
        "current"
    )

f3CardThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 2, 24)
)
f3CardThresholdCrossingAlert.setObjects(
      *(("CM-PERFORMANCE-MIB", "f3CardThresholdIndex"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdInterval"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdVariable"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdValueLo"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdValueHi"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdMonValue"))
)
if mibBuilder.loadTexts:
    f3CardThresholdCrossingAlert.setStatus(
        "current"
    )


# Notifications groups

cmPerfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 2)
)
cmPerfNotifGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmQosFlowPolicerThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmAccPortQosShaperThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "f3NetPortQosShaperThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "f3CardThresholdCrossingAlert"))
)
if mibBuilder.loadTexts:
    cmPerfNotifGroup.setStatus(
        "current"
    )

cmEGXPerfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 6)
)
cmEGXPerfNotifGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmQosPolicerV2ThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperV2ThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmLagThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmOAMFlowPointThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmTrafficPortQosShaperThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "ocnStmThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "stsVcPathThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "vtVcPathThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "e1t1ThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "e3t3ThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmPerQueryGenControl"),
        ("CM-PERFORMANCE-MIB", "cmPerQueryGenTrap"))
)
if mibBuilder.loadTexts:
    cmEGXPerfNotifGroup.setStatus(
        "current"
    )

cmPerfNotifGroupCmHub = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 8)
)
cmPerfNotifGroupCmHub.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetAccPortThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmEthernetNetPortThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmFlowThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmQosShaperThresholdCrossingAlert"))
)
if mibBuilder.loadTexts:
    cmPerfNotifGroupCmHub.setStatus(
        "current"
    )

cmXgProPerfNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 2, 20)
)
cmXgProPerfNotifGroup.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmEthernetTrafficPortThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "cmFlowPointThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "f3FpQosShaperThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "f3FpQosPolicerThresholdCrossingAlert"),
        ("CM-PERFORMANCE-MIB", "f3AclRuleThresholdCrossingAlert"))
)
if mibBuilder.loadTexts:
    cmXgProPerfNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmPerfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 5, 3, 1, 1)
)
cmPerfCompliance.setObjects(
      *(("CM-PERFORMANCE-MIB", "cmPerfObjectGroup"),
        ("CM-PERFORMANCE-MIB", "cmPerfNotifGroup"),
        ("CM-PERFORMANCE-MIB", "ethernetAccessPortPMGroup"),
        ("CM-PERFORMANCE-MIB", "ethernetNetworkPortPMGroup"),
        ("CM-PERFORMANCE-MIB", "trafficPMGroup"),
        ("CM-PERFORMANCE-MIB", "f3AclRulePerfGroup"))
)
if mibBuilder.loadTexts:
    cmPerfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-PERFORMANCE-MIB",
    **{"cmPerformanceMIB": cmPerformanceMIB,
       "cmPerfObjects": cmPerfObjects,
       "cmEthernetAccPortStatsTable": cmEthernetAccPortStatsTable,
       "cmEthernetAccPortStatsEntry": cmEthernetAccPortStatsEntry,
       "cmEthernetAccPortStatsIndex": cmEthernetAccPortStatsIndex,
       "cmEthernetAccPortStatsIntervalType": cmEthernetAccPortStatsIntervalType,
       "cmEthernetAccPortStatsValid": cmEthernetAccPortStatsValid,
       "cmEthernetAccPortStatsAction": cmEthernetAccPortStatsAction,
       "cmEthernetAccPortStatsESBF": cmEthernetAccPortStatsESBF,
       "cmEthernetAccPortStatsESBP": cmEthernetAccPortStatsESBP,
       "cmEthernetAccPortStatsESBS": cmEthernetAccPortStatsESBS,
       "cmEthernetAccPortStatsESC": cmEthernetAccPortStatsESC,
       "cmEthernetAccPortStatsESCAE": cmEthernetAccPortStatsESCAE,
       "cmEthernetAccPortStatsESDE": cmEthernetAccPortStatsESDE,
       "cmEthernetAccPortStatsESF": cmEthernetAccPortStatsESF,
       "cmEthernetAccPortStatsESFS": cmEthernetAccPortStatsESFS,
       "cmEthernetAccPortStatsESJ": cmEthernetAccPortStatsESJ,
       "cmEthernetAccPortStatsESMF": cmEthernetAccPortStatsESMF,
       "cmEthernetAccPortStatsESMP": cmEthernetAccPortStatsESMP,
       "cmEthernetAccPortStatsESO": cmEthernetAccPortStatsESO,
       "cmEthernetAccPortStatsESOF": cmEthernetAccPortStatsESOF,
       "cmEthernetAccPortStatsESOP": cmEthernetAccPortStatsESOP,
       "cmEthernetAccPortStatsESP": cmEthernetAccPortStatsESP,
       "cmEthernetAccPortStatsESP64": cmEthernetAccPortStatsESP64,
       "cmEthernetAccPortStatsESP65": cmEthernetAccPortStatsESP65,
       "cmEthernetAccPortStatsESP128": cmEthernetAccPortStatsESP128,
       "cmEthernetAccPortStatsESP256": cmEthernetAccPortStatsESP256,
       "cmEthernetAccPortStatsESP512": cmEthernetAccPortStatsESP512,
       "cmEthernetAccPortStatsESP1024": cmEthernetAccPortStatsESP1024,
       "cmEthernetAccPortStatsESP1519": cmEthernetAccPortStatsESP1519,
       "cmEthernetAccPortStatsESUF": cmEthernetAccPortStatsESUF,
       "cmEthernetAccPortStatsESUP": cmEthernetAccPortStatsESUP,
       "cmEthernetAccPortStatsL2CPFD": cmEthernetAccPortStatsL2CPFD,
       "cmEthernetAccPortStatsL2CPFP": cmEthernetAccPortStatsL2CPFP,
       "cmEthernetAccPortStatsLES": cmEthernetAccPortStatsLES,
       "cmEthernetAccPortStatsLBC": cmEthernetAccPortStatsLBC,
       "cmEthernetAccPortStatsOPT": cmEthernetAccPortStatsOPT,
       "cmEthernetAccPortStatsOPR": cmEthernetAccPortStatsOPR,
       "cmEthernetAccPortStatsAUFD": cmEthernetAccPortStatsAUFD,
       "cmEthernetAccPortStatsAPFD": cmEthernetAccPortStatsAPFD,
       "cmEthernetAccPortStatsABRRx": cmEthernetAccPortStatsABRRx,
       "cmEthernetAccPortStatsABRTx": cmEthernetAccPortStatsABRTx,
       "cmEthernetAccPortStatsTemp": cmEthernetAccPortStatsTemp,
       "cmEthernetAccPortStatsUAS": cmEthernetAccPortStatsUAS,
       "cmEthernetAccPortStatsL2PTRxFramesEncap": cmEthernetAccPortStatsL2PTRxFramesEncap,
       "cmEthernetAccPortStatsL2PTTxFramesDecap": cmEthernetAccPortStatsL2PTTxFramesDecap,
       "cmEthernetAccPortStatsIBRMaxRx": cmEthernetAccPortStatsIBRMaxRx,
       "cmEthernetAccPortStatsIBRMaxTx": cmEthernetAccPortStatsIBRMaxTx,
       "cmEthernetAccPortStatsIBRMinRx": cmEthernetAccPortStatsIBRMinRx,
       "cmEthernetAccPortStatsIBRMinTx": cmEthernetAccPortStatsIBRMinTx,
       "cmEthernetAccPortStatsIBRRx": cmEthernetAccPortStatsIBRRx,
       "cmEthernetAccPortStatsIBRTx": cmEthernetAccPortStatsIBRTx,
       "cmEthernetAccPortStatsFmcd": cmEthernetAccPortStatsFmcd,
       "cmEthernetAccPortStatsFbcd": cmEthernetAccPortStatsFbcd,
       "cmEthernetAccPortStatsAclDropNoMatch": cmEthernetAccPortStatsAclDropNoMatch,
       "cmEthernetAccPortStatsAclFwd2Cpu": cmEthernetAccPortStatsAclFwd2Cpu,
       "cmEthernetAccPortStatsDhcpDropNoAssocIf": cmEthernetAccPortStatsDhcpDropNoAssocIf,
       "cmEthernetAccPortStatsLkupFails": cmEthernetAccPortStatsLkupFails,
       "cmEthernetAccPortHistoryTable": cmEthernetAccPortHistoryTable,
       "cmEthernetAccPortHistoryEntry": cmEthernetAccPortHistoryEntry,
       "cmEthernetAccPortHistoryIndex": cmEthernetAccPortHistoryIndex,
       "cmEthernetAccPortHistoryTime": cmEthernetAccPortHistoryTime,
       "cmEthernetAccPortHistoryValid": cmEthernetAccPortHistoryValid,
       "cmEthernetAccPortHistoryAction": cmEthernetAccPortHistoryAction,
       "cmEthernetAccPortHistoryESBF": cmEthernetAccPortHistoryESBF,
       "cmEthernetAccPortHistoryESBP": cmEthernetAccPortHistoryESBP,
       "cmEthernetAccPortHistoryESBS": cmEthernetAccPortHistoryESBS,
       "cmEthernetAccPortHistoryESC": cmEthernetAccPortHistoryESC,
       "cmEthernetAccPortHistoryESCAE": cmEthernetAccPortHistoryESCAE,
       "cmEthernetAccPortHistoryESDE": cmEthernetAccPortHistoryESDE,
       "cmEthernetAccPortHistoryESF": cmEthernetAccPortHistoryESF,
       "cmEthernetAccPortHistoryESFS": cmEthernetAccPortHistoryESFS,
       "cmEthernetAccPortHistoryESJ": cmEthernetAccPortHistoryESJ,
       "cmEthernetAccPortHistoryESMF": cmEthernetAccPortHistoryESMF,
       "cmEthernetAccPortHistoryESMP": cmEthernetAccPortHistoryESMP,
       "cmEthernetAccPortHistoryESO": cmEthernetAccPortHistoryESO,
       "cmEthernetAccPortHistoryESOF": cmEthernetAccPortHistoryESOF,
       "cmEthernetAccPortHistoryESOP": cmEthernetAccPortHistoryESOP,
       "cmEthernetAccPortHistoryESP": cmEthernetAccPortHistoryESP,
       "cmEthernetAccPortHistoryESP64": cmEthernetAccPortHistoryESP64,
       "cmEthernetAccPortHistoryESP65": cmEthernetAccPortHistoryESP65,
       "cmEthernetAccPortHistoryESP128": cmEthernetAccPortHistoryESP128,
       "cmEthernetAccPortHistoryESP256": cmEthernetAccPortHistoryESP256,
       "cmEthernetAccPortHistoryESP512": cmEthernetAccPortHistoryESP512,
       "cmEthernetAccPortHistoryESP1024": cmEthernetAccPortHistoryESP1024,
       "cmEthernetAccPortHistoryESP1519": cmEthernetAccPortHistoryESP1519,
       "cmEthernetAccPortHistoryESUF": cmEthernetAccPortHistoryESUF,
       "cmEthernetAccPortHistoryESUP": cmEthernetAccPortHistoryESUP,
       "cmEthernetAccPortHistoryL2CPFD": cmEthernetAccPortHistoryL2CPFD,
       "cmEthernetAccPortHistoryL2CPFP": cmEthernetAccPortHistoryL2CPFP,
       "cmEthernetAccPortHistoryLES": cmEthernetAccPortHistoryLES,
       "cmEthernetAccPortHistoryLBC": cmEthernetAccPortHistoryLBC,
       "cmEthernetAccPortHistoryOPT": cmEthernetAccPortHistoryOPT,
       "cmEthernetAccPortHistoryOPR": cmEthernetAccPortHistoryOPR,
       "cmEthernetAccPortHistoryAUFD": cmEthernetAccPortHistoryAUFD,
       "cmEthernetAccPortHistoryAPFD": cmEthernetAccPortHistoryAPFD,
       "cmEthernetAccPortHistoryABRRx": cmEthernetAccPortHistoryABRRx,
       "cmEthernetAccPortHistoryABRTx": cmEthernetAccPortHistoryABRTx,
       "cmEthernetAccPortHistoryTemp": cmEthernetAccPortHistoryTemp,
       "cmEthernetAccPortHistoryUAS": cmEthernetAccPortHistoryUAS,
       "cmEthernetAccPortHistoryL2PTRxFramesEncap": cmEthernetAccPortHistoryL2PTRxFramesEncap,
       "cmEthernetAccPortHistoryL2PTTxFramesDecap": cmEthernetAccPortHistoryL2PTTxFramesDecap,
       "cmEthernetAccPortHistoryIBRMaxRx": cmEthernetAccPortHistoryIBRMaxRx,
       "cmEthernetAccPortHistoryIBRMaxTx": cmEthernetAccPortHistoryIBRMaxTx,
       "cmEthernetAccPortHistoryIBRMinRx": cmEthernetAccPortHistoryIBRMinRx,
       "cmEthernetAccPortHistoryIBRMinTx": cmEthernetAccPortHistoryIBRMinTx,
       "cmEthernetAccPortHistoryIBRRx": cmEthernetAccPortHistoryIBRRx,
       "cmEthernetAccPortHistoryIBRTx": cmEthernetAccPortHistoryIBRTx,
       "cmEthernetAccPortHistoryFmcd": cmEthernetAccPortHistoryFmcd,
       "cmEthernetAccPortHistoryFbcd": cmEthernetAccPortHistoryFbcd,
       "cmEthernetAccPortHistoryAclDropNoMatch": cmEthernetAccPortHistoryAclDropNoMatch,
       "cmEthernetAccPortHistoryAclFwd2Cpu": cmEthernetAccPortHistoryAclFwd2Cpu,
       "cmEthernetAccPortHistoryDhcpDropNoAssocIf": cmEthernetAccPortHistoryDhcpDropNoAssocIf,
       "cmEthernetAccPortHistoryLkupFails": cmEthernetAccPortHistoryLkupFails,
       "cmEthernetAccPortThresholdTable": cmEthernetAccPortThresholdTable,
       "cmEthernetAccPortThresholdEntry": cmEthernetAccPortThresholdEntry,
       "cmEthernetAccPortThresholdIndex": cmEthernetAccPortThresholdIndex,
       "cmEthernetAccPortThresholdInterval": cmEthernetAccPortThresholdInterval,
       "cmEthernetAccPortThresholdVariable": cmEthernetAccPortThresholdVariable,
       "cmEthernetAccPortThresholdValueLo": cmEthernetAccPortThresholdValueLo,
       "cmEthernetAccPortThresholdValueHi": cmEthernetAccPortThresholdValueHi,
       "cmEthernetAccPortThresholdMonValue": cmEthernetAccPortThresholdMonValue,
       "cmEthernetAccPortThresholdVarTable": cmEthernetAccPortThresholdVarTable,
       "cmEthernetAccPortThresholdVarEntry": cmEthernetAccPortThresholdVarEntry,
       "cmEthernetAccPortThresholdVarOprVariance": cmEthernetAccPortThresholdVarOprVariance,
       "cmEthernetAccPortThresholdVarOptVariance": cmEthernetAccPortThresholdVarOptVariance,
       "cmEthernetNetPortStatsTable": cmEthernetNetPortStatsTable,
       "cmEthernetNetPortStatsEntry": cmEthernetNetPortStatsEntry,
       "cmEthernetNetPortStatsIndex": cmEthernetNetPortStatsIndex,
       "cmEthernetNetPortStatsIntervalType": cmEthernetNetPortStatsIntervalType,
       "cmEthernetNetPortStatsValid": cmEthernetNetPortStatsValid,
       "cmEthernetNetPortStatsAction": cmEthernetNetPortStatsAction,
       "cmEthernetNetPortStatsESBF": cmEthernetNetPortStatsESBF,
       "cmEthernetNetPortStatsESBP": cmEthernetNetPortStatsESBP,
       "cmEthernetNetPortStatsESBS": cmEthernetNetPortStatsESBS,
       "cmEthernetNetPortStatsESC": cmEthernetNetPortStatsESC,
       "cmEthernetNetPortStatsESCAE": cmEthernetNetPortStatsESCAE,
       "cmEthernetNetPortStatsESDE": cmEthernetNetPortStatsESDE,
       "cmEthernetNetPortStatsESF": cmEthernetNetPortStatsESF,
       "cmEthernetNetPortStatsESFS": cmEthernetNetPortStatsESFS,
       "cmEthernetNetPortStatsESJ": cmEthernetNetPortStatsESJ,
       "cmEthernetNetPortStatsESMF": cmEthernetNetPortStatsESMF,
       "cmEthernetNetPortStatsESMP": cmEthernetNetPortStatsESMP,
       "cmEthernetNetPortStatsESO": cmEthernetNetPortStatsESO,
       "cmEthernetNetPortStatsESOF": cmEthernetNetPortStatsESOF,
       "cmEthernetNetPortStatsESOP": cmEthernetNetPortStatsESOP,
       "cmEthernetNetPortStatsESP": cmEthernetNetPortStatsESP,
       "cmEthernetNetPortStatsESP64": cmEthernetNetPortStatsESP64,
       "cmEthernetNetPortStatsESP65": cmEthernetNetPortStatsESP65,
       "cmEthernetNetPortStatsESP128": cmEthernetNetPortStatsESP128,
       "cmEthernetNetPortStatsESP256": cmEthernetNetPortStatsESP256,
       "cmEthernetNetPortStatsESP512": cmEthernetNetPortStatsESP512,
       "cmEthernetNetPortStatsESP1024": cmEthernetNetPortStatsESP1024,
       "cmEthernetNetPortStatsESP1519": cmEthernetNetPortStatsESP1519,
       "cmEthernetNetPortStatsESUF": cmEthernetNetPortStatsESUF,
       "cmEthernetNetPortStatsESUP": cmEthernetNetPortStatsESUP,
       "cmEthernetNetPortStatsL2CPFD": cmEthernetNetPortStatsL2CPFD,
       "cmEthernetNetPortStatsL2CPFP": cmEthernetNetPortStatsL2CPFP,
       "cmEthernetNetPortStatsLES": cmEthernetNetPortStatsLES,
       "cmEthernetNetPortStatsLBC": cmEthernetNetPortStatsLBC,
       "cmEthernetNetPortStatsOPT": cmEthernetNetPortStatsOPT,
       "cmEthernetNetPortStatsOPR": cmEthernetNetPortStatsOPR,
       "cmEthernetNetPortStatsAUFD": cmEthernetNetPortStatsAUFD,
       "cmEthernetNetPortStatsAPFD": cmEthernetNetPortStatsAPFD,
       "cmEthernetNetPortStatsABRRx": cmEthernetNetPortStatsABRRx,
       "cmEthernetNetPortStatsABRTx": cmEthernetNetPortStatsABRTx,
       "cmEthernetNetPortStatsPSC": cmEthernetNetPortStatsPSC,
       "cmEthernetNetPortStatsTemp": cmEthernetNetPortStatsTemp,
       "cmEthernetNetPortStatsUAS": cmEthernetNetPortStatsUAS,
       "cmEthernetNetPortStatsL2PTRxFramesEncap": cmEthernetNetPortStatsL2PTRxFramesEncap,
       "cmEthernetNetPortStatsL2PTTxFramesDecap": cmEthernetNetPortStatsL2PTTxFramesDecap,
       "cmEthernetNetPortStatsIBRMaxRx": cmEthernetNetPortStatsIBRMaxRx,
       "cmEthernetNetPortStatsIBRMaxTx": cmEthernetNetPortStatsIBRMaxTx,
       "cmEthernetNetPortStatsIBRMinRx": cmEthernetNetPortStatsIBRMinRx,
       "cmEthernetNetPortStatsIBRMinTx": cmEthernetNetPortStatsIBRMinTx,
       "cmEthernetNetPortStatsIBRRx": cmEthernetNetPortStatsIBRRx,
       "cmEthernetNetPortStatsIBRTx": cmEthernetNetPortStatsIBRTx,
       "cmEthernetNetPortStatsFmcd": cmEthernetNetPortStatsFmcd,
       "cmEthernetNetPortStatsFbcd": cmEthernetNetPortStatsFbcd,
       "cmEthernetNetPortStatsAclDropNoMatch": cmEthernetNetPortStatsAclDropNoMatch,
       "cmEthernetNetPortStatsAclFwd2Cpu": cmEthernetNetPortStatsAclFwd2Cpu,
       "cmEthernetNetPortStatsDhcpDropNoAssocIf": cmEthernetNetPortStatsDhcpDropNoAssocIf,
       "cmEthernetNetPortStatsLkupFails": cmEthernetNetPortStatsLkupFails,
       "cmEthernetNetPortHistoryTable": cmEthernetNetPortHistoryTable,
       "cmEthernetNetPortHistoryEntry": cmEthernetNetPortHistoryEntry,
       "cmEthernetNetPortHistoryIndex": cmEthernetNetPortHistoryIndex,
       "cmEthernetNetPortHistoryTime": cmEthernetNetPortHistoryTime,
       "cmEthernetNetPortHistoryValid": cmEthernetNetPortHistoryValid,
       "cmEthernetNetPortHistoryAction": cmEthernetNetPortHistoryAction,
       "cmEthernetNetPortHistoryESBF": cmEthernetNetPortHistoryESBF,
       "cmEthernetNetPortHistoryESBP": cmEthernetNetPortHistoryESBP,
       "cmEthernetNetPortHistoryESBS": cmEthernetNetPortHistoryESBS,
       "cmEthernetNetPortHistoryESC": cmEthernetNetPortHistoryESC,
       "cmEthernetNetPortHistoryESCAE": cmEthernetNetPortHistoryESCAE,
       "cmEthernetNetPortHistoryESDE": cmEthernetNetPortHistoryESDE,
       "cmEthernetNetPortHistoryESF": cmEthernetNetPortHistoryESF,
       "cmEthernetNetPortHistoryESFS": cmEthernetNetPortHistoryESFS,
       "cmEthernetNetPortHistoryESJ": cmEthernetNetPortHistoryESJ,
       "cmEthernetNetPortHistoryESMF": cmEthernetNetPortHistoryESMF,
       "cmEthernetNetPortHistoryESMP": cmEthernetNetPortHistoryESMP,
       "cmEthernetNetPortHistoryESO": cmEthernetNetPortHistoryESO,
       "cmEthernetNetPortHistoryESOF": cmEthernetNetPortHistoryESOF,
       "cmEthernetNetPortHistoryESOP": cmEthernetNetPortHistoryESOP,
       "cmEthernetNetPortHistoryESP": cmEthernetNetPortHistoryESP,
       "cmEthernetNetPortHistoryESP64": cmEthernetNetPortHistoryESP64,
       "cmEthernetNetPortHistoryESP65": cmEthernetNetPortHistoryESP65,
       "cmEthernetNetPortHistoryESP128": cmEthernetNetPortHistoryESP128,
       "cmEthernetNetPortHistoryESP256": cmEthernetNetPortHistoryESP256,
       "cmEthernetNetPortHistoryESP512": cmEthernetNetPortHistoryESP512,
       "cmEthernetNetPortHistoryESP1024": cmEthernetNetPortHistoryESP1024,
       "cmEthernetNetPortHistoryESP1519": cmEthernetNetPortHistoryESP1519,
       "cmEthernetNetPortHistoryESUF": cmEthernetNetPortHistoryESUF,
       "cmEthernetNetPortHistoryESUP": cmEthernetNetPortHistoryESUP,
       "cmEthernetNetPortHistoryL2CPFD": cmEthernetNetPortHistoryL2CPFD,
       "cmEthernetNetPortHistoryL2CPFP": cmEthernetNetPortHistoryL2CPFP,
       "cmEthernetNetPortHistoryLES": cmEthernetNetPortHistoryLES,
       "cmEthernetNetPortHistoryLBC": cmEthernetNetPortHistoryLBC,
       "cmEthernetNetPortHistoryOPT": cmEthernetNetPortHistoryOPT,
       "cmEthernetNetPortHistoryOPR": cmEthernetNetPortHistoryOPR,
       "cmEthernetNetPortHistoryAUFD": cmEthernetNetPortHistoryAUFD,
       "cmEthernetNetPortHistoryAPFD": cmEthernetNetPortHistoryAPFD,
       "cmEthernetNetPortHistoryABRRx": cmEthernetNetPortHistoryABRRx,
       "cmEthernetNetPortHistoryABRTx": cmEthernetNetPortHistoryABRTx,
       "cmEthernetNetPortHistoryPSC": cmEthernetNetPortHistoryPSC,
       "cmEthernetNetPortHistoryTemp": cmEthernetNetPortHistoryTemp,
       "cmEthernetNetPortHistoryUAS": cmEthernetNetPortHistoryUAS,
       "cmEthernetNetPortHistoryL2PTRxFramesEncap": cmEthernetNetPortHistoryL2PTRxFramesEncap,
       "cmEthernetNetPortHistoryL2PTTxFramesDecap": cmEthernetNetPortHistoryL2PTTxFramesDecap,
       "cmEthernetNetPortHistoryIBRMaxRx": cmEthernetNetPortHistoryIBRMaxRx,
       "cmEthernetNetPortHistoryIBRMaxTx": cmEthernetNetPortHistoryIBRMaxTx,
       "cmEthernetNetPortHistoryIBRMinRx": cmEthernetNetPortHistoryIBRMinRx,
       "cmEthernetNetPortHistoryIBRMinTx": cmEthernetNetPortHistoryIBRMinTx,
       "cmEthernetNetPortHistoryIBRRx": cmEthernetNetPortHistoryIBRRx,
       "cmEthernetNetPortHistoryIBRTx": cmEthernetNetPortHistoryIBRTx,
       "cmEthernetNetPortHistoryFmcd": cmEthernetNetPortHistoryFmcd,
       "cmEthernetNetPortHistoryFbcd": cmEthernetNetPortHistoryFbcd,
       "cmEthernetNetPortHistoryAclDropNoMatch": cmEthernetNetPortHistoryAclDropNoMatch,
       "cmEthernetNetPortHistoryAclFwd2Cpu": cmEthernetNetPortHistoryAclFwd2Cpu,
       "cmEthernetNetPortHistoryDhcpDropNoAssocIf": cmEthernetNetPortHistoryDhcpDropNoAssocIf,
       "cmEthernetNetPortHistoryLkupFails": cmEthernetNetPortHistoryLkupFails,
       "cmEthernetNetPortThresholdTable": cmEthernetNetPortThresholdTable,
       "cmEthernetNetPortThresholdEntry": cmEthernetNetPortThresholdEntry,
       "cmEthernetNetPortThresholdIndex": cmEthernetNetPortThresholdIndex,
       "cmEthernetNetPortThresholdInterval": cmEthernetNetPortThresholdInterval,
       "cmEthernetNetPortThresholdVariable": cmEthernetNetPortThresholdVariable,
       "cmEthernetNetPortThresholdValueLo": cmEthernetNetPortThresholdValueLo,
       "cmEthernetNetPortThresholdValueHi": cmEthernetNetPortThresholdValueHi,
       "cmEthernetNetPortThresholdMonValue": cmEthernetNetPortThresholdMonValue,
       "cmEthernetNetPortThresholdVarTable": cmEthernetNetPortThresholdVarTable,
       "cmEthernetNetPortThresholdVarEntry": cmEthernetNetPortThresholdVarEntry,
       "cmEthernetNetPortThresholdVarOprVariance": cmEthernetNetPortThresholdVarOprVariance,
       "cmEthernetNetPortThresholdVarOptVariance": cmEthernetNetPortThresholdVarOptVariance,
       "cmFlowStatsTable": cmFlowStatsTable,
       "cmFlowStatsEntry": cmFlowStatsEntry,
       "cmFlowStatsIndex": cmFlowStatsIndex,
       "cmFlowStatsIntervalType": cmFlowStatsIntervalType,
       "cmFlowStatsValid": cmFlowStatsValid,
       "cmFlowStatsAction": cmFlowStatsAction,
       "cmFlowStatsL2CPFD": cmFlowStatsL2CPFD,
       "cmFlowStatsABRA2N": cmFlowStatsABRA2N,
       "cmFlowStatsABRRLA2N": cmFlowStatsABRRLA2N,
       "cmFlowStatsABRRLRA2N": cmFlowStatsABRRLRA2N,
       "cmFlowStatsABRN2A": cmFlowStatsABRN2A,
       "cmFlowStatsABRRLN2A": cmFlowStatsABRRLN2A,
       "cmFlowStatsUAS": cmFlowStatsUAS,
       "cmFlowStatsES": cmFlowStatsES,
       "cmFlowStatsSES": cmFlowStatsSES,
       "cmFlowStatsFMGA2N": cmFlowStatsFMGA2N,
       "cmFlowStatsFMYA2N": cmFlowStatsFMYA2N,
       "cmFlowStatsFMYDA2N": cmFlowStatsFMYDA2N,
       "cmFlowStatsFMRDA2N": cmFlowStatsFMRDA2N,
       "cmFlowStatsBytesInA2N": cmFlowStatsBytesInA2N,
       "cmFlowStatsBytesOutA2N": cmFlowStatsBytesOutA2N,
       "cmFlowStatsFMGN2A": cmFlowStatsFMGN2A,
       "cmFlowStatsFMYN2A": cmFlowStatsFMYN2A,
       "cmFlowStatsFMYDN2A": cmFlowStatsFMYDN2A,
       "cmFlowStatsFMRDN2A": cmFlowStatsFMRDN2A,
       "cmFlowStatsBytesInN2A": cmFlowStatsBytesInN2A,
       "cmFlowStatsBytesOutN2A": cmFlowStatsBytesOutN2A,
       "cmFlowStatsFTDA2N": cmFlowStatsFTDA2N,
       "cmFlowStatsIBRA2NMax": cmFlowStatsIBRA2NMax,
       "cmFlowStatsIBRRlA2NMax": cmFlowStatsIBRRlA2NMax,
       "cmFlowStatsIBRA2NMin": cmFlowStatsIBRA2NMin,
       "cmFlowStatsIBRRlA2NMin": cmFlowStatsIBRRlA2NMin,
       "cmFlowStatsIBRA2N": cmFlowStatsIBRA2N,
       "cmFlowStatsIBRRlA2N": cmFlowStatsIBRRlA2N,
       "cmFlowStatsIBRN2AMax": cmFlowStatsIBRN2AMax,
       "cmFlowStatsIBRRlN2AMax": cmFlowStatsIBRRlN2AMax,
       "cmFlowStatsIBRN2AMin": cmFlowStatsIBRN2AMin,
       "cmFlowStatsIBRRlN2AMin": cmFlowStatsIBRRlN2AMin,
       "cmFlowStatsIBRN2A": cmFlowStatsIBRN2A,
       "cmFlowStatsIBRRlN2A": cmFlowStatsIBRRlN2A,
       "cmFlowStatsFMCDA2N": cmFlowStatsFMCDA2N,
       "cmFlowStatsFBCDA2N": cmFlowStatsFBCDA2N,
       "cmFlowStatsACLN2ADrop": cmFlowStatsACLN2ADrop,
       "cmFlowStatsACLA2NDrop": cmFlowStatsACLA2NDrop,
       "cmFlowHistoryTable": cmFlowHistoryTable,
       "cmFlowHistoryEntry": cmFlowHistoryEntry,
       "cmFlowHistoryIndex": cmFlowHistoryIndex,
       "cmFlowHistoryTime": cmFlowHistoryTime,
       "cmFlowHistoryValid": cmFlowHistoryValid,
       "cmFlowHistoryAction": cmFlowHistoryAction,
       "cmFlowHistoryL2CPFD": cmFlowHistoryL2CPFD,
       "cmFlowHistoryABRA2N": cmFlowHistoryABRA2N,
       "cmFlowHistoryABRRLA2N": cmFlowHistoryABRRLA2N,
       "cmFlowHistoryABRRLRA2N": cmFlowHistoryABRRLRA2N,
       "cmFlowHistoryABRN2A": cmFlowHistoryABRN2A,
       "cmFlowHistoryABRRLN2A": cmFlowHistoryABRRLN2A,
       "cmFlowHistoryUAS": cmFlowHistoryUAS,
       "cmFlowHistoryES": cmFlowHistoryES,
       "cmFlowHistorySES": cmFlowHistorySES,
       "cmFlowHistoryFMGA2N": cmFlowHistoryFMGA2N,
       "cmFlowHistoryFMYA2N": cmFlowHistoryFMYA2N,
       "cmFlowHistoryFMYDA2N": cmFlowHistoryFMYDA2N,
       "cmFlowHistoryFMRDA2N": cmFlowHistoryFMRDA2N,
       "cmFlowHistoryBytesInA2N": cmFlowHistoryBytesInA2N,
       "cmFlowHistoryBytesOutA2N": cmFlowHistoryBytesOutA2N,
       "cmFlowHistoryFMGN2A": cmFlowHistoryFMGN2A,
       "cmFlowHistoryFMYN2A": cmFlowHistoryFMYN2A,
       "cmFlowHistoryFMYDN2A": cmFlowHistoryFMYDN2A,
       "cmFlowHistoryFMRDN2A": cmFlowHistoryFMRDN2A,
       "cmFlowHistoryBytesInN2A": cmFlowHistoryBytesInN2A,
       "cmFlowHistoryBytesOutN2A": cmFlowHistoryBytesOutN2A,
       "cmFlowHistoryFTDA2N": cmFlowHistoryFTDA2N,
       "cmFlowHistoryIBRA2NMax": cmFlowHistoryIBRA2NMax,
       "cmFlowHistoryIBRRlA2NMax": cmFlowHistoryIBRRlA2NMax,
       "cmFlowHistoryIBRA2NMin": cmFlowHistoryIBRA2NMin,
       "cmFlowHistoryIBRRlA2NMin": cmFlowHistoryIBRRlA2NMin,
       "cmFlowHistoryIBRA2N": cmFlowHistoryIBRA2N,
       "cmFlowHistoryIBRRlA2N": cmFlowHistoryIBRRlA2N,
       "cmFlowHistoryIBRN2AMax": cmFlowHistoryIBRN2AMax,
       "cmFlowHistoryIBRRlN2AMax": cmFlowHistoryIBRRlN2AMax,
       "cmFlowHistoryIBRN2AMin": cmFlowHistoryIBRN2AMin,
       "cmFlowHistoryIBRRlN2AMin": cmFlowHistoryIBRRlN2AMin,
       "cmFlowHistoryIBRN2A": cmFlowHistoryIBRN2A,
       "cmFlowHistoryIBRRlN2A": cmFlowHistoryIBRRlN2A,
       "cmFlowHistoryFMCDA2N": cmFlowHistoryFMCDA2N,
       "cmFlowHistoryFBCDA2N": cmFlowHistoryFBCDA2N,
       "cmFlowHistoryACLN2ADrop": cmFlowHistoryACLN2ADrop,
       "cmFlowHistoryACLA2NDrop": cmFlowHistoryACLA2NDrop,
       "cmFlowThresholdTable": cmFlowThresholdTable,
       "cmFlowThresholdEntry": cmFlowThresholdEntry,
       "cmFlowThresholdIndex": cmFlowThresholdIndex,
       "cmFlowThresholdInterval": cmFlowThresholdInterval,
       "cmFlowThresholdVariable": cmFlowThresholdVariable,
       "cmFlowThresholdValueLo": cmFlowThresholdValueLo,
       "cmFlowThresholdValueHi": cmFlowThresholdValueHi,
       "cmFlowThresholdMonValue": cmFlowThresholdMonValue,
       "cmQosShaperStatsTable": cmQosShaperStatsTable,
       "cmQosShaperStatsEntry": cmQosShaperStatsEntry,
       "cmQosShaperStatsIndex": cmQosShaperStatsIndex,
       "cmQosShaperStatsIntervalType": cmQosShaperStatsIntervalType,
       "cmQosShaperStatsValid": cmQosShaperStatsValid,
       "cmQosShaperStatsAction": cmQosShaperStatsAction,
       "cmQosShaperStatsBT": cmQosShaperStatsBT,
       "cmQosShaperStatsBTD": cmQosShaperStatsBTD,
       "cmQosShaperStatsFD": cmQosShaperStatsFD,
       "cmQosShaperStatsFTD": cmQosShaperStatsFTD,
       "cmQosShaperStatsBR": cmQosShaperStatsBR,
       "cmQosShaperStatsFR": cmQosShaperStatsFR,
       "cmQosShaperStatsABRRL": cmQosShaperStatsABRRL,
       "cmQosShaperStatsABRRLR": cmQosShaperStatsABRRLR,
       "cmQosShaperStatsBREDD": cmQosShaperStatsBREDD,
       "cmQosShaperStatsFREDD": cmQosShaperStatsFREDD,
       "cmQosShaperHistoryTable": cmQosShaperHistoryTable,
       "cmQosShaperHistoryEntry": cmQosShaperHistoryEntry,
       "cmQosShaperHistoryIndex": cmQosShaperHistoryIndex,
       "cmQosShaperHistoryTime": cmQosShaperHistoryTime,
       "cmQosShaperHistoryValid": cmQosShaperHistoryValid,
       "cmQosShaperHistoryAction": cmQosShaperHistoryAction,
       "cmQosShaperHistoryBT": cmQosShaperHistoryBT,
       "cmQosShaperHistoryBTD": cmQosShaperHistoryBTD,
       "cmQosShaperHistoryFD": cmQosShaperHistoryFD,
       "cmQosShaperHistoryFTD": cmQosShaperHistoryFTD,
       "cmQosShaperHistoryBR": cmQosShaperHistoryBR,
       "cmQosShaperHistoryFR": cmQosShaperHistoryFR,
       "cmQosShaperHistoryABRRL": cmQosShaperHistoryABRRL,
       "cmQosShaperHistoryABRRLR": cmQosShaperHistoryABRRLR,
       "cmQosShaperHistoryBREDD": cmQosShaperHistoryBREDD,
       "cmQosShaperHistoryFREDD": cmQosShaperHistoryFREDD,
       "cmQosShaperThresholdTable": cmQosShaperThresholdTable,
       "cmQosShaperThresholdEntry": cmQosShaperThresholdEntry,
       "cmQosShaperThresholdIndex": cmQosShaperThresholdIndex,
       "cmQosShaperThresholdInterval": cmQosShaperThresholdInterval,
       "cmQosShaperThresholdVariable": cmQosShaperThresholdVariable,
       "cmQosShaperThresholdValueLo": cmQosShaperThresholdValueLo,
       "cmQosShaperThresholdValueHi": cmQosShaperThresholdValueHi,
       "cmQosShaperThresholdMonValue": cmQosShaperThresholdMonValue,
       "cmQosFlowPolicerStatsTable": cmQosFlowPolicerStatsTable,
       "cmQosFlowPolicerStatsEntry": cmQosFlowPolicerStatsEntry,
       "cmQosFlowPolicerStatsIndex": cmQosFlowPolicerStatsIndex,
       "cmQosFlowPolicerStatsIntervalType": cmQosFlowPolicerStatsIntervalType,
       "cmQosFlowPolicerStatsValid": cmQosFlowPolicerStatsValid,
       "cmQosFlowPolicerStatsAction": cmQosFlowPolicerStatsAction,
       "cmQosFlowPolicerStatsFMG": cmQosFlowPolicerStatsFMG,
       "cmQosFlowPolicerStatsFMY": cmQosFlowPolicerStatsFMY,
       "cmQosFlowPolicerStatsFMYD": cmQosFlowPolicerStatsFMYD,
       "cmQosFlowPolicerStatsFMRD": cmQosFlowPolicerStatsFMRD,
       "cmQosFlowPolicerStatsBytesIn": cmQosFlowPolicerStatsBytesIn,
       "cmQosFlowPolicerStatsBytesOut": cmQosFlowPolicerStatsBytesOut,
       "cmQosFlowPolicerStatsABR": cmQosFlowPolicerStatsABR,
       "cmQosFlowPolicerHistoryTable": cmQosFlowPolicerHistoryTable,
       "cmQosFlowPolicerHistoryEntry": cmQosFlowPolicerHistoryEntry,
       "cmQosFlowPolicerHistoryIndex": cmQosFlowPolicerHistoryIndex,
       "cmQosFlowPolicerHistoryTime": cmQosFlowPolicerHistoryTime,
       "cmQosFlowPolicerHistoryValid": cmQosFlowPolicerHistoryValid,
       "cmQosFlowPolicerHistoryAction": cmQosFlowPolicerHistoryAction,
       "cmQosFlowPolicerHistoryFMG": cmQosFlowPolicerHistoryFMG,
       "cmQosFlowPolicerHistoryFMY": cmQosFlowPolicerHistoryFMY,
       "cmQosFlowPolicerHistoryFMYD": cmQosFlowPolicerHistoryFMYD,
       "cmQosFlowPolicerHistoryFMRD": cmQosFlowPolicerHistoryFMRD,
       "cmQosFlowPolicerHistoryBytesIn": cmQosFlowPolicerHistoryBytesIn,
       "cmQosFlowPolicerHistoryBytesOut": cmQosFlowPolicerHistoryBytesOut,
       "cmQosFlowPolicerHistoryABR": cmQosFlowPolicerHistoryABR,
       "cmQosFlowPolicerThresholdTable": cmQosFlowPolicerThresholdTable,
       "cmQosFlowPolicerThresholdEntry": cmQosFlowPolicerThresholdEntry,
       "cmQosFlowPolicerThresholdIndex": cmQosFlowPolicerThresholdIndex,
       "cmQosFlowPolicerThresholdInterval": cmQosFlowPolicerThresholdInterval,
       "cmQosFlowPolicerThresholdVariable": cmQosFlowPolicerThresholdVariable,
       "cmQosFlowPolicerThresholdValueLo": cmQosFlowPolicerThresholdValueLo,
       "cmQosFlowPolicerThresholdValueHi": cmQosFlowPolicerThresholdValueHi,
       "cmQosFlowPolicerThresholdMonValue": cmQosFlowPolicerThresholdMonValue,
       "cmAccPortQosShaperStatsTable": cmAccPortQosShaperStatsTable,
       "cmAccPortQosShaperStatsEntry": cmAccPortQosShaperStatsEntry,
       "cmAccPortQosShaperStatsIndex": cmAccPortQosShaperStatsIndex,
       "cmAccPortQosShaperStatsIntervalType": cmAccPortQosShaperStatsIntervalType,
       "cmAccPortQosShaperStatsValid": cmAccPortQosShaperStatsValid,
       "cmAccPortQosShaperStatsAction": cmAccPortQosShaperStatsAction,
       "cmAccPortQosShaperStatsBT": cmAccPortQosShaperStatsBT,
       "cmAccPortQosShaperStatsBTD": cmAccPortQosShaperStatsBTD,
       "cmAccPortQosShaperStatsFD": cmAccPortQosShaperStatsFD,
       "cmAccPortQosShaperStatsFTD": cmAccPortQosShaperStatsFTD,
       "cmAccPortQosShaperStatsBR": cmAccPortQosShaperStatsBR,
       "cmAccPortQosShaperStatsFR": cmAccPortQosShaperStatsFR,
       "cmAccPortQosShaperStatsABRRL": cmAccPortQosShaperStatsABRRL,
       "cmAccPortQosShaperStatsBREDD": cmAccPortQosShaperStatsBREDD,
       "cmAccPortQosShaperStatsFREDD": cmAccPortQosShaperStatsFREDD,
       "cmAccPortQosShaperHistoryTable": cmAccPortQosShaperHistoryTable,
       "cmAccPortQosShaperHistoryEntry": cmAccPortQosShaperHistoryEntry,
       "cmAccPortQosShaperHistoryIndex": cmAccPortQosShaperHistoryIndex,
       "cmAccPortQosShaperHistoryTime": cmAccPortQosShaperHistoryTime,
       "cmAccPortQosShaperHistoryValid": cmAccPortQosShaperHistoryValid,
       "cmAccPortQosShaperHistoryAction": cmAccPortQosShaperHistoryAction,
       "cmAccPortQosShaperHistoryBT": cmAccPortQosShaperHistoryBT,
       "cmAccPortQosShaperHistoryBTD": cmAccPortQosShaperHistoryBTD,
       "cmAccPortQosShaperHistoryFD": cmAccPortQosShaperHistoryFD,
       "cmAccPortQosShaperHistoryFTD": cmAccPortQosShaperHistoryFTD,
       "cmAccPortQosShaperHistoryBR": cmAccPortQosShaperHistoryBR,
       "cmAccPortQosShaperHistoryFR": cmAccPortQosShaperHistoryFR,
       "cmAccPortQosShaperHistoryABRRL": cmAccPortQosShaperHistoryABRRL,
       "cmAccPortQosShaperHistoryBREDD": cmAccPortQosShaperHistoryBREDD,
       "cmAccPortQosShaperHistoryFREDD": cmAccPortQosShaperHistoryFREDD,
       "cmAccPortQosShaperThresholdTable": cmAccPortQosShaperThresholdTable,
       "cmAccPortQosShaperThresholdEntry": cmAccPortQosShaperThresholdEntry,
       "cmAccPortQosShaperThresholdIndex": cmAccPortQosShaperThresholdIndex,
       "cmAccPortQosShaperThresholdInterval": cmAccPortQosShaperThresholdInterval,
       "cmAccPortQosShaperThresholdVariable": cmAccPortQosShaperThresholdVariable,
       "cmAccPortQosShaperThresholdValueLo": cmAccPortQosShaperThresholdValueLo,
       "cmAccPortQosShaperThresholdValueHi": cmAccPortQosShaperThresholdValueHi,
       "cmAccPortQosShaperThresholdMonValue": cmAccPortQosShaperThresholdMonValue,
       "cmEthernetTrafficPortStatsTable": cmEthernetTrafficPortStatsTable,
       "cmEthernetTrafficPortStatsEntry": cmEthernetTrafficPortStatsEntry,
       "cmEthernetTrafficPortStatsIndex": cmEthernetTrafficPortStatsIndex,
       "cmEthernetTrafficPortStatsIntervalType": cmEthernetTrafficPortStatsIntervalType,
       "cmEthernetTrafficPortStatsValid": cmEthernetTrafficPortStatsValid,
       "cmEthernetTrafficPortStatsAction": cmEthernetTrafficPortStatsAction,
       "cmEthernetTrafficPortStatsESBF": cmEthernetTrafficPortStatsESBF,
       "cmEthernetTrafficPortStatsESBP": cmEthernetTrafficPortStatsESBP,
       "cmEthernetTrafficPortStatsESBS": cmEthernetTrafficPortStatsESBS,
       "cmEthernetTrafficPortStatsESC": cmEthernetTrafficPortStatsESC,
       "cmEthernetTrafficPortStatsESCAE": cmEthernetTrafficPortStatsESCAE,
       "cmEthernetTrafficPortStatsESDE": cmEthernetTrafficPortStatsESDE,
       "cmEthernetTrafficPortStatsESF": cmEthernetTrafficPortStatsESF,
       "cmEthernetTrafficPortStatsESFS": cmEthernetTrafficPortStatsESFS,
       "cmEthernetTrafficPortStatsESJ": cmEthernetTrafficPortStatsESJ,
       "cmEthernetTrafficPortStatsESMF": cmEthernetTrafficPortStatsESMF,
       "cmEthernetTrafficPortStatsESMP": cmEthernetTrafficPortStatsESMP,
       "cmEthernetTrafficPortStatsESO": cmEthernetTrafficPortStatsESO,
       "cmEthernetTrafficPortStatsESOF": cmEthernetTrafficPortStatsESOF,
       "cmEthernetTrafficPortStatsESOP": cmEthernetTrafficPortStatsESOP,
       "cmEthernetTrafficPortStatsESP": cmEthernetTrafficPortStatsESP,
       "cmEthernetTrafficPortStatsESP64": cmEthernetTrafficPortStatsESP64,
       "cmEthernetTrafficPortStatsESP65": cmEthernetTrafficPortStatsESP65,
       "cmEthernetTrafficPortStatsESP128": cmEthernetTrafficPortStatsESP128,
       "cmEthernetTrafficPortStatsESP256": cmEthernetTrafficPortStatsESP256,
       "cmEthernetTrafficPortStatsESP512": cmEthernetTrafficPortStatsESP512,
       "cmEthernetTrafficPortStatsESP1024": cmEthernetTrafficPortStatsESP1024,
       "cmEthernetTrafficPortStatsESP1519": cmEthernetTrafficPortStatsESP1519,
       "cmEthernetTrafficPortStatsESUF": cmEthernetTrafficPortStatsESUF,
       "cmEthernetTrafficPortStatsESUP": cmEthernetTrafficPortStatsESUP,
       "cmEthernetTrafficPortStatsL2CPFD": cmEthernetTrafficPortStatsL2CPFD,
       "cmEthernetTrafficPortStatsL2CPFP": cmEthernetTrafficPortStatsL2CPFP,
       "cmEthernetTrafficPortStatsLES": cmEthernetTrafficPortStatsLES,
       "cmEthernetTrafficPortStatsLBC": cmEthernetTrafficPortStatsLBC,
       "cmEthernetTrafficPortStatsOPT": cmEthernetTrafficPortStatsOPT,
       "cmEthernetTrafficPortStatsOPR": cmEthernetTrafficPortStatsOPR,
       "cmEthernetTrafficPortStatsAUFD": cmEthernetTrafficPortStatsAUFD,
       "cmEthernetTrafficPortStatsAPFD": cmEthernetTrafficPortStatsAPFD,
       "cmEthernetTrafficPortStatsABRRx": cmEthernetTrafficPortStatsABRRx,
       "cmEthernetTrafficPortStatsABRTx": cmEthernetTrafficPortStatsABRTx,
       "cmEthernetTrafficPortStatsATFD": cmEthernetTrafficPortStatsATFD,
       "cmEthernetTrafficPortStatsUAS": cmEthernetTrafficPortStatsUAS,
       "cmEthernetTrafficPortStatsTemp": cmEthernetTrafficPortStatsTemp,
       "cmEthernetTrafficPortStatsLkupFails": cmEthernetTrafficPortStatsLkupFails,
       "cmEthernetTrafficPortStatsPSC": cmEthernetTrafficPortStatsPSC,
       "cmEthernetTrafficPortStatsL2PTRxFramesEncap": cmEthernetTrafficPortStatsL2PTRxFramesEncap,
       "cmEthernetTrafficPortStatsL2PTTxFramesDecap": cmEthernetTrafficPortStatsL2PTTxFramesDecap,
       "cmEthernetTrafficPortStatsIBRMaxRx": cmEthernetTrafficPortStatsIBRMaxRx,
       "cmEthernetTrafficPortStatsIBRMaxTx": cmEthernetTrafficPortStatsIBRMaxTx,
       "cmEthernetTrafficPortStatsIBRMinRx": cmEthernetTrafficPortStatsIBRMinRx,
       "cmEthernetTrafficPortStatsIBRMinTx": cmEthernetTrafficPortStatsIBRMinTx,
       "cmEthernetTrafficPortStatsIBRRx": cmEthernetTrafficPortStatsIBRRx,
       "cmEthernetTrafficPortStatsIBRTx": cmEthernetTrafficPortStatsIBRTx,
       "cmEthernetTrafficPortStatsFmcd": cmEthernetTrafficPortStatsFmcd,
       "cmEthernetTrafficPortStatsFbcd": cmEthernetTrafficPortStatsFbcd,
       "cmEthernetTrafficPortStatsAclDropNoMatch": cmEthernetTrafficPortStatsAclDropNoMatch,
       "cmEthernetTrafficPortStatsAclFwd2Cpu": cmEthernetTrafficPortStatsAclFwd2Cpu,
       "cmEthernetTrafficPortStatsDhcpDropNoAssocIf": cmEthernetTrafficPortStatsDhcpDropNoAssocIf,
       "cmEthernetTrafficPortStatsDroppedFragmented": cmEthernetTrafficPortStatsDroppedFragmented,
       "cmEthernetTrafficPortStatsRLBC": cmEthernetTrafficPortStatsRLBC,
       "cmEthernetTrafficPortStatsROPT": cmEthernetTrafficPortStatsROPT,
       "cmEthernetTrafficPortStatsROPR": cmEthernetTrafficPortStatsROPR,
       "cmEthernetTrafficPortStatsRTemp": cmEthernetTrafficPortStatsRTemp,
       "cmEthernetTrafficPortHistoryTable": cmEthernetTrafficPortHistoryTable,
       "cmEthernetTrafficPortHistoryEntry": cmEthernetTrafficPortHistoryEntry,
       "cmEthernetTrafficPortHistoryIndex": cmEthernetTrafficPortHistoryIndex,
       "cmEthernetTrafficPortHistoryTime": cmEthernetTrafficPortHistoryTime,
       "cmEthernetTrafficPortHistoryValid": cmEthernetTrafficPortHistoryValid,
       "cmEthernetTrafficPortHistoryAction": cmEthernetTrafficPortHistoryAction,
       "cmEthernetTrafficPortHistoryESBF": cmEthernetTrafficPortHistoryESBF,
       "cmEthernetTrafficPortHistoryESBP": cmEthernetTrafficPortHistoryESBP,
       "cmEthernetTrafficPortHistoryESBS": cmEthernetTrafficPortHistoryESBS,
       "cmEthernetTrafficPortHistoryESC": cmEthernetTrafficPortHistoryESC,
       "cmEthernetTrafficPortHistoryESCAE": cmEthernetTrafficPortHistoryESCAE,
       "cmEthernetTrafficPortHistoryESDE": cmEthernetTrafficPortHistoryESDE,
       "cmEthernetTrafficPortHistoryESF": cmEthernetTrafficPortHistoryESF,
       "cmEthernetTrafficPortHistoryESFS": cmEthernetTrafficPortHistoryESFS,
       "cmEthernetTrafficPortHistoryESJ": cmEthernetTrafficPortHistoryESJ,
       "cmEthernetTrafficPortHistoryESMF": cmEthernetTrafficPortHistoryESMF,
       "cmEthernetTrafficPortHistoryESMP": cmEthernetTrafficPortHistoryESMP,
       "cmEthernetTrafficPortHistoryESO": cmEthernetTrafficPortHistoryESO,
       "cmEthernetTrafficPortHistoryESOF": cmEthernetTrafficPortHistoryESOF,
       "cmEthernetTrafficPortHistoryESOP": cmEthernetTrafficPortHistoryESOP,
       "cmEthernetTrafficPortHistoryESP": cmEthernetTrafficPortHistoryESP,
       "cmEthernetTrafficPortHistoryESP64": cmEthernetTrafficPortHistoryESP64,
       "cmEthernetTrafficPortHistoryESP65": cmEthernetTrafficPortHistoryESP65,
       "cmEthernetTrafficPortHistoryESP128": cmEthernetTrafficPortHistoryESP128,
       "cmEthernetTrafficPortHistoryESP256": cmEthernetTrafficPortHistoryESP256,
       "cmEthernetTrafficPortHistoryESP512": cmEthernetTrafficPortHistoryESP512,
       "cmEthernetTrafficPortHistoryESP1024": cmEthernetTrafficPortHistoryESP1024,
       "cmEthernetTrafficPortHistoryESP1519": cmEthernetTrafficPortHistoryESP1519,
       "cmEthernetTrafficPortHistoryESUF": cmEthernetTrafficPortHistoryESUF,
       "cmEthernetTrafficPortHistoryESUP": cmEthernetTrafficPortHistoryESUP,
       "cmEthernetTrafficPortHistoryL2CPFD": cmEthernetTrafficPortHistoryL2CPFD,
       "cmEthernetTrafficPortHistoryL2CPFP": cmEthernetTrafficPortHistoryL2CPFP,
       "cmEthernetTrafficPortHistoryLES": cmEthernetTrafficPortHistoryLES,
       "cmEthernetTrafficPortHistoryLBC": cmEthernetTrafficPortHistoryLBC,
       "cmEthernetTrafficPortHistoryOPT": cmEthernetTrafficPortHistoryOPT,
       "cmEthernetTrafficPortHistoryOPR": cmEthernetTrafficPortHistoryOPR,
       "cmEthernetTrafficPortHistoryAUFD": cmEthernetTrafficPortHistoryAUFD,
       "cmEthernetTrafficPortHistoryAPFD": cmEthernetTrafficPortHistoryAPFD,
       "cmEthernetTrafficPortHistoryABRRx": cmEthernetTrafficPortHistoryABRRx,
       "cmEthernetTrafficPortHistoryABRTx": cmEthernetTrafficPortHistoryABRTx,
       "cmEthernetTrafficPortHistoryATFD": cmEthernetTrafficPortHistoryATFD,
       "cmEthernetTrafficPortHistoryUAS": cmEthernetTrafficPortHistoryUAS,
       "cmEthernetTrafficPortHistoryTemp": cmEthernetTrafficPortHistoryTemp,
       "cmEthernetTrafficPortHistoryLkupFails": cmEthernetTrafficPortHistoryLkupFails,
       "cmEthernetTrafficPortHistoryPSC": cmEthernetTrafficPortHistoryPSC,
       "cmEthernetTrafficPortHistoryL2PTRxFramesEncap": cmEthernetTrafficPortHistoryL2PTRxFramesEncap,
       "cmEthernetTrafficPortHistoryL2PTTxFramesDecap": cmEthernetTrafficPortHistoryL2PTTxFramesDecap,
       "cmEthernetTrafficPortHistoryIBRMaxRx": cmEthernetTrafficPortHistoryIBRMaxRx,
       "cmEthernetTrafficPortHistoryIBRMaxTx": cmEthernetTrafficPortHistoryIBRMaxTx,
       "cmEthernetTrafficPortHistoryIBRMinRx": cmEthernetTrafficPortHistoryIBRMinRx,
       "cmEthernetTrafficPortHistoryIBRMinTx": cmEthernetTrafficPortHistoryIBRMinTx,
       "cmEthernetTrafficPortHistoryIBRRx": cmEthernetTrafficPortHistoryIBRRx,
       "cmEthernetTrafficPortHistoryIBRTx": cmEthernetTrafficPortHistoryIBRTx,
       "cmEthernetTrafficPortHistoryFmcd": cmEthernetTrafficPortHistoryFmcd,
       "cmEthernetTrafficPortHistoryFbcd": cmEthernetTrafficPortHistoryFbcd,
       "cmEthernetTrafficPortHistoryAclDropNoMatch": cmEthernetTrafficPortHistoryAclDropNoMatch,
       "cmEthernetTrafficPortHistoryAclFwd2Cpu": cmEthernetTrafficPortHistoryAclFwd2Cpu,
       "cmEthernetTrafficPortHistoryDhcpDropNoAssocIf": cmEthernetTrafficPortHistoryDhcpDropNoAssocIf,
       "cmEthernetTrafficPortHistoryDroppedFragmented": cmEthernetTrafficPortHistoryDroppedFragmented,
       "cmEthernetTrafficPortHistoryRLBC": cmEthernetTrafficPortHistoryRLBC,
       "cmEthernetTrafficPortHistoryROPT": cmEthernetTrafficPortHistoryROPT,
       "cmEthernetTrafficPortHistoryROPR": cmEthernetTrafficPortHistoryROPR,
       "cmEthernetTrafficPortHistoryRTemp": cmEthernetTrafficPortHistoryRTemp,
       "cmEthernetTrafficPortThresholdTable": cmEthernetTrafficPortThresholdTable,
       "cmEthernetTrafficPortThresholdEntry": cmEthernetTrafficPortThresholdEntry,
       "cmEthernetTrafficPortThresholdIndex": cmEthernetTrafficPortThresholdIndex,
       "cmEthernetTrafficPortThresholdInterval": cmEthernetTrafficPortThresholdInterval,
       "cmEthernetTrafficPortThresholdVariable": cmEthernetTrafficPortThresholdVariable,
       "cmEthernetTrafficPortThresholdValueLo": cmEthernetTrafficPortThresholdValueLo,
       "cmEthernetTrafficPortThresholdValueHi": cmEthernetTrafficPortThresholdValueHi,
       "cmEthernetTrafficPortThresholdMonValue": cmEthernetTrafficPortThresholdMonValue,
       "cmEthernetTrafficPortThresholdVarTable": cmEthernetTrafficPortThresholdVarTable,
       "cmEthernetTrafficPortThresholdVarEntry": cmEthernetTrafficPortThresholdVarEntry,
       "cmEthernetTrafficPortThresholdVarOprVariance": cmEthernetTrafficPortThresholdVarOprVariance,
       "cmEthernetTrafficPortThresholdVarOptVariance": cmEthernetTrafficPortThresholdVarOptVariance,
       "cmFlowPointStatsTable": cmFlowPointStatsTable,
       "cmFlowPointStatsEntry": cmFlowPointStatsEntry,
       "cmFlowPointStatsIndex": cmFlowPointStatsIndex,
       "cmFlowPointStatsIntervalType": cmFlowPointStatsIntervalType,
       "cmFlowPointStatsValid": cmFlowPointStatsValid,
       "cmFlowPointStatsAction": cmFlowPointStatsAction,
       "cmFlowPointStatsL2CPFD": cmFlowPointStatsL2CPFD,
       "cmFlowPointStatsABRRx": cmFlowPointStatsABRRx,
       "cmFlowPointStatsABRRLRx": cmFlowPointStatsABRRLRx,
       "cmFlowPointStatsUAS": cmFlowPointStatsUAS,
       "cmFlowPointStatsSES": cmFlowPointStatsSES,
       "cmFlowPointStatsFMG": cmFlowPointStatsFMG,
       "cmFlowPointStatsFMY": cmFlowPointStatsFMY,
       "cmFlowPointStatsFMRD": cmFlowPointStatsFMRD,
       "cmFlowPointStatsFTD": cmFlowPointStatsFTD,
       "cmFlowPointStatsBytesIn": cmFlowPointStatsBytesIn,
       "cmFlowPointStatsBytesOut": cmFlowPointStatsBytesOut,
       "cmFlowPointStatsFREDD": cmFlowPointStatsFREDD,
       "cmFlowPointStatsFACLD": cmFlowPointStatsFACLD,
       "cmFlowPointStatsFMYD": cmFlowPointStatsFMYD,
       "cmFlowPointStatsFMGD": cmFlowPointStatsFMGD,
       "cmFlowPointStatsFD": cmFlowPointStatsFD,
       "cmFlowPointStatsFMCD": cmFlowPointStatsFMCD,
       "cmFlowPointStatsFBCD": cmFlowPointStatsFBCD,
       "cmFlowPointStatsBT": cmFlowPointStatsBT,
       "cmFlowPointStatsFLD": cmFlowPointStatsFLD,
       "cmFlowPointStatsIBRMax": cmFlowPointStatsIBRMax,
       "cmFlowPointStatsIBRRlMax": cmFlowPointStatsIBRRlMax,
       "cmFlowPointStatsIBRMin": cmFlowPointStatsIBRMin,
       "cmFlowPointStatsIBRRlMin": cmFlowPointStatsIBRRlMin,
       "cmFlowPointStatsIBR": cmFlowPointStatsIBR,
       "cmFlowPointStatsIBRRl": cmFlowPointStatsIBRRl,
       "cmFlowPointStatsFdRxFb": cmFlowPointStatsFdRxFb,
       "cmFlowPointStatsFdTxFb": cmFlowPointStatsFdTxFb,
       "cmFlowPointStatsFdicd": cmFlowPointStatsFdicd,
       "cmFlowPointStatsNumLearnTableFlushes": cmFlowPointStatsNumLearnTableFlushes,
       "cmFlowPointStatsEfFramesDiscarded": cmFlowPointStatsEfFramesDiscarded,
       "cmFlowPointStatsEfBytesDiscarded": cmFlowPointStatsEfBytesDiscarded,
       "cmFlowPointStatsAclDropNoMatch": cmFlowPointStatsAclDropNoMatch,
       "cmFlowPointStatsAclRuleDrop": cmFlowPointStatsAclRuleDrop,
       "cmFlowPointHistoryTable": cmFlowPointHistoryTable,
       "cmFlowPointHistoryEntry": cmFlowPointHistoryEntry,
       "cmFlowPointHistoryIndex": cmFlowPointHistoryIndex,
       "cmFlowPointHistoryTime": cmFlowPointHistoryTime,
       "cmFlowPointHistoryValid": cmFlowPointHistoryValid,
       "cmFlowPointHistoryAction": cmFlowPointHistoryAction,
       "cmFlowPointHistoryL2CPFD": cmFlowPointHistoryL2CPFD,
       "cmFlowPointHistoryABRRx": cmFlowPointHistoryABRRx,
       "cmFlowPointHistoryABRRLRx": cmFlowPointHistoryABRRLRx,
       "cmFlowPointHistoryUAS": cmFlowPointHistoryUAS,
       "cmFlowPointHistorySES": cmFlowPointHistorySES,
       "cmFlowPointHistoryFMG": cmFlowPointHistoryFMG,
       "cmFlowPointHistoryFMY": cmFlowPointHistoryFMY,
       "cmFlowPointHistoryFMRD": cmFlowPointHistoryFMRD,
       "cmFlowPointHistoryFTD": cmFlowPointHistoryFTD,
       "cmFlowPointHistoryBytesIn": cmFlowPointHistoryBytesIn,
       "cmFlowPointHistoryBytesOut": cmFlowPointHistoryBytesOut,
       "cmFlowPointHistoryFREDD": cmFlowPointHistoryFREDD,
       "cmFlowPointHistoryFACLD": cmFlowPointHistoryFACLD,
       "cmFlowPointHistoryFMYD": cmFlowPointHistoryFMYD,
       "cmFlowPointHistoryFMGD": cmFlowPointHistoryFMGD,
       "cmFlowPointHistoryFD": cmFlowPointHistoryFD,
       "cmFlowPointHistoryFMCD": cmFlowPointHistoryFMCD,
       "cmFlowPointHistoryFBCD": cmFlowPointHistoryFBCD,
       "cmFlowPointHistoryBT": cmFlowPointHistoryBT,
       "cmFlowPointHistoryFLD": cmFlowPointHistoryFLD,
       "cmFlowPointHistoryIBRMax": cmFlowPointHistoryIBRMax,
       "cmFlowPointHistoryIBRRlMax": cmFlowPointHistoryIBRRlMax,
       "cmFlowPointHistoryIBRMin": cmFlowPointHistoryIBRMin,
       "cmFlowPointHistoryIBRRlMin": cmFlowPointHistoryIBRRlMin,
       "cmFlowPointHistoryIBR": cmFlowPointHistoryIBR,
       "cmFlowPointHistoryIBRRl": cmFlowPointHistoryIBRRl,
       "cmFlowPointHistoryFdRxFb": cmFlowPointHistoryFdRxFb,
       "cmFlowPointHistoryFdTxFb": cmFlowPointHistoryFdTxFb,
       "cmFlowPointHistoryFdicd": cmFlowPointHistoryFdicd,
       "cmFlowPointHistoryNumLearnTableFlushes": cmFlowPointHistoryNumLearnTableFlushes,
       "cmFlowPointHistoryEfFramesDiscarded": cmFlowPointHistoryEfFramesDiscarded,
       "cmFlowPointHistoryEfBytesDiscarded": cmFlowPointHistoryEfBytesDiscarded,
       "cmFlowPointHistoryAclDropNoMatch": cmFlowPointHistoryAclDropNoMatch,
       "cmFlowPointHistoryAclRuleDrop": cmFlowPointHistoryAclRuleDrop,
       "cmFlowPointThresholdTable": cmFlowPointThresholdTable,
       "cmFlowPointThresholdEntry": cmFlowPointThresholdEntry,
       "cmFlowPointThresholdIndex": cmFlowPointThresholdIndex,
       "cmFlowPointThresholdInterval": cmFlowPointThresholdInterval,
       "cmFlowPointThresholdVariable": cmFlowPointThresholdVariable,
       "cmFlowPointThresholdValueLo": cmFlowPointThresholdValueLo,
       "cmFlowPointThresholdValueHi": cmFlowPointThresholdValueHi,
       "cmFlowPointThresholdMonValue": cmFlowPointThresholdMonValue,
       "cmOAMFlowPointStatsTable": cmOAMFlowPointStatsTable,
       "cmOAMFlowPointStatsEntry": cmOAMFlowPointStatsEntry,
       "cmOAMFlowPointStatsIndex": cmOAMFlowPointStatsIndex,
       "cmOAMFlowPointStatsIntervalType": cmOAMFlowPointStatsIntervalType,
       "cmOAMFlowPointStatsValid": cmOAMFlowPointStatsValid,
       "cmOAMFlowPointStatsAction": cmOAMFlowPointStatsAction,
       "cmOAMFlowPointStatsUAS": cmOAMFlowPointStatsUAS,
       "cmOAMFlowPointStatsSES": cmOAMFlowPointStatsSES,
       "cmOAMFlowPointHistoryTable": cmOAMFlowPointHistoryTable,
       "cmOAMFlowPointHistoryEntry": cmOAMFlowPointHistoryEntry,
       "cmOAMFlowPointHistoryIndex": cmOAMFlowPointHistoryIndex,
       "cmOAMFlowPointHistoryTime": cmOAMFlowPointHistoryTime,
       "cmOAMFlowPointHistoryValid": cmOAMFlowPointHistoryValid,
       "cmOAMFlowPointHistoryAction": cmOAMFlowPointHistoryAction,
       "cmOAMFlowPointHistoryUAS": cmOAMFlowPointHistoryUAS,
       "cmOAMFlowPointHistorySES": cmOAMFlowPointHistorySES,
       "cmOAMFlowPointThresholdTable": cmOAMFlowPointThresholdTable,
       "cmOAMFlowPointThresholdEntry": cmOAMFlowPointThresholdEntry,
       "cmOAMFlowPointThresholdIndex": cmOAMFlowPointThresholdIndex,
       "cmOAMFlowPointThresholdInterval": cmOAMFlowPointThresholdInterval,
       "cmOAMFlowPointThresholdVariable": cmOAMFlowPointThresholdVariable,
       "cmOAMFlowPointThresholdValueLo": cmOAMFlowPointThresholdValueLo,
       "cmOAMFlowPointThresholdValueHi": cmOAMFlowPointThresholdValueHi,
       "cmOAMFlowPointThresholdMonValue": cmOAMFlowPointThresholdMonValue,
       "cmQosPolicerV2StatsTable": cmQosPolicerV2StatsTable,
       "cmQosPolicerV2StatsEntry": cmQosPolicerV2StatsEntry,
       "cmQosPolicerV2StatsIndex": cmQosPolicerV2StatsIndex,
       "cmQosPolicerV2StatsIntervalType": cmQosPolicerV2StatsIntervalType,
       "cmQosPolicerV2StatsValid": cmQosPolicerV2StatsValid,
       "cmQosPolicerV2StatsAction": cmQosPolicerV2StatsAction,
       "cmQosPolicerV2StatsFMG": cmQosPolicerV2StatsFMG,
       "cmQosPolicerV2StatsFMY": cmQosPolicerV2StatsFMY,
       "cmQosPolicerV2StatsFMYD": cmQosPolicerV2StatsFMYD,
       "cmQosPolicerV2StatsFMRD": cmQosPolicerV2StatsFMRD,
       "cmQosPolicerV2StatsBytesIn": cmQosPolicerV2StatsBytesIn,
       "cmQosPolicerV2StatsBytesOut": cmQosPolicerV2StatsBytesOut,
       "cmQosPolicerV2StatsABR": cmQosPolicerV2StatsABR,
       "cmQosPolicerV2HistoryTable": cmQosPolicerV2HistoryTable,
       "cmQosPolicerV2HistoryEntry": cmQosPolicerV2HistoryEntry,
       "cmQosPolicerV2HistoryIndex": cmQosPolicerV2HistoryIndex,
       "cmQosPolicerV2HistoryTime": cmQosPolicerV2HistoryTime,
       "cmQosPolicerV2HistoryValid": cmQosPolicerV2HistoryValid,
       "cmQosPolicerV2HistoryAction": cmQosPolicerV2HistoryAction,
       "cmQosPolicerV2HistoryFMG": cmQosPolicerV2HistoryFMG,
       "cmQosPolicerV2HistoryFMY": cmQosPolicerV2HistoryFMY,
       "cmQosPolicerV2HistoryFMYD": cmQosPolicerV2HistoryFMYD,
       "cmQosPolicerV2HistoryFMRD": cmQosPolicerV2HistoryFMRD,
       "cmQosPolicerV2HistoryBytesIn": cmQosPolicerV2HistoryBytesIn,
       "cmQosPolicerV2HistoryBytesOut": cmQosPolicerV2HistoryBytesOut,
       "cmQosPolicerV2HistoryABR": cmQosPolicerV2HistoryABR,
       "cmQosPolicerV2ThresholdTable": cmQosPolicerV2ThresholdTable,
       "cmQosPolicerV2ThresholdEntry": cmQosPolicerV2ThresholdEntry,
       "cmQosPolicerV2ThresholdIndex": cmQosPolicerV2ThresholdIndex,
       "cmQosPolicerV2ThresholdInterval": cmQosPolicerV2ThresholdInterval,
       "cmQosPolicerV2ThresholdVariable": cmQosPolicerV2ThresholdVariable,
       "cmQosPolicerV2ThresholdValueLo": cmQosPolicerV2ThresholdValueLo,
       "cmQosPolicerV2ThresholdValueHi": cmQosPolicerV2ThresholdValueHi,
       "cmQosPolicerV2ThresholdMonValue": cmQosPolicerV2ThresholdMonValue,
       "cmQosShaperV2StatsTable": cmQosShaperV2StatsTable,
       "cmQosShaperV2StatsEntry": cmQosShaperV2StatsEntry,
       "cmQosShaperV2StatsIndex": cmQosShaperV2StatsIndex,
       "cmQosShaperV2StatsIntervalType": cmQosShaperV2StatsIntervalType,
       "cmQosShaperV2StatsValid": cmQosShaperV2StatsValid,
       "cmQosShaperV2StatsAction": cmQosShaperV2StatsAction,
       "cmQosShaperV2StatsBT": cmQosShaperV2StatsBT,
       "cmQosShaperV2StatsBTD": cmQosShaperV2StatsBTD,
       "cmQosShaperV2StatsFD": cmQosShaperV2StatsFD,
       "cmQosShaperV2StatsFTD": cmQosShaperV2StatsFTD,
       "cmQosShaperV2StatsABRRL": cmQosShaperV2StatsABRRL,
       "cmQosShaperV2StatsBREDD": cmQosShaperV2StatsBREDD,
       "cmQosShaperV2StatsFREDD": cmQosShaperV2StatsFREDD,
       "cmQosShaperV2HistoryTable": cmQosShaperV2HistoryTable,
       "cmQosShaperV2HistoryEntry": cmQosShaperV2HistoryEntry,
       "cmQosShaperV2HistoryIndex": cmQosShaperV2HistoryIndex,
       "cmQosShaperV2HistoryTime": cmQosShaperV2HistoryTime,
       "cmQosShaperV2HistoryValid": cmQosShaperV2HistoryValid,
       "cmQosShaperV2HistoryAction": cmQosShaperV2HistoryAction,
       "cmQosShaperV2HistoryBT": cmQosShaperV2HistoryBT,
       "cmQosShaperV2HistoryBTD": cmQosShaperV2HistoryBTD,
       "cmQosShaperV2HistoryFD": cmQosShaperV2HistoryFD,
       "cmQosShaperV2HistoryFTD": cmQosShaperV2HistoryFTD,
       "cmQosShaperV2HistoryABRRL": cmQosShaperV2HistoryABRRL,
       "cmQosShaperV2HistoryBREDD": cmQosShaperV2HistoryBREDD,
       "cmQosShaperV2HistoryFREDD": cmQosShaperV2HistoryFREDD,
       "cmQosShaperV2ThresholdTable": cmQosShaperV2ThresholdTable,
       "cmQosShaperV2ThresholdEntry": cmQosShaperV2ThresholdEntry,
       "cmQosShaperV2ThresholdIndex": cmQosShaperV2ThresholdIndex,
       "cmQosShaperV2ThresholdInterval": cmQosShaperV2ThresholdInterval,
       "cmQosShaperV2ThresholdVariable": cmQosShaperV2ThresholdVariable,
       "cmQosShaperV2ThresholdValueLo": cmQosShaperV2ThresholdValueLo,
       "cmQosShaperV2ThresholdValueHi": cmQosShaperV2ThresholdValueHi,
       "cmQosShaperV2ThresholdMonValue": cmQosShaperV2ThresholdMonValue,
       "cmLagStatsTable": cmLagStatsTable,
       "cmLagStatsEntry": cmLagStatsEntry,
       "cmLagStatsIndex": cmLagStatsIndex,
       "cmLagStatsIntervalType": cmLagStatsIntervalType,
       "cmLagStatsValid": cmLagStatsValid,
       "cmLagStatsAction": cmLagStatsAction,
       "cmLagStatsESBF": cmLagStatsESBF,
       "cmLagStatsESBP": cmLagStatsESBP,
       "cmLagStatsESBS": cmLagStatsESBS,
       "cmLagStatsESC": cmLagStatsESC,
       "cmLagStatsESCAE": cmLagStatsESCAE,
       "cmLagStatsESDE": cmLagStatsESDE,
       "cmLagStatsESF": cmLagStatsESF,
       "cmLagStatsESFS": cmLagStatsESFS,
       "cmLagStatsESJ": cmLagStatsESJ,
       "cmLagStatsESMF": cmLagStatsESMF,
       "cmLagStatsESMP": cmLagStatsESMP,
       "cmLagStatsESO": cmLagStatsESO,
       "cmLagStatsESOF": cmLagStatsESOF,
       "cmLagStatsESOP": cmLagStatsESOP,
       "cmLagStatsESP": cmLagStatsESP,
       "cmLagStatsESP64": cmLagStatsESP64,
       "cmLagStatsESP65": cmLagStatsESP65,
       "cmLagStatsESP128": cmLagStatsESP128,
       "cmLagStatsESP256": cmLagStatsESP256,
       "cmLagStatsESP512": cmLagStatsESP512,
       "cmLagStatsESP1024": cmLagStatsESP1024,
       "cmLagStatsESP1519": cmLagStatsESP1519,
       "cmLagStatsESUF": cmLagStatsESUF,
       "cmLagStatsESUP": cmLagStatsESUP,
       "cmLagStatsL2CPFD": cmLagStatsL2CPFD,
       "cmLagStatsL2CPFP": cmLagStatsL2CPFP,
       "cmLagStatsAUFD": cmLagStatsAUFD,
       "cmLagStatsAPFD": cmLagStatsAPFD,
       "cmLagStatsABRRx": cmLagStatsABRRx,
       "cmLagStatsABRTx": cmLagStatsABRTx,
       "cmLagStatsATFD": cmLagStatsATFD,
       "cmLagStatsLkupFails": cmLagStatsLkupFails,
       "cmLagHistoryTable": cmLagHistoryTable,
       "cmLagHistoryEntry": cmLagHistoryEntry,
       "cmLagHistoryIndex": cmLagHistoryIndex,
       "cmLagHistoryTime": cmLagHistoryTime,
       "cmLagHistoryValid": cmLagHistoryValid,
       "cmLagHistoryAction": cmLagHistoryAction,
       "cmLagHistoryESBF": cmLagHistoryESBF,
       "cmLagHistoryESBP": cmLagHistoryESBP,
       "cmLagHistoryESBS": cmLagHistoryESBS,
       "cmLagHistoryESC": cmLagHistoryESC,
       "cmLagHistoryESCAE": cmLagHistoryESCAE,
       "cmLagHistoryESDE": cmLagHistoryESDE,
       "cmLagHistoryESF": cmLagHistoryESF,
       "cmLagHistoryESFS": cmLagHistoryESFS,
       "cmLagHistoryESJ": cmLagHistoryESJ,
       "cmLagHistoryESMF": cmLagHistoryESMF,
       "cmLagHistoryESMP": cmLagHistoryESMP,
       "cmLagHistoryESO": cmLagHistoryESO,
       "cmLagHistoryESOF": cmLagHistoryESOF,
       "cmLagHistoryESOP": cmLagHistoryESOP,
       "cmLagHistoryESP": cmLagHistoryESP,
       "cmLagHistoryESP64": cmLagHistoryESP64,
       "cmLagHistoryESP65": cmLagHistoryESP65,
       "cmLagHistoryESP128": cmLagHistoryESP128,
       "cmLagHistoryESP256": cmLagHistoryESP256,
       "cmLagHistoryESP512": cmLagHistoryESP512,
       "cmLagHistoryESP1024": cmLagHistoryESP1024,
       "cmLagHistoryESP1519": cmLagHistoryESP1519,
       "cmLagHistoryESUF": cmLagHistoryESUF,
       "cmLagHistoryESUP": cmLagHistoryESUP,
       "cmLagHistoryL2CPFD": cmLagHistoryL2CPFD,
       "cmLagHistoryL2CPFP": cmLagHistoryL2CPFP,
       "cmLagHistoryAUFD": cmLagHistoryAUFD,
       "cmLagHistoryAPFD": cmLagHistoryAPFD,
       "cmLagHistoryABRRx": cmLagHistoryABRRx,
       "cmLagHistoryABRTx": cmLagHistoryABRTx,
       "cmLagHistoryATFD": cmLagHistoryATFD,
       "cmLagHistoryLkupFails": cmLagHistoryLkupFails,
       "cmLagThresholdTable": cmLagThresholdTable,
       "cmLagThresholdEntry": cmLagThresholdEntry,
       "cmLagThresholdIndex": cmLagThresholdIndex,
       "cmLagThresholdInterval": cmLagThresholdInterval,
       "cmLagThresholdVariable": cmLagThresholdVariable,
       "cmLagThresholdValueLo": cmLagThresholdValueLo,
       "cmLagThresholdValueHi": cmLagThresholdValueHi,
       "cmLagThresholdMonValue": cmLagThresholdMonValue,
       "cmTrafficPortQosShaperStatsTable": cmTrafficPortQosShaperStatsTable,
       "cmTrafficPortQosShaperStatsEntry": cmTrafficPortQosShaperStatsEntry,
       "cmTrafficPortQosShaperStatsIndex": cmTrafficPortQosShaperStatsIndex,
       "cmTrafficPortQosShaperStatsIntervalType": cmTrafficPortQosShaperStatsIntervalType,
       "cmTrafficPortQosShaperStatsValid": cmTrafficPortQosShaperStatsValid,
       "cmTrafficPortQosShaperStatsAction": cmTrafficPortQosShaperStatsAction,
       "cmTrafficPortQosShaperStatsBT": cmTrafficPortQosShaperStatsBT,
       "cmTrafficPortQosShaperStatsBTD": cmTrafficPortQosShaperStatsBTD,
       "cmTrafficPortQosShaperStatsFD": cmTrafficPortQosShaperStatsFD,
       "cmTrafficPortQosShaperStatsFTD": cmTrafficPortQosShaperStatsFTD,
       "cmTrafficPortQosShaperStatsABRRL": cmTrafficPortQosShaperStatsABRRL,
       "cmTrafficPortQosShaperStatsBREDD": cmTrafficPortQosShaperStatsBREDD,
       "cmTrafficPortQosShaperStatsFREDD": cmTrafficPortQosShaperStatsFREDD,
       "cmTrafficPortQosShaperHistoryTable": cmTrafficPortQosShaperHistoryTable,
       "cmTrafficPortQosShaperHistoryEntry": cmTrafficPortQosShaperHistoryEntry,
       "cmTrafficPortQosShaperHistoryIndex": cmTrafficPortQosShaperHistoryIndex,
       "cmTrafficPortQosShaperHistoryTime": cmTrafficPortQosShaperHistoryTime,
       "cmTrafficPortQosShaperHistoryValid": cmTrafficPortQosShaperHistoryValid,
       "cmTrafficPortQosShaperHistoryAction": cmTrafficPortQosShaperHistoryAction,
       "cmTrafficPortQosShaperHistoryBT": cmTrafficPortQosShaperHistoryBT,
       "cmTrafficPortQosShaperHistoryBTD": cmTrafficPortQosShaperHistoryBTD,
       "cmTrafficPortQosShaperHistoryFD": cmTrafficPortQosShaperHistoryFD,
       "cmTrafficPortQosShaperHistoryFTD": cmTrafficPortQosShaperHistoryFTD,
       "cmTrafficPortQosShaperHistoryABRRL": cmTrafficPortQosShaperHistoryABRRL,
       "cmTrafficPortQosShaperHistoryBREDD": cmTrafficPortQosShaperHistoryBREDD,
       "cmTrafficPortQosShaperHistoryFREDD": cmTrafficPortQosShaperHistoryFREDD,
       "cmTrafficPortQosShaperThresholdTable": cmTrafficPortQosShaperThresholdTable,
       "cmTrafficPortQosShaperThresholdEntry": cmTrafficPortQosShaperThresholdEntry,
       "cmTrafficPortQosShaperThresholdIndex": cmTrafficPortQosShaperThresholdIndex,
       "cmTrafficPortQosShaperThresholdInterval": cmTrafficPortQosShaperThresholdInterval,
       "cmTrafficPortQosShaperThresholdVariable": cmTrafficPortQosShaperThresholdVariable,
       "cmTrafficPortQosShaperThresholdValueLo": cmTrafficPortQosShaperThresholdValueLo,
       "cmTrafficPortQosShaperThresholdValueHi": cmTrafficPortQosShaperThresholdValueHi,
       "cmTrafficPortQosShaperThresholdMonValue": cmTrafficPortQosShaperThresholdMonValue,
       "f3NetPortQosShaperStatsTable": f3NetPortQosShaperStatsTable,
       "f3NetPortQosShaperStatsEntry": f3NetPortQosShaperStatsEntry,
       "f3NetPortQosShaperStatsIndex": f3NetPortQosShaperStatsIndex,
       "f3NetPortQosShaperStatsIntervalType": f3NetPortQosShaperStatsIntervalType,
       "f3NetPortQosShaperStatsValid": f3NetPortQosShaperStatsValid,
       "f3NetPortQosShaperStatsAction": f3NetPortQosShaperStatsAction,
       "f3NetPortQosShaperStatsBT": f3NetPortQosShaperStatsBT,
       "f3NetPortQosShaperStatsBTD": f3NetPortQosShaperStatsBTD,
       "f3NetPortQosShaperStatsFD": f3NetPortQosShaperStatsFD,
       "f3NetPortQosShaperStatsFTD": f3NetPortQosShaperStatsFTD,
       "f3NetPortQosShaperStatsBR": f3NetPortQosShaperStatsBR,
       "f3NetPortQosShaperStatsFR": f3NetPortQosShaperStatsFR,
       "f3NetPortQosShaperStatsABRRL": f3NetPortQosShaperStatsABRRL,
       "f3NetPortQosShaperStatsBREDD": f3NetPortQosShaperStatsBREDD,
       "f3NetPortQosShaperStatsFREDD": f3NetPortQosShaperStatsFREDD,
       "f3NetPortQosShaperHistoryTable": f3NetPortQosShaperHistoryTable,
       "f3NetPortQosShaperHistoryEntry": f3NetPortQosShaperHistoryEntry,
       "f3NetPortQosShaperHistoryIndex": f3NetPortQosShaperHistoryIndex,
       "f3NetPortQosShaperHistoryTime": f3NetPortQosShaperHistoryTime,
       "f3NetPortQosShaperHistoryValid": f3NetPortQosShaperHistoryValid,
       "f3NetPortQosShaperHistoryAction": f3NetPortQosShaperHistoryAction,
       "f3NetPortQosShaperHistoryBT": f3NetPortQosShaperHistoryBT,
       "f3NetPortQosShaperHistoryBTD": f3NetPortQosShaperHistoryBTD,
       "f3NetPortQosShaperHistoryFD": f3NetPortQosShaperHistoryFD,
       "f3NetPortQosShaperHistoryFTD": f3NetPortQosShaperHistoryFTD,
       "f3NetPortQosShaperHistoryBR": f3NetPortQosShaperHistoryBR,
       "f3NetPortQosShaperHistoryFR": f3NetPortQosShaperHistoryFR,
       "f3NetPortQosShaperHistoryABRRL": f3NetPortQosShaperHistoryABRRL,
       "f3NetPortQosShaperHistoryBREDD": f3NetPortQosShaperHistoryBREDD,
       "f3NetPortQosShaperHistoryFREDD": f3NetPortQosShaperHistoryFREDD,
       "f3NetPortQosShaperThresholdTable": f3NetPortQosShaperThresholdTable,
       "f3NetPortQosShaperThresholdEntry": f3NetPortQosShaperThresholdEntry,
       "f3NetPortQosShaperThresholdIndex": f3NetPortQosShaperThresholdIndex,
       "f3NetPortQosShaperThresholdInterval": f3NetPortQosShaperThresholdInterval,
       "f3NetPortQosShaperThresholdVariable": f3NetPortQosShaperThresholdVariable,
       "f3NetPortQosShaperThresholdValueLo": f3NetPortQosShaperThresholdValueLo,
       "f3NetPortQosShaperThresholdValueHi": f3NetPortQosShaperThresholdValueHi,
       "f3NetPortQosShaperThresholdMonValue": f3NetPortQosShaperThresholdMonValue,
       "ocnStmStatsTable": ocnStmStatsTable,
       "ocnStmStatsEntry": ocnStmStatsEntry,
       "ocnStmStatsIndex": ocnStmStatsIndex,
       "ocnStmStatsIntervalType": ocnStmStatsIntervalType,
       "ocnStmStatsValid": ocnStmStatsValid,
       "ocnStmStatsAction": ocnStmStatsAction,
       "ocnStmStatsLineLBC": ocnStmStatsLineLBC,
       "ocnStmStatsLineOPT": ocnStmStatsLineOPT,
       "ocnStmStatsLineOPR": ocnStmStatsLineOPR,
       "ocnStmStatsLineTemp": ocnStmStatsLineTemp,
       "ocnStmStatsLinePSC": ocnStmStatsLinePSC,
       "ocnStmStatsLineESs": ocnStmStatsLineESs,
       "ocnStmStatsLineSESs": ocnStmStatsLineSESs,
       "ocnStmStatsLineCVs": ocnStmStatsLineCVs,
       "ocnStmStatsLineUASs": ocnStmStatsLineUASs,
       "ocnStmStatsLineFCs": ocnStmStatsLineFCs,
       "ocnStmStatsLineFarEndESs": ocnStmStatsLineFarEndESs,
       "ocnStmStatsLineFarEndSESs": ocnStmStatsLineFarEndSESs,
       "ocnStmStatsLineFarEndCVs": ocnStmStatsLineFarEndCVs,
       "ocnStmStatsLineFarEndUASs": ocnStmStatsLineFarEndUASs,
       "ocnStmStatsSectionESs": ocnStmStatsSectionESs,
       "ocnStmStatsSectionSESs": ocnStmStatsSectionSESs,
       "ocnStmStatsSectionCVs": ocnStmStatsSectionCVs,
       "ocnStmStatsSectionSEFs": ocnStmStatsSectionSEFs,
       "ocnStmStatsSectionUASs": ocnStmStatsSectionUASs,
       "ocnStmHistoryTable": ocnStmHistoryTable,
       "ocnStmHistoryEntry": ocnStmHistoryEntry,
       "ocnStmHistoryIndex": ocnStmHistoryIndex,
       "ocnStmHistoryTime": ocnStmHistoryTime,
       "ocnStmHistoryValid": ocnStmHistoryValid,
       "ocnStmHistoryAction": ocnStmHistoryAction,
       "ocnStmHistoryLineLBC": ocnStmHistoryLineLBC,
       "ocnStmHistoryLineOPT": ocnStmHistoryLineOPT,
       "ocnStmHistoryLineOPR": ocnStmHistoryLineOPR,
       "ocnStmHistoryLineTemp": ocnStmHistoryLineTemp,
       "ocnStmHistoryLinePSC": ocnStmHistoryLinePSC,
       "ocnStmHistoryLineESs": ocnStmHistoryLineESs,
       "ocnStmHistoryLineSESs": ocnStmHistoryLineSESs,
       "ocnStmHistoryLineCVs": ocnStmHistoryLineCVs,
       "ocnStmHistoryLineUASs": ocnStmHistoryLineUASs,
       "ocnStmHistoryLineFCs": ocnStmHistoryLineFCs,
       "ocnStmHistoryLineFarEndESs": ocnStmHistoryLineFarEndESs,
       "ocnStmHistoryLineFarEndSESs": ocnStmHistoryLineFarEndSESs,
       "ocnStmHistoryLineFarEndCVs": ocnStmHistoryLineFarEndCVs,
       "ocnStmHistoryLineFarEndUASs": ocnStmHistoryLineFarEndUASs,
       "ocnStmHistorySectionESs": ocnStmHistorySectionESs,
       "ocnStmHistorySectionSESs": ocnStmHistorySectionSESs,
       "ocnStmHistorySectionCVs": ocnStmHistorySectionCVs,
       "ocnStmHistorySectionSEFs": ocnStmHistorySectionSEFs,
       "ocnStmHistorySectionUASs": ocnStmHistorySectionUASs,
       "ocnStmThresholdTable": ocnStmThresholdTable,
       "ocnStmThresholdEntry": ocnStmThresholdEntry,
       "ocnStmThresholdIndex": ocnStmThresholdIndex,
       "ocnStmThresholdInterval": ocnStmThresholdInterval,
       "ocnStmThresholdVariable": ocnStmThresholdVariable,
       "ocnStmThresholdValueLo": ocnStmThresholdValueLo,
       "ocnStmThresholdValueHi": ocnStmThresholdValueHi,
       "ocnStmThresholdMonValue": ocnStmThresholdMonValue,
       "stsVcPathStatsTable": stsVcPathStatsTable,
       "stsVcPathStatsEntry": stsVcPathStatsEntry,
       "stsVcPathStatsIndex": stsVcPathStatsIndex,
       "stsVcPathStatsIntervalType": stsVcPathStatsIntervalType,
       "stsVcPathStatsValid": stsVcPathStatsValid,
       "stsVcPathStatsAction": stsVcPathStatsAction,
       "stsVcPathStatsESs": stsVcPathStatsESs,
       "stsVcPathStatsSESs": stsVcPathStatsSESs,
       "stsVcPathStatsCVs": stsVcPathStatsCVs,
       "stsVcPathStatsUASs": stsVcPathStatsUASs,
       "stsVcPathFarEndStatsESs": stsVcPathFarEndStatsESs,
       "stsVcPathFarEndStatsSESs": stsVcPathFarEndStatsSESs,
       "stsVcPathFarEndStatsCVs": stsVcPathFarEndStatsCVs,
       "stsVcPathFarEndStatsUASs": stsVcPathFarEndStatsUASs,
       "stsVcPathHistoryTable": stsVcPathHistoryTable,
       "stsVcPathHistoryEntry": stsVcPathHistoryEntry,
       "stsVcPathHistoryIndex": stsVcPathHistoryIndex,
       "stsVcPathHistoryTime": stsVcPathHistoryTime,
       "stsVcPathHistoryValid": stsVcPathHistoryValid,
       "stsVcPathHistoryAction": stsVcPathHistoryAction,
       "stsVcPathHistoryESs": stsVcPathHistoryESs,
       "stsVcPathHistorySESs": stsVcPathHistorySESs,
       "stsVcPathHistoryCVs": stsVcPathHistoryCVs,
       "stsVcPathHistoryUASs": stsVcPathHistoryUASs,
       "stsVcPathFarEndHistoryESs": stsVcPathFarEndHistoryESs,
       "stsVcPathFarEndHistorySESs": stsVcPathFarEndHistorySESs,
       "stsVcPathFarEndHistoryCVs": stsVcPathFarEndHistoryCVs,
       "stsVcPathFarEndHistoryUASs": stsVcPathFarEndHistoryUASs,
       "stsVcPathThresholdTable": stsVcPathThresholdTable,
       "stsVcPathThresholdEntry": stsVcPathThresholdEntry,
       "stsVcPathThresholdIndex": stsVcPathThresholdIndex,
       "stsVcPathThresholdInterval": stsVcPathThresholdInterval,
       "stsVcPathThresholdVariable": stsVcPathThresholdVariable,
       "stsVcPathThresholdValueLo": stsVcPathThresholdValueLo,
       "stsVcPathThresholdValueHi": stsVcPathThresholdValueHi,
       "stsVcPathThresholdMonValue": stsVcPathThresholdMonValue,
       "vtVcPathStatsTable": vtVcPathStatsTable,
       "vtVcPathStatsEntry": vtVcPathStatsEntry,
       "vtVcPathStatsIndex": vtVcPathStatsIndex,
       "vtVcPathStatsIntervalType": vtVcPathStatsIntervalType,
       "vtVcPathStatsValid": vtVcPathStatsValid,
       "vtVcPathStatsAction": vtVcPathStatsAction,
       "vtVcPathStatsESs": vtVcPathStatsESs,
       "vtVcPathStatsSESs": vtVcPathStatsSESs,
       "vtVcPathStatsCVs": vtVcPathStatsCVs,
       "vtVcPathStatsUASs": vtVcPathStatsUASs,
       "vtVcPathFarEndStatsESs": vtVcPathFarEndStatsESs,
       "vtVcPathFarEndStatsSESs": vtVcPathFarEndStatsSESs,
       "vtVcPathFarEndStatsCVs": vtVcPathFarEndStatsCVs,
       "vtVcPathFarEndStatsUASs": vtVcPathFarEndStatsUASs,
       "vtVcPathHistoryTable": vtVcPathHistoryTable,
       "vtVcPathHistoryEntry": vtVcPathHistoryEntry,
       "vtVcPathHistoryIndex": vtVcPathHistoryIndex,
       "vtVcPathHistoryTime": vtVcPathHistoryTime,
       "vtVcPathHistoryValid": vtVcPathHistoryValid,
       "vtVcPathHistoryAction": vtVcPathHistoryAction,
       "vtVcPathHistoryESs": vtVcPathHistoryESs,
       "vtVcPathHistorySESs": vtVcPathHistorySESs,
       "vtVcPathHistoryCVs": vtVcPathHistoryCVs,
       "vtVcPathHistoryUASs": vtVcPathHistoryUASs,
       "vtVcPathFarEndHistoryESs": vtVcPathFarEndHistoryESs,
       "vtVcPathFarEndHistorySESs": vtVcPathFarEndHistorySESs,
       "vtVcPathFarEndHistoryCVs": vtVcPathFarEndHistoryCVs,
       "vtVcPathFarEndHistoryUASs": vtVcPathFarEndHistoryUASs,
       "vtVcPathThresholdTable": vtVcPathThresholdTable,
       "vtVcPathThresholdEntry": vtVcPathThresholdEntry,
       "vtVcPathThresholdIndex": vtVcPathThresholdIndex,
       "vtVcPathThresholdInterval": vtVcPathThresholdInterval,
       "vtVcPathThresholdVariable": vtVcPathThresholdVariable,
       "vtVcPathThresholdValueLo": vtVcPathThresholdValueLo,
       "vtVcPathThresholdValueHi": vtVcPathThresholdValueHi,
       "vtVcPathThresholdMonValue": vtVcPathThresholdMonValue,
       "e1t1StatsTable": e1t1StatsTable,
       "e1t1StatsEntry": e1t1StatsEntry,
       "e1t1StatsIndex": e1t1StatsIndex,
       "e1t1StatsIntervalType": e1t1StatsIntervalType,
       "e1t1StatsValid": e1t1StatsValid,
       "e1t1StatsAction": e1t1StatsAction,
       "e1t1StatsLineCVs": e1t1StatsLineCVs,
       "e1t1StatsLineESs": e1t1StatsLineESs,
       "e1t1StatsLineSESs": e1t1StatsLineSESs,
       "e1t1StatsLineESsFarEnd": e1t1StatsLineESsFarEnd,
       "e1t1StatsLineUASs": e1t1StatsLineUASs,
       "e1t1StatsLineLOSSs": e1t1StatsLineLOSSs,
       "e1t1StatsPathCVs": e1t1StatsPathCVs,
       "e1t1StatsPathESs": e1t1StatsPathESs,
       "e1t1StatsPathSESs": e1t1StatsPathSESs,
       "e1t1StatsPathUASs": e1t1StatsPathUASs,
       "e1t1StatsPathCVsFarEnd": e1t1StatsPathCVsFarEnd,
       "e1t1StatsPathESsFarEnd": e1t1StatsPathESsFarEnd,
       "e1t1StatsPathSESsFarEnd": e1t1StatsPathSESsFarEnd,
       "e1t1StatsPathSEFsFarEnd": e1t1StatsPathSEFsFarEnd,
       "e1t1StatsPathUASsFarEnd": e1t1StatsPathUASsFarEnd,
       "e1t1StatsPathFCs": e1t1StatsPathFCs,
       "e1t1StatsPathFCsFarEnd": e1t1StatsPathFCsFarEnd,
       "e1t1StatsPathAISs": e1t1StatsPathAISs,
       "e1t1StatsPathSASs": e1t1StatsPathSASs,
       "e1t1HistoryTable": e1t1HistoryTable,
       "e1t1HistoryEntry": e1t1HistoryEntry,
       "e1t1HistoryIndex": e1t1HistoryIndex,
       "e1t1HistoryTime": e1t1HistoryTime,
       "e1t1HistoryValid": e1t1HistoryValid,
       "e1t1HistoryAction": e1t1HistoryAction,
       "e1t1HistoryLineCVs": e1t1HistoryLineCVs,
       "e1t1HistoryLineESs": e1t1HistoryLineESs,
       "e1t1HistoryLineSESs": e1t1HistoryLineSESs,
       "e1t1HistoryLineESsFarEnd": e1t1HistoryLineESsFarEnd,
       "e1t1HistoryLineUASs": e1t1HistoryLineUASs,
       "e1t1HistoryLineLOSSs": e1t1HistoryLineLOSSs,
       "e1t1HistoryPathCVs": e1t1HistoryPathCVs,
       "e1t1HistoryPathESs": e1t1HistoryPathESs,
       "e1t1HistoryPathSESs": e1t1HistoryPathSESs,
       "e1t1HistoryPathUASs": e1t1HistoryPathUASs,
       "e1t1HistoryPathCVsFarEnd": e1t1HistoryPathCVsFarEnd,
       "e1t1HistoryPathESsFarEnd": e1t1HistoryPathESsFarEnd,
       "e1t1HistoryPathSESsFarEnd": e1t1HistoryPathSESsFarEnd,
       "e1t1HistoryPathSEFsFarEnd": e1t1HistoryPathSEFsFarEnd,
       "e1t1HistoryPathUASsFarEnd": e1t1HistoryPathUASsFarEnd,
       "e1t1HistoryPathFCs": e1t1HistoryPathFCs,
       "e1t1HistoryPathFCsFarEnd": e1t1HistoryPathFCsFarEnd,
       "e1t1HistoryPathAISs": e1t1HistoryPathAISs,
       "e1t1HistoryPathSASs": e1t1HistoryPathSASs,
       "e1t1ThresholdTable": e1t1ThresholdTable,
       "e1t1ThresholdEntry": e1t1ThresholdEntry,
       "e1t1ThresholdIndex": e1t1ThresholdIndex,
       "e1t1ThresholdInterval": e1t1ThresholdInterval,
       "e1t1ThresholdVariable": e1t1ThresholdVariable,
       "e1t1ThresholdValueLo": e1t1ThresholdValueLo,
       "e1t1ThresholdValueHi": e1t1ThresholdValueHi,
       "e1t1ThresholdMonValue": e1t1ThresholdMonValue,
       "e3t3StatsTable": e3t3StatsTable,
       "e3t3StatsEntry": e3t3StatsEntry,
       "e3t3StatsIndex": e3t3StatsIndex,
       "e3t3StatsIntervalType": e3t3StatsIntervalType,
       "e3t3StatsValid": e3t3StatsValid,
       "e3t3StatsAction": e3t3StatsAction,
       "e3t3StatsLineCVs": e3t3StatsLineCVs,
       "e3t3StatsLineESs": e3t3StatsLineESs,
       "e3t3StatsLineSESs": e3t3StatsLineSESs,
       "e3t3StatsLineLOSSs": e3t3StatsLineLOSSs,
       "e3t3StatsPathPCVs": e3t3StatsPathPCVs,
       "e3t3StatsPathCCVs": e3t3StatsPathCCVs,
       "e3t3StatsPathAISs": e3t3StatsPathAISs,
       "e3t3StatsPathPESs": e3t3StatsPathPESs,
       "e3t3StatsPathCESs": e3t3StatsPathCESs,
       "e3t3StatsPathFCs": e3t3StatsPathFCs,
       "e3t3StatsPathSEFs": e3t3StatsPathSEFs,
       "e3t3StatsPathPSESs": e3t3StatsPathPSESs,
       "e3t3StatsPathCSESs": e3t3StatsPathCSESs,
       "e3t3StatsPathPUASs": e3t3StatsPathPUASs,
       "e3t3StatsPathCUASs": e3t3StatsPathCUASs,
       "e3t3StatsPathCCVsFarEnd": e3t3StatsPathCCVsFarEnd,
       "e3t3StatsPathCESsFarEnd": e3t3StatsPathCESsFarEnd,
       "e3t3StatsPathCSESsFarEnd": e3t3StatsPathCSESsFarEnd,
       "e3t3StatsPathCFCsFarEnd": e3t3StatsPathCFCsFarEnd,
       "e3t3StatsPathCUASsFarEnd": e3t3StatsPathCUASsFarEnd,
       "e3t3HistoryTable": e3t3HistoryTable,
       "e3t3HistoryEntry": e3t3HistoryEntry,
       "e3t3HistoryIndex": e3t3HistoryIndex,
       "e3t3HistoryTime": e3t3HistoryTime,
       "e3t3HistoryValid": e3t3HistoryValid,
       "e3t3HistoryAction": e3t3HistoryAction,
       "e3t3HistoryLineCVs": e3t3HistoryLineCVs,
       "e3t3HistoryLineESs": e3t3HistoryLineESs,
       "e3t3HistoryLineSESs": e3t3HistoryLineSESs,
       "e3t3HistoryLineLOSSs": e3t3HistoryLineLOSSs,
       "e3t3HistoryPathPCVs": e3t3HistoryPathPCVs,
       "e3t3HistoryPathCCVs": e3t3HistoryPathCCVs,
       "e3t3HistoryPathAISs": e3t3HistoryPathAISs,
       "e3t3HistoryPathPESs": e3t3HistoryPathPESs,
       "e3t3HistoryPathCESs": e3t3HistoryPathCESs,
       "e3t3HistoryPathFCs": e3t3HistoryPathFCs,
       "e3t3HistoryPathSEFs": e3t3HistoryPathSEFs,
       "e3t3HistoryPathPSESs": e3t3HistoryPathPSESs,
       "e3t3HistoryPathCSESs": e3t3HistoryPathCSESs,
       "e3t3HistoryPathPUASs": e3t3HistoryPathPUASs,
       "e3t3HistoryPathCUASs": e3t3HistoryPathCUASs,
       "e3t3HistoryPathCCVsFarEnd": e3t3HistoryPathCCVsFarEnd,
       "e3t3HistoryPathCESsFarEnd": e3t3HistoryPathCESsFarEnd,
       "e3t3HistoryPathCSESsFarEnd": e3t3HistoryPathCSESsFarEnd,
       "e3t3HistoryPathCFCsFarEnd": e3t3HistoryPathCFCsFarEnd,
       "e3t3HistoryPathCUASsFarEnd": e3t3HistoryPathCUASsFarEnd,
       "e3t3ThresholdTable": e3t3ThresholdTable,
       "e3t3ThresholdEntry": e3t3ThresholdEntry,
       "e3t3ThresholdIndex": e3t3ThresholdIndex,
       "e3t3ThresholdInterval": e3t3ThresholdInterval,
       "e3t3ThresholdVariable": e3t3ThresholdVariable,
       "e3t3ThresholdValueLo": e3t3ThresholdValueLo,
       "e3t3ThresholdValueHi": e3t3ThresholdValueHi,
       "e3t3ThresholdMonValue": e3t3ThresholdMonValue,
       "cmFlowBWExtTable": cmFlowBWExtTable,
       "cmFlowBWExtEntry": cmFlowBWExtEntry,
       "cmFlowBWA2NCIR": cmFlowBWA2NCIR,
       "cmFlowBWA2NEIR": cmFlowBWA2NEIR,
       "cmFlowBWN2ACIR": cmFlowBWN2ACIR,
       "cmFlowBWN2AEIR": cmFlowBWN2AEIR,
       "cmFlowBWA2NGFB": cmFlowBWA2NGFB,
       "cmFlowBWA2NMFB": cmFlowBWA2NMFB,
       "ocnStmThresholdVarTable": ocnStmThresholdVarTable,
       "ocnStmThresholdVarEntry": ocnStmThresholdVarEntry,
       "ocnStmThresholdVarOprVariance": ocnStmThresholdVarOprVariance,
       "ocnStmThresholdVarOptVariance": ocnStmThresholdVarOptVariance,
       "cmPerfScalarObjects": cmPerfScalarObjects,
       "cmPerQueryGenControl": cmPerQueryGenControl,
       "f3FpQosShaperStatsTable": f3FpQosShaperStatsTable,
       "f3FpQosShaperStatsEntry": f3FpQosShaperStatsEntry,
       "f3FpQosShaperStatsIndex": f3FpQosShaperStatsIndex,
       "f3FpQosShaperStatsIntervalType": f3FpQosShaperStatsIntervalType,
       "f3FpQosShaperStatsValid": f3FpQosShaperStatsValid,
       "f3FpQosShaperStatsAction": f3FpQosShaperStatsAction,
       "f3FpQosShaperStatsBT": f3FpQosShaperStatsBT,
       "f3FpQosShaperStatsBTD": f3FpQosShaperStatsBTD,
       "f3FpQosShaperStatsFD": f3FpQosShaperStatsFD,
       "f3FpQosShaperStatsFTD": f3FpQosShaperStatsFTD,
       "f3FpQosShaperStatsABRRL": f3FpQosShaperStatsABRRL,
       "f3FpQosShaperStatsBREDD": f3FpQosShaperStatsBREDD,
       "f3FpQosShaperStatsFREDD": f3FpQosShaperStatsFREDD,
       "f3FpQosShaperHistoryTable": f3FpQosShaperHistoryTable,
       "f3FpQosShaperHistoryEntry": f3FpQosShaperHistoryEntry,
       "f3FpQosShaperHistoryIndex": f3FpQosShaperHistoryIndex,
       "f3FpQosShaperHistoryTime": f3FpQosShaperHistoryTime,
       "f3FpQosShaperHistoryValid": f3FpQosShaperHistoryValid,
       "f3FpQosShaperHistoryAction": f3FpQosShaperHistoryAction,
       "f3FpQosShaperHistoryBT": f3FpQosShaperHistoryBT,
       "f3FpQosShaperHistoryBTD": f3FpQosShaperHistoryBTD,
       "f3FpQosShaperHistoryFD": f3FpQosShaperHistoryFD,
       "f3FpQosShaperHistoryFTD": f3FpQosShaperHistoryFTD,
       "f3FpQosShaperHistoryABRRL": f3FpQosShaperHistoryABRRL,
       "f3FpQosShaperHistoryBREDD": f3FpQosShaperHistoryBREDD,
       "f3FpQosShaperHistoryFREDD": f3FpQosShaperHistoryFREDD,
       "f3FpQosShaperThresholdTable": f3FpQosShaperThresholdTable,
       "f3FpQosShaperThresholdEntry": f3FpQosShaperThresholdEntry,
       "f3FpQosShaperThresholdIndex": f3FpQosShaperThresholdIndex,
       "f3FpQosShaperThresholdInterval": f3FpQosShaperThresholdInterval,
       "f3FpQosShaperThresholdVariable": f3FpQosShaperThresholdVariable,
       "f3FpQosShaperThresholdValueLo": f3FpQosShaperThresholdValueLo,
       "f3FpQosShaperThresholdValueHi": f3FpQosShaperThresholdValueHi,
       "f3FpQosShaperThresholdMonValue": f3FpQosShaperThresholdMonValue,
       "f3FpQosPolicerStatsTable": f3FpQosPolicerStatsTable,
       "f3FpQosPolicerStatsEntry": f3FpQosPolicerStatsEntry,
       "f3FpQosPolicerStatsIndex": f3FpQosPolicerStatsIndex,
       "f3FpQosPolicerStatsIntervalType": f3FpQosPolicerStatsIntervalType,
       "f3FpQosPolicerStatsValid": f3FpQosPolicerStatsValid,
       "f3FpQosPolicerStatsAction": f3FpQosPolicerStatsAction,
       "f3FpQosPolicerStatsFMG": f3FpQosPolicerStatsFMG,
       "f3FpQosPolicerStatsFMY": f3FpQosPolicerStatsFMY,
       "f3FpQosPolicerStatsFMRD": f3FpQosPolicerStatsFMRD,
       "f3FpQosPolicerStatsBytesIn": f3FpQosPolicerStatsBytesIn,
       "f3FpQosPolicerStatsBytesOut": f3FpQosPolicerStatsBytesOut,
       "f3FpQosPolicerStatsABR": f3FpQosPolicerStatsABR,
       "f3FpQosPolicerHistoryTable": f3FpQosPolicerHistoryTable,
       "f3FpQosPolicerHistoryEntry": f3FpQosPolicerHistoryEntry,
       "f3FpQosPolicerHistoryIndex": f3FpQosPolicerHistoryIndex,
       "f3FpQosPolicerHistoryTime": f3FpQosPolicerHistoryTime,
       "f3FpQosPolicerHistoryValid": f3FpQosPolicerHistoryValid,
       "f3FpQosPolicerHistoryAction": f3FpQosPolicerHistoryAction,
       "f3FpQosPolicerHistoryFMG": f3FpQosPolicerHistoryFMG,
       "f3FpQosPolicerHistoryFMY": f3FpQosPolicerHistoryFMY,
       "f3FpQosPolicerHistoryFMRD": f3FpQosPolicerHistoryFMRD,
       "f3FpQosPolicerHistoryBytesIn": f3FpQosPolicerHistoryBytesIn,
       "f3FpQosPolicerHistoryBytesOut": f3FpQosPolicerHistoryBytesOut,
       "f3FpQosPolicerHistoryABR": f3FpQosPolicerHistoryABR,
       "f3FpQosPolicerThresholdTable": f3FpQosPolicerThresholdTable,
       "f3FpQosPolicerThresholdEntry": f3FpQosPolicerThresholdEntry,
       "f3FpQosPolicerThresholdIndex": f3FpQosPolicerThresholdIndex,
       "f3FpQosPolicerThresholdInterval": f3FpQosPolicerThresholdInterval,
       "f3FpQosPolicerThresholdVariable": f3FpQosPolicerThresholdVariable,
       "f3FpQosPolicerThresholdValueLo": f3FpQosPolicerThresholdValueLo,
       "f3FpQosPolicerThresholdValueHi": f3FpQosPolicerThresholdValueHi,
       "f3FpQosPolicerThresholdMonValue": f3FpQosPolicerThresholdMonValue,
       "f3AclRuleStatsTable": f3AclRuleStatsTable,
       "f3AclRuleStatsEntry": f3AclRuleStatsEntry,
       "f3AclRuleStatsIndex": f3AclRuleStatsIndex,
       "f3AclRuleStatsIntervalType": f3AclRuleStatsIntervalType,
       "f3AclRuleStatsValid": f3AclRuleStatsValid,
       "f3AclRuleStatsAction": f3AclRuleStatsAction,
       "f3AclRuleStatsRuleMatch": f3AclRuleStatsRuleMatch,
       "f3AclRuleHistoryTable": f3AclRuleHistoryTable,
       "f3AclRuleHistoryEntry": f3AclRuleHistoryEntry,
       "f3AclRuleHistoryIndex": f3AclRuleHistoryIndex,
       "f3AclRuleHistoryTime": f3AclRuleHistoryTime,
       "f3AclRuleHistoryValid": f3AclRuleHistoryValid,
       "f3AclRuleHistoryAction": f3AclRuleHistoryAction,
       "f3AclRuleHistoryRuleMatch": f3AclRuleHistoryRuleMatch,
       "f3AclRuleThresholdTable": f3AclRuleThresholdTable,
       "f3AclRuleThresholdEntry": f3AclRuleThresholdEntry,
       "f3AclRuleThresholdIndex": f3AclRuleThresholdIndex,
       "f3AclRuleThresholdInterval": f3AclRuleThresholdInterval,
       "f3AclRuleThresholdVariable": f3AclRuleThresholdVariable,
       "f3AclRuleThresholdValueLo": f3AclRuleThresholdValueLo,
       "f3AclRuleThresholdValueHi": f3AclRuleThresholdValueHi,
       "f3AclRuleThresholdMonValue": f3AclRuleThresholdMonValue,
       "cmEthernetNetPortXdslStatsTable": cmEthernetNetPortXdslStatsTable,
       "cmEthernetNetPortXdslStatsEntry": cmEthernetNetPortXdslStatsEntry,
       "cmEthernetNetPortStatsXdslUsPkt": cmEthernetNetPortStatsXdslUsPkt,
       "cmEthernetNetPortStatsXdslUsCrcError": cmEthernetNetPortStatsXdslUsCrcError,
       "cmEthernetNetPortStatsXdslDsPkt": cmEthernetNetPortStatsXdslDsPkt,
       "cmEthernetNetPortStatsXdslUsFecs": cmEthernetNetPortStatsXdslUsFecs,
       "cmEthernetNetPortStatsXdslDsFecs": cmEthernetNetPortStatsXdslDsFecs,
       "cmEthernetNetPortStatsXdslUsEs": cmEthernetNetPortStatsXdslUsEs,
       "cmEthernetNetPortStatsXdslDsEs": cmEthernetNetPortStatsXdslDsEs,
       "cmEthernetNetPortStatsXdslUsSes": cmEthernetNetPortStatsXdslUsSes,
       "cmEthernetNetPortStatsXdslDsSes": cmEthernetNetPortStatsXdslDsSes,
       "cmEthernetNetPortStatsXdslUsLoss": cmEthernetNetPortStatsXdslUsLoss,
       "cmEthernetNetPortStatsXdslDsLoss": cmEthernetNetPortStatsXdslDsLoss,
       "cmEthernetNetPortStatsXdslDsUas": cmEthernetNetPortStatsXdslDsUas,
       "cmEthernetNetPortStatsXdslUsCv": cmEthernetNetPortStatsXdslUsCv,
       "cmEthernetNetPortStatsXdslDsCv": cmEthernetNetPortStatsXdslDsCv,
       "cmEthernetNetPortStatsXdslUsFec": cmEthernetNetPortStatsXdslUsFec,
       "cmEthernetNetPortStatsXdslDsFec": cmEthernetNetPortStatsXdslDsFec,
       "cmEthernetNetPortStatsXdslDsFullInits": cmEthernetNetPortStatsXdslDsFullInits,
       "cmEthernetNetPortStatsXdslUsFullInits": cmEthernetNetPortStatsXdslUsFullInits,
       "cmEthernetNetPortXdslHistoryTable": cmEthernetNetPortXdslHistoryTable,
       "cmEthernetNetPortXdslHistoryEntry": cmEthernetNetPortXdslHistoryEntry,
       "cmEthernetNetPortHistoryXdslUsPkt": cmEthernetNetPortHistoryXdslUsPkt,
       "cmEthernetNetPortHistoryXdslUsCrcError": cmEthernetNetPortHistoryXdslUsCrcError,
       "cmEthernetNetPortHistoryXdslDsPkt": cmEthernetNetPortHistoryXdslDsPkt,
       "cmEthernetNetPortHistoryXdslUsFecs": cmEthernetNetPortHistoryXdslUsFecs,
       "cmEthernetNetPortHistoryXdslDsFecs": cmEthernetNetPortHistoryXdslDsFecs,
       "cmEthernetNetPortHistoryXdslUsEs": cmEthernetNetPortHistoryXdslUsEs,
       "cmEthernetNetPortHistoryXdslDsEs": cmEthernetNetPortHistoryXdslDsEs,
       "cmEthernetNetPortHistoryXdslUsSes": cmEthernetNetPortHistoryXdslUsSes,
       "cmEthernetNetPortHistoryXdslDsSes": cmEthernetNetPortHistoryXdslDsSes,
       "cmEthernetNetPortHistoryXdslUsLoss": cmEthernetNetPortHistoryXdslUsLoss,
       "cmEthernetNetPortHistoryXdslDsLoss": cmEthernetNetPortHistoryXdslDsLoss,
       "cmEthernetNetPortHistoryXdslDsUas": cmEthernetNetPortHistoryXdslDsUas,
       "cmEthernetNetPortHistoryXdslUsCv": cmEthernetNetPortHistoryXdslUsCv,
       "cmEthernetNetPortHistoryXdslDsCv": cmEthernetNetPortHistoryXdslDsCv,
       "cmEthernetNetPortHistoryXdslUsFec": cmEthernetNetPortHistoryXdslUsFec,
       "cmEthernetNetPortHistoryXdslDsFec": cmEthernetNetPortHistoryXdslDsFec,
       "cmEthernetNetPortHistoryXdslDsFullInits": cmEthernetNetPortHistoryXdslDsFullInits,
       "cmEthernetNetPortHistoryXdslUsFullInits": cmEthernetNetPortHistoryXdslUsFullInits,
       "f3CardStatsTable": f3CardStatsTable,
       "f3CardStatsEntry": f3CardStatsEntry,
       "f3CardStatsIndex": f3CardStatsIndex,
       "f3CardStatsIntervalType": f3CardStatsIntervalType,
       "f3CardStatsValid": f3CardStatsValid,
       "f3CardStatsAction": f3CardStatsAction,
       "f3CardStatsACU": f3CardStatsACU,
       "f3CardStatsMCU": f3CardStatsMCU,
       "f3CardStatsICU": f3CardStatsICU,
       "f3CardStatsAMU": f3CardStatsAMU,
       "f3CardStatsMMU": f3CardStatsMMU,
       "f3CardStatsIMU": f3CardStatsIMU,
       "f3CardHistoryTable": f3CardHistoryTable,
       "f3CardHistoryEntry": f3CardHistoryEntry,
       "f3CardHistoryIndex": f3CardHistoryIndex,
       "f3CardHistoryTime": f3CardHistoryTime,
       "f3CardHistoryValid": f3CardHistoryValid,
       "f3CardHistoryAction": f3CardHistoryAction,
       "f3CardHistoryACU": f3CardHistoryACU,
       "f3CardHistoryMCU": f3CardHistoryMCU,
       "f3CardHistoryICU": f3CardHistoryICU,
       "f3CardHistoryAMU": f3CardHistoryAMU,
       "f3CardHistoryMMU": f3CardHistoryMMU,
       "f3CardHistoryIMU": f3CardHistoryIMU,
       "f3CardThresholdTable": f3CardThresholdTable,
       "f3CardThresholdEntry": f3CardThresholdEntry,
       "f3CardThresholdIndex": f3CardThresholdIndex,
       "f3CardThresholdInterval": f3CardThresholdInterval,
       "f3CardThresholdVariable": f3CardThresholdVariable,
       "f3CardThresholdValueLo": f3CardThresholdValueLo,
       "f3CardThresholdValueHi": f3CardThresholdValueHi,
       "f3CardThresholdMonValue": f3CardThresholdMonValue,
       "cmPerfNotifications": cmPerfNotifications,
       "cmEthernetAccPortThresholdCrossingAlert": cmEthernetAccPortThresholdCrossingAlert,
       "cmEthernetNetPortThresholdCrossingAlert": cmEthernetNetPortThresholdCrossingAlert,
       "cmFlowThresholdCrossingAlert": cmFlowThresholdCrossingAlert,
       "cmQosShaperThresholdCrossingAlert": cmQosShaperThresholdCrossingAlert,
       "cmQosFlowPolicerThresholdCrossingAlert": cmQosFlowPolicerThresholdCrossingAlert,
       "cmAccPortQosShaperThresholdCrossingAlert": cmAccPortQosShaperThresholdCrossingAlert,
       "cmEthernetTrafficPortThresholdCrossingAlert": cmEthernetTrafficPortThresholdCrossingAlert,
       "cmFlowPointThresholdCrossingAlert": cmFlowPointThresholdCrossingAlert,
       "cmOAMFlowPointThresholdCrossingAlert": cmOAMFlowPointThresholdCrossingAlert,
       "cmQosPolicerV2ThresholdCrossingAlert": cmQosPolicerV2ThresholdCrossingAlert,
       "cmQosShaperV2ThresholdCrossingAlert": cmQosShaperV2ThresholdCrossingAlert,
       "cmLagThresholdCrossingAlert": cmLagThresholdCrossingAlert,
       "cmTrafficPortQosShaperThresholdCrossingAlert": cmTrafficPortQosShaperThresholdCrossingAlert,
       "f3NetPortQosShaperThresholdCrossingAlert": f3NetPortQosShaperThresholdCrossingAlert,
       "ocnStmThresholdCrossingAlert": ocnStmThresholdCrossingAlert,
       "stsVcPathThresholdCrossingAlert": stsVcPathThresholdCrossingAlert,
       "vtVcPathThresholdCrossingAlert": vtVcPathThresholdCrossingAlert,
       "e1t1ThresholdCrossingAlert": e1t1ThresholdCrossingAlert,
       "e3t3ThresholdCrossingAlert": e3t3ThresholdCrossingAlert,
       "cmPerQueryGenTrap": cmPerQueryGenTrap,
       "f3FpQosShaperThresholdCrossingAlert": f3FpQosShaperThresholdCrossingAlert,
       "f3FpQosPolicerThresholdCrossingAlert": f3FpQosPolicerThresholdCrossingAlert,
       "f3AclRuleThresholdCrossingAlert": f3AclRuleThresholdCrossingAlert,
       "f3CardThresholdCrossingAlert": f3CardThresholdCrossingAlert,
       "cmPerfConformance": cmPerfConformance,
       "cmPerfCompliances": cmPerfCompliances,
       "cmPerfCompliance": cmPerfCompliance,
       "cmPerfGroups": cmPerfGroups,
       "cmPerfObjectGroup": cmPerfObjectGroup,
       "cmPerfNotifGroup": cmPerfNotifGroup,
       "ethernetAccessPortPMGroup": ethernetAccessPortPMGroup,
       "ethernetNetworkPortPMGroup": ethernetNetworkPortPMGroup,
       "trafficPMGroup": trafficPMGroup,
       "cmEGXPerfNotifGroup": cmEGXPerfNotifGroup,
       "trafficPMGroupCmHub": trafficPMGroupCmHub,
       "cmPerfNotifGroupCmHub": cmPerfNotifGroupCmHub,
       "ocnStmPortPerfGroup": ocnStmPortPerfGroup,
       "stsVcPathPerfGroup": stsVcPathPerfGroup,
       "vtVcPathPerfGroup": vtVcPathPerfGroup,
       "e1T1PerfGroup": e1T1PerfGroup,
       "flowPointPmGroup": flowPointPmGroup,
       "cmFlowBWPerfGroup": cmFlowBWPerfGroup,
       "ocnStmThresholdVarGroup": ocnStmThresholdVarGroup,
       "f3FpQosShaperPerfGroup": f3FpQosShaperPerfGroup,
       "f3FpQosPolicerPerfGroup": f3FpQosPolicerPerfGroup,
       "cmEthernetTrafficPortPerfGroup": cmEthernetTrafficPortPerfGroup,
       "f3AclRulePerfGroup": f3AclRulePerfGroup,
       "cmXgProPerfNotifGroup": cmXgProPerfNotifGroup,
       "cmEthernetNetPortXdslPerfGroup": cmEthernetNetPortXdslPerfGroup,
       "f3CardPerfGroup": f3CardPerfGroup}
)
