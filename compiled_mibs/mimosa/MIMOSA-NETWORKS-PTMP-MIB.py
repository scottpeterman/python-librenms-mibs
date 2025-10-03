# SNMP MIB module (MIMOSA-NETWORKS-PTMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\mimosa\MIMOSA-NETWORKS-PTMP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:40 2025
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

(DecimalOne,
 DecimalTwo,
 Mimosa5GHzChannelNumber,
 Mimosa5GHzFrequency) = mibBuilder.importSymbols(
    "MIMOSA-MIB-TC",
    "DecimalOne",
    "DecimalTwo",
    "Mimosa5GHzChannelNumber",
    "Mimosa5GHzFrequency")

(mimosaConformanceGroup,
 mimosaWireless) = mibBuilder.importSymbols(
    "MIMOSA-NETWORKS-BASE-MIB",
    "mimosaConformanceGroup",
    "mimosaWireless")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mimosaPtmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9)
)
if mibBuilder.loadTexts:
    mimosaPtmp.setRevisions(
        ("2017-04-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MimosaPtmpSsid_ObjectIdentity = ObjectIdentity
mimosaPtmpSsid = _MimosaPtmpSsid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1)
)
_MimosaPtmpSsidTable_Object = MibTable
mimosaPtmpSsidTable = _MimosaPtmpSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    mimosaPtmpSsidTable.setStatus("current")
_MimosaPtmpSsidEntry_Object = MibTableRow
mimosaPtmpSsidEntry = _MimosaPtmpSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1)
)
mimosaPtmpSsidEntry.setIndexNames(
    (0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidIndex"),
)
if mibBuilder.loadTexts:
    mimosaPtmpSsidEntry.setStatus("current")


class _MimosaPtmpSsidIndex_Type(Integer32):
    """Custom type mimosaPtmpSsidIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_MimosaPtmpSsidIndex_Type.__name__ = "Integer32"
_MimosaPtmpSsidIndex_Object = MibTableColumn
mimosaPtmpSsidIndex = _MimosaPtmpSsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 1),
    _MimosaPtmpSsidIndex_Type()
)
mimosaPtmpSsidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mimosaPtmpSsidIndex.setStatus("current")


class _MimosaPtmpSsidName_Type(DisplayString):
    """Custom type mimosaPtmpSsidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MimosaPtmpSsidName_Type.__name__ = "DisplayString"
_MimosaPtmpSsidName_Object = MibTableColumn
mimosaPtmpSsidName = _MimosaPtmpSsidName_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 2),
    _MimosaPtmpSsidName_Type()
)
mimosaPtmpSsidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpSsidName.setStatus("current")


class _MimosaPtmpSsidType_Type(Integer32):
    """Custom type mimosaPtmpSsidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hotspot", 0),
          ("cpe", 1))
    )


_MimosaPtmpSsidType_Type.__name__ = "Integer32"
_MimosaPtmpSsidType_Object = MibTableColumn
mimosaPtmpSsidType = _MimosaPtmpSsidType_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 3),
    _MimosaPtmpSsidType_Type()
)
mimosaPtmpSsidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpSsidType.setStatus("current")
_MimosaPtmpSsidEnabled_Type = TruthValue
_MimosaPtmpSsidEnabled_Object = MibTableColumn
mimosaPtmpSsidEnabled = _MimosaPtmpSsidEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 4),
    _MimosaPtmpSsidEnabled_Type()
)
mimosaPtmpSsidEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpSsidEnabled.setStatus("current")
_MimosaPtmpSsidBroadcastEnabled_Type = TruthValue
_MimosaPtmpSsidBroadcastEnabled_Object = MibTableColumn
mimosaPtmpSsidBroadcastEnabled = _MimosaPtmpSsidBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 5),
    _MimosaPtmpSsidBroadcastEnabled_Type()
)
mimosaPtmpSsidBroadcastEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpSsidBroadcastEnabled.setStatus("current")
_MimosaPtmpSsidIsolationEnabled_Type = TruthValue
_MimosaPtmpSsidIsolationEnabled_Object = MibTableColumn
mimosaPtmpSsidIsolationEnabled = _MimosaPtmpSsidIsolationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 6),
    _MimosaPtmpSsidIsolationEnabled_Type()
)
mimosaPtmpSsidIsolationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpSsidIsolationEnabled.setStatus("current")
_MimosaPtmpLinkInfo_ObjectIdentity = ObjectIdentity
mimosaPtmpLinkInfo = _MimosaPtmpLinkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2)
)


class _MimosaPtmpWirelessMode_Type(Integer32):
    """Custom type mimosaPtmpWirelessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srs", 1),
          ("wifiinterop", 2))
    )


_MimosaPtmpWirelessMode_Type.__name__ = "Integer32"
_MimosaPtmpWirelessMode_Object = MibScalar
mimosaPtmpWirelessMode = _MimosaPtmpWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2, 1),
    _MimosaPtmpWirelessMode_Type()
)
mimosaPtmpWirelessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpWirelessMode.setStatus("current")


