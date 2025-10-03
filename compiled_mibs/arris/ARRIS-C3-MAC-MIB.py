# SNMP MIB module (ARRIS-C3-MAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-MAC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:04 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

(TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB",
    "TenthdBmV")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

cmtsC3MACMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6)
)
if mibBuilder.loadTexts:
    cmtsC3MACMIB.setRevisions(
        ("2004-11-21 00:00",
         "2004-11-26 00:00",
         "2004-12-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DocsisMacType(TextualConvention, Integer32):
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
        *(("docsis", 1),
          ("euroDocsis", 2),
          ("mixed", 3),
          ("custom", 4))
    )



# MIB Managed Objects in the order of their OIDs

_DcxMACObjects_ObjectIdentity = ObjectIdentity
dcxMACObjects = _DcxMACObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1)
)
_DcxMACCmtsMacTable_Object = MibTable
dcxMACCmtsMacTable = _DcxMACCmtsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    dcxMACCmtsMacTable.setStatus("current")
_DcxMACCmtsMacEntry_Object = MibTableRow
dcxMACCmtsMacEntry = _DcxMACCmtsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1)
)
dcxMACCmtsMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dcxMACCmtsMacEntry.setStatus("current")
_DcxMACCmtsMacMode_Type = DocsisMacType
_DcxMACCmtsMacMode_Object = MibTableColumn
dcxMACCmtsMacMode = _DcxMACCmtsMacMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 1),
    _DcxMACCmtsMacMode_Type()
)
dcxMACCmtsMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACCmtsMacMode.setStatus("current")


class _DcxMACCableAdvanceType_Type(Integer32):
    """Custom type dcxMACCableAdvanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_DcxMACCableAdvanceType_Type.__name__ = "Integer32"
_DcxMACCableAdvanceType_Object = MibTableColumn
dcxMACCableAdvanceType = _DcxMACCableAdvanceType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 2),
    _DcxMACCableAdvanceType_Type()
)
dcxMACCableAdvanceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACCableAdvanceType.setStatus("current")


class _DcxMACPlantLength_Type(Unsigned32):
    """Custom type dcxMACPlantLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 161),
    )


_DcxMACPlantLength_Type.__name__ = "Unsigned32"
_DcxMACPlantLength_Object = MibTableColumn
dcxMACPlantLength = _DcxMACPlantLength_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 3),
    _DcxMACPlantLength_Type()
)
dcxMACPlantLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACPlantLength.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACPlantLength.setUnits("kilometers")


class _DcxMACFlapAgingTime_Type(Unsigned32):
    """Custom type dcxMACFlapAgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 864000),
    )


_DcxMACFlapAgingTime_Type.__name__ = "Unsigned32"
_DcxMACFlapAgingTime_Object = MibTableColumn
dcxMACFlapAgingTime = _DcxMACFlapAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 4),
    _DcxMACFlapAgingTime_Type()
)
dcxMACFlapAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACFlapAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACFlapAgingTime.setUnits("seconds")


class _DcxMACFlapInsertTime_Type(Unsigned32):
    """Custom type dcxMACFlapInsertTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DcxMACFlapInsertTime_Type.__name__ = "Unsigned32"
_DcxMACFlapInsertTime_Object = MibTableColumn
dcxMACFlapInsertTime = _DcxMACFlapInsertTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 5),
    _DcxMACFlapInsertTime_Type()
)
dcxMACFlapInsertTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACFlapInsertTime.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACFlapInsertTime.setUnits("seconds")


class _DcxMACFlapMissThresh_Type(Unsigned32):
    """Custom type dcxMACFlapMissThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_DcxMACFlapMissThresh_Type.__name__ = "Unsigned32"
_DcxMACFlapMissThresh_Object = MibTableColumn
dcxMACFlapMissThresh = _DcxMACFlapMissThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 6),
    _DcxMACFlapMissThresh_Type()
)
dcxMACFlapMissThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACFlapMissThresh.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACFlapMissThresh.setUnits("misses")


class _DcxMACFlapListSize_Type(Unsigned32):
    """Custom type dcxMACFlapListSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_DcxMACFlapListSize_Type.__name__ = "Unsigned32"
_DcxMACFlapListSize_Object = MibTableColumn
dcxMACFlapListSize = _DcxMACFlapListSize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 8),
    _DcxMACFlapListSize_Type()
)
dcxMACFlapListSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACFlapListSize.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACFlapListSize.setUnits("entries")


class _DcxMACCmOfflineAgingTime_Type(Unsigned32):
    """Custom type dcxMACCmOfflineAgingTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 864000),
    )


_DcxMACCmOfflineAgingTime_Type.__name__ = "Unsigned32"
_DcxMACCmOfflineAgingTime_Object = MibTableColumn
dcxMACCmOfflineAgingTime = _DcxMACCmOfflineAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 9),
    _DcxMACCmOfflineAgingTime_Type()
)
dcxMACCmOfflineAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACCmOfflineAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACCmOfflineAgingTime.setUnits("seconds")


class _DcxMACUccMaxFailedAttempts_Type(Unsigned32):
    """Custom type dcxMACUccMaxFailedAttempts based on Unsigned32"""
    defaultValue = 2


_DcxMACUccMaxFailedAttempts_Type.__name__ = "Unsigned32"
_DcxMACUccMaxFailedAttempts_Object = MibTableColumn
dcxMACUccMaxFailedAttempts = _DcxMACUccMaxFailedAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 1, 1, 10),
    _DcxMACUccMaxFailedAttempts_Type()
)
dcxMACUccMaxFailedAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUccMaxFailedAttempts.setStatus("current")
_DcxMACDownstreamChannelTable_Object = MibTable
dcxMACDownstreamChannelTable = _DcxMACDownstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    dcxMACDownstreamChannelTable.setStatus("current")
_DcxMACDownstreamChannelEntry_Object = MibTableRow
dcxMACDownstreamChannelEntry = _DcxMACDownstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1)
)
dcxMACDownstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dcxMACDownstreamChannelEntry.setStatus("current")
_DcxMACDownChannelMacMode_Type = DocsisMacType
_DcxMACDownChannelMacMode_Object = MibTableColumn
dcxMACDownChannelMacMode = _DcxMACDownChannelMacMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 1),
    _DcxMACDownChannelMacMode_Type()
)
dcxMACDownChannelMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACDownChannelMacMode.setStatus("current")


class _DcxMACDownChannelUpconverter_Type(Integer32):
    """Custom type dcxMACDownChannelUpconverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_DcxMACDownChannelUpconverter_Type.__name__ = "Integer32"
