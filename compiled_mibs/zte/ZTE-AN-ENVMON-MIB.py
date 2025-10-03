# SNMP MIB module (ZTE-AN-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zte\ZTE-AN-ENVMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:42 2025
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

(HCPerfCurrentCount,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAccessNode,
 zxAnEquipment) = mibBuilder.importSymbols(
    "ZTE-AN-SMI",
    "zxAccessNode",
    "zxAnEquipment")


# MODULE-IDENTITY

zxAnEnvMonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10)
)
if mibBuilder.loadTexts:
    zxAnEnvMonMib.setRevisions(
        ("2014-12-23 00:00",
         "2013-12-31 00:00",
         "2012-04-27 00:00",
         "2012-04-18 00:00",
         "2011-10-17 00:00",
         "2011-05-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZxAnEnvShutdownServiceType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("xpon", 0),
          ("xdsl", 1),
          ("p2p", 2),
          ("narrowband", 3))
    )


# MIB Managed Objects in the order of their OIDs

_ZxAnEnvMonGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnEnvMonGlobalObjects = _ZxAnEnvMonGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 1)
)


class _ZxAnEnvMonCapabilities_Type(Bits):
    """Custom type zxAnEnvMonCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("envTemperature", 0),
          ("fanAlarmBeep", 1),
          ("fanAutoSwitchByCardInstall", 2),
          ("fanSpeedCtrlBasedTemperature", 3),
          ("fanFixSpeed", 4),
          ("singleFanShutdown", 5),
          ("mpTemperature", 6),
          ("powerSupply", 7),
          ("cardTemperature", 8),
          ("fanSpeedPercentage", 9),
          ("backplaneInterface", 10),
          ("envMonitorInterfaceTrapEnable", 11),
          ("slaveShelfFanConfig", 12))
    )

_ZxAnEnvMonCapabilities_Type.__name__ = "Bits"
_ZxAnEnvMonCapabilities_Object = MibScalar
zxAnEnvMonCapabilities = _ZxAnEnvMonCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 1, 1),
    _ZxAnEnvMonCapabilities_Type()
)
zxAnEnvMonCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvMonCapabilities.setStatus("current")
_ZxAnEnvMonObjects_ObjectIdentity = ObjectIdentity
zxAnEnvMonObjects = _ZxAnEnvMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2)
)
_ZxAnEnvParamObjects_ObjectIdentity = ObjectIdentity
zxAnEnvParamObjects = _ZxAnEnvParamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1)
)
_ZxAnEnvParamGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnEnvParamGlobalObjects = _ZxAnEnvParamGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 1)
)


class _ZxAnEnvCardShutdownReason_Type(Integer32):
    """Custom type zxAnEnvCardShutdownReason based on Integer32"""
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
        *(("envHighTemperature", 1),
          ("cardHighTemperature", 2),
          ("chipHighTemperature", 3),
          ("emergencyPowerSaving", 4))
    )


_ZxAnEnvCardShutdownReason_Type.__name__ = "Integer32"
_ZxAnEnvCardShutdownReason_Object = MibScalar
zxAnEnvCardShutdownReason = _ZxAnEnvCardShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 1, 1),
    _ZxAnEnvCardShutdownReason_Type()
)
zxAnEnvCardShutdownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnEnvCardShutdownReason.setStatus("current")
_ZxAnEnvParamTable_Object = MibTable
zxAnEnvParamTable = _ZxAnEnvParamTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnEnvParamTable.setStatus("current")
_ZxAnEnvParamEntry_Object = MibTableRow
zxAnEnvParamEntry = _ZxAnEnvParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1)
)
zxAnEnvParamEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
)
if mibBuilder.loadTexts:
    zxAnEnvParamEntry.setStatus("current")
_ZxAnEnvRack_Type = Integer32
_ZxAnEnvRack_Object = MibTableColumn
zxAnEnvRack = _ZxAnEnvRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 1),
    _ZxAnEnvRack_Type()
)
zxAnEnvRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvRack.setStatus("current")
_ZxAnEnvShelf_Type = Integer32
_ZxAnEnvShelf_Object = MibTableColumn
zxAnEnvShelf = _ZxAnEnvShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 2),
    _ZxAnEnvShelf_Type()
)
zxAnEnvShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvShelf.setStatus("current")
_ZxAnEnvTemp_Type = Integer32
_ZxAnEnvTemp_Object = MibTableColumn
zxAnEnvTemp = _ZxAnEnvTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 3),
    _ZxAnEnvTemp_Type()
)
zxAnEnvTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvTemp.setUnits("Centigrade")


class _ZxAnEnvTempHighAlmThreshold_Type(Integer32):
    """Custom type zxAnEnvTempHighAlmThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 95),
    )


_ZxAnEnvTempHighAlmThreshold_Type.__name__ = "Integer32"
_ZxAnEnvTempHighAlmThreshold_Object = MibTableColumn
zxAnEnvTempHighAlmThreshold = _ZxAnEnvTempHighAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 4),
    _ZxAnEnvTempHighAlmThreshold_Type()
)
zxAnEnvTempHighAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvTempHighAlmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvTempHighAlmThreshold.setUnits("Centigrade")


class _ZxAnEnvTempCriticalAlmThreshold_Type(Integer32):
    """Custom type zxAnEnvTempCriticalAlmThreshold based on Integer32"""
    defaultValue = 100


_ZxAnEnvTempCriticalAlmThreshold_Type.__name__ = "Integer32"
_ZxAnEnvTempCriticalAlmThreshold_Object = MibTableColumn
zxAnEnvTempCriticalAlmThreshold = _ZxAnEnvTempCriticalAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 5),
    _ZxAnEnvTempCriticalAlmThreshold_Type()
)
zxAnEnvTempCriticalAlmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvTempCriticalAlmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvTempCriticalAlmThreshold.setUnits("Centigrade")


class _ZxAnEnvTempLowAlmThreshold_Type(Integer32):
    """Custom type zxAnEnvTempLowAlmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 0),
    )


_ZxAnEnvTempLowAlmThreshold_Type.__name__ = "Integer32"
_ZxAnEnvTempLowAlmThreshold_Object = MibTableColumn
zxAnEnvTempLowAlmThreshold = _ZxAnEnvTempLowAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 6),
    _ZxAnEnvTempLowAlmThreshold_Type()
)
zxAnEnvTempLowAlmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvTempLowAlmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvTempLowAlmThreshold.setUnits("Centigrade")
_ZxAnEnvShelfPowerConsumption_Type = Integer32
_ZxAnEnvShelfPowerConsumption_Object = MibTableColumn
zxAnEnvShelfPowerConsumption = _ZxAnEnvShelfPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 7),
    _ZxAnEnvShelfPowerConsumption_Type()
)
zxAnEnvShelfPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvShelfPowerConsumption.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvShelfPowerConsumption.setUnits("0.001W")
_ZxAnEnvShelfVoltage_Type = Integer32
_ZxAnEnvShelfVoltage_Object = MibTableColumn
zxAnEnvShelfVoltage = _ZxAnEnvShelfVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 8),
    _ZxAnEnvShelfVoltage_Type()
)
zxAnEnvShelfVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvShelfVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvShelfVoltage.setUnits("0.001Volts")
_ZxAnEnvShelfCurrent_Type = Integer32
_ZxAnEnvShelfCurrent_Object = MibTableColumn
zxAnEnvShelfCurrent = _ZxAnEnvShelfCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 5, 1, 9),
    _ZxAnEnvShelfCurrent_Type()
)
zxAnEnvShelfCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvShelfCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvShelfCurrent.setUnits("0.001Amp")
_ZxAnCardEnvParamTable_Object = MibTable
zxAnCardEnvParamTable = _ZxAnCardEnvParamTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnCardEnvParamTable.setStatus("current")
_ZxAnCardEnvParamEntry_Object = MibTableRow
zxAnCardEnvParamEntry = _ZxAnCardEnvParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1)
)
zxAnCardEnvParamEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvSlot"),
)
if mibBuilder.loadTexts:
    zxAnCardEnvParamEntry.setStatus("current")
_ZxAnEnvSlot_Type = Integer32
_ZxAnEnvSlot_Object = MibTableColumn
zxAnEnvSlot = _ZxAnEnvSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 1),
    _ZxAnEnvSlot_Type()
)
zxAnEnvSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvSlot.setStatus("current")
_ZxAnCardTemp_Type = Integer32
_ZxAnCardTemp_Object = MibTableColumn
zxAnCardTemp = _ZxAnCardTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 2),
    _ZxAnCardTemp_Type()
)
zxAnCardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardTemp.setStatus("current")
_ZxAnCardPowerConsumption_Type = Integer32
_ZxAnCardPowerConsumption_Object = MibTableColumn
zxAnCardPowerConsumption = _ZxAnCardPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 3),
    _ZxAnCardPowerConsumption_Type()
)
zxAnCardPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardPowerConsumption.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardPowerConsumption.setUnits("0.001W")
_ZxAnCardVoltage_Type = Integer32
_ZxAnCardVoltage_Object = MibTableColumn
zxAnCardVoltage = _ZxAnCardVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 4),
    _ZxAnCardVoltage_Type()
)
zxAnCardVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardVoltage.setUnits("0.001Volts")
_ZxAnCardCurrent_Type = Integer32
_ZxAnCardCurrent_Object = MibTableColumn
zxAnCardCurrent = _ZxAnCardCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 5),
    _ZxAnCardCurrent_Type()
)
zxAnCardCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardCurrent.setUnits("0.001Amp")
_ZxAnCardCriticalTempAlmThreshold_Type = Integer32
_ZxAnCardCriticalTempAlmThreshold_Object = MibTableColumn
zxAnCardCriticalTempAlmThreshold = _ZxAnCardCriticalTempAlmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 6),
    _ZxAnCardCriticalTempAlmThreshold_Type()
)
zxAnCardCriticalTempAlmThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnCardCriticalTempAlmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardCriticalTempAlmThreshold.setUnits("Centigrade")
_ZxAnCardOptHighestTemp_Type = Integer32
_ZxAnCardOptHighestTemp_Object = MibTableColumn
zxAnCardOptHighestTemp = _ZxAnCardOptHighestTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 7),
    _ZxAnCardOptHighestTemp_Type()
)
zxAnCardOptHighestTemp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnCardOptHighestTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardOptHighestTemp.setUnits("0.001Degrees")
_ZxAnCardOptCriticalTempAlmThresh_Type = Integer32
_ZxAnCardOptCriticalTempAlmThresh_Object = MibTableColumn
zxAnCardOptCriticalTempAlmThresh = _ZxAnCardOptCriticalTempAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 8),
    _ZxAnCardOptCriticalTempAlmThresh_Type()
)
zxAnCardOptCriticalTempAlmThresh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnCardOptCriticalTempAlmThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardOptCriticalTempAlmThresh.setUnits("Centigrade")
_ZxAnCardOptHighestTempPortNo_Type = Integer32
_ZxAnCardOptHighestTempPortNo_Object = MibTableColumn
zxAnCardOptHighestTempPortNo = _ZxAnCardOptHighestTempPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 9),
    _ZxAnCardOptHighestTempPortNo_Type()
)
zxAnCardOptHighestTempPortNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnCardOptHighestTempPortNo.setStatus("current")
_ZxAnCardHeatRadiationAlmThresh_Type = Integer32
_ZxAnCardHeatRadiationAlmThresh_Object = MibTableColumn
zxAnCardHeatRadiationAlmThresh = _ZxAnCardHeatRadiationAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 6, 1, 10),
    _ZxAnCardHeatRadiationAlmThresh_Type()
)
zxAnCardHeatRadiationAlmThresh.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnCardHeatRadiationAlmThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCardHeatRadiationAlmThresh.setUnits("Centigrade")
_ZxAnCardEnvHis15MinPerfTable_Object = MibTable
zxAnCardEnvHis15MinPerfTable = _ZxAnCardEnvHis15MinPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnCardEnvHis15MinPerfTable.setStatus("current")
_ZxAnCardEnvHis15MinPerfEntry_Object = MibTableRow
zxAnCardEnvHis15MinPerfEntry = _ZxAnCardEnvHis15MinPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 7, 1)
)
zxAnCardEnvHis15MinPerfEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvSlot"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnCardEnvHis15MinIntervalNo"),
)
if mibBuilder.loadTexts:
    zxAnCardEnvHis15MinPerfEntry.setStatus("current")


class _ZxAnCardEnvHis15MinIntervalNo_Type(Integer32):
    """Custom type zxAnCardEnvHis15MinIntervalNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ZxAnCardEnvHis15MinIntervalNo_Type.__name__ = "Integer32"