class _MimosaPtmpWirelessGender_Type(Integer32):
    """Custom type mimosaPtmpWirelessGender based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_MimosaPtmpWirelessGender_Type.__name__ = "Integer32"
_MimosaPtmpWirelessGender_Object = MibScalar
mimosaPtmpWirelessGender = _MimosaPtmpWirelessGender_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2, 2),
    _MimosaPtmpWirelessGender_Type()
)
mimosaPtmpWirelessGender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpWirelessGender.setStatus("current")
_MimosaPtmpWirelessTrafficSplit_Type = DisplayString
_MimosaPtmpWirelessTrafficSplit_Object = MibScalar
mimosaPtmpWirelessTrafficSplit = _MimosaPtmpWirelessTrafficSplit_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2, 3),
    _MimosaPtmpWirelessTrafficSplit_Type()
)
mimosaPtmpWirelessTrafficSplit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpWirelessTrafficSplit.setStatus("current")
_MimosaPtmpWirelessWindowLength_Type = Integer32
_MimosaPtmpWirelessWindowLength_Object = MibScalar
mimosaPtmpWirelessWindowLength = _MimosaPtmpWirelessWindowLength_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2, 4),
    _MimosaPtmpWirelessWindowLength_Type()
)
mimosaPtmpWirelessWindowLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpWirelessWindowLength.setStatus("current")
_MimosaPtmpChannelPower_ObjectIdentity = ObjectIdentity
mimosaPtmpChannelPower = _MimosaPtmpChannelPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3)
)
_MimosaPtmpAutoChannelEnabled_Type = TruthValue
_MimosaPtmpAutoChannelEnabled_Object = MibScalar
mimosaPtmpAutoChannelEnabled = _MimosaPtmpAutoChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 1),
    _MimosaPtmpAutoChannelEnabled_Type()
)
mimosaPtmpAutoChannelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpAutoChannelEnabled.setStatus("current")
_MimosaPtmpAntennaGain_Type = Unsigned32
_MimosaPtmpAntennaGain_Object = MibScalar
mimosaPtmpAntennaGain = _MimosaPtmpAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 2),
    _MimosaPtmpAntennaGain_Type()
)
mimosaPtmpAntennaGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpAntennaGain.setStatus("current")
_MimosaPtmpChannelPowerTable_Object = MibTable
mimosaPtmpChannelPowerTable = _MimosaPtmpChannelPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3)
)
if mibBuilder.loadTexts:
    mimosaPtmpChannelPowerTable.setStatus("current")
_MimosaPtmpChannelPowerEntry_Object = MibTableRow
mimosaPtmpChannelPowerEntry = _MimosaPtmpChannelPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1)
)
mimosaPtmpChannelPowerEntry.setIndexNames(
    (0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrRadioIndex"),
)
if mibBuilder.loadTexts:
    mimosaPtmpChannelPowerEntry.setStatus("current")
_MimosaPtmpChPwrRadioIndex_Type = Unsigned32
_MimosaPtmpChPwrRadioIndex_Object = MibTableColumn
mimosaPtmpChPwrRadioIndex = _MimosaPtmpChPwrRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 1),
    _MimosaPtmpChPwrRadioIndex_Type()
)
mimosaPtmpChPwrRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrRadioIndex.setStatus("current")


class _MimosaPtmpChPwrRadioName_Type(DisplayString):
    """Custom type mimosaPtmpChPwrRadioName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MimosaPtmpChPwrRadioName_Type.__name__ = "DisplayString"
_MimosaPtmpChPwrRadioName_Object = MibTableColumn
mimosaPtmpChPwrRadioName = _MimosaPtmpChPwrRadioName_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 2),
    _MimosaPtmpChPwrRadioName_Type()
)
mimosaPtmpChPwrRadioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrRadioName.setStatus("current")
_MimosaPtmpChPwrCntrFreqCfg_Type = Mimosa5GHzFrequency
_MimosaPtmpChPwrCntrFreqCfg_Object = MibTableColumn
mimosaPtmpChPwrCntrFreqCfg = _MimosaPtmpChPwrCntrFreqCfg_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 3),
    _MimosaPtmpChPwrCntrFreqCfg_Type()
)
mimosaPtmpChPwrCntrFreqCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrCntrFreqCfg.setStatus("current")
_MimosaPtmpChPwrPrimChannelCfg_Type = Mimosa5GHzChannelNumber
_MimosaPtmpChPwrPrimChannelCfg_Object = MibTableColumn
mimosaPtmpChPwrPrimChannelCfg = _MimosaPtmpChPwrPrimChannelCfg_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 4),
    _MimosaPtmpChPwrPrimChannelCfg_Type()
)
mimosaPtmpChPwrPrimChannelCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrPrimChannelCfg.setStatus("current")
_MimosaPtmpChPwrChWidthCfg_Type = Unsigned32
_MimosaPtmpChPwrChWidthCfg_Object = MibTableColumn
mimosaPtmpChPwrChWidthCfg = _MimosaPtmpChPwrChWidthCfg_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 5),
    _MimosaPtmpChPwrChWidthCfg_Type()
)
mimosaPtmpChPwrChWidthCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrChWidthCfg.setStatus("current")
_MimosaPtmpChPwrTxPowerCfg_Type = Integer32
_MimosaPtmpChPwrTxPowerCfg_Object = MibTableColumn
mimosaPtmpChPwrTxPowerCfg = _MimosaPtmpChPwrTxPowerCfg_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 6),
    _MimosaPtmpChPwrTxPowerCfg_Type()
)
mimosaPtmpChPwrTxPowerCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrTxPowerCfg.setStatus("current")
_MimosaPtmpChPwrCntrFreqCur_Type = Mimosa5GHzFrequency
_MimosaPtmpChPwrCntrFreqCur_Object = MibTableColumn
mimosaPtmpChPwrCntrFreqCur = _MimosaPtmpChPwrCntrFreqCur_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 7),
    _MimosaPtmpChPwrCntrFreqCur_Type()
)
mimosaPtmpChPwrCntrFreqCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrCntrFreqCur.setStatus("current")
_MimosaPtmpChPwrPrimChannelCur_Type = Mimosa5GHzChannelNumber
_MimosaPtmpChPwrPrimChannelCur_Object = MibTableColumn
mimosaPtmpChPwrPrimChannelCur = _MimosaPtmpChPwrPrimChannelCur_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 8),
    _MimosaPtmpChPwrPrimChannelCur_Type()
)
mimosaPtmpChPwrPrimChannelCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrPrimChannelCur.setStatus("current")
_MimosaPtmpChPwrChWidthCur_Type = Unsigned32
_MimosaPtmpChPwrChWidthCur_Object = MibTableColumn
mimosaPtmpChPwrChWidthCur = _MimosaPtmpChPwrChWidthCur_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 9),
    _MimosaPtmpChPwrChWidthCur_Type()
)
mimosaPtmpChPwrChWidthCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrChWidthCur.setStatus("current")
_MimosaPtmpChPwrTxPowerCur_Type = Integer32
_MimosaPtmpChPwrTxPowerCur_Object = MibTableColumn
mimosaPtmpChPwrTxPowerCur = _MimosaPtmpChPwrTxPowerCur_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 10),
    _MimosaPtmpChPwrTxPowerCur_Type()
)
mimosaPtmpChPwrTxPowerCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrTxPowerCur.setStatus("current")


