# SNMP MIB module (UBNT-AFLTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ubnt\UBNT-AFLTU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:37 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(ubntAFLTU,
 ubntAFLTUGroups) = mibBuilder.importSymbols(
    "UBNT-MIB",
    "ubntAFLTU",
    "ubntAFLTUGroups")


# MODULE-IDENTITY

afLTUMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1)
)
if mibBuilder.loadTexts:
    afLTUMIB.setRevisions(
        ("2018-06-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AfLTUCompliances_ObjectIdentity = ObjectIdentity
afLTUCompliances = _AfLTUCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 9, 1)
)
_AfLTUGroups_ObjectIdentity = ObjectIdentity
afLTUGroups = _AfLTUGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 9, 2)
)
_AfLTUConfig_ObjectIdentity = ObjectIdentity
afLTUConfig = _AfLTUConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2)
)


class _AfLTURole_Type(Integer32):
    """Custom type afLTURole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ap", 0),
          ("cpe", 1))
    )


_AfLTURole_Type.__name__ = "Integer32"
_AfLTURole_Object = MibScalar
afLTURole = _AfLTURole_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 1),
    _AfLTURole_Type()
)
afLTURole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTURole.setStatus("current")
_AfLTUFrequency_Type = Integer32
_AfLTUFrequency_Object = MibScalar
afLTUFrequency = _AfLTUFrequency_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 2),
    _AfLTUFrequency_Type()
)
afLTUFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUFrequency.setStatus("current")
if mibBuilder.loadTexts:
    afLTUFrequency.setUnits("MHz")


class _AfLTUAltFreqList_Type(DisplayString):
    """Custom type afLTUAltFreqList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_AfLTUAltFreqList_Type.__name__ = "DisplayString"
_AfLTUAltFreqList_Object = MibScalar
afLTUAltFreqList = _AfLTUAltFreqList_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 3),
    _AfLTUAltFreqList_Type()
)
afLTUAltFreqList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUAltFreqList.setStatus("current")


class _AfLTUBandwidth_Type(Integer32):
    """Custom type afLTUBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30,
              40,
              50,
              60,
              80,
              100)
        )
    )
    namedValues = NamedValues(
        *(("bw10M", 10),
          ("bw20M", 20),
          ("bw30M", 30),
          ("bw40M", 40),
          ("bw50M", 50),
          ("bw60M", 60),
          ("bw80M", 80),
          ("bw100M", 100))
    )


_AfLTUBandwidth_Type.__name__ = "Integer32"
_AfLTUBandwidth_Object = MibScalar
afLTUBandwidth = _AfLTUBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 4),
    _AfLTUBandwidth_Type()
)
afLTUBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    afLTUBandwidth.setUnits("MHz")


class _AfLTUSsid_Type(DisplayString):
    """Custom type afLTUSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AfLTUSsid_Type.__name__ = "DisplayString"
_AfLTUSsid_Object = MibScalar
afLTUSsid = _AfLTUSsid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 5),
    _AfLTUSsid_Type()
)
afLTUSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUSsid.setStatus("current")


class _AfLTUTxEIRP_Type(Integer32):
    """Custom type afLTUTxEIRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 100),
    )


_AfLTUTxEIRP_Type.__name__ = "Integer32"
_AfLTUTxEIRP_Object = MibScalar
afLTUTxEIRP = _AfLTUTxEIRP_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 6),
    _AfLTUTxEIRP_Type()
)
afLTUTxEIRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUTxEIRP.setStatus("current")


class _AfLTUAntennaGain_Type(Integer32):
    """Custom type afLTUAntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_AfLTUAntennaGain_Type.__name__ = "Integer32"
_AfLTUAntennaGain_Object = MibScalar
afLTUAntennaGain = _AfLTUAntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 7),
    _AfLTUAntennaGain_Type()
)
afLTUAntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUAntennaGain.setStatus("current")


class _AfLTUCableLoss_Type(Integer32):
    """Custom type afLTUCableLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AfLTUCableLoss_Type.__name__ = "Integer32"
_AfLTUCableLoss_Object = MibScalar
afLTUCableLoss = _AfLTUCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 8),
    _AfLTUCableLoss_Type()
)
afLTUCableLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUCableLoss.setStatus("current")
_AfLTUTxRate_Type = Integer32
_AfLTUTxRate_Object = MibScalar
afLTUTxRate = _AfLTUTxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 9),
    _AfLTUTxRate_Type()
)
afLTUTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUTxRate.setStatus("current")
if mibBuilder.loadTexts:
    afLTUTxRate.setUnits("x")


class _AfLTUTxRateAuto_Type(Integer32):
    """Custom type afLTUTxRateAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AfLTUTxRateAuto_Type.__name__ = "Integer32"
