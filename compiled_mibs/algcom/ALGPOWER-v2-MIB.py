# SNMP MIB module (ALGPOWER-v2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\algcom\ALGPOWER-v2
# Produced by pysmi-1.6.2 at Thu Oct  2 11:17:14 2025
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Algcom_ObjectIdentity = ObjectIdentity
algcom = _Algcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136)
)
_UpsObjects_ObjectIdentity = ObjectIdentity
upsObjects = _UpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1)
)
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1, 1)
)
_OutputVoltage_Type = Integer32
_OutputVoltage_Object = MibScalar
outputVoltage = _OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 1, 1),
    _OutputVoltage_Type()
)
outputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltage.setStatus("mandatory")
_OutputCurrent_Type = Integer32
_OutputCurrent_Object = MibScalar
outputCurrent = _OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 1, 2),
    _OutputCurrent_Type()
)
outputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrent.setStatus("mandatory")
_OidNotUsed0_Type = Integer32
_OidNotUsed0_Object = MibScalar
oidNotUsed0 = _OidNotUsed0_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 1, 3),
    _OidNotUsed0_Type()
)
oidNotUsed0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oidNotUsed0.setStatus("mandatory")
_OidNotUsed1_Type = Integer32
_OidNotUsed1_Object = MibScalar
oidNotUsed1 = _OidNotUsed1_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 1, 4),
    _OidNotUsed1_Type()
)
oidNotUsed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oidNotUsed1.setStatus("mandatory")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1, 2)
)
_BatteryVoltage_Type = Integer32
_BatteryVoltage_Object = MibScalar
batteryVoltage = _BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 2, 1),
    _BatteryVoltage_Type()
)
batteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltage.setStatus("mandatory")
_BatteryCurrent_Type = Integer32
_BatteryCurrent_Object = MibScalar
batteryCurrent = _BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 2, 2),
    _BatteryCurrent_Type()
)
batteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrent.setStatus("mandatory")
_ChargerStatus_Type = Integer32
_ChargerStatus_Object = MibScalar
chargerStatus = _ChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 2, 3),
    _ChargerStatus_Type()
)
chargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chargerStatus.setStatus("mandatory")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3)
)
_AlarmOnBattery_Type = Integer32
_AlarmOnBattery_Object = MibScalar
alarmOnBattery = _AlarmOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 1),
    _AlarmOnBattery_Type()
)
alarmOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmOnBattery.setStatus("mandatory")
_AcFail_Type = Integer32
_AcFail_Object = MibScalar
acFail = _AcFail_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 2),
    _AcFail_Type()
)
acFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acFail.setStatus("mandatory")
_BatteryCharging_Type = Integer32
_BatteryCharging_Object = MibScalar
batteryCharging = _BatteryCharging_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 3),
    _BatteryCharging_Type()
)
batteryCharging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCharging.setStatus("mandatory")
_BatteryDischarging_Type = Integer32
_BatteryDischarging_Object = MibScalar
batteryDischarging = _BatteryDischarging_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 4),
    _BatteryDischarging_Type()
)
batteryDischarging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryDischarging.setStatus("mandatory")
_Overheat_Type = Integer32
_Overheat_Object = MibScalar
overheat = _Overheat_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 5),
    _Overheat_Type()
)
overheat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overheat.setStatus("mandatory")
_Overload_Type = Integer32
_Overload_Object = MibScalar
overload = _Overload_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 6),
    _Overload_Type()
)
overload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overload.setStatus("mandatory")
_FanAfail_Type = Integer32
_FanAfail_Object = MibScalar
fanAfail = _FanAfail_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 7),
    _FanAfail_Type()
)
fanAfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanAfail.setStatus("mandatory")
_FanBfail_Type = Integer32
_FanBfail_Object = MibScalar
fanBfail = _FanBfail_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 8),
    _FanBfail_Type()
)
fanBfail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanBfail.setStatus("mandatory")
_OidNotUsed2_Type = Integer32
_OidNotUsed2_Object = MibScalar
oidNotUsed2 = _OidNotUsed2_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 9),
    _OidNotUsed2_Type()
)
oidNotUsed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oidNotUsed2.setStatus("mandatory")
_OidNotUsed3_Type = Integer32
_OidNotUsed3_Object = MibScalar
oidNotUsed3 = _OidNotUsed3_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 10),
    _OidNotUsed3_Type()
)
oidNotUsed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oidNotUsed3.setStatus("mandatory")
_UpTime_Type = Integer32
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 3, 11),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("mandatory")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1, 4)
)
_InnerTemperature_Type = Integer32
_InnerTemperature_Object = MibScalar
innerTemperature = _InnerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 4, 1),
    _InnerTemperature_Type()
)
innerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innerTemperature.setStatus("mandatory")
_OuterTemperature_Type = Integer32
_OuterTemperature_Object = MibScalar
outerTemperature = _OuterTemperature_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 4, 2),
    _OuterTemperature_Type()
)
outerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outerTemperature.setStatus("mandatory")
_HeatSinkTemperature_Type = Integer32
_HeatSinkTemperature_Object = MibScalar
heatSinkTemperature = _HeatSinkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 4, 3),
    _HeatSinkTemperature_Type()
)
heatSinkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heatSinkTemperature.setStatus("mandatory")
_Watchdog_ObjectIdentity = ObjectIdentity
watchdog = _Watchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5)
)
_WatchdogPing1_Type = Integer32
_WatchdogPing1_Object = MibScalar
watchdogPing1 = _WatchdogPing1_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 1),
    _WatchdogPing1_Type()
)
watchdogPing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing1.setStatus("mandatory")
_WatchdogPing2_Type = Integer32
_WatchdogPing2_Object = MibScalar
watchdogPing2 = _WatchdogPing2_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 2),
    _WatchdogPing2_Type()
)
watchdogPing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing2.setStatus("mandatory")
_WatchdogPing3_Type = Integer32
_WatchdogPing3_Object = MibScalar
watchdogPing3 = _WatchdogPing3_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 3),
    _WatchdogPing3_Type()
)
watchdogPing3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing3.setStatus("mandatory")
_WatchdogPing4_Type = Integer32
_WatchdogPing4_Object = MibScalar
watchdogPing4 = _WatchdogPing4_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 4),
    _WatchdogPing4_Type()
)
watchdogPing4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing4.setStatus("mandatory")
_WatchdogPing5_Type = Integer32
_WatchdogPing5_Object = MibScalar
watchdogPing5 = _WatchdogPing5_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 5),
    _WatchdogPing5_Type()
)
watchdogPing5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing5.setStatus("mandatory")
_WatchdogPing6_Type = Integer32
_WatchdogPing6_Object = MibScalar
watchdogPing6 = _WatchdogPing6_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 6),
    _WatchdogPing6_Type()
)
watchdogPing6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing6.setStatus("mandatory")
_WatchdogPing7_Type = Integer32
_WatchdogPing7_Object = MibScalar
watchdogPing7 = _WatchdogPing7_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 7),
    _WatchdogPing7_Type()
)
watchdogPing7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing7.setStatus("mandatory")
_WatchdogPing8_Type = Integer32
_WatchdogPing8_Object = MibScalar
watchdogPing8 = _WatchdogPing8_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 8),
    _WatchdogPing8_Type()
)
watchdogPing8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing8.setStatus("mandatory")
_WatchdogPing9_Type = Integer32
_WatchdogPing9_Object = MibScalar
watchdogPing9 = _WatchdogPing9_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 9),
    _WatchdogPing9_Type()
)
watchdogPing9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing9.setStatus("mandatory")
_WatchdogPing10_Type = Integer32
_WatchdogPing10_Object = MibScalar
watchdogPing10 = _WatchdogPing10_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 5, 10),
    _WatchdogPing10_Type()
)
watchdogPing10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogPing10.setStatus("mandatory")
_Supply_ObjectIdentity = ObjectIdentity
supply = _Supply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1, 6)
)
_SupplyVoltage_Type = Integer32
_SupplyVoltage_Object = MibScalar
supplyVoltage = _SupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 6, 1),
    _SupplyVoltage_Type()
)
supplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    supplyVoltage.setStatus("mandatory")
_Installation_ObjectIdentity = ObjectIdentity
installation = _Installation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7)
)


