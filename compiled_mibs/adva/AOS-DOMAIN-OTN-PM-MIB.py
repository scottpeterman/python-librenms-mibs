# SNMP MIB module (AOS-DOMAIN-OTN-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\AOS-DOMAIN-OTN-PM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:00 2025
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

(aosCommon,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "aosCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aosDomainOtnPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5)
)
if mibBuilder.loadTexts:
    aosDomainOtnPmMIB.setRevisions(
        ("2019-04-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AosDomainOtnPmObjects_ObjectIdentity = ObjectIdentity
aosDomainOtnPmObjects = _AosDomainOtnPmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 1)
)
_AosDomainOtnPmStatsObjects_ObjectIdentity = ObjectIdentity
aosDomainOtnPmStatsObjects = _AosDomainOtnPmStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2)
)
_AosDomainOtnPmOscOptPowerTable_Object = MibTable
aosDomainOtnPmOscOptPowerTable = _AosDomainOtnPmOscOptPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    aosDomainOtnPmOscOptPowerTable.setStatus("current")
_AosDomainOtnPmOscOptPowerEntry_Object = MibTableRow
aosDomainOtnPmOscOptPowerEntry = _AosDomainOtnPmOscOptPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 1, 1)
)
aosDomainOtnPmOscOptPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPmOscOptPowerEntry.setStatus("current")
_AosDomainOtnPmOscOptPowerRx_Type = Integer32
_AosDomainOtnPmOscOptPowerRx_Object = MibTableColumn
aosDomainOtnPmOscOptPowerRx = _AosDomainOtnPmOscOptPowerRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 1, 1, 1),
    _AosDomainOtnPmOscOptPowerRx_Type()
)
aosDomainOtnPmOscOptPowerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmOscOptPowerRx.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmOscOptPowerRx.setUnits("0.1 dBm")
_AosDomainOtnPmOscOptPowerTx_Type = Integer32
_AosDomainOtnPmOscOptPowerTx_Object = MibTableColumn
aosDomainOtnPmOscOptPowerTx = _AosDomainOtnPmOscOptPowerTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 1, 1, 2),
    _AosDomainOtnPmOscOptPowerTx_Type()
)
aosDomainOtnPmOscOptPowerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmOscOptPowerTx.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmOscOptPowerTx.setUnits("0.1 dBm")
_AosDomainOtnPmOscLaserTable_Object = MibTable
aosDomainOtnPmOscLaserTable = _AosDomainOtnPmOscLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    aosDomainOtnPmOscLaserTable.setStatus("current")
_AosDomainOtnPmOscLaserEntry_Object = MibTableRow
aosDomainOtnPmOscLaserEntry = _AosDomainOtnPmOscLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 2, 1)
)
aosDomainOtnPmOscLaserEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPmOscLaserEntry.setStatus("current")
_AosDomainOtnPmOscLaserBiasCurr_Type = Integer32
_AosDomainOtnPmOscLaserBiasCurr_Object = MibTableColumn
aosDomainOtnPmOscLaserBiasCurr = _AosDomainOtnPmOscLaserBiasCurr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 2, 1, 1),
    _AosDomainOtnPmOscLaserBiasCurr_Type()
)
aosDomainOtnPmOscLaserBiasCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmOscLaserBiasCurr.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmOscLaserBiasCurr.setUnits("mA")
_AosDomainOtnPmOscLaserTemp_Type = Integer32
_AosDomainOtnPmOscLaserTemp_Object = MibTableColumn
aosDomainOtnPmOscLaserTemp = _AosDomainOtnPmOscLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 2, 1, 2),
    _AosDomainOtnPmOscLaserTemp_Type()
)
aosDomainOtnPmOscLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmOscLaserTemp.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmOscLaserTemp.setUnits("0.1 C")
_AosDomainOtnPmSpanLossTable_Object = MibTable
aosDomainOtnPmSpanLossTable = _AosDomainOtnPmSpanLossTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    aosDomainOtnPmSpanLossTable.setStatus("current")
_AosDomainOtnPmSpanLossEntry_Object = MibTableRow
aosDomainOtnPmSpanLossEntry = _AosDomainOtnPmSpanLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 3, 1)
)
aosDomainOtnPmSpanLossEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPmSpanLossEntry.setStatus("current")
_AosDomainOtnPmSpanLossRx_Type = Integer32
_AosDomainOtnPmSpanLossRx_Object = MibTableColumn
aosDomainOtnPmSpanLossRx = _AosDomainOtnPmSpanLossRx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 3, 1, 1),
    _AosDomainOtnPmSpanLossRx_Type()
)
aosDomainOtnPmSpanLossRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmSpanLossRx.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmSpanLossRx.setUnits("0.1 dB")
_AosDomainOtnPmSpanLossTx_Type = Integer32
_AosDomainOtnPmSpanLossTx_Object = MibTableColumn
aosDomainOtnPmSpanLossTx = _AosDomainOtnPmSpanLossTx_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 3, 1, 2),
    _AosDomainOtnPmSpanLossTx_Type()
)
aosDomainOtnPmSpanLossTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmSpanLossTx.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmSpanLossTx.setUnits("0.1 dB")
_AosDomainOtnPmAmpTable_Object = MibTable
aosDomainOtnPmAmpTable = _AosDomainOtnPmAmpTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    aosDomainOtnPmAmpTable.setStatus("current")
_AosDomainOtnPmAmpEntry_Object = MibTableRow
aosDomainOtnPmAmpEntry = _AosDomainOtnPmAmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 4, 1)
)
aosDomainOtnPmAmpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPmAmpEntry.setStatus("current")
_AosDomainOtnPmAmpOperTime_Type = Integer32
_AosDomainOtnPmAmpOperTime_Object = MibTableColumn
aosDomainOtnPmAmpOperTime = _AosDomainOtnPmAmpOperTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 4, 1, 1),
    _AosDomainOtnPmAmpOperTime_Type()
)
aosDomainOtnPmAmpOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmAmpOperTime.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmAmpOperTime.setUnits("h")
_AosDomainOtnPmAmpTotalGain_Type = Integer32
_AosDomainOtnPmAmpTotalGain_Object = MibTableColumn
aosDomainOtnPmAmpTotalGain = _AosDomainOtnPmAmpTotalGain_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 4, 1, 2),
    _AosDomainOtnPmAmpTotalGain_Type()
)
aosDomainOtnPmAmpTotalGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmAmpTotalGain.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmAmpTotalGain.setUnits("0.1 dB")
_AosDomainOtnPmAmpTotalLase_Type = Integer32
_AosDomainOtnPmAmpTotalLase_Object = MibTableColumn
aosDomainOtnPmAmpTotalLase = _AosDomainOtnPmAmpTotalLase_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 4, 1, 3),
    _AosDomainOtnPmAmpTotalLase_Type()
)
aosDomainOtnPmAmpTotalLase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmAmpTotalLase.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmAmpTotalLase.setUnits("0.1 dBm")
_AosDomainOtnPmQualityTable_Object = MibTable
aosDomainOtnPmQualityTable = _AosDomainOtnPmQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityTable.setStatus("current")
_AosDomainOtnPmQualityEntry_Object = MibTableRow
aosDomainOtnPmQualityEntry = _AosDomainOtnPmQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 5, 1)
)
aosDomainOtnPmQualityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEntry.setStatus("current")
_AosDomainOtnPmQualityCdc_Type = Integer32
_AosDomainOtnPmQualityCdc_Object = MibTableColumn
aosDomainOtnPmQualityCdc = _AosDomainOtnPmQualityCdc_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 5, 1, 1),
    _AosDomainOtnPmQualityCdc_Type()
)
aosDomainOtnPmQualityCdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityCdc.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityCdc.setUnits("ps/nm")
_AosDomainOtnPmQualityCfo_Type = Integer32
_AosDomainOtnPmQualityCfo_Object = MibTableColumn
aosDomainOtnPmQualityCfo = _AosDomainOtnPmQualityCfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 5, 1, 2),
    _AosDomainOtnPmQualityCfo_Type()
)
aosDomainOtnPmQualityCfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityCfo.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityCfo.setUnits("0.001 GHz")
_AosDomainOtnPmQualitySnr_Type = Integer32
_AosDomainOtnPmQualitySnr_Object = MibTableColumn
aosDomainOtnPmQualitySnr = _AosDomainOtnPmQualitySnr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 5, 1, 3),
    _AosDomainOtnPmQualitySnr_Type()
)
aosDomainOtnPmQualitySnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualitySnr.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualitySnr.setUnits("0.1 dB")
_AosDomainOtnPmQualityDgd_Type = Integer32
_AosDomainOtnPmQualityDgd_Object = MibTableColumn
aosDomainOtnPmQualityDgd = _AosDomainOtnPmQualityDgd_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 5, 1, 4),
    _AosDomainOtnPmQualityDgd_Type()
)
aosDomainOtnPmQualityDgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityDgd.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityDgd.setUnits("ps")
_AosDomainOtnPmQualityQFactor_Type = Integer32
_AosDomainOtnPmQualityQFactor_Object = MibTableColumn
aosDomainOtnPmQualityQFactor = _AosDomainOtnPmQualityQFactor_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 5, 1, 5),
    _AosDomainOtnPmQualityQFactor_Type()
)
aosDomainOtnPmQualityQFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityQFactor.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityQFactor.setUnits("0.1 dB")
_AosDomainOtnPmQualityEnhancedTable_Object = MibTable
aosDomainOtnPmQualityEnhancedTable = _AosDomainOtnPmQualityEnhancedTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEnhancedTable.setStatus("current")
_AosDomainOtnPmQualityEnhancedEntry_Object = MibTableRow
aosDomainOtnPmQualityEnhancedEntry = _AosDomainOtnPmQualityEnhancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 6, 1)
)
aosDomainOtnPmQualityEnhancedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEnhancedEntry.setStatus("current")
_AosDomainOtnPmQualityEnhancedSopt_Type = Integer32
_AosDomainOtnPmQualityEnhancedSopt_Object = MibTableColumn
aosDomainOtnPmQualityEnhancedSopt = _AosDomainOtnPmQualityEnhancedSopt_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 6, 1, 1),
    _AosDomainOtnPmQualityEnhancedSopt_Type()
)
aosDomainOtnPmQualityEnhancedSopt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEnhancedSopt.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEnhancedSopt.setUnits("rad/sec")
_AosDomainOtnPmQualityEnhancedOsnr_Type = Integer32
_AosDomainOtnPmQualityEnhancedOsnr_Object = MibTableColumn
aosDomainOtnPmQualityEnhancedOsnr = _AosDomainOtnPmQualityEnhancedOsnr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 6, 1, 2),
    _AosDomainOtnPmQualityEnhancedOsnr_Type()
)
aosDomainOtnPmQualityEnhancedOsnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEnhancedOsnr.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEnhancedOsnr.setUnits("0.1 dB")
_AosDomainOtnPmQualityEnhancedPdl_Type = Integer32
_AosDomainOtnPmQualityEnhancedPdl_Object = MibTableColumn
aosDomainOtnPmQualityEnhancedPdl = _AosDomainOtnPmQualityEnhancedPdl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 6, 1, 3),
    _AosDomainOtnPmQualityEnhancedPdl_Type()
)
aosDomainOtnPmQualityEnhancedPdl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEnhancedPdl.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPmQualityEnhancedPdl.setUnits("0.1 dB")
_AosDomainOtnPm15MinOscOptPowerTable_Object = MibTable
aosDomainOtnPm15MinOscOptPowerTable = _AosDomainOtnPm15MinOscOptPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerTable.setStatus("current")
_AosDomainOtnPm15MinOscOptPowerEntry_Object = MibTableRow
aosDomainOtnPm15MinOscOptPowerEntry = _AosDomainOtnPm15MinOscOptPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1)
)
aosDomainOtnPm15MinOscOptPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinOscOptPowerSample"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerEntry.setStatus("current")


