# SNMP MIB module (HIMOINSAv14-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\himoinsa\HIMOINSAv14-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:27 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Himoinsa_ObjectIdentity = ObjectIdentity
himoinsa = _Himoinsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41809)
)
_Measures_ObjectIdentity = ObjectIdentity
measures = _Measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41809, 1)
)
_MainsFreq_Type = Integer32
_MainsFreq_Object = MibScalar
mainsFreq = _MainsFreq_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 1),
    _MainsFreq_Type()
)
mainsFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsFreq.setStatus("current")
_MainsVL12_Type = Integer32
_MainsVL12_Object = MibScalar
mainsVL12 = _MainsVL12_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 2),
    _MainsVL12_Type()
)
mainsVL12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL12.setStatus("current")
_MainsVL23_Type = Integer32
_MainsVL23_Object = MibScalar
mainsVL23 = _MainsVL23_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 3),
    _MainsVL23_Type()
)
mainsVL23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL23.setStatus("current")
_MainsVL13_Type = Integer32
_MainsVL13_Object = MibScalar
mainsVL13 = _MainsVL13_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 4),
    _MainsVL13_Type()
)
mainsVL13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL13.setStatus("current")
_MainsVL1N_Type = Integer32
_MainsVL1N_Object = MibScalar
mainsVL1N = _MainsVL1N_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 5),
    _MainsVL1N_Type()
)
mainsVL1N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL1N.setStatus("current")
_MainsVL2N_Type = Integer32
_MainsVL2N_Object = MibScalar
mainsVL2N = _MainsVL2N_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 6),
    _MainsVL2N_Type()
)
mainsVL2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL2N.setStatus("current")
_MainsVL3N_Type = Integer32
_MainsVL3N_Object = MibScalar
mainsVL3N = _MainsVL3N_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 7),
    _MainsVL3N_Type()
)
mainsVL3N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL3N.setStatus("current")
_GenFreq_Type = Integer32
_GenFreq_Object = MibScalar
genFreq = _GenFreq_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 8),
    _GenFreq_Type()
)
genFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genFreq.setStatus("current")
_GenVL12_Type = Integer32
_GenVL12_Object = MibScalar
genVL12 = _GenVL12_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 9),
    _GenVL12_Type()
)
genVL12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL12.setStatus("current")
_GenVL23_Type = Integer32
_GenVL23_Object = MibScalar
genVL23 = _GenVL23_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 10),
    _GenVL23_Type()
)
genVL23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL23.setStatus("current")
_GenVL13_Type = Integer32
_GenVL13_Object = MibScalar
genVL13 = _GenVL13_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 11),
    _GenVL13_Type()
)
genVL13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL13.setStatus("current")
_GenVL1N_Type = Integer32
_GenVL1N_Object = MibScalar
genVL1N = _GenVL1N_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 12),
    _GenVL1N_Type()
)
genVL1N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL1N.setStatus("current")
_GenVL2N_Type = Integer32
_GenVL2N_Object = MibScalar
genVL2N = _GenVL2N_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 13),
    _GenVL2N_Type()
)
genVL2N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL2N.setStatus("current")
_GenVL3N_Type = Integer32
_GenVL3N_Object = MibScalar
genVL3N = _GenVL3N_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 14),
    _GenVL3N_Type()
)
genVL3N.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL3N.setStatus("current")
_Ph1Amp_Type = Integer32
_Ph1Amp_Object = MibScalar
ph1Amp = _Ph1Amp_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 15),
    _Ph1Amp_Type()
)
ph1Amp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph1Amp.setStatus("current")
_Ph2Amp_Type = Integer32
_Ph2Amp_Object = MibScalar
ph2Amp = _Ph2Amp_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 16),
    _Ph2Amp_Type()
)
ph2Amp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph2Amp.setStatus("current")
_Ph3Amp_Type = Integer32
_Ph3Amp_Object = MibScalar
ph3Amp = _Ph3Amp_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 17),
    _Ph3Amp_Type()
)
ph3Amp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph3Amp.setStatus("current")
_FlagsCurrent_Type = Gauge32
_FlagsCurrent_Object = MibScalar
flagsCurrent = _FlagsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 18),
    _FlagsCurrent_Type()
)
flagsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flagsCurrent.setStatus("current")
_PFCTotal_Type = Integer32
_PFCTotal_Object = MibScalar
pFCTotal = _PFCTotal_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 19),
    _PFCTotal_Type()
)
pFCTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFCTotal.setStatus("current")
_PFC1_Type = Integer32
_PFC1_Object = MibScalar
pFC1 = _PFC1_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 20),
    _PFC1_Type()
)
pFC1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFC1.setStatus("current")
_PFC2_Type = Integer32
_PFC2_Object = MibScalar
pFC2 = _PFC2_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 21),
    _PFC2_Type()
)
pFC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFC2.setStatus("current")
_PFC3_Type = Integer32
_PFC3_Object = MibScalar
pFC3 = _PFC3_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 22),
    _PFC3_Type()
)
pFC3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFC3.setStatus("current")
_RealPow_Type = Integer32
_RealPow_Object = MibScalar
realPow = _RealPow_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 23),
    _RealPow_Type()
)
realPow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realPow.setStatus("current")
_AppPow_Type = Integer32
_AppPow_Object = MibScalar
appPow = _AppPow_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 24),
    _AppPow_Type()
)
appPow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appPow.setStatus("current")
_ReactivePow_Type = Integer32
_ReactivePow_Object = MibScalar
reactivePow = _ReactivePow_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 25),
    _ReactivePow_Type()
)
reactivePow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reactivePow.setStatus("current")
_Speed_Type = Integer32
_Speed_Object = MibScalar
speed = _Speed_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 26),
    _Speed_Type()
)
speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speed.setStatus("current")
_FuelLevel_Type = Integer32
_FuelLevel_Object = MibScalar
fuelLevel = _FuelLevel_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 27),
    _FuelLevel_Type()
)
fuelLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fuelLevel.setStatus("current")
_AltenatorVolt_Type = Integer32
_AltenatorVolt_Object = MibScalar
altenatorVolt = _AltenatorVolt_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 28),
    _AltenatorVolt_Type()
)
altenatorVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    altenatorVolt.setStatus("current")
_BatteryVolt_Type = Integer32
_BatteryVolt_Object = MibScalar
batteryVolt = _BatteryVolt_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 29),
    _BatteryVolt_Type()
)
batteryVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVolt.setStatus("current")
_WaterTemp_Type = Integer32
_WaterTemp_Object = MibScalar
waterTemp = _WaterTemp_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 30),
    _WaterTemp_Type()
)
waterTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterTemp.setStatus("current")
_OilPress_Type = Integer32
_OilPress_Object = MibScalar
oilPress = _OilPress_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 31),
    _OilPress_Type()
)
oilPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilPress.setStatus("current")
_OilTemp_Type = Integer32
_OilTemp_Object = MibScalar
oilTemp = _OilTemp_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 32),
    _OilTemp_Type()
)
oilTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oilTemp.setStatus("current")
_SensorDet_Type = Integer32
_SensorDet_Object = MibScalar
sensorDet = _SensorDet_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 33),
    _SensorDet_Type()
)
sensorDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorDet.setStatus("current")
_Units_Type = Integer32
_Units_Object = MibScalar
units = _Units_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 34),
    _Units_Type()
)
units.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    units.setStatus("current")
_TotalInstantPower_Type = Integer32
_TotalInstantPower_Object = MibScalar
totalInstantPower = _TotalInstantPower_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 35),
    _TotalInstantPower_Type()
)
totalInstantPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInstantPower.setStatus("current")
_PartialInstantPower_Type = Integer32
_PartialInstantPower_Object = MibScalar
partialInstantPower = _PartialInstantPower_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 36),
    _PartialInstantPower_Type()
)
partialInstantPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partialInstantPower.setStatus("current")
_PowerPerDay_Type = Integer32
_PowerPerDay_Object = MibScalar
powerPerDay = _PowerPerDay_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 37),
    _PowerPerDay_Type()
)
powerPerDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPerDay.setStatus("current")
_PowerPerMonth_Type = Integer32
_PowerPerMonth_Object = MibScalar
powerPerMonth = _PowerPerMonth_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 38),
    _PowerPerMonth_Type()
)
powerPerMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPerMonth.setStatus("current")
_PowerPerYear_Type = Integer32
_PowerPerYear_Object = MibScalar
powerPerYear = _PowerPerYear_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 39),
    _PowerPerYear_Type()
)
powerPerYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerPerYear.setStatus("current")
_TotalRunningTime_Type = Integer32
_TotalRunningTime_Object = MibScalar
totalRunningTime = _TotalRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 40),
    _TotalRunningTime_Type()
)
totalRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRunningTime.setStatus("current")
_PartialRunningTime_Type = Integer32
_PartialRunningTime_Object = MibScalar
partialRunningTime = _PartialRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 41),
    _PartialRunningTime_Type()
)
partialRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partialRunningTime.setStatus("current")
_SuccessfulStarts_Type = Integer32
_SuccessfulStarts_Object = MibScalar
successfulStarts = _SuccessfulStarts_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 42),
    _SuccessfulStarts_Type()
)
successfulStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    successfulStarts.setStatus("current")
_UnsuccessfulStarts_Type = Integer32
_UnsuccessfulStarts_Object = MibScalar
unsuccessfulStarts = _UnsuccessfulStarts_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 43),
    _UnsuccessfulStarts_Type()
)
unsuccessfulStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unsuccessfulStarts.setStatus("current")
_SwitchPanelCount_Type = Integer32
_SwitchPanelCount_Object = MibScalar
switchPanelCount = _SwitchPanelCount_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 44),
    _SwitchPanelCount_Type()
)
switchPanelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPanelCount.setStatus("current")
_SecondaryBatteryVoltage_Type = Integer32
_SecondaryBatteryVoltage_Object = MibScalar
secondaryBatteryVoltage = _SecondaryBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 45),
    _SecondaryBatteryVoltage_Type()
)
secondaryBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryBatteryVoltage.setStatus("current")
_Status_Type = Gauge32
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 46),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")
_AlarmBitMapHigh_Type = Gauge32
_AlarmBitMapHigh_Object = MibScalar
alarmBitMapHigh = _AlarmBitMapHigh_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 47),
    _AlarmBitMapHigh_Type()
)
alarmBitMapHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBitMapHigh.setStatus("current")
_AlarmBitMapLow_Type = Gauge32
_AlarmBitMapLow_Object = MibScalar
alarmBitMapLow = _AlarmBitMapLow_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 48),
    _AlarmBitMapLow_Type()
)
alarmBitMapLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBitMapLow.setStatus("current")
_AlarmBitMapHigh1_Type = Gauge32
_AlarmBitMapHigh1_Object = MibScalar
alarmBitMapHigh1 = _AlarmBitMapHigh1_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 49),
    _AlarmBitMapHigh1_Type()
)
alarmBitMapHigh1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBitMapHigh1.setStatus("current")
_FalloArranqueMeasure_Type = Gauge32
_FalloArranqueMeasure_Object = MibScalar
falloArranqueMeasure = _FalloArranqueMeasure_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 50),
    _FalloArranqueMeasure_Type()
)
falloArranqueMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falloArranqueMeasure.setStatus("current")
_NivelCombustibleMeasure_Type = Gauge32
_NivelCombustibleMeasure_Object = MibScalar
nivelCombustibleMeasure = _NivelCombustibleMeasure_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 51),
    _NivelCombustibleMeasure_Type()
)
nivelCombustibleMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nivelCombustibleMeasure.setStatus("current")
_CaidaGrupoMeasure_Type = Gauge32
_CaidaGrupoMeasure_Object = MibScalar
caidaGrupoMeasure = _CaidaGrupoMeasure_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 52),
    _CaidaGrupoMeasure_Type()
)
caidaGrupoMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caidaGrupoMeasure.setStatus("current")
_CaidaRedMeasure_Type = Gauge32
_CaidaRedMeasure_Object = MibScalar
caidaRedMeasure = _CaidaRedMeasure_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 53),
    _CaidaRedMeasure_Type()
)
caidaRedMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caidaRedMeasure.setStatus("current")
_CaidaGrupoConmMeasure_Type = Gauge32
_CaidaGrupoConmMeasure_Object = MibScalar
caidaGrupoConmMeasure = _CaidaGrupoConmMeasure_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 54),
    _CaidaGrupoConmMeasure_Type()
)
caidaGrupoConmMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caidaGrupoConmMeasure.setStatus("current")
_MeasuresConmTable_Object = MibTable
measuresConmTable = _MeasuresConmTable_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55)
)
if mibBuilder.loadTexts:
    measuresConmTable.setStatus("current")