_ZxAnCardEnvHis15MinIntervalNo_Object = MibTableColumn
zxAnCardEnvHis15MinIntervalNo = _ZxAnCardEnvHis15MinIntervalNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 7, 1, 1),
    _ZxAnCardEnvHis15MinIntervalNo_Type()
)
zxAnCardEnvHis15MinIntervalNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardEnvHis15MinIntervalNo.setStatus("current")
_ZxAnCardEnvHis15MinDateTime_Type = DateAndTime
_ZxAnCardEnvHis15MinDateTime_Object = MibTableColumn
zxAnCardEnvHis15MinDateTime = _ZxAnCardEnvHis15MinDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 7, 1, 2),
    _ZxAnCardEnvHis15MinDateTime_Type()
)
zxAnCardEnvHis15MinDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardEnvHis15MinDateTime.setStatus("current")
_ZxAnCardEnvHis15MinTemp_Type = Counter64
_ZxAnCardEnvHis15MinTemp_Object = MibTableColumn
zxAnCardEnvHis15MinTemp = _ZxAnCardEnvHis15MinTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 7, 1, 3),
    _ZxAnCardEnvHis15MinTemp_Type()
)
zxAnCardEnvHis15MinTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardEnvHis15MinTemp.setStatus("current")
_ZxAnCardEnvHis1DayPerfTable_Object = MibTable
zxAnCardEnvHis1DayPerfTable = _ZxAnCardEnvHis1DayPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 8)
)
if mibBuilder.loadTexts:
    zxAnCardEnvHis1DayPerfTable.setStatus("current")
_ZxAnCardEnvHis1DayPerfEntry_Object = MibTableRow
zxAnCardEnvHis1DayPerfEntry = _ZxAnCardEnvHis1DayPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 8, 1)
)
zxAnCardEnvHis1DayPerfEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvSlot"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnCardEnvHis1DayIntervalNo"),
)
if mibBuilder.loadTexts:
    zxAnCardEnvHis1DayPerfEntry.setStatus("current")


class _ZxAnCardEnvHis1DayIntervalNo_Type(Integer32):
    """Custom type zxAnCardEnvHis1DayIntervalNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ZxAnCardEnvHis1DayIntervalNo_Type.__name__ = "Integer32"
_ZxAnCardEnvHis1DayIntervalNo_Object = MibTableColumn
zxAnCardEnvHis1DayIntervalNo = _ZxAnCardEnvHis1DayIntervalNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 8, 1, 1),
    _ZxAnCardEnvHis1DayIntervalNo_Type()
)
zxAnCardEnvHis1DayIntervalNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardEnvHis1DayIntervalNo.setStatus("current")
_ZxAnCardEnvHis1DayDateTime_Type = DateAndTime
_ZxAnCardEnvHis1DayDateTime_Object = MibTableColumn
zxAnCardEnvHis1DayDateTime = _ZxAnCardEnvHis1DayDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 8, 1, 2),
    _ZxAnCardEnvHis1DayDateTime_Type()
)
zxAnCardEnvHis1DayDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardEnvHis1DayDateTime.setStatus("current")
_ZxAnCardEnvHis1DayTemp_Type = Counter64
_ZxAnCardEnvHis1DayTemp_Object = MibTableColumn
zxAnCardEnvHis1DayTemp = _ZxAnCardEnvHis1DayTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 8, 1, 3),
    _ZxAnCardEnvHis1DayTemp_Type()
)
zxAnCardEnvHis1DayTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCardEnvHis1DayTemp.setStatus("current")
_ZxAnCardEnvAlmProfileConfTable_Object = MibTable
zxAnCardEnvAlmProfileConfTable = _ZxAnCardEnvAlmProfileConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9)
)
if mibBuilder.loadTexts:
    zxAnCardEnvAlmProfileConfTable.setStatus("current")
_ZxAnCardEnvAlmProfileConfEntry_Object = MibTableRow
zxAnCardEnvAlmProfileConfEntry = _ZxAnCardEnvAlmProfileConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1)
)
zxAnCardEnvAlmProfileConfEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnCardEnvAlmProfileName"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnCardEnvPerfVariable"),
)
if mibBuilder.loadTexts:
    zxAnCardEnvAlmProfileConfEntry.setStatus("current")


class _ZxAnCardEnvAlmProfileName_Type(DisplayString):
    """Custom type zxAnCardEnvAlmProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnCardEnvAlmProfileName_Type.__name__ = "DisplayString"
_ZxAnCardEnvAlmProfileName_Object = MibTableColumn
zxAnCardEnvAlmProfileName = _ZxAnCardEnvAlmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 1),
    _ZxAnCardEnvAlmProfileName_Type()
)
zxAnCardEnvAlmProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardEnvAlmProfileName.setStatus("current")
_ZxAnCardEnvPerfVariable_Type = ObjectIdentifier
_ZxAnCardEnvPerfVariable_Object = MibTableColumn
zxAnCardEnvPerfVariable = _ZxAnCardEnvPerfVariable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 2),
    _ZxAnCardEnvPerfVariable_Type()
)
zxAnCardEnvPerfVariable.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCardEnvPerfVariable.setStatus("current")
_ZxAnCardEnvRiseAlmThresh_Type = HCPerfCurrentCount
_ZxAnCardEnvRiseAlmThresh_Object = MibTableColumn
zxAnCardEnvRiseAlmThresh = _ZxAnCardEnvRiseAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 3),
    _ZxAnCardEnvRiseAlmThresh_Type()
)
zxAnCardEnvRiseAlmThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvRiseAlmThresh.setStatus("current")
_ZxAnCardEnvClrRiseAlmThresh_Type = HCPerfCurrentCount
_ZxAnCardEnvClrRiseAlmThresh_Object = MibTableColumn
zxAnCardEnvClrRiseAlmThresh = _ZxAnCardEnvClrRiseAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 4),
    _ZxAnCardEnvClrRiseAlmThresh_Type()
)
zxAnCardEnvClrRiseAlmThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvClrRiseAlmThresh.setStatus("current")
_ZxAnCardEnvRiseWarnThresh_Type = HCPerfCurrentCount
_ZxAnCardEnvRiseWarnThresh_Object = MibTableColumn
zxAnCardEnvRiseWarnThresh = _ZxAnCardEnvRiseWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 5),
    _ZxAnCardEnvRiseWarnThresh_Type()
)
zxAnCardEnvRiseWarnThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvRiseWarnThresh.setStatus("current")
_ZxAnCardEnvClrRiseWarnThresh_Type = HCPerfCurrentCount
_ZxAnCardEnvClrRiseWarnThresh_Object = MibTableColumn
zxAnCardEnvClrRiseWarnThresh = _ZxAnCardEnvClrRiseWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 6),
    _ZxAnCardEnvClrRiseWarnThresh_Type()
)
zxAnCardEnvClrRiseWarnThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvClrRiseWarnThresh.setStatus("current")
_ZxAnCardEnvFallWarnThresh_Type = HCPerfCurrentCount
_ZxAnCardEnvFallWarnThresh_Object = MibTableColumn
zxAnCardEnvFallWarnThresh = _ZxAnCardEnvFallWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 7),
    _ZxAnCardEnvFallWarnThresh_Type()
)
zxAnCardEnvFallWarnThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvFallWarnThresh.setStatus("current")
_ZxAnCardEnvClrFallWarnThresh_Type = HCPerfCurrentCount
_ZxAnCardEnvClrFallWarnThresh_Object = MibTableColumn
zxAnCardEnvClrFallWarnThresh = _ZxAnCardEnvClrFallWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 8),
    _ZxAnCardEnvClrFallWarnThresh_Type()
)
zxAnCardEnvClrFallWarnThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvClrFallWarnThresh.setStatus("current")
_ZxAnCardEnvFallAlmThresh_Type = HCPerfCurrentCount
_ZxAnCardEnvFallAlmThresh_Object = MibTableColumn
zxAnCardEnvFallAlmThresh = _ZxAnCardEnvFallAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 9),
    _ZxAnCardEnvFallAlmThresh_Type()
)
zxAnCardEnvFallAlmThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvFallAlmThresh.setStatus("current")
_ZxAnCardEnvClrFallAlmThresh_Type = HCPerfCurrentCount
_ZxAnCardEnvClrFallAlmThresh_Object = MibTableColumn
zxAnCardEnvClrFallAlmThresh = _ZxAnCardEnvClrFallAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 10),
    _ZxAnCardEnvClrFallAlmThresh_Type()
)
zxAnCardEnvClrFallAlmThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvClrFallAlmThresh.setStatus("current")
_ZxAnCardEnvAlmPrfConfRowStatus_Type = RowStatus
_ZxAnCardEnvAlmPrfConfRowStatus_Object = MibTableColumn
zxAnCardEnvAlmPrfConfRowStatus = _ZxAnCardEnvAlmPrfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 9, 1, 50),
    _ZxAnCardEnvAlmPrfConfRowStatus_Type()
)
zxAnCardEnvAlmPrfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvAlmPrfConfRowStatus.setStatus("current")
_ZxAnCardEnvAlmProfileApplyTable_Object = MibTable
zxAnCardEnvAlmProfileApplyTable = _ZxAnCardEnvAlmProfileApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 10)
)
if mibBuilder.loadTexts:
    zxAnCardEnvAlmProfileApplyTable.setStatus("current")
_ZxAnCardEnvAlmProfileApplyEntry_Object = MibTableRow
zxAnCardEnvAlmProfileApplyEntry = _ZxAnCardEnvAlmProfileApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 10, 1)
)
zxAnCardEnvAlmProfileApplyEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvSlot"),
)
if mibBuilder.loadTexts:
    zxAnCardEnvAlmProfileApplyEntry.setStatus("current")


class _ZxAnCardEnvAlmPrf_Type(DisplayString):
    """Custom type zxAnCardEnvAlmPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnCardEnvAlmPrf_Type.__name__ = "DisplayString"
_ZxAnCardEnvAlmPrf_Object = MibTableColumn
zxAnCardEnvAlmPrf = _ZxAnCardEnvAlmPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 10, 1, 1),
    _ZxAnCardEnvAlmPrf_Type()
)
zxAnCardEnvAlmPrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvAlmPrf.setStatus("current")
_ZxAnCardEnvAlmPrfApplyRowStatus_Type = RowStatus
_ZxAnCardEnvAlmPrfApplyRowStatus_Object = MibTableColumn
zxAnCardEnvAlmPrfApplyRowStatus = _ZxAnCardEnvAlmPrfApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 10, 1, 50),
    _ZxAnCardEnvAlmPrfApplyRowStatus_Type()
)
zxAnCardEnvAlmPrfApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvAlmPrfApplyRowStatus.setStatus("current")
_ZxAnCardEnvAlmProfileTable_Object = MibTable
zxAnCardEnvAlmProfileTable = _ZxAnCardEnvAlmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 11)
)
if mibBuilder.loadTexts:
    zxAnCardEnvAlmProfileTable.setStatus("current")
_ZxAnCardEnvAlmProfileEntry_Object = MibTableRow
zxAnCardEnvAlmProfileEntry = _ZxAnCardEnvAlmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 11, 1)
)
zxAnCardEnvAlmProfileEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnCardEnvAlmProfileName"),
)
if mibBuilder.loadTexts:
    zxAnCardEnvAlmProfileEntry.setStatus("current")
_ZxAnCardEnvAlmPrfRowStatus_Type = RowStatus
_ZxAnCardEnvAlmPrfRowStatus_Object = MibTableColumn
zxAnCardEnvAlmPrfRowStatus = _ZxAnCardEnvAlmPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 11, 1, 50),
    _ZxAnCardEnvAlmPrfRowStatus_Type()
)
zxAnCardEnvAlmPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCardEnvAlmPrfRowStatus.setStatus("current")
_ZxAnEnvOverheatProtectTable_Object = MibTable
zxAnEnvOverheatProtectTable = _ZxAnEnvOverheatProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 13)
)
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectTable.setStatus("current")
_ZxAnEnvOverheatProtectEntry_Object = MibTableRow
zxAnEnvOverheatProtectEntry = _ZxAnEnvOverheatProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 13, 1)
)
zxAnEnvOverheatProtectEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
)
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectEntry.setStatus("current")


class _ZxAnEnvOverheatProtectEnable_Type(Integer32):
    """Custom type zxAnEnvOverheatProtectEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnEnvOverheatProtectEnable_Type.__name__ = "Integer32"
