# SNMP MIB module (CIENA-WS-PLATFORM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-PLATFORM-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:09 2025
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

(cienaWsPlatformConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsPlatformConfig")

(EnabledDisabledEnum,) = mibBuilder.importSymbols(
    "CIENA-WS-PLATFORM-TYPEDEFS-MIB",
    "EnabledDisabledEnum")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaWsPlatformPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22)
)
if mibBuilder.loadTexts:
    cienaWsPlatformPmMIB.setRevisions(
        ("2018-12-20 00:00",
         "2018-09-20 00:00",
         "2018-08-28 00:00",
         "2018-08-15 00:00",
         "2018-07-24 00:00",
         "2018-04-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmConfigurationMode(TextualConvention, Integer32):
    status = "current"
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
          ("autoCreated", 1),
          ("userCreated", 2))
    )



class PmEthernetMonType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64)
        )
    )
    namedValues = NamedValues(
        *(("rxBytes", 0),
          ("rxPkts", 1),
          ("rxCrcErrorPkts", 2),
          ("rxMcastPkts", 3),
          ("rxBcastPkts", 4),
          ("rxUndersizePkts", 5),
          ("rxOversizePkts", 6),
          ("rxFragmentPkts", 7),
          ("rxJabberPkts", 8),
          ("rxLOutRangePkts", 9),
          ("rxPausePkts", 10),
          ("rx64OctsPkts", 11),
          ("rx65To127OctsPkts", 12),
          ("rx128To255OctsPkts", 13),
          ("rx256To511Octs", 14),
          ("rx512To1023OctsPkts", 15),
          ("rx1024To1518OctsPkts", 16),
          ("rx1519ToJumboOctsPkts", 17),
          ("rxJumboOctsPkts", 18),
          ("rxBytesPerSec", 19),
          ("rxFramesPerSec", 20),
          ("rxAverageLinkUtilization", 21),
          ("rxMinLinkUtilization", 22),
          ("rxMaxLinkUtilization", 23),
          ("rxBlockErrorCount", 24),
          ("rxPcsLaneBipErrorCount", 25),
          ("rxFrameErrorRatio", 26),
          ("txBytes", 27),
          ("txPkts", 28),
          ("txExcessiveDeferredPkts", 29),
          ("txUnderRunPkts", 30),
          ("txCrcErrorPkts", 31),
          ("txLenCheckErrorPkts", 32),
          ("txLenOutOfRangePkts", 33),
          ("txPausePkts", 34),
          ("txGiantPkts", 35),
          ("txMcastPkts", 36),
          ("txBcastPkts", 37),
          ("txPacketsDropCountSummary", 38),
          ("tx64OctsPkts", 39),
          ("tx65To127OctsPkts", 40),
          ("tx128To255OctsPkts", 41),
          ("tx256To511OctsPkts", 42),
          ("tx512To1023OctsPkts", 43),
          ("tx1024To1518OctsPkts", 44),
          ("tx1519ToJumboOctsPkts", 45),
          ("txJumboOctsPkts", 46),
          ("txBytesPerSec", 47),
          ("txFramesPerSec", 48),
          ("txAverageLinkUtilization", 49),
          ("txBlockErrorCount", 50),
          ("txPcsLaneBipErrorCount", 51),
          ("txMinLinkUtilization", 52),
          ("txMaxLinkUtilization", 53),
          ("txFrameErrorRatio", 54),
          ("pcsES", 55),
          ("pcsSES", 56),
          ("pcsUAS", 57),
          ("syncHeaderErrorCount", 58),
          ("fecCorrCodewordCount", 59),
          ("fecUncorrCodewordCount", 60),
          ("fecErrorCount0", 61),
          ("fecErrorCount1", 62),
          ("fecErrorCount2", 63),
          ("fecErrorCount3", 64))
    )



class PmOtuMonType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("otuBBE", 0),
          ("otuES", 1),
          ("otuSES", 2),
          ("otuUAS", 3),
          ("otuFeBBE", 4),
          ("otuFeES", 5),
          ("otuFeSES", 6),
          ("otuFeUAS", 7))
    )



class PmOpticalPowerMonType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("rxMinimum", 0),
          ("rxMaximum", 1),
          ("rxAverage", 2),
          ("txMinimum", 3),
          ("txMaximum", 4),
          ("txAverage", 5),
          ("chanRxMinimum", 6),
          ("chanRxMaximum", 7),
          ("chanRxAverage", 8),
          ("aggregateRxMinimum", 9),
          ("aggregateRxMaximum", 10),
          ("aggregateRxAverage", 11),
          ("aggregateTxMinimum", 12),
          ("aggregateTxMaximum", 13),
          ("aggregateTxAverage", 14))
    )



class PmOduMonType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("oduBBE", 0),
          ("oduES", 1),
          ("oduSES", 2),
          ("oduUAS", 3),
          ("oduFeBBE", 4),
          ("oduFeES", 5),
          ("oduFeSES", 6),
          ("oduFeUAS", 7))
    )



class PmModemMonType(TextualConvention, Integer32):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("bitErrorRate", 0),
          ("berMaximum", 1),
          ("qFactor", 2),
          ("qMinimum", 3),
          ("qMaximum", 4),
          ("fecUncorrectedSecs", 5),
          ("unCorrectedBlockCount", 6),
          ("highCorrectionCountSeconds", 7),
          ("dgdMaximum", 8),
          ("dgdAverage", 9),
          ("pdlMaximum", 10),
          ("pdlAverage", 11),
          ("esnrAvg", 12),
          ("esnrMax", 13),
          ("esnrMin", 14),
          ("osnrAvg", 15),
          ("osnrMax", 16),
          ("osnrMin", 17),
          ("cdAvg", 18),
          ("cdMax", 19),
          ("cdMin", 20),
          ("qStdev", 21))
    )



class PmGcmMonType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gcmErrorCount", 0),
          ("gcmSES", 1),
          ("gcmUAS", 2))
    )



class PmPhotonicsMonType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("returnLossMinimum", 0),
          ("returnLossMaximum", 1),
          ("returnLossAverage", 2),
          ("rxSpanLossMinimum", 3),
          ("rxSpanLossMaximum", 4),
          ("rxSpanLossAverage", 5),
          ("txSpanLossMinimum", 6),
          ("txSpanLossMaximum", 7),
          ("txSpanLossAverage", 8))
    )



# MIB Managed Objects in the order of their OIDs

_PmObjects_ObjectIdentity = ObjectIdentity
pmObjects = _PmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 1)
)
_PmConformance_ObjectIdentity = ObjectIdentity
pmConformance = _PmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 2)
)
_PmGroups_ObjectIdentity = ObjectIdentity
pmGroups = _PmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 2, 1)
)
_PmCompliances_ObjectIdentity = ObjectIdentity
pmCompliances = _PmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 2, 2)
)
_PmGlobalConfigTable_Object = MibTable
pmGlobalConfigTable = _PmGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 3)
)
if mibBuilder.loadTexts:
    pmGlobalConfigTable.setStatus("current")
_PmGlobalConfigEntry_Object = MibTableRow
pmGlobalConfigEntry = _PmGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 3, 1)
)
pmGlobalConfigEntry.setIndexNames(
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmGlobalConfigTableSnmpKey"),
)
if mibBuilder.loadTexts:
    pmGlobalConfigEntry.setStatus("current")


class _PmGlobalConfigTableSnmpKey_Type(Integer32):
    """Custom type pmGlobalConfigTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PmGlobalConfigTableSnmpKey_Type.__name__ = "Integer32"
_PmGlobalConfigTableSnmpKey_Object = MibTableColumn
pmGlobalConfigTableSnmpKey = _PmGlobalConfigTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 3, 1, 1),
    _PmGlobalConfigTableSnmpKey_Type()
)
pmGlobalConfigTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmGlobalConfigTableSnmpKey.setStatus("current")
_PmAdminState_Type = EnabledDisabledEnum
_PmAdminState_Object = MibTableColumn
pmAdminState = _PmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 3, 1, 2),
    _PmAdminState_Type()
)
pmAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmAdminState.setStatus("current")
_PmEthernetCurrent15minStatsTable_Object = MibTable
pmEthernetCurrent15minStatsTable = _PmEthernetCurrent15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4)
)
if mibBuilder.loadTexts:
    pmEthernetCurrent15minStatsTable.setStatus("current")
_PmEthernetCurrent15minStatsEntry_Object = MibTableRow
pmEthernetCurrent15minStatsEntry = _PmEthernetCurrent15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1)
)
pmEthernetCurrent15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmEthernet15minMonType"),
)
if mibBuilder.loadTexts:
    pmEthernetCurrent15minStatsEntry.setStatus("current")
_PmEthernet15minMonType_Type = PmEthernetMonType
_PmEthernet15minMonType_Object = MibTableColumn
pmEthernet15minMonType = _PmEthernet15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1, 1),
    _PmEthernet15minMonType_Type()
)
pmEthernet15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmEthernet15minMonType.setStatus("current")
_PmEthernet15minMonTypeDescr_Type = DisplayString
_PmEthernet15minMonTypeDescr_Object = MibTableColumn
pmEthernet15minMonTypeDescr = _PmEthernet15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1, 2),
    _PmEthernet15minMonTypeDescr_Type()
)
pmEthernet15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet15minMonTypeDescr.setStatus("current")
_PmEthernet15minIfIndexDescr_Type = DisplayString
_PmEthernet15minIfIndexDescr_Object = MibTableColumn
pmEthernet15minIfIndexDescr = _PmEthernet15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1, 3),
    _PmEthernet15minIfIndexDescr_Type()
)
pmEthernet15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet15minIfIndexDescr.setStatus("current")
_PmEthernet15minMonValue_Type = DisplayString
_PmEthernet15minMonValue_Object = MibTableColumn
pmEthernet15minMonValue = _PmEthernet15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1, 4),
    _PmEthernet15minMonValue_Type()
)
pmEthernet15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet15minMonValue.setStatus("current")
_PmEthernet15minMonIDF_Type = DisplayString
_PmEthernet15minMonIDF_Object = MibTableColumn
pmEthernet15minMonIDF = _PmEthernet15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1, 5),
    _PmEthernet15minMonIDF_Type()
)
pmEthernet15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet15minMonIDF.setStatus("current")
_PmEthernet15minMonSupported_Type = TruthValue
_PmEthernet15minMonSupported_Object = MibTableColumn
pmEthernet15minMonSupported = _PmEthernet15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1, 6),
    _PmEthernet15minMonSupported_Type()
)
pmEthernet15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet15minMonSupported.setStatus("current")
_PmEthernet15minAdminState_Type = EnabledDisabledEnum
_PmEthernet15minAdminState_Object = MibTableColumn
pmEthernet15minAdminState = _PmEthernet15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1, 7),
    _PmEthernet15minAdminState_Type()
)
pmEthernet15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet15minAdminState.setStatus("current")
_PmEthernet15minMonStartDateTime_Type = DisplayString
_PmEthernet15minMonStartDateTime_Object = MibTableColumn
pmEthernet15minMonStartDateTime = _PmEthernet15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 4, 1, 8),
    _PmEthernet15minMonStartDateTime_Type()
)
pmEthernet15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet15minMonStartDateTime.setStatus("current")
_PmEthernetCurrent24HrStatsTable_Object = MibTable
pmEthernetCurrent24HrStatsTable = _PmEthernetCurrent24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5)
)
if mibBuilder.loadTexts:
    pmEthernetCurrent24HrStatsTable.setStatus("current")
_PmEthernetCurrent24HrStatsEntry_Object = MibTableRow
pmEthernetCurrent24HrStatsEntry = _PmEthernetCurrent24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1)
)
pmEthernetCurrent24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmEthernet24HrMonType"),
)
if mibBuilder.loadTexts:
    pmEthernetCurrent24HrStatsEntry.setStatus("current")
_PmEthernet24HrMonType_Type = PmEthernetMonType
_PmEthernet24HrMonType_Object = MibTableColumn
pmEthernet24HrMonType = _PmEthernet24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1, 1),
    _PmEthernet24HrMonType_Type()
)
pmEthernet24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmEthernet24HrMonType.setStatus("current")
_PmEthernet24HrMonTypeDescr_Type = DisplayString
_PmEthernet24HrMonTypeDescr_Object = MibTableColumn
pmEthernet24HrMonTypeDescr = _PmEthernet24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1, 2),
    _PmEthernet24HrMonTypeDescr_Type()
)
pmEthernet24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet24HrMonTypeDescr.setStatus("current")
_PmEthernet24HrIfIndexDescr_Type = DisplayString
_PmEthernet24HrIfIndexDescr_Object = MibTableColumn
pmEthernet24HrIfIndexDescr = _PmEthernet24HrIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1, 3),
    _PmEthernet24HrIfIndexDescr_Type()
)
pmEthernet24HrIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet24HrIfIndexDescr.setStatus("current")
_PmEthernet24HrMonValue_Type = DisplayString
_PmEthernet24HrMonValue_Object = MibTableColumn
pmEthernet24HrMonValue = _PmEthernet24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1, 4),
    _PmEthernet24HrMonValue_Type()
)
pmEthernet24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet24HrMonValue.setStatus("current")
_PmEthernet24HrMonIDF_Type = DisplayString
_PmEthernet24HrMonIDF_Object = MibTableColumn
pmEthernet24HrMonIDF = _PmEthernet24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1, 5),
    _PmEthernet24HrMonIDF_Type()
)
pmEthernet24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet24HrMonIDF.setStatus("current")
_PmEthernet24HrMonSupported_Type = TruthValue
_PmEthernet24HrMonSupported_Object = MibTableColumn
pmEthernet24HrMonSupported = _PmEthernet24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1, 6),
    _PmEthernet24HrMonSupported_Type()
)
pmEthernet24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet24HrMonSupported.setStatus("current")
_PmEthernet24HrAdminState_Type = EnabledDisabledEnum
_PmEthernet24HrAdminState_Object = MibTableColumn
pmEthernet24HrAdminState = _PmEthernet24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1, 7),
    _PmEthernet24HrAdminState_Type()
)
pmEthernet24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet24HrAdminState.setStatus("current")
_PmEthernet24HrMonStartDateTime_Type = DisplayString
_PmEthernet24HrMonStartDateTime_Object = MibTableColumn
pmEthernet24HrMonStartDateTime = _PmEthernet24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 5, 1, 8),
    _PmEthernet24HrMonStartDateTime_Type()
)
pmEthernet24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernet24HrMonStartDateTime.setStatus("current")
_PmEthernetUntimedStatsTable_Object = MibTable
pmEthernetUntimedStatsTable = _PmEthernetUntimedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6)
)
if mibBuilder.loadTexts:
    pmEthernetUntimedStatsTable.setStatus("current")
_PmEthernetUntimedStatsEntry_Object = MibTableRow
pmEthernetUntimedStatsEntry = _PmEthernetUntimedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1)
)
pmEthernetUntimedStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmEthernetUntimedMonType"),
)
if mibBuilder.loadTexts:
    pmEthernetUntimedStatsEntry.setStatus("current")
_PmEthernetUntimedMonType_Type = PmEthernetMonType
_PmEthernetUntimedMonType_Object = MibTableColumn
pmEthernetUntimedMonType = _PmEthernetUntimedMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1, 1),
    _PmEthernetUntimedMonType_Type()
)
pmEthernetUntimedMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmEthernetUntimedMonType.setStatus("current")
_PmEthernetUntimedMonTypeDescr_Type = DisplayString
_PmEthernetUntimedMonTypeDescr_Object = MibTableColumn
pmEthernetUntimedMonTypeDescr = _PmEthernetUntimedMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1, 2),
    _PmEthernetUntimedMonTypeDescr_Type()
)
pmEthernetUntimedMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetUntimedMonTypeDescr.setStatus("current")
_PmEthernetUntimedIfIndexDescr_Type = DisplayString
_PmEthernetUntimedIfIndexDescr_Object = MibTableColumn
pmEthernetUntimedIfIndexDescr = _PmEthernetUntimedIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1, 3),
    _PmEthernetUntimedIfIndexDescr_Type()
)
pmEthernetUntimedIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetUntimedIfIndexDescr.setStatus("current")
_PmEthernetUntimedMonValue_Type = DisplayString
_PmEthernetUntimedMonValue_Object = MibTableColumn
pmEthernetUntimedMonValue = _PmEthernetUntimedMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1, 4),
    _PmEthernetUntimedMonValue_Type()
)
pmEthernetUntimedMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetUntimedMonValue.setStatus("current")
_PmEthernetUntimedMonIDF_Type = DisplayString
_PmEthernetUntimedMonIDF_Object = MibTableColumn
pmEthernetUntimedMonIDF = _PmEthernetUntimedMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1, 5),
    _PmEthernetUntimedMonIDF_Type()
)
pmEthernetUntimedMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetUntimedMonIDF.setStatus("current")
_PmEthernetUntimedMonSupported_Type = TruthValue
_PmEthernetUntimedMonSupported_Object = MibTableColumn
pmEthernetUntimedMonSupported = _PmEthernetUntimedMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1, 6),
    _PmEthernetUntimedMonSupported_Type()
)
pmEthernetUntimedMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetUntimedMonSupported.setStatus("current")
_PmEthernetUntimedAdminState_Type = EnabledDisabledEnum
_PmEthernetUntimedAdminState_Object = MibTableColumn
pmEthernetUntimedAdminState = _PmEthernetUntimedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1, 7),
    _PmEthernetUntimedAdminState_Type()
)
pmEthernetUntimedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetUntimedAdminState.setStatus("current")
_PmEthernetUntimedMonStartDateTime_Type = DisplayString
_PmEthernetUntimedMonStartDateTime_Object = MibTableColumn
pmEthernetUntimedMonStartDateTime = _PmEthernetUntimedMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 6, 1, 8),
    _PmEthernetUntimedMonStartDateTime_Type()
)
pmEthernetUntimedMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetUntimedMonStartDateTime.setStatus("current")
_PmEthernetHistory15minStatsTable_Object = MibTable
pmEthernetHistory15minStatsTable = _PmEthernetHistory15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7)
)
if mibBuilder.loadTexts:
    pmEthernetHistory15minStatsTable.setStatus("current")
_PmEthernetHistory15minStatsEntry_Object = MibTableRow
pmEthernetHistory15minStatsEntry = _PmEthernetHistory15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1)
)
pmEthernetHistory15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minBinIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minMonType"),
)
if mibBuilder.loadTexts:
    pmEthernetHistory15minStatsEntry.setStatus("current")


class _PmEthernetHistory15minBinIndex_Type(Integer32):
    """Custom type pmEthernetHistory15minBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmEthernetHistory15minBinIndex_Type.__name__ = "Integer32"
_PmEthernetHistory15minBinIndex_Object = MibTableColumn
pmEthernetHistory15minBinIndex = _PmEthernetHistory15minBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 1),
    _PmEthernetHistory15minBinIndex_Type()
)
pmEthernetHistory15minBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmEthernetHistory15minBinIndex.setStatus("current")
_PmEthernetHistory15minMonType_Type = PmEthernetMonType
_PmEthernetHistory15minMonType_Object = MibTableColumn
pmEthernetHistory15minMonType = _PmEthernetHistory15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 2),
    _PmEthernetHistory15minMonType_Type()
)
pmEthernetHistory15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmEthernetHistory15minMonType.setStatus("current")
_PmEthernetHistory15minMonTypeDescr_Type = DisplayString
_PmEthernetHistory15minMonTypeDescr_Object = MibTableColumn
pmEthernetHistory15minMonTypeDescr = _PmEthernetHistory15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 3),
    _PmEthernetHistory15minMonTypeDescr_Type()
)
pmEthernetHistory15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory15minMonTypeDescr.setStatus("current")
_PmEthernetHistory15minIfIndexDescr_Type = DisplayString
_PmEthernetHistory15minIfIndexDescr_Object = MibTableColumn
pmEthernetHistory15minIfIndexDescr = _PmEthernetHistory15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 4),
    _PmEthernetHistory15minIfIndexDescr_Type()
)
pmEthernetHistory15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory15minIfIndexDescr.setStatus("current")
_PmEthernetHistory15minMonValue_Type = DisplayString
_PmEthernetHistory15minMonValue_Object = MibTableColumn
pmEthernetHistory15minMonValue = _PmEthernetHistory15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 5),
    _PmEthernetHistory15minMonValue_Type()
)
pmEthernetHistory15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory15minMonValue.setStatus("current")
_PmEthernetHistory15minMonIDF_Type = DisplayString
_PmEthernetHistory15minMonIDF_Object = MibTableColumn
pmEthernetHistory15minMonIDF = _PmEthernetHistory15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 6),
    _PmEthernetHistory15minMonIDF_Type()
)
pmEthernetHistory15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory15minMonIDF.setStatus("current")
_PmEthernetHistory15minMonSupported_Type = TruthValue
_PmEthernetHistory15minMonSupported_Object = MibTableColumn
pmEthernetHistory15minMonSupported = _PmEthernetHistory15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 7),
    _PmEthernetHistory15minMonSupported_Type()
)
pmEthernetHistory15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory15minMonSupported.setStatus("current")
_PmEthernetHistory15minAdminState_Type = EnabledDisabledEnum
_PmEthernetHistory15minAdminState_Object = MibTableColumn
pmEthernetHistory15minAdminState = _PmEthernetHistory15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 8),
    _PmEthernetHistory15minAdminState_Type()
)
pmEthernetHistory15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory15minAdminState.setStatus("current")
_PmEthernetHistory15minMonStartDateTime_Type = DisplayString
_PmEthernetHistory15minMonStartDateTime_Object = MibTableColumn
pmEthernetHistory15minMonStartDateTime = _PmEthernetHistory15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 7, 1, 9),
    _PmEthernetHistory15minMonStartDateTime_Type()
)
pmEthernetHistory15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory15minMonStartDateTime.setStatus("current")
_PmEthernetHistory24HrStatsTable_Object = MibTable
pmEthernetHistory24HrStatsTable = _PmEthernetHistory24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8)
)
if mibBuilder.loadTexts:
    pmEthernetHistory24HrStatsTable.setStatus("current")
