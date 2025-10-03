# SNMP MIB module (JUNIPER-SOAM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-SOAM-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:47 2025
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

(Dot1afCfmIndexIntegerNextFree,
 Dot1agCfmMepIdOrZero,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1afCfmIndexIntegerNextFree",
    "Dot1agCfmMepIdOrZero",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(IEEE8021PriorityValue,
 IEEE8021VlanIndex,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue",
    "IEEE8021VlanIndex",
    "ieee802dot1mibs")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpPortId,
 LldpPortIdSubtype) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpPortId",
    "LldpPortIdSubtype")

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
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

jnxSoamPmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78)
)
if mibBuilder.loadTexts:
    jnxSoamPmMib.setRevisions(
        ("2012-01-13 12:00",
         "2016-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxSoamTcTestPatternType(TextualConvention, Integer32):
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
        *(("null", 1),
          ("nullCrc32", 2),
          ("prbs", 3),
          ("prbsCrc32", 4))
    )



class JnxSoamTcDataPatternType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("zeroPattern", 1),
          ("onesPattern", 2))
    )



class JnxSoamTcOperationTimeType(TextualConvention, Integer32):
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
          ("immediate", 2),
          ("relative", 3),
          ("fixed", 4))
    )



class JnxSoamTcAvailabilityType(TextualConvention, Integer32):
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
        *(("available", 1),
          ("unavailable", 2),
          ("unknown", 3))
    )



class JnxSoamTcDelayMeasurementBinType(TextualConvention, Integer32):
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
        *(("twoWayFrameDelay", 1),
          ("forwardFrameDelay", 2),
          ("backwardFrameDelay", 3),
          ("twoWayIfdv", 4),
          ("forwardIfdv", 5),
          ("backwardIfdv", 6),
          ("twoWayFrameDelayRange", 7),
          ("forwardFrameDelayRange", 8),
          ("backwardFrameDelayRange", 9))
    )



# MIB Managed Objects in the order of their OIDs

_JnxSoamPmNotifications_ObjectIdentity = ObjectIdentity
jnxSoamPmNotifications = _JnxSoamPmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0)
)
_JnxSoamPmMibObjects_ObjectIdentity = ObjectIdentity
jnxSoamPmMibObjects = _JnxSoamPmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1)
)
_JnxSoamPmMep_ObjectIdentity = ObjectIdentity
jnxSoamPmMep = _JnxSoamPmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1)
)
_JnxSoamPmMepTable_Object = MibTable
jnxSoamPmMepTable = _JnxSoamPmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSoamPmMepTable.setStatus("current")
_JnxSoamPmMepEntry_Object = MibTableRow
jnxSoamPmMepEntry = _JnxSoamPmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSoamPmMepEntry.setStatus("current")
_JnxSoamPmMepOperNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_JnxSoamPmMepOperNextIndex_Object = MibTableColumn
jnxSoamPmMepOperNextIndex = _JnxSoamPmMepOperNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1, 1),
    _JnxSoamPmMepOperNextIndex_Type()
)
jnxSoamPmMepOperNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamPmMepOperNextIndex.setStatus("current")


class _JnxSoamPmMepLmSingleEndedResponder_Type(TruthValue):
    """Custom type jnxSoamPmMepLmSingleEndedResponder based on TruthValue"""
    defaultValue = 1


_JnxSoamPmMepLmSingleEndedResponder_Type.__name__ = "TruthValue"
_JnxSoamPmMepLmSingleEndedResponder_Object = MibTableColumn
jnxSoamPmMepLmSingleEndedResponder = _JnxSoamPmMepLmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1, 2),
    _JnxSoamPmMepLmSingleEndedResponder_Type()
)
jnxSoamPmMepLmSingleEndedResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamPmMepLmSingleEndedResponder.setStatus("current")


class _JnxSoamPmMepSlmSingleEndedResponder_Type(TruthValue):
    """Custom type jnxSoamPmMepSlmSingleEndedResponder based on TruthValue"""
    defaultValue = 1


_JnxSoamPmMepSlmSingleEndedResponder_Type.__name__ = "TruthValue"
_JnxSoamPmMepSlmSingleEndedResponder_Object = MibTableColumn
jnxSoamPmMepSlmSingleEndedResponder = _JnxSoamPmMepSlmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1, 3),
    _JnxSoamPmMepSlmSingleEndedResponder_Type()
)
jnxSoamPmMepSlmSingleEndedResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamPmMepSlmSingleEndedResponder.setStatus("current")


class _JnxSoamPmMepDmSingleEndedResponder_Type(TruthValue):
    """Custom type jnxSoamPmMepDmSingleEndedResponder based on TruthValue"""
    defaultValue = 1


_JnxSoamPmMepDmSingleEndedResponder_Type.__name__ = "TruthValue"
_JnxSoamPmMepDmSingleEndedResponder_Object = MibTableColumn
jnxSoamPmMepDmSingleEndedResponder = _JnxSoamPmMepDmSingleEndedResponder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 1, 1, 1, 4),
    _JnxSoamPmMepDmSingleEndedResponder_Type()
)
jnxSoamPmMepDmSingleEndedResponder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamPmMepDmSingleEndedResponder.setStatus("current")
_JnxSoamPmLmObjects_ObjectIdentity = ObjectIdentity
jnxSoamPmLmObjects = _JnxSoamPmLmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2)
)
_JnxSoamLmCfgTable_Object = MibTable
jnxSoamLmCfgTable = _JnxSoamLmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxSoamLmCfgTable.setStatus("current")
_JnxSoamLmCfgEntry_Object = MibTableRow
jnxSoamLmCfgEntry = _JnxSoamLmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1)
)
jnxSoamLmCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmCfgEntry.setStatus("current")


class _JnxSoamLmCfgIndex_Type(Unsigned32):
    """Custom type jnxSoamLmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxSoamLmCfgIndex_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgIndex_Object = MibTableColumn
jnxSoamLmCfgIndex = _JnxSoamLmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 1),
    _JnxSoamLmCfgIndex_Type()
)
jnxSoamLmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgIndex.setStatus("current")


class _JnxSoamLmCfgType_Type(Integer32):
    """Custom type jnxSoamLmCfgType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lmLmm", 1),
          ("lmSlm", 2),
          ("lmCcm", 3))
    )


_JnxSoamLmCfgType_Type.__name__ = "Integer32"
_JnxSoamLmCfgType_Object = MibTableColumn
jnxSoamLmCfgType = _JnxSoamLmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 2),
    _JnxSoamLmCfgType_Type()
)
jnxSoamLmCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgType.setStatus("current")


class _JnxSoamLmCfgVersion_Type(Unsigned32):
    """Custom type jnxSoamLmCfgVersion based on Unsigned32"""
    defaultValue = 0


_JnxSoamLmCfgVersion_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgVersion_Object = MibTableColumn
jnxSoamLmCfgVersion = _JnxSoamLmCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 3),
    _JnxSoamLmCfgVersion_Type()
)
jnxSoamLmCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgVersion.setStatus("current")


class _JnxSoamLmCfgEnabled_Type(TruthValue):
    """Custom type jnxSoamLmCfgEnabled based on TruthValue"""
    defaultValue = 1


_JnxSoamLmCfgEnabled_Type.__name__ = "TruthValue"
_JnxSoamLmCfgEnabled_Object = MibTableColumn
jnxSoamLmCfgEnabled = _JnxSoamLmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 4),
    _JnxSoamLmCfgEnabled_Type()
)
jnxSoamLmCfgEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgEnabled.setStatus("current")


class _JnxSoamLmCfgMeasurementEnable_Type(Bits):
    """Custom type jnxSoamLmCfgMeasurementEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bForwardTransmitedFrames", 0),
          ("bForwardReceivedFrames", 1),
          ("bForwardMinFlr", 2),
          ("bForwardMaxFlr", 3),
          ("bForwardAvgFlr", 4),
          ("bBackwardTransmitedFrames", 5),
          ("bBackwardReceivedFrames", 6),
          ("bBackwardMinFlr", 7),
          ("bBackwardMaxFlr", 8),
          ("bBackwardAvgFlr", 9),
          ("bSoamPdusSent", 10),
          ("bSoamPdusReceived", 11),
          ("bAvailForwardHighLoss", 12),
          ("bAvailForwardConsecutiveHighLoss", 13),
          ("bAvailForwardAvailable", 14),
          ("bAvailForwardUnavailable", 15),
          ("bAvailForwardMinFlr", 16),
          ("bAvailForwardMaxFlr", 17),
          ("bAvailForwardAvgFlr", 18),
          ("bAvailBackwardHighLoss", 19),
          ("bAvailBackwardConsecutiveHighLoss", 20),
          ("bAvailBackwardAvailable", 21),
          ("bAvailBackwardUnavailable", 22),
          ("bAvailBackwardMinFlr", 23),
          ("bAvailBackwardMaxFlr", 24),
          ("bAvailBackwardAvgFlr", 25),
          ("bMeasuredStatsForwardMeasuredFlr", 26),
          ("bMeasuredStatsBackwardMeasuredFlr", 27),
          ("bMeasuredStatsAvailForwardStatus", 28),
          ("bMeasuredStatsAvailBackwardStatus", 29))
    )

_JnxSoamLmCfgMeasurementEnable_Type.__name__ = "Bits"
_JnxSoamLmCfgMeasurementEnable_Object = MibTableColumn
jnxSoamLmCfgMeasurementEnable = _JnxSoamLmCfgMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 5),
    _JnxSoamLmCfgMeasurementEnable_Type()
)
jnxSoamLmCfgMeasurementEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgMeasurementEnable.setStatus("current")


class _JnxSoamLmCfgMessagePeriod_Type(Integer32):
    """Custom type jnxSoamLmCfgMessagePeriod based on Integer32"""
    defaultValue = 1000


_JnxSoamLmCfgMessagePeriod_Type.__name__ = "Integer32"
_JnxSoamLmCfgMessagePeriod_Object = MibTableColumn
jnxSoamLmCfgMessagePeriod = _JnxSoamLmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 6),
    _JnxSoamLmCfgMessagePeriod_Type()
)
jnxSoamLmCfgMessagePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgMessagePeriod.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgMessagePeriod.setUnits("ms")
_JnxSoamLmCfgPriority_Type = IEEE8021PriorityValue
_JnxSoamLmCfgPriority_Object = MibTableColumn
jnxSoamLmCfgPriority = _JnxSoamLmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 7),
    _JnxSoamLmCfgPriority_Type()
)
jnxSoamLmCfgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgPriority.setStatus("current")


class _JnxSoamLmCfgFrameSize_Type(Unsigned32):
    """Custom type jnxSoamLmCfgFrameSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9600),
    )


_JnxSoamLmCfgFrameSize_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgFrameSize_Object = MibTableColumn
jnxSoamLmCfgFrameSize = _JnxSoamLmCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 8),
    _JnxSoamLmCfgFrameSize_Type()
)
jnxSoamLmCfgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgFrameSize.setUnits("bytes")


class _JnxSoamLmCfgDataPattern_Type(JnxSoamTcDataPatternType):
    """Custom type jnxSoamLmCfgDataPattern based on JnxSoamTcDataPatternType"""
    defaultValue = 1


_JnxSoamLmCfgDataPattern_Type.__name__ = "JnxSoamTcDataPatternType"
_JnxSoamLmCfgDataPattern_Object = MibTableColumn
jnxSoamLmCfgDataPattern = _JnxSoamLmCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 9),
    _JnxSoamLmCfgDataPattern_Type()
)
jnxSoamLmCfgDataPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgDataPattern.setStatus("current")


class _JnxSoamLmCfgTestTlvIncluded_Type(TruthValue):
    """Custom type jnxSoamLmCfgTestTlvIncluded based on TruthValue"""
    defaultValue = 2


_JnxSoamLmCfgTestTlvIncluded_Type.__name__ = "TruthValue"
_JnxSoamLmCfgTestTlvIncluded_Object = MibTableColumn
jnxSoamLmCfgTestTlvIncluded = _JnxSoamLmCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 10),
    _JnxSoamLmCfgTestTlvIncluded_Type()
)
jnxSoamLmCfgTestTlvIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgTestTlvIncluded.setStatus("current")


class _JnxSoamLmCfgTestTlvPattern_Type(JnxSoamTcTestPatternType):
    """Custom type jnxSoamLmCfgTestTlvPattern based on JnxSoamTcTestPatternType"""
    defaultValue = 1


_JnxSoamLmCfgTestTlvPattern_Type.__name__ = "JnxSoamTcTestPatternType"
_JnxSoamLmCfgTestTlvPattern_Object = MibTableColumn
jnxSoamLmCfgTestTlvPattern = _JnxSoamLmCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 11),
    _JnxSoamLmCfgTestTlvPattern_Type()
)
jnxSoamLmCfgTestTlvPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgTestTlvPattern.setStatus("current")


class _JnxSoamLmCfgNumIntervalsStored_Type(Unsigned32):
    """Custom type jnxSoamLmCfgNumIntervalsStored based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnxSoamLmCfgNumIntervalsStored_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgNumIntervalsStored_Object = MibTableColumn
jnxSoamLmCfgNumIntervalsStored = _JnxSoamLmCfgNumIntervalsStored_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 12),
    _JnxSoamLmCfgNumIntervalsStored_Type()
)
jnxSoamLmCfgNumIntervalsStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgNumIntervalsStored.setStatus("current")


class _JnxSoamLmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type jnxSoamLmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_JnxSoamLmCfgDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_JnxSoamLmCfgDestMepId_Object = MibTableColumn
jnxSoamLmCfgDestMepId = _JnxSoamLmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 13),
    _JnxSoamLmCfgDestMepId_Type()
)
jnxSoamLmCfgDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgDestMepId.setStatus("current")


class _JnxSoamLmCfgDestIsMepId_Type(TruthValue):
    """Custom type jnxSoamLmCfgDestIsMepId based on TruthValue"""
    defaultValue = 1


_JnxSoamLmCfgDestIsMepId_Type.__name__ = "TruthValue"
_JnxSoamLmCfgDestIsMepId_Object = MibTableColumn
jnxSoamLmCfgDestIsMepId = _JnxSoamLmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 14),
    _JnxSoamLmCfgDestIsMepId_Type()
)
jnxSoamLmCfgDestIsMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgDestIsMepId.setStatus("current")


class _JnxSoamLmCfgStartTimeType_Type(JnxSoamTcOperationTimeType):
    """Custom type jnxSoamLmCfgStartTimeType based on JnxSoamTcOperationTimeType"""
    defaultValue = 2


_JnxSoamLmCfgStartTimeType_Type.__name__ = "JnxSoamTcOperationTimeType"
_JnxSoamLmCfgStartTimeType_Object = MibTableColumn
jnxSoamLmCfgStartTimeType = _JnxSoamLmCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 15),
    _JnxSoamLmCfgStartTimeType_Type()
)
jnxSoamLmCfgStartTimeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgStartTimeType.setStatus("current")


class _JnxSoamLmCfgFixedStartDateAndTime_Type(DateAndTime):
    """Custom type jnxSoamLmCfgFixedStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_JnxSoamLmCfgFixedStartDateAndTime_Type.__name__ = "DateAndTime"
_JnxSoamLmCfgFixedStartDateAndTime_Object = MibTableColumn
jnxSoamLmCfgFixedStartDateAndTime = _JnxSoamLmCfgFixedStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 16),
    _JnxSoamLmCfgFixedStartDateAndTime_Type()
)
jnxSoamLmCfgFixedStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgFixedStartDateAndTime.setStatus("current")


class _JnxSoamLmCfgRelativeStartTime_Type(TimeInterval):
    """Custom type jnxSoamLmCfgRelativeStartTime based on TimeInterval"""
    defaultValue = 0


_JnxSoamLmCfgRelativeStartTime_Type.__name__ = "TimeInterval"
_JnxSoamLmCfgRelativeStartTime_Object = MibTableColumn
jnxSoamLmCfgRelativeStartTime = _JnxSoamLmCfgRelativeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 17),
    _JnxSoamLmCfgRelativeStartTime_Type()
)
jnxSoamLmCfgRelativeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRelativeStartTime.setStatus("current")


class _JnxSoamLmCfgRepetitionTime_Type(Unsigned32):
    """Custom type jnxSoamLmCfgRepetitionTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_JnxSoamLmCfgRepetitionTime_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgRepetitionTime_Object = MibTableColumn
jnxSoamLmCfgRepetitionTime = _JnxSoamLmCfgRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 18),
    _JnxSoamLmCfgRepetitionTime_Type()
)
jnxSoamLmCfgRepetitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRepetitionTime.setUnits("seconds")


class _JnxSoamLmCfgAlignMeasurementIntervals_Type(TruthValue):
    """Custom type jnxSoamLmCfgAlignMeasurementIntervals based on TruthValue"""
    defaultValue = 1


_JnxSoamLmCfgAlignMeasurementIntervals_Type.__name__ = "TruthValue"
_JnxSoamLmCfgAlignMeasurementIntervals_Object = MibTableColumn
jnxSoamLmCfgAlignMeasurementIntervals = _JnxSoamLmCfgAlignMeasurementIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 19),
    _JnxSoamLmCfgAlignMeasurementIntervals_Type()
)
jnxSoamLmCfgAlignMeasurementIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAlignMeasurementIntervals.setStatus("current")


class _JnxSoamLmCfgAlignMeasurementOffset_Type(Unsigned32):
    """Custom type jnxSoamLmCfgAlignMeasurementOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_JnxSoamLmCfgAlignMeasurementOffset_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgAlignMeasurementOffset_Object = MibTableColumn
jnxSoamLmCfgAlignMeasurementOffset = _JnxSoamLmCfgAlignMeasurementOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 20),
    _JnxSoamLmCfgAlignMeasurementOffset_Type()
)
jnxSoamLmCfgAlignMeasurementOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAlignMeasurementOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAlignMeasurementOffset.setUnits("minutes")


class _JnxSoamLmCfgSessionType_Type(OctetString):
    """Custom type jnxSoamLmCfgSessionType based on OctetString"""
    defaultValue = OctetString("proactive")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 42),
    )


