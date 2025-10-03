# SNMP MIB module (WIS-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\wis\WIS-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:15 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(wisBridgeGroups,
 wisMIB) = mibBuilder.importSymbols(
    "WIS-MIB",
    "wisBridgeGroups",
    "wisMIB")


# MODULE-IDENTITY

wisBridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4)
)
if mibBuilder.loadTexts:
    wisBridge.setRevisions(
        ("2017-10-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WisRadioTable_Object = MibTable
wisRadioTable = _WisRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wisRadioTable.setStatus("current")
_WisRadioEntry_Object = MibTableRow
wisRadioEntry = _WisRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1)
)
wisRadioEntry.setIndexNames(
    (0, "WIS-BRIDGE-MIB", "wisRadioIndex"),
)
if mibBuilder.loadTexts:
    wisRadioEntry.setStatus("current")


class _WisRadioIndex_Type(Integer32):
    """Custom type wisRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WisRadioIndex_Type.__name__ = "Integer32"
_WisRadioIndex_Object = MibTableColumn
wisRadioIndex = _WisRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 1),
    _WisRadioIndex_Type()
)
wisRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wisRadioIndex.setStatus("current")


class _WisRadioMode_Type(Integer32):
    """Custom type wisRadioMode based on Integer32"""
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
        *(("sta", 1),
          ("ap", 2),
          ("aprepeater", 3),
          ("apwds", 4))
    )


_WisRadioMode_Type.__name__ = "Integer32"
_WisRadioMode_Object = MibTableColumn
wisRadioMode = _WisRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 2),
    _WisRadioMode_Type()
)
wisRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioMode.setStatus("current")
_WisRadioCCode_Type = Integer32
_WisRadioCCode_Object = MibTableColumn
wisRadioCCode = _WisRadioCCode_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 3),
    _WisRadioCCode_Type()
)
wisRadioCCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioCCode.setStatus("current")


class _WisRadioFreq_Type(Integer32):
    """Custom type wisRadioFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WisRadioFreq_Type.__name__ = "Integer32"
_WisRadioFreq_Object = MibTableColumn
wisRadioFreq = _WisRadioFreq_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 4),
    _WisRadioFreq_Type()
)
wisRadioFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioFreq.setStatus("current")
_WisRadioDfsEnabled_Type = TruthValue
_WisRadioDfsEnabled_Object = MibTableColumn
wisRadioDfsEnabled = _WisRadioDfsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 5),
    _WisRadioDfsEnabled_Type()
)
wisRadioDfsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioDfsEnabled.setStatus("current")


class _WisRadioTxPower_Type(Integer32):
    """Custom type wisRadioTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WisRadioTxPower_Type.__name__ = "Integer32"
_WisRadioTxPower_Object = MibTableColumn
wisRadioTxPower = _WisRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 6),
    _WisRadioTxPower_Type()
)
wisRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioTxPower.setStatus("current")


class _WisRadioDistance_Type(Integer32):
    """Custom type wisRadioDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WisRadioDistance_Type.__name__ = "Integer32"
_WisRadioDistance_Object = MibTableColumn
wisRadioDistance = _WisRadioDistance_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 7),
    _WisRadioDistance_Type()
)
wisRadioDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioDistance.setStatus("current")