_PmEthernetHistory24HrStatsEntry_Object = MibTableRow
pmEthernetHistory24HrStatsEntry = _PmEthernetHistory24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1)
)
pmEthernetHistory24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory24HrMonType"),
)
if mibBuilder.loadTexts:
    pmEthernetHistory24HrStatsEntry.setStatus("current")
_PmEthernetHistory24HrMonType_Type = PmEthernetMonType
_PmEthernetHistory24HrMonType_Object = MibTableColumn
pmEthernetHistory24HrMonType = _PmEthernetHistory24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1, 1),
    _PmEthernetHistory24HrMonType_Type()
)
pmEthernetHistory24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmEthernetHistory24HrMonType.setStatus("current")
_PmEthernetHistory24HrMonTypeDescr_Type = DisplayString
_PmEthernetHistory24HrMonTypeDescr_Object = MibTableColumn
pmEthernetHistory24HrMonTypeDescr = _PmEthernetHistory24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1, 2),
    _PmEthernetHistory24HrMonTypeDescr_Type()
)
pmEthernetHistory24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory24HrMonTypeDescr.setStatus("current")
_PmEthernetHistory24HrIndexDescr_Type = DisplayString
_PmEthernetHistory24HrIndexDescr_Object = MibTableColumn
pmEthernetHistory24HrIndexDescr = _PmEthernetHistory24HrIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1, 3),
    _PmEthernetHistory24HrIndexDescr_Type()
)
pmEthernetHistory24HrIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory24HrIndexDescr.setStatus("current")
_PmEthernetHistory24HrMonValue_Type = DisplayString
_PmEthernetHistory24HrMonValue_Object = MibTableColumn
pmEthernetHistory24HrMonValue = _PmEthernetHistory24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1, 4),
    _PmEthernetHistory24HrMonValue_Type()
)
pmEthernetHistory24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory24HrMonValue.setStatus("current")
_PmEthernetHistory24HrMonIDF_Type = DisplayString
_PmEthernetHistory24HrMonIDF_Object = MibTableColumn
pmEthernetHistory24HrMonIDF = _PmEthernetHistory24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1, 5),
    _PmEthernetHistory24HrMonIDF_Type()
)
pmEthernetHistory24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory24HrMonIDF.setStatus("current")
_PmEthernetHistory24HrMonSupported_Type = TruthValue
_PmEthernetHistory24HrMonSupported_Object = MibTableColumn
pmEthernetHistory24HrMonSupported = _PmEthernetHistory24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1, 6),
    _PmEthernetHistory24HrMonSupported_Type()
)
pmEthernetHistory24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory24HrMonSupported.setStatus("current")
_PmEthernetHistory24HrAdminState_Type = EnabledDisabledEnum
_PmEthernetHistory24HrAdminState_Object = MibTableColumn
pmEthernetHistory24HrAdminState = _PmEthernetHistory24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1, 7),
    _PmEthernetHistory24HrAdminState_Type()
)
pmEthernetHistory24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory24HrAdminState.setStatus("current")
_PmEthernetHistory24HrMonStartDateTime_Type = DisplayString
_PmEthernetHistory24HrMonStartDateTime_Object = MibTableColumn
pmEthernetHistory24HrMonStartDateTime = _PmEthernetHistory24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 8, 1, 8),
    _PmEthernetHistory24HrMonStartDateTime_Type()
)
pmEthernetHistory24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthernetHistory24HrMonStartDateTime.setStatus("current")
_PmModemCurrent15minStatsTable_Object = MibTable
pmModemCurrent15minStatsTable = _PmModemCurrent15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9)
)
if mibBuilder.loadTexts:
    pmModemCurrent15minStatsTable.setStatus("current")
_PmModemCurrent15minStatsEntry_Object = MibTableRow
pmModemCurrent15minStatsEntry = _PmModemCurrent15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1)
)
pmModemCurrent15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmModem15minMonType"),
)
if mibBuilder.loadTexts:
    pmModemCurrent15minStatsEntry.setStatus("current")
_PmModem15minMonType_Type = PmModemMonType
_PmModem15minMonType_Object = MibTableColumn
pmModem15minMonType = _PmModem15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1, 1),
    _PmModem15minMonType_Type()
)
pmModem15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmModem15minMonType.setStatus("current")
_PmModem15minMonTypeDescr_Type = DisplayString
_PmModem15minMonTypeDescr_Object = MibTableColumn
pmModem15minMonTypeDescr = _PmModem15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1, 2),
    _PmModem15minMonTypeDescr_Type()
)
pmModem15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem15minMonTypeDescr.setStatus("current")
_PmModem15minIfIndexDescr_Type = DisplayString
_PmModem15minIfIndexDescr_Object = MibTableColumn
pmModem15minIfIndexDescr = _PmModem15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1, 3),
    _PmModem15minIfIndexDescr_Type()
)
pmModem15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem15minIfIndexDescr.setStatus("current")
_PmModem15minMonValue_Type = DisplayString
_PmModem15minMonValue_Object = MibTableColumn
pmModem15minMonValue = _PmModem15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1, 4),
    _PmModem15minMonValue_Type()
)
pmModem15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem15minMonValue.setStatus("current")
_PmModem15minMonIDF_Type = DisplayString
_PmModem15minMonIDF_Object = MibTableColumn
pmModem15minMonIDF = _PmModem15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1, 5),
    _PmModem15minMonIDF_Type()
)
pmModem15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem15minMonIDF.setStatus("current")
_PmModem15minMonSupported_Type = TruthValue
_PmModem15minMonSupported_Object = MibTableColumn
pmModem15minMonSupported = _PmModem15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1, 6),
    _PmModem15minMonSupported_Type()
)
pmModem15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem15minMonSupported.setStatus("current")
_PmModem15minAdminState_Type = EnabledDisabledEnum
_PmModem15minAdminState_Object = MibTableColumn
pmModem15minAdminState = _PmModem15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1, 7),
    _PmModem15minAdminState_Type()
)
pmModem15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem15minAdminState.setStatus("current")
_PmModem15minMonStartDateTime_Type = DisplayString
_PmModem15minMonStartDateTime_Object = MibTableColumn
pmModem15minMonStartDateTime = _PmModem15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 9, 1, 8),
    _PmModem15minMonStartDateTime_Type()
)
pmModem15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem15minMonStartDateTime.setStatus("current")
_PmModemCurrent24HrStatsTable_Object = MibTable
pmModemCurrent24HrStatsTable = _PmModemCurrent24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10)
)
if mibBuilder.loadTexts:
    pmModemCurrent24HrStatsTable.setStatus("current")
_PmModemCurrent24HrStatsEntry_Object = MibTableRow
pmModemCurrent24HrStatsEntry = _PmModemCurrent24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1)
)
pmModemCurrent24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmModem24HrMonType"),
)
if mibBuilder.loadTexts:
    pmModemCurrent24HrStatsEntry.setStatus("current")
_PmModem24HrMonType_Type = PmModemMonType
_PmModem24HrMonType_Object = MibTableColumn
pmModem24HrMonType = _PmModem24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1, 1),
    _PmModem24HrMonType_Type()
)
pmModem24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmModem24HrMonType.setStatus("current")
_PmModem24HrMonTypeDescr_Type = DisplayString
_PmModem24HrMonTypeDescr_Object = MibTableColumn
pmModem24HrMonTypeDescr = _PmModem24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1, 2),
    _PmModem24HrMonTypeDescr_Type()
)
pmModem24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem24HrMonTypeDescr.setStatus("current")
_PmModem24HrIfIndexDescr_Type = DisplayString
_PmModem24HrIfIndexDescr_Object = MibTableColumn
pmModem24HrIfIndexDescr = _PmModem24HrIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1, 3),
    _PmModem24HrIfIndexDescr_Type()
)
pmModem24HrIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem24HrIfIndexDescr.setStatus("current")
_PmModem24HrMonValue_Type = DisplayString
_PmModem24HrMonValue_Object = MibTableColumn
pmModem24HrMonValue = _PmModem24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1, 4),
    _PmModem24HrMonValue_Type()
)
pmModem24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem24HrMonValue.setStatus("current")
_PmModem24HrMonIDF_Type = DisplayString
_PmModem24HrMonIDF_Object = MibTableColumn
pmModem24HrMonIDF = _PmModem24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1, 5),
    _PmModem24HrMonIDF_Type()
)
pmModem24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem24HrMonIDF.setStatus("current")
_PmModem24HrMonSupported_Type = TruthValue
_PmModem24HrMonSupported_Object = MibTableColumn
pmModem24HrMonSupported = _PmModem24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1, 6),
    _PmModem24HrMonSupported_Type()
)
pmModem24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem24HrMonSupported.setStatus("current")
_PmModem24HrAdminState_Type = EnabledDisabledEnum
_PmModem24HrAdminState_Object = MibTableColumn
pmModem24HrAdminState = _PmModem24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1, 7),
    _PmModem24HrAdminState_Type()
)
pmModem24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem24HrAdminState.setStatus("current")
_PmModem24HrMonStartDateTime_Type = DisplayString
_PmModem24HrMonStartDateTime_Object = MibTableColumn
pmModem24HrMonStartDateTime = _PmModem24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 10, 1, 8),
    _PmModem24HrMonStartDateTime_Type()
)
pmModem24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModem24HrMonStartDateTime.setStatus("current")
_PmModemUntimedStatsTable_Object = MibTable
pmModemUntimedStatsTable = _PmModemUntimedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11)
)
if mibBuilder.loadTexts:
    pmModemUntimedStatsTable.setStatus("current")
_PmModemUntimedStatsEntry_Object = MibTableRow
pmModemUntimedStatsEntry = _PmModemUntimedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1)
)
pmModemUntimedStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmModemUntimedMonType"),
)
if mibBuilder.loadTexts:
    pmModemUntimedStatsEntry.setStatus("current")
_PmModemUntimedMonType_Type = PmModemMonType
_PmModemUntimedMonType_Object = MibTableColumn
pmModemUntimedMonType = _PmModemUntimedMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1, 1),
    _PmModemUntimedMonType_Type()
)
pmModemUntimedMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmModemUntimedMonType.setStatus("current")
_PmModemUntimedMonTypeDescr_Type = DisplayString
_PmModemUntimedMonTypeDescr_Object = MibTableColumn
pmModemUntimedMonTypeDescr = _PmModemUntimedMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1, 2),
    _PmModemUntimedMonTypeDescr_Type()
)
pmModemUntimedMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemUntimedMonTypeDescr.setStatus("current")
_PmModemUntimedIfIndexDescr_Type = DisplayString
_PmModemUntimedIfIndexDescr_Object = MibTableColumn
pmModemUntimedIfIndexDescr = _PmModemUntimedIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1, 3),
    _PmModemUntimedIfIndexDescr_Type()
)
pmModemUntimedIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemUntimedIfIndexDescr.setStatus("current")
_PmModemUntimedMonValue_Type = DisplayString
_PmModemUntimedMonValue_Object = MibTableColumn
pmModemUntimedMonValue = _PmModemUntimedMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1, 4),
    _PmModemUntimedMonValue_Type()
)
pmModemUntimedMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemUntimedMonValue.setStatus("current")
_PmModemUntimedMonIDF_Type = DisplayString
_PmModemUntimedMonIDF_Object = MibTableColumn
pmModemUntimedMonIDF = _PmModemUntimedMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1, 5),
    _PmModemUntimedMonIDF_Type()
)
pmModemUntimedMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemUntimedMonIDF.setStatus("current")
_PmModemUntimedMonSupported_Type = TruthValue
_PmModemUntimedMonSupported_Object = MibTableColumn
pmModemUntimedMonSupported = _PmModemUntimedMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1, 6),
    _PmModemUntimedMonSupported_Type()
)
pmModemUntimedMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemUntimedMonSupported.setStatus("current")
_PmModemUntimedAdminState_Type = EnabledDisabledEnum
_PmModemUntimedAdminState_Object = MibTableColumn
pmModemUntimedAdminState = _PmModemUntimedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1, 7),
    _PmModemUntimedAdminState_Type()
)
pmModemUntimedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemUntimedAdminState.setStatus("current")
_PmModemUntimedMonStartDateTime_Type = DisplayString
_PmModemUntimedMonStartDateTime_Object = MibTableColumn
pmModemUntimedMonStartDateTime = _PmModemUntimedMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 11, 1, 8),
    _PmModemUntimedMonStartDateTime_Type()
)
pmModemUntimedMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemUntimedMonStartDateTime.setStatus("current")
_PmModemHistory15minStatsTable_Object = MibTable
pmModemHistory15minStatsTable = _PmModemHistory15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12)
)
if mibBuilder.loadTexts:
    pmModemHistory15minStatsTable.setStatus("current")
_PmModemHistory15minStatsEntry_Object = MibTableRow
pmModemHistory15minStatsEntry = _PmModemHistory15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1)
)
pmModemHistory15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minBinIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minMonType"),
)
if mibBuilder.loadTexts:
    pmModemHistory15minStatsEntry.setStatus("current")


