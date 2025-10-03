# SNMP MIB module (PRVT-STATISTICS-CES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-STATISTICS-CES-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:29:55 2025
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

(dsx1CurrentEntry,
 dsx1FarEndCurrentEntry,
 dsx1FarEndIntervalEntry,
 dsx1FarEndTotalEntry,
 dsx1IntervalEntry,
 dsx1TotalEntry) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1CurrentEntry",
    "dsx1FarEndCurrentEntry",
    "dsx1FarEndIntervalEntry",
    "dsx1FarEndTotalEntry",
    "dsx1IntervalEntry",
    "dsx1TotalEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(sonetFarEndLineCurrentEntry,
 sonetFarEndLineIntervalEntry,
 sonetFarEndPathCurrentEntry,
 sonetFarEndPathIntervalEntry,
 sonetFarEndVTCurrentEntry,
 sonetFarEndVTIntervalEntry,
 sonetLineCurrentEntry,
 sonetLineIntervalEntry,
 sonetPathCurrentEntry,
 sonetPathIntervalEntry,
 sonetSectionCurrentEntry,
 sonetSectionIntervalEntry,
 sonetVTCurrentEntry,
 sonetVTIntervalEntry) = mibBuilder.importSymbols(
    "SONET-MIB",
    "sonetFarEndLineCurrentEntry",
    "sonetFarEndLineIntervalEntry",
    "sonetFarEndPathCurrentEntry",
    "sonetFarEndPathIntervalEntry",
    "sonetFarEndVTCurrentEntry",
    "sonetFarEndVTIntervalEntry",
    "sonetLineCurrentEntry",
    "sonetLineIntervalEntry",
    "sonetPathCurrentEntry",
    "sonetPathIntervalEntry",
    "sonetSectionCurrentEntry",
    "sonetSectionIntervalEntry",
    "sonetVTCurrentEntry",
    "sonetVTIntervalEntry")


# MODULE-IDENTITY

prvtStatisticsCESMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114)
)
if mibBuilder.loadTexts:
    prvtStatisticsCESMib.setRevisions(
        ("2009-04-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SonetLineAlarmType(TextualConvention, Integer32):
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
        *(("sonetAlarmLineMSAIS", 1),
          ("sonetAlarmLineLAIS", 2),
          ("sonetAlarmLineMSRDI", 3),
          ("sonetAlarmLineLRDI", 4))
    )



class SonetSectionAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sonetAlarmSectionLOS", 5),
          ("sonetAlarmSectionLOF", 6),
          ("sonetAlarmSectionRSLOF", 7))
    )



class SonetPathAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("sonetAlarmPathLOP", 8),
          ("sonetAlarmPathAIS", 9),
          ("sonetAlarmPathRDI", 10),
          ("sonetAlarmPathUNEQUIPPED", 11),
          ("sonetAlarmPathLABELMISMATCH", 12))
    )



class SonetVTAlarmType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("sonetAlarmVtTULOP", 13),
          ("sonetAlarmVtVLOP", 14),
          ("sonetAlarmVtTUAIS", 15),
          ("sonetAlarmVtVAIS", 16),
          ("sonetAlarmVtLPRDI", 17),
          ("sonetAlarmVtVRDI", 18),
          ("sonetAlarmVtLPRFI", 19),
          ("sonetAlarmVtVRFI", 20),
          ("sonetAlarmVtLPUNEQUIPPED", 21),
          ("sonetAlarmVtVUNEQUIPPED", 22),
          ("sonetAlarmVtLPLBLMISMATCH", 23),
          ("sonetAlarmVtVLBLMISMATCH", 24))
    )



class SonetAlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sonetAlarmDown", 0),
          ("sonetAlarmUp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtStatisticsNotifications_ObjectIdentity = ObjectIdentity
prvtStatisticsNotifications = _PrvtStatisticsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 0)
)
_PrvtStatisticsObjects_ObjectIdentity = ObjectIdentity
prvtStatisticsObjects = _PrvtStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1)
)
_PrvtStatisticsDSx1_ObjectIdentity = ObjectIdentity
prvtStatisticsDSx1 = _PrvtStatisticsDSx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1)
)
_PrvtDSx1CurrentTable_Object = MibTable
prvtDSx1CurrentTable = _PrvtDSx1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtDSx1CurrentTable.setStatus("current")
_PrvtDSx1CurrentEntry_Object = MibTableRow
prvtDSx1CurrentEntry = _PrvtDSx1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtDSx1CurrentEntry.setStatus("current")
_PrvtDSx1CurrentBBEs_Type = PerfCurrentCount
_PrvtDSx1CurrentBBEs_Object = MibTableColumn
prvtDSx1CurrentBBEs = _PrvtDSx1CurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 1, 1, 1),
    _PrvtDSx1CurrentBBEs_Type()
)
prvtDSx1CurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1CurrentBBEs.setStatus("current")
_PrvtDSx1CurrentLSESs_Type = PerfCurrentCount
_PrvtDSx1CurrentLSESs_Object = MibTableColumn
prvtDSx1CurrentLSESs = _PrvtDSx1CurrentLSESs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 1, 1, 2),
    _PrvtDSx1CurrentLSESs_Type()
)
prvtDSx1CurrentLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1CurrentLSESs.setStatus("current")
_PrvtDSx1CurrentPFCs_Type = PerfCurrentCount
_PrvtDSx1CurrentPFCs_Object = MibTableColumn
prvtDSx1CurrentPFCs = _PrvtDSx1CurrentPFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 1, 1, 3),
    _PrvtDSx1CurrentPFCs_Type()
)
prvtDSx1CurrentPFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1CurrentPFCs.setStatus("current")
_PrvtDSx1IntervalTable_Object = MibTable
prvtDSx1IntervalTable = _PrvtDSx1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 2)
)
if mibBuilder.loadTexts:
    prvtDSx1IntervalTable.setStatus("current")
_PrvtDSx1IntervalEntry_Object = MibTableRow
prvtDSx1IntervalEntry = _PrvtDSx1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    prvtDSx1IntervalEntry.setStatus("current")
_PrvtDSx1IntervalBBEs_Type = PerfIntervalCount
_PrvtDSx1IntervalBBEs_Object = MibTableColumn
prvtDSx1IntervalBBEs = _PrvtDSx1IntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 2, 1, 1),
    _PrvtDSx1IntervalBBEs_Type()
)
prvtDSx1IntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1IntervalBBEs.setStatus("current")
_PrvtDSx1IntervalLSESs_Type = PerfIntervalCount
_PrvtDSx1IntervalLSESs_Object = MibTableColumn
prvtDSx1IntervalLSESs = _PrvtDSx1IntervalLSESs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 2, 1, 2),
    _PrvtDSx1IntervalLSESs_Type()
)
prvtDSx1IntervalLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1IntervalLSESs.setStatus("current")
_PrvtDSx1IntervalPFCs_Type = PerfIntervalCount
_PrvtDSx1IntervalPFCs_Object = MibTableColumn
prvtDSx1IntervalPFCs = _PrvtDSx1IntervalPFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 2, 1, 3),
    _PrvtDSx1IntervalPFCs_Type()
)
prvtDSx1IntervalPFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1IntervalPFCs.setStatus("current")
_PrvtDSx1TotalTable_Object = MibTable
prvtDSx1TotalTable = _PrvtDSx1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 3)
)
if mibBuilder.loadTexts:
    prvtDSx1TotalTable.setStatus("current")
_PrvtDSx1TotalEntry_Object = MibTableRow
prvtDSx1TotalEntry = _PrvtDSx1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    prvtDSx1TotalEntry.setStatus("current")
_PrvtDSx1TotalBBEs_Type = PerfTotalCount
_PrvtDSx1TotalBBEs_Object = MibTableColumn
prvtDSx1TotalBBEs = _PrvtDSx1TotalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 3, 1, 1),
    _PrvtDSx1TotalBBEs_Type()
)
prvtDSx1TotalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1TotalBBEs.setStatus("current")
_PrvtDSx1TotalLSESs_Type = PerfTotalCount
_PrvtDSx1TotalLSESs_Object = MibTableColumn
prvtDSx1TotalLSESs = _PrvtDSx1TotalLSESs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 3, 1, 2),
    _PrvtDSx1TotalLSESs_Type()
)
prvtDSx1TotalLSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1TotalLSESs.setStatus("current")
_PrvtDSx1TotalPFCs_Type = PerfTotalCount
_PrvtDSx1TotalPFCs_Object = MibTableColumn
prvtDSx1TotalPFCs = _PrvtDSx1TotalPFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 3, 1, 3),
    _PrvtDSx1TotalPFCs_Type()
)
prvtDSx1TotalPFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtDSx1TotalPFCs.setStatus("current")
_PrvtDSx1FarEndCurrentTable_Object = MibTable
prvtDSx1FarEndCurrentTable = _PrvtDSx1FarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 4)
)
if mibBuilder.loadTexts:
    prvtDSx1FarEndCurrentTable.setStatus("current")
_PrvtDSx1FarEndCurrentEntry_Object = MibTableRow
prvtDSx1FarEndCurrentEntry = _PrvtDSx1FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    prvtDSx1FarEndCurrentEntry.setStatus("current")
_PrvtFarEndDSx1CurrentBBEs_Type = PerfCurrentCount
_PrvtFarEndDSx1CurrentBBEs_Object = MibTableColumn
prvtFarEndDSx1CurrentBBEs = _PrvtFarEndDSx1CurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 4, 1, 1),
    _PrvtFarEndDSx1CurrentBBEs_Type()
)
prvtFarEndDSx1CurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndDSx1CurrentBBEs.setStatus("current")
_PrvtFarEndDSx1CurrentPFCs_Type = PerfCurrentCount
_PrvtFarEndDSx1CurrentPFCs_Object = MibTableColumn
prvtFarEndDSx1CurrentPFCs = _PrvtFarEndDSx1CurrentPFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 4, 1, 2),
    _PrvtFarEndDSx1CurrentPFCs_Type()
)
prvtFarEndDSx1CurrentPFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndDSx1CurrentPFCs.setStatus("current")
_PrvtDSx1FarEndIntervalTable_Object = MibTable
prvtDSx1FarEndIntervalTable = _PrvtDSx1FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 5)
)
if mibBuilder.loadTexts:
    prvtDSx1FarEndIntervalTable.setStatus("current")