_JnxSoamLmCfgSessionType_Type.__name__ = "OctetString"
_JnxSoamLmCfgSessionType_Object = MibTableColumn
jnxSoamLmCfgSessionType = _JnxSoamLmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 21),
    _JnxSoamLmCfgSessionType_Type()
)
jnxSoamLmCfgSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgSessionType.setStatus("current")


class _JnxSoamLmCfgSessionStatus_Type(OctetString):
    """Custom type jnxSoamLmCfgSessionStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 44),
    )


_JnxSoamLmCfgSessionStatus_Type.__name__ = "OctetString"
_JnxSoamLmCfgSessionStatus_Object = MibTableColumn
jnxSoamLmCfgSessionStatus = _JnxSoamLmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 22),
    _JnxSoamLmCfgSessionStatus_Type()
)
jnxSoamLmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgSessionStatus.setStatus("current")


class _JnxSoamLmCfgHistoryClear_Type(TruthValue):
    """Custom type jnxSoamLmCfgHistoryClear based on TruthValue"""
    defaultValue = 2


_JnxSoamLmCfgHistoryClear_Type.__name__ = "TruthValue"
_JnxSoamLmCfgHistoryClear_Object = MibTableColumn
jnxSoamLmCfgHistoryClear = _JnxSoamLmCfgHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 23),
    _JnxSoamLmCfgHistoryClear_Type()
)
jnxSoamLmCfgHistoryClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgHistoryClear.setStatus("current")
_JnxSoamLmCfgRowStatus_Type = RowStatus
_JnxSoamLmCfgRowStatus_Object = MibTableColumn
jnxSoamLmCfgRowStatus = _JnxSoamLmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 24),
    _JnxSoamLmCfgRowStatus_Type()
)
jnxSoamLmCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRowStatus.setStatus("current")


class _JnxSoamLmCfgMeasurementInterval_Type(Unsigned32):
    """Custom type jnxSoamLmCfgMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 525600),
    )


_JnxSoamLmCfgMeasurementInterval_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgMeasurementInterval_Object = MibTableColumn
jnxSoamLmCfgMeasurementInterval = _JnxSoamLmCfgMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 25),
    _JnxSoamLmCfgMeasurementInterval_Type()
)
jnxSoamLmCfgMeasurementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgMeasurementInterval.setUnits("minutes")
_JnxSoamLmCfgDestMacAddress_Type = MacAddress
_JnxSoamLmCfgDestMacAddress_Object = MibTableColumn
jnxSoamLmCfgDestMacAddress = _JnxSoamLmCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 26),
    _JnxSoamLmCfgDestMacAddress_Type()
)
jnxSoamLmCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamLmCfgDestMacAddress.setStatus("current")


class _JnxSoamLmCfgStopTimeType_Type(JnxSoamTcOperationTimeType):
    """Custom type jnxSoamLmCfgStopTimeType based on JnxSoamTcOperationTimeType"""
    defaultValue = 1


_JnxSoamLmCfgStopTimeType_Type.__name__ = "JnxSoamTcOperationTimeType"
_JnxSoamLmCfgStopTimeType_Object = MibTableColumn
jnxSoamLmCfgStopTimeType = _JnxSoamLmCfgStopTimeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 27),
    _JnxSoamLmCfgStopTimeType_Type()
)
jnxSoamLmCfgStopTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamLmCfgStopTimeType.setStatus("current")


class _JnxSoamLmCfgFixedStopDateAndTime_Type(DateAndTime):
    """Custom type jnxSoamLmCfgFixedStopDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_JnxSoamLmCfgFixedStopDateAndTime_Type.__name__ = "DateAndTime"
_JnxSoamLmCfgFixedStopDateAndTime_Object = MibTableColumn
jnxSoamLmCfgFixedStopDateAndTime = _JnxSoamLmCfgFixedStopDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 28),
    _JnxSoamLmCfgFixedStopDateAndTime_Type()
)
jnxSoamLmCfgFixedStopDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCfgFixedStopDateAndTime.setStatus("current")


class _JnxSoamLmCfgRelativeStopTime_Type(TimeInterval):
    """Custom type jnxSoamLmCfgRelativeStopTime based on TimeInterval"""
    defaultValue = 0


_JnxSoamLmCfgRelativeStopTime_Type.__name__ = "TimeInterval"
_JnxSoamLmCfgRelativeStopTime_Object = MibTableColumn
jnxSoamLmCfgRelativeStopTime = _JnxSoamLmCfgRelativeStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 29),
    _JnxSoamLmCfgRelativeStopTime_Type()
)
jnxSoamLmCfgRelativeStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamLmCfgRelativeStopTime.setStatus("current")


class _JnxSoamLmCfgAvailabilityMeasurementInterval_Type(Unsigned32):
    """Custom type jnxSoamLmCfgAvailabilityMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 525600),
    )


_JnxSoamLmCfgAvailabilityMeasurementInterval_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgAvailabilityMeasurementInterval_Object = MibTableColumn
jnxSoamLmCfgAvailabilityMeasurementInterval = _JnxSoamLmCfgAvailabilityMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 30),
    _JnxSoamLmCfgAvailabilityMeasurementInterval_Type()
)
jnxSoamLmCfgAvailabilityMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAvailabilityMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAvailabilityMeasurementInterval.setUnits("minutes")


class _JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type(Unsigned32):
    """Custom type jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Object = MibTableColumn
jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus = _JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 31),
    _JnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus_Type()
)
jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus.setStatus("current")


class _JnxSoamLmCfgAvailabilityFlrThreshold_Type(Unsigned32):
    """Custom type jnxSoamLmCfgAvailabilityFlrThreshold based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCfgAvailabilityFlrThreshold_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgAvailabilityFlrThreshold_Object = MibTableColumn
jnxSoamLmCfgAvailabilityFlrThreshold = _JnxSoamLmCfgAvailabilityFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 32),
    _JnxSoamLmCfgAvailabilityFlrThreshold_Type()
)
jnxSoamLmCfgAvailabilityFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAvailabilityFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAvailabilityFlrThreshold.setUnits("milli-percent")


class _JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Type(Unsigned32):
    """Custom type jnxSoamLmCfgAvailabilityNumConsecutiveIntervals based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Object = MibTableColumn
jnxSoamLmCfgAvailabilityNumConsecutiveIntervals = _JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 33),
    _JnxSoamLmCfgAvailabilityNumConsecutiveIntervals_Type()
)
jnxSoamLmCfgAvailabilityNumConsecutiveIntervals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAvailabilityNumConsecutiveIntervals.setStatus("current")


class _JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Object = MibTableColumn
jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr = _JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 1, 1, 34),
    _JnxSoamLmCfgAvailabilityNumConsecutiveHighFlr_Type()
)
jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr.setStatus("current")
_JnxSoamLmMeasuredStatsTable_Object = MibTable
jnxSoamLmMeasuredStatsTable = _JnxSoamLmMeasuredStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsTable.setStatus("current")
_JnxSoamLmMeasuredStatsEntry_Object = MibTableRow
jnxSoamLmMeasuredStatsEntry = _JnxSoamLmMeasuredStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1)
)
jnxSoamLmMeasuredStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsEntry.setStatus("current")


class _JnxSoamLmMeasuredStatsForwardFlr_Type(Unsigned32):
    """Custom type jnxSoamLmMeasuredStatsForwardFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmMeasuredStatsForwardFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmMeasuredStatsForwardFlr_Object = MibTableColumn
jnxSoamLmMeasuredStatsForwardFlr = _JnxSoamLmMeasuredStatsForwardFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1, 1),
    _JnxSoamLmMeasuredStatsForwardFlr_Type()
)
jnxSoamLmMeasuredStatsForwardFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsForwardFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsForwardFlr.setUnits("milli-percent")


class _JnxSoamLmMeasuredStatsBackwardFlr_Type(Unsigned32):
    """Custom type jnxSoamLmMeasuredStatsBackwardFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmMeasuredStatsBackwardFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmMeasuredStatsBackwardFlr_Object = MibTableColumn
jnxSoamLmMeasuredStatsBackwardFlr = _JnxSoamLmMeasuredStatsBackwardFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1, 2),
    _JnxSoamLmMeasuredStatsBackwardFlr_Type()
)
jnxSoamLmMeasuredStatsBackwardFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsBackwardFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsBackwardFlr.setUnits("milli-percent")
_JnxSoamLmMeasuredStatsAvailForwardStatus_Type = JnxSoamTcAvailabilityType
_JnxSoamLmMeasuredStatsAvailForwardStatus_Object = MibTableColumn
jnxSoamLmMeasuredStatsAvailForwardStatus = _JnxSoamLmMeasuredStatsAvailForwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1, 3),
    _JnxSoamLmMeasuredStatsAvailForwardStatus_Type()
)
jnxSoamLmMeasuredStatsAvailForwardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsAvailForwardStatus.setStatus("current")
_JnxSoamLmMeasuredStatsAvailBackwardStatus_Type = JnxSoamTcAvailabilityType
_JnxSoamLmMeasuredStatsAvailBackwardStatus_Object = MibTableColumn
jnxSoamLmMeasuredStatsAvailBackwardStatus = _JnxSoamLmMeasuredStatsAvailBackwardStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1, 4),
    _JnxSoamLmMeasuredStatsAvailBackwardStatus_Type()
)
jnxSoamLmMeasuredStatsAvailBackwardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsAvailBackwardStatus.setStatus("current")
_JnxSoamLmMeasuredStatsAvailForwardLastTransitionTime_Type = DateAndTime
_JnxSoamLmMeasuredStatsAvailForwardLastTransitionTime_Object = MibTableColumn
jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime = _JnxSoamLmMeasuredStatsAvailForwardLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1, 5),
    _JnxSoamLmMeasuredStatsAvailForwardLastTransitionTime_Type()
)
jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime.setStatus("current")
_JnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Type = DateAndTime
_JnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Object = MibTableColumn
jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime = _JnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 2, 1, 6),
    _JnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime_Type()
)
jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime.setStatus("current")
_JnxSoamLmCurrentStatsTable_Object = MibTable
jnxSoamLmCurrentStatsTable = _JnxSoamLmCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3)
)
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsTable.setStatus("current")
_JnxSoamLmCurrentStatsEntry_Object = MibTableRow
jnxSoamLmCurrentStatsEntry = _JnxSoamLmCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1)
)
jnxSoamLmCurrentStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsEntry.setStatus("current")
_JnxSoamLmCurrentStatsIndex_Type = Unsigned32
_JnxSoamLmCurrentStatsIndex_Object = MibTableColumn
jnxSoamLmCurrentStatsIndex = _JnxSoamLmCurrentStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 1),
    _JnxSoamLmCurrentStatsIndex_Type()
)
jnxSoamLmCurrentStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsIndex.setStatus("current")
_JnxSoamLmCurrentStatsStartTime_Type = DateAndTime
_JnxSoamLmCurrentStatsStartTime_Object = MibTableColumn
jnxSoamLmCurrentStatsStartTime = _JnxSoamLmCurrentStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 2),
    _JnxSoamLmCurrentStatsStartTime_Type()
)
jnxSoamLmCurrentStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsStartTime.setStatus("current")
_JnxSoamLmCurrentStatsElapsedTime_Type = TimeInterval
_JnxSoamLmCurrentStatsElapsedTime_Object = MibTableColumn
jnxSoamLmCurrentStatsElapsedTime = _JnxSoamLmCurrentStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 3),
    _JnxSoamLmCurrentStatsElapsedTime_Type()
)
jnxSoamLmCurrentStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsElapsedTime.setStatus("current")
_JnxSoamLmCurrentStatsSuspect_Type = TruthValue
_JnxSoamLmCurrentStatsSuspect_Object = MibTableColumn
jnxSoamLmCurrentStatsSuspect = _JnxSoamLmCurrentStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 4),
    _JnxSoamLmCurrentStatsSuspect_Type()
)
jnxSoamLmCurrentStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsSuspect.setStatus("current")
_JnxSoamLmCurrentStatsForwardTransmittedFrames_Type = Gauge32
_JnxSoamLmCurrentStatsForwardTransmittedFrames_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardTransmittedFrames = _JnxSoamLmCurrentStatsForwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 5),
    _JnxSoamLmCurrentStatsForwardTransmittedFrames_Type()
)
jnxSoamLmCurrentStatsForwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardTransmittedFrames.setStatus("current")
_JnxSoamLmCurrentStatsForwardReceivedFrames_Type = Gauge32
_JnxSoamLmCurrentStatsForwardReceivedFrames_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardReceivedFrames = _JnxSoamLmCurrentStatsForwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 6),
    _JnxSoamLmCurrentStatsForwardReceivedFrames_Type()
)
jnxSoamLmCurrentStatsForwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardReceivedFrames.setStatus("current")


class _JnxSoamLmCurrentStatsForwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsForwardMinFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardMinFlr = _JnxSoamLmCurrentStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 7),
    _JnxSoamLmCurrentStatsForwardMinFlr_Type()
)
jnxSoamLmCurrentStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsForwardMaxFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardMaxFlr = _JnxSoamLmCurrentStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 8),
    _JnxSoamLmCurrentStatsForwardMaxFlr_Type()
)
jnxSoamLmCurrentStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsForwardAvgFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsForwardAvgFlr = _JnxSoamLmCurrentStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 9),
    _JnxSoamLmCurrentStatsForwardAvgFlr_Type()
)
jnxSoamLmCurrentStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsForwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmCurrentStatsBackwardTransmittedFrames_Type = Gauge32
_JnxSoamLmCurrentStatsBackwardTransmittedFrames_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardTransmittedFrames = _JnxSoamLmCurrentStatsBackwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 10),
    _JnxSoamLmCurrentStatsBackwardTransmittedFrames_Type()
)
jnxSoamLmCurrentStatsBackwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardTransmittedFrames.setStatus("current")
_JnxSoamLmCurrentStatsBackwardReceivedFrames_Type = Gauge32
_JnxSoamLmCurrentStatsBackwardReceivedFrames_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardReceivedFrames = _JnxSoamLmCurrentStatsBackwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 11),
    _JnxSoamLmCurrentStatsBackwardReceivedFrames_Type()
)
jnxSoamLmCurrentStatsBackwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardReceivedFrames.setStatus("current")


class _JnxSoamLmCurrentStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsBackwardMinFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardMinFlr = _JnxSoamLmCurrentStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 12),
    _JnxSoamLmCurrentStatsBackwardMinFlr_Type()
)
jnxSoamLmCurrentStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsBackwardMaxFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardMaxFlr = _JnxSoamLmCurrentStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 13),
    _JnxSoamLmCurrentStatsBackwardMaxFlr_Type()
)
jnxSoamLmCurrentStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentStatsBackwardAvgFlr_Object = MibTableColumn
jnxSoamLmCurrentStatsBackwardAvgFlr = _JnxSoamLmCurrentStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 14),
    _JnxSoamLmCurrentStatsBackwardAvgFlr_Type()
)
jnxSoamLmCurrentStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsBackwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmCurrentStatsSoamPdusSent_Type = Gauge32
_JnxSoamLmCurrentStatsSoamPdusSent_Object = MibTableColumn
jnxSoamLmCurrentStatsSoamPdusSent = _JnxSoamLmCurrentStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 15),
    _JnxSoamLmCurrentStatsSoamPdusSent_Type()
)
jnxSoamLmCurrentStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsSoamPdusSent.setStatus("current")
_JnxSoamLmCurrentStatsSoamPdusReceived_Type = Gauge32
_JnxSoamLmCurrentStatsSoamPdusReceived_Object = MibTableColumn
jnxSoamLmCurrentStatsSoamPdusReceived = _JnxSoamLmCurrentStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 3, 1, 16),
    _JnxSoamLmCurrentStatsSoamPdusReceived_Type()
)
jnxSoamLmCurrentStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentStatsSoamPdusReceived.setStatus("current")
_JnxSoamLmHistoryStatsTable_Object = MibTable
jnxSoamLmHistoryStatsTable = _JnxSoamLmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsTable.setStatus("current")
_JnxSoamLmHistoryStatsEntry_Object = MibTableRow
jnxSoamLmHistoryStatsEntry = _JnxSoamLmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1)
)
jnxSoamLmHistoryStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmHistoryStatsIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsEntry.setStatus("current")
_JnxSoamLmHistoryStatsIndex_Type = Unsigned32
_JnxSoamLmHistoryStatsIndex_Object = MibTableColumn
jnxSoamLmHistoryStatsIndex = _JnxSoamLmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 1),
    _JnxSoamLmHistoryStatsIndex_Type()
)
jnxSoamLmHistoryStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsIndex.setStatus("current")
_JnxSoamLmHistoryStatsEndTime_Type = DateAndTime
_JnxSoamLmHistoryStatsEndTime_Object = MibTableColumn
jnxSoamLmHistoryStatsEndTime = _JnxSoamLmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 2),
    _JnxSoamLmHistoryStatsEndTime_Type()
)
jnxSoamLmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsEndTime.setStatus("current")
_JnxSoamLmHistoryStatsElapsedTime_Type = TimeInterval
_JnxSoamLmHistoryStatsElapsedTime_Object = MibTableColumn
jnxSoamLmHistoryStatsElapsedTime = _JnxSoamLmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 3),
    _JnxSoamLmHistoryStatsElapsedTime_Type()
)
jnxSoamLmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsElapsedTime.setStatus("current")
_JnxSoamLmHistoryStatsSuspect_Type = TruthValue
_JnxSoamLmHistoryStatsSuspect_Object = MibTableColumn
jnxSoamLmHistoryStatsSuspect = _JnxSoamLmHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 4),
    _JnxSoamLmHistoryStatsSuspect_Type()
)
jnxSoamLmHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsSuspect.setStatus("current")
_JnxSoamLmHistoryStatsForwardTransmittedFrames_Type = Gauge32
_JnxSoamLmHistoryStatsForwardTransmittedFrames_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardTransmittedFrames = _JnxSoamLmHistoryStatsForwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 5),
    _JnxSoamLmHistoryStatsForwardTransmittedFrames_Type()
)
jnxSoamLmHistoryStatsForwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardTransmittedFrames.setStatus("current")
_JnxSoamLmHistoryStatsForwardReceivedFrames_Type = Gauge32
_JnxSoamLmHistoryStatsForwardReceivedFrames_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardReceivedFrames = _JnxSoamLmHistoryStatsForwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 6),
    _JnxSoamLmHistoryStatsForwardReceivedFrames_Type()
)
jnxSoamLmHistoryStatsForwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardReceivedFrames.setStatus("current")


class _JnxSoamLmHistoryStatsForwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsForwardMinFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardMinFlr = _JnxSoamLmHistoryStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 7),
    _JnxSoamLmHistoryStatsForwardMinFlr_Type()
)
jnxSoamLmHistoryStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsForwardMaxFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardMaxFlr = _JnxSoamLmHistoryStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 8),
    _JnxSoamLmHistoryStatsForwardMaxFlr_Type()
)
jnxSoamLmHistoryStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsForwardAvgFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsForwardAvgFlr = _JnxSoamLmHistoryStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 9),
    _JnxSoamLmHistoryStatsForwardAvgFlr_Type()
)
jnxSoamLmHistoryStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsForwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmHistoryStatsBackwardTransmittedFrames_Type = Gauge32
_JnxSoamLmHistoryStatsBackwardTransmittedFrames_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardTransmittedFrames = _JnxSoamLmHistoryStatsBackwardTransmittedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 10),
    _JnxSoamLmHistoryStatsBackwardTransmittedFrames_Type()
)
jnxSoamLmHistoryStatsBackwardTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardTransmittedFrames.setStatus("current")
_JnxSoamLmHistoryStatsBackwardReceivedFrames_Type = Gauge32
_JnxSoamLmHistoryStatsBackwardReceivedFrames_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardReceivedFrames = _JnxSoamLmHistoryStatsBackwardReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 11),
    _JnxSoamLmHistoryStatsBackwardReceivedFrames_Type()
)
jnxSoamLmHistoryStatsBackwardReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardReceivedFrames.setStatus("current")


class _JnxSoamLmHistoryStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsBackwardMinFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardMinFlr = _JnxSoamLmHistoryStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 12),
    _JnxSoamLmHistoryStatsBackwardMinFlr_Type()
)
jnxSoamLmHistoryStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsBackwardMaxFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardMaxFlr = _JnxSoamLmHistoryStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 13),
    _JnxSoamLmHistoryStatsBackwardMaxFlr_Type()
)
jnxSoamLmHistoryStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryStatsBackwardAvgFlr_Object = MibTableColumn
jnxSoamLmHistoryStatsBackwardAvgFlr = _JnxSoamLmHistoryStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 14),
    _JnxSoamLmHistoryStatsBackwardAvgFlr_Type()
)
jnxSoamLmHistoryStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsBackwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmHistoryStatsSoamPdusSent_Type = Gauge32
_JnxSoamLmHistoryStatsSoamPdusSent_Object = MibTableColumn
jnxSoamLmHistoryStatsSoamPdusSent = _JnxSoamLmHistoryStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 15),
    _JnxSoamLmHistoryStatsSoamPdusSent_Type()
)
jnxSoamLmHistoryStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsSoamPdusSent.setStatus("current")
_JnxSoamLmHistoryStatsSoamPdusReceived_Type = Gauge32
_JnxSoamLmHistoryStatsSoamPdusReceived_Object = MibTableColumn
jnxSoamLmHistoryStatsSoamPdusReceived = _JnxSoamLmHistoryStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 4, 1, 16),
    _JnxSoamLmHistoryStatsSoamPdusReceived_Type()
)
jnxSoamLmHistoryStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryStatsSoamPdusReceived.setStatus("current")
_JnxSoamLmThresholdCfgTable_Object = MibTable
jnxSoamLmThresholdCfgTable = _JnxSoamLmThresholdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5)
)
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgTable.setStatus("current")
_JnxSoamLmThresholdCfgEntry_Object = MibTableRow
jnxSoamLmThresholdCfgEntry = _JnxSoamLmThresholdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1)
)
jnxSoamLmThresholdCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmThresholdCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgEntry.setStatus("current")


class _JnxSoamLmThresholdCfgIndex_Type(Unsigned32):
    """Custom type jnxSoamLmThresholdCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSoamLmThresholdCfgIndex_Type.__name__ = "Unsigned32"