_DcxMACDownChannelUpconverter_Object = MibTableColumn
dcxMACDownChannelUpconverter = _DcxMACDownChannelUpconverter_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 2),
    _DcxMACDownChannelUpconverter_Type()
)
dcxMACDownChannelUpconverter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACDownChannelUpconverter.setStatus("current")


class _DcxMACDownChannelIfFrequency_Type(Integer32):
    """Custom type dcxMACDownChannelIfFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000000, 60000000),
    )


_DcxMACDownChannelIfFrequency_Type.__name__ = "Integer32"
_DcxMACDownChannelIfFrequency_Object = MibTableColumn
dcxMACDownChannelIfFrequency = _DcxMACDownChannelIfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 3),
    _DcxMACDownChannelIfFrequency_Type()
)
dcxMACDownChannelIfFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACDownChannelIfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACDownChannelIfFrequency.setUnits("hertz")


class _DcxMACDownChannelWirelessMode_Type(Integer32):
    """Custom type dcxMACDownChannelWirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_DcxMACDownChannelWirelessMode_Type.__name__ = "Integer32"
_DcxMACDownChannelWirelessMode_Object = MibTableColumn
dcxMACDownChannelWirelessMode = _DcxMACDownChannelWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 4),
    _DcxMACDownChannelWirelessMode_Type()
)
dcxMACDownChannelWirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACDownChannelWirelessMode.setStatus("current")


class _DcxMACDownChannelSymbolRate_Type(Integer32):
    """Custom type dcxMACDownChannelSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1250000, 6952000),
    )


_DcxMACDownChannelSymbolRate_Type.__name__ = "Integer32"
_DcxMACDownChannelSymbolRate_Object = MibTableColumn
dcxMACDownChannelSymbolRate = _DcxMACDownChannelSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 5),
    _DcxMACDownChannelSymbolRate_Type()
)
dcxMACDownChannelSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACDownChannelSymbolRate.setStatus("current")
_DcxMACDownChannelAlpha_Type = Integer32
_DcxMACDownChannelAlpha_Object = MibTableColumn
dcxMACDownChannelAlpha = _DcxMACDownChannelAlpha_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 2, 1, 6),
    _DcxMACDownChannelAlpha_Type()
)
dcxMACDownChannelAlpha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxMACDownChannelAlpha.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACDownChannelAlpha.setUnits("percent")
_DcxMACUpstreamChannelTable_Object = MibTable
dcxMACUpstreamChannelTable = _DcxMACUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3)
)
if mibBuilder.loadTexts:
    dcxMACUpstreamChannelTable.setStatus("current")
_DcxMACUpstreamChannelEntry_Object = MibTableRow
dcxMACUpstreamChannelEntry = _DcxMACUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1)
)
dcxMACUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dcxMACUpstreamChannelEntry.setStatus("current")
_DcxMACUpChannelMacMode_Type = DocsisMacType
_DcxMACUpChannelMacMode_Object = MibTableColumn
dcxMACUpChannelMacMode = _DcxMACUpChannelMacMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 1),
    _DcxMACUpChannelMacMode_Type()
)
dcxMACUpChannelMacMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelMacMode.setStatus("current")
_DcxMACUpChannelAmpAttenuation_Type = TenthdBmV
_DcxMACUpChannelAmpAttenuation_Object = MibTableColumn
dcxMACUpChannelAmpAttenuation = _DcxMACUpChannelAmpAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 2),
    _DcxMACUpChannelAmpAttenuation_Type()
)
dcxMACUpChannelAmpAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelAmpAttenuation.setStatus("current")


class _DcxMACUpChannelIngressCancellation_Type(Integer32):
    """Custom type dcxMACUpChannelIngressCancellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("tdmaOnly", 2),
          ("scdmaSec", 3),
          ("scdmaInc1", 4),
          ("scdmaInc2", 5))
    )


_DcxMACUpChannelIngressCancellation_Type.__name__ = "Integer32"
_DcxMACUpChannelIngressCancellation_Object = MibTableColumn
dcxMACUpChannelIngressCancellation = _DcxMACUpChannelIngressCancellation_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 3),
    _DcxMACUpChannelIngressCancellation_Type()
)
dcxMACUpChannelIngressCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelIngressCancellation.setStatus("current")
_DcxMACUpChannelGroupId_Type = Unsigned32
_DcxMACUpChannelGroupId_Object = MibTableColumn
dcxMACUpChannelGroupId = _DcxMACUpChannelGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 4),
    _DcxMACUpChannelGroupId_Type()
)
dcxMACUpChannelGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelGroupId.setStatus("current")


class _DcxMACUpChannelShortPollInterval_Type(TimeInterval):
    """Custom type dcxMACUpChannelShortPollInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DcxMACUpChannelShortPollInterval_Type.__name__ = "TimeInterval"
_DcxMACUpChannelShortPollInterval_Object = MibTableColumn
dcxMACUpChannelShortPollInterval = _DcxMACUpChannelShortPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 5),
    _DcxMACUpChannelShortPollInterval_Type()
)
dcxMACUpChannelShortPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelShortPollInterval.setStatus("current")


class _DcxMACUpChannelPeriodicPollInterval_Type(TimeInterval):
    """Custom type dcxMACUpChannelPeriodicPollInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_DcxMACUpChannelPeriodicPollInterval_Type.__name__ = "TimeInterval"
_DcxMACUpChannelPeriodicPollInterval_Object = MibTableColumn
dcxMACUpChannelPeriodicPollInterval = _DcxMACUpChannelPeriodicPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 6),
    _DcxMACUpChannelPeriodicPollInterval_Type()
)
dcxMACUpChannelPeriodicPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelPeriodicPollInterval.setStatus("current")