_PrvtDSx1FarEndIntervalEntry_Object = MibTableRow
prvtDSx1FarEndIntervalEntry = _PrvtDSx1FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    prvtDSx1FarEndIntervalEntry.setStatus("current")
_PrvtFarEndDSx1IntervalBBEs_Type = PerfIntervalCount
_PrvtFarEndDSx1IntervalBBEs_Object = MibTableColumn
prvtFarEndDSx1IntervalBBEs = _PrvtFarEndDSx1IntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 5, 1, 1),
    _PrvtFarEndDSx1IntervalBBEs_Type()
)
prvtFarEndDSx1IntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndDSx1IntervalBBEs.setStatus("current")
_PrvtFarEndDSx1IntervalPFCs_Type = PerfIntervalCount
_PrvtFarEndDSx1IntervalPFCs_Object = MibTableColumn
prvtFarEndDSx1IntervalPFCs = _PrvtFarEndDSx1IntervalPFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 5, 1, 2),
    _PrvtFarEndDSx1IntervalPFCs_Type()
)
prvtFarEndDSx1IntervalPFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndDSx1IntervalPFCs.setStatus("current")
_PrvtDSx1FarEndTotalTable_Object = MibTable
prvtDSx1FarEndTotalTable = _PrvtDSx1FarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 6)
)
if mibBuilder.loadTexts:
    prvtDSx1FarEndTotalTable.setStatus("current")
_PrvtDSx1FarEndTotalEntry_Object = MibTableRow
prvtDSx1FarEndTotalEntry = _PrvtDSx1FarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    prvtDSx1FarEndTotalEntry.setStatus("current")
_PrvtFarEndDSx1TotalBBEs_Type = PerfTotalCount
_PrvtFarEndDSx1TotalBBEs_Object = MibTableColumn
prvtFarEndDSx1TotalBBEs = _PrvtFarEndDSx1TotalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 6, 1, 1),
    _PrvtFarEndDSx1TotalBBEs_Type()
)
prvtFarEndDSx1TotalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndDSx1TotalBBEs.setStatus("current")
_PrvtFarEndDSx1TotalPFCs_Type = PerfTotalCount
_PrvtFarEndDSx1TotalPFCs_Object = MibTableColumn
prvtFarEndDSx1TotalPFCs = _PrvtFarEndDSx1TotalPFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 1, 6, 1, 2),
    _PrvtFarEndDSx1TotalPFCs_Type()
)
prvtFarEndDSx1TotalPFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndDSx1TotalPFCs.setStatus("current")
_PrvtStatisticsSection_ObjectIdentity = ObjectIdentity
prvtStatisticsSection = _PrvtStatisticsSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2)
)
_PrvtSectionCurrentTable_Object = MibTable
prvtSectionCurrentTable = _PrvtSectionCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 1)
)
if mibBuilder.loadTexts:
    prvtSectionCurrentTable.setStatus("current")
_PrvtSectionCurrentEntry_Object = MibTableRow
prvtSectionCurrentEntry = _PrvtSectionCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    prvtSectionCurrentEntry.setStatus("current")
_PrvtSectionCurrentBBEs_Type = PerfCurrentCount
_PrvtSectionCurrentBBEs_Object = MibTableColumn
prvtSectionCurrentBBEs = _PrvtSectionCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 1, 1, 1),
    _PrvtSectionCurrentBBEs_Type()
)
prvtSectionCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionCurrentBBEs.setStatus("current")
_PrvtSectionCurrentESAs_Type = PerfCurrentCount
_PrvtSectionCurrentESAs_Object = MibTableColumn
prvtSectionCurrentESAs = _PrvtSectionCurrentESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 1, 1, 2),
    _PrvtSectionCurrentESAs_Type()
)
prvtSectionCurrentESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionCurrentESAs.setStatus("current")
_PrvtSectionCurrentESBs_Type = PerfCurrentCount
_PrvtSectionCurrentESBs_Object = MibTableColumn
prvtSectionCurrentESBs = _PrvtSectionCurrentESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 1, 1, 3),
    _PrvtSectionCurrentESBs_Type()
)
prvtSectionCurrentESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionCurrentESBs.setStatus("current")
_PrvtSectionCurrentUASs_Type = PerfCurrentCount
_PrvtSectionCurrentUASs_Object = MibTableColumn
prvtSectionCurrentUASs = _PrvtSectionCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 1, 1, 4),
    _PrvtSectionCurrentUASs_Type()
)
prvtSectionCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionCurrentUASs.setStatus("current")
_PrvtSectionCurrentLOSSs_Type = PerfCurrentCount
_PrvtSectionCurrentLOSSs_Object = MibTableColumn
prvtSectionCurrentLOSSs = _PrvtSectionCurrentLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 1, 1, 5),
    _PrvtSectionCurrentLOSSs_Type()
)
prvtSectionCurrentLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionCurrentLOSSs.setStatus("current")
_PrvtSectionCurrentOOFs_Type = PerfCurrentCount
_PrvtSectionCurrentOOFs_Object = MibTableColumn
prvtSectionCurrentOOFs = _PrvtSectionCurrentOOFs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 1, 1, 6),
    _PrvtSectionCurrentOOFs_Type()
)
prvtSectionCurrentOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionCurrentOOFs.setStatus("current")
_PrvtSectionIntervalTable_Object = MibTable
prvtSectionIntervalTable = _PrvtSectionIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 2)
)
if mibBuilder.loadTexts:
    prvtSectionIntervalTable.setStatus("current")
_PrvtSectionIntervalEntry_Object = MibTableRow
prvtSectionIntervalEntry = _PrvtSectionIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    prvtSectionIntervalEntry.setStatus("current")
_PrvtSectionIntervalBBEs_Type = PerfIntervalCount
_PrvtSectionIntervalBBEs_Object = MibTableColumn
prvtSectionIntervalBBEs = _PrvtSectionIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 2, 1, 1),
    _PrvtSectionIntervalBBEs_Type()
)
prvtSectionIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionIntervalBBEs.setStatus("current")
_PrvtSectionIntervalESAs_Type = PerfIntervalCount
_PrvtSectionIntervalESAs_Object = MibTableColumn
prvtSectionIntervalESAs = _PrvtSectionIntervalESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 2, 1, 2),
    _PrvtSectionIntervalESAs_Type()
)
prvtSectionIntervalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionIntervalESAs.setStatus("current")
_PrvtSectionIntervalESBs_Type = PerfIntervalCount
_PrvtSectionIntervalESBs_Object = MibTableColumn
prvtSectionIntervalESBs = _PrvtSectionIntervalESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 2, 1, 3),
    _PrvtSectionIntervalESBs_Type()
)
prvtSectionIntervalESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionIntervalESBs.setStatus("current")
_PrvtSectionIntervalUASs_Type = PerfIntervalCount
_PrvtSectionIntervalUASs_Object = MibTableColumn
prvtSectionIntervalUASs = _PrvtSectionIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 2, 1, 4),
    _PrvtSectionIntervalUASs_Type()
)
prvtSectionIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionIntervalUASs.setStatus("current")
_PrvtSectionIntervalLOSSs_Type = PerfIntervalCount
_PrvtSectionIntervalLOSSs_Object = MibTableColumn
prvtSectionIntervalLOSSs = _PrvtSectionIntervalLOSSs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 2, 1, 5),
    _PrvtSectionIntervalLOSSs_Type()
)
prvtSectionIntervalLOSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionIntervalLOSSs.setStatus("current")
_PrvtSectionIntervalOOFs_Type = PerfIntervalCount
_PrvtSectionIntervalOOFs_Object = MibTableColumn
prvtSectionIntervalOOFs = _PrvtSectionIntervalOOFs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 2, 1, 6),
    _PrvtSectionIntervalOOFs_Type()
)
prvtSectionIntervalOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtSectionIntervalOOFs.setStatus("current")
_PrvtSonetSectionAlarmsTable_Object = MibTable
prvtSonetSectionAlarmsTable = _PrvtSonetSectionAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 3)
)
if mibBuilder.loadTexts:
    prvtSonetSectionAlarmsTable.setStatus("current")
_PrvtSonetSectionAlarmsEntry_Object = MibTableRow
prvtSonetSectionAlarmsEntry = _PrvtSonetSectionAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 3, 1)
)
prvtSonetSectionAlarmsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtSonetSectionAlarmsEntry.setStatus("current")
_PrvtSonetSectionAlarmType_Type = SonetSectionAlarmType
_PrvtSonetSectionAlarmType_Object = MibTableColumn
prvtSonetSectionAlarmType = _PrvtSonetSectionAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 3, 1, 1),
    _PrvtSonetSectionAlarmType_Type()
)
prvtSonetSectionAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtSonetSectionAlarmType.setStatus("current")
_PrvtSonetSectionAlarmStatus_Type = SonetAlarmStatus
_PrvtSonetSectionAlarmStatus_Object = MibTableColumn
prvtSonetSectionAlarmStatus = _PrvtSonetSectionAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 2, 3, 1, 2),
    _PrvtSonetSectionAlarmStatus_Type()
)
prvtSonetSectionAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtSonetSectionAlarmStatus.setStatus("current")
_PrvtStatisticsLine_ObjectIdentity = ObjectIdentity
prvtStatisticsLine = _PrvtStatisticsLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3)
)
_PrvtLineCurrentTable_Object = MibTable
prvtLineCurrentTable = _PrvtLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1)
)
if mibBuilder.loadTexts:
    prvtLineCurrentTable.setStatus("current")
_PrvtLineCurrentEntry_Object = MibTableRow
prvtLineCurrentEntry = _PrvtLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    prvtLineCurrentEntry.setStatus("current")
_PrvtLineCurrentFCs_Type = PerfCurrentCount
_PrvtLineCurrentFCs_Object = MibTableColumn
prvtLineCurrentFCs = _PrvtLineCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 1),
    _PrvtLineCurrentFCs_Type()
)
prvtLineCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentFCs.setStatus("current")
_PrvtLineCurrentBBEs_Type = PerfCurrentCount
_PrvtLineCurrentBBEs_Object = MibTableColumn
prvtLineCurrentBBEs = _PrvtLineCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 2),
    _PrvtLineCurrentBBEs_Type()
)
prvtLineCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentBBEs.setStatus("current")
_PrvtLineCurrentESAs_Type = PerfCurrentCount
_PrvtLineCurrentESAs_Object = MibTableColumn
prvtLineCurrentESAs = _PrvtLineCurrentESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 3),
    _PrvtLineCurrentESAs_Type()
)
prvtLineCurrentESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentESAs.setStatus("current")
_PrvtLineCurrentESBs_Type = PerfCurrentCount
_PrvtLineCurrentESBs_Object = MibTableColumn
prvtLineCurrentESBs = _PrvtLineCurrentESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 4),
    _PrvtLineCurrentESBs_Type()
)
prvtLineCurrentESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentESBs.setStatus("current")
_PrvtLineCurrentLBCs_Type = PerfCurrentCount
_PrvtLineCurrentLBCs_Object = MibTableColumn
prvtLineCurrentLBCs = _PrvtLineCurrentLBCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 5),
    _PrvtLineCurrentLBCs_Type()
)
prvtLineCurrentLBCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentLBCs.setStatus("current")
_PrvtLineCurrentOPRs_Type = PerfCurrentCount
_PrvtLineCurrentOPRs_Object = MibTableColumn
prvtLineCurrentOPRs = _PrvtLineCurrentOPRs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 6),
    _PrvtLineCurrentOPRs_Type()
)
prvtLineCurrentOPRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentOPRs.setStatus("current")
_PrtvLineCurrentOPTs_Type = PerfCurrentCount
_PrtvLineCurrentOPTs_Object = MibTableColumn
prtvLineCurrentOPTs = _PrtvLineCurrentOPTs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 7),
    _PrtvLineCurrentOPTs_Type()
)
prtvLineCurrentOPTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtvLineCurrentOPTs.setStatus("current")
_PrvtLineCurrentAISs_Type = PerfCurrentCount
_PrvtLineCurrentAISs_Object = MibTableColumn
prvtLineCurrentAISs = _PrvtLineCurrentAISs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 8),
    _PrvtLineCurrentAISs_Type()
)
prvtLineCurrentAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentAISs.setStatus("current")
_PrvtLineCurrentPSCs_Type = PerfCurrentCount
_PrvtLineCurrentPSCs_Object = MibTableColumn
prvtLineCurrentPSCs = _PrvtLineCurrentPSCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 9),
    _PrvtLineCurrentPSCs_Type()
)
prvtLineCurrentPSCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentPSCs.setStatus("current")
_PrvtLineCurrentPSDs_Type = PerfCurrentCount
_PrvtLineCurrentPSDs_Object = MibTableColumn
prvtLineCurrentPSDs = _PrvtLineCurrentPSDs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 1, 1, 10),
    _PrvtLineCurrentPSDs_Type()
)
prvtLineCurrentPSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineCurrentPSDs.setStatus("current")
_PrvtLineIntervalTable_Object = MibTable
prvtLineIntervalTable = _PrvtLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2)
)
if mibBuilder.loadTexts:
    prvtLineIntervalTable.setStatus("current")