class _MimosaPtmpChPwrAgcMode_Type(Integer32):
    """Custom type mimosaPtmpChPwrAgcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("manual", 1))
    )


_MimosaPtmpChPwrAgcMode_Type.__name__ = "Integer32"
_MimosaPtmpChPwrAgcMode_Object = MibTableColumn
mimosaPtmpChPwrAgcMode = _MimosaPtmpChPwrAgcMode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 11),
    _MimosaPtmpChPwrAgcMode_Type()
)
mimosaPtmpChPwrAgcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrAgcMode.setStatus("current")


class _MimosaPtmpChPwrMinRxPower_Type(Integer32):
    """Custom type mimosaPtmpChPwrMinRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -10),
    )


_MimosaPtmpChPwrMinRxPower_Type.__name__ = "Integer32"
_MimosaPtmpChPwrMinRxPower_Object = MibTableColumn
mimosaPtmpChPwrMinRxPower = _MimosaPtmpChPwrMinRxPower_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 12),
    _MimosaPtmpChPwrMinRxPower_Type()
)
mimosaPtmpChPwrMinRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChPwrMinRxPower.setStatus("current")
_MimosaPtmpChannelExclusionTable_Object = MibTable
mimosaPtmpChannelExclusionTable = _MimosaPtmpChannelExclusionTable_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4)
)
if mibBuilder.loadTexts:
    mimosaPtmpChannelExclusionTable.setStatus("current")
_MimosaPtmpChannelExclusionEntry_Object = MibTableRow
mimosaPtmpChannelExclusionEntry = _MimosaPtmpChannelExclusionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4, 1)
)
mimosaPtmpChannelExclusionEntry.setIndexNames(
    (0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChannelExclusionIndex"),
)
if mibBuilder.loadTexts:
    mimosaPtmpChannelExclusionEntry.setStatus("current")


class _MimosaPtmpChannelExclusionIndex_Type(Integer32):
    """Custom type mimosaPtmpChannelExclusionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MimosaPtmpChannelExclusionIndex_Type.__name__ = "Integer32"
_MimosaPtmpChannelExclusionIndex_Object = MibTableColumn
mimosaPtmpChannelExclusionIndex = _MimosaPtmpChannelExclusionIndex_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4, 1, 1),
    _MimosaPtmpChannelExclusionIndex_Type()
)
mimosaPtmpChannelExclusionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mimosaPtmpChannelExclusionIndex.setStatus("current")
_MimosaPtmpChannelExclusionStart_Type = Integer32
_MimosaPtmpChannelExclusionStart_Object = MibTableColumn
mimosaPtmpChannelExclusionStart = _MimosaPtmpChannelExclusionStart_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4, 1, 2),
    _MimosaPtmpChannelExclusionStart_Type()
)
mimosaPtmpChannelExclusionStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChannelExclusionStart.setStatus("current")
_MimosaPtmpChannelExclusionEnd_Type = Integer32
_MimosaPtmpChannelExclusionEnd_Object = MibTableColumn
mimosaPtmpChannelExclusionEnd = _MimosaPtmpChannelExclusionEnd_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4, 1, 3),
    _MimosaPtmpChannelExclusionEnd_Type()
)
mimosaPtmpChannelExclusionEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpChannelExclusionEnd.setStatus("current")
_MimosaPtmpApStats_ObjectIdentity = ObjectIdentity
mimosaPtmpApStats = _MimosaPtmpApStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4)
)
_MimosaPtmpApStatsRxBytes_Type = Counter64
_MimosaPtmpApStatsRxBytes_Object = MibScalar
mimosaPtmpApStatsRxBytes = _MimosaPtmpApStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 1),
    _MimosaPtmpApStatsRxBytes_Type()
)
mimosaPtmpApStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpApStatsRxBytes.setStatus("current")
_MimosaPtmpApStatsTxBytes_Type = Counter64
_MimosaPtmpApStatsTxBytes_Object = MibScalar
mimosaPtmpApStatsTxBytes = _MimosaPtmpApStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 2),
    _MimosaPtmpApStatsTxBytes_Type()
)
mimosaPtmpApStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpApStatsTxBytes.setStatus("current")
_MimosaPtmpApStatsRxPkts_Type = Counter64
_MimosaPtmpApStatsRxPkts_Object = MibScalar
mimosaPtmpApStatsRxPkts = _MimosaPtmpApStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 3),
    _MimosaPtmpApStatsRxPkts_Type()
)
mimosaPtmpApStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpApStatsRxPkts.setStatus("current")
_MimosaPtmpApStatsTxPkts_Type = Counter64
_MimosaPtmpApStatsTxPkts_Object = MibScalar
mimosaPtmpApStatsTxPkts = _MimosaPtmpApStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 4),
    _MimosaPtmpApStatsTxPkts_Type()
)
mimosaPtmpApStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpApStatsTxPkts.setStatus("current")
_MimosaPtmpApStatsTxPer_Type = Integer32
_MimosaPtmpApStatsTxPer_Object = MibScalar
mimosaPtmpApStatsTxPer = _MimosaPtmpApStatsTxPer_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 5),
    _MimosaPtmpApStatsTxPer_Type()
)
mimosaPtmpApStatsTxPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpApStatsTxPer.setStatus("current")
_MimosaPtmpApStatsLastUpdated_Type = TimeStamp
_MimosaPtmpApStatsLastUpdated_Object = MibScalar
mimosaPtmpApStatsLastUpdated = _MimosaPtmpApStatsLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 6),
    _MimosaPtmpApStatsLastUpdated_Type()
)
mimosaPtmpApStatsLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpApStatsLastUpdated.setStatus("current")
_MimosaPtmpClientInfo_ObjectIdentity = ObjectIdentity
mimosaPtmpClientInfo = _MimosaPtmpClientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5)
)
_MimosaPtmpClientInfoTable_Object = MibTable
mimosaPtmpClientInfoTable = _MimosaPtmpClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1)
)
if mibBuilder.loadTexts:
    mimosaPtmpClientInfoTable.setStatus("current")
_MimosaPtmpClientInfoEntry_Object = MibTableRow
mimosaPtmpClientInfoEntry = _MimosaPtmpClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1)
)
mimosaPtmpClientInfoEntry.setIndexNames(
    (0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientInfoIndex"),
)
if mibBuilder.loadTexts:
    mimosaPtmpClientInfoEntry.setStatus("current")
_MimosaPtmpClientInfoIndex_Type = Unsigned32
_MimosaPtmpClientInfoIndex_Object = MibTableColumn
mimosaPtmpClientInfoIndex = _MimosaPtmpClientInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 1),
    _MimosaPtmpClientInfoIndex_Type()
)
mimosaPtmpClientInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mimosaPtmpClientInfoIndex.setStatus("current")
_MimosaPtmpClientInfoMacAddress_Type = MacAddress
_MimosaPtmpClientInfoMacAddress_Object = MibTableColumn
mimosaPtmpClientInfoMacAddress = _MimosaPtmpClientInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 2),
    _MimosaPtmpClientInfoMacAddress_Type()
)
mimosaPtmpClientInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientInfoMacAddress.setStatus("current")


class _MimosaPtmpClientName_Type(DisplayString):
    """Custom type mimosaPtmpClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MimosaPtmpClientName_Type.__name__ = "DisplayString"
_MimosaPtmpClientName_Object = MibTableColumn
mimosaPtmpClientName = _MimosaPtmpClientName_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 3),
    _MimosaPtmpClientName_Type()
)
mimosaPtmpClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientName.setStatus("current")