class _PmModemHistory15minBinIndex_Type(Integer32):
    """Custom type pmModemHistory15minBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmModemHistory15minBinIndex_Type.__name__ = "Integer32"
_PmModemHistory15minBinIndex_Object = MibTableColumn
pmModemHistory15minBinIndex = _PmModemHistory15minBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 1),
    _PmModemHistory15minBinIndex_Type()
)
pmModemHistory15minBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmModemHistory15minBinIndex.setStatus("current")
_PmModemHistory15minMonType_Type = PmModemMonType
_PmModemHistory15minMonType_Object = MibTableColumn
pmModemHistory15minMonType = _PmModemHistory15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 2),
    _PmModemHistory15minMonType_Type()
)
pmModemHistory15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmModemHistory15minMonType.setStatus("current")
_PmModemHistory15minMonTypeDescr_Type = DisplayString
_PmModemHistory15minMonTypeDescr_Object = MibTableColumn
pmModemHistory15minMonTypeDescr = _PmModemHistory15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 3),
    _PmModemHistory15minMonTypeDescr_Type()
)
pmModemHistory15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory15minMonTypeDescr.setStatus("current")
_PmModemHistory15minIfIndexDescr_Type = DisplayString
_PmModemHistory15minIfIndexDescr_Object = MibTableColumn
pmModemHistory15minIfIndexDescr = _PmModemHistory15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 4),
    _PmModemHistory15minIfIndexDescr_Type()
)
pmModemHistory15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory15minIfIndexDescr.setStatus("current")
_PmModemHistory15minMonValue_Type = DisplayString
_PmModemHistory15minMonValue_Object = MibTableColumn
pmModemHistory15minMonValue = _PmModemHistory15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 5),
    _PmModemHistory15minMonValue_Type()
)
pmModemHistory15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory15minMonValue.setStatus("current")
_PmModemHistory15minMonIDF_Type = DisplayString
_PmModemHistory15minMonIDF_Object = MibTableColumn
pmModemHistory15minMonIDF = _PmModemHistory15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 6),
    _PmModemHistory15minMonIDF_Type()
)
pmModemHistory15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory15minMonIDF.setStatus("current")
_PmModemHistory15minMonSupported_Type = TruthValue
_PmModemHistory15minMonSupported_Object = MibTableColumn
pmModemHistory15minMonSupported = _PmModemHistory15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 7),
    _PmModemHistory15minMonSupported_Type()
)
pmModemHistory15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory15minMonSupported.setStatus("current")
_PmModemHistory15minAdminState_Type = EnabledDisabledEnum
_PmModemHistory15minAdminState_Object = MibTableColumn
pmModemHistory15minAdminState = _PmModemHistory15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 8),
    _PmModemHistory15minAdminState_Type()
)
pmModemHistory15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory15minAdminState.setStatus("current")
_PmModemHistory15minMonStartDateTime_Type = DisplayString
_PmModemHistory15minMonStartDateTime_Object = MibTableColumn
pmModemHistory15minMonStartDateTime = _PmModemHistory15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 12, 1, 9),
    _PmModemHistory15minMonStartDateTime_Type()
)
pmModemHistory15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory15minMonStartDateTime.setStatus("current")
_PmModemHistory24HrStatsTable_Object = MibTable
pmModemHistory24HrStatsTable = _PmModemHistory24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13)
)
if mibBuilder.loadTexts:
    pmModemHistory24HrStatsTable.setStatus("current")
_PmModemHistory24HrStatsEntry_Object = MibTableRow
pmModemHistory24HrStatsEntry = _PmModemHistory24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1)
)
pmModemHistory24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory24HrMonType"),
)
if mibBuilder.loadTexts:
    pmModemHistory24HrStatsEntry.setStatus("current")
_PmModemHistory24HrMonType_Type = PmModemMonType
_PmModemHistory24HrMonType_Object = MibTableColumn
pmModemHistory24HrMonType = _PmModemHistory24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1, 1),
    _PmModemHistory24HrMonType_Type()
)
pmModemHistory24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmModemHistory24HrMonType.setStatus("current")
_PmModemHistory24HrMonTypeDescr_Type = DisplayString
_PmModemHistory24HrMonTypeDescr_Object = MibTableColumn
pmModemHistory24HrMonTypeDescr = _PmModemHistory24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1, 2),
    _PmModemHistory24HrMonTypeDescr_Type()
)
pmModemHistory24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory24HrMonTypeDescr.setStatus("current")
_PmModemHistory24HrIndexDescr_Type = DisplayString
_PmModemHistory24HrIndexDescr_Object = MibTableColumn
pmModemHistory24HrIndexDescr = _PmModemHistory24HrIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1, 3),
    _PmModemHistory24HrIndexDescr_Type()
)
pmModemHistory24HrIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory24HrIndexDescr.setStatus("current")
_PmModemHistory24HrMonValue_Type = DisplayString
_PmModemHistory24HrMonValue_Object = MibTableColumn
pmModemHistory24HrMonValue = _PmModemHistory24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1, 4),
    _PmModemHistory24HrMonValue_Type()
)
pmModemHistory24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory24HrMonValue.setStatus("current")
_PmModemHistory24HrMonIDF_Type = DisplayString
_PmModemHistory24HrMonIDF_Object = MibTableColumn
pmModemHistory24HrMonIDF = _PmModemHistory24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1, 5),
    _PmModemHistory24HrMonIDF_Type()
)
pmModemHistory24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory24HrMonIDF.setStatus("current")
_PmModemHistory24HrMonSupported_Type = TruthValue
_PmModemHistory24HrMonSupported_Object = MibTableColumn
pmModemHistory24HrMonSupported = _PmModemHistory24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1, 6),
    _PmModemHistory24HrMonSupported_Type()
)
pmModemHistory24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory24HrMonSupported.setStatus("current")
_PmModemHistory24HrAdminState_Type = EnabledDisabledEnum
_PmModemHistory24HrAdminState_Object = MibTableColumn
pmModemHistory24HrAdminState = _PmModemHistory24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1, 7),
    _PmModemHistory24HrAdminState_Type()
)
pmModemHistory24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory24HrAdminState.setStatus("current")
_PmModemHistory24HrMonStartDateTime_Type = DisplayString
_PmModemHistory24HrMonStartDateTime_Object = MibTableColumn
pmModemHistory24HrMonStartDateTime = _PmModemHistory24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 13, 1, 8),
    _PmModemHistory24HrMonStartDateTime_Type()
)
pmModemHistory24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmModemHistory24HrMonStartDateTime.setStatus("current")
_PmOtuCurrent15minStatsTable_Object = MibTable
pmOtuCurrent15minStatsTable = _PmOtuCurrent15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14)
)
if mibBuilder.loadTexts:
    pmOtuCurrent15minStatsTable.setStatus("current")
_PmOtuCurrent15minStatsEntry_Object = MibTableRow
pmOtuCurrent15minStatsEntry = _PmOtuCurrent15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1)
)
pmOtuCurrent15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOtu15minMonType"),
)
if mibBuilder.loadTexts:
    pmOtuCurrent15minStatsEntry.setStatus("current")
_PmOtu15minMonType_Type = PmOtuMonType
_PmOtu15minMonType_Object = MibTableColumn
pmOtu15minMonType = _PmOtu15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1, 1),
    _PmOtu15minMonType_Type()
)
pmOtu15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOtu15minMonType.setStatus("current")
_PmOtu15minMonTypeDescr_Type = DisplayString
_PmOtu15minMonTypeDescr_Object = MibTableColumn
pmOtu15minMonTypeDescr = _PmOtu15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1, 2),
    _PmOtu15minMonTypeDescr_Type()
)
pmOtu15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu15minMonTypeDescr.setStatus("current")
_PmOtu15minIfIndexDescr_Type = DisplayString
_PmOtu15minIfIndexDescr_Object = MibTableColumn
pmOtu15minIfIndexDescr = _PmOtu15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1, 3),
    _PmOtu15minIfIndexDescr_Type()
)
pmOtu15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu15minIfIndexDescr.setStatus("current")
_PmOtu15minMonValue_Type = DisplayString
_PmOtu15minMonValue_Object = MibTableColumn
pmOtu15minMonValue = _PmOtu15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1, 4),
    _PmOtu15minMonValue_Type()
)
pmOtu15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu15minMonValue.setStatus("current")
_PmOtu15minMonIDF_Type = DisplayString
_PmOtu15minMonIDF_Object = MibTableColumn
pmOtu15minMonIDF = _PmOtu15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1, 5),
    _PmOtu15minMonIDF_Type()
)
pmOtu15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu15minMonIDF.setStatus("current")
_PmOtu15minMonSupported_Type = TruthValue
_PmOtu15minMonSupported_Object = MibTableColumn
pmOtu15minMonSupported = _PmOtu15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1, 6),
    _PmOtu15minMonSupported_Type()
)
pmOtu15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu15minMonSupported.setStatus("current")
_PmOtu15minAdminState_Type = EnabledDisabledEnum
_PmOtu15minAdminState_Object = MibTableColumn
pmOtu15minAdminState = _PmOtu15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1, 7),
    _PmOtu15minAdminState_Type()
)
pmOtu15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu15minAdminState.setStatus("current")
_PmOtu15minMonStartDateTime_Type = DisplayString
_PmOtu15minMonStartDateTime_Object = MibTableColumn
pmOtu15minMonStartDateTime = _PmOtu15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 14, 1, 8),
    _PmOtu15minMonStartDateTime_Type()
)
pmOtu15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu15minMonStartDateTime.setStatus("current")
_PmOtuCurrent24HrStatsTable_Object = MibTable
pmOtuCurrent24HrStatsTable = _PmOtuCurrent24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15)
)
if mibBuilder.loadTexts:
    pmOtuCurrent24HrStatsTable.setStatus("current")
_PmOtuCurrent24HrStatsEntry_Object = MibTableRow
pmOtuCurrent24HrStatsEntry = _PmOtuCurrent24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1)
)
pmOtuCurrent24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOtu24HrMonType"),
)
if mibBuilder.loadTexts:
    pmOtuCurrent24HrStatsEntry.setStatus("current")
_PmOtu24HrMonType_Type = PmOtuMonType
_PmOtu24HrMonType_Object = MibTableColumn
pmOtu24HrMonType = _PmOtu24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1, 1),
    _PmOtu24HrMonType_Type()
)
pmOtu24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOtu24HrMonType.setStatus("current")
_PmOtu24HrMonTypeDescr_Type = DisplayString
_PmOtu24HrMonTypeDescr_Object = MibTableColumn
pmOtu24HrMonTypeDescr = _PmOtu24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1, 2),
    _PmOtu24HrMonTypeDescr_Type()
)
pmOtu24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu24HrMonTypeDescr.setStatus("current")
_PmOtu24HrIfIndexDescr_Type = DisplayString
_PmOtu24HrIfIndexDescr_Object = MibTableColumn
pmOtu24HrIfIndexDescr = _PmOtu24HrIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1, 3),
    _PmOtu24HrIfIndexDescr_Type()
)
pmOtu24HrIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu24HrIfIndexDescr.setStatus("current")
_PmOtu24HrMonValue_Type = DisplayString
_PmOtu24HrMonValue_Object = MibTableColumn
pmOtu24HrMonValue = _PmOtu24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1, 4),
    _PmOtu24HrMonValue_Type()
)
pmOtu24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu24HrMonValue.setStatus("current")
_PmOtu24HrMonIDF_Type = DisplayString
_PmOtu24HrMonIDF_Object = MibTableColumn
pmOtu24HrMonIDF = _PmOtu24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1, 5),
    _PmOtu24HrMonIDF_Type()
)
pmOtu24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu24HrMonIDF.setStatus("current")
_PmOtu24HrMonSupported_Type = TruthValue
_PmOtu24HrMonSupported_Object = MibTableColumn
pmOtu24HrMonSupported = _PmOtu24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1, 6),
    _PmOtu24HrMonSupported_Type()
)
pmOtu24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu24HrMonSupported.setStatus("current")
_PmOtu24HrAdminState_Type = EnabledDisabledEnum
_PmOtu24HrAdminState_Object = MibTableColumn
pmOtu24HrAdminState = _PmOtu24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1, 7),
    _PmOtu24HrAdminState_Type()
)
pmOtu24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu24HrAdminState.setStatus("current")
_PmOtu24HrMonStartDateTime_Type = DisplayString
_PmOtu24HrMonStartDateTime_Object = MibTableColumn
pmOtu24HrMonStartDateTime = _PmOtu24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 15, 1, 8),
    _PmOtu24HrMonStartDateTime_Type()
)
pmOtu24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtu24HrMonStartDateTime.setStatus("current")
_PmOtuUntimedStatsTable_Object = MibTable
pmOtuUntimedStatsTable = _PmOtuUntimedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16)
)
if mibBuilder.loadTexts:
    pmOtuUntimedStatsTable.setStatus("current")
_PmOtuUntimedStatsEntry_Object = MibTableRow
pmOtuUntimedStatsEntry = _PmOtuUntimedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1)
)
pmOtuUntimedStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOtuUntimedMonType"),
)
if mibBuilder.loadTexts:
    pmOtuUntimedStatsEntry.setStatus("current")
_PmOtuUntimedMonType_Type = PmOtuMonType
_PmOtuUntimedMonType_Object = MibTableColumn
pmOtuUntimedMonType = _PmOtuUntimedMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1, 1),
    _PmOtuUntimedMonType_Type()
)
pmOtuUntimedMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOtuUntimedMonType.setStatus("current")
_PmOtuUntimedMonTypeDescr_Type = DisplayString
_PmOtuUntimedMonTypeDescr_Object = MibTableColumn
pmOtuUntimedMonTypeDescr = _PmOtuUntimedMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1, 2),
    _PmOtuUntimedMonTypeDescr_Type()
)
pmOtuUntimedMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuUntimedMonTypeDescr.setStatus("current")
_PmOtuUntimedIfIndexDescr_Type = DisplayString
_PmOtuUntimedIfIndexDescr_Object = MibTableColumn
pmOtuUntimedIfIndexDescr = _PmOtuUntimedIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1, 3),
    _PmOtuUntimedIfIndexDescr_Type()
)
pmOtuUntimedIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuUntimedIfIndexDescr.setStatus("current")
_PmOtuUntimedMonValue_Type = DisplayString
_PmOtuUntimedMonValue_Object = MibTableColumn
pmOtuUntimedMonValue = _PmOtuUntimedMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1, 4),
    _PmOtuUntimedMonValue_Type()
)
pmOtuUntimedMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuUntimedMonValue.setStatus("current")
_PmOtuUntimedMonIDF_Type = DisplayString
_PmOtuUntimedMonIDF_Object = MibTableColumn
pmOtuUntimedMonIDF = _PmOtuUntimedMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1, 5),
    _PmOtuUntimedMonIDF_Type()
)
pmOtuUntimedMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuUntimedMonIDF.setStatus("current")
_PmOtuUntimedMonSupported_Type = TruthValue
_PmOtuUntimedMonSupported_Object = MibTableColumn
pmOtuUntimedMonSupported = _PmOtuUntimedMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1, 6),
    _PmOtuUntimedMonSupported_Type()
)
pmOtuUntimedMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuUntimedMonSupported.setStatus("current")
_PmOtuUntimedAdminState_Type = EnabledDisabledEnum
_PmOtuUntimedAdminState_Object = MibTableColumn
pmOtuUntimedAdminState = _PmOtuUntimedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1, 7),
    _PmOtuUntimedAdminState_Type()
)
pmOtuUntimedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuUntimedAdminState.setStatus("current")
_PmOtuUntimedMonStartDateTime_Type = DisplayString
_PmOtuUntimedMonStartDateTime_Object = MibTableColumn
pmOtuUntimedMonStartDateTime = _PmOtuUntimedMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 16, 1, 8),
    _PmOtuUntimedMonStartDateTime_Type()
)
pmOtuUntimedMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuUntimedMonStartDateTime.setStatus("current")
_PmOtuHistory15minStatsTable_Object = MibTable
pmOtuHistory15minStatsTable = _PmOtuHistory15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17)
)
if mibBuilder.loadTexts:
    pmOtuHistory15minStatsTable.setStatus("current")
_PmOtuHistory15minStatsEntry_Object = MibTableRow
pmOtuHistory15minStatsEntry = _PmOtuHistory15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1)
)
pmOtuHistory15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minBinIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minMonType"),
)
if mibBuilder.loadTexts:
    pmOtuHistory15minStatsEntry.setStatus("current")


class _PmOtuHistory15minBinIndex_Type(Integer32):
    """Custom type pmOtuHistory15minBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmOtuHistory15minBinIndex_Type.__name__ = "Integer32"
_PmOtuHistory15minBinIndex_Object = MibTableColumn
pmOtuHistory15minBinIndex = _PmOtuHistory15minBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 1),
    _PmOtuHistory15minBinIndex_Type()
)
pmOtuHistory15minBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOtuHistory15minBinIndex.setStatus("current")
_PmOtuHistory15minMonType_Type = PmOtuMonType
_PmOtuHistory15minMonType_Object = MibTableColumn
pmOtuHistory15minMonType = _PmOtuHistory15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 2),
    _PmOtuHistory15minMonType_Type()
)
pmOtuHistory15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOtuHistory15minMonType.setStatus("current")
_PmOtuHistory15minMonTypeDescr_Type = DisplayString
_PmOtuHistory15minMonTypeDescr_Object = MibTableColumn
pmOtuHistory15minMonTypeDescr = _PmOtuHistory15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 3),
    _PmOtuHistory15minMonTypeDescr_Type()
)
pmOtuHistory15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory15minMonTypeDescr.setStatus("current")
_PmOtuHistory15minIndexDescr_Type = DisplayString
_PmOtuHistory15minIndexDescr_Object = MibTableColumn
pmOtuHistory15minIndexDescr = _PmOtuHistory15minIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 4),
    _PmOtuHistory15minIndexDescr_Type()
)
pmOtuHistory15minIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory15minIndexDescr.setStatus("current")
_PmOtuHistory15minMonValue_Type = DisplayString
_PmOtuHistory15minMonValue_Object = MibTableColumn
pmOtuHistory15minMonValue = _PmOtuHistory15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 5),
    _PmOtuHistory15minMonValue_Type()
)
pmOtuHistory15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory15minMonValue.setStatus("current")
_PmOtuHistory15minMonIDF_Type = DisplayString
_PmOtuHistory15minMonIDF_Object = MibTableColumn
pmOtuHistory15minMonIDF = _PmOtuHistory15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 6),
    _PmOtuHistory15minMonIDF_Type()
)
pmOtuHistory15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory15minMonIDF.setStatus("current")
_PmOtuHistory15minMonSupported_Type = TruthValue
_PmOtuHistory15minMonSupported_Object = MibTableColumn
pmOtuHistory15minMonSupported = _PmOtuHistory15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 7),
    _PmOtuHistory15minMonSupported_Type()
)
pmOtuHistory15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory15minMonSupported.setStatus("current")
_PmOtuHistory15minAdminState_Type = EnabledDisabledEnum
_PmOtuHistory15minAdminState_Object = MibTableColumn
pmOtuHistory15minAdminState = _PmOtuHistory15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 8),
    _PmOtuHistory15minAdminState_Type()
)
pmOtuHistory15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory15minAdminState.setStatus("current")
_PmOtuHistory15minMonStartDateTime_Type = DisplayString
_PmOtuHistory15minMonStartDateTime_Object = MibTableColumn
pmOtuHistory15minMonStartDateTime = _PmOtuHistory15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 17, 1, 9),
    _PmOtuHistory15minMonStartDateTime_Type()
)
pmOtuHistory15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory15minMonStartDateTime.setStatus("current")
_PmOtuHistory24HrStatsTable_Object = MibTable
pmOtuHistory24HrStatsTable = _PmOtuHistory24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18)
)
if mibBuilder.loadTexts:
    pmOtuHistory24HrStatsTable.setStatus("current")
_PmOtuHistory24HrStatsEntry_Object = MibTableRow
pmOtuHistory24HrStatsEntry = _PmOtuHistory24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1)
)
pmOtuHistory24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory24HrMonType"),
)
if mibBuilder.loadTexts:
    pmOtuHistory24HrStatsEntry.setStatus("current")
_PmOtuHistory24HrMonType_Type = PmOtuMonType
_PmOtuHistory24HrMonType_Object = MibTableColumn
pmOtuHistory24HrMonType = _PmOtuHistory24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1, 1),
    _PmOtuHistory24HrMonType_Type()
)
pmOtuHistory24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOtuHistory24HrMonType.setStatus("current")
_PmOtuHistory24HrMonTypeDescr_Type = DisplayString
_PmOtuHistory24HrMonTypeDescr_Object = MibTableColumn
pmOtuHistory24HrMonTypeDescr = _PmOtuHistory24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1, 2),
    _PmOtuHistory24HrMonTypeDescr_Type()
)
pmOtuHistory24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory24HrMonTypeDescr.setStatus("current")
_PmOtuHistory24HrIndexDescr_Type = DisplayString
_PmOtuHistory24HrIndexDescr_Object = MibTableColumn
pmOtuHistory24HrIndexDescr = _PmOtuHistory24HrIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1, 3),
    _PmOtuHistory24HrIndexDescr_Type()
)
pmOtuHistory24HrIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory24HrIndexDescr.setStatus("current")
_PmOtuHistory24HrMonValue_Type = DisplayString
_PmOtuHistory24HrMonValue_Object = MibTableColumn
pmOtuHistory24HrMonValue = _PmOtuHistory24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1, 4),
    _PmOtuHistory24HrMonValue_Type()
)
pmOtuHistory24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory24HrMonValue.setStatus("current")
_PmOtuHistory24HrMonIDF_Type = DisplayString
_PmOtuHistory24HrMonIDF_Object = MibTableColumn
pmOtuHistory24HrMonIDF = _PmOtuHistory24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1, 5),
    _PmOtuHistory24HrMonIDF_Type()
)
pmOtuHistory24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory24HrMonIDF.setStatus("current")
_PmOtuHistory24HrMonSupported_Type = TruthValue
_PmOtuHistory24HrMonSupported_Object = MibTableColumn
pmOtuHistory24HrMonSupported = _PmOtuHistory24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1, 6),
    _PmOtuHistory24HrMonSupported_Type()
)
pmOtuHistory24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory24HrMonSupported.setStatus("current")
_PmOtuHistory24HrAdminState_Type = EnabledDisabledEnum
_PmOtuHistory24HrAdminState_Object = MibTableColumn
pmOtuHistory24HrAdminState = _PmOtuHistory24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1, 7),
    _PmOtuHistory24HrAdminState_Type()
)
pmOtuHistory24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory24HrAdminState.setStatus("current")
_PmOtuHistory24HrMonStartDateTime_Type = DisplayString
_PmOtuHistory24HrMonStartDateTime_Object = MibTableColumn
pmOtuHistory24HrMonStartDateTime = _PmOtuHistory24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 18, 1, 8),
    _PmOtuHistory24HrMonStartDateTime_Type()
)
pmOtuHistory24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOtuHistory24HrMonStartDateTime.setStatus("current")
_PmOduCurrent15minStatsTable_Object = MibTable
pmOduCurrent15minStatsTable = _PmOduCurrent15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19)
)
if mibBuilder.loadTexts:
    pmOduCurrent15minStatsTable.setStatus("current")
_PmOduCurrent15minStatsEntry_Object = MibTableRow
pmOduCurrent15minStatsEntry = _PmOduCurrent15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1)
)
pmOduCurrent15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOdu15minMonType"),
)
if mibBuilder.loadTexts:
    pmOduCurrent15minStatsEntry.setStatus("current")
_PmOdu15minMonType_Type = PmOduMonType
_PmOdu15minMonType_Object = MibTableColumn
pmOdu15minMonType = _PmOdu15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1, 1),
    _PmOdu15minMonType_Type()
)
pmOdu15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOdu15minMonType.setStatus("current")
_PmOdu15minMonTypeDescr_Type = DisplayString
_PmOdu15minMonTypeDescr_Object = MibTableColumn
pmOdu15minMonTypeDescr = _PmOdu15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1, 2),
    _PmOdu15minMonTypeDescr_Type()
)
pmOdu15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu15minMonTypeDescr.setStatus("current")
_PmOdu15minIfIndexDescr_Type = DisplayString
_PmOdu15minIfIndexDescr_Object = MibTableColumn
pmOdu15minIfIndexDescr = _PmOdu15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1, 3),
    _PmOdu15minIfIndexDescr_Type()
)
pmOdu15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu15minIfIndexDescr.setStatus("current")
_PmOdu15minMonValue_Type = DisplayString
_PmOdu15minMonValue_Object = MibTableColumn
pmOdu15minMonValue = _PmOdu15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1, 4),
    _PmOdu15minMonValue_Type()
)
pmOdu15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu15minMonValue.setStatus("current")
_PmOdu15minMonIDF_Type = DisplayString
_PmOdu15minMonIDF_Object = MibTableColumn
pmOdu15minMonIDF = _PmOdu15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1, 5),
    _PmOdu15minMonIDF_Type()
)
pmOdu15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu15minMonIDF.setStatus("current")
_PmOdu15minMonSupported_Type = TruthValue
_PmOdu15minMonSupported_Object = MibTableColumn
pmOdu15minMonSupported = _PmOdu15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1, 6),
    _PmOdu15minMonSupported_Type()
)
pmOdu15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu15minMonSupported.setStatus("current")
_PmOdu15minAdminState_Type = EnabledDisabledEnum
_PmOdu15minAdminState_Object = MibTableColumn
pmOdu15minAdminState = _PmOdu15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1, 7),
    _PmOdu15minAdminState_Type()
)
pmOdu15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu15minAdminState.setStatus("current")
_PmOdu15minMonStartDateTime_Type = DisplayString
_PmOdu15minMonStartDateTime_Object = MibTableColumn
pmOdu15minMonStartDateTime = _PmOdu15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 19, 1, 8),
    _PmOdu15minMonStartDateTime_Type()
)
pmOdu15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu15minMonStartDateTime.setStatus("current")
_PmOduCurrent24HrStatsTable_Object = MibTable
pmOduCurrent24HrStatsTable = _PmOduCurrent24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20)
)
if mibBuilder.loadTexts:
    pmOduCurrent24HrStatsTable.setStatus("current")
_PmOduCurrent24HrStatsEntry_Object = MibTableRow
pmOduCurrent24HrStatsEntry = _PmOduCurrent24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1)
)
pmOduCurrent24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOdu24HrMonType"),
)
if mibBuilder.loadTexts:
    pmOduCurrent24HrStatsEntry.setStatus("current")