class _WisRadioChainmask_Type(Integer32):
    """Custom type wisRadioChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WisRadioChainmask_Type.__name__ = "Integer32"
_WisRadioChainmask_Object = MibTableColumn
wisRadioChainmask = _WisRadioChainmask_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 8),
    _WisRadioChainmask_Type()
)
wisRadioChainmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioChainmask.setStatus("current")
_WisRadioAntenna_Type = DisplayString
_WisRadioAntenna_Object = MibTableColumn
wisRadioAntenna = _WisRadioAntenna_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 1, 1, 9),
    _WisRadioAntenna_Type()
)
wisRadioAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioAntenna.setStatus("current")
_WisRadioRssiTable_Object = MibTable
wisRadioRssiTable = _WisRadioRssiTable_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wisRadioRssiTable.setStatus("current")
_WisRadioRssiEntry_Object = MibTableRow
wisRadioRssiEntry = _WisRadioRssiEntry_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 2, 1)
)
wisRadioRssiEntry.setIndexNames(
    (0, "WIS-BRIDGE-MIB", "wisRadioIndex"),
    (0, "WIS-BRIDGE-MIB", "wisRadioRssiIndex"),
)
if mibBuilder.loadTexts:
    wisRadioRssiEntry.setStatus("current")


class _WisRadioRssiIndex_Type(Integer32):
    """Custom type wisRadioRssiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WisRadioRssiIndex_Type.__name__ = "Integer32"
_WisRadioRssiIndex_Object = MibTableColumn
wisRadioRssiIndex = _WisRadioRssiIndex_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 2, 1, 1),
    _WisRadioRssiIndex_Type()
)
wisRadioRssiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wisRadioRssiIndex.setStatus("current")
_WisRadioRssi_Type = Integer32
_WisRadioRssi_Object = MibTableColumn
wisRadioRssi = _WisRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 2, 1, 2),
    _WisRadioRssi_Type()
)
wisRadioRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioRssi.setStatus("current")
_WisRadioRssiMgmt_Type = Integer32
_WisRadioRssiMgmt_Object = MibTableColumn
wisRadioRssiMgmt = _WisRadioRssiMgmt_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 2, 1, 3),
    _WisRadioRssiMgmt_Type()
)
wisRadioRssiMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioRssiMgmt.setStatus("current")
_WisRadioRssiExt_Type = Integer32
_WisRadioRssiExt_Object = MibTableColumn
wisRadioRssiExt = _WisRadioRssiExt_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 2, 1, 4),
    _WisRadioRssiExt_Type()
)
wisRadioRssiExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisRadioRssiExt.setStatus("current")
_WisWlStatTable_Object = MibTable
wisWlStatTable = _WisWlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3)
)
if mibBuilder.loadTexts:
    wisWlStatTable.setStatus("current")
_WisWlStatEntry_Object = MibTableRow
wisWlStatEntry = _WisWlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1)
)
wisWlStatEntry.setIndexNames(
    (0, "WIS-BRIDGE-MIB", "wisWlStatIndex"),
)
if mibBuilder.loadTexts:
    wisWlStatEntry.setStatus("current")