class _AosDomainOtnPm15MinOscOptPowerSample_Type(Integer32):
    """Custom type aosDomainOtnPm15MinOscOptPowerSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosDomainOtnPm15MinOscOptPowerSample_Type.__name__ = "Integer32"
_AosDomainOtnPm15MinOscOptPowerSample_Object = MibTableColumn
aosDomainOtnPm15MinOscOptPowerSample = _AosDomainOtnPm15MinOscOptPowerSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1, 1),
    _AosDomainOtnPm15MinOscOptPowerSample_Type()
)
aosDomainOtnPm15MinOscOptPowerSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerSample.setStatus("current")
_AosDomainOtnPm15MinOscOptPowerSampleTime_Type = TimeTicks
_AosDomainOtnPm15MinOscOptPowerSampleTime_Object = MibTableColumn
aosDomainOtnPm15MinOscOptPowerSampleTime = _AosDomainOtnPm15MinOscOptPowerSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1, 2),
    _AosDomainOtnPm15MinOscOptPowerSampleTime_Type()
)
aosDomainOtnPm15MinOscOptPowerSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerSampleTime.setStatus("current")
_AosDomainOtnPm15MinOscOptPowerRxLow_Type = Integer32
_AosDomainOtnPm15MinOscOptPowerRxLow_Object = MibTableColumn
aosDomainOtnPm15MinOscOptPowerRxLow = _AosDomainOtnPm15MinOscOptPowerRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1, 3),
    _AosDomainOtnPm15MinOscOptPowerRxLow_Type()
)
aosDomainOtnPm15MinOscOptPowerRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerRxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerRxLow.setUnits("0.1 dBm")
_AosDomainOtnPm15MinOscOptPowerRxMean_Type = Integer32
_AosDomainOtnPm15MinOscOptPowerRxMean_Object = MibTableColumn
aosDomainOtnPm15MinOscOptPowerRxMean = _AosDomainOtnPm15MinOscOptPowerRxMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1, 4),
    _AosDomainOtnPm15MinOscOptPowerRxMean_Type()
)
aosDomainOtnPm15MinOscOptPowerRxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerRxMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerRxMean.setUnits("0.1 dBm")
_AosDomainOtnPm15MinOscOptPowerRxHigh_Type = Integer32
_AosDomainOtnPm15MinOscOptPowerRxHigh_Object = MibTableColumn
aosDomainOtnPm15MinOscOptPowerRxHigh = _AosDomainOtnPm15MinOscOptPowerRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1, 5),
    _AosDomainOtnPm15MinOscOptPowerRxHigh_Type()
)
aosDomainOtnPm15MinOscOptPowerRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerRxHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerRxHigh.setUnits("0.1 dBm")
_AosDomainOtnPm15MinOscOptPowerTxLow_Type = Integer32
_AosDomainOtnPm15MinOscOptPowerTxLow_Object = MibTableColumn
aosDomainOtnPm15MinOscOptPowerTxLow = _AosDomainOtnPm15MinOscOptPowerTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1, 6),
    _AosDomainOtnPm15MinOscOptPowerTxLow_Type()
)
aosDomainOtnPm15MinOscOptPowerTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerTxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerTxLow.setUnits("0.1 dBm")
_AosDomainOtnPm15MinOscOptPowerTxMean_Type = Integer32
_AosDomainOtnPm15MinOscOptPowerTxMean_Object = MibTableColumn
aosDomainOtnPm15MinOscOptPowerTxMean = _AosDomainOtnPm15MinOscOptPowerTxMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1, 7),
    _AosDomainOtnPm15MinOscOptPowerTxMean_Type()
)
aosDomainOtnPm15MinOscOptPowerTxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerTxMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerTxMean.setUnits("0.1 dBm")
_AosDomainOtnPm15MinOscOptPowerTxHigh_Type = Integer32
_AosDomainOtnPm15MinOscOptPowerTxHigh_Object = MibTableColumn
aosDomainOtnPm15MinOscOptPowerTxHigh = _AosDomainOtnPm15MinOscOptPowerTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 20, 1, 8),
    _AosDomainOtnPm15MinOscOptPowerTxHigh_Type()
)
aosDomainOtnPm15MinOscOptPowerTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerTxHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinOscOptPowerTxHigh.setUnits("0.1 dBm")
_AosDomainOtnPm15MinSpanLossTable_Object = MibTable
aosDomainOtnPm15MinSpanLossTable = _AosDomainOtnPm15MinSpanLossTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossTable.setStatus("current")
_AosDomainOtnPm15MinSpanLossEntry_Object = MibTableRow
aosDomainOtnPm15MinSpanLossEntry = _AosDomainOtnPm15MinSpanLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1)
)
aosDomainOtnPm15MinSpanLossEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinSpanLossSample"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossEntry.setStatus("current")


class _AosDomainOtnPm15MinSpanLossSample_Type(Integer32):
    """Custom type aosDomainOtnPm15MinSpanLossSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosDomainOtnPm15MinSpanLossSample_Type.__name__ = "Integer32"
_AosDomainOtnPm15MinSpanLossSample_Object = MibTableColumn
aosDomainOtnPm15MinSpanLossSample = _AosDomainOtnPm15MinSpanLossSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1, 1),
    _AosDomainOtnPm15MinSpanLossSample_Type()
)
aosDomainOtnPm15MinSpanLossSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossSample.setStatus("current")
_AosDomainOtnPm15MinSpanLossSampleTime_Type = TimeTicks
_AosDomainOtnPm15MinSpanLossSampleTime_Object = MibTableColumn
aosDomainOtnPm15MinSpanLossSampleTime = _AosDomainOtnPm15MinSpanLossSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1, 2),
    _AosDomainOtnPm15MinSpanLossSampleTime_Type()
)
aosDomainOtnPm15MinSpanLossSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossSampleTime.setStatus("current")
_AosDomainOtnPm15MinSpanLossRxLow_Type = Integer32
_AosDomainOtnPm15MinSpanLossRxLow_Object = MibTableColumn
aosDomainOtnPm15MinSpanLossRxLow = _AosDomainOtnPm15MinSpanLossRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1, 3),
    _AosDomainOtnPm15MinSpanLossRxLow_Type()
)
aosDomainOtnPm15MinSpanLossRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossRxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossRxLow.setUnits("0.1 dB")
_AosDomainOtnPm15MinSpanLossRxMean_Type = Integer32
_AosDomainOtnPm15MinSpanLossRxMean_Object = MibTableColumn
aosDomainOtnPm15MinSpanLossRxMean = _AosDomainOtnPm15MinSpanLossRxMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1, 4),
    _AosDomainOtnPm15MinSpanLossRxMean_Type()
)
aosDomainOtnPm15MinSpanLossRxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossRxMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossRxMean.setUnits("0.1 dB")
_AosDomainOtnPm15MinSpanLossRxHigh_Type = Integer32
_AosDomainOtnPm15MinSpanLossRxHigh_Object = MibTableColumn
aosDomainOtnPm15MinSpanLossRxHigh = _AosDomainOtnPm15MinSpanLossRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1, 5),
    _AosDomainOtnPm15MinSpanLossRxHigh_Type()
)
aosDomainOtnPm15MinSpanLossRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossRxHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossRxHigh.setUnits("0.1 dB")
_AosDomainOtnPm15MinSpanLossTxLow_Type = Integer32
_AosDomainOtnPm15MinSpanLossTxLow_Object = MibTableColumn
aosDomainOtnPm15MinSpanLossTxLow = _AosDomainOtnPm15MinSpanLossTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1, 6),
    _AosDomainOtnPm15MinSpanLossTxLow_Type()
)
aosDomainOtnPm15MinSpanLossTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossTxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossTxLow.setUnits("0.1 dB")
_AosDomainOtnPm15MinSpanLossTxMean_Type = Integer32
_AosDomainOtnPm15MinSpanLossTxMean_Object = MibTableColumn
aosDomainOtnPm15MinSpanLossTxMean = _AosDomainOtnPm15MinSpanLossTxMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1, 7),
    _AosDomainOtnPm15MinSpanLossTxMean_Type()
)
aosDomainOtnPm15MinSpanLossTxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossTxMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossTxMean.setUnits("0.1 dB")
_AosDomainOtnPm15MinSpanLossTxHigh_Type = Integer32
_AosDomainOtnPm15MinSpanLossTxHigh_Object = MibTableColumn
aosDomainOtnPm15MinSpanLossTxHigh = _AosDomainOtnPm15MinSpanLossTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 21, 1, 8),
    _AosDomainOtnPm15MinSpanLossTxHigh_Type()
)
aosDomainOtnPm15MinSpanLossTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossTxHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinSpanLossTxHigh.setUnits("0.1 dB")
_AosDomainOtnPm15MinDefectTable_Object = MibTable
aosDomainOtnPm15MinDefectTable = _AosDomainOtnPm15MinDefectTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectTable.setStatus("current")
_AosDomainOtnPm15MinDefectEntry_Object = MibTableRow
aosDomainOtnPm15MinDefectEntry = _AosDomainOtnPm15MinDefectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1)
)
aosDomainOtnPm15MinDefectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectSample"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectEntry.setStatus("current")


