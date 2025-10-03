# SNMP MIB module (JUNIPER-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-TWAMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:58 2025
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

(pingCtlOwnerIndex,
 pingCtlTestName,
 pingProbeHistoryIndex) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlOwnerIndex",
    "pingCtlTestName",
    "pingProbeHistoryIndex")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(jnxTwampMibRoot,
 jnxTwampNotificationPrefix) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxTwampMibRoot",
    "jnxTwampNotificationPrefix")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxTwampMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1)
)
if mibBuilder.loadTexts:
    jnxTwampMib.setRevisions(
        ("2014-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxTwampClientCollectionType(TextualConvention, Integer32):
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
        *(("currentTest", 1),
          ("lastCompletedTest", 2),
          ("movingAverage", 3),
          ("allTests", 4))
    )



class JnxTwampClientMeasurementType(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("roundTripTime", 1),
          ("rttJitter", 2),
          ("rttInterarrivalJitter", 3),
          ("egress", 4),
          ("egressJitter", 5),
          ("egressInterarrivalJitter", 6),
          ("ingress", 7),
          ("ingressJitter", 8),
          ("ingressInterarrivalJitter", 9))
    )



class JnxTwampClientMeasurementSet(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("roundTripTime", 1),
          ("posRttJitter", 2),
          ("negRttJitter", 3),
          ("egress", 4),
          ("posEgressJitter", 5),
          ("negEgressJitter", 6),
          ("ingress", 7),
          ("posIngressJitter", 8),
          ("negIngressJitter", 9))
    )



class JnxTwampPercentType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-6"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



# MIB Managed Objects in the order of their OIDs

_JnxTwampClientNode_ObjectIdentity = ObjectIdentity
jnxTwampClientNode = _JnxTwampClientNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1)
)
if mibBuilder.loadTexts:
    jnxTwampClientNode.setStatus("current")
_JnxTwampClientResultsSampleTable_Object = MibTable
jnxTwampClientResultsSampleTable = _JnxTwampClientResultsSampleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxTwampClientResultsSampleTable.setStatus("current")
_JnxTwampClientResultsSampleEntry_Object = MibTableRow
jnxTwampClientResultsSampleEntry = _JnxTwampClientResultsSampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 1, 1)
)
jnxTwampClientResultsSampleEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampResSampleType"),
)
if mibBuilder.loadTexts:
    jnxTwampClientResultsSampleEntry.setStatus("current")
_JnxTwampResSampleType_Type = JnxTwampClientMeasurementType
_JnxTwampResSampleType_Object = MibTableColumn
jnxTwampResSampleType = _JnxTwampResSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 1, 1, 1),
    _JnxTwampResSampleType_Type()
)
jnxTwampResSampleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTwampResSampleType.setStatus("current")
_JnxTwampResSampleValue_Type = Integer32
_JnxTwampResSampleValue_Object = MibTableColumn
jnxTwampResSampleValue = _JnxTwampResSampleValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 1, 1, 2),
    _JnxTwampResSampleValue_Type()
)
jnxTwampResSampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResSampleValue.setStatus("current")
_JnxTwampResSampleDate_Type = DateAndTime
_JnxTwampResSampleDate_Object = MibTableColumn
jnxTwampResSampleDate = _JnxTwampResSampleDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 1, 1, 3),
    _JnxTwampResSampleDate_Type()
)
jnxTwampResSampleDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResSampleDate.setStatus("current")
_JnxTwampClientResultsSummaryTable_Object = MibTable
jnxTwampClientResultsSummaryTable = _JnxTwampClientResultsSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxTwampClientResultsSummaryTable.setStatus("current")
_JnxTwampClientResultsSummaryEntry_Object = MibTableRow
jnxTwampClientResultsSummaryEntry = _JnxTwampClientResultsSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 2, 1)
)
jnxTwampClientResultsSummaryEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampResSumCollection"),
)
if mibBuilder.loadTexts:
    jnxTwampClientResultsSummaryEntry.setStatus("current")