class _WisWlStatIndex_Type(Integer32):
    """Custom type wisWlStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WisWlStatIndex_Type.__name__ = "Integer32"
_WisWlStatIndex_Object = MibTableColumn
wisWlStatIndex = _WisWlStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 1),
    _WisWlStatIndex_Type()
)
wisWlStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wisWlStatIndex.setStatus("current")
_WisWlStatSsid_Type = DisplayString
_WisWlStatSsid_Object = MibTableColumn
wisWlStatSsid = _WisWlStatSsid_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 2),
    _WisWlStatSsid_Type()
)
wisWlStatSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatSsid.setStatus("current")
_WisWlStatHideSsid_Type = TruthValue
_WisWlStatHideSsid_Object = MibTableColumn
wisWlStatHideSsid = _WisWlStatHideSsid_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 3),
    _WisWlStatHideSsid_Type()
)
wisWlStatHideSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatHideSsid.setStatus("current")
_WisWlStatApMac_Type = MacAddress
_WisWlStatApMac_Object = MibTableColumn
wisWlStatApMac = _WisWlStatApMac_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 4),
    _WisWlStatApMac_Type()
)
wisWlStatApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatApMac.setStatus("current")
_WisWlStatSignal_Type = Integer32
_WisWlStatSignal_Object = MibTableColumn
wisWlStatSignal = _WisWlStatSignal_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 5),
    _WisWlStatSignal_Type()
)
wisWlStatSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatSignal.setStatus("current")
_WisWlStatRssi_Type = Integer32
_WisWlStatRssi_Object = MibTableColumn
wisWlStatRssi = _WisWlStatRssi_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 6),
    _WisWlStatRssi_Type()
)
wisWlStatRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatRssi.setStatus("current")
_WisWlStatCcq_Type = Integer32
_WisWlStatCcq_Object = MibTableColumn
wisWlStatCcq = _WisWlStatCcq_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 7),
    _WisWlStatCcq_Type()
)
wisWlStatCcq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatCcq.setStatus("current")
_WisWlStatNoiseFloor_Type = Integer32
_WisWlStatNoiseFloor_Object = MibTableColumn
wisWlStatNoiseFloor = _WisWlStatNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 8),
    _WisWlStatNoiseFloor_Type()
)
wisWlStatNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatNoiseFloor.setStatus("current")
_WisWlStatTxRate_Type = Integer32
_WisWlStatTxRate_Object = MibTableColumn
wisWlStatTxRate = _WisWlStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 9),
    _WisWlStatTxRate_Type()
)
wisWlStatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatTxRate.setStatus("current")
_WisWlStatRxRate_Type = Integer32
_WisWlStatRxRate_Object = MibTableColumn
wisWlStatRxRate = _WisWlStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 10),
    _WisWlStatRxRate_Type()
)
wisWlStatRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatRxRate.setStatus("current")
_WisWlStatSecurity_Type = DisplayString
_WisWlStatSecurity_Object = MibTableColumn
wisWlStatSecurity = _WisWlStatSecurity_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 11),
    _WisWlStatSecurity_Type()
)
wisWlStatSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatSecurity.setStatus("current")
_WisWlStatWdsEnabled_Type = TruthValue
_WisWlStatWdsEnabled_Object = MibTableColumn
wisWlStatWdsEnabled = _WisWlStatWdsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 12),
    _WisWlStatWdsEnabled_Type()
)
wisWlStatWdsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatWdsEnabled.setStatus("current")
_WisWlStatApRepeater_Type = TruthValue
_WisWlStatApRepeater_Object = MibTableColumn
wisWlStatApRepeater = _WisWlStatApRepeater_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 13),
    _WisWlStatApRepeater_Type()
)
wisWlStatApRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatApRepeater.setStatus("current")
_WisWlStatChanWidth_Type = Integer32
_WisWlStatChanWidth_Object = MibTableColumn
wisWlStatChanWidth = _WisWlStatChanWidth_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 14),
    _WisWlStatChanWidth_Type()
)
wisWlStatChanWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatChanWidth.setStatus("current")
_WisWlStatStaCount_Type = Gauge32
_WisWlStatStaCount_Object = MibTableColumn
wisWlStatStaCount = _WisWlStatStaCount_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 3, 1, 15),
    _WisWlStatStaCount_Type()
)
wisWlStatStaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisWlStatStaCount.setStatus("current")
_WisStaTable_Object = MibTable
wisStaTable = _WisStaTable_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4)
)
if mibBuilder.loadTexts:
    wisStaTable.setStatus("current")
_WisStaEntry_Object = MibTableRow
wisStaEntry = _WisStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1)
)
wisStaEntry.setIndexNames(
    (0, "WIS-BRIDGE-MIB", "wisWlStatIndex"),
    (0, "WIS-BRIDGE-MIB", "wisStaMac"),
)
if mibBuilder.loadTexts:
    wisStaEntry.setStatus("current")
_WisStaMac_Type = MacAddress
_WisStaMac_Object = MibTableColumn
wisStaMac = _WisStaMac_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 1),
    _WisStaMac_Type()
)
wisStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wisStaMac.setStatus("current")
_WisStaName_Type = DisplayString
_WisStaName_Object = MibTableColumn
wisStaName = _WisStaName_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 2),
    _WisStaName_Type()
)
wisStaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaName.setStatus("current")
_WisStaSignal_Type = Integer32
_WisStaSignal_Object = MibTableColumn
wisStaSignal = _WisStaSignal_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 3),
    _WisStaSignal_Type()
)
wisStaSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaSignal.setStatus("current")
_WisStaNoiseFloor_Type = Integer32
_WisStaNoiseFloor_Object = MibTableColumn
wisStaNoiseFloor = _WisStaNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 4),
    _WisStaNoiseFloor_Type()
)
wisStaNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaNoiseFloor.setStatus("current")


class _WisStaDistance_Type(Integer32):
    """Custom type wisStaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WisStaDistance_Type.__name__ = "Integer32"