_MeasuresConmEntry_Object = MibTableRow
measuresConmEntry = _MeasuresConmEntry_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1)
)
measuresConmEntry.setIndexNames(
    (0, "HIMOINSAv14-MIB", "measuresConmIndex"),
)
if mibBuilder.loadTexts:
    measuresConmEntry.setStatus("current")
_MeasuresConmIndex_Type = InterfaceIndex
_MeasuresConmIndex_Object = MibTableColumn
measuresConmIndex = _MeasuresConmIndex_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 1),
    _MeasuresConmIndex_Type()
)
measuresConmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    measuresConmIndex.setStatus("current")
_MainsFreqConm_Type = Integer32
_MainsFreqConm_Object = MibTableColumn
mainsFreqConm = _MainsFreqConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 2),
    _MainsFreqConm_Type()
)
mainsFreqConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsFreqConm.setStatus("current")
_MainsVL12Conm_Type = Integer32
_MainsVL12Conm_Object = MibTableColumn
mainsVL12Conm = _MainsVL12Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 3),
    _MainsVL12Conm_Type()
)
mainsVL12Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL12Conm.setStatus("current")
_MainsVL23Conm_Type = Integer32
_MainsVL23Conm_Object = MibTableColumn
mainsVL23Conm = _MainsVL23Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 4),
    _MainsVL23Conm_Type()
)
mainsVL23Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL23Conm.setStatus("current")
_MainsVL13Conm_Type = Integer32
_MainsVL13Conm_Object = MibTableColumn
mainsVL13Conm = _MainsVL13Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 5),
    _MainsVL13Conm_Type()
)
mainsVL13Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL13Conm.setStatus("current")
_MainsVL1NConm_Type = Integer32
_MainsVL1NConm_Object = MibTableColumn
mainsVL1NConm = _MainsVL1NConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 6),
    _MainsVL1NConm_Type()
)
mainsVL1NConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL1NConm.setStatus("current")
_MainsVL2NConm_Type = Integer32
_MainsVL2NConm_Object = MibTableColumn
mainsVL2NConm = _MainsVL2NConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 7),
    _MainsVL2NConm_Type()
)
mainsVL2NConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL2NConm.setStatus("current")
_MainsVL3NConm_Type = Integer32
_MainsVL3NConm_Object = MibTableColumn
mainsVL3NConm = _MainsVL3NConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 8),
    _MainsVL3NConm_Type()
)
mainsVL3NConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVL3NConm.setStatus("current")
_GenFreqConm_Type = Integer32
_GenFreqConm_Object = MibTableColumn
genFreqConm = _GenFreqConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 9),
    _GenFreqConm_Type()
)
genFreqConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genFreqConm.setStatus("current")
_GenVL12Conm_Type = Integer32
_GenVL12Conm_Object = MibTableColumn
genVL12Conm = _GenVL12Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 10),
    _GenVL12Conm_Type()
)
genVL12Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL12Conm.setStatus("current")
_GenVL23Conm_Type = Integer32
_GenVL23Conm_Object = MibTableColumn
genVL23Conm = _GenVL23Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 11),
    _GenVL23Conm_Type()
)
genVL23Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL23Conm.setStatus("current")
_GenVL13Conm_Type = Integer32
_GenVL13Conm_Object = MibTableColumn
genVL13Conm = _GenVL13Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 12),
    _GenVL13Conm_Type()
)
genVL13Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL13Conm.setStatus("current")
_GenVL1NConm_Type = Integer32
_GenVL1NConm_Object = MibTableColumn
genVL1NConm = _GenVL1NConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 13),
    _GenVL1NConm_Type()
)
genVL1NConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL1NConm.setStatus("current")
_GenVL2NConm_Type = Integer32
_GenVL2NConm_Object = MibTableColumn
genVL2NConm = _GenVL2NConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 14),
    _GenVL2NConm_Type()
)
genVL2NConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL2NConm.setStatus("current")
_GenVL3NConm_Type = Integer32
_GenVL3NConm_Object = MibTableColumn
genVL3NConm = _GenVL3NConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 15),
    _GenVL3NConm_Type()
)
genVL3NConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVL3NConm.setStatus("current")
_Ph1AmpConm_Type = Integer32
_Ph1AmpConm_Object = MibTableColumn
ph1AmpConm = _Ph1AmpConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 16),
    _Ph1AmpConm_Type()
)
ph1AmpConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph1AmpConm.setStatus("current")
_Ph2AmpConm_Type = Integer32
_Ph2AmpConm_Object = MibTableColumn
ph2AmpConm = _Ph2AmpConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 17),
    _Ph2AmpConm_Type()
)
ph2AmpConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph2AmpConm.setStatus("current")
_Ph3AmpConm_Type = Integer32
_Ph3AmpConm_Object = MibTableColumn
ph3AmpConm = _Ph3AmpConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 18),
    _Ph3AmpConm_Type()
)
ph3AmpConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph3AmpConm.setStatus("current")
_FlagsCurrentConm_Type = Gauge32
_FlagsCurrentConm_Object = MibTableColumn
flagsCurrentConm = _FlagsCurrentConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 19),
    _FlagsCurrentConm_Type()
)
flagsCurrentConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flagsCurrentConm.setStatus("current")
_PFCTotalConm_Type = Integer32
_PFCTotalConm_Object = MibTableColumn
pFCTotalConm = _PFCTotalConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 20),
    _PFCTotalConm_Type()
)
pFCTotalConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFCTotalConm.setStatus("current")
_PFC1Conm_Type = Integer32
_PFC1Conm_Object = MibTableColumn
pFC1Conm = _PFC1Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 21),
    _PFC1Conm_Type()
)
pFC1Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFC1Conm.setStatus("current")
_PFC2Conm_Type = Integer32
_PFC2Conm_Object = MibTableColumn
pFC2Conm = _PFC2Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 22),
    _PFC2Conm_Type()
)
pFC2Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFC2Conm.setStatus("current")
_PFC3Conm_Type = Integer32
_PFC3Conm_Object = MibTableColumn
pFC3Conm = _PFC3Conm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 23),
    _PFC3Conm_Type()
)
pFC3Conm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pFC3Conm.setStatus("current")
_RealPowConm_Type = Integer32
_RealPowConm_Object = MibTableColumn
realPowConm = _RealPowConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 24),
    _RealPowConm_Type()
)
realPowConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realPowConm.setStatus("current")
_AppPowConm_Type = Integer32
_AppPowConm_Object = MibTableColumn
appPowConm = _AppPowConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 25),
    _AppPowConm_Type()
)
appPowConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appPowConm.setStatus("current")
_ReactPowConm_Type = Integer32
_ReactPowConm_Object = MibTableColumn
reactPowConm = _ReactPowConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 26),
    _ReactPowConm_Type()
)
reactPowConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reactPowConm.setStatus("current")
_MainsControlType_Type = Integer32
_MainsControlType_Object = MibTableColumn
mainsControlType = _MainsControlType_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 27),
    _MainsControlType_Type()
)
mainsControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsControlType.setStatus("current")
_StatusConm_Type = Gauge32
_StatusConm_Object = MibTableColumn
statusConm = _StatusConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 28),
    _StatusConm_Type()
)
statusConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusConm.setStatus("current")
_AlarmBitMapConm_Type = Gauge32
_AlarmBitMapConm_Object = MibTableColumn
alarmBitMapConm = _AlarmBitMapConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 1, 55, 1, 29),
    _AlarmBitMapConm_Type()
)
alarmBitMapConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBitMapConm.setStatus("current")
_Parameters_ObjectIdentity = ObjectIdentity
parameters = _Parameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41809, 2)
)
_StartsCount_Type = Integer32
_StartsCount_Object = MibScalar
startsCount = _StartsCount_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 1),
    _StartsCount_Type()
)
startsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startsCount.setStatus("current")
_TimeBetweenStarts_Type = Integer32
_TimeBetweenStarts_Object = MibScalar
timeBetweenStarts = _TimeBetweenStarts_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 2),
    _TimeBetweenStarts_Type()
)
timeBetweenStarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeBetweenStarts.setStatus("current")
_StartDelay_Type = Integer32
_StartDelay_Object = MibScalar
startDelay = _StartDelay_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 3),
    _StartDelay_Type()
)
startDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startDelay.setStatus("current")
_PreheatingTime_Type = Integer32
_PreheatingTime_Object = MibScalar
preheatingTime = _PreheatingTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 4),
    _PreheatingTime_Type()
)
preheatingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preheatingTime.setStatus("current")
_StartupTime_Type = Integer32
_StartupTime_Object = MibScalar
startupTime = _StartupTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 5),
    _StartupTime_Type()
)
startupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startupTime.setStatus("current")
_LoadActivationTime_Type = Integer32
_LoadActivationTime_Object = MibScalar
loadActivationTime = _LoadActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 6),
    _LoadActivationTime_Type()
)
loadActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadActivationTime.setStatus("current")
_NominalConditionTime_Type = Integer32
_NominalConditionTime_Object = MibScalar
nominalConditionTime = _NominalConditionTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 7),
    _NominalConditionTime_Type()
)
nominalConditionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nominalConditionTime.setStatus("current")
_DplusActivationTime_Type = Integer32
_DplusActivationTime_Object = MibScalar
dplusActivationTime = _DplusActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 8),
    _DplusActivationTime_Type()
)
dplusActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dplusActivationTime.setStatus("current")
_EJP1ActivationDelayTime_Type = Integer32
_EJP1ActivationDelayTime_Object = MibScalar
eJP1ActivationDelayTime = _EJP1ActivationDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 9),
    _EJP1ActivationDelayTime_Type()
)
eJP1ActivationDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eJP1ActivationDelayTime.setStatus("current")
_MainsActivationDelay_Type = Integer32
_MainsActivationDelay_Object = MibScalar
mainsActivationDelay = _MainsActivationDelay_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 10),
    _MainsActivationDelay_Type()
)
mainsActivationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsActivationDelay.setStatus("current")
_CoolingTime_Type = Integer32
_CoolingTime_Object = MibScalar
coolingTime = _CoolingTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 11),
    _CoolingTime_Type()
)
coolingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coolingTime.setStatus("current")
_PEActivationTime_Type = Integer32
_PEActivationTime_Object = MibScalar
pEActivationTime = _PEActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 12),
    _PEActivationTime_Type()
)
pEActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pEActivationTime.setStatus("current")
_CounterDetectionTime_Type = Integer32
_CounterDetectionTime_Object = MibScalar
counterDetectionTime = _CounterDetectionTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 13),
    _CounterDetectionTime_Type()
)
counterDetectionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterDetectionTime.setStatus("current")
_MaximumAlarmActivationTime_Type = Integer32
_MaximumAlarmActivationTime_Object = MibScalar
maximumAlarmActivationTime = _MaximumAlarmActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 14),
    _MaximumAlarmActivationTime_Type()
)
maximumAlarmActivationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maximumAlarmActivationTime.setStatus("current")
_PhaseNumber_Type = Integer32
_PhaseNumber_Object = MibScalar
phaseNumber = _PhaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 15),
    _PhaseNumber_Type()
)
phaseNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseNumber.setStatus("current")
_MaxGensetVoltage_Type = Integer32
_MaxGensetVoltage_Object = MibScalar
maxGensetVoltage = _MaxGensetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 16),
    _MaxGensetVoltage_Type()
)
maxGensetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxGensetVoltage.setStatus("current")
_MinGensetVoltage_Type = Integer32
_MinGensetVoltage_Object = MibScalar
minGensetVoltage = _MinGensetVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 17),
    _MinGensetVoltage_Type()
)
minGensetVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minGensetVoltage.setStatus("current")
_MaxGensetAsymetryValue_Type = Integer32
_MaxGensetAsymetryValue_Object = MibScalar
maxGensetAsymetryValue = _MaxGensetAsymetryValue_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 18),
    _MaxGensetAsymetryValue_Type()
)
maxGensetAsymetryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxGensetAsymetryValue.setStatus("current")
_MaxGensetFrequency_Type = Integer32
_MaxGensetFrequency_Object = MibScalar
maxGensetFrequency = _MaxGensetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 19),
    _MaxGensetFrequency_Type()
)
maxGensetFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxGensetFrequency.setStatus("current")
_MinGensetFrequency_Type = Integer32
_MinGensetFrequency_Object = MibScalar
minGensetFrequency = _MinGensetFrequency_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 20),
    _MinGensetFrequency_Type()
)
minGensetFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minGensetFrequency.setStatus("current")
_MaxGensetCurrent_Type = Integer32
_MaxGensetCurrent_Object = MibScalar
maxGensetCurrent = _MaxGensetCurrent_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 21),
    _MaxGensetCurrent_Type()
)
maxGensetCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxGensetCurrent.setStatus("current")
_ShortCircuitDetection_Type = Integer32
_ShortCircuitDetection_Object = MibScalar
shortCircuitDetection = _ShortCircuitDetection_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 22),
    _ShortCircuitDetection_Type()
)
shortCircuitDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shortCircuitDetection.setStatus("current")
_GensetNominalPower_Type = Integer32
_GensetNominalPower_Object = MibScalar
gensetNominalPower = _GensetNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 23),
    _GensetNominalPower_Type()
)
gensetNominalPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gensetNominalPower.setStatus("current")
_MaxReversePower_Type = Integer32
_MaxReversePower_Object = MibScalar
maxReversePower = _MaxReversePower_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 24),
    _MaxReversePower_Type()
)
maxReversePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxReversePower.setStatus("current")
_MaxPickupSpeed_Type = Integer32
_MaxPickupSpeed_Object = MibScalar
maxPickupSpeed = _MaxPickupSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 25),
    _MaxPickupSpeed_Type()
)
maxPickupSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxPickupSpeed.setStatus("current")
_MinPickupSpeed_Type = Integer32
_MinPickupSpeed_Object = MibScalar
minPickupSpeed = _MinPickupSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 26),
    _MinPickupSpeed_Type()
)
minPickupSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minPickupSpeed.setStatus("current")
_MaxMainsVoltage_Type = Integer32
_MaxMainsVoltage_Object = MibScalar
maxMainsVoltage = _MaxMainsVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 27),
    _MaxMainsVoltage_Type()
)
maxMainsVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxMainsVoltage.setStatus("current")
_MinMainsVoltage_Type = Integer32
_MinMainsVoltage_Object = MibScalar
minMainsVoltage = _MinMainsVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 28),
    _MinMainsVoltage_Type()
)
minMainsVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minMainsVoltage.setStatus("current")
_MaxMainsFrequency_Type = Integer32
_MaxMainsFrequency_Object = MibScalar
maxMainsFrequency = _MaxMainsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 29),
    _MaxMainsFrequency_Type()
)
maxMainsFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxMainsFrequency.setStatus("current")
_MinMainsFrequency_Type = Integer32
_MinMainsFrequency_Object = MibScalar
minMainsFrequency = _MinMainsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 30),
    _MinMainsFrequency_Type()
)
minMainsFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minMainsFrequency.setStatus("current")
_MinBatteryVoltage_Type = Integer32
_MinBatteryVoltage_Object = MibScalar
minBatteryVoltage = _MinBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 31),
    _MinBatteryVoltage_Type()
)
minBatteryVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minBatteryVoltage.setStatus("current")
_TransferPumpMinLevel_Type = Integer32
_TransferPumpMinLevel_Object = MibScalar
transferPumpMinLevel = _TransferPumpMinLevel_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 32),
    _TransferPumpMinLevel_Type()
)
transferPumpMinLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferPumpMinLevel.setStatus("current")
_TransferPumpMaxLevel_Type = Integer32
_TransferPumpMaxLevel_Object = MibScalar
transferPumpMaxLevel = _TransferPumpMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 33),
    _TransferPumpMaxLevel_Type()
)
transferPumpMaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferPumpMaxLevel.setStatus("current")
_StartingVoltageGensetSignal_Type = Integer32
_StartingVoltageGensetSignal_Object = MibScalar
startingVoltageGensetSignal = _StartingVoltageGensetSignal_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 34),
    _StartingVoltageGensetSignal_Type()
)
startingVoltageGensetSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startingVoltageGensetSignal.setStatus("current")
_StartingVoltageAlternator_Type = Integer32
_StartingVoltageAlternator_Object = MibScalar
startingVoltageAlternator = _StartingVoltageAlternator_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 35),
    _StartingVoltageAlternator_Type()
)
startingVoltageAlternator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startingVoltageAlternator.setStatus("current")
_StartingSpeed_Type = Integer32
_StartingSpeed_Object = MibScalar
startingSpeed = _StartingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 36),
    _StartingSpeed_Type()
)
startingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startingSpeed.setStatus("current")
_EngineFlywheelTeeth_Type = Integer32
_EngineFlywheelTeeth_Object = MibScalar
engineFlywheelTeeth = _EngineFlywheelTeeth_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 37),
    _EngineFlywheelTeeth_Type()
)
engineFlywheelTeeth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    engineFlywheelTeeth.setStatus("current")
_FuelReserveLevel_Type = Integer32
_FuelReserveLevel_Object = MibScalar
fuelReserveLevel = _FuelReserveLevel_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 38),
    _FuelReserveLevel_Type()
)
fuelReserveLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fuelReserveLevel.setStatus("current")
_LowOilPressure_Type = Integer32
_LowOilPressure_Object = MibScalar
lowOilPressure = _LowOilPressure_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 39),
    _LowOilPressure_Type()
)
lowOilPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowOilPressure.setStatus("current")
_HighWaterTemperatureThreshold_Type = Integer32
_HighWaterTemperatureThreshold_Object = MibScalar
highWaterTemperatureThreshold = _HighWaterTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 40),
    _HighWaterTemperatureThreshold_Type()
)
highWaterTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highWaterTemperatureThreshold.setStatus("current")
_LowEngineTemperature_Type = Integer32
_LowEngineTemperature_Object = MibScalar
lowEngineTemperature = _LowEngineTemperature_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 41),
    _LowEngineTemperature_Type()
)
lowEngineTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowEngineTemperature.setStatus("current")
_MinPreheatingTemp_Type = Integer32
_MinPreheatingTemp_Object = MibScalar
minPreheatingTemp = _MinPreheatingTemp_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 42),
    _MinPreheatingTemp_Type()
)
minPreheatingTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minPreheatingTemp.setStatus("current")
_MaxPreheatingTemp_Type = Integer32
_MaxPreheatingTemp_Object = MibScalar
maxPreheatingTemp = _MaxPreheatingTemp_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 43),
    _MaxPreheatingTemp_Type()
)
maxPreheatingTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxPreheatingTemp.setStatus("current")
_DeviceIpAddress_Type = IpAddress
_DeviceIpAddress_Object = MibScalar
deviceIpAddress = _DeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 44),
    _DeviceIpAddress_Type()
)
deviceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIpAddress.setStatus("current")
_DeviceMaskSubnet_Type = IpAddress
_DeviceMaskSubnet_Object = MibScalar
deviceMaskSubnet = _DeviceMaskSubnet_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 45),
    _DeviceMaskSubnet_Type()
)
deviceMaskSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMaskSubnet.setStatus("current")
_DeviceGateway_Type = IpAddress
_DeviceGateway_Object = MibScalar
deviceGateway = _DeviceGateway_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 46),
    _DeviceGateway_Type()
)
deviceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGateway.setStatus("current")
_ManagerAddress_Type = IpAddress
_ManagerAddress_Object = MibScalar
managerAddress = _ManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 47),
    _ManagerAddress_Type()
)
managerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerAddress.setStatus("current")
_AgentSNMPPort_Type = Integer32
_AgentSNMPPort_Object = MibScalar
agentSNMPPort = _AgentSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 48),
    _AgentSNMPPort_Type()
)
agentSNMPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSNMPPort.setStatus("current")
_ManagertrapsPort_Type = Integer32
_ManagertrapsPort_Object = MibScalar
managertrapsPort = _ManagertrapsPort_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 49),
    _ManagertrapsPort_Type()
)
managertrapsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managertrapsPort.setStatus("current")
_Reset_Type = Integer32
_Reset_Object = MibScalar
reset = _Reset_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 50),
    _Reset_Type()
)
reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reset.setStatus("current")
_Version_Type = Integer32
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 51),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_GensetStartStop_Type = Integer32
_GensetStartStop_Object = MibScalar
gensetStartStop = _GensetStartStop_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 52),
    _GensetStartStop_Type()
)
gensetStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gensetStartStop.setStatus("current")
_GensetMode_Type = Integer32
_GensetMode_Object = MibScalar
gensetMode = _GensetMode_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 53),
    _GensetMode_Type()
)
gensetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gensetMode.setStatus("current")
_MainsBreakerStatus_Type = Integer32
_MainsBreakerStatus_Object = MibScalar
mainsBreakerStatus = _MainsBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 54),
    _MainsBreakerStatus_Type()
)
mainsBreakerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsBreakerStatus.setStatus("current")
_GensetBreakerStatus_Type = Integer32
_GensetBreakerStatus_Object = MibScalar
gensetBreakerStatus = _GensetBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 55),
    _GensetBreakerStatus_Type()
)
gensetBreakerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gensetBreakerStatus.setStatus("current")
_ParametersConmTable_Object = MibTable
parametersConmTable = _ParametersConmTable_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56)
)
if mibBuilder.loadTexts:
    parametersConmTable.setStatus("current")