_PmOdu24HrMonType_Type = PmOduMonType
_PmOdu24HrMonType_Object = MibTableColumn
pmOdu24HrMonType = _PmOdu24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1, 1),
    _PmOdu24HrMonType_Type()
)
pmOdu24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOdu24HrMonType.setStatus("current")
_PmOdu24HrMonTypeDescr_Type = DisplayString
_PmOdu24HrMonTypeDescr_Object = MibTableColumn
pmOdu24HrMonTypeDescr = _PmOdu24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1, 2),
    _PmOdu24HrMonTypeDescr_Type()
)
pmOdu24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu24HrMonTypeDescr.setStatus("current")
_PmOdu24HrIfIndexDescr_Type = DisplayString
_PmOdu24HrIfIndexDescr_Object = MibTableColumn
pmOdu24HrIfIndexDescr = _PmOdu24HrIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1, 3),
    _PmOdu24HrIfIndexDescr_Type()
)
pmOdu24HrIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu24HrIfIndexDescr.setStatus("current")
_PmOdu24HrMonValue_Type = DisplayString
_PmOdu24HrMonValue_Object = MibTableColumn
pmOdu24HrMonValue = _PmOdu24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1, 4),
    _PmOdu24HrMonValue_Type()
)
pmOdu24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu24HrMonValue.setStatus("current")
_PmOdu24HrMonIDF_Type = DisplayString
_PmOdu24HrMonIDF_Object = MibTableColumn
pmOdu24HrMonIDF = _PmOdu24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1, 5),
    _PmOdu24HrMonIDF_Type()
)
pmOdu24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu24HrMonIDF.setStatus("current")
_PmOdu24HrMonSupported_Type = TruthValue
_PmOdu24HrMonSupported_Object = MibTableColumn
pmOdu24HrMonSupported = _PmOdu24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1, 6),
    _PmOdu24HrMonSupported_Type()
)
pmOdu24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu24HrMonSupported.setStatus("current")
_PmOdu24HrAdminState_Type = EnabledDisabledEnum
_PmOdu24HrAdminState_Object = MibTableColumn
pmOdu24HrAdminState = _PmOdu24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1, 7),
    _PmOdu24HrAdminState_Type()
)
pmOdu24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu24HrAdminState.setStatus("current")
_PmOdu24HrMonStartDateTime_Type = DisplayString
_PmOdu24HrMonStartDateTime_Object = MibTableColumn
pmOdu24HrMonStartDateTime = _PmOdu24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 20, 1, 8),
    _PmOdu24HrMonStartDateTime_Type()
)
pmOdu24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOdu24HrMonStartDateTime.setStatus("current")
_PmOduUntimedStatsTable_Object = MibTable
pmOduUntimedStatsTable = _PmOduUntimedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21)
)
if mibBuilder.loadTexts:
    pmOduUntimedStatsTable.setStatus("current")
_PmOduUntimedStatsEntry_Object = MibTableRow
pmOduUntimedStatsEntry = _PmOduUntimedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1)
)
pmOduUntimedStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOduUntimedMonType"),
)
if mibBuilder.loadTexts:
    pmOduUntimedStatsEntry.setStatus("current")
_PmOduUntimedMonType_Type = PmOduMonType
_PmOduUntimedMonType_Object = MibTableColumn
pmOduUntimedMonType = _PmOduUntimedMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1, 1),
    _PmOduUntimedMonType_Type()
)
pmOduUntimedMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOduUntimedMonType.setStatus("current")
_PmOduUntimedMonTypeDescr_Type = DisplayString
_PmOduUntimedMonTypeDescr_Object = MibTableColumn
pmOduUntimedMonTypeDescr = _PmOduUntimedMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1, 2),
    _PmOduUntimedMonTypeDescr_Type()
)
pmOduUntimedMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduUntimedMonTypeDescr.setStatus("current")
_PmOduUntimedIfIndexDescr_Type = DisplayString
_PmOduUntimedIfIndexDescr_Object = MibTableColumn
pmOduUntimedIfIndexDescr = _PmOduUntimedIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1, 3),
    _PmOduUntimedIfIndexDescr_Type()
)
pmOduUntimedIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduUntimedIfIndexDescr.setStatus("current")
_PmOduUntimedMonValue_Type = DisplayString
_PmOduUntimedMonValue_Object = MibTableColumn
pmOduUntimedMonValue = _PmOduUntimedMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1, 4),
    _PmOduUntimedMonValue_Type()
)
pmOduUntimedMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduUntimedMonValue.setStatus("current")
_PmOduUntimedMonIDF_Type = DisplayString
_PmOduUntimedMonIDF_Object = MibTableColumn
pmOduUntimedMonIDF = _PmOduUntimedMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1, 5),
    _PmOduUntimedMonIDF_Type()
)
pmOduUntimedMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduUntimedMonIDF.setStatus("current")
_PmOduUntimedMonSupported_Type = TruthValue
_PmOduUntimedMonSupported_Object = MibTableColumn
pmOduUntimedMonSupported = _PmOduUntimedMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1, 6),
    _PmOduUntimedMonSupported_Type()
)
pmOduUntimedMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduUntimedMonSupported.setStatus("current")
_PmOduUntimedAdminState_Type = EnabledDisabledEnum
_PmOduUntimedAdminState_Object = MibTableColumn
pmOduUntimedAdminState = _PmOduUntimedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1, 7),
    _PmOduUntimedAdminState_Type()
)
pmOduUntimedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduUntimedAdminState.setStatus("current")
_PmOduUntimedMonStartDateTime_Type = DisplayString
_PmOduUntimedMonStartDateTime_Object = MibTableColumn
pmOduUntimedMonStartDateTime = _PmOduUntimedMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 21, 1, 8),
    _PmOduUntimedMonStartDateTime_Type()
)
pmOduUntimedMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduUntimedMonStartDateTime.setStatus("current")
_PmOduHistory15minStatsTable_Object = MibTable
pmOduHistory15minStatsTable = _PmOduHistory15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22)
)
if mibBuilder.loadTexts:
    pmOduHistory15minStatsTable.setStatus("current")
_PmOduHistory15minStatsEntry_Object = MibTableRow
pmOduHistory15minStatsEntry = _PmOduHistory15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1)
)
pmOduHistory15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minBinIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minMonType"),
)
if mibBuilder.loadTexts:
    pmOduHistory15minStatsEntry.setStatus("current")


class _PmOduHistory15minBinIndex_Type(Integer32):
    """Custom type pmOduHistory15minBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmOduHistory15minBinIndex_Type.__name__ = "Integer32"
_PmOduHistory15minBinIndex_Object = MibTableColumn
pmOduHistory15minBinIndex = _PmOduHistory15minBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 1),
    _PmOduHistory15minBinIndex_Type()
)
pmOduHistory15minBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOduHistory15minBinIndex.setStatus("current")
_PmOduHistory15minMonType_Type = PmOduMonType
_PmOduHistory15minMonType_Object = MibTableColumn
pmOduHistory15minMonType = _PmOduHistory15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 2),
    _PmOduHistory15minMonType_Type()
)
pmOduHistory15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOduHistory15minMonType.setStatus("current")
_PmOduHistory15minMonTypeDescr_Type = DisplayString
_PmOduHistory15minMonTypeDescr_Object = MibTableColumn
pmOduHistory15minMonTypeDescr = _PmOduHistory15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 3),
    _PmOduHistory15minMonTypeDescr_Type()
)
pmOduHistory15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory15minMonTypeDescr.setStatus("current")
_PmOduHistory15minIndexDescr_Type = DisplayString
_PmOduHistory15minIndexDescr_Object = MibTableColumn
pmOduHistory15minIndexDescr = _PmOduHistory15minIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 4),
    _PmOduHistory15minIndexDescr_Type()
)
pmOduHistory15minIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory15minIndexDescr.setStatus("current")
_PmOduHistory15minMonValue_Type = DisplayString
_PmOduHistory15minMonValue_Object = MibTableColumn
pmOduHistory15minMonValue = _PmOduHistory15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 5),
    _PmOduHistory15minMonValue_Type()
)
pmOduHistory15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory15minMonValue.setStatus("current")
_PmOduHistory15minMonIDF_Type = DisplayString
_PmOduHistory15minMonIDF_Object = MibTableColumn
pmOduHistory15minMonIDF = _PmOduHistory15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 6),
    _PmOduHistory15minMonIDF_Type()
)
pmOduHistory15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory15minMonIDF.setStatus("current")
_PmOduHistory15minMonSupported_Type = TruthValue
_PmOduHistory15minMonSupported_Object = MibTableColumn
pmOduHistory15minMonSupported = _PmOduHistory15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 7),
    _PmOduHistory15minMonSupported_Type()
)
pmOduHistory15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory15minMonSupported.setStatus("current")
_PmOduHistory15minAdminState_Type = EnabledDisabledEnum
_PmOduHistory15minAdminState_Object = MibTableColumn
pmOduHistory15minAdminState = _PmOduHistory15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 8),
    _PmOduHistory15minAdminState_Type()
)
pmOduHistory15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory15minAdminState.setStatus("current")
_PmOduHistory15minMonStartDateTime_Type = DisplayString
_PmOduHistory15minMonStartDateTime_Object = MibTableColumn
pmOduHistory15minMonStartDateTime = _PmOduHistory15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 22, 1, 9),
    _PmOduHistory15minMonStartDateTime_Type()
)
pmOduHistory15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory15minMonStartDateTime.setStatus("current")
_PmOduHistory24HrStatsTable_Object = MibTable
pmOduHistory24HrStatsTable = _PmOduHistory24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23)
)
if mibBuilder.loadTexts:
    pmOduHistory24HrStatsTable.setStatus("current")
_PmOduHistory24HrStatsEntry_Object = MibTableRow
pmOduHistory24HrStatsEntry = _PmOduHistory24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1)
)
pmOduHistory24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory24HrMonType"),
)
if mibBuilder.loadTexts:
    pmOduHistory24HrStatsEntry.setStatus("current")
_PmOduHistory24HrMonType_Type = PmOduMonType
_PmOduHistory24HrMonType_Object = MibTableColumn
pmOduHistory24HrMonType = _PmOduHistory24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1, 1),
    _PmOduHistory24HrMonType_Type()
)
pmOduHistory24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOduHistory24HrMonType.setStatus("current")
_PmOduHistory24HrMonTypeDescr_Type = DisplayString
_PmOduHistory24HrMonTypeDescr_Object = MibTableColumn
pmOduHistory24HrMonTypeDescr = _PmOduHistory24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1, 2),
    _PmOduHistory24HrMonTypeDescr_Type()
)
pmOduHistory24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory24HrMonTypeDescr.setStatus("current")
_PmOduHistory24HrIndexDescr_Type = DisplayString
_PmOduHistory24HrIndexDescr_Object = MibTableColumn
pmOduHistory24HrIndexDescr = _PmOduHistory24HrIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1, 3),
    _PmOduHistory24HrIndexDescr_Type()
)
pmOduHistory24HrIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory24HrIndexDescr.setStatus("current")
_PmOduHistory24HrMonValue_Type = DisplayString
_PmOduHistory24HrMonValue_Object = MibTableColumn
pmOduHistory24HrMonValue = _PmOduHistory24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1, 4),
    _PmOduHistory24HrMonValue_Type()
)
pmOduHistory24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory24HrMonValue.setStatus("current")
_PmOduHistory24HrMonIDF_Type = DisplayString
_PmOduHistory24HrMonIDF_Object = MibTableColumn
pmOduHistory24HrMonIDF = _PmOduHistory24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1, 5),
    _PmOduHistory24HrMonIDF_Type()
)
pmOduHistory24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory24HrMonIDF.setStatus("current")
_PmOduHistory24HrMonSupported_Type = TruthValue
_PmOduHistory24HrMonSupported_Object = MibTableColumn
pmOduHistory24HrMonSupported = _PmOduHistory24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1, 6),
    _PmOduHistory24HrMonSupported_Type()
)
pmOduHistory24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory24HrMonSupported.setStatus("current")
_PmOduHistory24HrAdminState_Type = EnabledDisabledEnum
_PmOduHistory24HrAdminState_Object = MibTableColumn
pmOduHistory24HrAdminState = _PmOduHistory24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1, 7),
    _PmOduHistory24HrAdminState_Type()
)
pmOduHistory24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory24HrAdminState.setStatus("current")
_PmOduHistory24HrMonStartDateTime_Type = DisplayString
_PmOduHistory24HrMonStartDateTime_Object = MibTableColumn
pmOduHistory24HrMonStartDateTime = _PmOduHistory24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 23, 1, 8),
    _PmOduHistory24HrMonStartDateTime_Type()
)
pmOduHistory24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOduHistory24HrMonStartDateTime.setStatus("current")
_PmOpticalPowerCurrent15minStatsTable_Object = MibTable
pmOpticalPowerCurrent15minStatsTable = _PmOpticalPowerCurrent15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24)
)
if mibBuilder.loadTexts:
    pmOpticalPowerCurrent15minStatsTable.setStatus("current")
_PmOpticalPowerCurrent15minStatsEntry_Object = MibTableRow
pmOpticalPowerCurrent15minStatsEntry = _PmOpticalPowerCurrent15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1)
)
pmOpticalPowerCurrent15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minLaneIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minMonType"),
)
if mibBuilder.loadTexts:
    pmOpticalPowerCurrent15minStatsEntry.setStatus("current")


class _PmOpticalPower15minLaneIndex_Type(Integer32):
    """Custom type pmOpticalPower15minLaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmOpticalPower15minLaneIndex_Type.__name__ = "Integer32"
_PmOpticalPower15minLaneIndex_Object = MibTableColumn
pmOpticalPower15minLaneIndex = _PmOpticalPower15minLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 1),
    _PmOpticalPower15minLaneIndex_Type()
)
pmOpticalPower15minLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPower15minLaneIndex.setStatus("current")
_PmOpticalPower15minMonType_Type = PmOpticalPowerMonType
_PmOpticalPower15minMonType_Object = MibTableColumn
pmOpticalPower15minMonType = _PmOpticalPower15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 2),
    _PmOpticalPower15minMonType_Type()
)
pmOpticalPower15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPower15minMonType.setStatus("current")
_PmOpticalPower15minMonTypeDescr_Type = DisplayString
_PmOpticalPower15minMonTypeDescr_Object = MibTableColumn
pmOpticalPower15minMonTypeDescr = _PmOpticalPower15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 3),
    _PmOpticalPower15minMonTypeDescr_Type()
)
pmOpticalPower15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower15minMonTypeDescr.setStatus("current")
_PmOpticalPower15minIfIndexDescr_Type = DisplayString
_PmOpticalPower15minIfIndexDescr_Object = MibTableColumn
pmOpticalPower15minIfIndexDescr = _PmOpticalPower15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 4),
    _PmOpticalPower15minIfIndexDescr_Type()
)
pmOpticalPower15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower15minIfIndexDescr.setStatus("current")
_PmOpticalPower15minMonValue_Type = DisplayString
_PmOpticalPower15minMonValue_Object = MibTableColumn
pmOpticalPower15minMonValue = _PmOpticalPower15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 5),
    _PmOpticalPower15minMonValue_Type()
)
pmOpticalPower15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower15minMonValue.setStatus("current")
_PmOpticalPower15minMonIDF_Type = DisplayString
_PmOpticalPower15minMonIDF_Object = MibTableColumn
pmOpticalPower15minMonIDF = _PmOpticalPower15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 6),
    _PmOpticalPower15minMonIDF_Type()
)
pmOpticalPower15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower15minMonIDF.setStatus("current")
_PmOpticalPower15minMonSupported_Type = TruthValue
_PmOpticalPower15minMonSupported_Object = MibTableColumn
pmOpticalPower15minMonSupported = _PmOpticalPower15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 7),
    _PmOpticalPower15minMonSupported_Type()
)
pmOpticalPower15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower15minMonSupported.setStatus("current")
_PmOpticalPower15minAdminState_Type = EnabledDisabledEnum
_PmOpticalPower15minAdminState_Object = MibTableColumn
pmOpticalPower15minAdminState = _PmOpticalPower15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 8),
    _PmOpticalPower15minAdminState_Type()
)
pmOpticalPower15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower15minAdminState.setStatus("current")
_PmOpticalPower15minMonStartDateTime_Type = DisplayString
_PmOpticalPower15minMonStartDateTime_Object = MibTableColumn
pmOpticalPower15minMonStartDateTime = _PmOpticalPower15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 24, 1, 9),
    _PmOpticalPower15minMonStartDateTime_Type()
)
pmOpticalPower15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower15minMonStartDateTime.setStatus("current")
_PmOpticalPowerCurrent24HrStatsTable_Object = MibTable
pmOpticalPowerCurrent24HrStatsTable = _PmOpticalPowerCurrent24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25)
)
if mibBuilder.loadTexts:
    pmOpticalPowerCurrent24HrStatsTable.setStatus("current")
_PmOpticalPowerCurrent24HrStatsEntry_Object = MibTableRow
pmOpticalPowerCurrent24HrStatsEntry = _PmOpticalPowerCurrent24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1)
)
pmOpticalPowerCurrent24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrLaneIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrMonType"),
)
if mibBuilder.loadTexts:
    pmOpticalPowerCurrent24HrStatsEntry.setStatus("current")


class _PmOpticalPower24HrLaneIndex_Type(Integer32):
    """Custom type pmOpticalPower24HrLaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmOpticalPower24HrLaneIndex_Type.__name__ = "Integer32"
_PmOpticalPower24HrLaneIndex_Object = MibTableColumn
pmOpticalPower24HrLaneIndex = _PmOpticalPower24HrLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 1),
    _PmOpticalPower24HrLaneIndex_Type()
)
pmOpticalPower24HrLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPower24HrLaneIndex.setStatus("current")
_PmOpticalPower24HrMonType_Type = PmOpticalPowerMonType
_PmOpticalPower24HrMonType_Object = MibTableColumn
pmOpticalPower24HrMonType = _PmOpticalPower24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 2),
    _PmOpticalPower24HrMonType_Type()
)
pmOpticalPower24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPower24HrMonType.setStatus("current")
_PmOpticalPower24HrMonTypeDescr_Type = DisplayString
_PmOpticalPower24HrMonTypeDescr_Object = MibTableColumn
pmOpticalPower24HrMonTypeDescr = _PmOpticalPower24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 3),
    _PmOpticalPower24HrMonTypeDescr_Type()
)
pmOpticalPower24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower24HrMonTypeDescr.setStatus("current")
_PmOpticalPower24HrIfIndexDescr_Type = DisplayString
_PmOpticalPower24HrIfIndexDescr_Object = MibTableColumn
pmOpticalPower24HrIfIndexDescr = _PmOpticalPower24HrIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 4),
    _PmOpticalPower24HrIfIndexDescr_Type()
)
pmOpticalPower24HrIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower24HrIfIndexDescr.setStatus("current")
_PmOpticalPower24HrMonValue_Type = DisplayString
_PmOpticalPower24HrMonValue_Object = MibTableColumn
pmOpticalPower24HrMonValue = _PmOpticalPower24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 5),
    _PmOpticalPower24HrMonValue_Type()
)
pmOpticalPower24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower24HrMonValue.setStatus("current")
_PmOpticalPower24HrMonIDF_Type = DisplayString
_PmOpticalPower24HrMonIDF_Object = MibTableColumn
pmOpticalPower24HrMonIDF = _PmOpticalPower24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 6),
    _PmOpticalPower24HrMonIDF_Type()
)
pmOpticalPower24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower24HrMonIDF.setStatus("current")
_PmOpticalPower24HrMonSupported_Type = TruthValue
_PmOpticalPower24HrMonSupported_Object = MibTableColumn
pmOpticalPower24HrMonSupported = _PmOpticalPower24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 7),
    _PmOpticalPower24HrMonSupported_Type()
)
pmOpticalPower24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower24HrMonSupported.setStatus("current")
_PmOpticalPower24HrAdminState_Type = EnabledDisabledEnum
_PmOpticalPower24HrAdminState_Object = MibTableColumn
pmOpticalPower24HrAdminState = _PmOpticalPower24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 8),
    _PmOpticalPower24HrAdminState_Type()
)
pmOpticalPower24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower24HrAdminState.setStatus("current")
_PmOpticalPower24HrMonStartDateTime_Type = DisplayString
_PmOpticalPower24HrMonStartDateTime_Object = MibTableColumn
pmOpticalPower24HrMonStartDateTime = _PmOpticalPower24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 25, 1, 9),
    _PmOpticalPower24HrMonStartDateTime_Type()
)
pmOpticalPower24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPower24HrMonStartDateTime.setStatus("current")
_PmOpticalPowerUntimedStatsTable_Object = MibTable
pmOpticalPowerUntimedStatsTable = _PmOpticalPowerUntimedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26)
)
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedStatsTable.setStatus("current")
_PmOpticalPowerUntimedStatsEntry_Object = MibTableRow
pmOpticalPowerUntimedStatsEntry = _PmOpticalPowerUntimedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1)
)
pmOpticalPowerUntimedStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedLaneIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedMonType"),
)
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedStatsEntry.setStatus("current")


class _PmOpticalPowerUntimedLaneIndex_Type(Integer32):
    """Custom type pmOpticalPowerUntimedLaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmOpticalPowerUntimedLaneIndex_Type.__name__ = "Integer32"