class _DcxMACUpChannelInputPowerMode_Type(Integer32):
    """Custom type dcxMACUpChannelInputPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("automatic", 2))
    )


_DcxMACUpChannelInputPowerMode_Type.__name__ = "Integer32"
_DcxMACUpChannelInputPowerMode_Object = MibTableColumn
dcxMACUpChannelInputPowerMode = _DcxMACUpChannelInputPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 7),
    _DcxMACUpChannelInputPowerMode_Type()
)
dcxMACUpChannelInputPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelInputPowerMode.setStatus("current")
_DcxMACUpChannelPower_Type = TenthdBmV
_DcxMACUpChannelPower_Object = MibTableColumn
dcxMACUpChannelPower = _DcxMACUpChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 8),
    _DcxMACUpChannelPower_Type()
)
dcxMACUpChannelPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelPower.setStatus("current")


class _DcxMACUpChannelPlantLength_Type(Unsigned32):
    """Custom type dcxMACUpChannelPlantLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 320),
    )


_DcxMACUpChannelPlantLength_Type.__name__ = "Unsigned32"
_DcxMACUpChannelPlantLength_Object = MibTableColumn
dcxMACUpChannelPlantLength = _DcxMACUpChannelPlantLength_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 9),
    _DcxMACUpChannelPlantLength_Type()
)
dcxMACUpChannelPlantLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelPlantLength.setStatus("current")


class _DcxMACUpChannelMaxCmMapProcTime_Type(Unsigned32):
    """Custom type dcxMACUpChannelMaxCmMapProcTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_DcxMACUpChannelMaxCmMapProcTime_Type.__name__ = "Unsigned32"
_DcxMACUpChannelMaxCmMapProcTime_Object = MibTableColumn
dcxMACUpChannelMaxCmMapProcTime = _DcxMACUpChannelMaxCmMapProcTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 10),
    _DcxMACUpChannelMaxCmMapProcTime_Type()
)
dcxMACUpChannelMaxCmMapProcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelMaxCmMapProcTime.setStatus("current")
_DcxMACUpChannelConcatenation_Type = TruthValue
_DcxMACUpChannelConcatenation_Object = MibTableColumn
dcxMACUpChannelConcatenation = _DcxMACUpChannelConcatenation_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 11),
    _DcxMACUpChannelConcatenation_Type()
)
dcxMACUpChannelConcatenation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelConcatenation.setStatus("current")


class _DcxMACUpChannelSpMgtTriggerIndex_Type(Unsigned32):
    """Custom type dcxMACUpChannelSpMgtTriggerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcxMACUpChannelSpMgtTriggerIndex_Type.__name__ = "Unsigned32"
_DcxMACUpChannelSpMgtTriggerIndex_Object = MibTableColumn
dcxMACUpChannelSpMgtTriggerIndex = _DcxMACUpChannelSpMgtTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 12),
    _DcxMACUpChannelSpMgtTriggerIndex_Type()
)
dcxMACUpChannelSpMgtTriggerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelSpMgtTriggerIndex.setStatus("current")


class _DcxMACUpChannelLowPowerOffset_Type(TenthdBmV):
    """Custom type dcxMACUpChannelLowPowerOffset based on TenthdBmV"""
    defaultValue = -60

    subtypeSpec = TenthdBmV.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -10),
    )


_DcxMACUpChannelLowPowerOffset_Type.__name__ = "TenthdBmV"
_DcxMACUpChannelLowPowerOffset_Object = MibTableColumn
dcxMACUpChannelLowPowerOffset = _DcxMACUpChannelLowPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 13),
    _DcxMACUpChannelLowPowerOffset_Type()
)
dcxMACUpChannelLowPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelLowPowerOffset.setStatus("current")


class _DcxMACUpChannelHighPowerOffset_Type(TenthdBmV):
    """Custom type dcxMACUpChannelHighPowerOffset based on TenthdBmV"""
    defaultValue = 60

    subtypeSpec = TenthdBmV.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_DcxMACUpChannelHighPowerOffset_Type.__name__ = "TenthdBmV"
_DcxMACUpChannelHighPowerOffset_Object = MibTableColumn
dcxMACUpChannelHighPowerOffset = _DcxMACUpChannelHighPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 14),
    _DcxMACUpChannelHighPowerOffset_Type()
)
dcxMACUpChannelHighPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelHighPowerOffset.setStatus("current")


class _DcxMACUpChannelLogSnrAveTimeconstant_Type(Unsigned32):
    """Custom type dcxMACUpChannelLogSnrAveTimeconstant based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_DcxMACUpChannelLogSnrAveTimeconstant_Type.__name__ = "Unsigned32"
_DcxMACUpChannelLogSnrAveTimeconstant_Object = MibTableColumn
dcxMACUpChannelLogSnrAveTimeconstant = _DcxMACUpChannelLogSnrAveTimeconstant_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 15),
    _DcxMACUpChannelLogSnrAveTimeconstant_Type()
)
dcxMACUpChannelLogSnrAveTimeconstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelLogSnrAveTimeconstant.setStatus("current")


class _DcxMACUpChannelImpulseMitigation_Type(Integer32):
    """Custom type dcxMACUpChannelImpulseMitigation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_DcxMACUpChannelImpulseMitigation_Type.__name__ = "Integer32"
_DcxMACUpChannelImpulseMitigation_Object = MibTableColumn
dcxMACUpChannelImpulseMitigation = _DcxMACUpChannelImpulseMitigation_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 16),
    _DcxMACUpChannelImpulseMitigation_Type()
)
dcxMACUpChannelImpulseMitigation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelImpulseMitigation.setStatus("current")
_DcxMACUpChannelRngPreambleGuardSymbols_Type = Unsigned32
_DcxMACUpChannelRngPreambleGuardSymbols_Object = MibTableColumn
dcxMACUpChannelRngPreambleGuardSymbols = _DcxMACUpChannelRngPreambleGuardSymbols_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 17),
    _DcxMACUpChannelRngPreambleGuardSymbols_Type()
)
dcxMACUpChannelRngPreambleGuardSymbols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelRngPreambleGuardSymbols.setStatus("current")
_DcxMACUpChannelNrngPreambleGuardSymbols_Type = Unsigned32
_DcxMACUpChannelNrngPreambleGuardSymbols_Object = MibTableColumn
dcxMACUpChannelNrngPreambleGuardSymbols = _DcxMACUpChannelNrngPreambleGuardSymbols_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 18),
    _DcxMACUpChannelNrngPreambleGuardSymbols_Type()
)
dcxMACUpChannelNrngPreambleGuardSymbols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelNrngPreambleGuardSymbols.setStatus("current")