class _AosDomainOtnPm15MinDefectSample_Type(Integer32):
    """Custom type aosDomainOtnPm15MinDefectSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosDomainOtnPm15MinDefectSample_Type.__name__ = "Integer32"
_AosDomainOtnPm15MinDefectSample_Object = MibTableColumn
aosDomainOtnPm15MinDefectSample = _AosDomainOtnPm15MinDefectSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 1),
    _AosDomainOtnPm15MinDefectSample_Type()
)
aosDomainOtnPm15MinDefectSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectSample.setStatus("current")
_AosDomainOtnPm15MinDefectSampleTime_Type = TimeTicks
_AosDomainOtnPm15MinDefectSampleTime_Object = MibTableColumn
aosDomainOtnPm15MinDefectSampleTime = _AosDomainOtnPm15MinDefectSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 2),
    _AosDomainOtnPm15MinDefectSampleTime_Type()
)
aosDomainOtnPm15MinDefectSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectSampleTime.setStatus("current")
_AosDomainOtnPm15MinDefectSes_Type = Integer32
_AosDomainOtnPm15MinDefectSes_Object = MibTableColumn
aosDomainOtnPm15MinDefectSes = _AosDomainOtnPm15MinDefectSes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 3),
    _AosDomainOtnPm15MinDefectSes_Type()
)
aosDomainOtnPm15MinDefectSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectSes.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectSes.setUnits("sec")
_AosDomainOtnPm15MinDefectSesInPayload_Type = Integer32
_AosDomainOtnPm15MinDefectSesInPayload_Object = MibTableColumn
aosDomainOtnPm15MinDefectSesInPayload = _AosDomainOtnPm15MinDefectSesInPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 4),
    _AosDomainOtnPm15MinDefectSesInPayload_Type()
)
aosDomainOtnPm15MinDefectSesInPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectSesInPayload.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectSesInPayload.setUnits("sec")
_AosDomainOtnPm15MinDefectSesInOverhead_Type = Integer32
_AosDomainOtnPm15MinDefectSesInOverhead_Object = MibTableColumn
aosDomainOtnPm15MinDefectSesInOverhead = _AosDomainOtnPm15MinDefectSesInOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 5),
    _AosDomainOtnPm15MinDefectSesInOverhead_Type()
)
aosDomainOtnPm15MinDefectSesInOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectSesInOverhead.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectSesInOverhead.setUnits("sec")
_AosDomainOtnPm15MinDefectUas_Type = Integer32
_AosDomainOtnPm15MinDefectUas_Object = MibTableColumn
aosDomainOtnPm15MinDefectUas = _AosDomainOtnPm15MinDefectUas_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 6),
    _AosDomainOtnPm15MinDefectUas_Type()
)
aosDomainOtnPm15MinDefectUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectUas.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectUas.setUnits("sec")
_AosDomainOtnPm15MinDefectUasInPayload_Type = Integer32
_AosDomainOtnPm15MinDefectUasInPayload_Object = MibTableColumn
aosDomainOtnPm15MinDefectUasInPayload = _AosDomainOtnPm15MinDefectUasInPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 7),
    _AosDomainOtnPm15MinDefectUasInPayload_Type()
)
aosDomainOtnPm15MinDefectUasInPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectUasInPayload.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectUasInPayload.setUnits("sec")
_AosDomainOtnPm15MinDefectUasInOverhead_Type = Integer32
_AosDomainOtnPm15MinDefectUasInOverhead_Object = MibTableColumn
aosDomainOtnPm15MinDefectUasInOverhead = _AosDomainOtnPm15MinDefectUasInOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 8),
    _AosDomainOtnPm15MinDefectUasInOverhead_Type()
)
aosDomainOtnPm15MinDefectUasInOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectUasInOverhead.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectUasInOverhead.setUnits("sec")
_AosDomainOtnPm15MinDefectBbe_Type = Integer32
_AosDomainOtnPm15MinDefectBbe_Object = MibTableColumn
aosDomainOtnPm15MinDefectBbe = _AosDomainOtnPm15MinDefectBbe_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 9),
    _AosDomainOtnPm15MinDefectBbe_Type()
)
aosDomainOtnPm15MinDefectBbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectBbe.setStatus("current")
_AosDomainOtnPm15MinDefectEs_Type = Integer32
_AosDomainOtnPm15MinDefectEs_Object = MibTableColumn
aosDomainOtnPm15MinDefectEs = _AosDomainOtnPm15MinDefectEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 22, 1, 10),
    _AosDomainOtnPm15MinDefectEs_Type()
)
aosDomainOtnPm15MinDefectEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinDefectEs.setStatus("current")
_AosDomainOtnPm15MinQualityTable_Object = MibTable
aosDomainOtnPm15MinQualityTable = _AosDomainOtnPm15MinQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityTable.setStatus("current")
_AosDomainOtnPm15MinQualityEntry_Object = MibTableRow
aosDomainOtnPm15MinQualityEntry = _AosDomainOtnPm15MinQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1)
)
aosDomainOtnPm15MinQualityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualitySample"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEntry.setStatus("current")


class _AosDomainOtnPm15MinQualitySample_Type(Integer32):
    """Custom type aosDomainOtnPm15MinQualitySample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosDomainOtnPm15MinQualitySample_Type.__name__ = "Integer32"
_AosDomainOtnPm15MinQualitySample_Object = MibTableColumn
aosDomainOtnPm15MinQualitySample = _AosDomainOtnPm15MinQualitySample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 1),
    _AosDomainOtnPm15MinQualitySample_Type()
)
aosDomainOtnPm15MinQualitySample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualitySample.setStatus("current")
_AosDomainOtnPm15MinQualitySampleTime_Type = TimeTicks
_AosDomainOtnPm15MinQualitySampleTime_Object = MibTableColumn
aosDomainOtnPm15MinQualitySampleTime = _AosDomainOtnPm15MinQualitySampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 2),
    _AosDomainOtnPm15MinQualitySampleTime_Type()
)
aosDomainOtnPm15MinQualitySampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualitySampleTime.setStatus("current")
_AosDomainOtnPm15MinQualityCdcLow_Type = Integer32
_AosDomainOtnPm15MinQualityCdcLow_Object = MibTableColumn
aosDomainOtnPm15MinQualityCdcLow = _AosDomainOtnPm15MinQualityCdcLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 3),
    _AosDomainOtnPm15MinQualityCdcLow_Type()
)
aosDomainOtnPm15MinQualityCdcLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCdcLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCdcLow.setUnits("ps/nm")
_AosDomainOtnPm15MinQualityCdcMean_Type = Integer32
_AosDomainOtnPm15MinQualityCdcMean_Object = MibTableColumn
aosDomainOtnPm15MinQualityCdcMean = _AosDomainOtnPm15MinQualityCdcMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 4),
    _AosDomainOtnPm15MinQualityCdcMean_Type()
)
aosDomainOtnPm15MinQualityCdcMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCdcMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCdcMean.setUnits("ps/nm")
_AosDomainOtnPm15MinQualityCdcHigh_Type = Integer32
_AosDomainOtnPm15MinQualityCdcHigh_Object = MibTableColumn
aosDomainOtnPm15MinQualityCdcHigh = _AosDomainOtnPm15MinQualityCdcHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 5),
    _AosDomainOtnPm15MinQualityCdcHigh_Type()
)
aosDomainOtnPm15MinQualityCdcHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCdcHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCdcHigh.setUnits("ps/nm")
_AosDomainOtnPm15MinQualityCfoLow_Type = Integer32
_AosDomainOtnPm15MinQualityCfoLow_Object = MibTableColumn
aosDomainOtnPm15MinQualityCfoLow = _AosDomainOtnPm15MinQualityCfoLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 6),
    _AosDomainOtnPm15MinQualityCfoLow_Type()
)
aosDomainOtnPm15MinQualityCfoLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCfoLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCfoLow.setUnits("0.001 GHz")
_AosDomainOtnPm15MinQualityCfoMean_Type = Integer32
_AosDomainOtnPm15MinQualityCfoMean_Object = MibTableColumn
aosDomainOtnPm15MinQualityCfoMean = _AosDomainOtnPm15MinQualityCfoMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 7),
    _AosDomainOtnPm15MinQualityCfoMean_Type()
)
aosDomainOtnPm15MinQualityCfoMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCfoMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCfoMean.setUnits("0.001 GHz")
_AosDomainOtnPm15MinQualityCfoHigh_Type = Integer32
_AosDomainOtnPm15MinQualityCfoHigh_Object = MibTableColumn
aosDomainOtnPm15MinQualityCfoHigh = _AosDomainOtnPm15MinQualityCfoHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 8),
    _AosDomainOtnPm15MinQualityCfoHigh_Type()
)
aosDomainOtnPm15MinQualityCfoHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCfoHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityCfoHigh.setUnits("0.001 GHz")
_AosDomainOtnPm15MinQualitySnrLow_Type = Integer32
_AosDomainOtnPm15MinQualitySnrLow_Object = MibTableColumn
aosDomainOtnPm15MinQualitySnrLow = _AosDomainOtnPm15MinQualitySnrLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 9),
    _AosDomainOtnPm15MinQualitySnrLow_Type()
)
aosDomainOtnPm15MinQualitySnrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualitySnrLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualitySnrLow.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualitySnrMean_Type = Integer32
_AosDomainOtnPm15MinQualitySnrMean_Object = MibTableColumn
aosDomainOtnPm15MinQualitySnrMean = _AosDomainOtnPm15MinQualitySnrMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 10),
    _AosDomainOtnPm15MinQualitySnrMean_Type()
)
aosDomainOtnPm15MinQualitySnrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualitySnrMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualitySnrMean.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualitySnrHigh_Type = Integer32
_AosDomainOtnPm15MinQualitySnrHigh_Object = MibTableColumn
aosDomainOtnPm15MinQualitySnrHigh = _AosDomainOtnPm15MinQualitySnrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 11),
    _AosDomainOtnPm15MinQualitySnrHigh_Type()
)
aosDomainOtnPm15MinQualitySnrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualitySnrHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualitySnrHigh.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityDgdLow_Type = Integer32
_AosDomainOtnPm15MinQualityDgdLow_Object = MibTableColumn
aosDomainOtnPm15MinQualityDgdLow = _AosDomainOtnPm15MinQualityDgdLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 12),
    _AosDomainOtnPm15MinQualityDgdLow_Type()
)
aosDomainOtnPm15MinQualityDgdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityDgdLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityDgdLow.setUnits("ps")
_AosDomainOtnPm15MinQualityDgdMean_Type = Integer32
_AosDomainOtnPm15MinQualityDgdMean_Object = MibTableColumn
aosDomainOtnPm15MinQualityDgdMean = _AosDomainOtnPm15MinQualityDgdMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 13),
    _AosDomainOtnPm15MinQualityDgdMean_Type()
)
aosDomainOtnPm15MinQualityDgdMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityDgdMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityDgdMean.setUnits("ps")
_AosDomainOtnPm15MinQualityDgdHigh_Type = Integer32
_AosDomainOtnPm15MinQualityDgdHigh_Object = MibTableColumn
aosDomainOtnPm15MinQualityDgdHigh = _AosDomainOtnPm15MinQualityDgdHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 14),
    _AosDomainOtnPm15MinQualityDgdHigh_Type()
)
aosDomainOtnPm15MinQualityDgdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityDgdHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityDgdHigh.setUnits("ps")
_AosDomainOtnPm15MinQualityQFactorLow_Type = Integer32
_AosDomainOtnPm15MinQualityQFactorLow_Object = MibTableColumn
aosDomainOtnPm15MinQualityQFactorLow = _AosDomainOtnPm15MinQualityQFactorLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 15),
    _AosDomainOtnPm15MinQualityQFactorLow_Type()
)
aosDomainOtnPm15MinQualityQFactorLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityQFactorLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityQFactorLow.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityQFactorMean_Type = Integer32
_AosDomainOtnPm15MinQualityQFactorMean_Object = MibTableColumn
aosDomainOtnPm15MinQualityQFactorMean = _AosDomainOtnPm15MinQualityQFactorMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 16),
    _AosDomainOtnPm15MinQualityQFactorMean_Type()
)
aosDomainOtnPm15MinQualityQFactorMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityQFactorMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityQFactorMean.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityQFactorHigh_Type = Integer32
_AosDomainOtnPm15MinQualityQFactorHigh_Object = MibTableColumn
aosDomainOtnPm15MinQualityQFactorHigh = _AosDomainOtnPm15MinQualityQFactorHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 23, 1, 17),
    _AosDomainOtnPm15MinQualityQFactorHigh_Type()
)
aosDomainOtnPm15MinQualityQFactorHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityQFactorHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityQFactorHigh.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityEnhancedTable_Object = MibTable
aosDomainOtnPm15MinQualityEnhancedTable = _AosDomainOtnPm15MinQualityEnhancedTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedTable.setStatus("current")
_AosDomainOtnPm15MinQualityEnhancedEntry_Object = MibTableRow
aosDomainOtnPm15MinQualityEnhancedEntry = _AosDomainOtnPm15MinQualityEnhancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1)
)
aosDomainOtnPm15MinQualityEnhancedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedEntry.setStatus("current")