_JnxTwampResSumCollection_Type = JnxTwampClientCollectionType
_JnxTwampResSumCollection_Object = MibTableColumn
jnxTwampResSumCollection = _JnxTwampResSumCollection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 2, 1, 1),
    _JnxTwampResSumCollection_Type()
)
jnxTwampResSumCollection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTwampResSumCollection.setStatus("current")
_JnxTwampResSumSent_Type = Unsigned32
_JnxTwampResSumSent_Object = MibTableColumn
jnxTwampResSumSent = _JnxTwampResSumSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 2, 1, 2),
    _JnxTwampResSumSent_Type()
)
jnxTwampResSumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResSumSent.setStatus("current")
_JnxTwampResSumReceived_Type = Unsigned32
_JnxTwampResSumReceived_Object = MibTableColumn
jnxTwampResSumReceived = _JnxTwampResSumReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 2, 1, 3),
    _JnxTwampResSumReceived_Type()
)
jnxTwampResSumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResSumReceived.setStatus("current")
_JnxTwampResSumPercentLost_Type = JnxTwampPercentType
_JnxTwampResSumPercentLost_Object = MibTableColumn
jnxTwampResSumPercentLost = _JnxTwampResSumPercentLost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 2, 1, 4),
    _JnxTwampResSumPercentLost_Type()
)
jnxTwampResSumPercentLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResSumPercentLost.setStatus("current")
_JnxTwampResSumDate_Type = DateAndTime
_JnxTwampResSumDate_Object = MibTableColumn
jnxTwampResSumDate = _JnxTwampResSumDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 2, 1, 5),
    _JnxTwampResSumDate_Type()
)
jnxTwampResSumDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResSumDate.setStatus("current")
_JnxTwampClientResultsCalculatedTable_Object = MibTable
jnxTwampClientResultsCalculatedTable = _JnxTwampClientResultsCalculatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxTwampClientResultsCalculatedTable.setStatus("current")
_JnxTwampClientResultsCalculatedEntry_Object = MibTableRow
jnxTwampClientResultsCalculatedEntry = _JnxTwampClientResultsCalculatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1)
)
jnxTwampClientResultsCalculatedEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampResSumCollection"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampResCalcSet"),
)
if mibBuilder.loadTexts:
    jnxTwampClientResultsCalculatedEntry.setStatus("current")