_PrvtLineIntervalEntry_Object = MibTableRow
prvtLineIntervalEntry = _PrvtLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    prvtLineIntervalEntry.setStatus("current")
_PrvtLineIntervalFCs_Type = PerfIntervalCount
_PrvtLineIntervalFCs_Object = MibTableColumn
prvtLineIntervalFCs = _PrvtLineIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 1),
    _PrvtLineIntervalFCs_Type()
)
prvtLineIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntervalFCs.setStatus("current")
_PrvtLineIntervalBBEs_Type = PerfIntervalCount
_PrvtLineIntervalBBEs_Object = MibTableColumn
prvtLineIntervalBBEs = _PrvtLineIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 2),
    _PrvtLineIntervalBBEs_Type()
)
prvtLineIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntervalBBEs.setStatus("current")
_PrvtLineIntervalESAs_Type = PerfIntervalCount
_PrvtLineIntervalESAs_Object = MibTableColumn
prvtLineIntervalESAs = _PrvtLineIntervalESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 3),
    _PrvtLineIntervalESAs_Type()
)
prvtLineIntervalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntervalESAs.setStatus("current")
_PrvtLineIntervalESBs_Type = PerfIntervalCount
_PrvtLineIntervalESBs_Object = MibTableColumn
prvtLineIntervalESBs = _PrvtLineIntervalESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 4),
    _PrvtLineIntervalESBs_Type()
)
prvtLineIntervalESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntervalESBs.setStatus("current")
_PrvtLineIntervalLBCs_Type = PerfIntervalCount
_PrvtLineIntervalLBCs_Object = MibTableColumn
prvtLineIntervalLBCs = _PrvtLineIntervalLBCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 5),
    _PrvtLineIntervalLBCs_Type()
)
prvtLineIntervalLBCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntervalLBCs.setStatus("current")
_PrvtLineIntervalOPRs_Type = PerfIntervalCount
_PrvtLineIntervalOPRs_Object = MibTableColumn
prvtLineIntervalOPRs = _PrvtLineIntervalOPRs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 6),
    _PrvtLineIntervalOPRs_Type()
)
prvtLineIntervalOPRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntervalOPRs.setStatus("current")
_PrtvLineIntervalOPTs_Type = PerfIntervalCount
_PrtvLineIntervalOPTs_Object = MibTableColumn
prtvLineIntervalOPTs = _PrtvLineIntervalOPTs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 7),
    _PrtvLineIntervalOPTs_Type()
)
prtvLineIntervalOPTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtvLineIntervalOPTs.setStatus("current")
_PrvtLineIntevalAISs_Type = PerfIntervalCount
_PrvtLineIntevalAISs_Object = MibTableColumn
prvtLineIntevalAISs = _PrvtLineIntevalAISs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 8),
    _PrvtLineIntevalAISs_Type()
)
prvtLineIntevalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntevalAISs.setStatus("current")
_PrvtLineIntervalPSCs_Type = PerfIntervalCount
_PrvtLineIntervalPSCs_Object = MibTableColumn
prvtLineIntervalPSCs = _PrvtLineIntervalPSCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 9),
    _PrvtLineIntervalPSCs_Type()
)
prvtLineIntervalPSCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntervalPSCs.setStatus("current")
_PrvtLineIntervalPSDs_Type = PerfIntervalCount
_PrvtLineIntervalPSDs_Object = MibTableColumn
prvtLineIntervalPSDs = _PrvtLineIntervalPSDs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 2, 1, 10),
    _PrvtLineIntervalPSDs_Type()
)
prvtLineIntervalPSDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLineIntervalPSDs.setStatus("current")
_PrvtFarEndLineCurrentTable_Object = MibTable
prvtFarEndLineCurrentTable = _PrvtFarEndLineCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 3)
)
if mibBuilder.loadTexts:
    prvtFarEndLineCurrentTable.setStatus("current")
_PrvtFarEndLineCurrentEntry_Object = MibTableRow
prvtFarEndLineCurrentEntry = _PrvtFarEndLineCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    prvtFarEndLineCurrentEntry.setStatus("current")
_PrvtFarEndLineCurrentFCs_Type = PerfCurrentCount
_PrvtFarEndLineCurrentFCs_Object = MibTableColumn
prvtFarEndLineCurrentFCs = _PrvtFarEndLineCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 3, 1, 1),
    _PrvtFarEndLineCurrentFCs_Type()
)
prvtFarEndLineCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineCurrentFCs.setStatus("current")
_PrvtFarEndLineCurrentBBEs_Type = PerfCurrentCount
_PrvtFarEndLineCurrentBBEs_Object = MibTableColumn
prvtFarEndLineCurrentBBEs = _PrvtFarEndLineCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 3, 1, 2),
    _PrvtFarEndLineCurrentBBEs_Type()
)
prvtFarEndLineCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineCurrentBBEs.setStatus("current")
_PrvtFarEndLineCurrentESAs_Type = PerfCurrentCount
_PrvtFarEndLineCurrentESAs_Object = MibTableColumn
prvtFarEndLineCurrentESAs = _PrvtFarEndLineCurrentESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 3, 1, 3),
    _PrvtFarEndLineCurrentESAs_Type()
)
prvtFarEndLineCurrentESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineCurrentESAs.setStatus("current")
_PrvtFarEndLineCurrentESBs_Type = PerfCurrentCount
_PrvtFarEndLineCurrentESBs_Object = MibTableColumn
prvtFarEndLineCurrentESBs = _PrvtFarEndLineCurrentESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 3, 1, 4),
    _PrvtFarEndLineCurrentESBs_Type()
)
prvtFarEndLineCurrentESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineCurrentESBs.setStatus("current")
_PrvtFarEndLineCurrentAISs_Type = PerfCurrentCount
_PrvtFarEndLineCurrentAISs_Object = MibTableColumn
prvtFarEndLineCurrentAISs = _PrvtFarEndLineCurrentAISs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 3, 1, 5),
    _PrvtFarEndLineCurrentAISs_Type()
)
prvtFarEndLineCurrentAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineCurrentAISs.setStatus("current")
_PrvtFarEndLineCurrentRFIs_Type = PerfCurrentCount
_PrvtFarEndLineCurrentRFIs_Object = MibTableColumn
prvtFarEndLineCurrentRFIs = _PrvtFarEndLineCurrentRFIs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 3, 1, 6),
    _PrvtFarEndLineCurrentRFIs_Type()
)
prvtFarEndLineCurrentRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineCurrentRFIs.setStatus("current")
_PrvtFarEndLineIntervalTable_Object = MibTable
prvtFarEndLineIntervalTable = _PrvtFarEndLineIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 4)
)
if mibBuilder.loadTexts:
    prvtFarEndLineIntervalTable.setStatus("current")
_PrvtFarEndLineIntervalEntry_Object = MibTableRow
prvtFarEndLineIntervalEntry = _PrvtFarEndLineIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    prvtFarEndLineIntervalEntry.setStatus("current")
_PrvtFarEndLineIntervalFCs_Type = PerfIntervalCount
_PrvtFarEndLineIntervalFCs_Object = MibTableColumn
prvtFarEndLineIntervalFCs = _PrvtFarEndLineIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 4, 1, 1),
    _PrvtFarEndLineIntervalFCs_Type()
)
prvtFarEndLineIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineIntervalFCs.setStatus("current")
_PrvtFarEndLineIntervalBBEs_Type = PerfIntervalCount
_PrvtFarEndLineIntervalBBEs_Object = MibTableColumn
prvtFarEndLineIntervalBBEs = _PrvtFarEndLineIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 4, 1, 2),
    _PrvtFarEndLineIntervalBBEs_Type()
)
prvtFarEndLineIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineIntervalBBEs.setStatus("current")
_PrvtFarEndLineIntervalESAs_Type = PerfIntervalCount
_PrvtFarEndLineIntervalESAs_Object = MibTableColumn
prvtFarEndLineIntervalESAs = _PrvtFarEndLineIntervalESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 4, 1, 3),
    _PrvtFarEndLineIntervalESAs_Type()
)
prvtFarEndLineIntervalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineIntervalESAs.setStatus("current")
_PrvtFarEndLineIntervalESBs_Type = PerfIntervalCount
_PrvtFarEndLineIntervalESBs_Object = MibTableColumn
prvtFarEndLineIntervalESBs = _PrvtFarEndLineIntervalESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 4, 1, 4),
    _PrvtFarEndLineIntervalESBs_Type()
)
prvtFarEndLineIntervalESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineIntervalESBs.setStatus("current")
_PrvtFarEndLineIntervalAISs_Type = PerfIntervalCount
_PrvtFarEndLineIntervalAISs_Object = MibTableColumn
prvtFarEndLineIntervalAISs = _PrvtFarEndLineIntervalAISs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 4, 1, 5),
    _PrvtFarEndLineIntervalAISs_Type()
)
prvtFarEndLineIntervalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineIntervalAISs.setStatus("current")
_PrvtFarEndLineIntervalRFIs_Type = PerfIntervalCount
_PrvtFarEndLineIntervalRFIs_Object = MibTableColumn
prvtFarEndLineIntervalRFIs = _PrvtFarEndLineIntervalRFIs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 4, 1, 6),
    _PrvtFarEndLineIntervalRFIs_Type()
)
prvtFarEndLineIntervalRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndLineIntervalRFIs.setStatus("current")
_PrvtSonetLineAlarmsTable_Object = MibTable
prvtSonetLineAlarmsTable = _PrvtSonetLineAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 5)
)
if mibBuilder.loadTexts:
    prvtSonetLineAlarmsTable.setStatus("current")