_PmOpticalPowerUntimedLaneIndex_Object = MibTableColumn
pmOpticalPowerUntimedLaneIndex = _PmOpticalPowerUntimedLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 1),
    _PmOpticalPowerUntimedLaneIndex_Type()
)
pmOpticalPowerUntimedLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedLaneIndex.setStatus("current")
_PmOpticalPowerUntimedMonType_Type = PmOpticalPowerMonType
_PmOpticalPowerUntimedMonType_Object = MibTableColumn
pmOpticalPowerUntimedMonType = _PmOpticalPowerUntimedMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 2),
    _PmOpticalPowerUntimedMonType_Type()
)
pmOpticalPowerUntimedMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedMonType.setStatus("current")
_PmOpticalPowerUntimedMonTypeDescr_Type = DisplayString
_PmOpticalPowerUntimedMonTypeDescr_Object = MibTableColumn
pmOpticalPowerUntimedMonTypeDescr = _PmOpticalPowerUntimedMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 3),
    _PmOpticalPowerUntimedMonTypeDescr_Type()
)
pmOpticalPowerUntimedMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedMonTypeDescr.setStatus("current")
_PmOpticalPowerUntimedIfIndexDescr_Type = DisplayString
_PmOpticalPowerUntimedIfIndexDescr_Object = MibTableColumn
pmOpticalPowerUntimedIfIndexDescr = _PmOpticalPowerUntimedIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 4),
    _PmOpticalPowerUntimedIfIndexDescr_Type()
)
pmOpticalPowerUntimedIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedIfIndexDescr.setStatus("current")
_PmOpticalPowerUntimedMonValue_Type = DisplayString
_PmOpticalPowerUntimedMonValue_Object = MibTableColumn
pmOpticalPowerUntimedMonValue = _PmOpticalPowerUntimedMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 5),
    _PmOpticalPowerUntimedMonValue_Type()
)
pmOpticalPowerUntimedMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedMonValue.setStatus("current")
_PmOpticalPowerUntimedMonIDF_Type = DisplayString
_PmOpticalPowerUntimedMonIDF_Object = MibTableColumn
pmOpticalPowerUntimedMonIDF = _PmOpticalPowerUntimedMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 6),
    _PmOpticalPowerUntimedMonIDF_Type()
)
pmOpticalPowerUntimedMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedMonIDF.setStatus("current")
_PmOpticalPowerUntimedMonSupported_Type = TruthValue
_PmOpticalPowerUntimedMonSupported_Object = MibTableColumn
pmOpticalPowerUntimedMonSupported = _PmOpticalPowerUntimedMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 7),
    _PmOpticalPowerUntimedMonSupported_Type()
)
pmOpticalPowerUntimedMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedMonSupported.setStatus("current")
_PmOpticalPowerUntimedAdminState_Type = EnabledDisabledEnum
_PmOpticalPowerUntimedAdminState_Object = MibTableColumn
pmOpticalPowerUntimedAdminState = _PmOpticalPowerUntimedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 8),
    _PmOpticalPowerUntimedAdminState_Type()
)
pmOpticalPowerUntimedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedAdminState.setStatus("current")
_PmOpticalPowerUntimedMonStartDateTime_Type = DisplayString
_PmOpticalPowerUntimedMonStartDateTime_Object = MibTableColumn
pmOpticalPowerUntimedMonStartDateTime = _PmOpticalPowerUntimedMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 26, 1, 9),
    _PmOpticalPowerUntimedMonStartDateTime_Type()
)
pmOpticalPowerUntimedMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerUntimedMonStartDateTime.setStatus("current")
_PmOpticalPowerHistory15minStatsTable_Object = MibTable
pmOpticalPowerHistory15minStatsTable = _PmOpticalPowerHistory15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27)
)
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minStatsTable.setStatus("current")
_PmOpticalPowerHistory15minStatsEntry_Object = MibTableRow
pmOpticalPowerHistory15minStatsEntry = _PmOpticalPowerHistory15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1)
)
pmOpticalPowerHistory15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minBinIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minLaneIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minMonType"),
)
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minStatsEntry.setStatus("current")


class _PmOpticalPowerHistory15minBinIndex_Type(Integer32):
    """Custom type pmOpticalPowerHistory15minBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmOpticalPowerHistory15minBinIndex_Type.__name__ = "Integer32"
_PmOpticalPowerHistory15minBinIndex_Object = MibTableColumn
pmOpticalPowerHistory15minBinIndex = _PmOpticalPowerHistory15minBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 1),
    _PmOpticalPowerHistory15minBinIndex_Type()
)
pmOpticalPowerHistory15minBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minBinIndex.setStatus("current")


class _PmOpticalPowerHistory15minLaneIndex_Type(Integer32):
    """Custom type pmOpticalPowerHistory15minLaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmOpticalPowerHistory15minLaneIndex_Type.__name__ = "Integer32"
_PmOpticalPowerHistory15minLaneIndex_Object = MibTableColumn
pmOpticalPowerHistory15minLaneIndex = _PmOpticalPowerHistory15minLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 2),
    _PmOpticalPowerHistory15minLaneIndex_Type()
)
pmOpticalPowerHistory15minLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minLaneIndex.setStatus("current")
_PmOpticalPowerHistory15minMonType_Type = PmOpticalPowerMonType
_PmOpticalPowerHistory15minMonType_Object = MibTableColumn
pmOpticalPowerHistory15minMonType = _PmOpticalPowerHistory15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 3),
    _PmOpticalPowerHistory15minMonType_Type()
)
pmOpticalPowerHistory15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minMonType.setStatus("current")
_PmOpticalPowerHistory15minMonTypeDescr_Type = DisplayString
_PmOpticalPowerHistory15minMonTypeDescr_Object = MibTableColumn
pmOpticalPowerHistory15minMonTypeDescr = _PmOpticalPowerHistory15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 4),
    _PmOpticalPowerHistory15minMonTypeDescr_Type()
)
pmOpticalPowerHistory15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minMonTypeDescr.setStatus("current")
_PmOpticalPowerHistory15minIndexDescr_Type = DisplayString
_PmOpticalPowerHistory15minIndexDescr_Object = MibTableColumn
pmOpticalPowerHistory15minIndexDescr = _PmOpticalPowerHistory15minIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 5),
    _PmOpticalPowerHistory15minIndexDescr_Type()
)
pmOpticalPowerHistory15minIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minIndexDescr.setStatus("current")
_PmOpticalPowerHistory15minMonValue_Type = DisplayString
_PmOpticalPowerHistory15minMonValue_Object = MibTableColumn
pmOpticalPowerHistory15minMonValue = _PmOpticalPowerHistory15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 6),
    _PmOpticalPowerHistory15minMonValue_Type()
)
pmOpticalPowerHistory15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minMonValue.setStatus("current")
_PmOpticalPowerHistory15minMonIDF_Type = DisplayString
_PmOpticalPowerHistory15minMonIDF_Object = MibTableColumn
pmOpticalPowerHistory15minMonIDF = _PmOpticalPowerHistory15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 7),
    _PmOpticalPowerHistory15minMonIDF_Type()
)
pmOpticalPowerHistory15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minMonIDF.setStatus("current")
_PmOpticalPowerHistory15minMonSupported_Type = TruthValue
_PmOpticalPowerHistory15minMonSupported_Object = MibTableColumn
pmOpticalPowerHistory15minMonSupported = _PmOpticalPowerHistory15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 8),
    _PmOpticalPowerHistory15minMonSupported_Type()
)
pmOpticalPowerHistory15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minMonSupported.setStatus("current")
_PmOpticalPowerHistory15minAdminState_Type = EnabledDisabledEnum
_PmOpticalPowerHistory15minAdminState_Object = MibTableColumn
pmOpticalPowerHistory15minAdminState = _PmOpticalPowerHistory15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 9),
    _PmOpticalPowerHistory15minAdminState_Type()
)
pmOpticalPowerHistory15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minAdminState.setStatus("current")
_PmOpticalPowerHistory15minMonStartDateTime_Type = DisplayString
_PmOpticalPowerHistory15minMonStartDateTime_Object = MibTableColumn
pmOpticalPowerHistory15minMonStartDateTime = _PmOpticalPowerHistory15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 27, 1, 10),
    _PmOpticalPowerHistory15minMonStartDateTime_Type()
)
pmOpticalPowerHistory15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory15minMonStartDateTime.setStatus("current")
_PmOpticalPowerHistory24HrStatsTable_Object = MibTable
pmOpticalPowerHistory24HrStatsTable = _PmOpticalPowerHistory24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28)
)
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrStatsTable.setStatus("current")
_PmOpticalPowerHistory24HrStatsEntry_Object = MibTableRow
pmOpticalPowerHistory24HrStatsEntry = _PmOpticalPowerHistory24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1)
)
pmOpticalPowerHistory24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory24HrLaneIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory24HrMonType"),
)
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrStatsEntry.setStatus("current")


class _PmOpticalPowerHistory24HrLaneIndex_Type(Integer32):
    """Custom type pmOpticalPowerHistory24HrLaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmOpticalPowerHistory24HrLaneIndex_Type.__name__ = "Integer32"
_PmOpticalPowerHistory24HrLaneIndex_Object = MibTableColumn
pmOpticalPowerHistory24HrLaneIndex = _PmOpticalPowerHistory24HrLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 1),
    _PmOpticalPowerHistory24HrLaneIndex_Type()
)
pmOpticalPowerHistory24HrLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrLaneIndex.setStatus("current")
_PmOpticalPowerHistory24HrMonType_Type = PmOpticalPowerMonType
_PmOpticalPowerHistory24HrMonType_Object = MibTableColumn
pmOpticalPowerHistory24HrMonType = _PmOpticalPowerHistory24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 2),
    _PmOpticalPowerHistory24HrMonType_Type()
)
pmOpticalPowerHistory24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrMonType.setStatus("current")
_PmOpticalPowerHistory24HrMonTypeDescr_Type = DisplayString
_PmOpticalPowerHistory24HrMonTypeDescr_Object = MibTableColumn
pmOpticalPowerHistory24HrMonTypeDescr = _PmOpticalPowerHistory24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 3),
    _PmOpticalPowerHistory24HrMonTypeDescr_Type()
)
pmOpticalPowerHistory24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrMonTypeDescr.setStatus("current")
_PmOpticalPowerHistory24HrIndexDescr_Type = DisplayString
_PmOpticalPowerHistory24HrIndexDescr_Object = MibTableColumn
pmOpticalPowerHistory24HrIndexDescr = _PmOpticalPowerHistory24HrIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 4),
    _PmOpticalPowerHistory24HrIndexDescr_Type()
)
pmOpticalPowerHistory24HrIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrIndexDescr.setStatus("current")
_PmOpticalPowerHistory24HrMonValue_Type = DisplayString
_PmOpticalPowerHistory24HrMonValue_Object = MibTableColumn
pmOpticalPowerHistory24HrMonValue = _PmOpticalPowerHistory24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 5),
    _PmOpticalPowerHistory24HrMonValue_Type()
)
pmOpticalPowerHistory24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrMonValue.setStatus("current")
_PmOpticalPowerHistory24HrMonIDF_Type = DisplayString
_PmOpticalPowerHistory24HrMonIDF_Object = MibTableColumn
pmOpticalPowerHistory24HrMonIDF = _PmOpticalPowerHistory24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 6),
    _PmOpticalPowerHistory24HrMonIDF_Type()
)
pmOpticalPowerHistory24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrMonIDF.setStatus("current")
_PmOpticalPowerHistory24HrMonSupported_Type = TruthValue
_PmOpticalPowerHistory24HrMonSupported_Object = MibTableColumn
pmOpticalPowerHistory24HrMonSupported = _PmOpticalPowerHistory24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 7),
    _PmOpticalPowerHistory24HrMonSupported_Type()
)
pmOpticalPowerHistory24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrMonSupported.setStatus("current")
_PmOpticalPowerHistory24HrAdminState_Type = EnabledDisabledEnum
_PmOpticalPowerHistory24HrAdminState_Object = MibTableColumn
pmOpticalPowerHistory24HrAdminState = _PmOpticalPowerHistory24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 8),
    _PmOpticalPowerHistory24HrAdminState_Type()
)
pmOpticalPowerHistory24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrAdminState.setStatus("current")
_PmOpticalPowerHistory24HrMonStartDateTime_Type = DisplayString
_PmOpticalPowerHistory24HrMonStartDateTime_Object = MibTableColumn
pmOpticalPowerHistory24HrMonStartDateTime = _PmOpticalPowerHistory24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 28, 1, 9),
    _PmOpticalPowerHistory24HrMonStartDateTime_Type()
)
pmOpticalPowerHistory24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmOpticalPowerHistory24HrMonStartDateTime.setStatus("current")
_PmGcmCurrent15minStatsTable_Object = MibTable
pmGcmCurrent15minStatsTable = _PmGcmCurrent15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29)
)
if mibBuilder.loadTexts:
    pmGcmCurrent15minStatsTable.setStatus("current")
_PmGcmCurrent15minStatsEntry_Object = MibTableRow
pmGcmCurrent15minStatsEntry = _PmGcmCurrent15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1)
)
pmGcmCurrent15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmGcm15minMonType"),
)
if mibBuilder.loadTexts:
    pmGcmCurrent15minStatsEntry.setStatus("current")
_PmGcm15minMonType_Type = PmGcmMonType
_PmGcm15minMonType_Object = MibTableColumn
pmGcm15minMonType = _PmGcm15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1, 1),
    _PmGcm15minMonType_Type()
)
pmGcm15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmGcm15minMonType.setStatus("current")
_PmGcm15minMonTypeDescr_Type = DisplayString
_PmGcm15minMonTypeDescr_Object = MibTableColumn
pmGcm15minMonTypeDescr = _PmGcm15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1, 2),
    _PmGcm15minMonTypeDescr_Type()
)
pmGcm15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm15minMonTypeDescr.setStatus("current")
_PmGcm15minIfIndexDescr_Type = DisplayString
_PmGcm15minIfIndexDescr_Object = MibTableColumn
pmGcm15minIfIndexDescr = _PmGcm15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1, 3),
    _PmGcm15minIfIndexDescr_Type()
)
pmGcm15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm15minIfIndexDescr.setStatus("current")
_PmGcm15minMonValue_Type = DisplayString
_PmGcm15minMonValue_Object = MibTableColumn
pmGcm15minMonValue = _PmGcm15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1, 4),
    _PmGcm15minMonValue_Type()
)
pmGcm15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm15minMonValue.setStatus("current")
_PmGcm15minMonIDF_Type = DisplayString
_PmGcm15minMonIDF_Object = MibTableColumn
pmGcm15minMonIDF = _PmGcm15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1, 5),
    _PmGcm15minMonIDF_Type()
)
pmGcm15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm15minMonIDF.setStatus("current")
_PmGcm15minMonSupported_Type = TruthValue
_PmGcm15minMonSupported_Object = MibTableColumn
pmGcm15minMonSupported = _PmGcm15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1, 6),
    _PmGcm15minMonSupported_Type()
)
pmGcm15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm15minMonSupported.setStatus("current")
_PmGcm15minAdminState_Type = EnabledDisabledEnum
_PmGcm15minAdminState_Object = MibTableColumn
pmGcm15minAdminState = _PmGcm15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1, 7),
    _PmGcm15minAdminState_Type()
)
pmGcm15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm15minAdminState.setStatus("current")
_PmGcm15minMonStartDateTime_Type = DisplayString
_PmGcm15minMonStartDateTime_Object = MibTableColumn
pmGcm15minMonStartDateTime = _PmGcm15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 29, 1, 8),
    _PmGcm15minMonStartDateTime_Type()
)
pmGcm15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm15minMonStartDateTime.setStatus("current")
_PmGcmCurrent24HrStatsTable_Object = MibTable
pmGcmCurrent24HrStatsTable = _PmGcmCurrent24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30)
)
if mibBuilder.loadTexts:
    pmGcmCurrent24HrStatsTable.setStatus("current")
_PmGcmCurrent24HrStatsEntry_Object = MibTableRow
pmGcmCurrent24HrStatsEntry = _PmGcmCurrent24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1)
)
pmGcmCurrent24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmGcm24HrMonType"),
)
if mibBuilder.loadTexts:
    pmGcmCurrent24HrStatsEntry.setStatus("current")
_PmGcm24HrMonType_Type = PmGcmMonType
_PmGcm24HrMonType_Object = MibTableColumn
pmGcm24HrMonType = _PmGcm24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1, 1),
    _PmGcm24HrMonType_Type()
)
pmGcm24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmGcm24HrMonType.setStatus("current")
_PmGcm24HrMonTypeDescr_Type = DisplayString
_PmGcm24HrMonTypeDescr_Object = MibTableColumn
pmGcm24HrMonTypeDescr = _PmGcm24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1, 2),
    _PmGcm24HrMonTypeDescr_Type()
)
pmGcm24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm24HrMonTypeDescr.setStatus("current")
_PmGcm24HrIfIndexDescr_Type = DisplayString
_PmGcm24HrIfIndexDescr_Object = MibTableColumn
pmGcm24HrIfIndexDescr = _PmGcm24HrIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1, 3),
    _PmGcm24HrIfIndexDescr_Type()
)
pmGcm24HrIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm24HrIfIndexDescr.setStatus("current")
_PmGcm24HrMonValue_Type = DisplayString
_PmGcm24HrMonValue_Object = MibTableColumn
pmGcm24HrMonValue = _PmGcm24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1, 4),
    _PmGcm24HrMonValue_Type()
)
pmGcm24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm24HrMonValue.setStatus("current")
_PmGcm24HrMonIDF_Type = DisplayString
_PmGcm24HrMonIDF_Object = MibTableColumn
pmGcm24HrMonIDF = _PmGcm24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1, 5),
    _PmGcm24HrMonIDF_Type()
)
pmGcm24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm24HrMonIDF.setStatus("current")
_PmGcm24HrMonSupported_Type = TruthValue
_PmGcm24HrMonSupported_Object = MibTableColumn
pmGcm24HrMonSupported = _PmGcm24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1, 6),
    _PmGcm24HrMonSupported_Type()
)
pmGcm24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm24HrMonSupported.setStatus("current")
_PmGcm24HrAdminState_Type = EnabledDisabledEnum
_PmGcm24HrAdminState_Object = MibTableColumn
pmGcm24HrAdminState = _PmGcm24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1, 7),
    _PmGcm24HrAdminState_Type()
)
pmGcm24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm24HrAdminState.setStatus("current")
_PmGcm24HrMonStartDateTime_Type = DisplayString
_PmGcm24HrMonStartDateTime_Object = MibTableColumn
pmGcm24HrMonStartDateTime = _PmGcm24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 30, 1, 8),
    _PmGcm24HrMonStartDateTime_Type()
)
pmGcm24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcm24HrMonStartDateTime.setStatus("current")
_PmGcmUntimedStatsTable_Object = MibTable
pmGcmUntimedStatsTable = _PmGcmUntimedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31)
)
if mibBuilder.loadTexts:
    pmGcmUntimedStatsTable.setStatus("current")
_PmGcmUntimedStatsEntry_Object = MibTableRow
pmGcmUntimedStatsEntry = _PmGcmUntimedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1)
)
pmGcmUntimedStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmGcmUntimedMonType"),
)
if mibBuilder.loadTexts:
    pmGcmUntimedStatsEntry.setStatus("current")
_PmGcmUntimedMonType_Type = PmGcmMonType
_PmGcmUntimedMonType_Object = MibTableColumn
pmGcmUntimedMonType = _PmGcmUntimedMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1, 1),
    _PmGcmUntimedMonType_Type()
)
pmGcmUntimedMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmGcmUntimedMonType.setStatus("current")
_PmGcmUntimedMonTypeDescr_Type = DisplayString
_PmGcmUntimedMonTypeDescr_Object = MibTableColumn
pmGcmUntimedMonTypeDescr = _PmGcmUntimedMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1, 2),
    _PmGcmUntimedMonTypeDescr_Type()
)
pmGcmUntimedMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmUntimedMonTypeDescr.setStatus("current")
_PmGcmUntimedIfIndexDescr_Type = DisplayString
_PmGcmUntimedIfIndexDescr_Object = MibTableColumn
pmGcmUntimedIfIndexDescr = _PmGcmUntimedIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1, 3),
    _PmGcmUntimedIfIndexDescr_Type()
)
pmGcmUntimedIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmUntimedIfIndexDescr.setStatus("current")
_PmGcmUntimedMonValue_Type = DisplayString
_PmGcmUntimedMonValue_Object = MibTableColumn
pmGcmUntimedMonValue = _PmGcmUntimedMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1, 4),
    _PmGcmUntimedMonValue_Type()
)
pmGcmUntimedMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmUntimedMonValue.setStatus("current")
_PmGcmUntimedMonIDF_Type = DisplayString
_PmGcmUntimedMonIDF_Object = MibTableColumn
pmGcmUntimedMonIDF = _PmGcmUntimedMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1, 5),
    _PmGcmUntimedMonIDF_Type()
)
pmGcmUntimedMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmUntimedMonIDF.setStatus("current")
_PmGcmUntimedMonSupported_Type = TruthValue
_PmGcmUntimedMonSupported_Object = MibTableColumn
pmGcmUntimedMonSupported = _PmGcmUntimedMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1, 6),
    _PmGcmUntimedMonSupported_Type()
)
pmGcmUntimedMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmUntimedMonSupported.setStatus("current")
_PmGcmUntimedAdminState_Type = EnabledDisabledEnum
_PmGcmUntimedAdminState_Object = MibTableColumn
pmGcmUntimedAdminState = _PmGcmUntimedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1, 7),
    _PmGcmUntimedAdminState_Type()
)
pmGcmUntimedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmUntimedAdminState.setStatus("current")
_PmGcmUntimedMonStartDateTime_Type = DisplayString
_PmGcmUntimedMonStartDateTime_Object = MibTableColumn
pmGcmUntimedMonStartDateTime = _PmGcmUntimedMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 31, 1, 8),
    _PmGcmUntimedMonStartDateTime_Type()
)
pmGcmUntimedMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmUntimedMonStartDateTime.setStatus("current")
_PmGcmHistory15minStatsTable_Object = MibTable
pmGcmHistory15minStatsTable = _PmGcmHistory15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32)
)
if mibBuilder.loadTexts:
    pmGcmHistory15minStatsTable.setStatus("current")
_PmGcmHistory15minStatsEntry_Object = MibTableRow
pmGcmHistory15minStatsEntry = _PmGcmHistory15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1)
)
pmGcmHistory15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minBinIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minMonType"),
)
if mibBuilder.loadTexts:
    pmGcmHistory15minStatsEntry.setStatus("current")


class _PmGcmHistory15minBinIndex_Type(Integer32):
    """Custom type pmGcmHistory15minBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmGcmHistory15minBinIndex_Type.__name__ = "Integer32"