_JnxTwampResCalcSet_Type = JnxTwampClientMeasurementSet
_JnxTwampResCalcSet_Object = MibTableColumn
jnxTwampResCalcSet = _JnxTwampResCalcSet_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1, 1),
    _JnxTwampResCalcSet_Type()
)
jnxTwampResCalcSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTwampResCalcSet.setStatus("current")
_JnxTwampResCalcSamples_Type = Unsigned32
_JnxTwampResCalcSamples_Object = MibTableColumn
jnxTwampResCalcSamples = _JnxTwampResCalcSamples_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1, 2),
    _JnxTwampResCalcSamples_Type()
)
jnxTwampResCalcSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResCalcSamples.setStatus("current")
_JnxTwampResCalcMin_Type = Unsigned32
_JnxTwampResCalcMin_Object = MibTableColumn
jnxTwampResCalcMin = _JnxTwampResCalcMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1, 3),
    _JnxTwampResCalcMin_Type()
)
jnxTwampResCalcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResCalcMin.setStatus("current")
_JnxTwampResCalcMax_Type = Unsigned32
_JnxTwampResCalcMax_Object = MibTableColumn
jnxTwampResCalcMax = _JnxTwampResCalcMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1, 4),
    _JnxTwampResCalcMax_Type()
)
jnxTwampResCalcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResCalcMax.setStatus("current")
_JnxTwampResCalcAverage_Type = Unsigned32
_JnxTwampResCalcAverage_Object = MibTableColumn
jnxTwampResCalcAverage = _JnxTwampResCalcAverage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1, 5),
    _JnxTwampResCalcAverage_Type()
)
jnxTwampResCalcAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResCalcAverage.setStatus("current")
_JnxTwampResCalcPkToPk_Type = Unsigned32
_JnxTwampResCalcPkToPk_Object = MibTableColumn
jnxTwampResCalcPkToPk = _JnxTwampResCalcPkToPk_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1, 6),
    _JnxTwampResCalcPkToPk_Type()
)
jnxTwampResCalcPkToPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResCalcPkToPk.setStatus("current")
_JnxTwampResCalcStdDev_Type = Unsigned32
_JnxTwampResCalcStdDev_Object = MibTableColumn
jnxTwampResCalcStdDev = _JnxTwampResCalcStdDev_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1, 7),
    _JnxTwampResCalcStdDev_Type()
)
jnxTwampResCalcStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResCalcStdDev.setStatus("current")
_JnxTwampResCalcSum_Type = CounterBasedGauge64
_JnxTwampResCalcSum_Object = MibTableColumn
jnxTwampResCalcSum = _JnxTwampResCalcSum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 3, 1, 8),
    _JnxTwampResCalcSum_Type()
)
jnxTwampResCalcSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampResCalcSum.setStatus("current")
_JnxTwampClientHistorySampleTable_Object = MibTable
jnxTwampClientHistorySampleTable = _JnxTwampClientHistorySampleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxTwampClientHistorySampleTable.setStatus("current")
_JnxTwampClientHistorySampleEntry_Object = MibTableRow
jnxTwampClientHistorySampleEntry = _JnxTwampClientHistorySampleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 4, 1)
)
jnxTwampClientHistorySampleEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "DISMAN-PING-MIB", "pingProbeHistoryIndex"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampHistSampleType"),
)
if mibBuilder.loadTexts:
    jnxTwampClientHistorySampleEntry.setStatus("current")
_JnxTwampHistSampleType_Type = JnxTwampClientMeasurementType
_JnxTwampHistSampleType_Object = MibTableColumn
jnxTwampHistSampleType = _JnxTwampHistSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 4, 1, 1),
    _JnxTwampHistSampleType_Type()
)
jnxTwampHistSampleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTwampHistSampleType.setStatus("current")
_JnxTwampHistSampleValue_Type = Integer32
_JnxTwampHistSampleValue_Object = MibTableColumn
jnxTwampHistSampleValue = _JnxTwampHistSampleValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 4, 1, 2),
    _JnxTwampHistSampleValue_Type()
)
jnxTwampHistSampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistSampleValue.setStatus("current")
_JnxTwampClientHistorySummaryTable_Object = MibTable
jnxTwampClientHistorySummaryTable = _JnxTwampClientHistorySummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxTwampClientHistorySummaryTable.setStatus("current")
_JnxTwampClientHistorySummaryEntry_Object = MibTableRow
jnxTwampClientHistorySummaryEntry = _JnxTwampClientHistorySummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 5, 1)
)
jnxTwampClientHistorySummaryEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "DISMAN-PING-MIB", "pingProbeHistoryIndex"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampHistSumCollection"),
)
if mibBuilder.loadTexts:
    jnxTwampClientHistorySummaryEntry.setStatus("current")