_PrvtSonetLineAlarmsEntry_Object = MibTableRow
prvtSonetLineAlarmsEntry = _PrvtSonetLineAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 5, 1)
)
prvtSonetLineAlarmsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtSonetLineAlarmsEntry.setStatus("current")
_PrvtSonetLineAlarmType_Type = SonetLineAlarmType
_PrvtSonetLineAlarmType_Object = MibTableColumn
prvtSonetLineAlarmType = _PrvtSonetLineAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 5, 1, 1),
    _PrvtSonetLineAlarmType_Type()
)
prvtSonetLineAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtSonetLineAlarmType.setStatus("current")
_PrvtSonetLineAlarmStatus_Type = SonetAlarmStatus
_PrvtSonetLineAlarmStatus_Object = MibTableColumn
prvtSonetLineAlarmStatus = _PrvtSonetLineAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 3, 5, 1, 2),
    _PrvtSonetLineAlarmStatus_Type()
)
prvtSonetLineAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtSonetLineAlarmStatus.setStatus("current")
_PrvtStatisticsPath_ObjectIdentity = ObjectIdentity
prvtStatisticsPath = _PrvtStatisticsPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4)
)
_PrvtPathCurrentTable_Object = MibTable
prvtPathCurrentTable = _PrvtPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1)
)
if mibBuilder.loadTexts:
    prvtPathCurrentTable.setStatus("current")
_PrvtPathCurrentEntry_Object = MibTableRow
prvtPathCurrentEntry = _PrvtPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    prvtPathCurrentEntry.setStatus("current")
_PrvtPathCurrentFCs_Type = PerfCurrentCount
_PrvtPathCurrentFCs_Object = MibTableColumn
prvtPathCurrentFCs = _PrvtPathCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 1),
    _PrvtPathCurrentFCs_Type()
)
prvtPathCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentFCs.setStatus("current")
_PrvtPathCurrentESAs_Type = PerfCurrentCount
_PrvtPathCurrentESAs_Object = MibTableColumn
prvtPathCurrentESAs = _PrvtPathCurrentESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 2),
    _PrvtPathCurrentESAs_Type()
)
prvtPathCurrentESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentESAs.setStatus("current")
_PrvtPathCurrentESBs_Type = PerfCurrentCount
_PrvtPathCurrentESBs_Object = MibTableColumn
prvtPathCurrentESBs = _PrvtPathCurrentESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 3),
    _PrvtPathCurrentESBs_Type()
)
prvtPathCurrentESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentESBs.setStatus("current")
_PrvtPathCurrentBBEs_Type = PerfCurrentCount
_PrvtPathCurrentBBEs_Object = MibTableColumn
prvtPathCurrentBBEs = _PrvtPathCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 4),
    _PrvtPathCurrentBBEs_Type()
)
prvtPathCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentBBEs.setStatus("current")
_PrvtPathCurrentAISs_Type = PerfCurrentCount
_PrvtPathCurrentAISs_Object = MibTableColumn
prvtPathCurrentAISs = _PrvtPathCurrentAISs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 5),
    _PrvtPathCurrentAISs_Type()
)
prvtPathCurrentAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentAISs.setStatus("current")
_PrvtPathCurrentPPJCPGen_Type = PerfCurrentCount
_PrvtPathCurrentPPJCPGen_Object = MibTableColumn
prvtPathCurrentPPJCPGen = _PrvtPathCurrentPPJCPGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 6),
    _PrvtPathCurrentPPJCPGen_Type()
)
prvtPathCurrentPPJCPGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentPPJCPGen.setStatus("current")
_PrvtPathCurrentNPJCPGen_Type = PerfCurrentCount
_PrvtPathCurrentNPJCPGen_Object = MibTableColumn
prvtPathCurrentNPJCPGen = _PrvtPathCurrentNPJCPGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 7),
    _PrvtPathCurrentNPJCPGen_Type()
)
prvtPathCurrentNPJCPGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentNPJCPGen.setStatus("current")
_PrvtPathCurrentPPJCPDet_Type = PerfCurrentCount
_PrvtPathCurrentPPJCPDet_Object = MibTableColumn
prvtPathCurrentPPJCPDet = _PrvtPathCurrentPPJCPDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 8),
    _PrvtPathCurrentPPJCPDet_Type()
)
prvtPathCurrentPPJCPDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentPPJCPDet.setStatus("current")
_PrvtPathCurrentNPJCPDet_Type = PerfCurrentCount
_PrvtPathCurrentNPJCPDet_Object = MibTableColumn
prvtPathCurrentNPJCPDet = _PrvtPathCurrentNPJCPDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 9),
    _PrvtPathCurrentNPJCPDet_Type()
)
prvtPathCurrentNPJCPDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentNPJCPDet.setStatus("current")
_PrvtPathCurrentPJCSPDet_Type = PerfCurrentCount
_PrvtPathCurrentPJCSPDet_Object = MibTableColumn
prvtPathCurrentPJCSPDet = _PrvtPathCurrentPJCSPDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 10),
    _PrvtPathCurrentPJCSPDet_Type()
)
prvtPathCurrentPJCSPDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentPJCSPDet.setStatus("current")
_PrvtPathCurrentPJCSPGen_Type = PerfCurrentCount
_PrvtPathCurrentPJCSPGen_Object = MibTableColumn
prvtPathCurrentPJCSPGen = _PrvtPathCurrentPJCSPGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 11),
    _PrvtPathCurrentPJCSPGen_Type()
)
prvtPathCurrentPJCSPGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentPJCSPGen.setStatus("current")
_PrvtPathCurrentJCDiffP_Type = PerfCurrentCount
_PrvtPathCurrentJCDiffP_Object = MibTableColumn
prvtPathCurrentJCDiffP = _PrvtPathCurrentJCDiffP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 1, 1, 12),
    _PrvtPathCurrentJCDiffP_Type()
)
prvtPathCurrentJCDiffP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathCurrentJCDiffP.setStatus("current")
_PrvtPathIntervalTable_Object = MibTable
prvtPathIntervalTable = _PrvtPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2)
)
if mibBuilder.loadTexts:
    prvtPathIntervalTable.setStatus("current")
_PrvtPathIntervalEntry_Object = MibTableRow
prvtPathIntervalEntry = _PrvtPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    prvtPathIntervalEntry.setStatus("current")
_PrvtPathIntervalFCs_Type = PerfIntervalCount
_PrvtPathIntervalFCs_Object = MibTableColumn
prvtPathIntervalFCs = _PrvtPathIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 1),
    _PrvtPathIntervalFCs_Type()
)
prvtPathIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalFCs.setStatus("current")
_PrvtPathIntervalESAs_Type = PerfIntervalCount
_PrvtPathIntervalESAs_Object = MibTableColumn
prvtPathIntervalESAs = _PrvtPathIntervalESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 2),
    _PrvtPathIntervalESAs_Type()
)
prvtPathIntervalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalESAs.setStatus("current")
_PrvtPathIntervalESBs_Type = PerfIntervalCount
_PrvtPathIntervalESBs_Object = MibTableColumn
prvtPathIntervalESBs = _PrvtPathIntervalESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 3),
    _PrvtPathIntervalESBs_Type()
)
prvtPathIntervalESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalESBs.setStatus("current")
_PrvtPathIntervalBBEs_Type = PerfIntervalCount
_PrvtPathIntervalBBEs_Object = MibTableColumn
prvtPathIntervalBBEs = _PrvtPathIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 4),
    _PrvtPathIntervalBBEs_Type()
)
prvtPathIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalBBEs.setStatus("current")
_PrvtPathIntervalAISs_Type = PerfIntervalCount
_PrvtPathIntervalAISs_Object = MibTableColumn
prvtPathIntervalAISs = _PrvtPathIntervalAISs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 5),
    _PrvtPathIntervalAISs_Type()
)
prvtPathIntervalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalAISs.setStatus("current")
_PrvtPathIntervalPPJCPGen_Type = PerfIntervalCount
_PrvtPathIntervalPPJCPGen_Object = MibTableColumn
prvtPathIntervalPPJCPGen = _PrvtPathIntervalPPJCPGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 6),
    _PrvtPathIntervalPPJCPGen_Type()
)
prvtPathIntervalPPJCPGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalPPJCPGen.setStatus("current")
_PrvtPathIntervalNPJCPGen_Type = PerfIntervalCount
_PrvtPathIntervalNPJCPGen_Object = MibTableColumn
prvtPathIntervalNPJCPGen = _PrvtPathIntervalNPJCPGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 7),
    _PrvtPathIntervalNPJCPGen_Type()
)
prvtPathIntervalNPJCPGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalNPJCPGen.setStatus("current")
_PrvtPathIntervalPPJCPDet_Type = PerfIntervalCount
_PrvtPathIntervalPPJCPDet_Object = MibTableColumn
prvtPathIntervalPPJCPDet = _PrvtPathIntervalPPJCPDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 8),
    _PrvtPathIntervalPPJCPDet_Type()
)
prvtPathIntervalPPJCPDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalPPJCPDet.setStatus("current")
_PrvtPathIntervalNPJCPDet_Type = PerfIntervalCount
_PrvtPathIntervalNPJCPDet_Object = MibTableColumn
prvtPathIntervalNPJCPDet = _PrvtPathIntervalNPJCPDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 9),
    _PrvtPathIntervalNPJCPDet_Type()
)
prvtPathIntervalNPJCPDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalNPJCPDet.setStatus("current")
_PrvtPathIntervalPJCSPDet_Type = PerfIntervalCount
_PrvtPathIntervalPJCSPDet_Object = MibTableColumn
prvtPathIntervalPJCSPDet = _PrvtPathIntervalPJCSPDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 10),
    _PrvtPathIntervalPJCSPDet_Type()
)
prvtPathIntervalPJCSPDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalPJCSPDet.setStatus("current")
_PrvtPathIntervalPJCSPGen_Type = PerfIntervalCount
_PrvtPathIntervalPJCSPGen_Object = MibTableColumn
prvtPathIntervalPJCSPGen = _PrvtPathIntervalPJCSPGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 11),
    _PrvtPathIntervalPJCSPGen_Type()
)
prvtPathIntervalPJCSPGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalPJCSPGen.setStatus("current")
_PrvtPathIntervalJCDiffP_Type = PerfIntervalCount
_PrvtPathIntervalJCDiffP_Object = MibTableColumn
prvtPathIntervalJCDiffP = _PrvtPathIntervalJCDiffP_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 2, 1, 12),
    _PrvtPathIntervalJCDiffP_Type()
)
prvtPathIntervalJCDiffP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPathIntervalJCDiffP.setStatus("current")
_PrvtFarEndPathCurrentTable_Object = MibTable
prvtFarEndPathCurrentTable = _PrvtFarEndPathCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 3)
)
if mibBuilder.loadTexts:
    prvtFarEndPathCurrentTable.setStatus("current")