_ZxAnEnvOverheatProtectEnable_Object = MibTableColumn
zxAnEnvOverheatProtectEnable = _ZxAnEnvOverheatProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 13, 1, 1),
    _ZxAnEnvOverheatProtectEnable_Type()
)
zxAnEnvOverheatProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectEnable.setStatus("current")


class _ZxAnEnvOverheatProtectDelay_Type(Integer32):
    """Custom type zxAnEnvOverheatProtectDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxAnEnvOverheatProtectDelay_Type.__name__ = "Integer32"
_ZxAnEnvOverheatProtectDelay_Object = MibTableColumn
zxAnEnvOverheatProtectDelay = _ZxAnEnvOverheatProtectDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 13, 1, 2),
    _ZxAnEnvOverheatProtectDelay_Type()
)
zxAnEnvOverheatProtectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectDelay.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectDelay.setUnits("minutes")


class _ZxAnEnvOverheatProtectFirstStep_Type(ZxAnEnvShutdownServiceType):
    """Custom type zxAnEnvOverheatProtectFirstStep based on ZxAnEnvShutdownServiceType"""
    defaultBinValue = "111"


_ZxAnEnvOverheatProtectFirstStep_Type.__name__ = "ZxAnEnvShutdownServiceType"
_ZxAnEnvOverheatProtectFirstStep_Object = MibTableColumn
zxAnEnvOverheatProtectFirstStep = _ZxAnEnvOverheatProtectFirstStep_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 13, 1, 3),
    _ZxAnEnvOverheatProtectFirstStep_Type()
)
zxAnEnvOverheatProtectFirstStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectFirstStep.setStatus("current")


class _ZxAnEnvOverheatProtectSecondStep_Type(ZxAnEnvShutdownServiceType):
    """Custom type zxAnEnvOverheatProtectSecondStep based on ZxAnEnvShutdownServiceType"""
    defaultBinValue = "0001"


_ZxAnEnvOverheatProtectSecondStep_Type.__name__ = "ZxAnEnvShutdownServiceType"
_ZxAnEnvOverheatProtectSecondStep_Object = MibTableColumn
zxAnEnvOverheatProtectSecondStep = _ZxAnEnvOverheatProtectSecondStep_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 13, 1, 4),
    _ZxAnEnvOverheatProtectSecondStep_Type()
)
zxAnEnvOverheatProtectSecondStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvOverheatProtectSecondStep.setStatus("current")
_ZxAnEnvCardOverheatProtectTable_Object = MibTable
zxAnEnvCardOverheatProtectTable = _ZxAnEnvCardOverheatProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 14)
)
if mibBuilder.loadTexts:
    zxAnEnvCardOverheatProtectTable.setStatus("current")
_ZxAnEnvCardOverheatProtectEntry_Object = MibTableRow
zxAnEnvCardOverheatProtectEntry = _ZxAnEnvCardOverheatProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 14, 1)
)
zxAnEnvCardOverheatProtectEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
)
if mibBuilder.loadTexts:
    zxAnEnvCardOverheatProtectEntry.setStatus("current")


class _ZxAnEnvCardCriticalTempProtectEn_Type(Integer32):
    """Custom type zxAnEnvCardCriticalTempProtectEn based on Integer32"""
    defaultValue = 1

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


_ZxAnEnvCardCriticalTempProtectEn_Type.__name__ = "Integer32"
_ZxAnEnvCardCriticalTempProtectEn_Object = MibTableColumn
zxAnEnvCardCriticalTempProtectEn = _ZxAnEnvCardCriticalTempProtectEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 1, 14, 1, 1),
    _ZxAnEnvCardCriticalTempProtectEn_Type()
)
zxAnEnvCardCriticalTempProtectEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvCardCriticalTempProtectEn.setStatus("current")
_ZxAnEnvMonInterfaceObjects_ObjectIdentity = ObjectIdentity
zxAnEnvMonInterfaceObjects = _ZxAnEnvMonInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 2)
)
_ZxAnEnvMonInterfaceTable_Object = MibTable
zxAnEnvMonInterfaceTable = _ZxAnEnvMonInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnEnvMonInterfaceTable.setStatus("current")
_ZxAnEnvMonInterfaceEntry_Object = MibTableRow
zxAnEnvMonInterfaceEntry = _ZxAnEnvMonInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 2, 5, 1)
)
zxAnEnvMonInterfaceEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
)
if mibBuilder.loadTexts:
    zxAnEnvMonInterfaceEntry.setStatus("current")


class _ZxAnEnvMonInterfaceUsage_Type(Integer32):
    """Custom type zxAnEnvMonInterfaceUsage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("epm", 1),
          ("fanTray", 2),
          ("noUse", 3),
          ("noSupport", 4),
          ("etmWithTestSubcard", 5),
          ("etmWithoutTestSubcard", 6))
    )


_ZxAnEnvMonInterfaceUsage_Type.__name__ = "Integer32"
_ZxAnEnvMonInterfaceUsage_Object = MibTableColumn
zxAnEnvMonInterfaceUsage = _ZxAnEnvMonInterfaceUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 2, 5, 1, 1),
    _ZxAnEnvMonInterfaceUsage_Type()
)
zxAnEnvMonInterfaceUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvMonInterfaceUsage.setStatus("current")


class _ZxAnEnvEpmConnectPort_Type(Integer32):
    """Custom type zxAnEnvEpmConnectPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("port0", 1),
          ("port1", 2),
          ("notconfigured", 255))
    )


_ZxAnEnvEpmConnectPort_Type.__name__ = "Integer32"
_ZxAnEnvEpmConnectPort_Object = MibTableColumn
zxAnEnvEpmConnectPort = _ZxAnEnvEpmConnectPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 2, 5, 1, 2),
    _ZxAnEnvEpmConnectPort_Type()
)
zxAnEnvEpmConnectPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvEpmConnectPort.setStatus("current")


class _ZxAnEnvBackplaneInterfaceUsage_Type(Integer32):
    """Custom type zxAnEnvBackplaneInterfaceUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fan", 1),
          ("noUse", 3),
          ("noSupport", 255))
    )


_ZxAnEnvBackplaneInterfaceUsage_Type.__name__ = "Integer32"
_ZxAnEnvBackplaneInterfaceUsage_Object = MibTableColumn
zxAnEnvBackplaneInterfaceUsage = _ZxAnEnvBackplaneInterfaceUsage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 2, 5, 1, 3),
    _ZxAnEnvBackplaneInterfaceUsage_Type()
)
zxAnEnvBackplaneInterfaceUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvBackplaneInterfaceUsage.setStatus("current")
_ZxAnEnvPowerSupplyObjects_ObjectIdentity = ObjectIdentity
zxAnEnvPowerSupplyObjects = _ZxAnEnvPowerSupplyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3)
)
_ZxAnPowerSupplyGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnPowerSupplyGlobalObjects = _ZxAnPowerSupplyGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 1)
)


class _ZxAnEnvEmergencyPowerSaveEnable_Type(Integer32):
    """Custom type zxAnEnvEmergencyPowerSaveEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnEnvEmergencyPowerSaveEnable_Type.__name__ = "Integer32"
_ZxAnEnvEmergencyPowerSaveEnable_Object = MibScalar
zxAnEnvEmergencyPowerSaveEnable = _ZxAnEnvEmergencyPowerSaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 1, 1),
    _ZxAnEnvEmergencyPowerSaveEnable_Type()
)
zxAnEnvEmergencyPowerSaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyPowerSaveEnable.setStatus("current")


class _ZxAnEnvEmergencyPowerSaveDelay_Type(Integer32):
    """Custom type zxAnEnvEmergencyPowerSaveDelay based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_ZxAnEnvEmergencyPowerSaveDelay_Type.__name__ = "Integer32"
_ZxAnEnvEmergencyPowerSaveDelay_Object = MibScalar
zxAnEnvEmergencyPowerSaveDelay = _ZxAnEnvEmergencyPowerSaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 1, 2),
    _ZxAnEnvEmergencyPowerSaveDelay_Type()
)
zxAnEnvEmergencyPowerSaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyPowerSaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyPowerSaveDelay.setUnits("Minutes")


class _ZxAnEnvEmergencyPowerSaveRecover_Type(Integer32):
    """Custom type zxAnEnvEmergencyPowerSaveRecover based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_ZxAnEnvEmergencyPowerSaveRecover_Type.__name__ = "Integer32"
_ZxAnEnvEmergencyPowerSaveRecover_Object = MibScalar
zxAnEnvEmergencyPowerSaveRecover = _ZxAnEnvEmergencyPowerSaveRecover_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 1, 3),
    _ZxAnEnvEmergencyPowerSaveRecover_Type()
)
zxAnEnvEmergencyPowerSaveRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyPowerSaveRecover.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyPowerSaveRecover.setUnits("Minutes")


class _ZxAnEnvEmergencyPowerSaveSvcType_Type(ZxAnEnvShutdownServiceType):
    """Custom type zxAnEnvEmergencyPowerSaveSvcType based on ZxAnEnvShutdownServiceType"""
    defaultBinValue = "111"


_ZxAnEnvEmergencyPowerSaveSvcType_Type.__name__ = "ZxAnEnvShutdownServiceType"
_ZxAnEnvEmergencyPowerSaveSvcType_Object = MibScalar
zxAnEnvEmergencyPowerSaveSvcType = _ZxAnEnvEmergencyPowerSaveSvcType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 1, 4),
    _ZxAnEnvEmergencyPowerSaveSvcType_Type()
)
zxAnEnvEmergencyPowerSaveSvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyPowerSaveSvcType.setStatus("current")


class _ZxAnEnvPowerMode_Type(Integer32):
    """Custom type zxAnEnvPowerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("battery", 2))
    )


_ZxAnEnvPowerMode_Type.__name__ = "Integer32"
_ZxAnEnvPowerMode_Object = MibScalar
zxAnEnvPowerMode = _ZxAnEnvPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 1, 5),
    _ZxAnEnvPowerMode_Type()
)
zxAnEnvPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvPowerMode.setStatus("current")
_ZxAnEnvEmergencyBatteryVoltage_Type = Integer32
_ZxAnEnvEmergencyBatteryVoltage_Object = MibScalar
zxAnEnvEmergencyBatteryVoltage = _ZxAnEnvEmergencyBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 1, 6),
    _ZxAnEnvEmergencyBatteryVoltage_Type()
)
zxAnEnvEmergencyBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyBatteryVoltage.setUnits("0.001Volts")


class _ZxAnEnvEmergencyBatteryThreshold_Type(Integer32):
    """Custom type zxAnEnvEmergencyBatteryThreshold based on Integer32"""
    defaultValue = 48000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45000, 53000),
    )


_ZxAnEnvEmergencyBatteryThreshold_Type.__name__ = "Integer32"
_ZxAnEnvEmergencyBatteryThreshold_Object = MibScalar
zxAnEnvEmergencyBatteryThreshold = _ZxAnEnvEmergencyBatteryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 1, 7),
    _ZxAnEnvEmergencyBatteryThreshold_Type()
)
zxAnEnvEmergencyBatteryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyBatteryThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEnvEmergencyBatteryThreshold.setUnits("0.001Volts")
_ZxAnPowerSupplyCapabilityTable_Object = MibTable
zxAnPowerSupplyCapabilityTable = _ZxAnPowerSupplyCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 10)
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyCapabilityTable.setStatus("current")
_ZxAnPowerSupplyCapabilityEntry_Object = MibTableRow
zxAnPowerSupplyCapabilityEntry = _ZxAnPowerSupplyCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 10, 1)
)
zxAnPowerSupplyCapabilityEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyCapabilityEntry.setStatus("current")
_ZxAnPowerSupplyMaxPowerNum_Type = Integer32
_ZxAnPowerSupplyMaxPowerNum_Object = MibTableColumn
zxAnPowerSupplyMaxPowerNum = _ZxAnPowerSupplyMaxPowerNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 10, 1, 1),
    _ZxAnPowerSupplyMaxPowerNum_Type()
)
zxAnPowerSupplyMaxPowerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyMaxPowerNum.setStatus("current")
_ZxAnPowerSupplyTable_Object = MibTable
zxAnPowerSupplyTable = _ZxAnPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11)
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyTable.setStatus("current")
_ZxAnPowerSupplyEntry_Object = MibTableRow
zxAnPowerSupplyEntry = _ZxAnPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11, 1)
)
zxAnPowerSupplyEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvSlot"),
)
if mibBuilder.loadTexts:
    zxAnPowerSupplyEntry.setStatus("current")