_JnxTwampHistSumCollection_Type = JnxTwampClientCollectionType
_JnxTwampHistSumCollection_Object = MibTableColumn
jnxTwampHistSumCollection = _JnxTwampHistSumCollection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 5, 1, 1),
    _JnxTwampHistSumCollection_Type()
)
jnxTwampHistSumCollection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTwampHistSumCollection.setStatus("current")
_JnxTwampHistSumSent_Type = Unsigned32
_JnxTwampHistSumSent_Object = MibTableColumn
jnxTwampHistSumSent = _JnxTwampHistSumSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 5, 1, 2),
    _JnxTwampHistSumSent_Type()
)
jnxTwampHistSumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistSumSent.setStatus("current")
_JnxTwampHistSumReceived_Type = Unsigned32
_JnxTwampHistSumReceived_Object = MibTableColumn
jnxTwampHistSumReceived = _JnxTwampHistSumReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 5, 1, 3),
    _JnxTwampHistSumReceived_Type()
)
jnxTwampHistSumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistSumReceived.setStatus("current")
_JnxTwampHistSumPercentLost_Type = JnxTwampPercentType
_JnxTwampHistSumPercentLost_Object = MibTableColumn
jnxTwampHistSumPercentLost = _JnxTwampHistSumPercentLost_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 5, 1, 4),
    _JnxTwampHistSumPercentLost_Type()
)
jnxTwampHistSumPercentLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistSumPercentLost.setStatus("current")
_JnxTwampClientHistoryCalculatedTable_Object = MibTable
jnxTwampClientHistoryCalculatedTable = _JnxTwampClientHistoryCalculatedTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6)
)
if mibBuilder.loadTexts:
    jnxTwampClientHistoryCalculatedTable.setStatus("current")
_JnxTwampClientHistoryCalculatedEntry_Object = MibTableRow
jnxTwampClientHistoryCalculatedEntry = _JnxTwampClientHistoryCalculatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1)
)
jnxTwampClientHistoryCalculatedEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
    (0, "DISMAN-PING-MIB", "pingProbeHistoryIndex"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampHistSumCollection"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampHistCalcSet"),
)
if mibBuilder.loadTexts:
    jnxTwampClientHistoryCalculatedEntry.setStatus("current")
_JnxTwampHistCalcSet_Type = JnxTwampClientMeasurementSet
_JnxTwampHistCalcSet_Object = MibTableColumn
jnxTwampHistCalcSet = _JnxTwampHistCalcSet_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1, 1),
    _JnxTwampHistCalcSet_Type()
)
jnxTwampHistCalcSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTwampHistCalcSet.setStatus("current")
_JnxTwampHistCalcSamples_Type = Unsigned32
_JnxTwampHistCalcSamples_Object = MibTableColumn
jnxTwampHistCalcSamples = _JnxTwampHistCalcSamples_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1, 2),
    _JnxTwampHistCalcSamples_Type()
)
jnxTwampHistCalcSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistCalcSamples.setStatus("current")
_JnxTwampHistCalcMin_Type = Unsigned32
_JnxTwampHistCalcMin_Object = MibTableColumn
jnxTwampHistCalcMin = _JnxTwampHistCalcMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1, 3),
    _JnxTwampHistCalcMin_Type()
)
jnxTwampHistCalcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistCalcMin.setStatus("current")
_JnxTwampHistCalcMax_Type = Unsigned32
_JnxTwampHistCalcMax_Object = MibTableColumn
jnxTwampHistCalcMax = _JnxTwampHistCalcMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1, 4),
    _JnxTwampHistCalcMax_Type()
)
jnxTwampHistCalcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistCalcMax.setStatus("current")
_JnxTwampHistCalcAverage_Type = Unsigned32
_JnxTwampHistCalcAverage_Object = MibTableColumn
jnxTwampHistCalcAverage = _JnxTwampHistCalcAverage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1, 5),
    _JnxTwampHistCalcAverage_Type()
)
jnxTwampHistCalcAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistCalcAverage.setStatus("current")
_JnxTwampHistCalcPkToPk_Type = Unsigned32
_JnxTwampHistCalcPkToPk_Object = MibTableColumn
jnxTwampHistCalcPkToPk = _JnxTwampHistCalcPkToPk_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1, 6),
    _JnxTwampHistCalcPkToPk_Type()
)
jnxTwampHistCalcPkToPk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistCalcPkToPk.setStatus("current")
_JnxTwampHistCalcStdDev_Type = Unsigned32
_JnxTwampHistCalcStdDev_Object = MibTableColumn
jnxTwampHistCalcStdDev = _JnxTwampHistCalcStdDev_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1, 7),
    _JnxTwampHistCalcStdDev_Type()
)
jnxTwampHistCalcStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistCalcStdDev.setStatus("current")
_JnxTwampHistCalcSum_Type = CounterBasedGauge64
_JnxTwampHistCalcSum_Object = MibTableColumn
jnxTwampHistCalcSum = _JnxTwampHistCalcSum_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 6, 1, 8),
    _JnxTwampHistCalcSum_Type()
)
jnxTwampHistCalcSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampHistCalcSum.setStatus("current")
_JnxTwampClientControlConnectionTable_Object = MibTable
jnxTwampClientControlConnectionTable = _JnxTwampClientControlConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7)
)
if mibBuilder.loadTexts:
    jnxTwampClientControlConnectionTable.setStatus("current")