class _PopName_Type(DisplayString):
    """Custom type popName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )
    fixed_length = 30


_PopName_Type.__name__ = "DisplayString"
_PopName_Object = MibScalar
popName = _PopName_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7, 1),
    _PopName_Type()
)
popName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    popName.setStatus("mandatory")


class _FacilityAddr_Type(DisplayString):
    """Custom type facilityAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_FacilityAddr_Type.__name__ = "DisplayString"
_FacilityAddr_Object = MibScalar
facilityAddr = _FacilityAddr_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7, 2),
    _FacilityAddr_Type()
)
facilityAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityAddr.setStatus("mandatory")


class _FacilityCity_Type(DisplayString):
    """Custom type facilityCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )
    fixed_length = 30


_FacilityCity_Type.__name__ = "DisplayString"
_FacilityCity_Object = MibScalar
facilityCity = _FacilityCity_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7, 3),
    _FacilityCity_Type()
)
facilityCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    facilityCity.setStatus("mandatory")


class _InstDate_Type(DisplayString):
    """Custom type instDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_InstDate_Type.__name__ = "DisplayString"
_InstDate_Object = MibScalar
instDate = _InstDate_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7, 4),
    _InstDate_Type()
)
instDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instDate.setStatus("mandatory")
_BatCapacity_Type = Integer32
_BatCapacity_Object = MibScalar
batCapacity = _BatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7, 5),
    _BatCapacity_Type()
)
batCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batCapacity.setStatus("mandatory")


class _BatBrand_Type(DisplayString):
    """Custom type batBrand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )
    fixed_length = 30


_BatBrand_Type.__name__ = "DisplayString"
_BatBrand_Object = MibScalar
batBrand = _BatBrand_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7, 6),
    _BatBrand_Type()
)
batBrand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batBrand.setStatus("mandatory")


class _BatInstDate_Type(DisplayString):
    """Custom type batInstDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_BatInstDate_Type.__name__ = "DisplayString"