_JnxSoamLmThresholdCfgIndex_Object = MibTableColumn
jnxSoamLmThresholdCfgIndex = _JnxSoamLmThresholdCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 1),
    _JnxSoamLmThresholdCfgIndex_Type()
)
jnxSoamLmThresholdCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgIndex.setStatus("current")


class _JnxSoamLmThresholdCfgEnable_Type(Bits):
    """Custom type jnxSoamLmThresholdCfgEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bJnxSoamLmMeasuredFlrForwardThreshold", 0),
          ("bJnxSoamLmMaxFlrForwardThreshold", 1),
          ("bJnxSoamLmAvgFlrForwardThreshold", 2),
          ("bJnxSoamLmMeasuredFlrBackwardThreshold", 3),
          ("bJnxSoamLmMaxFlrBackwardThreshold", 4),
          ("bJnxSoamLmAvgFlrBackwardThreshold", 5))
    )

_JnxSoamLmThresholdCfgEnable_Type.__name__ = "Bits"
_JnxSoamLmThresholdCfgEnable_Object = MibTableColumn
jnxSoamLmThresholdCfgEnable = _JnxSoamLmThresholdCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 2),
    _JnxSoamLmThresholdCfgEnable_Type()
)
jnxSoamLmThresholdCfgEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgEnable.setStatus("current")


class _JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type(Unsigned32):
    """Custom type jnxSoamLmThresholdCfgAvgFlrForwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type.__name__ = "Unsigned32"
_JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Object = MibTableColumn
jnxSoamLmThresholdCfgAvgFlrForwardThreshold = _JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 3),
    _JnxSoamLmThresholdCfgAvgFlrForwardThreshold_Type()
)
jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgAvgFlrForwardThreshold.setUnits("milli-percent")


class _JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type(Unsigned32):
    """Custom type jnxSoamLmThresholdCfgAvgFlrBackwardThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type.__name__ = "Unsigned32"
_JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Object = MibTableColumn
jnxSoamLmThresholdCfgAvgFlrBackwardThreshold = _JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 4),
    _JnxSoamLmThresholdCfgAvgFlrBackwardThreshold_Type()
)
jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgAvgFlrBackwardThreshold.setUnits("milli-percent")
_JnxSoamLmThresholdCfgRowStatus_Type = RowStatus
_JnxSoamLmThresholdCfgRowStatus_Object = MibTableColumn
jnxSoamLmThresholdCfgRowStatus = _JnxSoamLmThresholdCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 5, 1, 5),
    _JnxSoamLmThresholdCfgRowStatus_Type()
)
jnxSoamLmThresholdCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmThresholdCfgRowStatus.setStatus("current")
_JnxSoamLmCurrentAvailStatsTable_Object = MibTable
jnxSoamLmCurrentAvailStatsTable = _JnxSoamLmCurrentAvailStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6)
)
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsTable.setStatus("current")
_JnxSoamLmCurrentAvailStatsEntry_Object = MibTableRow
jnxSoamLmCurrentAvailStatsEntry = _JnxSoamLmCurrentAvailStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1)
)
jnxSoamLmCurrentAvailStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsEntry.setStatus("current")
_JnxSoamLmCurrentAvailStatsIndex_Type = Unsigned32
_JnxSoamLmCurrentAvailStatsIndex_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsIndex = _JnxSoamLmCurrentAvailStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 1),
    _JnxSoamLmCurrentAvailStatsIndex_Type()
)
jnxSoamLmCurrentAvailStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsIndex.setStatus("current")
_JnxSoamLmCurrentAvailStatsStartTime_Type = DateAndTime
_JnxSoamLmCurrentAvailStatsStartTime_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsStartTime = _JnxSoamLmCurrentAvailStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 2),
    _JnxSoamLmCurrentAvailStatsStartTime_Type()
)
jnxSoamLmCurrentAvailStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsStartTime.setStatus("current")
_JnxSoamLmCurrentAvailStatsElapsedTime_Type = TimeInterval
_JnxSoamLmCurrentAvailStatsElapsedTime_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsElapsedTime = _JnxSoamLmCurrentAvailStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 3),
    _JnxSoamLmCurrentAvailStatsElapsedTime_Type()
)
jnxSoamLmCurrentAvailStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsElapsedTime.setStatus("current")
_JnxSoamLmCurrentAvailStatsSuspect_Type = TruthValue
_JnxSoamLmCurrentAvailStatsSuspect_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsSuspect = _JnxSoamLmCurrentAvailStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 4),
    _JnxSoamLmCurrentAvailStatsSuspect_Type()
)
jnxSoamLmCurrentAvailStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsSuspect.setStatus("current")
_JnxSoamLmCurrentAvailStatsForwardHighLoss_Type = Unsigned32
_JnxSoamLmCurrentAvailStatsForwardHighLoss_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsForwardHighLoss = _JnxSoamLmCurrentAvailStatsForwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 5),
    _JnxSoamLmCurrentAvailStatsForwardHighLoss_Type()
)
jnxSoamLmCurrentAvailStatsForwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardHighLoss.setStatus("current")
_JnxSoamLmCurrentAvailStatsBackwardHighLoss_Type = Unsigned32
_JnxSoamLmCurrentAvailStatsBackwardHighLoss_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardHighLoss = _JnxSoamLmCurrentAvailStatsBackwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 6),
    _JnxSoamLmCurrentAvailStatsBackwardHighLoss_Type()
)
jnxSoamLmCurrentAvailStatsBackwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardHighLoss.setStatus("current")
_JnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Type = Unsigned32
_JnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss = _JnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 7),
    _JnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss_Type()
)
jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss.setStatus("current")
_JnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Type = Unsigned32
_JnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss = _JnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 8),
    _JnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss_Type()
)
jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss.setStatus("current")
_JnxSoamLmCurrentAvailStatsForwardAvailable_Type = Gauge32
_JnxSoamLmCurrentAvailStatsForwardAvailable_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsForwardAvailable = _JnxSoamLmCurrentAvailStatsForwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 9),
    _JnxSoamLmCurrentAvailStatsForwardAvailable_Type()
)
jnxSoamLmCurrentAvailStatsForwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardAvailable.setStatus("current")
_JnxSoamLmCurrentAvailStatsBackwardAvailable_Type = Gauge32
_JnxSoamLmCurrentAvailStatsBackwardAvailable_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardAvailable = _JnxSoamLmCurrentAvailStatsBackwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 10),
    _JnxSoamLmCurrentAvailStatsBackwardAvailable_Type()
)
jnxSoamLmCurrentAvailStatsBackwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardAvailable.setStatus("current")
_JnxSoamLmCurrentAvailStatsForwardUnavailable_Type = Gauge32
_JnxSoamLmCurrentAvailStatsForwardUnavailable_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsForwardUnavailable = _JnxSoamLmCurrentAvailStatsForwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 11),
    _JnxSoamLmCurrentAvailStatsForwardUnavailable_Type()
)
jnxSoamLmCurrentAvailStatsForwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardUnavailable.setStatus("current")
_JnxSoamLmCurrentAvailStatsBackwardUnavailable_Type = Gauge32
_JnxSoamLmCurrentAvailStatsBackwardUnavailable_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardUnavailable = _JnxSoamLmCurrentAvailStatsBackwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 12),
    _JnxSoamLmCurrentAvailStatsBackwardUnavailable_Type()
)
jnxSoamLmCurrentAvailStatsBackwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardUnavailable.setStatus("current")


class _JnxSoamLmCurrentAvailStatsForwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentAvailStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentAvailStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentAvailStatsForwardMinFlr_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsForwardMinFlr = _JnxSoamLmCurrentAvailStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 13),
    _JnxSoamLmCurrentAvailStatsForwardMinFlr_Type()
)
jnxSoamLmCurrentAvailStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentAvailStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentAvailStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentAvailStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentAvailStatsForwardMaxFlr_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsForwardMaxFlr = _JnxSoamLmCurrentAvailStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 14),
    _JnxSoamLmCurrentAvailStatsForwardMaxFlr_Type()
)
jnxSoamLmCurrentAvailStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentAvailStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentAvailStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentAvailStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentAvailStatsForwardAvgFlr_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsForwardAvgFlr = _JnxSoamLmCurrentAvailStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 15),
    _JnxSoamLmCurrentAvailStatsForwardAvgFlr_Type()
)
jnxSoamLmCurrentAvailStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsForwardAvgFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentAvailStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentAvailStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentAvailStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentAvailStatsBackwardMinFlr_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardMinFlr = _JnxSoamLmCurrentAvailStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 16),
    _JnxSoamLmCurrentAvailStatsBackwardMinFlr_Type()
)
jnxSoamLmCurrentAvailStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentAvailStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardMaxFlr = _JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 17),
    _JnxSoamLmCurrentAvailStatsBackwardMaxFlr_Type()
)
jnxSoamLmCurrentAvailStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmCurrentAvailStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Object = MibTableColumn
jnxSoamLmCurrentAvailStatsBackwardAvgFlr = _JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 6, 1, 18),
    _JnxSoamLmCurrentAvailStatsBackwardAvgFlr_Type()
)
jnxSoamLmCurrentAvailStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmCurrentAvailStatsBackwardAvgFlr.setUnits("milli-percent")
_JnxSoamLmHistoryAvailStatsTable_Object = MibTable
jnxSoamLmHistoryAvailStatsTable = _JnxSoamLmHistoryAvailStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7)
)
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsTable.setStatus("current")
_JnxSoamLmHistoryAvailStatsEntry_Object = MibTableRow
jnxSoamLmHistoryAvailStatsEntry = _JnxSoamLmHistoryAvailStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1)
)
jnxSoamLmHistoryAvailStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamLmHistoryAvailStatsIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsEntry.setStatus("current")
_JnxSoamLmHistoryAvailStatsIndex_Type = Unsigned32
_JnxSoamLmHistoryAvailStatsIndex_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsIndex = _JnxSoamLmHistoryAvailStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 1),
    _JnxSoamLmHistoryAvailStatsIndex_Type()
)
jnxSoamLmHistoryAvailStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsIndex.setStatus("current")
_JnxSoamLmHistoryAvailStatsEndTime_Type = DateAndTime
_JnxSoamLmHistoryAvailStatsEndTime_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsEndTime = _JnxSoamLmHistoryAvailStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 2),
    _JnxSoamLmHistoryAvailStatsEndTime_Type()
)
jnxSoamLmHistoryAvailStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsEndTime.setStatus("current")
_JnxSoamLmHistoryAvailStatsElapsedTime_Type = TimeInterval
_JnxSoamLmHistoryAvailStatsElapsedTime_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsElapsedTime = _JnxSoamLmHistoryAvailStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 3),
    _JnxSoamLmHistoryAvailStatsElapsedTime_Type()
)
jnxSoamLmHistoryAvailStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsElapsedTime.setStatus("current")
_JnxSoamLmHistoryAvailStatsSuspect_Type = TruthValue
_JnxSoamLmHistoryAvailStatsSuspect_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsSuspect = _JnxSoamLmHistoryAvailStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 4),
    _JnxSoamLmHistoryAvailStatsSuspect_Type()
)
jnxSoamLmHistoryAvailStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsSuspect.setStatus("current")
_JnxSoamLmHistoryAvailStatsForwardHighLoss_Type = Unsigned32
_JnxSoamLmHistoryAvailStatsForwardHighLoss_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsForwardHighLoss = _JnxSoamLmHistoryAvailStatsForwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 5),
    _JnxSoamLmHistoryAvailStatsForwardHighLoss_Type()
)
jnxSoamLmHistoryAvailStatsForwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardHighLoss.setStatus("current")
_JnxSoamLmHistoryAvailStatsBackwardHighLoss_Type = Unsigned32
_JnxSoamLmHistoryAvailStatsBackwardHighLoss_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardHighLoss = _JnxSoamLmHistoryAvailStatsBackwardHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 6),
    _JnxSoamLmHistoryAvailStatsBackwardHighLoss_Type()
)
jnxSoamLmHistoryAvailStatsBackwardHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardHighLoss.setStatus("current")
_JnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Type = Unsigned32
_JnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss = _JnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 7),
    _JnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss_Type()
)
jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss.setStatus("current")
_JnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Type = Unsigned32
_JnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss = _JnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 8),
    _JnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss_Type()
)
jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss.setStatus("current")
_JnxSoamLmHistoryAvailStatsForwardAvailable_Type = Gauge32
_JnxSoamLmHistoryAvailStatsForwardAvailable_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsForwardAvailable = _JnxSoamLmHistoryAvailStatsForwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 9),
    _JnxSoamLmHistoryAvailStatsForwardAvailable_Type()
)
jnxSoamLmHistoryAvailStatsForwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardAvailable.setStatus("current")
_JnxSoamLmHistoryAvailStatsBackwardAvailable_Type = Gauge32
_JnxSoamLmHistoryAvailStatsBackwardAvailable_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardAvailable = _JnxSoamLmHistoryAvailStatsBackwardAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 10),
    _JnxSoamLmHistoryAvailStatsBackwardAvailable_Type()
)
jnxSoamLmHistoryAvailStatsBackwardAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardAvailable.setStatus("current")
_JnxSoamLmHistoryAvailStatsForwardUnavailable_Type = Gauge32
_JnxSoamLmHistoryAvailStatsForwardUnavailable_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsForwardUnavailable = _JnxSoamLmHistoryAvailStatsForwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 11),
    _JnxSoamLmHistoryAvailStatsForwardUnavailable_Type()
)
jnxSoamLmHistoryAvailStatsForwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardUnavailable.setStatus("current")
_JnxSoamLmHistoryAvailStatsBackwardUnavailable_Type = Gauge32
_JnxSoamLmHistoryAvailStatsBackwardUnavailable_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardUnavailable = _JnxSoamLmHistoryAvailStatsBackwardUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 12),
    _JnxSoamLmHistoryAvailStatsBackwardUnavailable_Type()
)
jnxSoamLmHistoryAvailStatsBackwardUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardUnavailable.setStatus("current")


class _JnxSoamLmHistoryAvailStatsForwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryAvailStatsForwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryAvailStatsForwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryAvailStatsForwardMinFlr_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsForwardMinFlr = _JnxSoamLmHistoryAvailStatsForwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 13),
    _JnxSoamLmHistoryAvailStatsForwardMinFlr_Type()
)
jnxSoamLmHistoryAvailStatsForwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryAvailStatsForwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryAvailStatsForwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryAvailStatsForwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryAvailStatsForwardMaxFlr_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsForwardMaxFlr = _JnxSoamLmHistoryAvailStatsForwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 14),
    _JnxSoamLmHistoryAvailStatsForwardMaxFlr_Type()
)
jnxSoamLmHistoryAvailStatsForwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryAvailStatsForwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryAvailStatsForwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryAvailStatsForwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryAvailStatsForwardAvgFlr_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsForwardAvgFlr = _JnxSoamLmHistoryAvailStatsForwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 15),
    _JnxSoamLmHistoryAvailStatsForwardAvgFlr_Type()
)
jnxSoamLmHistoryAvailStatsForwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsForwardAvgFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryAvailStatsBackwardMinFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryAvailStatsBackwardMinFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryAvailStatsBackwardMinFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryAvailStatsBackwardMinFlr_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardMinFlr = _JnxSoamLmHistoryAvailStatsBackwardMinFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 16),
    _JnxSoamLmHistoryAvailStatsBackwardMinFlr_Type()
)
jnxSoamLmHistoryAvailStatsBackwardMinFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardMinFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardMinFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryAvailStatsBackwardMaxFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardMaxFlr = _JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 17),
    _JnxSoamLmHistoryAvailStatsBackwardMaxFlr_Type()
)
jnxSoamLmHistoryAvailStatsBackwardMaxFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardMaxFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardMaxFlr.setUnits("milli-percent")


class _JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Type(Unsigned32):
    """Custom type jnxSoamLmHistoryAvailStatsBackwardAvgFlr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Type.__name__ = "Unsigned32"
_JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Object = MibTableColumn
jnxSoamLmHistoryAvailStatsBackwardAvgFlr = _JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 2, 7, 1, 18),
    _JnxSoamLmHistoryAvailStatsBackwardAvgFlr_Type()
)
jnxSoamLmHistoryAvailStatsBackwardAvgFlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardAvgFlr.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamLmHistoryAvailStatsBackwardAvgFlr.setUnits("milli-percent")
_JnxSoamPmDmObjects_ObjectIdentity = ObjectIdentity
jnxSoamPmDmObjects = _JnxSoamPmDmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3)
)
_JnxSoamDmCfgTable_Object = MibTable
jnxSoamDmCfgTable = _JnxSoamDmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxSoamDmCfgTable.setStatus("current")
_JnxSoamDmCfgEntry_Object = MibTableRow
jnxSoamDmCfgEntry = _JnxSoamDmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1)
)
jnxSoamDmCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmCfgEntry.setStatus("current")


class _JnxSoamDmCfgIndex_Type(Unsigned32):
    """Custom type jnxSoamDmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxSoamDmCfgIndex_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgIndex_Object = MibTableColumn
jnxSoamDmCfgIndex = _JnxSoamDmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 1),
    _JnxSoamDmCfgIndex_Type()
)
jnxSoamDmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgIndex.setStatus("current")


class _JnxSoamDmCfgType_Type(Integer32):
    """Custom type jnxSoamDmCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dmDmm", 1),
          ("dm1DmTx", 2),
          ("dm1DmRx", 3))
    )


_JnxSoamDmCfgType_Type.__name__ = "Integer32"
_JnxSoamDmCfgType_Object = MibTableColumn
jnxSoamDmCfgType = _JnxSoamDmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 2),
    _JnxSoamDmCfgType_Type()
)
jnxSoamDmCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgType.setStatus("current")


class _JnxSoamDmCfgVersion_Type(Unsigned32):
    """Custom type jnxSoamDmCfgVersion based on Unsigned32"""
    defaultValue = 0


_JnxSoamDmCfgVersion_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgVersion_Object = MibTableColumn
jnxSoamDmCfgVersion = _JnxSoamDmCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 3),
    _JnxSoamDmCfgVersion_Type()
)
jnxSoamDmCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgVersion.setStatus("current")


class _JnxSoamDmCfgEnabled_Type(TruthValue):
    """Custom type jnxSoamDmCfgEnabled based on TruthValue"""
    defaultValue = 1


_JnxSoamDmCfgEnabled_Type.__name__ = "TruthValue"
_JnxSoamDmCfgEnabled_Object = MibTableColumn
jnxSoamDmCfgEnabled = _JnxSoamDmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 4),
    _JnxSoamDmCfgEnabled_Type()
)
jnxSoamDmCfgEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgEnabled.setStatus("current")


class _JnxSoamDmCfgMeasurementEnable_Type(Bits):
    """Custom type jnxSoamDmCfgMeasurementEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bSoamPdusSent", 0),
          ("bSoamPdusReceived", 1),
          ("bFrameDelayTwoWayBins", 2),
          ("bFrameDelayTwoWayMin", 3),
          ("bFrameDelayTwoWayMax", 4),
          ("bFrameDelayTwoWayAvg", 5),
          ("bFrameDelayForwardBins", 6),
          ("bFrameDelayForwardMin", 7),
          ("bFrameDelayForwardMax", 8),
          ("bFrameDelayForwardAvg", 9),
          ("bFrameDelayBackwardBins", 10),
          ("bFrameDelayBackwardMin", 11),
          ("bFrameDelayBackwardMax", 12),
          ("bFrameDelayBackwardAvg", 13),
          ("bIfdvForwardBins", 14),
          ("bIfdvForwardMin", 15),
          ("bIfdvForwardMax", 16),
          ("bIfdvForwardAvg", 17),
          ("bIfdvBackwardBins", 18),
          ("bIfdvBackwardMin", 19),
          ("bIfdvBackwardMax", 20),
          ("bIfdvBackwardAvg", 21),
          ("bIfdvTwoWayBins", 22),
          ("bIfdvTwoWayMin", 23),
          ("bIfdvTwoWayMax", 24),
          ("bIfdvTwoWayAvg", 25),
          ("bFrameDelayRangeForwardBins", 26),
          ("bFrameDelayRangeForwardMax", 27),
          ("bFrameDelayRangeForwardAvg", 28),
          ("bFrameDelayRangeBackwardBins", 29),
          ("bFrameDelayRangeBackwardMax", 30),
          ("bFrameDelayRangeBackwardAvg", 31),
          ("bFrameDelayRangeTwoWayBins", 32),
          ("bFrameDelayRangeTwoWayMax", 33),
          ("bFrameDelayRangeTwoWayAvg", 34),
          ("bMeasuredStatsFrameDelayTwoWay", 35),
          ("bMeasuredStatsFrameDelayForward", 36),
          ("bMeasuredStatsFrameDelayBackward", 37),
          ("bMeasuredStatsIfdvTwoWay", 38),
          ("bMeasuredStatsIfdvForward", 39),
          ("bMeasuredStatsIfdvBackward", 40))
    )

_JnxSoamDmCfgMeasurementEnable_Type.__name__ = "Bits"
_JnxSoamDmCfgMeasurementEnable_Object = MibTableColumn
jnxSoamDmCfgMeasurementEnable = _JnxSoamDmCfgMeasurementEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 5),
    _JnxSoamDmCfgMeasurementEnable_Type()
)
jnxSoamDmCfgMeasurementEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasurementEnable.setStatus("current")


class _JnxSoamDmCfgMessagePeriod_Type(Integer32):
    """Custom type jnxSoamDmCfgMessagePeriod based on Integer32"""
    defaultValue = 100


_JnxSoamDmCfgMessagePeriod_Type.__name__ = "Integer32"
_JnxSoamDmCfgMessagePeriod_Object = MibTableColumn
jnxSoamDmCfgMessagePeriod = _JnxSoamDmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 6),
    _JnxSoamDmCfgMessagePeriod_Type()
)
jnxSoamDmCfgMessagePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMessagePeriod.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMessagePeriod.setUnits("ms")
_JnxSoamDmCfgPriority_Type = IEEE8021PriorityValue
_JnxSoamDmCfgPriority_Object = MibTableColumn
jnxSoamDmCfgPriority = _JnxSoamDmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 7),
    _JnxSoamDmCfgPriority_Type()
)
jnxSoamDmCfgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgPriority.setStatus("current")


class _JnxSoamDmCfgFrameSize_Type(Unsigned32):
    """Custom type jnxSoamDmCfgFrameSize based on Unsigned32"""
    defaultValue = 64


_JnxSoamDmCfgFrameSize_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgFrameSize_Object = MibTableColumn
jnxSoamDmCfgFrameSize = _JnxSoamDmCfgFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 8),
    _JnxSoamDmCfgFrameSize_Type()
)
jnxSoamDmCfgFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgFrameSize.setStatus("current")


class _JnxSoamDmCfgDataPattern_Type(JnxSoamTcDataPatternType):
    """Custom type jnxSoamDmCfgDataPattern based on JnxSoamTcDataPatternType"""
    defaultValue = 1


_JnxSoamDmCfgDataPattern_Type.__name__ = "JnxSoamTcDataPatternType"
_JnxSoamDmCfgDataPattern_Object = MibTableColumn
jnxSoamDmCfgDataPattern = _JnxSoamDmCfgDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 9),
    _JnxSoamDmCfgDataPattern_Type()
)
jnxSoamDmCfgDataPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgDataPattern.setStatus("current")


class _JnxSoamDmCfgTestTlvIncluded_Type(TruthValue):
    """Custom type jnxSoamDmCfgTestTlvIncluded based on TruthValue"""
    defaultValue = 2


_JnxSoamDmCfgTestTlvIncluded_Type.__name__ = "TruthValue"
_JnxSoamDmCfgTestTlvIncluded_Object = MibTableColumn
jnxSoamDmCfgTestTlvIncluded = _JnxSoamDmCfgTestTlvIncluded_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 10),
    _JnxSoamDmCfgTestTlvIncluded_Type()
)
jnxSoamDmCfgTestTlvIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgTestTlvIncluded.setStatus("current")


class _JnxSoamDmCfgTestTlvPattern_Type(JnxSoamTcTestPatternType):
    """Custom type jnxSoamDmCfgTestTlvPattern based on JnxSoamTcTestPatternType"""
    defaultValue = 1


_JnxSoamDmCfgTestTlvPattern_Type.__name__ = "JnxSoamTcTestPatternType"
_JnxSoamDmCfgTestTlvPattern_Object = MibTableColumn
jnxSoamDmCfgTestTlvPattern = _JnxSoamDmCfgTestTlvPattern_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 11),
    _JnxSoamDmCfgTestTlvPattern_Type()
)
jnxSoamDmCfgTestTlvPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgTestTlvPattern.setStatus("current")


class _JnxSoamDmCfgNumIntervalsStored_Type(Unsigned32):
    """Custom type jnxSoamDmCfgNumIntervalsStored based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnxSoamDmCfgNumIntervalsStored_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgNumIntervalsStored_Object = MibTableColumn
jnxSoamDmCfgNumIntervalsStored = _JnxSoamDmCfgNumIntervalsStored_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 12),
    _JnxSoamDmCfgNumIntervalsStored_Type()
)
jnxSoamDmCfgNumIntervalsStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgNumIntervalsStored.setStatus("current")


class _JnxSoamDmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type jnxSoamDmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_JnxSoamDmCfgDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_JnxSoamDmCfgDestMepId_Object = MibTableColumn
jnxSoamDmCfgDestMepId = _JnxSoamDmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 13),
    _JnxSoamDmCfgDestMepId_Type()
)
jnxSoamDmCfgDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgDestMepId.setStatus("current")


class _JnxSoamDmCfgDestIsMepId_Type(TruthValue):
    """Custom type jnxSoamDmCfgDestIsMepId based on TruthValue"""
    defaultValue = 1


_JnxSoamDmCfgDestIsMepId_Type.__name__ = "TruthValue"
_JnxSoamDmCfgDestIsMepId_Object = MibTableColumn
jnxSoamDmCfgDestIsMepId = _JnxSoamDmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 14),
    _JnxSoamDmCfgDestIsMepId_Type()
)
jnxSoamDmCfgDestIsMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgDestIsMepId.setStatus("current")


class _JnxSoamDmCfgStartTimeType_Type(JnxSoamTcOperationTimeType):
    """Custom type jnxSoamDmCfgStartTimeType based on JnxSoamTcOperationTimeType"""
    defaultValue = 2


_JnxSoamDmCfgStartTimeType_Type.__name__ = "JnxSoamTcOperationTimeType"
_JnxSoamDmCfgStartTimeType_Object = MibTableColumn
jnxSoamDmCfgStartTimeType = _JnxSoamDmCfgStartTimeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 15),
    _JnxSoamDmCfgStartTimeType_Type()
)
jnxSoamDmCfgStartTimeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgStartTimeType.setStatus("current")


class _JnxSoamDmCfgRepetitionTime_Type(Unsigned32):
    """Custom type jnxSoamDmCfgRepetitionTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31536000),
    )


_JnxSoamDmCfgRepetitionTime_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgRepetitionTime_Object = MibTableColumn
jnxSoamDmCfgRepetitionTime = _JnxSoamDmCfgRepetitionTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 16),
    _JnxSoamDmCfgRepetitionTime_Type()
)
jnxSoamDmCfgRepetitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgRepetitionTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCfgRepetitionTime.setUnits("seconds")


class _JnxSoamDmCfgAlignMeasurementIntervals_Type(TruthValue):
    """Custom type jnxSoamDmCfgAlignMeasurementIntervals based on TruthValue"""
    defaultValue = 1


_JnxSoamDmCfgAlignMeasurementIntervals_Type.__name__ = "TruthValue"
_JnxSoamDmCfgAlignMeasurementIntervals_Object = MibTableColumn
jnxSoamDmCfgAlignMeasurementIntervals = _JnxSoamDmCfgAlignMeasurementIntervals_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 17),
    _JnxSoamDmCfgAlignMeasurementIntervals_Type()
)
jnxSoamDmCfgAlignMeasurementIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgAlignMeasurementIntervals.setStatus("current")


class _JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type(Unsigned32):
    """Custom type jnxSoamDmCfgInterFrameDelayVariationSelectionOffset based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Object = MibTableColumn
jnxSoamDmCfgInterFrameDelayVariationSelectionOffset = _JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 18),
    _JnxSoamDmCfgInterFrameDelayVariationSelectionOffset_Type()
)
jnxSoamDmCfgInterFrameDelayVariationSelectionOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgInterFrameDelayVariationSelectionOffset.setStatus("current")


class _JnxSoamDmCfgSessionType_Type(OctetString):
    """Custom type jnxSoamDmCfgSessionType based on OctetString"""
    defaultValue = OctetString("proactive")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 42),
    )


_JnxSoamDmCfgSessionType_Type.__name__ = "OctetString"
_JnxSoamDmCfgSessionType_Object = MibTableColumn
jnxSoamDmCfgSessionType = _JnxSoamDmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 19),
    _JnxSoamDmCfgSessionType_Type()
)
jnxSoamDmCfgSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgSessionType.setStatus("current")


class _JnxSoamDmCfgSessionStatus_Type(OctetString):
    """Custom type jnxSoamDmCfgSessionStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 42),
    )


_JnxSoamDmCfgSessionStatus_Type.__name__ = "OctetString"
_JnxSoamDmCfgSessionStatus_Object = MibTableColumn
jnxSoamDmCfgSessionStatus = _JnxSoamDmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 20),
    _JnxSoamDmCfgSessionStatus_Type()
)
jnxSoamDmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgSessionStatus.setStatus("current")


class _JnxSoamDmCfgHistoryClear_Type(TruthValue):
    """Custom type jnxSoamDmCfgHistoryClear based on TruthValue"""
    defaultValue = 2


_JnxSoamDmCfgHistoryClear_Type.__name__ = "TruthValue"
_JnxSoamDmCfgHistoryClear_Object = MibTableColumn
jnxSoamDmCfgHistoryClear = _JnxSoamDmCfgHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 21),
    _JnxSoamDmCfgHistoryClear_Type()
)
jnxSoamDmCfgHistoryClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgHistoryClear.setStatus("current")
_JnxSoamDmCfgRowStatus_Type = RowStatus
_JnxSoamDmCfgRowStatus_Object = MibTableColumn
jnxSoamDmCfgRowStatus = _JnxSoamDmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 22),
    _JnxSoamDmCfgRowStatus_Type()
)
jnxSoamDmCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCfgRowStatus.setStatus("current")


class _JnxSoamDmCfgMeasurementInterval_Type(Unsigned32):
    """Custom type jnxSoamDmCfgMeasurementInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_JnxSoamDmCfgMeasurementInterval_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgMeasurementInterval_Object = MibTableColumn
jnxSoamDmCfgMeasurementInterval = _JnxSoamDmCfgMeasurementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 23),
    _JnxSoamDmCfgMeasurementInterval_Type()
)
jnxSoamDmCfgMeasurementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasurementInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasurementInterval.setUnits("minutes")
_JnxSoamDmCfgDestMacAddress_Type = MacAddress
_JnxSoamDmCfgDestMacAddress_Object = MibTableColumn
jnxSoamDmCfgDestMacAddress = _JnxSoamDmCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 24),
    _JnxSoamDmCfgDestMacAddress_Type()
)
jnxSoamDmCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgDestMacAddress.setStatus("current")
_JnxSoamDmCfgSourceMacAddress_Type = MacAddress
_JnxSoamDmCfgSourceMacAddress_Object = MibTableColumn
jnxSoamDmCfgSourceMacAddress = _JnxSoamDmCfgSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 25),
    _JnxSoamDmCfgSourceMacAddress_Type()
)
jnxSoamDmCfgSourceMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgSourceMacAddress.setStatus("current")