class _ZxAnPowerSupplyOperStatus_Type(Integer32):
    """Custom type zxAnPowerSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("hwOffline", 2),
          ("powerFaulty", 3))
    )


_ZxAnPowerSupplyOperStatus_Type.__name__ = "Integer32"
_ZxAnPowerSupplyOperStatus_Object = MibTableColumn
zxAnPowerSupplyOperStatus = _ZxAnPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11, 1, 1),
    _ZxAnPowerSupplyOperStatus_Type()
)
zxAnPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyOperStatus.setStatus("current")
_ZxAnPowerSupplyInVoltage_Type = Integer32
_ZxAnPowerSupplyInVoltage_Object = MibTableColumn
zxAnPowerSupplyInVoltage = _ZxAnPowerSupplyInVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11, 1, 2),
    _ZxAnPowerSupplyInVoltage_Type()
)
zxAnPowerSupplyInVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInVoltage.setUnits("Volts")


class _ZxAnPowerSupplyInVoltageStatus_Type(Integer32):
    """Custom type zxAnPowerSupplyInVoltageStatus based on Integer32"""
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
        *(("normal", 1),
          ("overVoltage", 2),
          ("underVoltage", 3),
          ("off", 4))
    )


_ZxAnPowerSupplyInVoltageStatus_Type.__name__ = "Integer32"
_ZxAnPowerSupplyInVoltageStatus_Object = MibTableColumn
zxAnPowerSupplyInVoltageStatus = _ZxAnPowerSupplyInVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11, 1, 3),
    _ZxAnPowerSupplyInVoltageStatus_Type()
)
zxAnPowerSupplyInVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInVoltageStatus.setStatus("current")


class _ZxAnPowerInVoltageUpperThresh_Type(Integer32):
    """Custom type zxAnPowerInVoltageUpperThresh based on Integer32"""
    defaultValue = 0


_ZxAnPowerInVoltageUpperThresh_Type.__name__ = "Integer32"
_ZxAnPowerInVoltageUpperThresh_Object = MibTableColumn
zxAnPowerInVoltageUpperThresh = _ZxAnPowerInVoltageUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11, 1, 4),
    _ZxAnPowerInVoltageUpperThresh_Type()
)
zxAnPowerInVoltageUpperThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPowerInVoltageUpperThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerInVoltageUpperThresh.setUnits("Volts")


class _ZxAnPowerInVoltageLowerThresh_Type(Integer32):
    """Custom type zxAnPowerInVoltageLowerThresh based on Integer32"""
    defaultValue = 0


_ZxAnPowerInVoltageLowerThresh_Type.__name__ = "Integer32"
_ZxAnPowerInVoltageLowerThresh_Object = MibTableColumn
zxAnPowerInVoltageLowerThresh = _ZxAnPowerInVoltageLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11, 1, 5),
    _ZxAnPowerInVoltageLowerThresh_Type()
)
zxAnPowerInVoltageLowerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPowerInVoltageLowerThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerInVoltageLowerThresh.setUnits("Volts")
_ZxAnPowerSupplyInCurrent_Type = Integer32
_ZxAnPowerSupplyInCurrent_Object = MibTableColumn
zxAnPowerSupplyInCurrent = _ZxAnPowerSupplyInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11, 1, 6),
    _ZxAnPowerSupplyInCurrent_Type()
)
zxAnPowerSupplyInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerSupplyInCurrent.setUnits("Amp")


class _ZxAnPowerInCurrentThresh_Type(Integer32):
    """Custom type zxAnPowerInCurrentThresh based on Integer32"""
    defaultValue = 0


_ZxAnPowerInCurrentThresh_Type.__name__ = "Integer32"
_ZxAnPowerInCurrentThresh_Object = MibTableColumn
zxAnPowerInCurrentThresh = _ZxAnPowerInCurrentThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 3, 11, 1, 7),
    _ZxAnPowerInCurrentThresh_Type()
)
zxAnPowerInCurrentThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPowerInCurrentThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPowerInCurrentThresh.setUnits("Amp")
_ZxAnEnvFanObjects_ObjectIdentity = ObjectIdentity
zxAnEnvFanObjects = _ZxAnEnvFanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4)
)
_ZxAnEnvFanTrayTable_Object = MibTable
zxAnEnvFanTrayTable = _ZxAnEnvFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10)
)
if mibBuilder.loadTexts:
    zxAnEnvFanTrayTable.setStatus("current")
_ZxAnEnvFanTrayEntry_Object = MibTableRow
zxAnEnvFanTrayEntry = _ZxAnEnvFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1)
)
zxAnEnvFanTrayEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
)
if mibBuilder.loadTexts:
    zxAnEnvFanTrayEntry.setStatus("current")


class _ZxAnFanTrayAlarmBeepEnable_Type(Integer32):
    """Custom type zxAnFanTrayAlarmBeepEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnFanTrayAlarmBeepEnable_Type.__name__ = "Integer32"
_ZxAnFanTrayAlarmBeepEnable_Object = MibTableColumn
zxAnFanTrayAlarmBeepEnable = _ZxAnFanTrayAlarmBeepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 1),
    _ZxAnFanTrayAlarmBeepEnable_Type()
)
zxAnFanTrayAlarmBeepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayAlarmBeepEnable.setStatus("current")


class _ZxAnFanTrayAutoSwitchByCardUp_Type(Integer32):
    """Custom type zxAnFanTrayAutoSwitchByCardUp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnFanTrayAutoSwitchByCardUp_Type.__name__ = "Integer32"
_ZxAnFanTrayAutoSwitchByCardUp_Object = MibTableColumn
zxAnFanTrayAutoSwitchByCardUp = _ZxAnFanTrayAutoSwitchByCardUp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 2),
    _ZxAnFanTrayAutoSwitchByCardUp_Type()
)
zxAnFanTrayAutoSwitchByCardUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayAutoSwitchByCardUp.setStatus("current")
_ZxAnFanTrayHardwareVersion_Type = DisplayString
_ZxAnFanTrayHardwareVersion_Object = MibTableColumn
zxAnFanTrayHardwareVersion = _ZxAnFanTrayHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 3),
    _ZxAnFanTrayHardwareVersion_Type()
)
zxAnFanTrayHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanTrayHardwareVersion.setStatus("current")
_ZxAnFanTraySoftwareVersion_Type = DisplayString
_ZxAnFanTraySoftwareVersion_Object = MibTableColumn
zxAnFanTraySoftwareVersion = _ZxAnFanTraySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 4),
    _ZxAnFanTraySoftwareVersion_Type()
)
zxAnFanTraySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanTraySoftwareVersion.setStatus("current")


class _ZxAnFanTraySpeedCtrlMode_Type(Integer32):
    """Custom type zxAnFanTraySpeedCtrlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temperatureBasedAutoCtrl", 1),
          ("fixSpeed", 2))
    )


_ZxAnFanTraySpeedCtrlMode_Type.__name__ = "Integer32"
_ZxAnFanTraySpeedCtrlMode_Object = MibTableColumn
zxAnFanTraySpeedCtrlMode = _ZxAnFanTraySpeedCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 5),
    _ZxAnFanTraySpeedCtrlMode_Type()
)
zxAnFanTraySpeedCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTraySpeedCtrlMode.setStatus("current")
_ZxAnFanTrayLowSpeed_Type = Integer32
_ZxAnFanTrayLowSpeed_Object = MibTableColumn
zxAnFanTrayLowSpeed = _ZxAnFanTrayLowSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 6),
    _ZxAnFanTrayLowSpeed_Type()
)
zxAnFanTrayLowSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayLowSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayLowSpeed.setUnits("RPM")
_ZxAnFanTrayStdSpeed_Type = Integer32
_ZxAnFanTrayStdSpeed_Object = MibTableColumn
zxAnFanTrayStdSpeed = _ZxAnFanTrayStdSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 7),
    _ZxAnFanTrayStdSpeed_Type()
)
zxAnFanTrayStdSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayStdSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayStdSpeed.setUnits("RPM")
_ZxAnFanTrayHighSpeed_Type = Integer32
_ZxAnFanTrayHighSpeed_Object = MibTableColumn
zxAnFanTrayHighSpeed = _ZxAnFanTrayHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 8),
    _ZxAnFanTrayHighSpeed_Type()
)
zxAnFanTrayHighSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayHighSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayHighSpeed.setUnits("RPM")
_ZxAnFanTraySuperSpeed_Type = Integer32
_ZxAnFanTraySuperSpeed_Object = MibTableColumn
zxAnFanTraySuperSpeed = _ZxAnFanTraySuperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 9),
    _ZxAnFanTraySuperSpeed_Type()
)
zxAnFanTraySuperSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTraySuperSpeed.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTraySuperSpeed.setUnits("RPM")


class _ZxAnFanTrayLowSpeedShiftTemp_Type(Integer32):
    """Custom type zxAnFanTrayLowSpeedShiftTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 55),
    )


_ZxAnFanTrayLowSpeedShiftTemp_Type.__name__ = "Integer32"
_ZxAnFanTrayLowSpeedShiftTemp_Object = MibTableColumn
zxAnFanTrayLowSpeedShiftTemp = _ZxAnFanTrayLowSpeedShiftTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 10),
    _ZxAnFanTrayLowSpeedShiftTemp_Type()
)
zxAnFanTrayLowSpeedShiftTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayLowSpeedShiftTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayLowSpeedShiftTemp.setUnits("centigrade")


class _ZxAnFanTrayStdSpeedShiftTemp_Type(Integer32):
    """Custom type zxAnFanTrayStdSpeedShiftTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_ZxAnFanTrayStdSpeedShiftTemp_Type.__name__ = "Integer32"
_ZxAnFanTrayStdSpeedShiftTemp_Object = MibTableColumn
zxAnFanTrayStdSpeedShiftTemp = _ZxAnFanTrayStdSpeedShiftTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 11),
    _ZxAnFanTrayStdSpeedShiftTemp_Type()
)
zxAnFanTrayStdSpeedShiftTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayStdSpeedShiftTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayStdSpeedShiftTemp.setUnits("centigrade")


class _ZxAnFanTrayHighSpeedShiftTemp_Type(Integer32):
    """Custom type zxAnFanTrayHighSpeedShiftTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65),
    )


_ZxAnFanTrayHighSpeedShiftTemp_Type.__name__ = "Integer32"
_ZxAnFanTrayHighSpeedShiftTemp_Object = MibTableColumn
zxAnFanTrayHighSpeedShiftTemp = _ZxAnFanTrayHighSpeedShiftTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 12),
    _ZxAnFanTrayHighSpeedShiftTemp_Type()
)
zxAnFanTrayHighSpeedShiftTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayHighSpeedShiftTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayHighSpeedShiftTemp.setUnits("centigrade")


class _ZxAnFanTraySuperSpeedShiftTemp_Type(Integer32):
    """Custom type zxAnFanTraySuperSpeedShiftTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 70),
    )


_ZxAnFanTraySuperSpeedShiftTemp_Type.__name__ = "Integer32"
_ZxAnFanTraySuperSpeedShiftTemp_Object = MibTableColumn
zxAnFanTraySuperSpeedShiftTemp = _ZxAnFanTraySuperSpeedShiftTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 13),
    _ZxAnFanTraySuperSpeedShiftTemp_Type()
)
zxAnFanTraySuperSpeedShiftTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTraySuperSpeedShiftTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTraySuperSpeedShiftTemp.setUnits("centigrade")


class _ZxAnFanTrayLowSpeedPercent_Type(Integer32):
    """Custom type zxAnFanTrayLowSpeedPercent based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 97),
    )


_ZxAnFanTrayLowSpeedPercent_Type.__name__ = "Integer32"
_ZxAnFanTrayLowSpeedPercent_Object = MibTableColumn
zxAnFanTrayLowSpeedPercent = _ZxAnFanTrayLowSpeedPercent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 14),
    _ZxAnFanTrayLowSpeedPercent_Type()
)
zxAnFanTrayLowSpeedPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayLowSpeedPercent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayLowSpeedPercent.setUnits("percent")


class _ZxAnFanTrayStdSpeedPercent_Type(Integer32):
    """Custom type zxAnFanTrayStdSpeedPercent based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(11, 98),
    )


_ZxAnFanTrayStdSpeedPercent_Type.__name__ = "Integer32"
_ZxAnFanTrayStdSpeedPercent_Object = MibTableColumn
zxAnFanTrayStdSpeedPercent = _ZxAnFanTrayStdSpeedPercent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 15),
    _ZxAnFanTrayStdSpeedPercent_Type()
)
zxAnFanTrayStdSpeedPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayStdSpeedPercent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayStdSpeedPercent.setUnits("percent")