_AfLTUTxRateAuto_Object = MibScalar
afLTUTxRateAuto = _AfLTUTxRateAuto_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 10),
    _AfLTUTxRateAuto_Type()
)
afLTUTxRateAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUTxRateAuto.setStatus("current")


class _AfLTUDistanceScale_Type(Integer32):
    """Custom type afLTUDistanceScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AfLTUDistanceScale_Type.__name__ = "Integer32"
_AfLTUDistanceScale_Object = MibScalar
afLTUDistanceScale = _AfLTUDistanceScale_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 2, 11),
    _AfLTUDistanceScale_Type()
)
afLTUDistanceScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUDistanceScale.setStatus("current")
_AfLTUStatus_ObjectIdentity = ObjectIdentity
afLTUStatus = _AfLTUStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 3)
)
_AfLTUMac_Type = MacAddress
_AfLTUMac_Object = MibScalar
afLTUMac = _AfLTUMac_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 3, 1),
    _AfLTUMac_Type()
)
afLTUMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUMac.setStatus("current")
_AfLTUDevModel_Type = DisplayString
_AfLTUDevModel_Object = MibScalar
afLTUDevModel = _AfLTUDevModel_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 3, 2),
    _AfLTUDevModel_Type()
)
afLTUDevModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUDevModel.setStatus("current")
_AfLTUDevName_Type = DisplayString
_AfLTUDevName_Object = MibScalar
afLTUDevName = _AfLTUDevName_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 3, 3),
    _AfLTUDevName_Type()
)
afLTUDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUDevName.setStatus("current")
_AfLTUFirmwareVersion_Type = DisplayString
_AfLTUFirmwareVersion_Object = MibScalar
afLTUFirmwareVersion = _AfLTUFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 3, 4),
    _AfLTUFirmwareVersion_Type()
)
afLTUFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUFirmwareVersion.setStatus("current")
_AfLTUMemoryUsage_Type = Integer32
_AfLTUMemoryUsage_Object = MibScalar
afLTUMemoryUsage = _AfLTUMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 3, 5),
    _AfLTUMemoryUsage_Type()
)
afLTUMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    afLTUMemoryUsage.setUnits("%")
_AfLTUCpuUsage_Type = Integer32
_AfLTUCpuUsage_Object = MibScalar
afLTUCpuUsage = _AfLTUCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 3, 6),
    _AfLTUCpuUsage_Type()
)
afLTUCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    afLTUCpuUsage.setUnits("%")
_AfLTUUptime_Type = Counter64
_AfLTUUptime_Object = MibScalar
afLTUUptime = _AfLTUUptime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 3, 7),
    _AfLTUUptime_Type()
)
afLTUUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUUptime.setStatus("current")
if mibBuilder.loadTexts:
    afLTUUptime.setUnits("s")
_AfLTUStationTable_Object = MibTable
afLTUStationTable = _AfLTUStationTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4)
)
if mibBuilder.loadTexts:
    afLTUStationTable.setStatus("current")
_AfLTUStationEntry_Object = MibTableRow
afLTUStationEntry = _AfLTUStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1)
)
afLTUStationEntry.setIndexNames(
    (0, "UBNT-AFLTU-MIB", "afLTUStaRemoteMac"),
)
if mibBuilder.loadTexts:
    afLTUStationEntry.setStatus("current")
_AfLTUStaTxRate_Type = Integer32
_AfLTUStaTxRate_Object = MibTableColumn
afLTUStaTxRate = _AfLTUStaTxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 1),
    _AfLTUStaTxRate_Type()
)
afLTUStaTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUStaTxRate.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaTxRate.setUnits("x")
_AfLTUStaRxRate_Type = Integer32
_AfLTUStaRxRate_Object = MibTableColumn
afLTUStaRxRate = _AfLTUStaRxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 2),
    _AfLTUStaRxRate_Type()
)
afLTUStaRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    afLTUStaRxRate.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRxRate.setUnits("x")
_AfLTUStaTxCapacity_Type = Integer32
_AfLTUStaTxCapacity_Object = MibTableColumn
afLTUStaTxCapacity = _AfLTUStaTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 3),
    _AfLTUStaTxCapacity_Type()
)
afLTUStaTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaTxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaTxCapacity.setUnits("Kbps")
_AfLTUStaRxCapacity_Type = Integer32
_AfLTUStaRxCapacity_Object = MibTableColumn
afLTUStaRxCapacity = _AfLTUStaRxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 4),
    _AfLTUStaRxCapacity_Type()
)
afLTUStaRxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRxCapacity.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRxCapacity.setUnits("Kbps")
_AfLTUStaRxPower0_Type = Integer32
_AfLTUStaRxPower0_Object = MibTableColumn
afLTUStaRxPower0 = _AfLTUStaRxPower0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 5),
    _AfLTUStaRxPower0_Type()
)
afLTUStaRxPower0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRxPower0.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRxPower0.setUnits("dBm")
_AfLTUStaRxPower1_Type = Integer32
_AfLTUStaRxPower1_Object = MibTableColumn
afLTUStaRxPower1 = _AfLTUStaRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 6),
    _AfLTUStaRxPower1_Type()
)
afLTUStaRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRxPower1.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRxPower1.setUnits("dBm")
_AfLTUStaIdealRxPower0_Type = Integer32
_AfLTUStaIdealRxPower0_Object = MibTableColumn
afLTUStaIdealRxPower0 = _AfLTUStaIdealRxPower0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 7),
    _AfLTUStaIdealRxPower0_Type()
)
afLTUStaIdealRxPower0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaIdealRxPower0.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaIdealRxPower0.setUnits("dBm")
_AfLTUStaIdealRxPower1_Type = Integer32
_AfLTUStaIdealRxPower1_Object = MibTableColumn
afLTUStaIdealRxPower1 = _AfLTUStaIdealRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 8),
    _AfLTUStaIdealRxPower1_Type()
)
afLTUStaIdealRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaIdealRxPower1.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaIdealRxPower1.setUnits("dBm")


class _AfLTUStaRxPowerLevel0_Type(Integer32):
    """Custom type afLTUStaRxPowerLevel0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AfLTUStaRxPowerLevel0_Type.__name__ = "Integer32"