class _JnxSoamDmCfgFixedStartDateAndTime_Type(DateAndTime):
    """Custom type jnxSoamDmCfgFixedStartDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_JnxSoamDmCfgFixedStartDateAndTime_Type.__name__ = "DateAndTime"
_JnxSoamDmCfgFixedStartDateAndTime_Object = MibTableColumn
jnxSoamDmCfgFixedStartDateAndTime = _JnxSoamDmCfgFixedStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 26),
    _JnxSoamDmCfgFixedStartDateAndTime_Type()
)
jnxSoamDmCfgFixedStartDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgFixedStartDateAndTime.setStatus("current")


class _JnxSoamDmCfgRelativeStartTime_Type(TimeInterval):
    """Custom type jnxSoamDmCfgRelativeStartTime based on TimeInterval"""
    defaultValue = 0


_JnxSoamDmCfgRelativeStartTime_Type.__name__ = "TimeInterval"
_JnxSoamDmCfgRelativeStartTime_Object = MibTableColumn
jnxSoamDmCfgRelativeStartTime = _JnxSoamDmCfgRelativeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 27),
    _JnxSoamDmCfgRelativeStartTime_Type()
)
jnxSoamDmCfgRelativeStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgRelativeStartTime.setStatus("current")


class _JnxSoamDmCfgStopTimeType_Type(JnxSoamTcOperationTimeType):
    """Custom type jnxSoamDmCfgStopTimeType based on JnxSoamTcOperationTimeType"""
    defaultValue = 1


_JnxSoamDmCfgStopTimeType_Type.__name__ = "JnxSoamTcOperationTimeType"
_JnxSoamDmCfgStopTimeType_Object = MibTableColumn
jnxSoamDmCfgStopTimeType = _JnxSoamDmCfgStopTimeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 28),
    _JnxSoamDmCfgStopTimeType_Type()
)
jnxSoamDmCfgStopTimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgStopTimeType.setStatus("current")


class _JnxSoamDmCfgFixedStopDateAndTime_Type(DateAndTime):
    """Custom type jnxSoamDmCfgFixedStopDateAndTime based on DateAndTime"""
    defaultHexValue = "0000010100000000"


_JnxSoamDmCfgFixedStopDateAndTime_Type.__name__ = "DateAndTime"
_JnxSoamDmCfgFixedStopDateAndTime_Object = MibTableColumn
jnxSoamDmCfgFixedStopDateAndTime = _JnxSoamDmCfgFixedStopDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 29),
    _JnxSoamDmCfgFixedStopDateAndTime_Type()
)
jnxSoamDmCfgFixedStopDateAndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgFixedStopDateAndTime.setStatus("current")


class _JnxSoamDmCfgRelativeStopTime_Type(TimeInterval):
    """Custom type jnxSoamDmCfgRelativeStopTime based on TimeInterval"""
    defaultValue = 0


_JnxSoamDmCfgRelativeStopTime_Type.__name__ = "TimeInterval"
_JnxSoamDmCfgRelativeStopTime_Object = MibTableColumn
jnxSoamDmCfgRelativeStopTime = _JnxSoamDmCfgRelativeStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 30),
    _JnxSoamDmCfgRelativeStopTime_Type()
)
jnxSoamDmCfgRelativeStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgRelativeStopTime.setStatus("current")


class _JnxSoamDmCfgAlignMeasurementOffset_Type(Unsigned32):
    """Custom type jnxSoamDmCfgAlignMeasurementOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_JnxSoamDmCfgAlignMeasurementOffset_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgAlignMeasurementOffset_Object = MibTableColumn
jnxSoamDmCfgAlignMeasurementOffset = _JnxSoamDmCfgAlignMeasurementOffset_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 31),
    _JnxSoamDmCfgAlignMeasurementOffset_Type()
)
jnxSoamDmCfgAlignMeasurementOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgAlignMeasurementOffset.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCfgAlignMeasurementOffset.setUnits("minutes")


class _JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type(Unsigned32):
    """Custom type jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Object = MibTableColumn
jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval = _JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 32),
    _JnxSoamDmCfgNumMeasBinsPerFrameDelayInterval_Type()
)
jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval.setStatus("current")


class _JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type(Unsigned32):
    """Custom type jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Object = MibTableColumn
jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval = _JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 33),
    _JnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval_Type()
)
jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval.setStatus("current")


class _JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type(Unsigned32):
    """Custom type jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type.__name__ = "Unsigned32"
_JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Object = MibTableColumn
jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval = _JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 1, 1, 34),
    _JnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval_Type()
)
jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval.setStatus("current")
_JnxSoamDmMeasuredStatsTable_Object = MibTable
jnxSoamDmMeasuredStatsTable = _JnxSoamDmMeasuredStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsTable.setStatus("current")
_JnxSoamDmMeasuredStatsEntry_Object = MibTableRow
jnxSoamDmMeasuredStatsEntry = _JnxSoamDmMeasuredStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1)
)
jnxSoamDmMeasuredStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsEntry.setStatus("current")
_JnxSoamDmMeasuredStatsFrameDelayTwoWay_Type = Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayTwoWay_Object = MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayTwoWay = _JnxSoamDmMeasuredStatsFrameDelayTwoWay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 1),
    _JnxSoamDmMeasuredStatsFrameDelayTwoWay_Type()
)
jnxSoamDmMeasuredStatsFrameDelayTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayTwoWay.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayTwoWay.setUnits("microseconds")
_JnxSoamDmMeasuredStatsFrameDelayForward_Type = Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayForward_Object = MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayForward = _JnxSoamDmMeasuredStatsFrameDelayForward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 2),
    _JnxSoamDmMeasuredStatsFrameDelayForward_Type()
)
jnxSoamDmMeasuredStatsFrameDelayForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayForward.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayForward.setUnits("microseconds")
_JnxSoamDmMeasuredStatsFrameDelayBackward_Type = Unsigned32
_JnxSoamDmMeasuredStatsFrameDelayBackward_Object = MibTableColumn
jnxSoamDmMeasuredStatsFrameDelayBackward = _JnxSoamDmMeasuredStatsFrameDelayBackward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 3),
    _JnxSoamDmMeasuredStatsFrameDelayBackward_Type()
)
jnxSoamDmMeasuredStatsFrameDelayBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayBackward.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsFrameDelayBackward.setUnits("microseconds")
_JnxSoamDmMeasuredStatsIfdvTwoWay_Type = Unsigned32
_JnxSoamDmMeasuredStatsIfdvTwoWay_Object = MibTableColumn
jnxSoamDmMeasuredStatsIfdvTwoWay = _JnxSoamDmMeasuredStatsIfdvTwoWay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 4),
    _JnxSoamDmMeasuredStatsIfdvTwoWay_Type()
)
jnxSoamDmMeasuredStatsIfdvTwoWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvTwoWay.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvTwoWay.setUnits("microseconds")
_JnxSoamDmMeasuredStatsIfdvForward_Type = Unsigned32
_JnxSoamDmMeasuredStatsIfdvForward_Object = MibTableColumn
jnxSoamDmMeasuredStatsIfdvForward = _JnxSoamDmMeasuredStatsIfdvForward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 5),
    _JnxSoamDmMeasuredStatsIfdvForward_Type()
)
jnxSoamDmMeasuredStatsIfdvForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvForward.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvForward.setUnits("microseconds")
_JnxSoamDmMeasuredStatsIfdvBackward_Type = Unsigned32
_JnxSoamDmMeasuredStatsIfdvBackward_Object = MibTableColumn
jnxSoamDmMeasuredStatsIfdvBackward = _JnxSoamDmMeasuredStatsIfdvBackward_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 2, 1, 6),
    _JnxSoamDmMeasuredStatsIfdvBackward_Type()
)
jnxSoamDmMeasuredStatsIfdvBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvBackward.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmMeasuredStatsIfdvBackward.setUnits("microseconds")
_JnxSoamDmCurrentStatsTable_Object = MibTable
jnxSoamDmCurrentStatsTable = _JnxSoamDmCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3)
)
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsTable.setStatus("current")
_JnxSoamDmCurrentStatsEntry_Object = MibTableRow
jnxSoamDmCurrentStatsEntry = _JnxSoamDmCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1)
)
jnxSoamDmCurrentStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsEntry.setStatus("current")
_JnxSoamDmCurrentStatsIndex_Type = Unsigned32
_JnxSoamDmCurrentStatsIndex_Object = MibTableColumn
jnxSoamDmCurrentStatsIndex = _JnxSoamDmCurrentStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 1),
    _JnxSoamDmCurrentStatsIndex_Type()
)
jnxSoamDmCurrentStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIndex.setStatus("current")
_JnxSoamDmCurrentStatsStartTime_Type = DateAndTime
_JnxSoamDmCurrentStatsStartTime_Object = MibTableColumn
jnxSoamDmCurrentStatsStartTime = _JnxSoamDmCurrentStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 2),
    _JnxSoamDmCurrentStatsStartTime_Type()
)
jnxSoamDmCurrentStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsStartTime.setStatus("current")
_JnxSoamDmCurrentStatsElapsedTime_Type = TimeInterval
_JnxSoamDmCurrentStatsElapsedTime_Object = MibTableColumn
jnxSoamDmCurrentStatsElapsedTime = _JnxSoamDmCurrentStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 3),
    _JnxSoamDmCurrentStatsElapsedTime_Type()
)
jnxSoamDmCurrentStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsElapsedTime.setStatus("current")
_JnxSoamDmCurrentStatsSuspect_Type = TruthValue
_JnxSoamDmCurrentStatsSuspect_Object = MibTableColumn
jnxSoamDmCurrentStatsSuspect = _JnxSoamDmCurrentStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 4),
    _JnxSoamDmCurrentStatsSuspect_Type()
)
jnxSoamDmCurrentStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsSuspect.setStatus("current")
_JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayMin = _JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 5),
    _JnxSoamDmCurrentStatsFrameDelayTwoWayMin_Type()
)
jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayMax = _JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 6),
    _JnxSoamDmCurrentStatsFrameDelayTwoWayMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayTwoWayAvg = _JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 7),
    _JnxSoamDmCurrentStatsFrameDelayTwoWayAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayTwoWayAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayForwardMin_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardMin_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardMin = _JnxSoamDmCurrentStatsFrameDelayForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 8),
    _JnxSoamDmCurrentStatsFrameDelayForwardMin_Type()
)
jnxSoamDmCurrentStatsFrameDelayForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayForwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardMax = _JnxSoamDmCurrentStatsFrameDelayForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 9),
    _JnxSoamDmCurrentStatsFrameDelayForwardMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayForwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayForwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayForwardAvg = _JnxSoamDmCurrentStatsFrameDelayForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 10),
    _JnxSoamDmCurrentStatsFrameDelayForwardAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayForwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayBackwardMin_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardMin_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardMin = _JnxSoamDmCurrentStatsFrameDelayBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 11),
    _JnxSoamDmCurrentStatsFrameDelayBackwardMin_Type()
)
jnxSoamDmCurrentStatsFrameDelayBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayBackwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardMax = _JnxSoamDmCurrentStatsFrameDelayBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 12),
    _JnxSoamDmCurrentStatsFrameDelayBackwardMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayBackwardAvg = _JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 13),
    _JnxSoamDmCurrentStatsFrameDelayBackwardAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayBackwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvForwardMin_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardMin_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardMin = _JnxSoamDmCurrentStatsIfdvForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 14),
    _JnxSoamDmCurrentStatsIfdvForwardMin_Type()
)
jnxSoamDmCurrentStatsIfdvForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvForwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardMax = _JnxSoamDmCurrentStatsIfdvForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 15),
    _JnxSoamDmCurrentStatsIfdvForwardMax_Type()
)
jnxSoamDmCurrentStatsIfdvForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvForwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvForwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvForwardAvg = _JnxSoamDmCurrentStatsIfdvForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 16),
    _JnxSoamDmCurrentStatsIfdvForwardAvg_Type()
)
jnxSoamDmCurrentStatsIfdvForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvForwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvBackwardMin_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardMin_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardMin = _JnxSoamDmCurrentStatsIfdvBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 17),
    _JnxSoamDmCurrentStatsIfdvBackwardMin_Type()
)
jnxSoamDmCurrentStatsIfdvBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvBackwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardMax = _JnxSoamDmCurrentStatsIfdvBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 18),
    _JnxSoamDmCurrentStatsIfdvBackwardMax_Type()
)
jnxSoamDmCurrentStatsIfdvBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvBackwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvBackwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvBackwardAvg = _JnxSoamDmCurrentStatsIfdvBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 19),
    _JnxSoamDmCurrentStatsIfdvBackwardAvg_Type()
)
jnxSoamDmCurrentStatsIfdvBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvBackwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvTwoWayMin_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayMin_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayMin = _JnxSoamDmCurrentStatsIfdvTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 20),
    _JnxSoamDmCurrentStatsIfdvTwoWayMin_Type()
)
jnxSoamDmCurrentStatsIfdvTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayMin.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvTwoWayMax_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayMax_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayMax = _JnxSoamDmCurrentStatsIfdvTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 21),
    _JnxSoamDmCurrentStatsIfdvTwoWayMax_Type()
)
jnxSoamDmCurrentStatsIfdvTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsIfdvTwoWayAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsIfdvTwoWayAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsIfdvTwoWayAvg = _JnxSoamDmCurrentStatsIfdvTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 22),
    _JnxSoamDmCurrentStatsIfdvTwoWayAvg_Type()
)
jnxSoamDmCurrentStatsIfdvTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsIfdvTwoWayAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsSoamPdusSent_Type = Gauge32
_JnxSoamDmCurrentStatsSoamPdusSent_Object = MibTableColumn
jnxSoamDmCurrentStatsSoamPdusSent = _JnxSoamDmCurrentStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 23),
    _JnxSoamDmCurrentStatsSoamPdusSent_Type()
)
jnxSoamDmCurrentStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsSoamPdusSent.setStatus("current")
_JnxSoamDmCurrentStatsSoamPdusReceived_Type = Gauge32
_JnxSoamDmCurrentStatsSoamPdusReceived_Object = MibTableColumn
jnxSoamDmCurrentStatsSoamPdusReceived = _JnxSoamDmCurrentStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 24),
    _JnxSoamDmCurrentStatsSoamPdusReceived_Type()
)
jnxSoamDmCurrentStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsSoamPdusReceived.setStatus("current")
_JnxSoamDmCurrentStatsFrameDelayRangeForwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeForwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeForwardMax = _JnxSoamDmCurrentStatsFrameDelayRangeForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 25),
    _JnxSoamDmCurrentStatsFrameDelayRangeForwardMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayRangeForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeForwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayRangeForwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeForwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg = _JnxSoamDmCurrentStatsFrameDelayRangeForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 26),
    _JnxSoamDmCurrentStatsFrameDelayRangeForwardAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayRangeBackwardMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeBackwardMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax = _JnxSoamDmCurrentStatsFrameDelayRangeBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 27),
    _JnxSoamDmCurrentStatsFrameDelayRangeBackwardMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg = _JnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 28),
    _JnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax = _JnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 29),
    _JnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax_Type()
)
jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax.setUnits("microseconds")
_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Type = Unsigned32
_JnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Object = MibTableColumn
jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg = _JnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 3, 1, 30),
    _JnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg_Type()
)
jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsTable_Object = MibTable
jnxSoamDmHistoryStatsTable = _JnxSoamDmHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4)
)
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsTable.setStatus("current")
_JnxSoamDmHistoryStatsEntry_Object = MibTableRow
jnxSoamDmHistoryStatsEntry = _JnxSoamDmHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1)
)
jnxSoamDmHistoryStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmHistoryStatsIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsEntry.setStatus("current")
_JnxSoamDmHistoryStatsIndex_Type = Unsigned32
_JnxSoamDmHistoryStatsIndex_Object = MibTableColumn
jnxSoamDmHistoryStatsIndex = _JnxSoamDmHistoryStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 1),
    _JnxSoamDmHistoryStatsIndex_Type()
)
jnxSoamDmHistoryStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIndex.setStatus("current")
_JnxSoamDmHistoryStatsEndTime_Type = DateAndTime
_JnxSoamDmHistoryStatsEndTime_Object = MibTableColumn
jnxSoamDmHistoryStatsEndTime = _JnxSoamDmHistoryStatsEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 2),
    _JnxSoamDmHistoryStatsEndTime_Type()
)
jnxSoamDmHistoryStatsEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsEndTime.setStatus("current")
_JnxSoamDmHistoryStatsElapsedTime_Type = TimeInterval
_JnxSoamDmHistoryStatsElapsedTime_Object = MibTableColumn
jnxSoamDmHistoryStatsElapsedTime = _JnxSoamDmHistoryStatsElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 3),
    _JnxSoamDmHistoryStatsElapsedTime_Type()
)
jnxSoamDmHistoryStatsElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsElapsedTime.setStatus("current")
_JnxSoamDmHistoryStatsSuspect_Type = TruthValue
_JnxSoamDmHistoryStatsSuspect_Object = MibTableColumn
jnxSoamDmHistoryStatsSuspect = _JnxSoamDmHistoryStatsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 4),
    _JnxSoamDmHistoryStatsSuspect_Type()
)
jnxSoamDmHistoryStatsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsSuspect.setStatus("current")
_JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayMin = _JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 5),
    _JnxSoamDmHistoryStatsFrameDelayTwoWayMin_Type()
)
jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayMax = _JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 6),
    _JnxSoamDmHistoryStatsFrameDelayTwoWayMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayTwoWayAvg = _JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 7),
    _JnxSoamDmHistoryStatsFrameDelayTwoWayAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayTwoWayAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayForwardMin_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardMin_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardMin = _JnxSoamDmHistoryStatsFrameDelayForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 8),
    _JnxSoamDmHistoryStatsFrameDelayForwardMin_Type()
)
jnxSoamDmHistoryStatsFrameDelayForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayForwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardMax = _JnxSoamDmHistoryStatsFrameDelayForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 9),
    _JnxSoamDmHistoryStatsFrameDelayForwardMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayForwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayForwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayForwardAvg = _JnxSoamDmHistoryStatsFrameDelayForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 10),
    _JnxSoamDmHistoryStatsFrameDelayForwardAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayForwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayBackwardMin_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardMin_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardMin = _JnxSoamDmHistoryStatsFrameDelayBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 11),
    _JnxSoamDmHistoryStatsFrameDelayBackwardMin_Type()
)
jnxSoamDmHistoryStatsFrameDelayBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayBackwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardMax = _JnxSoamDmHistoryStatsFrameDelayBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 12),
    _JnxSoamDmHistoryStatsFrameDelayBackwardMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayBackwardAvg = _JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 13),
    _JnxSoamDmHistoryStatsFrameDelayBackwardAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayBackwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvForwardMin_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardMin_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardMin = _JnxSoamDmHistoryStatsIfdvForwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 14),
    _JnxSoamDmHistoryStatsIfdvForwardMin_Type()
)
jnxSoamDmHistoryStatsIfdvForwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvForwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardMax = _JnxSoamDmHistoryStatsIfdvForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 15),
    _JnxSoamDmHistoryStatsIfdvForwardMax_Type()
)
jnxSoamDmHistoryStatsIfdvForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvForwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvForwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvForwardAvg = _JnxSoamDmHistoryStatsIfdvForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 16),
    _JnxSoamDmHistoryStatsIfdvForwardAvg_Type()
)
jnxSoamDmHistoryStatsIfdvForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvForwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvBackwardMin_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardMin_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardMin = _JnxSoamDmHistoryStatsIfdvBackwardMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 17),
    _JnxSoamDmHistoryStatsIfdvBackwardMin_Type()
)
jnxSoamDmHistoryStatsIfdvBackwardMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvBackwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardMax = _JnxSoamDmHistoryStatsIfdvBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 18),
    _JnxSoamDmHistoryStatsIfdvBackwardMax_Type()
)
jnxSoamDmHistoryStatsIfdvBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvBackwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvBackwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvBackwardAvg = _JnxSoamDmHistoryStatsIfdvBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 19),
    _JnxSoamDmHistoryStatsIfdvBackwardAvg_Type()
)
jnxSoamDmHistoryStatsIfdvBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvBackwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvTwoWayMin_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayMin_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayMin = _JnxSoamDmHistoryStatsIfdvTwoWayMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 20),
    _JnxSoamDmHistoryStatsIfdvTwoWayMin_Type()
)
jnxSoamDmHistoryStatsIfdvTwoWayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayMin.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayMin.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvTwoWayMax_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayMax_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayMax = _JnxSoamDmHistoryStatsIfdvTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 21),
    _JnxSoamDmHistoryStatsIfdvTwoWayMax_Type()
)
jnxSoamDmHistoryStatsIfdvTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsIfdvTwoWayAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsIfdvTwoWayAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsIfdvTwoWayAvg = _JnxSoamDmHistoryStatsIfdvTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 22),
    _JnxSoamDmHistoryStatsIfdvTwoWayAvg_Type()
)
jnxSoamDmHistoryStatsIfdvTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsIfdvTwoWayAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsSoamPdusSent_Type = Gauge32
_JnxSoamDmHistoryStatsSoamPdusSent_Object = MibTableColumn
jnxSoamDmHistoryStatsSoamPdusSent = _JnxSoamDmHistoryStatsSoamPdusSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 23),
    _JnxSoamDmHistoryStatsSoamPdusSent_Type()
)
jnxSoamDmHistoryStatsSoamPdusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsSoamPdusSent.setStatus("current")
_JnxSoamDmHistoryStatsSoamPdusReceived_Type = Gauge32
_JnxSoamDmHistoryStatsSoamPdusReceived_Object = MibTableColumn
jnxSoamDmHistoryStatsSoamPdusReceived = _JnxSoamDmHistoryStatsSoamPdusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 24),
    _JnxSoamDmHistoryStatsSoamPdusReceived_Type()
)
jnxSoamDmHistoryStatsSoamPdusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsSoamPdusReceived.setStatus("current")
_JnxSoamDmHistoryStatsFrameDelayRangeForwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeForwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeForwardMax = _JnxSoamDmHistoryStatsFrameDelayRangeForwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 25),
    _JnxSoamDmHistoryStatsFrameDelayRangeForwardMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayRangeForwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeForwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeForwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayRangeForwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeForwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg = _JnxSoamDmHistoryStatsFrameDelayRangeForwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 26),
    _JnxSoamDmHistoryStatsFrameDelayRangeForwardAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayRangeBackwardMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeBackwardMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax = _JnxSoamDmHistoryStatsFrameDelayRangeBackwardMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 27),
    _JnxSoamDmHistoryStatsFrameDelayRangeBackwardMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg = _JnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 28),
    _JnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax = _JnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 29),
    _JnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax_Type()
)
jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax.setUnits("microseconds")
_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Type = Unsigned32
_JnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Object = MibTableColumn
jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg = _JnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 4, 1, 30),
    _JnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg_Type()
)
jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg.setUnits("microseconds")
_JnxSoamDmThresholdCfgTable_Object = MibTable
jnxSoamDmThresholdCfgTable = _JnxSoamDmThresholdCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5)
)
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgTable.setStatus("current")
_JnxSoamDmThresholdCfgEntry_Object = MibTableRow
jnxSoamDmThresholdCfgEntry = _JnxSoamDmThresholdCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1)
)
jnxSoamDmThresholdCfgEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmThresholdCfgIndex"),
)
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgEntry.setStatus("current")


class _JnxSoamDmThresholdCfgIndex_Type(Unsigned32):
    """Custom type jnxSoamDmThresholdCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxSoamDmThresholdCfgIndex_Type.__name__ = "Unsigned32"