_JnxTwampClientCCEntry_Object = MibTableRow
jnxTwampClientCCEntry = _JnxTwampClientCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1)
)
jnxTwampClientCCEntry.setIndexNames(
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampClientControlConnectionID"),
)
if mibBuilder.loadTexts:
    jnxTwampClientCCEntry.setStatus("current")


class _JnxTwampClientControlConnectionID_Type(SnmpAdminString):
    """Custom type jnxTwampClientControlConnectionID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxTwampClientControlConnectionID_Type.__name__ = "SnmpAdminString"
_JnxTwampClientControlConnectionID_Object = MibTableColumn
jnxTwampClientControlConnectionID = _JnxTwampClientControlConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1, 1),
    _JnxTwampClientControlConnectionID_Type()
)
jnxTwampClientControlConnectionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTwampClientControlConnectionID.setStatus("current")
_JnxTwampClientCCName_Type = DisplayString
_JnxTwampClientCCName_Object = MibTableColumn
jnxTwampClientCCName = _JnxTwampClientCCName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1, 2),
    _JnxTwampClientCCName_Type()
)
jnxTwampClientCCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientCCName.setStatus("current")


class _JnxTwampClientCCStatus_Type(Integer32):
    """Custom type jnxTwampClientCCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stopped", 2))
    )


_JnxTwampClientCCStatus_Type.__name__ = "Integer32"
_JnxTwampClientCCStatus_Object = MibTableColumn
jnxTwampClientCCStatus = _JnxTwampClientCCStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1, 3),
    _JnxTwampClientCCStatus_Type()
)
jnxTwampClientCCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientCCStatus.setStatus("current")
_JnxTwampClientServerAddress_Type = IpAddress
_JnxTwampClientServerAddress_Object = MibTableColumn
jnxTwampClientServerAddress = _JnxTwampClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1, 4),
    _JnxTwampClientServerAddress_Type()
)
jnxTwampClientServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientServerAddress.setStatus("current")


class _JnxTwampClientServerPort_Type(Integer32):
    """Custom type jnxTwampClientServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxTwampClientServerPort_Type.__name__ = "Integer32"
_JnxTwampClientServerPort_Object = MibTableColumn
jnxTwampClientServerPort = _JnxTwampClientServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1, 5),
    _JnxTwampClientServerPort_Type()
)
jnxTwampClientServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientServerPort.setStatus("current")


class _JnxTwampClientTSConfiguredCount_Type(Integer32):
    """Custom type jnxTwampClientTSConfiguredCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxTwampClientTSConfiguredCount_Type.__name__ = "Integer32"
_JnxTwampClientTSConfiguredCount_Object = MibTableColumn
jnxTwampClientTSConfiguredCount = _JnxTwampClientTSConfiguredCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1, 6),
    _JnxTwampClientTSConfiguredCount_Type()
)
jnxTwampClientTSConfiguredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientTSConfiguredCount.setStatus("current")