class _DcxMACUpChannelExtendedFrequencyErrorDetect_Type(Integer32):
    """Custom type dcxMACUpChannelExtendedFrequencyErrorDetect based on Integer32"""
    defaultValue = 0

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
          ("initialRanging", 1),
          ("periodicRanging", 2),
          ("allRanging", 3))
    )


_DcxMACUpChannelExtendedFrequencyErrorDetect_Type.__name__ = "Integer32"
_DcxMACUpChannelExtendedFrequencyErrorDetect_Object = MibTableColumn
dcxMACUpChannelExtendedFrequencyErrorDetect = _DcxMACUpChannelExtendedFrequencyErrorDetect_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 19),
    _DcxMACUpChannelExtendedFrequencyErrorDetect_Type()
)
dcxMACUpChannelExtendedFrequencyErrorDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelExtendedFrequencyErrorDetect.setStatus("current")
_DcxMACUpChannelLogC3SnrTimeconstant_Type = Unsigned32
_DcxMACUpChannelLogC3SnrTimeconstant_Object = MibTableColumn
dcxMACUpChannelLogC3SnrTimeconstant = _DcxMACUpChannelLogC3SnrTimeconstant_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 20),
    _DcxMACUpChannelLogC3SnrTimeconstant_Type()
)
dcxMACUpChannelLogC3SnrTimeconstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelLogC3SnrTimeconstant.setStatus("current")
_DcxMACUpChannelSignalNoise_Type = TenthdB
_DcxMACUpChannelSignalNoise_Object = MibTableColumn
dcxMACUpChannelSignalNoise = _DcxMACUpChannelSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 21),
    _DcxMACUpChannelSignalNoise_Type()
)
dcxMACUpChannelSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxMACUpChannelSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACUpChannelSignalNoise.setUnits("dB")
_DcxMACUpChannelSafeConfig_Type = TruthValue
_DcxMACUpChannelSafeConfig_Object = MibTableColumn
dcxMACUpChannelSafeConfig = _DcxMACUpChannelSafeConfig_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 22),
    _DcxMACUpChannelSafeConfig_Type()
)
dcxMACUpChannelSafeConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelSafeConfig.setStatus("current")


class _DcxMACUpChannelInitialRangingDelay_Type(Unsigned32):
    """Custom type dcxMACUpChannelInitialRangingDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3000),
    )


_DcxMACUpChannelInitialRangingDelay_Type.__name__ = "Unsigned32"
_DcxMACUpChannelInitialRangingDelay_Object = MibTableColumn
dcxMACUpChannelInitialRangingDelay = _DcxMACUpChannelInitialRangingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 3, 1, 23),
    _DcxMACUpChannelInitialRangingDelay_Type()
)
dcxMACUpChannelInitialRangingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxMACUpChannelInitialRangingDelay.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACUpChannelInitialRangingDelay.setUnits("microseconds")
_DcxMACUpstreamGroupTable_Object = MibTable
dcxMACUpstreamGroupTable = _DcxMACUpstreamGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4)
)
if mibBuilder.loadTexts:
    dcxMACUpstreamGroupTable.setStatus("current")
_DcxMACUpstreamGroupEntry_Object = MibTableRow
dcxMACUpstreamGroupEntry = _DcxMACUpstreamGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1)
)
dcxMACUpstreamGroupEntry.setIndexNames(
    (0, "ARRIS-C3-MAC-MIB", "dcxMACUpstreamGroupId"),
)
if mibBuilder.loadTexts:
    dcxMACUpstreamGroupEntry.setStatus("current")


class _DcxMACUpstreamGroupId_Type(Unsigned32):
    """Custom type dcxMACUpstreamGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DcxMACUpstreamGroupId_Type.__name__ = "Unsigned32"
_DcxMACUpstreamGroupId_Object = MibTableColumn
dcxMACUpstreamGroupId = _DcxMACUpstreamGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 1),
    _DcxMACUpstreamGroupId_Type()
)
dcxMACUpstreamGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxMACUpstreamGroupId.setStatus("current")


class _DcxMACUpstreamGroupName_Type(OctetString):
    """Custom type dcxMACUpstreamGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_DcxMACUpstreamGroupName_Type.__name__ = "OctetString"
_DcxMACUpstreamGroupName_Object = MibTableColumn
dcxMACUpstreamGroupName = _DcxMACUpstreamGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 2),
    _DcxMACUpstreamGroupName_Type()
)
dcxMACUpstreamGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACUpstreamGroupName.setStatus("current")


class _DcxMACUpstreamGroupLoadBalancing_Type(Integer32):
    """Custom type dcxMACUpstreamGroupLoadBalancing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("initialNumeric", 2),
          ("periodic", 3))
    )


_DcxMACUpstreamGroupLoadBalancing_Type.__name__ = "Integer32"
_DcxMACUpstreamGroupLoadBalancing_Object = MibTableColumn
dcxMACUpstreamGroupLoadBalancing = _DcxMACUpstreamGroupLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 3),
    _DcxMACUpstreamGroupLoadBalancing_Type()
)
dcxMACUpstreamGroupLoadBalancing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACUpstreamGroupLoadBalancing.setStatus("current")


class _DcxMACUpstreamGroupFrequencyIndex_Type(Unsigned32):
    """Custom type dcxMACUpstreamGroupFrequencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcxMACUpstreamGroupFrequencyIndex_Type.__name__ = "Unsigned32"
_DcxMACUpstreamGroupFrequencyIndex_Object = MibTableColumn
dcxMACUpstreamGroupFrequencyIndex = _DcxMACUpstreamGroupFrequencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 4),
    _DcxMACUpstreamGroupFrequencyIndex_Type()
)
dcxMACUpstreamGroupFrequencyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACUpstreamGroupFrequencyIndex.setStatus("current")


class _DcxMACUpstreamGroupSpMgtTriggerIndex_Type(Unsigned32):
    """Custom type dcxMACUpstreamGroupSpMgtTriggerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcxMACUpstreamGroupSpMgtTriggerIndex_Type.__name__ = "Unsigned32"