_JnxSoamDmThresholdCfgIndex_Object = MibTableColumn
jnxSoamDmThresholdCfgIndex = _JnxSoamDmThresholdCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 1),
    _JnxSoamDmThresholdCfgIndex_Type()
)
jnxSoamDmThresholdCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgIndex.setStatus("current")


class _JnxSoamDmThresholdCfgEnable_Type(Bits):
    """Custom type jnxSoamDmThresholdCfgEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bJnxSoamDmMeasuredFrameDelayTwoWayThreshold", 0),
          ("bJnxSoamDmMaxFrameDelayTwoWayThreshold", 1),
          ("bJnxSoamDmAvgFrameDelayTwoWayThreshold", 2),
          ("bJnxSoamDmMeasuredIfdvTwoWayThreshold", 3),
          ("bJnxSoamDmMaxIfdvTwoWayThreshold", 4),
          ("bJnxSoamDmAvgIfdvTwoWayThreshold", 5),
          ("bJnxSoamDmMaxFrameDelayRangeTwoWayThreshold", 6),
          ("bJnxSoamDmAvgFrameDelayRangeTwoWayThreshold", 7),
          ("bJnxSoamDmMeasuredFrameDelayForwardThreshold", 8),
          ("bJnxSoamDmMaxFrameDelayForwardThreshold", 9),
          ("bJnxSoamDmAvgFrameDelayForwardThreshold", 10),
          ("bJnxSoamDmMeasuredIfdvForwardThreshold", 11),
          ("bJnxSoamDmMaxIfdvForwardThreshold", 12),
          ("bJnxSoamDmAvgIfdvForwardThreshold", 13),
          ("bJnxSoamDmMaxFrameDelayRangeForwardThreshold", 14),
          ("bJnxSoamDmAvgFrameDelayRangeForwardThreshold", 15),
          ("bJnxSoamDmMeasuredFrameDelayBackwardThreshold", 16),
          ("bJnxSoamDmMaxFrameDelayBackwardThreshold", 17),
          ("bJnxSoamDmAvgFrameDelayBackwardThreshold", 18),
          ("bJnxSoamDmMeasuredIfdvBackwardThreshold", 19),
          ("bJnxSoamDmMaxIfdvBackwardThreshold", 20),
          ("bJnxSoamDmAvgIfdvBackwardThreshold", 21),
          ("bJnxSoamDmMaxFrameDelayRangeBackwardThreshold", 22),
          ("bJnxSoamDmAvgFrameDelayRangeBackwardThreshold", 23))
    )

_JnxSoamDmThresholdCfgEnable_Type.__name__ = "Bits"
_JnxSoamDmThresholdCfgEnable_Object = MibTableColumn
jnxSoamDmThresholdCfgEnable = _JnxSoamDmThresholdCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 2),
    _JnxSoamDmThresholdCfgEnable_Type()
)
jnxSoamDmThresholdCfgEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgEnable.setStatus("current")


class _JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type(Unsigned32):
    """Custom type jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type.__name__ = "Unsigned32"
_JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Object = MibTableColumn
jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold = _JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 3),
    _JnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold_Type()
)
jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold.setUnits("microseconds")


class _JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type(Unsigned32):
    """Custom type jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold based on Unsigned32"""
    defaultValue = 4294967295


_JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type.__name__ = "Unsigned32"
_JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Object = MibTableColumn
jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold = _JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 4),
    _JnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold_Type()
)
jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold.setUnits("microseconds")
_JnxSoamDmThresholdCfgRowStatus_Type = RowStatus
_JnxSoamDmThresholdCfgRowStatus_Object = MibTableColumn
jnxSoamDmThresholdCfgRowStatus = _JnxSoamDmThresholdCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 5, 1, 5),
    _JnxSoamDmThresholdCfgRowStatus_Type()
)
jnxSoamDmThresholdCfgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmThresholdCfgRowStatus.setStatus("current")
_JnxSoamDmCfgMeasBinTable_Object = MibTable
jnxSoamDmCfgMeasBinTable = _JnxSoamDmCfgMeasBinTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 6)
)
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasBinTable.setStatus("current")
_JnxSoamDmCfgMeasBinEntry_Object = MibTableRow
jnxSoamDmCfgMeasBinEntry = _JnxSoamDmCfgMeasBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 6, 1)
)
jnxSoamDmCfgMeasBinEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgMeasBinType"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasBinEntry.setStatus("current")
_JnxSoamDmCfgMeasBinType_Type = JnxSoamTcDelayMeasurementBinType
_JnxSoamDmCfgMeasBinType_Object = MibTableColumn
jnxSoamDmCfgMeasBinType = _JnxSoamDmCfgMeasBinType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 6, 1, 1),
    _JnxSoamDmCfgMeasBinType_Type()
)
jnxSoamDmCfgMeasBinType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasBinType.setStatus("current")
_JnxSoamDmCfgMeasBinNumber_Type = Unsigned32
_JnxSoamDmCfgMeasBinNumber_Object = MibTableColumn
jnxSoamDmCfgMeasBinNumber = _JnxSoamDmCfgMeasBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 6, 1, 2),
    _JnxSoamDmCfgMeasBinNumber_Type()
)
jnxSoamDmCfgMeasBinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasBinNumber.setStatus("current")
_JnxSoamDmCfgMeasBinLowerBound_Type = Unsigned32
_JnxSoamDmCfgMeasBinLowerBound_Object = MibTableColumn
jnxSoamDmCfgMeasBinLowerBound = _JnxSoamDmCfgMeasBinLowerBound_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 6, 1, 3),
    _JnxSoamDmCfgMeasBinLowerBound_Type()
)
jnxSoamDmCfgMeasBinLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasBinLowerBound.setStatus("current")
if mibBuilder.loadTexts:
    jnxSoamDmCfgMeasBinLowerBound.setUnits("microseconds (us)")
_JnxSoamDmCurrentStatsBinsTable_Object = MibTable
jnxSoamDmCurrentStatsBinsTable = _JnxSoamDmCurrentStatsBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 7)
)
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsBinsTable.setStatus("current")
_JnxSoamDmCurrentStatsBinsEntry_Object = MibTableRow
jnxSoamDmCurrentStatsBinsEntry = _JnxSoamDmCurrentStatsBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 7, 1)
)
jnxSoamDmCurrentStatsBinsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgMeasBinType"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsBinsEntry.setStatus("current")
_JnxSoamDmCurrentStatsBinsCounter_Type = Gauge32
_JnxSoamDmCurrentStatsBinsCounter_Object = MibTableColumn
jnxSoamDmCurrentStatsBinsCounter = _JnxSoamDmCurrentStatsBinsCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 7, 1, 1),
    _JnxSoamDmCurrentStatsBinsCounter_Type()
)
jnxSoamDmCurrentStatsBinsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmCurrentStatsBinsCounter.setStatus("current")
_JnxSoamDmHistoryStatsBinsTable_Object = MibTable
jnxSoamDmHistoryStatsBinsTable = _JnxSoamDmHistoryStatsBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 8)
)
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsBinsTable.setStatus("current")
_JnxSoamDmHistoryStatsBinsEntry_Object = MibTableRow
jnxSoamDmHistoryStatsBinsEntry = _JnxSoamDmHistoryStatsBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 8, 1)
)
jnxSoamDmHistoryStatsBinsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmHistoryStatsIndex"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgMeasBinType"),
    (0, "JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgMeasBinNumber"),
)
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsBinsEntry.setStatus("current")
_JnxSoamDmHistoryStatsBinsCounter_Type = Gauge32
_JnxSoamDmHistoryStatsBinsCounter_Object = MibTableColumn
jnxSoamDmHistoryStatsBinsCounter = _JnxSoamDmHistoryStatsBinsCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 3, 8, 1, 1),
    _JnxSoamDmHistoryStatsBinsCounter_Type()
)
jnxSoamDmHistoryStatsBinsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSoamDmHistoryStatsBinsCounter.setStatus("current")
_JnxSoamPmNotificationCfg_ObjectIdentity = ObjectIdentity
jnxSoamPmNotificationCfg = _JnxSoamPmNotificationCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 4)
)
_JnxSoamPmNotificationObj_ObjectIdentity = ObjectIdentity
jnxSoamPmNotificationObj = _JnxSoamPmNotificationObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5)
)
_JnxSoamPmNotificationObjDateAndTime_Type = DateAndTime
_JnxSoamPmNotificationObjDateAndTime_Object = MibScalar
jnxSoamPmNotificationObjDateAndTime = _JnxSoamPmNotificationObjDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 1),
    _JnxSoamPmNotificationObjDateAndTime_Type()
)
jnxSoamPmNotificationObjDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjDateAndTime.setStatus("current")
_JnxSoamPmNotificationObjThresholdId_Type = ObjectIdentifier
_JnxSoamPmNotificationObjThresholdId_Object = MibScalar
jnxSoamPmNotificationObjThresholdId = _JnxSoamPmNotificationObjThresholdId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 2),
    _JnxSoamPmNotificationObjThresholdId_Type()
)
jnxSoamPmNotificationObjThresholdId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjThresholdId.setStatus("current")
_JnxSoamPmNotificationObjThresholdConfig_Type = Unsigned32
_JnxSoamPmNotificationObjThresholdConfig_Object = MibScalar
jnxSoamPmNotificationObjThresholdConfig = _JnxSoamPmNotificationObjThresholdConfig_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 3),
    _JnxSoamPmNotificationObjThresholdConfig_Type()
)
jnxSoamPmNotificationObjThresholdConfig.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjThresholdConfig.setStatus("current")
_JnxSoamPmNotificationObjThresholdValue_Type = Unsigned32
_JnxSoamPmNotificationObjThresholdValue_Object = MibScalar
jnxSoamPmNotificationObjThresholdValue = _JnxSoamPmNotificationObjThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 4),
    _JnxSoamPmNotificationObjThresholdValue_Type()
)
jnxSoamPmNotificationObjThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjThresholdValue.setStatus("current")
_JnxSoamPmNotificationObjSuspect_Type = TruthValue
_JnxSoamPmNotificationObjSuspect_Object = MibScalar
jnxSoamPmNotificationObjSuspect = _JnxSoamPmNotificationObjSuspect_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 5),
    _JnxSoamPmNotificationObjSuspect_Type()
)
jnxSoamPmNotificationObjSuspect.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjSuspect.setStatus("current")


class _JnxSoamPmNotificationObjCrossingType_Type(Integer32):
    """Custom type jnxSoamPmNotificationObjCrossingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aboveAlarm", 1),
          ("setAlarm", 2),
          ("clearAlarm", 3))
    )


_JnxSoamPmNotificationObjCrossingType_Type.__name__ = "Integer32"
_JnxSoamPmNotificationObjCrossingType_Object = MibScalar
jnxSoamPmNotificationObjCrossingType = _JnxSoamPmNotificationObjCrossingType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 6),
    _JnxSoamPmNotificationObjCrossingType_Type()
)
jnxSoamPmNotificationObjCrossingType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjCrossingType.setStatus("current")
_JnxSoamPmNotificationObjDestinationMep_Type = MacAddress
_JnxSoamPmNotificationObjDestinationMep_Object = MibScalar
jnxSoamPmNotificationObjDestinationMep = _JnxSoamPmNotificationObjDestinationMep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 7),
    _JnxSoamPmNotificationObjDestinationMep_Type()
)
jnxSoamPmNotificationObjDestinationMep.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjDestinationMep.setStatus("current")
_JnxSoamPmNotificationObjPriority_Type = MacAddress
_JnxSoamPmNotificationObjPriority_Object = MibScalar
jnxSoamPmNotificationObjPriority = _JnxSoamPmNotificationObjPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 8),
    _JnxSoamPmNotificationObjPriority_Type()
)
jnxSoamPmNotificationObjPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjPriority.setStatus("current")
_JnxSoamPmNotificationTotalFlaps_Type = Unsigned32
_JnxSoamPmNotificationTotalFlaps_Object = MibScalar
jnxSoamPmNotificationTotalFlaps = _JnxSoamPmNotificationTotalFlaps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 9),
    _JnxSoamPmNotificationTotalFlaps_Type()
)
jnxSoamPmNotificationTotalFlaps.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationTotalFlaps.setStatus("current")
_JnxSoamPmNotificationAccTotalFlaps_Type = Unsigned32
_JnxSoamPmNotificationAccTotalFlaps_Object = MibScalar
jnxSoamPmNotificationAccTotalFlaps = _JnxSoamPmNotificationAccTotalFlaps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 10),
    _JnxSoamPmNotificationAccTotalFlaps_Type()
)
jnxSoamPmNotificationAccTotalFlaps.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationAccTotalFlaps.setStatus("current")
_JnxSoamPmNotificationObjThresholdLastValue_Type = Unsigned32
_JnxSoamPmNotificationObjThresholdLastValue_Object = MibScalar
jnxSoamPmNotificationObjThresholdLastValue = _JnxSoamPmNotificationObjThresholdLastValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 11),
    _JnxSoamPmNotificationObjThresholdLastValue_Type()
)
jnxSoamPmNotificationObjThresholdLastValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjThresholdLastValue.setStatus("current")


class _JnxSoamPmNotificationObjCurrentState_Type(Integer32):
    """Custom type jnxSoamPmNotificationObjCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aboveAlarm", 1),
          ("setAlarm", 2),
          ("clearAlarm", 3))
    )