class _ZxAnFanTrayHighSpeedPercent_Type(Integer32):
    """Custom type zxAnFanTrayHighSpeedPercent based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 99),
    )


_ZxAnFanTrayHighSpeedPercent_Type.__name__ = "Integer32"
_ZxAnFanTrayHighSpeedPercent_Object = MibTableColumn
zxAnFanTrayHighSpeedPercent = _ZxAnFanTrayHighSpeedPercent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 16),
    _ZxAnFanTrayHighSpeedPercent_Type()
)
zxAnFanTrayHighSpeedPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayHighSpeedPercent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayHighSpeedPercent.setUnits("percent")


class _ZxAnFanTraySuperSpeedPercent_Type(Integer32):
    """Custom type zxAnFanTraySuperSpeedPercent based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(13, 100),
    )


_ZxAnFanTraySuperSpeedPercent_Type.__name__ = "Integer32"
_ZxAnFanTraySuperSpeedPercent_Object = MibTableColumn
zxAnFanTraySuperSpeedPercent = _ZxAnFanTraySuperSpeedPercent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 17),
    _ZxAnFanTraySuperSpeedPercent_Type()
)
zxAnFanTraySuperSpeedPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTraySuperSpeedPercent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTraySuperSpeedPercent.setUnits("percent")


class _ZxAnFanTrayAdminStatus_Type(Integer32):
    """Custom type zxAnFanTrayAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnFanTrayAdminStatus_Type.__name__ = "Integer32"
_ZxAnFanTrayAdminStatus_Object = MibTableColumn
zxAnFanTrayAdminStatus = _ZxAnFanTrayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 18),
    _ZxAnFanTrayAdminStatus_Type()
)
zxAnFanTrayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayAdminStatus.setStatus("current")


class _ZxAnFanTrayConfSpeedLevel_Type(Integer32):
    """Custom type zxAnFanTrayConfSpeedLevel based on Integer32"""
    defaultValue = 2

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
        *(("lowSpeed", 1),
          ("standardSpeed", 2),
          ("highSpeed", 3),
          ("superSpeed", 4))
    )


_ZxAnFanTrayConfSpeedLevel_Type.__name__ = "Integer32"
_ZxAnFanTrayConfSpeedLevel_Object = MibTableColumn
zxAnFanTrayConfSpeedLevel = _ZxAnFanTrayConfSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 19),
    _ZxAnFanTrayConfSpeedLevel_Type()
)
zxAnFanTrayConfSpeedLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTrayConfSpeedLevel.setStatus("current")
_ZxAnFanTrayPowerConsumption_Type = Integer32
_ZxAnFanTrayPowerConsumption_Object = MibTableColumn
zxAnFanTrayPowerConsumption = _ZxAnFanTrayPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 20),
    _ZxAnFanTrayPowerConsumption_Type()
)
zxAnFanTrayPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanTrayPowerConsumption.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayPowerConsumption.setUnits("0.001W")


class _ZxAnFanTraySn_Type(DisplayString):
    """Custom type zxAnFanTraySn based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ZxAnFanTraySn_Type.__name__ = "DisplayString"
_ZxAnFanTraySn_Object = MibTableColumn
zxAnFanTraySn = _ZxAnFanTraySn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 21),
    _ZxAnFanTraySn_Type()
)
zxAnFanTraySn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFanTraySn.setStatus("current")
_ZxAnFanTrayVoltage_Type = Integer32
_ZxAnFanTrayVoltage_Object = MibTableColumn
zxAnFanTrayVoltage = _ZxAnFanTrayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 22),
    _ZxAnFanTrayVoltage_Type()
)
zxAnFanTrayVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanTrayVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayVoltage.setUnits("0.001Volts")
_ZxAnFanTrayCurrent_Type = Integer32
_ZxAnFanTrayCurrent_Object = MibTableColumn
zxAnFanTrayCurrent = _ZxAnFanTrayCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 23),
    _ZxAnFanTrayCurrent_Type()
)
zxAnFanTrayCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanTrayCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayCurrent.setUnits("0.001Amp")
_ZxAnFanTrayTemp_Type = Integer32
_ZxAnFanTrayTemp_Object = MibTableColumn
zxAnFanTrayTemp = _ZxAnFanTrayTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 10, 1, 24),
    _ZxAnFanTrayTemp_Type()
)
zxAnFanTrayTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnFanTrayTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnFanTrayTemp.setUnits("Centigrade")
_ZxAnEnvFanTable_Object = MibTable
zxAnEnvFanTable = _ZxAnEnvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11)
)
if mibBuilder.loadTexts:
    zxAnEnvFanTable.setStatus("current")
_ZxAnEnvFanEntry_Object = MibTableRow
zxAnEnvFanEntry = _ZxAnEnvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11, 1)
)
zxAnEnvFanEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvRack"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvShelf"),
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvFanIndex"),
)
if mibBuilder.loadTexts:
    zxAnEnvFanEntry.setStatus("current")
_ZxAnEnvFanIndex_Type = Integer32
_ZxAnEnvFanIndex_Object = MibTableColumn
zxAnEnvFanIndex = _ZxAnEnvFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11, 1, 1),
    _ZxAnEnvFanIndex_Type()
)
zxAnEnvFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvFanIndex.setStatus("current")


class _ZxAnEnvFanConfSpeedLevel_Type(Integer32):
    """Custom type zxAnEnvFanConfSpeedLevel based on Integer32"""
    defaultValue = 2

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
        *(("lowSpeed", 1),
          ("standardSpeed", 2),
          ("highSpeed", 3),
          ("superSpeed", 4))
    )


_ZxAnEnvFanConfSpeedLevel_Type.__name__ = "Integer32"
_ZxAnEnvFanConfSpeedLevel_Object = MibTableColumn
zxAnEnvFanConfSpeedLevel = _ZxAnEnvFanConfSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11, 1, 2),
    _ZxAnEnvFanConfSpeedLevel_Type()
)
zxAnEnvFanConfSpeedLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanConfSpeedLevel.setStatus("current")


class _ZxAnEnvFanActualSpeedLevel_Type(Integer32):
    """Custom type zxAnEnvFanActualSpeedLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("lowSpeed", 1),
          ("standardSpeed", 2),
          ("highSpeed", 3),
          ("superSpeed", 4),
          ("other", 10))
    )


_ZxAnEnvFanActualSpeedLevel_Type.__name__ = "Integer32"
_ZxAnEnvFanActualSpeedLevel_Object = MibTableColumn
zxAnEnvFanActualSpeedLevel = _ZxAnEnvFanActualSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11, 1, 3),
    _ZxAnEnvFanActualSpeedLevel_Type()
)
zxAnEnvFanActualSpeedLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanActualSpeedLevel.setStatus("current")


class _ZxAnEnvFanAdminStatus_Type(Integer32):
    """Custom type zxAnEnvFanAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnEnvFanAdminStatus_Type.__name__ = "Integer32"
_ZxAnEnvFanAdminStatus_Object = MibTableColumn
zxAnEnvFanAdminStatus = _ZxAnEnvFanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11, 1, 4),
    _ZxAnEnvFanAdminStatus_Type()
)
zxAnEnvFanAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanAdminStatus.setStatus("current")


class _ZxAnEnvFanOperStatus_Type(Integer32):
    """Custom type zxAnEnvFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_ZxAnEnvFanOperStatus_Type.__name__ = "Integer32"
_ZxAnEnvFanOperStatus_Object = MibTableColumn
zxAnEnvFanOperStatus = _ZxAnEnvFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11, 1, 5),
    _ZxAnEnvFanOperStatus_Type()
)
zxAnEnvFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanOperStatus.setStatus("current")


class _ZxAnEnvFanOnlineStatus_Type(Integer32):
    """Custom type zxAnEnvFanOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("unknown", 3))
    )


_ZxAnEnvFanOnlineStatus_Type.__name__ = "Integer32"
_ZxAnEnvFanOnlineStatus_Object = MibTableColumn
zxAnEnvFanOnlineStatus = _ZxAnEnvFanOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11, 1, 6),
    _ZxAnEnvFanOnlineStatus_Type()
)
zxAnEnvFanOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanOnlineStatus.setStatus("current")
_ZxAnEnvFanActualSpeed_Type = Integer32
_ZxAnEnvFanActualSpeed_Object = MibTableColumn
zxAnEnvFanActualSpeed = _ZxAnEnvFanActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 11, 1, 7),
    _ZxAnEnvFanActualSpeed_Type()
)
zxAnEnvFanActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvFanActualSpeed.setStatus("current")
_ZxAnEnvFanTrayResetObjects_ObjectIdentity = ObjectIdentity
zxAnEnvFanTrayResetObjects = _ZxAnEnvFanTrayResetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 12)
)
_ZxAnEnvFanTrayResetRack_Type = Integer32
_ZxAnEnvFanTrayResetRack_Object = MibScalar
zxAnEnvFanTrayResetRack = _ZxAnEnvFanTrayResetRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 12, 1),
    _ZxAnEnvFanTrayResetRack_Type()
)
zxAnEnvFanTrayResetRack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanTrayResetRack.setStatus("current")


class _ZxAnEnvFanTrayResetShelfList_Type(DisplayString):
    """Custom type zxAnEnvFanTrayResetShelfList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ZxAnEnvFanTrayResetShelfList_Type.__name__ = "DisplayString"
_ZxAnEnvFanTrayResetShelfList_Object = MibScalar
zxAnEnvFanTrayResetShelfList = _ZxAnEnvFanTrayResetShelfList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 12, 2),
    _ZxAnEnvFanTrayResetShelfList_Type()
)
zxAnEnvFanTrayResetShelfList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanTrayResetShelfList.setStatus("current")


class _ZxAnEnvFanTrayResetAction_Type(Integer32):
    """Custom type zxAnEnvFanTrayResetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZxAnEnvFanTrayResetAction_Type.__name__ = "Integer32"
_ZxAnEnvFanTrayResetAction_Object = MibScalar
zxAnEnvFanTrayResetAction = _ZxAnEnvFanTrayResetAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 4, 12, 3),
    _ZxAnEnvFanTrayResetAction_Type()
)
zxAnEnvFanTrayResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvFanTrayResetAction.setStatus("current")
_ZxAnEnvDeviceObjects_ObjectIdentity = ObjectIdentity
zxAnEnvDeviceObjects = _ZxAnEnvDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5)
)
_ZxAnEnvDeviceTable_Object = MibTable
zxAnEnvDeviceTable = _ZxAnEnvDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 2)
)
if mibBuilder.loadTexts:
    zxAnEnvDeviceTable.setStatus("current")
_ZxAnEnvDeviceEntry_Object = MibTableRow
zxAnEnvDeviceEntry = _ZxAnEnvDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 2, 1)
)
zxAnEnvDeviceEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvDeviceId"),
)
if mibBuilder.loadTexts:
    zxAnEnvDeviceEntry.setStatus("current")


class _ZxAnEnvDeviceId_Type(Integer32):
    """Custom type zxAnEnvDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnEnvDeviceId_Type.__name__ = "Integer32"
_ZxAnEnvDeviceId_Object = MibTableColumn
zxAnEnvDeviceId = _ZxAnEnvDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 2, 1, 1),
    _ZxAnEnvDeviceId_Type()
)
zxAnEnvDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvDeviceId.setStatus("current")


class _ZxAnEnvDeviceName_Type(DisplayString):
    """Custom type zxAnEnvDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEnvDeviceName_Type.__name__ = "DisplayString"
_ZxAnEnvDeviceName_Object = MibTableColumn
zxAnEnvDeviceName = _ZxAnEnvDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 2, 1, 2),
    _ZxAnEnvDeviceName_Type()
)
zxAnEnvDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEnvDeviceName.setStatus("current")
_ZxAnEnvDeviceRowStatus_Type = RowStatus
_ZxAnEnvDeviceRowStatus_Object = MibTableColumn
zxAnEnvDeviceRowStatus = _ZxAnEnvDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 2, 1, 50),
    _ZxAnEnvDeviceRowStatus_Type()
)
zxAnEnvDeviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEnvDeviceRowStatus.setStatus("current")
_ZxAnEnvDevMonSwitchTable_Object = MibTable
zxAnEnvDevMonSwitchTable = _ZxAnEnvDevMonSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 3)
)
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchTable.setStatus("current")
_ZxAnEnvDevMonSwitchEntry_Object = MibTableRow
zxAnEnvDevMonSwitchEntry = _ZxAnEnvDevMonSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 3, 1)
)
zxAnEnvDevMonSwitchEntry.setIndexNames(
    (0, "ZTE-AN-ENVMON-MIB", "zxAnEnvDevMonSwitchId"),
)
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchEntry.setStatus("current")