class _JnxTwampClientTSActiveCount_Type(Integer32):
    """Custom type jnxTwampClientTSActiveCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxTwampClientTSActiveCount_Type.__name__ = "Integer32"
_JnxTwampClientTSActiveCount_Object = MibTableColumn
jnxTwampClientTSActiveCount = _JnxTwampClientTSActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1, 7),
    _JnxTwampClientTSActiveCount_Type()
)
jnxTwampClientTSActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientTSActiveCount.setStatus("current")


class _JnxTwampClientAuthMode_Type(Integer32):
    """Custom type jnxTwampClientAuthMode based on Integer32"""
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
          ("authenticated", 2),
          ("encrypted", 3),
          ("controlOnlyEncrypted", 4))
    )


_JnxTwampClientAuthMode_Type.__name__ = "Integer32"
_JnxTwampClientAuthMode_Object = MibTableColumn
jnxTwampClientAuthMode = _JnxTwampClientAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 7, 1, 8),
    _JnxTwampClientAuthMode_Type()
)
jnxTwampClientAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientAuthMode.setStatus("current")
_JnxTwampClientTestSessionsTable_Object = MibTable
jnxTwampClientTestSessionsTable = _JnxTwampClientTestSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8)
)
if mibBuilder.loadTexts:
    jnxTwampClientTestSessionsTable.setStatus("current")
_JnxTwampClientTSEntry_Object = MibTableRow
jnxTwampClientTSEntry = _JnxTwampClientTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8, 1)
)
jnxTwampClientTSEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "JUNIPER-TWAMP-MIB", "jnxTwampClientTestSessionID"),
)
if mibBuilder.loadTexts:
    jnxTwampClientTSEntry.setStatus("current")


class _JnxTwampClientTestSessionID_Type(SnmpAdminString):
    """Custom type jnxTwampClientTestSessionID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxTwampClientTestSessionID_Type.__name__ = "SnmpAdminString"
_JnxTwampClientTestSessionID_Object = MibTableColumn
jnxTwampClientTestSessionID = _JnxTwampClientTestSessionID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8, 1, 1),
    _JnxTwampClientTestSessionID_Type()
)
jnxTwampClientTestSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxTwampClientTestSessionID.setStatus("current")
_JnxTwampClientTSName_Type = DisplayString
_JnxTwampClientTSName_Object = MibTableColumn
jnxTwampClientTSName = _JnxTwampClientTSName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8, 1, 2),
    _JnxTwampClientTSName_Type()
)
jnxTwampClientTSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientTSName.setStatus("current")


class _JnxTwampClientTSStatus_Type(Integer32):
    """Custom type jnxTwampClientTSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stopped", 2))
    )


_JnxTwampClientTSStatus_Type.__name__ = "Integer32"
_JnxTwampClientTSStatus_Object = MibTableColumn
jnxTwampClientTSStatus = _JnxTwampClientTSStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8, 1, 3),
    _JnxTwampClientTSStatus_Type()
)
jnxTwampClientTSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientTSStatus.setStatus("current")
_JnxTwampClientTSSenderAddress_Type = IpAddress
_JnxTwampClientTSSenderAddress_Object = MibTableColumn
jnxTwampClientTSSenderAddress = _JnxTwampClientTSSenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8, 1, 4),
    _JnxTwampClientTSSenderAddress_Type()
)
jnxTwampClientTSSenderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientTSSenderAddress.setStatus("current")


class _JnxTwampClientTSSenderPort_Type(Integer32):
    """Custom type jnxTwampClientTSSenderPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxTwampClientTSSenderPort_Type.__name__ = "Integer32"
_JnxTwampClientTSSenderPort_Object = MibTableColumn
jnxTwampClientTSSenderPort = _JnxTwampClientTSSenderPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8, 1, 5),
    _JnxTwampClientTSSenderPort_Type()
)
jnxTwampClientTSSenderPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientTSSenderPort.setStatus("current")
_JnxTwampClientTSReflectorAddress_Type = IpAddress
_JnxTwampClientTSReflectorAddress_Object = MibTableColumn
jnxTwampClientTSReflectorAddress = _JnxTwampClientTSReflectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8, 1, 6),
    _JnxTwampClientTSReflectorAddress_Type()
)
jnxTwampClientTSReflectorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientTSReflectorAddress.setStatus("current")