_PrvtFarEndPathCurrentEntry_Object = MibTableRow
prvtFarEndPathCurrentEntry = _PrvtFarEndPathCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    prvtFarEndPathCurrentEntry.setStatus("current")
_PrvtFarEndPathCurrentFCs_Type = PerfCurrentCount
_PrvtFarEndPathCurrentFCs_Object = MibTableColumn
prvtFarEndPathCurrentFCs = _PrvtFarEndPathCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 3, 1, 1),
    _PrvtFarEndPathCurrentFCs_Type()
)
prvtFarEndPathCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathCurrentFCs.setStatus("current")
_PrvtFarEndPathCurrentESAs_Type = PerfCurrentCount
_PrvtFarEndPathCurrentESAs_Object = MibTableColumn
prvtFarEndPathCurrentESAs = _PrvtFarEndPathCurrentESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 3, 1, 2),
    _PrvtFarEndPathCurrentESAs_Type()
)
prvtFarEndPathCurrentESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathCurrentESAs.setStatus("current")
_PrvtFarEndPathCurrentESBs_Type = PerfCurrentCount
_PrvtFarEndPathCurrentESBs_Object = MibTableColumn
prvtFarEndPathCurrentESBs = _PrvtFarEndPathCurrentESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 3, 1, 3),
    _PrvtFarEndPathCurrentESBs_Type()
)
prvtFarEndPathCurrentESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathCurrentESBs.setStatus("current")
_PrvtFarEndPathCurrentBBEs_Type = PerfCurrentCount
_PrvtFarEndPathCurrentBBEs_Object = MibTableColumn
prvtFarEndPathCurrentBBEs = _PrvtFarEndPathCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 3, 1, 4),
    _PrvtFarEndPathCurrentBBEs_Type()
)
prvtFarEndPathCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathCurrentBBEs.setStatus("current")
_PrvtFarEndPathCurrentRFIs_Type = PerfCurrentCount
_PrvtFarEndPathCurrentRFIs_Object = MibTableColumn
prvtFarEndPathCurrentRFIs = _PrvtFarEndPathCurrentRFIs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 3, 1, 5),
    _PrvtFarEndPathCurrentRFIs_Type()
)
prvtFarEndPathCurrentRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathCurrentRFIs.setStatus("current")
_PrvtFarEndPathIntervalTable_Object = MibTable
prvtFarEndPathIntervalTable = _PrvtFarEndPathIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 4)
)
if mibBuilder.loadTexts:
    prvtFarEndPathIntervalTable.setStatus("current")
_PrvtFarEndPathIntervalEntry_Object = MibTableRow
prvtFarEndPathIntervalEntry = _PrvtFarEndPathIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    prvtFarEndPathIntervalEntry.setStatus("current")
_PrvtFarEndPathIntervalFCs_Type = PerfIntervalCount
_PrvtFarEndPathIntervalFCs_Object = MibTableColumn
prvtFarEndPathIntervalFCs = _PrvtFarEndPathIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 4, 1, 1),
    _PrvtFarEndPathIntervalFCs_Type()
)
prvtFarEndPathIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathIntervalFCs.setStatus("current")
_PrvtFarEndPathIntervalESAs_Type = PerfIntervalCount
_PrvtFarEndPathIntervalESAs_Object = MibTableColumn
prvtFarEndPathIntervalESAs = _PrvtFarEndPathIntervalESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 4, 1, 2),
    _PrvtFarEndPathIntervalESAs_Type()
)
prvtFarEndPathIntervalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathIntervalESAs.setStatus("current")
_PrvtFarEndPathIntervalESBs_Type = PerfIntervalCount
_PrvtFarEndPathIntervalESBs_Object = MibTableColumn
prvtFarEndPathIntervalESBs = _PrvtFarEndPathIntervalESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 4, 1, 3),
    _PrvtFarEndPathIntervalESBs_Type()
)
prvtFarEndPathIntervalESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathIntervalESBs.setStatus("current")
_PrvtFarEndPathIntervalBBEs_Type = PerfIntervalCount
_PrvtFarEndPathIntervalBBEs_Object = MibTableColumn
prvtFarEndPathIntervalBBEs = _PrvtFarEndPathIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 4, 1, 4),
    _PrvtFarEndPathIntervalBBEs_Type()
)
prvtFarEndPathIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathIntervalBBEs.setStatus("current")
_PrvtFarEndPathIntervalRFIs_Type = PerfIntervalCount
_PrvtFarEndPathIntervalRFIs_Object = MibTableColumn
prvtFarEndPathIntervalRFIs = _PrvtFarEndPathIntervalRFIs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 4, 1, 5),
    _PrvtFarEndPathIntervalRFIs_Type()
)
prvtFarEndPathIntervalRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndPathIntervalRFIs.setStatus("current")
_PrvtSonetPathAlarmsTable_Object = MibTable
prvtSonetPathAlarmsTable = _PrvtSonetPathAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 5)
)
if mibBuilder.loadTexts:
    prvtSonetPathAlarmsTable.setStatus("current")
_PrvtSonetPathAlarmsEntry_Object = MibTableRow
prvtSonetPathAlarmsEntry = _PrvtSonetPathAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 5, 1)
)
prvtSonetPathAlarmsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtSonetPathAlarmsEntry.setStatus("current")
_PrvtSonetPathAlarmType_Type = SonetPathAlarmType
_PrvtSonetPathAlarmType_Object = MibTableColumn
prvtSonetPathAlarmType = _PrvtSonetPathAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 5, 1, 1),
    _PrvtSonetPathAlarmType_Type()
)
prvtSonetPathAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtSonetPathAlarmType.setStatus("current")
_PrvtSonetPathAlarmStatus_Type = SonetAlarmStatus
_PrvtSonetPathAlarmStatus_Object = MibTableColumn
prvtSonetPathAlarmStatus = _PrvtSonetPathAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 4, 5, 1, 2),
    _PrvtSonetPathAlarmStatus_Type()
)
prvtSonetPathAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtSonetPathAlarmStatus.setStatus("current")
_PrvtStatisticsVt_ObjectIdentity = ObjectIdentity
prvtStatisticsVt = _PrvtStatisticsVt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5)
)
_PrvtVtCurrentTable_Object = MibTable
prvtVtCurrentTable = _PrvtVtCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1)
)
if mibBuilder.loadTexts:
    prvtVtCurrentTable.setStatus("current")
_PrvtVtCurrentEntry_Object = MibTableRow
prvtVtCurrentEntry = _PrvtVtCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    prvtVtCurrentEntry.setStatus("current")
_PrvtVtCurrentFCs_Type = PerfCurrentCount
_PrvtVtCurrentFCs_Object = MibTableColumn
prvtVtCurrentFCs = _PrvtVtCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 1),
    _PrvtVtCurrentFCs_Type()
)
prvtVtCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentFCs.setStatus("current")
_PrvtVtCurrentESAs_Type = PerfCurrentCount
_PrvtVtCurrentESAs_Object = MibTableColumn
prvtVtCurrentESAs = _PrvtVtCurrentESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 2),
    _PrvtVtCurrentESAs_Type()
)
prvtVtCurrentESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentESAs.setStatus("current")
_PrvtVtCurrentESBs_Type = PerfCurrentCount
_PrvtVtCurrentESBs_Object = MibTableColumn
prvtVtCurrentESBs = _PrvtVtCurrentESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 3),
    _PrvtVtCurrentESBs_Type()
)
prvtVtCurrentESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentESBs.setStatus("current")
_PrvtVtCurrentBBEs_Type = PerfCurrentCount
_PrvtVtCurrentBBEs_Object = MibTableColumn
prvtVtCurrentBBEs = _PrvtVtCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 4),
    _PrvtVtCurrentBBEs_Type()
)
prvtVtCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentBBEs.setStatus("current")
_PrvtVtCurrentAISs_Type = PerfCurrentCount
_PrvtVtCurrentAISs_Object = MibTableColumn
prvtVtCurrentAISs = _PrvtVtCurrentAISs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 5),
    _PrvtVtCurrentAISs_Type()
)
prvtVtCurrentAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentAISs.setStatus("current")
_PrvtVtCurrentPPJCVGen_Type = PerfCurrentCount
_PrvtVtCurrentPPJCVGen_Object = MibTableColumn
prvtVtCurrentPPJCVGen = _PrvtVtCurrentPPJCVGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 6),
    _PrvtVtCurrentPPJCVGen_Type()
)
prvtVtCurrentPPJCVGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentPPJCVGen.setStatus("current")
_PrvtVtCurrentNPJCVGen_Type = PerfCurrentCount
_PrvtVtCurrentNPJCVGen_Object = MibTableColumn
prvtVtCurrentNPJCVGen = _PrvtVtCurrentNPJCVGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 7),
    _PrvtVtCurrentNPJCVGen_Type()
)
prvtVtCurrentNPJCVGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentNPJCVGen.setStatus("current")
_PrvtVtCurrentPPJCVDet_Type = PerfCurrentCount
_PrvtVtCurrentPPJCVDet_Object = MibTableColumn
prvtVtCurrentPPJCVDet = _PrvtVtCurrentPPJCVDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 8),
    _PrvtVtCurrentPPJCVDet_Type()
)
prvtVtCurrentPPJCVDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentPPJCVDet.setStatus("current")
_PrvtVtCurrentNPJCVDet_Type = PerfCurrentCount
_PrvtVtCurrentNPJCVDet_Object = MibTableColumn
prvtVtCurrentNPJCVDet = _PrvtVtCurrentNPJCVDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 9),
    _PrvtVtCurrentNPJCVDet_Type()
)
prvtVtCurrentNPJCVDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentNPJCVDet.setStatus("current")
_PrvtVtCurrentPJCSVDet_Type = PerfCurrentCount
_PrvtVtCurrentPJCSVDet_Object = MibTableColumn
prvtVtCurrentPJCSVDet = _PrvtVtCurrentPJCSVDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 10),
    _PrvtVtCurrentPJCSVDet_Type()
)
prvtVtCurrentPJCSVDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentPJCSVDet.setStatus("current")
_PrvtVtCurrentPJCSVGen_Type = PerfCurrentCount
_PrvtVtCurrentPJCSVGen_Object = MibTableColumn
prvtVtCurrentPJCSVGen = _PrvtVtCurrentPJCSVGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 11),
    _PrvtVtCurrentPJCSVGen_Type()
)
prvtVtCurrentPJCSVGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentPJCSVGen.setStatus("current")
_PrvtVtCurrentPJCSVPJCDiffV_Type = PerfCurrentCount
_PrvtVtCurrentPJCSVPJCDiffV_Object = MibTableColumn
prvtVtCurrentPJCSVPJCDiffV = _PrvtVtCurrentPJCSVPJCDiffV_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 1, 1, 12),
    _PrvtVtCurrentPJCSVPJCDiffV_Type()
)
prvtVtCurrentPJCSVPJCDiffV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtCurrentPJCSVPJCDiffV.setStatus("current")
_PrvtVtIntervalTable_Object = MibTable
prvtVtIntervalTable = _PrvtVtIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2)
)
if mibBuilder.loadTexts:
    prvtVtIntervalTable.setStatus("current")