_DcxMACUpstreamGroupSpMgtTriggerIndex_Object = MibTableColumn
dcxMACUpstreamGroupSpMgtTriggerIndex = _DcxMACUpstreamGroupSpMgtTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 5),
    _DcxMACUpstreamGroupSpMgtTriggerIndex_Type()
)
dcxMACUpstreamGroupSpMgtTriggerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACUpstreamGroupSpMgtTriggerIndex.setStatus("current")
_DcxMACUpstreamGroupStatus_Type = RowStatus
_DcxMACUpstreamGroupStatus_Object = MibTableColumn
dcxMACUpstreamGroupStatus = _DcxMACUpstreamGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 4, 1, 6),
    _DcxMACUpstreamGroupStatus_Type()
)
dcxMACUpstreamGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACUpstreamGroupStatus.setStatus("current")
_DcxMACUpstreamFrequencyTable_Object = MibTable
dcxMACUpstreamFrequencyTable = _DcxMACUpstreamFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5)
)
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyTable.setStatus("current")
_DcxMACUpstreamFrequencyEntry_Object = MibTableRow
dcxMACUpstreamFrequencyEntry = _DcxMACUpstreamFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1)
)
dcxMACUpstreamFrequencyEntry.setIndexNames(
    (0, "ARRIS-C3-MAC-MIB", "dcxMACUpstreamFrequencyIndex"),
    (0, "ARRIS-C3-MAC-MIB", "dcxMACUpstreamFrequencyRegion"),
)
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyEntry.setStatus("current")


class _DcxMACUpstreamFrequencyIndex_Type(Unsigned32):
    """Custom type dcxMACUpstreamFrequencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DcxMACUpstreamFrequencyIndex_Type.__name__ = "Unsigned32"
_DcxMACUpstreamFrequencyIndex_Object = MibTableColumn
dcxMACUpstreamFrequencyIndex = _DcxMACUpstreamFrequencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 1),
    _DcxMACUpstreamFrequencyIndex_Type()
)
dcxMACUpstreamFrequencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyIndex.setStatus("current")


class _DcxMACUpstreamFrequencyRegion_Type(Unsigned32):
    """Custom type dcxMACUpstreamFrequencyRegion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DcxMACUpstreamFrequencyRegion_Type.__name__ = "Unsigned32"
_DcxMACUpstreamFrequencyRegion_Object = MibTableColumn
dcxMACUpstreamFrequencyRegion = _DcxMACUpstreamFrequencyRegion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 2),
    _DcxMACUpstreamFrequencyRegion_Type()
)
dcxMACUpstreamFrequencyRegion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyRegion.setStatus("current")
_DcxMACUpstreamFrequencyStart_Type = Integer32
_DcxMACUpstreamFrequencyStart_Object = MibTableColumn
dcxMACUpstreamFrequencyStart = _DcxMACUpstreamFrequencyStart_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 3),
    _DcxMACUpstreamFrequencyStart_Type()
)
dcxMACUpstreamFrequencyStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyStart.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyStart.setUnits("hertz")
_DcxMACUpstreamFrequencyStop_Type = Integer32
_DcxMACUpstreamFrequencyStop_Object = MibTableColumn
dcxMACUpstreamFrequencyStop = _DcxMACUpstreamFrequencyStop_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 4),
    _DcxMACUpstreamFrequencyStop_Type()
)
dcxMACUpstreamFrequencyStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyStop.setStatus("current")
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyStop.setUnits("hertz")
_DcxMACUpstreamFrequencyStatus_Type = RowStatus
_DcxMACUpstreamFrequencyStatus_Object = MibTableColumn
dcxMACUpstreamFrequencyStatus = _DcxMACUpstreamFrequencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 5, 1, 5),
    _DcxMACUpstreamFrequencyStatus_Type()
)
dcxMACUpstreamFrequencyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACUpstreamFrequencyStatus.setStatus("current")
_DcxMACSpectralMgtObjects_ObjectIdentity = ObjectIdentity
dcxMACSpectralMgtObjects = _DcxMACSpectralMgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6)
)
_DcxMACSpectralMgtTriggerTable_Object = MibTable
dcxMACSpectralMgtTriggerTable = _DcxMACSpectralMgtTriggerTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dcxMACSpectralMgtTriggerTable.setStatus("current")
_DcxMACSpectralMgtTriggerEntry_Object = MibTableRow
dcxMACSpectralMgtTriggerEntry = _DcxMACSpectralMgtTriggerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1)
)
dcxMACSpectralMgtTriggerEntry.setIndexNames(
    (0, "ARRIS-C3-MAC-MIB", "dcxMACSpMgtTriggerIndex"),
    (0, "ARRIS-C3-MAC-MIB", "dcxMACSpMgtTriggerNumber"),
)
if mibBuilder.loadTexts:
    dcxMACSpectralMgtTriggerEntry.setStatus("current")


class _DcxMACSpMgtTriggerIndex_Type(Unsigned32):
    """Custom type dcxMACSpMgtTriggerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcxMACSpMgtTriggerIndex_Type.__name__ = "Unsigned32"
_DcxMACSpMgtTriggerIndex_Object = MibTableColumn
dcxMACSpMgtTriggerIndex = _DcxMACSpMgtTriggerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 1),
    _DcxMACSpMgtTriggerIndex_Type()
)
dcxMACSpMgtTriggerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerIndex.setStatus("current")


class _DcxMACSpMgtTriggerNumber_Type(Unsigned32):
    """Custom type dcxMACSpMgtTriggerNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DcxMACSpMgtTriggerNumber_Type.__name__ = "Unsigned32"
_DcxMACSpMgtTriggerNumber_Object = MibTableColumn
dcxMACSpMgtTriggerNumber = _DcxMACSpMgtTriggerNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 2),
    _DcxMACSpMgtTriggerNumber_Type()
)
dcxMACSpMgtTriggerNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerNumber.setStatus("current")
_DcxMACSpMgtTriggerType_Type = Integer32
_DcxMACSpMgtTriggerType_Object = MibTableColumn
dcxMACSpMgtTriggerType = _DcxMACSpMgtTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 3),
    _DcxMACSpMgtTriggerType_Type()
)
dcxMACSpMgtTriggerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerType.setStatus("current")