_AfLTUStaRxPowerLevel0_Object = MibTableColumn
afLTUStaRxPowerLevel0 = _AfLTUStaRxPowerLevel0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 9),
    _AfLTUStaRxPowerLevel0_Type()
)
afLTUStaRxPowerLevel0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRxPowerLevel0.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRxPowerLevel0.setUnits("%")


class _AfLTUStaRxPowerLevel1_Type(Integer32):
    """Custom type afLTUStaRxPowerLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AfLTUStaRxPowerLevel1_Type.__name__ = "Integer32"
_AfLTUStaRxPowerLevel1_Object = MibTableColumn
afLTUStaRxPowerLevel1 = _AfLTUStaRxPowerLevel1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 10),
    _AfLTUStaRxPowerLevel1_Type()
)
afLTUStaRxPowerLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRxPowerLevel1.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRxPowerLevel1.setUnits("%")
_AfLTUStaRemoteMac_Type = MacAddress
_AfLTUStaRemoteMac_Object = MibTableColumn
afLTUStaRemoteMac = _AfLTUStaRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 11),
    _AfLTUStaRemoteMac_Type()
)
afLTUStaRemoteMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    afLTUStaRemoteMac.setStatus("current")
_AfLTUStaRemoteDevModel_Type = DisplayString
_AfLTUStaRemoteDevModel_Object = MibTableColumn
afLTUStaRemoteDevModel = _AfLTUStaRemoteDevModel_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 12),
    _AfLTUStaRemoteDevModel_Type()
)
afLTUStaRemoteDevModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteDevModel.setStatus("current")
_AfLTUStaRemoteDevName_Type = DisplayString
_AfLTUStaRemoteDevName_Object = MibTableColumn
afLTUStaRemoteDevName = _AfLTUStaRemoteDevName_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 13),
    _AfLTUStaRemoteDevName_Type()
)
afLTUStaRemoteDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteDevName.setStatus("current")
_AfLTUStaRemoteFirmwareVersion_Type = DisplayString
_AfLTUStaRemoteFirmwareVersion_Object = MibTableColumn
afLTUStaRemoteFirmwareVersion = _AfLTUStaRemoteFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 14),
    _AfLTUStaRemoteFirmwareVersion_Type()
)
afLTUStaRemoteFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteFirmwareVersion.setStatus("current")
_AfLTUStaRemoteTxEIRP_Type = Integer32
_AfLTUStaRemoteTxEIRP_Object = MibTableColumn
afLTUStaRemoteTxEIRP = _AfLTUStaRemoteTxEIRP_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 15),
    _AfLTUStaRemoteTxEIRP_Type()
)
afLTUStaRemoteTxEIRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteTxEIRP.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteTxEIRP.setUnits("dBm")
_AfLTUStaRemoteRxPower0_Type = Integer32
_AfLTUStaRemoteRxPower0_Object = MibTableColumn
afLTUStaRemoteRxPower0 = _AfLTUStaRemoteRxPower0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 16),
    _AfLTUStaRemoteRxPower0_Type()
)
afLTUStaRemoteRxPower0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteRxPower0.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteRxPower0.setUnits("dBm")
_AfLTUStaRemoteRxPower1_Type = Integer32
_AfLTUStaRemoteRxPower1_Object = MibTableColumn
afLTUStaRemoteRxPower1 = _AfLTUStaRemoteRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 17),
    _AfLTUStaRemoteRxPower1_Type()
)
afLTUStaRemoteRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteRxPower1.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteRxPower1.setUnits("dBm")
_AfLTUStaRemoteIdealRxPower0_Type = Integer32
_AfLTUStaRemoteIdealRxPower0_Object = MibTableColumn
afLTUStaRemoteIdealRxPower0 = _AfLTUStaRemoteIdealRxPower0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 18),
    _AfLTUStaRemoteIdealRxPower0_Type()
)
afLTUStaRemoteIdealRxPower0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteIdealRxPower0.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteIdealRxPower0.setUnits("dBm")
_AfLTUStaRemoteIdealRxPower1_Type = Integer32
_AfLTUStaRemoteIdealRxPower1_Object = MibTableColumn
afLTUStaRemoteIdealRxPower1 = _AfLTUStaRemoteIdealRxPower1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 19),
    _AfLTUStaRemoteIdealRxPower1_Type()
)
afLTUStaRemoteIdealRxPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteIdealRxPower1.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteIdealRxPower1.setUnits("dBm")


class _AfLTUStaRemoteRxPowerLevel0_Type(Integer32):
    """Custom type afLTUStaRemoteRxPowerLevel0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AfLTUStaRemoteRxPowerLevel0_Type.__name__ = "Integer32"