_PrvtVtIntervalEntry_Object = MibTableRow
prvtVtIntervalEntry = _PrvtVtIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    prvtVtIntervalEntry.setStatus("current")
_PrvtVtIntervalFCs_Type = PerfIntervalCount
_PrvtVtIntervalFCs_Object = MibTableColumn
prvtVtIntervalFCs = _PrvtVtIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 1),
    _PrvtVtIntervalFCs_Type()
)
prvtVtIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalFCs.setStatus("current")
_PrvtVtIntervalESAs_Type = PerfIntervalCount
_PrvtVtIntervalESAs_Object = MibTableColumn
prvtVtIntervalESAs = _PrvtVtIntervalESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 2),
    _PrvtVtIntervalESAs_Type()
)
prvtVtIntervalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalESAs.setStatus("current")
_PrvtVtIntervalESBs_Type = PerfIntervalCount
_PrvtVtIntervalESBs_Object = MibTableColumn
prvtVtIntervalESBs = _PrvtVtIntervalESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 3),
    _PrvtVtIntervalESBs_Type()
)
prvtVtIntervalESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalESBs.setStatus("current")
_PrvtVtIntervalBBEs_Type = PerfIntervalCount
_PrvtVtIntervalBBEs_Object = MibTableColumn
prvtVtIntervalBBEs = _PrvtVtIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 4),
    _PrvtVtIntervalBBEs_Type()
)
prvtVtIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalBBEs.setStatus("current")
_PrvtVtIntervalAISs_Type = PerfIntervalCount
_PrvtVtIntervalAISs_Object = MibTableColumn
prvtVtIntervalAISs = _PrvtVtIntervalAISs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 5),
    _PrvtVtIntervalAISs_Type()
)
prvtVtIntervalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalAISs.setStatus("current")
_PrvtVtIntervalPPJCVGen_Type = PerfIntervalCount
_PrvtVtIntervalPPJCVGen_Object = MibTableColumn
prvtVtIntervalPPJCVGen = _PrvtVtIntervalPPJCVGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 6),
    _PrvtVtIntervalPPJCVGen_Type()
)
prvtVtIntervalPPJCVGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalPPJCVGen.setStatus("current")
_PrvtVtIntervalNPJCVGen_Type = PerfIntervalCount
_PrvtVtIntervalNPJCVGen_Object = MibTableColumn
prvtVtIntervalNPJCVGen = _PrvtVtIntervalNPJCVGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 7),
    _PrvtVtIntervalNPJCVGen_Type()
)
prvtVtIntervalNPJCVGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalNPJCVGen.setStatus("current")
_PrvtVtIntervalPPJCVDet_Type = PerfIntervalCount
_PrvtVtIntervalPPJCVDet_Object = MibTableColumn
prvtVtIntervalPPJCVDet = _PrvtVtIntervalPPJCVDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 8),
    _PrvtVtIntervalPPJCVDet_Type()
)
prvtVtIntervalPPJCVDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalPPJCVDet.setStatus("current")
_PrvtVtIntervalNPJCVDet_Type = PerfIntervalCount
_PrvtVtIntervalNPJCVDet_Object = MibTableColumn
prvtVtIntervalNPJCVDet = _PrvtVtIntervalNPJCVDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 9),
    _PrvtVtIntervalNPJCVDet_Type()
)
prvtVtIntervalNPJCVDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalNPJCVDet.setStatus("current")
_PrvtVtIntervalPJCSVDet_Type = PerfIntervalCount
_PrvtVtIntervalPJCSVDet_Object = MibTableColumn
prvtVtIntervalPJCSVDet = _PrvtVtIntervalPJCSVDet_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 10),
    _PrvtVtIntervalPJCSVDet_Type()
)
prvtVtIntervalPJCSVDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalPJCSVDet.setStatus("current")
_PrvtVtIntervalPJCSVGen_Type = PerfIntervalCount
_PrvtVtIntervalPJCSVGen_Object = MibTableColumn
prvtVtIntervalPJCSVGen = _PrvtVtIntervalPJCSVGen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 11),
    _PrvtVtIntervalPJCSVGen_Type()
)
prvtVtIntervalPJCSVGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalPJCSVGen.setStatus("current")
_PrvtVtIntervalPJCSVPJCDiffV_Type = PerfIntervalCount
_PrvtVtIntervalPJCSVPJCDiffV_Object = MibTableColumn
prvtVtIntervalPJCSVPJCDiffV = _PrvtVtIntervalPJCSVPJCDiffV_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 2, 1, 12),
    _PrvtVtIntervalPJCSVPJCDiffV_Type()
)
prvtVtIntervalPJCSVPJCDiffV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVtIntervalPJCSVPJCDiffV.setStatus("current")
_PrvtFarEndVtCurrentTable_Object = MibTable
prvtFarEndVtCurrentTable = _PrvtFarEndVtCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 3)
)
if mibBuilder.loadTexts:
    prvtFarEndVtCurrentTable.setStatus("current")
_PrvtFarEndVtCurrentEntry_Object = MibTableRow
prvtFarEndVtCurrentEntry = _PrvtFarEndVtCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    prvtFarEndVtCurrentEntry.setStatus("current")
_PrvtFarEndVtCurrentFCs_Type = PerfCurrentCount
_PrvtFarEndVtCurrentFCs_Object = MibTableColumn
prvtFarEndVtCurrentFCs = _PrvtFarEndVtCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 3, 1, 1),
    _PrvtFarEndVtCurrentFCs_Type()
)
prvtFarEndVtCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtCurrentFCs.setStatus("current")
_PrvtFarEndVtCurrentESAs_Type = PerfCurrentCount
_PrvtFarEndVtCurrentESAs_Object = MibTableColumn
prvtFarEndVtCurrentESAs = _PrvtFarEndVtCurrentESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 3, 1, 2),
    _PrvtFarEndVtCurrentESAs_Type()
)
prvtFarEndVtCurrentESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtCurrentESAs.setStatus("current")
_PrvtFarEndVtCurrentESBs_Type = PerfCurrentCount
_PrvtFarEndVtCurrentESBs_Object = MibTableColumn
prvtFarEndVtCurrentESBs = _PrvtFarEndVtCurrentESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 3, 1, 3),
    _PrvtFarEndVtCurrentESBs_Type()
)
prvtFarEndVtCurrentESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtCurrentESBs.setStatus("current")
_PrvtFarEndVtCurrentBBEs_Type = PerfCurrentCount
_PrvtFarEndVtCurrentBBEs_Object = MibTableColumn
prvtFarEndVtCurrentBBEs = _PrvtFarEndVtCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 3, 1, 4),
    _PrvtFarEndVtCurrentBBEs_Type()
)
prvtFarEndVtCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtCurrentBBEs.setStatus("current")
_PrvtFarEndVtCurrentRFIs_Type = PerfCurrentCount
_PrvtFarEndVtCurrentRFIs_Object = MibTableColumn
prvtFarEndVtCurrentRFIs = _PrvtFarEndVtCurrentRFIs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 3, 1, 5),
    _PrvtFarEndVtCurrentRFIs_Type()
)
prvtFarEndVtCurrentRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtCurrentRFIs.setStatus("current")
_PrvtFarEndVtIntervalTable_Object = MibTable
prvtFarEndVtIntervalTable = _PrvtFarEndVtIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 4)
)
if mibBuilder.loadTexts:
    prvtFarEndVtIntervalTable.setStatus("current")
_PrvtFarEndVtIntervalEntry_Object = MibTableRow
prvtFarEndVtIntervalEntry = _PrvtFarEndVtIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    prvtFarEndVtIntervalEntry.setStatus("current")
_PrvtFarEndVtIntervalFCs_Type = PerfIntervalCount
_PrvtFarEndVtIntervalFCs_Object = MibTableColumn
prvtFarEndVtIntervalFCs = _PrvtFarEndVtIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 4, 1, 1),
    _PrvtFarEndVtIntervalFCs_Type()
)
prvtFarEndVtIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtIntervalFCs.setStatus("current")
_PrvtFarEndVtIntervalESAs_Type = PerfIntervalCount
_PrvtFarEndVtIntervalESAs_Object = MibTableColumn
prvtFarEndVtIntervalESAs = _PrvtFarEndVtIntervalESAs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 4, 1, 2),
    _PrvtFarEndVtIntervalESAs_Type()
)
prvtFarEndVtIntervalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtIntervalESAs.setStatus("current")
_PrvtFarEndVtIntervalESBs_Type = PerfIntervalCount
_PrvtFarEndVtIntervalESBs_Object = MibTableColumn
prvtFarEndVtIntervalESBs = _PrvtFarEndVtIntervalESBs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 4, 1, 3),
    _PrvtFarEndVtIntervalESBs_Type()
)
prvtFarEndVtIntervalESBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtIntervalESBs.setStatus("current")
_PrvtFarEndVtIntervalBBEs_Type = PerfIntervalCount
_PrvtFarEndVtIntervalBBEs_Object = MibTableColumn
prvtFarEndVtIntervalBBEs = _PrvtFarEndVtIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 4, 1, 4),
    _PrvtFarEndVtIntervalBBEs_Type()
)
prvtFarEndVtIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtIntervalBBEs.setStatus("current")
_PrvtFarEndVtIntervalRFIs_Type = PerfIntervalCount
_PrvtFarEndVtIntervalRFIs_Object = MibTableColumn
prvtFarEndVtIntervalRFIs = _PrvtFarEndVtIntervalRFIs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 4, 1, 5),
    _PrvtFarEndVtIntervalRFIs_Type()
)
prvtFarEndVtIntervalRFIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtFarEndVtIntervalRFIs.setStatus("current")
_PrvtSonetVTAlarmsTable_Object = MibTable
prvtSonetVTAlarmsTable = _PrvtSonetVTAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 5)
)
if mibBuilder.loadTexts:
    prvtSonetVTAlarmsTable.setStatus("current")