class _JnxTwampClientTSReflectorPort_Type(Integer32):
    """Custom type jnxTwampClientTSReflectorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxTwampClientTSReflectorPort_Type.__name__ = "Integer32"
_JnxTwampClientTSReflectorPort_Object = MibTableColumn
jnxTwampClientTSReflectorPort = _JnxTwampClientTSReflectorPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 1, 8, 1, 7),
    _JnxTwampClientTSReflectorPort_Type()
)
jnxTwampClientTSReflectorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampClientTSReflectorPort.setStatus("current")


class _JnxTwampRpmIdentity_Type(Integer32):
    """Custom type jnxTwampRpmIdentity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpm", 1),
          ("twamp", 2))
    )


_JnxTwampRpmIdentity_Type.__name__ = "Integer32"
_JnxTwampRpmIdentity_Object = MibScalar
jnxTwampRpmIdentity = _JnxTwampRpmIdentity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 77, 1, 2),
    _JnxTwampRpmIdentity_Type()
)
jnxTwampRpmIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTwampRpmIdentity.setStatus("current")
_TwampNotifications_ObjectIdentity = ObjectIdentity
twampNotifications = _TwampNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 27, 1)
)

# Managed Objects groups


# Notification objects

jnxTwampClientControlConnectionClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 27, 1, 1)
)
jnxTwampClientControlConnectionClosed.setObjects(
    ("JUNIPER-TWAMP-MIB", "jnxTwampClientCCName")
)
if mibBuilder.loadTexts:
    jnxTwampClientControlConnectionClosed.setStatus(
        "current"
    )

jnxTwampClientTestIterationFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 27, 1, 2)
)
jnxTwampClientTestIterationFinished.setObjects(
    ("JUNIPER-TWAMP-MIB", "jnxTwampClientCCName")
)
if mibBuilder.loadTexts:
    jnxTwampClientTestIterationFinished.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-TWAMP-MIB",
    **{"JnxTwampClientCollectionType": JnxTwampClientCollectionType,
       "JnxTwampClientMeasurementType": JnxTwampClientMeasurementType,
       "JnxTwampClientMeasurementSet": JnxTwampClientMeasurementSet,
       "JnxTwampPercentType": JnxTwampPercentType,
       "jnxTwampMib": jnxTwampMib,
       "jnxTwampClientNode": jnxTwampClientNode,
       "jnxTwampClientResultsSampleTable": jnxTwampClientResultsSampleTable,
       "jnxTwampClientResultsSampleEntry": jnxTwampClientResultsSampleEntry,
       "jnxTwampResSampleType": jnxTwampResSampleType,
       "jnxTwampResSampleValue": jnxTwampResSampleValue,
       "jnxTwampResSampleDate": jnxTwampResSampleDate,
       "jnxTwampClientResultsSummaryTable": jnxTwampClientResultsSummaryTable,
       "jnxTwampClientResultsSummaryEntry": jnxTwampClientResultsSummaryEntry,
       "jnxTwampResSumCollection": jnxTwampResSumCollection,
       "jnxTwampResSumSent": jnxTwampResSumSent,
       "jnxTwampResSumReceived": jnxTwampResSumReceived,
       "jnxTwampResSumPercentLost": jnxTwampResSumPercentLost,
       "jnxTwampResSumDate": jnxTwampResSumDate,
       "jnxTwampClientResultsCalculatedTable": jnxTwampClientResultsCalculatedTable,
       "jnxTwampClientResultsCalculatedEntry": jnxTwampClientResultsCalculatedEntry,
       "jnxTwampResCalcSet": jnxTwampResCalcSet,
       "jnxTwampResCalcSamples": jnxTwampResCalcSamples,
       "jnxTwampResCalcMin": jnxTwampResCalcMin,
       "jnxTwampResCalcMax": jnxTwampResCalcMax,
       "jnxTwampResCalcAverage": jnxTwampResCalcAverage,
       "jnxTwampResCalcPkToPk": jnxTwampResCalcPkToPk,
       "jnxTwampResCalcStdDev": jnxTwampResCalcStdDev,
       "jnxTwampResCalcSum": jnxTwampResCalcSum,
       "jnxTwampClientHistorySampleTable": jnxTwampClientHistorySampleTable,
       "jnxTwampClientHistorySampleEntry": jnxTwampClientHistorySampleEntry,
       "jnxTwampHistSampleType": jnxTwampHistSampleType,
       "jnxTwampHistSampleValue": jnxTwampHistSampleValue,
       "jnxTwampClientHistorySummaryTable": jnxTwampClientHistorySummaryTable,
       "jnxTwampClientHistorySummaryEntry": jnxTwampClientHistorySummaryEntry,
       "jnxTwampHistSumCollection": jnxTwampHistSumCollection,
       "jnxTwampHistSumSent": jnxTwampHistSumSent,
       "jnxTwampHistSumReceived": jnxTwampHistSumReceived,
       "jnxTwampHistSumPercentLost": jnxTwampHistSumPercentLost,
       "jnxTwampClientHistoryCalculatedTable": jnxTwampClientHistoryCalculatedTable,
       "jnxTwampClientHistoryCalculatedEntry": jnxTwampClientHistoryCalculatedEntry,
       "jnxTwampHistCalcSet": jnxTwampHistCalcSet,
       "jnxTwampHistCalcSamples": jnxTwampHistCalcSamples,
       "jnxTwampHistCalcMin": jnxTwampHistCalcMin,
       "jnxTwampHistCalcMax": jnxTwampHistCalcMax,
       "jnxTwampHistCalcAverage": jnxTwampHistCalcAverage,
       "jnxTwampHistCalcPkToPk": jnxTwampHistCalcPkToPk,
       "jnxTwampHistCalcStdDev": jnxTwampHistCalcStdDev,
       "jnxTwampHistCalcSum": jnxTwampHistCalcSum,
       "jnxTwampClientControlConnectionTable": jnxTwampClientControlConnectionTable,
       "jnxTwampClientCCEntry": jnxTwampClientCCEntry,
       "jnxTwampClientControlConnectionID": jnxTwampClientControlConnectionID,
       "jnxTwampClientCCName": jnxTwampClientCCName,
       "jnxTwampClientCCStatus": jnxTwampClientCCStatus,
       "jnxTwampClientServerAddress": jnxTwampClientServerAddress,
       "jnxTwampClientServerPort": jnxTwampClientServerPort,
       "jnxTwampClientTSConfiguredCount": jnxTwampClientTSConfiguredCount,
       "jnxTwampClientTSActiveCount": jnxTwampClientTSActiveCount,
       "jnxTwampClientAuthMode": jnxTwampClientAuthMode,
       "jnxTwampClientTestSessionsTable": jnxTwampClientTestSessionsTable,
       "jnxTwampClientTSEntry": jnxTwampClientTSEntry,
       "jnxTwampClientTestSessionID": jnxTwampClientTestSessionID,
       "jnxTwampClientTSName": jnxTwampClientTSName,
       "jnxTwampClientTSStatus": jnxTwampClientTSStatus,
       "jnxTwampClientTSSenderAddress": jnxTwampClientTSSenderAddress,
       "jnxTwampClientTSSenderPort": jnxTwampClientTSSenderPort,
       "jnxTwampClientTSReflectorAddress": jnxTwampClientTSReflectorAddress,
       "jnxTwampClientTSReflectorPort": jnxTwampClientTSReflectorPort,
       "jnxTwampRpmIdentity": jnxTwampRpmIdentity,
       "twampNotifications": twampNotifications,
       "jnxTwampClientControlConnectionClosed": jnxTwampClientControlConnectionClosed,
       "jnxTwampClientTestIterationFinished": jnxTwampClientTestIterationFinished}
)