class _DcxMACSpMgtTriggerAction_Type(Unsigned32):
    """Custom type dcxMACSpMgtTriggerAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DcxMACSpMgtTriggerAction_Type.__name__ = "Unsigned32"
_DcxMACSpMgtTriggerAction_Object = MibTableColumn
dcxMACSpMgtTriggerAction = _DcxMACSpMgtTriggerAction_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 4),
    _DcxMACSpMgtTriggerAction_Type()
)
dcxMACSpMgtTriggerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerAction.setStatus("current")
_DcxMACSpMgtTriggerParam1_Type = Integer32
_DcxMACSpMgtTriggerParam1_Object = MibTableColumn
dcxMACSpMgtTriggerParam1 = _DcxMACSpMgtTriggerParam1_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 5),
    _DcxMACSpMgtTriggerParam1_Type()
)
dcxMACSpMgtTriggerParam1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerParam1.setStatus("current")
_DcxMACSpMgtTriggerParam2_Type = Integer32
_DcxMACSpMgtTriggerParam2_Object = MibTableColumn
dcxMACSpMgtTriggerParam2 = _DcxMACSpMgtTriggerParam2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 6),
    _DcxMACSpMgtTriggerParam2_Type()
)
dcxMACSpMgtTriggerParam2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerParam2.setStatus("current")
_DcxMACSpMgtTriggerParam3_Type = Integer32
_DcxMACSpMgtTriggerParam3_Object = MibTableColumn
dcxMACSpMgtTriggerParam3 = _DcxMACSpMgtTriggerParam3_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 7),
    _DcxMACSpMgtTriggerParam3_Type()
)
dcxMACSpMgtTriggerParam3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerParam3.setStatus("current")
_DcxMACSpMgtTriggerParam4_Type = Integer32
_DcxMACSpMgtTriggerParam4_Object = MibTableColumn
dcxMACSpMgtTriggerParam4 = _DcxMACSpMgtTriggerParam4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 8),
    _DcxMACSpMgtTriggerParam4_Type()
)
dcxMACSpMgtTriggerParam4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerParam4.setStatus("current")
_DcxMACSpMgtTriggerParam5_Type = Integer32
_DcxMACSpMgtTriggerParam5_Object = MibTableColumn
dcxMACSpMgtTriggerParam5 = _DcxMACSpMgtTriggerParam5_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 9),
    _DcxMACSpMgtTriggerParam5_Type()
)
dcxMACSpMgtTriggerParam5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerParam5.setStatus("current")
_DcxMACSpMgtTriggerParam6_Type = Integer32
_DcxMACSpMgtTriggerParam6_Object = MibTableColumn
dcxMACSpMgtTriggerParam6 = _DcxMACSpMgtTriggerParam6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 10),
    _DcxMACSpMgtTriggerParam6_Type()
)
dcxMACSpMgtTriggerParam6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerParam6.setStatus("current")
_DcxMACSpMgtTriggerParam7_Type = Integer32
_DcxMACSpMgtTriggerParam7_Object = MibTableColumn
dcxMACSpMgtTriggerParam7 = _DcxMACSpMgtTriggerParam7_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 11),
    _DcxMACSpMgtTriggerParam7_Type()
)
dcxMACSpMgtTriggerParam7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerParam7.setStatus("current")
_DcxMACSpMgtTriggerParam8_Type = Integer32
_DcxMACSpMgtTriggerParam8_Object = MibTableColumn
dcxMACSpMgtTriggerParam8 = _DcxMACSpMgtTriggerParam8_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 12),
    _DcxMACSpMgtTriggerParam8_Type()
)
dcxMACSpMgtTriggerParam8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerParam8.setStatus("current")
_DcxMACSpMgtTriggerStatus_Type = RowStatus
_DcxMACSpMgtTriggerStatus_Object = MibTableColumn
dcxMACSpMgtTriggerStatus = _DcxMACSpMgtTriggerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 1, 1, 13),
    _DcxMACSpMgtTriggerStatus_Type()
)
dcxMACSpMgtTriggerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtTriggerStatus.setStatus("current")
_DcxMACSpectralMgtActionTable_Object = MibTable
dcxMACSpectralMgtActionTable = _DcxMACSpectralMgtActionTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dcxMACSpectralMgtActionTable.setStatus("current")
_DcxMACSpectralMgtActionEntry_Object = MibTableRow
dcxMACSpectralMgtActionEntry = _DcxMACSpectralMgtActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1)
)
dcxMACSpectralMgtActionEntry.setIndexNames(
    (0, "ARRIS-C3-MAC-MIB", "dcxMACSpMgtActionIndex"),
)
if mibBuilder.loadTexts:
    dcxMACSpectralMgtActionEntry.setStatus("current")


class _DcxMACSpMgtActionIndex_Type(Unsigned32):
    """Custom type dcxMACSpMgtActionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DcxMACSpMgtActionIndex_Type.__name__ = "Unsigned32"