_PrvtSonetVTAlarmsEntry_Object = MibTableRow
prvtSonetVTAlarmsEntry = _PrvtSonetVTAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 5, 1)
)
prvtSonetVTAlarmsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtSonetVTAlarmsEntry.setStatus("current")
_PrvtSonetVTAlarmType_Type = SonetVTAlarmType
_PrvtSonetVTAlarmType_Object = MibTableColumn
prvtSonetVTAlarmType = _PrvtSonetVTAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 5, 1, 1),
    _PrvtSonetVTAlarmType_Type()
)
prvtSonetVTAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtSonetVTAlarmType.setStatus("current")
_PrvtSonetVTAlarmStatus_Type = SonetAlarmStatus
_PrvtSonetVTAlarmStatus_Object = MibTableColumn
prvtSonetVTAlarmStatus = _PrvtSonetVTAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 1, 5, 5, 1, 2),
    _PrvtSonetVTAlarmStatus_Type()
)
prvtSonetVTAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtSonetVTAlarmStatus.setStatus("current")
_PrvtStatisticsConformance_ObjectIdentity = ObjectIdentity
prvtStatisticsConformance = _PrvtStatisticsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 2)
)
dsx1CurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtDSx1CurrentEntry")
)
prvtDSx1CurrentEntry.setIndexNames(*dsx1CurrentEntry.getIndexNames())
dsx1IntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtDSx1IntervalEntry")
)
prvtDSx1IntervalEntry.setIndexNames(*dsx1IntervalEntry.getIndexNames())
dsx1TotalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtDSx1TotalEntry")
)
prvtDSx1TotalEntry.setIndexNames(*dsx1TotalEntry.getIndexNames())
dsx1FarEndCurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtDSx1FarEndCurrentEntry")
)
prvtDSx1FarEndCurrentEntry.setIndexNames(*dsx1FarEndCurrentEntry.getIndexNames())
dsx1FarEndIntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtDSx1FarEndIntervalEntry")
)
prvtDSx1FarEndIntervalEntry.setIndexNames(*dsx1FarEndIntervalEntry.getIndexNames())
dsx1FarEndTotalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtDSx1FarEndTotalEntry")
)
prvtDSx1FarEndTotalEntry.setIndexNames(*dsx1FarEndTotalEntry.getIndexNames())
sonetSectionCurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtSectionCurrentEntry")
)
prvtSectionCurrentEntry.setIndexNames(*sonetSectionCurrentEntry.getIndexNames())
sonetSectionIntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtSectionIntervalEntry")
)
prvtSectionIntervalEntry.setIndexNames(*sonetSectionIntervalEntry.getIndexNames())
sonetLineCurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtLineCurrentEntry")
)
prvtLineCurrentEntry.setIndexNames(*sonetLineCurrentEntry.getIndexNames())
sonetLineIntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtLineIntervalEntry")
)
prvtLineIntervalEntry.setIndexNames(*sonetLineIntervalEntry.getIndexNames())
sonetFarEndLineCurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtFarEndLineCurrentEntry")
)
prvtFarEndLineCurrentEntry.setIndexNames(*sonetFarEndLineCurrentEntry.getIndexNames())
sonetFarEndLineIntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtFarEndLineIntervalEntry")
)
prvtFarEndLineIntervalEntry.setIndexNames(*sonetFarEndLineIntervalEntry.getIndexNames())
sonetPathCurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtPathCurrentEntry")
)
prvtPathCurrentEntry.setIndexNames(*sonetPathCurrentEntry.getIndexNames())
sonetPathIntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtPathIntervalEntry")
)
prvtPathIntervalEntry.setIndexNames(*sonetPathIntervalEntry.getIndexNames())
sonetFarEndPathCurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtFarEndPathCurrentEntry")
)
prvtFarEndPathCurrentEntry.setIndexNames(*sonetFarEndPathCurrentEntry.getIndexNames())
sonetFarEndPathIntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtFarEndPathIntervalEntry")
)
prvtFarEndPathIntervalEntry.setIndexNames(*sonetFarEndPathIntervalEntry.getIndexNames())
sonetVTCurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtVtCurrentEntry")
)
prvtVtCurrentEntry.setIndexNames(*sonetVTCurrentEntry.getIndexNames())
sonetVTIntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtVtIntervalEntry")
)
prvtVtIntervalEntry.setIndexNames(*sonetVTIntervalEntry.getIndexNames())
sonetFarEndVTCurrentEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtFarEndVtCurrentEntry")
)
prvtFarEndVtCurrentEntry.setIndexNames(*sonetFarEndVTCurrentEntry.getIndexNames())
sonetFarEndVTIntervalEntry.registerAugmentions(
    ("PRVT-STATISTICS-CES-MIB",
     "prvtFarEndVtIntervalEntry")
)
prvtFarEndVtIntervalEntry.setIndexNames(*sonetFarEndVTIntervalEntry.getIndexNames())

# Managed Objects groups


# Notification objects

prvtSonetSectionAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 0, 1)
)
prvtSonetSectionAlarms.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRVT-STATISTICS-CES-MIB", "prvtSonetSectionAlarmType"),
        ("PRVT-STATISTICS-CES-MIB", "prvtSonetSectionAlarmStatus"))
)
if mibBuilder.loadTexts:
    prvtSonetSectionAlarms.setStatus(
        "current"
    )

prvtSonetLineAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 0, 2)
)
prvtSonetLineAlarms.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRVT-STATISTICS-CES-MIB", "prvtSonetLineAlarmType"),
        ("PRVT-STATISTICS-CES-MIB", "prvtSonetLineAlarmStatus"))
)
if mibBuilder.loadTexts:
    prvtSonetLineAlarms.setStatus(
        "current"
    )

prvtSonetPathAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 0, 3)
)
prvtSonetPathAlarms.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRVT-STATISTICS-CES-MIB", "prvtSonetPathAlarmType"),
        ("PRVT-STATISTICS-CES-MIB", "prvtSonetPathAlarmStatus"))
)
if mibBuilder.loadTexts:
    prvtSonetPathAlarms.setStatus(
        "current"
    )