_PmGcmHistory15minBinIndex_Object = MibTableColumn
pmGcmHistory15minBinIndex = _PmGcmHistory15minBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 1),
    _PmGcmHistory15minBinIndex_Type()
)
pmGcmHistory15minBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmGcmHistory15minBinIndex.setStatus("current")
_PmGcmHistory15minMonType_Type = PmGcmMonType
_PmGcmHistory15minMonType_Object = MibTableColumn
pmGcmHistory15minMonType = _PmGcmHistory15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 2),
    _PmGcmHistory15minMonType_Type()
)
pmGcmHistory15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmGcmHistory15minMonType.setStatus("current")
_PmGcmHistory15minMonTypeDescr_Type = DisplayString
_PmGcmHistory15minMonTypeDescr_Object = MibTableColumn
pmGcmHistory15minMonTypeDescr = _PmGcmHistory15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 3),
    _PmGcmHistory15minMonTypeDescr_Type()
)
pmGcmHistory15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory15minMonTypeDescr.setStatus("current")
_PmGcmHistory15minIndexDescr_Type = DisplayString
_PmGcmHistory15minIndexDescr_Object = MibTableColumn
pmGcmHistory15minIndexDescr = _PmGcmHistory15minIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 4),
    _PmGcmHistory15minIndexDescr_Type()
)
pmGcmHistory15minIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory15minIndexDescr.setStatus("current")
_PmGcmHistory15minMonValue_Type = DisplayString
_PmGcmHistory15minMonValue_Object = MibTableColumn
pmGcmHistory15minMonValue = _PmGcmHistory15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 5),
    _PmGcmHistory15minMonValue_Type()
)
pmGcmHistory15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory15minMonValue.setStatus("current")
_PmGcmHistory15minMonIDF_Type = DisplayString
_PmGcmHistory15minMonIDF_Object = MibTableColumn
pmGcmHistory15minMonIDF = _PmGcmHistory15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 6),
    _PmGcmHistory15minMonIDF_Type()
)
pmGcmHistory15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory15minMonIDF.setStatus("current")
_PmGcmHistory15minMonSupported_Type = TruthValue
_PmGcmHistory15minMonSupported_Object = MibTableColumn
pmGcmHistory15minMonSupported = _PmGcmHistory15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 7),
    _PmGcmHistory15minMonSupported_Type()
)
pmGcmHistory15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory15minMonSupported.setStatus("current")
_PmGcmHistory15minAdminState_Type = EnabledDisabledEnum
_PmGcmHistory15minAdminState_Object = MibTableColumn
pmGcmHistory15minAdminState = _PmGcmHistory15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 8),
    _PmGcmHistory15minAdminState_Type()
)
pmGcmHistory15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory15minAdminState.setStatus("current")
_PmGcmHistory15minMonStartDateTime_Type = DisplayString
_PmGcmHistory15minMonStartDateTime_Object = MibTableColumn
pmGcmHistory15minMonStartDateTime = _PmGcmHistory15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 32, 1, 9),
    _PmGcmHistory15minMonStartDateTime_Type()
)
pmGcmHistory15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory15minMonStartDateTime.setStatus("current")
_PmGcmHistory24HrStatsTable_Object = MibTable
pmGcmHistory24HrStatsTable = _PmGcmHistory24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33)
)
if mibBuilder.loadTexts:
    pmGcmHistory24HrStatsTable.setStatus("current")
_PmGcmHistory24HrStatsEntry_Object = MibTableRow
pmGcmHistory24HrStatsEntry = _PmGcmHistory24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1)
)
pmGcmHistory24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory24HrMonType"),
)
if mibBuilder.loadTexts:
    pmGcmHistory24HrStatsEntry.setStatus("current")
_PmGcmHistory24HrMonType_Type = PmGcmMonType
_PmGcmHistory24HrMonType_Object = MibTableColumn
pmGcmHistory24HrMonType = _PmGcmHistory24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1, 1),
    _PmGcmHistory24HrMonType_Type()
)
pmGcmHistory24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmGcmHistory24HrMonType.setStatus("current")
_PmGcmHistory24HrMonTypeDescr_Type = DisplayString
_PmGcmHistory24HrMonTypeDescr_Object = MibTableColumn
pmGcmHistory24HrMonTypeDescr = _PmGcmHistory24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1, 2),
    _PmGcmHistory24HrMonTypeDescr_Type()
)
pmGcmHistory24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory24HrMonTypeDescr.setStatus("current")
_PmGcmHistory24HrIndexDescr_Type = DisplayString
_PmGcmHistory24HrIndexDescr_Object = MibTableColumn
pmGcmHistory24HrIndexDescr = _PmGcmHistory24HrIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1, 3),
    _PmGcmHistory24HrIndexDescr_Type()
)
pmGcmHistory24HrIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory24HrIndexDescr.setStatus("current")
_PmGcmHistory24HrMonValue_Type = DisplayString
_PmGcmHistory24HrMonValue_Object = MibTableColumn
pmGcmHistory24HrMonValue = _PmGcmHistory24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1, 4),
    _PmGcmHistory24HrMonValue_Type()
)
pmGcmHistory24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory24HrMonValue.setStatus("current")
_PmGcmHistory24HrMonIDF_Type = DisplayString
_PmGcmHistory24HrMonIDF_Object = MibTableColumn
pmGcmHistory24HrMonIDF = _PmGcmHistory24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1, 5),
    _PmGcmHistory24HrMonIDF_Type()
)
pmGcmHistory24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory24HrMonIDF.setStatus("current")
_PmGcmHistory24HrMonSupported_Type = TruthValue
_PmGcmHistory24HrMonSupported_Object = MibTableColumn
pmGcmHistory24HrMonSupported = _PmGcmHistory24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1, 6),
    _PmGcmHistory24HrMonSupported_Type()
)
pmGcmHistory24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory24HrMonSupported.setStatus("current")
_PmGcmHistory24HrAdminState_Type = EnabledDisabledEnum
_PmGcmHistory24HrAdminState_Object = MibTableColumn
pmGcmHistory24HrAdminState = _PmGcmHistory24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1, 7),
    _PmGcmHistory24HrAdminState_Type()
)
pmGcmHistory24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory24HrAdminState.setStatus("current")
_PmGcmHistory24HrMonStartDateTime_Type = DisplayString
_PmGcmHistory24HrMonStartDateTime_Object = MibTableColumn
pmGcmHistory24HrMonStartDateTime = _PmGcmHistory24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 33, 1, 8),
    _PmGcmHistory24HrMonStartDateTime_Type()
)
pmGcmHistory24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGcmHistory24HrMonStartDateTime.setStatus("current")
_PmPhotonicsCurrent15minStatsTable_Object = MibTable
pmPhotonicsCurrent15minStatsTable = _PmPhotonicsCurrent15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34)
)
if mibBuilder.loadTexts:
    pmPhotonicsCurrent15minStatsTable.setStatus("current")
_PmPhotonicsCurrent15minStatsEntry_Object = MibTableRow
pmPhotonicsCurrent15minStatsEntry = _PmPhotonicsCurrent15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1)
)
pmPhotonicsCurrent15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics15minMonType"),
)
if mibBuilder.loadTexts:
    pmPhotonicsCurrent15minStatsEntry.setStatus("current")
_PmPhotonics15minMonType_Type = PmPhotonicsMonType
_PmPhotonics15minMonType_Object = MibTableColumn
pmPhotonics15minMonType = _PmPhotonics15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1, 1),
    _PmPhotonics15minMonType_Type()
)
pmPhotonics15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPhotonics15minMonType.setStatus("current")
_PmPhotonics15minMonTypeDescr_Type = DisplayString
_PmPhotonics15minMonTypeDescr_Object = MibTableColumn
pmPhotonics15minMonTypeDescr = _PmPhotonics15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1, 2),
    _PmPhotonics15minMonTypeDescr_Type()
)
pmPhotonics15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics15minMonTypeDescr.setStatus("current")
_PmPhotonics15minIfIndexDescr_Type = DisplayString
_PmPhotonics15minIfIndexDescr_Object = MibTableColumn
pmPhotonics15minIfIndexDescr = _PmPhotonics15minIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1, 3),
    _PmPhotonics15minIfIndexDescr_Type()
)
pmPhotonics15minIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics15minIfIndexDescr.setStatus("current")
_PmPhotonics15minMonValue_Type = DisplayString
_PmPhotonics15minMonValue_Object = MibTableColumn
pmPhotonics15minMonValue = _PmPhotonics15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1, 4),
    _PmPhotonics15minMonValue_Type()
)
pmPhotonics15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics15minMonValue.setStatus("current")
_PmPhotonics15minMonIDF_Type = DisplayString
_PmPhotonics15minMonIDF_Object = MibTableColumn
pmPhotonics15minMonIDF = _PmPhotonics15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1, 5),
    _PmPhotonics15minMonIDF_Type()
)
pmPhotonics15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics15minMonIDF.setStatus("current")
_PmPhotonics15minMonSupported_Type = TruthValue
_PmPhotonics15minMonSupported_Object = MibTableColumn
pmPhotonics15minMonSupported = _PmPhotonics15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1, 6),
    _PmPhotonics15minMonSupported_Type()
)
pmPhotonics15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics15minMonSupported.setStatus("current")
_PmPhotonics15minAdminState_Type = EnabledDisabledEnum
_PmPhotonics15minAdminState_Object = MibTableColumn
pmPhotonics15minAdminState = _PmPhotonics15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1, 7),
    _PmPhotonics15minAdminState_Type()
)
pmPhotonics15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics15minAdminState.setStatus("current")
_PmPhotonics15minMonStartDateTime_Type = DisplayString
_PmPhotonics15minMonStartDateTime_Object = MibTableColumn
pmPhotonics15minMonStartDateTime = _PmPhotonics15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 34, 1, 8),
    _PmPhotonics15minMonStartDateTime_Type()
)
pmPhotonics15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics15minMonStartDateTime.setStatus("current")
_PmPhotonicsCurrent24HrStatsTable_Object = MibTable
pmPhotonicsCurrent24HrStatsTable = _PmPhotonicsCurrent24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35)
)
if mibBuilder.loadTexts:
    pmPhotonicsCurrent24HrStatsTable.setStatus("current")
_PmPhotonicsCurrent24HrStatsEntry_Object = MibTableRow
pmPhotonicsCurrent24HrStatsEntry = _PmPhotonicsCurrent24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1)
)
pmPhotonicsCurrent24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics24HrMonType"),
)
if mibBuilder.loadTexts:
    pmPhotonicsCurrent24HrStatsEntry.setStatus("current")
_PmPhotonics24HrMonType_Type = PmPhotonicsMonType
_PmPhotonics24HrMonType_Object = MibTableColumn
pmPhotonics24HrMonType = _PmPhotonics24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1, 1),
    _PmPhotonics24HrMonType_Type()
)
pmPhotonics24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPhotonics24HrMonType.setStatus("current")
_PmPhotonics24HrMonTypeDescr_Type = DisplayString
_PmPhotonics24HrMonTypeDescr_Object = MibTableColumn
pmPhotonics24HrMonTypeDescr = _PmPhotonics24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1, 2),
    _PmPhotonics24HrMonTypeDescr_Type()
)
pmPhotonics24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics24HrMonTypeDescr.setStatus("current")
_PmPhotonics24HrIfIndexDescr_Type = DisplayString
_PmPhotonics24HrIfIndexDescr_Object = MibTableColumn
pmPhotonics24HrIfIndexDescr = _PmPhotonics24HrIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1, 3),
    _PmPhotonics24HrIfIndexDescr_Type()
)
pmPhotonics24HrIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics24HrIfIndexDescr.setStatus("current")
_PmPhotonics24HrMonValue_Type = DisplayString
_PmPhotonics24HrMonValue_Object = MibTableColumn
pmPhotonics24HrMonValue = _PmPhotonics24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1, 4),
    _PmPhotonics24HrMonValue_Type()
)
pmPhotonics24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics24HrMonValue.setStatus("current")
_PmPhotonics24HrMonIDF_Type = DisplayString
_PmPhotonics24HrMonIDF_Object = MibTableColumn
pmPhotonics24HrMonIDF = _PmPhotonics24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1, 5),
    _PmPhotonics24HrMonIDF_Type()
)
pmPhotonics24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics24HrMonIDF.setStatus("current")
_PmPhotonics24HrMonSupported_Type = TruthValue
_PmPhotonics24HrMonSupported_Object = MibTableColumn
pmPhotonics24HrMonSupported = _PmPhotonics24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1, 6),
    _PmPhotonics24HrMonSupported_Type()
)
pmPhotonics24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics24HrMonSupported.setStatus("current")
_PmPhotonics24HrAdminState_Type = EnabledDisabledEnum
_PmPhotonics24HrAdminState_Object = MibTableColumn
pmPhotonics24HrAdminState = _PmPhotonics24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1, 7),
    _PmPhotonics24HrAdminState_Type()
)
pmPhotonics24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics24HrAdminState.setStatus("current")
_PmPhotonics24HrMonStartDateTime_Type = DisplayString
_PmPhotonics24HrMonStartDateTime_Object = MibTableColumn
pmPhotonics24HrMonStartDateTime = _PmPhotonics24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 35, 1, 8),
    _PmPhotonics24HrMonStartDateTime_Type()
)
pmPhotonics24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonics24HrMonStartDateTime.setStatus("current")
_PmPhotonicsUntimedStatsTable_Object = MibTable
pmPhotonicsUntimedStatsTable = _PmPhotonicsUntimedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36)
)
if mibBuilder.loadTexts:
    pmPhotonicsUntimedStatsTable.setStatus("current")
_PmPhotonicsUntimedStatsEntry_Object = MibTableRow
pmPhotonicsUntimedStatsEntry = _PmPhotonicsUntimedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1)
)
pmPhotonicsUntimedStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsUntimedMonType"),
)
if mibBuilder.loadTexts:
    pmPhotonicsUntimedStatsEntry.setStatus("current")
_PmPhotonicsUntimedMonType_Type = PmPhotonicsMonType
_PmPhotonicsUntimedMonType_Object = MibTableColumn
pmPhotonicsUntimedMonType = _PmPhotonicsUntimedMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1, 1),
    _PmPhotonicsUntimedMonType_Type()
)
pmPhotonicsUntimedMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPhotonicsUntimedMonType.setStatus("current")
_PmPhotonicsUntimedMonTypeDescr_Type = DisplayString
_PmPhotonicsUntimedMonTypeDescr_Object = MibTableColumn
pmPhotonicsUntimedMonTypeDescr = _PmPhotonicsUntimedMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1, 2),
    _PmPhotonicsUntimedMonTypeDescr_Type()
)
pmPhotonicsUntimedMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsUntimedMonTypeDescr.setStatus("current")
_PmPhotonicsUntimedIfIndexDescr_Type = DisplayString
_PmPhotonicsUntimedIfIndexDescr_Object = MibTableColumn
pmPhotonicsUntimedIfIndexDescr = _PmPhotonicsUntimedIfIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1, 3),
    _PmPhotonicsUntimedIfIndexDescr_Type()
)
pmPhotonicsUntimedIfIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsUntimedIfIndexDescr.setStatus("current")
_PmPhotonicsUntimedMonValue_Type = DisplayString
_PmPhotonicsUntimedMonValue_Object = MibTableColumn
pmPhotonicsUntimedMonValue = _PmPhotonicsUntimedMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1, 4),
    _PmPhotonicsUntimedMonValue_Type()
)
pmPhotonicsUntimedMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsUntimedMonValue.setStatus("current")
_PmPhotonicsUntimedMonIDF_Type = DisplayString
_PmPhotonicsUntimedMonIDF_Object = MibTableColumn
pmPhotonicsUntimedMonIDF = _PmPhotonicsUntimedMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1, 5),
    _PmPhotonicsUntimedMonIDF_Type()
)
pmPhotonicsUntimedMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsUntimedMonIDF.setStatus("current")
_PmPhotonicsUntimedMonSupported_Type = TruthValue
_PmPhotonicsUntimedMonSupported_Object = MibTableColumn
pmPhotonicsUntimedMonSupported = _PmPhotonicsUntimedMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1, 6),
    _PmPhotonicsUntimedMonSupported_Type()
)
pmPhotonicsUntimedMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsUntimedMonSupported.setStatus("current")
_PmPhotonicsUntimedAdminState_Type = EnabledDisabledEnum
_PmPhotonicsUntimedAdminState_Object = MibTableColumn
pmPhotonicsUntimedAdminState = _PmPhotonicsUntimedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1, 7),
    _PmPhotonicsUntimedAdminState_Type()
)
pmPhotonicsUntimedAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsUntimedAdminState.setStatus("current")
_PmPhotonicsUntimedMonStartDateTime_Type = DisplayString
_PmPhotonicsUntimedMonStartDateTime_Object = MibTableColumn
pmPhotonicsUntimedMonStartDateTime = _PmPhotonicsUntimedMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 36, 1, 8),
    _PmPhotonicsUntimedMonStartDateTime_Type()
)
pmPhotonicsUntimedMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsUntimedMonStartDateTime.setStatus("current")
_PmPhotonicsHistory15minStatsTable_Object = MibTable
pmPhotonicsHistory15minStatsTable = _PmPhotonicsHistory15minStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37)
)
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minStatsTable.setStatus("current")
_PmPhotonicsHistory15minStatsEntry_Object = MibTableRow
pmPhotonicsHistory15minStatsEntry = _PmPhotonicsHistory15minStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1)
)
pmPhotonicsHistory15minStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minBinIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minMonType"),
)
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minStatsEntry.setStatus("current")