class _AosDomainOtnPm15MinQualityEnhancedSample_Type(Integer32):
    """Custom type aosDomainOtnPm15MinQualityEnhancedSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosDomainOtnPm15MinQualityEnhancedSample_Type.__name__ = "Integer32"
_AosDomainOtnPm15MinQualityEnhancedSample_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedSample = _AosDomainOtnPm15MinQualityEnhancedSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 1),
    _AosDomainOtnPm15MinQualityEnhancedSample_Type()
)
aosDomainOtnPm15MinQualityEnhancedSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedSample.setStatus("current")
_AosDomainOtnPm15MinQualityEnhancedSampleTime_Type = TimeTicks
_AosDomainOtnPm15MinQualityEnhancedSampleTime_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedSampleTime = _AosDomainOtnPm15MinQualityEnhancedSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 2),
    _AosDomainOtnPm15MinQualityEnhancedSampleTime_Type()
)
aosDomainOtnPm15MinQualityEnhancedSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedSampleTime.setStatus("current")
_AosDomainOtnPm15MinQualityEnhancedSoptLow_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedSoptLow_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedSoptLow = _AosDomainOtnPm15MinQualityEnhancedSoptLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 3),
    _AosDomainOtnPm15MinQualityEnhancedSoptLow_Type()
)
aosDomainOtnPm15MinQualityEnhancedSoptLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedSoptLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedSoptLow.setUnits("rad/sec")
_AosDomainOtnPm15MinQualityEnhancedSoptMean_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedSoptMean_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedSoptMean = _AosDomainOtnPm15MinQualityEnhancedSoptMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 4),
    _AosDomainOtnPm15MinQualityEnhancedSoptMean_Type()
)
aosDomainOtnPm15MinQualityEnhancedSoptMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedSoptMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedSoptMean.setUnits("rad/sec")
_AosDomainOtnPm15MinQualityEnhancedSoptHigh_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedSoptHigh_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedSoptHigh = _AosDomainOtnPm15MinQualityEnhancedSoptHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 5),
    _AosDomainOtnPm15MinQualityEnhancedSoptHigh_Type()
)
aosDomainOtnPm15MinQualityEnhancedSoptHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedSoptHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedSoptHigh.setUnits("rad/sec")
_AosDomainOtnPm15MinQualityEnhancedOsnrLow_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedOsnrLow_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedOsnrLow = _AosDomainOtnPm15MinQualityEnhancedOsnrLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 6),
    _AosDomainOtnPm15MinQualityEnhancedOsnrLow_Type()
)
aosDomainOtnPm15MinQualityEnhancedOsnrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedOsnrLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedOsnrLow.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityEnhancedOsnrMean_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedOsnrMean_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedOsnrMean = _AosDomainOtnPm15MinQualityEnhancedOsnrMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 7),
    _AosDomainOtnPm15MinQualityEnhancedOsnrMean_Type()
)
aosDomainOtnPm15MinQualityEnhancedOsnrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedOsnrMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedOsnrMean.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityEnhancedOsnrHigh_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedOsnrHigh_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedOsnrHigh = _AosDomainOtnPm15MinQualityEnhancedOsnrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 8),
    _AosDomainOtnPm15MinQualityEnhancedOsnrHigh_Type()
)
aosDomainOtnPm15MinQualityEnhancedOsnrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedOsnrHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedOsnrHigh.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityEnhancedPdlLow_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedPdlLow_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedPdlLow = _AosDomainOtnPm15MinQualityEnhancedPdlLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 9),
    _AosDomainOtnPm15MinQualityEnhancedPdlLow_Type()
)
aosDomainOtnPm15MinQualityEnhancedPdlLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedPdlLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedPdlLow.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityEnhancedPdlMean_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedPdlMean_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedPdlMean = _AosDomainOtnPm15MinQualityEnhancedPdlMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 10),
    _AosDomainOtnPm15MinQualityEnhancedPdlMean_Type()
)
aosDomainOtnPm15MinQualityEnhancedPdlMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedPdlMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedPdlMean.setUnits("0.1 dB")
_AosDomainOtnPm15MinQualityEnhancedPdlHigh_Type = Integer32
_AosDomainOtnPm15MinQualityEnhancedPdlHigh_Object = MibTableColumn
aosDomainOtnPm15MinQualityEnhancedPdlHigh = _AosDomainOtnPm15MinQualityEnhancedPdlHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 24, 1, 11),
    _AosDomainOtnPm15MinQualityEnhancedPdlHigh_Type()
)
aosDomainOtnPm15MinQualityEnhancedPdlHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedPdlHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm15MinQualityEnhancedPdlHigh.setUnits("0.1 dB")
_AosDomainOtnPm1DayOscOptPowerTable_Object = MibTable
aosDomainOtnPm1DayOscOptPowerTable = _AosDomainOtnPm1DayOscOptPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerTable.setStatus("current")
_AosDomainOtnPm1DayOscOptPowerEntry_Object = MibTableRow
aosDomainOtnPm1DayOscOptPowerEntry = _AosDomainOtnPm1DayOscOptPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1)
)
aosDomainOtnPm1DayOscOptPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayOscOptPowerSample"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerEntry.setStatus("current")


class _AosDomainOtnPm1DayOscOptPowerSample_Type(Integer32):
    """Custom type aosDomainOtnPm1DayOscOptPowerSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AosDomainOtnPm1DayOscOptPowerSample_Type.__name__ = "Integer32"
_AosDomainOtnPm1DayOscOptPowerSample_Object = MibTableColumn
aosDomainOtnPm1DayOscOptPowerSample = _AosDomainOtnPm1DayOscOptPowerSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1, 1),
    _AosDomainOtnPm1DayOscOptPowerSample_Type()
)
aosDomainOtnPm1DayOscOptPowerSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerSample.setStatus("current")
_AosDomainOtnPm1DayOscOptPowerSampleTime_Type = TimeTicks
_AosDomainOtnPm1DayOscOptPowerSampleTime_Object = MibTableColumn
aosDomainOtnPm1DayOscOptPowerSampleTime = _AosDomainOtnPm1DayOscOptPowerSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1, 2),
    _AosDomainOtnPm1DayOscOptPowerSampleTime_Type()
)
aosDomainOtnPm1DayOscOptPowerSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerSampleTime.setStatus("current")
_AosDomainOtnPm1DayOscOptPowerRxLow_Type = Integer32
_AosDomainOtnPm1DayOscOptPowerRxLow_Object = MibTableColumn
aosDomainOtnPm1DayOscOptPowerRxLow = _AosDomainOtnPm1DayOscOptPowerRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1, 3),
    _AosDomainOtnPm1DayOscOptPowerRxLow_Type()
)
aosDomainOtnPm1DayOscOptPowerRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerRxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerRxLow.setUnits("0.1 dBm")
_AosDomainOtnPm1DayOscOptPowerRxMean_Type = Integer32
_AosDomainOtnPm1DayOscOptPowerRxMean_Object = MibTableColumn
aosDomainOtnPm1DayOscOptPowerRxMean = _AosDomainOtnPm1DayOscOptPowerRxMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1, 4),
    _AosDomainOtnPm1DayOscOptPowerRxMean_Type()
)
aosDomainOtnPm1DayOscOptPowerRxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerRxMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerRxMean.setUnits("0.1 dBm")
_AosDomainOtnPm1DayOscOptPowerRxHigh_Type = Integer32
_AosDomainOtnPm1DayOscOptPowerRxHigh_Object = MibTableColumn
aosDomainOtnPm1DayOscOptPowerRxHigh = _AosDomainOtnPm1DayOscOptPowerRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1, 5),
    _AosDomainOtnPm1DayOscOptPowerRxHigh_Type()
)
aosDomainOtnPm1DayOscOptPowerRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerRxHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerRxHigh.setUnits("0.1 dBm")
_AosDomainOtnPm1DayOscOptPowerTxLow_Type = Integer32
_AosDomainOtnPm1DayOscOptPowerTxLow_Object = MibTableColumn
aosDomainOtnPm1DayOscOptPowerTxLow = _AosDomainOtnPm1DayOscOptPowerTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1, 6),
    _AosDomainOtnPm1DayOscOptPowerTxLow_Type()
)
aosDomainOtnPm1DayOscOptPowerTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerTxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerTxLow.setUnits("0.1 dBm")
_AosDomainOtnPm1DayOscOptPowerTxMean_Type = Integer32
_AosDomainOtnPm1DayOscOptPowerTxMean_Object = MibTableColumn
aosDomainOtnPm1DayOscOptPowerTxMean = _AosDomainOtnPm1DayOscOptPowerTxMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1, 7),
    _AosDomainOtnPm1DayOscOptPowerTxMean_Type()
)
aosDomainOtnPm1DayOscOptPowerTxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerTxMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerTxMean.setUnits("0.1 dBm")
_AosDomainOtnPm1DayOscOptPowerTxHigh_Type = Integer32
_AosDomainOtnPm1DayOscOptPowerTxHigh_Object = MibTableColumn
aosDomainOtnPm1DayOscOptPowerTxHigh = _AosDomainOtnPm1DayOscOptPowerTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 40, 1, 8),
    _AosDomainOtnPm1DayOscOptPowerTxHigh_Type()
)
aosDomainOtnPm1DayOscOptPowerTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerTxHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayOscOptPowerTxHigh.setUnits("0.1 dBm")
_AosDomainOtnPm1DaySpanLossTable_Object = MibTable
aosDomainOtnPm1DaySpanLossTable = _AosDomainOtnPm1DaySpanLossTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossTable.setStatus("current")
_AosDomainOtnPm1DaySpanLossEntry_Object = MibTableRow
aosDomainOtnPm1DaySpanLossEntry = _AosDomainOtnPm1DaySpanLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1)
)
aosDomainOtnPm1DaySpanLossEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DaySpanLossSample"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossEntry.setStatus("current")