prvtSonetVTAlarms = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 114, 0, 4)
)
prvtSonetVTAlarms.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PRVT-STATISTICS-CES-MIB", "prvtSonetVTAlarmType"),
        ("PRVT-STATISTICS-CES-MIB", "prvtSonetVTAlarmStatus"))
)
if mibBuilder.loadTexts:
    prvtSonetVTAlarms.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-STATISTICS-CES-MIB",
    **{"SonetLineAlarmType": SonetLineAlarmType,
       "SonetSectionAlarmType": SonetSectionAlarmType,
       "SonetPathAlarmType": SonetPathAlarmType,
       "SonetVTAlarmType": SonetVTAlarmType,
       "SonetAlarmStatus": SonetAlarmStatus,
       "prvtStatisticsCESMib": prvtStatisticsCESMib,
       "prvtStatisticsNotifications": prvtStatisticsNotifications,
       "prvtSonetSectionAlarms": prvtSonetSectionAlarms,
       "prvtSonetLineAlarms": prvtSonetLineAlarms,
       "prvtSonetPathAlarms": prvtSonetPathAlarms,
       "prvtSonetVTAlarms": prvtSonetVTAlarms,
       "prvtStatisticsObjects": prvtStatisticsObjects,
       "prvtStatisticsDSx1": prvtStatisticsDSx1,
       "prvtDSx1CurrentTable": prvtDSx1CurrentTable,
       "prvtDSx1CurrentEntry": prvtDSx1CurrentEntry,
       "prvtDSx1CurrentBBEs": prvtDSx1CurrentBBEs,
       "prvtDSx1CurrentLSESs": prvtDSx1CurrentLSESs,
       "prvtDSx1CurrentPFCs": prvtDSx1CurrentPFCs,
       "prvtDSx1IntervalTable": prvtDSx1IntervalTable,
       "prvtDSx1IntervalEntry": prvtDSx1IntervalEntry,
       "prvtDSx1IntervalBBEs": prvtDSx1IntervalBBEs,
       "prvtDSx1IntervalLSESs": prvtDSx1IntervalLSESs,
       "prvtDSx1IntervalPFCs": prvtDSx1IntervalPFCs,
       "prvtDSx1TotalTable": prvtDSx1TotalTable,
       "prvtDSx1TotalEntry": prvtDSx1TotalEntry,
       "prvtDSx1TotalBBEs": prvtDSx1TotalBBEs,
       "prvtDSx1TotalLSESs": prvtDSx1TotalLSESs,
       "prvtDSx1TotalPFCs": prvtDSx1TotalPFCs,
       "prvtDSx1FarEndCurrentTable": prvtDSx1FarEndCurrentTable,
       "prvtDSx1FarEndCurrentEntry": prvtDSx1FarEndCurrentEntry,
       "prvtFarEndDSx1CurrentBBEs": prvtFarEndDSx1CurrentBBEs,
       "prvtFarEndDSx1CurrentPFCs": prvtFarEndDSx1CurrentPFCs,
       "prvtDSx1FarEndIntervalTable": prvtDSx1FarEndIntervalTable,
       "prvtDSx1FarEndIntervalEntry": prvtDSx1FarEndIntervalEntry,
       "prvtFarEndDSx1IntervalBBEs": prvtFarEndDSx1IntervalBBEs,
       "prvtFarEndDSx1IntervalPFCs": prvtFarEndDSx1IntervalPFCs,
       "prvtDSx1FarEndTotalTable": prvtDSx1FarEndTotalTable,
       "prvtDSx1FarEndTotalEntry": prvtDSx1FarEndTotalEntry,
       "prvtFarEndDSx1TotalBBEs": prvtFarEndDSx1TotalBBEs,
       "prvtFarEndDSx1TotalPFCs": prvtFarEndDSx1TotalPFCs,
       "prvtStatisticsSection": prvtStatisticsSection,
       "prvtSectionCurrentTable": prvtSectionCurrentTable,
       "prvtSectionCurrentEntry": prvtSectionCurrentEntry,
       "prvtSectionCurrentBBEs": prvtSectionCurrentBBEs,
       "prvtSectionCurrentESAs": prvtSectionCurrentESAs,
       "prvtSectionCurrentESBs": prvtSectionCurrentESBs,
       "prvtSectionCurrentUASs": prvtSectionCurrentUASs,
       "prvtSectionCurrentLOSSs": prvtSectionCurrentLOSSs,
       "prvtSectionCurrentOOFs": prvtSectionCurrentOOFs,
       "prvtSectionIntervalTable": prvtSectionIntervalTable,
       "prvtSectionIntervalEntry": prvtSectionIntervalEntry,
       "prvtSectionIntervalBBEs": prvtSectionIntervalBBEs,
       "prvtSectionIntervalESAs": prvtSectionIntervalESAs,
       "prvtSectionIntervalESBs": prvtSectionIntervalESBs,
       "prvtSectionIntervalUASs": prvtSectionIntervalUASs,
       "prvtSectionIntervalLOSSs": prvtSectionIntervalLOSSs,
       "prvtSectionIntervalOOFs": prvtSectionIntervalOOFs,
       "prvtSonetSectionAlarmsTable": prvtSonetSectionAlarmsTable,
       "prvtSonetSectionAlarmsEntry": prvtSonetSectionAlarmsEntry,
       "prvtSonetSectionAlarmType": prvtSonetSectionAlarmType,
       "prvtSonetSectionAlarmStatus": prvtSonetSectionAlarmStatus,
       "prvtStatisticsLine": prvtStatisticsLine,
       "prvtLineCurrentTable": prvtLineCurrentTable,
       "prvtLineCurrentEntry": prvtLineCurrentEntry,
       "prvtLineCurrentFCs": prvtLineCurrentFCs,
       "prvtLineCurrentBBEs": prvtLineCurrentBBEs,
       "prvtLineCurrentESAs": prvtLineCurrentESAs,
       "prvtLineCurrentESBs": prvtLineCurrentESBs,
       "prvtLineCurrentLBCs": prvtLineCurrentLBCs,
       "prvtLineCurrentOPRs": prvtLineCurrentOPRs,
       "prtvLineCurrentOPTs": prtvLineCurrentOPTs,
       "prvtLineCurrentAISs": prvtLineCurrentAISs,
       "prvtLineCurrentPSCs": prvtLineCurrentPSCs,
       "prvtLineCurrentPSDs": prvtLineCurrentPSDs,
       "prvtLineIntervalTable": prvtLineIntervalTable,
       "prvtLineIntervalEntry": prvtLineIntervalEntry,
       "prvtLineIntervalFCs": prvtLineIntervalFCs,
       "prvtLineIntervalBBEs": prvtLineIntervalBBEs,
       "prvtLineIntervalESAs": prvtLineIntervalESAs,
       "prvtLineIntervalESBs": prvtLineIntervalESBs,
       "prvtLineIntervalLBCs": prvtLineIntervalLBCs,
       "prvtLineIntervalOPRs": prvtLineIntervalOPRs,
       "prtvLineIntervalOPTs": prtvLineIntervalOPTs,
       "prvtLineIntevalAISs": prvtLineIntevalAISs,
       "prvtLineIntervalPSCs": prvtLineIntervalPSCs,
       "prvtLineIntervalPSDs": prvtLineIntervalPSDs,
       "prvtFarEndLineCurrentTable": prvtFarEndLineCurrentTable,
       "prvtFarEndLineCurrentEntry": prvtFarEndLineCurrentEntry,
       "prvtFarEndLineCurrentFCs": prvtFarEndLineCurrentFCs,
       "prvtFarEndLineCurrentBBEs": prvtFarEndLineCurrentBBEs,
       "prvtFarEndLineCurrentESAs": prvtFarEndLineCurrentESAs,
       "prvtFarEndLineCurrentESBs": prvtFarEndLineCurrentESBs,
       "prvtFarEndLineCurrentAISs": prvtFarEndLineCurrentAISs,
       "prvtFarEndLineCurrentRFIs": prvtFarEndLineCurrentRFIs,
       "prvtFarEndLineIntervalTable": prvtFarEndLineIntervalTable,
       "prvtFarEndLineIntervalEntry": prvtFarEndLineIntervalEntry,
       "prvtFarEndLineIntervalFCs": prvtFarEndLineIntervalFCs,
       "prvtFarEndLineIntervalBBEs": prvtFarEndLineIntervalBBEs,
       "prvtFarEndLineIntervalESAs": prvtFarEndLineIntervalESAs,
       "prvtFarEndLineIntervalESBs": prvtFarEndLineIntervalESBs,
       "prvtFarEndLineIntervalAISs": prvtFarEndLineIntervalAISs,
       "prvtFarEndLineIntervalRFIs": prvtFarEndLineIntervalRFIs,
       "prvtSonetLineAlarmsTable": prvtSonetLineAlarmsTable,
       "prvtSonetLineAlarmsEntry": prvtSonetLineAlarmsEntry,
       "prvtSonetLineAlarmType": prvtSonetLineAlarmType,
       "prvtSonetLineAlarmStatus": prvtSonetLineAlarmStatus,
       "prvtStatisticsPath": prvtStatisticsPath,
       "prvtPathCurrentTable": prvtPathCurrentTable,
       "prvtPathCurrentEntry": prvtPathCurrentEntry,
       "prvtPathCurrentFCs": prvtPathCurrentFCs,
       "prvtPathCurrentESAs": prvtPathCurrentESAs,
       "prvtPathCurrentESBs": prvtPathCurrentESBs,
       "prvtPathCurrentBBEs": prvtPathCurrentBBEs,
       "prvtPathCurrentAISs": prvtPathCurrentAISs,
       "prvtPathCurrentPPJCPGen": prvtPathCurrentPPJCPGen,
       "prvtPathCurrentNPJCPGen": prvtPathCurrentNPJCPGen,
       "prvtPathCurrentPPJCPDet": prvtPathCurrentPPJCPDet,
       "prvtPathCurrentNPJCPDet": prvtPathCurrentNPJCPDet,
       "prvtPathCurrentPJCSPDet": prvtPathCurrentPJCSPDet,
       "prvtPathCurrentPJCSPGen": prvtPathCurrentPJCSPGen,
       "prvtPathCurrentJCDiffP": prvtPathCurrentJCDiffP,
       "prvtPathIntervalTable": prvtPathIntervalTable,
       "prvtPathIntervalEntry": prvtPathIntervalEntry,
       "prvtPathIntervalFCs": prvtPathIntervalFCs,
       "prvtPathIntervalESAs": prvtPathIntervalESAs,
       "prvtPathIntervalESBs": prvtPathIntervalESBs,
       "prvtPathIntervalBBEs": prvtPathIntervalBBEs,
       "prvtPathIntervalAISs": prvtPathIntervalAISs,
       "prvtPathIntervalPPJCPGen": prvtPathIntervalPPJCPGen,
       "prvtPathIntervalNPJCPGen": prvtPathIntervalNPJCPGen,
       "prvtPathIntervalPPJCPDet": prvtPathIntervalPPJCPDet,
       "prvtPathIntervalNPJCPDet": prvtPathIntervalNPJCPDet,
       "prvtPathIntervalPJCSPDet": prvtPathIntervalPJCSPDet,
       "prvtPathIntervalPJCSPGen": prvtPathIntervalPJCSPGen,
       "prvtPathIntervalJCDiffP": prvtPathIntervalJCDiffP,
       "prvtFarEndPathCurrentTable": prvtFarEndPathCurrentTable,
       "prvtFarEndPathCurrentEntry": prvtFarEndPathCurrentEntry,
       "prvtFarEndPathCurrentFCs": prvtFarEndPathCurrentFCs,
       "prvtFarEndPathCurrentESAs": prvtFarEndPathCurrentESAs,
       "prvtFarEndPathCurrentESBs": prvtFarEndPathCurrentESBs,
       "prvtFarEndPathCurrentBBEs": prvtFarEndPathCurrentBBEs,
       "prvtFarEndPathCurrentRFIs": prvtFarEndPathCurrentRFIs,
       "prvtFarEndPathIntervalTable": prvtFarEndPathIntervalTable,
       "prvtFarEndPathIntervalEntry": prvtFarEndPathIntervalEntry,
       "prvtFarEndPathIntervalFCs": prvtFarEndPathIntervalFCs,
       "prvtFarEndPathIntervalESAs": prvtFarEndPathIntervalESAs,
       "prvtFarEndPathIntervalESBs": prvtFarEndPathIntervalESBs,
       "prvtFarEndPathIntervalBBEs": prvtFarEndPathIntervalBBEs,
       "prvtFarEndPathIntervalRFIs": prvtFarEndPathIntervalRFIs,
       "prvtSonetPathAlarmsTable": prvtSonetPathAlarmsTable,
       "prvtSonetPathAlarmsEntry": prvtSonetPathAlarmsEntry,
       "prvtSonetPathAlarmType": prvtSonetPathAlarmType,
       "prvtSonetPathAlarmStatus": prvtSonetPathAlarmStatus,
       "prvtStatisticsVt": prvtStatisticsVt,
       "prvtVtCurrentTable": prvtVtCurrentTable,
       "prvtVtCurrentEntry": prvtVtCurrentEntry,
       "prvtVtCurrentFCs": prvtVtCurrentFCs,
       "prvtVtCurrentESAs": prvtVtCurrentESAs,
       "prvtVtCurrentESBs": prvtVtCurrentESBs,
       "prvtVtCurrentBBEs": prvtVtCurrentBBEs,
       "prvtVtCurrentAISs": prvtVtCurrentAISs,
       "prvtVtCurrentPPJCVGen": prvtVtCurrentPPJCVGen,
       "prvtVtCurrentNPJCVGen": prvtVtCurrentNPJCVGen,
       "prvtVtCurrentPPJCVDet": prvtVtCurrentPPJCVDet,
       "prvtVtCurrentNPJCVDet": prvtVtCurrentNPJCVDet,
       "prvtVtCurrentPJCSVDet": prvtVtCurrentPJCSVDet,
       "prvtVtCurrentPJCSVGen": prvtVtCurrentPJCSVGen,
       "prvtVtCurrentPJCSVPJCDiffV": prvtVtCurrentPJCSVPJCDiffV,
       "prvtVtIntervalTable": prvtVtIntervalTable,
       "prvtVtIntervalEntry": prvtVtIntervalEntry,
       "prvtVtIntervalFCs": prvtVtIntervalFCs,
       "prvtVtIntervalESAs": prvtVtIntervalESAs,
       "prvtVtIntervalESBs": prvtVtIntervalESBs,
       "prvtVtIntervalBBEs": prvtVtIntervalBBEs,
       "prvtVtIntervalAISs": prvtVtIntervalAISs,
       "prvtVtIntervalPPJCVGen": prvtVtIntervalPPJCVGen,
       "prvtVtIntervalNPJCVGen": prvtVtIntervalNPJCVGen,
       "prvtVtIntervalPPJCVDet": prvtVtIntervalPPJCVDet,
       "prvtVtIntervalNPJCVDet": prvtVtIntervalNPJCVDet,
       "prvtVtIntervalPJCSVDet": prvtVtIntervalPJCSVDet,
       "prvtVtIntervalPJCSVGen": prvtVtIntervalPJCSVGen,
       "prvtVtIntervalPJCSVPJCDiffV": prvtVtIntervalPJCSVPJCDiffV,
       "prvtFarEndVtCurrentTable": prvtFarEndVtCurrentTable,
       "prvtFarEndVtCurrentEntry": prvtFarEndVtCurrentEntry,
       "prvtFarEndVtCurrentFCs": prvtFarEndVtCurrentFCs,
       "prvtFarEndVtCurrentESAs": prvtFarEndVtCurrentESAs,
       "prvtFarEndVtCurrentESBs": prvtFarEndVtCurrentESBs,
       "prvtFarEndVtCurrentBBEs": prvtFarEndVtCurrentBBEs,
       "prvtFarEndVtCurrentRFIs": prvtFarEndVtCurrentRFIs,
       "prvtFarEndVtIntervalTable": prvtFarEndVtIntervalTable,
       "prvtFarEndVtIntervalEntry": prvtFarEndVtIntervalEntry,
       "prvtFarEndVtIntervalFCs": prvtFarEndVtIntervalFCs,
       "prvtFarEndVtIntervalESAs": prvtFarEndVtIntervalESAs,
       "prvtFarEndVtIntervalESBs": prvtFarEndVtIntervalESBs,
       "prvtFarEndVtIntervalBBEs": prvtFarEndVtIntervalBBEs,
       "prvtFarEndVtIntervalRFIs": prvtFarEndVtIntervalRFIs,
       "prvtSonetVTAlarmsTable": prvtSonetVTAlarmsTable,
       "prvtSonetVTAlarmsEntry": prvtSonetVTAlarmsEntry,
       "prvtSonetVTAlarmType": prvtSonetVTAlarmType,
       "prvtSonetVTAlarmStatus": prvtSonetVTAlarmStatus,
       "prvtStatisticsConformance": prvtStatisticsConformance}
)