_BatInstDate_Object = MibScalar
batInstDate = _BatInstDate_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7, 7),
    _BatInstDate_Type()
)
batInstDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batInstDate.setStatus("mandatory")


class _RespPers_Type(DisplayString):
    """Custom type respPers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_RespPers_Type.__name__ = "DisplayString"
_RespPers_Object = MibScalar
respPers = _RespPers_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 7, 8),
    _RespPers_Type()
)
respPers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    respPers.setStatus("mandatory")
_Bat_tst_ObjectIdentity = ObjectIdentity
bat_tst = _Bat_tst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8)
)


class _Btst_date_Type(DisplayString):
    """Custom type btst_date based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_Btst_date_Type.__name__ = "DisplayString"
_Btst_date_Object = MibScalar
btst_date = _Btst_date_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8, 1),
    _Btst_date_Type()
)
btst_date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btst_date.setStatus("mandatory")
_Btst_status_Type = Integer32
_Btst_status_Object = MibScalar
btst_status = _Btst_status_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8, 2),
    _Btst_status_Type()
)
btst_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btst_status.setStatus("mandatory")
_Btst_duration_Type = Integer32
_Btst_duration_Object = MibScalar
btst_duration = _Btst_duration_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8, 3),
    _Btst_duration_Type()
)
btst_duration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btst_duration.setStatus("mandatory")
_Btst_elapsed_Type = Integer32
_Btst_elapsed_Object = MibScalar
btst_elapsed = _Btst_elapsed_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8, 4),
    _Btst_elapsed_Type()
)
btst_elapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btst_elapsed.setStatus("mandatory")
_Btst_volt_i_Type = Integer32
_Btst_volt_i_Object = MibScalar
btst_volt_i = _Btst_volt_i_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8, 5),
    _Btst_volt_i_Type()
)
btst_volt_i.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btst_volt_i.setStatus("mandatory")
_Btst_amp_i_Type = Integer32
_Btst_amp_i_Object = MibScalar
btst_amp_i = _Btst_amp_i_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8, 6),
    _Btst_amp_i_Type()
)
btst_amp_i.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btst_amp_i.setStatus("mandatory")
_Btst_volt_f_Type = Integer32
_Btst_volt_f_Object = MibScalar
btst_volt_f = _Btst_volt_f_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8, 7),
    _Btst_volt_f_Type()
)
btst_volt_f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btst_volt_f.setStatus("mandatory")
_Btst_amp_f_Type = Integer32
_Btst_amp_f_Object = MibScalar
btst_amp_f = _Btst_amp_f_Object(
    (1, 3, 6, 1, 4, 1, 49136, 1, 8, 8),
    _Btst_amp_f_Type()
)
btst_amp_f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    btst_amp_f.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALGPOWER-v2-MIB",
    **{"algcom": algcom,
       "upsObjects": upsObjects,
       "output": output,
       "outputVoltage": outputVoltage,
       "outputCurrent": outputCurrent,
       "oidNotUsed0": oidNotUsed0,
       "oidNotUsed1": oidNotUsed1,
       "battery": battery,
       "batteryVoltage": batteryVoltage,
       "batteryCurrent": batteryCurrent,
       "chargerStatus": chargerStatus,
       "input": input,
       "alarmOnBattery": alarmOnBattery,
       "acFail": acFail,
       "batteryCharging": batteryCharging,
       "batteryDischarging": batteryDischarging,
       "overheat": overheat,
       "overload": overload,
       "fanAfail": fanAfail,
       "fanBfail": fanBfail,
       "oidNotUsed2": oidNotUsed2,
       "oidNotUsed3": oidNotUsed3,
       "upTime": upTime,
       "temperature": temperature,
       "innerTemperature": innerTemperature,
       "outerTemperature": outerTemperature,
       "heatSinkTemperature": heatSinkTemperature,
       "watchdog": watchdog,
       "watchdogPing1": watchdogPing1,
       "watchdogPing2": watchdogPing2,
       "watchdogPing3": watchdogPing3,
       "watchdogPing4": watchdogPing4,
       "watchdogPing5": watchdogPing5,
       "watchdogPing6": watchdogPing6,
       "watchdogPing7": watchdogPing7,
       "watchdogPing8": watchdogPing8,
       "watchdogPing9": watchdogPing9,
       "watchdogPing10": watchdogPing10,
       "supply": supply,
       "supplyVoltage": supplyVoltage,
       "installation": installation,
       "popName": popName,
       "facilityAddr": facilityAddr,
       "facilityCity": facilityCity,
       "instDate": instDate,
       "batCapacity": batCapacity,
       "batBrand": batBrand,
       "batInstDate": batInstDate,
       "respPers": respPers,
       "bat-tst": bat_tst,
       "btst-date": btst_date,
       "btst-status": btst_status,
       "btst-duration": btst_duration,
       "btst-elapsed": btst_elapsed,
       "btst-volt-i": btst_volt_i,
       "btst-amp-i": btst_amp_i,
       "btst-volt-f": btst_volt_f,
       "btst-amp-f": btst_amp_f}
)