class _AosDomainOtnPm1DaySpanLossSample_Type(Integer32):
    """Custom type aosDomainOtnPm1DaySpanLossSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AosDomainOtnPm1DaySpanLossSample_Type.__name__ = "Integer32"
_AosDomainOtnPm1DaySpanLossSample_Object = MibTableColumn
aosDomainOtnPm1DaySpanLossSample = _AosDomainOtnPm1DaySpanLossSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1, 1),
    _AosDomainOtnPm1DaySpanLossSample_Type()
)
aosDomainOtnPm1DaySpanLossSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossSample.setStatus("current")
_AosDomainOtnPm1DaySpanLossSampleTime_Type = TimeTicks
_AosDomainOtnPm1DaySpanLossSampleTime_Object = MibTableColumn
aosDomainOtnPm1DaySpanLossSampleTime = _AosDomainOtnPm1DaySpanLossSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1, 2),
    _AosDomainOtnPm1DaySpanLossSampleTime_Type()
)
aosDomainOtnPm1DaySpanLossSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossSampleTime.setStatus("current")
_AosDomainOtnPm1DaySpanLossRxLow_Type = Integer32
_AosDomainOtnPm1DaySpanLossRxLow_Object = MibTableColumn
aosDomainOtnPm1DaySpanLossRxLow = _AosDomainOtnPm1DaySpanLossRxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1, 3),
    _AosDomainOtnPm1DaySpanLossRxLow_Type()
)
aosDomainOtnPm1DaySpanLossRxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossRxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossRxLow.setUnits("0.1 dB")
_AosDomainOtnPm1DaySpanLossRxMean_Type = Integer32
_AosDomainOtnPm1DaySpanLossRxMean_Object = MibTableColumn
aosDomainOtnPm1DaySpanLossRxMean = _AosDomainOtnPm1DaySpanLossRxMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1, 4),
    _AosDomainOtnPm1DaySpanLossRxMean_Type()
)
aosDomainOtnPm1DaySpanLossRxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossRxMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossRxMean.setUnits("0.1 dB")
_AosDomainOtnPm1DaySpanLossRxHigh_Type = Integer32
_AosDomainOtnPm1DaySpanLossRxHigh_Object = MibTableColumn
aosDomainOtnPm1DaySpanLossRxHigh = _AosDomainOtnPm1DaySpanLossRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1, 5),
    _AosDomainOtnPm1DaySpanLossRxHigh_Type()
)
aosDomainOtnPm1DaySpanLossRxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossRxHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossRxHigh.setUnits("0.1 dB")
_AosDomainOtnPm1DaySpanLossTxLow_Type = Integer32
_AosDomainOtnPm1DaySpanLossTxLow_Object = MibTableColumn
aosDomainOtnPm1DaySpanLossTxLow = _AosDomainOtnPm1DaySpanLossTxLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1, 6),
    _AosDomainOtnPm1DaySpanLossTxLow_Type()
)
aosDomainOtnPm1DaySpanLossTxLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossTxLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossTxLow.setUnits("0.1 dB")
_AosDomainOtnPm1DaySpanLossTxMean_Type = Integer32
_AosDomainOtnPm1DaySpanLossTxMean_Object = MibTableColumn
aosDomainOtnPm1DaySpanLossTxMean = _AosDomainOtnPm1DaySpanLossTxMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1, 7),
    _AosDomainOtnPm1DaySpanLossTxMean_Type()
)
aosDomainOtnPm1DaySpanLossTxMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossTxMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossTxMean.setUnits("0.1 dB")
_AosDomainOtnPm1DaySpanLossTxHigh_Type = Integer32
_AosDomainOtnPm1DaySpanLossTxHigh_Object = MibTableColumn
aosDomainOtnPm1DaySpanLossTxHigh = _AosDomainOtnPm1DaySpanLossTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 41, 1, 8),
    _AosDomainOtnPm1DaySpanLossTxHigh_Type()
)
aosDomainOtnPm1DaySpanLossTxHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossTxHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DaySpanLossTxHigh.setUnits("0.1 dB")
_AosDomainOtnPm1DayDefectTable_Object = MibTable
aosDomainOtnPm1DayDefectTable = _AosDomainOtnPm1DayDefectTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectTable.setStatus("current")
_AosDomainOtnPm1DayDefectEntry_Object = MibTableRow
aosDomainOtnPm1DayDefectEntry = _AosDomainOtnPm1DayDefectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1)
)
aosDomainOtnPm1DayDefectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectSample"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectEntry.setStatus("current")


class _AosDomainOtnPm1DayDefectSample_Type(Integer32):
    """Custom type aosDomainOtnPm1DayDefectSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosDomainOtnPm1DayDefectSample_Type.__name__ = "Integer32"
_AosDomainOtnPm1DayDefectSample_Object = MibTableColumn
aosDomainOtnPm1DayDefectSample = _AosDomainOtnPm1DayDefectSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 1),
    _AosDomainOtnPm1DayDefectSample_Type()
)
aosDomainOtnPm1DayDefectSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectSample.setStatus("current")
_AosDomainOtnPm1DayDefectSampleTime_Type = TimeTicks
_AosDomainOtnPm1DayDefectSampleTime_Object = MibTableColumn
aosDomainOtnPm1DayDefectSampleTime = _AosDomainOtnPm1DayDefectSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 2),
    _AosDomainOtnPm1DayDefectSampleTime_Type()
)
aosDomainOtnPm1DayDefectSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectSampleTime.setStatus("current")
_AosDomainOtnPm1DayDefectSes_Type = Integer32
_AosDomainOtnPm1DayDefectSes_Object = MibTableColumn
aosDomainOtnPm1DayDefectSes = _AosDomainOtnPm1DayDefectSes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 3),
    _AosDomainOtnPm1DayDefectSes_Type()
)
aosDomainOtnPm1DayDefectSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectSes.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectSes.setUnits("sec")
_AosDomainOtnPm1DayDefectSesInPayload_Type = Integer32
_AosDomainOtnPm1DayDefectSesInPayload_Object = MibTableColumn
aosDomainOtnPm1DayDefectSesInPayload = _AosDomainOtnPm1DayDefectSesInPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 4),
    _AosDomainOtnPm1DayDefectSesInPayload_Type()
)
aosDomainOtnPm1DayDefectSesInPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectSesInPayload.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectSesInPayload.setUnits("sec")
_AosDomainOtnPm1DayDefectSesInOverhead_Type = Integer32
_AosDomainOtnPm1DayDefectSesInOverhead_Object = MibTableColumn
aosDomainOtnPm1DayDefectSesInOverhead = _AosDomainOtnPm1DayDefectSesInOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 5),
    _AosDomainOtnPm1DayDefectSesInOverhead_Type()
)
aosDomainOtnPm1DayDefectSesInOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectSesInOverhead.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectSesInOverhead.setUnits("sec")
_AosDomainOtnPm1DayDefectUas_Type = Integer32
_AosDomainOtnPm1DayDefectUas_Object = MibTableColumn
aosDomainOtnPm1DayDefectUas = _AosDomainOtnPm1DayDefectUas_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 6),
    _AosDomainOtnPm1DayDefectUas_Type()
)
aosDomainOtnPm1DayDefectUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectUas.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectUas.setUnits("sec")
_AosDomainOtnPm1DayDefectUasInPayload_Type = Integer32
_AosDomainOtnPm1DayDefectUasInPayload_Object = MibTableColumn
aosDomainOtnPm1DayDefectUasInPayload = _AosDomainOtnPm1DayDefectUasInPayload_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 7),
    _AosDomainOtnPm1DayDefectUasInPayload_Type()
)
aosDomainOtnPm1DayDefectUasInPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectUasInPayload.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectUasInPayload.setUnits("sec")
_AosDomainOtnPm1DayDefectUasInOverhead_Type = Integer32
_AosDomainOtnPm1DayDefectUasInOverhead_Object = MibTableColumn
aosDomainOtnPm1DayDefectUasInOverhead = _AosDomainOtnPm1DayDefectUasInOverhead_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 8),
    _AosDomainOtnPm1DayDefectUasInOverhead_Type()
)
aosDomainOtnPm1DayDefectUasInOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectUasInOverhead.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectUasInOverhead.setUnits("sec")
_AosDomainOtnPm1DayDefectBbe_Type = Integer32
_AosDomainOtnPm1DayDefectBbe_Object = MibTableColumn
aosDomainOtnPm1DayDefectBbe = _AosDomainOtnPm1DayDefectBbe_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 9),
    _AosDomainOtnPm1DayDefectBbe_Type()
)
aosDomainOtnPm1DayDefectBbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectBbe.setStatus("current")
_AosDomainOtnPm1DayDefectEs_Type = Integer32
_AosDomainOtnPm1DayDefectEs_Object = MibTableColumn
aosDomainOtnPm1DayDefectEs = _AosDomainOtnPm1DayDefectEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 42, 1, 10),
    _AosDomainOtnPm1DayDefectEs_Type()
)
aosDomainOtnPm1DayDefectEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayDefectEs.setStatus("current")
_AosDomainOtnPm1DayQualityTable_Object = MibTable
aosDomainOtnPm1DayQualityTable = _AosDomainOtnPm1DayQualityTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityTable.setStatus("current")
_AosDomainOtnPm1DayQualityEntry_Object = MibTableRow
aosDomainOtnPm1DayQualityEntry = _AosDomainOtnPm1DayQualityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1)
)
aosDomainOtnPm1DayQualityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualitySample"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEntry.setStatus("current")