_ParametersConmEntry_Object = MibTableRow
parametersConmEntry = _ParametersConmEntry_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1)
)
parametersConmEntry.setIndexNames(
    (0, "HIMOINSAv14-MIB", "parametersConmIndex"),
)
if mibBuilder.loadTexts:
    parametersConmEntry.setStatus("current")
_ParametersConmIndex_Type = InterfaceIndex
_ParametersConmIndex_Object = MibTableColumn
parametersConmIndex = _ParametersConmIndex_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 1),
    _ParametersConmIndex_Type()
)
parametersConmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    parametersConmIndex.setStatus("current")
_PhaseNumberConm_Type = Integer32
_PhaseNumberConm_Object = MibTableColumn
phaseNumberConm = _PhaseNumberConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 2),
    _PhaseNumberConm_Type()
)
phaseNumberConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phaseNumberConm.setStatus("current")
_MaxGensetVoltageConm_Type = Integer32
_MaxGensetVoltageConm_Object = MibTableColumn
maxGensetVoltageConm = _MaxGensetVoltageConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 3),
    _MaxGensetVoltageConm_Type()
)
maxGensetVoltageConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxGensetVoltageConm.setStatus("current")
_MinGensetVoltageConm_Type = Integer32
_MinGensetVoltageConm_Object = MibTableColumn
minGensetVoltageConm = _MinGensetVoltageConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 4),
    _MinGensetVoltageConm_Type()
)
minGensetVoltageConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minGensetVoltageConm.setStatus("current")
_MaxGensetAsymetryValueConm_Type = Integer32
_MaxGensetAsymetryValueConm_Object = MibTableColumn
maxGensetAsymetryValueConm = _MaxGensetAsymetryValueConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 5),
    _MaxGensetAsymetryValueConm_Type()
)
maxGensetAsymetryValueConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxGensetAsymetryValueConm.setStatus("current")
_MaxGensetFrequencyConm_Type = Integer32
_MaxGensetFrequencyConm_Object = MibTableColumn
maxGensetFrequencyConm = _MaxGensetFrequencyConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 6),
    _MaxGensetFrequencyConm_Type()
)
maxGensetFrequencyConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxGensetFrequencyConm.setStatus("current")
_MinGensetFrequencyConm_Type = Integer32
_MinGensetFrequencyConm_Object = MibTableColumn
minGensetFrequencyConm = _MinGensetFrequencyConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 7),
    _MinGensetFrequencyConm_Type()
)
minGensetFrequencyConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minGensetFrequencyConm.setStatus("current")
_MaxGensetCurrentConm_Type = Integer32
_MaxGensetCurrentConm_Object = MibTableColumn
maxGensetCurrentConm = _MaxGensetCurrentConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 8),
    _MaxGensetCurrentConm_Type()
)
maxGensetCurrentConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxGensetCurrentConm.setStatus("current")
_ShortCircuitDetectionConm_Type = Integer32
_ShortCircuitDetectionConm_Object = MibTableColumn
shortCircuitDetectionConm = _ShortCircuitDetectionConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 9),
    _ShortCircuitDetectionConm_Type()
)
shortCircuitDetectionConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shortCircuitDetectionConm.setStatus("current")
_GensetNominalPowerConm_Type = Integer32
_GensetNominalPowerConm_Object = MibTableColumn
gensetNominalPowerConm = _GensetNominalPowerConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 10),
    _GensetNominalPowerConm_Type()
)
gensetNominalPowerConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gensetNominalPowerConm.setStatus("current")
_MaxReversePowerConm_Type = Integer32
_MaxReversePowerConm_Object = MibTableColumn
maxReversePowerConm = _MaxReversePowerConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 11),
    _MaxReversePowerConm_Type()
)
maxReversePowerConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxReversePowerConm.setStatus("current")
_MaxPickupSpeedConm_Type = Integer32
_MaxPickupSpeedConm_Object = MibTableColumn
maxPickupSpeedConm = _MaxPickupSpeedConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 12),
    _MaxPickupSpeedConm_Type()
)
maxPickupSpeedConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxPickupSpeedConm.setStatus("current")
_MinPickupSpeedConm_Type = Integer32
_MinPickupSpeedConm_Object = MibTableColumn
minPickupSpeedConm = _MinPickupSpeedConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 13),
    _MinPickupSpeedConm_Type()
)
minPickupSpeedConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minPickupSpeedConm.setStatus("current")
_MaxMainsVoltageConm_Type = Integer32
_MaxMainsVoltageConm_Object = MibTableColumn
maxMainsVoltageConm = _MaxMainsVoltageConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 14),
    _MaxMainsVoltageConm_Type()
)
maxMainsVoltageConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxMainsVoltageConm.setStatus("current")
_MinMainsVoltageConm_Type = Integer32
_MinMainsVoltageConm_Object = MibTableColumn
minMainsVoltageConm = _MinMainsVoltageConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 15),
    _MinMainsVoltageConm_Type()
)
minMainsVoltageConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minMainsVoltageConm.setStatus("current")
_MaxMainsFrequencyConm_Type = Integer32
_MaxMainsFrequencyConm_Object = MibTableColumn
maxMainsFrequencyConm = _MaxMainsFrequencyConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 16),
    _MaxMainsFrequencyConm_Type()
)
maxMainsFrequencyConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxMainsFrequencyConm.setStatus("current")
_MinMainsFrequencyConm_Type = Integer32
_MinMainsFrequencyConm_Object = MibTableColumn
minMainsFrequencyConm = _MinMainsFrequencyConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 17),
    _MinMainsFrequencyConm_Type()
)
minMainsFrequencyConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minMainsFrequencyConm.setStatus("current")
_StartingVoltageValueConm_Type = Integer32
_StartingVoltageValueConm_Object = MibTableColumn
startingVoltageValueConm = _StartingVoltageValueConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 2, 56, 1, 18),
    _StartingVoltageValueConm_Type()
)
startingVoltageValueConm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startingVoltageValueConm.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41809, 3)
)
_AlarmString_Type = DisplayString
_AlarmString_Object = MibScalar
alarmString = _AlarmString_Object(
    (1, 3, 6, 1, 4, 1, 41809, 3, 1),
    _AlarmString_Type()
)
alarmString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmString.setStatus("mandatory")
_FalloArranque_Type = DisplayString
_FalloArranque_Object = MibScalar
falloArranque = _FalloArranque_Object(
    (1, 3, 6, 1, 4, 1, 41809, 3, 2),
    _FalloArranque_Type()
)
falloArranque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    falloArranque.setStatus("mandatory")
_NivelCombustible_Type = DisplayString
_NivelCombustible_Object = MibScalar
nivelCombustible = _NivelCombustible_Object(
    (1, 3, 6, 1, 4, 1, 41809, 3, 4),
    _NivelCombustible_Type()
)
nivelCombustible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nivelCombustible.setStatus("mandatory")
_CaidaGrupo_Type = DisplayString
_CaidaGrupo_Object = MibScalar
caidaGrupo = _CaidaGrupo_Object(
    (1, 3, 6, 1, 4, 1, 41809, 3, 6),
    _CaidaGrupo_Type()
)
caidaGrupo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caidaGrupo.setStatus("mandatory")
_CaidaRed_Type = DisplayString
_CaidaRed_Object = MibScalar
caidaRed = _CaidaRed_Object(
    (1, 3, 6, 1, 4, 1, 41809, 3, 8),
    _CaidaRed_Type()
)
caidaRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caidaRed.setStatus("mandatory")
_CaidaGrupoConm_Type = DisplayString
_CaidaGrupoConm_Object = MibScalar
caidaGrupoConm = _CaidaGrupoConm_Object(
    (1, 3, 6, 1, 4, 1, 41809, 3, 10),
    _CaidaGrupoConm_Type()
)
caidaGrupoConm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caidaGrupoConm.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIMOINSAv14-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "himoinsa": himoinsa,
       "measures": measures,
       "mainsFreq": mainsFreq,
       "mainsVL12": mainsVL12,
       "mainsVL23": mainsVL23,
       "mainsVL13": mainsVL13,
       "mainsVL1N": mainsVL1N,
       "mainsVL2N": mainsVL2N,
       "mainsVL3N": mainsVL3N,
       "genFreq": genFreq,
       "genVL12": genVL12,
       "genVL23": genVL23,
       "genVL13": genVL13,
       "genVL1N": genVL1N,
       "genVL2N": genVL2N,
       "genVL3N": genVL3N,
       "ph1Amp": ph1Amp,
       "ph2Amp": ph2Amp,
       "ph3Amp": ph3Amp,
       "flagsCurrent": flagsCurrent,
       "pFCTotal": pFCTotal,
       "pFC1": pFC1,
       "pFC2": pFC2,
       "pFC3": pFC3,
       "realPow": realPow,
       "appPow": appPow,
       "reactivePow": reactivePow,
       "speed": speed,
       "fuelLevel": fuelLevel,
       "altenatorVolt": altenatorVolt,
       "batteryVolt": batteryVolt,
       "waterTemp": waterTemp,
       "oilPress": oilPress,
       "oilTemp": oilTemp,
       "sensorDet": sensorDet,
       "units": units,
       "totalInstantPower": totalInstantPower,
       "partialInstantPower": partialInstantPower,
       "powerPerDay": powerPerDay,
       "powerPerMonth": powerPerMonth,
       "powerPerYear": powerPerYear,
       "totalRunningTime": totalRunningTime,
       "partialRunningTime": partialRunningTime,
       "successfulStarts": successfulStarts,
       "unsuccessfulStarts": unsuccessfulStarts,
       "switchPanelCount": switchPanelCount,
       "secondaryBatteryVoltage": secondaryBatteryVoltage,
       "status": status,
       "alarmBitMapHigh": alarmBitMapHigh,
       "alarmBitMapLow": alarmBitMapLow,
       "alarmBitMapHigh1": alarmBitMapHigh1,
       "falloArranqueMeasure": falloArranqueMeasure,
       "nivelCombustibleMeasure": nivelCombustibleMeasure,
       "caidaGrupoMeasure": caidaGrupoMeasure,
       "caidaRedMeasure": caidaRedMeasure,
       "caidaGrupoConmMeasure": caidaGrupoConmMeasure,
       "measuresConmTable": measuresConmTable,
       "measuresConmEntry": measuresConmEntry,
       "measuresConmIndex": measuresConmIndex,
       "mainsFreqConm": mainsFreqConm,
       "mainsVL12Conm": mainsVL12Conm,
       "mainsVL23Conm": mainsVL23Conm,
       "mainsVL13Conm": mainsVL13Conm,
       "mainsVL1NConm": mainsVL1NConm,
       "mainsVL2NConm": mainsVL2NConm,
       "mainsVL3NConm": mainsVL3NConm,
       "genFreqConm": genFreqConm,
       "genVL12Conm": genVL12Conm,
       "genVL23Conm": genVL23Conm,
       "genVL13Conm": genVL13Conm,
       "genVL1NConm": genVL1NConm,
       "genVL2NConm": genVL2NConm,
       "genVL3NConm": genVL3NConm,
       "ph1AmpConm": ph1AmpConm,
       "ph2AmpConm": ph2AmpConm,
       "ph3AmpConm": ph3AmpConm,
       "flagsCurrentConm": flagsCurrentConm,
       "pFCTotalConm": pFCTotalConm,
       "pFC1Conm": pFC1Conm,
       "pFC2Conm": pFC2Conm,
       "pFC3Conm": pFC3Conm,
       "realPowConm": realPowConm,
       "appPowConm": appPowConm,
       "reactPowConm": reactPowConm,
       "mainsControlType": mainsControlType,
       "statusConm": statusConm,
       "alarmBitMapConm": alarmBitMapConm,
       "parameters": parameters,
       "startsCount": startsCount,
       "timeBetweenStarts": timeBetweenStarts,
       "startDelay": startDelay,
       "preheatingTime": preheatingTime,
       "startupTime": startupTime,
       "loadActivationTime": loadActivationTime,
       "nominalConditionTime": nominalConditionTime,
       "dplusActivationTime": dplusActivationTime,
       "eJP1ActivationDelayTime": eJP1ActivationDelayTime,
       "mainsActivationDelay": mainsActivationDelay,
       "coolingTime": coolingTime,
       "pEActivationTime": pEActivationTime,
       "counterDetectionTime": counterDetectionTime,
       "maximumAlarmActivationTime": maximumAlarmActivationTime,
       "phaseNumber": phaseNumber,
       "maxGensetVoltage": maxGensetVoltage,
       "minGensetVoltage": minGensetVoltage,
       "maxGensetAsymetryValue": maxGensetAsymetryValue,
       "maxGensetFrequency": maxGensetFrequency,
       "minGensetFrequency": minGensetFrequency,
       "maxGensetCurrent": maxGensetCurrent,
       "shortCircuitDetection": shortCircuitDetection,
       "gensetNominalPower": gensetNominalPower,
       "maxReversePower": maxReversePower,
       "maxPickupSpeed": maxPickupSpeed,
       "minPickupSpeed": minPickupSpeed,
       "maxMainsVoltage": maxMainsVoltage,
       "minMainsVoltage": minMainsVoltage,
       "maxMainsFrequency": maxMainsFrequency,
       "minMainsFrequency": minMainsFrequency,
       "minBatteryVoltage": minBatteryVoltage,
       "transferPumpMinLevel": transferPumpMinLevel,
       "transferPumpMaxLevel": transferPumpMaxLevel,
       "startingVoltageGensetSignal": startingVoltageGensetSignal,
       "startingVoltageAlternator": startingVoltageAlternator,
       "startingSpeed": startingSpeed,
       "engineFlywheelTeeth": engineFlywheelTeeth,
       "fuelReserveLevel": fuelReserveLevel,
       "lowOilPressure": lowOilPressure,
       "highWaterTemperatureThreshold": highWaterTemperatureThreshold,
       "lowEngineTemperature": lowEngineTemperature,
       "minPreheatingTemp": minPreheatingTemp,
       "maxPreheatingTemp": maxPreheatingTemp,
       "deviceIpAddress": deviceIpAddress,
       "deviceMaskSubnet": deviceMaskSubnet,
       "deviceGateway": deviceGateway,
       "managerAddress": managerAddress,
       "agentSNMPPort": agentSNMPPort,
       "managertrapsPort": managertrapsPort,
       "reset": reset,
       "version": version,
       "gensetStartStop": gensetStartStop,
       "gensetMode": gensetMode,
       "mainsBreakerStatus": mainsBreakerStatus,
       "gensetBreakerStatus": gensetBreakerStatus,
       "parametersConmTable": parametersConmTable,
       "parametersConmEntry": parametersConmEntry,
       "parametersConmIndex": parametersConmIndex,
       "phaseNumberConm": phaseNumberConm,
       "maxGensetVoltageConm": maxGensetVoltageConm,
       "minGensetVoltageConm": minGensetVoltageConm,
       "maxGensetAsymetryValueConm": maxGensetAsymetryValueConm,
       "maxGensetFrequencyConm": maxGensetFrequencyConm,
       "minGensetFrequencyConm": minGensetFrequencyConm,
       "maxGensetCurrentConm": maxGensetCurrentConm,
       "shortCircuitDetectionConm": shortCircuitDetectionConm,
       "gensetNominalPowerConm": gensetNominalPowerConm,
       "maxReversePowerConm": maxReversePowerConm,
       "maxPickupSpeedConm": maxPickupSpeedConm,
       "minPickupSpeedConm": minPickupSpeedConm,
       "maxMainsVoltageConm": maxMainsVoltageConm,
       "minMainsVoltageConm": minMainsVoltageConm,
       "maxMainsFrequencyConm": maxMainsFrequencyConm,
       "minMainsFrequencyConm": minMainsFrequencyConm,
       "startingVoltageValueConm": startingVoltageValueConm,
       "traps": traps,
       "alarmString": alarmString,
       "falloArranque": falloArranque,
       "nivelCombustible": nivelCombustible,
       "caidaGrupo": caidaGrupo,
       "caidaRed": caidaRed,
       "caidaGrupoConm": caidaGrupoConm}
)