_AfLTUStaRemoteRxPowerLevel0_Object = MibTableColumn
afLTUStaRemoteRxPowerLevel0 = _AfLTUStaRemoteRxPowerLevel0_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 20),
    _AfLTUStaRemoteRxPowerLevel0_Type()
)
afLTUStaRemoteRxPowerLevel0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteRxPowerLevel0.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteRxPowerLevel0.setUnits("%")


class _AfLTUStaRemoteRxPowerLevel1_Type(Integer32):
    """Custom type afLTUStaRemoteRxPowerLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AfLTUStaRemoteRxPowerLevel1_Type.__name__ = "Integer32"
_AfLTUStaRemoteRxPowerLevel1_Object = MibTableColumn
afLTUStaRemoteRxPowerLevel1 = _AfLTUStaRemoteRxPowerLevel1_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 21),
    _AfLTUStaRemoteRxPowerLevel1_Type()
)
afLTUStaRemoteRxPowerLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteRxPowerLevel1.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteRxPowerLevel1.setUnits("%")
_AfLTUStaRemoteLatency_Type = Integer32
_AfLTUStaRemoteLatency_Object = MibTableColumn
afLTUStaRemoteLatency = _AfLTUStaRemoteLatency_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 22),
    _AfLTUStaRemoteLatency_Type()
)
afLTUStaRemoteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteLatency.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteLatency.setUnits("ms")
_AfLTUStaRemoteDistance_Type = Integer32
_AfLTUStaRemoteDistance_Object = MibTableColumn
afLTUStaRemoteDistance = _AfLTUStaRemoteDistance_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 23),
    _AfLTUStaRemoteDistance_Type()
)
afLTUStaRemoteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteDistance.setStatus("current")
if mibBuilder.loadTexts:
    afLTUStaRemoteDistance.setUnits("km")
_AfLTUStaRemoteConnectionTime_Type = Counter64
_AfLTUStaRemoteConnectionTime_Object = MibTableColumn
afLTUStaRemoteConnectionTime = _AfLTUStaRemoteConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 24),
    _AfLTUStaRemoteConnectionTime_Type()
)
afLTUStaRemoteConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteConnectionTime.setStatus("current")
_AfLTUStaRemoteLastIp_Type = IpAddress
_AfLTUStaRemoteLastIp_Object = MibTableColumn
afLTUStaRemoteLastIp = _AfLTUStaRemoteLastIp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 25),
    _AfLTUStaRemoteLastIp_Type()
)
afLTUStaRemoteLastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteLastIp.setStatus("current")
_AfLTUStaRemoteRegistrationAttempts_Type = Integer32
_AfLTUStaRemoteRegistrationAttempts_Object = MibTableColumn
afLTUStaRemoteRegistrationAttempts = _AfLTUStaRemoteRegistrationAttempts_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 4, 1, 26),
    _AfLTUStaRemoteRegistrationAttempts_Type()
)
afLTUStaRemoteRegistrationAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUStaRemoteRegistrationAttempts.setStatus("current")
_AfLTUStats_ObjectIdentity = ObjectIdentity
afLTUStats = _AfLTUStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 5)
)
_AfLTUTxBytes_Type = Counter64
_AfLTUTxBytes_Object = MibScalar
afLTUTxBytes = _AfLTUTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 5, 1),
    _AfLTUTxBytes_Type()
)
afLTUTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUTxBytes.setStatus("current")
_AfLTUTxPps_Type = Integer32
_AfLTUTxPps_Object = MibScalar
afLTUTxPps = _AfLTUTxPps_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 5, 2),
    _AfLTUTxPps_Type()
)
afLTUTxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUTxPps.setStatus("current")
_AfLTURxBytes_Type = Counter64
_AfLTURxBytes_Object = MibScalar
afLTURxBytes = _AfLTURxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 5, 3),
    _AfLTURxBytes_Type()
)
afLTURxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTURxBytes.setStatus("current")
_AfLTURxPps_Type = Integer32
_AfLTURxPps_Object = MibScalar
afLTURxPps = _AfLTURxPps_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 5, 4),
    _AfLTURxPps_Type()
)
afLTURxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTURxPps.setStatus("current")


class _AfLTUConnected_Type(Integer32):
    """Custom type afLTUConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_AfLTUConnected_Type.__name__ = "Integer32"