class _AosDomainOtnPm1DayQualitySample_Type(Integer32):
    """Custom type aosDomainOtnPm1DayQualitySample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AosDomainOtnPm1DayQualitySample_Type.__name__ = "Integer32"
_AosDomainOtnPm1DayQualitySample_Object = MibTableColumn
aosDomainOtnPm1DayQualitySample = _AosDomainOtnPm1DayQualitySample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 1),
    _AosDomainOtnPm1DayQualitySample_Type()
)
aosDomainOtnPm1DayQualitySample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualitySample.setStatus("current")
_AosDomainOtnPm1DayQualitySampleTime_Type = TimeTicks
_AosDomainOtnPm1DayQualitySampleTime_Object = MibTableColumn
aosDomainOtnPm1DayQualitySampleTime = _AosDomainOtnPm1DayQualitySampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 2),
    _AosDomainOtnPm1DayQualitySampleTime_Type()
)
aosDomainOtnPm1DayQualitySampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualitySampleTime.setStatus("current")
_AosDomainOtnPm1DayQualityCdcLow_Type = Integer32
_AosDomainOtnPm1DayQualityCdcLow_Object = MibTableColumn
aosDomainOtnPm1DayQualityCdcLow = _AosDomainOtnPm1DayQualityCdcLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 3),
    _AosDomainOtnPm1DayQualityCdcLow_Type()
)
aosDomainOtnPm1DayQualityCdcLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCdcLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCdcLow.setUnits("ps/nm")
_AosDomainOtnPm1DayQualityCdcMean_Type = Integer32
_AosDomainOtnPm1DayQualityCdcMean_Object = MibTableColumn
aosDomainOtnPm1DayQualityCdcMean = _AosDomainOtnPm1DayQualityCdcMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 4),
    _AosDomainOtnPm1DayQualityCdcMean_Type()
)
aosDomainOtnPm1DayQualityCdcMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCdcMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCdcMean.setUnits("ps/nm")
_AosDomainOtnPm1DayQualityCdcHigh_Type = Integer32
_AosDomainOtnPm1DayQualityCdcHigh_Object = MibTableColumn
aosDomainOtnPm1DayQualityCdcHigh = _AosDomainOtnPm1DayQualityCdcHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 5),
    _AosDomainOtnPm1DayQualityCdcHigh_Type()
)
aosDomainOtnPm1DayQualityCdcHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCdcHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCdcHigh.setUnits("ps/nm")
_AosDomainOtnPm1DayQualityCfoLow_Type = Integer32
_AosDomainOtnPm1DayQualityCfoLow_Object = MibTableColumn
aosDomainOtnPm1DayQualityCfoLow = _AosDomainOtnPm1DayQualityCfoLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 6),
    _AosDomainOtnPm1DayQualityCfoLow_Type()
)
aosDomainOtnPm1DayQualityCfoLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCfoLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCfoLow.setUnits("0.001 GHz")
_AosDomainOtnPm1DayQualityCfoMean_Type = Integer32
_AosDomainOtnPm1DayQualityCfoMean_Object = MibTableColumn
aosDomainOtnPm1DayQualityCfoMean = _AosDomainOtnPm1DayQualityCfoMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 7),
    _AosDomainOtnPm1DayQualityCfoMean_Type()
)
aosDomainOtnPm1DayQualityCfoMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCfoMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCfoMean.setUnits("0.001 GHz")
_AosDomainOtnPm1DayQualityCfoHigh_Type = Integer32
_AosDomainOtnPm1DayQualityCfoHigh_Object = MibTableColumn
aosDomainOtnPm1DayQualityCfoHigh = _AosDomainOtnPm1DayQualityCfoHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 8),
    _AosDomainOtnPm1DayQualityCfoHigh_Type()
)
aosDomainOtnPm1DayQualityCfoHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCfoHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityCfoHigh.setUnits("0.001 GHz")
_AosDomainOtnPm1DayQualitySnrLow_Type = Integer32
_AosDomainOtnPm1DayQualitySnrLow_Object = MibTableColumn
aosDomainOtnPm1DayQualitySnrLow = _AosDomainOtnPm1DayQualitySnrLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 9),
    _AosDomainOtnPm1DayQualitySnrLow_Type()
)
aosDomainOtnPm1DayQualitySnrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualitySnrLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualitySnrLow.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualitySnrMean_Type = Integer32
_AosDomainOtnPm1DayQualitySnrMean_Object = MibTableColumn
aosDomainOtnPm1DayQualitySnrMean = _AosDomainOtnPm1DayQualitySnrMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 10),
    _AosDomainOtnPm1DayQualitySnrMean_Type()
)
aosDomainOtnPm1DayQualitySnrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualitySnrMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualitySnrMean.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualitySnrHigh_Type = Integer32
_AosDomainOtnPm1DayQualitySnrHigh_Object = MibTableColumn
aosDomainOtnPm1DayQualitySnrHigh = _AosDomainOtnPm1DayQualitySnrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 11),
    _AosDomainOtnPm1DayQualitySnrHigh_Type()
)
aosDomainOtnPm1DayQualitySnrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualitySnrHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualitySnrHigh.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityDgdLow_Type = Integer32
_AosDomainOtnPm1DayQualityDgdLow_Object = MibTableColumn
aosDomainOtnPm1DayQualityDgdLow = _AosDomainOtnPm1DayQualityDgdLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 12),
    _AosDomainOtnPm1DayQualityDgdLow_Type()
)
aosDomainOtnPm1DayQualityDgdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityDgdLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityDgdLow.setUnits("ps")
_AosDomainOtnPm1DayQualityDgdMean_Type = Integer32
_AosDomainOtnPm1DayQualityDgdMean_Object = MibTableColumn
aosDomainOtnPm1DayQualityDgdMean = _AosDomainOtnPm1DayQualityDgdMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 13),
    _AosDomainOtnPm1DayQualityDgdMean_Type()
)
aosDomainOtnPm1DayQualityDgdMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityDgdMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityDgdMean.setUnits("ps")
_AosDomainOtnPm1DayQualityDgdHigh_Type = Integer32
_AosDomainOtnPm1DayQualityDgdHigh_Object = MibTableColumn
aosDomainOtnPm1DayQualityDgdHigh = _AosDomainOtnPm1DayQualityDgdHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 14),
    _AosDomainOtnPm1DayQualityDgdHigh_Type()
)
aosDomainOtnPm1DayQualityDgdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityDgdHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityDgdHigh.setUnits("ps")
_AosDomainOtnPm1DayQualityQFactorLow_Type = Integer32
_AosDomainOtnPm1DayQualityQFactorLow_Object = MibTableColumn
aosDomainOtnPm1DayQualityQFactorLow = _AosDomainOtnPm1DayQualityQFactorLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 15),
    _AosDomainOtnPm1DayQualityQFactorLow_Type()
)
aosDomainOtnPm1DayQualityQFactorLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityQFactorLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityQFactorLow.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityQFactorMean_Type = Integer32
_AosDomainOtnPm1DayQualityQFactorMean_Object = MibTableColumn
aosDomainOtnPm1DayQualityQFactorMean = _AosDomainOtnPm1DayQualityQFactorMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 16),
    _AosDomainOtnPm1DayQualityQFactorMean_Type()
)
aosDomainOtnPm1DayQualityQFactorMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityQFactorMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityQFactorMean.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityQFactorHigh_Type = Integer32
_AosDomainOtnPm1DayQualityQFactorHigh_Object = MibTableColumn
aosDomainOtnPm1DayQualityQFactorHigh = _AosDomainOtnPm1DayQualityQFactorHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 43, 1, 17),
    _AosDomainOtnPm1DayQualityQFactorHigh_Type()
)
aosDomainOtnPm1DayQualityQFactorHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityQFactorHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityQFactorHigh.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityEnhancedTable_Object = MibTable
aosDomainOtnPm1DayQualityEnhancedTable = _AosDomainOtnPm1DayQualityEnhancedTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44)
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedTable.setStatus("current")
_AosDomainOtnPm1DayQualityEnhancedEntry_Object = MibTableRow
aosDomainOtnPm1DayQualityEnhancedEntry = _AosDomainOtnPm1DayQualityEnhancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1)
)
aosDomainOtnPm1DayQualityEnhancedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedEntry.setStatus("current")


class _AosDomainOtnPm1DayQualityEnhancedSample_Type(Integer32):
    """Custom type aosDomainOtnPm1DayQualityEnhancedSample based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AosDomainOtnPm1DayQualityEnhancedSample_Type.__name__ = "Integer32"
_AosDomainOtnPm1DayQualityEnhancedSample_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedSample = _AosDomainOtnPm1DayQualityEnhancedSample_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 1),
    _AosDomainOtnPm1DayQualityEnhancedSample_Type()
)
aosDomainOtnPm1DayQualityEnhancedSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedSample.setStatus("current")
_AosDomainOtnPm1DayQualityEnhancedSampleTime_Type = TimeTicks
_AosDomainOtnPm1DayQualityEnhancedSampleTime_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedSampleTime = _AosDomainOtnPm1DayQualityEnhancedSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 2),
    _AosDomainOtnPm1DayQualityEnhancedSampleTime_Type()
)
aosDomainOtnPm1DayQualityEnhancedSampleTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedSampleTime.setStatus("current")
_AosDomainOtnPm1DayQualityEnhancedSoptLow_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedSoptLow_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedSoptLow = _AosDomainOtnPm1DayQualityEnhancedSoptLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 3),
    _AosDomainOtnPm1DayQualityEnhancedSoptLow_Type()
)
aosDomainOtnPm1DayQualityEnhancedSoptLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedSoptLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedSoptLow.setUnits("rad/sec")
_AosDomainOtnPm1DayQualityEnhancedSoptMean_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedSoptMean_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedSoptMean = _AosDomainOtnPm1DayQualityEnhancedSoptMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 4),
    _AosDomainOtnPm1DayQualityEnhancedSoptMean_Type()
)
aosDomainOtnPm1DayQualityEnhancedSoptMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedSoptMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedSoptMean.setUnits("rad/sec")
_AosDomainOtnPm1DayQualityEnhancedSoptHigh_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedSoptHigh_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedSoptHigh = _AosDomainOtnPm1DayQualityEnhancedSoptHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 5),
    _AosDomainOtnPm1DayQualityEnhancedSoptHigh_Type()
)
aosDomainOtnPm1DayQualityEnhancedSoptHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedSoptHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedSoptHigh.setUnits("rad/sec")
_AosDomainOtnPm1DayQualityEnhancedOsnrLow_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedOsnrLow_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedOsnrLow = _AosDomainOtnPm1DayQualityEnhancedOsnrLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 6),
    _AosDomainOtnPm1DayQualityEnhancedOsnrLow_Type()
)
aosDomainOtnPm1DayQualityEnhancedOsnrLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedOsnrLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedOsnrLow.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityEnhancedOsnrMean_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedOsnrMean_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedOsnrMean = _AosDomainOtnPm1DayQualityEnhancedOsnrMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 7),
    _AosDomainOtnPm1DayQualityEnhancedOsnrMean_Type()
)
aosDomainOtnPm1DayQualityEnhancedOsnrMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedOsnrMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedOsnrMean.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityEnhancedOsnrHigh_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedOsnrHigh_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedOsnrHigh = _AosDomainOtnPm1DayQualityEnhancedOsnrHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 8),
    _AosDomainOtnPm1DayQualityEnhancedOsnrHigh_Type()
)
aosDomainOtnPm1DayQualityEnhancedOsnrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedOsnrHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedOsnrHigh.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityEnhancedPdlLow_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedPdlLow_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedPdlLow = _AosDomainOtnPm1DayQualityEnhancedPdlLow_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 9),
    _AosDomainOtnPm1DayQualityEnhancedPdlLow_Type()
)
aosDomainOtnPm1DayQualityEnhancedPdlLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedPdlLow.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedPdlLow.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityEnhancedPdlMean_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedPdlMean_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedPdlMean = _AosDomainOtnPm1DayQualityEnhancedPdlMean_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 10),
    _AosDomainOtnPm1DayQualityEnhancedPdlMean_Type()
)
aosDomainOtnPm1DayQualityEnhancedPdlMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedPdlMean.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedPdlMean.setUnits("0.1 dB")
_AosDomainOtnPm1DayQualityEnhancedPdlHigh_Type = Integer32
_AosDomainOtnPm1DayQualityEnhancedPdlHigh_Object = MibTableColumn
aosDomainOtnPm1DayQualityEnhancedPdlHigh = _AosDomainOtnPm1DayQualityEnhancedPdlHigh_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 2, 44, 1, 11),
    _AosDomainOtnPm1DayQualityEnhancedPdlHigh_Type()
)
aosDomainOtnPm1DayQualityEnhancedPdlHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedPdlHigh.setStatus("current")
if mibBuilder.loadTexts:
    aosDomainOtnPm1DayQualityEnhancedPdlHigh.setUnits("0.1 dB")
_AosDomainOtnPmConformance_ObjectIdentity = ObjectIdentity
aosDomainOtnPmConformance = _AosDomainOtnPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 3)
)
_AosDomainOtnPmCompliances_ObjectIdentity = ObjectIdentity
aosDomainOtnPmCompliances = _AosDomainOtnPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 3, 1)
)
_AosDomainOtnPmGroups_ObjectIdentity = ObjectIdentity
aosDomainOtnPmGroups = _AosDomainOtnPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 3, 2)
)