_DcxMACSpMgtActionIndex_Object = MibTableColumn
dcxMACSpMgtActionIndex = _DcxMACSpMgtActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 1),
    _DcxMACSpMgtActionIndex_Type()
)
dcxMACSpMgtActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionIndex.setStatus("current")
_DcxMACSpMgtActionType_Type = Integer32
_DcxMACSpMgtActionType_Object = MibTableColumn
dcxMACSpMgtActionType = _DcxMACSpMgtActionType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 2),
    _DcxMACSpMgtActionType_Type()
)
dcxMACSpMgtActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionType.setStatus("current")
_DcxMACSpMgtActionParam1_Type = Integer32
_DcxMACSpMgtActionParam1_Object = MibTableColumn
dcxMACSpMgtActionParam1 = _DcxMACSpMgtActionParam1_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 3),
    _DcxMACSpMgtActionParam1_Type()
)
dcxMACSpMgtActionParam1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionParam1.setStatus("current")
_DcxMACSpMgtActionParam2_Type = Integer32
_DcxMACSpMgtActionParam2_Object = MibTableColumn
dcxMACSpMgtActionParam2 = _DcxMACSpMgtActionParam2_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 4),
    _DcxMACSpMgtActionParam2_Type()
)
dcxMACSpMgtActionParam2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionParam2.setStatus("current")
_DcxMACSpMgtActionParam3_Type = Integer32
_DcxMACSpMgtActionParam3_Object = MibTableColumn
dcxMACSpMgtActionParam3 = _DcxMACSpMgtActionParam3_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 5),
    _DcxMACSpMgtActionParam3_Type()
)
dcxMACSpMgtActionParam3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionParam3.setStatus("current")
_DcxMACSpMgtActionParam4_Type = Integer32
_DcxMACSpMgtActionParam4_Object = MibTableColumn
dcxMACSpMgtActionParam4 = _DcxMACSpMgtActionParam4_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 6),
    _DcxMACSpMgtActionParam4_Type()
)
dcxMACSpMgtActionParam4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionParam4.setStatus("current")
_DcxMACSpMgtActionParam5_Type = Integer32
_DcxMACSpMgtActionParam5_Object = MibTableColumn
dcxMACSpMgtActionParam5 = _DcxMACSpMgtActionParam5_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 7),
    _DcxMACSpMgtActionParam5_Type()
)
dcxMACSpMgtActionParam5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionParam5.setStatus("current")
_DcxMACSpMgtActionParam6_Type = Integer32
_DcxMACSpMgtActionParam6_Object = MibTableColumn
dcxMACSpMgtActionParam6 = _DcxMACSpMgtActionParam6_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 8),
    _DcxMACSpMgtActionParam6_Type()
)
dcxMACSpMgtActionParam6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionParam6.setStatus("current")
_DcxMACSpMgtActionParam7_Type = Integer32
_DcxMACSpMgtActionParam7_Object = MibTableColumn
dcxMACSpMgtActionParam7 = _DcxMACSpMgtActionParam7_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 9),
    _DcxMACSpMgtActionParam7_Type()
)
dcxMACSpMgtActionParam7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionParam7.setStatus("current")
_DcxMACSpMgtActionParam8_Type = Integer32
_DcxMACSpMgtActionParam8_Object = MibTableColumn
dcxMACSpMgtActionParam8 = _DcxMACSpMgtActionParam8_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 10),
    _DcxMACSpMgtActionParam8_Type()
)
dcxMACSpMgtActionParam8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionParam8.setStatus("current")
_DcxMACSpMgtActionStatus_Type = RowStatus
_DcxMACSpMgtActionStatus_Object = MibTableColumn
dcxMACSpMgtActionStatus = _DcxMACSpMgtActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 6, 2, 1, 11),
    _DcxMACSpMgtActionStatus_Type()
)
dcxMACSpMgtActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSpMgtActionStatus.setStatus("current")
_DcxMACSharedSecretTable_Object = MibTable
dcxMACSharedSecretTable = _DcxMACSharedSecretTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7)
)
if mibBuilder.loadTexts:
    dcxMACSharedSecretTable.setStatus("current")
_DcxMACSharedSecretEntry_Object = MibTableRow
dcxMACSharedSecretEntry = _DcxMACSharedSecretEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7, 1)
)
dcxMACSharedSecretEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARRIS-C3-MAC-MIB", "dcxMACSharedSecretId"),
)
if mibBuilder.loadTexts:
    dcxMACSharedSecretEntry.setStatus("current")