class _MimosaPtmpClientFWVersion_Type(DisplayString):
    """Custom type mimosaPtmpClientFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MimosaPtmpClientFWVersion_Type.__name__ = "DisplayString"
_MimosaPtmpClientFWVersion_Object = MibTableColumn
mimosaPtmpClientFWVersion = _MimosaPtmpClientFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 4),
    _MimosaPtmpClientFWVersion_Type()
)
mimosaPtmpClientFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientFWVersion.setStatus("current")
_MimosaPtmpClientIPAddress_Type = IpAddress
_MimosaPtmpClientIPAddress_Object = MibTableColumn
mimosaPtmpClientIPAddress = _MimosaPtmpClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 5),
    _MimosaPtmpClientIPAddress_Type()
)
mimosaPtmpClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientIPAddress.setStatus("current")
_MimosaPtmpClientAssociatedTime_Type = TimeStamp
_MimosaPtmpClientAssociatedTime_Object = MibTableColumn
mimosaPtmpClientAssociatedTime = _MimosaPtmpClientAssociatedTime_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 6),
    _MimosaPtmpClientAssociatedTime_Type()
)
mimosaPtmpClientAssociatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientAssociatedTime.setStatus("current")
_MimosaPtmpClientPlanName_Type = DisplayString
_MimosaPtmpClientPlanName_Object = MibTableColumn
mimosaPtmpClientPlanName = _MimosaPtmpClientPlanName_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 7),
    _MimosaPtmpClientPlanName_Type()
)
mimosaPtmpClientPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientPlanName.setStatus("current")
_MimosaPtmpClientUlCommitted_Type = Unsigned32
_MimosaPtmpClientUlCommitted_Object = MibTableColumn
mimosaPtmpClientUlCommitted = _MimosaPtmpClientUlCommitted_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 8),
    _MimosaPtmpClientUlCommitted_Type()
)
mimosaPtmpClientUlCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientUlCommitted.setStatus("current")
_MimosaPtmpClientUlPeak_Type = Unsigned32
_MimosaPtmpClientUlPeak_Object = MibTableColumn
mimosaPtmpClientUlPeak = _MimosaPtmpClientUlPeak_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 9),
    _MimosaPtmpClientUlPeak_Type()
)
mimosaPtmpClientUlPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientUlPeak.setStatus("current")
_MimosaPtmpClientDlCommitted_Type = Unsigned32
_MimosaPtmpClientDlCommitted_Object = MibTableColumn
mimosaPtmpClientDlCommitted = _MimosaPtmpClientDlCommitted_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 10),
    _MimosaPtmpClientDlCommitted_Type()
)
mimosaPtmpClientDlCommitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientDlCommitted.setStatus("current")
_MimosaPtmpClientDlPeak_Type = Unsigned32
_MimosaPtmpClientDlPeak_Object = MibTableColumn
mimosaPtmpClientDlPeak = _MimosaPtmpClientDlPeak_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 11),
    _MimosaPtmpClientDlPeak_Type()
)
mimosaPtmpClientDlPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientDlPeak.setStatus("current")
_MimosaPtmpClientInfoLastUpdated_Type = TimeStamp
_MimosaPtmpClientInfoLastUpdated_Object = MibTableColumn
mimosaPtmpClientInfoLastUpdated = _MimosaPtmpClientInfoLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 12),
    _MimosaPtmpClientInfoLastUpdated_Type()
)
mimosaPtmpClientInfoLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientInfoLastUpdated.setStatus("current")
_MimosaPtmpClientStats_ObjectIdentity = ObjectIdentity
mimosaPtmpClientStats = _MimosaPtmpClientStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6)
)
_MimosaPtmpClientStatsTable_Object = MibTable
mimosaPtmpClientStatsTable = _MimosaPtmpClientStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1)
)
if mibBuilder.loadTexts:
    mimosaPtmpClientStatsTable.setStatus("current")
_MimosaPtmpClientStatsEntry_Object = MibTableRow
mimosaPtmpClientStatsEntry = _MimosaPtmpClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1)
)
mimosaPtmpClientStatsEntry.setIndexNames(
    (0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientStatsIndex"),
)
if mibBuilder.loadTexts:
    mimosaPtmpClientStatsEntry.setStatus("current")
_MimosaPtmpClientStatsIndex_Type = Unsigned32
_MimosaPtmpClientStatsIndex_Object = MibTableColumn
mimosaPtmpClientStatsIndex = _MimosaPtmpClientStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 1),
    _MimosaPtmpClientStatsIndex_Type()
)
mimosaPtmpClientStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mimosaPtmpClientStatsIndex.setStatus("current")
_MimosaPtmpClientStatsMacAddress_Type = MacAddress
_MimosaPtmpClientStatsMacAddress_Object = MibTableColumn
mimosaPtmpClientStatsMacAddress = _MimosaPtmpClientStatsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 2),
    _MimosaPtmpClientStatsMacAddress_Type()
)
mimosaPtmpClientStatsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientStatsMacAddress.setStatus("current")
_MimosaPtmpClientAssocBW_Type = Unsigned32
_MimosaPtmpClientAssocBW_Object = MibTableColumn
mimosaPtmpClientAssocBW = _MimosaPtmpClientAssocBW_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 3),
    _MimosaPtmpClientAssocBW_Type()
)
mimosaPtmpClientAssocBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientAssocBW.setStatus("current")
_MimosaPtmpClientRxBytes_Type = Counter64
_MimosaPtmpClientRxBytes_Object = MibTableColumn
mimosaPtmpClientRxBytes = _MimosaPtmpClientRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 4),
    _MimosaPtmpClientRxBytes_Type()
)
mimosaPtmpClientRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientRxBytes.setStatus("current")
_MimosaPtmpClientTxBytes_Type = Counter64
_MimosaPtmpClientTxBytes_Object = MibTableColumn
mimosaPtmpClientTxBytes = _MimosaPtmpClientTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 5),
    _MimosaPtmpClientTxBytes_Type()
)
mimosaPtmpClientTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientTxBytes.setStatus("current")
_MimosaPtmpClientRxPkts_Type = Counter64
_MimosaPtmpClientRxPkts_Object = MibTableColumn
mimosaPtmpClientRxPkts = _MimosaPtmpClientRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 6),
    _MimosaPtmpClientRxPkts_Type()
)
mimosaPtmpClientRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientRxPkts.setStatus("current")
_MimosaPtmpClientTxPkts_Type = Counter64
_MimosaPtmpClientTxPkts_Object = MibTableColumn
mimosaPtmpClientTxPkts = _MimosaPtmpClientTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 7),
    _MimosaPtmpClientTxPkts_Type()
)
mimosaPtmpClientTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientTxPkts.setStatus("current")
_MimosaPtmpClientRxPhyRate_Type = Unsigned32
_MimosaPtmpClientRxPhyRate_Object = MibTableColumn
mimosaPtmpClientRxPhyRate = _MimosaPtmpClientRxPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 8),
    _MimosaPtmpClientRxPhyRate_Type()
)
mimosaPtmpClientRxPhyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientRxPhyRate.setStatus("current")
_MimosaPtmpClientTxPhyRate_Type = Unsigned32
_MimosaPtmpClientTxPhyRate_Object = MibTableColumn
mimosaPtmpClientTxPhyRate = _MimosaPtmpClientTxPhyRate_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 9),
    _MimosaPtmpClientTxPhyRate_Type()
)
mimosaPtmpClientTxPhyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientTxPhyRate.setStatus("current")
_MimosaPtmpClientTxAvgPer_Type = DecimalTwo
_MimosaPtmpClientTxAvgPer_Object = MibTableColumn
mimosaPtmpClientTxAvgPer = _MimosaPtmpClientTxAvgPer_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 10),
    _MimosaPtmpClientTxAvgPer_Type()
)
mimosaPtmpClientTxAvgPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientTxAvgPer.setStatus("current")
_MimosaPtmpClientRssiAvg_Type = DecimalOne
_MimosaPtmpClientRssiAvg_Object = MibTableColumn
mimosaPtmpClientRssiAvg = _MimosaPtmpClientRssiAvg_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 11),
    _MimosaPtmpClientRssiAvg_Type()
)
mimosaPtmpClientRssiAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientRssiAvg.setStatus("current")
_MimosaPtmpClientStatsLastUpdated_Type = TimeStamp
_MimosaPtmpClientStatsLastUpdated_Object = MibTableColumn
mimosaPtmpClientStatsLastUpdated = _MimosaPtmpClientStatsLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 12),
    _MimosaPtmpClientStatsLastUpdated_Type()
)
mimosaPtmpClientStatsLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpClientStatsLastUpdated.setStatus("current")
_MimosaPtmpMgmtInfo_ObjectIdentity = ObjectIdentity
mimosaPtmpMgmtInfo = _MimosaPtmpMgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7)
)
_MimosaPtmpMgmtIpAddress_Type = IpAddress
_MimosaPtmpMgmtIpAddress_Object = MibScalar
mimosaPtmpMgmtIpAddress = _MimosaPtmpMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 1),
    _MimosaPtmpMgmtIpAddress_Type()
)
mimosaPtmpMgmtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtIpAddress.setStatus("current")
_MimosaPtmpMgmtIpNetmask_Type = IpAddress
_MimosaPtmpMgmtIpNetmask_Object = MibScalar
mimosaPtmpMgmtIpNetmask = _MimosaPtmpMgmtIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 2),
    _MimosaPtmpMgmtIpNetmask_Type()
)
mimosaPtmpMgmtIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtIpNetmask.setStatus("current")
_MimosaPtmpMgmtIpGateway_Type = IpAddress
_MimosaPtmpMgmtIpGateway_Object = MibScalar
mimosaPtmpMgmtIpGateway = _MimosaPtmpMgmtIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 3),
    _MimosaPtmpMgmtIpGateway_Type()
)
mimosaPtmpMgmtIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtIpGateway.setStatus("current")


class _MimosaPtmpMgmtIpMode_Type(DisplayString):
    """Custom type mimosaPtmpMgmtIpMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 6),
    )