_WisStaDistance_Object = MibTableColumn
wisStaDistance = _WisStaDistance_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 5),
    _WisStaDistance_Type()
)
wisStaDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaDistance.setStatus("current")
_WisStaCcq_Type = Integer32
_WisStaCcq_Object = MibTableColumn
wisStaCcq = _WisStaCcq_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 6),
    _WisStaCcq_Type()
)
wisStaCcq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaCcq.setStatus("current")
_WisStaAmp_Type = Integer32
_WisStaAmp_Object = MibTableColumn
wisStaAmp = _WisStaAmp_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 7),
    _WisStaAmp_Type()
)
wisStaAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaAmp.setStatus("current")
_WisStaAmq_Type = Integer32
_WisStaAmq_Object = MibTableColumn
wisStaAmq = _WisStaAmq_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 8),
    _WisStaAmq_Type()
)
wisStaAmq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaAmq.setStatus("current")
_WisStaAmc_Type = Integer32
_WisStaAmc_Object = MibTableColumn
wisStaAmc = _WisStaAmc_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 9),
    _WisStaAmc_Type()
)
wisStaAmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaAmc.setStatus("current")
_WisStaLastIp_Type = IpAddress
_WisStaLastIp_Object = MibTableColumn
wisStaLastIp = _WisStaLastIp_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 10),
    _WisStaLastIp_Type()
)
wisStaLastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaLastIp.setStatus("current")
_WisStaTxRate_Type = Integer32
_WisStaTxRate_Object = MibTableColumn
wisStaTxRate = _WisStaTxRate_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 11),
    _WisStaTxRate_Type()
)
wisStaTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaTxRate.setStatus("current")
_WisStaRxRate_Type = Integer32
_WisStaRxRate_Object = MibTableColumn
wisStaRxRate = _WisStaRxRate_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 12),
    _WisStaRxRate_Type()
)
wisStaRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaRxRate.setStatus("current")
_WisStaTxBytes_Type = Counter64
_WisStaTxBytes_Object = MibTableColumn
wisStaTxBytes = _WisStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 13),
    _WisStaTxBytes_Type()
)
wisStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaTxBytes.setStatus("current")
_WisStaRxBytes_Type = Counter64
_WisStaRxBytes_Object = MibTableColumn
wisStaRxBytes = _WisStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 14),
    _WisStaRxBytes_Type()
)
wisStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaRxBytes.setStatus("current")
_WisStaConnTime_Type = TimeTicks
_WisStaConnTime_Object = MibTableColumn
wisStaConnTime = _WisStaConnTime_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 15),
    _WisStaConnTime_Type()
)
wisStaConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaConnTime.setStatus("current")
_WisStaLocalCINR_Type = Integer32
_WisStaLocalCINR_Object = MibTableColumn
wisStaLocalCINR = _WisStaLocalCINR_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 16),
    _WisStaLocalCINR_Type()
)
wisStaLocalCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaLocalCINR.setStatus("current")
_WisStaTxCapacity_Type = Integer32
_WisStaTxCapacity_Object = MibTableColumn
wisStaTxCapacity = _WisStaTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 17),
    _WisStaTxCapacity_Type()
)
wisStaTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaTxCapacity.setStatus("current")
_WisStaRxCapacity_Type = Integer32
_WisStaRxCapacity_Object = MibTableColumn
wisStaRxCapacity = _WisStaRxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 18),
    _WisStaRxCapacity_Type()
)
wisStaRxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaRxCapacity.setStatus("current")
_WisStaTxAirtime_Type = Integer32
_WisStaTxAirtime_Object = MibTableColumn
wisStaTxAirtime = _WisStaTxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 19),
    _WisStaTxAirtime_Type()
)
wisStaTxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaTxAirtime.setStatus("current")
_WisStaRxAirtime_Type = Integer32
_WisStaRxAirtime_Object = MibTableColumn
wisStaRxAirtime = _WisStaRxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 20),
    _WisStaRxAirtime_Type()
)
wisStaRxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaRxAirtime.setStatus("current")
_WisStaTxLatency_Type = Integer32
_WisStaTxLatency_Object = MibTableColumn
wisStaTxLatency = _WisStaTxLatency_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 4, 1, 21),
    _WisStaTxLatency_Type()
)
wisStaTxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisStaTxLatency.setStatus("current")
_WisHostInfo_ObjectIdentity = ObjectIdentity
wisHostInfo = _WisHostInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 5)
)
_WisHostProductName_Type = DisplayString
_WisHostProductName_Object = MibScalar
wisHostProductName = _WisHostProductName_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 5, 1),
    _WisHostProductName_Type()
)
wisHostProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisHostProductName.setStatus("current")
_WisHostWirelessInfo_Type = DisplayString
_WisHostWirelessInfo_Object = MibScalar
wisHostWirelessInfo = _WisHostWirelessInfo_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 5, 2),
    _WisHostWirelessInfo_Type()
)
wisHostWirelessInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisHostWirelessInfo.setStatus("current")