class _DcxMACSharedSecretId_Type(Integer32):
    """Custom type dcxMACSharedSecretId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcxMACSharedSecretId_Type.__name__ = "Integer32"
_DcxMACSharedSecretId_Object = MibTableColumn
dcxMACSharedSecretId = _DcxMACSharedSecretId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7, 1, 1),
    _DcxMACSharedSecretId_Type()
)
dcxMACSharedSecretId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxMACSharedSecretId.setStatus("current")
_DcxMACSharedSecretStr_Type = DisplayString
_DcxMACSharedSecretStr_Object = MibTableColumn
dcxMACSharedSecretStr = _DcxMACSharedSecretStr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7, 1, 2),
    _DcxMACSharedSecretStr_Type()
)
dcxMACSharedSecretStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSharedSecretStr.setStatus("current")
_DcxMACSharedSecretStatus_Type = RowStatus
_DcxMACSharedSecretStatus_Object = MibTableColumn
dcxMACSharedSecretStatus = _DcxMACSharedSecretStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 6, 1, 7, 1, 3),
    _DcxMACSharedSecretStatus_Type()
)
dcxMACSharedSecretStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dcxMACSharedSecretStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-MAC-MIB",
    **{"DocsisMacType": DocsisMacType,
       "cmtsC3MACMIB": cmtsC3MACMIB,
       "dcxMACObjects": dcxMACObjects,
       "dcxMACCmtsMacTable": dcxMACCmtsMacTable,
       "dcxMACCmtsMacEntry": dcxMACCmtsMacEntry,
       "dcxMACCmtsMacMode": dcxMACCmtsMacMode,
       "dcxMACCableAdvanceType": dcxMACCableAdvanceType,
       "dcxMACPlantLength": dcxMACPlantLength,
       "dcxMACFlapAgingTime": dcxMACFlapAgingTime,
       "dcxMACFlapInsertTime": dcxMACFlapInsertTime,
       "dcxMACFlapMissThresh": dcxMACFlapMissThresh,
       "dcxMACFlapListSize": dcxMACFlapListSize,
       "dcxMACCmOfflineAgingTime": dcxMACCmOfflineAgingTime,
       "dcxMACUccMaxFailedAttempts": dcxMACUccMaxFailedAttempts,
       "dcxMACDownstreamChannelTable": dcxMACDownstreamChannelTable,
       "dcxMACDownstreamChannelEntry": dcxMACDownstreamChannelEntry,
       "dcxMACDownChannelMacMode": dcxMACDownChannelMacMode,
       "dcxMACDownChannelUpconverter": dcxMACDownChannelUpconverter,
       "dcxMACDownChannelIfFrequency": dcxMACDownChannelIfFrequency,
       "dcxMACDownChannelWirelessMode": dcxMACDownChannelWirelessMode,
       "dcxMACDownChannelSymbolRate": dcxMACDownChannelSymbolRate,
       "dcxMACDownChannelAlpha": dcxMACDownChannelAlpha,
       "dcxMACUpstreamChannelTable": dcxMACUpstreamChannelTable,
       "dcxMACUpstreamChannelEntry": dcxMACUpstreamChannelEntry,
       "dcxMACUpChannelMacMode": dcxMACUpChannelMacMode,
       "dcxMACUpChannelAmpAttenuation": dcxMACUpChannelAmpAttenuation,
       "dcxMACUpChannelIngressCancellation": dcxMACUpChannelIngressCancellation,
       "dcxMACUpChannelGroupId": dcxMACUpChannelGroupId,
       "dcxMACUpChannelShortPollInterval": dcxMACUpChannelShortPollInterval,
       "dcxMACUpChannelPeriodicPollInterval": dcxMACUpChannelPeriodicPollInterval,
       "dcxMACUpChannelInputPowerMode": dcxMACUpChannelInputPowerMode,
       "dcxMACUpChannelPower": dcxMACUpChannelPower,
       "dcxMACUpChannelPlantLength": dcxMACUpChannelPlantLength,
       "dcxMACUpChannelMaxCmMapProcTime": dcxMACUpChannelMaxCmMapProcTime,
       "dcxMACUpChannelConcatenation": dcxMACUpChannelConcatenation,
       "dcxMACUpChannelSpMgtTriggerIndex": dcxMACUpChannelSpMgtTriggerIndex,
       "dcxMACUpChannelLowPowerOffset": dcxMACUpChannelLowPowerOffset,
       "dcxMACUpChannelHighPowerOffset": dcxMACUpChannelHighPowerOffset,
       "dcxMACUpChannelLogSnrAveTimeconstant": dcxMACUpChannelLogSnrAveTimeconstant,
       "dcxMACUpChannelImpulseMitigation": dcxMACUpChannelImpulseMitigation,
       "dcxMACUpChannelRngPreambleGuardSymbols": dcxMACUpChannelRngPreambleGuardSymbols,
       "dcxMACUpChannelNrngPreambleGuardSymbols": dcxMACUpChannelNrngPreambleGuardSymbols,
       "dcxMACUpChannelExtendedFrequencyErrorDetect": dcxMACUpChannelExtendedFrequencyErrorDetect,
       "dcxMACUpChannelLogC3SnrTimeconstant": dcxMACUpChannelLogC3SnrTimeconstant,
       "dcxMACUpChannelSignalNoise": dcxMACUpChannelSignalNoise,
       "dcxMACUpChannelSafeConfig": dcxMACUpChannelSafeConfig,
       "dcxMACUpChannelInitialRangingDelay": dcxMACUpChannelInitialRangingDelay,
       "dcxMACUpstreamGroupTable": dcxMACUpstreamGroupTable,
       "dcxMACUpstreamGroupEntry": dcxMACUpstreamGroupEntry,
       "dcxMACUpstreamGroupId": dcxMACUpstreamGroupId,
       "dcxMACUpstreamGroupName": dcxMACUpstreamGroupName,
       "dcxMACUpstreamGroupLoadBalancing": dcxMACUpstreamGroupLoadBalancing,
       "dcxMACUpstreamGroupFrequencyIndex": dcxMACUpstreamGroupFrequencyIndex,
       "dcxMACUpstreamGroupSpMgtTriggerIndex": dcxMACUpstreamGroupSpMgtTriggerIndex,
       "dcxMACUpstreamGroupStatus": dcxMACUpstreamGroupStatus,
       "dcxMACUpstreamFrequencyTable": dcxMACUpstreamFrequencyTable,
       "dcxMACUpstreamFrequencyEntry": dcxMACUpstreamFrequencyEntry,
       "dcxMACUpstreamFrequencyIndex": dcxMACUpstreamFrequencyIndex,
       "dcxMACUpstreamFrequencyRegion": dcxMACUpstreamFrequencyRegion,
       "dcxMACUpstreamFrequencyStart": dcxMACUpstreamFrequencyStart,
       "dcxMACUpstreamFrequencyStop": dcxMACUpstreamFrequencyStop,
       "dcxMACUpstreamFrequencyStatus": dcxMACUpstreamFrequencyStatus,
       "dcxMACSpectralMgtObjects": dcxMACSpectralMgtObjects,
       "dcxMACSpectralMgtTriggerTable": dcxMACSpectralMgtTriggerTable,
       "dcxMACSpectralMgtTriggerEntry": dcxMACSpectralMgtTriggerEntry,
       "dcxMACSpMgtTriggerIndex": dcxMACSpMgtTriggerIndex,
       "dcxMACSpMgtTriggerNumber": dcxMACSpMgtTriggerNumber,
       "dcxMACSpMgtTriggerType": dcxMACSpMgtTriggerType,
       "dcxMACSpMgtTriggerAction": dcxMACSpMgtTriggerAction,
       "dcxMACSpMgtTriggerParam1": dcxMACSpMgtTriggerParam1,
       "dcxMACSpMgtTriggerParam2": dcxMACSpMgtTriggerParam2,
       "dcxMACSpMgtTriggerParam3": dcxMACSpMgtTriggerParam3,
       "dcxMACSpMgtTriggerParam4": dcxMACSpMgtTriggerParam4,
       "dcxMACSpMgtTriggerParam5": dcxMACSpMgtTriggerParam5,
       "dcxMACSpMgtTriggerParam6": dcxMACSpMgtTriggerParam6,
       "dcxMACSpMgtTriggerParam7": dcxMACSpMgtTriggerParam7,
       "dcxMACSpMgtTriggerParam8": dcxMACSpMgtTriggerParam8,
       "dcxMACSpMgtTriggerStatus": dcxMACSpMgtTriggerStatus,
       "dcxMACSpectralMgtActionTable": dcxMACSpectralMgtActionTable,
       "dcxMACSpectralMgtActionEntry": dcxMACSpectralMgtActionEntry,
       "dcxMACSpMgtActionIndex": dcxMACSpMgtActionIndex,
       "dcxMACSpMgtActionType": dcxMACSpMgtActionType,
       "dcxMACSpMgtActionParam1": dcxMACSpMgtActionParam1,
       "dcxMACSpMgtActionParam2": dcxMACSpMgtActionParam2,
       "dcxMACSpMgtActionParam3": dcxMACSpMgtActionParam3,
       "dcxMACSpMgtActionParam4": dcxMACSpMgtActionParam4,
       "dcxMACSpMgtActionParam5": dcxMACSpMgtActionParam5,
       "dcxMACSpMgtActionParam6": dcxMACSpMgtActionParam6,
       "dcxMACSpMgtActionParam7": dcxMACSpMgtActionParam7,
       "dcxMACSpMgtActionParam8": dcxMACSpMgtActionParam8,
       "dcxMACSpMgtActionStatus": dcxMACSpMgtActionStatus,
       "dcxMACSharedSecretTable": dcxMACSharedSecretTable,
       "dcxMACSharedSecretEntry": dcxMACSharedSecretEntry,
       "dcxMACSharedSecretId": dcxMACSharedSecretId,
       "dcxMACSharedSecretStr": dcxMACSharedSecretStr,
       "dcxMACSharedSecretStatus": dcxMACSharedSecretStatus}
)