class _PmPhotonicsHistory15minBinIndex_Type(Integer32):
    """Custom type pmPhotonicsHistory15minBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmPhotonicsHistory15minBinIndex_Type.__name__ = "Integer32"
_PmPhotonicsHistory15minBinIndex_Object = MibTableColumn
pmPhotonicsHistory15minBinIndex = _PmPhotonicsHistory15minBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 1),
    _PmPhotonicsHistory15minBinIndex_Type()
)
pmPhotonicsHistory15minBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minBinIndex.setStatus("current")
_PmPhotonicsHistory15minMonType_Type = PmPhotonicsMonType
_PmPhotonicsHistory15minMonType_Object = MibTableColumn
pmPhotonicsHistory15minMonType = _PmPhotonicsHistory15minMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 2),
    _PmPhotonicsHistory15minMonType_Type()
)
pmPhotonicsHistory15minMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minMonType.setStatus("current")
_PmPhotonicsHistory15minMonTypeDescr_Type = DisplayString
_PmPhotonicsHistory15minMonTypeDescr_Object = MibTableColumn
pmPhotonicsHistory15minMonTypeDescr = _PmPhotonicsHistory15minMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 3),
    _PmPhotonicsHistory15minMonTypeDescr_Type()
)
pmPhotonicsHistory15minMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minMonTypeDescr.setStatus("current")
_PmPhotonicsHistory15minIndexDescr_Type = DisplayString
_PmPhotonicsHistory15minIndexDescr_Object = MibTableColumn
pmPhotonicsHistory15minIndexDescr = _PmPhotonicsHistory15minIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 4),
    _PmPhotonicsHistory15minIndexDescr_Type()
)
pmPhotonicsHistory15minIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minIndexDescr.setStatus("current")
_PmPhotonicsHistory15minMonValue_Type = DisplayString
_PmPhotonicsHistory15minMonValue_Object = MibTableColumn
pmPhotonicsHistory15minMonValue = _PmPhotonicsHistory15minMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 5),
    _PmPhotonicsHistory15minMonValue_Type()
)
pmPhotonicsHistory15minMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minMonValue.setStatus("current")
_PmPhotonicsHistory15minMonIDF_Type = DisplayString
_PmPhotonicsHistory15minMonIDF_Object = MibTableColumn
pmPhotonicsHistory15minMonIDF = _PmPhotonicsHistory15minMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 6),
    _PmPhotonicsHistory15minMonIDF_Type()
)
pmPhotonicsHistory15minMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minMonIDF.setStatus("current")
_PmPhotonicsHistory15minMonSupported_Type = TruthValue
_PmPhotonicsHistory15minMonSupported_Object = MibTableColumn
pmPhotonicsHistory15minMonSupported = _PmPhotonicsHistory15minMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 7),
    _PmPhotonicsHistory15minMonSupported_Type()
)
pmPhotonicsHistory15minMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minMonSupported.setStatus("current")
_PmPhotonicsHistory15minAdminState_Type = EnabledDisabledEnum
_PmPhotonicsHistory15minAdminState_Object = MibTableColumn
pmPhotonicsHistory15minAdminState = _PmPhotonicsHistory15minAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 8),
    _PmPhotonicsHistory15minAdminState_Type()
)
pmPhotonicsHistory15minAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minAdminState.setStatus("current")
_PmPhotonicsHistory15minMonStartDateTime_Type = DisplayString
_PmPhotonicsHistory15minMonStartDateTime_Object = MibTableColumn
pmPhotonicsHistory15minMonStartDateTime = _PmPhotonicsHistory15minMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 37, 1, 9),
    _PmPhotonicsHistory15minMonStartDateTime_Type()
)
pmPhotonicsHistory15minMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory15minMonStartDateTime.setStatus("current")
_PmPhotonicsHistory24HrStatsTable_Object = MibTable
pmPhotonicsHistory24HrStatsTable = _PmPhotonicsHistory24HrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38)
)
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrStatsTable.setStatus("current")
_PmPhotonicsHistory24HrStatsEntry_Object = MibTableRow
pmPhotonicsHistory24HrStatsEntry = _PmPhotonicsHistory24HrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1)
)
pmPhotonicsHistory24HrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory24HrMonType"),
)
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrStatsEntry.setStatus("current")
_PmPhotonicsHistory24HrMonType_Type = PmPhotonicsMonType
_PmPhotonicsHistory24HrMonType_Object = MibTableColumn
pmPhotonicsHistory24HrMonType = _PmPhotonicsHistory24HrMonType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1, 1),
    _PmPhotonicsHistory24HrMonType_Type()
)
pmPhotonicsHistory24HrMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrMonType.setStatus("current")
_PmPhotonicsHistory24HrMonTypeDescr_Type = DisplayString
_PmPhotonicsHistory24HrMonTypeDescr_Object = MibTableColumn
pmPhotonicsHistory24HrMonTypeDescr = _PmPhotonicsHistory24HrMonTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1, 2),
    _PmPhotonicsHistory24HrMonTypeDescr_Type()
)
pmPhotonicsHistory24HrMonTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrMonTypeDescr.setStatus("current")
_PmPhotonicsHistory24HrIndexDescr_Type = DisplayString
_PmPhotonicsHistory24HrIndexDescr_Object = MibTableColumn
pmPhotonicsHistory24HrIndexDescr = _PmPhotonicsHistory24HrIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1, 3),
    _PmPhotonicsHistory24HrIndexDescr_Type()
)
pmPhotonicsHistory24HrIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrIndexDescr.setStatus("current")
_PmPhotonicsHistory24HrMonValue_Type = DisplayString
_PmPhotonicsHistory24HrMonValue_Object = MibTableColumn
pmPhotonicsHistory24HrMonValue = _PmPhotonicsHistory24HrMonValue_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1, 4),
    _PmPhotonicsHistory24HrMonValue_Type()
)
pmPhotonicsHistory24HrMonValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrMonValue.setStatus("current")
_PmPhotonicsHistory24HrMonIDF_Type = DisplayString
_PmPhotonicsHistory24HrMonIDF_Object = MibTableColumn
pmPhotonicsHistory24HrMonIDF = _PmPhotonicsHistory24HrMonIDF_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1, 5),
    _PmPhotonicsHistory24HrMonIDF_Type()
)
pmPhotonicsHistory24HrMonIDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrMonIDF.setStatus("current")
_PmPhotonicsHistory24HrMonSupported_Type = TruthValue
_PmPhotonicsHistory24HrMonSupported_Object = MibTableColumn
pmPhotonicsHistory24HrMonSupported = _PmPhotonicsHistory24HrMonSupported_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1, 6),
    _PmPhotonicsHistory24HrMonSupported_Type()
)
pmPhotonicsHistory24HrMonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrMonSupported.setStatus("current")
_PmPhotonicsHistory24HrAdminState_Type = EnabledDisabledEnum
_PmPhotonicsHistory24HrAdminState_Object = MibTableColumn
pmPhotonicsHistory24HrAdminState = _PmPhotonicsHistory24HrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1, 7),
    _PmPhotonicsHistory24HrAdminState_Type()
)
pmPhotonicsHistory24HrAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrAdminState.setStatus("current")
_PmPhotonicsHistory24HrMonStartDateTime_Type = DisplayString
_PmPhotonicsHistory24HrMonStartDateTime_Object = MibTableColumn
pmPhotonicsHistory24HrMonStartDateTime = _PmPhotonicsHistory24HrMonStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 38, 1, 8),
    _PmPhotonicsHistory24HrMonStartDateTime_Type()
)
pmPhotonicsHistory24HrMonStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmPhotonicsHistory24HrMonStartDateTime.setStatus("current")

# Managed Objects groups

pmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 2, 1, 1)
)
pmGroup.setObjects(
      *(("CIENA-WS-PLATFORM-PM-MIB", "pmAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet24HrIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernet24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetUntimedMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetUntimedIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetUntimedMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetUntimedMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetUntimedMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetUntimedAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetUntimedMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory24HrIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmEthernetHistory24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem24HrIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModem24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemUntimedMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemUntimedIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemUntimedMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemUntimedMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemUntimedMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemUntimedAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemUntimedMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory24HrIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmModemHistory24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu24HrIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtu24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuUntimedMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuUntimedIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuUntimedMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuUntimedMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuUntimedMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuUntimedAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuUntimedMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory24HrIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOtuHistory24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu24HrIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOdu24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduUntimedMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduUntimedIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduUntimedMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduUntimedMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduUntimedMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduUntimedAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduUntimedMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory24HrIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOduHistory24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPower24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerUntimedMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory24HrIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmOpticalPowerHistory24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm24HrIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcm24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmUntimedMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmUntimedIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmUntimedMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmUntimedMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmUntimedMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmUntimedAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmUntimedMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory24HrIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmGcmHistory24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics15minIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics24HrIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics24HrAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonics24HrMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsUntimedMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsUntimedIfIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsUntimedMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsUntimedMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsUntimedMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsUntimedAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsUntimedMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minAdminState"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory15minMonStartDateTime"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory24HrMonTypeDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory24HrIndexDescr"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory24HrMonValue"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory24HrMonIDF"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory24HrMonSupported"),
        ("CIENA-WS-PLATFORM-PM-MIB", "pmPhotonicsHistory24HrMonStartDateTime"))
)
if mibBuilder.loadTexts:
    pmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 5, 22, 2, 2, 1)
)
pmCompliance.setObjects(
    ("CIENA-WS-PLATFORM-PM-MIB", "pmGroup")
)
if mibBuilder.loadTexts:
    pmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-PLATFORM-PM-MIB",
    **{"PmConfigurationMode": PmConfigurationMode,
       "PmEthernetMonType": PmEthernetMonType,
       "PmOtuMonType": PmOtuMonType,
       "PmOpticalPowerMonType": PmOpticalPowerMonType,
       "PmOduMonType": PmOduMonType,
       "PmModemMonType": PmModemMonType,
       "PmGcmMonType": PmGcmMonType,
       "PmPhotonicsMonType": PmPhotonicsMonType,
       "cienaWsPlatformPmMIB": cienaWsPlatformPmMIB,
       "pmObjects": pmObjects,
       "pmConformance": pmConformance,
       "pmGroups": pmGroups,
       "pmGroup": pmGroup,
       "pmCompliances": pmCompliances,
       "pmCompliance": pmCompliance,
       "pmGlobalConfigTable": pmGlobalConfigTable,
       "pmGlobalConfigEntry": pmGlobalConfigEntry,
       "pmGlobalConfigTableSnmpKey": pmGlobalConfigTableSnmpKey,
       "pmAdminState": pmAdminState,
       "pmEthernetCurrent15minStatsTable": pmEthernetCurrent15minStatsTable,
       "pmEthernetCurrent15minStatsEntry": pmEthernetCurrent15minStatsEntry,
       "pmEthernet15minMonType": pmEthernet15minMonType,
       "pmEthernet15minMonTypeDescr": pmEthernet15minMonTypeDescr,
       "pmEthernet15minIfIndexDescr": pmEthernet15minIfIndexDescr,
       "pmEthernet15minMonValue": pmEthernet15minMonValue,
       "pmEthernet15minMonIDF": pmEthernet15minMonIDF,
       "pmEthernet15minMonSupported": pmEthernet15minMonSupported,
       "pmEthernet15minAdminState": pmEthernet15minAdminState,
       "pmEthernet15minMonStartDateTime": pmEthernet15minMonStartDateTime,
       "pmEthernetCurrent24HrStatsTable": pmEthernetCurrent24HrStatsTable,
       "pmEthernetCurrent24HrStatsEntry": pmEthernetCurrent24HrStatsEntry,
       "pmEthernet24HrMonType": pmEthernet24HrMonType,
       "pmEthernet24HrMonTypeDescr": pmEthernet24HrMonTypeDescr,
       "pmEthernet24HrIfIndexDescr": pmEthernet24HrIfIndexDescr,
       "pmEthernet24HrMonValue": pmEthernet24HrMonValue,
       "pmEthernet24HrMonIDF": pmEthernet24HrMonIDF,
       "pmEthernet24HrMonSupported": pmEthernet24HrMonSupported,
       "pmEthernet24HrAdminState": pmEthernet24HrAdminState,
       "pmEthernet24HrMonStartDateTime": pmEthernet24HrMonStartDateTime,
       "pmEthernetUntimedStatsTable": pmEthernetUntimedStatsTable,
       "pmEthernetUntimedStatsEntry": pmEthernetUntimedStatsEntry,
       "pmEthernetUntimedMonType": pmEthernetUntimedMonType,
       "pmEthernetUntimedMonTypeDescr": pmEthernetUntimedMonTypeDescr,
       "pmEthernetUntimedIfIndexDescr": pmEthernetUntimedIfIndexDescr,
       "pmEthernetUntimedMonValue": pmEthernetUntimedMonValue,
       "pmEthernetUntimedMonIDF": pmEthernetUntimedMonIDF,
       "pmEthernetUntimedMonSupported": pmEthernetUntimedMonSupported,
       "pmEthernetUntimedAdminState": pmEthernetUntimedAdminState,
       "pmEthernetUntimedMonStartDateTime": pmEthernetUntimedMonStartDateTime,
       "pmEthernetHistory15minStatsTable": pmEthernetHistory15minStatsTable,
       "pmEthernetHistory15minStatsEntry": pmEthernetHistory15minStatsEntry,
       "pmEthernetHistory15minBinIndex": pmEthernetHistory15minBinIndex,
       "pmEthernetHistory15minMonType": pmEthernetHistory15minMonType,
       "pmEthernetHistory15minMonTypeDescr": pmEthernetHistory15minMonTypeDescr,
       "pmEthernetHistory15minIfIndexDescr": pmEthernetHistory15minIfIndexDescr,
       "pmEthernetHistory15minMonValue": pmEthernetHistory15minMonValue,
       "pmEthernetHistory15minMonIDF": pmEthernetHistory15minMonIDF,
       "pmEthernetHistory15minMonSupported": pmEthernetHistory15minMonSupported,
       "pmEthernetHistory15minAdminState": pmEthernetHistory15minAdminState,
       "pmEthernetHistory15minMonStartDateTime": pmEthernetHistory15minMonStartDateTime,
       "pmEthernetHistory24HrStatsTable": pmEthernetHistory24HrStatsTable,
       "pmEthernetHistory24HrStatsEntry": pmEthernetHistory24HrStatsEntry,
       "pmEthernetHistory24HrMonType": pmEthernetHistory24HrMonType,
       "pmEthernetHistory24HrMonTypeDescr": pmEthernetHistory24HrMonTypeDescr,
       "pmEthernetHistory24HrIndexDescr": pmEthernetHistory24HrIndexDescr,
       "pmEthernetHistory24HrMonValue": pmEthernetHistory24HrMonValue,
       "pmEthernetHistory24HrMonIDF": pmEthernetHistory24HrMonIDF,
       "pmEthernetHistory24HrMonSupported": pmEthernetHistory24HrMonSupported,
       "pmEthernetHistory24HrAdminState": pmEthernetHistory24HrAdminState,
       "pmEthernetHistory24HrMonStartDateTime": pmEthernetHistory24HrMonStartDateTime,
       "pmModemCurrent15minStatsTable": pmModemCurrent15minStatsTable,
       "pmModemCurrent15minStatsEntry": pmModemCurrent15minStatsEntry,
       "pmModem15minMonType": pmModem15minMonType,
       "pmModem15minMonTypeDescr": pmModem15minMonTypeDescr,
       "pmModem15minIfIndexDescr": pmModem15minIfIndexDescr,
       "pmModem15minMonValue": pmModem15minMonValue,
       "pmModem15minMonIDF": pmModem15minMonIDF,
       "pmModem15minMonSupported": pmModem15minMonSupported,
       "pmModem15minAdminState": pmModem15minAdminState,
       "pmModem15minMonStartDateTime": pmModem15minMonStartDateTime,
       "pmModemCurrent24HrStatsTable": pmModemCurrent24HrStatsTable,
       "pmModemCurrent24HrStatsEntry": pmModemCurrent24HrStatsEntry,
       "pmModem24HrMonType": pmModem24HrMonType,
       "pmModem24HrMonTypeDescr": pmModem24HrMonTypeDescr,
       "pmModem24HrIfIndexDescr": pmModem24HrIfIndexDescr,
       "pmModem24HrMonValue": pmModem24HrMonValue,
       "pmModem24HrMonIDF": pmModem24HrMonIDF,
       "pmModem24HrMonSupported": pmModem24HrMonSupported,
       "pmModem24HrAdminState": pmModem24HrAdminState,
       "pmModem24HrMonStartDateTime": pmModem24HrMonStartDateTime,
       "pmModemUntimedStatsTable": pmModemUntimedStatsTable,
       "pmModemUntimedStatsEntry": pmModemUntimedStatsEntry,
       "pmModemUntimedMonType": pmModemUntimedMonType,
       "pmModemUntimedMonTypeDescr": pmModemUntimedMonTypeDescr,
       "pmModemUntimedIfIndexDescr": pmModemUntimedIfIndexDescr,
       "pmModemUntimedMonValue": pmModemUntimedMonValue,
       "pmModemUntimedMonIDF": pmModemUntimedMonIDF,
       "pmModemUntimedMonSupported": pmModemUntimedMonSupported,
       "pmModemUntimedAdminState": pmModemUntimedAdminState,
       "pmModemUntimedMonStartDateTime": pmModemUntimedMonStartDateTime,
       "pmModemHistory15minStatsTable": pmModemHistory15minStatsTable,
       "pmModemHistory15minStatsEntry": pmModemHistory15minStatsEntry,
       "pmModemHistory15minBinIndex": pmModemHistory15minBinIndex,
       "pmModemHistory15minMonType": pmModemHistory15minMonType,
       "pmModemHistory15minMonTypeDescr": pmModemHistory15minMonTypeDescr,
       "pmModemHistory15minIfIndexDescr": pmModemHistory15minIfIndexDescr,
       "pmModemHistory15minMonValue": pmModemHistory15minMonValue,
       "pmModemHistory15minMonIDF": pmModemHistory15minMonIDF,
       "pmModemHistory15minMonSupported": pmModemHistory15minMonSupported,
       "pmModemHistory15minAdminState": pmModemHistory15minAdminState,
       "pmModemHistory15minMonStartDateTime": pmModemHistory15minMonStartDateTime,
       "pmModemHistory24HrStatsTable": pmModemHistory24HrStatsTable,
       "pmModemHistory24HrStatsEntry": pmModemHistory24HrStatsEntry,
       "pmModemHistory24HrMonType": pmModemHistory24HrMonType,
       "pmModemHistory24HrMonTypeDescr": pmModemHistory24HrMonTypeDescr,
       "pmModemHistory24HrIndexDescr": pmModemHistory24HrIndexDescr,
       "pmModemHistory24HrMonValue": pmModemHistory24HrMonValue,
       "pmModemHistory24HrMonIDF": pmModemHistory24HrMonIDF,
       "pmModemHistory24HrMonSupported": pmModemHistory24HrMonSupported,
       "pmModemHistory24HrAdminState": pmModemHistory24HrAdminState,
       "pmModemHistory24HrMonStartDateTime": pmModemHistory24HrMonStartDateTime,
       "pmOtuCurrent15minStatsTable": pmOtuCurrent15minStatsTable,
       "pmOtuCurrent15minStatsEntry": pmOtuCurrent15minStatsEntry,
       "pmOtu15minMonType": pmOtu15minMonType,
       "pmOtu15minMonTypeDescr": pmOtu15minMonTypeDescr,
       "pmOtu15minIfIndexDescr": pmOtu15minIfIndexDescr,
       "pmOtu15minMonValue": pmOtu15minMonValue,
       "pmOtu15minMonIDF": pmOtu15minMonIDF,
       "pmOtu15minMonSupported": pmOtu15minMonSupported,
       "pmOtu15minAdminState": pmOtu15minAdminState,
       "pmOtu15minMonStartDateTime": pmOtu15minMonStartDateTime,
       "pmOtuCurrent24HrStatsTable": pmOtuCurrent24HrStatsTable,
       "pmOtuCurrent24HrStatsEntry": pmOtuCurrent24HrStatsEntry,
       "pmOtu24HrMonType": pmOtu24HrMonType,
       "pmOtu24HrMonTypeDescr": pmOtu24HrMonTypeDescr,
       "pmOtu24HrIfIndexDescr": pmOtu24HrIfIndexDescr,
       "pmOtu24HrMonValue": pmOtu24HrMonValue,
       "pmOtu24HrMonIDF": pmOtu24HrMonIDF,
       "pmOtu24HrMonSupported": pmOtu24HrMonSupported,
       "pmOtu24HrAdminState": pmOtu24HrAdminState,
       "pmOtu24HrMonStartDateTime": pmOtu24HrMonStartDateTime,
       "pmOtuUntimedStatsTable": pmOtuUntimedStatsTable,
       "pmOtuUntimedStatsEntry": pmOtuUntimedStatsEntry,
       "pmOtuUntimedMonType": pmOtuUntimedMonType,
       "pmOtuUntimedMonTypeDescr": pmOtuUntimedMonTypeDescr,
       "pmOtuUntimedIfIndexDescr": pmOtuUntimedIfIndexDescr,
       "pmOtuUntimedMonValue": pmOtuUntimedMonValue,
       "pmOtuUntimedMonIDF": pmOtuUntimedMonIDF,
       "pmOtuUntimedMonSupported": pmOtuUntimedMonSupported,
       "pmOtuUntimedAdminState": pmOtuUntimedAdminState,
       "pmOtuUntimedMonStartDateTime": pmOtuUntimedMonStartDateTime,
       "pmOtuHistory15minStatsTable": pmOtuHistory15minStatsTable,
       "pmOtuHistory15minStatsEntry": pmOtuHistory15minStatsEntry,
       "pmOtuHistory15minBinIndex": pmOtuHistory15minBinIndex,
       "pmOtuHistory15minMonType": pmOtuHistory15minMonType,
       "pmOtuHistory15minMonTypeDescr": pmOtuHistory15minMonTypeDescr,
       "pmOtuHistory15minIndexDescr": pmOtuHistory15minIndexDescr,
       "pmOtuHistory15minMonValue": pmOtuHistory15minMonValue,
       "pmOtuHistory15minMonIDF": pmOtuHistory15minMonIDF,
       "pmOtuHistory15minMonSupported": pmOtuHistory15minMonSupported,
       "pmOtuHistory15minAdminState": pmOtuHistory15minAdminState,
       "pmOtuHistory15minMonStartDateTime": pmOtuHistory15minMonStartDateTime,
       "pmOtuHistory24HrStatsTable": pmOtuHistory24HrStatsTable,
       "pmOtuHistory24HrStatsEntry": pmOtuHistory24HrStatsEntry,
       "pmOtuHistory24HrMonType": pmOtuHistory24HrMonType,
       "pmOtuHistory24HrMonTypeDescr": pmOtuHistory24HrMonTypeDescr,
       "pmOtuHistory24HrIndexDescr": pmOtuHistory24HrIndexDescr,
       "pmOtuHistory24HrMonValue": pmOtuHistory24HrMonValue,
       "pmOtuHistory24HrMonIDF": pmOtuHistory24HrMonIDF,
       "pmOtuHistory24HrMonSupported": pmOtuHistory24HrMonSupported,
       "pmOtuHistory24HrAdminState": pmOtuHistory24HrAdminState,
       "pmOtuHistory24HrMonStartDateTime": pmOtuHistory24HrMonStartDateTime,
       "pmOduCurrent15minStatsTable": pmOduCurrent15minStatsTable,
       "pmOduCurrent15minStatsEntry": pmOduCurrent15minStatsEntry,
       "pmOdu15minMonType": pmOdu15minMonType,
       "pmOdu15minMonTypeDescr": pmOdu15minMonTypeDescr,
       "pmOdu15minIfIndexDescr": pmOdu15minIfIndexDescr,
       "pmOdu15minMonValue": pmOdu15minMonValue,
       "pmOdu15minMonIDF": pmOdu15minMonIDF,
       "pmOdu15minMonSupported": pmOdu15minMonSupported,
       "pmOdu15minAdminState": pmOdu15minAdminState,
       "pmOdu15minMonStartDateTime": pmOdu15minMonStartDateTime,
       "pmOduCurrent24HrStatsTable": pmOduCurrent24HrStatsTable,
       "pmOduCurrent24HrStatsEntry": pmOduCurrent24HrStatsEntry,
       "pmOdu24HrMonType": pmOdu24HrMonType,
       "pmOdu24HrMonTypeDescr": pmOdu24HrMonTypeDescr,
       "pmOdu24HrIfIndexDescr": pmOdu24HrIfIndexDescr,
       "pmOdu24HrMonValue": pmOdu24HrMonValue,
       "pmOdu24HrMonIDF": pmOdu24HrMonIDF,
       "pmOdu24HrMonSupported": pmOdu24HrMonSupported,
       "pmOdu24HrAdminState": pmOdu24HrAdminState,
       "pmOdu24HrMonStartDateTime": pmOdu24HrMonStartDateTime,
       "pmOduUntimedStatsTable": pmOduUntimedStatsTable,
       "pmOduUntimedStatsEntry": pmOduUntimedStatsEntry,
       "pmOduUntimedMonType": pmOduUntimedMonType,
       "pmOduUntimedMonTypeDescr": pmOduUntimedMonTypeDescr,
       "pmOduUntimedIfIndexDescr": pmOduUntimedIfIndexDescr,
       "pmOduUntimedMonValue": pmOduUntimedMonValue,
       "pmOduUntimedMonIDF": pmOduUntimedMonIDF,
       "pmOduUntimedMonSupported": pmOduUntimedMonSupported,
       "pmOduUntimedAdminState": pmOduUntimedAdminState,
       "pmOduUntimedMonStartDateTime": pmOduUntimedMonStartDateTime,
       "pmOduHistory15minStatsTable": pmOduHistory15minStatsTable,
       "pmOduHistory15minStatsEntry": pmOduHistory15minStatsEntry,
       "pmOduHistory15minBinIndex": pmOduHistory15minBinIndex,
       "pmOduHistory15minMonType": pmOduHistory15minMonType,
       "pmOduHistory15minMonTypeDescr": pmOduHistory15minMonTypeDescr,
       "pmOduHistory15minIndexDescr": pmOduHistory15minIndexDescr,
       "pmOduHistory15minMonValue": pmOduHistory15minMonValue,
       "pmOduHistory15minMonIDF": pmOduHistory15minMonIDF,
       "pmOduHistory15minMonSupported": pmOduHistory15minMonSupported,
       "pmOduHistory15minAdminState": pmOduHistory15minAdminState,
       "pmOduHistory15minMonStartDateTime": pmOduHistory15minMonStartDateTime,
       "pmOduHistory24HrStatsTable": pmOduHistory24HrStatsTable,
       "pmOduHistory24HrStatsEntry": pmOduHistory24HrStatsEntry,
       "pmOduHistory24HrMonType": pmOduHistory24HrMonType,
       "pmOduHistory24HrMonTypeDescr": pmOduHistory24HrMonTypeDescr,
       "pmOduHistory24HrIndexDescr": pmOduHistory24HrIndexDescr,
       "pmOduHistory24HrMonValue": pmOduHistory24HrMonValue,
       "pmOduHistory24HrMonIDF": pmOduHistory24HrMonIDF,
       "pmOduHistory24HrMonSupported": pmOduHistory24HrMonSupported,
       "pmOduHistory24HrAdminState": pmOduHistory24HrAdminState,
       "pmOduHistory24HrMonStartDateTime": pmOduHistory24HrMonStartDateTime,
       "pmOpticalPowerCurrent15minStatsTable": pmOpticalPowerCurrent15minStatsTable,
       "pmOpticalPowerCurrent15minStatsEntry": pmOpticalPowerCurrent15minStatsEntry,
       "pmOpticalPower15minLaneIndex": pmOpticalPower15minLaneIndex,
       "pmOpticalPower15minMonType": pmOpticalPower15minMonType,
       "pmOpticalPower15minMonTypeDescr": pmOpticalPower15minMonTypeDescr,
       "pmOpticalPower15minIfIndexDescr": pmOpticalPower15minIfIndexDescr,
       "pmOpticalPower15minMonValue": pmOpticalPower15minMonValue,
       "pmOpticalPower15minMonIDF": pmOpticalPower15minMonIDF,
       "pmOpticalPower15minMonSupported": pmOpticalPower15minMonSupported,
       "pmOpticalPower15minAdminState": pmOpticalPower15minAdminState,
       "pmOpticalPower15minMonStartDateTime": pmOpticalPower15minMonStartDateTime,
       "pmOpticalPowerCurrent24HrStatsTable": pmOpticalPowerCurrent24HrStatsTable,
       "pmOpticalPowerCurrent24HrStatsEntry": pmOpticalPowerCurrent24HrStatsEntry,
       "pmOpticalPower24HrLaneIndex": pmOpticalPower24HrLaneIndex,
       "pmOpticalPower24HrMonType": pmOpticalPower24HrMonType,
       "pmOpticalPower24HrMonTypeDescr": pmOpticalPower24HrMonTypeDescr,
       "pmOpticalPower24HrIfIndexDescr": pmOpticalPower24HrIfIndexDescr,
       "pmOpticalPower24HrMonValue": pmOpticalPower24HrMonValue,
       "pmOpticalPower24HrMonIDF": pmOpticalPower24HrMonIDF,
       "pmOpticalPower24HrMonSupported": pmOpticalPower24HrMonSupported,
       "pmOpticalPower24HrAdminState": pmOpticalPower24HrAdminState,
       "pmOpticalPower24HrMonStartDateTime": pmOpticalPower24HrMonStartDateTime,
       "pmOpticalPowerUntimedStatsTable": pmOpticalPowerUntimedStatsTable,
       "pmOpticalPowerUntimedStatsEntry": pmOpticalPowerUntimedStatsEntry,
       "pmOpticalPowerUntimedLaneIndex": pmOpticalPowerUntimedLaneIndex,
       "pmOpticalPowerUntimedMonType": pmOpticalPowerUntimedMonType,
       "pmOpticalPowerUntimedMonTypeDescr": pmOpticalPowerUntimedMonTypeDescr,
       "pmOpticalPowerUntimedIfIndexDescr": pmOpticalPowerUntimedIfIndexDescr,
       "pmOpticalPowerUntimedMonValue": pmOpticalPowerUntimedMonValue,
       "pmOpticalPowerUntimedMonIDF": pmOpticalPowerUntimedMonIDF,
       "pmOpticalPowerUntimedMonSupported": pmOpticalPowerUntimedMonSupported,
       "pmOpticalPowerUntimedAdminState": pmOpticalPowerUntimedAdminState,
       "pmOpticalPowerUntimedMonStartDateTime": pmOpticalPowerUntimedMonStartDateTime,
       "pmOpticalPowerHistory15minStatsTable": pmOpticalPowerHistory15minStatsTable,
       "pmOpticalPowerHistory15minStatsEntry": pmOpticalPowerHistory15minStatsEntry,
       "pmOpticalPowerHistory15minBinIndex": pmOpticalPowerHistory15minBinIndex,
       "pmOpticalPowerHistory15minLaneIndex": pmOpticalPowerHistory15minLaneIndex,
       "pmOpticalPowerHistory15minMonType": pmOpticalPowerHistory15minMonType,
       "pmOpticalPowerHistory15minMonTypeDescr": pmOpticalPowerHistory15minMonTypeDescr,
       "pmOpticalPowerHistory15minIndexDescr": pmOpticalPowerHistory15minIndexDescr,
       "pmOpticalPowerHistory15minMonValue": pmOpticalPowerHistory15minMonValue,
       "pmOpticalPowerHistory15minMonIDF": pmOpticalPowerHistory15minMonIDF,
       "pmOpticalPowerHistory15minMonSupported": pmOpticalPowerHistory15minMonSupported,
       "pmOpticalPowerHistory15minAdminState": pmOpticalPowerHistory15minAdminState,
       "pmOpticalPowerHistory15minMonStartDateTime": pmOpticalPowerHistory15minMonStartDateTime,
       "pmOpticalPowerHistory24HrStatsTable": pmOpticalPowerHistory24HrStatsTable,
       "pmOpticalPowerHistory24HrStatsEntry": pmOpticalPowerHistory24HrStatsEntry,
       "pmOpticalPowerHistory24HrLaneIndex": pmOpticalPowerHistory24HrLaneIndex,
       "pmOpticalPowerHistory24HrMonType": pmOpticalPowerHistory24HrMonType,
       "pmOpticalPowerHistory24HrMonTypeDescr": pmOpticalPowerHistory24HrMonTypeDescr,
       "pmOpticalPowerHistory24HrIndexDescr": pmOpticalPowerHistory24HrIndexDescr,
       "pmOpticalPowerHistory24HrMonValue": pmOpticalPowerHistory24HrMonValue,
       "pmOpticalPowerHistory24HrMonIDF": pmOpticalPowerHistory24HrMonIDF,
       "pmOpticalPowerHistory24HrMonSupported": pmOpticalPowerHistory24HrMonSupported,
       "pmOpticalPowerHistory24HrAdminState": pmOpticalPowerHistory24HrAdminState,
       "pmOpticalPowerHistory24HrMonStartDateTime": pmOpticalPowerHistory24HrMonStartDateTime,
       "pmGcmCurrent15minStatsTable": pmGcmCurrent15minStatsTable,
       "pmGcmCurrent15minStatsEntry": pmGcmCurrent15minStatsEntry,
       "pmGcm15minMonType": pmGcm15minMonType,
       "pmGcm15minMonTypeDescr": pmGcm15minMonTypeDescr,
       "pmGcm15minIfIndexDescr": pmGcm15minIfIndexDescr,
       "pmGcm15minMonValue": pmGcm15minMonValue,
       "pmGcm15minMonIDF": pmGcm15minMonIDF,
       "pmGcm15minMonSupported": pmGcm15minMonSupported,
       "pmGcm15minAdminState": pmGcm15minAdminState,
       "pmGcm15minMonStartDateTime": pmGcm15minMonStartDateTime,
       "pmGcmCurrent24HrStatsTable": pmGcmCurrent24HrStatsTable,
       "pmGcmCurrent24HrStatsEntry": pmGcmCurrent24HrStatsEntry,
       "pmGcm24HrMonType": pmGcm24HrMonType,
       "pmGcm24HrMonTypeDescr": pmGcm24HrMonTypeDescr,
       "pmGcm24HrIfIndexDescr": pmGcm24HrIfIndexDescr,
       "pmGcm24HrMonValue": pmGcm24HrMonValue,
       "pmGcm24HrMonIDF": pmGcm24HrMonIDF,
       "pmGcm24HrMonSupported": pmGcm24HrMonSupported,
       "pmGcm24HrAdminState": pmGcm24HrAdminState,
       "pmGcm24HrMonStartDateTime": pmGcm24HrMonStartDateTime,
       "pmGcmUntimedStatsTable": pmGcmUntimedStatsTable,
       "pmGcmUntimedStatsEntry": pmGcmUntimedStatsEntry,
       "pmGcmUntimedMonType": pmGcmUntimedMonType,
       "pmGcmUntimedMonTypeDescr": pmGcmUntimedMonTypeDescr,
       "pmGcmUntimedIfIndexDescr": pmGcmUntimedIfIndexDescr,
       "pmGcmUntimedMonValue": pmGcmUntimedMonValue,
       "pmGcmUntimedMonIDF": pmGcmUntimedMonIDF,
       "pmGcmUntimedMonSupported": pmGcmUntimedMonSupported,
       "pmGcmUntimedAdminState": pmGcmUntimedAdminState,
       "pmGcmUntimedMonStartDateTime": pmGcmUntimedMonStartDateTime,
       "pmGcmHistory15minStatsTable": pmGcmHistory15minStatsTable,
       "pmGcmHistory15minStatsEntry": pmGcmHistory15minStatsEntry,
       "pmGcmHistory15minBinIndex": pmGcmHistory15minBinIndex,
       "pmGcmHistory15minMonType": pmGcmHistory15minMonType,
       "pmGcmHistory15minMonTypeDescr": pmGcmHistory15minMonTypeDescr,
       "pmGcmHistory15minIndexDescr": pmGcmHistory15minIndexDescr,
       "pmGcmHistory15minMonValue": pmGcmHistory15minMonValue,
       "pmGcmHistory15minMonIDF": pmGcmHistory15minMonIDF,
       "pmGcmHistory15minMonSupported": pmGcmHistory15minMonSupported,
       "pmGcmHistory15minAdminState": pmGcmHistory15minAdminState,
       "pmGcmHistory15minMonStartDateTime": pmGcmHistory15minMonStartDateTime,
       "pmGcmHistory24HrStatsTable": pmGcmHistory24HrStatsTable,
       "pmGcmHistory24HrStatsEntry": pmGcmHistory24HrStatsEntry,
       "pmGcmHistory24HrMonType": pmGcmHistory24HrMonType,
       "pmGcmHistory24HrMonTypeDescr": pmGcmHistory24HrMonTypeDescr,
       "pmGcmHistory24HrIndexDescr": pmGcmHistory24HrIndexDescr,
       "pmGcmHistory24HrMonValue": pmGcmHistory24HrMonValue,
       "pmGcmHistory24HrMonIDF": pmGcmHistory24HrMonIDF,
       "pmGcmHistory24HrMonSupported": pmGcmHistory24HrMonSupported,
       "pmGcmHistory24HrAdminState": pmGcmHistory24HrAdminState,
       "pmGcmHistory24HrMonStartDateTime": pmGcmHistory24HrMonStartDateTime,
       "pmPhotonicsCurrent15minStatsTable": pmPhotonicsCurrent15minStatsTable,
       "pmPhotonicsCurrent15minStatsEntry": pmPhotonicsCurrent15minStatsEntry,
       "pmPhotonics15minMonType": pmPhotonics15minMonType,
       "pmPhotonics15minMonTypeDescr": pmPhotonics15minMonTypeDescr,
       "pmPhotonics15minIfIndexDescr": pmPhotonics15minIfIndexDescr,
       "pmPhotonics15minMonValue": pmPhotonics15minMonValue,
       "pmPhotonics15minMonIDF": pmPhotonics15minMonIDF,
       "pmPhotonics15minMonSupported": pmPhotonics15minMonSupported,
       "pmPhotonics15minAdminState": pmPhotonics15minAdminState,
       "pmPhotonics15minMonStartDateTime": pmPhotonics15minMonStartDateTime,
       "pmPhotonicsCurrent24HrStatsTable": pmPhotonicsCurrent24HrStatsTable,
       "pmPhotonicsCurrent24HrStatsEntry": pmPhotonicsCurrent24HrStatsEntry,
       "pmPhotonics24HrMonType": pmPhotonics24HrMonType,
       "pmPhotonics24HrMonTypeDescr": pmPhotonics24HrMonTypeDescr,
       "pmPhotonics24HrIfIndexDescr": pmPhotonics24HrIfIndexDescr,
       "pmPhotonics24HrMonValue": pmPhotonics24HrMonValue,
       "pmPhotonics24HrMonIDF": pmPhotonics24HrMonIDF,
       "pmPhotonics24HrMonSupported": pmPhotonics24HrMonSupported,
       "pmPhotonics24HrAdminState": pmPhotonics24HrAdminState,
       "pmPhotonics24HrMonStartDateTime": pmPhotonics24HrMonStartDateTime,
       "pmPhotonicsUntimedStatsTable": pmPhotonicsUntimedStatsTable,
       "pmPhotonicsUntimedStatsEntry": pmPhotonicsUntimedStatsEntry,
       "pmPhotonicsUntimedMonType": pmPhotonicsUntimedMonType,
       "pmPhotonicsUntimedMonTypeDescr": pmPhotonicsUntimedMonTypeDescr,
       "pmPhotonicsUntimedIfIndexDescr": pmPhotonicsUntimedIfIndexDescr,
       "pmPhotonicsUntimedMonValue": pmPhotonicsUntimedMonValue,
       "pmPhotonicsUntimedMonIDF": pmPhotonicsUntimedMonIDF,
       "pmPhotonicsUntimedMonSupported": pmPhotonicsUntimedMonSupported,
       "pmPhotonicsUntimedAdminState": pmPhotonicsUntimedAdminState,
       "pmPhotonicsUntimedMonStartDateTime": pmPhotonicsUntimedMonStartDateTime,
       "pmPhotonicsHistory15minStatsTable": pmPhotonicsHistory15minStatsTable,
       "pmPhotonicsHistory15minStatsEntry": pmPhotonicsHistory15minStatsEntry,
       "pmPhotonicsHistory15minBinIndex": pmPhotonicsHistory15minBinIndex,
       "pmPhotonicsHistory15minMonType": pmPhotonicsHistory15minMonType,
       "pmPhotonicsHistory15minMonTypeDescr": pmPhotonicsHistory15minMonTypeDescr,
       "pmPhotonicsHistory15minIndexDescr": pmPhotonicsHistory15minIndexDescr,
       "pmPhotonicsHistory15minMonValue": pmPhotonicsHistory15minMonValue,
       "pmPhotonicsHistory15minMonIDF": pmPhotonicsHistory15minMonIDF,
       "pmPhotonicsHistory15minMonSupported": pmPhotonicsHistory15minMonSupported,
       "pmPhotonicsHistory15minAdminState": pmPhotonicsHistory15minAdminState,
       "pmPhotonicsHistory15minMonStartDateTime": pmPhotonicsHistory15minMonStartDateTime,
       "pmPhotonicsHistory24HrStatsTable": pmPhotonicsHistory24HrStatsTable,
       "pmPhotonicsHistory24HrStatsEntry": pmPhotonicsHistory24HrStatsEntry,
       "pmPhotonicsHistory24HrMonType": pmPhotonicsHistory24HrMonType,
       "pmPhotonicsHistory24HrMonTypeDescr": pmPhotonicsHistory24HrMonTypeDescr,
       "pmPhotonicsHistory24HrIndexDescr": pmPhotonicsHistory24HrIndexDescr,
       "pmPhotonicsHistory24HrMonValue": pmPhotonicsHistory24HrMonValue,
       "pmPhotonicsHistory24HrMonIDF": pmPhotonicsHistory24HrMonIDF,
       "pmPhotonicsHistory24HrMonSupported": pmPhotonicsHistory24HrMonSupported,
       "pmPhotonicsHistory24HrAdminState": pmPhotonicsHistory24HrAdminState,
       "pmPhotonicsHistory24HrMonStartDateTime": pmPhotonicsHistory24HrMonStartDateTime}
)