# Managed Objects groups

aosDomainOtnPmStatsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 3, 2, 1)
)
aosDomainOtnPmStatsObjectGroup.setObjects(
      *(("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmOscOptPowerRx"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmOscOptPowerTx"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmOscLaserBiasCurr"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmOscLaserTemp"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmSpanLossRx"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmSpanLossTx"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmAmpOperTime"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmAmpTotalGain"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmAmpTotalLase"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmQualityCdc"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmQualityCfo"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmQualitySnr"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmQualityDgd"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmQualityQFactor"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmQualityEnhancedSopt"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmQualityEnhancedOsnr"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmQualityEnhancedPdl"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinOscOptPowerRxLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinOscOptPowerRxMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinOscOptPowerRxHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinOscOptPowerTxLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinOscOptPowerTxMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinOscOptPowerTxHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinSpanLossRxLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinSpanLossRxMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinSpanLossRxHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinSpanLossTxLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinSpanLossTxMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinSpanLossTxHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectSes"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectSesInPayload"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectSesInOverhead"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectUas"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectUasInPayload"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectUasInOverhead"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectBbe"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinDefectEs"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityCdcLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityCdcMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityCdcHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityCfoLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityCfoMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityCfoHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualitySnrLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualitySnrMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualitySnrHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityDgdLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityDgdMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityDgdHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityQFactorLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityQFactorMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityQFactorHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedSoptLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedSoptMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedSoptHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedOsnrLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedOsnrMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedOsnrHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedPdlLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedPdlMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm15MinQualityEnhancedPdlHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayOscOptPowerRxLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayOscOptPowerRxMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayOscOptPowerRxHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayOscOptPowerTxLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayOscOptPowerTxMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayOscOptPowerTxHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DaySpanLossRxLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DaySpanLossRxMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DaySpanLossRxHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DaySpanLossTxLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DaySpanLossTxMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DaySpanLossTxHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectSes"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectSesInPayload"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectSesInOverhead"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectUas"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectUasInPayload"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectUasInOverhead"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectBbe"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayDefectEs"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityCdcLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityCdcMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityCdcHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityCfoLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityCfoMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityCfoHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualitySnrLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualitySnrMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualitySnrHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityDgdLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityDgdMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityDgdHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityQFactorLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityQFactorMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityQFactorHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedSoptLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedSoptMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedSoptHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedOsnrLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedOsnrMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedOsnrHigh"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedPdlLow"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedPdlMean"),
        ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPm1DayQualityEnhancedPdlHigh"))
)
if mibBuilder.loadTexts:
    aosDomainOtnPmStatsObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aosDomainOtnPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 20, 1, 5, 3, 1, 1)
)
aosDomainOtnPmCompliance.setObjects(
    ("AOS-DOMAIN-OTN-PM-MIB", "aosDomainOtnPmStatsObjectGroup")
)
if mibBuilder.loadTexts:
    aosDomainOtnPmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AOS-DOMAIN-OTN-PM-MIB",
    **{"aosDomainOtnPmMIB": aosDomainOtnPmMIB,
       "aosDomainOtnPmObjects": aosDomainOtnPmObjects,
       "aosDomainOtnPmStatsObjects": aosDomainOtnPmStatsObjects,
       "aosDomainOtnPmOscOptPowerTable": aosDomainOtnPmOscOptPowerTable,
       "aosDomainOtnPmOscOptPowerEntry": aosDomainOtnPmOscOptPowerEntry,
       "aosDomainOtnPmOscOptPowerRx": aosDomainOtnPmOscOptPowerRx,
       "aosDomainOtnPmOscOptPowerTx": aosDomainOtnPmOscOptPowerTx,
       "aosDomainOtnPmOscLaserTable": aosDomainOtnPmOscLaserTable,
       "aosDomainOtnPmOscLaserEntry": aosDomainOtnPmOscLaserEntry,
       "aosDomainOtnPmOscLaserBiasCurr": aosDomainOtnPmOscLaserBiasCurr,
       "aosDomainOtnPmOscLaserTemp": aosDomainOtnPmOscLaserTemp,
       "aosDomainOtnPmSpanLossTable": aosDomainOtnPmSpanLossTable,
       "aosDomainOtnPmSpanLossEntry": aosDomainOtnPmSpanLossEntry,
       "aosDomainOtnPmSpanLossRx": aosDomainOtnPmSpanLossRx,
       "aosDomainOtnPmSpanLossTx": aosDomainOtnPmSpanLossTx,
       "aosDomainOtnPmAmpTable": aosDomainOtnPmAmpTable,
       "aosDomainOtnPmAmpEntry": aosDomainOtnPmAmpEntry,
       "aosDomainOtnPmAmpOperTime": aosDomainOtnPmAmpOperTime,
       "aosDomainOtnPmAmpTotalGain": aosDomainOtnPmAmpTotalGain,
       "aosDomainOtnPmAmpTotalLase": aosDomainOtnPmAmpTotalLase,
       "aosDomainOtnPmQualityTable": aosDomainOtnPmQualityTable,
       "aosDomainOtnPmQualityEntry": aosDomainOtnPmQualityEntry,
       "aosDomainOtnPmQualityCdc": aosDomainOtnPmQualityCdc,
       "aosDomainOtnPmQualityCfo": aosDomainOtnPmQualityCfo,
       "aosDomainOtnPmQualitySnr": aosDomainOtnPmQualitySnr,
       "aosDomainOtnPmQualityDgd": aosDomainOtnPmQualityDgd,
       "aosDomainOtnPmQualityQFactor": aosDomainOtnPmQualityQFactor,
       "aosDomainOtnPmQualityEnhancedTable": aosDomainOtnPmQualityEnhancedTable,
       "aosDomainOtnPmQualityEnhancedEntry": aosDomainOtnPmQualityEnhancedEntry,
       "aosDomainOtnPmQualityEnhancedSopt": aosDomainOtnPmQualityEnhancedSopt,
       "aosDomainOtnPmQualityEnhancedOsnr": aosDomainOtnPmQualityEnhancedOsnr,
       "aosDomainOtnPmQualityEnhancedPdl": aosDomainOtnPmQualityEnhancedPdl,
       "aosDomainOtnPm15MinOscOptPowerTable": aosDomainOtnPm15MinOscOptPowerTable,
       "aosDomainOtnPm15MinOscOptPowerEntry": aosDomainOtnPm15MinOscOptPowerEntry,
       "aosDomainOtnPm15MinOscOptPowerSample": aosDomainOtnPm15MinOscOptPowerSample,
       "aosDomainOtnPm15MinOscOptPowerSampleTime": aosDomainOtnPm15MinOscOptPowerSampleTime,
       "aosDomainOtnPm15MinOscOptPowerRxLow": aosDomainOtnPm15MinOscOptPowerRxLow,
       "aosDomainOtnPm15MinOscOptPowerRxMean": aosDomainOtnPm15MinOscOptPowerRxMean,
       "aosDomainOtnPm15MinOscOptPowerRxHigh": aosDomainOtnPm15MinOscOptPowerRxHigh,
       "aosDomainOtnPm15MinOscOptPowerTxLow": aosDomainOtnPm15MinOscOptPowerTxLow,
       "aosDomainOtnPm15MinOscOptPowerTxMean": aosDomainOtnPm15MinOscOptPowerTxMean,
       "aosDomainOtnPm15MinOscOptPowerTxHigh": aosDomainOtnPm15MinOscOptPowerTxHigh,
       "aosDomainOtnPm15MinSpanLossTable": aosDomainOtnPm15MinSpanLossTable,
       "aosDomainOtnPm15MinSpanLossEntry": aosDomainOtnPm15MinSpanLossEntry,
       "aosDomainOtnPm15MinSpanLossSample": aosDomainOtnPm15MinSpanLossSample,
       "aosDomainOtnPm15MinSpanLossSampleTime": aosDomainOtnPm15MinSpanLossSampleTime,
       "aosDomainOtnPm15MinSpanLossRxLow": aosDomainOtnPm15MinSpanLossRxLow,
       "aosDomainOtnPm15MinSpanLossRxMean": aosDomainOtnPm15MinSpanLossRxMean,
       "aosDomainOtnPm15MinSpanLossRxHigh": aosDomainOtnPm15MinSpanLossRxHigh,
       "aosDomainOtnPm15MinSpanLossTxLow": aosDomainOtnPm15MinSpanLossTxLow,
       "aosDomainOtnPm15MinSpanLossTxMean": aosDomainOtnPm15MinSpanLossTxMean,
       "aosDomainOtnPm15MinSpanLossTxHigh": aosDomainOtnPm15MinSpanLossTxHigh,
       "aosDomainOtnPm15MinDefectTable": aosDomainOtnPm15MinDefectTable,
       "aosDomainOtnPm15MinDefectEntry": aosDomainOtnPm15MinDefectEntry,
       "aosDomainOtnPm15MinDefectSample": aosDomainOtnPm15MinDefectSample,
       "aosDomainOtnPm15MinDefectSampleTime": aosDomainOtnPm15MinDefectSampleTime,
       "aosDomainOtnPm15MinDefectSes": aosDomainOtnPm15MinDefectSes,
       "aosDomainOtnPm15MinDefectSesInPayload": aosDomainOtnPm15MinDefectSesInPayload,
       "aosDomainOtnPm15MinDefectSesInOverhead": aosDomainOtnPm15MinDefectSesInOverhead,
       "aosDomainOtnPm15MinDefectUas": aosDomainOtnPm15MinDefectUas,
       "aosDomainOtnPm15MinDefectUasInPayload": aosDomainOtnPm15MinDefectUasInPayload,
       "aosDomainOtnPm15MinDefectUasInOverhead": aosDomainOtnPm15MinDefectUasInOverhead,
       "aosDomainOtnPm15MinDefectBbe": aosDomainOtnPm15MinDefectBbe,
       "aosDomainOtnPm15MinDefectEs": aosDomainOtnPm15MinDefectEs,
       "aosDomainOtnPm15MinQualityTable": aosDomainOtnPm15MinQualityTable,
       "aosDomainOtnPm15MinQualityEntry": aosDomainOtnPm15MinQualityEntry,
       "aosDomainOtnPm15MinQualitySample": aosDomainOtnPm15MinQualitySample,
       "aosDomainOtnPm15MinQualitySampleTime": aosDomainOtnPm15MinQualitySampleTime,
       "aosDomainOtnPm15MinQualityCdcLow": aosDomainOtnPm15MinQualityCdcLow,
       "aosDomainOtnPm15MinQualityCdcMean": aosDomainOtnPm15MinQualityCdcMean,
       "aosDomainOtnPm15MinQualityCdcHigh": aosDomainOtnPm15MinQualityCdcHigh,
       "aosDomainOtnPm15MinQualityCfoLow": aosDomainOtnPm15MinQualityCfoLow,
       "aosDomainOtnPm15MinQualityCfoMean": aosDomainOtnPm15MinQualityCfoMean,
       "aosDomainOtnPm15MinQualityCfoHigh": aosDomainOtnPm15MinQualityCfoHigh,
       "aosDomainOtnPm15MinQualitySnrLow": aosDomainOtnPm15MinQualitySnrLow,
       "aosDomainOtnPm15MinQualitySnrMean": aosDomainOtnPm15MinQualitySnrMean,
       "aosDomainOtnPm15MinQualitySnrHigh": aosDomainOtnPm15MinQualitySnrHigh,
       "aosDomainOtnPm15MinQualityDgdLow": aosDomainOtnPm15MinQualityDgdLow,
       "aosDomainOtnPm15MinQualityDgdMean": aosDomainOtnPm15MinQualityDgdMean,
       "aosDomainOtnPm15MinQualityDgdHigh": aosDomainOtnPm15MinQualityDgdHigh,
       "aosDomainOtnPm15MinQualityQFactorLow": aosDomainOtnPm15MinQualityQFactorLow,
       "aosDomainOtnPm15MinQualityQFactorMean": aosDomainOtnPm15MinQualityQFactorMean,
       "aosDomainOtnPm15MinQualityQFactorHigh": aosDomainOtnPm15MinQualityQFactorHigh,
       "aosDomainOtnPm15MinQualityEnhancedTable": aosDomainOtnPm15MinQualityEnhancedTable,
       "aosDomainOtnPm15MinQualityEnhancedEntry": aosDomainOtnPm15MinQualityEnhancedEntry,
       "aosDomainOtnPm15MinQualityEnhancedSample": aosDomainOtnPm15MinQualityEnhancedSample,
       "aosDomainOtnPm15MinQualityEnhancedSampleTime": aosDomainOtnPm15MinQualityEnhancedSampleTime,
       "aosDomainOtnPm15MinQualityEnhancedSoptLow": aosDomainOtnPm15MinQualityEnhancedSoptLow,
       "aosDomainOtnPm15MinQualityEnhancedSoptMean": aosDomainOtnPm15MinQualityEnhancedSoptMean,
       "aosDomainOtnPm15MinQualityEnhancedSoptHigh": aosDomainOtnPm15MinQualityEnhancedSoptHigh,
       "aosDomainOtnPm15MinQualityEnhancedOsnrLow": aosDomainOtnPm15MinQualityEnhancedOsnrLow,
       "aosDomainOtnPm15MinQualityEnhancedOsnrMean": aosDomainOtnPm15MinQualityEnhancedOsnrMean,
       "aosDomainOtnPm15MinQualityEnhancedOsnrHigh": aosDomainOtnPm15MinQualityEnhancedOsnrHigh,
       "aosDomainOtnPm15MinQualityEnhancedPdlLow": aosDomainOtnPm15MinQualityEnhancedPdlLow,
       "aosDomainOtnPm15MinQualityEnhancedPdlMean": aosDomainOtnPm15MinQualityEnhancedPdlMean,
       "aosDomainOtnPm15MinQualityEnhancedPdlHigh": aosDomainOtnPm15MinQualityEnhancedPdlHigh,
       "aosDomainOtnPm1DayOscOptPowerTable": aosDomainOtnPm1DayOscOptPowerTable,
       "aosDomainOtnPm1DayOscOptPowerEntry": aosDomainOtnPm1DayOscOptPowerEntry,
       "aosDomainOtnPm1DayOscOptPowerSample": aosDomainOtnPm1DayOscOptPowerSample,
       "aosDomainOtnPm1DayOscOptPowerSampleTime": aosDomainOtnPm1DayOscOptPowerSampleTime,
       "aosDomainOtnPm1DayOscOptPowerRxLow": aosDomainOtnPm1DayOscOptPowerRxLow,
       "aosDomainOtnPm1DayOscOptPowerRxMean": aosDomainOtnPm1DayOscOptPowerRxMean,
       "aosDomainOtnPm1DayOscOptPowerRxHigh": aosDomainOtnPm1DayOscOptPowerRxHigh,
       "aosDomainOtnPm1DayOscOptPowerTxLow": aosDomainOtnPm1DayOscOptPowerTxLow,
       "aosDomainOtnPm1DayOscOptPowerTxMean": aosDomainOtnPm1DayOscOptPowerTxMean,
       "aosDomainOtnPm1DayOscOptPowerTxHigh": aosDomainOtnPm1DayOscOptPowerTxHigh,
       "aosDomainOtnPm1DaySpanLossTable": aosDomainOtnPm1DaySpanLossTable,
       "aosDomainOtnPm1DaySpanLossEntry": aosDomainOtnPm1DaySpanLossEntry,
       "aosDomainOtnPm1DaySpanLossSample": aosDomainOtnPm1DaySpanLossSample,
       "aosDomainOtnPm1DaySpanLossSampleTime": aosDomainOtnPm1DaySpanLossSampleTime,
       "aosDomainOtnPm1DaySpanLossRxLow": aosDomainOtnPm1DaySpanLossRxLow,
       "aosDomainOtnPm1DaySpanLossRxMean": aosDomainOtnPm1DaySpanLossRxMean,
       "aosDomainOtnPm1DaySpanLossRxHigh": aosDomainOtnPm1DaySpanLossRxHigh,
       "aosDomainOtnPm1DaySpanLossTxLow": aosDomainOtnPm1DaySpanLossTxLow,
       "aosDomainOtnPm1DaySpanLossTxMean": aosDomainOtnPm1DaySpanLossTxMean,
       "aosDomainOtnPm1DaySpanLossTxHigh": aosDomainOtnPm1DaySpanLossTxHigh,
       "aosDomainOtnPm1DayDefectTable": aosDomainOtnPm1DayDefectTable,
       "aosDomainOtnPm1DayDefectEntry": aosDomainOtnPm1DayDefectEntry,
       "aosDomainOtnPm1DayDefectSample": aosDomainOtnPm1DayDefectSample,
       "aosDomainOtnPm1DayDefectSampleTime": aosDomainOtnPm1DayDefectSampleTime,
       "aosDomainOtnPm1DayDefectSes": aosDomainOtnPm1DayDefectSes,
       "aosDomainOtnPm1DayDefectSesInPayload": aosDomainOtnPm1DayDefectSesInPayload,
       "aosDomainOtnPm1DayDefectSesInOverhead": aosDomainOtnPm1DayDefectSesInOverhead,
       "aosDomainOtnPm1DayDefectUas": aosDomainOtnPm1DayDefectUas,
       "aosDomainOtnPm1DayDefectUasInPayload": aosDomainOtnPm1DayDefectUasInPayload,
       "aosDomainOtnPm1DayDefectUasInOverhead": aosDomainOtnPm1DayDefectUasInOverhead,
       "aosDomainOtnPm1DayDefectBbe": aosDomainOtnPm1DayDefectBbe,
       "aosDomainOtnPm1DayDefectEs": aosDomainOtnPm1DayDefectEs,
       "aosDomainOtnPm1DayQualityTable": aosDomainOtnPm1DayQualityTable,
       "aosDomainOtnPm1DayQualityEntry": aosDomainOtnPm1DayQualityEntry,
       "aosDomainOtnPm1DayQualitySample": aosDomainOtnPm1DayQualitySample,
       "aosDomainOtnPm1DayQualitySampleTime": aosDomainOtnPm1DayQualitySampleTime,
       "aosDomainOtnPm1DayQualityCdcLow": aosDomainOtnPm1DayQualityCdcLow,
       "aosDomainOtnPm1DayQualityCdcMean": aosDomainOtnPm1DayQualityCdcMean,
       "aosDomainOtnPm1DayQualityCdcHigh": aosDomainOtnPm1DayQualityCdcHigh,
       "aosDomainOtnPm1DayQualityCfoLow": aosDomainOtnPm1DayQualityCfoLow,
       "aosDomainOtnPm1DayQualityCfoMean": aosDomainOtnPm1DayQualityCfoMean,
       "aosDomainOtnPm1DayQualityCfoHigh": aosDomainOtnPm1DayQualityCfoHigh,
       "aosDomainOtnPm1DayQualitySnrLow": aosDomainOtnPm1DayQualitySnrLow,
       "aosDomainOtnPm1DayQualitySnrMean": aosDomainOtnPm1DayQualitySnrMean,
       "aosDomainOtnPm1DayQualitySnrHigh": aosDomainOtnPm1DayQualitySnrHigh,
       "aosDomainOtnPm1DayQualityDgdLow": aosDomainOtnPm1DayQualityDgdLow,
       "aosDomainOtnPm1DayQualityDgdMean": aosDomainOtnPm1DayQualityDgdMean,
       "aosDomainOtnPm1DayQualityDgdHigh": aosDomainOtnPm1DayQualityDgdHigh,
       "aosDomainOtnPm1DayQualityQFactorLow": aosDomainOtnPm1DayQualityQFactorLow,
       "aosDomainOtnPm1DayQualityQFactorMean": aosDomainOtnPm1DayQualityQFactorMean,
       "aosDomainOtnPm1DayQualityQFactorHigh": aosDomainOtnPm1DayQualityQFactorHigh,
       "aosDomainOtnPm1DayQualityEnhancedTable": aosDomainOtnPm1DayQualityEnhancedTable,
       "aosDomainOtnPm1DayQualityEnhancedEntry": aosDomainOtnPm1DayQualityEnhancedEntry,
       "aosDomainOtnPm1DayQualityEnhancedSample": aosDomainOtnPm1DayQualityEnhancedSample,
       "aosDomainOtnPm1DayQualityEnhancedSampleTime": aosDomainOtnPm1DayQualityEnhancedSampleTime,
       "aosDomainOtnPm1DayQualityEnhancedSoptLow": aosDomainOtnPm1DayQualityEnhancedSoptLow,
       "aosDomainOtnPm1DayQualityEnhancedSoptMean": aosDomainOtnPm1DayQualityEnhancedSoptMean,
       "aosDomainOtnPm1DayQualityEnhancedSoptHigh": aosDomainOtnPm1DayQualityEnhancedSoptHigh,
       "aosDomainOtnPm1DayQualityEnhancedOsnrLow": aosDomainOtnPm1DayQualityEnhancedOsnrLow,
       "aosDomainOtnPm1DayQualityEnhancedOsnrMean": aosDomainOtnPm1DayQualityEnhancedOsnrMean,
       "aosDomainOtnPm1DayQualityEnhancedOsnrHigh": aosDomainOtnPm1DayQualityEnhancedOsnrHigh,
       "aosDomainOtnPm1DayQualityEnhancedPdlLow": aosDomainOtnPm1DayQualityEnhancedPdlLow,
       "aosDomainOtnPm1DayQualityEnhancedPdlMean": aosDomainOtnPm1DayQualityEnhancedPdlMean,
       "aosDomainOtnPm1DayQualityEnhancedPdlHigh": aosDomainOtnPm1DayQualityEnhancedPdlHigh,
       "aosDomainOtnPmConformance": aosDomainOtnPmConformance,
       "aosDomainOtnPmCompliances": aosDomainOtnPmCompliances,
       "aosDomainOtnPmCompliance": aosDomainOtnPmCompliance,
       "aosDomainOtnPmGroups": aosDomainOtnPmGroups,
       "aosDomainOtnPmStatsObjectGroup": aosDomainOtnPmStatsObjectGroup}
)