class _ZxAnEnvDevMonSwitchId_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnEnvDevMonSwitchId_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchId_Object = MibTableColumn
zxAnEnvDevMonSwitchId = _ZxAnEnvDevMonSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 3, 1, 1),
    _ZxAnEnvDevMonSwitchId_Type()
)
zxAnEnvDevMonSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchId.setStatus("current")


class _ZxAnEnvDevMonSwitchDeviceId_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchDeviceId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEnvDevMonSwitchDeviceId_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchDeviceId_Object = MibTableColumn
zxAnEnvDevMonSwitchDeviceId = _ZxAnEnvDevMonSwitchDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 3, 1, 2),
    _ZxAnEnvDevMonSwitchDeviceId_Type()
)
zxAnEnvDevMonSwitchDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchDeviceId.setStatus("current")


class _ZxAnEnvDevMonSwitchTrapEnable_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchTrapEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnEnvDevMonSwitchTrapEnable_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchTrapEnable_Object = MibTableColumn
zxAnEnvDevMonSwitchTrapEnable = _ZxAnEnvDevMonSwitchTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 3, 1, 3),
    _ZxAnEnvDevMonSwitchTrapEnable_Type()
)
zxAnEnvDevMonSwitchTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchTrapEnable.setStatus("current")


class _ZxAnEnvDevMonSwitchNormalStatus_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchNormalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowLevel", 1),
          ("highLevel", 2))
    )


_ZxAnEnvDevMonSwitchNormalStatus_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchNormalStatus_Object = MibTableColumn
zxAnEnvDevMonSwitchNormalStatus = _ZxAnEnvDevMonSwitchNormalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 3, 1, 4),
    _ZxAnEnvDevMonSwitchNormalStatus_Type()
)
zxAnEnvDevMonSwitchNormalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchNormalStatus.setStatus("current")