_AfLTUConnected_Object = MibScalar
afLTUConnected = _AfLTUConnected_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 5, 5),
    _AfLTUConnected_Type()
)
afLTUConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUConnected.setStatus("current")
_AfLTUethStats_ObjectIdentity = ObjectIdentity
afLTUethStats = _AfLTUethStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 6)
)
_AfLTUethTxBytes_Type = Counter64
_AfLTUethTxBytes_Object = MibScalar
afLTUethTxBytes = _AfLTUethTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 6, 1),
    _AfLTUethTxBytes_Type()
)
afLTUethTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUethTxBytes.setStatus("current")
_AfLTUethTxPps_Type = Integer32
_AfLTUethTxPps_Object = MibScalar
afLTUethTxPps = _AfLTUethTxPps_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 6, 2),
    _AfLTUethTxPps_Type()
)
afLTUethTxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUethTxPps.setStatus("current")
_AfLTUethRxBytes_Type = Counter64
_AfLTUethRxBytes_Object = MibScalar
afLTUethRxBytes = _AfLTUethRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 6, 3),
    _AfLTUethRxBytes_Type()
)
afLTUethRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUethRxBytes.setStatus("current")
_AfLTUethRxPps_Type = Integer32
_AfLTUethRxPps_Object = MibScalar
afLTUethRxPps = _AfLTUethRxPps_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 6, 4),
    _AfLTUethRxPps_Type()
)
afLTUethRxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUethRxPps.setStatus("current")


class _AfLTUethConnected_Type(Integer32):
    """Custom type afLTUethConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_AfLTUethConnected_Type.__name__ = "Integer32"
_AfLTUethConnected_Object = MibScalar
afLTUethConnected = _AfLTUethConnected_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 6, 5),
    _AfLTUethConnected_Type()
)
afLTUethConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUethConnected.setStatus("current")
_AfLTUgpsStats_ObjectIdentity = ObjectIdentity
afLTUgpsStats = _AfLTUgpsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7)
)


class _AfLTUgpsStatus_Type(Integer32):
    """Custom type afLTUgpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("off", 1),
          ("on", 2))
    )