_JnxSoamPmNotificationObjCurrentState_Type.__name__ = "Integer32"
_JnxSoamPmNotificationObjCurrentState_Object = MibScalar
jnxSoamPmNotificationObjCurrentState = _JnxSoamPmNotificationObjCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 12),
    _JnxSoamPmNotificationObjCurrentState_Type()
)
jnxSoamPmNotificationObjCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjCurrentState.setStatus("current")
_JnxSoamPmNotificationObjLastDateAndTime_Type = DateAndTime
_JnxSoamPmNotificationObjLastDateAndTime_Object = MibScalar
jnxSoamPmNotificationObjLastDateAndTime = _JnxSoamPmNotificationObjLastDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 1, 5, 13),
    _JnxSoamPmNotificationObjLastDateAndTime_Type()
)
jnxSoamPmNotificationObjLastDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSoamPmNotificationObjLastDateAndTime.setStatus("current")
_JnxSoamPmMibConformance_ObjectIdentity = ObjectIdentity
jnxSoamPmMibConformance = _JnxSoamPmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("JUNIPER-SOAM-PM-MIB",
     "jnxSoamPmMepEntry")
)
jnxSoamPmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxSoamLmSessionStartStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0, 1)
)
jnxSoamLmSessionStartStopAlarm.setObjects(
      *(("JUNIPER-SOAM-PM-MIB", "jnxSoamLmCfgSessionStatus"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDateAndTime"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    jnxSoamLmSessionStartStopAlarm.setStatus(
        "current"
    )

jnxSoamDmSessionStartStopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0, 2)
)
jnxSoamDmSessionStartStopAlarm.setObjects(
      *(("JUNIPER-SOAM-PM-MIB", "jnxSoamDmCfgSessionStatus"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDateAndTime"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    jnxSoamDmSessionStartStopAlarm.setStatus(
        "current"
    )

jnxSoamPmThresholdCrossingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0, 3)
)
jnxSoamPmThresholdCrossingAlarm.setObjects(
      *(("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjCrossingType"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdId"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdConfig"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdValue"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjSuspect"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDateAndTime"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    jnxSoamPmThresholdCrossingAlarm.setStatus(
        "current"
    )

jnxSoamPmThresholdFlapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 78, 0, 4)
)
jnxSoamPmThresholdFlapAlarm.setObjects(
      *(("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdId"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdConfig"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjThresholdLastValue"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationTotalFlaps"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationAccTotalFlaps"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjCurrentState"),
        ("JUNIPER-SOAM-PM-MIB", "jnxSoamPmNotificationObjDestinationMep"))
)
if mibBuilder.loadTexts:
    jnxSoamPmThresholdFlapAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SOAM-PM-MIB",
    **{"JnxSoamTcTestPatternType": JnxSoamTcTestPatternType,
       "JnxSoamTcDataPatternType": JnxSoamTcDataPatternType,
       "JnxSoamTcOperationTimeType": JnxSoamTcOperationTimeType,
       "JnxSoamTcAvailabilityType": JnxSoamTcAvailabilityType,
       "JnxSoamTcDelayMeasurementBinType": JnxSoamTcDelayMeasurementBinType,
       "jnxSoamPmMib": jnxSoamPmMib,
       "jnxSoamPmNotifications": jnxSoamPmNotifications,
       "jnxSoamLmSessionStartStopAlarm": jnxSoamLmSessionStartStopAlarm,
       "jnxSoamDmSessionStartStopAlarm": jnxSoamDmSessionStartStopAlarm,
       "jnxSoamPmThresholdCrossingAlarm": jnxSoamPmThresholdCrossingAlarm,
       "jnxSoamPmThresholdFlapAlarm": jnxSoamPmThresholdFlapAlarm,
       "jnxSoamPmMibObjects": jnxSoamPmMibObjects,
       "jnxSoamPmMep": jnxSoamPmMep,
       "jnxSoamPmMepTable": jnxSoamPmMepTable,
       "jnxSoamPmMepEntry": jnxSoamPmMepEntry,
       "jnxSoamPmMepOperNextIndex": jnxSoamPmMepOperNextIndex,
       "jnxSoamPmMepLmSingleEndedResponder": jnxSoamPmMepLmSingleEndedResponder,
       "jnxSoamPmMepSlmSingleEndedResponder": jnxSoamPmMepSlmSingleEndedResponder,
       "jnxSoamPmMepDmSingleEndedResponder": jnxSoamPmMepDmSingleEndedResponder,
       "jnxSoamPmLmObjects": jnxSoamPmLmObjects,
       "jnxSoamLmCfgTable": jnxSoamLmCfgTable,
       "jnxSoamLmCfgEntry": jnxSoamLmCfgEntry,
       "jnxSoamLmCfgIndex": jnxSoamLmCfgIndex,
       "jnxSoamLmCfgType": jnxSoamLmCfgType,
       "jnxSoamLmCfgVersion": jnxSoamLmCfgVersion,
       "jnxSoamLmCfgEnabled": jnxSoamLmCfgEnabled,
       "jnxSoamLmCfgMeasurementEnable": jnxSoamLmCfgMeasurementEnable,
       "jnxSoamLmCfgMessagePeriod": jnxSoamLmCfgMessagePeriod,
       "jnxSoamLmCfgPriority": jnxSoamLmCfgPriority,
       "jnxSoamLmCfgFrameSize": jnxSoamLmCfgFrameSize,
       "jnxSoamLmCfgDataPattern": jnxSoamLmCfgDataPattern,
       "jnxSoamLmCfgTestTlvIncluded": jnxSoamLmCfgTestTlvIncluded,
       "jnxSoamLmCfgTestTlvPattern": jnxSoamLmCfgTestTlvPattern,
       "jnxSoamLmCfgNumIntervalsStored": jnxSoamLmCfgNumIntervalsStored,
       "jnxSoamLmCfgDestMepId": jnxSoamLmCfgDestMepId,
       "jnxSoamLmCfgDestIsMepId": jnxSoamLmCfgDestIsMepId,
       "jnxSoamLmCfgStartTimeType": jnxSoamLmCfgStartTimeType,
       "jnxSoamLmCfgFixedStartDateAndTime": jnxSoamLmCfgFixedStartDateAndTime,
       "jnxSoamLmCfgRelativeStartTime": jnxSoamLmCfgRelativeStartTime,
       "jnxSoamLmCfgRepetitionTime": jnxSoamLmCfgRepetitionTime,
       "jnxSoamLmCfgAlignMeasurementIntervals": jnxSoamLmCfgAlignMeasurementIntervals,
       "jnxSoamLmCfgAlignMeasurementOffset": jnxSoamLmCfgAlignMeasurementOffset,
       "jnxSoamLmCfgSessionType": jnxSoamLmCfgSessionType,
       "jnxSoamLmCfgSessionStatus": jnxSoamLmCfgSessionStatus,
       "jnxSoamLmCfgHistoryClear": jnxSoamLmCfgHistoryClear,
       "jnxSoamLmCfgRowStatus": jnxSoamLmCfgRowStatus,
       "jnxSoamLmCfgMeasurementInterval": jnxSoamLmCfgMeasurementInterval,
       "jnxSoamLmCfgDestMacAddress": jnxSoamLmCfgDestMacAddress,
       "jnxSoamLmCfgStopTimeType": jnxSoamLmCfgStopTimeType,
       "jnxSoamLmCfgFixedStopDateAndTime": jnxSoamLmCfgFixedStopDateAndTime,
       "jnxSoamLmCfgRelativeStopTime": jnxSoamLmCfgRelativeStopTime,
       "jnxSoamLmCfgAvailabilityMeasurementInterval": jnxSoamLmCfgAvailabilityMeasurementInterval,
       "jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus": jnxSoamLmCfgAvailabilityNumConsecutiveMeasPdus,
       "jnxSoamLmCfgAvailabilityFlrThreshold": jnxSoamLmCfgAvailabilityFlrThreshold,
       "jnxSoamLmCfgAvailabilityNumConsecutiveIntervals": jnxSoamLmCfgAvailabilityNumConsecutiveIntervals,
       "jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr": jnxSoamLmCfgAvailabilityNumConsecutiveHighFlr,
       "jnxSoamLmMeasuredStatsTable": jnxSoamLmMeasuredStatsTable,
       "jnxSoamLmMeasuredStatsEntry": jnxSoamLmMeasuredStatsEntry,
       "jnxSoamLmMeasuredStatsForwardFlr": jnxSoamLmMeasuredStatsForwardFlr,
       "jnxSoamLmMeasuredStatsBackwardFlr": jnxSoamLmMeasuredStatsBackwardFlr,
       "jnxSoamLmMeasuredStatsAvailForwardStatus": jnxSoamLmMeasuredStatsAvailForwardStatus,
       "jnxSoamLmMeasuredStatsAvailBackwardStatus": jnxSoamLmMeasuredStatsAvailBackwardStatus,
       "jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime": jnxSoamLmMeasuredStatsAvailForwardLastTransitionTime,
       "jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime": jnxSoamLmMeasuredStatsAvailBackwardLastTransitionTime,
       "jnxSoamLmCurrentStatsTable": jnxSoamLmCurrentStatsTable,
       "jnxSoamLmCurrentStatsEntry": jnxSoamLmCurrentStatsEntry,
       "jnxSoamLmCurrentStatsIndex": jnxSoamLmCurrentStatsIndex,
       "jnxSoamLmCurrentStatsStartTime": jnxSoamLmCurrentStatsStartTime,
       "jnxSoamLmCurrentStatsElapsedTime": jnxSoamLmCurrentStatsElapsedTime,
       "jnxSoamLmCurrentStatsSuspect": jnxSoamLmCurrentStatsSuspect,
       "jnxSoamLmCurrentStatsForwardTransmittedFrames": jnxSoamLmCurrentStatsForwardTransmittedFrames,
       "jnxSoamLmCurrentStatsForwardReceivedFrames": jnxSoamLmCurrentStatsForwardReceivedFrames,
       "jnxSoamLmCurrentStatsForwardMinFlr": jnxSoamLmCurrentStatsForwardMinFlr,
       "jnxSoamLmCurrentStatsForwardMaxFlr": jnxSoamLmCurrentStatsForwardMaxFlr,
       "jnxSoamLmCurrentStatsForwardAvgFlr": jnxSoamLmCurrentStatsForwardAvgFlr,
       "jnxSoamLmCurrentStatsBackwardTransmittedFrames": jnxSoamLmCurrentStatsBackwardTransmittedFrames,
       "jnxSoamLmCurrentStatsBackwardReceivedFrames": jnxSoamLmCurrentStatsBackwardReceivedFrames,
       "jnxSoamLmCurrentStatsBackwardMinFlr": jnxSoamLmCurrentStatsBackwardMinFlr,
       "jnxSoamLmCurrentStatsBackwardMaxFlr": jnxSoamLmCurrentStatsBackwardMaxFlr,
       "jnxSoamLmCurrentStatsBackwardAvgFlr": jnxSoamLmCurrentStatsBackwardAvgFlr,
       "jnxSoamLmCurrentStatsSoamPdusSent": jnxSoamLmCurrentStatsSoamPdusSent,
       "jnxSoamLmCurrentStatsSoamPdusReceived": jnxSoamLmCurrentStatsSoamPdusReceived,
       "jnxSoamLmHistoryStatsTable": jnxSoamLmHistoryStatsTable,
       "jnxSoamLmHistoryStatsEntry": jnxSoamLmHistoryStatsEntry,
       "jnxSoamLmHistoryStatsIndex": jnxSoamLmHistoryStatsIndex,
       "jnxSoamLmHistoryStatsEndTime": jnxSoamLmHistoryStatsEndTime,
       "jnxSoamLmHistoryStatsElapsedTime": jnxSoamLmHistoryStatsElapsedTime,
       "jnxSoamLmHistoryStatsSuspect": jnxSoamLmHistoryStatsSuspect,
       "jnxSoamLmHistoryStatsForwardTransmittedFrames": jnxSoamLmHistoryStatsForwardTransmittedFrames,
       "jnxSoamLmHistoryStatsForwardReceivedFrames": jnxSoamLmHistoryStatsForwardReceivedFrames,
       "jnxSoamLmHistoryStatsForwardMinFlr": jnxSoamLmHistoryStatsForwardMinFlr,
       "jnxSoamLmHistoryStatsForwardMaxFlr": jnxSoamLmHistoryStatsForwardMaxFlr,
       "jnxSoamLmHistoryStatsForwardAvgFlr": jnxSoamLmHistoryStatsForwardAvgFlr,
       "jnxSoamLmHistoryStatsBackwardTransmittedFrames": jnxSoamLmHistoryStatsBackwardTransmittedFrames,
       "jnxSoamLmHistoryStatsBackwardReceivedFrames": jnxSoamLmHistoryStatsBackwardReceivedFrames,
       "jnxSoamLmHistoryStatsBackwardMinFlr": jnxSoamLmHistoryStatsBackwardMinFlr,
       "jnxSoamLmHistoryStatsBackwardMaxFlr": jnxSoamLmHistoryStatsBackwardMaxFlr,
       "jnxSoamLmHistoryStatsBackwardAvgFlr": jnxSoamLmHistoryStatsBackwardAvgFlr,
       "jnxSoamLmHistoryStatsSoamPdusSent": jnxSoamLmHistoryStatsSoamPdusSent,
       "jnxSoamLmHistoryStatsSoamPdusReceived": jnxSoamLmHistoryStatsSoamPdusReceived,
       "jnxSoamLmThresholdCfgTable": jnxSoamLmThresholdCfgTable,
       "jnxSoamLmThresholdCfgEntry": jnxSoamLmThresholdCfgEntry,
       "jnxSoamLmThresholdCfgIndex": jnxSoamLmThresholdCfgIndex,
       "jnxSoamLmThresholdCfgEnable": jnxSoamLmThresholdCfgEnable,
       "jnxSoamLmThresholdCfgAvgFlrForwardThreshold": jnxSoamLmThresholdCfgAvgFlrForwardThreshold,
       "jnxSoamLmThresholdCfgAvgFlrBackwardThreshold": jnxSoamLmThresholdCfgAvgFlrBackwardThreshold,
       "jnxSoamLmThresholdCfgRowStatus": jnxSoamLmThresholdCfgRowStatus,
       "jnxSoamLmCurrentAvailStatsTable": jnxSoamLmCurrentAvailStatsTable,
       "jnxSoamLmCurrentAvailStatsEntry": jnxSoamLmCurrentAvailStatsEntry,
       "jnxSoamLmCurrentAvailStatsIndex": jnxSoamLmCurrentAvailStatsIndex,
       "jnxSoamLmCurrentAvailStatsStartTime": jnxSoamLmCurrentAvailStatsStartTime,
       "jnxSoamLmCurrentAvailStatsElapsedTime": jnxSoamLmCurrentAvailStatsElapsedTime,
       "jnxSoamLmCurrentAvailStatsSuspect": jnxSoamLmCurrentAvailStatsSuspect,
       "jnxSoamLmCurrentAvailStatsForwardHighLoss": jnxSoamLmCurrentAvailStatsForwardHighLoss,
       "jnxSoamLmCurrentAvailStatsBackwardHighLoss": jnxSoamLmCurrentAvailStatsBackwardHighLoss,
       "jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss": jnxSoamLmCurrentAvailStatsForwardConsecutiveHighLoss,
       "jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss": jnxSoamLmCurrentAvailStatsBackwardConsecutiveHighLoss,
       "jnxSoamLmCurrentAvailStatsForwardAvailable": jnxSoamLmCurrentAvailStatsForwardAvailable,
       "jnxSoamLmCurrentAvailStatsBackwardAvailable": jnxSoamLmCurrentAvailStatsBackwardAvailable,
       "jnxSoamLmCurrentAvailStatsForwardUnavailable": jnxSoamLmCurrentAvailStatsForwardUnavailable,
       "jnxSoamLmCurrentAvailStatsBackwardUnavailable": jnxSoamLmCurrentAvailStatsBackwardUnavailable,
       "jnxSoamLmCurrentAvailStatsForwardMinFlr": jnxSoamLmCurrentAvailStatsForwardMinFlr,
       "jnxSoamLmCurrentAvailStatsForwardMaxFlr": jnxSoamLmCurrentAvailStatsForwardMaxFlr,
       "jnxSoamLmCurrentAvailStatsForwardAvgFlr": jnxSoamLmCurrentAvailStatsForwardAvgFlr,
       "jnxSoamLmCurrentAvailStatsBackwardMinFlr": jnxSoamLmCurrentAvailStatsBackwardMinFlr,
       "jnxSoamLmCurrentAvailStatsBackwardMaxFlr": jnxSoamLmCurrentAvailStatsBackwardMaxFlr,
       "jnxSoamLmCurrentAvailStatsBackwardAvgFlr": jnxSoamLmCurrentAvailStatsBackwardAvgFlr,
       "jnxSoamLmHistoryAvailStatsTable": jnxSoamLmHistoryAvailStatsTable,
       "jnxSoamLmHistoryAvailStatsEntry": jnxSoamLmHistoryAvailStatsEntry,
       "jnxSoamLmHistoryAvailStatsIndex": jnxSoamLmHistoryAvailStatsIndex,
       "jnxSoamLmHistoryAvailStatsEndTime": jnxSoamLmHistoryAvailStatsEndTime,
       "jnxSoamLmHistoryAvailStatsElapsedTime": jnxSoamLmHistoryAvailStatsElapsedTime,
       "jnxSoamLmHistoryAvailStatsSuspect": jnxSoamLmHistoryAvailStatsSuspect,
       "jnxSoamLmHistoryAvailStatsForwardHighLoss": jnxSoamLmHistoryAvailStatsForwardHighLoss,
       "jnxSoamLmHistoryAvailStatsBackwardHighLoss": jnxSoamLmHistoryAvailStatsBackwardHighLoss,
       "jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss": jnxSoamLmHistoryAvailStatsForwardConsecutiveHighLoss,
       "jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss": jnxSoamLmHistoryAvailStatsBackwardConsecutiveHighLoss,
       "jnxSoamLmHistoryAvailStatsForwardAvailable": jnxSoamLmHistoryAvailStatsForwardAvailable,
       "jnxSoamLmHistoryAvailStatsBackwardAvailable": jnxSoamLmHistoryAvailStatsBackwardAvailable,
       "jnxSoamLmHistoryAvailStatsForwardUnavailable": jnxSoamLmHistoryAvailStatsForwardUnavailable,
       "jnxSoamLmHistoryAvailStatsBackwardUnavailable": jnxSoamLmHistoryAvailStatsBackwardUnavailable,
       "jnxSoamLmHistoryAvailStatsForwardMinFlr": jnxSoamLmHistoryAvailStatsForwardMinFlr,
       "jnxSoamLmHistoryAvailStatsForwardMaxFlr": jnxSoamLmHistoryAvailStatsForwardMaxFlr,
       "jnxSoamLmHistoryAvailStatsForwardAvgFlr": jnxSoamLmHistoryAvailStatsForwardAvgFlr,
       "jnxSoamLmHistoryAvailStatsBackwardMinFlr": jnxSoamLmHistoryAvailStatsBackwardMinFlr,
       "jnxSoamLmHistoryAvailStatsBackwardMaxFlr": jnxSoamLmHistoryAvailStatsBackwardMaxFlr,
       "jnxSoamLmHistoryAvailStatsBackwardAvgFlr": jnxSoamLmHistoryAvailStatsBackwardAvgFlr,
       "jnxSoamPmDmObjects": jnxSoamPmDmObjects,
       "jnxSoamDmCfgTable": jnxSoamDmCfgTable,
       "jnxSoamDmCfgEntry": jnxSoamDmCfgEntry,
       "jnxSoamDmCfgIndex": jnxSoamDmCfgIndex,
       "jnxSoamDmCfgType": jnxSoamDmCfgType,
       "jnxSoamDmCfgVersion": jnxSoamDmCfgVersion,
       "jnxSoamDmCfgEnabled": jnxSoamDmCfgEnabled,
       "jnxSoamDmCfgMeasurementEnable": jnxSoamDmCfgMeasurementEnable,
       "jnxSoamDmCfgMessagePeriod": jnxSoamDmCfgMessagePeriod,
       "jnxSoamDmCfgPriority": jnxSoamDmCfgPriority,
       "jnxSoamDmCfgFrameSize": jnxSoamDmCfgFrameSize,
       "jnxSoamDmCfgDataPattern": jnxSoamDmCfgDataPattern,
       "jnxSoamDmCfgTestTlvIncluded": jnxSoamDmCfgTestTlvIncluded,
       "jnxSoamDmCfgTestTlvPattern": jnxSoamDmCfgTestTlvPattern,
       "jnxSoamDmCfgNumIntervalsStored": jnxSoamDmCfgNumIntervalsStored,
       "jnxSoamDmCfgDestMepId": jnxSoamDmCfgDestMepId,
       "jnxSoamDmCfgDestIsMepId": jnxSoamDmCfgDestIsMepId,
       "jnxSoamDmCfgStartTimeType": jnxSoamDmCfgStartTimeType,
       "jnxSoamDmCfgRepetitionTime": jnxSoamDmCfgRepetitionTime,
       "jnxSoamDmCfgAlignMeasurementIntervals": jnxSoamDmCfgAlignMeasurementIntervals,
       "jnxSoamDmCfgInterFrameDelayVariationSelectionOffset": jnxSoamDmCfgInterFrameDelayVariationSelectionOffset,
       "jnxSoamDmCfgSessionType": jnxSoamDmCfgSessionType,
       "jnxSoamDmCfgSessionStatus": jnxSoamDmCfgSessionStatus,
       "jnxSoamDmCfgHistoryClear": jnxSoamDmCfgHistoryClear,
       "jnxSoamDmCfgRowStatus": jnxSoamDmCfgRowStatus,
       "jnxSoamDmCfgMeasurementInterval": jnxSoamDmCfgMeasurementInterval,
       "jnxSoamDmCfgDestMacAddress": jnxSoamDmCfgDestMacAddress,
       "jnxSoamDmCfgSourceMacAddress": jnxSoamDmCfgSourceMacAddress,
       "jnxSoamDmCfgFixedStartDateAndTime": jnxSoamDmCfgFixedStartDateAndTime,
       "jnxSoamDmCfgRelativeStartTime": jnxSoamDmCfgRelativeStartTime,
       "jnxSoamDmCfgStopTimeType": jnxSoamDmCfgStopTimeType,
       "jnxSoamDmCfgFixedStopDateAndTime": jnxSoamDmCfgFixedStopDateAndTime,
       "jnxSoamDmCfgRelativeStopTime": jnxSoamDmCfgRelativeStopTime,
       "jnxSoamDmCfgAlignMeasurementOffset": jnxSoamDmCfgAlignMeasurementOffset,
       "jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval": jnxSoamDmCfgNumMeasBinsPerFrameDelayInterval,
       "jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval": jnxSoamDmCfgNumMeasBinsPerInterFrameDelayVariationInterval,
       "jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval": jnxSoamDmCfgNumMeasBinsPerFrameDelayRangeInterval,
       "jnxSoamDmMeasuredStatsTable": jnxSoamDmMeasuredStatsTable,
       "jnxSoamDmMeasuredStatsEntry": jnxSoamDmMeasuredStatsEntry,
       "jnxSoamDmMeasuredStatsFrameDelayTwoWay": jnxSoamDmMeasuredStatsFrameDelayTwoWay,
       "jnxSoamDmMeasuredStatsFrameDelayForward": jnxSoamDmMeasuredStatsFrameDelayForward,
       "jnxSoamDmMeasuredStatsFrameDelayBackward": jnxSoamDmMeasuredStatsFrameDelayBackward,
       "jnxSoamDmMeasuredStatsIfdvTwoWay": jnxSoamDmMeasuredStatsIfdvTwoWay,
       "jnxSoamDmMeasuredStatsIfdvForward": jnxSoamDmMeasuredStatsIfdvForward,
       "jnxSoamDmMeasuredStatsIfdvBackward": jnxSoamDmMeasuredStatsIfdvBackward,
       "jnxSoamDmCurrentStatsTable": jnxSoamDmCurrentStatsTable,
       "jnxSoamDmCurrentStatsEntry": jnxSoamDmCurrentStatsEntry,
       "jnxSoamDmCurrentStatsIndex": jnxSoamDmCurrentStatsIndex,
       "jnxSoamDmCurrentStatsStartTime": jnxSoamDmCurrentStatsStartTime,
       "jnxSoamDmCurrentStatsElapsedTime": jnxSoamDmCurrentStatsElapsedTime,
       "jnxSoamDmCurrentStatsSuspect": jnxSoamDmCurrentStatsSuspect,
       "jnxSoamDmCurrentStatsFrameDelayTwoWayMin": jnxSoamDmCurrentStatsFrameDelayTwoWayMin,
       "jnxSoamDmCurrentStatsFrameDelayTwoWayMax": jnxSoamDmCurrentStatsFrameDelayTwoWayMax,
       "jnxSoamDmCurrentStatsFrameDelayTwoWayAvg": jnxSoamDmCurrentStatsFrameDelayTwoWayAvg,
       "jnxSoamDmCurrentStatsFrameDelayForwardMin": jnxSoamDmCurrentStatsFrameDelayForwardMin,
       "jnxSoamDmCurrentStatsFrameDelayForwardMax": jnxSoamDmCurrentStatsFrameDelayForwardMax,
       "jnxSoamDmCurrentStatsFrameDelayForwardAvg": jnxSoamDmCurrentStatsFrameDelayForwardAvg,
       "jnxSoamDmCurrentStatsFrameDelayBackwardMin": jnxSoamDmCurrentStatsFrameDelayBackwardMin,
       "jnxSoamDmCurrentStatsFrameDelayBackwardMax": jnxSoamDmCurrentStatsFrameDelayBackwardMax,
       "jnxSoamDmCurrentStatsFrameDelayBackwardAvg": jnxSoamDmCurrentStatsFrameDelayBackwardAvg,
       "jnxSoamDmCurrentStatsIfdvForwardMin": jnxSoamDmCurrentStatsIfdvForwardMin,
       "jnxSoamDmCurrentStatsIfdvForwardMax": jnxSoamDmCurrentStatsIfdvForwardMax,
       "jnxSoamDmCurrentStatsIfdvForwardAvg": jnxSoamDmCurrentStatsIfdvForwardAvg,
       "jnxSoamDmCurrentStatsIfdvBackwardMin": jnxSoamDmCurrentStatsIfdvBackwardMin,
       "jnxSoamDmCurrentStatsIfdvBackwardMax": jnxSoamDmCurrentStatsIfdvBackwardMax,
       "jnxSoamDmCurrentStatsIfdvBackwardAvg": jnxSoamDmCurrentStatsIfdvBackwardAvg,
       "jnxSoamDmCurrentStatsIfdvTwoWayMin": jnxSoamDmCurrentStatsIfdvTwoWayMin,
       "jnxSoamDmCurrentStatsIfdvTwoWayMax": jnxSoamDmCurrentStatsIfdvTwoWayMax,
       "jnxSoamDmCurrentStatsIfdvTwoWayAvg": jnxSoamDmCurrentStatsIfdvTwoWayAvg,
       "jnxSoamDmCurrentStatsSoamPdusSent": jnxSoamDmCurrentStatsSoamPdusSent,
       "jnxSoamDmCurrentStatsSoamPdusReceived": jnxSoamDmCurrentStatsSoamPdusReceived,
       "jnxSoamDmCurrentStatsFrameDelayRangeForwardMax": jnxSoamDmCurrentStatsFrameDelayRangeForwardMax,
       "jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg": jnxSoamDmCurrentStatsFrameDelayRangeForwardAvg,
       "jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax": jnxSoamDmCurrentStatsFrameDelayRangeBackwardMax,
       "jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg": jnxSoamDmCurrentStatsFrameDelayRangeBackwardAvg,
       "jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax": jnxSoamDmCurrentStatsFrameDelayRangeTwoWayMax,
       "jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg": jnxSoamDmCurrentStatsFrameDelayRangeTwoWayAvg,
       "jnxSoamDmHistoryStatsTable": jnxSoamDmHistoryStatsTable,
       "jnxSoamDmHistoryStatsEntry": jnxSoamDmHistoryStatsEntry,
       "jnxSoamDmHistoryStatsIndex": jnxSoamDmHistoryStatsIndex,
       "jnxSoamDmHistoryStatsEndTime": jnxSoamDmHistoryStatsEndTime,
       "jnxSoamDmHistoryStatsElapsedTime": jnxSoamDmHistoryStatsElapsedTime,
       "jnxSoamDmHistoryStatsSuspect": jnxSoamDmHistoryStatsSuspect,
       "jnxSoamDmHistoryStatsFrameDelayTwoWayMin": jnxSoamDmHistoryStatsFrameDelayTwoWayMin,
       "jnxSoamDmHistoryStatsFrameDelayTwoWayMax": jnxSoamDmHistoryStatsFrameDelayTwoWayMax,
       "jnxSoamDmHistoryStatsFrameDelayTwoWayAvg": jnxSoamDmHistoryStatsFrameDelayTwoWayAvg,
       "jnxSoamDmHistoryStatsFrameDelayForwardMin": jnxSoamDmHistoryStatsFrameDelayForwardMin,
       "jnxSoamDmHistoryStatsFrameDelayForwardMax": jnxSoamDmHistoryStatsFrameDelayForwardMax,
       "jnxSoamDmHistoryStatsFrameDelayForwardAvg": jnxSoamDmHistoryStatsFrameDelayForwardAvg,
       "jnxSoamDmHistoryStatsFrameDelayBackwardMin": jnxSoamDmHistoryStatsFrameDelayBackwardMin,
       "jnxSoamDmHistoryStatsFrameDelayBackwardMax": jnxSoamDmHistoryStatsFrameDelayBackwardMax,
       "jnxSoamDmHistoryStatsFrameDelayBackwardAvg": jnxSoamDmHistoryStatsFrameDelayBackwardAvg,
       "jnxSoamDmHistoryStatsIfdvForwardMin": jnxSoamDmHistoryStatsIfdvForwardMin,
       "jnxSoamDmHistoryStatsIfdvForwardMax": jnxSoamDmHistoryStatsIfdvForwardMax,
       "jnxSoamDmHistoryStatsIfdvForwardAvg": jnxSoamDmHistoryStatsIfdvForwardAvg,
       "jnxSoamDmHistoryStatsIfdvBackwardMin": jnxSoamDmHistoryStatsIfdvBackwardMin,
       "jnxSoamDmHistoryStatsIfdvBackwardMax": jnxSoamDmHistoryStatsIfdvBackwardMax,
       "jnxSoamDmHistoryStatsIfdvBackwardAvg": jnxSoamDmHistoryStatsIfdvBackwardAvg,
       "jnxSoamDmHistoryStatsIfdvTwoWayMin": jnxSoamDmHistoryStatsIfdvTwoWayMin,
       "jnxSoamDmHistoryStatsIfdvTwoWayMax": jnxSoamDmHistoryStatsIfdvTwoWayMax,
       "jnxSoamDmHistoryStatsIfdvTwoWayAvg": jnxSoamDmHistoryStatsIfdvTwoWayAvg,
       "jnxSoamDmHistoryStatsSoamPdusSent": jnxSoamDmHistoryStatsSoamPdusSent,
       "jnxSoamDmHistoryStatsSoamPdusReceived": jnxSoamDmHistoryStatsSoamPdusReceived,
       "jnxSoamDmHistoryStatsFrameDelayRangeForwardMax": jnxSoamDmHistoryStatsFrameDelayRangeForwardMax,
       "jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg": jnxSoamDmHistoryStatsFrameDelayRangeForwardAvg,
       "jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax": jnxSoamDmHistoryStatsFrameDelayRangeBackwardMax,
       "jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg": jnxSoamDmHistoryStatsFrameDelayRangeBackwardAvg,
       "jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax": jnxSoamDmHistoryStatsFrameDelayRangeTwoWayMax,
       "jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg": jnxSoamDmHistoryStatsFrameDelayRangeTwoWayAvg,
       "jnxSoamDmThresholdCfgTable": jnxSoamDmThresholdCfgTable,
       "jnxSoamDmThresholdCfgEntry": jnxSoamDmThresholdCfgEntry,
       "jnxSoamDmThresholdCfgIndex": jnxSoamDmThresholdCfgIndex,
       "jnxSoamDmThresholdCfgEnable": jnxSoamDmThresholdCfgEnable,
       "jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold": jnxSoamDmThresholdCfgAvgFrameDelayTwoWayThreshold,
       "jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold": jnxSoamDmThresholdCfgAvgIfdvTwoWayThreshold,
       "jnxSoamDmThresholdCfgRowStatus": jnxSoamDmThresholdCfgRowStatus,
       "jnxSoamDmCfgMeasBinTable": jnxSoamDmCfgMeasBinTable,
       "jnxSoamDmCfgMeasBinEntry": jnxSoamDmCfgMeasBinEntry,
       "jnxSoamDmCfgMeasBinType": jnxSoamDmCfgMeasBinType,
       "jnxSoamDmCfgMeasBinNumber": jnxSoamDmCfgMeasBinNumber,
       "jnxSoamDmCfgMeasBinLowerBound": jnxSoamDmCfgMeasBinLowerBound,
       "jnxSoamDmCurrentStatsBinsTable": jnxSoamDmCurrentStatsBinsTable,
       "jnxSoamDmCurrentStatsBinsEntry": jnxSoamDmCurrentStatsBinsEntry,
       "jnxSoamDmCurrentStatsBinsCounter": jnxSoamDmCurrentStatsBinsCounter,
       "jnxSoamDmHistoryStatsBinsTable": jnxSoamDmHistoryStatsBinsTable,
       "jnxSoamDmHistoryStatsBinsEntry": jnxSoamDmHistoryStatsBinsEntry,
       "jnxSoamDmHistoryStatsBinsCounter": jnxSoamDmHistoryStatsBinsCounter,
       "jnxSoamPmNotificationCfg": jnxSoamPmNotificationCfg,
       "jnxSoamPmNotificationObj": jnxSoamPmNotificationObj,
       "jnxSoamPmNotificationObjDateAndTime": jnxSoamPmNotificationObjDateAndTime,
       "jnxSoamPmNotificationObjThresholdId": jnxSoamPmNotificationObjThresholdId,
       "jnxSoamPmNotificationObjThresholdConfig": jnxSoamPmNotificationObjThresholdConfig,
       "jnxSoamPmNotificationObjThresholdValue": jnxSoamPmNotificationObjThresholdValue,
       "jnxSoamPmNotificationObjSuspect": jnxSoamPmNotificationObjSuspect,
       "jnxSoamPmNotificationObjCrossingType": jnxSoamPmNotificationObjCrossingType,
       "jnxSoamPmNotificationObjDestinationMep": jnxSoamPmNotificationObjDestinationMep,
       "jnxSoamPmNotificationObjPriority": jnxSoamPmNotificationObjPriority,
       "jnxSoamPmNotificationTotalFlaps": jnxSoamPmNotificationTotalFlaps,
       "jnxSoamPmNotificationAccTotalFlaps": jnxSoamPmNotificationAccTotalFlaps,
       "jnxSoamPmNotificationObjThresholdLastValue": jnxSoamPmNotificationObjThresholdLastValue,
       "jnxSoamPmNotificationObjCurrentState": jnxSoamPmNotificationObjCurrentState,
       "jnxSoamPmNotificationObjLastDateAndTime": jnxSoamPmNotificationObjLastDateAndTime,
       "jnxSoamPmMibConformance": jnxSoamPmMibConformance}
)