class _ZxAnEnvDevMonSwitchCurrStatus_Type(Integer32):
    """Custom type zxAnEnvDevMonSwitchCurrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("lowLevel", 1),
          ("highLevel", 2),
          ("unknown", 255))
    )


_ZxAnEnvDevMonSwitchCurrStatus_Type.__name__ = "Integer32"
_ZxAnEnvDevMonSwitchCurrStatus_Object = MibTableColumn
zxAnEnvDevMonSwitchCurrStatus = _ZxAnEnvDevMonSwitchCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 2, 5, 3, 1, 5),
    _ZxAnEnvDevMonSwitchCurrStatus_Type()
)
zxAnEnvDevMonSwitchCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEnvDevMonSwitchCurrStatus.setStatus("current")
_ZxAnEnvMonNotifications_ObjectIdentity = ObjectIdentity
zxAnEnvMonNotifications = _ZxAnEnvMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3)
)
_ZxAnEnvMonTempTraps_ObjectIdentity = ObjectIdentity
zxAnEnvMonTempTraps = _ZxAnEnvMonTempTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1)
)
_ZxAnEnvMonInterfaceTraps_ObjectIdentity = ObjectIdentity
zxAnEnvMonInterfaceTraps = _ZxAnEnvMonInterfaceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 2)
)
_ZxAnEnvMonPowerSupplyTraps_ObjectIdentity = ObjectIdentity
zxAnEnvMonPowerSupplyTraps = _ZxAnEnvMonPowerSupplyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3)
)
_ZxAnEnvMonFanTraps_ObjectIdentity = ObjectIdentity
zxAnEnvMonFanTraps = _ZxAnEnvMonFanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 4)
)
_ZxAnEnvDeviceTraps_ObjectIdentity = ObjectIdentity
zxAnEnvDeviceTraps = _ZxAnEnvDeviceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 5)
)
_ZxAnEnvMonConformance_ObjectIdentity = ObjectIdentity
zxAnEnvMonConformance = _ZxAnEnvMonConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4)
)
_ZxAnEnvMonCompliances_ObjectIdentity = ObjectIdentity
zxAnEnvMonCompliances = _ZxAnEnvMonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 1)
)
_ZxAnEnvMonGroups_ObjectIdentity = ObjectIdentity
zxAnEnvMonGroups = _ZxAnEnvMonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2)
)

# Managed Objects groups

zxAnEnvMonCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2, 1)
)
zxAnEnvMonCapabilitiesGroup.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnEnvMonCapabilities")
)
if mibBuilder.loadTexts:
    zxAnEnvMonCapabilitiesGroup.setStatus("current")

zxAnEnvTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2, 2)
)
zxAnEnvTempGroup.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempHighAlmThreshold"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempCriticalAlmThreshold"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempLowAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvTempGroup.setStatus("current")

zxAnEnvCardTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2, 3)
)
zxAnEnvCardTempGroup.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnCardTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvHis15MinTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvHis1DayTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvRiseAlmThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvClrRiseAlmThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvRiseWarnThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvClrRiseWarnThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvFallWarnThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvClrFallWarnThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvFallAlmThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvClrFallAlmThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvAlmPrfConfRowStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvAlmPrf"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvAlmPrfApplyRowStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardEnvAlmPrfRowStatus"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardTempGroup.setStatus("current")

zxAnEnvInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2, 4)
)
zxAnEnvInterfaceGroup.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvMonInterfaceUsage"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvEpmConnectPort"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvBackplaneInterfaceUsage"))
)
if mibBuilder.loadTexts:
    zxAnEnvInterfaceGroup.setStatus("current")

zxAnEnvPowerSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2, 5)
)
zxAnEnvPowerSupplyGroup.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyMaxPowerNum"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyOperStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInVoltageStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerInVoltageUpperThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerInVoltageLowerThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInCurrent"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerInCurrentThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerSupplyGroup.setStatus("current")

zxAnEnvFanTrayTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2, 6)
)
zxAnEnvFanTrayTableGroup.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnFanTrayAlarmBeepEnable"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayAutoSwitchByCardUp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayHardwareVersion"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTraySoftwareVersion"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTraySpeedCtrlMode"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayLowSpeed"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayStdSpeed"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayHighSpeed"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTraySuperSpeed"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayLowSpeedShiftTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayStdSpeedShiftTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayHighSpeedShiftTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTraySuperSpeedShiftTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayLowSpeedPercent"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayStdSpeedPercent"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTrayHighSpeedPercent"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTraySuperSpeedPercent"),
        ("ZTE-AN-ENVMON-MIB", "zxAnFanTraySn"))
)
if mibBuilder.loadTexts:
    zxAnEnvFanTrayTableGroup.setStatus("current")

zxAnEnvFanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2, 7)
)
zxAnEnvFanTableGroup.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvFanConfSpeedLevel"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanActualSpeedLevel"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanAdminStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanOperStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanOnlineStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanActualSpeed"))
)
if mibBuilder.loadTexts:
    zxAnEnvFanTableGroup.setStatus("current")

zxAnEnvMonNotificationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 2, 8)
)
zxAnEnvMonNotificationsGroup.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvHighTempAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvHighTempClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvMonitorInterfaceLinkDown"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvMonitorInterfaceLinkUp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanLinkDown"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanLinkUp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempSensorFailure"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanFailureAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanFailureClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerSupplyModuleDown"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerSupplyModuleUp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanTrayLinkDown"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanTrayLinkUp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerOverVoltageAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerOverVoltageClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerUnderVoltageAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerUnderVoltageClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerOff"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerOn"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvACPowerDownAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvACPowerDownClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvNoBatteryAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvNoBatteryClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvBatteryUnderVoltageAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvBatteryUnderVoltageClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvCardShutdownAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvCardShutdownClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvCriticalTempAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvCriticalTempClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvLowTempAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvLowTempClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvOptNearCriticalTempAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvOptNearCriticalTempClr"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvHeatRadiationAbnormalAlm"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvHeatRadiationAbnormalClr"))
)
if mibBuilder.loadTexts:
    zxAnEnvMonNotificationsGroup.setStatus("current")


# Notification objects

zxAnEnvHighTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 1)
)
zxAnEnvHighTempAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempHighAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvHighTempAlm.setStatus(
        "current"
    )

zxAnEnvHighTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 2)
)
zxAnEnvHighTempClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempHighAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvHighTempClr.setStatus(
        "current"
    )

zxAnEnvTempSensorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnEnvTempSensorFailure.setStatus(
        "current"
    )

zxAnEnvCriticalTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 6)
)
zxAnEnvCriticalTempAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempCriticalAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCriticalTempAlm.setStatus(
        "current"
    )

zxAnEnvCriticalTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 7)
)
zxAnEnvCriticalTempClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempCriticalAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCriticalTempClr.setStatus(
        "current"
    )

zxAnEnvLowTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 8)
)
zxAnEnvLowTempAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempLowAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvLowTempAlm.setStatus(
        "current"
    )

zxAnEnvLowTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 9)
)
zxAnEnvLowTempClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempLowAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvLowTempClr.setStatus(
        "current"
    )

zxAnEnvCardShutdownAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 30)
)
zxAnEnvCardShutdownAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvCardShutdownReason"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvEmergencyBatteryVoltage"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvEmergencyBatteryThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardShutdownAlm.setStatus(
        "current"
    )

zxAnEnvCardShutdownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 31)
)
zxAnEnvCardShutdownClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvCardShutdownReason"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvEmergencyBatteryVoltage"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvEmergencyBatteryThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardShutdownClr.setStatus(
        "current"
    )

zxAnEnvTemperatureAbnormalAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 32)
)
if mibBuilder.loadTexts:
    zxAnEnvTemperatureAbnormalAlm.setStatus(
        "current"
    )

zxAnEnvTemperatureAbnormalClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 33)
)
if mibBuilder.loadTexts:
    zxAnEnvTemperatureAbnormalClr.setStatus(
        "current"
    )

zxAnEnvNearCriticalTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 34)
)
zxAnEnvNearCriticalTempAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempCriticalAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvNearCriticalTempAlm.setStatus(
        "current"
    )

zxAnEnvNearCriticalTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 35)
)
zxAnEnvNearCriticalTempClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempCriticalAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvNearCriticalTempClr.setStatus(
        "current"
    )

zxAnEnvCardNearCriticalTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 36)
)
zxAnEnvCardNearCriticalTempAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnCardTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardCriticalTempAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardNearCriticalTempAlm.setStatus(
        "current"
    )

zxAnEnvCardNearCriticalTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 37)
)
zxAnEnvCardNearCriticalTempClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnCardTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardCriticalTempAlmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnEnvCardNearCriticalTempClr.setStatus(
        "current"
    )

zxAnEnvOptNearCriticalTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 38)
)
zxAnEnvOptNearCriticalTempAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnCardOptHighestTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardOptCriticalTempAlmThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardOptHighestTempPortNo"))
)
if mibBuilder.loadTexts:
    zxAnEnvOptNearCriticalTempAlm.setStatus(
        "current"
    )

zxAnEnvOptNearCriticalTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 39)
)
zxAnEnvOptNearCriticalTempClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnCardOptHighestTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardOptCriticalTempAlmThresh"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardOptHighestTempPortNo"))
)
if mibBuilder.loadTexts:
    zxAnEnvOptNearCriticalTempClr.setStatus(
        "current"
    )

zxAnEnvHeatRadiationAbnormalAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 40)
)
zxAnEnvHeatRadiationAbnormalAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardHeatRadiationAlmThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvHeatRadiationAbnormalAlm.setStatus(
        "current"
    )

zxAnEnvHeatRadiationAbnormalClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 1, 41)
)
zxAnEnvHeatRadiationAbnormalClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardTemp"),
        ("ZTE-AN-ENVMON-MIB", "zxAnCardHeatRadiationAlmThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvHeatRadiationAbnormalClr.setStatus(
        "current"
    )

zxAnEnvMonitorInterfaceLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnEnvMonitorInterfaceLinkDown.setStatus(
        "current"
    )

zxAnEnvMonitorInterfaceLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnEnvMonitorInterfaceLinkUp.setStatus(
        "current"
    )

zxAnEnvPowerSupplyModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 1)
)
zxAnEnvPowerSupplyModuleDown.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyOperStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvPowerSupplyModuleDown.setStatus(
        "current"
    )

zxAnEnvPowerSupplyModuleUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 2)
)
zxAnEnvPowerSupplyModuleUp.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyOperStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvPowerSupplyModuleUp.setStatus(
        "current"
    )

zxAnEnvPowerOverVoltageAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 3)
)
zxAnEnvPowerOverVoltageAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerInVoltageUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerOverVoltageAlm.setStatus(
        "current"
    )

zxAnEnvPowerOverVoltageClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 4)
)
zxAnEnvPowerOverVoltageClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerInVoltageUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerOverVoltageClr.setStatus(
        "current"
    )

zxAnEnvPowerUnderVoltageAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 5)
)
zxAnEnvPowerUnderVoltageAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerInVoltageLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerUnderVoltageAlm.setStatus(
        "current"
    )

zxAnEnvPowerUnderVoltageClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 6)
)
zxAnEnvPowerUnderVoltageClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInVoltage"),
        ("ZTE-AN-ENVMON-MIB", "zxAnPowerInVoltageLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnEnvPowerUnderVoltageClr.setStatus(
        "current"
    )

zxAnEnvPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 7)
)
zxAnEnvPowerOff.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInVoltageStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvPowerOff.setStatus(
        "current"
    )

zxAnEnvPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 8)
)
zxAnEnvPowerOn.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnPowerSupplyInVoltageStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvPowerOn.setStatus(
        "current"
    )

zxAnEnvEmergencyPowerSaveAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 9)
)
if mibBuilder.loadTexts:
    zxAnEnvEmergencyPowerSaveAlm.setStatus(
        "current"
    )

zxAnEnvEmergencyPowerSaveClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 10)
)
if mibBuilder.loadTexts:
    zxAnEnvEmergencyPowerSaveClr.setStatus(
        "current"
    )

zxAnEnvACPowerDownAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 11)
)
if mibBuilder.loadTexts:
    zxAnEnvACPowerDownAlm.setStatus(
        "current"
    )

zxAnEnvACPowerDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 12)
)
if mibBuilder.loadTexts:
    zxAnEnvACPowerDownClr.setStatus(
        "current"
    )

zxAnEnvNoBatteryAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 13)
)
if mibBuilder.loadTexts:
    zxAnEnvNoBatteryAlm.setStatus(
        "current"
    )

zxAnEnvNoBatteryClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 14)
)
if mibBuilder.loadTexts:
    zxAnEnvNoBatteryClr.setStatus(
        "current"
    )

zxAnEnvBatteryUnderVoltageAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 15)
)
if mibBuilder.loadTexts:
    zxAnEnvBatteryUnderVoltageAlm.setStatus(
        "current"
    )

zxAnEnvBatteryUnderVoltageClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 3, 16)
)
if mibBuilder.loadTexts:
    zxAnEnvBatteryUnderVoltageClr.setStatus(
        "current"
    )

zxAnEnvFanLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 4, 1)
)
zxAnEnvFanLinkDown.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanOnlineStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvFanLinkDown.setStatus(
        "current"
    )

zxAnEnvFanLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 4, 2)
)
zxAnEnvFanLinkUp.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanOnlineStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvFanLinkUp.setStatus(
        "current"
    )

zxAnEnvFanTrayLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 4, 3)
)
if mibBuilder.loadTexts:
    zxAnEnvFanTrayLinkDown.setStatus(
        "current"
    )

zxAnEnvFanTrayLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 4, 4)
)
if mibBuilder.loadTexts:
    zxAnEnvFanTrayLinkUp.setStatus(
        "current"
    )

zxAnEnvFanFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 4, 5)
)
zxAnEnvFanFailureAlm.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanOperStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvFanFailureAlm.setStatus(
        "current"
    )

zxAnEnvFanFailureClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 4, 6)
)
zxAnEnvFanFailureClr.setObjects(
    ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanOperStatus")
)
if mibBuilder.loadTexts:
    zxAnEnvFanFailureClr.setStatus(
        "current"
    )

zxAnEnvDeviceAbnormalAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 5, 1)
)
zxAnEnvDeviceAbnormalAlm.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvDevMonSwitchDeviceId"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvDevMonSwitchNormalStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvDevMonSwitchCurrStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvDeviceName"))
)
if mibBuilder.loadTexts:
    zxAnEnvDeviceAbnormalAlm.setStatus(
        "current"
    )

zxAnEnvDeviceAbnormalClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 3, 5, 2)
)
zxAnEnvDeviceAbnormalClr.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvDevMonSwitchDeviceId"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvDevMonSwitchNormalStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvDevMonSwitchCurrStatus"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvDeviceName"))
)
if mibBuilder.loadTexts:
    zxAnEnvDeviceAbnormalClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

zxAnEnvMonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3902, 1082, 10, 10, 4, 1, 1)
)
zxAnEnvMonCompliance.setObjects(
      *(("ZTE-AN-ENVMON-MIB", "zxAnEnvMonCapabilitiesGroup"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvTempGroup"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvCardTempGroup"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvInterfaceGroup"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvPowerSupplyGroup"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanTrayTableGroup"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvFanTableGroup"),
        ("ZTE-AN-ENVMON-MIB", "zxAnEnvMonNotificationsGroup"))
)
if mibBuilder.loadTexts:
    zxAnEnvMonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ENVMON-MIB",
    **{"ZxAnEnvShutdownServiceType": ZxAnEnvShutdownServiceType,
       "zxAnEnvMonMib": zxAnEnvMonMib,
       "zxAnEnvMonGlobalObjects": zxAnEnvMonGlobalObjects,
       "zxAnEnvMonCapabilities": zxAnEnvMonCapabilities,
       "zxAnEnvMonObjects": zxAnEnvMonObjects,
       "zxAnEnvParamObjects": zxAnEnvParamObjects,
       "zxAnEnvParamGlobalObjects": zxAnEnvParamGlobalObjects,
       "zxAnEnvCardShutdownReason": zxAnEnvCardShutdownReason,
       "zxAnEnvParamTable": zxAnEnvParamTable,
       "zxAnEnvParamEntry": zxAnEnvParamEntry,
       "zxAnEnvRack": zxAnEnvRack,
       "zxAnEnvShelf": zxAnEnvShelf,
       "zxAnEnvTemp": zxAnEnvTemp,
       "zxAnEnvTempHighAlmThreshold": zxAnEnvTempHighAlmThreshold,
       "zxAnEnvTempCriticalAlmThreshold": zxAnEnvTempCriticalAlmThreshold,
       "zxAnEnvTempLowAlmThreshold": zxAnEnvTempLowAlmThreshold,
       "zxAnEnvShelfPowerConsumption": zxAnEnvShelfPowerConsumption,
       "zxAnEnvShelfVoltage": zxAnEnvShelfVoltage,
       "zxAnEnvShelfCurrent": zxAnEnvShelfCurrent,
       "zxAnCardEnvParamTable": zxAnCardEnvParamTable,
       "zxAnCardEnvParamEntry": zxAnCardEnvParamEntry,
       "zxAnEnvSlot": zxAnEnvSlot,
       "zxAnCardTemp": zxAnCardTemp,
       "zxAnCardPowerConsumption": zxAnCardPowerConsumption,
       "zxAnCardVoltage": zxAnCardVoltage,
       "zxAnCardCurrent": zxAnCardCurrent,
       "zxAnCardCriticalTempAlmThreshold": zxAnCardCriticalTempAlmThreshold,
       "zxAnCardOptHighestTemp": zxAnCardOptHighestTemp,
       "zxAnCardOptCriticalTempAlmThresh": zxAnCardOptCriticalTempAlmThresh,
       "zxAnCardOptHighestTempPortNo": zxAnCardOptHighestTempPortNo,
       "zxAnCardHeatRadiationAlmThresh": zxAnCardHeatRadiationAlmThresh,
       "zxAnCardEnvHis15MinPerfTable": zxAnCardEnvHis15MinPerfTable,
       "zxAnCardEnvHis15MinPerfEntry": zxAnCardEnvHis15MinPerfEntry,
       "zxAnCardEnvHis15MinIntervalNo": zxAnCardEnvHis15MinIntervalNo,
       "zxAnCardEnvHis15MinDateTime": zxAnCardEnvHis15MinDateTime,
       "zxAnCardEnvHis15MinTemp": zxAnCardEnvHis15MinTemp,
       "zxAnCardEnvHis1DayPerfTable": zxAnCardEnvHis1DayPerfTable,
       "zxAnCardEnvHis1DayPerfEntry": zxAnCardEnvHis1DayPerfEntry,
       "zxAnCardEnvHis1DayIntervalNo": zxAnCardEnvHis1DayIntervalNo,
       "zxAnCardEnvHis1DayDateTime": zxAnCardEnvHis1DayDateTime,
       "zxAnCardEnvHis1DayTemp": zxAnCardEnvHis1DayTemp,
       "zxAnCardEnvAlmProfileConfTable": zxAnCardEnvAlmProfileConfTable,
       "zxAnCardEnvAlmProfileConfEntry": zxAnCardEnvAlmProfileConfEntry,
       "zxAnCardEnvAlmProfileName": zxAnCardEnvAlmProfileName,
       "zxAnCardEnvPerfVariable": zxAnCardEnvPerfVariable,
       "zxAnCardEnvRiseAlmThresh": zxAnCardEnvRiseAlmThresh,
       "zxAnCardEnvClrRiseAlmThresh": zxAnCardEnvClrRiseAlmThresh,
       "zxAnCardEnvRiseWarnThresh": zxAnCardEnvRiseWarnThresh,
       "zxAnCardEnvClrRiseWarnThresh": zxAnCardEnvClrRiseWarnThresh,
       "zxAnCardEnvFallWarnThresh": zxAnCardEnvFallWarnThresh,
       "zxAnCardEnvClrFallWarnThresh": zxAnCardEnvClrFallWarnThresh,
       "zxAnCardEnvFallAlmThresh": zxAnCardEnvFallAlmThresh,
       "zxAnCardEnvClrFallAlmThresh": zxAnCardEnvClrFallAlmThresh,
       "zxAnCardEnvAlmPrfConfRowStatus": zxAnCardEnvAlmPrfConfRowStatus,
       "zxAnCardEnvAlmProfileApplyTable": zxAnCardEnvAlmProfileApplyTable,
       "zxAnCardEnvAlmProfileApplyEntry": zxAnCardEnvAlmProfileApplyEntry,
       "zxAnCardEnvAlmPrf": zxAnCardEnvAlmPrf,
       "zxAnCardEnvAlmPrfApplyRowStatus": zxAnCardEnvAlmPrfApplyRowStatus,
       "zxAnCardEnvAlmProfileTable": zxAnCardEnvAlmProfileTable,
       "zxAnCardEnvAlmProfileEntry": zxAnCardEnvAlmProfileEntry,
       "zxAnCardEnvAlmPrfRowStatus": zxAnCardEnvAlmPrfRowStatus,
       "zxAnEnvOverheatProtectTable": zxAnEnvOverheatProtectTable,
       "zxAnEnvOverheatProtectEntry": zxAnEnvOverheatProtectEntry,
       "zxAnEnvOverheatProtectEnable": zxAnEnvOverheatProtectEnable,
       "zxAnEnvOverheatProtectDelay": zxAnEnvOverheatProtectDelay,
       "zxAnEnvOverheatProtectFirstStep": zxAnEnvOverheatProtectFirstStep,
       "zxAnEnvOverheatProtectSecondStep": zxAnEnvOverheatProtectSecondStep,
       "zxAnEnvCardOverheatProtectTable": zxAnEnvCardOverheatProtectTable,
       "zxAnEnvCardOverheatProtectEntry": zxAnEnvCardOverheatProtectEntry,
       "zxAnEnvCardCriticalTempProtectEn": zxAnEnvCardCriticalTempProtectEn,
       "zxAnEnvMonInterfaceObjects": zxAnEnvMonInterfaceObjects,
       "zxAnEnvMonInterfaceTable": zxAnEnvMonInterfaceTable,
       "zxAnEnvMonInterfaceEntry": zxAnEnvMonInterfaceEntry,
       "zxAnEnvMonInterfaceUsage": zxAnEnvMonInterfaceUsage,
       "zxAnEnvEpmConnectPort": zxAnEnvEpmConnectPort,
       "zxAnEnvBackplaneInterfaceUsage": zxAnEnvBackplaneInterfaceUsage,
       "zxAnEnvPowerSupplyObjects": zxAnEnvPowerSupplyObjects,
       "zxAnPowerSupplyGlobalObjects": zxAnPowerSupplyGlobalObjects,
       "zxAnEnvEmergencyPowerSaveEnable": zxAnEnvEmergencyPowerSaveEnable,
       "zxAnEnvEmergencyPowerSaveDelay": zxAnEnvEmergencyPowerSaveDelay,
       "zxAnEnvEmergencyPowerSaveRecover": zxAnEnvEmergencyPowerSaveRecover,
       "zxAnEnvEmergencyPowerSaveSvcType": zxAnEnvEmergencyPowerSaveSvcType,
       "zxAnEnvPowerMode": zxAnEnvPowerMode,
       "zxAnEnvEmergencyBatteryVoltage": zxAnEnvEmergencyBatteryVoltage,
       "zxAnEnvEmergencyBatteryThreshold": zxAnEnvEmergencyBatteryThreshold,
       "zxAnPowerSupplyCapabilityTable": zxAnPowerSupplyCapabilityTable,
       "zxAnPowerSupplyCapabilityEntry": zxAnPowerSupplyCapabilityEntry,
       "zxAnPowerSupplyMaxPowerNum": zxAnPowerSupplyMaxPowerNum,
       "zxAnPowerSupplyTable": zxAnPowerSupplyTable,
       "zxAnPowerSupplyEntry": zxAnPowerSupplyEntry,
       "zxAnPowerSupplyOperStatus": zxAnPowerSupplyOperStatus,
       "zxAnPowerSupplyInVoltage": zxAnPowerSupplyInVoltage,
       "zxAnPowerSupplyInVoltageStatus": zxAnPowerSupplyInVoltageStatus,
       "zxAnPowerInVoltageUpperThresh": zxAnPowerInVoltageUpperThresh,
       "zxAnPowerInVoltageLowerThresh": zxAnPowerInVoltageLowerThresh,
       "zxAnPowerSupplyInCurrent": zxAnPowerSupplyInCurrent,
       "zxAnPowerInCurrentThresh": zxAnPowerInCurrentThresh,
       "zxAnEnvFanObjects": zxAnEnvFanObjects,
       "zxAnEnvFanTrayTable": zxAnEnvFanTrayTable,
       "zxAnEnvFanTrayEntry": zxAnEnvFanTrayEntry,
       "zxAnFanTrayAlarmBeepEnable": zxAnFanTrayAlarmBeepEnable,
       "zxAnFanTrayAutoSwitchByCardUp": zxAnFanTrayAutoSwitchByCardUp,
       "zxAnFanTrayHardwareVersion": zxAnFanTrayHardwareVersion,
       "zxAnFanTraySoftwareVersion": zxAnFanTraySoftwareVersion,
       "zxAnFanTraySpeedCtrlMode": zxAnFanTraySpeedCtrlMode,
       "zxAnFanTrayLowSpeed": zxAnFanTrayLowSpeed,
       "zxAnFanTrayStdSpeed": zxAnFanTrayStdSpeed,
       "zxAnFanTrayHighSpeed": zxAnFanTrayHighSpeed,
       "zxAnFanTraySuperSpeed": zxAnFanTraySuperSpeed,
       "zxAnFanTrayLowSpeedShiftTemp": zxAnFanTrayLowSpeedShiftTemp,
       "zxAnFanTrayStdSpeedShiftTemp": zxAnFanTrayStdSpeedShiftTemp,
       "zxAnFanTrayHighSpeedShiftTemp": zxAnFanTrayHighSpeedShiftTemp,
       "zxAnFanTraySuperSpeedShiftTemp": zxAnFanTraySuperSpeedShiftTemp,
       "zxAnFanTrayLowSpeedPercent": zxAnFanTrayLowSpeedPercent,
       "zxAnFanTrayStdSpeedPercent": zxAnFanTrayStdSpeedPercent,
       "zxAnFanTrayHighSpeedPercent": zxAnFanTrayHighSpeedPercent,
       "zxAnFanTraySuperSpeedPercent": zxAnFanTraySuperSpeedPercent,
       "zxAnFanTrayAdminStatus": zxAnFanTrayAdminStatus,
       "zxAnFanTrayConfSpeedLevel": zxAnFanTrayConfSpeedLevel,
       "zxAnFanTrayPowerConsumption": zxAnFanTrayPowerConsumption,
       "zxAnFanTraySn": zxAnFanTraySn,
       "zxAnFanTrayVoltage": zxAnFanTrayVoltage,
       "zxAnFanTrayCurrent": zxAnFanTrayCurrent,
       "zxAnFanTrayTemp": zxAnFanTrayTemp,
       "zxAnEnvFanTable": zxAnEnvFanTable,
       "zxAnEnvFanEntry": zxAnEnvFanEntry,
       "zxAnEnvFanIndex": zxAnEnvFanIndex,
       "zxAnEnvFanConfSpeedLevel": zxAnEnvFanConfSpeedLevel,
       "zxAnEnvFanActualSpeedLevel": zxAnEnvFanActualSpeedLevel,
       "zxAnEnvFanAdminStatus": zxAnEnvFanAdminStatus,
       "zxAnEnvFanOperStatus": zxAnEnvFanOperStatus,
       "zxAnEnvFanOnlineStatus": zxAnEnvFanOnlineStatus,
       "zxAnEnvFanActualSpeed": zxAnEnvFanActualSpeed,
       "zxAnEnvFanTrayResetObjects": zxAnEnvFanTrayResetObjects,
       "zxAnEnvFanTrayResetRack": zxAnEnvFanTrayResetRack,
       "zxAnEnvFanTrayResetShelfList": zxAnEnvFanTrayResetShelfList,
       "zxAnEnvFanTrayResetAction": zxAnEnvFanTrayResetAction,
       "zxAnEnvDeviceObjects": zxAnEnvDeviceObjects,
       "zxAnEnvDeviceTable": zxAnEnvDeviceTable,
       "zxAnEnvDeviceEntry": zxAnEnvDeviceEntry,
       "zxAnEnvDeviceId": zxAnEnvDeviceId,
       "zxAnEnvDeviceName": zxAnEnvDeviceName,
       "zxAnEnvDeviceRowStatus": zxAnEnvDeviceRowStatus,
       "zxAnEnvDevMonSwitchTable": zxAnEnvDevMonSwitchTable,
       "zxAnEnvDevMonSwitchEntry": zxAnEnvDevMonSwitchEntry,
       "zxAnEnvDevMonSwitchId": zxAnEnvDevMonSwitchId,
       "zxAnEnvDevMonSwitchDeviceId": zxAnEnvDevMonSwitchDeviceId,
       "zxAnEnvDevMonSwitchTrapEnable": zxAnEnvDevMonSwitchTrapEnable,
       "zxAnEnvDevMonSwitchNormalStatus": zxAnEnvDevMonSwitchNormalStatus,
       "zxAnEnvDevMonSwitchCurrStatus": zxAnEnvDevMonSwitchCurrStatus,
       "zxAnEnvMonNotifications": zxAnEnvMonNotifications,
       "zxAnEnvMonTempTraps": zxAnEnvMonTempTraps,
       "zxAnEnvHighTempAlm": zxAnEnvHighTempAlm,
       "zxAnEnvHighTempClr": zxAnEnvHighTempClr,
       "zxAnEnvTempSensorFailure": zxAnEnvTempSensorFailure,
       "zxAnEnvCriticalTempAlm": zxAnEnvCriticalTempAlm,
       "zxAnEnvCriticalTempClr": zxAnEnvCriticalTempClr,
       "zxAnEnvLowTempAlm": zxAnEnvLowTempAlm,
       "zxAnEnvLowTempClr": zxAnEnvLowTempClr,
       "zxAnEnvCardShutdownAlm": zxAnEnvCardShutdownAlm,
       "zxAnEnvCardShutdownClr": zxAnEnvCardShutdownClr,
       "zxAnEnvTemperatureAbnormalAlm": zxAnEnvTemperatureAbnormalAlm,
       "zxAnEnvTemperatureAbnormalClr": zxAnEnvTemperatureAbnormalClr,
       "zxAnEnvNearCriticalTempAlm": zxAnEnvNearCriticalTempAlm,
       "zxAnEnvNearCriticalTempClr": zxAnEnvNearCriticalTempClr,
       "zxAnEnvCardNearCriticalTempAlm": zxAnEnvCardNearCriticalTempAlm,
       "zxAnEnvCardNearCriticalTempClr": zxAnEnvCardNearCriticalTempClr,
       "zxAnEnvOptNearCriticalTempAlm": zxAnEnvOptNearCriticalTempAlm,
       "zxAnEnvOptNearCriticalTempClr": zxAnEnvOptNearCriticalTempClr,
       "zxAnEnvHeatRadiationAbnormalAlm": zxAnEnvHeatRadiationAbnormalAlm,
       "zxAnEnvHeatRadiationAbnormalClr": zxAnEnvHeatRadiationAbnormalClr,
       "zxAnEnvMonInterfaceTraps": zxAnEnvMonInterfaceTraps,
       "zxAnEnvMonitorInterfaceLinkDown": zxAnEnvMonitorInterfaceLinkDown,
       "zxAnEnvMonitorInterfaceLinkUp": zxAnEnvMonitorInterfaceLinkUp,
       "zxAnEnvMonPowerSupplyTraps": zxAnEnvMonPowerSupplyTraps,
       "zxAnEnvPowerSupplyModuleDown": zxAnEnvPowerSupplyModuleDown,
       "zxAnEnvPowerSupplyModuleUp": zxAnEnvPowerSupplyModuleUp,
       "zxAnEnvPowerOverVoltageAlm": zxAnEnvPowerOverVoltageAlm,
       "zxAnEnvPowerOverVoltageClr": zxAnEnvPowerOverVoltageClr,
       "zxAnEnvPowerUnderVoltageAlm": zxAnEnvPowerUnderVoltageAlm,
       "zxAnEnvPowerUnderVoltageClr": zxAnEnvPowerUnderVoltageClr,
       "zxAnEnvPowerOff": zxAnEnvPowerOff,
       "zxAnEnvPowerOn": zxAnEnvPowerOn,
       "zxAnEnvEmergencyPowerSaveAlm": zxAnEnvEmergencyPowerSaveAlm,
       "zxAnEnvEmergencyPowerSaveClr": zxAnEnvEmergencyPowerSaveClr,
       "zxAnEnvACPowerDownAlm": zxAnEnvACPowerDownAlm,
       "zxAnEnvACPowerDownClr": zxAnEnvACPowerDownClr,
       "zxAnEnvNoBatteryAlm": zxAnEnvNoBatteryAlm,
       "zxAnEnvNoBatteryClr": zxAnEnvNoBatteryClr,
       "zxAnEnvBatteryUnderVoltageAlm": zxAnEnvBatteryUnderVoltageAlm,
       "zxAnEnvBatteryUnderVoltageClr": zxAnEnvBatteryUnderVoltageClr,
       "zxAnEnvMonFanTraps": zxAnEnvMonFanTraps,
       "zxAnEnvFanLinkDown": zxAnEnvFanLinkDown,
       "zxAnEnvFanLinkUp": zxAnEnvFanLinkUp,
       "zxAnEnvFanTrayLinkDown": zxAnEnvFanTrayLinkDown,
       "zxAnEnvFanTrayLinkUp": zxAnEnvFanTrayLinkUp,
       "zxAnEnvFanFailureAlm": zxAnEnvFanFailureAlm,
       "zxAnEnvFanFailureClr": zxAnEnvFanFailureClr,
       "zxAnEnvDeviceTraps": zxAnEnvDeviceTraps,
       "zxAnEnvDeviceAbnormalAlm": zxAnEnvDeviceAbnormalAlm,
       "zxAnEnvDeviceAbnormalClr": zxAnEnvDeviceAbnormalClr,
       "zxAnEnvMonConformance": zxAnEnvMonConformance,
       "zxAnEnvMonCompliances": zxAnEnvMonCompliances,
       "zxAnEnvMonCompliance": zxAnEnvMonCompliance,
       "zxAnEnvMonGroups": zxAnEnvMonGroups,
       "zxAnEnvMonCapabilitiesGroup": zxAnEnvMonCapabilitiesGroup,
       "zxAnEnvTempGroup": zxAnEnvTempGroup,
       "zxAnEnvCardTempGroup": zxAnEnvCardTempGroup,
       "zxAnEnvInterfaceGroup": zxAnEnvInterfaceGroup,
       "zxAnEnvPowerSupplyGroup": zxAnEnvPowerSupplyGroup,
       "zxAnEnvFanTrayTableGroup": zxAnEnvFanTrayTableGroup,
       "zxAnEnvFanTableGroup": zxAnEnvFanTableGroup,
       "zxAnEnvMonNotificationsGroup": zxAnEnvMonNotificationsGroup}
)