_MimosaPtmpMgmtIpMode_Type.__name__ = "DisplayString"
_MimosaPtmpMgmtIpMode_Object = MibScalar
mimosaPtmpMgmtIpMode = _MimosaPtmpMgmtIpMode_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 4),
    _MimosaPtmpMgmtIpMode_Type()
)
mimosaPtmpMgmtIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtIpMode.setStatus("current")
_MimosaPtmpMgmtPrimaryDNS_Type = IpAddress
_MimosaPtmpMgmtPrimaryDNS_Object = MibScalar
mimosaPtmpMgmtPrimaryDNS = _MimosaPtmpMgmtPrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 5),
    _MimosaPtmpMgmtPrimaryDNS_Type()
)
mimosaPtmpMgmtPrimaryDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtPrimaryDNS.setStatus("current")
_MimosaPtmpMgmtSecondaryDNS_Type = IpAddress
_MimosaPtmpMgmtSecondaryDNS_Object = MibScalar
mimosaPtmpMgmtSecondaryDNS = _MimosaPtmpMgmtSecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 6),
    _MimosaPtmpMgmtSecondaryDNS_Type()
)
mimosaPtmpMgmtSecondaryDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtSecondaryDNS.setStatus("current")


class _MimosaPtmpMgmtVlanStatus_Type(Integer32):
    """Custom type mimosaPtmpMgmtVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MimosaPtmpMgmtVlanStatus_Type.__name__ = "Integer32"
_MimosaPtmpMgmtVlanStatus_Object = MibScalar
mimosaPtmpMgmtVlanStatus = _MimosaPtmpMgmtVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 7),
    _MimosaPtmpMgmtVlanStatus_Type()
)
mimosaPtmpMgmtVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtVlanStatus.setStatus("current")
_MimosaPtmpMgmtVlanId_Type = Integer32
_MimosaPtmpMgmtVlanId_Object = MibScalar
mimosaPtmpMgmtVlanId = _MimosaPtmpMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 8),
    _MimosaPtmpMgmtVlanId_Type()
)
mimosaPtmpMgmtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtVlanId.setStatus("current")


class _MimosaPtmpMgmtVlanPassthrough_Type(Integer32):
    """Custom type mimosaPtmpMgmtVlanPassthrough based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MimosaPtmpMgmtVlanPassthrough_Type.__name__ = "Integer32"