_AfLTUgpsStatus_Type.__name__ = "Integer32"
_AfLTUgpsStatus_Object = MibScalar
afLTUgpsStatus = _AfLTUgpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 1),
    _AfLTUgpsStatus_Type()
)
afLTUgpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsStatus.setStatus("current")


class _AfLTUgpsDimensions_Type(Integer32):
    """Custom type afLTUgpsDimensions based on Integer32"""
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
          ("nofix", 1),
          ("fix2d", 2),
          ("fix3d", 3))
    )


_AfLTUgpsDimensions_Type.__name__ = "Integer32"
_AfLTUgpsDimensions_Object = MibScalar
afLTUgpsDimensions = _AfLTUgpsDimensions_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 2),
    _AfLTUgpsDimensions_Type()
)
afLTUgpsDimensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsDimensions.setStatus("current")
_AfLTUgpsLat_Type = DisplayString
_AfLTUgpsLat_Object = MibScalar
afLTUgpsLat = _AfLTUgpsLat_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 3),
    _AfLTUgpsLat_Type()
)
afLTUgpsLat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsLat.setStatus("current")
_AfLTUgpsLon_Type = DisplayString
_AfLTUgpsLon_Object = MibScalar
afLTUgpsLon = _AfLTUgpsLon_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 4),
    _AfLTUgpsLon_Type()
)
afLTUgpsLon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsLon.setStatus("current")
_AfLTUgpsAltMeter_Type = DisplayString
_AfLTUgpsAltMeter_Object = MibScalar
afLTUgpsAltMeter = _AfLTUgpsAltMeter_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 5),
    _AfLTUgpsAltMeter_Type()
)
afLTUgpsAltMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsAltMeter.setStatus("current")
if mibBuilder.loadTexts:
    afLTUgpsAltMeter.setUnits("(m)")
_AfLTUgpsAltFeet_Type = DisplayString
_AfLTUgpsAltFeet_Object = MibScalar
afLTUgpsAltFeet = _AfLTUgpsAltFeet_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 6),
    _AfLTUgpsAltFeet_Type()
)
afLTUgpsAltFeet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsAltFeet.setStatus("current")
if mibBuilder.loadTexts:
    afLTUgpsAltFeet.setUnits("(ft)")
_AfLTUgpsSatsVisible_Type = Integer32
_AfLTUgpsSatsVisible_Object = MibScalar
afLTUgpsSatsVisible = _AfLTUgpsSatsVisible_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 7),
    _AfLTUgpsSatsVisible_Type()
)
afLTUgpsSatsVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsSatsVisible.setStatus("current")
_AfLTUgpsSatsTracked_Type = Integer32
_AfLTUgpsSatsTracked_Object = MibScalar
afLTUgpsSatsTracked = _AfLTUgpsSatsTracked_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 8),
    _AfLTUgpsSatsTracked_Type()
)
afLTUgpsSatsTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsSatsTracked.setStatus("current")
_AfLTUgpsHDOP_Type = DisplayString
_AfLTUgpsHDOP_Object = MibScalar
afLTUgpsHDOP = _AfLTUgpsHDOP_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 10, 1, 7, 9),
    _AfLTUgpsHDOP_Type()
)
afLTUgpsHDOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    afLTUgpsHDOP.setStatus("current")

# Managed Objects groups

ubntAFLTUStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 9, 2, 1)
)
ubntAFLTUStatusGroup.setObjects(
      *(("UBNT-AFLTU-MIB", "afLTURole"),
        ("UBNT-AFLTU-MIB", "afLTUFrequency"),
        ("UBNT-AFLTU-MIB", "afLTUAltFreqList"),
        ("UBNT-AFLTU-MIB", "afLTUBandwidth"),
        ("UBNT-AFLTU-MIB", "afLTUSsid"),
        ("UBNT-AFLTU-MIB", "afLTUTxEIRP"),
        ("UBNT-AFLTU-MIB", "afLTUAntennaGain"),
        ("UBNT-AFLTU-MIB", "afLTUCableLoss"),
        ("UBNT-AFLTU-MIB", "afLTUTxRate"),
        ("UBNT-AFLTU-MIB", "afLTUTxRateAuto"),
        ("UBNT-AFLTU-MIB", "afLTUDistanceScale"),
        ("UBNT-AFLTU-MIB", "afLTUMac"),
        ("UBNT-AFLTU-MIB", "afLTUDevModel"),
        ("UBNT-AFLTU-MIB", "afLTUDevName"),
        ("UBNT-AFLTU-MIB", "afLTUFirmwareVersion"),
        ("UBNT-AFLTU-MIB", "afLTUMemoryUsage"),
        ("UBNT-AFLTU-MIB", "afLTUCpuUsage"),
        ("UBNT-AFLTU-MIB", "afLTUUptime"),
        ("UBNT-AFLTU-MIB", "afLTUTxBytes"),
        ("UBNT-AFLTU-MIB", "afLTUTxPps"),
        ("UBNT-AFLTU-MIB", "afLTURxBytes"),
        ("UBNT-AFLTU-MIB", "afLTURxPps"),
        ("UBNT-AFLTU-MIB", "afLTUConnected"),
        ("UBNT-AFLTU-MIB", "afLTUethTxBytes"),
        ("UBNT-AFLTU-MIB", "afLTUethTxPps"),
        ("UBNT-AFLTU-MIB", "afLTUethRxBytes"),
        ("UBNT-AFLTU-MIB", "afLTUethRxPps"),
        ("UBNT-AFLTU-MIB", "afLTUethConnected"),
        ("UBNT-AFLTU-MIB", "afLTUgpsStatus"),
        ("UBNT-AFLTU-MIB", "afLTUgpsDimensions"),
        ("UBNT-AFLTU-MIB", "afLTUgpsLat"),
        ("UBNT-AFLTU-MIB", "afLTUgpsLon"),
        ("UBNT-AFLTU-MIB", "afLTUgpsAltMeter"),
        ("UBNT-AFLTU-MIB", "afLTUgpsAltFeet"),
        ("UBNT-AFLTU-MIB", "afLTUgpsSatsVisible"),
        ("UBNT-AFLTU-MIB", "afLTUgpsSatsTracked"),
        ("UBNT-AFLTU-MIB", "afLTUgpsHDOP"),
        ("UBNT-AFLTU-MIB", "afLTUStaTxRate"),
        ("UBNT-AFLTU-MIB", "afLTUStaRxRate"),
        ("UBNT-AFLTU-MIB", "afLTUStaTxCapacity"),
        ("UBNT-AFLTU-MIB", "afLTUStaRxCapacity"),
        ("UBNT-AFLTU-MIB", "afLTUStaRxPower0"),
        ("UBNT-AFLTU-MIB", "afLTUStaRxPower1"),
        ("UBNT-AFLTU-MIB", "afLTUStaIdealRxPower0"),
        ("UBNT-AFLTU-MIB", "afLTUStaIdealRxPower1"),
        ("UBNT-AFLTU-MIB", "afLTUStaRxPowerLevel0"),
        ("UBNT-AFLTU-MIB", "afLTUStaRxPowerLevel1"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteDevModel"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteDevName"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteFirmwareVersion"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteTxEIRP"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteRxPower0"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteRxPower1"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteIdealRxPower0"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteIdealRxPower1"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteRxPowerLevel0"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteRxPowerLevel1"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteLatency"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteDistance"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteConnectionTime"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteLastIp"),
        ("UBNT-AFLTU-MIB", "afLTUStaRemoteRegistrationAttempts"))
)
if mibBuilder.loadTexts:
    ubntAFLTUStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubntAFLTUStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 9, 2, 2)
)
ubntAFLTUStatusCompliance.setObjects(
    ("UBNT-AFLTU-MIB", "ubntAFLTUStatusGroup")
)
if mibBuilder.loadTexts:
    ubntAFLTUStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBNT-AFLTU-MIB",
    **{"afLTUCompliances": afLTUCompliances,
       "afLTUGroups": afLTUGroups,
       "ubntAFLTUStatusGroup": ubntAFLTUStatusGroup,
       "ubntAFLTUStatusCompliance": ubntAFLTUStatusCompliance,
       "afLTUMIB": afLTUMIB,
       "afLTUConfig": afLTUConfig,
       "afLTURole": afLTURole,
       "afLTUFrequency": afLTUFrequency,
       "afLTUAltFreqList": afLTUAltFreqList,
       "afLTUBandwidth": afLTUBandwidth,
       "afLTUSsid": afLTUSsid,
       "afLTUTxEIRP": afLTUTxEIRP,
       "afLTUAntennaGain": afLTUAntennaGain,
       "afLTUCableLoss": afLTUCableLoss,
       "afLTUTxRate": afLTUTxRate,
       "afLTUTxRateAuto": afLTUTxRateAuto,
       "afLTUDistanceScale": afLTUDistanceScale,
       "afLTUStatus": afLTUStatus,
       "afLTUMac": afLTUMac,
       "afLTUDevModel": afLTUDevModel,
       "afLTUDevName": afLTUDevName,
       "afLTUFirmwareVersion": afLTUFirmwareVersion,
       "afLTUMemoryUsage": afLTUMemoryUsage,
       "afLTUCpuUsage": afLTUCpuUsage,
       "afLTUUptime": afLTUUptime,
       "afLTUStationTable": afLTUStationTable,
       "afLTUStationEntry": afLTUStationEntry,
       "afLTUStaTxRate": afLTUStaTxRate,
       "afLTUStaRxRate": afLTUStaRxRate,
       "afLTUStaTxCapacity": afLTUStaTxCapacity,
       "afLTUStaRxCapacity": afLTUStaRxCapacity,
       "afLTUStaRxPower0": afLTUStaRxPower0,
       "afLTUStaRxPower1": afLTUStaRxPower1,
       "afLTUStaIdealRxPower0": afLTUStaIdealRxPower0,
       "afLTUStaIdealRxPower1": afLTUStaIdealRxPower1,
       "afLTUStaRxPowerLevel0": afLTUStaRxPowerLevel0,
       "afLTUStaRxPowerLevel1": afLTUStaRxPowerLevel1,
       "afLTUStaRemoteMac": afLTUStaRemoteMac,
       "afLTUStaRemoteDevModel": afLTUStaRemoteDevModel,
       "afLTUStaRemoteDevName": afLTUStaRemoteDevName,
       "afLTUStaRemoteFirmwareVersion": afLTUStaRemoteFirmwareVersion,
       "afLTUStaRemoteTxEIRP": afLTUStaRemoteTxEIRP,
       "afLTUStaRemoteRxPower0": afLTUStaRemoteRxPower0,
       "afLTUStaRemoteRxPower1": afLTUStaRemoteRxPower1,
       "afLTUStaRemoteIdealRxPower0": afLTUStaRemoteIdealRxPower0,
       "afLTUStaRemoteIdealRxPower1": afLTUStaRemoteIdealRxPower1,
       "afLTUStaRemoteRxPowerLevel0": afLTUStaRemoteRxPowerLevel0,
       "afLTUStaRemoteRxPowerLevel1": afLTUStaRemoteRxPowerLevel1,
       "afLTUStaRemoteLatency": afLTUStaRemoteLatency,
       "afLTUStaRemoteDistance": afLTUStaRemoteDistance,
       "afLTUStaRemoteConnectionTime": afLTUStaRemoteConnectionTime,
       "afLTUStaRemoteLastIp": afLTUStaRemoteLastIp,
       "afLTUStaRemoteRegistrationAttempts": afLTUStaRemoteRegistrationAttempts,
       "afLTUStats": afLTUStats,
       "afLTUTxBytes": afLTUTxBytes,
       "afLTUTxPps": afLTUTxPps,
       "afLTURxBytes": afLTURxBytes,
       "afLTURxPps": afLTURxPps,
       "afLTUConnected": afLTUConnected,
       "afLTUethStats": afLTUethStats,
       "afLTUethTxBytes": afLTUethTxBytes,
       "afLTUethTxPps": afLTUethTxPps,
       "afLTUethRxBytes": afLTUethRxBytes,
       "afLTUethRxPps": afLTUethRxPps,
       "afLTUethConnected": afLTUethConnected,
       "afLTUgpsStats": afLTUgpsStats,
       "afLTUgpsStatus": afLTUgpsStatus,
       "afLTUgpsDimensions": afLTUgpsDimensions,
       "afLTUgpsLat": afLTUgpsLat,
       "afLTUgpsLon": afLTUgpsLon,
       "afLTUgpsAltMeter": afLTUgpsAltMeter,
       "afLTUgpsAltFeet": afLTUgpsAltFeet,
       "afLTUgpsSatsVisible": afLTUgpsSatsVisible,
       "afLTUgpsSatsTracked": afLTUgpsSatsTracked,
       "afLTUgpsHDOP": afLTUgpsHDOP}
)