class _WisHostCpuLoad_Type(Integer32):
    """Custom type wisHostCpuLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WisHostCpuLoad_Type.__name__ = "Integer32"
_WisHostCpuLoad_Object = MibScalar
wisHostCpuLoad = _WisHostCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 5, 3),
    _WisHostCpuLoad_Type()
)
wisHostCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisHostCpuLoad.setStatus("current")


class _WisHostTemperature_Type(Integer32):
    """Custom type wisHostTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WisHostTemperature_Type.__name__ = "Integer32"
_WisHostTemperature_Object = MibScalar
wisHostTemperature = _WisHostTemperature_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 5, 4),
    _WisHostTemperature_Type()
)
wisHostTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisHostTemperature.setStatus("current")
_WisHostLocaltime_Type = DisplayString
_WisHostLocaltime_Object = MibScalar
wisHostLocaltime = _WisHostLocaltime_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 5, 5),
    _WisHostLocaltime_Type()
)
wisHostLocaltime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisHostLocaltime.setStatus("current")


class _WisHostNetrole_Type(Integer32):
    """Custom type wisHostNetrole based on Integer32"""
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
        *(("unknown", 0),
          ("bridge", 1),
          ("router", 2),
          ("soho", 3))
    )


_WisHostNetrole_Type.__name__ = "Integer32"
_WisHostNetrole_Object = MibScalar
wisHostNetrole = _WisHostNetrole_Object(
    (1, 3, 6, 1, 4, 1, 62821, 1, 4, 5, 6),
    _WisHostNetrole_Type()
)
wisHostNetrole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wisHostNetrole.setStatus("current")

# Managed Objects groups

wisBridgeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 62821, 1, 2, 2, 1)
)
wisBridgeStatusGroup.setObjects(
      *(("WIS-BRIDGE-MIB", "wisStaName"),
        ("WIS-BRIDGE-MIB", "wisStaSignal"),
        ("WIS-BRIDGE-MIB", "wisStaNoiseFloor"),
        ("WIS-BRIDGE-MIB", "wisStaDistance"),
        ("WIS-BRIDGE-MIB", "wisStaCcq"),
        ("WIS-BRIDGE-MIB", "wisStaAmp"),
        ("WIS-BRIDGE-MIB", "wisStaAmq"),
        ("WIS-BRIDGE-MIB", "wisStaAmc"),
        ("WIS-BRIDGE-MIB", "wisStaLastIp"),
        ("WIS-BRIDGE-MIB", "wisStaTxRate"),
        ("WIS-BRIDGE-MIB", "wisStaRxRate"),
        ("WIS-BRIDGE-MIB", "wisStaTxBytes"),
        ("WIS-BRIDGE-MIB", "wisStaRxBytes"),
        ("WIS-BRIDGE-MIB", "wisStaConnTime"),
        ("WIS-BRIDGE-MIB", "wisStaLocalCINR"),
        ("WIS-BRIDGE-MIB", "wisStaTxCapacity"),
        ("WIS-BRIDGE-MIB", "wisStaRxCapacity"),
        ("WIS-BRIDGE-MIB", "wisStaTxAirtime"),
        ("WIS-BRIDGE-MIB", "wisStaRxAirtime"),
        ("WIS-BRIDGE-MIB", "wisStaTxLatency"),
        ("WIS-BRIDGE-MIB", "wisRadioMode"),
        ("WIS-BRIDGE-MIB", "wisRadioCCode"),
        ("WIS-BRIDGE-MIB", "wisRadioFreq"),
        ("WIS-BRIDGE-MIB", "wisRadioDfsEnabled"),
        ("WIS-BRIDGE-MIB", "wisRadioTxPower"),
        ("WIS-BRIDGE-MIB", "wisRadioDistance"),
        ("WIS-BRIDGE-MIB", "wisRadioChainmask"),
        ("WIS-BRIDGE-MIB", "wisRadioAntenna"),
        ("WIS-BRIDGE-MIB", "wisRadioRssi"),
        ("WIS-BRIDGE-MIB", "wisRadioRssiMgmt"),
        ("WIS-BRIDGE-MIB", "wisRadioRssiExt"),
        ("WIS-BRIDGE-MIB", "wisWlStatSsid"),
        ("WIS-BRIDGE-MIB", "wisWlStatHideSsid"),
        ("WIS-BRIDGE-MIB", "wisWlStatApMac"),
        ("WIS-BRIDGE-MIB", "wisWlStatSignal"),
        ("WIS-BRIDGE-MIB", "wisWlStatRssi"),
        ("WIS-BRIDGE-MIB", "wisWlStatCcq"),
        ("WIS-BRIDGE-MIB", "wisWlStatNoiseFloor"),
        ("WIS-BRIDGE-MIB", "wisWlStatTxRate"),
        ("WIS-BRIDGE-MIB", "wisWlStatRxRate"),
        ("WIS-BRIDGE-MIB", "wisWlStatSecurity"),
        ("WIS-BRIDGE-MIB", "wisWlStatWdsEnabled"),
        ("WIS-BRIDGE-MIB", "wisWlStatApRepeater"),
        ("WIS-BRIDGE-MIB", "wisWlStatChanWidth"),
        ("WIS-BRIDGE-MIB", "wisWlStatStaCount"),
        ("WIS-BRIDGE-MIB", "wisHostLocaltime"),
        ("WIS-BRIDGE-MIB", "wisHostWirelessInfo"),
        ("WIS-BRIDGE-MIB", "wisHostProductName"),
        ("WIS-BRIDGE-MIB", "wisHostNetrole"),
        ("WIS-BRIDGE-MIB", "wisHostCpuLoad"),
        ("WIS-BRIDGE-MIB", "wisHostTemperature"))
)
if mibBuilder.loadTexts:
    wisBridgeStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wisBridgeStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 62821, 1, 2, 2, 2)
)
wisBridgeStatusCompliance.setObjects(
    ("WIS-BRIDGE-MIB", "wisBridgeStatusGroup")
)
if mibBuilder.loadTexts:
    wisBridgeStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WIS-BRIDGE-MIB",
    **{"wisBridgeStatusGroup": wisBridgeStatusGroup,
       "wisBridgeStatusCompliance": wisBridgeStatusCompliance,
       "wisBridge": wisBridge,
       "wisRadioTable": wisRadioTable,
       "wisRadioEntry": wisRadioEntry,
       "wisRadioIndex": wisRadioIndex,
       "wisRadioMode": wisRadioMode,
       "wisRadioCCode": wisRadioCCode,
       "wisRadioFreq": wisRadioFreq,
       "wisRadioDfsEnabled": wisRadioDfsEnabled,
       "wisRadioTxPower": wisRadioTxPower,
       "wisRadioDistance": wisRadioDistance,
       "wisRadioChainmask": wisRadioChainmask,
       "wisRadioAntenna": wisRadioAntenna,
       "wisRadioRssiTable": wisRadioRssiTable,
       "wisRadioRssiEntry": wisRadioRssiEntry,
       "wisRadioRssiIndex": wisRadioRssiIndex,
       "wisRadioRssi": wisRadioRssi,
       "wisRadioRssiMgmt": wisRadioRssiMgmt,
       "wisRadioRssiExt": wisRadioRssiExt,
       "wisWlStatTable": wisWlStatTable,
       "wisWlStatEntry": wisWlStatEntry,
       "wisWlStatIndex": wisWlStatIndex,
       "wisWlStatSsid": wisWlStatSsid,
       "wisWlStatHideSsid": wisWlStatHideSsid,
       "wisWlStatApMac": wisWlStatApMac,
       "wisWlStatSignal": wisWlStatSignal,
       "wisWlStatRssi": wisWlStatRssi,
       "wisWlStatCcq": wisWlStatCcq,
       "wisWlStatNoiseFloor": wisWlStatNoiseFloor,
       "wisWlStatTxRate": wisWlStatTxRate,
       "wisWlStatRxRate": wisWlStatRxRate,
       "wisWlStatSecurity": wisWlStatSecurity,
       "wisWlStatWdsEnabled": wisWlStatWdsEnabled,
       "wisWlStatApRepeater": wisWlStatApRepeater,
       "wisWlStatChanWidth": wisWlStatChanWidth,
       "wisWlStatStaCount": wisWlStatStaCount,
       "wisStaTable": wisStaTable,
       "wisStaEntry": wisStaEntry,
       "wisStaMac": wisStaMac,
       "wisStaName": wisStaName,
       "wisStaSignal": wisStaSignal,
       "wisStaNoiseFloor": wisStaNoiseFloor,
       "wisStaDistance": wisStaDistance,
       "wisStaCcq": wisStaCcq,
       "wisStaAmp": wisStaAmp,
       "wisStaAmq": wisStaAmq,
       "wisStaAmc": wisStaAmc,
       "wisStaLastIp": wisStaLastIp,
       "wisStaTxRate": wisStaTxRate,
       "wisStaRxRate": wisStaRxRate,
       "wisStaTxBytes": wisStaTxBytes,
       "wisStaRxBytes": wisStaRxBytes,
       "wisStaConnTime": wisStaConnTime,
       "wisStaLocalCINR": wisStaLocalCINR,
       "wisStaTxCapacity": wisStaTxCapacity,
       "wisStaRxCapacity": wisStaRxCapacity,
       "wisStaTxAirtime": wisStaTxAirtime,
       "wisStaRxAirtime": wisStaRxAirtime,
       "wisStaTxLatency": wisStaTxLatency,
       "wisHostInfo": wisHostInfo,
       "wisHostProductName": wisHostProductName,
       "wisHostWirelessInfo": wisHostWirelessInfo,
       "wisHostCpuLoad": wisHostCpuLoad,
       "wisHostTemperature": wisHostTemperature,
       "wisHostLocaltime": wisHostLocaltime,
       "wisHostNetrole": wisHostNetrole}
)