_MimosaPtmpMgmtVlanPassthrough_Object = MibScalar
mimosaPtmpMgmtVlanPassthrough = _MimosaPtmpMgmtVlanPassthrough_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 9),
    _MimosaPtmpMgmtVlanPassthrough_Type()
)
mimosaPtmpMgmtVlanPassthrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtVlanPassthrough.setStatus("current")
_MimosaPtmpMgmtEthernetMac_Type = MacAddress
_MimosaPtmpMgmtEthernetMac_Object = MibScalar
mimosaPtmpMgmtEthernetMac = _MimosaPtmpMgmtEthernetMac_Object(
    (1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 10),
    _MimosaPtmpMgmtEthernetMac_Type()
)
mimosaPtmpMgmtEthernetMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mimosaPtmpMgmtEthernetMac.setStatus("current")
_MimosaPtmpConformance_ObjectIdentity = ObjectIdentity
mimosaPtmpConformance = _MimosaPtmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2)
)
_MimosaPtmpCompliances_ObjectIdentity = ObjectIdentity
mimosaPtmpCompliances = _MimosaPtmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 1)
)
_MimosaPtmpGroups_ObjectIdentity = ObjectIdentity
mimosaPtmpGroups = _MimosaPtmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2)
)

# Managed Objects groups

mimosaPtmpSsidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 1)
)
mimosaPtmpSsidGroup.setObjects(
      *(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidName"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidType"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidEnabled"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidBroadcastEnabled"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidIsolationEnabled"))
)
if mibBuilder.loadTexts:
    mimosaPtmpSsidGroup.setStatus("current")

mimosaPtmpLinkInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 2)
)
mimosaPtmpLinkInfoGroup.setObjects(
      *(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpWirelessMode"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpWirelessGender"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpWirelessTrafficSplit"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpWirelessWindowLength"))
)
if mibBuilder.loadTexts:
    mimosaPtmpLinkInfoGroup.setStatus("current")

mimosaPtmpChannelPowerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 3)
)
mimosaPtmpChannelPowerGroup.setObjects(
      *(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpAutoChannelEnabled"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpAntennaGain"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrRadioName"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrCntrFreqCfg"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrPrimChannelCfg"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrChWidthCfg"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrTxPowerCfg"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrCntrFreqCur"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrPrimChannelCur"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrChWidthCur"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrTxPowerCur"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrAgcMode"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrMinRxPower"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChannelExclusionStart"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChannelExclusionEnd"))
)
if mibBuilder.loadTexts:
    mimosaPtmpChannelPowerGroup.setStatus("current")

mimosaPtmpApStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 4)
)
mimosaPtmpApStatsGroup.setObjects(
      *(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsRxBytes"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsTxBytes"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsRxPkts"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsTxPkts"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsTxPer"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsLastUpdated"))
)
if mibBuilder.loadTexts:
    mimosaPtmpApStatsGroup.setStatus("current")

mimosaPtmpClientInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 5)
)
mimosaPtmpClientInfoGroup.setObjects(
      *(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientName"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientFWVersion"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientIPAddress"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientAssociatedTime"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientPlanName"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientUlCommitted"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientUlPeak"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientDlCommitted"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientDlPeak"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientInfoLastUpdated"))
)
if mibBuilder.loadTexts:
    mimosaPtmpClientInfoGroup.setStatus("current")

mimosaPtmpClientStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 6)
)
mimosaPtmpClientStatsGroup.setObjects(
      *(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientStatsMacAddress"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientAssocBW"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientRxBytes"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientRxPkts"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientTxPkts"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientRssiAvg"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientRxPhyRate"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientTxAvgPer"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientTxPhyRate"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientTxBytes"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientStatsLastUpdated"))
)
if mibBuilder.loadTexts:
    mimosaPtmpClientStatsGroup.setStatus("current")

mimosaPtmpMgmtInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 7)
)
mimosaPtmpMgmtInfoGroup.setObjects(
      *(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtIpAddress"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtIpNetmask"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtIpGateway"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtIpMode"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtPrimaryDNS"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtSecondaryDNS"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtVlanStatus"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtVlanId"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtVlanPassthrough"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtEthernetMac"))
)
if mibBuilder.loadTexts:
    mimosaPtmpMgmtInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mimosaPtmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 1, 1)
)
mimosaPtmpCompliance.setObjects(
      *(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidGroup"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpLinkInfoGroup"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChannelPowerGroup"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsGroup"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientStatsGroup"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientInfoGroup"),
        ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtInfoGroup"))
)
if mibBuilder.loadTexts:
    mimosaPtmpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIMOSA-NETWORKS-PTMP-MIB",
    **{"mimosaPtmp": mimosaPtmp,
       "mimosaPtmpSsid": mimosaPtmpSsid,
       "mimosaPtmpSsidTable": mimosaPtmpSsidTable,
       "mimosaPtmpSsidEntry": mimosaPtmpSsidEntry,
       "mimosaPtmpSsidIndex": mimosaPtmpSsidIndex,
       "mimosaPtmpSsidName": mimosaPtmpSsidName,
       "mimosaPtmpSsidType": mimosaPtmpSsidType,
       "mimosaPtmpSsidEnabled": mimosaPtmpSsidEnabled,
       "mimosaPtmpSsidBroadcastEnabled": mimosaPtmpSsidBroadcastEnabled,
       "mimosaPtmpSsidIsolationEnabled": mimosaPtmpSsidIsolationEnabled,
       "mimosaPtmpLinkInfo": mimosaPtmpLinkInfo,
       "mimosaPtmpWirelessMode": mimosaPtmpWirelessMode,
       "mimosaPtmpWirelessGender": mimosaPtmpWirelessGender,
       "mimosaPtmpWirelessTrafficSplit": mimosaPtmpWirelessTrafficSplit,
       "mimosaPtmpWirelessWindowLength": mimosaPtmpWirelessWindowLength,
       "mimosaPtmpChannelPower": mimosaPtmpChannelPower,
       "mimosaPtmpAutoChannelEnabled": mimosaPtmpAutoChannelEnabled,
       "mimosaPtmpAntennaGain": mimosaPtmpAntennaGain,
       "mimosaPtmpChannelPowerTable": mimosaPtmpChannelPowerTable,
       "mimosaPtmpChannelPowerEntry": mimosaPtmpChannelPowerEntry,
       "mimosaPtmpChPwrRadioIndex": mimosaPtmpChPwrRadioIndex,
       "mimosaPtmpChPwrRadioName": mimosaPtmpChPwrRadioName,
       "mimosaPtmpChPwrCntrFreqCfg": mimosaPtmpChPwrCntrFreqCfg,
       "mimosaPtmpChPwrPrimChannelCfg": mimosaPtmpChPwrPrimChannelCfg,
       "mimosaPtmpChPwrChWidthCfg": mimosaPtmpChPwrChWidthCfg,
       "mimosaPtmpChPwrTxPowerCfg": mimosaPtmpChPwrTxPowerCfg,
       "mimosaPtmpChPwrCntrFreqCur": mimosaPtmpChPwrCntrFreqCur,
       "mimosaPtmpChPwrPrimChannelCur": mimosaPtmpChPwrPrimChannelCur,
       "mimosaPtmpChPwrChWidthCur": mimosaPtmpChPwrChWidthCur,
       "mimosaPtmpChPwrTxPowerCur": mimosaPtmpChPwrTxPowerCur,
       "mimosaPtmpChPwrAgcMode": mimosaPtmpChPwrAgcMode,
       "mimosaPtmpChPwrMinRxPower": mimosaPtmpChPwrMinRxPower,
       "mimosaPtmpChannelExclusionTable": mimosaPtmpChannelExclusionTable,
       "mimosaPtmpChannelExclusionEntry": mimosaPtmpChannelExclusionEntry,
       "mimosaPtmpChannelExclusionIndex": mimosaPtmpChannelExclusionIndex,
       "mimosaPtmpChannelExclusionStart": mimosaPtmpChannelExclusionStart,
       "mimosaPtmpChannelExclusionEnd": mimosaPtmpChannelExclusionEnd,
       "mimosaPtmpApStats": mimosaPtmpApStats,
       "mimosaPtmpApStatsRxBytes": mimosaPtmpApStatsRxBytes,
       "mimosaPtmpApStatsTxBytes": mimosaPtmpApStatsTxBytes,
       "mimosaPtmpApStatsRxPkts": mimosaPtmpApStatsRxPkts,
       "mimosaPtmpApStatsTxPkts": mimosaPtmpApStatsTxPkts,
       "mimosaPtmpApStatsTxPer": mimosaPtmpApStatsTxPer,
       "mimosaPtmpApStatsLastUpdated": mimosaPtmpApStatsLastUpdated,
       "mimosaPtmpClientInfo": mimosaPtmpClientInfo,
       "mimosaPtmpClientInfoTable": mimosaPtmpClientInfoTable,
       "mimosaPtmpClientInfoEntry": mimosaPtmpClientInfoEntry,
       "mimosaPtmpClientInfoIndex": mimosaPtmpClientInfoIndex,
       "mimosaPtmpClientInfoMacAddress": mimosaPtmpClientInfoMacAddress,
       "mimosaPtmpClientName": mimosaPtmpClientName,
       "mimosaPtmpClientFWVersion": mimosaPtmpClientFWVersion,
       "mimosaPtmpClientIPAddress": mimosaPtmpClientIPAddress,
       "mimosaPtmpClientAssociatedTime": mimosaPtmpClientAssociatedTime,
       "mimosaPtmpClientPlanName": mimosaPtmpClientPlanName,
       "mimosaPtmpClientUlCommitted": mimosaPtmpClientUlCommitted,
       "mimosaPtmpClientUlPeak": mimosaPtmpClientUlPeak,
       "mimosaPtmpClientDlCommitted": mimosaPtmpClientDlCommitted,
       "mimosaPtmpClientDlPeak": mimosaPtmpClientDlPeak,
       "mimosaPtmpClientInfoLastUpdated": mimosaPtmpClientInfoLastUpdated,
       "mimosaPtmpClientStats": mimosaPtmpClientStats,
       "mimosaPtmpClientStatsTable": mimosaPtmpClientStatsTable,
       "mimosaPtmpClientStatsEntry": mimosaPtmpClientStatsEntry,
       "mimosaPtmpClientStatsIndex": mimosaPtmpClientStatsIndex,
       "mimosaPtmpClientStatsMacAddress": mimosaPtmpClientStatsMacAddress,
       "mimosaPtmpClientAssocBW": mimosaPtmpClientAssocBW,
       "mimosaPtmpClientRxBytes": mimosaPtmpClientRxBytes,
       "mimosaPtmpClientTxBytes": mimosaPtmpClientTxBytes,
       "mimosaPtmpClientRxPkts": mimosaPtmpClientRxPkts,
       "mimosaPtmpClientTxPkts": mimosaPtmpClientTxPkts,
       "mimosaPtmpClientRxPhyRate": mimosaPtmpClientRxPhyRate,
       "mimosaPtmpClientTxPhyRate": mimosaPtmpClientTxPhyRate,
       "mimosaPtmpClientTxAvgPer": mimosaPtmpClientTxAvgPer,
       "mimosaPtmpClientRssiAvg": mimosaPtmpClientRssiAvg,
       "mimosaPtmpClientStatsLastUpdated": mimosaPtmpClientStatsLastUpdated,
       "mimosaPtmpMgmtInfo": mimosaPtmpMgmtInfo,
       "mimosaPtmpMgmtIpAddress": mimosaPtmpMgmtIpAddress,
       "mimosaPtmpMgmtIpNetmask": mimosaPtmpMgmtIpNetmask,
       "mimosaPtmpMgmtIpGateway": mimosaPtmpMgmtIpGateway,
       "mimosaPtmpMgmtIpMode": mimosaPtmpMgmtIpMode,
       "mimosaPtmpMgmtPrimaryDNS": mimosaPtmpMgmtPrimaryDNS,
       "mimosaPtmpMgmtSecondaryDNS": mimosaPtmpMgmtSecondaryDNS,
       "mimosaPtmpMgmtVlanStatus": mimosaPtmpMgmtVlanStatus,
       "mimosaPtmpMgmtVlanId": mimosaPtmpMgmtVlanId,
       "mimosaPtmpMgmtVlanPassthrough": mimosaPtmpMgmtVlanPassthrough,
       "mimosaPtmpMgmtEthernetMac": mimosaPtmpMgmtEthernetMac,
       "mimosaPtmpConformance": mimosaPtmpConformance,
       "mimosaPtmpCompliances": mimosaPtmpCompliances,
       "mimosaPtmpCompliance": mimosaPtmpCompliance,
       "mimosaPtmpGroups": mimosaPtmpGroups,
       "mimosaPtmpSsidGroup": mimosaPtmpSsidGroup,
       "mimosaPtmpLinkInfoGroup": mimosaPtmpLinkInfoGroup,
       "mimosaPtmpChannelPowerGroup": mimosaPtmpChannelPowerGroup,
       "mimosaPtmpApStatsGroup": mimosaPtmpApStatsGroup,
       "mimosaPtmpClientInfoGroup": mimosaPtmpClientInfoGroup,
       "mimosaPtmpClientStatsGroup": mimosaPtmpClientStatsGroup,
       "mimosaPtmpMgmtInfoGroup": mimosaPtmpMgmtInfoGroup}
)
