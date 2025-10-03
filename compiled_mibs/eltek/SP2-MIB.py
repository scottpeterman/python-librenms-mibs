# SNMP MIB module (SP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\eltek\SP2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:16 2025
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

(eltek,) = mibBuilder.importSymbols(
    "ELTEK-COMMON-MIB",
    "eltek")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ENexus_ObjectIdentity = ObjectIdentity
eNexus = _ENexus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10)
)
_EltekTraps_ObjectIdentity = ObjectIdentity
eltekTraps = _EltekTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1)
)
_PowerAlarmVars_ObjectIdentity = ObjectIdentity
powerAlarmVars = _PowerAlarmVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1)
)


class _AlarmSubsysSourceDescr_Type(DisplayString):
    """Custom type alarmSubsysSourceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlarmSubsysSourceDescr_Type.__name__ = "DisplayString"
_AlarmSubsysSourceDescr_Object = MibScalar
alarmSubsysSourceDescr = _AlarmSubsysSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 1),
    _AlarmSubsysSourceDescr_Type()
)
alarmSubsysSourceDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubsysSourceDescr.setStatus("current")
_AlarmSubsysStatusOid_Type = ObjectIdentifier
_AlarmSubsysStatusOid_Object = MibScalar
alarmSubsysStatusOid = _AlarmSubsysStatusOid_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 2),
    _AlarmSubsysStatusOid_Type()
)
alarmSubsysStatusOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubsysStatusOid.setStatus("current")


class _AlarmSubsysStatusValue_Type(Integer32):
    """Custom type alarmSubsysStatusValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_AlarmSubsysStatusValue_Type.__name__ = "Integer32"
_AlarmSubsysStatusValue_Object = MibScalar
alarmSubsysStatusValue = _AlarmSubsysStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 3),
    _AlarmSubsysStatusValue_Type()
)
alarmSubsysStatusValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubsysStatusValue.setStatus("current")


class _AlarmSubsysStatusOnOff_Type(Integer32):
    """Custom type alarmSubsysStatusOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlarmSubsysStatusOnOff_Type.__name__ = "Integer32"
_AlarmSubsysStatusOnOff_Object = MibScalar
alarmSubsysStatusOnOff = _AlarmSubsysStatusOnOff_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 4),
    _AlarmSubsysStatusOnOff_Type()
)
alarmSubsysStatusOnOff.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSubsysStatusOnOff.setStatus("current")
_AlarmMeasuredVarOid_Type = ObjectIdentifier
_AlarmMeasuredVarOid_Object = MibScalar
alarmMeasuredVarOid = _AlarmMeasuredVarOid_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 5),
    _AlarmMeasuredVarOid_Type()
)
alarmMeasuredVarOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmMeasuredVarOid.setStatus("current")
_AlarmMeasuredVarValue_Type = Integer32
_AlarmMeasuredVarValue_Object = MibScalar
alarmMeasuredVarValue = _AlarmMeasuredVarValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 6),
    _AlarmMeasuredVarValue_Type()
)
alarmMeasuredVarValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmMeasuredVarValue.setStatus("current")
_AlarmTrapCounterVarValue_Type = Integer32
_AlarmTrapCounterVarValue_Object = MibScalar
alarmTrapCounterVarValue = _AlarmTrapCounterVarValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 1, 7),
    _AlarmTrapCounterVarValue_Type()
)
alarmTrapCounterVarValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmTrapCounterVarValue.setStatus("current")
_PowerSystemTraps_ObjectIdentity = ObjectIdentity
powerSystemTraps = _PowerSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2)
)
_PowerSystem_ObjectIdentity = ObjectIdentity
powerSystem = _PowerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2)
)


class _PowerSystemStatus_Type(Integer32):
    """Custom type powerSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_PowerSystemStatus_Type.__name__ = "Integer32"
_PowerSystemStatus_Object = MibScalar
powerSystemStatus = _PowerSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 1),
    _PowerSystemStatus_Type()
)
powerSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemStatus.setStatus("current")


class _PowerSystemType_Type(Integer32):
    """Custom type powerSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("smartpack2", 1),
          ("smartpackS", 2),
          ("compack", 3))
    )


_PowerSystemType_Type.__name__ = "Integer32"
_PowerSystemType_Object = MibScalar
powerSystemType = _PowerSystemType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 2),
    _PowerSystemType_Type()
)
powerSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemType.setStatus("current")


class _PowerSystemMode_Type(Integer32):
    """Custom type powerSystemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("test", 1),
          ("boost", 2),
          ("float", 3),
          ("emergency", 4),
          ("startupdelay", 5),
          ("equalize", 6))
    )


_PowerSystemMode_Type.__name__ = "Integer32"
_PowerSystemMode_Object = MibScalar
powerSystemMode = _PowerSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 3),
    _PowerSystemMode_Type()
)
powerSystemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemMode.setStatus("current")


class _PowerSystemCompany_Type(DisplayString):
    """Custom type powerSystemCompany based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PowerSystemCompany_Type.__name__ = "DisplayString"
_PowerSystemCompany_Object = MibScalar
powerSystemCompany = _PowerSystemCompany_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 4),
    _PowerSystemCompany_Type()
)
powerSystemCompany.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemCompany.setStatus("current")


class _PowerSystemSite_Type(DisplayString):
    """Custom type powerSystemSite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PowerSystemSite_Type.__name__ = "DisplayString"
_PowerSystemSite_Object = MibScalar
powerSystemSite = _PowerSystemSite_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 5),
    _PowerSystemSite_Type()
)
powerSystemSite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemSite.setStatus("current")


class _PowerSystemModel_Type(DisplayString):
    """Custom type powerSystemModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PowerSystemModel_Type.__name__ = "DisplayString"
_PowerSystemModel_Object = MibScalar
powerSystemModel = _PowerSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 6),
    _PowerSystemModel_Type()
)
powerSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemModel.setStatus("current")


class _PowerSystemSerialNumber_Type(DisplayString):
    """Custom type powerSystemSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PowerSystemSerialNumber_Type.__name__ = "DisplayString"
_PowerSystemSerialNumber_Object = MibScalar
powerSystemSerialNumber = _PowerSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 7),
    _PowerSystemSerialNumber_Type()
)
powerSystemSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemSerialNumber.setStatus("current")
_PowerSystemInstallDate_Type = DateAndTime
_PowerSystemInstallDate_Object = MibScalar
powerSystemInstallDate = _PowerSystemInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 8),
    _PowerSystemInstallDate_Type()
)
powerSystemInstallDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemInstallDate.setStatus("current")
_PowerSystemNominalVoltage_Type = Integer32
_PowerSystemNominalVoltage_Object = MibScalar
powerSystemNominalVoltage = _PowerSystemNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 9),
    _PowerSystemNominalVoltage_Type()
)
powerSystemNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSystemNominalVoltage.setStatus("current")


class _PowerSystemLongitude_Type(Integer32):
    """Custom type powerSystemLongitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180, 180),
    )


_PowerSystemLongitude_Type.__name__ = "Integer32"
_PowerSystemLongitude_Object = MibScalar
powerSystemLongitude = _PowerSystemLongitude_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 10),
    _PowerSystemLongitude_Type()
)
powerSystemLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemLongitude.setStatus("current")
_PowerSystemLongitudeDecimal_Type = Integer32
_PowerSystemLongitudeDecimal_Object = MibScalar
powerSystemLongitudeDecimal = _PowerSystemLongitudeDecimal_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 11),
    _PowerSystemLongitudeDecimal_Type()
)
powerSystemLongitudeDecimal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemLongitudeDecimal.setStatus("current")


class _PowerSystemLatitude_Type(Integer32):
    """Custom type powerSystemLatitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 90),
    )


_PowerSystemLatitude_Type.__name__ = "Integer32"
_PowerSystemLatitude_Object = MibScalar
powerSystemLatitude = _PowerSystemLatitude_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 12),
    _PowerSystemLatitude_Type()
)
powerSystemLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemLatitude.setStatus("current")
_PowerSystemLatitudeDecimal_Type = Integer32
_PowerSystemLatitudeDecimal_Object = MibScalar
powerSystemLatitudeDecimal = _PowerSystemLatitudeDecimal_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 13),
    _PowerSystemLatitudeDecimal_Type()
)
powerSystemLatitudeDecimal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemLatitudeDecimal.setStatus("current")
_PowerSystemElevation_Type = Integer32
_PowerSystemElevation_Object = MibScalar
powerSystemElevation = _PowerSystemElevation_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 14),
    _PowerSystemElevation_Type()
)
powerSystemElevation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemElevation.setStatus("current")


class _PowerSystemCurrentDecimalSetting_Type(Integer32):
    """Custom type powerSystemCurrentDecimalSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ampere", 0),
          ("deciAmpere", 1))
    )


_PowerSystemCurrentDecimalSetting_Type.__name__ = "Integer32"
_PowerSystemCurrentDecimalSetting_Object = MibScalar
powerSystemCurrentDecimalSetting = _PowerSystemCurrentDecimalSetting_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 15),
    _PowerSystemCurrentDecimalSetting_Type()
)
powerSystemCurrentDecimalSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemCurrentDecimalSetting.setStatus("current")


class _PowerSystemTemperatureScale_Type(Integer32):
    """Custom type powerSystemTemperatureScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("celcius", 0),
          ("fahrenheit", 1))
    )


_PowerSystemTemperatureScale_Type.__name__ = "Integer32"
_PowerSystemTemperatureScale_Object = MibScalar
powerSystemTemperatureScale = _PowerSystemTemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 16),
    _PowerSystemTemperatureScale_Type()
)
powerSystemTemperatureScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemTemperatureScale.setStatus("current")


class _PowerSystemCapacityScale_Type(Integer32):
    """Custom type powerSystemCapacityScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ah", 0),
          ("percent", 1))
    )


_PowerSystemCapacityScale_Type.__name__ = "Integer32"
_PowerSystemCapacityScale_Object = MibScalar
powerSystemCapacityScale = _PowerSystemCapacityScale_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 2, 17),
    _PowerSystemCapacityScale_Type()
)
powerSystemCapacityScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSystemCapacityScale.setStatus("current")
_Mains_ObjectIdentity = ObjectIdentity
mains = _Mains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3)
)


class _MainsStatus_Type(Integer32):
    """Custom type mainsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsStatus_Type.__name__ = "Integer32"
_MainsStatus_Object = MibScalar
mainsStatus = _MainsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 1),
    _MainsStatus_Type()
)
mainsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsStatus.setStatus("current")
_MainsMainsFailure_ObjectIdentity = ObjectIdentity
mainsMainsFailure = _MainsMainsFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2)
)


class _MainsMainsFailureStatus_Type(Integer32):
    """Custom type mainsMainsFailureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsMainsFailureStatus_Type.__name__ = "Integer32"
_MainsMainsFailureStatus_Object = MibScalar
mainsMainsFailureStatus = _MainsMainsFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 1),
    _MainsMainsFailureStatus_Type()
)
mainsMainsFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMainsFailureStatus.setStatus("current")


class _MainsMainsFailureDescription_Type(DisplayString):
    """Custom type mainsMainsFailureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsMainsFailureDescription_Type.__name__ = "DisplayString"
_MainsMainsFailureDescription_Object = MibScalar
mainsMainsFailureDescription = _MainsMainsFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 2),
    _MainsMainsFailureDescription_Type()
)
mainsMainsFailureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMainsFailureDescription.setStatus("current")
_MainsMainsFailureTrapRepeatCounter_Type = Integer32
_MainsMainsFailureTrapRepeatCounter_Object = MibScalar
mainsMainsFailureTrapRepeatCounter = _MainsMainsFailureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 3),
    _MainsMainsFailureTrapRepeatCounter_Type()
)
mainsMainsFailureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMainsFailureTrapRepeatCounter.setStatus("current")


class _MainsMainsFailureAlarmEnable_Type(Integer32):
    """Custom type mainsMainsFailureAlarmEnable based on Integer32"""
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


_MainsMainsFailureAlarmEnable_Type.__name__ = "Integer32"
_MainsMainsFailureAlarmEnable_Object = MibScalar
mainsMainsFailureAlarmEnable = _MainsMainsFailureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 4),
    _MainsMainsFailureAlarmEnable_Type()
)
mainsMainsFailureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMainsFailureAlarmEnable.setStatus("current")
_MainsMainsFailureValue_Type = Integer32
_MainsMainsFailureValue_Object = MibScalar
mainsMainsFailureValue = _MainsMainsFailureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 5),
    _MainsMainsFailureValue_Type()
)
mainsMainsFailureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMainsFailureValue.setStatus("current")
_MainsMainsFailureMajorAlarmLevel_Type = Integer32
_MainsMainsFailureMajorAlarmLevel_Object = MibScalar
mainsMainsFailureMajorAlarmLevel = _MainsMainsFailureMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 6),
    _MainsMainsFailureMajorAlarmLevel_Type()
)
mainsMainsFailureMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMainsFailureMajorAlarmLevel.setStatus("current")
_MainsMainsFailureMinorAlarmLevel_Type = Integer32
_MainsMainsFailureMinorAlarmLevel_Object = MibScalar
mainsMainsFailureMinorAlarmLevel = _MainsMainsFailureMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 2, 7),
    _MainsMainsFailureMinorAlarmLevel_Type()
)
mainsMainsFailureMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMainsFailureMinorAlarmLevel.setStatus("current")
_MainsNumberOfPhases_Type = Integer32
_MainsNumberOfPhases_Object = MibScalar
mainsNumberOfPhases = _MainsNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 3),
    _MainsNumberOfPhases_Type()
)
mainsNumberOfPhases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsNumberOfPhases.setStatus("current")
_MainsVoltageTable_Object = MibTable
mainsVoltageTable = _MainsVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4)
)
if mibBuilder.loadTexts:
    mainsVoltageTable.setStatus("current")
_MainsVoltageEntry_Object = MibTableRow
mainsVoltageEntry = _MainsVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1)
)
mainsVoltageEntry.setIndexNames(
    (0, "SP2-MIB", "mainsVoltageIndex"),
)
if mibBuilder.loadTexts:
    mainsVoltageEntry.setStatus("current")


class _MainsVoltageIndex_Type(Integer32):
    """Custom type mainsVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_MainsVoltageIndex_Type.__name__ = "Integer32"
_MainsVoltageIndex_Object = MibTableColumn
mainsVoltageIndex = _MainsVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 1),
    _MainsVoltageIndex_Type()
)
mainsVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsVoltageIndex.setStatus("current")


class _MainsVoltageStatus_Type(Integer32):
    """Custom type mainsVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsVoltageStatus_Type.__name__ = "Integer32"
_MainsVoltageStatus_Object = MibTableColumn
mainsVoltageStatus = _MainsVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 2),
    _MainsVoltageStatus_Type()
)
mainsVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVoltageStatus.setStatus("current")


class _MainsVoltageDescription_Type(DisplayString):
    """Custom type mainsVoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsVoltageDescription_Type.__name__ = "DisplayString"
_MainsVoltageDescription_Object = MibTableColumn
mainsVoltageDescription = _MainsVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 3),
    _MainsVoltageDescription_Type()
)
mainsVoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageDescription.setStatus("current")
_MainsVoltageTrapRepeatCounter_Type = Counter32
_MainsVoltageTrapRepeatCounter_Object = MibTableColumn
mainsVoltageTrapRepeatCounter = _MainsVoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 4),
    _MainsVoltageTrapRepeatCounter_Type()
)
mainsVoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsVoltageTrapRepeatCounter.setStatus("current")


class _MainsVoltageAlarmEnable_Type(Integer32):
    """Custom type mainsVoltageAlarmEnable based on Integer32"""
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


_MainsVoltageAlarmEnable_Type.__name__ = "Integer32"
_MainsVoltageAlarmEnable_Object = MibTableColumn
mainsVoltageAlarmEnable = _MainsVoltageAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 5),
    _MainsVoltageAlarmEnable_Type()
)
mainsVoltageAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageAlarmEnable.setStatus("current")
_MainsVoltageValue_Type = Integer32
_MainsVoltageValue_Object = MibTableColumn
mainsVoltageValue = _MainsVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 6),
    _MainsVoltageValue_Type()
)
mainsVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsVoltageValue.setStatus("current")
_MainsVoltageMajorHighLevel_Type = Integer32
_MainsVoltageMajorHighLevel_Object = MibTableColumn
mainsVoltageMajorHighLevel = _MainsVoltageMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 7),
    _MainsVoltageMajorHighLevel_Type()
)
mainsVoltageMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageMajorHighLevel.setStatus("current")
_MainsVoltageMinorHighLevel_Type = Integer32
_MainsVoltageMinorHighLevel_Object = MibTableColumn
mainsVoltageMinorHighLevel = _MainsVoltageMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 8),
    _MainsVoltageMinorHighLevel_Type()
)
mainsVoltageMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageMinorHighLevel.setStatus("current")
_MainsVoltageMinorLowLevel_Type = Integer32
_MainsVoltageMinorLowLevel_Object = MibTableColumn
mainsVoltageMinorLowLevel = _MainsVoltageMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 9),
    _MainsVoltageMinorLowLevel_Type()
)
mainsVoltageMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageMinorLowLevel.setStatus("current")
_MainsVoltageMajorLowLevel_Type = Integer32
_MainsVoltageMajorLowLevel_Object = MibTableColumn
mainsVoltageMajorLowLevel = _MainsVoltageMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 4, 1, 10),
    _MainsVoltageMajorLowLevel_Type()
)
mainsVoltageMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsVoltageMajorLowLevel.setStatus("current")
_MainsMonitors_ObjectIdentity = ObjectIdentity
mainsMonitors = _MainsMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5)
)


class _MainsMonitorsNumberOfUnits_Type(Integer32):
    """Custom type mainsMonitorsNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_MainsMonitorsNumberOfUnits_Type.__name__ = "Integer32"
_MainsMonitorsNumberOfUnits_Object = MibScalar
mainsMonitorsNumberOfUnits = _MainsMonitorsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 1),
    _MainsMonitorsNumberOfUnits_Type()
)
mainsMonitorsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorsNumberOfUnits.setStatus("current")
_MainsMonitorsTable_Object = MibTable
mainsMonitorsTable = _MainsMonitorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2)
)
if mibBuilder.loadTexts:
    mainsMonitorsTable.setStatus("current")
_MainsMonitorsEntry_Object = MibTableRow
mainsMonitorsEntry = _MainsMonitorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1)
)
mainsMonitorsEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorsEntry.setStatus("current")


class _MainsMonitorIndex_Type(Integer32):
    """Custom type mainsMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_MainsMonitorIndex_Type.__name__ = "Integer32"
_MainsMonitorIndex_Object = MibTableColumn
mainsMonitorIndex = _MainsMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1, 1),
    _MainsMonitorIndex_Type()
)
mainsMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorIndex.setStatus("current")


class _MainsMonitorNumberOfVoltages_Type(Integer32):
    """Custom type mainsMonitorNumberOfVoltages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MainsMonitorNumberOfVoltages_Type.__name__ = "Integer32"
_MainsMonitorNumberOfVoltages_Object = MibTableColumn
mainsMonitorNumberOfVoltages = _MainsMonitorNumberOfVoltages_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1, 2),
    _MainsMonitorNumberOfVoltages_Type()
)
mainsMonitorNumberOfVoltages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorNumberOfVoltages.setStatus("current")


class _MainsMonitorNumberOfCurrents_Type(Integer32):
    """Custom type mainsMonitorNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MainsMonitorNumberOfCurrents_Type.__name__ = "Integer32"
_MainsMonitorNumberOfCurrents_Object = MibTableColumn
mainsMonitorNumberOfCurrents = _MainsMonitorNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1, 3),
    _MainsMonitorNumberOfCurrents_Type()
)
mainsMonitorNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorNumberOfCurrents.setStatus("current")


class _MainsMonitorNumberOfFrequencies_Type(Integer32):
    """Custom type mainsMonitorNumberOfFrequencies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MainsMonitorNumberOfFrequencies_Type.__name__ = "Integer32"
_MainsMonitorNumberOfFrequencies_Object = MibTableColumn
mainsMonitorNumberOfFrequencies = _MainsMonitorNumberOfFrequencies_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 2, 1, 4),
    _MainsMonitorNumberOfFrequencies_Type()
)
mainsMonitorNumberOfFrequencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorNumberOfFrequencies.setStatus("current")
_MainsMonitorVoltageTable_Object = MibTable
mainsMonitorVoltageTable = _MainsMonitorVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3)
)
if mibBuilder.loadTexts:
    mainsMonitorVoltageTable.setStatus("current")
_MainsMonitorVoltageEntry_Object = MibTableRow
mainsMonitorVoltageEntry = _MainsMonitorVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1)
)
mainsMonitorVoltageEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorPhaseIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorVoltageEntry.setStatus("current")


class _MainsMonitorPhaseIndex_Type(Integer32):
    """Custom type mainsMonitorPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MainsMonitorPhaseIndex_Type.__name__ = "Integer32"
_MainsMonitorPhaseIndex_Object = MibTableColumn
mainsMonitorPhaseIndex = _MainsMonitorPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 1),
    _MainsMonitorPhaseIndex_Type()
)
mainsMonitorPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorPhaseIndex.setStatus("current")


class _MainsMonitorVoltageStatus_Type(Integer32):
    """Custom type mainsMonitorVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsMonitorVoltageStatus_Type.__name__ = "Integer32"
_MainsMonitorVoltageStatus_Object = MibTableColumn
mainsMonitorVoltageStatus = _MainsMonitorVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 2),
    _MainsMonitorVoltageStatus_Type()
)
mainsMonitorVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorVoltageStatus.setStatus("current")


class _MainsMonitorVoltageDescription_Type(DisplayString):
    """Custom type mainsMonitorVoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MainsMonitorVoltageDescription_Type.__name__ = "DisplayString"
_MainsMonitorVoltageDescription_Object = MibTableColumn
mainsMonitorVoltageDescription = _MainsMonitorVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 3),
    _MainsMonitorVoltageDescription_Type()
)
mainsMonitorVoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageDescription.setStatus("current")
_MainsMonitorVoltageTrapRepeatCounter_Type = Counter32
_MainsMonitorVoltageTrapRepeatCounter_Object = MibTableColumn
mainsMonitorVoltageTrapRepeatCounter = _MainsMonitorVoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 4),
    _MainsMonitorVoltageTrapRepeatCounter_Type()
)
mainsMonitorVoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMonitorVoltageTrapRepeatCounter.setStatus("current")


class _MainsMonitorVoltageAlarmEnable_Type(Integer32):
    """Custom type mainsMonitorVoltageAlarmEnable based on Integer32"""
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


_MainsMonitorVoltageAlarmEnable_Type.__name__ = "Integer32"
_MainsMonitorVoltageAlarmEnable_Object = MibTableColumn
mainsMonitorVoltageAlarmEnable = _MainsMonitorVoltageAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 5),
    _MainsMonitorVoltageAlarmEnable_Type()
)
mainsMonitorVoltageAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageAlarmEnable.setStatus("current")
_MainsMonitorVoltageValue_Type = Integer32
_MainsMonitorVoltageValue_Object = MibTableColumn
mainsMonitorVoltageValue = _MainsMonitorVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 6),
    _MainsMonitorVoltageValue_Type()
)
mainsMonitorVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorVoltageValue.setStatus("current")
_MainsMonitorVoltageMajorHighLevel_Type = Integer32
_MainsMonitorVoltageMajorHighLevel_Object = MibTableColumn
mainsMonitorVoltageMajorHighLevel = _MainsMonitorVoltageMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 7),
    _MainsMonitorVoltageMajorHighLevel_Type()
)
mainsMonitorVoltageMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageMajorHighLevel.setStatus("current")
_MainsMonitorVoltageMinorHighLevel_Type = Integer32
_MainsMonitorVoltageMinorHighLevel_Object = MibTableColumn
mainsMonitorVoltageMinorHighLevel = _MainsMonitorVoltageMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 8),
    _MainsMonitorVoltageMinorHighLevel_Type()
)
mainsMonitorVoltageMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageMinorHighLevel.setStatus("current")
_MainsMonitorVoltageMinorLowLevel_Type = Integer32
_MainsMonitorVoltageMinorLowLevel_Object = MibTableColumn
mainsMonitorVoltageMinorLowLevel = _MainsMonitorVoltageMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 9),
    _MainsMonitorVoltageMinorLowLevel_Type()
)
mainsMonitorVoltageMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageMinorLowLevel.setStatus("current")
_MainsMonitorVoltageMajorLowLevel_Type = Integer32
_MainsMonitorVoltageMajorLowLevel_Object = MibTableColumn
mainsMonitorVoltageMajorLowLevel = _MainsMonitorVoltageMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 3, 1, 10),
    _MainsMonitorVoltageMajorLowLevel_Type()
)
mainsMonitorVoltageMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorVoltageMajorLowLevel.setStatus("current")
_MainsMonitorCurrentTable_Object = MibTable
mainsMonitorCurrentTable = _MainsMonitorCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4)
)
if mibBuilder.loadTexts:
    mainsMonitorCurrentTable.setStatus("current")
_MainsMonitorCurrentEntry_Object = MibTableRow
mainsMonitorCurrentEntry = _MainsMonitorCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1)
)
mainsMonitorCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorPhaseIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorCurrentEntry.setStatus("current")


class _MainsMonitorCurrentStatus_Type(Integer32):
    """Custom type mainsMonitorCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsMonitorCurrentStatus_Type.__name__ = "Integer32"
_MainsMonitorCurrentStatus_Object = MibTableColumn
mainsMonitorCurrentStatus = _MainsMonitorCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 1),
    _MainsMonitorCurrentStatus_Type()
)
mainsMonitorCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorCurrentStatus.setStatus("current")


class _MainsMonitorCurrentDescription_Type(DisplayString):
    """Custom type mainsMonitorCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MainsMonitorCurrentDescription_Type.__name__ = "DisplayString"
_MainsMonitorCurrentDescription_Object = MibTableColumn
mainsMonitorCurrentDescription = _MainsMonitorCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 2),
    _MainsMonitorCurrentDescription_Type()
)
mainsMonitorCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorCurrentDescription.setStatus("current")
_MainsMonitorCurrentTrapRepeatCounter_Type = Counter32
_MainsMonitorCurrentTrapRepeatCounter_Object = MibTableColumn
mainsMonitorCurrentTrapRepeatCounter = _MainsMonitorCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 3),
    _MainsMonitorCurrentTrapRepeatCounter_Type()
)
mainsMonitorCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMonitorCurrentTrapRepeatCounter.setStatus("current")


class _MainsMonitorCurrentAlarmEnable_Type(Integer32):
    """Custom type mainsMonitorCurrentAlarmEnable based on Integer32"""
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


_MainsMonitorCurrentAlarmEnable_Type.__name__ = "Integer32"
_MainsMonitorCurrentAlarmEnable_Object = MibTableColumn
mainsMonitorCurrentAlarmEnable = _MainsMonitorCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 4),
    _MainsMonitorCurrentAlarmEnable_Type()
)
mainsMonitorCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorCurrentAlarmEnable.setStatus("current")
_MainsMonitorCurrentValue_Type = Integer32
_MainsMonitorCurrentValue_Object = MibTableColumn
mainsMonitorCurrentValue = _MainsMonitorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 5),
    _MainsMonitorCurrentValue_Type()
)
mainsMonitorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorCurrentValue.setStatus("current")
_MainsMonitorCurrentMajorHighLevel_Type = Integer32
_MainsMonitorCurrentMajorHighLevel_Object = MibTableColumn
mainsMonitorCurrentMajorHighLevel = _MainsMonitorCurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 6),
    _MainsMonitorCurrentMajorHighLevel_Type()
)
mainsMonitorCurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorCurrentMajorHighLevel.setStatus("current")
_MainsMonitorCurrentMinorHighLevel_Type = Integer32
_MainsMonitorCurrentMinorHighLevel_Object = MibTableColumn
mainsMonitorCurrentMinorHighLevel = _MainsMonitorCurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 4, 1, 7),
    _MainsMonitorCurrentMinorHighLevel_Type()
)
mainsMonitorCurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorCurrentMinorHighLevel.setStatus("current")
_MainsMonitorFrequencyTable_Object = MibTable
mainsMonitorFrequencyTable = _MainsMonitorFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5)
)
if mibBuilder.loadTexts:
    mainsMonitorFrequencyTable.setStatus("current")
_MainsMonitorFrequencyEntry_Object = MibTableRow
mainsMonitorFrequencyEntry = _MainsMonitorFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1)
)
mainsMonitorFrequencyEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorFrequencyEntry.setStatus("current")


class _MainsMonitorFrequencyStatus_Type(Integer32):
    """Custom type mainsMonitorFrequencyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsMonitorFrequencyStatus_Type.__name__ = "Integer32"
_MainsMonitorFrequencyStatus_Object = MibTableColumn
mainsMonitorFrequencyStatus = _MainsMonitorFrequencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 1),
    _MainsMonitorFrequencyStatus_Type()
)
mainsMonitorFrequencyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyStatus.setStatus("current")


class _MainsMonitorFrequencyDescription_Type(DisplayString):
    """Custom type mainsMonitorFrequencyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsMonitorFrequencyDescription_Type.__name__ = "DisplayString"
_MainsMonitorFrequencyDescription_Object = MibTableColumn
mainsMonitorFrequencyDescription = _MainsMonitorFrequencyDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 2),
    _MainsMonitorFrequencyDescription_Type()
)
mainsMonitorFrequencyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyDescription.setStatus("current")
_MainsMonitorFrequencyTrapRepeatCounter_Type = Counter32
_MainsMonitorFrequencyTrapRepeatCounter_Object = MibTableColumn
mainsMonitorFrequencyTrapRepeatCounter = _MainsMonitorFrequencyTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 3),
    _MainsMonitorFrequencyTrapRepeatCounter_Type()
)
mainsMonitorFrequencyTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyTrapRepeatCounter.setStatus("current")


class _MainsMonitorFrequencyAlarmEnable_Type(Integer32):
    """Custom type mainsMonitorFrequencyAlarmEnable based on Integer32"""
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


_MainsMonitorFrequencyAlarmEnable_Type.__name__ = "Integer32"
_MainsMonitorFrequencyAlarmEnable_Object = MibTableColumn
mainsMonitorFrequencyAlarmEnable = _MainsMonitorFrequencyAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 4),
    _MainsMonitorFrequencyAlarmEnable_Type()
)
mainsMonitorFrequencyAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyAlarmEnable.setStatus("current")
_MainsMonitorFrequencyValue_Type = Integer32
_MainsMonitorFrequencyValue_Object = MibTableColumn
mainsMonitorFrequencyValue = _MainsMonitorFrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 5),
    _MainsMonitorFrequencyValue_Type()
)
mainsMonitorFrequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyValue.setStatus("current")
_MainsMonitorFrequencyMajorHighLevel_Type = Integer32
_MainsMonitorFrequencyMajorHighLevel_Object = MibTableColumn
mainsMonitorFrequencyMajorHighLevel = _MainsMonitorFrequencyMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 6),
    _MainsMonitorFrequencyMajorHighLevel_Type()
)
mainsMonitorFrequencyMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyMajorHighLevel.setStatus("current")
_MainsMonitorFrequencyMinorHighLevel_Type = Integer32
_MainsMonitorFrequencyMinorHighLevel_Object = MibTableColumn
mainsMonitorFrequencyMinorHighLevel = _MainsMonitorFrequencyMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 7),
    _MainsMonitorFrequencyMinorHighLevel_Type()
)
mainsMonitorFrequencyMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyMinorHighLevel.setStatus("current")
_MainsMonitorFrequencyMinorLowLevel_Type = Integer32
_MainsMonitorFrequencyMinorLowLevel_Object = MibTableColumn
mainsMonitorFrequencyMinorLowLevel = _MainsMonitorFrequencyMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 8),
    _MainsMonitorFrequencyMinorLowLevel_Type()
)
mainsMonitorFrequencyMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyMinorLowLevel.setStatus("current")
_MainsMonitorFrequencyMajorLowLevel_Type = Integer32
_MainsMonitorFrequencyMajorLowLevel_Object = MibTableColumn
mainsMonitorFrequencyMajorLowLevel = _MainsMonitorFrequencyMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 5, 1, 9),
    _MainsMonitorFrequencyMajorLowLevel_Type()
)
mainsMonitorFrequencyMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorFrequencyMajorLowLevel.setStatus("current")
_MainsMonitorEnergyLogAccumulatedTable_Object = MibTable
mainsMonitorEnergyLogAccumulatedTable = _MainsMonitorEnergyLogAccumulatedTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 6)
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogAccumulatedTable.setStatus("current")
_MainsMonitorEnergyLogAccumulatedEntry_Object = MibTableRow
mainsMonitorEnergyLogAccumulatedEntry = _MainsMonitorEnergyLogAccumulatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 6, 1)
)
mainsMonitorEnergyLogAccumulatedEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogAccumulatedEntry.setStatus("current")
_MainsMonitorEnergyLogAccumulated_Type = Integer32
_MainsMonitorEnergyLogAccumulated_Object = MibTableColumn
mainsMonitorEnergyLogAccumulated = _MainsMonitorEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 6, 1, 1),
    _MainsMonitorEnergyLogAccumulated_Type()
)
mainsMonitorEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogAccumulated.setStatus("current")


class _MainsMonitorEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsMonitorEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastHoursNumberOfEntries_Object = MibScalar
mainsMonitorEnergyLogLastHoursNumberOfEntries = _MainsMonitorEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 7),
    _MainsMonitorEnergyLogLastHoursNumberOfEntries_Type()
)
mainsMonitorEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursNumberOfEntries.setStatus("current")
_MainsMonitorEnergyLogLastHoursTable_Object = MibTable
mainsMonitorEnergyLogLastHoursTable = _MainsMonitorEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 8)
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursTable.setStatus("current")
_MainsMonitorEnergyLogLastHoursEntry_Object = MibTableRow
mainsMonitorEnergyLogLastHoursEntry = _MainsMonitorEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 8, 1)
)
mainsMonitorEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursEntry.setStatus("current")


class _MainsMonitorEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsMonitorEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastHoursIndex_Object = MibTableColumn
mainsMonitorEnergyLogLastHoursIndex = _MainsMonitorEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 8, 1, 1),
    _MainsMonitorEnergyLogLastHoursIndex_Type()
)
mainsMonitorEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursIndex.setStatus("current")
_MainsMonitorEnergyLogLastHoursValue_Type = Integer32
_MainsMonitorEnergyLogLastHoursValue_Object = MibTableColumn
mainsMonitorEnergyLogLastHoursValue = _MainsMonitorEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 8, 1, 2),
    _MainsMonitorEnergyLogLastHoursValue_Type()
)
mainsMonitorEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastHoursValue.setStatus("current")


class _MainsMonitorEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsMonitorEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastDaysNumberOfEntries_Object = MibScalar
mainsMonitorEnergyLogLastDaysNumberOfEntries = _MainsMonitorEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 9),
    _MainsMonitorEnergyLogLastDaysNumberOfEntries_Type()
)
mainsMonitorEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysNumberOfEntries.setStatus("current")
_MainsMonitorEnergyLogLastDaysTable_Object = MibTable
mainsMonitorEnergyLogLastDaysTable = _MainsMonitorEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 10)
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysTable.setStatus("current")
_MainsMonitorEnergyLogLastDaysEntry_Object = MibTableRow
mainsMonitorEnergyLogLastDaysEntry = _MainsMonitorEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 10, 1)
)
mainsMonitorEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysEntry.setStatus("current")


class _MainsMonitorEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsMonitorEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastDaysIndex_Object = MibTableColumn
mainsMonitorEnergyLogLastDaysIndex = _MainsMonitorEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 10, 1, 1),
    _MainsMonitorEnergyLogLastDaysIndex_Type()
)
mainsMonitorEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysIndex.setStatus("current")
_MainsMonitorEnergyLogLastDaysValue_Type = Integer32
_MainsMonitorEnergyLogLastDaysValue_Object = MibTableColumn
mainsMonitorEnergyLogLastDaysValue = _MainsMonitorEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 10, 1, 2),
    _MainsMonitorEnergyLogLastDaysValue_Type()
)
mainsMonitorEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastDaysValue.setStatus("current")


class _MainsMonitorEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsMonitorEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
mainsMonitorEnergyLogLastWeeksNumberOfEntries = _MainsMonitorEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 11),
    _MainsMonitorEnergyLogLastWeeksNumberOfEntries_Type()
)
mainsMonitorEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_MainsMonitorEnergyLogLastWeeksTable_Object = MibTable
mainsMonitorEnergyLogLastWeeksTable = _MainsMonitorEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 12)
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksTable.setStatus("current")
_MainsMonitorEnergyLogLastWeeksEntry_Object = MibTableRow
mainsMonitorEnergyLogLastWeeksEntry = _MainsMonitorEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 12, 1)
)
mainsMonitorEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "mainsMonitorIndex"),
    (0, "SP2-MIB", "mainsMonitorEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksEntry.setStatus("current")


class _MainsMonitorEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type mainsMonitorEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsMonitorEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_MainsMonitorEnergyLogLastWeeksIndex_Object = MibTableColumn
mainsMonitorEnergyLogLastWeeksIndex = _MainsMonitorEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 12, 1, 1),
    _MainsMonitorEnergyLogLastWeeksIndex_Type()
)
mainsMonitorEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksIndex.setStatus("current")
_MainsMonitorEnergyLogLastWeeksValue_Type = Integer32
_MainsMonitorEnergyLogLastWeeksValue_Object = MibTableColumn
mainsMonitorEnergyLogLastWeeksValue = _MainsMonitorEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 5, 12, 1, 2),
    _MainsMonitorEnergyLogLastWeeksValue_Type()
)
mainsMonitorEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorEnergyLogLastWeeksValue.setStatus("current")
_MainsOutageLog_ObjectIdentity = ObjectIdentity
mainsOutageLog = _MainsOutageLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6)
)
_MainsOutageTotal_Type = Integer32
_MainsOutageTotal_Object = MibScalar
mainsOutageTotal = _MainsOutageTotal_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 1),
    _MainsOutageTotal_Type()
)
mainsOutageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageTotal.setStatus("current")


class _MainsOutageLogDaysNumberOfEntries_Type(Integer32):
    """Custom type mainsOutageLogDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsOutageLogDaysNumberOfEntries_Type.__name__ = "Integer32"
_MainsOutageLogDaysNumberOfEntries_Object = MibScalar
mainsOutageLogDaysNumberOfEntries = _MainsOutageLogDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 2),
    _MainsOutageLogDaysNumberOfEntries_Type()
)
mainsOutageLogDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogDaysNumberOfEntries.setStatus("current")
_MainsOutageLogDaysTable_Object = MibTable
mainsOutageLogDaysTable = _MainsOutageLogDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 3)
)
if mibBuilder.loadTexts:
    mainsOutageLogDaysTable.setStatus("current")
_MainsOutageLogDaysEntry_Object = MibTableRow
mainsOutageLogDaysEntry = _MainsOutageLogDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 3, 1)
)
mainsOutageLogDaysEntry.setIndexNames(
    (0, "SP2-MIB", "mainsOutageLogDaysIndex"),
)
if mibBuilder.loadTexts:
    mainsOutageLogDaysEntry.setStatus("current")


class _MainsOutageLogDaysIndex_Type(Integer32):
    """Custom type mainsOutageLogDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsOutageLogDaysIndex_Type.__name__ = "Integer32"
_MainsOutageLogDaysIndex_Object = MibTableColumn
mainsOutageLogDaysIndex = _MainsOutageLogDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 3, 1, 1),
    _MainsOutageLogDaysIndex_Type()
)
mainsOutageLogDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsOutageLogDaysIndex.setStatus("current")
_MainsOutageLogDaysValue_Type = Integer32
_MainsOutageLogDaysValue_Object = MibTableColumn
mainsOutageLogDaysValue = _MainsOutageLogDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 3, 1, 2),
    _MainsOutageLogDaysValue_Type()
)
mainsOutageLogDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogDaysValue.setStatus("current")


class _MainsOutageLogWeeksNumberOfEntries_Type(Integer32):
    """Custom type mainsOutageLogWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsOutageLogWeeksNumberOfEntries_Type.__name__ = "Integer32"
_MainsOutageLogWeeksNumberOfEntries_Object = MibScalar
mainsOutageLogWeeksNumberOfEntries = _MainsOutageLogWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 4),
    _MainsOutageLogWeeksNumberOfEntries_Type()
)
mainsOutageLogWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogWeeksNumberOfEntries.setStatus("current")
_MainsOutageLogWeeksTable_Object = MibTable
mainsOutageLogWeeksTable = _MainsOutageLogWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 5)
)
if mibBuilder.loadTexts:
    mainsOutageLogWeeksTable.setStatus("current")
_MainsOutageLogWeeksEntry_Object = MibTableRow
mainsOutageLogWeeksEntry = _MainsOutageLogWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 5, 1)
)
mainsOutageLogWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "mainsOutageLogWeeksIndex"),
)
if mibBuilder.loadTexts:
    mainsOutageLogWeeksEntry.setStatus("current")


class _MainsOutageLogWeeksIndex_Type(Integer32):
    """Custom type mainsOutageLogWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsOutageLogWeeksIndex_Type.__name__ = "Integer32"
_MainsOutageLogWeeksIndex_Object = MibTableColumn
mainsOutageLogWeeksIndex = _MainsOutageLogWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 5, 1, 1),
    _MainsOutageLogWeeksIndex_Type()
)
mainsOutageLogWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsOutageLogWeeksIndex.setStatus("current")
_MainsOutageLogWeeksValue_Type = Integer32
_MainsOutageLogWeeksValue_Object = MibTableColumn
mainsOutageLogWeeksValue = _MainsOutageLogWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 5, 1, 2),
    _MainsOutageLogWeeksValue_Type()
)
mainsOutageLogWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogWeeksValue.setStatus("current")


class _MainsOutageLogMonthsNumberOfEntries_Type(Integer32):
    """Custom type mainsOutageLogMonthsNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_MainsOutageLogMonthsNumberOfEntries_Type.__name__ = "Integer32"
_MainsOutageLogMonthsNumberOfEntries_Object = MibScalar
mainsOutageLogMonthsNumberOfEntries = _MainsOutageLogMonthsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 6),
    _MainsOutageLogMonthsNumberOfEntries_Type()
)
mainsOutageLogMonthsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogMonthsNumberOfEntries.setStatus("current")
_MainsOutageLogMonthsTable_Object = MibTable
mainsOutageLogMonthsTable = _MainsOutageLogMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 7)
)
if mibBuilder.loadTexts:
    mainsOutageLogMonthsTable.setStatus("current")
_MainsOutageLogMonthsEntry_Object = MibTableRow
mainsOutageLogMonthsEntry = _MainsOutageLogMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 7, 1)
)
mainsOutageLogMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "mainsOutageLogMonthsIndex"),
)
if mibBuilder.loadTexts:
    mainsOutageLogMonthsEntry.setStatus("current")


class _MainsOutageLogMonthsIndex_Type(Integer32):
    """Custom type mainsOutageLogMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsOutageLogMonthsIndex_Type.__name__ = "Integer32"
_MainsOutageLogMonthsIndex_Object = MibTableColumn
mainsOutageLogMonthsIndex = _MainsOutageLogMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 7, 1, 1),
    _MainsOutageLogMonthsIndex_Type()
)
mainsOutageLogMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsOutageLogMonthsIndex.setStatus("current")
_MainsOutageLogMonthsValue_Type = Integer32
_MainsOutageLogMonthsValue_Object = MibTableColumn
mainsOutageLogMonthsValue = _MainsOutageLogMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 6, 7, 1, 2),
    _MainsOutageLogMonthsValue_Type()
)
mainsOutageLogMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsOutageLogMonthsValue.setStatus("current")
_MainsNumberOfGroups_Type = Integer32
_MainsNumberOfGroups_Object = MibScalar
mainsNumberOfGroups = _MainsNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 7),
    _MainsNumberOfGroups_Type()
)
mainsNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsNumberOfGroups.setStatus("current")
_MainsGroupsTable_Object = MibTable
mainsGroupsTable = _MainsGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 8)
)
if mibBuilder.loadTexts:
    mainsGroupsTable.setStatus("current")
_MainsGroupsEntry_Object = MibTableRow
mainsGroupsEntry = _MainsGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 8, 1)
)
mainsGroupsEntry.setIndexNames(
    (0, "SP2-MIB", "mainsGroupIndex"),
)
if mibBuilder.loadTexts:
    mainsGroupsEntry.setStatus("current")


class _MainsGroupIndex_Type(Integer32):
    """Custom type mainsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MainsGroupIndex_Type.__name__ = "Integer32"
_MainsGroupIndex_Object = MibTableColumn
mainsGroupIndex = _MainsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 8, 1, 1),
    _MainsGroupIndex_Type()
)
mainsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsGroupIndex.setStatus("current")


class _MainsGroupStatus_Type(Integer32):
    """Custom type mainsGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsGroupStatus_Type.__name__ = "Integer32"
_MainsGroupStatus_Object = MibTableColumn
mainsGroupStatus = _MainsGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 8, 1, 2),
    _MainsGroupStatus_Type()
)
mainsGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupStatus.setStatus("current")
_MainsGroupNumberOfPhases_Type = Integer32
_MainsGroupNumberOfPhases_Object = MibTableColumn
mainsGroupNumberOfPhases = _MainsGroupNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 8, 1, 3),
    _MainsGroupNumberOfPhases_Type()
)
mainsGroupNumberOfPhases.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupNumberOfPhases.setStatus("current")
_MainsGroupMainsFailureTable_Object = MibTable
mainsGroupMainsFailureTable = _MainsGroupMainsFailureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9)
)
if mibBuilder.loadTexts:
    mainsGroupMainsFailureTable.setStatus("current")
_MainsGroupMainsFailureEntry_Object = MibTableRow
mainsGroupMainsFailureEntry = _MainsGroupMainsFailureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9, 1)
)
mainsGroupMainsFailureEntry.setIndexNames(
    (0, "SP2-MIB", "mainsGroupIndex"),
)
if mibBuilder.loadTexts:
    mainsGroupMainsFailureEntry.setStatus("current")


class _MainsGroupMainsFailureStatus_Type(Integer32):
    """Custom type mainsGroupMainsFailureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsGroupMainsFailureStatus_Type.__name__ = "Integer32"
_MainsGroupMainsFailureStatus_Object = MibTableColumn
mainsGroupMainsFailureStatus = _MainsGroupMainsFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9, 1, 1),
    _MainsGroupMainsFailureStatus_Type()
)
mainsGroupMainsFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupMainsFailureStatus.setStatus("current")


class _MainsGroupMainsFailureDescription_Type(DisplayString):
    """Custom type mainsGroupMainsFailureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsGroupMainsFailureDescription_Type.__name__ = "DisplayString"
_MainsGroupMainsFailureDescription_Object = MibTableColumn
mainsGroupMainsFailureDescription = _MainsGroupMainsFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9, 1, 2),
    _MainsGroupMainsFailureDescription_Type()
)
mainsGroupMainsFailureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupMainsFailureDescription.setStatus("current")
_MainsGroupMainsFailureTrapRepeatCounter_Type = Integer32
_MainsGroupMainsFailureTrapRepeatCounter_Object = MibTableColumn
mainsGroupMainsFailureTrapRepeatCounter = _MainsGroupMainsFailureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9, 1, 3),
    _MainsGroupMainsFailureTrapRepeatCounter_Type()
)
mainsGroupMainsFailureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsGroupMainsFailureTrapRepeatCounter.setStatus("current")


class _MainsGroupMainsFailureAlarmEnable_Type(Integer32):
    """Custom type mainsGroupMainsFailureAlarmEnable based on Integer32"""
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


_MainsGroupMainsFailureAlarmEnable_Type.__name__ = "Integer32"
_MainsGroupMainsFailureAlarmEnable_Object = MibTableColumn
mainsGroupMainsFailureAlarmEnable = _MainsGroupMainsFailureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9, 1, 4),
    _MainsGroupMainsFailureAlarmEnable_Type()
)
mainsGroupMainsFailureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupMainsFailureAlarmEnable.setStatus("current")
_MainsGroupMainsFailureValue_Type = Integer32
_MainsGroupMainsFailureValue_Object = MibTableColumn
mainsGroupMainsFailureValue = _MainsGroupMainsFailureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9, 1, 5),
    _MainsGroupMainsFailureValue_Type()
)
mainsGroupMainsFailureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupMainsFailureValue.setStatus("current")
_MainsGroupMainsFailureMajorAlarmLevel_Type = Integer32
_MainsGroupMainsFailureMajorAlarmLevel_Object = MibTableColumn
mainsGroupMainsFailureMajorAlarmLevel = _MainsGroupMainsFailureMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9, 1, 6),
    _MainsGroupMainsFailureMajorAlarmLevel_Type()
)
mainsGroupMainsFailureMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupMainsFailureMajorAlarmLevel.setStatus("current")
_MainsGroupMainsFailureMinorAlarmLevel_Type = Integer32
_MainsGroupMainsFailureMinorAlarmLevel_Object = MibTableColumn
mainsGroupMainsFailureMinorAlarmLevel = _MainsGroupMainsFailureMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 9, 1, 7),
    _MainsGroupMainsFailureMinorAlarmLevel_Type()
)
mainsGroupMainsFailureMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupMainsFailureMinorAlarmLevel.setStatus("current")
_MainsGroupVoltageTable_Object = MibTable
mainsGroupVoltageTable = _MainsGroupVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10)
)
if mibBuilder.loadTexts:
    mainsGroupVoltageTable.setStatus("current")
_MainsGroupVoltageEntry_Object = MibTableRow
mainsGroupVoltageEntry = _MainsGroupVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1)
)
mainsGroupVoltageEntry.setIndexNames(
    (0, "SP2-MIB", "mainsGroupIndex"),
    (0, "SP2-MIB", "mainsGroupVoltageIndex"),
)
if mibBuilder.loadTexts:
    mainsGroupVoltageEntry.setStatus("current")


class _MainsGroupVoltageIndex_Type(Integer32):
    """Custom type mainsGroupVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_MainsGroupVoltageIndex_Type.__name__ = "Integer32"
_MainsGroupVoltageIndex_Object = MibTableColumn
mainsGroupVoltageIndex = _MainsGroupVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 1),
    _MainsGroupVoltageIndex_Type()
)
mainsGroupVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsGroupVoltageIndex.setStatus("current")


class _MainsGroupVoltageStatus_Type(Integer32):
    """Custom type mainsGroupVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsGroupVoltageStatus_Type.__name__ = "Integer32"
_MainsGroupVoltageStatus_Object = MibTableColumn
mainsGroupVoltageStatus = _MainsGroupVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 2),
    _MainsGroupVoltageStatus_Type()
)
mainsGroupVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupVoltageStatus.setStatus("current")


class _MainsGroupVoltageDescription_Type(DisplayString):
    """Custom type mainsGroupVoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsGroupVoltageDescription_Type.__name__ = "DisplayString"
_MainsGroupVoltageDescription_Object = MibTableColumn
mainsGroupVoltageDescription = _MainsGroupVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 3),
    _MainsGroupVoltageDescription_Type()
)
mainsGroupVoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupVoltageDescription.setStatus("current")
_MainsGroupVoltageTrapRepeatCounter_Type = Integer32
_MainsGroupVoltageTrapRepeatCounter_Object = MibTableColumn
mainsGroupVoltageTrapRepeatCounter = _MainsGroupVoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 4),
    _MainsGroupVoltageTrapRepeatCounter_Type()
)
mainsGroupVoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsGroupVoltageTrapRepeatCounter.setStatus("current")


class _MainsGroupVoltageAlarmEnable_Type(Integer32):
    """Custom type mainsGroupVoltageAlarmEnable based on Integer32"""
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


_MainsGroupVoltageAlarmEnable_Type.__name__ = "Integer32"
_MainsGroupVoltageAlarmEnable_Object = MibTableColumn
mainsGroupVoltageAlarmEnable = _MainsGroupVoltageAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 5),
    _MainsGroupVoltageAlarmEnable_Type()
)
mainsGroupVoltageAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupVoltageAlarmEnable.setStatus("current")
_MainsGroupVoltageValue_Type = Integer32
_MainsGroupVoltageValue_Object = MibTableColumn
mainsGroupVoltageValue = _MainsGroupVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 6),
    _MainsGroupVoltageValue_Type()
)
mainsGroupVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupVoltageValue.setStatus("current")
_MainsGroupVoltageMajorHighLevel_Type = Integer32
_MainsGroupVoltageMajorHighLevel_Object = MibTableColumn
mainsGroupVoltageMajorHighLevel = _MainsGroupVoltageMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 7),
    _MainsGroupVoltageMajorHighLevel_Type()
)
mainsGroupVoltageMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupVoltageMajorHighLevel.setStatus("current")
_MainsGroupVoltageMinorHighLevel_Type = Integer32
_MainsGroupVoltageMinorHighLevel_Object = MibTableColumn
mainsGroupVoltageMinorHighLevel = _MainsGroupVoltageMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 8),
    _MainsGroupVoltageMinorHighLevel_Type()
)
mainsGroupVoltageMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupVoltageMinorHighLevel.setStatus("current")
_MainsGroupVoltageMinorLowLevel_Type = Integer32
_MainsGroupVoltageMinorLowLevel_Object = MibTableColumn
mainsGroupVoltageMinorLowLevel = _MainsGroupVoltageMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 9),
    _MainsGroupVoltageMinorLowLevel_Type()
)
mainsGroupVoltageMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupVoltageMinorLowLevel.setStatus("current")
_MainsGroupVoltageMajorLowLevel_Type = Integer32
_MainsGroupVoltageMajorLowLevel_Object = MibTableColumn
mainsGroupVoltageMajorLowLevel = _MainsGroupVoltageMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 10, 1, 10),
    _MainsGroupVoltageMajorLowLevel_Type()
)
mainsGroupVoltageMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsGroupVoltageMajorLowLevel.setStatus("current")
_MainsGroupOutageLogTable_Object = MibTable
mainsGroupOutageLogTable = _MainsGroupOutageLogTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 11)
)
if mibBuilder.loadTexts:
    mainsGroupOutageLogTable.setStatus("current")
_MainsGroupOutageLogEntry_Object = MibTableRow
mainsGroupOutageLogEntry = _MainsGroupOutageLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 11, 1)
)
mainsGroupOutageLogEntry.setIndexNames(
    (0, "SP2-MIB", "mainsGroupIndex"),
)
if mibBuilder.loadTexts:
    mainsGroupOutageLogEntry.setStatus("current")
_MainsGroupOutageTotal_Type = Integer32
_MainsGroupOutageTotal_Object = MibTableColumn
mainsGroupOutageTotal = _MainsGroupOutageTotal_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 11, 1, 1),
    _MainsGroupOutageTotal_Type()
)
mainsGroupOutageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupOutageTotal.setStatus("current")
_MainsGroupOutageLogDaysNumberOfEntries_Type = Integer32
_MainsGroupOutageLogDaysNumberOfEntries_Object = MibTableColumn
mainsGroupOutageLogDaysNumberOfEntries = _MainsGroupOutageLogDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 11, 1, 2),
    _MainsGroupOutageLogDaysNumberOfEntries_Type()
)
mainsGroupOutageLogDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupOutageLogDaysNumberOfEntries.setStatus("current")
_MainsGroupOutageLogWeeksNumberOfEntries_Type = Integer32
_MainsGroupOutageLogWeeksNumberOfEntries_Object = MibTableColumn
mainsGroupOutageLogWeeksNumberOfEntries = _MainsGroupOutageLogWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 11, 1, 3),
    _MainsGroupOutageLogWeeksNumberOfEntries_Type()
)
mainsGroupOutageLogWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupOutageLogWeeksNumberOfEntries.setStatus("current")
_MainsGroupOutageLogMonthsNumberOfEntries_Type = Integer32
_MainsGroupOutageLogMonthsNumberOfEntries_Object = MibTableColumn
mainsGroupOutageLogMonthsNumberOfEntries = _MainsGroupOutageLogMonthsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 11, 1, 4),
    _MainsGroupOutageLogMonthsNumberOfEntries_Type()
)
mainsGroupOutageLogMonthsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupOutageLogMonthsNumberOfEntries.setStatus("current")
_MainsGroupOutageLogDaysTable_Object = MibTable
mainsGroupOutageLogDaysTable = _MainsGroupOutageLogDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 12)
)
if mibBuilder.loadTexts:
    mainsGroupOutageLogDaysTable.setStatus("current")
_MainsGroupOutageLogDaysEntry_Object = MibTableRow
mainsGroupOutageLogDaysEntry = _MainsGroupOutageLogDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 12, 1)
)
mainsGroupOutageLogDaysEntry.setIndexNames(
    (0, "SP2-MIB", "mainsGroupIndex"),
    (0, "SP2-MIB", "mainsGroupOutageLogDaysIndex"),
)
if mibBuilder.loadTexts:
    mainsGroupOutageLogDaysEntry.setStatus("current")


class _MainsGroupOutageLogDaysIndex_Type(Integer32):
    """Custom type mainsGroupOutageLogDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsGroupOutageLogDaysIndex_Type.__name__ = "Integer32"
_MainsGroupOutageLogDaysIndex_Object = MibTableColumn
mainsGroupOutageLogDaysIndex = _MainsGroupOutageLogDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 12, 1, 1),
    _MainsGroupOutageLogDaysIndex_Type()
)
mainsGroupOutageLogDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsGroupOutageLogDaysIndex.setStatus("current")
_MainsGroupOutageLogDaysValue_Type = Integer32
_MainsGroupOutageLogDaysValue_Object = MibTableColumn
mainsGroupOutageLogDaysValue = _MainsGroupOutageLogDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 12, 1, 2),
    _MainsGroupOutageLogDaysValue_Type()
)
mainsGroupOutageLogDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupOutageLogDaysValue.setStatus("current")
_MainsGroupOutageLogWeeksTable_Object = MibTable
mainsGroupOutageLogWeeksTable = _MainsGroupOutageLogWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 13)
)
if mibBuilder.loadTexts:
    mainsGroupOutageLogWeeksTable.setStatus("current")
_MainsGroupOutageLogWeeksEntry_Object = MibTableRow
mainsGroupOutageLogWeeksEntry = _MainsGroupOutageLogWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 13, 1)
)
mainsGroupOutageLogWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "mainsGroupIndex"),
    (0, "SP2-MIB", "mainsGroupOutageLogWeeksIndex"),
)
if mibBuilder.loadTexts:
    mainsGroupOutageLogWeeksEntry.setStatus("current")


class _MainsGroupOutageLogWeeksIndex_Type(Integer32):
    """Custom type mainsGroupOutageLogWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsGroupOutageLogWeeksIndex_Type.__name__ = "Integer32"
_MainsGroupOutageLogWeeksIndex_Object = MibTableColumn
mainsGroupOutageLogWeeksIndex = _MainsGroupOutageLogWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 13, 1, 1),
    _MainsGroupOutageLogWeeksIndex_Type()
)
mainsGroupOutageLogWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsGroupOutageLogWeeksIndex.setStatus("current")
_MainsGroupOutageLogWeeksValue_Type = Integer32
_MainsGroupOutageLogWeeksValue_Object = MibTableColumn
mainsGroupOutageLogWeeksValue = _MainsGroupOutageLogWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 13, 1, 2),
    _MainsGroupOutageLogWeeksValue_Type()
)
mainsGroupOutageLogWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupOutageLogWeeksValue.setStatus("current")
_MainsGroupOutageLogMonthsTable_Object = MibTable
mainsGroupOutageLogMonthsTable = _MainsGroupOutageLogMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 14)
)
if mibBuilder.loadTexts:
    mainsGroupOutageLogMonthsTable.setStatus("current")
_MainsGroupOutageLogMonthsEntry_Object = MibTableRow
mainsGroupOutageLogMonthsEntry = _MainsGroupOutageLogMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 14, 1)
)
mainsGroupOutageLogMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "mainsGroupIndex"),
    (0, "SP2-MIB", "mainsGroupOutageLogMonthsIndex"),
)
if mibBuilder.loadTexts:
    mainsGroupOutageLogMonthsEntry.setStatus("current")


class _MainsGroupOutageLogMonthsIndex_Type(Integer32):
    """Custom type mainsGroupOutageLogMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_MainsGroupOutageLogMonthsIndex_Type.__name__ = "Integer32"
_MainsGroupOutageLogMonthsIndex_Object = MibTableColumn
mainsGroupOutageLogMonthsIndex = _MainsGroupOutageLogMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 14, 1, 1),
    _MainsGroupOutageLogMonthsIndex_Type()
)
mainsGroupOutageLogMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainsGroupOutageLogMonthsIndex.setStatus("current")
_MainsGroupOutageLogMonthsValue_Type = Integer32
_MainsGroupOutageLogMonthsValue_Object = MibTableColumn
mainsGroupOutageLogMonthsValue = _MainsGroupOutageLogMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 3, 14, 1, 2),
    _MainsGroupOutageLogMonthsValue_Type()
)
mainsGroupOutageLogMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsGroupOutageLogMonthsValue.setStatus("current")
_Generator_ObjectIdentity = ObjectIdentity
generator = _Generator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4)
)


class _GeneratorStatus_Type(Integer32):
    """Custom type generatorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_GeneratorStatus_Type.__name__ = "Integer32"
_GeneratorStatus_Object = MibScalar
generatorStatus = _GeneratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 1),
    _GeneratorStatus_Type()
)
generatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorStatus.setStatus("current")


class _GeneratorFailStatus_Type(Integer32):
    """Custom type generatorFailStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_GeneratorFailStatus_Type.__name__ = "Integer32"
_GeneratorFailStatus_Object = MibScalar
generatorFailStatus = _GeneratorFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 2),
    _GeneratorFailStatus_Type()
)
generatorFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFailStatus.setStatus("current")
_GeneratorActivation_Type = Integer32
_GeneratorActivation_Object = MibScalar
generatorActivation = _GeneratorActivation_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 3),
    _GeneratorActivation_Type()
)
generatorActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorActivation.setStatus("current")
_GeneratorDischargeValue_Type = Integer32
_GeneratorDischargeValue_Object = MibScalar
generatorDischargeValue = _GeneratorDischargeValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 4),
    _GeneratorDischargeValue_Type()
)
generatorDischargeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorDischargeValue.setStatus("current")
_GeneratorMainsDelay_Type = Integer32
_GeneratorMainsDelay_Object = MibScalar
generatorMainsDelay = _GeneratorMainsDelay_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 5),
    _GeneratorMainsDelay_Type()
)
generatorMainsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorMainsDelay.setStatus("current")
_GeneratorChargeTime_Type = Integer32
_GeneratorChargeTime_Object = MibScalar
generatorChargeTime = _GeneratorChargeTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 6),
    _GeneratorChargeTime_Type()
)
generatorChargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorChargeTime.setStatus("current")


class _GeneratorCapacityControlledStartStopEnable_Type(Integer32):
    """Custom type generatorCapacityControlledStartStopEnable based on Integer32"""
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


_GeneratorCapacityControlledStartStopEnable_Type.__name__ = "Integer32"
_GeneratorCapacityControlledStartStopEnable_Object = MibScalar
generatorCapacityControlledStartStopEnable = _GeneratorCapacityControlledStartStopEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 7),
    _GeneratorCapacityControlledStartStopEnable_Type()
)
generatorCapacityControlledStartStopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCapacityControlledStartStopEnable.setStatus("current")


class _GeneratorCapacityStartOnDischargeLimit_Type(Integer32):
    """Custom type generatorCapacityStartOnDischargeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeneratorCapacityStartOnDischargeLimit_Type.__name__ = "Integer32"
_GeneratorCapacityStartOnDischargeLimit_Object = MibScalar
generatorCapacityStartOnDischargeLimit = _GeneratorCapacityStartOnDischargeLimit_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 8),
    _GeneratorCapacityStartOnDischargeLimit_Type()
)
generatorCapacityStartOnDischargeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCapacityStartOnDischargeLimit.setStatus("current")


class _GeneratorCapacityStopOnChargeLimit_Type(Integer32):
    """Custom type generatorCapacityStopOnChargeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeneratorCapacityStopOnChargeLimit_Type.__name__ = "Integer32"
_GeneratorCapacityStopOnChargeLimit_Object = MibScalar
generatorCapacityStopOnChargeLimit = _GeneratorCapacityStopOnChargeLimit_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 9),
    _GeneratorCapacityStopOnChargeLimit_Type()
)
generatorCapacityStopOnChargeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCapacityStopOnChargeLimit.setStatus("current")


class _GeneratorCurrentLimitControlledStopEnable_Type(Integer32):
    """Custom type generatorCurrentLimitControlledStopEnable based on Integer32"""
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


_GeneratorCurrentLimitControlledStopEnable_Type.__name__ = "Integer32"
_GeneratorCurrentLimitControlledStopEnable_Object = MibScalar
generatorCurrentLimitControlledStopEnable = _GeneratorCurrentLimitControlledStopEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 10),
    _GeneratorCurrentLimitControlledStopEnable_Type()
)
generatorCurrentLimitControlledStopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCurrentLimitControlledStopEnable.setStatus("current")


class _GeneratorCurrentLimitControlledStopValue_Type(Integer32):
    """Custom type generatorCurrentLimitControlledStopValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GeneratorCurrentLimitControlledStopValue_Type.__name__ = "Integer32"
_GeneratorCurrentLimitControlledStopValue_Object = MibScalar
generatorCurrentLimitControlledStopValue = _GeneratorCurrentLimitControlledStopValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 11),
    _GeneratorCurrentLimitControlledStopValue_Type()
)
generatorCurrentLimitControlledStopValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorCurrentLimitControlledStopValue.setStatus("current")


class _GeneratorVoltageControlledStartEnable_Type(Integer32):
    """Custom type generatorVoltageControlledStartEnable based on Integer32"""
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


_GeneratorVoltageControlledStartEnable_Type.__name__ = "Integer32"
_GeneratorVoltageControlledStartEnable_Object = MibScalar
generatorVoltageControlledStartEnable = _GeneratorVoltageControlledStartEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 12),
    _GeneratorVoltageControlledStartEnable_Type()
)
generatorVoltageControlledStartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorVoltageControlledStartEnable.setStatus("current")
_GeneratorVoltageControlStartVoltage_Type = Integer32
_GeneratorVoltageControlStartVoltage_Object = MibScalar
generatorVoltageControlStartVoltage = _GeneratorVoltageControlStartVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 13),
    _GeneratorVoltageControlStartVoltage_Type()
)
generatorVoltageControlStartVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorVoltageControlStartVoltage.setStatus("current")
_GeneratorVoltageControlStopAfter_Type = Integer32
_GeneratorVoltageControlStopAfter_Object = MibScalar
generatorVoltageControlStopAfter = _GeneratorVoltageControlStopAfter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 14),
    _GeneratorVoltageControlStopAfter_Type()
)
generatorVoltageControlStopAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorVoltageControlStopAfter.setStatus("current")


class _GeneratorDailyRunEnable_Type(Integer32):
    """Custom type generatorDailyRunEnable based on Integer32"""
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


_GeneratorDailyRunEnable_Type.__name__ = "Integer32"
_GeneratorDailyRunEnable_Object = MibScalar
generatorDailyRunEnable = _GeneratorDailyRunEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 15),
    _GeneratorDailyRunEnable_Type()
)
generatorDailyRunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorDailyRunEnable.setStatus("current")
_GeneratorDailyRunSetupTable_Object = MibTable
generatorDailyRunSetupTable = _GeneratorDailyRunSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16)
)
if mibBuilder.loadTexts:
    generatorDailyRunSetupTable.setStatus("current")
_GeneratorDailyRunSetupEntry_Object = MibTableRow
generatorDailyRunSetupEntry = _GeneratorDailyRunSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16, 1)
)
generatorDailyRunSetupEntry.setIndexNames(
    (0, "SP2-MIB", "generatorDailyRunDayIndex"),
)
if mibBuilder.loadTexts:
    generatorDailyRunSetupEntry.setStatus("current")


class _GeneratorDailyRunDayIndex_Type(Integer32):
    """Custom type generatorDailyRunDayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_GeneratorDailyRunDayIndex_Type.__name__ = "Integer32"
_GeneratorDailyRunDayIndex_Object = MibTableColumn
generatorDailyRunDayIndex = _GeneratorDailyRunDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16, 1, 1),
    _GeneratorDailyRunDayIndex_Type()
)
generatorDailyRunDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorDailyRunDayIndex.setStatus("current")


class _GeneratorDailyRunStartHour_Type(Integer32):
    """Custom type generatorDailyRunStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GeneratorDailyRunStartHour_Type.__name__ = "Integer32"
_GeneratorDailyRunStartHour_Object = MibTableColumn
generatorDailyRunStartHour = _GeneratorDailyRunStartHour_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16, 1, 2),
    _GeneratorDailyRunStartHour_Type()
)
generatorDailyRunStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorDailyRunStartHour.setStatus("current")


class _GeneratorDailyRunStopHour_Type(Integer32):
    """Custom type generatorDailyRunStopHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GeneratorDailyRunStopHour_Type.__name__ = "Integer32"
_GeneratorDailyRunStopHour_Object = MibTableColumn
generatorDailyRunStopHour = _GeneratorDailyRunStopHour_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 16, 1, 3),
    _GeneratorDailyRunStopHour_Type()
)
generatorDailyRunStopHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorDailyRunStopHour.setStatus("current")


class _GeneratorMonthlyRunEnable_Type(Integer32):
    """Custom type generatorMonthlyRunEnable based on Integer32"""
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


_GeneratorMonthlyRunEnable_Type.__name__ = "Integer32"
_GeneratorMonthlyRunEnable_Object = MibScalar
generatorMonthlyRunEnable = _GeneratorMonthlyRunEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 17),
    _GeneratorMonthlyRunEnable_Type()
)
generatorMonthlyRunEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorMonthlyRunEnable.setStatus("current")


class _GeneratorMonthlyRunStartTime_Type(Integer32):
    """Custom type generatorMonthlyRunStartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_GeneratorMonthlyRunStartTime_Type.__name__ = "Integer32"
_GeneratorMonthlyRunStartTime_Object = MibScalar
generatorMonthlyRunStartTime = _GeneratorMonthlyRunStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 18),
    _GeneratorMonthlyRunStartTime_Type()
)
generatorMonthlyRunStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorMonthlyRunStartTime.setStatus("current")


class _GeneratorMonthlyRunStartDayinMonth1_Type(Integer32):
    """Custom type generatorMonthlyRunStartDayinMonth1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_GeneratorMonthlyRunStartDayinMonth1_Type.__name__ = "Integer32"
_GeneratorMonthlyRunStartDayinMonth1_Object = MibScalar
generatorMonthlyRunStartDayinMonth1 = _GeneratorMonthlyRunStartDayinMonth1_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 19),
    _GeneratorMonthlyRunStartDayinMonth1_Type()
)
generatorMonthlyRunStartDayinMonth1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorMonthlyRunStartDayinMonth1.setStatus("current")


class _GeneratorMonthlyRunStartDayinMonth2_Type(Integer32):
    """Custom type generatorMonthlyRunStartDayinMonth2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_GeneratorMonthlyRunStartDayinMonth2_Type.__name__ = "Integer32"
_GeneratorMonthlyRunStartDayinMonth2_Object = MibScalar
generatorMonthlyRunStartDayinMonth2 = _GeneratorMonthlyRunStartDayinMonth2_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 20),
    _GeneratorMonthlyRunStartDayinMonth2_Type()
)
generatorMonthlyRunStartDayinMonth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorMonthlyRunStartDayinMonth2.setStatus("current")


class _GeneratorTankNumberOfTanks_Type(Integer32):
    """Custom type generatorTankNumberOfTanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GeneratorTankNumberOfTanks_Type.__name__ = "Integer32"
_GeneratorTankNumberOfTanks_Object = MibScalar
generatorTankNumberOfTanks = _GeneratorTankNumberOfTanks_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 21),
    _GeneratorTankNumberOfTanks_Type()
)
generatorTankNumberOfTanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorTankNumberOfTanks.setStatus("current")
_GeneratorTankTable_Object = MibTable
generatorTankTable = _GeneratorTankTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22)
)
if mibBuilder.loadTexts:
    generatorTankTable.setStatus("current")
_GeneratorTankEntry_Object = MibTableRow
generatorTankEntry = _GeneratorTankEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1)
)
generatorTankEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
)
if mibBuilder.loadTexts:
    generatorTankEntry.setStatus("current")


class _GeneratorTankIndex_Type(Integer32):
    """Custom type generatorTankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GeneratorTankIndex_Type.__name__ = "Integer32"
_GeneratorTankIndex_Object = MibTableColumn
generatorTankIndex = _GeneratorTankIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 1),
    _GeneratorTankIndex_Type()
)
generatorTankIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorTankIndex.setStatus("current")


class _GeneratorTankStatus_Type(Integer32):
    """Custom type generatorTankStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_GeneratorTankStatus_Type.__name__ = "Integer32"
_GeneratorTankStatus_Object = MibTableColumn
generatorTankStatus = _GeneratorTankStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 2),
    _GeneratorTankStatus_Type()
)
generatorTankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorTankStatus.setStatus("current")


class _GeneratorTankDescription_Type(DisplayString):
    """Custom type generatorTankDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GeneratorTankDescription_Type.__name__ = "DisplayString"
_GeneratorTankDescription_Object = MibTableColumn
generatorTankDescription = _GeneratorTankDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 3),
    _GeneratorTankDescription_Type()
)
generatorTankDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankDescription.setStatus("current")
_GeneratorTankTrapRepeatCounter_Type = Counter32
_GeneratorTankTrapRepeatCounter_Object = MibTableColumn
generatorTankTrapRepeatCounter = _GeneratorTankTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 4),
    _GeneratorTankTrapRepeatCounter_Type()
)
generatorTankTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    generatorTankTrapRepeatCounter.setStatus("current")


class _GeneratorTankEnable_Type(Integer32):
    """Custom type generatorTankEnable based on Integer32"""
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


_GeneratorTankEnable_Type.__name__ = "Integer32"
_GeneratorTankEnable_Object = MibTableColumn
generatorTankEnable = _GeneratorTankEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 5),
    _GeneratorTankEnable_Type()
)
generatorTankEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankEnable.setStatus("current")
_GeneratorTankValue_Type = Integer32
_GeneratorTankValue_Object = MibTableColumn
generatorTankValue = _GeneratorTankValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 6),
    _GeneratorTankValue_Type()
)
generatorTankValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorTankValue.setStatus("current")
_GeneratorTankMajorHighLevel_Type = Integer32
_GeneratorTankMajorHighLevel_Object = MibTableColumn
generatorTankMajorHighLevel = _GeneratorTankMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 7),
    _GeneratorTankMajorHighLevel_Type()
)
generatorTankMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankMajorHighLevel.setStatus("current")
_GeneratorTankMinorHighLevel_Type = Integer32
_GeneratorTankMinorHighLevel_Object = MibTableColumn
generatorTankMinorHighLevel = _GeneratorTankMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 8),
    _GeneratorTankMinorHighLevel_Type()
)
generatorTankMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankMinorHighLevel.setStatus("current")
_GeneratorTankMinorLowLevel_Type = Integer32
_GeneratorTankMinorLowLevel_Object = MibTableColumn
generatorTankMinorLowLevel = _GeneratorTankMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 9),
    _GeneratorTankMinorLowLevel_Type()
)
generatorTankMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankMinorLowLevel.setStatus("current")
_GeneratorTankMajorLowLevel_Type = Integer32
_GeneratorTankMajorLowLevel_Object = MibTableColumn
generatorTankMajorLowLevel = _GeneratorTankMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 22, 1, 10),
    _GeneratorTankMajorLowLevel_Type()
)
generatorTankMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    generatorTankMajorLowLevel.setStatus("current")
_GeneratorEnergyLog_ObjectIdentity = ObjectIdentity
generatorEnergyLog = _GeneratorEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23)
)
_GeneratorEnergyLogAccumulated_Type = Integer32
_GeneratorEnergyLogAccumulated_Object = MibScalar
generatorEnergyLogAccumulated = _GeneratorEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 1),
    _GeneratorEnergyLogAccumulated_Type()
)
generatorEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogAccumulated.setStatus("current")


class _GeneratorEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type generatorEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastHoursNumberOfEntries_Object = MibScalar
generatorEnergyLogLastHoursNumberOfEntries = _GeneratorEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 2),
    _GeneratorEnergyLogLastHoursNumberOfEntries_Type()
)
generatorEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursNumberOfEntries.setStatus("current")
_GeneratorEnergyLogLastHoursTable_Object = MibTable
generatorEnergyLogLastHoursTable = _GeneratorEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 3)
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursTable.setStatus("current")
_GeneratorEnergyLogLastHoursEntry_Object = MibTableRow
generatorEnergyLogLastHoursEntry = _GeneratorEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 3, 1)
)
generatorEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "generatorEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursEntry.setStatus("current")


class _GeneratorEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type generatorEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastHoursIndex_Object = MibTableColumn
generatorEnergyLogLastHoursIndex = _GeneratorEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 3, 1, 1),
    _GeneratorEnergyLogLastHoursIndex_Type()
)
generatorEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursIndex.setStatus("current")
_GeneratorEnergyLogLastHoursValue_Type = Integer32
_GeneratorEnergyLogLastHoursValue_Object = MibTableColumn
generatorEnergyLogLastHoursValue = _GeneratorEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 3, 1, 2),
    _GeneratorEnergyLogLastHoursValue_Type()
)
generatorEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastHoursValue.setStatus("current")


class _GeneratorEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type generatorEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastDaysNumberOfEntries_Object = MibScalar
generatorEnergyLogLastDaysNumberOfEntries = _GeneratorEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 4),
    _GeneratorEnergyLogLastDaysNumberOfEntries_Type()
)
generatorEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysNumberOfEntries.setStatus("current")
_GeneratorEnergyLogLastDaysTable_Object = MibTable
generatorEnergyLogLastDaysTable = _GeneratorEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 5)
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysTable.setStatus("current")
_GeneratorEnergyLogLastDaysEntry_Object = MibTableRow
generatorEnergyLogLastDaysEntry = _GeneratorEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 5, 1)
)
generatorEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "generatorEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysEntry.setStatus("current")


class _GeneratorEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type generatorEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastDaysIndex_Object = MibTableColumn
generatorEnergyLogLastDaysIndex = _GeneratorEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 5, 1, 1),
    _GeneratorEnergyLogLastDaysIndex_Type()
)
generatorEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysIndex.setStatus("current")
_GeneratorEnergyLogLastDaysValue_Type = Integer32
_GeneratorEnergyLogLastDaysValue_Object = MibTableColumn
generatorEnergyLogLastDaysValue = _GeneratorEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 5, 1, 2),
    _GeneratorEnergyLogLastDaysValue_Type()
)
generatorEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastDaysValue.setStatus("current")


class _GeneratorEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type generatorEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
generatorEnergyLogLastWeeksNumberOfEntries = _GeneratorEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 6),
    _GeneratorEnergyLogLastWeeksNumberOfEntries_Type()
)
generatorEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_GeneratorEnergyLogLastWeeksTable_Object = MibTable
generatorEnergyLogLastWeeksTable = _GeneratorEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 7)
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksTable.setStatus("current")
_GeneratorEnergyLogLastWeeksEntry_Object = MibTableRow
generatorEnergyLogLastWeeksEntry = _GeneratorEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 7, 1)
)
generatorEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "generatorEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksEntry.setStatus("current")


class _GeneratorEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type generatorEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_GeneratorEnergyLogLastWeeksIndex_Object = MibTableColumn
generatorEnergyLogLastWeeksIndex = _GeneratorEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 7, 1, 1),
    _GeneratorEnergyLogLastWeeksIndex_Type()
)
generatorEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksIndex.setStatus("current")
_GeneratorEnergyLogLastWeeksValue_Type = Integer32
_GeneratorEnergyLogLastWeeksValue_Object = MibTableColumn
generatorEnergyLogLastWeeksValue = _GeneratorEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 23, 7, 1, 2),
    _GeneratorEnergyLogLastWeeksValue_Type()
)
generatorEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorEnergyLogLastWeeksValue.setStatus("current")
_GeneratorRunHoursLog_ObjectIdentity = ObjectIdentity
generatorRunHoursLog = _GeneratorRunHoursLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24)
)
_GeneratorRunHoursTotalHours_Type = Integer32
_GeneratorRunHoursTotalHours_Object = MibScalar
generatorRunHoursTotalHours = _GeneratorRunHoursTotalHours_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 1),
    _GeneratorRunHoursTotalHours_Type()
)
generatorRunHoursTotalHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursTotalHours.setStatus("current")


class _GeneratorRunHoursLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type generatorRunHoursLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorRunHoursLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastDaysNumberOfEntries_Object = MibScalar
generatorRunHoursLogLastDaysNumberOfEntries = _GeneratorRunHoursLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 2),
    _GeneratorRunHoursLogLastDaysNumberOfEntries_Type()
)
generatorRunHoursLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysNumberOfEntries.setStatus("current")
_GeneratorRunHoursLogLastDaysTable_Object = MibTable
generatorRunHoursLogLastDaysTable = _GeneratorRunHoursLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 3)
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysTable.setStatus("current")
_GeneratorRunHoursLogLastDaysEntry_Object = MibTableRow
generatorRunHoursLogLastDaysEntry = _GeneratorRunHoursLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 3, 1)
)
generatorRunHoursLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "generatorRunHoursLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysEntry.setStatus("current")


class _GeneratorRunHoursLogLastDaysIndex_Type(Integer32):
    """Custom type generatorRunHoursLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorRunHoursLogLastDaysIndex_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastDaysIndex_Object = MibTableColumn
generatorRunHoursLogLastDaysIndex = _GeneratorRunHoursLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 3, 1, 1),
    _GeneratorRunHoursLogLastDaysIndex_Type()
)
generatorRunHoursLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysIndex.setStatus("current")
_GeneratorRunHoursLogLastDaysValue_Type = Integer32
_GeneratorRunHoursLogLastDaysValue_Object = MibTableColumn
generatorRunHoursLogLastDaysValue = _GeneratorRunHoursLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 3, 1, 2),
    _GeneratorRunHoursLogLastDaysValue_Type()
)
generatorRunHoursLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastDaysValue.setStatus("current")


class _GeneratorRunHoursLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type generatorRunHoursLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorRunHoursLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastWeeksNumberOfEntries_Object = MibScalar
generatorRunHoursLogLastWeeksNumberOfEntries = _GeneratorRunHoursLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 4),
    _GeneratorRunHoursLogLastWeeksNumberOfEntries_Type()
)
generatorRunHoursLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksNumberOfEntries.setStatus("current")
_GeneratorRunHoursLogLastWeeksTable_Object = MibTable
generatorRunHoursLogLastWeeksTable = _GeneratorRunHoursLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 5)
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksTable.setStatus("current")
_GeneratorRunHoursLogLastWeeksEntry_Object = MibTableRow
generatorRunHoursLogLastWeeksEntry = _GeneratorRunHoursLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 5, 1)
)
generatorRunHoursLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "generatorRunHoursLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksEntry.setStatus("current")


class _GeneratorRunHoursLogLastWeeksIndex_Type(Integer32):
    """Custom type generatorRunHoursLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorRunHoursLogLastWeeksIndex_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastWeeksIndex_Object = MibTableColumn
generatorRunHoursLogLastWeeksIndex = _GeneratorRunHoursLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 5, 1, 1),
    _GeneratorRunHoursLogLastWeeksIndex_Type()
)
generatorRunHoursLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksIndex.setStatus("current")
_GeneratorRunHoursLogLastWeeksValue_Type = Integer32
_GeneratorRunHoursLogLastWeeksValue_Object = MibTableColumn
generatorRunHoursLogLastWeeksValue = _GeneratorRunHoursLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 5, 1, 2),
    _GeneratorRunHoursLogLastWeeksValue_Type()
)
generatorRunHoursLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastWeeksValue.setStatus("current")


class _GeneratorRunHoursLogLastMonthsNumberOfEntries_Type(Integer32):
    """Custom type generatorRunHoursLogLastMonthsNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorRunHoursLogLastMonthsNumberOfEntries_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastMonthsNumberOfEntries_Object = MibScalar
generatorRunHoursLogLastMonthsNumberOfEntries = _GeneratorRunHoursLogLastMonthsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 6),
    _GeneratorRunHoursLogLastMonthsNumberOfEntries_Type()
)
generatorRunHoursLogLastMonthsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsNumberOfEntries.setStatus("current")
_GeneratorRunHoursLogLastMonthsTable_Object = MibTable
generatorRunHoursLogLastMonthsTable = _GeneratorRunHoursLogLastMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 7)
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsTable.setStatus("current")
_GeneratorRunHoursLogLastMonthsEntry_Object = MibTableRow
generatorRunHoursLogLastMonthsEntry = _GeneratorRunHoursLogLastMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 7, 1)
)
generatorRunHoursLogLastMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "generatorRunHoursLogLastMonthsIndex"),
)
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsEntry.setStatus("current")


class _GeneratorRunHoursLogLastMonthsIndex_Type(Integer32):
    """Custom type generatorRunHoursLogLastMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorRunHoursLogLastMonthsIndex_Type.__name__ = "Integer32"
_GeneratorRunHoursLogLastMonthsIndex_Object = MibTableColumn
generatorRunHoursLogLastMonthsIndex = _GeneratorRunHoursLogLastMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 7, 1, 1),
    _GeneratorRunHoursLogLastMonthsIndex_Type()
)
generatorRunHoursLogLastMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsIndex.setStatus("current")
_GeneratorRunHoursLogLastMonthsValue_Type = Integer32
_GeneratorRunHoursLogLastMonthsValue_Object = MibTableColumn
generatorRunHoursLogLastMonthsValue = _GeneratorRunHoursLogLastMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 24, 7, 1, 2),
    _GeneratorRunHoursLogLastMonthsValue_Type()
)
generatorRunHoursLogLastMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorRunHoursLogLastMonthsValue.setStatus("current")
_GeneratorFuelConsumptionLog_ObjectIdentity = ObjectIdentity
generatorFuelConsumptionLog = _GeneratorFuelConsumptionLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25)
)
_GeneratorFuelConsumptionTotalUsedTable_Object = MibTable
generatorFuelConsumptionTotalUsedTable = _GeneratorFuelConsumptionTotalUsedTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 1)
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionTotalUsedTable.setStatus("current")
_GeneratorFuelConsumptionTotalUsedEntry_Object = MibTableRow
generatorFuelConsumptionTotalUsedEntry = _GeneratorFuelConsumptionTotalUsedEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 1, 1)
)
generatorFuelConsumptionTotalUsedEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionTotalUsedEntry.setStatus("current")
_GeneratorFuelConsumptionTotalUsed_Type = Integer32
_GeneratorFuelConsumptionTotalUsed_Object = MibTableColumn
generatorFuelConsumptionTotalUsed = _GeneratorFuelConsumptionTotalUsed_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 1, 1, 1),
    _GeneratorFuelConsumptionTotalUsed_Type()
)
generatorFuelConsumptionTotalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionTotalUsed.setStatus("current")


class _GeneratorFuelConsumptionLogLastDaysNoOfEntries_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastDaysNoOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorFuelConsumptionLogLastDaysNoOfEntries_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastDaysNoOfEntries_Object = MibScalar
generatorFuelConsumptionLogLastDaysNoOfEntries = _GeneratorFuelConsumptionLogLastDaysNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 2),
    _GeneratorFuelConsumptionLogLastDaysNoOfEntries_Type()
)
generatorFuelConsumptionLogLastDaysNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysNoOfEntries.setStatus("current")
_GeneratorFuelConsumptionLogLastDaysTable_Object = MibTable
generatorFuelConsumptionLogLastDaysTable = _GeneratorFuelConsumptionLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 3)
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysTable.setStatus("current")
_GeneratorFuelConsumptionLogLastDaysEntry_Object = MibTableRow
generatorFuelConsumptionLogLastDaysEntry = _GeneratorFuelConsumptionLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 3, 1)
)
generatorFuelConsumptionLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
    (0, "SP2-MIB", "generatorFuelConsumptionLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysEntry.setStatus("current")


class _GeneratorFuelConsumptionLogLastDaysIndex_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorFuelConsumptionLogLastDaysIndex_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastDaysIndex_Object = MibTableColumn
generatorFuelConsumptionLogLastDaysIndex = _GeneratorFuelConsumptionLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 3, 1, 1),
    _GeneratorFuelConsumptionLogLastDaysIndex_Type()
)
generatorFuelConsumptionLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysIndex.setStatus("current")
_GeneratorFuelConsumptionLogLastDaysValue_Type = Integer32
_GeneratorFuelConsumptionLogLastDaysValue_Object = MibTableColumn
generatorFuelConsumptionLogLastDaysValue = _GeneratorFuelConsumptionLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 3, 1, 2),
    _GeneratorFuelConsumptionLogLastDaysValue_Type()
)
generatorFuelConsumptionLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastDaysValue.setStatus("current")


class _GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastWeeksNoOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Object = MibScalar
generatorFuelConsumptionLogLastWeeksNoOfEntries = _GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 4),
    _GeneratorFuelConsumptionLogLastWeeksNoOfEntries_Type()
)
generatorFuelConsumptionLogLastWeeksNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksNoOfEntries.setStatus("current")
_GeneratorFuelConsumptionLogLastWeeksTable_Object = MibTable
generatorFuelConsumptionLogLastWeeksTable = _GeneratorFuelConsumptionLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 5)
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksTable.setStatus("current")
_GeneratorFuelConsumptionLogLastWeeksEntry_Object = MibTableRow
generatorFuelConsumptionLogLastWeeksEntry = _GeneratorFuelConsumptionLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 5, 1)
)
generatorFuelConsumptionLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
    (0, "SP2-MIB", "generatorFuelConsumptionLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksEntry.setStatus("current")


class _GeneratorFuelConsumptionLogLastWeeksIndex_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorFuelConsumptionLogLastWeeksIndex_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastWeeksIndex_Object = MibTableColumn
generatorFuelConsumptionLogLastWeeksIndex = _GeneratorFuelConsumptionLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 5, 1, 1),
    _GeneratorFuelConsumptionLogLastWeeksIndex_Type()
)
generatorFuelConsumptionLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksIndex.setStatus("current")
_GeneratorFuelConsumptionLogLastWeeksValue_Type = Integer32
_GeneratorFuelConsumptionLogLastWeeksValue_Object = MibTableColumn
generatorFuelConsumptionLogLastWeeksValue = _GeneratorFuelConsumptionLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 5, 1, 2),
    _GeneratorFuelConsumptionLogLastWeeksValue_Type()
)
generatorFuelConsumptionLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastWeeksValue.setStatus("current")


class _GeneratorFuelConsumptionLogLastMonthsNoOfEntries_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastMonthsNoOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_GeneratorFuelConsumptionLogLastMonthsNoOfEntries_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastMonthsNoOfEntries_Object = MibScalar
generatorFuelConsumptionLogLastMonthsNoOfEntries = _GeneratorFuelConsumptionLogLastMonthsNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 6),
    _GeneratorFuelConsumptionLogLastMonthsNoOfEntries_Type()
)
generatorFuelConsumptionLogLastMonthsNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastMonthsNoOfEntries.setStatus("current")
_GeneratorFuelConsumptionLogLastMonthsTable_Object = MibTable
generatorFuelConsumptionLogLastMonthsTable = _GeneratorFuelConsumptionLogLastMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 7)
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastMonthsTable.setStatus("current")
_GeneratorFuelConsumptionLogLastMonthsEntry_Object = MibTableRow
generatorFuelConsumptionLogLastMonthsEntry = _GeneratorFuelConsumptionLogLastMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 7, 1)
)
generatorFuelConsumptionLogLastMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "generatorTankIndex"),
    (0, "SP2-MIB", "generatorFuelConsumptionLogLastMonthsIndex"),
)
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastMonthsEntry.setStatus("current")


class _GeneratorFuelConsumptionLogLastMonthsIndex_Type(Integer32):
    """Custom type generatorFuelConsumptionLogLastMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_GeneratorFuelConsumptionLogLastMonthsIndex_Type.__name__ = "Integer32"
_GeneratorFuelConsumptionLogLastMonthsIndex_Object = MibTableColumn
generatorFuelConsumptionLogLastMonthsIndex = _GeneratorFuelConsumptionLogLastMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 7, 1, 1),
    _GeneratorFuelConsumptionLogLastMonthsIndex_Type()
)
generatorFuelConsumptionLogLastMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastMonthsIndex.setStatus("current")
_GeneratorFuelConsumptionLogLastMonthsValue_Type = Integer32
_GeneratorFuelConsumptionLogLastMonthsValue_Object = MibTableColumn
generatorFuelConsumptionLogLastMonthsValue = _GeneratorFuelConsumptionLogLastMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 4, 25, 7, 1, 2),
    _GeneratorFuelConsumptionLogLastMonthsValue_Type()
)
generatorFuelConsumptionLogLastMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    generatorFuelConsumptionLogLastMonthsValue.setStatus("current")
_Rectifiers_ObjectIdentity = ObjectIdentity
rectifiers = _Rectifiers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5)
)


class _RectifiersStatus_Type(Integer32):
    """Custom type rectifiersStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifiersStatus_Type.__name__ = "Integer32"
_RectifiersStatus_Object = MibScalar
rectifiersStatus = _RectifiersStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 1),
    _RectifiersStatus_Type()
)
rectifiersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersStatus.setStatus("current")
_RectifiersCurrent_ObjectIdentity = ObjectIdentity
rectifiersCurrent = _RectifiersCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2)
)


class _RectifiersCurrentStatus_Type(Integer32):
    """Custom type rectifiersCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifiersCurrentStatus_Type.__name__ = "Integer32"
_RectifiersCurrentStatus_Object = MibScalar
rectifiersCurrentStatus = _RectifiersCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 1),
    _RectifiersCurrentStatus_Type()
)
rectifiersCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersCurrentStatus.setStatus("current")


class _RectifiersCurrentDescription_Type(DisplayString):
    """Custom type rectifiersCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifiersCurrentDescription_Type.__name__ = "DisplayString"
_RectifiersCurrentDescription_Object = MibScalar
rectifiersCurrentDescription = _RectifiersCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 2),
    _RectifiersCurrentDescription_Type()
)
rectifiersCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCurrentDescription.setStatus("current")
_RectifiersCurrentTrapRepeatCounter_Type = Counter32
_RectifiersCurrentTrapRepeatCounter_Object = MibScalar
rectifiersCurrentTrapRepeatCounter = _RectifiersCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 3),
    _RectifiersCurrentTrapRepeatCounter_Type()
)
rectifiersCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifiersCurrentTrapRepeatCounter.setStatus("current")


class _RectifiersCurrentAlarmEnable_Type(Integer32):
    """Custom type rectifiersCurrentAlarmEnable based on Integer32"""
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


_RectifiersCurrentAlarmEnable_Type.__name__ = "Integer32"
_RectifiersCurrentAlarmEnable_Object = MibScalar
rectifiersCurrentAlarmEnable = _RectifiersCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 4),
    _RectifiersCurrentAlarmEnable_Type()
)
rectifiersCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCurrentAlarmEnable.setStatus("current")
_RectifiersCurrentValue_Type = Integer32
_RectifiersCurrentValue_Object = MibScalar
rectifiersCurrentValue = _RectifiersCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 5),
    _RectifiersCurrentValue_Type()
)
rectifiersCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersCurrentValue.setStatus("current")
_RectifiersCurrentMajorAlarmLevel_Type = Integer32
_RectifiersCurrentMajorAlarmLevel_Object = MibScalar
rectifiersCurrentMajorAlarmLevel = _RectifiersCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 6),
    _RectifiersCurrentMajorAlarmLevel_Type()
)
rectifiersCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCurrentMajorAlarmLevel.setStatus("current")
_RectifiersCurrentMinorAlarmLevel_Type = Integer32
_RectifiersCurrentMinorAlarmLevel_Object = MibScalar
rectifiersCurrentMinorAlarmLevel = _RectifiersCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 2, 7),
    _RectifiersCurrentMinorAlarmLevel_Type()
)
rectifiersCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCurrentMinorAlarmLevel.setStatus("current")
_RectifiersCapacity_ObjectIdentity = ObjectIdentity
rectifiersCapacity = _RectifiersCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3)
)


class _RectifiersCapacityStatus_Type(Integer32):
    """Custom type rectifiersCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifiersCapacityStatus_Type.__name__ = "Integer32"
_RectifiersCapacityStatus_Object = MibScalar
rectifiersCapacityStatus = _RectifiersCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 1),
    _RectifiersCapacityStatus_Type()
)
rectifiersCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersCapacityStatus.setStatus("current")


class _RectifiersCapacityDescription_Type(DisplayString):
    """Custom type rectifiersCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifiersCapacityDescription_Type.__name__ = "DisplayString"
_RectifiersCapacityDescription_Object = MibScalar
rectifiersCapacityDescription = _RectifiersCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 2),
    _RectifiersCapacityDescription_Type()
)
rectifiersCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCapacityDescription.setStatus("current")
_RectifiersCapacityTrapRepeatCounter_Type = Counter32
_RectifiersCapacityTrapRepeatCounter_Object = MibScalar
rectifiersCapacityTrapRepeatCounter = _RectifiersCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 3),
    _RectifiersCapacityTrapRepeatCounter_Type()
)
rectifiersCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifiersCapacityTrapRepeatCounter.setStatus("current")


class _RectifiersCapacityAlarmEnable_Type(Integer32):
    """Custom type rectifiersCapacityAlarmEnable based on Integer32"""
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


_RectifiersCapacityAlarmEnable_Type.__name__ = "Integer32"
_RectifiersCapacityAlarmEnable_Object = MibScalar
rectifiersCapacityAlarmEnable = _RectifiersCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 4),
    _RectifiersCapacityAlarmEnable_Type()
)
rectifiersCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCapacityAlarmEnable.setStatus("current")
_RectifiersCapacityValue_Type = Integer32
_RectifiersCapacityValue_Object = MibScalar
rectifiersCapacityValue = _RectifiersCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 5),
    _RectifiersCapacityValue_Type()
)
rectifiersCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersCapacityValue.setStatus("current")
_RectifiersCapacityMajorAlarmLevel_Type = Integer32
_RectifiersCapacityMajorAlarmLevel_Object = MibScalar
rectifiersCapacityMajorAlarmLevel = _RectifiersCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 6),
    _RectifiersCapacityMajorAlarmLevel_Type()
)
rectifiersCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCapacityMajorAlarmLevel.setStatus("current")
_RectifiersCapacityMinorAlarmLevel_Type = Integer32
_RectifiersCapacityMinorAlarmLevel_Object = MibScalar
rectifiersCapacityMinorAlarmLevel = _RectifiersCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 3, 7),
    _RectifiersCapacityMinorAlarmLevel_Type()
)
rectifiersCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersCapacityMinorAlarmLevel.setStatus("current")
_RectifiersError_ObjectIdentity = ObjectIdentity
rectifiersError = _RectifiersError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4)
)


class _RectifiersErrorStatus_Type(Integer32):
    """Custom type rectifiersErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifiersErrorStatus_Type.__name__ = "Integer32"
_RectifiersErrorStatus_Object = MibScalar
rectifiersErrorStatus = _RectifiersErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 1),
    _RectifiersErrorStatus_Type()
)
rectifiersErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersErrorStatus.setStatus("current")


class _RectifiersErrorDescription_Type(DisplayString):
    """Custom type rectifiersErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifiersErrorDescription_Type.__name__ = "DisplayString"
_RectifiersErrorDescription_Object = MibScalar
rectifiersErrorDescription = _RectifiersErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 2),
    _RectifiersErrorDescription_Type()
)
rectifiersErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersErrorDescription.setStatus("current")
_RectifiersErrorTrapRepeatCounter_Type = Counter32
_RectifiersErrorTrapRepeatCounter_Object = MibScalar
rectifiersErrorTrapRepeatCounter = _RectifiersErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 3),
    _RectifiersErrorTrapRepeatCounter_Type()
)
rectifiersErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifiersErrorTrapRepeatCounter.setStatus("current")


class _RectifiersErrorEnable_Type(Integer32):
    """Custom type rectifiersErrorEnable based on Integer32"""
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


_RectifiersErrorEnable_Type.__name__ = "Integer32"
_RectifiersErrorEnable_Object = MibScalar
rectifiersErrorEnable = _RectifiersErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 4),
    _RectifiersErrorEnable_Type()
)
rectifiersErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersErrorEnable.setStatus("current")
_RectifiersErrorValue_Type = Integer32
_RectifiersErrorValue_Object = MibScalar
rectifiersErrorValue = _RectifiersErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 5),
    _RectifiersErrorValue_Type()
)
rectifiersErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersErrorValue.setStatus("current")
_RectifiersErrorMajorAlarmLevel_Type = Integer32
_RectifiersErrorMajorAlarmLevel_Object = MibScalar
rectifiersErrorMajorAlarmLevel = _RectifiersErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 6),
    _RectifiersErrorMajorAlarmLevel_Type()
)
rectifiersErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersErrorMajorAlarmLevel.setStatus("current")
_RectifiersErrorMinorAlarmLevel_Type = Integer32
_RectifiersErrorMinorAlarmLevel_Object = MibScalar
rectifiersErrorMinorAlarmLevel = _RectifiersErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 4, 7),
    _RectifiersErrorMinorAlarmLevel_Type()
)
rectifiersErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersErrorMinorAlarmLevel.setStatus("current")


class _RectifiersNumberOfRectifiers_Type(Integer32):
    """Custom type rectifiersNumberOfRectifiers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RectifiersNumberOfRectifiers_Type.__name__ = "Integer32"
_RectifiersNumberOfRectifiers_Object = MibScalar
rectifiersNumberOfRectifiers = _RectifiersNumberOfRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 5),
    _RectifiersNumberOfRectifiers_Type()
)
rectifiersNumberOfRectifiers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersNumberOfRectifiers.setStatus("current")
_RectifierTable_Object = MibTable
rectifierTable = _RectifierTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6)
)
if mibBuilder.loadTexts:
    rectifierTable.setStatus("current")
_RectifierEntry_Object = MibTableRow
rectifierEntry = _RectifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1)
)
rectifierEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierIndex"),
)
if mibBuilder.loadTexts:
    rectifierEntry.setStatus("current")


class _RectifierIndex_Type(Integer32):
    """Custom type rectifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RectifierIndex_Type.__name__ = "Integer32"
_RectifierIndex_Object = MibTableColumn
rectifierIndex = _RectifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 1),
    _RectifierIndex_Type()
)
rectifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifierIndex.setStatus("current")


class _RectifierStatus_Type(Integer32):
    """Custom type rectifierStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifierStatus_Type.__name__ = "Integer32"
_RectifierStatus_Object = MibTableColumn
rectifierStatus = _RectifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 2),
    _RectifierStatus_Type()
)
rectifierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierStatus.setStatus("current")
_RectifierOutputCurrentValue_Type = Integer32
_RectifierOutputCurrentValue_Object = MibTableColumn
rectifierOutputCurrentValue = _RectifierOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 3),
    _RectifierOutputCurrentValue_Type()
)
rectifierOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierOutputCurrentValue.setStatus("current")
_RectifierInputVoltageValue_Type = Integer32
_RectifierInputVoltageValue_Object = MibTableColumn
rectifierInputVoltageValue = _RectifierInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 4),
    _RectifierInputVoltageValue_Type()
)
rectifierInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierInputVoltageValue.setStatus("current")


class _RectifierType_Type(DisplayString):
    """Custom type rectifierType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_RectifierType_Type.__name__ = "DisplayString"
_RectifierType_Object = MibTableColumn
rectifierType = _RectifierType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 5),
    _RectifierType_Type()
)
rectifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierType.setStatus("current")


class _RectifierHwPartNumber_Type(DisplayString):
    """Custom type rectifierHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RectifierHwPartNumber_Type.__name__ = "DisplayString"
_RectifierHwPartNumber_Object = MibTableColumn
rectifierHwPartNumber = _RectifierHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 6),
    _RectifierHwPartNumber_Type()
)
rectifierHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierHwPartNumber.setStatus("current")


class _RectifierHwVersion_Type(DisplayString):
    """Custom type rectifierHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RectifierHwVersion_Type.__name__ = "DisplayString"
_RectifierHwVersion_Object = MibTableColumn
rectifierHwVersion = _RectifierHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 7),
    _RectifierHwVersion_Type()
)
rectifierHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierHwVersion.setStatus("current")


class _RectifierSwPartNumber_Type(DisplayString):
    """Custom type rectifierSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RectifierSwPartNumber_Type.__name__ = "DisplayString"
_RectifierSwPartNumber_Object = MibTableColumn
rectifierSwPartNumber = _RectifierSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 8),
    _RectifierSwPartNumber_Type()
)
rectifierSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierSwPartNumber.setStatus("current")


class _RectifierSwVersion_Type(DisplayString):
    """Custom type rectifierSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RectifierSwVersion_Type.__name__ = "DisplayString"
_RectifierSwVersion_Object = MibTableColumn
rectifierSwVersion = _RectifierSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 6, 1, 9),
    _RectifierSwVersion_Type()
)
rectifierSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierSwVersion.setStatus("current")
_RectifiersEnergyLog_ObjectIdentity = ObjectIdentity
rectifiersEnergyLog = _RectifiersEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7)
)
_RectifiersEnergyLogAccumulated_Type = Integer32
_RectifiersEnergyLogAccumulated_Object = MibScalar
rectifiersEnergyLogAccumulated = _RectifiersEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 1),
    _RectifiersEnergyLogAccumulated_Type()
)
rectifiersEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogAccumulated.setStatus("current")


class _RectifiersEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type rectifiersEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_RectifiersEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastHoursNumberOfEntries_Object = MibScalar
rectifiersEnergyLogLastHoursNumberOfEntries = _RectifiersEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 2),
    _RectifiersEnergyLogLastHoursNumberOfEntries_Type()
)
rectifiersEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursNumberOfEntries.setStatus("current")
_RectifiersEnergyLogLastHoursTable_Object = MibTable
rectifiersEnergyLogLastHoursTable = _RectifiersEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 3)
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursTable.setStatus("current")
_RectifiersEnergyLogLastHoursEntry_Object = MibTableRow
rectifiersEnergyLogLastHoursEntry = _RectifiersEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 3, 1)
)
rectifiersEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "rectifiersEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursEntry.setStatus("current")


class _RectifiersEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type rectifiersEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifiersEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastHoursIndex_Object = MibTableColumn
rectifiersEnergyLogLastHoursIndex = _RectifiersEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 3, 1, 1),
    _RectifiersEnergyLogLastHoursIndex_Type()
)
rectifiersEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursIndex.setStatus("current")
_RectifiersEnergyLogLastHoursValue_Type = Integer32
_RectifiersEnergyLogLastHoursValue_Object = MibTableColumn
rectifiersEnergyLogLastHoursValue = _RectifiersEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 3, 1, 2),
    _RectifiersEnergyLogLastHoursValue_Type()
)
rectifiersEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastHoursValue.setStatus("current")


class _RectifiersEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type rectifiersEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_RectifiersEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastDaysNumberOfEntries_Object = MibScalar
rectifiersEnergyLogLastDaysNumberOfEntries = _RectifiersEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 4),
    _RectifiersEnergyLogLastDaysNumberOfEntries_Type()
)
rectifiersEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysNumberOfEntries.setStatus("current")
_RectifiersEnergyLogLastDaysTable_Object = MibTable
rectifiersEnergyLogLastDaysTable = _RectifiersEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 5)
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysTable.setStatus("current")
_RectifiersEnergyLogLastDaysEntry_Object = MibTableRow
rectifiersEnergyLogLastDaysEntry = _RectifiersEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 5, 1)
)
rectifiersEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "rectifiersEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysEntry.setStatus("current")


class _RectifiersEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type rectifiersEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifiersEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastDaysIndex_Object = MibTableColumn
rectifiersEnergyLogLastDaysIndex = _RectifiersEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 5, 1, 1),
    _RectifiersEnergyLogLastDaysIndex_Type()
)
rectifiersEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysIndex.setStatus("current")
_RectifiersEnergyLogLastDaysValue_Type = Integer32
_RectifiersEnergyLogLastDaysValue_Object = MibTableColumn
rectifiersEnergyLogLastDaysValue = _RectifiersEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 5, 1, 2),
    _RectifiersEnergyLogLastDaysValue_Type()
)
rectifiersEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastDaysValue.setStatus("current")


class _RectifiersEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type rectifiersEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_RectifiersEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
rectifiersEnergyLogLastWeeksNumberOfEntries = _RectifiersEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 6),
    _RectifiersEnergyLogLastWeeksNumberOfEntries_Type()
)
rectifiersEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_RectifiersEnergyLogLastWeeksTable_Object = MibTable
rectifiersEnergyLogLastWeeksTable = _RectifiersEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 7)
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksTable.setStatus("current")
_RectifiersEnergyLogLastWeeksEntry_Object = MibTableRow
rectifiersEnergyLogLastWeeksEntry = _RectifiersEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 7, 1)
)
rectifiersEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "rectifiersEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksEntry.setStatus("current")


class _RectifiersEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type rectifiersEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifiersEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_RectifiersEnergyLogLastWeeksIndex_Object = MibTableColumn
rectifiersEnergyLogLastWeeksIndex = _RectifiersEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 7, 1, 1),
    _RectifiersEnergyLogLastWeeksIndex_Type()
)
rectifiersEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksIndex.setStatus("current")
_RectifiersEnergyLogLastWeeksValue_Type = Integer32
_RectifiersEnergyLogLastWeeksValue_Object = MibTableColumn
rectifiersEnergyLogLastWeeksValue = _RectifiersEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 7, 7, 1, 2),
    _RectifiersEnergyLogLastWeeksValue_Type()
)
rectifiersEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersEnergyLogLastWeeksValue.setStatus("current")
_RectifiersNumberOfGroups_Type = Integer32
_RectifiersNumberOfGroups_Object = MibScalar
rectifiersNumberOfGroups = _RectifiersNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 8),
    _RectifiersNumberOfGroups_Type()
)
rectifiersNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersNumberOfGroups.setStatus("current")
_RectifierGroupsTable_Object = MibTable
rectifierGroupsTable = _RectifierGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 9)
)
if mibBuilder.loadTexts:
    rectifierGroupsTable.setStatus("current")
_RectifierGroupsEntry_Object = MibTableRow
rectifierGroupsEntry = _RectifierGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 9, 1)
)
rectifierGroupsEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupsEntry.setStatus("current")


class _RectifierGroupIndex_Type(Integer32):
    """Custom type rectifierGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RectifierGroupIndex_Type.__name__ = "Integer32"
_RectifierGroupIndex_Object = MibTableColumn
rectifierGroupIndex = _RectifierGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 9, 1, 1),
    _RectifierGroupIndex_Type()
)
rectifierGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifierGroupIndex.setStatus("current")


class _RectifierGroupStatus_Type(Integer32):
    """Custom type rectifierGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifierGroupStatus_Type.__name__ = "Integer32"
_RectifierGroupStatus_Object = MibTableColumn
rectifierGroupStatus = _RectifierGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 9, 1, 2),
    _RectifierGroupStatus_Type()
)
rectifierGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupStatus.setStatus("current")


class _RectifierGroupNumberOfRectifiers_Type(Integer32):
    """Custom type rectifierGroupNumberOfRectifiers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RectifierGroupNumberOfRectifiers_Type.__name__ = "Integer32"
_RectifierGroupNumberOfRectifiers_Object = MibTableColumn
rectifierGroupNumberOfRectifiers = _RectifierGroupNumberOfRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 9, 1, 3),
    _RectifierGroupNumberOfRectifiers_Type()
)
rectifierGroupNumberOfRectifiers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupNumberOfRectifiers.setStatus("current")
_RectifierGroupCurrentTable_Object = MibTable
rectifierGroupCurrentTable = _RectifierGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10)
)
if mibBuilder.loadTexts:
    rectifierGroupCurrentTable.setStatus("current")
_RectifierGroupCurrentEntry_Object = MibTableRow
rectifierGroupCurrentEntry = _RectifierGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10, 1)
)
rectifierGroupCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupCurrentEntry.setStatus("current")


class _RectifierGroupCurrentStatus_Type(Integer32):
    """Custom type rectifierGroupCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifierGroupCurrentStatus_Type.__name__ = "Integer32"
_RectifierGroupCurrentStatus_Object = MibTableColumn
rectifierGroupCurrentStatus = _RectifierGroupCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10, 1, 1),
    _RectifierGroupCurrentStatus_Type()
)
rectifierGroupCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupCurrentStatus.setStatus("current")


class _RectifierGroupCurrentDescription_Type(DisplayString):
    """Custom type rectifierGroupCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierGroupCurrentDescription_Type.__name__ = "DisplayString"
_RectifierGroupCurrentDescription_Object = MibTableColumn
rectifierGroupCurrentDescription = _RectifierGroupCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10, 1, 2),
    _RectifierGroupCurrentDescription_Type()
)
rectifierGroupCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupCurrentDescription.setStatus("current")
_RectifierGroupCurrentTrapRepeatCounter_Type = Integer32
_RectifierGroupCurrentTrapRepeatCounter_Object = MibTableColumn
rectifierGroupCurrentTrapRepeatCounter = _RectifierGroupCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10, 1, 3),
    _RectifierGroupCurrentTrapRepeatCounter_Type()
)
rectifierGroupCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifierGroupCurrentTrapRepeatCounter.setStatus("current")


class _RectifierGroupCurrentAlarmEnable_Type(Integer32):
    """Custom type rectifierGroupCurrentAlarmEnable based on Integer32"""
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


_RectifierGroupCurrentAlarmEnable_Type.__name__ = "Integer32"
_RectifierGroupCurrentAlarmEnable_Object = MibTableColumn
rectifierGroupCurrentAlarmEnable = _RectifierGroupCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10, 1, 4),
    _RectifierGroupCurrentAlarmEnable_Type()
)
rectifierGroupCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupCurrentAlarmEnable.setStatus("current")
_RectifierGroupCurrentValue_Type = Integer32
_RectifierGroupCurrentValue_Object = MibTableColumn
rectifierGroupCurrentValue = _RectifierGroupCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10, 1, 5),
    _RectifierGroupCurrentValue_Type()
)
rectifierGroupCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupCurrentValue.setStatus("current")
_RectifierGroupCurrentMajorAlarmLevel_Type = Integer32
_RectifierGroupCurrentMajorAlarmLevel_Object = MibTableColumn
rectifierGroupCurrentMajorAlarmLevel = _RectifierGroupCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10, 1, 6),
    _RectifierGroupCurrentMajorAlarmLevel_Type()
)
rectifierGroupCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupCurrentMajorAlarmLevel.setStatus("current")
_RectifierGroupCurrentMinorAlarmLevel_Type = Integer32
_RectifierGroupCurrentMinorAlarmLevel_Object = MibTableColumn
rectifierGroupCurrentMinorAlarmLevel = _RectifierGroupCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 10, 1, 7),
    _RectifierGroupCurrentMinorAlarmLevel_Type()
)
rectifierGroupCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupCurrentMinorAlarmLevel.setStatus("current")
_RectifierGroupCapacityTable_Object = MibTable
rectifierGroupCapacityTable = _RectifierGroupCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11)
)
if mibBuilder.loadTexts:
    rectifierGroupCapacityTable.setStatus("current")
_RectifierGroupCapacityEntry_Object = MibTableRow
rectifierGroupCapacityEntry = _RectifierGroupCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11, 1)
)
rectifierGroupCapacityEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupCapacityEntry.setStatus("current")


class _RectifierGroupCapacityStatus_Type(Integer32):
    """Custom type rectifierGroupCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifierGroupCapacityStatus_Type.__name__ = "Integer32"
_RectifierGroupCapacityStatus_Object = MibTableColumn
rectifierGroupCapacityStatus = _RectifierGroupCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11, 1, 1),
    _RectifierGroupCapacityStatus_Type()
)
rectifierGroupCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupCapacityStatus.setStatus("current")


class _RectifierGroupCapacityDescription_Type(DisplayString):
    """Custom type rectifierGroupCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierGroupCapacityDescription_Type.__name__ = "DisplayString"
_RectifierGroupCapacityDescription_Object = MibTableColumn
rectifierGroupCapacityDescription = _RectifierGroupCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11, 1, 2),
    _RectifierGroupCapacityDescription_Type()
)
rectifierGroupCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupCapacityDescription.setStatus("current")
_RectifierGroupCapacityTrapRepeatCounter_Type = Integer32
_RectifierGroupCapacityTrapRepeatCounter_Object = MibTableColumn
rectifierGroupCapacityTrapRepeatCounter = _RectifierGroupCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11, 1, 3),
    _RectifierGroupCapacityTrapRepeatCounter_Type()
)
rectifierGroupCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifierGroupCapacityTrapRepeatCounter.setStatus("current")


class _RectifierGroupCapacityAlarmEnable_Type(Integer32):
    """Custom type rectifierGroupCapacityAlarmEnable based on Integer32"""
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


_RectifierGroupCapacityAlarmEnable_Type.__name__ = "Integer32"
_RectifierGroupCapacityAlarmEnable_Object = MibTableColumn
rectifierGroupCapacityAlarmEnable = _RectifierGroupCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11, 1, 4),
    _RectifierGroupCapacityAlarmEnable_Type()
)
rectifierGroupCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupCapacityAlarmEnable.setStatus("current")
_RectifierGroupCapacityValue_Type = Integer32
_RectifierGroupCapacityValue_Object = MibTableColumn
rectifierGroupCapacityValue = _RectifierGroupCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11, 1, 5),
    _RectifierGroupCapacityValue_Type()
)
rectifierGroupCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupCapacityValue.setStatus("current")
_RectifierGroupCapacityMajorAlarmLevel_Type = Integer32
_RectifierGroupCapacityMajorAlarmLevel_Object = MibTableColumn
rectifierGroupCapacityMajorAlarmLevel = _RectifierGroupCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11, 1, 6),
    _RectifierGroupCapacityMajorAlarmLevel_Type()
)
rectifierGroupCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupCapacityMajorAlarmLevel.setStatus("current")
_RectifierGroupCapacityMinorAlarmLevel_Type = Integer32
_RectifierGroupCapacityMinorAlarmLevel_Object = MibTableColumn
rectifierGroupCapacityMinorAlarmLevel = _RectifierGroupCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 11, 1, 7),
    _RectifierGroupCapacityMinorAlarmLevel_Type()
)
rectifierGroupCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupCapacityMinorAlarmLevel.setStatus("current")
_RectifierGroupErrorTable_Object = MibTable
rectifierGroupErrorTable = _RectifierGroupErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12)
)
if mibBuilder.loadTexts:
    rectifierGroupErrorTable.setStatus("current")
_RectifierGroupErrorEntry_Object = MibTableRow
rectifierGroupErrorEntry = _RectifierGroupErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12, 1)
)
rectifierGroupErrorEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupErrorEntry.setStatus("current")


class _RectifierGroupErrorStatus_Type(Integer32):
    """Custom type rectifierGroupErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifierGroupErrorStatus_Type.__name__ = "Integer32"
_RectifierGroupErrorStatus_Object = MibTableColumn
rectifierGroupErrorStatus = _RectifierGroupErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12, 1, 1),
    _RectifierGroupErrorStatus_Type()
)
rectifierGroupErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupErrorStatus.setStatus("current")


class _RectifierGroupErrorDescription_Type(DisplayString):
    """Custom type rectifierGroupErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierGroupErrorDescription_Type.__name__ = "DisplayString"
_RectifierGroupErrorDescription_Object = MibTableColumn
rectifierGroupErrorDescription = _RectifierGroupErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12, 1, 2),
    _RectifierGroupErrorDescription_Type()
)
rectifierGroupErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupErrorDescription.setStatus("current")
_RectifierGroupErrorTrapRepeatCounter_Type = Integer32
_RectifierGroupErrorTrapRepeatCounter_Object = MibTableColumn
rectifierGroupErrorTrapRepeatCounter = _RectifierGroupErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12, 1, 3),
    _RectifierGroupErrorTrapRepeatCounter_Type()
)
rectifierGroupErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifierGroupErrorTrapRepeatCounter.setStatus("current")


class _RectifierGroupErrorAlarmEnable_Type(Integer32):
    """Custom type rectifierGroupErrorAlarmEnable based on Integer32"""
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


_RectifierGroupErrorAlarmEnable_Type.__name__ = "Integer32"
_RectifierGroupErrorAlarmEnable_Object = MibTableColumn
rectifierGroupErrorAlarmEnable = _RectifierGroupErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12, 1, 4),
    _RectifierGroupErrorAlarmEnable_Type()
)
rectifierGroupErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupErrorAlarmEnable.setStatus("current")
_RectifierGroupErrorValue_Type = Integer32
_RectifierGroupErrorValue_Object = MibTableColumn
rectifierGroupErrorValue = _RectifierGroupErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12, 1, 5),
    _RectifierGroupErrorValue_Type()
)
rectifierGroupErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupErrorValue.setStatus("current")
_RectifierGroupErrorMajorAlarmLevel_Type = Integer32
_RectifierGroupErrorMajorAlarmLevel_Object = MibTableColumn
rectifierGroupErrorMajorAlarmLevel = _RectifierGroupErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12, 1, 6),
    _RectifierGroupErrorMajorAlarmLevel_Type()
)
rectifierGroupErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupErrorMajorAlarmLevel.setStatus("current")
_RectifierGroupErrorMinorAlarmLevel_Type = Integer32
_RectifierGroupErrorMinorAlarmLevel_Object = MibTableColumn
rectifierGroupErrorMinorAlarmLevel = _RectifierGroupErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 12, 1, 7),
    _RectifierGroupErrorMinorAlarmLevel_Type()
)
rectifierGroupErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupErrorMinorAlarmLevel.setStatus("current")
_RectifierGroupRectifierTable_Object = MibTable
rectifierGroupRectifierTable = _RectifierGroupRectifierTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13)
)
if mibBuilder.loadTexts:
    rectifierGroupRectifierTable.setStatus("current")
_RectifierGroupRectifierEntry_Object = MibTableRow
rectifierGroupRectifierEntry = _RectifierGroupRectifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1)
)
rectifierGroupRectifierEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
    (0, "SP2-MIB", "rectifierGroupRectifierIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupRectifierEntry.setStatus("current")


class _RectifierGroupRectifierIndex_Type(Integer32):
    """Custom type rectifierGroupRectifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RectifierGroupRectifierIndex_Type.__name__ = "Integer32"
_RectifierGroupRectifierIndex_Object = MibTableColumn
rectifierGroupRectifierIndex = _RectifierGroupRectifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 1),
    _RectifierGroupRectifierIndex_Type()
)
rectifierGroupRectifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifierGroupRectifierIndex.setStatus("current")


class _RectifierGroupRectifierStatus_Type(Integer32):
    """Custom type rectifierGroupRectifierStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifierGroupRectifierStatus_Type.__name__ = "Integer32"
_RectifierGroupRectifierStatus_Object = MibTableColumn
rectifierGroupRectifierStatus = _RectifierGroupRectifierStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 2),
    _RectifierGroupRectifierStatus_Type()
)
rectifierGroupRectifierStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupRectifierStatus.setStatus("current")
_RectifierGroupRectifierOutputCurrentValue_Type = Integer32
_RectifierGroupRectifierOutputCurrentValue_Object = MibTableColumn
rectifierGroupRectifierOutputCurrentValue = _RectifierGroupRectifierOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 3),
    _RectifierGroupRectifierOutputCurrentValue_Type()
)
rectifierGroupRectifierOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupRectifierOutputCurrentValue.setStatus("current")
_RectifierGroupRectifierInputVoltageValue_Type = Integer32
_RectifierGroupRectifierInputVoltageValue_Object = MibTableColumn
rectifierGroupRectifierInputVoltageValue = _RectifierGroupRectifierInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 4),
    _RectifierGroupRectifierInputVoltageValue_Type()
)
rectifierGroupRectifierInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupRectifierInputVoltageValue.setStatus("current")


class _RectifierGroupRectifierType_Type(DisplayString):
    """Custom type rectifierGroupRectifierType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_RectifierGroupRectifierType_Type.__name__ = "DisplayString"
_RectifierGroupRectifierType_Object = MibTableColumn
rectifierGroupRectifierType = _RectifierGroupRectifierType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 5),
    _RectifierGroupRectifierType_Type()
)
rectifierGroupRectifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupRectifierType.setStatus("current")


class _RectifierGroupRectifierHwPartNumber_Type(DisplayString):
    """Custom type rectifierGroupRectifierHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RectifierGroupRectifierHwPartNumber_Type.__name__ = "DisplayString"
_RectifierGroupRectifierHwPartNumber_Object = MibTableColumn
rectifierGroupRectifierHwPartNumber = _RectifierGroupRectifierHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 6),
    _RectifierGroupRectifierHwPartNumber_Type()
)
rectifierGroupRectifierHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupRectifierHwPartNumber.setStatus("current")


class _RectifierGroupRectifierHwVersion_Type(DisplayString):
    """Custom type rectifierGroupRectifierHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RectifierGroupRectifierHwVersion_Type.__name__ = "DisplayString"
_RectifierGroupRectifierHwVersion_Object = MibTableColumn
rectifierGroupRectifierHwVersion = _RectifierGroupRectifierHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 7),
    _RectifierGroupRectifierHwVersion_Type()
)
rectifierGroupRectifierHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupRectifierHwVersion.setStatus("current")


class _RectifierGroupRectifierSwPartNumber_Type(DisplayString):
    """Custom type rectifierGroupRectifierSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RectifierGroupRectifierSwPartNumber_Type.__name__ = "DisplayString"
_RectifierGroupRectifierSwPartNumber_Object = MibTableColumn
rectifierGroupRectifierSwPartNumber = _RectifierGroupRectifierSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 8),
    _RectifierGroupRectifierSwPartNumber_Type()
)
rectifierGroupRectifierSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupRectifierSwPartNumber.setStatus("current")


class _RectifierGroupRectifierSwVersion_Type(DisplayString):
    """Custom type rectifierGroupRectifierSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RectifierGroupRectifierSwVersion_Type.__name__ = "DisplayString"
_RectifierGroupRectifierSwVersion_Object = MibTableColumn
rectifierGroupRectifierSwVersion = _RectifierGroupRectifierSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 13, 1, 9),
    _RectifierGroupRectifierSwVersion_Type()
)
rectifierGroupRectifierSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupRectifierSwVersion.setStatus("current")
_RectifierGroupEnergyLogTable_Object = MibTable
rectifierGroupEnergyLogTable = _RectifierGroupEnergyLogTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 14)
)
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogTable.setStatus("current")
_RectifierGroupEnergyLogEntry_Object = MibTableRow
rectifierGroupEnergyLogEntry = _RectifierGroupEnergyLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 14, 1)
)
rectifierGroupEnergyLogEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogEntry.setStatus("current")
_RectifierGroupEnergyLogAccumulated_Type = Integer32
_RectifierGroupEnergyLogAccumulated_Object = MibTableColumn
rectifierGroupEnergyLogAccumulated = _RectifierGroupEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 14, 1, 1),
    _RectifierGroupEnergyLogAccumulated_Type()
)
rectifierGroupEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogAccumulated.setStatus("current")
_RectifierGroupEnergyLogLastHoursNumberOfEntries_Type = Integer32
_RectifierGroupEnergyLogLastHoursNumberOfEntries_Object = MibTableColumn
rectifierGroupEnergyLogLastHoursNumberOfEntries = _RectifierGroupEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 14, 1, 2),
    _RectifierGroupEnergyLogLastHoursNumberOfEntries_Type()
)
rectifierGroupEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastHoursNumberOfEntries.setStatus("current")
_RectifierGroupEnergyLogLastDaysNumberOfEntries_Type = Integer32
_RectifierGroupEnergyLogLastDaysNumberOfEntries_Object = MibTableColumn
rectifierGroupEnergyLogLastDaysNumberOfEntries = _RectifierGroupEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 14, 1, 3),
    _RectifierGroupEnergyLogLastDaysNumberOfEntries_Type()
)
rectifierGroupEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastDaysNumberOfEntries.setStatus("current")
_RectifierGroupEnergyLogLastWeeksNumberOfEntries_Type = Integer32
_RectifierGroupEnergyLogLastWeeksNumberOfEntries_Object = MibTableColumn
rectifierGroupEnergyLogLastWeeksNumberOfEntries = _RectifierGroupEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 14, 1, 4),
    _RectifierGroupEnergyLogLastWeeksNumberOfEntries_Type()
)
rectifierGroupEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_RectifierGroupEnergyLogLastHoursTable_Object = MibTable
rectifierGroupEnergyLogLastHoursTable = _RectifierGroupEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 15)
)
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastHoursTable.setStatus("current")
_RectifierGroupEnergyLogLastHoursEntry_Object = MibTableRow
rectifierGroupEnergyLogLastHoursEntry = _RectifierGroupEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 15, 1)
)
rectifierGroupEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
    (0, "SP2-MIB", "rectifierGroupEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastHoursEntry.setStatus("current")


class _RectifierGroupEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type rectifierGroupEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifierGroupEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_RectifierGroupEnergyLogLastHoursIndex_Object = MibTableColumn
rectifierGroupEnergyLogLastHoursIndex = _RectifierGroupEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 15, 1, 1),
    _RectifierGroupEnergyLogLastHoursIndex_Type()
)
rectifierGroupEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastHoursIndex.setStatus("current")
_RectifierGroupEnergyLogLastHoursValue_Type = Integer32
_RectifierGroupEnergyLogLastHoursValue_Object = MibTableColumn
rectifierGroupEnergyLogLastHoursValue = _RectifierGroupEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 15, 1, 2),
    _RectifierGroupEnergyLogLastHoursValue_Type()
)
rectifierGroupEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastHoursValue.setStatus("current")
_RectifierGroupEnergyLogLastDaysTable_Object = MibTable
rectifierGroupEnergyLogLastDaysTable = _RectifierGroupEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 16)
)
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastDaysTable.setStatus("current")
_RectifierGroupEnergyLogLastDaysEntry_Object = MibTableRow
rectifierGroupEnergyLogLastDaysEntry = _RectifierGroupEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 16, 1)
)
rectifierGroupEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
    (0, "SP2-MIB", "rectifierGroupEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastDaysEntry.setStatus("current")


class _RectifierGroupEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type rectifierGroupEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifierGroupEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_RectifierGroupEnergyLogLastDaysIndex_Object = MibTableColumn
rectifierGroupEnergyLogLastDaysIndex = _RectifierGroupEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 16, 1, 1),
    _RectifierGroupEnergyLogLastDaysIndex_Type()
)
rectifierGroupEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastDaysIndex.setStatus("current")
_RectifierGroupEnergyLogLastDaysValue_Type = Integer32
_RectifierGroupEnergyLogLastDaysValue_Object = MibTableColumn
rectifierGroupEnergyLogLastDaysValue = _RectifierGroupEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 16, 1, 2),
    _RectifierGroupEnergyLogLastDaysValue_Type()
)
rectifierGroupEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastDaysValue.setStatus("current")
_RectifierGroupEnergyLogLastWeeksTable_Object = MibTable
rectifierGroupEnergyLogLastWeeksTable = _RectifierGroupEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 17)
)
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastWeeksTable.setStatus("current")
_RectifierGroupEnergyLogLastWeeksEntry_Object = MibTableRow
rectifierGroupEnergyLogLastWeeksEntry = _RectifierGroupEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 17, 1)
)
rectifierGroupEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
    (0, "SP2-MIB", "rectifierGroupEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastWeeksEntry.setStatus("current")


class _RectifierGroupEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type rectifierGroupEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_RectifierGroupEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_RectifierGroupEnergyLogLastWeeksIndex_Object = MibTableColumn
rectifierGroupEnergyLogLastWeeksIndex = _RectifierGroupEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 17, 1, 1),
    _RectifierGroupEnergyLogLastWeeksIndex_Type()
)
rectifierGroupEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastWeeksIndex.setStatus("current")
_RectifierGroupEnergyLogLastWeeksValue_Type = Integer32
_RectifierGroupEnergyLogLastWeeksValue_Object = MibTableColumn
rectifierGroupEnergyLogLastWeeksValue = _RectifierGroupEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 17, 1, 2),
    _RectifierGroupEnergyLogLastWeeksValue_Type()
)
rectifierGroupEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupEnergyLogLastWeeksValue.setStatus("current")
_RectifiersTemperature_ObjectIdentity = ObjectIdentity
rectifiersTemperature = _RectifiersTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18)
)


class _RectifiersTemperatureStatus_Type(Integer32):
    """Custom type rectifiersTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifiersTemperatureStatus_Type.__name__ = "Integer32"
_RectifiersTemperatureStatus_Object = MibScalar
rectifiersTemperatureStatus = _RectifiersTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 1),
    _RectifiersTemperatureStatus_Type()
)
rectifiersTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersTemperatureStatus.setStatus("current")


class _RectifiersTemperatureDescription_Type(DisplayString):
    """Custom type rectifiersTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifiersTemperatureDescription_Type.__name__ = "DisplayString"
_RectifiersTemperatureDescription_Object = MibScalar
rectifiersTemperatureDescription = _RectifiersTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 2),
    _RectifiersTemperatureDescription_Type()
)
rectifiersTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersTemperatureDescription.setStatus("current")
_RectifiersTemperatureTrapRepeatCounter_Type = Counter32
_RectifiersTemperatureTrapRepeatCounter_Object = MibScalar
rectifiersTemperatureTrapRepeatCounter = _RectifiersTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 3),
    _RectifiersTemperatureTrapRepeatCounter_Type()
)
rectifiersTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifiersTemperatureTrapRepeatCounter.setStatus("current")


class _RectifiersTemperatureAlarmEnable_Type(Integer32):
    """Custom type rectifiersTemperatureAlarmEnable based on Integer32"""
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


_RectifiersTemperatureAlarmEnable_Type.__name__ = "Integer32"
_RectifiersTemperatureAlarmEnable_Object = MibScalar
rectifiersTemperatureAlarmEnable = _RectifiersTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 4),
    _RectifiersTemperatureAlarmEnable_Type()
)
rectifiersTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersTemperatureAlarmEnable.setStatus("current")


class _RectifiersTemperatureValue_Type(Integer32):
    """Custom type rectifiersTemperatureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_RectifiersTemperatureValue_Type.__name__ = "Integer32"
_RectifiersTemperatureValue_Object = MibScalar
rectifiersTemperatureValue = _RectifiersTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 5),
    _RectifiersTemperatureValue_Type()
)
rectifiersTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifiersTemperatureValue.setStatus("current")
_RectifiersTemperatureMajorHighLevel_Type = Integer32
_RectifiersTemperatureMajorHighLevel_Object = MibScalar
rectifiersTemperatureMajorHighLevel = _RectifiersTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 6),
    _RectifiersTemperatureMajorHighLevel_Type()
)
rectifiersTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersTemperatureMajorHighLevel.setStatus("current")
_RectifiersTemperatureMinorHighLevel_Type = Integer32
_RectifiersTemperatureMinorHighLevel_Object = MibScalar
rectifiersTemperatureMinorHighLevel = _RectifiersTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 7),
    _RectifiersTemperatureMinorHighLevel_Type()
)
rectifiersTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersTemperatureMinorHighLevel.setStatus("current")
_RectifiersTemperatureMinorLowLevel_Type = Integer32
_RectifiersTemperatureMinorLowLevel_Object = MibScalar
rectifiersTemperatureMinorLowLevel = _RectifiersTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 8),
    _RectifiersTemperatureMinorLowLevel_Type()
)
rectifiersTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersTemperatureMinorLowLevel.setStatus("current")
_RectifiersTemperatureMajorLowLevel_Type = Integer32
_RectifiersTemperatureMajorLowLevel_Object = MibScalar
rectifiersTemperatureMajorLowLevel = _RectifiersTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 18, 9),
    _RectifiersTemperatureMajorLowLevel_Type()
)
rectifiersTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifiersTemperatureMajorLowLevel.setStatus("current")
_RectifierGroupTemperatureTable_Object = MibTable
rectifierGroupTemperatureTable = _RectifierGroupTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19)
)
if mibBuilder.loadTexts:
    rectifierGroupTemperatureTable.setStatus("current")
_RectifierGroupTemperatureEntry_Object = MibTableRow
rectifierGroupTemperatureEntry = _RectifierGroupTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1)
)
rectifierGroupTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "rectifierGroupIndex"),
)
if mibBuilder.loadTexts:
    rectifierGroupTemperatureEntry.setStatus("current")


class _RectifierGroupTemperatureStatus_Type(Integer32):
    """Custom type rectifierGroupTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_RectifierGroupTemperatureStatus_Type.__name__ = "Integer32"
_RectifierGroupTemperatureStatus_Object = MibTableColumn
rectifierGroupTemperatureStatus = _RectifierGroupTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 1),
    _RectifierGroupTemperatureStatus_Type()
)
rectifierGroupTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureStatus.setStatus("current")


class _RectifierGroupTemperatureDescription_Type(DisplayString):
    """Custom type rectifierGroupTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RectifierGroupTemperatureDescription_Type.__name__ = "DisplayString"
_RectifierGroupTemperatureDescription_Object = MibTableColumn
rectifierGroupTemperatureDescription = _RectifierGroupTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 2),
    _RectifierGroupTemperatureDescription_Type()
)
rectifierGroupTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureDescription.setStatus("current")
_RectifierGroupTemperatureTrapRepeatCounter_Type = Integer32
_RectifierGroupTemperatureTrapRepeatCounter_Object = MibTableColumn
rectifierGroupTemperatureTrapRepeatCounter = _RectifierGroupTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 3),
    _RectifierGroupTemperatureTrapRepeatCounter_Type()
)
rectifierGroupTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureTrapRepeatCounter.setStatus("current")


class _RectifierGroupTemperatureAlarmEnable_Type(Integer32):
    """Custom type rectifierGroupTemperatureAlarmEnable based on Integer32"""
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


_RectifierGroupTemperatureAlarmEnable_Type.__name__ = "Integer32"
_RectifierGroupTemperatureAlarmEnable_Object = MibTableColumn
rectifierGroupTemperatureAlarmEnable = _RectifierGroupTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 4),
    _RectifierGroupTemperatureAlarmEnable_Type()
)
rectifierGroupTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureAlarmEnable.setStatus("current")
_RectifierGroupTemperatureValue_Type = Integer32
_RectifierGroupTemperatureValue_Object = MibTableColumn
rectifierGroupTemperatureValue = _RectifierGroupTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 5),
    _RectifierGroupTemperatureValue_Type()
)
rectifierGroupTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureValue.setStatus("current")
_RectifierGroupTemperatureMajorHighLevel_Type = Integer32
_RectifierGroupTemperatureMajorHighLevel_Object = MibTableColumn
rectifierGroupTemperatureMajorHighLevel = _RectifierGroupTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 6),
    _RectifierGroupTemperatureMajorHighLevel_Type()
)
rectifierGroupTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureMajorHighLevel.setStatus("current")
_RectifierGroupTemperatureMinorHighLevel_Type = Integer32
_RectifierGroupTemperatureMinorHighLevel_Object = MibTableColumn
rectifierGroupTemperatureMinorHighLevel = _RectifierGroupTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 7),
    _RectifierGroupTemperatureMinorHighLevel_Type()
)
rectifierGroupTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureMinorHighLevel.setStatus("current")
_RectifierGroupTemperatureMinorLowLevel_Type = Integer32
_RectifierGroupTemperatureMinorLowLevel_Object = MibTableColumn
rectifierGroupTemperatureMinorLowLevel = _RectifierGroupTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 8),
    _RectifierGroupTemperatureMinorLowLevel_Type()
)
rectifierGroupTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureMinorLowLevel.setStatus("current")
_RectifierGroupTemperatureMajorLowLevel_Type = Integer32
_RectifierGroupTemperatureMajorLowLevel_Object = MibTableColumn
rectifierGroupTemperatureMajorLowLevel = _RectifierGroupTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 5, 19, 1, 9),
    _RectifierGroupTemperatureMajorLowLevel_Type()
)
rectifierGroupTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rectifierGroupTemperatureMajorLowLevel.setStatus("current")
_Dcdc_ObjectIdentity = ObjectIdentity
dcdc = _Dcdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6)
)


class _DcdcNumberOfGroups_Type(Integer32):
    """Custom type dcdcNumberOfGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DcdcNumberOfGroups_Type.__name__ = "Integer32"
_DcdcNumberOfGroups_Object = MibScalar
dcdcNumberOfGroups = _DcdcNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 1),
    _DcdcNumberOfGroups_Type()
)
dcdcNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcNumberOfGroups.setStatus("current")
_DcdcGroupsTable_Object = MibTable
dcdcGroupsTable = _DcdcGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2)
)
if mibBuilder.loadTexts:
    dcdcGroupsTable.setStatus("current")
_DcdcGroupsEntry_Object = MibTableRow
dcdcGroupsEntry = _DcdcGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1)
)
dcdcGroupsEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcGroupsEntry.setStatus("current")


class _DcdcGroupIndex_Type(Integer32):
    """Custom type dcdcGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DcdcGroupIndex_Type.__name__ = "Integer32"
_DcdcGroupIndex_Object = MibTableColumn
dcdcGroupIndex = _DcdcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 1),
    _DcdcGroupIndex_Type()
)
dcdcGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcdcGroupIndex.setStatus("current")


class _DcdcGroupStatus_Type(Integer32):
    """Custom type dcdcGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_DcdcGroupStatus_Type.__name__ = "Integer32"
_DcdcGroupStatus_Object = MibTableColumn
dcdcGroupStatus = _DcdcGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 2),
    _DcdcGroupStatus_Type()
)
dcdcGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcGroupStatus.setStatus("current")
_DcdcGroupNumberOfDcdcConverters_Type = Integer32
_DcdcGroupNumberOfDcdcConverters_Object = MibTableColumn
dcdcGroupNumberOfDcdcConverters = _DcdcGroupNumberOfDcdcConverters_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 3),
    _DcdcGroupNumberOfDcdcConverters_Type()
)
dcdcGroupNumberOfDcdcConverters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcGroupNumberOfDcdcConverters.setStatus("current")
_DcdcGroupOutputVoltage_Type = Integer32
_DcdcGroupOutputVoltage_Object = MibTableColumn
dcdcGroupOutputVoltage = _DcdcGroupOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 4),
    _DcdcGroupOutputVoltage_Type()
)
dcdcGroupOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcGroupOutputVoltage.setStatus("current")


class _DcdcNumberOfCurrents_Type(Integer32):
    """Custom type dcdcNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DcdcNumberOfCurrents_Type.__name__ = "Integer32"
_DcdcNumberOfCurrents_Object = MibTableColumn
dcdcNumberOfCurrents = _DcdcNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 5),
    _DcdcNumberOfCurrents_Type()
)
dcdcNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcNumberOfCurrents.setStatus("current")


class _DcdcNumberOfCapacities_Type(Integer32):
    """Custom type dcdcNumberOfCapacities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DcdcNumberOfCapacities_Type.__name__ = "Integer32"
_DcdcNumberOfCapacities_Object = MibTableColumn
dcdcNumberOfCapacities = _DcdcNumberOfCapacities_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 6),
    _DcdcNumberOfCapacities_Type()
)
dcdcNumberOfCapacities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcNumberOfCapacities.setStatus("current")


class _DcdcNumberOfAlarms_Type(Integer32):
    """Custom type dcdcNumberOfAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_DcdcNumberOfAlarms_Type.__name__ = "Integer32"
_DcdcNumberOfAlarms_Object = MibTableColumn
dcdcNumberOfAlarms = _DcdcNumberOfAlarms_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 2, 1, 7),
    _DcdcNumberOfAlarms_Type()
)
dcdcNumberOfAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcNumberOfAlarms.setStatus("current")
_DcdcCurrentTable_Object = MibTable
dcdcCurrentTable = _DcdcCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3)
)
if mibBuilder.loadTexts:
    dcdcCurrentTable.setStatus("current")
_DcdcCurrentEntry_Object = MibTableRow
dcdcCurrentEntry = _DcdcCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1)
)
dcdcCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcCurrentEntry.setStatus("current")


class _DcdcCurrentStatus_Type(Integer32):
    """Custom type dcdcCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_DcdcCurrentStatus_Type.__name__ = "Integer32"
_DcdcCurrentStatus_Object = MibTableColumn
dcdcCurrentStatus = _DcdcCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 1),
    _DcdcCurrentStatus_Type()
)
dcdcCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCurrentStatus.setStatus("current")


class _DcdcCurrentDescription_Type(DisplayString):
    """Custom type dcdcCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DcdcCurrentDescription_Type.__name__ = "DisplayString"
_DcdcCurrentDescription_Object = MibTableColumn
dcdcCurrentDescription = _DcdcCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 2),
    _DcdcCurrentDescription_Type()
)
dcdcCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCurrentDescription.setStatus("current")
_DcdcCurrentTrapRepeatCounter_Type = Counter32
_DcdcCurrentTrapRepeatCounter_Object = MibTableColumn
dcdcCurrentTrapRepeatCounter = _DcdcCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 3),
    _DcdcCurrentTrapRepeatCounter_Type()
)
dcdcCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dcdcCurrentTrapRepeatCounter.setStatus("current")


class _DcdcCurrentAlarmEnable_Type(Integer32):
    """Custom type dcdcCurrentAlarmEnable based on Integer32"""
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


_DcdcCurrentAlarmEnable_Type.__name__ = "Integer32"
_DcdcCurrentAlarmEnable_Object = MibTableColumn
dcdcCurrentAlarmEnable = _DcdcCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 4),
    _DcdcCurrentAlarmEnable_Type()
)
dcdcCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCurrentAlarmEnable.setStatus("current")
_DcdcCurrentValue_Type = Integer32
_DcdcCurrentValue_Object = MibTableColumn
dcdcCurrentValue = _DcdcCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 5),
    _DcdcCurrentValue_Type()
)
dcdcCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCurrentValue.setStatus("current")
_DcdcCurrentMajorAlarmLevel_Type = Integer32
_DcdcCurrentMajorAlarmLevel_Object = MibTableColumn
dcdcCurrentMajorAlarmLevel = _DcdcCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 6),
    _DcdcCurrentMajorAlarmLevel_Type()
)
dcdcCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCurrentMajorAlarmLevel.setStatus("current")
_DcdcCurrentMinorAlarmLevel_Type = Integer32
_DcdcCurrentMinorAlarmLevel_Object = MibTableColumn
dcdcCurrentMinorAlarmLevel = _DcdcCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 3, 1, 7),
    _DcdcCurrentMinorAlarmLevel_Type()
)
dcdcCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCurrentMinorAlarmLevel.setStatus("current")
_DcdcCapacityTable_Object = MibTable
dcdcCapacityTable = _DcdcCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4)
)
if mibBuilder.loadTexts:
    dcdcCapacityTable.setStatus("current")
_DcdcCapacityEntry_Object = MibTableRow
dcdcCapacityEntry = _DcdcCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1)
)
dcdcCapacityEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcCapacityEntry.setStatus("current")


class _DcdcCapacityStatus_Type(Integer32):
    """Custom type dcdcCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_DcdcCapacityStatus_Type.__name__ = "Integer32"
_DcdcCapacityStatus_Object = MibTableColumn
dcdcCapacityStatus = _DcdcCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 1),
    _DcdcCapacityStatus_Type()
)
dcdcCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCapacityStatus.setStatus("current")


class _DcdcCapacityDescription_Type(DisplayString):
    """Custom type dcdcCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DcdcCapacityDescription_Type.__name__ = "DisplayString"
_DcdcCapacityDescription_Object = MibTableColumn
dcdcCapacityDescription = _DcdcCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 2),
    _DcdcCapacityDescription_Type()
)
dcdcCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCapacityDescription.setStatus("current")
_DcdcCapacityTrapRepeatCounter_Type = Counter32
_DcdcCapacityTrapRepeatCounter_Object = MibTableColumn
dcdcCapacityTrapRepeatCounter = _DcdcCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 3),
    _DcdcCapacityTrapRepeatCounter_Type()
)
dcdcCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dcdcCapacityTrapRepeatCounter.setStatus("current")


class _DcdcCapacityAlarmEnable_Type(Integer32):
    """Custom type dcdcCapacityAlarmEnable based on Integer32"""
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


_DcdcCapacityAlarmEnable_Type.__name__ = "Integer32"
_DcdcCapacityAlarmEnable_Object = MibTableColumn
dcdcCapacityAlarmEnable = _DcdcCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 4),
    _DcdcCapacityAlarmEnable_Type()
)
dcdcCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCapacityAlarmEnable.setStatus("current")
_DcdcCapacityValue_Type = Integer32
_DcdcCapacityValue_Object = MibTableColumn
dcdcCapacityValue = _DcdcCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 5),
    _DcdcCapacityValue_Type()
)
dcdcCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcCapacityValue.setStatus("current")
_DcdcCapacityMajorAlarmLevel_Type = Integer32
_DcdcCapacityMajorAlarmLevel_Object = MibTableColumn
dcdcCapacityMajorAlarmLevel = _DcdcCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 6),
    _DcdcCapacityMajorAlarmLevel_Type()
)
dcdcCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCapacityMajorAlarmLevel.setStatus("current")
_DcdcCapacityMinorAlarmLevel_Type = Integer32
_DcdcCapacityMinorAlarmLevel_Object = MibTableColumn
dcdcCapacityMinorAlarmLevel = _DcdcCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 4, 1, 7),
    _DcdcCapacityMinorAlarmLevel_Type()
)
dcdcCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcCapacityMinorAlarmLevel.setStatus("current")
_DcdcTable_Object = MibTable
dcdcTable = _DcdcTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5)
)
if mibBuilder.loadTexts:
    dcdcTable.setStatus("current")
_DcdcEntry_Object = MibTableRow
dcdcEntry = _DcdcEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1)
)
dcdcEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
    (0, "SP2-MIB", "dcdcIndex"),
)
if mibBuilder.loadTexts:
    dcdcEntry.setStatus("current")


class _DcdcIndex_Type(Integer32):
    """Custom type dcdcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DcdcIndex_Type.__name__ = "Integer32"
_DcdcIndex_Object = MibTableColumn
dcdcIndex = _DcdcIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 1),
    _DcdcIndex_Type()
)
dcdcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcdcIndex.setStatus("current")


class _DcdcStatus_Type(Integer32):
    """Custom type dcdcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_DcdcStatus_Type.__name__ = "Integer32"
_DcdcStatus_Object = MibTableColumn
dcdcStatus = _DcdcStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 2),
    _DcdcStatus_Type()
)
dcdcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcStatus.setStatus("current")
_DcdcOutputCurrentValue_Type = Integer32
_DcdcOutputCurrentValue_Object = MibTableColumn
dcdcOutputCurrentValue = _DcdcOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 3),
    _DcdcOutputCurrentValue_Type()
)
dcdcOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcOutputCurrentValue.setStatus("current")
_DcdcInputVoltageValue_Type = Integer32
_DcdcInputVoltageValue_Object = MibTableColumn
dcdcInputVoltageValue = _DcdcInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 4),
    _DcdcInputVoltageValue_Type()
)
dcdcInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcInputVoltageValue.setStatus("current")


class _DcdcType_Type(DisplayString):
    """Custom type dcdcType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_DcdcType_Type.__name__ = "DisplayString"
_DcdcType_Object = MibTableColumn
dcdcType = _DcdcType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 5),
    _DcdcType_Type()
)
dcdcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcType.setStatus("current")


class _DcdcHwPartNumber_Type(DisplayString):
    """Custom type dcdcHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DcdcHwPartNumber_Type.__name__ = "DisplayString"
_DcdcHwPartNumber_Object = MibTableColumn
dcdcHwPartNumber = _DcdcHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 6),
    _DcdcHwPartNumber_Type()
)
dcdcHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcHwPartNumber.setStatus("current")


class _DcdcHwVersion_Type(DisplayString):
    """Custom type dcdcHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_DcdcHwVersion_Type.__name__ = "DisplayString"
_DcdcHwVersion_Object = MibTableColumn
dcdcHwVersion = _DcdcHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 7),
    _DcdcHwVersion_Type()
)
dcdcHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcHwVersion.setStatus("current")


class _DcdcSwPartNumber_Type(DisplayString):
    """Custom type dcdcSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DcdcSwPartNumber_Type.__name__ = "DisplayString"
_DcdcSwPartNumber_Object = MibTableColumn
dcdcSwPartNumber = _DcdcSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 8),
    _DcdcSwPartNumber_Type()
)
dcdcSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcSwPartNumber.setStatus("current")


class _DcdcSwVersion_Type(DisplayString):
    """Custom type dcdcSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_DcdcSwVersion_Type.__name__ = "DisplayString"
_DcdcSwVersion_Object = MibTableColumn
dcdcSwVersion = _DcdcSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 5, 1, 9),
    _DcdcSwVersion_Type()
)
dcdcSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcSwVersion.setStatus("current")
_DcdcErrorTable_Object = MibTable
dcdcErrorTable = _DcdcErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6)
)
if mibBuilder.loadTexts:
    dcdcErrorTable.setStatus("current")
_DcdcErrorEntry_Object = MibTableRow
dcdcErrorEntry = _DcdcErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1)
)
dcdcErrorEntry.setIndexNames(
    (0, "SP2-MIB", "dcdcGroupIndex"),
)
if mibBuilder.loadTexts:
    dcdcErrorEntry.setStatus("current")


class _DcdcErrorStatus_Type(Integer32):
    """Custom type dcdcErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_DcdcErrorStatus_Type.__name__ = "Integer32"
_DcdcErrorStatus_Object = MibTableColumn
dcdcErrorStatus = _DcdcErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 1),
    _DcdcErrorStatus_Type()
)
dcdcErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcErrorStatus.setStatus("current")


class _DcdcErrorDescription_Type(DisplayString):
    """Custom type dcdcErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DcdcErrorDescription_Type.__name__ = "DisplayString"
_DcdcErrorDescription_Object = MibTableColumn
dcdcErrorDescription = _DcdcErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 2),
    _DcdcErrorDescription_Type()
)
dcdcErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcErrorDescription.setStatus("current")
_DcdcErrorTrapRepeatCounter_Type = Counter32
_DcdcErrorTrapRepeatCounter_Object = MibTableColumn
dcdcErrorTrapRepeatCounter = _DcdcErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 3),
    _DcdcErrorTrapRepeatCounter_Type()
)
dcdcErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dcdcErrorTrapRepeatCounter.setStatus("current")


class _DcdcErrorEnable_Type(Integer32):
    """Custom type dcdcErrorEnable based on Integer32"""
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


_DcdcErrorEnable_Type.__name__ = "Integer32"
_DcdcErrorEnable_Object = MibTableColumn
dcdcErrorEnable = _DcdcErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 4),
    _DcdcErrorEnable_Type()
)
dcdcErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcErrorEnable.setStatus("current")
_DcdcErrorValue_Type = Integer32
_DcdcErrorValue_Object = MibTableColumn
dcdcErrorValue = _DcdcErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 5),
    _DcdcErrorValue_Type()
)
dcdcErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcdcErrorValue.setStatus("current")
_DcdcErrorMajorAlarmLevel_Type = Integer32
_DcdcErrorMajorAlarmLevel_Object = MibTableColumn
dcdcErrorMajorAlarmLevel = _DcdcErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 6),
    _DcdcErrorMajorAlarmLevel_Type()
)
dcdcErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcErrorMajorAlarmLevel.setStatus("current")
_DcdcErrorMinorAlarmLevel_Type = Integer32
_DcdcErrorMinorAlarmLevel_Object = MibTableColumn
dcdcErrorMinorAlarmLevel = _DcdcErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 6, 1, 7),
    _DcdcErrorMinorAlarmLevel_Type()
)
dcdcErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcdcErrorMinorAlarmLevel.setStatus("current")
_DcdcObsolete_ObjectIdentity = ObjectIdentity
dcdcObsolete = _DcdcObsolete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 6, 7)
)
_SolarChargers_ObjectIdentity = ObjectIdentity
solarChargers = _SolarChargers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7)
)


class _SolarChargersStatus_Type(Integer32):
    """Custom type solarChargersStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_SolarChargersStatus_Type.__name__ = "Integer32"
_SolarChargersStatus_Object = MibScalar
solarChargersStatus = _SolarChargersStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 1),
    _SolarChargersStatus_Type()
)
solarChargersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersStatus.setStatus("current")
_SolarChargersCurrent_ObjectIdentity = ObjectIdentity
solarChargersCurrent = _SolarChargersCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2)
)


class _SolarChargersCurrentStatus_Type(Integer32):
    """Custom type solarChargersCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_SolarChargersCurrentStatus_Type.__name__ = "Integer32"
_SolarChargersCurrentStatus_Object = MibScalar
solarChargersCurrentStatus = _SolarChargersCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 1),
    _SolarChargersCurrentStatus_Type()
)
solarChargersCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersCurrentStatus.setStatus("current")


class _SolarChargersCurrentDescription_Type(DisplayString):
    """Custom type solarChargersCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolarChargersCurrentDescription_Type.__name__ = "DisplayString"
_SolarChargersCurrentDescription_Object = MibScalar
solarChargersCurrentDescription = _SolarChargersCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 2),
    _SolarChargersCurrentDescription_Type()
)
solarChargersCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCurrentDescription.setStatus("current")
_SolarChargersCurrentTrapRepeatCounter_Type = Counter32
_SolarChargersCurrentTrapRepeatCounter_Object = MibScalar
solarChargersCurrentTrapRepeatCounter = _SolarChargersCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 3),
    _SolarChargersCurrentTrapRepeatCounter_Type()
)
solarChargersCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    solarChargersCurrentTrapRepeatCounter.setStatus("current")


class _SolarChargersCurrentAlarmEnable_Type(Integer32):
    """Custom type solarChargersCurrentAlarmEnable based on Integer32"""
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


_SolarChargersCurrentAlarmEnable_Type.__name__ = "Integer32"
_SolarChargersCurrentAlarmEnable_Object = MibScalar
solarChargersCurrentAlarmEnable = _SolarChargersCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 4),
    _SolarChargersCurrentAlarmEnable_Type()
)
solarChargersCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCurrentAlarmEnable.setStatus("current")
_SolarChargersCurrentValue_Type = Integer32
_SolarChargersCurrentValue_Object = MibScalar
solarChargersCurrentValue = _SolarChargersCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 5),
    _SolarChargersCurrentValue_Type()
)
solarChargersCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersCurrentValue.setStatus("current")
_SolarChargersCurrentMajorAlarmLevel_Type = Integer32
_SolarChargersCurrentMajorAlarmLevel_Object = MibScalar
solarChargersCurrentMajorAlarmLevel = _SolarChargersCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 6),
    _SolarChargersCurrentMajorAlarmLevel_Type()
)
solarChargersCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCurrentMajorAlarmLevel.setStatus("current")
_SolarChargersCurrentMinorAlarmLevel_Type = Integer32
_SolarChargersCurrentMinorAlarmLevel_Object = MibScalar
solarChargersCurrentMinorAlarmLevel = _SolarChargersCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 2, 7),
    _SolarChargersCurrentMinorAlarmLevel_Type()
)
solarChargersCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersCurrentMinorAlarmLevel.setStatus("current")
_SolarChargersObsolete_ObjectIdentity = ObjectIdentity
solarChargersObsolete = _SolarChargersObsolete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 3)
)
_SolarChargersError_ObjectIdentity = ObjectIdentity
solarChargersError = _SolarChargersError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4)
)


class _SolarChargersErrorStatus_Type(Integer32):
    """Custom type solarChargersErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_SolarChargersErrorStatus_Type.__name__ = "Integer32"
_SolarChargersErrorStatus_Object = MibScalar
solarChargersErrorStatus = _SolarChargersErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 1),
    _SolarChargersErrorStatus_Type()
)
solarChargersErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersErrorStatus.setStatus("current")


class _SolarChargersErrorDescription_Type(DisplayString):
    """Custom type solarChargersErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SolarChargersErrorDescription_Type.__name__ = "DisplayString"
_SolarChargersErrorDescription_Object = MibScalar
solarChargersErrorDescription = _SolarChargersErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 2),
    _SolarChargersErrorDescription_Type()
)
solarChargersErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersErrorDescription.setStatus("current")
_SolarChargersErrorTrapRepeatCounter_Type = Counter32
_SolarChargersErrorTrapRepeatCounter_Object = MibScalar
solarChargersErrorTrapRepeatCounter = _SolarChargersErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 3),
    _SolarChargersErrorTrapRepeatCounter_Type()
)
solarChargersErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    solarChargersErrorTrapRepeatCounter.setStatus("current")


class _SolarChargersErrorEnable_Type(Integer32):
    """Custom type solarChargersErrorEnable based on Integer32"""
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


_SolarChargersErrorEnable_Type.__name__ = "Integer32"
_SolarChargersErrorEnable_Object = MibScalar
solarChargersErrorEnable = _SolarChargersErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 4),
    _SolarChargersErrorEnable_Type()
)
solarChargersErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersErrorEnable.setStatus("current")
_SolarChargersErrorValue_Type = Integer32
_SolarChargersErrorValue_Object = MibScalar
solarChargersErrorValue = _SolarChargersErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 5),
    _SolarChargersErrorValue_Type()
)
solarChargersErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersErrorValue.setStatus("current")
_SolarChargersErrorMajorAlarmLevel_Type = Integer32
_SolarChargersErrorMajorAlarmLevel_Object = MibScalar
solarChargersErrorMajorAlarmLevel = _SolarChargersErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 6),
    _SolarChargersErrorMajorAlarmLevel_Type()
)
solarChargersErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersErrorMajorAlarmLevel.setStatus("current")
_SolarChargersErrorMinorAlarmLevel_Type = Integer32
_SolarChargersErrorMinorAlarmLevel_Object = MibScalar
solarChargersErrorMinorAlarmLevel = _SolarChargersErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 4, 7),
    _SolarChargersErrorMinorAlarmLevel_Type()
)
solarChargersErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersErrorMinorAlarmLevel.setStatus("current")


class _SolarChargersNumberOfSolarChargers_Type(Integer32):
    """Custom type solarChargersNumberOfSolarChargers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SolarChargersNumberOfSolarChargers_Type.__name__ = "Integer32"
_SolarChargersNumberOfSolarChargers_Object = MibScalar
solarChargersNumberOfSolarChargers = _SolarChargersNumberOfSolarChargers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 5),
    _SolarChargersNumberOfSolarChargers_Type()
)
solarChargersNumberOfSolarChargers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    solarChargersNumberOfSolarChargers.setStatus("current")
_SolarChargerTable_Object = MibTable
solarChargerTable = _SolarChargerTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6)
)
if mibBuilder.loadTexts:
    solarChargerTable.setStatus("current")
_SolarChargerEntry_Object = MibTableRow
solarChargerEntry = _SolarChargerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1)
)
solarChargerEntry.setIndexNames(
    (0, "SP2-MIB", "solarChargerIndex"),
)
if mibBuilder.loadTexts:
    solarChargerEntry.setStatus("current")


class _SolarChargerIndex_Type(Integer32):
    """Custom type solarChargerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SolarChargerIndex_Type.__name__ = "Integer32"
_SolarChargerIndex_Object = MibTableColumn
solarChargerIndex = _SolarChargerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 1),
    _SolarChargerIndex_Type()
)
solarChargerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    solarChargerIndex.setStatus("current")


class _SolarChargerStatus_Type(Integer32):
    """Custom type solarChargerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_SolarChargerStatus_Type.__name__ = "Integer32"
_SolarChargerStatus_Object = MibTableColumn
solarChargerStatus = _SolarChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 2),
    _SolarChargerStatus_Type()
)
solarChargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerStatus.setStatus("current")
_SolarChargerOutputCurrentValue_Type = Integer32
_SolarChargerOutputCurrentValue_Object = MibTableColumn
solarChargerOutputCurrentValue = _SolarChargerOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 3),
    _SolarChargerOutputCurrentValue_Type()
)
solarChargerOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerOutputCurrentValue.setStatus("current")
_SolarChargerInputVoltageValue_Type = Integer32
_SolarChargerInputVoltageValue_Object = MibTableColumn
solarChargerInputVoltageValue = _SolarChargerInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 4),
    _SolarChargerInputVoltageValue_Type()
)
solarChargerInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerInputVoltageValue.setStatus("current")


class _SolarChargerType_Type(DisplayString):
    """Custom type solarChargerType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_SolarChargerType_Type.__name__ = "DisplayString"
_SolarChargerType_Object = MibTableColumn
solarChargerType = _SolarChargerType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 5),
    _SolarChargerType_Type()
)
solarChargerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerType.setStatus("current")


class _SolarChargerHwPartNumber_Type(DisplayString):
    """Custom type solarChargerHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SolarChargerHwPartNumber_Type.__name__ = "DisplayString"
_SolarChargerHwPartNumber_Object = MibTableColumn
solarChargerHwPartNumber = _SolarChargerHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 6),
    _SolarChargerHwPartNumber_Type()
)
solarChargerHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerHwPartNumber.setStatus("current")


class _SolarChargerHwVersion_Type(DisplayString):
    """Custom type solarChargerHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SolarChargerHwVersion_Type.__name__ = "DisplayString"
_SolarChargerHwVersion_Object = MibTableColumn
solarChargerHwVersion = _SolarChargerHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 7),
    _SolarChargerHwVersion_Type()
)
solarChargerHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerHwVersion.setStatus("current")


class _SolarChargerSwPartNumber_Type(DisplayString):
    """Custom type solarChargerSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SolarChargerSwPartNumber_Type.__name__ = "DisplayString"
_SolarChargerSwPartNumber_Object = MibTableColumn
solarChargerSwPartNumber = _SolarChargerSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 8),
    _SolarChargerSwPartNumber_Type()
)
solarChargerSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerSwPartNumber.setStatus("current")


class _SolarChargerSwVersion_Type(DisplayString):
    """Custom type solarChargerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SolarChargerSwVersion_Type.__name__ = "DisplayString"
_SolarChargerSwVersion_Object = MibTableColumn
solarChargerSwVersion = _SolarChargerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 6, 1, 9),
    _SolarChargerSwVersion_Type()
)
solarChargerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargerSwVersion.setStatus("current")
_SolarChargersEnergyLog_ObjectIdentity = ObjectIdentity
solarChargersEnergyLog = _SolarChargersEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7)
)
_SolarChargersEnergyLogAccumulated_Type = Integer32
_SolarChargersEnergyLogAccumulated_Object = MibScalar
solarChargersEnergyLogAccumulated = _SolarChargersEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 1),
    _SolarChargersEnergyLogAccumulated_Type()
)
solarChargersEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogAccumulated.setStatus("current")
_SolarChargersEnergyLogLastHoursNumberOfEntries_Type = Integer32
_SolarChargersEnergyLogLastHoursNumberOfEntries_Object = MibScalar
solarChargersEnergyLogLastHoursNumberOfEntries = _SolarChargersEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 2),
    _SolarChargersEnergyLogLastHoursNumberOfEntries_Type()
)
solarChargersEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursNumberOfEntries.setStatus("current")
_SolarChargersEnergyLogLastHoursTable_Object = MibTable
solarChargersEnergyLogLastHoursTable = _SolarChargersEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 3)
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursTable.setStatus("current")
_SolarChargersEnergyLogLastHoursEntry_Object = MibTableRow
solarChargersEnergyLogLastHoursEntry = _SolarChargersEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 3, 1)
)
solarChargersEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "solarChargersEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursEntry.setStatus("current")


class _SolarChargersEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type solarChargersEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_SolarChargersEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_SolarChargersEnergyLogLastHoursIndex_Object = MibTableColumn
solarChargersEnergyLogLastHoursIndex = _SolarChargersEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 3, 1, 1),
    _SolarChargersEnergyLogLastHoursIndex_Type()
)
solarChargersEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursIndex.setStatus("current")
_SolarChargersEnergyLogLastHoursValue_Type = Integer32
_SolarChargersEnergyLogLastHoursValue_Object = MibTableColumn
solarChargersEnergyLogLastHoursValue = _SolarChargersEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 3, 1, 2),
    _SolarChargersEnergyLogLastHoursValue_Type()
)
solarChargersEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastHoursValue.setStatus("current")
_SolarChargersEnergyLogLastDaysNumberOfEntries_Type = Integer32
_SolarChargersEnergyLogLastDaysNumberOfEntries_Object = MibScalar
solarChargersEnergyLogLastDaysNumberOfEntries = _SolarChargersEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 4),
    _SolarChargersEnergyLogLastDaysNumberOfEntries_Type()
)
solarChargersEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysNumberOfEntries.setStatus("current")
_SolarChargersEnergyLogLastDaysTable_Object = MibTable
solarChargersEnergyLogLastDaysTable = _SolarChargersEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 5)
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysTable.setStatus("current")
_SolarChargersEnergyLogLastDaysEntry_Object = MibTableRow
solarChargersEnergyLogLastDaysEntry = _SolarChargersEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 5, 1)
)
solarChargersEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "solarChargersEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysEntry.setStatus("current")


class _SolarChargersEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type solarChargersEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_SolarChargersEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_SolarChargersEnergyLogLastDaysIndex_Object = MibTableColumn
solarChargersEnergyLogLastDaysIndex = _SolarChargersEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 5, 1, 1),
    _SolarChargersEnergyLogLastDaysIndex_Type()
)
solarChargersEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysIndex.setStatus("current")
_SolarChargersEnergyLogLastDaysValue_Type = Integer32
_SolarChargersEnergyLogLastDaysValue_Object = MibTableColumn
solarChargersEnergyLogLastDaysValue = _SolarChargersEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 5, 1, 2),
    _SolarChargersEnergyLogLastDaysValue_Type()
)
solarChargersEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastDaysValue.setStatus("current")
_SolarChargersEnergyLogLastWeeksNumberOfEntries_Type = Integer32
_SolarChargersEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
solarChargersEnergyLogLastWeeksNumberOfEntries = _SolarChargersEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 6),
    _SolarChargersEnergyLogLastWeeksNumberOfEntries_Type()
)
solarChargersEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_SolarChargersEnergyLogLastWeeksTable_Object = MibTable
solarChargersEnergyLogLastWeeksTable = _SolarChargersEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 7)
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksTable.setStatus("current")
_SolarChargersEnergyLogLastWeeksEntry_Object = MibTableRow
solarChargersEnergyLogLastWeeksEntry = _SolarChargersEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 7, 1)
)
solarChargersEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "solarChargersEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksEntry.setStatus("current")


class _SolarChargersEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type solarChargersEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_SolarChargersEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_SolarChargersEnergyLogLastWeeksIndex_Object = MibTableColumn
solarChargersEnergyLogLastWeeksIndex = _SolarChargersEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 7, 1, 1),
    _SolarChargersEnergyLogLastWeeksIndex_Type()
)
solarChargersEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksIndex.setStatus("current")
_SolarChargersEnergyLogLastWeeksValue_Type = Integer32
_SolarChargersEnergyLogLastWeeksValue_Object = MibTableColumn
solarChargersEnergyLogLastWeeksValue = _SolarChargersEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 7, 7, 7, 1, 2),
    _SolarChargersEnergyLogLastWeeksValue_Type()
)
solarChargersEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    solarChargersEnergyLogLastWeeksValue.setStatus("current")
_WindChargers_ObjectIdentity = ObjectIdentity
windChargers = _WindChargers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8)
)


class _WindChargersStatus_Type(Integer32):
    """Custom type windChargersStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_WindChargersStatus_Type.__name__ = "Integer32"
_WindChargersStatus_Object = MibScalar
windChargersStatus = _WindChargersStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 1),
    _WindChargersStatus_Type()
)
windChargersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersStatus.setStatus("current")
_WindChargersCurrent_ObjectIdentity = ObjectIdentity
windChargersCurrent = _WindChargersCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2)
)


class _WindChargersCurrentStatus_Type(Integer32):
    """Custom type windChargersCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_WindChargersCurrentStatus_Type.__name__ = "Integer32"
_WindChargersCurrentStatus_Object = MibScalar
windChargersCurrentStatus = _WindChargersCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 1),
    _WindChargersCurrentStatus_Type()
)
windChargersCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersCurrentStatus.setStatus("current")


class _WindChargersCurrentDescription_Type(DisplayString):
    """Custom type windChargersCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WindChargersCurrentDescription_Type.__name__ = "DisplayString"
_WindChargersCurrentDescription_Object = MibScalar
windChargersCurrentDescription = _WindChargersCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 2),
    _WindChargersCurrentDescription_Type()
)
windChargersCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCurrentDescription.setStatus("current")
_WindChargersCurrentTrapRepeatCounter_Type = Counter32
_WindChargersCurrentTrapRepeatCounter_Object = MibScalar
windChargersCurrentTrapRepeatCounter = _WindChargersCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 3),
    _WindChargersCurrentTrapRepeatCounter_Type()
)
windChargersCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    windChargersCurrentTrapRepeatCounter.setStatus("current")


class _WindChargersCurrentAlarmEnable_Type(Integer32):
    """Custom type windChargersCurrentAlarmEnable based on Integer32"""
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


_WindChargersCurrentAlarmEnable_Type.__name__ = "Integer32"
_WindChargersCurrentAlarmEnable_Object = MibScalar
windChargersCurrentAlarmEnable = _WindChargersCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 4),
    _WindChargersCurrentAlarmEnable_Type()
)
windChargersCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCurrentAlarmEnable.setStatus("current")
_WindChargersCurrentValue_Type = Integer32
_WindChargersCurrentValue_Object = MibScalar
windChargersCurrentValue = _WindChargersCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 5),
    _WindChargersCurrentValue_Type()
)
windChargersCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersCurrentValue.setStatus("current")
_WindChargersCurrentMajorAlarmLevel_Type = Integer32
_WindChargersCurrentMajorAlarmLevel_Object = MibScalar
windChargersCurrentMajorAlarmLevel = _WindChargersCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 6),
    _WindChargersCurrentMajorAlarmLevel_Type()
)
windChargersCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCurrentMajorAlarmLevel.setStatus("current")
_WindChargersCurrentMinorAlarmLevel_Type = Integer32
_WindChargersCurrentMinorAlarmLevel_Object = MibScalar
windChargersCurrentMinorAlarmLevel = _WindChargersCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 2, 7),
    _WindChargersCurrentMinorAlarmLevel_Type()
)
windChargersCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersCurrentMinorAlarmLevel.setStatus("current")
_WindChargersObsolete_ObjectIdentity = ObjectIdentity
windChargersObsolete = _WindChargersObsolete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 3)
)
_WindChargersError_ObjectIdentity = ObjectIdentity
windChargersError = _WindChargersError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4)
)


class _WindChargersErrorStatus_Type(Integer32):
    """Custom type windChargersErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_WindChargersErrorStatus_Type.__name__ = "Integer32"
_WindChargersErrorStatus_Object = MibScalar
windChargersErrorStatus = _WindChargersErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 1),
    _WindChargersErrorStatus_Type()
)
windChargersErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersErrorStatus.setStatus("current")


class _WindChargersErrorDescription_Type(DisplayString):
    """Custom type windChargersErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WindChargersErrorDescription_Type.__name__ = "DisplayString"
_WindChargersErrorDescription_Object = MibScalar
windChargersErrorDescription = _WindChargersErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 2),
    _WindChargersErrorDescription_Type()
)
windChargersErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersErrorDescription.setStatus("current")
_WindChargersErrorTrapRepeatCounter_Type = Counter32
_WindChargersErrorTrapRepeatCounter_Object = MibScalar
windChargersErrorTrapRepeatCounter = _WindChargersErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 3),
    _WindChargersErrorTrapRepeatCounter_Type()
)
windChargersErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    windChargersErrorTrapRepeatCounter.setStatus("current")


class _WindChargersErrorEnable_Type(Integer32):
    """Custom type windChargersErrorEnable based on Integer32"""
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


_WindChargersErrorEnable_Type.__name__ = "Integer32"
_WindChargersErrorEnable_Object = MibScalar
windChargersErrorEnable = _WindChargersErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 4),
    _WindChargersErrorEnable_Type()
)
windChargersErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersErrorEnable.setStatus("current")
_WindChargersErrorValue_Type = Integer32
_WindChargersErrorValue_Object = MibScalar
windChargersErrorValue = _WindChargersErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 5),
    _WindChargersErrorValue_Type()
)
windChargersErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersErrorValue.setStatus("current")
_WindChargersErrorMajorAlarmLevel_Type = Integer32
_WindChargersErrorMajorAlarmLevel_Object = MibScalar
windChargersErrorMajorAlarmLevel = _WindChargersErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 6),
    _WindChargersErrorMajorAlarmLevel_Type()
)
windChargersErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersErrorMajorAlarmLevel.setStatus("current")
_WindChargersErrorMinorAlarmLevel_Type = Integer32
_WindChargersErrorMinorAlarmLevel_Object = MibScalar
windChargersErrorMinorAlarmLevel = _WindChargersErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 4, 7),
    _WindChargersErrorMinorAlarmLevel_Type()
)
windChargersErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersErrorMinorAlarmLevel.setStatus("current")


class _WindChargersNumberOfWindChargers_Type(Integer32):
    """Custom type windChargersNumberOfWindChargers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_WindChargersNumberOfWindChargers_Type.__name__ = "Integer32"
_WindChargersNumberOfWindChargers_Object = MibScalar
windChargersNumberOfWindChargers = _WindChargersNumberOfWindChargers_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 5),
    _WindChargersNumberOfWindChargers_Type()
)
windChargersNumberOfWindChargers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    windChargersNumberOfWindChargers.setStatus("current")
_WindChargerTable_Object = MibTable
windChargerTable = _WindChargerTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6)
)
if mibBuilder.loadTexts:
    windChargerTable.setStatus("current")
_WindChargerEntry_Object = MibTableRow
windChargerEntry = _WindChargerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1)
)
windChargerEntry.setIndexNames(
    (0, "SP2-MIB", "windChargerIndex"),
)
if mibBuilder.loadTexts:
    windChargerEntry.setStatus("current")


class _WindChargerIndex_Type(Integer32):
    """Custom type windChargerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WindChargerIndex_Type.__name__ = "Integer32"
_WindChargerIndex_Object = MibTableColumn
windChargerIndex = _WindChargerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 1),
    _WindChargerIndex_Type()
)
windChargerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    windChargerIndex.setStatus("current")


class _WindChargerStatus_Type(Integer32):
    """Custom type windChargerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_WindChargerStatus_Type.__name__ = "Integer32"
_WindChargerStatus_Object = MibTableColumn
windChargerStatus = _WindChargerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 2),
    _WindChargerStatus_Type()
)
windChargerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerStatus.setStatus("current")
_WindChargerOutputCurrentValue_Type = Integer32
_WindChargerOutputCurrentValue_Object = MibTableColumn
windChargerOutputCurrentValue = _WindChargerOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 3),
    _WindChargerOutputCurrentValue_Type()
)
windChargerOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerOutputCurrentValue.setStatus("current")
_WindChargerInputVoltageValue_Type = Integer32
_WindChargerInputVoltageValue_Object = MibTableColumn
windChargerInputVoltageValue = _WindChargerInputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 4),
    _WindChargerInputVoltageValue_Type()
)
windChargerInputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerInputVoltageValue.setStatus("current")


class _WindChargerType_Type(DisplayString):
    """Custom type windChargerType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_WindChargerType_Type.__name__ = "DisplayString"
_WindChargerType_Object = MibTableColumn
windChargerType = _WindChargerType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 5),
    _WindChargerType_Type()
)
windChargerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerType.setStatus("current")


class _WindChargerHwPartNumber_Type(DisplayString):
    """Custom type windChargerHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WindChargerHwPartNumber_Type.__name__ = "DisplayString"
_WindChargerHwPartNumber_Object = MibTableColumn
windChargerHwPartNumber = _WindChargerHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 6),
    _WindChargerHwPartNumber_Type()
)
windChargerHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerHwPartNumber.setStatus("current")


class _WindChargerHwVersion_Type(DisplayString):
    """Custom type windChargerHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_WindChargerHwVersion_Type.__name__ = "DisplayString"
_WindChargerHwVersion_Object = MibTableColumn
windChargerHwVersion = _WindChargerHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 7),
    _WindChargerHwVersion_Type()
)
windChargerHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerHwVersion.setStatus("current")


class _WindChargerSwPartNumber_Type(DisplayString):
    """Custom type windChargerSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_WindChargerSwPartNumber_Type.__name__ = "DisplayString"
_WindChargerSwPartNumber_Object = MibTableColumn
windChargerSwPartNumber = _WindChargerSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 8),
    _WindChargerSwPartNumber_Type()
)
windChargerSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerSwPartNumber.setStatus("current")


class _WindChargerSwVersion_Type(DisplayString):
    """Custom type windChargerSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_WindChargerSwVersion_Type.__name__ = "DisplayString"
_WindChargerSwVersion_Object = MibTableColumn
windChargerSwVersion = _WindChargerSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 6, 1, 9),
    _WindChargerSwVersion_Type()
)
windChargerSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargerSwVersion.setStatus("current")
_WindChargersEnergyLog_ObjectIdentity = ObjectIdentity
windChargersEnergyLog = _WindChargersEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7)
)
_WindChargersEnergyLogAccumulated_Type = Integer32
_WindChargersEnergyLogAccumulated_Object = MibScalar
windChargersEnergyLogAccumulated = _WindChargersEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 1),
    _WindChargersEnergyLogAccumulated_Type()
)
windChargersEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogAccumulated.setStatus("current")


class _WindChargersEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type windChargersEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_WindChargersEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastHoursNumberOfEntries_Object = MibScalar
windChargersEnergyLogLastHoursNumberOfEntries = _WindChargersEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 2),
    _WindChargersEnergyLogLastHoursNumberOfEntries_Type()
)
windChargersEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursNumberOfEntries.setStatus("current")
_WindChargersEnergyLogLastHoursTable_Object = MibTable
windChargersEnergyLogLastHoursTable = _WindChargersEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 3)
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursTable.setStatus("current")
_WindChargersEnergyLogLastHoursEntry_Object = MibTableRow
windChargersEnergyLogLastHoursEntry = _WindChargersEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 3, 1)
)
windChargersEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "windChargersEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursEntry.setStatus("current")


class _WindChargersEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type windChargersEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_WindChargersEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastHoursIndex_Object = MibTableColumn
windChargersEnergyLogLastHoursIndex = _WindChargersEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 3, 1, 1),
    _WindChargersEnergyLogLastHoursIndex_Type()
)
windChargersEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursIndex.setStatus("current")
_WindChargersEnergyLogLastHoursValue_Type = Integer32
_WindChargersEnergyLogLastHoursValue_Object = MibTableColumn
windChargersEnergyLogLastHoursValue = _WindChargersEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 3, 1, 2),
    _WindChargersEnergyLogLastHoursValue_Type()
)
windChargersEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastHoursValue.setStatus("current")


class _WindChargersEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type windChargersEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_WindChargersEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastDaysNumberOfEntries_Object = MibScalar
windChargersEnergyLogLastDaysNumberOfEntries = _WindChargersEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 4),
    _WindChargersEnergyLogLastDaysNumberOfEntries_Type()
)
windChargersEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysNumberOfEntries.setStatus("current")
_WindChargersEnergyLogLastDaysTable_Object = MibTable
windChargersEnergyLogLastDaysTable = _WindChargersEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 5)
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysTable.setStatus("current")
_WindChargersEnergyLogLastDaysEntry_Object = MibTableRow
windChargersEnergyLogLastDaysEntry = _WindChargersEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 5, 1)
)
windChargersEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "windChargersEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysEntry.setStatus("current")


class _WindChargersEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type windChargersEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_WindChargersEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastDaysIndex_Object = MibTableColumn
windChargersEnergyLogLastDaysIndex = _WindChargersEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 5, 1, 1),
    _WindChargersEnergyLogLastDaysIndex_Type()
)
windChargersEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysIndex.setStatus("current")
_WindChargersEnergyLogLastDaysValue_Type = Integer32
_WindChargersEnergyLogLastDaysValue_Object = MibTableColumn
windChargersEnergyLogLastDaysValue = _WindChargersEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 5, 1, 2),
    _WindChargersEnergyLogLastDaysValue_Type()
)
windChargersEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastDaysValue.setStatus("current")


class _WindChargersEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type windChargersEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_WindChargersEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
windChargersEnergyLogLastWeeksNumberOfEntries = _WindChargersEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 6),
    _WindChargersEnergyLogLastWeeksNumberOfEntries_Type()
)
windChargersEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_WindChargersEnergyLogLastWeeksTable_Object = MibTable
windChargersEnergyLogLastWeeksTable = _WindChargersEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 7)
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksTable.setStatus("current")
_WindChargersEnergyLogLastWeeksEntry_Object = MibTableRow
windChargersEnergyLogLastWeeksEntry = _WindChargersEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 7, 1)
)
windChargersEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "windChargersEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksEntry.setStatus("current")


class _WindChargersEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type windChargersEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_WindChargersEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_WindChargersEnergyLogLastWeeksIndex_Object = MibTableColumn
windChargersEnergyLogLastWeeksIndex = _WindChargersEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 7, 1, 1),
    _WindChargersEnergyLogLastWeeksIndex_Type()
)
windChargersEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksIndex.setStatus("current")
_WindChargersEnergyLogLastWeeksValue_Type = Integer32
_WindChargersEnergyLogLastWeeksValue_Object = MibTableColumn
windChargersEnergyLogLastWeeksValue = _WindChargersEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 8, 7, 7, 1, 2),
    _WindChargersEnergyLogLastWeeksValue_Type()
)
windChargersEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    windChargersEnergyLogLastWeeksValue.setStatus("current")
_Load_ObjectIdentity = ObjectIdentity
load = _Load_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9)
)


class _LoadStatus_Type(Integer32):
    """Custom type loadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_LoadStatus_Type.__name__ = "Integer32"
_LoadStatus_Object = MibScalar
loadStatus = _LoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 1),
    _LoadStatus_Type()
)
loadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadStatus.setStatus("current")
_LoadCurrent_ObjectIdentity = ObjectIdentity
loadCurrent = _LoadCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2)
)


class _LoadCurrentStatus_Type(Integer32):
    """Custom type loadCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_LoadCurrentStatus_Type.__name__ = "Integer32"
_LoadCurrentStatus_Object = MibScalar
loadCurrentStatus = _LoadCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 1),
    _LoadCurrentStatus_Type()
)
loadCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCurrentStatus.setStatus("current")


class _LoadCurrentDescription_Type(DisplayString):
    """Custom type loadCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadCurrentDescription_Type.__name__ = "DisplayString"
_LoadCurrentDescription_Object = MibScalar
loadCurrentDescription = _LoadCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 2),
    _LoadCurrentDescription_Type()
)
loadCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadCurrentDescription.setStatus("current")
_LoadCurrentTrapRepeatCounter_Type = Counter32
_LoadCurrentTrapRepeatCounter_Object = MibScalar
loadCurrentTrapRepeatCounter = _LoadCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 3),
    _LoadCurrentTrapRepeatCounter_Type()
)
loadCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadCurrentTrapRepeatCounter.setStatus("current")


class _LoadCurrentAlarmEnable_Type(Integer32):
    """Custom type loadCurrentAlarmEnable based on Integer32"""
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


_LoadCurrentAlarmEnable_Type.__name__ = "Integer32"
_LoadCurrentAlarmEnable_Object = MibScalar
loadCurrentAlarmEnable = _LoadCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 4),
    _LoadCurrentAlarmEnable_Type()
)
loadCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadCurrentAlarmEnable.setStatus("current")
_LoadCurrentValue_Type = Integer32
_LoadCurrentValue_Object = MibScalar
loadCurrentValue = _LoadCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 5),
    _LoadCurrentValue_Type()
)
loadCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCurrentValue.setStatus("current")
_LoadCurrentMajorHighLevel_Type = Integer32
_LoadCurrentMajorHighLevel_Object = MibScalar
loadCurrentMajorHighLevel = _LoadCurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 6),
    _LoadCurrentMajorHighLevel_Type()
)
loadCurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadCurrentMajorHighLevel.setStatus("current")
_LoadCurrentMinorHighLevel_Type = Integer32
_LoadCurrentMinorHighLevel_Object = MibScalar
loadCurrentMinorHighLevel = _LoadCurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 2, 7),
    _LoadCurrentMinorHighLevel_Type()
)
loadCurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadCurrentMinorHighLevel.setStatus("current")


class _LoadFusesStatus_Type(Integer32):
    """Custom type loadFusesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_LoadFusesStatus_Type.__name__ = "Integer32"
_LoadFusesStatus_Object = MibScalar
loadFusesStatus = _LoadFusesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 3),
    _LoadFusesStatus_Type()
)
loadFusesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFusesStatus.setStatus("current")


class _LoadNumberOfGroups_Type(Integer32):
    """Custom type loadNumberOfGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LoadNumberOfGroups_Type.__name__ = "Integer32"
_LoadNumberOfGroups_Object = MibScalar
loadNumberOfGroups = _LoadNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 4),
    _LoadNumberOfGroups_Type()
)
loadNumberOfGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadNumberOfGroups.setStatus("current")
_LoadGroupTable_Object = MibTable
loadGroupTable = _LoadGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5)
)
if mibBuilder.loadTexts:
    loadGroupTable.setStatus("current")
_LoadGroupEntry_Object = MibTableRow
loadGroupEntry = _LoadGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1)
)
loadGroupEntry.setIndexNames(
    (0, "SP2-MIB", "loadGroupIndex"),
)
if mibBuilder.loadTexts:
    loadGroupEntry.setStatus("current")


class _LoadGroupIndex_Type(Integer32):
    """Custom type loadGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LoadGroupIndex_Type.__name__ = "Integer32"
_LoadGroupIndex_Object = MibTableColumn
loadGroupIndex = _LoadGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1, 1),
    _LoadGroupIndex_Type()
)
loadGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadGroupIndex.setStatus("current")


class _LoadGroupStatus_Type(Integer32):
    """Custom type loadGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_LoadGroupStatus_Type.__name__ = "Integer32"
_LoadGroupStatus_Object = MibTableColumn
loadGroupStatus = _LoadGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1, 2),
    _LoadGroupStatus_Type()
)
loadGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadGroupStatus.setStatus("current")


class _LoadNumberOfLVLDs_Type(Integer32):
    """Custom type loadNumberOfLVLDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_LoadNumberOfLVLDs_Type.__name__ = "Integer32"
_LoadNumberOfLVLDs_Object = MibTableColumn
loadNumberOfLVLDs = _LoadNumberOfLVLDs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1, 3),
    _LoadNumberOfLVLDs_Type()
)
loadNumberOfLVLDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadNumberOfLVLDs.setStatus("current")


class _LoadNumberOfVoltages_Type(Integer32):
    """Custom type loadNumberOfVoltages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_LoadNumberOfVoltages_Type.__name__ = "Integer32"
_LoadNumberOfVoltages_Object = MibTableColumn
loadNumberOfVoltages = _LoadNumberOfVoltages_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 5, 1, 4),
    _LoadNumberOfVoltages_Type()
)
loadNumberOfVoltages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadNumberOfVoltages.setStatus("current")
_LoadLVLDTable_Object = MibTable
loadLVLDTable = _LoadLVLDTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6)
)
if mibBuilder.loadTexts:
    loadLVLDTable.setStatus("current")
_LoadLVLDEntry_Object = MibTableRow
loadLVLDEntry = _LoadLVLDEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1)
)
loadLVLDEntry.setIndexNames(
    (0, "SP2-MIB", "loadGroupIndex"),
    (0, "SP2-MIB", "loadLVLDIndex"),
)
if mibBuilder.loadTexts:
    loadLVLDEntry.setStatus("current")


class _LoadLVLDIndex_Type(Integer32):
    """Custom type loadLVLDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_LoadLVLDIndex_Type.__name__ = "Integer32"
_LoadLVLDIndex_Object = MibTableColumn
loadLVLDIndex = _LoadLVLDIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 1),
    _LoadLVLDIndex_Type()
)
loadLVLDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadLVLDIndex.setStatus("current")


class _LoadLVLDStatus_Type(Integer32):
    """Custom type loadLVLDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_LoadLVLDStatus_Type.__name__ = "Integer32"
_LoadLVLDStatus_Object = MibTableColumn
loadLVLDStatus = _LoadLVLDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 2),
    _LoadLVLDStatus_Type()
)
loadLVLDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVLDStatus.setStatus("current")


class _LoadLVLDDescription_Type(DisplayString):
    """Custom type loadLVLDDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadLVLDDescription_Type.__name__ = "DisplayString"
_LoadLVLDDescription_Object = MibTableColumn
loadLVLDDescription = _LoadLVLDDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 3),
    _LoadLVLDDescription_Type()
)
loadLVLDDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVLDDescription.setStatus("current")
_LoadLVLDTrapRepeatCounter_Type = Counter32
_LoadLVLDTrapRepeatCounter_Object = MibTableColumn
loadLVLDTrapRepeatCounter = _LoadLVLDTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 4),
    _LoadLVLDTrapRepeatCounter_Type()
)
loadLVLDTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadLVLDTrapRepeatCounter.setStatus("current")


class _LoadLVLDEnable_Type(Integer32):
    """Custom type loadLVLDEnable based on Integer32"""
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


_LoadLVLDEnable_Type.__name__ = "Integer32"
_LoadLVLDEnable_Object = MibTableColumn
loadLVLDEnable = _LoadLVLDEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 5),
    _LoadLVLDEnable_Type()
)
loadLVLDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVLDEnable.setStatus("current")
_LoadLVLDValue_Type = Integer32
_LoadLVLDValue_Object = MibTableColumn
loadLVLDValue = _LoadLVLDValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 6),
    _LoadLVLDValue_Type()
)
loadLVLDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadLVLDValue.setStatus("current")
_LoadLVLDConnectVoltage_Type = Integer32
_LoadLVLDConnectVoltage_Object = MibTableColumn
loadLVLDConnectVoltage = _LoadLVLDConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 7),
    _LoadLVLDConnectVoltage_Type()
)
loadLVLDConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVLDConnectVoltage.setStatus("current")
_LoadLVLDDisconnectVoltage_Type = Integer32
_LoadLVLDDisconnectVoltage_Object = MibTableColumn
loadLVLDDisconnectVoltage = _LoadLVLDDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 6, 1, 8),
    _LoadLVLDDisconnectVoltage_Type()
)
loadLVLDDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadLVLDDisconnectVoltage.setStatus("current")
_LoadFuseTable_Object = MibTable
loadFuseTable = _LoadFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7)
)
if mibBuilder.loadTexts:
    loadFuseTable.setStatus("current")
_LoadFuseEntry_Object = MibTableRow
loadFuseEntry = _LoadFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1)
)
loadFuseEntry.setIndexNames(
    (0, "SP2-MIB", "loadGroupIndex"),
)
if mibBuilder.loadTexts:
    loadFuseEntry.setStatus("current")


class _LoadFuseStatus_Type(Integer32):
    """Custom type loadFuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11))
    )


_LoadFuseStatus_Type.__name__ = "Integer32"
_LoadFuseStatus_Object = MibTableColumn
loadFuseStatus = _LoadFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 1),
    _LoadFuseStatus_Type()
)
loadFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFuseStatus.setStatus("current")


class _LoadFuseDescription_Type(DisplayString):
    """Custom type loadFuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadFuseDescription_Type.__name__ = "DisplayString"
_LoadFuseDescription_Object = MibTableColumn
loadFuseDescription = _LoadFuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 2),
    _LoadFuseDescription_Type()
)
loadFuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFuseDescription.setStatus("current")
_LoadFuseTrapRepeatCounter_Type = Counter32
_LoadFuseTrapRepeatCounter_Object = MibTableColumn
loadFuseTrapRepeatCounter = _LoadFuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 3),
    _LoadFuseTrapRepeatCounter_Type()
)
loadFuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadFuseTrapRepeatCounter.setStatus("current")


class _LoadFuseAlarmEnable_Type(Integer32):
    """Custom type loadFuseAlarmEnable based on Integer32"""
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


_LoadFuseAlarmEnable_Type.__name__ = "Integer32"
_LoadFuseAlarmEnable_Object = MibTableColumn
loadFuseAlarmEnable = _LoadFuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 4),
    _LoadFuseAlarmEnable_Type()
)
loadFuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFuseAlarmEnable.setStatus("current")
_LoadFuseValue_Type = Integer32
_LoadFuseValue_Object = MibTableColumn
loadFuseValue = _LoadFuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 7, 1, 5),
    _LoadFuseValue_Type()
)
loadFuseValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadFuseValue.setStatus("current")
_LoadEnergyLog_ObjectIdentity = ObjectIdentity
loadEnergyLog = _LoadEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8)
)
_LoadEnergyLogAccumulated_Type = Integer32
_LoadEnergyLogAccumulated_Object = MibScalar
loadEnergyLogAccumulated = _LoadEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 1),
    _LoadEnergyLogAccumulated_Type()
)
loadEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogAccumulated.setStatus("current")


class _LoadEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type loadEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_LoadEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_LoadEnergyLogLastHoursNumberOfEntries_Object = MibScalar
loadEnergyLogLastHoursNumberOfEntries = _LoadEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 2),
    _LoadEnergyLogLastHoursNumberOfEntries_Type()
)
loadEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursNumberOfEntries.setStatus("current")
_LoadEnergyLogLastHoursTable_Object = MibTable
loadEnergyLogLastHoursTable = _LoadEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 3)
)
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursTable.setStatus("current")
_LoadEnergyLogLastHoursEntry_Object = MibTableRow
loadEnergyLogLastHoursEntry = _LoadEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 3, 1)
)
loadEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "loadEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursEntry.setStatus("current")


class _LoadEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type loadEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_LoadEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_LoadEnergyLogLastHoursIndex_Object = MibTableColumn
loadEnergyLogLastHoursIndex = _LoadEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 3, 1, 1),
    _LoadEnergyLogLastHoursIndex_Type()
)
loadEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursIndex.setStatus("current")
_LoadEnergyLogLastHoursValue_Type = Integer32
_LoadEnergyLogLastHoursValue_Object = MibTableColumn
loadEnergyLogLastHoursValue = _LoadEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 3, 1, 2),
    _LoadEnergyLogLastHoursValue_Type()
)
loadEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastHoursValue.setStatus("current")


class _LoadEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type loadEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_LoadEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_LoadEnergyLogLastDaysNumberOfEntries_Object = MibScalar
loadEnergyLogLastDaysNumberOfEntries = _LoadEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 4),
    _LoadEnergyLogLastDaysNumberOfEntries_Type()
)
loadEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysNumberOfEntries.setStatus("current")
_LoadEnergyLogLastDaysTable_Object = MibTable
loadEnergyLogLastDaysTable = _LoadEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 5)
)
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysTable.setStatus("current")
_LoadEnergyLogLastDaysEntry_Object = MibTableRow
loadEnergyLogLastDaysEntry = _LoadEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 5, 1)
)
loadEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "loadEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysEntry.setStatus("current")


class _LoadEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type loadEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_LoadEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_LoadEnergyLogLastDaysIndex_Object = MibTableColumn
loadEnergyLogLastDaysIndex = _LoadEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 5, 1, 1),
    _LoadEnergyLogLastDaysIndex_Type()
)
loadEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysIndex.setStatus("current")
_LoadEnergyLogLastDaysValue_Type = Integer32
_LoadEnergyLogLastDaysValue_Object = MibTableColumn
loadEnergyLogLastDaysValue = _LoadEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 5, 1, 2),
    _LoadEnergyLogLastDaysValue_Type()
)
loadEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastDaysValue.setStatus("current")


class _LoadEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type loadEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_LoadEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_LoadEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
loadEnergyLogLastWeeksNumberOfEntries = _LoadEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 6),
    _LoadEnergyLogLastWeeksNumberOfEntries_Type()
)
loadEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_LoadEnergyLogLastWeeksTable_Object = MibTable
loadEnergyLogLastWeeksTable = _LoadEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 7)
)
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksTable.setStatus("current")
_LoadEnergyLogLastWeeksEntry_Object = MibTableRow
loadEnergyLogLastWeeksEntry = _LoadEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 7, 1)
)
loadEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "loadEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksEntry.setStatus("current")


class _LoadEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type loadEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_LoadEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_LoadEnergyLogLastWeeksIndex_Object = MibTableColumn
loadEnergyLogLastWeeksIndex = _LoadEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 7, 1, 1),
    _LoadEnergyLogLastWeeksIndex_Type()
)
loadEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksIndex.setStatus("current")
_LoadEnergyLogLastWeeksValue_Type = Integer32
_LoadEnergyLogLastWeeksValue_Object = MibTableColumn
loadEnergyLogLastWeeksValue = _LoadEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 8, 7, 1, 2),
    _LoadEnergyLogLastWeeksValue_Type()
)
loadEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadEnergyLogLastWeeksValue.setStatus("current")
_LoadVoltageTable_Object = MibTable
loadVoltageTable = _LoadVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 9)
)
if mibBuilder.loadTexts:
    loadVoltageTable.setStatus("current")
_LoadVoltageEntry_Object = MibTableRow
loadVoltageEntry = _LoadVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 9, 1)
)
loadVoltageEntry.setIndexNames(
    (0, "SP2-MIB", "loadGroupIndex"),
    (0, "SP2-MIB", "loadVoltageIndex"),
)
if mibBuilder.loadTexts:
    loadVoltageEntry.setStatus("current")


class _LoadVoltageIndex_Type(Integer32):
    """Custom type loadVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LoadVoltageIndex_Type.__name__ = "Integer32"
_LoadVoltageIndex_Object = MibTableColumn
loadVoltageIndex = _LoadVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 9, 1, 1),
    _LoadVoltageIndex_Type()
)
loadVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    loadVoltageIndex.setStatus("current")


class _LoadVoltageStatus_Type(Integer32):
    """Custom type loadVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_LoadVoltageStatus_Type.__name__ = "Integer32"
_LoadVoltageStatus_Object = MibTableColumn
loadVoltageStatus = _LoadVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 9, 1, 2),
    _LoadVoltageStatus_Type()
)
loadVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadVoltageStatus.setStatus("current")


class _LoadVoltageDescription_Type(DisplayString):
    """Custom type loadVoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadVoltageDescription_Type.__name__ = "DisplayString"
_LoadVoltageDescription_Object = MibTableColumn
loadVoltageDescription = _LoadVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 9, 1, 3),
    _LoadVoltageDescription_Type()
)
loadVoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadVoltageDescription.setStatus("current")
_LoadVoltageTrapRepeatCounter_Type = Counter32
_LoadVoltageTrapRepeatCounter_Object = MibTableColumn
loadVoltageTrapRepeatCounter = _LoadVoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 9, 1, 4),
    _LoadVoltageTrapRepeatCounter_Type()
)
loadVoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadVoltageTrapRepeatCounter.setStatus("current")


class _LoadVoltageEnable_Type(Integer32):
    """Custom type loadVoltageEnable based on Integer32"""
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


_LoadVoltageEnable_Type.__name__ = "Integer32"
_LoadVoltageEnable_Object = MibTableColumn
loadVoltageEnable = _LoadVoltageEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 9, 1, 5),
    _LoadVoltageEnable_Type()
)
loadVoltageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadVoltageEnable.setStatus("current")
_LoadVoltageValue_Type = Integer32
_LoadVoltageValue_Object = MibTableColumn
loadVoltageValue = _LoadVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 9, 9, 1, 6),
    _LoadVoltageValue_Type()
)
loadVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadVoltageValue.setStatus("current")
_Battery_ObjectIdentity = ObjectIdentity
battery = _Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10)
)


class _BatteryStatus_Type(Integer32):
    """Custom type batteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryStatus_Type.__name__ = "Integer32"
_BatteryStatus_Object = MibScalar
batteryStatus = _BatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 1),
    _BatteryStatus_Type()
)
batteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryStatus.setStatus("current")


class _BatteryDescription_Type(DisplayString):
    """Custom type batteryDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BatteryDescription_Type.__name__ = "DisplayString"
_BatteryDescription_Object = MibScalar
batteryDescription = _BatteryDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 2),
    _BatteryDescription_Type()
)
batteryDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryDescription.setStatus("current")


class _BatteryReferenceVoltage_Type(Integer32):
    """Custom type batteryReferenceVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(840, 60417),
    )


_BatteryReferenceVoltage_Type.__name__ = "Integer32"
_BatteryReferenceVoltage_Object = MibScalar
batteryReferenceVoltage = _BatteryReferenceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 3),
    _BatteryReferenceVoltage_Type()
)
batteryReferenceVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryReferenceVoltage.setStatus("current")


class _BatteryFusesStatus_Type(Integer32):
    """Custom type batteryFusesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryFusesStatus_Type.__name__ = "Integer32"
_BatteryFusesStatus_Object = MibScalar
batteryFusesStatus = _BatteryFusesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 4),
    _BatteryFusesStatus_Type()
)
batteryFusesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFusesStatus.setStatus("current")
_BatteryVoltage_ObjectIdentity = ObjectIdentity
batteryVoltage = _BatteryVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5)
)


class _BatteryVoltageStatus_Type(Integer32):
    """Custom type batteryVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryVoltageStatus_Type.__name__ = "Integer32"
_BatteryVoltageStatus_Object = MibScalar
batteryVoltageStatus = _BatteryVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 1),
    _BatteryVoltageStatus_Type()
)
batteryVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageStatus.setStatus("current")


class _BatteryVoltageDescription_Type(DisplayString):
    """Custom type batteryVoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryVoltageDescription_Type.__name__ = "DisplayString"
_BatteryVoltageDescription_Object = MibScalar
batteryVoltageDescription = _BatteryVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 2),
    _BatteryVoltageDescription_Type()
)
batteryVoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageDescription.setStatus("current")
_BatteryVoltageTrapRepeatCounter_Type = Counter32
_BatteryVoltageTrapRepeatCounter_Object = MibScalar
batteryVoltageTrapRepeatCounter = _BatteryVoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 3),
    _BatteryVoltageTrapRepeatCounter_Type()
)
batteryVoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryVoltageTrapRepeatCounter.setStatus("current")


class _BatteryVoltageAlarmEnable_Type(Integer32):
    """Custom type batteryVoltageAlarmEnable based on Integer32"""
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


_BatteryVoltageAlarmEnable_Type.__name__ = "Integer32"
_BatteryVoltageAlarmEnable_Object = MibScalar
batteryVoltageAlarmEnable = _BatteryVoltageAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 4),
    _BatteryVoltageAlarmEnable_Type()
)
batteryVoltageAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageAlarmEnable.setStatus("current")


class _BatteryVoltageValue_Type(Integer32):
    """Custom type batteryVoltageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_BatteryVoltageValue_Type.__name__ = "Integer32"
_BatteryVoltageValue_Object = MibScalar
batteryVoltageValue = _BatteryVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 5),
    _BatteryVoltageValue_Type()
)
batteryVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryVoltageValue.setStatus("current")
_BatteryVoltageMajorHighLevel_Type = Integer32
_BatteryVoltageMajorHighLevel_Object = MibScalar
batteryVoltageMajorHighLevel = _BatteryVoltageMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 6),
    _BatteryVoltageMajorHighLevel_Type()
)
batteryVoltageMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageMajorHighLevel.setStatus("current")
_BatteryVoltageMinorHighLevel_Type = Integer32
_BatteryVoltageMinorHighLevel_Object = MibScalar
batteryVoltageMinorHighLevel = _BatteryVoltageMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 7),
    _BatteryVoltageMinorHighLevel_Type()
)
batteryVoltageMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageMinorHighLevel.setStatus("current")
_BatteryVoltageMinorLowLevel_Type = Integer32
_BatteryVoltageMinorLowLevel_Object = MibScalar
batteryVoltageMinorLowLevel = _BatteryVoltageMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 8),
    _BatteryVoltageMinorLowLevel_Type()
)
batteryVoltageMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageMinorLowLevel.setStatus("current")
_BatteryVoltageMajorLowLevel_Type = Integer32
_BatteryVoltageMajorLowLevel_Object = MibScalar
batteryVoltageMajorLowLevel = _BatteryVoltageMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 5, 9),
    _BatteryVoltageMajorLowLevel_Type()
)
batteryVoltageMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryVoltageMajorLowLevel.setStatus("current")
_BatteryCurrents_ObjectIdentity = ObjectIdentity
batteryCurrents = _BatteryCurrents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6)
)


class _BatteryCurrentsStatus_Type(Integer32):
    """Custom type batteryCurrentsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryCurrentsStatus_Type.__name__ = "Integer32"
_BatteryCurrentsStatus_Object = MibScalar
batteryCurrentsStatus = _BatteryCurrentsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 1),
    _BatteryCurrentsStatus_Type()
)
batteryCurrentsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentsStatus.setStatus("current")


class _BatteryCurrentsDescription_Type(DisplayString):
    """Custom type batteryCurrentsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryCurrentsDescription_Type.__name__ = "DisplayString"
_BatteryCurrentsDescription_Object = MibScalar
batteryCurrentsDescription = _BatteryCurrentsDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 2),
    _BatteryCurrentsDescription_Type()
)
batteryCurrentsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsDescription.setStatus("current")
_BatteryCurrentsTrapRepeatCounter_Type = Counter32
_BatteryCurrentsTrapRepeatCounter_Object = MibScalar
batteryCurrentsTrapRepeatCounter = _BatteryCurrentsTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 3),
    _BatteryCurrentsTrapRepeatCounter_Type()
)
batteryCurrentsTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryCurrentsTrapRepeatCounter.setStatus("current")


class _BatteryCurrentsAlarmEnable_Type(Integer32):
    """Custom type batteryCurrentsAlarmEnable based on Integer32"""
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


_BatteryCurrentsAlarmEnable_Type.__name__ = "Integer32"
_BatteryCurrentsAlarmEnable_Object = MibScalar
batteryCurrentsAlarmEnable = _BatteryCurrentsAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 4),
    _BatteryCurrentsAlarmEnable_Type()
)
batteryCurrentsAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsAlarmEnable.setStatus("current")
_BatteryCurrentsValue_Type = Integer32
_BatteryCurrentsValue_Object = MibScalar
batteryCurrentsValue = _BatteryCurrentsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 5),
    _BatteryCurrentsValue_Type()
)
batteryCurrentsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentsValue.setStatus("current")
_BatteryCurrentsMajorHighLevel_Type = Integer32
_BatteryCurrentsMajorHighLevel_Object = MibScalar
batteryCurrentsMajorHighLevel = _BatteryCurrentsMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 6),
    _BatteryCurrentsMajorHighLevel_Type()
)
batteryCurrentsMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsMajorHighLevel.setStatus("current")
_BatteryCurrentsMinorHighLevel_Type = Integer32
_BatteryCurrentsMinorHighLevel_Object = MibScalar
batteryCurrentsMinorHighLevel = _BatteryCurrentsMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 7),
    _BatteryCurrentsMinorHighLevel_Type()
)
batteryCurrentsMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsMinorHighLevel.setStatus("current")
_BatteryCurrentsMinorLowLevel_Type = Integer32
_BatteryCurrentsMinorLowLevel_Object = MibScalar
batteryCurrentsMinorLowLevel = _BatteryCurrentsMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 8),
    _BatteryCurrentsMinorLowLevel_Type()
)
batteryCurrentsMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsMinorLowLevel.setStatus("current")
_BatteryCurrentsMajorLowLevel_Type = Integer32
_BatteryCurrentsMajorLowLevel_Object = MibScalar
batteryCurrentsMajorLowLevel = _BatteryCurrentsMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 6, 9),
    _BatteryCurrentsMajorLowLevel_Type()
)
batteryCurrentsMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentsMajorLowLevel.setStatus("current")
_BatteryTemperatures_ObjectIdentity = ObjectIdentity
batteryTemperatures = _BatteryTemperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7)
)


class _BatteryTemperaturesStatus_Type(Integer32):
    """Custom type batteryTemperaturesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryTemperaturesStatus_Type.__name__ = "Integer32"
_BatteryTemperaturesStatus_Object = MibScalar
batteryTemperaturesStatus = _BatteryTemperaturesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 1),
    _BatteryTemperaturesStatus_Type()
)
batteryTemperaturesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperaturesStatus.setStatus("current")


class _BatteryTemperaturesDescription_Type(DisplayString):
    """Custom type batteryTemperaturesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTemperaturesDescription_Type.__name__ = "DisplayString"
_BatteryTemperaturesDescription_Object = MibScalar
batteryTemperaturesDescription = _BatteryTemperaturesDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 2),
    _BatteryTemperaturesDescription_Type()
)
batteryTemperaturesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesDescription.setStatus("current")
_BatteryTemperaturesTrapRepeatCounter_Type = Counter32
_BatteryTemperaturesTrapRepeatCounter_Object = MibScalar
batteryTemperaturesTrapRepeatCounter = _BatteryTemperaturesTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 3),
    _BatteryTemperaturesTrapRepeatCounter_Type()
)
batteryTemperaturesTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryTemperaturesTrapRepeatCounter.setStatus("current")


class _BatteryTemperaturesAlarmEnable_Type(Integer32):
    """Custom type batteryTemperaturesAlarmEnable based on Integer32"""
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


_BatteryTemperaturesAlarmEnable_Type.__name__ = "Integer32"
_BatteryTemperaturesAlarmEnable_Object = MibScalar
batteryTemperaturesAlarmEnable = _BatteryTemperaturesAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 4),
    _BatteryTemperaturesAlarmEnable_Type()
)
batteryTemperaturesAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesAlarmEnable.setStatus("current")


class _BatteryTemperaturesValue_Type(Integer32):
    """Custom type batteryTemperaturesValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_BatteryTemperaturesValue_Type.__name__ = "Integer32"
_BatteryTemperaturesValue_Object = MibScalar
batteryTemperaturesValue = _BatteryTemperaturesValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 5),
    _BatteryTemperaturesValue_Type()
)
batteryTemperaturesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperaturesValue.setStatus("current")
_BatteryTemperaturesMajorHighLevel_Type = Integer32
_BatteryTemperaturesMajorHighLevel_Object = MibScalar
batteryTemperaturesMajorHighLevel = _BatteryTemperaturesMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 6),
    _BatteryTemperaturesMajorHighLevel_Type()
)
batteryTemperaturesMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesMajorHighLevel.setStatus("current")
_BatteryTemperaturesMinorHighLevel_Type = Integer32
_BatteryTemperaturesMinorHighLevel_Object = MibScalar
batteryTemperaturesMinorHighLevel = _BatteryTemperaturesMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 7),
    _BatteryTemperaturesMinorHighLevel_Type()
)
batteryTemperaturesMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesMinorHighLevel.setStatus("current")
_BatteryTemperaturesMinorLowLevel_Type = Integer32
_BatteryTemperaturesMinorLowLevel_Object = MibScalar
batteryTemperaturesMinorLowLevel = _BatteryTemperaturesMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 8),
    _BatteryTemperaturesMinorLowLevel_Type()
)
batteryTemperaturesMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesMinorLowLevel.setStatus("current")
_BatteryTemperaturesMajorLowLevel_Type = Integer32
_BatteryTemperaturesMajorLowLevel_Object = MibScalar
batteryTemperaturesMajorLowLevel = _BatteryTemperaturesMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 7, 9),
    _BatteryTemperaturesMajorLowLevel_Type()
)
batteryTemperaturesMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperaturesMajorLowLevel.setStatus("current")
_BatteryTimeLeft_ObjectIdentity = ObjectIdentity
batteryTimeLeft = _BatteryTimeLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8)
)


class _BatteryTimeLeftStatus_Type(Integer32):
    """Custom type batteryTimeLeftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryTimeLeftStatus_Type.__name__ = "Integer32"
_BatteryTimeLeftStatus_Object = MibScalar
batteryTimeLeftStatus = _BatteryTimeLeftStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 1),
    _BatteryTimeLeftStatus_Type()
)
batteryTimeLeftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTimeLeftStatus.setStatus("current")


class _BatteryTimeLeftDescription_Type(DisplayString):
    """Custom type batteryTimeLeftDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTimeLeftDescription_Type.__name__ = "DisplayString"
_BatteryTimeLeftDescription_Object = MibScalar
batteryTimeLeftDescription = _BatteryTimeLeftDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 2),
    _BatteryTimeLeftDescription_Type()
)
batteryTimeLeftDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTimeLeftDescription.setStatus("current")
_BatteryTimeLeftTrapRepeatCounter_Type = Counter32
_BatteryTimeLeftTrapRepeatCounter_Object = MibScalar
batteryTimeLeftTrapRepeatCounter = _BatteryTimeLeftTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 3),
    _BatteryTimeLeftTrapRepeatCounter_Type()
)
batteryTimeLeftTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryTimeLeftTrapRepeatCounter.setStatus("current")


class _BatteryTimeLeftAlarmEnable_Type(Integer32):
    """Custom type batteryTimeLeftAlarmEnable based on Integer32"""
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


_BatteryTimeLeftAlarmEnable_Type.__name__ = "Integer32"
_BatteryTimeLeftAlarmEnable_Object = MibScalar
batteryTimeLeftAlarmEnable = _BatteryTimeLeftAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 4),
    _BatteryTimeLeftAlarmEnable_Type()
)
batteryTimeLeftAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTimeLeftAlarmEnable.setStatus("current")
_BatteryTimeLeftValue_Type = Integer32
_BatteryTimeLeftValue_Object = MibScalar
batteryTimeLeftValue = _BatteryTimeLeftValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 5),
    _BatteryTimeLeftValue_Type()
)
batteryTimeLeftValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTimeLeftValue.setStatus("current")
_BatteryTimeLeftMinorAlarmLevel_Type = Integer32
_BatteryTimeLeftMinorAlarmLevel_Object = MibScalar
batteryTimeLeftMinorAlarmLevel = _BatteryTimeLeftMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 6),
    _BatteryTimeLeftMinorAlarmLevel_Type()
)
batteryTimeLeftMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTimeLeftMinorAlarmLevel.setStatus("current")
_BatteryTimeLeftMajorAlarmLevel_Type = Integer32
_BatteryTimeLeftMajorAlarmLevel_Object = MibScalar
batteryTimeLeftMajorAlarmLevel = _BatteryTimeLeftMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 8, 7),
    _BatteryTimeLeftMajorAlarmLevel_Type()
)
batteryTimeLeftMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTimeLeftMajorAlarmLevel.setStatus("current")
_BatteryRemainingCapacity_ObjectIdentity = ObjectIdentity
batteryRemainingCapacity = _BatteryRemainingCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9)
)


class _BatteryRemainingCapacityStatus_Type(Integer32):
    """Custom type batteryRemainingCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryRemainingCapacityStatus_Type.__name__ = "Integer32"
_BatteryRemainingCapacityStatus_Object = MibScalar
batteryRemainingCapacityStatus = _BatteryRemainingCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 1),
    _BatteryRemainingCapacityStatus_Type()
)
batteryRemainingCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRemainingCapacityStatus.setStatus("current")


class _BatteryRemainingCapacityDescription_Type(DisplayString):
    """Custom type batteryRemainingCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryRemainingCapacityDescription_Type.__name__ = "DisplayString"
_BatteryRemainingCapacityDescription_Object = MibScalar
batteryRemainingCapacityDescription = _BatteryRemainingCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 2),
    _BatteryRemainingCapacityDescription_Type()
)
batteryRemainingCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryRemainingCapacityDescription.setStatus("current")
_BatteryRemainingCapacityTrapRepeatCounter_Type = Counter32
_BatteryRemainingCapacityTrapRepeatCounter_Object = MibScalar
batteryRemainingCapacityTrapRepeatCounter = _BatteryRemainingCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 3),
    _BatteryRemainingCapacityTrapRepeatCounter_Type()
)
batteryRemainingCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryRemainingCapacityTrapRepeatCounter.setStatus("current")


class _BatteryRemainingCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryRemainingCapacityAlarmEnable based on Integer32"""
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


_BatteryRemainingCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryRemainingCapacityAlarmEnable_Object = MibScalar
batteryRemainingCapacityAlarmEnable = _BatteryRemainingCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 4),
    _BatteryRemainingCapacityAlarmEnable_Type()
)
batteryRemainingCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryRemainingCapacityAlarmEnable.setStatus("current")
_BatteryRemainingCapacityValue_Type = Integer32
_BatteryRemainingCapacityValue_Object = MibScalar
batteryRemainingCapacityValue = _BatteryRemainingCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 5),
    _BatteryRemainingCapacityValue_Type()
)
batteryRemainingCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryRemainingCapacityValue.setStatus("current")
_BatteryRemainingCapacityMinorLowLevel_Type = Integer32
_BatteryRemainingCapacityMinorLowLevel_Object = MibScalar
batteryRemainingCapacityMinorLowLevel = _BatteryRemainingCapacityMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 6),
    _BatteryRemainingCapacityMinorLowLevel_Type()
)
batteryRemainingCapacityMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryRemainingCapacityMinorLowLevel.setStatus("current")
_BatteryRemainingCapacityMajorLowLevel_Type = Integer32
_BatteryRemainingCapacityMajorLowLevel_Object = MibScalar
batteryRemainingCapacityMajorLowLevel = _BatteryRemainingCapacityMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 9, 7),
    _BatteryRemainingCapacityMajorLowLevel_Type()
)
batteryRemainingCapacityMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryRemainingCapacityMajorLowLevel.setStatus("current")
_BatteryUsedCapacity_ObjectIdentity = ObjectIdentity
batteryUsedCapacity = _BatteryUsedCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10)
)


class _BatteryUsedCapacityStatus_Type(Integer32):
    """Custom type batteryUsedCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryUsedCapacityStatus_Type.__name__ = "Integer32"
_BatteryUsedCapacityStatus_Object = MibScalar
batteryUsedCapacityStatus = _BatteryUsedCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 1),
    _BatteryUsedCapacityStatus_Type()
)
batteryUsedCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryUsedCapacityStatus.setStatus("current")


class _BatteryUsedCapacityDescription_Type(DisplayString):
    """Custom type batteryUsedCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryUsedCapacityDescription_Type.__name__ = "DisplayString"
_BatteryUsedCapacityDescription_Object = MibScalar
batteryUsedCapacityDescription = _BatteryUsedCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 2),
    _BatteryUsedCapacityDescription_Type()
)
batteryUsedCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryUsedCapacityDescription.setStatus("current")
_BatteryUsedCapacityTrapRepeatCounter_Type = Counter32
_BatteryUsedCapacityTrapRepeatCounter_Object = MibScalar
batteryUsedCapacityTrapRepeatCounter = _BatteryUsedCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 3),
    _BatteryUsedCapacityTrapRepeatCounter_Type()
)
batteryUsedCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryUsedCapacityTrapRepeatCounter.setStatus("current")


class _BatteryUsedCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryUsedCapacityAlarmEnable based on Integer32"""
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


_BatteryUsedCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryUsedCapacityAlarmEnable_Object = MibScalar
batteryUsedCapacityAlarmEnable = _BatteryUsedCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 4),
    _BatteryUsedCapacityAlarmEnable_Type()
)
batteryUsedCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryUsedCapacityAlarmEnable.setStatus("current")
_BatteryUsedCapacityValue_Type = Integer32
_BatteryUsedCapacityValue_Object = MibScalar
batteryUsedCapacityValue = _BatteryUsedCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 5),
    _BatteryUsedCapacityValue_Type()
)
batteryUsedCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryUsedCapacityValue.setStatus("current")
_BatteryUsedCapacityMajorAlarmLevel_Type = Integer32
_BatteryUsedCapacityMajorAlarmLevel_Object = MibScalar
batteryUsedCapacityMajorAlarmLevel = _BatteryUsedCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 6),
    _BatteryUsedCapacityMajorAlarmLevel_Type()
)
batteryUsedCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryUsedCapacityMajorAlarmLevel.setStatus("current")
_BatteryUsedCapacityMinorAlarmLevel_Type = Integer32
_BatteryUsedCapacityMinorAlarmLevel_Object = MibScalar
batteryUsedCapacityMinorAlarmLevel = _BatteryUsedCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 10, 7),
    _BatteryUsedCapacityMinorAlarmLevel_Type()
)
batteryUsedCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryUsedCapacityMinorAlarmLevel.setStatus("current")
_BatteryTotalCapacity_ObjectIdentity = ObjectIdentity
batteryTotalCapacity = _BatteryTotalCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11)
)


class _BatteryTotalCapacityStatus_Type(Integer32):
    """Custom type batteryTotalCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryTotalCapacityStatus_Type.__name__ = "Integer32"
_BatteryTotalCapacityStatus_Object = MibScalar
batteryTotalCapacityStatus = _BatteryTotalCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 1),
    _BatteryTotalCapacityStatus_Type()
)
batteryTotalCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTotalCapacityStatus.setStatus("current")


class _BatteryTotalCapacityDescription_Type(DisplayString):
    """Custom type batteryTotalCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTotalCapacityDescription_Type.__name__ = "DisplayString"
_BatteryTotalCapacityDescription_Object = MibScalar
batteryTotalCapacityDescription = _BatteryTotalCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 2),
    _BatteryTotalCapacityDescription_Type()
)
batteryTotalCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTotalCapacityDescription.setStatus("current")
_BatteryTotalCapacityTrapRepeatCounter_Type = Counter32
_BatteryTotalCapacityTrapRepeatCounter_Object = MibScalar
batteryTotalCapacityTrapRepeatCounter = _BatteryTotalCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 3),
    _BatteryTotalCapacityTrapRepeatCounter_Type()
)
batteryTotalCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryTotalCapacityTrapRepeatCounter.setStatus("current")


class _BatteryTotalCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryTotalCapacityAlarmEnable based on Integer32"""
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


_BatteryTotalCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryTotalCapacityAlarmEnable_Object = MibScalar
batteryTotalCapacityAlarmEnable = _BatteryTotalCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 4),
    _BatteryTotalCapacityAlarmEnable_Type()
)
batteryTotalCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTotalCapacityAlarmEnable.setStatus("current")
_BatteryTotalCapacityValue_Type = Integer32
_BatteryTotalCapacityValue_Object = MibScalar
batteryTotalCapacityValue = _BatteryTotalCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 5),
    _BatteryTotalCapacityValue_Type()
)
batteryTotalCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTotalCapacityValue.setStatus("current")
_BatteryTotalCapacityMinorLowLevel_Type = Integer32
_BatteryTotalCapacityMinorLowLevel_Object = MibScalar
batteryTotalCapacityMinorLowLevel = _BatteryTotalCapacityMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 6),
    _BatteryTotalCapacityMinorLowLevel_Type()
)
batteryTotalCapacityMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTotalCapacityMinorLowLevel.setStatus("current")
_BatteryTotalCapacityMajorLowLevel_Type = Integer32
_BatteryTotalCapacityMajorLowLevel_Object = MibScalar
batteryTotalCapacityMajorLowLevel = _BatteryTotalCapacityMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 11, 7),
    _BatteryTotalCapacityMajorLowLevel_Type()
)
batteryTotalCapacityMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTotalCapacityMajorLowLevel.setStatus("current")
_BatteryQuality_ObjectIdentity = ObjectIdentity
batteryQuality = _BatteryQuality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12)
)


class _BatteryQualityStatus_Type(Integer32):
    """Custom type batteryQualityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryQualityStatus_Type.__name__ = "Integer32"
_BatteryQualityStatus_Object = MibScalar
batteryQualityStatus = _BatteryQualityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 1),
    _BatteryQualityStatus_Type()
)
batteryQualityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryQualityStatus.setStatus("current")


class _BatteryQualityDescription_Type(DisplayString):
    """Custom type batteryQualityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryQualityDescription_Type.__name__ = "DisplayString"
_BatteryQualityDescription_Object = MibScalar
batteryQualityDescription = _BatteryQualityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 2),
    _BatteryQualityDescription_Type()
)
batteryQualityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryQualityDescription.setStatus("current")
_BatteryQualityTrapRepeatCounter_Type = Counter32
_BatteryQualityTrapRepeatCounter_Object = MibScalar
batteryQualityTrapRepeatCounter = _BatteryQualityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 3),
    _BatteryQualityTrapRepeatCounter_Type()
)
batteryQualityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryQualityTrapRepeatCounter.setStatus("current")


class _BatteryQualityAlarmEnable_Type(Integer32):
    """Custom type batteryQualityAlarmEnable based on Integer32"""
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


_BatteryQualityAlarmEnable_Type.__name__ = "Integer32"
_BatteryQualityAlarmEnable_Object = MibScalar
batteryQualityAlarmEnable = _BatteryQualityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 4),
    _BatteryQualityAlarmEnable_Type()
)
batteryQualityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryQualityAlarmEnable.setStatus("current")
_BatteryQualityValue_Type = Integer32
_BatteryQualityValue_Object = MibScalar
batteryQualityValue = _BatteryQualityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 5),
    _BatteryQualityValue_Type()
)
batteryQualityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryQualityValue.setStatus("current")
_BatteryQualityMinorAlarmLevel_Type = Integer32
_BatteryQualityMinorAlarmLevel_Object = MibScalar
batteryQualityMinorAlarmLevel = _BatteryQualityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 6),
    _BatteryQualityMinorAlarmLevel_Type()
)
batteryQualityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryQualityMinorAlarmLevel.setStatus("current")
_BatteryQualityMajorAlarmLevel_Type = Integer32
_BatteryQualityMajorAlarmLevel_Object = MibScalar
batteryQualityMajorAlarmLevel = _BatteryQualityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 12, 7),
    _BatteryQualityMajorAlarmLevel_Type()
)
batteryQualityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryQualityMajorAlarmLevel.setStatus("current")
_BatteryLVBD_ObjectIdentity = ObjectIdentity
batteryLVBD = _BatteryLVBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13)
)


class _BatteryLVBDStatus_Type(Integer32):
    """Custom type batteryLVBDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryLVBDStatus_Type.__name__ = "Integer32"
_BatteryLVBDStatus_Object = MibScalar
batteryLVBDStatus = _BatteryLVBDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 1),
    _BatteryLVBDStatus_Type()
)
batteryLVBDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLVBDStatus.setStatus("current")


class _BatteryLVBDDescription_Type(DisplayString):
    """Custom type batteryLVBDDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryLVBDDescription_Type.__name__ = "DisplayString"
_BatteryLVBDDescription_Object = MibScalar
batteryLVBDDescription = _BatteryLVBDDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 2),
    _BatteryLVBDDescription_Type()
)
batteryLVBDDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVBDDescription.setStatus("current")
_BatteryLVBDTrapRepeatCounter_Type = Counter32
_BatteryLVBDTrapRepeatCounter_Object = MibScalar
batteryLVBDTrapRepeatCounter = _BatteryLVBDTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 3),
    _BatteryLVBDTrapRepeatCounter_Type()
)
batteryLVBDTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryLVBDTrapRepeatCounter.setStatus("current")


class _BatteryLVBDEnable_Type(Integer32):
    """Custom type batteryLVBDEnable based on Integer32"""
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


_BatteryLVBDEnable_Type.__name__ = "Integer32"
_BatteryLVBDEnable_Object = MibScalar
batteryLVBDEnable = _BatteryLVBDEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 4),
    _BatteryLVBDEnable_Type()
)
batteryLVBDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVBDEnable.setStatus("current")
_BatteryLVBDValue_Type = Integer32
_BatteryLVBDValue_Object = MibScalar
batteryLVBDValue = _BatteryLVBDValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 5),
    _BatteryLVBDValue_Type()
)
batteryLVBDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryLVBDValue.setStatus("current")
_BatteryLVBDConnectVoltage_Type = Integer32
_BatteryLVBDConnectVoltage_Object = MibScalar
batteryLVBDConnectVoltage = _BatteryLVBDConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 6),
    _BatteryLVBDConnectVoltage_Type()
)
batteryLVBDConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVBDConnectVoltage.setStatus("current")
_BatteryLVBDDisconnectVoltage_Type = Integer32
_BatteryLVBDDisconnectVoltage_Object = MibScalar
batteryLVBDDisconnectVoltage = _BatteryLVBDDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 13, 7),
    _BatteryLVBDDisconnectVoltage_Type()
)
batteryLVBDDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryLVBDDisconnectVoltage.setStatus("current")
_BatteryChargeCurrentLimit_ObjectIdentity = ObjectIdentity
batteryChargeCurrentLimit = _BatteryChargeCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 14)
)


class _BatteryChargeCurrentLimitEnable_Type(Integer32):
    """Custom type batteryChargeCurrentLimitEnable based on Integer32"""
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


_BatteryChargeCurrentLimitEnable_Type.__name__ = "Integer32"
_BatteryChargeCurrentLimitEnable_Object = MibScalar
batteryChargeCurrentLimitEnable = _BatteryChargeCurrentLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 14, 1),
    _BatteryChargeCurrentLimitEnable_Type()
)
batteryChargeCurrentLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitEnable.setStatus("current")


class _BatteryChargeCurrentLimitValue_Type(Integer32):
    """Custom type batteryChargeCurrentLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BatteryChargeCurrentLimitValue_Type.__name__ = "Integer32"
_BatteryChargeCurrentLimitValue_Object = MibScalar
batteryChargeCurrentLimitValue = _BatteryChargeCurrentLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 14, 2),
    _BatteryChargeCurrentLimitValue_Type()
)
batteryChargeCurrentLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryChargeCurrentLimitValue.setStatus("current")
_BatteryBoost_ObjectIdentity = ObjectIdentity
batteryBoost = _BatteryBoost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15)
)


class _BatteryBoostVoltage_Type(Integer32):
    """Custom type batteryBoostVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(870, 60418),
    )


_BatteryBoostVoltage_Type.__name__ = "Integer32"
_BatteryBoostVoltage_Object = MibScalar
batteryBoostVoltage = _BatteryBoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15, 1),
    _BatteryBoostVoltage_Type()
)
batteryBoostVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostVoltage.setStatus("current")


class _BatteryBoostCommand_Type(Integer32):
    """Custom type batteryBoostCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("startboost", 1),
          ("stopboost", 2))
    )


_BatteryBoostCommand_Type.__name__ = "Integer32"
_BatteryBoostCommand_Object = MibScalar
batteryBoostCommand = _BatteryBoostCommand_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15, 2),
    _BatteryBoostCommand_Type()
)
batteryBoostCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostCommand.setStatus("current")
_BatteryBoostCurrentThreshold_Type = Integer32
_BatteryBoostCurrentThreshold_Object = MibScalar
batteryBoostCurrentThreshold = _BatteryBoostCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15, 3),
    _BatteryBoostCurrentThreshold_Type()
)
batteryBoostCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostCurrentThreshold.setStatus("current")


class _BatteryBoostManualMaxDuration_Type(Integer32):
    """Custom type batteryBoostManualMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_BatteryBoostManualMaxDuration_Type.__name__ = "Integer32"
_BatteryBoostManualMaxDuration_Object = MibScalar
batteryBoostManualMaxDuration = _BatteryBoostManualMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 15, 4),
    _BatteryBoostManualMaxDuration_Type()
)
batteryBoostManualMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBoostManualMaxDuration.setStatus("current")
_BatteryTest_ObjectIdentity = ObjectIdentity
batteryTest = _BatteryTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16)
)
_BatteryTestVoltage_Type = Integer32
_BatteryTestVoltage_Object = MibScalar
batteryTestVoltage = _BatteryTestVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 1),
    _BatteryTestVoltage_Type()
)
batteryTestVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTestVoltage.setStatus("current")


class _BatteryTestCommand_Type(Integer32):
    """Custom type batteryTestCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("starttest", 1),
          ("stoptest", 2))
    )


_BatteryTestCommand_Type.__name__ = "Integer32"
_BatteryTestCommand_Object = MibScalar
batteryTestCommand = _BatteryTestCommand_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 2),
    _BatteryTestCommand_Type()
)
batteryTestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTestCommand.setStatus("current")


class _BatteryTestNumberOfResults_Type(Integer32):
    """Custom type batteryTestNumberOfResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_BatteryTestNumberOfResults_Type.__name__ = "Integer32"
_BatteryTestNumberOfResults_Object = MibScalar
batteryTestNumberOfResults = _BatteryTestNumberOfResults_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 3),
    _BatteryTestNumberOfResults_Type()
)
batteryTestNumberOfResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestNumberOfResults.setStatus("current")
_BatteryTestResultTable_Object = MibTable
batteryTestResultTable = _BatteryTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4)
)
if mibBuilder.loadTexts:
    batteryTestResultTable.setStatus("current")
_BatteryTestResultEntry_Object = MibTableRow
batteryTestResultEntry = _BatteryTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1)
)
batteryTestResultEntry.setIndexNames(
    (0, "SP2-MIB", "batteryTestResultIndex"),
)
if mibBuilder.loadTexts:
    batteryTestResultEntry.setStatus("current")


class _BatteryTestResultIndex_Type(Integer32):
    """Custom type batteryTestResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BatteryTestResultIndex_Type.__name__ = "Integer32"
_BatteryTestResultIndex_Object = MibTableColumn
batteryTestResultIndex = _BatteryTestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 1),
    _BatteryTestResultIndex_Type()
)
batteryTestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryTestResultIndex.setStatus("current")
_BatteryTestResultStartDateTime_Type = DateAndTime
_BatteryTestResultStartDateTime_Object = MibTableColumn
batteryTestResultStartDateTime = _BatteryTestResultStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 2),
    _BatteryTestResultStartDateTime_Type()
)
batteryTestResultStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResultStartDateTime.setStatus("current")
_BatteryTestResultDuration_Type = Integer32
_BatteryTestResultDuration_Object = MibTableColumn
batteryTestResultDuration = _BatteryTestResultDuration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 3),
    _BatteryTestResultDuration_Type()
)
batteryTestResultDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResultDuration.setStatus("current")
_BatteryTestResultDischarged_Type = Integer32
_BatteryTestResultDischarged_Object = MibTableColumn
batteryTestResultDischarged = _BatteryTestResultDischarged_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 4),
    _BatteryTestResultDischarged_Type()
)
batteryTestResultDischarged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResultDischarged.setStatus("current")
_BatteryTestResultQuality_Type = Integer32
_BatteryTestResultQuality_Object = MibTableColumn
batteryTestResultQuality = _BatteryTestResultQuality_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 16, 4, 1, 5),
    _BatteryTestResultQuality_Type()
)
batteryTestResultQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTestResultQuality.setStatus("current")
_BatteryTempComp_ObjectIdentity = ObjectIdentity
batteryTempComp = _BatteryTempComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 17)
)


class _BatteryTempCompEnable_Type(Integer32):
    """Custom type batteryTempCompEnable based on Integer32"""
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


_BatteryTempCompEnable_Type.__name__ = "Integer32"
_BatteryTempCompEnable_Object = MibScalar
batteryTempCompEnable = _BatteryTempCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 17, 1),
    _BatteryTempCompEnable_Type()
)
batteryTempCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTempCompEnable.setStatus("current")
_BatteryBank_ObjectIdentity = ObjectIdentity
batteryBank = _BatteryBank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18)
)


class _BatteryBankNumberOfBanks_Type(Integer32):
    """Custom type batteryBankNumberOfBanks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BatteryBankNumberOfBanks_Type.__name__ = "Integer32"
_BatteryBankNumberOfBanks_Object = MibScalar
batteryBankNumberOfBanks = _BatteryBankNumberOfBanks_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 1),
    _BatteryBankNumberOfBanks_Type()
)
batteryBankNumberOfBanks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBankNumberOfBanks.setStatus("current")
_BatteryBankTable_Object = MibTable
batteryBankTable = _BatteryBankTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2)
)
if mibBuilder.loadTexts:
    batteryBankTable.setStatus("current")
_BatteryBankEntry_Object = MibTableRow
batteryBankEntry = _BatteryBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1)
)
batteryBankEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
)
if mibBuilder.loadTexts:
    batteryBankEntry.setStatus("current")


class _BatteryBankIndex_Type(Integer32):
    """Custom type batteryBankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryBankIndex_Type.__name__ = "Integer32"
_BatteryBankIndex_Object = MibTableColumn
batteryBankIndex = _BatteryBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 1),
    _BatteryBankIndex_Type()
)
batteryBankIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryBankIndex.setStatus("current")


class _BatteryBankStatus_Type(Integer32):
    """Custom type batteryBankStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryBankStatus_Type.__name__ = "Integer32"
_BatteryBankStatus_Object = MibTableColumn
batteryBankStatus = _BatteryBankStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 2),
    _BatteryBankStatus_Type()
)
batteryBankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankStatus.setStatus("current")


class _BatteryBankNumberOfTemperatures_Type(Integer32):
    """Custom type batteryBankNumberOfTemperatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryBankNumberOfTemperatures_Type.__name__ = "Integer32"
_BatteryBankNumberOfTemperatures_Object = MibTableColumn
batteryBankNumberOfTemperatures = _BatteryBankNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 3),
    _BatteryBankNumberOfTemperatures_Type()
)
batteryBankNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankNumberOfTemperatures.setStatus("current")


class _BatteryBankNumberOfCurrents_Type(Integer32):
    """Custom type batteryBankNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryBankNumberOfCurrents_Type.__name__ = "Integer32"
_BatteryBankNumberOfCurrents_Object = MibTableColumn
batteryBankNumberOfCurrents = _BatteryBankNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 4),
    _BatteryBankNumberOfCurrents_Type()
)
batteryBankNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankNumberOfCurrents.setStatus("current")


class _BatteryBankNumberOfFuses_Type(Integer32):
    """Custom type batteryBankNumberOfFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryBankNumberOfFuses_Type.__name__ = "Integer32"
_BatteryBankNumberOfFuses_Object = MibTableColumn
batteryBankNumberOfFuses = _BatteryBankNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 5),
    _BatteryBankNumberOfFuses_Type()
)
batteryBankNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankNumberOfFuses.setStatus("current")


class _BatteryBankNumberOfSymmetries_Type(Integer32):
    """Custom type batteryBankNumberOfSymmetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryBankNumberOfSymmetries_Type.__name__ = "Integer32"
_BatteryBankNumberOfSymmetries_Object = MibTableColumn
batteryBankNumberOfSymmetries = _BatteryBankNumberOfSymmetries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 2, 1, 6),
    _BatteryBankNumberOfSymmetries_Type()
)
batteryBankNumberOfSymmetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankNumberOfSymmetries.setStatus("current")
_BatteryBankTemperatureTable_Object = MibTable
batteryBankTemperatureTable = _BatteryBankTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3)
)
if mibBuilder.loadTexts:
    batteryBankTemperatureTable.setStatus("current")
_BatteryBankTemperatureEntry_Object = MibTableRow
batteryBankTemperatureEntry = _BatteryBankTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1)
)
batteryBankTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
    (0, "SP2-MIB", "batteryTemperatureIndex"),
)
if mibBuilder.loadTexts:
    batteryBankTemperatureEntry.setStatus("current")


class _BatteryTemperatureIndex_Type(Integer32):
    """Custom type batteryTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryTemperatureIndex_Type.__name__ = "Integer32"
_BatteryTemperatureIndex_Object = MibTableColumn
batteryTemperatureIndex = _BatteryTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 1),
    _BatteryTemperatureIndex_Type()
)
batteryTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryTemperatureIndex.setStatus("current")


class _BatteryTemperatureStatus_Type(Integer32):
    """Custom type batteryTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryTemperatureStatus_Type.__name__ = "Integer32"
_BatteryTemperatureStatus_Object = MibTableColumn
batteryTemperatureStatus = _BatteryTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 2),
    _BatteryTemperatureStatus_Type()
)
batteryTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperatureStatus.setStatus("current")


class _BatteryTemperatureDescription_Type(DisplayString):
    """Custom type batteryTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryTemperatureDescription_Type.__name__ = "DisplayString"
_BatteryTemperatureDescription_Object = MibTableColumn
batteryTemperatureDescription = _BatteryTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 3),
    _BatteryTemperatureDescription_Type()
)
batteryTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureDescription.setStatus("current")
_BatteryTemperatureTrapRepeatCounter_Type = Counter32
_BatteryTemperatureTrapRepeatCounter_Object = MibTableColumn
batteryTemperatureTrapRepeatCounter = _BatteryTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 4),
    _BatteryTemperatureTrapRepeatCounter_Type()
)
batteryTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryTemperatureTrapRepeatCounter.setStatus("current")


class _BatteryTemperatureAlarmEnable_Type(Integer32):
    """Custom type batteryTemperatureAlarmEnable based on Integer32"""
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


_BatteryTemperatureAlarmEnable_Type.__name__ = "Integer32"
_BatteryTemperatureAlarmEnable_Object = MibTableColumn
batteryTemperatureAlarmEnable = _BatteryTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 5),
    _BatteryTemperatureAlarmEnable_Type()
)
batteryTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureAlarmEnable.setStatus("current")
_BatteryTemperatureValue_Type = Integer32
_BatteryTemperatureValue_Object = MibTableColumn
batteryTemperatureValue = _BatteryTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 6),
    _BatteryTemperatureValue_Type()
)
batteryTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryTemperatureValue.setStatus("current")
_BatteryTemperatureMajorHighLevel_Type = Integer32
_BatteryTemperatureMajorHighLevel_Object = MibTableColumn
batteryTemperatureMajorHighLevel = _BatteryTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 7),
    _BatteryTemperatureMajorHighLevel_Type()
)
batteryTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureMajorHighLevel.setStatus("current")
_BatteryTemperatureMinorHighLevel_Type = Integer32
_BatteryTemperatureMinorHighLevel_Object = MibTableColumn
batteryTemperatureMinorHighLevel = _BatteryTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 8),
    _BatteryTemperatureMinorHighLevel_Type()
)
batteryTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureMinorHighLevel.setStatus("current")
_BatteryTemperatureMinorLowLevel_Type = Integer32
_BatteryTemperatureMinorLowLevel_Object = MibTableColumn
batteryTemperatureMinorLowLevel = _BatteryTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 9),
    _BatteryTemperatureMinorLowLevel_Type()
)
batteryTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureMinorLowLevel.setStatus("current")
_BatteryTemperatureMajorLowLevel_Type = Integer32
_BatteryTemperatureMajorLowLevel_Object = MibTableColumn
batteryTemperatureMajorLowLevel = _BatteryTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 3, 1, 10),
    _BatteryTemperatureMajorLowLevel_Type()
)
batteryTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryTemperatureMajorLowLevel.setStatus("current")
_BatteryBankCurrentTable_Object = MibTable
batteryBankCurrentTable = _BatteryBankCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4)
)
if mibBuilder.loadTexts:
    batteryBankCurrentTable.setStatus("current")
_BatteryBankCurrentEntry_Object = MibTableRow
batteryBankCurrentEntry = _BatteryBankCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1)
)
batteryBankCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
    (0, "SP2-MIB", "batteryCurrentIndex"),
)
if mibBuilder.loadTexts:
    batteryBankCurrentEntry.setStatus("current")


class _BatteryCurrentIndex_Type(Integer32):
    """Custom type batteryCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryCurrentIndex_Type.__name__ = "Integer32"
_BatteryCurrentIndex_Object = MibTableColumn
batteryCurrentIndex = _BatteryCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 1),
    _BatteryCurrentIndex_Type()
)
batteryCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryCurrentIndex.setStatus("current")


class _BatteryCurrentStatus_Type(Integer32):
    """Custom type batteryCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryCurrentStatus_Type.__name__ = "Integer32"
_BatteryCurrentStatus_Object = MibTableColumn
batteryCurrentStatus = _BatteryCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 2),
    _BatteryCurrentStatus_Type()
)
batteryCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentStatus.setStatus("current")


class _BatteryCurrentDescription_Type(DisplayString):
    """Custom type batteryCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryCurrentDescription_Type.__name__ = "DisplayString"
_BatteryCurrentDescription_Object = MibTableColumn
batteryCurrentDescription = _BatteryCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 3),
    _BatteryCurrentDescription_Type()
)
batteryCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentDescription.setStatus("current")
_BatteryCurrentTrapRepeatCounter_Type = Counter32
_BatteryCurrentTrapRepeatCounter_Object = MibTableColumn
batteryCurrentTrapRepeatCounter = _BatteryCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 4),
    _BatteryCurrentTrapRepeatCounter_Type()
)
batteryCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryCurrentTrapRepeatCounter.setStatus("current")


class _BatteryCurrentAlarmEnable_Type(Integer32):
    """Custom type batteryCurrentAlarmEnable based on Integer32"""
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


_BatteryCurrentAlarmEnable_Type.__name__ = "Integer32"
_BatteryCurrentAlarmEnable_Object = MibTableColumn
batteryCurrentAlarmEnable = _BatteryCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 5),
    _BatteryCurrentAlarmEnable_Type()
)
batteryCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentAlarmEnable.setStatus("current")
_BatteryCurrentValue_Type = Integer32
_BatteryCurrentValue_Object = MibTableColumn
batteryCurrentValue = _BatteryCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 6),
    _BatteryCurrentValue_Type()
)
batteryCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCurrentValue.setStatus("current")
_BatteryCurrentMajorHighLevel_Type = Integer32
_BatteryCurrentMajorHighLevel_Object = MibTableColumn
batteryCurrentMajorHighLevel = _BatteryCurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 7),
    _BatteryCurrentMajorHighLevel_Type()
)
batteryCurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentMajorHighLevel.setStatus("current")
_BatteryCurrentMinorHighLevel_Type = Integer32
_BatteryCurrentMinorHighLevel_Object = MibTableColumn
batteryCurrentMinorHighLevel = _BatteryCurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 8),
    _BatteryCurrentMinorHighLevel_Type()
)
batteryCurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentMinorHighLevel.setStatus("current")
_BatteryCurrentMinorLowLevel_Type = Integer32
_BatteryCurrentMinorLowLevel_Object = MibTableColumn
batteryCurrentMinorLowLevel = _BatteryCurrentMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 9),
    _BatteryCurrentMinorLowLevel_Type()
)
batteryCurrentMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentMinorLowLevel.setStatus("current")
_BatteryCurrentMajorLowLevel_Type = Integer32
_BatteryCurrentMajorLowLevel_Object = MibTableColumn
batteryCurrentMajorLowLevel = _BatteryCurrentMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 4, 1, 10),
    _BatteryCurrentMajorLowLevel_Type()
)
batteryCurrentMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryCurrentMajorLowLevel.setStatus("current")
_BatteryBankFuseTable_Object = MibTable
batteryBankFuseTable = _BatteryBankFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5)
)
if mibBuilder.loadTexts:
    batteryBankFuseTable.setStatus("current")
_BatteryBankFuseEntry_Object = MibTableRow
batteryBankFuseEntry = _BatteryBankFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1)
)
batteryBankFuseEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
    (0, "SP2-MIB", "batteryFuseIndex"),
)
if mibBuilder.loadTexts:
    batteryBankFuseEntry.setStatus("current")


class _BatteryFuseIndex_Type(Integer32):
    """Custom type batteryFuseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryFuseIndex_Type.__name__ = "Integer32"
_BatteryFuseIndex_Object = MibTableColumn
batteryFuseIndex = _BatteryFuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 1),
    _BatteryFuseIndex_Type()
)
batteryFuseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryFuseIndex.setStatus("current")


class _BatteryFuseStatus_Type(Integer32):
    """Custom type batteryFuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryFuseStatus_Type.__name__ = "Integer32"
_BatteryFuseStatus_Object = MibTableColumn
batteryFuseStatus = _BatteryFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 2),
    _BatteryFuseStatus_Type()
)
batteryFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFuseStatus.setStatus("current")


class _BatteryFuseDescription_Type(DisplayString):
    """Custom type batteryFuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryFuseDescription_Type.__name__ = "DisplayString"
_BatteryFuseDescription_Object = MibTableColumn
batteryFuseDescription = _BatteryFuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 3),
    _BatteryFuseDescription_Type()
)
batteryFuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryFuseDescription.setStatus("current")
_BatteryFuseTrapRepeatCounter_Type = Counter32
_BatteryFuseTrapRepeatCounter_Object = MibTableColumn
batteryFuseTrapRepeatCounter = _BatteryFuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 4),
    _BatteryFuseTrapRepeatCounter_Type()
)
batteryFuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryFuseTrapRepeatCounter.setStatus("current")


class _BatteryFuseAlarmEnable_Type(Integer32):
    """Custom type batteryFuseAlarmEnable based on Integer32"""
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


_BatteryFuseAlarmEnable_Type.__name__ = "Integer32"
_BatteryFuseAlarmEnable_Object = MibTableColumn
batteryFuseAlarmEnable = _BatteryFuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 5),
    _BatteryFuseAlarmEnable_Type()
)
batteryFuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryFuseAlarmEnable.setStatus("current")
_BatteryFuseValue_Type = Integer32
_BatteryFuseValue_Object = MibTableColumn
batteryFuseValue = _BatteryFuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 5, 1, 6),
    _BatteryFuseValue_Type()
)
batteryFuseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryFuseValue.setStatus("current")
_BatteryBankSymmetryTable_Object = MibTable
batteryBankSymmetryTable = _BatteryBankSymmetryTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6)
)
if mibBuilder.loadTexts:
    batteryBankSymmetryTable.setStatus("current")
_BatteryBankSymmetryEntry_Object = MibTableRow
batteryBankSymmetryEntry = _BatteryBankSymmetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1)
)
batteryBankSymmetryEntry.setIndexNames(
    (0, "SP2-MIB", "batteryBankIndex"),
    (0, "SP2-MIB", "batteryBankSymmetryIndex"),
)
if mibBuilder.loadTexts:
    batteryBankSymmetryEntry.setStatus("current")


class _BatteryBankSymmetryIndex_Type(Integer32):
    """Custom type batteryBankSymmetryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryBankSymmetryIndex_Type.__name__ = "Integer32"
_BatteryBankSymmetryIndex_Object = MibTableColumn
batteryBankSymmetryIndex = _BatteryBankSymmetryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 1),
    _BatteryBankSymmetryIndex_Type()
)
batteryBankSymmetryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryBankSymmetryIndex.setStatus("current")


class _BatteryBankSymmetryStatus_Type(Integer32):
    """Custom type batteryBankSymmetryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryBankSymmetryStatus_Type.__name__ = "Integer32"
_BatteryBankSymmetryStatus_Object = MibTableColumn
batteryBankSymmetryStatus = _BatteryBankSymmetryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 2),
    _BatteryBankSymmetryStatus_Type()
)
batteryBankSymmetryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankSymmetryStatus.setStatus("current")


class _BatteryBankSymmetryDescription_Type(DisplayString):
    """Custom type batteryBankSymmetryDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryBankSymmetryDescription_Type.__name__ = "DisplayString"
_BatteryBankSymmetryDescription_Object = MibTableColumn
batteryBankSymmetryDescription = _BatteryBankSymmetryDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 3),
    _BatteryBankSymmetryDescription_Type()
)
batteryBankSymmetryDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBankSymmetryDescription.setStatus("current")
_BatteryBankSymmetryTrapRepeatCounter_Type = Counter32
_BatteryBankSymmetryTrapRepeatCounter_Object = MibTableColumn
batteryBankSymmetryTrapRepeatCounter = _BatteryBankSymmetryTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 4),
    _BatteryBankSymmetryTrapRepeatCounter_Type()
)
batteryBankSymmetryTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryBankSymmetryTrapRepeatCounter.setStatus("current")


class _BatteryBankSymmetryAlarmEnable_Type(Integer32):
    """Custom type batteryBankSymmetryAlarmEnable based on Integer32"""
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


_BatteryBankSymmetryAlarmEnable_Type.__name__ = "Integer32"
_BatteryBankSymmetryAlarmEnable_Object = MibTableColumn
batteryBankSymmetryAlarmEnable = _BatteryBankSymmetryAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 5),
    _BatteryBankSymmetryAlarmEnable_Type()
)
batteryBankSymmetryAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBankSymmetryAlarmEnable.setStatus("current")
_BatteryBankSymmetryMeasureValue_Type = Integer32
_BatteryBankSymmetryMeasureValue_Object = MibTableColumn
batteryBankSymmetryMeasureValue = _BatteryBankSymmetryMeasureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 6),
    _BatteryBankSymmetryMeasureValue_Type()
)
batteryBankSymmetryMeasureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankSymmetryMeasureValue.setStatus("current")
_BatteryBankSymmetryDeltaValue_Type = Integer32
_BatteryBankSymmetryDeltaValue_Object = MibTableColumn
batteryBankSymmetryDeltaValue = _BatteryBankSymmetryDeltaValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 7),
    _BatteryBankSymmetryDeltaValue_Type()
)
batteryBankSymmetryDeltaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryBankSymmetryDeltaValue.setStatus("current")
_BatteryBankSymmetryMajorAlarmLevel_Type = Integer32
_BatteryBankSymmetryMajorAlarmLevel_Object = MibTableColumn
batteryBankSymmetryMajorAlarmLevel = _BatteryBankSymmetryMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 8),
    _BatteryBankSymmetryMajorAlarmLevel_Type()
)
batteryBankSymmetryMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBankSymmetryMajorAlarmLevel.setStatus("current")
_BatteryBankSymmetryMinorAlarmLevel_Type = Integer32
_BatteryBankSymmetryMinorAlarmLevel_Object = MibTableColumn
batteryBankSymmetryMinorAlarmLevel = _BatteryBankSymmetryMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 18, 6, 1, 9),
    _BatteryBankSymmetryMinorAlarmLevel_Type()
)
batteryBankSymmetryMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryBankSymmetryMinorAlarmLevel.setStatus("current")
_BatteryMonitors_ObjectIdentity = ObjectIdentity
batteryMonitors = _BatteryMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19)
)
_BatteryMonitorsNumberOfUnits_Type = Integer32
_BatteryMonitorsNumberOfUnits_Object = MibScalar
batteryMonitorsNumberOfUnits = _BatteryMonitorsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 1),
    _BatteryMonitorsNumberOfUnits_Type()
)
batteryMonitorsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorsNumberOfUnits.setStatus("current")
_BatteryMonitorsTable_Object = MibTable
batteryMonitorsTable = _BatteryMonitorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2)
)
if mibBuilder.loadTexts:
    batteryMonitorsTable.setStatus("current")
_BatteryMonitorsEntry_Object = MibTableRow
batteryMonitorsEntry = _BatteryMonitorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1)
)
batteryMonitorsEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorsEntry.setStatus("current")


class _BatteryMonitorIndex_Type(Integer32):
    """Custom type batteryMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryMonitorIndex_Type.__name__ = "Integer32"
_BatteryMonitorIndex_Object = MibTableColumn
batteryMonitorIndex = _BatteryMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 1),
    _BatteryMonitorIndex_Type()
)
batteryMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorIndex.setStatus("current")


class _BatteryMonitorNumberOfTemperatures_Type(Integer32):
    """Custom type batteryMonitorNumberOfTemperatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryMonitorNumberOfTemperatures_Type.__name__ = "Integer32"
_BatteryMonitorNumberOfTemperatures_Object = MibTableColumn
batteryMonitorNumberOfTemperatures = _BatteryMonitorNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 2),
    _BatteryMonitorNumberOfTemperatures_Type()
)
batteryMonitorNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorNumberOfTemperatures.setStatus("current")


class _BatteryMonitorNumberOfCurrents_Type(Integer32):
    """Custom type batteryMonitorNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryMonitorNumberOfCurrents_Type.__name__ = "Integer32"
_BatteryMonitorNumberOfCurrents_Object = MibTableColumn
batteryMonitorNumberOfCurrents = _BatteryMonitorNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 3),
    _BatteryMonitorNumberOfCurrents_Type()
)
batteryMonitorNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorNumberOfCurrents.setStatus("current")


class _BatteryMonitorNumberOfFuses_Type(Integer32):
    """Custom type batteryMonitorNumberOfFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryMonitorNumberOfFuses_Type.__name__ = "Integer32"
_BatteryMonitorNumberOfFuses_Object = MibTableColumn
batteryMonitorNumberOfFuses = _BatteryMonitorNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 4),
    _BatteryMonitorNumberOfFuses_Type()
)
batteryMonitorNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorNumberOfFuses.setStatus("current")


class _BatteryMonitorNumberOfSymmetries_Type(Integer32):
    """Custom type batteryMonitorNumberOfSymmetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_BatteryMonitorNumberOfSymmetries_Type.__name__ = "Integer32"
_BatteryMonitorNumberOfSymmetries_Object = MibTableColumn
batteryMonitorNumberOfSymmetries = _BatteryMonitorNumberOfSymmetries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 2, 1, 5),
    _BatteryMonitorNumberOfSymmetries_Type()
)
batteryMonitorNumberOfSymmetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorNumberOfSymmetries.setStatus("current")
_BatteryMonitorTemperatureTable_Object = MibTable
batteryMonitorTemperatureTable = _BatteryMonitorTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3)
)
if mibBuilder.loadTexts:
    batteryMonitorTemperatureTable.setStatus("current")
_BatteryMonitorTemperatureEntry_Object = MibTableRow
batteryMonitorTemperatureEntry = _BatteryMonitorTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1)
)
batteryMonitorTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
    (0, "SP2-MIB", "batteryMonitorTemperatureIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorTemperatureEntry.setStatus("current")


class _BatteryMonitorTemperatureIndex_Type(Integer32):
    """Custom type batteryMonitorTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryMonitorTemperatureIndex_Type.__name__ = "Integer32"
_BatteryMonitorTemperatureIndex_Object = MibTableColumn
batteryMonitorTemperatureIndex = _BatteryMonitorTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 1),
    _BatteryMonitorTemperatureIndex_Type()
)
batteryMonitorTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureIndex.setStatus("current")


class _BatteryMonitorTemperatureStatus_Type(Integer32):
    """Custom type batteryMonitorTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryMonitorTemperatureStatus_Type.__name__ = "Integer32"
_BatteryMonitorTemperatureStatus_Object = MibTableColumn
batteryMonitorTemperatureStatus = _BatteryMonitorTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 2),
    _BatteryMonitorTemperatureStatus_Type()
)
batteryMonitorTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureStatus.setStatus("current")


class _BatteryMonitorTemperatureDescription_Type(DisplayString):
    """Custom type batteryMonitorTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorTemperatureDescription_Type.__name__ = "DisplayString"
_BatteryMonitorTemperatureDescription_Object = MibTableColumn
batteryMonitorTemperatureDescription = _BatteryMonitorTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 3),
    _BatteryMonitorTemperatureDescription_Type()
)
batteryMonitorTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureDescription.setStatus("current")
_BatteryMonitorTemperatureTrapRepeatCounter_Type = Counter32
_BatteryMonitorTemperatureTrapRepeatCounter_Object = MibTableColumn
batteryMonitorTemperatureTrapRepeatCounter = _BatteryMonitorTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 4),
    _BatteryMonitorTemperatureTrapRepeatCounter_Type()
)
batteryMonitorTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureTrapRepeatCounter.setStatus("current")


class _BatteryMonitorTemperatureAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorTemperatureAlarmEnable based on Integer32"""
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


_BatteryMonitorTemperatureAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorTemperatureAlarmEnable_Object = MibTableColumn
batteryMonitorTemperatureAlarmEnable = _BatteryMonitorTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 5),
    _BatteryMonitorTemperatureAlarmEnable_Type()
)
batteryMonitorTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureAlarmEnable.setStatus("current")
_BatteryMonitorTemperatureValue_Type = Integer32
_BatteryMonitorTemperatureValue_Object = MibTableColumn
batteryMonitorTemperatureValue = _BatteryMonitorTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 6),
    _BatteryMonitorTemperatureValue_Type()
)
batteryMonitorTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureValue.setStatus("current")
_BatteryMonitorTemperatureMajorHighLevel_Type = Integer32
_BatteryMonitorTemperatureMajorHighLevel_Object = MibTableColumn
batteryMonitorTemperatureMajorHighLevel = _BatteryMonitorTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 7),
    _BatteryMonitorTemperatureMajorHighLevel_Type()
)
batteryMonitorTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureMajorHighLevel.setStatus("current")
_BatteryMonitorTemperatureMinorHighLevel_Type = Integer32
_BatteryMonitorTemperatureMinorHighLevel_Object = MibTableColumn
batteryMonitorTemperatureMinorHighLevel = _BatteryMonitorTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 8),
    _BatteryMonitorTemperatureMinorHighLevel_Type()
)
batteryMonitorTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureMinorHighLevel.setStatus("current")
_BatteryMonitorTemperatureMinorLowLevel_Type = Integer32
_BatteryMonitorTemperatureMinorLowLevel_Object = MibTableColumn
batteryMonitorTemperatureMinorLowLevel = _BatteryMonitorTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 9),
    _BatteryMonitorTemperatureMinorLowLevel_Type()
)
batteryMonitorTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureMinorLowLevel.setStatus("current")
_BatteryMonitorTemperatureMajorLowLevel_Type = Integer32
_BatteryMonitorTemperatureMajorLowLevel_Object = MibTableColumn
batteryMonitorTemperatureMajorLowLevel = _BatteryMonitorTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 3, 1, 10),
    _BatteryMonitorTemperatureMajorLowLevel_Type()
)
batteryMonitorTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorTemperatureMajorLowLevel.setStatus("current")
_BatteryMonitorCurrentTable_Object = MibTable
batteryMonitorCurrentTable = _BatteryMonitorCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4)
)
if mibBuilder.loadTexts:
    batteryMonitorCurrentTable.setStatus("current")
_BatteryMonitorCurrentEntry_Object = MibTableRow
batteryMonitorCurrentEntry = _BatteryMonitorCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1)
)
batteryMonitorCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
    (0, "SP2-MIB", "batteryMonitorCurrentIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorCurrentEntry.setStatus("current")


class _BatteryMonitorCurrentIndex_Type(Integer32):
    """Custom type batteryMonitorCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryMonitorCurrentIndex_Type.__name__ = "Integer32"
_BatteryMonitorCurrentIndex_Object = MibTableColumn
batteryMonitorCurrentIndex = _BatteryMonitorCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 1),
    _BatteryMonitorCurrentIndex_Type()
)
batteryMonitorCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorCurrentIndex.setStatus("current")


class _BatteryMonitorCurrentStatus_Type(Integer32):
    """Custom type batteryMonitorCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryMonitorCurrentStatus_Type.__name__ = "Integer32"
_BatteryMonitorCurrentStatus_Object = MibTableColumn
batteryMonitorCurrentStatus = _BatteryMonitorCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 2),
    _BatteryMonitorCurrentStatus_Type()
)
batteryMonitorCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorCurrentStatus.setStatus("current")


class _BatteryMonitorCurrentDescription_Type(DisplayString):
    """Custom type batteryMonitorCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorCurrentDescription_Type.__name__ = "DisplayString"
_BatteryMonitorCurrentDescription_Object = MibTableColumn
batteryMonitorCurrentDescription = _BatteryMonitorCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 3),
    _BatteryMonitorCurrentDescription_Type()
)
batteryMonitorCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentDescription.setStatus("current")
_BatteryMonitorCurrentTrapRepeatCounter_Type = Counter32
_BatteryMonitorCurrentTrapRepeatCounter_Object = MibTableColumn
batteryMonitorCurrentTrapRepeatCounter = _BatteryMonitorCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 4),
    _BatteryMonitorCurrentTrapRepeatCounter_Type()
)
batteryMonitorCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorCurrentTrapRepeatCounter.setStatus("current")


class _BatteryMonitorCurrentAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorCurrentAlarmEnable based on Integer32"""
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


_BatteryMonitorCurrentAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorCurrentAlarmEnable_Object = MibTableColumn
batteryMonitorCurrentAlarmEnable = _BatteryMonitorCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 5),
    _BatteryMonitorCurrentAlarmEnable_Type()
)
batteryMonitorCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentAlarmEnable.setStatus("current")
_BatteryMonitorCurrentValue_Type = Integer32
_BatteryMonitorCurrentValue_Object = MibTableColumn
batteryMonitorCurrentValue = _BatteryMonitorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 6),
    _BatteryMonitorCurrentValue_Type()
)
batteryMonitorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorCurrentValue.setStatus("current")
_BatteryMonitorCurrentMajorHighLevel_Type = Integer32
_BatteryMonitorCurrentMajorHighLevel_Object = MibTableColumn
batteryMonitorCurrentMajorHighLevel = _BatteryMonitorCurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 7),
    _BatteryMonitorCurrentMajorHighLevel_Type()
)
batteryMonitorCurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentMajorHighLevel.setStatus("current")
_BatteryMonitorCurrentMinorHighLevel_Type = Integer32
_BatteryMonitorCurrentMinorHighLevel_Object = MibTableColumn
batteryMonitorCurrentMinorHighLevel = _BatteryMonitorCurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 8),
    _BatteryMonitorCurrentMinorHighLevel_Type()
)
batteryMonitorCurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentMinorHighLevel.setStatus("current")
_BatteryMonitorCurrentMinorLowLevel_Type = Integer32
_BatteryMonitorCurrentMinorLowLevel_Object = MibTableColumn
batteryMonitorCurrentMinorLowLevel = _BatteryMonitorCurrentMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 9),
    _BatteryMonitorCurrentMinorLowLevel_Type()
)
batteryMonitorCurrentMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentMinorLowLevel.setStatus("current")
_BatteryMonitorCurrentMajorLowLevel_Type = Integer32
_BatteryMonitorCurrentMajorLowLevel_Object = MibTableColumn
batteryMonitorCurrentMajorLowLevel = _BatteryMonitorCurrentMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 4, 1, 10),
    _BatteryMonitorCurrentMajorLowLevel_Type()
)
batteryMonitorCurrentMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorCurrentMajorLowLevel.setStatus("current")
_BatteryMonitorFuseTable_Object = MibTable
batteryMonitorFuseTable = _BatteryMonitorFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5)
)
if mibBuilder.loadTexts:
    batteryMonitorFuseTable.setStatus("current")
_BatteryMonitorFuseEntry_Object = MibTableRow
batteryMonitorFuseEntry = _BatteryMonitorFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1)
)
batteryMonitorFuseEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
    (0, "SP2-MIB", "batteryMonitorFuseIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorFuseEntry.setStatus("current")


class _BatteryMonitorFuseIndex_Type(Integer32):
    """Custom type batteryMonitorFuseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryMonitorFuseIndex_Type.__name__ = "Integer32"
_BatteryMonitorFuseIndex_Object = MibTableColumn
batteryMonitorFuseIndex = _BatteryMonitorFuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 1),
    _BatteryMonitorFuseIndex_Type()
)
batteryMonitorFuseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorFuseIndex.setStatus("current")


class _BatteryMonitorFuseStatus_Type(Integer32):
    """Custom type batteryMonitorFuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryMonitorFuseStatus_Type.__name__ = "Integer32"
_BatteryMonitorFuseStatus_Object = MibTableColumn
batteryMonitorFuseStatus = _BatteryMonitorFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 2),
    _BatteryMonitorFuseStatus_Type()
)
batteryMonitorFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorFuseStatus.setStatus("current")


class _BatteryMonitorFuseDescription_Type(DisplayString):
    """Custom type batteryMonitorFuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorFuseDescription_Type.__name__ = "DisplayString"
_BatteryMonitorFuseDescription_Object = MibTableColumn
batteryMonitorFuseDescription = _BatteryMonitorFuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 3),
    _BatteryMonitorFuseDescription_Type()
)
batteryMonitorFuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorFuseDescription.setStatus("current")
_BatteryMonitorFuseTrapRepeatCounter_Type = Counter32
_BatteryMonitorFuseTrapRepeatCounter_Object = MibTableColumn
batteryMonitorFuseTrapRepeatCounter = _BatteryMonitorFuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 4),
    _BatteryMonitorFuseTrapRepeatCounter_Type()
)
batteryMonitorFuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorFuseTrapRepeatCounter.setStatus("current")


class _BatteryMonitorFuseAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorFuseAlarmEnable based on Integer32"""
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


_BatteryMonitorFuseAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorFuseAlarmEnable_Object = MibTableColumn
batteryMonitorFuseAlarmEnable = _BatteryMonitorFuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 5),
    _BatteryMonitorFuseAlarmEnable_Type()
)
batteryMonitorFuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorFuseAlarmEnable.setStatus("current")
_BatteryMonitorFuseValue_Type = Integer32
_BatteryMonitorFuseValue_Object = MibTableColumn
batteryMonitorFuseValue = _BatteryMonitorFuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 5, 1, 6),
    _BatteryMonitorFuseValue_Type()
)
batteryMonitorFuseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorFuseValue.setStatus("current")
_BatteryMonitorSymmetryTable_Object = MibTable
batteryMonitorSymmetryTable = _BatteryMonitorSymmetryTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6)
)
if mibBuilder.loadTexts:
    batteryMonitorSymmetryTable.setStatus("current")
_BatteryMonitorSymmetryEntry_Object = MibTableRow
batteryMonitorSymmetryEntry = _BatteryMonitorSymmetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1)
)
batteryMonitorSymmetryEntry.setIndexNames(
    (0, "SP2-MIB", "batteryMonitorIndex"),
    (0, "SP2-MIB", "batteryMonitorSymmetryIndex"),
)
if mibBuilder.loadTexts:
    batteryMonitorSymmetryEntry.setStatus("current")


class _BatteryMonitorSymmetryIndex_Type(Integer32):
    """Custom type batteryMonitorSymmetryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryMonitorSymmetryIndex_Type.__name__ = "Integer32"
_BatteryMonitorSymmetryIndex_Object = MibTableColumn
batteryMonitorSymmetryIndex = _BatteryMonitorSymmetryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 1),
    _BatteryMonitorSymmetryIndex_Type()
)
batteryMonitorSymmetryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryIndex.setStatus("current")


class _BatteryMonitorSymmetryStatus_Type(Integer32):
    """Custom type batteryMonitorSymmetryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryMonitorSymmetryStatus_Type.__name__ = "Integer32"
_BatteryMonitorSymmetryStatus_Object = MibTableColumn
batteryMonitorSymmetryStatus = _BatteryMonitorSymmetryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 2),
    _BatteryMonitorSymmetryStatus_Type()
)
batteryMonitorSymmetryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryStatus.setStatus("current")


class _BatteryMonitorSymmetryDescription_Type(DisplayString):
    """Custom type batteryMonitorSymmetryDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorSymmetryDescription_Type.__name__ = "DisplayString"
_BatteryMonitorSymmetryDescription_Object = MibTableColumn
batteryMonitorSymmetryDescription = _BatteryMonitorSymmetryDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 3),
    _BatteryMonitorSymmetryDescription_Type()
)
batteryMonitorSymmetryDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryDescription.setStatus("current")
_BatteryMonitorSymmetryTrapRepeatCounter_Type = Counter32
_BatteryMonitorSymmetryTrapRepeatCounter_Object = MibTableColumn
batteryMonitorSymmetryTrapRepeatCounter = _BatteryMonitorSymmetryTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 4),
    _BatteryMonitorSymmetryTrapRepeatCounter_Type()
)
batteryMonitorSymmetryTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryTrapRepeatCounter.setStatus("current")


class _BatteryMonitorSymmetryAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorSymmetryAlarmEnable based on Integer32"""
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


_BatteryMonitorSymmetryAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorSymmetryAlarmEnable_Object = MibTableColumn
batteryMonitorSymmetryAlarmEnable = _BatteryMonitorSymmetryAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 5),
    _BatteryMonitorSymmetryAlarmEnable_Type()
)
batteryMonitorSymmetryAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryAlarmEnable.setStatus("current")
_BatteryMonitorSymmetryMeasureValue_Type = Integer32
_BatteryMonitorSymmetryMeasureValue_Object = MibTableColumn
batteryMonitorSymmetryMeasureValue = _BatteryMonitorSymmetryMeasureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 6),
    _BatteryMonitorSymmetryMeasureValue_Type()
)
batteryMonitorSymmetryMeasureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryMeasureValue.setStatus("current")
_BatteryMonitorSymmetryDeltaValue_Type = Integer32
_BatteryMonitorSymmetryDeltaValue_Object = MibTableColumn
batteryMonitorSymmetryDeltaValue = _BatteryMonitorSymmetryDeltaValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 7),
    _BatteryMonitorSymmetryDeltaValue_Type()
)
batteryMonitorSymmetryDeltaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryDeltaValue.setStatus("current")
_BatteryMonitorSymmetryMajorAlarmLevel_Type = Integer32
_BatteryMonitorSymmetryMajorAlarmLevel_Object = MibTableColumn
batteryMonitorSymmetryMajorAlarmLevel = _BatteryMonitorSymmetryMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 8),
    _BatteryMonitorSymmetryMajorAlarmLevel_Type()
)
batteryMonitorSymmetryMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryMajorAlarmLevel.setStatus("current")
_BatteryMonitorSymmetryMinorAlarmLevel_Type = Integer32
_BatteryMonitorSymmetryMinorAlarmLevel_Object = MibTableColumn
batteryMonitorSymmetryMinorAlarmLevel = _BatteryMonitorSymmetryMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 19, 6, 1, 9),
    _BatteryMonitorSymmetryMinorAlarmLevel_Type()
)
batteryMonitorSymmetryMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorSymmetryMinorAlarmLevel.setStatus("current")
_BatteryEnergyLog_ObjectIdentity = ObjectIdentity
batteryEnergyLog = _BatteryEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20)
)
_BatteryEnergyLogAccumulated_Type = Integer32
_BatteryEnergyLogAccumulated_Object = MibScalar
batteryEnergyLogAccumulated = _BatteryEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 1),
    _BatteryEnergyLogAccumulated_Type()
)
batteryEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogAccumulated.setStatus("current")


class _BatteryEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type batteryEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_BatteryEnergyLogLastHoursNumberOfEntries_Object = MibScalar
batteryEnergyLogLastHoursNumberOfEntries = _BatteryEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 2),
    _BatteryEnergyLogLastHoursNumberOfEntries_Type()
)
batteryEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursNumberOfEntries.setStatus("current")
_BatteryEnergyLogLastHoursTable_Object = MibTable
batteryEnergyLogLastHoursTable = _BatteryEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 3)
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursTable.setStatus("current")
_BatteryEnergyLogLastHoursEntry_Object = MibTableRow
batteryEnergyLogLastHoursEntry = _BatteryEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 3, 1)
)
batteryEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "batteryEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursEntry.setStatus("current")


class _BatteryEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type batteryEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_BatteryEnergyLogLastHoursIndex_Object = MibTableColumn
batteryEnergyLogLastHoursIndex = _BatteryEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 3, 1, 1),
    _BatteryEnergyLogLastHoursIndex_Type()
)
batteryEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursIndex.setStatus("current")
_BatteryEnergyLogLastHoursValue_Type = Integer32
_BatteryEnergyLogLastHoursValue_Object = MibTableColumn
batteryEnergyLogLastHoursValue = _BatteryEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 3, 1, 2),
    _BatteryEnergyLogLastHoursValue_Type()
)
batteryEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastHoursValue.setStatus("current")


class _BatteryEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type batteryEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_BatteryEnergyLogLastDaysNumberOfEntries_Object = MibScalar
batteryEnergyLogLastDaysNumberOfEntries = _BatteryEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 4),
    _BatteryEnergyLogLastDaysNumberOfEntries_Type()
)
batteryEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysNumberOfEntries.setStatus("current")
_BatteryEnergyLogLastDaysTable_Object = MibTable
batteryEnergyLogLastDaysTable = _BatteryEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 5)
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysTable.setStatus("current")
_BatteryEnergyLogLastDaysEntry_Object = MibTableRow
batteryEnergyLogLastDaysEntry = _BatteryEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 5, 1)
)
batteryEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "batteryEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysEntry.setStatus("current")


class _BatteryEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type batteryEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_BatteryEnergyLogLastDaysIndex_Object = MibTableColumn
batteryEnergyLogLastDaysIndex = _BatteryEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 5, 1, 1),
    _BatteryEnergyLogLastDaysIndex_Type()
)
batteryEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysIndex.setStatus("current")
_BatteryEnergyLogLastDaysValue_Type = Integer32
_BatteryEnergyLogLastDaysValue_Object = MibTableColumn
batteryEnergyLogLastDaysValue = _BatteryEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 5, 1, 2),
    _BatteryEnergyLogLastDaysValue_Type()
)
batteryEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastDaysValue.setStatus("current")


class _BatteryEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type batteryEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_BatteryEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
batteryEnergyLogLastWeeksNumberOfEntries = _BatteryEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 6),
    _BatteryEnergyLogLastWeeksNumberOfEntries_Type()
)
batteryEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_BatteryEnergyLogLastWeeksTable_Object = MibTable
batteryEnergyLogLastWeeksTable = _BatteryEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 7)
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksTable.setStatus("current")
_BatteryEnergyLogLastWeeksEntry_Object = MibTableRow
batteryEnergyLogLastWeeksEntry = _BatteryEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 7, 1)
)
batteryEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "batteryEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksEntry.setStatus("current")


class _BatteryEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type batteryEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_BatteryEnergyLogLastWeeksIndex_Object = MibTableColumn
batteryEnergyLogLastWeeksIndex = _BatteryEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 7, 1, 1),
    _BatteryEnergyLogLastWeeksIndex_Type()
)
batteryEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksIndex.setStatus("current")
_BatteryEnergyLogLastWeeksValue_Type = Integer32
_BatteryEnergyLogLastWeeksValue_Object = MibTableColumn
batteryEnergyLogLastWeeksValue = _BatteryEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 20, 7, 1, 2),
    _BatteryEnergyLogLastWeeksValue_Type()
)
batteryEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryEnergyLogLastWeeksValue.setStatus("current")
_BatteryCycleLog_ObjectIdentity = ObjectIdentity
batteryCycleLog = _BatteryCycleLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21)
)
_BatteryCycleLogTotalCycles_Type = Integer32
_BatteryCycleLogTotalCycles_Object = MibScalar
batteryCycleLogTotalCycles = _BatteryCycleLogTotalCycles_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 1),
    _BatteryCycleLogTotalCycles_Type()
)
batteryCycleLogTotalCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogTotalCycles.setStatus("current")


class _BatteryCycleLogDaysNumberOfEntries_Type(Integer32):
    """Custom type batteryCycleLogDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryCycleLogDaysNumberOfEntries_Type.__name__ = "Integer32"
_BatteryCycleLogDaysNumberOfEntries_Object = MibScalar
batteryCycleLogDaysNumberOfEntries = _BatteryCycleLogDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 2),
    _BatteryCycleLogDaysNumberOfEntries_Type()
)
batteryCycleLogDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogDaysNumberOfEntries.setStatus("current")
_BatteryCycleLogDaysTable_Object = MibTable
batteryCycleLogDaysTable = _BatteryCycleLogDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 3)
)
if mibBuilder.loadTexts:
    batteryCycleLogDaysTable.setStatus("current")
_BatteryCycleLogDaysEntry_Object = MibTableRow
batteryCycleLogDaysEntry = _BatteryCycleLogDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 3, 1)
)
batteryCycleLogDaysEntry.setIndexNames(
    (0, "SP2-MIB", "batteryCycleLogDaysIndex"),
)
if mibBuilder.loadTexts:
    batteryCycleLogDaysEntry.setStatus("current")


class _BatteryCycleLogDaysIndex_Type(Integer32):
    """Custom type batteryCycleLogDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryCycleLogDaysIndex_Type.__name__ = "Integer32"
_BatteryCycleLogDaysIndex_Object = MibTableColumn
batteryCycleLogDaysIndex = _BatteryCycleLogDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 3, 1, 1),
    _BatteryCycleLogDaysIndex_Type()
)
batteryCycleLogDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryCycleLogDaysIndex.setStatus("current")
_BatteryCycleLogDaysValue_Type = Integer32
_BatteryCycleLogDaysValue_Object = MibTableColumn
batteryCycleLogDaysValue = _BatteryCycleLogDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 3, 1, 2),
    _BatteryCycleLogDaysValue_Type()
)
batteryCycleLogDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogDaysValue.setStatus("current")


class _BatteryCycleLogWeeksNumberOfEntries_Type(Integer32):
    """Custom type batteryCycleLogWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryCycleLogWeeksNumberOfEntries_Type.__name__ = "Integer32"
_BatteryCycleLogWeeksNumberOfEntries_Object = MibScalar
batteryCycleLogWeeksNumberOfEntries = _BatteryCycleLogWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 4),
    _BatteryCycleLogWeeksNumberOfEntries_Type()
)
batteryCycleLogWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogWeeksNumberOfEntries.setStatus("current")
_BatteryCycleLogWeeksTable_Object = MibTable
batteryCycleLogWeeksTable = _BatteryCycleLogWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 5)
)
if mibBuilder.loadTexts:
    batteryCycleLogWeeksTable.setStatus("current")
_BatteryCycleLogWeeksEntry_Object = MibTableRow
batteryCycleLogWeeksEntry = _BatteryCycleLogWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 5, 1)
)
batteryCycleLogWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "batteryCycleLogWeeksIndex"),
)
if mibBuilder.loadTexts:
    batteryCycleLogWeeksEntry.setStatus("current")


class _BatteryCycleLogWeeksIndex_Type(Integer32):
    """Custom type batteryCycleLogWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryCycleLogWeeksIndex_Type.__name__ = "Integer32"
_BatteryCycleLogWeeksIndex_Object = MibTableColumn
batteryCycleLogWeeksIndex = _BatteryCycleLogWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 5, 1, 1),
    _BatteryCycleLogWeeksIndex_Type()
)
batteryCycleLogWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryCycleLogWeeksIndex.setStatus("current")
_BatteryCycleLogWeeksValue_Type = Integer32
_BatteryCycleLogWeeksValue_Object = MibTableColumn
batteryCycleLogWeeksValue = _BatteryCycleLogWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 5, 1, 2),
    _BatteryCycleLogWeeksValue_Type()
)
batteryCycleLogWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogWeeksValue.setStatus("current")


class _BatteryCycleLogMonthsNumberOfEntries_Type(Integer32):
    """Custom type batteryCycleLogMonthsNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryCycleLogMonthsNumberOfEntries_Type.__name__ = "Integer32"
_BatteryCycleLogMonthsNumberOfEntries_Object = MibScalar
batteryCycleLogMonthsNumberOfEntries = _BatteryCycleLogMonthsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 6),
    _BatteryCycleLogMonthsNumberOfEntries_Type()
)
batteryCycleLogMonthsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogMonthsNumberOfEntries.setStatus("current")
_BatteryCycleLogMonthsTable_Object = MibTable
batteryCycleLogMonthsTable = _BatteryCycleLogMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 7)
)
if mibBuilder.loadTexts:
    batteryCycleLogMonthsTable.setStatus("current")
_BatteryCycleLogMonthsEntry_Object = MibTableRow
batteryCycleLogMonthsEntry = _BatteryCycleLogMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 7, 1)
)
batteryCycleLogMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "batteryCycleLogMonthsIndex"),
)
if mibBuilder.loadTexts:
    batteryCycleLogMonthsEntry.setStatus("current")


class _BatteryCycleLogMonthsIndex_Type(Integer32):
    """Custom type batteryCycleLogMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryCycleLogMonthsIndex_Type.__name__ = "Integer32"
_BatteryCycleLogMonthsIndex_Object = MibTableColumn
batteryCycleLogMonthsIndex = _BatteryCycleLogMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 7, 1, 1),
    _BatteryCycleLogMonthsIndex_Type()
)
batteryCycleLogMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryCycleLogMonthsIndex.setStatus("current")
_BatteryCycleLogMonthsValue_Type = Integer32
_BatteryCycleLogMonthsValue_Object = MibTableColumn
batteryCycleLogMonthsValue = _BatteryCycleLogMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 21, 7, 1, 2),
    _BatteryCycleLogMonthsValue_Type()
)
batteryCycleLogMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryCycleLogMonthsValue.setStatus("current")
_BatteryEqualize_ObjectIdentity = ObjectIdentity
batteryEqualize = _BatteryEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 22)
)


class _BatteryEqualizeVoltage_Type(Integer32):
    """Custom type batteryEqualizeVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(870, 60418),
    )


_BatteryEqualizeVoltage_Type.__name__ = "Integer32"
_BatteryEqualizeVoltage_Object = MibScalar
batteryEqualizeVoltage = _BatteryEqualizeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 22, 1),
    _BatteryEqualizeVoltage_Type()
)
batteryEqualizeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryEqualizeVoltage.setStatus("current")


class _BatteryEqualizeCommand_Type(Integer32):
    """Custom type batteryEqualizeCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("startequalize", 1),
          ("stopequalize", 2))
    )


_BatteryEqualizeCommand_Type.__name__ = "Integer32"
_BatteryEqualizeCommand_Object = MibScalar
batteryEqualizeCommand = _BatteryEqualizeCommand_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 22, 2),
    _BatteryEqualizeCommand_Type()
)
batteryEqualizeCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryEqualizeCommand.setStatus("current")
_BatteryEqualizeCurrentThreshold_Type = Integer32
_BatteryEqualizeCurrentThreshold_Object = MibScalar
batteryEqualizeCurrentThreshold = _BatteryEqualizeCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 22, 3),
    _BatteryEqualizeCurrentThreshold_Type()
)
batteryEqualizeCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryEqualizeCurrentThreshold.setStatus("current")


class _BatteryEqualizeManualMaxDuration_Type(Integer32):
    """Custom type batteryEqualizeManualMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_BatteryEqualizeManualMaxDuration_Type.__name__ = "Integer32"
_BatteryEqualizeManualMaxDuration_Object = MibScalar
batteryEqualizeManualMaxDuration = _BatteryEqualizeManualMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 22, 4),
    _BatteryEqualizeManualMaxDuration_Type()
)
batteryEqualizeManualMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryEqualizeManualMaxDuration.setStatus("current")
_BatteryAhCharged_ObjectIdentity = ObjectIdentity
batteryAhCharged = _BatteryAhCharged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 23)
)


class _BatteryAhChargedStatus_Type(Integer32):
    """Custom type batteryAhChargedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryAhChargedStatus_Type.__name__ = "Integer32"
_BatteryAhChargedStatus_Object = MibScalar
batteryAhChargedStatus = _BatteryAhChargedStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 23, 1),
    _BatteryAhChargedStatus_Type()
)
batteryAhChargedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryAhChargedStatus.setStatus("current")


class _BatteryAhChargedDescription_Type(DisplayString):
    """Custom type batteryAhChargedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryAhChargedDescription_Type.__name__ = "DisplayString"
_BatteryAhChargedDescription_Object = MibScalar
batteryAhChargedDescription = _BatteryAhChargedDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 23, 2),
    _BatteryAhChargedDescription_Type()
)
batteryAhChargedDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAhChargedDescription.setStatus("current")
_BatteryAhChargedTrapRepeatCounter_Type = Counter32
_BatteryAhChargedTrapRepeatCounter_Object = MibScalar
batteryAhChargedTrapRepeatCounter = _BatteryAhChargedTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 23, 3),
    _BatteryAhChargedTrapRepeatCounter_Type()
)
batteryAhChargedTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryAhChargedTrapRepeatCounter.setStatus("current")


class _BatteryAhChargedAlarmEnable_Type(Integer32):
    """Custom type batteryAhChargedAlarmEnable based on Integer32"""
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


_BatteryAhChargedAlarmEnable_Type.__name__ = "Integer32"
_BatteryAhChargedAlarmEnable_Object = MibScalar
batteryAhChargedAlarmEnable = _BatteryAhChargedAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 23, 4),
    _BatteryAhChargedAlarmEnable_Type()
)
batteryAhChargedAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAhChargedAlarmEnable.setStatus("current")
_BatteryAhChargedValue_Type = Integer32
_BatteryAhChargedValue_Object = MibScalar
batteryAhChargedValue = _BatteryAhChargedValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 23, 5),
    _BatteryAhChargedValue_Type()
)
batteryAhChargedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryAhChargedValue.setStatus("current")
_BatteryAhChargedMinorHighLevel_Type = Integer32
_BatteryAhChargedMinorHighLevel_Object = MibScalar
batteryAhChargedMinorHighLevel = _BatteryAhChargedMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 23, 6),
    _BatteryAhChargedMinorHighLevel_Type()
)
batteryAhChargedMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAhChargedMinorHighLevel.setStatus("current")
_BatteryAhChargedMajorHighLevel_Type = Integer32
_BatteryAhChargedMajorHighLevel_Object = MibScalar
batteryAhChargedMajorHighLevel = _BatteryAhChargedMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 23, 7),
    _BatteryAhChargedMajorHighLevel_Type()
)
batteryAhChargedMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAhChargedMajorHighLevel.setStatus("current")
_BatteryAhDischarged_ObjectIdentity = ObjectIdentity
batteryAhDischarged = _BatteryAhDischarged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 24)
)


class _BatteryAhDischargedStatus_Type(Integer32):
    """Custom type batteryAhDischargedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryAhDischargedStatus_Type.__name__ = "Integer32"
_BatteryAhDischargedStatus_Object = MibScalar
batteryAhDischargedStatus = _BatteryAhDischargedStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 24, 1),
    _BatteryAhDischargedStatus_Type()
)
batteryAhDischargedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryAhDischargedStatus.setStatus("current")


class _BatteryAhDischargedDescription_Type(DisplayString):
    """Custom type batteryAhDischargedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryAhDischargedDescription_Type.__name__ = "DisplayString"
_BatteryAhDischargedDescription_Object = MibScalar
batteryAhDischargedDescription = _BatteryAhDischargedDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 24, 2),
    _BatteryAhDischargedDescription_Type()
)
batteryAhDischargedDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAhDischargedDescription.setStatus("current")
_BatteryAhDischargedTrapRepeatCounter_Type = Counter32
_BatteryAhDischargedTrapRepeatCounter_Object = MibScalar
batteryAhDischargedTrapRepeatCounter = _BatteryAhDischargedTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 24, 3),
    _BatteryAhDischargedTrapRepeatCounter_Type()
)
batteryAhDischargedTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryAhDischargedTrapRepeatCounter.setStatus("current")


class _BatteryAhDischargedAlarmEnable_Type(Integer32):
    """Custom type batteryAhDischargedAlarmEnable based on Integer32"""
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


_BatteryAhDischargedAlarmEnable_Type.__name__ = "Integer32"
_BatteryAhDischargedAlarmEnable_Object = MibScalar
batteryAhDischargedAlarmEnable = _BatteryAhDischargedAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 24, 4),
    _BatteryAhDischargedAlarmEnable_Type()
)
batteryAhDischargedAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAhDischargedAlarmEnable.setStatus("current")
_BatteryAhDischargedValue_Type = Integer32
_BatteryAhDischargedValue_Object = MibScalar
batteryAhDischargedValue = _BatteryAhDischargedValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 24, 5),
    _BatteryAhDischargedValue_Type()
)
batteryAhDischargedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryAhDischargedValue.setStatus("current")
_BatteryAhDischargedMinorHighLevel_Type = Integer32
_BatteryAhDischargedMinorHighLevel_Object = MibScalar
batteryAhDischargedMinorHighLevel = _BatteryAhDischargedMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 24, 6),
    _BatteryAhDischargedMinorHighLevel_Type()
)
batteryAhDischargedMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAhDischargedMinorHighLevel.setStatus("current")
_BatteryAhDischargedMajorHighLevel_Type = Integer32
_BatteryAhDischargedMajorHighLevel_Object = MibScalar
batteryAhDischargedMajorHighLevel = _BatteryAhDischargedMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 10, 24, 7),
    _BatteryAhDischargedMajorHighLevel_Type()
)
batteryAhDischargedMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryAhDischargedMajorHighLevel.setStatus("current")
_Inputs_ObjectIdentity = ObjectIdentity
inputs = _Inputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11)
)
_InputControlUnitsTable_Object = MibTable
inputControlUnitsTable = _InputControlUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 1)
)
if mibBuilder.loadTexts:
    inputControlUnitsTable.setStatus("current")
_InputControlUnitsEntry_Object = MibTableRow
inputControlUnitsEntry = _InputControlUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 1, 1)
)
inputControlUnitsEntry.setIndexNames(
    (0, "SP2-MIB", "inputControlUnitIndex"),
)
if mibBuilder.loadTexts:
    inputControlUnitsEntry.setStatus("current")


class _InputControlUnitIndex_Type(Integer32):
    """Custom type inputControlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_InputControlUnitIndex_Type.__name__ = "Integer32"
_InputControlUnitIndex_Object = MibTableColumn
inputControlUnitIndex = _InputControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 1, 1, 1),
    _InputControlUnitIndex_Type()
)
inputControlUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputControlUnitIndex.setStatus("current")


class _InputControlUnitNumberOfInputs_Type(Integer32):
    """Custom type inputControlUnitNumberOfInputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_InputControlUnitNumberOfInputs_Type.__name__ = "Integer32"
_InputControlUnitNumberOfInputs_Object = MibTableColumn
inputControlUnitNumberOfInputs = _InputControlUnitNumberOfInputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 1, 1, 2),
    _InputControlUnitNumberOfInputs_Type()
)
inputControlUnitNumberOfInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputControlUnitNumberOfInputs.setStatus("current")
_InputControlUnitInputTable_Object = MibTable
inputControlUnitInputTable = _InputControlUnitInputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2)
)
if mibBuilder.loadTexts:
    inputControlUnitInputTable.setStatus("current")
_InputControlUnitInputEntry_Object = MibTableRow
inputControlUnitInputEntry = _InputControlUnitInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1)
)
inputControlUnitInputEntry.setIndexNames(
    (0, "SP2-MIB", "inputControlUnitIndex"),
    (0, "SP2-MIB", "inputControlUnitInputIndex"),
)
if mibBuilder.loadTexts:
    inputControlUnitInputEntry.setStatus("current")


class _InputControlUnitInputIndex_Type(Integer32):
    """Custom type inputControlUnitInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_InputControlUnitInputIndex_Type.__name__ = "Integer32"
_InputControlUnitInputIndex_Object = MibTableColumn
inputControlUnitInputIndex = _InputControlUnitInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 1),
    _InputControlUnitInputIndex_Type()
)
inputControlUnitInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputControlUnitInputIndex.setStatus("current")


class _InputControlUnitInputStatus_Type(Integer32):
    """Custom type inputControlUnitInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InputControlUnitInputStatus_Type.__name__ = "Integer32"
_InputControlUnitInputStatus_Object = MibTableColumn
inputControlUnitInputStatus = _InputControlUnitInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 2),
    _InputControlUnitInputStatus_Type()
)
inputControlUnitInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputControlUnitInputStatus.setStatus("current")


class _InputControlUnitInputDescription_Type(DisplayString):
    """Custom type inputControlUnitInputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputControlUnitInputDescription_Type.__name__ = "DisplayString"
_InputControlUnitInputDescription_Object = MibTableColumn
inputControlUnitInputDescription = _InputControlUnitInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 3),
    _InputControlUnitInputDescription_Type()
)
inputControlUnitInputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputControlUnitInputDescription.setStatus("current")
_InputControlUnitInputTrapRepeatCounter_Type = Counter32
_InputControlUnitInputTrapRepeatCounter_Object = MibTableColumn
inputControlUnitInputTrapRepeatCounter = _InputControlUnitInputTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 4),
    _InputControlUnitInputTrapRepeatCounter_Type()
)
inputControlUnitInputTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inputControlUnitInputTrapRepeatCounter.setStatus("current")


class _InputControlUnitInputAlarmEnable_Type(Integer32):
    """Custom type inputControlUnitInputAlarmEnable based on Integer32"""
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


_InputControlUnitInputAlarmEnable_Type.__name__ = "Integer32"
_InputControlUnitInputAlarmEnable_Object = MibTableColumn
inputControlUnitInputAlarmEnable = _InputControlUnitInputAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 5),
    _InputControlUnitInputAlarmEnable_Type()
)
inputControlUnitInputAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputControlUnitInputAlarmEnable.setStatus("current")
_InputControlUnitInputValue_Type = Integer32
_InputControlUnitInputValue_Object = MibTableColumn
inputControlUnitInputValue = _InputControlUnitInputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 6),
    _InputControlUnitInputValue_Type()
)
inputControlUnitInputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputControlUnitInputValue.setStatus("current")


class _InputControlUnitInputConfiguration_Type(Integer32):
    """Custom type inputControlUnitInputConfiguration based on Integer32"""
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
        *(("normallyOpen", 1),
          ("normallyClosed", 2),
          ("diodeMatrix", 3),
          ("voltage", 4),
          ("clock", 5),
          ("virtual", 6))
    )


_InputControlUnitInputConfiguration_Type.__name__ = "Integer32"
_InputControlUnitInputConfiguration_Object = MibTableColumn
inputControlUnitInputConfiguration = _InputControlUnitInputConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 2, 1, 7),
    _InputControlUnitInputConfiguration_Type()
)
inputControlUnitInputConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputControlUnitInputConfiguration.setStatus("current")
_InputIoUnitsTable_Object = MibTable
inputIoUnitsTable = _InputIoUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 3)
)
if mibBuilder.loadTexts:
    inputIoUnitsTable.setStatus("current")
_InputIoUnitsEntry_Object = MibTableRow
inputIoUnitsEntry = _InputIoUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 3, 1)
)
inputIoUnitsEntry.setIndexNames(
    (0, "SP2-MIB", "inputIoUnitIndex"),
)
if mibBuilder.loadTexts:
    inputIoUnitsEntry.setStatus("current")


class _InputIoUnitIndex_Type(Integer32):
    """Custom type inputIoUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_InputIoUnitIndex_Type.__name__ = "Integer32"
_InputIoUnitIndex_Object = MibTableColumn
inputIoUnitIndex = _InputIoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 3, 1, 1),
    _InputIoUnitIndex_Type()
)
inputIoUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputIoUnitIndex.setStatus("current")


class _InputIoUnitNumberOfInputs_Type(Integer32):
    """Custom type inputIoUnitNumberOfInputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_InputIoUnitNumberOfInputs_Type.__name__ = "Integer32"
_InputIoUnitNumberOfInputs_Object = MibTableColumn
inputIoUnitNumberOfInputs = _InputIoUnitNumberOfInputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 3, 1, 2),
    _InputIoUnitNumberOfInputs_Type()
)
inputIoUnitNumberOfInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputIoUnitNumberOfInputs.setStatus("current")
_InputIoUnitProgInputTable_Object = MibTable
inputIoUnitProgInputTable = _InputIoUnitProgInputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4)
)
if mibBuilder.loadTexts:
    inputIoUnitProgInputTable.setStatus("current")
_InputIoUnitProgInputEntry_Object = MibTableRow
inputIoUnitProgInputEntry = _InputIoUnitProgInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1)
)
inputIoUnitProgInputEntry.setIndexNames(
    (0, "SP2-MIB", "inputIoUnitIndex"),
    (0, "SP2-MIB", "inputIoUnitProgInputIndex"),
)
if mibBuilder.loadTexts:
    inputIoUnitProgInputEntry.setStatus("current")


class _InputIoUnitProgInputIndex_Type(Integer32):
    """Custom type inputIoUnitProgInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_InputIoUnitProgInputIndex_Type.__name__ = "Integer32"
_InputIoUnitProgInputIndex_Object = MibTableColumn
inputIoUnitProgInputIndex = _InputIoUnitProgInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 1),
    _InputIoUnitProgInputIndex_Type()
)
inputIoUnitProgInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inputIoUnitProgInputIndex.setStatus("current")


class _InputIoUnitProgInputStatus_Type(Integer32):
    """Custom type inputIoUnitProgInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InputIoUnitProgInputStatus_Type.__name__ = "Integer32"
_InputIoUnitProgInputStatus_Object = MibTableColumn
inputIoUnitProgInputStatus = _InputIoUnitProgInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 2),
    _InputIoUnitProgInputStatus_Type()
)
inputIoUnitProgInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputIoUnitProgInputStatus.setStatus("current")


class _InputIoUnitProgInputDescription_Type(DisplayString):
    """Custom type inputIoUnitProgInputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InputIoUnitProgInputDescription_Type.__name__ = "DisplayString"
_InputIoUnitProgInputDescription_Object = MibTableColumn
inputIoUnitProgInputDescription = _InputIoUnitProgInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 3),
    _InputIoUnitProgInputDescription_Type()
)
inputIoUnitProgInputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputIoUnitProgInputDescription.setStatus("current")
_InputIoUnitProgInputTrapRepeatCounter_Type = Counter32
_InputIoUnitProgInputTrapRepeatCounter_Object = MibTableColumn
inputIoUnitProgInputTrapRepeatCounter = _InputIoUnitProgInputTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 4),
    _InputIoUnitProgInputTrapRepeatCounter_Type()
)
inputIoUnitProgInputTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inputIoUnitProgInputTrapRepeatCounter.setStatus("current")


class _InputIoUnitProgInputAlarmEnable_Type(Integer32):
    """Custom type inputIoUnitProgInputAlarmEnable based on Integer32"""
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


_InputIoUnitProgInputAlarmEnable_Type.__name__ = "Integer32"
_InputIoUnitProgInputAlarmEnable_Object = MibTableColumn
inputIoUnitProgInputAlarmEnable = _InputIoUnitProgInputAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 5),
    _InputIoUnitProgInputAlarmEnable_Type()
)
inputIoUnitProgInputAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputIoUnitProgInputAlarmEnable.setStatus("current")
_InputIoUnitProgInputValue_Type = Integer32
_InputIoUnitProgInputValue_Object = MibTableColumn
inputIoUnitProgInputValue = _InputIoUnitProgInputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 6),
    _InputIoUnitProgInputValue_Type()
)
inputIoUnitProgInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputIoUnitProgInputValue.setStatus("current")


class _InputIoUnitProgInputConfiguration_Type(Integer32):
    """Custom type inputIoUnitProgInputConfiguration based on Integer32"""
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
        *(("normallyOpen", 1),
          ("normallyClosed", 2),
          ("diodeMatrix", 3),
          ("voltage", 4),
          ("clock", 5))
    )


_InputIoUnitProgInputConfiguration_Type.__name__ = "Integer32"
_InputIoUnitProgInputConfiguration_Object = MibTableColumn
inputIoUnitProgInputConfiguration = _InputIoUnitProgInputConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 11, 4, 1, 7),
    _InputIoUnitProgInputConfiguration_Type()
)
inputIoUnitProgInputConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputIoUnitProgInputConfiguration.setStatus("current")
_Outputs_ObjectIdentity = ObjectIdentity
outputs = _Outputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12)
)
_OutputControlUnitTable_Object = MibTable
outputControlUnitTable = _OutputControlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 1)
)
if mibBuilder.loadTexts:
    outputControlUnitTable.setStatus("current")
_OutputControlUnitEntry_Object = MibTableRow
outputControlUnitEntry = _OutputControlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 1, 1)
)
outputControlUnitEntry.setIndexNames(
    (0, "SP2-MIB", "outputControlUnitIndex"),
)
if mibBuilder.loadTexts:
    outputControlUnitEntry.setStatus("current")


class _OutputControlUnitIndex_Type(Integer32):
    """Custom type outputControlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_OutputControlUnitIndex_Type.__name__ = "Integer32"
_OutputControlUnitIndex_Object = MibTableColumn
outputControlUnitIndex = _OutputControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 1, 1, 1),
    _OutputControlUnitIndex_Type()
)
outputControlUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputControlUnitIndex.setStatus("current")


class _OutputControlUnitNumberOfOutputs_Type(Integer32):
    """Custom type outputControlUnitNumberOfOutputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_OutputControlUnitNumberOfOutputs_Type.__name__ = "Integer32"
_OutputControlUnitNumberOfOutputs_Object = MibTableColumn
outputControlUnitNumberOfOutputs = _OutputControlUnitNumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 1, 1, 2),
    _OutputControlUnitNumberOfOutputs_Type()
)
outputControlUnitNumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputControlUnitNumberOfOutputs.setStatus("current")
_OutputControlUnitOutputTable_Object = MibTable
outputControlUnitOutputTable = _OutputControlUnitOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2)
)
if mibBuilder.loadTexts:
    outputControlUnitOutputTable.setStatus("current")
_OutputControlUnitOutputEntry_Object = MibTableRow
outputControlUnitOutputEntry = _OutputControlUnitOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2, 1)
)
outputControlUnitOutputEntry.setIndexNames(
    (0, "SP2-MIB", "outputControlUnitIndex"),
    (0, "SP2-MIB", "outputControlUnitOutputIndex"),
)
if mibBuilder.loadTexts:
    outputControlUnitOutputEntry.setStatus("current")


class _OutputControlUnitOutputIndex_Type(Integer32):
    """Custom type outputControlUnitOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OutputControlUnitOutputIndex_Type.__name__ = "Integer32"
_OutputControlUnitOutputIndex_Object = MibTableColumn
outputControlUnitOutputIndex = _OutputControlUnitOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2, 1, 1),
    _OutputControlUnitOutputIndex_Type()
)
outputControlUnitOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputControlUnitOutputIndex.setStatus("current")


class _OutputControlUnitOutputStatus_Type(Integer32):
    """Custom type outputControlUnitOutputStatus based on Integer32"""
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
        *(("notenergized", 0),
          ("energized", 1),
          ("disconnected", 2),
          ("connected", 3))
    )


_OutputControlUnitOutputStatus_Type.__name__ = "Integer32"
_OutputControlUnitOutputStatus_Object = MibTableColumn
outputControlUnitOutputStatus = _OutputControlUnitOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2, 1, 2),
    _OutputControlUnitOutputStatus_Type()
)
outputControlUnitOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputControlUnitOutputStatus.setStatus("current")


class _OutputControlUnitOutputDescription_Type(DisplayString):
    """Custom type outputControlUnitOutputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OutputControlUnitOutputDescription_Type.__name__ = "DisplayString"
_OutputControlUnitOutputDescription_Object = MibTableColumn
outputControlUnitOutputDescription = _OutputControlUnitOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 2, 1, 3),
    _OutputControlUnitOutputDescription_Type()
)
outputControlUnitOutputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputControlUnitOutputDescription.setStatus("current")
_OutputIoUnitTable_Object = MibTable
outputIoUnitTable = _OutputIoUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 3)
)
if mibBuilder.loadTexts:
    outputIoUnitTable.setStatus("current")
_OutputIoUnitEntry_Object = MibTableRow
outputIoUnitEntry = _OutputIoUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 3, 1)
)
outputIoUnitEntry.setIndexNames(
    (0, "SP2-MIB", "outputIoUnitIndex"),
)
if mibBuilder.loadTexts:
    outputIoUnitEntry.setStatus("current")


class _OutputIoUnitIndex_Type(Integer32):
    """Custom type outputIoUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_OutputIoUnitIndex_Type.__name__ = "Integer32"
_OutputIoUnitIndex_Object = MibTableColumn
outputIoUnitIndex = _OutputIoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 3, 1, 1),
    _OutputIoUnitIndex_Type()
)
outputIoUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputIoUnitIndex.setStatus("current")


class _OutputIoUnitNumberOfOutputs_Type(Integer32):
    """Custom type outputIoUnitNumberOfOutputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_OutputIoUnitNumberOfOutputs_Type.__name__ = "Integer32"
_OutputIoUnitNumberOfOutputs_Object = MibTableColumn
outputIoUnitNumberOfOutputs = _OutputIoUnitNumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 3, 1, 2),
    _OutputIoUnitNumberOfOutputs_Type()
)
outputIoUnitNumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputIoUnitNumberOfOutputs.setStatus("current")
_OutputIoUnitOutputTable_Object = MibTable
outputIoUnitOutputTable = _OutputIoUnitOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4)
)
if mibBuilder.loadTexts:
    outputIoUnitOutputTable.setStatus("current")
_OutputIoUnitOutputEntry_Object = MibTableRow
outputIoUnitOutputEntry = _OutputIoUnitOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4, 1)
)
outputIoUnitOutputEntry.setIndexNames(
    (0, "SP2-MIB", "outputIoUnitIndex"),
    (0, "SP2-MIB", "outputIoUnitOutputIndex"),
)
if mibBuilder.loadTexts:
    outputIoUnitOutputEntry.setStatus("current")


class _OutputIoUnitOutputIndex_Type(Integer32):
    """Custom type outputIoUnitOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_OutputIoUnitOutputIndex_Type.__name__ = "Integer32"
_OutputIoUnitOutputIndex_Object = MibTableColumn
outputIoUnitOutputIndex = _OutputIoUnitOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4, 1, 1),
    _OutputIoUnitOutputIndex_Type()
)
outputIoUnitOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    outputIoUnitOutputIndex.setStatus("current")


class _OutputIoUnitOutputStatus_Type(Integer32):
    """Custom type outputIoUnitOutputStatus based on Integer32"""
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
        *(("notenergized", 0),
          ("energized", 1),
          ("disconnected", 2),
          ("connected", 3))
    )


_OutputIoUnitOutputStatus_Type.__name__ = "Integer32"
_OutputIoUnitOutputStatus_Object = MibTableColumn
outputIoUnitOutputStatus = _OutputIoUnitOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4, 1, 2),
    _OutputIoUnitOutputStatus_Type()
)
outputIoUnitOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputIoUnitOutputStatus.setStatus("current")


class _OutputIoUnitOutputDescription_Type(DisplayString):
    """Custom type outputIoUnitOutputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OutputIoUnitOutputDescription_Type.__name__ = "DisplayString"
_OutputIoUnitOutputDescription_Object = MibTableColumn
outputIoUnitOutputDescription = _OutputIoUnitOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 12, 4, 1, 3),
    _OutputIoUnitOutputDescription_Type()
)
outputIoUnitOutputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputIoUnitOutputDescription.setStatus("current")
_ControlSystem_ObjectIdentity = ObjectIdentity
controlSystem = _ControlSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13)
)


class _ControlSystemStatus_Type(Integer32):
    """Custom type controlSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_ControlSystemStatus_Type.__name__ = "Integer32"
_ControlSystemStatus_Object = MibScalar
controlSystemStatus = _ControlSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 1),
    _ControlSystemStatus_Type()
)
controlSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemStatus.setStatus("current")


class _ControlSystemClock_Type(DateAndTime):
    """Custom type controlSystemClock based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 11),
    )


_ControlSystemClock_Type.__name__ = "DateAndTime"
_ControlSystemClock_Object = MibScalar
controlSystemClock = _ControlSystemClock_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 2),
    _ControlSystemClock_Type()
)
controlSystemClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemClock.setStatus("current")


class _ControlSystemNumberOfControlUnits_Type(Integer32):
    """Custom type controlSystemNumberOfControlUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ControlSystemNumberOfControlUnits_Type.__name__ = "Integer32"
_ControlSystemNumberOfControlUnits_Object = MibScalar
controlSystemNumberOfControlUnits = _ControlSystemNumberOfControlUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 3),
    _ControlSystemNumberOfControlUnits_Type()
)
controlSystemNumberOfControlUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemNumberOfControlUnits.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4)
)


class _SnmpSendOffTraps_Type(Integer32):
    """Custom type snmpSendOffTraps based on Integer32"""
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


_SnmpSendOffTraps_Type.__name__ = "Integer32"
_SnmpSendOffTraps_Object = MibScalar
snmpSendOffTraps = _SnmpSendOffTraps_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4, 1),
    _SnmpSendOffTraps_Type()
)
snmpSendOffTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSendOffTraps.setStatus("current")


class _SnmpTrapRepeatRate_Type(Integer32):
    """Custom type snmpTrapRepeatRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SnmpTrapRepeatRate_Type.__name__ = "Integer32"
_SnmpTrapRepeatRate_Object = MibScalar
snmpTrapRepeatRate = _SnmpTrapRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4, 2),
    _SnmpTrapRepeatRate_Type()
)
snmpTrapRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRepeatRate.setStatus("current")


class _SnmpHeartBeatTrapRepeatRate_Type(Integer32):
    """Custom type snmpHeartBeatTrapRepeatRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SnmpHeartBeatTrapRepeatRate_Type.__name__ = "Integer32"
_SnmpHeartBeatTrapRepeatRate_Object = MibScalar
snmpHeartBeatTrapRepeatRate = _SnmpHeartBeatTrapRepeatRate_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4, 3),
    _SnmpHeartBeatTrapRepeatRate_Type()
)
snmpHeartBeatTrapRepeatRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpHeartBeatTrapRepeatRate.setStatus("current")


class _SnmpInhibitTraps_Type(Integer32):
    """Custom type snmpInhibitTraps based on Integer32"""
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


_SnmpInhibitTraps_Type.__name__ = "Integer32"
_SnmpInhibitTraps_Object = MibScalar
snmpInhibitTraps = _SnmpInhibitTraps_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 4, 4),
    _SnmpInhibitTraps_Type()
)
snmpInhibitTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInhibitTraps.setStatus("current")


class _ControlSystemResetManualAlarms_Type(Integer32):
    """Custom type controlSystemResetManualAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("resetalarm", 1))
    )


_ControlSystemResetManualAlarms_Type.__name__ = "Integer32"
_ControlSystemResetManualAlarms_Object = MibScalar
controlSystemResetManualAlarms = _ControlSystemResetManualAlarms_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 5),
    _ControlSystemResetManualAlarms_Type()
)
controlSystemResetManualAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemResetManualAlarms.setStatus("current")


class _ControlSystemResetNumberOfModules_Type(Integer32):
    """Custom type controlSystemResetNumberOfModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("resetnumber", 1))
    )


_ControlSystemResetNumberOfModules_Type.__name__ = "Integer32"
_ControlSystemResetNumberOfModules_Object = MibScalar
controlSystemResetNumberOfModules = _ControlSystemResetNumberOfModules_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 6),
    _ControlSystemResetNumberOfModules_Type()
)
controlSystemResetNumberOfModules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemResetNumberOfModules.setStatus("current")
_ControlSystemIoUnits_ObjectIdentity = ObjectIdentity
controlSystemIoUnits = _ControlSystemIoUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7)
)


class _ControlSystemIoUnitsNumberOfUnits_Type(Integer32):
    """Custom type controlSystemIoUnitsNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ControlSystemIoUnitsNumberOfUnits_Type.__name__ = "Integer32"
_ControlSystemIoUnitsNumberOfUnits_Object = MibScalar
controlSystemIoUnitsNumberOfUnits = _ControlSystemIoUnitsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 1),
    _ControlSystemIoUnitsNumberOfUnits_Type()
)
controlSystemIoUnitsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitsNumberOfUnits.setStatus("current")
_ControlSystemIoUnitsTable_Object = MibTable
controlSystemIoUnitsTable = _ControlSystemIoUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2)
)
if mibBuilder.loadTexts:
    controlSystemIoUnitsTable.setStatus("current")
_ControlSystemIoUnitsEntry_Object = MibTableRow
controlSystemIoUnitsEntry = _ControlSystemIoUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2, 1)
)
controlSystemIoUnitsEntry.setIndexNames(
    (0, "SP2-MIB", "controlSystemIoUnitIndex"),
)
if mibBuilder.loadTexts:
    controlSystemIoUnitsEntry.setStatus("current")


class _ControlSystemIoUnitIndex_Type(Integer32):
    """Custom type controlSystemIoUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ControlSystemIoUnitIndex_Type.__name__ = "Integer32"
_ControlSystemIoUnitIndex_Object = MibTableColumn
controlSystemIoUnitIndex = _ControlSystemIoUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2, 1, 1),
    _ControlSystemIoUnitIndex_Type()
)
controlSystemIoUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSystemIoUnitIndex.setStatus("current")


class _ControlSystemIoUnitNumberOfTemperatures_Type(Integer32):
    """Custom type controlSystemIoUnitNumberOfTemperatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ControlSystemIoUnitNumberOfTemperatures_Type.__name__ = "Integer32"
_ControlSystemIoUnitNumberOfTemperatures_Object = MibTableColumn
controlSystemIoUnitNumberOfTemperatures = _ControlSystemIoUnitNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2, 1, 2),
    _ControlSystemIoUnitNumberOfTemperatures_Type()
)
controlSystemIoUnitNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitNumberOfTemperatures.setStatus("current")


class _ControlSystemIoUnitNumberOfFans_Type(Integer32):
    """Custom type controlSystemIoUnitNumberOfFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_ControlSystemIoUnitNumberOfFans_Type.__name__ = "Integer32"
_ControlSystemIoUnitNumberOfFans_Object = MibTableColumn
controlSystemIoUnitNumberOfFans = _ControlSystemIoUnitNumberOfFans_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 2, 1, 3),
    _ControlSystemIoUnitNumberOfFans_Type()
)
controlSystemIoUnitNumberOfFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitNumberOfFans.setStatus("current")
_ControlSystemIoUnitTemperatureTable_Object = MibTable
controlSystemIoUnitTemperatureTable = _ControlSystemIoUnitTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3)
)
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureTable.setStatus("current")
_ControlSystemIoUnitTemperatureEntry_Object = MibTableRow
controlSystemIoUnitTemperatureEntry = _ControlSystemIoUnitTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1)
)
controlSystemIoUnitTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "controlSystemIoUnitIndex"),
    (0, "SP2-MIB", "controlSystemIoUnitTemperatureIndex"),
)
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureEntry.setStatus("current")


class _ControlSystemIoUnitTemperatureIndex_Type(Integer32):
    """Custom type controlSystemIoUnitTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ControlSystemIoUnitTemperatureIndex_Type.__name__ = "Integer32"
_ControlSystemIoUnitTemperatureIndex_Object = MibTableColumn
controlSystemIoUnitTemperatureIndex = _ControlSystemIoUnitTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 1),
    _ControlSystemIoUnitTemperatureIndex_Type()
)
controlSystemIoUnitTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureIndex.setStatus("current")


class _ControlSystemIoUnitTemperatureStatus_Type(Integer32):
    """Custom type controlSystemIoUnitTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_ControlSystemIoUnitTemperatureStatus_Type.__name__ = "Integer32"
_ControlSystemIoUnitTemperatureStatus_Object = MibTableColumn
controlSystemIoUnitTemperatureStatus = _ControlSystemIoUnitTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 2),
    _ControlSystemIoUnitTemperatureStatus_Type()
)
controlSystemIoUnitTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureStatus.setStatus("current")


class _ControlSystemIoUnitTemperatureDescription_Type(DisplayString):
    """Custom type controlSystemIoUnitTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ControlSystemIoUnitTemperatureDescription_Type.__name__ = "DisplayString"
_ControlSystemIoUnitTemperatureDescription_Object = MibTableColumn
controlSystemIoUnitTemperatureDescription = _ControlSystemIoUnitTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 3),
    _ControlSystemIoUnitTemperatureDescription_Type()
)
controlSystemIoUnitTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureDescription.setStatus("current")
_ControlSystemIoUnitTemperatureTrapRepeatCounter_Type = Counter32
_ControlSystemIoUnitTemperatureTrapRepeatCounter_Object = MibTableColumn
controlSystemIoUnitTemperatureTrapRepeatCounter = _ControlSystemIoUnitTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 4),
    _ControlSystemIoUnitTemperatureTrapRepeatCounter_Type()
)
controlSystemIoUnitTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureTrapRepeatCounter.setStatus("current")


class _ControlSystemIoUnitTemperatureAlarmEnable_Type(Integer32):
    """Custom type controlSystemIoUnitTemperatureAlarmEnable based on Integer32"""
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


_ControlSystemIoUnitTemperatureAlarmEnable_Type.__name__ = "Integer32"
_ControlSystemIoUnitTemperatureAlarmEnable_Object = MibTableColumn
controlSystemIoUnitTemperatureAlarmEnable = _ControlSystemIoUnitTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 5),
    _ControlSystemIoUnitTemperatureAlarmEnable_Type()
)
controlSystemIoUnitTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureAlarmEnable.setStatus("current")
_ControlSystemIoUnitTemperatureValue_Type = Integer32
_ControlSystemIoUnitTemperatureValue_Object = MibTableColumn
controlSystemIoUnitTemperatureValue = _ControlSystemIoUnitTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 6),
    _ControlSystemIoUnitTemperatureValue_Type()
)
controlSystemIoUnitTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureValue.setStatus("current")
_ControlSystemIoUnitTemperatureMajorHighLevel_Type = Integer32
_ControlSystemIoUnitTemperatureMajorHighLevel_Object = MibTableColumn
controlSystemIoUnitTemperatureMajorHighLevel = _ControlSystemIoUnitTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 7),
    _ControlSystemIoUnitTemperatureMajorHighLevel_Type()
)
controlSystemIoUnitTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureMajorHighLevel.setStatus("current")
_ControlSystemIoUnitTemperatureMinorHighLevel_Type = Integer32
_ControlSystemIoUnitTemperatureMinorHighLevel_Object = MibTableColumn
controlSystemIoUnitTemperatureMinorHighLevel = _ControlSystemIoUnitTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 8),
    _ControlSystemIoUnitTemperatureMinorHighLevel_Type()
)
controlSystemIoUnitTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureMinorHighLevel.setStatus("current")
_ControlSystemIoUnitTemperatureMinorLowLevel_Type = Integer32
_ControlSystemIoUnitTemperatureMinorLowLevel_Object = MibTableColumn
controlSystemIoUnitTemperatureMinorLowLevel = _ControlSystemIoUnitTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 9),
    _ControlSystemIoUnitTemperatureMinorLowLevel_Type()
)
controlSystemIoUnitTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureMinorLowLevel.setStatus("current")
_ControlSystemIoUnitTemperatureMajorLowLevel_Type = Integer32
_ControlSystemIoUnitTemperatureMajorLowLevel_Object = MibTableColumn
controlSystemIoUnitTemperatureMajorLowLevel = _ControlSystemIoUnitTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 3, 1, 10),
    _ControlSystemIoUnitTemperatureMajorLowLevel_Type()
)
controlSystemIoUnitTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlSystemIoUnitTemperatureMajorLowLevel.setStatus("current")
_ControlSystemIoUnitFanTable_Object = MibTable
controlSystemIoUnitFanTable = _ControlSystemIoUnitFanTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4)
)
if mibBuilder.loadTexts:
    controlSystemIoUnitFanTable.setStatus("current")
_ControlSystemIoUnitFanEntry_Object = MibTableRow
controlSystemIoUnitFanEntry = _ControlSystemIoUnitFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1)
)
controlSystemIoUnitFanEntry.setIndexNames(
    (0, "SP2-MIB", "controlSystemIoUnitIndex"),
    (0, "SP2-MIB", "controlSystemIoUnitFanIndex"),
)
if mibBuilder.loadTexts:
    controlSystemIoUnitFanEntry.setStatus("current")


class _ControlSystemIoUnitFanIndex_Type(Integer32):
    """Custom type controlSystemIoUnitFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ControlSystemIoUnitFanIndex_Type.__name__ = "Integer32"
_ControlSystemIoUnitFanIndex_Object = MibTableColumn
controlSystemIoUnitFanIndex = _ControlSystemIoUnitFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1, 1),
    _ControlSystemIoUnitFanIndex_Type()
)
controlSystemIoUnitFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlSystemIoUnitFanIndex.setStatus("current")
_ControlSystemIoUnitFanSpeedValue_Type = Integer32
_ControlSystemIoUnitFanSpeedValue_Object = MibTableColumn
controlSystemIoUnitFanSpeedValue = _ControlSystemIoUnitFanSpeedValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1, 2),
    _ControlSystemIoUnitFanSpeedValue_Type()
)
controlSystemIoUnitFanSpeedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitFanSpeedValue.setStatus("current")
_ControlSystemIoUnitFanSpeedDeviation_Type = Integer32
_ControlSystemIoUnitFanSpeedDeviation_Object = MibTableColumn
controlSystemIoUnitFanSpeedDeviation = _ControlSystemIoUnitFanSpeedDeviation_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1, 3),
    _ControlSystemIoUnitFanSpeedDeviation_Type()
)
controlSystemIoUnitFanSpeedDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitFanSpeedDeviation.setStatus("current")
_ControlSystemIoUnitFanControl_Type = Integer32
_ControlSystemIoUnitFanControl_Object = MibTableColumn
controlSystemIoUnitFanControl = _ControlSystemIoUnitFanControl_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 7, 4, 1, 4),
    _ControlSystemIoUnitFanControl_Type()
)
controlSystemIoUnitFanControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlSystemIoUnitFanControl.setStatus("current")
_ControlSystemInventory_ObjectIdentity = ObjectIdentity
controlSystemInventory = _ControlSystemInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8)
)


class _ControlUnitNumberOfUnits_Type(Integer32):
    """Custom type controlUnitNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ControlUnitNumberOfUnits_Type.__name__ = "Integer32"
_ControlUnitNumberOfUnits_Object = MibScalar
controlUnitNumberOfUnits = _ControlUnitNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 1),
    _ControlUnitNumberOfUnits_Type()
)
controlUnitNumberOfUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitNumberOfUnits.setStatus("current")
_ControlUnitTable_Object = MibTable
controlUnitTable = _ControlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2)
)
if mibBuilder.loadTexts:
    controlUnitTable.setStatus("current")
_ControlUnitEntry_Object = MibTableRow
controlUnitEntry = _ControlUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1)
)
controlUnitEntry.setIndexNames(
    (0, "SP2-MIB", "controlUnitIndex"),
)
if mibBuilder.loadTexts:
    controlUnitEntry.setStatus("current")


class _ControlUnitIndex_Type(Integer32):
    """Custom type controlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_ControlUnitIndex_Type.__name__ = "Integer32"
_ControlUnitIndex_Object = MibTableColumn
controlUnitIndex = _ControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 1),
    _ControlUnitIndex_Type()
)
controlUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    controlUnitIndex.setStatus("current")


class _ControlUnitDescription_Type(DisplayString):
    """Custom type controlUnitDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ControlUnitDescription_Type.__name__ = "DisplayString"
_ControlUnitDescription_Object = MibTableColumn
controlUnitDescription = _ControlUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 2),
    _ControlUnitDescription_Type()
)
controlUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitDescription.setStatus("current")


class _ControlUnitStatus_Type(Integer32):
    """Custom type controlUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_ControlUnitStatus_Type.__name__ = "Integer32"
_ControlUnitStatus_Object = MibTableColumn
controlUnitStatus = _ControlUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 3),
    _ControlUnitStatus_Type()
)
controlUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitStatus.setStatus("current")


class _ControlUnitSerialNumber_Type(DisplayString):
    """Custom type controlUnitSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ControlUnitSerialNumber_Type.__name__ = "DisplayString"
_ControlUnitSerialNumber_Object = MibTableColumn
controlUnitSerialNumber = _ControlUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 4),
    _ControlUnitSerialNumber_Type()
)
controlUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitSerialNumber.setStatus("current")


class _ControlUnitHwPartNumber_Type(DisplayString):
    """Custom type controlUnitHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ControlUnitHwPartNumber_Type.__name__ = "DisplayString"
_ControlUnitHwPartNumber_Object = MibTableColumn
controlUnitHwPartNumber = _ControlUnitHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 5),
    _ControlUnitHwPartNumber_Type()
)
controlUnitHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitHwPartNumber.setStatus("current")


class _ControlUnitHwVersion_Type(DisplayString):
    """Custom type controlUnitHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ControlUnitHwVersion_Type.__name__ = "DisplayString"
_ControlUnitHwVersion_Object = MibTableColumn
controlUnitHwVersion = _ControlUnitHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 6),
    _ControlUnitHwVersion_Type()
)
controlUnitHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitHwVersion.setStatus("current")


class _ControlUnitSwPartNumber_Type(DisplayString):
    """Custom type controlUnitSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ControlUnitSwPartNumber_Type.__name__ = "DisplayString"
_ControlUnitSwPartNumber_Object = MibTableColumn
controlUnitSwPartNumber = _ControlUnitSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 7),
    _ControlUnitSwPartNumber_Type()
)
controlUnitSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitSwPartNumber.setStatus("current")


class _ControlUnitSwVersion_Type(DisplayString):
    """Custom type controlUnitSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ControlUnitSwVersion_Type.__name__ = "DisplayString"
_ControlUnitSwVersion_Object = MibTableColumn
controlUnitSwVersion = _ControlUnitSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 8, 2, 1, 8),
    _ControlUnitSwVersion_Type()
)
controlUnitSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlUnitSwVersion.setStatus("current")
_CurrentMonitors_ObjectIdentity = ObjectIdentity
currentMonitors = _CurrentMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9)
)


class _CurrentMonitorsNumberOfUnits_Type(Integer32):
    """Custom type currentMonitorsNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_CurrentMonitorsNumberOfUnits_Type.__name__ = "Integer32"
_CurrentMonitorsNumberOfUnits_Object = MibScalar
currentMonitorsNumberOfUnits = _CurrentMonitorsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 1),
    _CurrentMonitorsNumberOfUnits_Type()
)
currentMonitorsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorsNumberOfUnits.setStatus("current")
_CurrentMonitorsTable_Object = MibTable
currentMonitorsTable = _CurrentMonitorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2)
)
if mibBuilder.loadTexts:
    currentMonitorsTable.setStatus("current")
_CurrentMonitorsEntry_Object = MibTableRow
currentMonitorsEntry = _CurrentMonitorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1)
)
currentMonitorsEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorsEntry.setStatus("current")


class _CurrentMonitorIndex_Type(Integer32):
    """Custom type currentMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_CurrentMonitorIndex_Type.__name__ = "Integer32"
_CurrentMonitorIndex_Object = MibTableColumn
currentMonitorIndex = _CurrentMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 1),
    _CurrentMonitorIndex_Type()
)
currentMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorIndex.setStatus("current")


class _CurrentMonitorType_Type(Integer32):
    """Custom type currentMonitorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("stdLoadMonitor", 1),
          ("loadCurrMonitor", 2),
          ("rectCurrMonitor", 3),
          ("dcdcCurrMonitor", 4),
          ("solarCurrMonitor", 5),
          ("windCurrMonitor", 6),
          ("fuelcellCurrMonitor", 7))
    )


_CurrentMonitorType_Type.__name__ = "Integer32"
_CurrentMonitorType_Object = MibTableColumn
currentMonitorType = _CurrentMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 2),
    _CurrentMonitorType_Type()
)
currentMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorType.setStatus("current")
_CurrentMonitorId_Type = Integer32
_CurrentMonitorId_Object = MibTableColumn
currentMonitorId = _CurrentMonitorId_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 3),
    _CurrentMonitorId_Type()
)
currentMonitorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorId.setStatus("current")


class _CurrentMonitorNumberOfFuses_Type(Integer32):
    """Custom type currentMonitorNumberOfFuses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CurrentMonitorNumberOfFuses_Type.__name__ = "Integer32"
_CurrentMonitorNumberOfFuses_Object = MibTableColumn
currentMonitorNumberOfFuses = _CurrentMonitorNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 4),
    _CurrentMonitorNumberOfFuses_Type()
)
currentMonitorNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorNumberOfFuses.setStatus("current")


class _CurrentMonitorNumberOfCurrents_Type(Integer32):
    """Custom type currentMonitorNumberOfCurrents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CurrentMonitorNumberOfCurrents_Type.__name__ = "Integer32"
_CurrentMonitorNumberOfCurrents_Object = MibTableColumn
currentMonitorNumberOfCurrents = _CurrentMonitorNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 2, 1, 5),
    _CurrentMonitorNumberOfCurrents_Type()
)
currentMonitorNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorNumberOfCurrents.setStatus("current")
_CurrentMonitorFuseTable_Object = MibTable
currentMonitorFuseTable = _CurrentMonitorFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3)
)
if mibBuilder.loadTexts:
    currentMonitorFuseTable.setStatus("current")
_CurrentMonitorFuseEntry_Object = MibTableRow
currentMonitorFuseEntry = _CurrentMonitorFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1)
)
currentMonitorFuseEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorFuseIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorFuseEntry.setStatus("current")


class _CurrentMonitorFuseIndex_Type(Integer32):
    """Custom type currentMonitorFuseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CurrentMonitorFuseIndex_Type.__name__ = "Integer32"
_CurrentMonitorFuseIndex_Object = MibTableColumn
currentMonitorFuseIndex = _CurrentMonitorFuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 1),
    _CurrentMonitorFuseIndex_Type()
)
currentMonitorFuseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorFuseIndex.setStatus("current")


class _CurrentMonitorFuseStatus_Type(Integer32):
    """Custom type currentMonitorFuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_CurrentMonitorFuseStatus_Type.__name__ = "Integer32"
_CurrentMonitorFuseStatus_Object = MibTableColumn
currentMonitorFuseStatus = _CurrentMonitorFuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 2),
    _CurrentMonitorFuseStatus_Type()
)
currentMonitorFuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorFuseStatus.setStatus("current")


class _CurrentMonitorFuseDescription_Type(DisplayString):
    """Custom type currentMonitorFuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CurrentMonitorFuseDescription_Type.__name__ = "DisplayString"
_CurrentMonitorFuseDescription_Object = MibTableColumn
currentMonitorFuseDescription = _CurrentMonitorFuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 3),
    _CurrentMonitorFuseDescription_Type()
)
currentMonitorFuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorFuseDescription.setStatus("current")
_CurrentMonitorFuseTrapRepeatCounter_Type = Counter32
_CurrentMonitorFuseTrapRepeatCounter_Object = MibTableColumn
currentMonitorFuseTrapRepeatCounter = _CurrentMonitorFuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 4),
    _CurrentMonitorFuseTrapRepeatCounter_Type()
)
currentMonitorFuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentMonitorFuseTrapRepeatCounter.setStatus("current")


class _CurrentMonitorFuseAlarmEnable_Type(Integer32):
    """Custom type currentMonitorFuseAlarmEnable based on Integer32"""
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


_CurrentMonitorFuseAlarmEnable_Type.__name__ = "Integer32"
_CurrentMonitorFuseAlarmEnable_Object = MibTableColumn
currentMonitorFuseAlarmEnable = _CurrentMonitorFuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 5),
    _CurrentMonitorFuseAlarmEnable_Type()
)
currentMonitorFuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorFuseAlarmEnable.setStatus("current")
_CurrentMonitorFuseValue_Type = Integer32
_CurrentMonitorFuseValue_Object = MibTableColumn
currentMonitorFuseValue = _CurrentMonitorFuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 3, 1, 6),
    _CurrentMonitorFuseValue_Type()
)
currentMonitorFuseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorFuseValue.setStatus("current")
_CurrentMonitorCurrentTable_Object = MibTable
currentMonitorCurrentTable = _CurrentMonitorCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4)
)
if mibBuilder.loadTexts:
    currentMonitorCurrentTable.setStatus("current")
_CurrentMonitorCurrentEntry_Object = MibTableRow
currentMonitorCurrentEntry = _CurrentMonitorCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1)
)
currentMonitorCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorCurrentEntry.setStatus("current")


class _CurrentMonitorCurrentIndex_Type(Integer32):
    """Custom type currentMonitorCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CurrentMonitorCurrentIndex_Type.__name__ = "Integer32"
_CurrentMonitorCurrentIndex_Object = MibTableColumn
currentMonitorCurrentIndex = _CurrentMonitorCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 1),
    _CurrentMonitorCurrentIndex_Type()
)
currentMonitorCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorCurrentIndex.setStatus("current")


class _CurrentMonitorCurrentStatus_Type(Integer32):
    """Custom type currentMonitorCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_CurrentMonitorCurrentStatus_Type.__name__ = "Integer32"
_CurrentMonitorCurrentStatus_Object = MibTableColumn
currentMonitorCurrentStatus = _CurrentMonitorCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 2),
    _CurrentMonitorCurrentStatus_Type()
)
currentMonitorCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorCurrentStatus.setStatus("current")


class _CurrentMonitorCurrentDescription_Type(DisplayString):
    """Custom type currentMonitorCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CurrentMonitorCurrentDescription_Type.__name__ = "DisplayString"
_CurrentMonitorCurrentDescription_Object = MibTableColumn
currentMonitorCurrentDescription = _CurrentMonitorCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 3),
    _CurrentMonitorCurrentDescription_Type()
)
currentMonitorCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorCurrentDescription.setStatus("current")
_CurrentMonitorCurrentTrapRepeatCounter_Type = Counter32
_CurrentMonitorCurrentTrapRepeatCounter_Object = MibTableColumn
currentMonitorCurrentTrapRepeatCounter = _CurrentMonitorCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 4),
    _CurrentMonitorCurrentTrapRepeatCounter_Type()
)
currentMonitorCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentMonitorCurrentTrapRepeatCounter.setStatus("current")


class _CurrentMonitorCurrentAlarmEnable_Type(Integer32):
    """Custom type currentMonitorCurrentAlarmEnable based on Integer32"""
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


_CurrentMonitorCurrentAlarmEnable_Type.__name__ = "Integer32"
_CurrentMonitorCurrentAlarmEnable_Object = MibTableColumn
currentMonitorCurrentAlarmEnable = _CurrentMonitorCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 5),
    _CurrentMonitorCurrentAlarmEnable_Type()
)
currentMonitorCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorCurrentAlarmEnable.setStatus("current")
_CurrentMonitorCurrentValue_Type = Integer32
_CurrentMonitorCurrentValue_Object = MibTableColumn
currentMonitorCurrentValue = _CurrentMonitorCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 6),
    _CurrentMonitorCurrentValue_Type()
)
currentMonitorCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorCurrentValue.setStatus("current")
_CurrentMonitorCurrentMajorAlarmLevel_Type = Integer32
_CurrentMonitorCurrentMajorAlarmLevel_Object = MibTableColumn
currentMonitorCurrentMajorAlarmLevel = _CurrentMonitorCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 7),
    _CurrentMonitorCurrentMajorAlarmLevel_Type()
)
currentMonitorCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorCurrentMajorAlarmLevel.setStatus("current")
_CurrentMonitorCurrentMinorAlarmLevel_Type = Integer32
_CurrentMonitorCurrentMinorAlarmLevel_Object = MibTableColumn
currentMonitorCurrentMinorAlarmLevel = _CurrentMonitorCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 4, 1, 8),
    _CurrentMonitorCurrentMinorAlarmLevel_Type()
)
currentMonitorCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentMonitorCurrentMinorAlarmLevel.setStatus("current")
_CurrentMonitorEnergyLogAccumulatedTable_Object = MibTable
currentMonitorEnergyLogAccumulatedTable = _CurrentMonitorEnergyLogAccumulatedTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 5)
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogAccumulatedTable.setStatus("current")
_CurrentMonitorEnergyLogAccumulatedEntry_Object = MibTableRow
currentMonitorEnergyLogAccumulatedEntry = _CurrentMonitorEnergyLogAccumulatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 5, 1)
)
currentMonitorEnergyLogAccumulatedEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogAccumulatedEntry.setStatus("current")
_CurrentMonitorEnergyLogAccumulated_Type = Integer32
_CurrentMonitorEnergyLogAccumulated_Object = MibTableColumn
currentMonitorEnergyLogAccumulated = _CurrentMonitorEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 5, 1, 1),
    _CurrentMonitorEnergyLogAccumulated_Type()
)
currentMonitorEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogAccumulated.setStatus("current")


class _CurrentMonitorEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CurrentMonitorEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastHoursNumberOfEntries_Object = MibScalar
currentMonitorEnergyLogLastHoursNumberOfEntries = _CurrentMonitorEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 6),
    _CurrentMonitorEnergyLogLastHoursNumberOfEntries_Type()
)
currentMonitorEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursNumberOfEntries.setStatus("current")
_CurrentMonitorEnergyLogLastHoursTable_Object = MibTable
currentMonitorEnergyLogLastHoursTable = _CurrentMonitorEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 7)
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursTable.setStatus("current")
_CurrentMonitorEnergyLogLastHoursEntry_Object = MibTableRow
currentMonitorEnergyLogLastHoursEntry = _CurrentMonitorEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 7, 1)
)
currentMonitorEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
    (0, "SP2-MIB", "currentMonitorEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursEntry.setStatus("current")


class _CurrentMonitorEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_CurrentMonitorEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastHoursIndex_Object = MibTableColumn
currentMonitorEnergyLogLastHoursIndex = _CurrentMonitorEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 7, 1, 1),
    _CurrentMonitorEnergyLogLastHoursIndex_Type()
)
currentMonitorEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursIndex.setStatus("current")
_CurrentMonitorEnergyLogLastHoursValue_Type = Integer32
_CurrentMonitorEnergyLogLastHoursValue_Object = MibTableColumn
currentMonitorEnergyLogLastHoursValue = _CurrentMonitorEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 7, 1, 2),
    _CurrentMonitorEnergyLogLastHoursValue_Type()
)
currentMonitorEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastHoursValue.setStatus("current")


class _CurrentMonitorEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CurrentMonitorEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastDaysNumberOfEntries_Object = MibScalar
currentMonitorEnergyLogLastDaysNumberOfEntries = _CurrentMonitorEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 8),
    _CurrentMonitorEnergyLogLastDaysNumberOfEntries_Type()
)
currentMonitorEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysNumberOfEntries.setStatus("current")
_CurrentMonitorEnergyLogLastDaysTable_Object = MibTable
currentMonitorEnergyLogLastDaysTable = _CurrentMonitorEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 9)
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysTable.setStatus("current")
_CurrentMonitorEnergyLogLastDaysEntry_Object = MibTableRow
currentMonitorEnergyLogLastDaysEntry = _CurrentMonitorEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 9, 1)
)
currentMonitorEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
    (0, "SP2-MIB", "currentMonitorEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysEntry.setStatus("current")


class _CurrentMonitorEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_CurrentMonitorEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastDaysIndex_Object = MibTableColumn
currentMonitorEnergyLogLastDaysIndex = _CurrentMonitorEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 9, 1, 1),
    _CurrentMonitorEnergyLogLastDaysIndex_Type()
)
currentMonitorEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysIndex.setStatus("current")
_CurrentMonitorEnergyLogLastDaysValue_Type = Integer32
_CurrentMonitorEnergyLogLastDaysValue_Object = MibTableColumn
currentMonitorEnergyLogLastDaysValue = _CurrentMonitorEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 9, 1, 2),
    _CurrentMonitorEnergyLogLastDaysValue_Type()
)
currentMonitorEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastDaysValue.setStatus("current")


class _CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
currentMonitorEnergyLogLastWeeksNumberOfEntries = _CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 10),
    _CurrentMonitorEnergyLogLastWeeksNumberOfEntries_Type()
)
currentMonitorEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_CurrentMonitorEnergyLogLastWeeksTable_Object = MibTable
currentMonitorEnergyLogLastWeeksTable = _CurrentMonitorEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 11)
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksTable.setStatus("current")
_CurrentMonitorEnergyLogLastWeeksEntry_Object = MibTableRow
currentMonitorEnergyLogLastWeeksEntry = _CurrentMonitorEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 11, 1)
)
currentMonitorEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "currentMonitorIndex"),
    (0, "SP2-MIB", "currentMonitorCurrentIndex"),
    (0, "SP2-MIB", "currentMonitorEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksEntry.setStatus("current")


class _CurrentMonitorEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type currentMonitorEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_CurrentMonitorEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_CurrentMonitorEnergyLogLastWeeksIndex_Object = MibTableColumn
currentMonitorEnergyLogLastWeeksIndex = _CurrentMonitorEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 11, 1, 1),
    _CurrentMonitorEnergyLogLastWeeksIndex_Type()
)
currentMonitorEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksIndex.setStatus("current")
_CurrentMonitorEnergyLogLastWeeksValue_Type = Integer32
_CurrentMonitorEnergyLogLastWeeksValue_Object = MibTableColumn
currentMonitorEnergyLogLastWeeksValue = _CurrentMonitorEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 9, 11, 1, 2),
    _CurrentMonitorEnergyLogLastWeeksValue_Type()
)
currentMonitorEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMonitorEnergyLogLastWeeksValue.setStatus("current")
_FlexiMonitors_ObjectIdentity = ObjectIdentity
flexiMonitors = _FlexiMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10)
)


class _FlexiMonitorsNumberOfUnits_Type(Integer32):
    """Custom type flexiMonitorsNumberOfUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_FlexiMonitorsNumberOfUnits_Type.__name__ = "Integer32"
_FlexiMonitorsNumberOfUnits_Object = MibScalar
flexiMonitorsNumberOfUnits = _FlexiMonitorsNumberOfUnits_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 1),
    _FlexiMonitorsNumberOfUnits_Type()
)
flexiMonitorsNumberOfUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorsNumberOfUnits.setStatus("current")
_FlexiMonitorsTable_Object = MibTable
flexiMonitorsTable = _FlexiMonitorsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 2)
)
if mibBuilder.loadTexts:
    flexiMonitorsTable.setStatus("current")
_FlexiMonitorsEntry_Object = MibTableRow
flexiMonitorsEntry = _FlexiMonitorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 2, 1)
)
flexiMonitorsEntry.setIndexNames(
    (0, "SP2-MIB", "flexiMonitorIndex"),
)
if mibBuilder.loadTexts:
    flexiMonitorsEntry.setStatus("current")


class _FlexiMonitorIndex_Type(Integer32):
    """Custom type flexiMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_FlexiMonitorIndex_Type.__name__ = "Integer32"
_FlexiMonitorIndex_Object = MibTableColumn
flexiMonitorIndex = _FlexiMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 2, 1, 1),
    _FlexiMonitorIndex_Type()
)
flexiMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flexiMonitorIndex.setStatus("current")


class _FlexiMonitorType_Type(Integer32):
    """Custom type flexiMonitorType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("battFlexiMonitor", 1),
          ("loadFlexiMonitor", 2),
          ("rectFlexiMonitor", 3),
          ("contrFlexiMonitor", 4),
          ("dcdcFlexiMonitor", 5),
          ("solarFlexiMonitor", 6),
          ("windFlexiMonitor", 7),
          ("fuelcFlexiMonitor", 8))
    )


_FlexiMonitorType_Type.__name__ = "Integer32"
_FlexiMonitorType_Object = MibTableColumn
flexiMonitorType = _FlexiMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 2, 1, 2),
    _FlexiMonitorType_Type()
)
flexiMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorType.setStatus("current")
_FlexiMonitorId_Type = Integer32
_FlexiMonitorId_Object = MibTableColumn
flexiMonitorId = _FlexiMonitorId_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 2, 1, 3),
    _FlexiMonitorId_Type()
)
flexiMonitorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorId.setStatus("current")


class _FlexiMonitorNumberOfInputs_Type(Integer32):
    """Custom type flexiMonitorNumberOfInputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FlexiMonitorNumberOfInputs_Type.__name__ = "Integer32"
_FlexiMonitorNumberOfInputs_Object = MibTableColumn
flexiMonitorNumberOfInputs = _FlexiMonitorNumberOfInputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 2, 1, 4),
    _FlexiMonitorNumberOfInputs_Type()
)
flexiMonitorNumberOfInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorNumberOfInputs.setStatus("current")
_FlexiMonitorNumberOfOutputs_Type = Integer32
_FlexiMonitorNumberOfOutputs_Object = MibTableColumn
flexiMonitorNumberOfOutputs = _FlexiMonitorNumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 2, 1, 5),
    _FlexiMonitorNumberOfOutputs_Type()
)
flexiMonitorNumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorNumberOfOutputs.setStatus("current")
_FlexiMonitorInputTable_Object = MibTable
flexiMonitorInputTable = _FlexiMonitorInputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3)
)
if mibBuilder.loadTexts:
    flexiMonitorInputTable.setStatus("current")
_FlexiMonitorInputEntry_Object = MibTableRow
flexiMonitorInputEntry = _FlexiMonitorInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3, 1)
)
flexiMonitorInputEntry.setIndexNames(
    (0, "SP2-MIB", "flexiMonitorIndex"),
    (0, "SP2-MIB", "flexiMonitorInputIndex"),
)
if mibBuilder.loadTexts:
    flexiMonitorInputEntry.setStatus("current")


class _FlexiMonitorInputIndex_Type(Integer32):
    """Custom type flexiMonitorInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FlexiMonitorInputIndex_Type.__name__ = "Integer32"
_FlexiMonitorInputIndex_Object = MibTableColumn
flexiMonitorInputIndex = _FlexiMonitorInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3, 1, 1),
    _FlexiMonitorInputIndex_Type()
)
flexiMonitorInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flexiMonitorInputIndex.setStatus("current")


class _FlexiMonitorInputStatus_Type(Integer32):
    """Custom type flexiMonitorInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_FlexiMonitorInputStatus_Type.__name__ = "Integer32"
_FlexiMonitorInputStatus_Object = MibTableColumn
flexiMonitorInputStatus = _FlexiMonitorInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3, 1, 2),
    _FlexiMonitorInputStatus_Type()
)
flexiMonitorInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorInputStatus.setStatus("current")


class _FlexiMonitorInputDescription_Type(DisplayString):
    """Custom type flexiMonitorInputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FlexiMonitorInputDescription_Type.__name__ = "DisplayString"
_FlexiMonitorInputDescription_Object = MibTableColumn
flexiMonitorInputDescription = _FlexiMonitorInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3, 1, 3),
    _FlexiMonitorInputDescription_Type()
)
flexiMonitorInputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorInputDescription.setStatus("current")
_FlexiMonitorInputTrapRepeatCounter_Type = Counter32
_FlexiMonitorInputTrapRepeatCounter_Object = MibTableColumn
flexiMonitorInputTrapRepeatCounter = _FlexiMonitorInputTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3, 1, 4),
    _FlexiMonitorInputTrapRepeatCounter_Type()
)
flexiMonitorInputTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flexiMonitorInputTrapRepeatCounter.setStatus("current")


class _FlexiMonitorInputAlarmEnable_Type(Integer32):
    """Custom type flexiMonitorInputAlarmEnable based on Integer32"""
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


_FlexiMonitorInputAlarmEnable_Type.__name__ = "Integer32"
_FlexiMonitorInputAlarmEnable_Object = MibTableColumn
flexiMonitorInputAlarmEnable = _FlexiMonitorInputAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3, 1, 5),
    _FlexiMonitorInputAlarmEnable_Type()
)
flexiMonitorInputAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorInputAlarmEnable.setStatus("current")
_FlexiMonitorInputValue_Type = Integer32
_FlexiMonitorInputValue_Object = MibTableColumn
flexiMonitorInputValue = _FlexiMonitorInputValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3, 1, 6),
    _FlexiMonitorInputValue_Type()
)
flexiMonitorInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorInputValue.setStatus("current")


class _FlexiMonitorInputConfiguration_Type(Integer32):
    """Custom type flexiMonitorInputConfiguration based on Integer32"""
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
        *(("progIn-NormallyOpen", 1),
          ("progIn-NormallyClosed", 2),
          ("voltage", 3),
          ("temperature", 4),
          ("current", 5),
          ("speed", 6),
          ("fuse-NormallyOpen", 7),
          ("fuse-NormallyClosed", 8),
          ("fuse-DiodeMatrix", 9))
    )


_FlexiMonitorInputConfiguration_Type.__name__ = "Integer32"
_FlexiMonitorInputConfiguration_Object = MibTableColumn
flexiMonitorInputConfiguration = _FlexiMonitorInputConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 3, 1, 7),
    _FlexiMonitorInputConfiguration_Type()
)
flexiMonitorInputConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorInputConfiguration.setStatus("current")
_FlexiMonitorOutputTable_Object = MibTable
flexiMonitorOutputTable = _FlexiMonitorOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 4)
)
if mibBuilder.loadTexts:
    flexiMonitorOutputTable.setStatus("current")
_FlexiMonitorOutputEntry_Object = MibTableRow
flexiMonitorOutputEntry = _FlexiMonitorOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 4, 1)
)
flexiMonitorOutputEntry.setIndexNames(
    (0, "SP2-MIB", "flexiMonitorIndex"),
    (0, "SP2-MIB", "flexiMonitorOutputIndex"),
)
if mibBuilder.loadTexts:
    flexiMonitorOutputEntry.setStatus("current")


class _FlexiMonitorOutputIndex_Type(Integer32):
    """Custom type flexiMonitorOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FlexiMonitorOutputIndex_Type.__name__ = "Integer32"
_FlexiMonitorOutputIndex_Object = MibTableColumn
flexiMonitorOutputIndex = _FlexiMonitorOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 4, 1, 1),
    _FlexiMonitorOutputIndex_Type()
)
flexiMonitorOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flexiMonitorOutputIndex.setStatus("current")


class _FlexiMonitorOutputStatus_Type(Integer32):
    """Custom type flexiMonitorOutputStatus based on Integer32"""
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
        *(("notenergized", 0),
          ("energized", 1),
          ("disconnected", 2),
          ("connected", 3))
    )


_FlexiMonitorOutputStatus_Type.__name__ = "Integer32"
_FlexiMonitorOutputStatus_Object = MibTableColumn
flexiMonitorOutputStatus = _FlexiMonitorOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 4, 1, 2),
    _FlexiMonitorOutputStatus_Type()
)
flexiMonitorOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorOutputStatus.setStatus("current")
_FlexiMonitorOutputDescription_Type = DisplayString
_FlexiMonitorOutputDescription_Object = MibTableColumn
flexiMonitorOutputDescription = _FlexiMonitorOutputDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 10, 4, 1, 3),
    _FlexiMonitorOutputDescription_Type()
)
flexiMonitorOutputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorOutputDescription.setStatus("current")
_MainControlUnits_ObjectIdentity = ObjectIdentity
mainControlUnits = _MainControlUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11)
)
_MainControlUnitsTable_Object = MibTable
mainControlUnitsTable = _MainControlUnitsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 1)
)
if mibBuilder.loadTexts:
    mainControlUnitsTable.setStatus("current")
_MainControlUnitsEntry_Object = MibTableRow
mainControlUnitsEntry = _MainControlUnitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 1, 1)
)
mainControlUnitsEntry.setIndexNames(
    (0, "SP2-MIB", "mainControlUnitIndex"),
)
if mibBuilder.loadTexts:
    mainControlUnitsEntry.setStatus("current")


class _MainControlUnitIndex_Type(Integer32):
    """Custom type mainControlUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_MainControlUnitIndex_Type.__name__ = "Integer32"
_MainControlUnitIndex_Object = MibTableColumn
mainControlUnitIndex = _MainControlUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 1, 1, 1),
    _MainControlUnitIndex_Type()
)
mainControlUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainControlUnitIndex.setStatus("current")


class _MainControlUnitNumberOfTemperatures_Type(Integer32):
    """Custom type mainControlUnitNumberOfTemperatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_MainControlUnitNumberOfTemperatures_Type.__name__ = "Integer32"
_MainControlUnitNumberOfTemperatures_Object = MibTableColumn
mainControlUnitNumberOfTemperatures = _MainControlUnitNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 1, 1, 2),
    _MainControlUnitNumberOfTemperatures_Type()
)
mainControlUnitNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainControlUnitNumberOfTemperatures.setStatus("current")
_MainControlUnitTemperatureTable_Object = MibTable
mainControlUnitTemperatureTable = _MainControlUnitTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2)
)
if mibBuilder.loadTexts:
    mainControlUnitTemperatureTable.setStatus("current")
_MainControlUnitTemperatureEntry_Object = MibTableRow
mainControlUnitTemperatureEntry = _MainControlUnitTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1)
)
mainControlUnitTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "mainControlUnitIndex"),
    (0, "SP2-MIB", "mainControlUnitTemperatureIndex"),
)
if mibBuilder.loadTexts:
    mainControlUnitTemperatureEntry.setStatus("current")


class _MainControlUnitTemperatureIndex_Type(Integer32):
    """Custom type mainControlUnitTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_MainControlUnitTemperatureIndex_Type.__name__ = "Integer32"
_MainControlUnitTemperatureIndex_Object = MibTableColumn
mainControlUnitTemperatureIndex = _MainControlUnitTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 1),
    _MainControlUnitTemperatureIndex_Type()
)
mainControlUnitTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureIndex.setStatus("current")


class _MainControlUnitTemperatureStatus_Type(Integer32):
    """Custom type mainControlUnitTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainControlUnitTemperatureStatus_Type.__name__ = "Integer32"
_MainControlUnitTemperatureStatus_Object = MibTableColumn
mainControlUnitTemperatureStatus = _MainControlUnitTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 2),
    _MainControlUnitTemperatureStatus_Type()
)
mainControlUnitTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureStatus.setStatus("current")


class _MainControlUnitTemperatureDescription_Type(DisplayString):
    """Custom type mainControlUnitTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainControlUnitTemperatureDescription_Type.__name__ = "DisplayString"
_MainControlUnitTemperatureDescription_Object = MibTableColumn
mainControlUnitTemperatureDescription = _MainControlUnitTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 3),
    _MainControlUnitTemperatureDescription_Type()
)
mainControlUnitTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureDescription.setStatus("current")
_MainControlUnitTemperatureTrapRepeatCounter_Type = Counter32
_MainControlUnitTemperatureTrapRepeatCounter_Object = MibTableColumn
mainControlUnitTemperatureTrapRepeatCounter = _MainControlUnitTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 4),
    _MainControlUnitTemperatureTrapRepeatCounter_Type()
)
mainControlUnitTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureTrapRepeatCounter.setStatus("current")


class _MainControlUnitTemperatureAlarmEnable_Type(Integer32):
    """Custom type mainControlUnitTemperatureAlarmEnable based on Integer32"""
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


_MainControlUnitTemperatureAlarmEnable_Type.__name__ = "Integer32"
_MainControlUnitTemperatureAlarmEnable_Object = MibTableColumn
mainControlUnitTemperatureAlarmEnable = _MainControlUnitTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 5),
    _MainControlUnitTemperatureAlarmEnable_Type()
)
mainControlUnitTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureAlarmEnable.setStatus("current")
_MainControlUnitTemperatureValue_Type = Integer32
_MainControlUnitTemperatureValue_Object = MibTableColumn
mainControlUnitTemperatureValue = _MainControlUnitTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 6),
    _MainControlUnitTemperatureValue_Type()
)
mainControlUnitTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureValue.setStatus("current")
_MainControlUnitTemperatureMajorHighLevel_Type = Integer32
_MainControlUnitTemperatureMajorHighLevel_Object = MibTableColumn
mainControlUnitTemperatureMajorHighLevel = _MainControlUnitTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 7),
    _MainControlUnitTemperatureMajorHighLevel_Type()
)
mainControlUnitTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureMajorHighLevel.setStatus("current")
_MainControlUnitTemperatureMinorHighLevel_Type = Integer32
_MainControlUnitTemperatureMinorHighLevel_Object = MibTableColumn
mainControlUnitTemperatureMinorHighLevel = _MainControlUnitTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 8),
    _MainControlUnitTemperatureMinorHighLevel_Type()
)
mainControlUnitTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureMinorHighLevel.setStatus("current")
_MainControlUnitTemperatureMinorLowLevel_Type = Integer32
_MainControlUnitTemperatureMinorLowLevel_Object = MibTableColumn
mainControlUnitTemperatureMinorLowLevel = _MainControlUnitTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 9),
    _MainControlUnitTemperatureMinorLowLevel_Type()
)
mainControlUnitTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureMinorLowLevel.setStatus("current")
_MainControlUnitTemperatureMajorLowLevel_Type = Integer32
_MainControlUnitTemperatureMajorLowLevel_Object = MibTableColumn
mainControlUnitTemperatureMajorLowLevel = _MainControlUnitTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 2, 1, 10),
    _MainControlUnitTemperatureMajorLowLevel_Type()
)
mainControlUnitTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitTemperatureMajorLowLevel.setStatus("current")
_MainControlUnitEarthFaultTable_Object = MibTable
mainControlUnitEarthFaultTable = _MainControlUnitEarthFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 3)
)
if mibBuilder.loadTexts:
    mainControlUnitEarthFaultTable.setStatus("current")
_MainControlUnitEarthFaultEntry_Object = MibTableRow
mainControlUnitEarthFaultEntry = _MainControlUnitEarthFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 3, 1)
)
mainControlUnitEarthFaultEntry.setIndexNames(
    (0, "SP2-MIB", "mainControlUnitIndex"),
)
if mibBuilder.loadTexts:
    mainControlUnitEarthFaultEntry.setStatus("current")


class _MainControlUnitEarthFaultStatus_Type(Integer32):
    """Custom type mainControlUnitEarthFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainControlUnitEarthFaultStatus_Type.__name__ = "Integer32"
_MainControlUnitEarthFaultStatus_Object = MibTableColumn
mainControlUnitEarthFaultStatus = _MainControlUnitEarthFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 3, 1, 1),
    _MainControlUnitEarthFaultStatus_Type()
)
mainControlUnitEarthFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainControlUnitEarthFaultStatus.setStatus("current")


class _MainControlUnitEarthFaultDescription_Type(DisplayString):
    """Custom type mainControlUnitEarthFaultDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainControlUnitEarthFaultDescription_Type.__name__ = "DisplayString"
_MainControlUnitEarthFaultDescription_Object = MibTableColumn
mainControlUnitEarthFaultDescription = _MainControlUnitEarthFaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 3, 1, 2),
    _MainControlUnitEarthFaultDescription_Type()
)
mainControlUnitEarthFaultDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitEarthFaultDescription.setStatus("current")
_MainControlUnitEarthFaultTrapRepeatCounter_Type = Integer32
_MainControlUnitEarthFaultTrapRepeatCounter_Object = MibTableColumn
mainControlUnitEarthFaultTrapRepeatCounter = _MainControlUnitEarthFaultTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 3, 1, 3),
    _MainControlUnitEarthFaultTrapRepeatCounter_Type()
)
mainControlUnitEarthFaultTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainControlUnitEarthFaultTrapRepeatCounter.setStatus("current")


class _MainControlUnitEarthFaultAlarmEnable_Type(Integer32):
    """Custom type mainControlUnitEarthFaultAlarmEnable based on Integer32"""
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


_MainControlUnitEarthFaultAlarmEnable_Type.__name__ = "Integer32"
_MainControlUnitEarthFaultAlarmEnable_Object = MibTableColumn
mainControlUnitEarthFaultAlarmEnable = _MainControlUnitEarthFaultAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 3, 1, 4),
    _MainControlUnitEarthFaultAlarmEnable_Type()
)
mainControlUnitEarthFaultAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitEarthFaultAlarmEnable.setStatus("current")
_MainControlUnitEarthFaultValue_Type = Integer32
_MainControlUnitEarthFaultValue_Object = MibTableColumn
mainControlUnitEarthFaultValue = _MainControlUnitEarthFaultValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 3, 1, 5),
    _MainControlUnitEarthFaultValue_Type()
)
mainControlUnitEarthFaultValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainControlUnitEarthFaultValue.setStatus("current")
_MainControlUnitEarthFaultMajorAlarmLevel_Type = Integer32
_MainControlUnitEarthFaultMajorAlarmLevel_Object = MibTableColumn
mainControlUnitEarthFaultMajorAlarmLevel = _MainControlUnitEarthFaultMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 11, 3, 1, 6),
    _MainControlUnitEarthFaultMajorAlarmLevel_Type()
)
mainControlUnitEarthFaultMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitEarthFaultMajorAlarmLevel.setStatus("current")
_ControlSystemSummary_ObjectIdentity = ObjectIdentity
controlSystemSummary = _ControlSystemSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12)
)
_MainControlUnitsError_ObjectIdentity = ObjectIdentity
mainControlUnitsError = _MainControlUnitsError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 1)
)


class _MainControlUnitsErrorStatus_Type(Integer32):
    """Custom type mainControlUnitsErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainControlUnitsErrorStatus_Type.__name__ = "Integer32"
_MainControlUnitsErrorStatus_Object = MibScalar
mainControlUnitsErrorStatus = _MainControlUnitsErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 1, 1),
    _MainControlUnitsErrorStatus_Type()
)
mainControlUnitsErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainControlUnitsErrorStatus.setStatus("current")


class _MainControlUnitsErrorDescription_Type(DisplayString):
    """Custom type mainControlUnitsErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainControlUnitsErrorDescription_Type.__name__ = "DisplayString"
_MainControlUnitsErrorDescription_Object = MibScalar
mainControlUnitsErrorDescription = _MainControlUnitsErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 1, 2),
    _MainControlUnitsErrorDescription_Type()
)
mainControlUnitsErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitsErrorDescription.setStatus("current")
_MainControlUnitsErrorTrapRepeatCounter_Type = Integer32
_MainControlUnitsErrorTrapRepeatCounter_Object = MibScalar
mainControlUnitsErrorTrapRepeatCounter = _MainControlUnitsErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 1, 3),
    _MainControlUnitsErrorTrapRepeatCounter_Type()
)
mainControlUnitsErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainControlUnitsErrorTrapRepeatCounter.setStatus("current")


class _MainControlUnitsErrorAlarmEnable_Type(Integer32):
    """Custom type mainControlUnitsErrorAlarmEnable based on Integer32"""
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


_MainControlUnitsErrorAlarmEnable_Type.__name__ = "Integer32"
_MainControlUnitsErrorAlarmEnable_Object = MibScalar
mainControlUnitsErrorAlarmEnable = _MainControlUnitsErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 1, 4),
    _MainControlUnitsErrorAlarmEnable_Type()
)
mainControlUnitsErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitsErrorAlarmEnable.setStatus("current")
_MainControlUnitsErrorValue_Type = Integer32
_MainControlUnitsErrorValue_Object = MibScalar
mainControlUnitsErrorValue = _MainControlUnitsErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 1, 5),
    _MainControlUnitsErrorValue_Type()
)
mainControlUnitsErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainControlUnitsErrorValue.setStatus("current")
_MainControlUnitsErrorMajorAlarmLevel_Type = Integer32
_MainControlUnitsErrorMajorAlarmLevel_Object = MibScalar
mainControlUnitsErrorMajorAlarmLevel = _MainControlUnitsErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 1, 6),
    _MainControlUnitsErrorMajorAlarmLevel_Type()
)
mainControlUnitsErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitsErrorMajorAlarmLevel.setStatus("current")
_MainControlUnitsErrorMinorAlarmLevel_Type = Integer32
_MainControlUnitsErrorMinorAlarmLevel_Object = MibScalar
mainControlUnitsErrorMinorAlarmLevel = _MainControlUnitsErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 1, 7),
    _MainControlUnitsErrorMinorAlarmLevel_Type()
)
mainControlUnitsErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainControlUnitsErrorMinorAlarmLevel.setStatus("current")
_SmartNodeError_ObjectIdentity = ObjectIdentity
smartNodeError = _SmartNodeError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 2)
)


class _SmartNodeErrorStatus_Type(Integer32):
    """Custom type smartNodeErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_SmartNodeErrorStatus_Type.__name__ = "Integer32"
_SmartNodeErrorStatus_Object = MibScalar
smartNodeErrorStatus = _SmartNodeErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 2, 1),
    _SmartNodeErrorStatus_Type()
)
smartNodeErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartNodeErrorStatus.setStatus("current")


class _SmartNodeErrorDescription_Type(DisplayString):
    """Custom type smartNodeErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SmartNodeErrorDescription_Type.__name__ = "DisplayString"
_SmartNodeErrorDescription_Object = MibScalar
smartNodeErrorDescription = _SmartNodeErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 2, 2),
    _SmartNodeErrorDescription_Type()
)
smartNodeErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartNodeErrorDescription.setStatus("current")
_SmartNodeErrorTrapRepeatCounter_Type = Integer32
_SmartNodeErrorTrapRepeatCounter_Object = MibScalar
smartNodeErrorTrapRepeatCounter = _SmartNodeErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 2, 3),
    _SmartNodeErrorTrapRepeatCounter_Type()
)
smartNodeErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smartNodeErrorTrapRepeatCounter.setStatus("current")


class _SmartNodeErrorAlarmEnable_Type(Integer32):
    """Custom type smartNodeErrorAlarmEnable based on Integer32"""
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


_SmartNodeErrorAlarmEnable_Type.__name__ = "Integer32"
_SmartNodeErrorAlarmEnable_Object = MibScalar
smartNodeErrorAlarmEnable = _SmartNodeErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 2, 4),
    _SmartNodeErrorAlarmEnable_Type()
)
smartNodeErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartNodeErrorAlarmEnable.setStatus("current")
_SmartNodeErrorValue_Type = Integer32
_SmartNodeErrorValue_Object = MibScalar
smartNodeErrorValue = _SmartNodeErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 2, 5),
    _SmartNodeErrorValue_Type()
)
smartNodeErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartNodeErrorValue.setStatus("current")
_SmartNodeErrorMajorAlarmLevel_Type = Integer32
_SmartNodeErrorMajorAlarmLevel_Object = MibScalar
smartNodeErrorMajorAlarmLevel = _SmartNodeErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 2, 6),
    _SmartNodeErrorMajorAlarmLevel_Type()
)
smartNodeErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartNodeErrorMajorAlarmLevel.setStatus("current")
_SmartNodeErrorMinorAlarmLevel_Type = Integer32
_SmartNodeErrorMinorAlarmLevel_Object = MibScalar
smartNodeErrorMinorAlarmLevel = _SmartNodeErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 2, 7),
    _SmartNodeErrorMinorAlarmLevel_Type()
)
smartNodeErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smartNodeErrorMinorAlarmLevel.setStatus("current")
_BatteryMonitorError_ObjectIdentity = ObjectIdentity
batteryMonitorError = _BatteryMonitorError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 3)
)


class _BatteryMonitorErrorStatus_Type(Integer32):
    """Custom type batteryMonitorErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryMonitorErrorStatus_Type.__name__ = "Integer32"
_BatteryMonitorErrorStatus_Object = MibScalar
batteryMonitorErrorStatus = _BatteryMonitorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 3, 1),
    _BatteryMonitorErrorStatus_Type()
)
batteryMonitorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorErrorStatus.setStatus("current")


class _BatteryMonitorErrorDescription_Type(DisplayString):
    """Custom type batteryMonitorErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryMonitorErrorDescription_Type.__name__ = "DisplayString"
_BatteryMonitorErrorDescription_Object = MibScalar
batteryMonitorErrorDescription = _BatteryMonitorErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 3, 2),
    _BatteryMonitorErrorDescription_Type()
)
batteryMonitorErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorErrorDescription.setStatus("current")
_BatteryMonitorErrorTrapRepeatCounter_Type = Integer32
_BatteryMonitorErrorTrapRepeatCounter_Object = MibScalar
batteryMonitorErrorTrapRepeatCounter = _BatteryMonitorErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 3, 3),
    _BatteryMonitorErrorTrapRepeatCounter_Type()
)
batteryMonitorErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryMonitorErrorTrapRepeatCounter.setStatus("current")


class _BatteryMonitorErrorAlarmEnable_Type(Integer32):
    """Custom type batteryMonitorErrorAlarmEnable based on Integer32"""
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


_BatteryMonitorErrorAlarmEnable_Type.__name__ = "Integer32"
_BatteryMonitorErrorAlarmEnable_Object = MibScalar
batteryMonitorErrorAlarmEnable = _BatteryMonitorErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 3, 4),
    _BatteryMonitorErrorAlarmEnable_Type()
)
batteryMonitorErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorErrorAlarmEnable.setStatus("current")
_BatteryMonitorErrorValue_Type = Integer32
_BatteryMonitorErrorValue_Object = MibScalar
batteryMonitorErrorValue = _BatteryMonitorErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 3, 5),
    _BatteryMonitorErrorValue_Type()
)
batteryMonitorErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryMonitorErrorValue.setStatus("current")
_BatteryMonitorErrorMajorAlarmLevel_Type = Integer32
_BatteryMonitorErrorMajorAlarmLevel_Object = MibScalar
batteryMonitorErrorMajorAlarmLevel = _BatteryMonitorErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 3, 6),
    _BatteryMonitorErrorMajorAlarmLevel_Type()
)
batteryMonitorErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorErrorMajorAlarmLevel.setStatus("current")
_BatteryMonitorErrorMinorAlarmLevel_Type = Integer32
_BatteryMonitorErrorMinorAlarmLevel_Object = MibScalar
batteryMonitorErrorMinorAlarmLevel = _BatteryMonitorErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 3, 7),
    _BatteryMonitorErrorMinorAlarmLevel_Type()
)
batteryMonitorErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryMonitorErrorMinorAlarmLevel.setStatus("current")
_LoadMonitorError_ObjectIdentity = ObjectIdentity
loadMonitorError = _LoadMonitorError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 4)
)


class _LoadMonitorErrorStatus_Type(Integer32):
    """Custom type loadMonitorErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_LoadMonitorErrorStatus_Type.__name__ = "Integer32"
_LoadMonitorErrorStatus_Object = MibScalar
loadMonitorErrorStatus = _LoadMonitorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 4, 1),
    _LoadMonitorErrorStatus_Type()
)
loadMonitorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorErrorStatus.setStatus("current")


class _LoadMonitorErrorDescription_Type(DisplayString):
    """Custom type loadMonitorErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LoadMonitorErrorDescription_Type.__name__ = "DisplayString"
_LoadMonitorErrorDescription_Object = MibScalar
loadMonitorErrorDescription = _LoadMonitorErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 4, 2),
    _LoadMonitorErrorDescription_Type()
)
loadMonitorErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadMonitorErrorDescription.setStatus("current")
_LoadMonitorErrorTrapRepeatCounter_Type = Integer32
_LoadMonitorErrorTrapRepeatCounter_Object = MibScalar
loadMonitorErrorTrapRepeatCounter = _LoadMonitorErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 4, 3),
    _LoadMonitorErrorTrapRepeatCounter_Type()
)
loadMonitorErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    loadMonitorErrorTrapRepeatCounter.setStatus("current")


class _LoadMonitorErrorAlarmEnable_Type(Integer32):
    """Custom type loadMonitorErrorAlarmEnable based on Integer32"""
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


_LoadMonitorErrorAlarmEnable_Type.__name__ = "Integer32"
_LoadMonitorErrorAlarmEnable_Object = MibScalar
loadMonitorErrorAlarmEnable = _LoadMonitorErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 4, 4),
    _LoadMonitorErrorAlarmEnable_Type()
)
loadMonitorErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadMonitorErrorAlarmEnable.setStatus("current")
_LoadMonitorErrorValue_Type = Integer32
_LoadMonitorErrorValue_Object = MibScalar
loadMonitorErrorValue = _LoadMonitorErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 4, 5),
    _LoadMonitorErrorValue_Type()
)
loadMonitorErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadMonitorErrorValue.setStatus("current")
_LoadMonitorErrorMajorAlarmLevel_Type = Integer32
_LoadMonitorErrorMajorAlarmLevel_Object = MibScalar
loadMonitorErrorMajorAlarmLevel = _LoadMonitorErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 4, 6),
    _LoadMonitorErrorMajorAlarmLevel_Type()
)
loadMonitorErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadMonitorErrorMajorAlarmLevel.setStatus("current")
_LoadMonitorErrorMinorAlarmLevel_Type = Integer32
_LoadMonitorErrorMinorAlarmLevel_Object = MibScalar
loadMonitorErrorMinorAlarmLevel = _LoadMonitorErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 4, 7),
    _LoadMonitorErrorMinorAlarmLevel_Type()
)
loadMonitorErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadMonitorErrorMinorAlarmLevel.setStatus("current")
_IoUnitError_ObjectIdentity = ObjectIdentity
ioUnitError = _IoUnitError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 5)
)


class _IoUnitErrorStatus_Type(Integer32):
    """Custom type ioUnitErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_IoUnitErrorStatus_Type.__name__ = "Integer32"
_IoUnitErrorStatus_Object = MibScalar
ioUnitErrorStatus = _IoUnitErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 5, 1),
    _IoUnitErrorStatus_Type()
)
ioUnitErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitErrorStatus.setStatus("current")


class _IoUnitErrorDescription_Type(DisplayString):
    """Custom type ioUnitErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IoUnitErrorDescription_Type.__name__ = "DisplayString"
_IoUnitErrorDescription_Object = MibScalar
ioUnitErrorDescription = _IoUnitErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 5, 2),
    _IoUnitErrorDescription_Type()
)
ioUnitErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioUnitErrorDescription.setStatus("current")
_IoUnitErrorTrapRepeatCounter_Type = Integer32
_IoUnitErrorTrapRepeatCounter_Object = MibScalar
ioUnitErrorTrapRepeatCounter = _IoUnitErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 5, 3),
    _IoUnitErrorTrapRepeatCounter_Type()
)
ioUnitErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ioUnitErrorTrapRepeatCounter.setStatus("current")


class _IoUnitErrorAlarmEnable_Type(Integer32):
    """Custom type ioUnitErrorAlarmEnable based on Integer32"""
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


_IoUnitErrorAlarmEnable_Type.__name__ = "Integer32"
_IoUnitErrorAlarmEnable_Object = MibScalar
ioUnitErrorAlarmEnable = _IoUnitErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 5, 4),
    _IoUnitErrorAlarmEnable_Type()
)
ioUnitErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioUnitErrorAlarmEnable.setStatus("current")
_IoUnitErrorValue_Type = Integer32
_IoUnitErrorValue_Object = MibScalar
ioUnitErrorValue = _IoUnitErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 5, 5),
    _IoUnitErrorValue_Type()
)
ioUnitErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioUnitErrorValue.setStatus("current")
_IoUnitErrorMajorAlarmLevel_Type = Integer32
_IoUnitErrorMajorAlarmLevel_Object = MibScalar
ioUnitErrorMajorAlarmLevel = _IoUnitErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 5, 6),
    _IoUnitErrorMajorAlarmLevel_Type()
)
ioUnitErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioUnitErrorMajorAlarmLevel.setStatus("current")
_IoUnitErrorMinorAlarmLevel_Type = Integer32
_IoUnitErrorMinorAlarmLevel_Object = MibScalar
ioUnitErrorMinorAlarmLevel = _IoUnitErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 5, 7),
    _IoUnitErrorMinorAlarmLevel_Type()
)
ioUnitErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ioUnitErrorMinorAlarmLevel.setStatus("current")
_MainsMonitorError_ObjectIdentity = ObjectIdentity
mainsMonitorError = _MainsMonitorError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 6)
)


class _MainsMonitorErrorStatus_Type(Integer32):
    """Custom type mainsMonitorErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_MainsMonitorErrorStatus_Type.__name__ = "Integer32"
_MainsMonitorErrorStatus_Object = MibScalar
mainsMonitorErrorStatus = _MainsMonitorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 6, 1),
    _MainsMonitorErrorStatus_Type()
)
mainsMonitorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorErrorStatus.setStatus("current")


class _MainsMonitorErrorDescription_Type(DisplayString):
    """Custom type mainsMonitorErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MainsMonitorErrorDescription_Type.__name__ = "DisplayString"
_MainsMonitorErrorDescription_Object = MibScalar
mainsMonitorErrorDescription = _MainsMonitorErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 6, 2),
    _MainsMonitorErrorDescription_Type()
)
mainsMonitorErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorErrorDescription.setStatus("current")
_MainsMonitorErrorTrapRepeatCounter_Type = Integer32
_MainsMonitorErrorTrapRepeatCounter_Object = MibScalar
mainsMonitorErrorTrapRepeatCounter = _MainsMonitorErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 6, 3),
    _MainsMonitorErrorTrapRepeatCounter_Type()
)
mainsMonitorErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mainsMonitorErrorTrapRepeatCounter.setStatus("current")


class _MainsMonitorErrorAlarmEnable_Type(Integer32):
    """Custom type mainsMonitorErrorAlarmEnable based on Integer32"""
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


_MainsMonitorErrorAlarmEnable_Type.__name__ = "Integer32"
_MainsMonitorErrorAlarmEnable_Object = MibScalar
mainsMonitorErrorAlarmEnable = _MainsMonitorErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 6, 4),
    _MainsMonitorErrorAlarmEnable_Type()
)
mainsMonitorErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorErrorAlarmEnable.setStatus("current")
_MainsMonitorErrorValue_Type = Integer32
_MainsMonitorErrorValue_Object = MibScalar
mainsMonitorErrorValue = _MainsMonitorErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 6, 5),
    _MainsMonitorErrorValue_Type()
)
mainsMonitorErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainsMonitorErrorValue.setStatus("current")
_MainsMonitorErrorMajorAlarmLevel_Type = Integer32
_MainsMonitorErrorMajorAlarmLevel_Object = MibScalar
mainsMonitorErrorMajorAlarmLevel = _MainsMonitorErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 6, 6),
    _MainsMonitorErrorMajorAlarmLevel_Type()
)
mainsMonitorErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorErrorMajorAlarmLevel.setStatus("current")
_MainsMonitorErrorMinorAlarmLevel_Type = Integer32
_MainsMonitorErrorMinorAlarmLevel_Object = MibScalar
mainsMonitorErrorMinorAlarmLevel = _MainsMonitorErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 6, 7),
    _MainsMonitorErrorMinorAlarmLevel_Type()
)
mainsMonitorErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mainsMonitorErrorMinorAlarmLevel.setStatus("current")
_FlexiMonitorError_ObjectIdentity = ObjectIdentity
flexiMonitorError = _FlexiMonitorError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 7)
)


class _FlexiMonitorErrorStatus_Type(Integer32):
    """Custom type flexiMonitorErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_FlexiMonitorErrorStatus_Type.__name__ = "Integer32"
_FlexiMonitorErrorStatus_Object = MibScalar
flexiMonitorErrorStatus = _FlexiMonitorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 7, 1),
    _FlexiMonitorErrorStatus_Type()
)
flexiMonitorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorErrorStatus.setStatus("current")


class _FlexiMonitorErrorDescription_Type(DisplayString):
    """Custom type flexiMonitorErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FlexiMonitorErrorDescription_Type.__name__ = "DisplayString"
_FlexiMonitorErrorDescription_Object = MibScalar
flexiMonitorErrorDescription = _FlexiMonitorErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 7, 2),
    _FlexiMonitorErrorDescription_Type()
)
flexiMonitorErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorErrorDescription.setStatus("current")
_FlexiMonitorErrorTrapRepeatCounter_Type = Integer32
_FlexiMonitorErrorTrapRepeatCounter_Object = MibScalar
flexiMonitorErrorTrapRepeatCounter = _FlexiMonitorErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 7, 3),
    _FlexiMonitorErrorTrapRepeatCounter_Type()
)
flexiMonitorErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    flexiMonitorErrorTrapRepeatCounter.setStatus("current")


class _FlexiMonitorErrorAlarmEnable_Type(Integer32):
    """Custom type flexiMonitorErrorAlarmEnable based on Integer32"""
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


_FlexiMonitorErrorAlarmEnable_Type.__name__ = "Integer32"
_FlexiMonitorErrorAlarmEnable_Object = MibScalar
flexiMonitorErrorAlarmEnable = _FlexiMonitorErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 7, 4),
    _FlexiMonitorErrorAlarmEnable_Type()
)
flexiMonitorErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorErrorAlarmEnable.setStatus("current")
_FlexiMonitorErrorValue_Type = Integer32
_FlexiMonitorErrorValue_Object = MibScalar
flexiMonitorErrorValue = _FlexiMonitorErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 7, 5),
    _FlexiMonitorErrorValue_Type()
)
flexiMonitorErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexiMonitorErrorValue.setStatus("current")
_FlexiMonitorErrorMajorAlarmLevel_Type = Integer32
_FlexiMonitorErrorMajorAlarmLevel_Object = MibScalar
flexiMonitorErrorMajorAlarmLevel = _FlexiMonitorErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 7, 6),
    _FlexiMonitorErrorMajorAlarmLevel_Type()
)
flexiMonitorErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorErrorMajorAlarmLevel.setStatus("current")
_FlexiMonitorErrorMinorAlarmLevel_Type = Integer32
_FlexiMonitorErrorMinorAlarmLevel_Object = MibScalar
flexiMonitorErrorMinorAlarmLevel = _FlexiMonitorErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 12, 7, 7),
    _FlexiMonitorErrorMinorAlarmLevel_Type()
)
flexiMonitorErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexiMonitorErrorMinorAlarmLevel.setStatus("current")
_AmbientTemperature_ObjectIdentity = ObjectIdentity
ambientTemperature = _AmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13)
)


class _AmbientTemperatureStatus_Type(Integer32):
    """Custom type ambientTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_AmbientTemperatureStatus_Type.__name__ = "Integer32"
_AmbientTemperatureStatus_Object = MibScalar
ambientTemperatureStatus = _AmbientTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 1),
    _AmbientTemperatureStatus_Type()
)
ambientTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientTemperatureStatus.setStatus("current")


class _AmbientTemperatureDescription_Type(DisplayString):
    """Custom type ambientTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AmbientTemperatureDescription_Type.__name__ = "DisplayString"
_AmbientTemperatureDescription_Object = MibScalar
ambientTemperatureDescription = _AmbientTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 2),
    _AmbientTemperatureDescription_Type()
)
ambientTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ambientTemperatureDescription.setStatus("current")
_AmbientTemperatureTrapRepeatCounter_Type = Counter32
_AmbientTemperatureTrapRepeatCounter_Object = MibScalar
ambientTemperatureTrapRepeatCounter = _AmbientTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 3),
    _AmbientTemperatureTrapRepeatCounter_Type()
)
ambientTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ambientTemperatureTrapRepeatCounter.setStatus("current")


class _AmbientTemperatureAlarmEnable_Type(Integer32):
    """Custom type ambientTemperatureAlarmEnable based on Integer32"""
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


_AmbientTemperatureAlarmEnable_Type.__name__ = "Integer32"
_AmbientTemperatureAlarmEnable_Object = MibScalar
ambientTemperatureAlarmEnable = _AmbientTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 4),
    _AmbientTemperatureAlarmEnable_Type()
)
ambientTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ambientTemperatureAlarmEnable.setStatus("current")


class _AmbientTemperatureValue_Type(Integer32):
    """Custom type ambientTemperatureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_AmbientTemperatureValue_Type.__name__ = "Integer32"
_AmbientTemperatureValue_Object = MibScalar
ambientTemperatureValue = _AmbientTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 5),
    _AmbientTemperatureValue_Type()
)
ambientTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ambientTemperatureValue.setStatus("current")
_AmbientTemperatureMajorHighLevel_Type = Integer32
_AmbientTemperatureMajorHighLevel_Object = MibScalar
ambientTemperatureMajorHighLevel = _AmbientTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 6),
    _AmbientTemperatureMajorHighLevel_Type()
)
ambientTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ambientTemperatureMajorHighLevel.setStatus("current")
_AmbientTemperatureMinorHighLevel_Type = Integer32
_AmbientTemperatureMinorHighLevel_Object = MibScalar
ambientTemperatureMinorHighLevel = _AmbientTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 7),
    _AmbientTemperatureMinorHighLevel_Type()
)
ambientTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ambientTemperatureMinorHighLevel.setStatus("current")
_AmbientTemperatureMinorLowLevel_Type = Integer32
_AmbientTemperatureMinorLowLevel_Object = MibScalar
ambientTemperatureMinorLowLevel = _AmbientTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 8),
    _AmbientTemperatureMinorLowLevel_Type()
)
ambientTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ambientTemperatureMinorLowLevel.setStatus("current")
_AmbientTemperatureMajorLowLevel_Type = Integer32
_AmbientTemperatureMajorLowLevel_Object = MibScalar
ambientTemperatureMajorLowLevel = _AmbientTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 13, 9),
    _AmbientTemperatureMajorLowLevel_Type()
)
ambientTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ambientTemperatureMajorLowLevel.setStatus("current")
_DeltaTemperature_ObjectIdentity = ObjectIdentity
deltaTemperature = _DeltaTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14)
)


class _DeltaTemperatureStatus_Type(Integer32):
    """Custom type deltaTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_DeltaTemperatureStatus_Type.__name__ = "Integer32"
_DeltaTemperatureStatus_Object = MibScalar
deltaTemperatureStatus = _DeltaTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 1),
    _DeltaTemperatureStatus_Type()
)
deltaTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deltaTemperatureStatus.setStatus("current")


class _DeltaTemperatureDescription_Type(DisplayString):
    """Custom type deltaTemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeltaTemperatureDescription_Type.__name__ = "DisplayString"
_DeltaTemperatureDescription_Object = MibScalar
deltaTemperatureDescription = _DeltaTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 2),
    _DeltaTemperatureDescription_Type()
)
deltaTemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deltaTemperatureDescription.setStatus("current")
_DeltaTemperatureTrapRepeatCounter_Type = Counter32
_DeltaTemperatureTrapRepeatCounter_Object = MibScalar
deltaTemperatureTrapRepeatCounter = _DeltaTemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 3),
    _DeltaTemperatureTrapRepeatCounter_Type()
)
deltaTemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deltaTemperatureTrapRepeatCounter.setStatus("current")


class _DeltaTemperatureAlarmEnable_Type(Integer32):
    """Custom type deltaTemperatureAlarmEnable based on Integer32"""
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


_DeltaTemperatureAlarmEnable_Type.__name__ = "Integer32"
_DeltaTemperatureAlarmEnable_Object = MibScalar
deltaTemperatureAlarmEnable = _DeltaTemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 4),
    _DeltaTemperatureAlarmEnable_Type()
)
deltaTemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deltaTemperatureAlarmEnable.setStatus("current")


class _DeltaTemperatureValue_Type(Integer32):
    """Custom type deltaTemperatureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_DeltaTemperatureValue_Type.__name__ = "Integer32"
_DeltaTemperatureValue_Object = MibScalar
deltaTemperatureValue = _DeltaTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 5),
    _DeltaTemperatureValue_Type()
)
deltaTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deltaTemperatureValue.setStatus("current")
_DeltaTemperatureMajorHighLevel_Type = Integer32
_DeltaTemperatureMajorHighLevel_Object = MibScalar
deltaTemperatureMajorHighLevel = _DeltaTemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 6),
    _DeltaTemperatureMajorHighLevel_Type()
)
deltaTemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deltaTemperatureMajorHighLevel.setStatus("current")
_DeltaTemperatureMinorHighLevel_Type = Integer32
_DeltaTemperatureMinorHighLevel_Object = MibScalar
deltaTemperatureMinorHighLevel = _DeltaTemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 7),
    _DeltaTemperatureMinorHighLevel_Type()
)
deltaTemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deltaTemperatureMinorHighLevel.setStatus("current")
_DeltaTemperatureMinorLowLevel_Type = Integer32
_DeltaTemperatureMinorLowLevel_Object = MibScalar
deltaTemperatureMinorLowLevel = _DeltaTemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 8),
    _DeltaTemperatureMinorLowLevel_Type()
)
deltaTemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deltaTemperatureMinorLowLevel.setStatus("current")
_DeltaTemperatureMajorLowLevel_Type = Integer32
_DeltaTemperatureMajorLowLevel_Object = MibScalar
deltaTemperatureMajorLowLevel = _DeltaTemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 14, 9),
    _DeltaTemperatureMajorLowLevel_Type()
)
deltaTemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deltaTemperatureMajorLowLevel.setStatus("current")
_UserSuspended_ObjectIdentity = ObjectIdentity
userSuspended = _UserSuspended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 15)
)


class _UserSuspendedStatus_Type(Integer32):
    """Custom type userSuspendedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_UserSuspendedStatus_Type.__name__ = "Integer32"
_UserSuspendedStatus_Object = MibScalar
userSuspendedStatus = _UserSuspendedStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 15, 1),
    _UserSuspendedStatus_Type()
)
userSuspendedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSuspendedStatus.setStatus("current")


class _UserSuspendedDescription_Type(DisplayString):
    """Custom type userSuspendedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UserSuspendedDescription_Type.__name__ = "DisplayString"
_UserSuspendedDescription_Object = MibScalar
userSuspendedDescription = _UserSuspendedDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 15, 2),
    _UserSuspendedDescription_Type()
)
userSuspendedDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSuspendedDescription.setStatus("current")
_UserSuspendedTrapRepeatCounter_Type = Integer32
_UserSuspendedTrapRepeatCounter_Object = MibScalar
userSuspendedTrapRepeatCounter = _UserSuspendedTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 15, 3),
    _UserSuspendedTrapRepeatCounter_Type()
)
userSuspendedTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    userSuspendedTrapRepeatCounter.setStatus("current")


class _UserSuspendedAlarmEnable_Type(Integer32):
    """Custom type userSuspendedAlarmEnable based on Integer32"""
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


_UserSuspendedAlarmEnable_Type.__name__ = "Integer32"
_UserSuspendedAlarmEnable_Object = MibScalar
userSuspendedAlarmEnable = _UserSuspendedAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 15, 4),
    _UserSuspendedAlarmEnable_Type()
)
userSuspendedAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSuspendedAlarmEnable.setStatus("current")
_UserSuspendedValue_Type = Integer32
_UserSuspendedValue_Object = MibScalar
userSuspendedValue = _UserSuspendedValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 15, 5),
    _UserSuspendedValue_Type()
)
userSuspendedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userSuspendedValue.setStatus("current")
_UserSuspendedMajorAlarmLevel_Type = Integer32
_UserSuspendedMajorAlarmLevel_Object = MibScalar
userSuspendedMajorAlarmLevel = _UserSuspendedMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 13, 15, 6),
    _UserSuspendedMajorAlarmLevel_Type()
)
userSuspendedMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userSuspendedMajorAlarmLevel.setStatus("current")
_AlarmGroups_ObjectIdentity = ObjectIdentity
alarmGroups = _AlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14)
)
_AlarmGroupTable_Object = MibTable
alarmGroupTable = _AlarmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1)
)
if mibBuilder.loadTexts:
    alarmGroupTable.setStatus("current")
_AlarmGroupEntry_Object = MibTableRow
alarmGroupEntry = _AlarmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1, 1)
)
alarmGroupEntry.setIndexNames(
    (0, "SP2-MIB", "alarmGroupIndex"),
)
if mibBuilder.loadTexts:
    alarmGroupEntry.setStatus("current")


class _AlarmGroupIndex_Type(Integer32):
    """Custom type alarmGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49),
    )


_AlarmGroupIndex_Type.__name__ = "Integer32"
_AlarmGroupIndex_Object = MibTableColumn
alarmGroupIndex = _AlarmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1, 1, 1),
    _AlarmGroupIndex_Type()
)
alarmGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmGroupIndex.setStatus("current")


class _AlarmGroupStatus_Type(Integer32):
    """Custom type alarmGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("alarm", 1))
    )


_AlarmGroupStatus_Type.__name__ = "Integer32"
_AlarmGroupStatus_Object = MibTableColumn
alarmGroupStatus = _AlarmGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1, 1, 2),
    _AlarmGroupStatus_Type()
)
alarmGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmGroupStatus.setStatus("current")


class _AlarmGroupDescription_Type(DisplayString):
    """Custom type alarmGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AlarmGroupDescription_Type.__name__ = "DisplayString"
_AlarmGroupDescription_Object = MibTableColumn
alarmGroupDescription = _AlarmGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 14, 1, 1, 3),
    _AlarmGroupDescription_Type()
)
alarmGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmGroupDescription.setStatus("current")
_BatteryGroup2_ObjectIdentity = ObjectIdentity
batteryGroup2 = _BatteryGroup2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15)
)


class _BatteryGroup2Status_Type(Integer32):
    """Custom type batteryGroup2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2Status_Type.__name__ = "Integer32"
_BatteryGroup2Status_Object = MibScalar
batteryGroup2Status = _BatteryGroup2Status_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 1),
    _BatteryGroup2Status_Type()
)
batteryGroup2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2Status.setStatus("current")


class _BatteryGroup2Description_Type(DisplayString):
    """Custom type batteryGroup2Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BatteryGroup2Description_Type.__name__ = "DisplayString"
_BatteryGroup2Description_Object = MibScalar
batteryGroup2Description = _BatteryGroup2Description_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 2),
    _BatteryGroup2Description_Type()
)
batteryGroup2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2Description.setStatus("current")


class _BatteryGroup2ReferenceVoltage_Type(Integer32):
    """Custom type batteryGroup2ReferenceVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(840, 60417),
    )


_BatteryGroup2ReferenceVoltage_Type.__name__ = "Integer32"
_BatteryGroup2ReferenceVoltage_Object = MibScalar
batteryGroup2ReferenceVoltage = _BatteryGroup2ReferenceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 3),
    _BatteryGroup2ReferenceVoltage_Type()
)
batteryGroup2ReferenceVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2ReferenceVoltage.setStatus("current")


class _BatteryGroup2FusesStatus_Type(Integer32):
    """Custom type batteryGroup2FusesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2FusesStatus_Type.__name__ = "Integer32"
_BatteryGroup2FusesStatus_Object = MibScalar
batteryGroup2FusesStatus = _BatteryGroup2FusesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 4),
    _BatteryGroup2FusesStatus_Type()
)
batteryGroup2FusesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2FusesStatus.setStatus("current")
_BatteryGroup2Voltage_ObjectIdentity = ObjectIdentity
batteryGroup2Voltage = _BatteryGroup2Voltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5)
)


class _BatteryGroup2VoltageStatus_Type(Integer32):
    """Custom type batteryGroup2VoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2VoltageStatus_Type.__name__ = "Integer32"
_BatteryGroup2VoltageStatus_Object = MibScalar
batteryGroup2VoltageStatus = _BatteryGroup2VoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 1),
    _BatteryGroup2VoltageStatus_Type()
)
batteryGroup2VoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2VoltageStatus.setStatus("current")


class _BatteryGroup2VoltageDescription_Type(DisplayString):
    """Custom type batteryGroup2VoltageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2VoltageDescription_Type.__name__ = "DisplayString"
_BatteryGroup2VoltageDescription_Object = MibScalar
batteryGroup2VoltageDescription = _BatteryGroup2VoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 2),
    _BatteryGroup2VoltageDescription_Type()
)
batteryGroup2VoltageDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2VoltageDescription.setStatus("current")
_BatteryGroup2VoltageTrapRepeatCounter_Type = Counter32
_BatteryGroup2VoltageTrapRepeatCounter_Object = MibScalar
batteryGroup2VoltageTrapRepeatCounter = _BatteryGroup2VoltageTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 3),
    _BatteryGroup2VoltageTrapRepeatCounter_Type()
)
batteryGroup2VoltageTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2VoltageTrapRepeatCounter.setStatus("current")


class _BatteryGroup2VoltageAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2VoltageAlarmEnable based on Integer32"""
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


_BatteryGroup2VoltageAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2VoltageAlarmEnable_Object = MibScalar
batteryGroup2VoltageAlarmEnable = _BatteryGroup2VoltageAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 4),
    _BatteryGroup2VoltageAlarmEnable_Type()
)
batteryGroup2VoltageAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2VoltageAlarmEnable.setStatus("current")


class _BatteryGroup2VoltageValue_Type(Integer32):
    """Custom type batteryGroup2VoltageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7500),
    )


_BatteryGroup2VoltageValue_Type.__name__ = "Integer32"
_BatteryGroup2VoltageValue_Object = MibScalar
batteryGroup2VoltageValue = _BatteryGroup2VoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 5),
    _BatteryGroup2VoltageValue_Type()
)
batteryGroup2VoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2VoltageValue.setStatus("current")
_BatteryGroup2VoltageMajorHighLevel_Type = Integer32
_BatteryGroup2VoltageMajorHighLevel_Object = MibScalar
batteryGroup2VoltageMajorHighLevel = _BatteryGroup2VoltageMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 6),
    _BatteryGroup2VoltageMajorHighLevel_Type()
)
batteryGroup2VoltageMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2VoltageMajorHighLevel.setStatus("current")
_BatteryGroup2VoltageMinorHighLevel_Type = Integer32
_BatteryGroup2VoltageMinorHighLevel_Object = MibScalar
batteryGroup2VoltageMinorHighLevel = _BatteryGroup2VoltageMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 7),
    _BatteryGroup2VoltageMinorHighLevel_Type()
)
batteryGroup2VoltageMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2VoltageMinorHighLevel.setStatus("current")
_BatteryGroup2VoltageMinorLowLevel_Type = Integer32
_BatteryGroup2VoltageMinorLowLevel_Object = MibScalar
batteryGroup2VoltageMinorLowLevel = _BatteryGroup2VoltageMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 8),
    _BatteryGroup2VoltageMinorLowLevel_Type()
)
batteryGroup2VoltageMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2VoltageMinorLowLevel.setStatus("current")
_BatteryGroup2VoltageMajorLowLevel_Type = Integer32
_BatteryGroup2VoltageMajorLowLevel_Object = MibScalar
batteryGroup2VoltageMajorLowLevel = _BatteryGroup2VoltageMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 5, 9),
    _BatteryGroup2VoltageMajorLowLevel_Type()
)
batteryGroup2VoltageMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2VoltageMajorLowLevel.setStatus("current")
_BatteryGroup2Currents_ObjectIdentity = ObjectIdentity
batteryGroup2Currents = _BatteryGroup2Currents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6)
)


class _BatteryGroup2CurrentsStatus_Type(Integer32):
    """Custom type batteryGroup2CurrentsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2CurrentsStatus_Type.__name__ = "Integer32"
_BatteryGroup2CurrentsStatus_Object = MibScalar
batteryGroup2CurrentsStatus = _BatteryGroup2CurrentsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 1),
    _BatteryGroup2CurrentsStatus_Type()
)
batteryGroup2CurrentsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsStatus.setStatus("current")


class _BatteryGroup2CurrentsDescription_Type(DisplayString):
    """Custom type batteryGroup2CurrentsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2CurrentsDescription_Type.__name__ = "DisplayString"
_BatteryGroup2CurrentsDescription_Object = MibScalar
batteryGroup2CurrentsDescription = _BatteryGroup2CurrentsDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 2),
    _BatteryGroup2CurrentsDescription_Type()
)
batteryGroup2CurrentsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsDescription.setStatus("current")
_BatteryGroup2CurrentsTrapRepeatCounter_Type = Counter32
_BatteryGroup2CurrentsTrapRepeatCounter_Object = MibScalar
batteryGroup2CurrentsTrapRepeatCounter = _BatteryGroup2CurrentsTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 3),
    _BatteryGroup2CurrentsTrapRepeatCounter_Type()
)
batteryGroup2CurrentsTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsTrapRepeatCounter.setStatus("current")


class _BatteryGroup2CurrentsAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2CurrentsAlarmEnable based on Integer32"""
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


_BatteryGroup2CurrentsAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2CurrentsAlarmEnable_Object = MibScalar
batteryGroup2CurrentsAlarmEnable = _BatteryGroup2CurrentsAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 4),
    _BatteryGroup2CurrentsAlarmEnable_Type()
)
batteryGroup2CurrentsAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsAlarmEnable.setStatus("current")
_BatteryGroup2CurrentsValue_Type = Integer32
_BatteryGroup2CurrentsValue_Object = MibScalar
batteryGroup2CurrentsValue = _BatteryGroup2CurrentsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 5),
    _BatteryGroup2CurrentsValue_Type()
)
batteryGroup2CurrentsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsValue.setStatus("current")
_BatteryGroup2CurrentsMajorHighLevel_Type = Integer32
_BatteryGroup2CurrentsMajorHighLevel_Object = MibScalar
batteryGroup2CurrentsMajorHighLevel = _BatteryGroup2CurrentsMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 6),
    _BatteryGroup2CurrentsMajorHighLevel_Type()
)
batteryGroup2CurrentsMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsMajorHighLevel.setStatus("current")
_BatteryGroup2CurrentsMinorHighLevel_Type = Integer32
_BatteryGroup2CurrentsMinorHighLevel_Object = MibScalar
batteryGroup2CurrentsMinorHighLevel = _BatteryGroup2CurrentsMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 7),
    _BatteryGroup2CurrentsMinorHighLevel_Type()
)
batteryGroup2CurrentsMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsMinorHighLevel.setStatus("current")
_BatteryGroup2CurrentsMinorLowLevel_Type = Integer32
_BatteryGroup2CurrentsMinorLowLevel_Object = MibScalar
batteryGroup2CurrentsMinorLowLevel = _BatteryGroup2CurrentsMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 8),
    _BatteryGroup2CurrentsMinorLowLevel_Type()
)
batteryGroup2CurrentsMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsMinorLowLevel.setStatus("current")
_BatteryGroup2CurrentsMajorLowLevel_Type = Integer32
_BatteryGroup2CurrentsMajorLowLevel_Object = MibScalar
batteryGroup2CurrentsMajorLowLevel = _BatteryGroup2CurrentsMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 6, 9),
    _BatteryGroup2CurrentsMajorLowLevel_Type()
)
batteryGroup2CurrentsMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentsMajorLowLevel.setStatus("current")
_BatteryGroup2Temperatures_ObjectIdentity = ObjectIdentity
batteryGroup2Temperatures = _BatteryGroup2Temperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7)
)


class _BatteryGroup2TemperaturesStatus_Type(Integer32):
    """Custom type batteryGroup2TemperaturesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2TemperaturesStatus_Type.__name__ = "Integer32"
_BatteryGroup2TemperaturesStatus_Object = MibScalar
batteryGroup2TemperaturesStatus = _BatteryGroup2TemperaturesStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 1),
    _BatteryGroup2TemperaturesStatus_Type()
)
batteryGroup2TemperaturesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesStatus.setStatus("current")


class _BatteryGroup2TemperaturesDescription_Type(DisplayString):
    """Custom type batteryGroup2TemperaturesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2TemperaturesDescription_Type.__name__ = "DisplayString"
_BatteryGroup2TemperaturesDescription_Object = MibScalar
batteryGroup2TemperaturesDescription = _BatteryGroup2TemperaturesDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 2),
    _BatteryGroup2TemperaturesDescription_Type()
)
batteryGroup2TemperaturesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesDescription.setStatus("current")
_BatteryGroup2TemperaturesTrapRepeatCounter_Type = Counter32
_BatteryGroup2TemperaturesTrapRepeatCounter_Object = MibScalar
batteryGroup2TemperaturesTrapRepeatCounter = _BatteryGroup2TemperaturesTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 3),
    _BatteryGroup2TemperaturesTrapRepeatCounter_Type()
)
batteryGroup2TemperaturesTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesTrapRepeatCounter.setStatus("current")


class _BatteryGroup2TemperaturesAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2TemperaturesAlarmEnable based on Integer32"""
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


_BatteryGroup2TemperaturesAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2TemperaturesAlarmEnable_Object = MibScalar
batteryGroup2TemperaturesAlarmEnable = _BatteryGroup2TemperaturesAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 4),
    _BatteryGroup2TemperaturesAlarmEnable_Type()
)
batteryGroup2TemperaturesAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesAlarmEnable.setStatus("current")


class _BatteryGroup2TemperaturesValue_Type(Integer32):
    """Custom type batteryGroup2TemperaturesValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_BatteryGroup2TemperaturesValue_Type.__name__ = "Integer32"
_BatteryGroup2TemperaturesValue_Object = MibScalar
batteryGroup2TemperaturesValue = _BatteryGroup2TemperaturesValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 5),
    _BatteryGroup2TemperaturesValue_Type()
)
batteryGroup2TemperaturesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesValue.setStatus("current")
_BatteryGroup2TemperaturesMajorHighLevel_Type = Integer32
_BatteryGroup2TemperaturesMajorHighLevel_Object = MibScalar
batteryGroup2TemperaturesMajorHighLevel = _BatteryGroup2TemperaturesMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 6),
    _BatteryGroup2TemperaturesMajorHighLevel_Type()
)
batteryGroup2TemperaturesMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesMajorHighLevel.setStatus("current")
_BatteryGroup2TemperaturesMinorHighLevel_Type = Integer32
_BatteryGroup2TemperaturesMinorHighLevel_Object = MibScalar
batteryGroup2TemperaturesMinorHighLevel = _BatteryGroup2TemperaturesMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 7),
    _BatteryGroup2TemperaturesMinorHighLevel_Type()
)
batteryGroup2TemperaturesMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesMinorHighLevel.setStatus("current")
_BatteryGroup2TemperaturesMinorLowLevel_Type = Integer32
_BatteryGroup2TemperaturesMinorLowLevel_Object = MibScalar
batteryGroup2TemperaturesMinorLowLevel = _BatteryGroup2TemperaturesMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 8),
    _BatteryGroup2TemperaturesMinorLowLevel_Type()
)
batteryGroup2TemperaturesMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesMinorLowLevel.setStatus("current")
_BatteryGroup2TemperaturesMajorLowLevel_Type = Integer32
_BatteryGroup2TemperaturesMajorLowLevel_Object = MibScalar
batteryGroup2TemperaturesMajorLowLevel = _BatteryGroup2TemperaturesMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 7, 9),
    _BatteryGroup2TemperaturesMajorLowLevel_Type()
)
batteryGroup2TemperaturesMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperaturesMajorLowLevel.setStatus("current")
_BatteryGroup2TimeLeft_ObjectIdentity = ObjectIdentity
batteryGroup2TimeLeft = _BatteryGroup2TimeLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 8)
)


class _BatteryGroup2TimeLeftStatus_Type(Integer32):
    """Custom type batteryGroup2TimeLeftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2TimeLeftStatus_Type.__name__ = "Integer32"
_BatteryGroup2TimeLeftStatus_Object = MibScalar
batteryGroup2TimeLeftStatus = _BatteryGroup2TimeLeftStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 8, 1),
    _BatteryGroup2TimeLeftStatus_Type()
)
batteryGroup2TimeLeftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TimeLeftStatus.setStatus("current")


class _BatteryGroup2TimeLeftDescription_Type(DisplayString):
    """Custom type batteryGroup2TimeLeftDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2TimeLeftDescription_Type.__name__ = "DisplayString"
_BatteryGroup2TimeLeftDescription_Object = MibScalar
batteryGroup2TimeLeftDescription = _BatteryGroup2TimeLeftDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 8, 2),
    _BatteryGroup2TimeLeftDescription_Type()
)
batteryGroup2TimeLeftDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TimeLeftDescription.setStatus("current")
_BatteryGroup2TimeLeftTrapRepeatCounter_Type = Counter32
_BatteryGroup2TimeLeftTrapRepeatCounter_Object = MibScalar
batteryGroup2TimeLeftTrapRepeatCounter = _BatteryGroup2TimeLeftTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 8, 3),
    _BatteryGroup2TimeLeftTrapRepeatCounter_Type()
)
batteryGroup2TimeLeftTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2TimeLeftTrapRepeatCounter.setStatus("current")


class _BatteryGroup2TimeLeftAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2TimeLeftAlarmEnable based on Integer32"""
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


_BatteryGroup2TimeLeftAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2TimeLeftAlarmEnable_Object = MibScalar
batteryGroup2TimeLeftAlarmEnable = _BatteryGroup2TimeLeftAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 8, 4),
    _BatteryGroup2TimeLeftAlarmEnable_Type()
)
batteryGroup2TimeLeftAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TimeLeftAlarmEnable.setStatus("current")
_BatteryGroup2TimeLeftValue_Type = Integer32
_BatteryGroup2TimeLeftValue_Object = MibScalar
batteryGroup2TimeLeftValue = _BatteryGroup2TimeLeftValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 8, 5),
    _BatteryGroup2TimeLeftValue_Type()
)
batteryGroup2TimeLeftValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TimeLeftValue.setStatus("current")
_BatteryGroup2TimeLeftMinorAlarmLevel_Type = Integer32
_BatteryGroup2TimeLeftMinorAlarmLevel_Object = MibScalar
batteryGroup2TimeLeftMinorAlarmLevel = _BatteryGroup2TimeLeftMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 8, 6),
    _BatteryGroup2TimeLeftMinorAlarmLevel_Type()
)
batteryGroup2TimeLeftMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TimeLeftMinorAlarmLevel.setStatus("current")
_BatteryGroup2TimeLeftMajorAlarmLevel_Type = Integer32
_BatteryGroup2TimeLeftMajorAlarmLevel_Object = MibScalar
batteryGroup2TimeLeftMajorAlarmLevel = _BatteryGroup2TimeLeftMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 8, 7),
    _BatteryGroup2TimeLeftMajorAlarmLevel_Type()
)
batteryGroup2TimeLeftMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TimeLeftMajorAlarmLevel.setStatus("current")
_BatteryGroup2RemainingCapacity_ObjectIdentity = ObjectIdentity
batteryGroup2RemainingCapacity = _BatteryGroup2RemainingCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 9)
)


class _BatteryGroup2RemainingCapacityStatus_Type(Integer32):
    """Custom type batteryGroup2RemainingCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2RemainingCapacityStatus_Type.__name__ = "Integer32"
_BatteryGroup2RemainingCapacityStatus_Object = MibScalar
batteryGroup2RemainingCapacityStatus = _BatteryGroup2RemainingCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 9, 1),
    _BatteryGroup2RemainingCapacityStatus_Type()
)
batteryGroup2RemainingCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2RemainingCapacityStatus.setStatus("current")


class _BatteryGroup2RemainingCapacityDescription_Type(DisplayString):
    """Custom type batteryGroup2RemainingCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2RemainingCapacityDescription_Type.__name__ = "DisplayString"
_BatteryGroup2RemainingCapacityDescription_Object = MibScalar
batteryGroup2RemainingCapacityDescription = _BatteryGroup2RemainingCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 9, 2),
    _BatteryGroup2RemainingCapacityDescription_Type()
)
batteryGroup2RemainingCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2RemainingCapacityDescription.setStatus("current")
_BatteryGroup2RemainingCapacityTrapRepeatCounter_Type = Counter32
_BatteryGroup2RemainingCapacityTrapRepeatCounter_Object = MibScalar
batteryGroup2RemainingCapacityTrapRepeatCounter = _BatteryGroup2RemainingCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 9, 3),
    _BatteryGroup2RemainingCapacityTrapRepeatCounter_Type()
)
batteryGroup2RemainingCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2RemainingCapacityTrapRepeatCounter.setStatus("current")


class _BatteryGroup2RemainingCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2RemainingCapacityAlarmEnable based on Integer32"""
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


_BatteryGroup2RemainingCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2RemainingCapacityAlarmEnable_Object = MibScalar
batteryGroup2RemainingCapacityAlarmEnable = _BatteryGroup2RemainingCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 9, 4),
    _BatteryGroup2RemainingCapacityAlarmEnable_Type()
)
batteryGroup2RemainingCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2RemainingCapacityAlarmEnable.setStatus("current")
_BatteryGroup2RemainingCapacityValue_Type = Integer32
_BatteryGroup2RemainingCapacityValue_Object = MibScalar
batteryGroup2RemainingCapacityValue = _BatteryGroup2RemainingCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 9, 5),
    _BatteryGroup2RemainingCapacityValue_Type()
)
batteryGroup2RemainingCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2RemainingCapacityValue.setStatus("current")
_BatteryGroup2RemainingCapacityMinorLowLevel_Type = Integer32
_BatteryGroup2RemainingCapacityMinorLowLevel_Object = MibScalar
batteryGroup2RemainingCapacityMinorLowLevel = _BatteryGroup2RemainingCapacityMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 9, 6),
    _BatteryGroup2RemainingCapacityMinorLowLevel_Type()
)
batteryGroup2RemainingCapacityMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2RemainingCapacityMinorLowLevel.setStatus("current")
_BatteryGroup2RemainingCapacityMajorLowLevel_Type = Integer32
_BatteryGroup2RemainingCapacityMajorLowLevel_Object = MibScalar
batteryGroup2RemainingCapacityMajorLowLevel = _BatteryGroup2RemainingCapacityMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 9, 7),
    _BatteryGroup2RemainingCapacityMajorLowLevel_Type()
)
batteryGroup2RemainingCapacityMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2RemainingCapacityMajorLowLevel.setStatus("current")
_BatteryGroup2UsedCapacity_ObjectIdentity = ObjectIdentity
batteryGroup2UsedCapacity = _BatteryGroup2UsedCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 10)
)


class _BatteryGroup2UsedCapacityStatus_Type(Integer32):
    """Custom type batteryGroup2UsedCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2UsedCapacityStatus_Type.__name__ = "Integer32"
_BatteryGroup2UsedCapacityStatus_Object = MibScalar
batteryGroup2UsedCapacityStatus = _BatteryGroup2UsedCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 10, 1),
    _BatteryGroup2UsedCapacityStatus_Type()
)
batteryGroup2UsedCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2UsedCapacityStatus.setStatus("current")


class _BatteryGroup2UsedCapacityDescription_Type(DisplayString):
    """Custom type batteryGroup2UsedCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2UsedCapacityDescription_Type.__name__ = "DisplayString"
_BatteryGroup2UsedCapacityDescription_Object = MibScalar
batteryGroup2UsedCapacityDescription = _BatteryGroup2UsedCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 10, 2),
    _BatteryGroup2UsedCapacityDescription_Type()
)
batteryGroup2UsedCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2UsedCapacityDescription.setStatus("current")
_BatteryGroup2UsedCapacityTrapRepeatCounter_Type = Counter32
_BatteryGroup2UsedCapacityTrapRepeatCounter_Object = MibScalar
batteryGroup2UsedCapacityTrapRepeatCounter = _BatteryGroup2UsedCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 10, 3),
    _BatteryGroup2UsedCapacityTrapRepeatCounter_Type()
)
batteryGroup2UsedCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2UsedCapacityTrapRepeatCounter.setStatus("current")


class _BatteryGroup2UsedCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2UsedCapacityAlarmEnable based on Integer32"""
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


_BatteryGroup2UsedCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2UsedCapacityAlarmEnable_Object = MibScalar
batteryGroup2UsedCapacityAlarmEnable = _BatteryGroup2UsedCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 10, 4),
    _BatteryGroup2UsedCapacityAlarmEnable_Type()
)
batteryGroup2UsedCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2UsedCapacityAlarmEnable.setStatus("current")
_BatteryGroup2UsedCapacityValue_Type = Integer32
_BatteryGroup2UsedCapacityValue_Object = MibScalar
batteryGroup2UsedCapacityValue = _BatteryGroup2UsedCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 10, 5),
    _BatteryGroup2UsedCapacityValue_Type()
)
batteryGroup2UsedCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2UsedCapacityValue.setStatus("current")
_BatteryGroup2UsedCapacityMajorAlarmLevel_Type = Integer32
_BatteryGroup2UsedCapacityMajorAlarmLevel_Object = MibScalar
batteryGroup2UsedCapacityMajorAlarmLevel = _BatteryGroup2UsedCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 10, 6),
    _BatteryGroup2UsedCapacityMajorAlarmLevel_Type()
)
batteryGroup2UsedCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2UsedCapacityMajorAlarmLevel.setStatus("current")
_BatteryGroup2UsedCapacityMinorAlarmLevel_Type = Integer32
_BatteryGroup2UsedCapacityMinorAlarmLevel_Object = MibScalar
batteryGroup2UsedCapacityMinorAlarmLevel = _BatteryGroup2UsedCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 10, 7),
    _BatteryGroup2UsedCapacityMinorAlarmLevel_Type()
)
batteryGroup2UsedCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2UsedCapacityMinorAlarmLevel.setStatus("current")
_BatteryGroup2TotalCapacity_ObjectIdentity = ObjectIdentity
batteryGroup2TotalCapacity = _BatteryGroup2TotalCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 11)
)


class _BatteryGroup2TotalCapacityStatus_Type(Integer32):
    """Custom type batteryGroup2TotalCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2TotalCapacityStatus_Type.__name__ = "Integer32"
_BatteryGroup2TotalCapacityStatus_Object = MibScalar
batteryGroup2TotalCapacityStatus = _BatteryGroup2TotalCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 11, 1),
    _BatteryGroup2TotalCapacityStatus_Type()
)
batteryGroup2TotalCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TotalCapacityStatus.setStatus("current")


class _BatteryGroup2TotalCapacityDescription_Type(DisplayString):
    """Custom type batteryGroup2TotalCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2TotalCapacityDescription_Type.__name__ = "DisplayString"
_BatteryGroup2TotalCapacityDescription_Object = MibScalar
batteryGroup2TotalCapacityDescription = _BatteryGroup2TotalCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 11, 2),
    _BatteryGroup2TotalCapacityDescription_Type()
)
batteryGroup2TotalCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TotalCapacityDescription.setStatus("current")
_BatteryGroup2TotalCapacityTrapRepeatCounter_Type = Counter32
_BatteryGroup2TotalCapacityTrapRepeatCounter_Object = MibScalar
batteryGroup2TotalCapacityTrapRepeatCounter = _BatteryGroup2TotalCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 11, 3),
    _BatteryGroup2TotalCapacityTrapRepeatCounter_Type()
)
batteryGroup2TotalCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2TotalCapacityTrapRepeatCounter.setStatus("current")


class _BatteryGroup2TotalCapacityAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2TotalCapacityAlarmEnable based on Integer32"""
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


_BatteryGroup2TotalCapacityAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2TotalCapacityAlarmEnable_Object = MibScalar
batteryGroup2TotalCapacityAlarmEnable = _BatteryGroup2TotalCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 11, 4),
    _BatteryGroup2TotalCapacityAlarmEnable_Type()
)
batteryGroup2TotalCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TotalCapacityAlarmEnable.setStatus("current")
_BatteryGroup2TotalCapacityValue_Type = Integer32
_BatteryGroup2TotalCapacityValue_Object = MibScalar
batteryGroup2TotalCapacityValue = _BatteryGroup2TotalCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 11, 5),
    _BatteryGroup2TotalCapacityValue_Type()
)
batteryGroup2TotalCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TotalCapacityValue.setStatus("current")
_BatteryGroup2TotalCapacityMinorLowLevel_Type = Integer32
_BatteryGroup2TotalCapacityMinorLowLevel_Object = MibScalar
batteryGroup2TotalCapacityMinorLowLevel = _BatteryGroup2TotalCapacityMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 11, 6),
    _BatteryGroup2TotalCapacityMinorLowLevel_Type()
)
batteryGroup2TotalCapacityMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TotalCapacityMinorLowLevel.setStatus("current")
_BatteryGroup2TotalCapacityMajorLowLevel_Type = Integer32
_BatteryGroup2TotalCapacityMajorLowLevel_Object = MibScalar
batteryGroup2TotalCapacityMajorLowLevel = _BatteryGroup2TotalCapacityMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 11, 7),
    _BatteryGroup2TotalCapacityMajorLowLevel_Type()
)
batteryGroup2TotalCapacityMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TotalCapacityMajorLowLevel.setStatus("current")
_BatteryGroup2Quality_ObjectIdentity = ObjectIdentity
batteryGroup2Quality = _BatteryGroup2Quality_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 12)
)


class _BatteryGroup2QualityStatus_Type(Integer32):
    """Custom type batteryGroup2QualityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2QualityStatus_Type.__name__ = "Integer32"
_BatteryGroup2QualityStatus_Object = MibScalar
batteryGroup2QualityStatus = _BatteryGroup2QualityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 12, 1),
    _BatteryGroup2QualityStatus_Type()
)
batteryGroup2QualityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2QualityStatus.setStatus("current")


class _BatteryGroup2QualityDescription_Type(DisplayString):
    """Custom type batteryGroup2QualityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2QualityDescription_Type.__name__ = "DisplayString"
_BatteryGroup2QualityDescription_Object = MibScalar
batteryGroup2QualityDescription = _BatteryGroup2QualityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 12, 2),
    _BatteryGroup2QualityDescription_Type()
)
batteryGroup2QualityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2QualityDescription.setStatus("current")
_BatteryGroup2QualityTrapRepeatCounter_Type = Counter32
_BatteryGroup2QualityTrapRepeatCounter_Object = MibScalar
batteryGroup2QualityTrapRepeatCounter = _BatteryGroup2QualityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 12, 3),
    _BatteryGroup2QualityTrapRepeatCounter_Type()
)
batteryGroup2QualityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2QualityTrapRepeatCounter.setStatus("current")


class _BatteryGroup2QualityAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2QualityAlarmEnable based on Integer32"""
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


_BatteryGroup2QualityAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2QualityAlarmEnable_Object = MibScalar
batteryGroup2QualityAlarmEnable = _BatteryGroup2QualityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 12, 4),
    _BatteryGroup2QualityAlarmEnable_Type()
)
batteryGroup2QualityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2QualityAlarmEnable.setStatus("current")
_BatteryGroup2QualityValue_Type = Integer32
_BatteryGroup2QualityValue_Object = MibScalar
batteryGroup2QualityValue = _BatteryGroup2QualityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 12, 5),
    _BatteryGroup2QualityValue_Type()
)
batteryGroup2QualityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2QualityValue.setStatus("current")
_BatteryGroup2QualityMinorAlarmLevel_Type = Integer32
_BatteryGroup2QualityMinorAlarmLevel_Object = MibScalar
batteryGroup2QualityMinorAlarmLevel = _BatteryGroup2QualityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 12, 6),
    _BatteryGroup2QualityMinorAlarmLevel_Type()
)
batteryGroup2QualityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2QualityMinorAlarmLevel.setStatus("current")
_BatteryGroup2QualityMajorAlarmLevel_Type = Integer32
_BatteryGroup2QualityMajorAlarmLevel_Object = MibScalar
batteryGroup2QualityMajorAlarmLevel = _BatteryGroup2QualityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 12, 7),
    _BatteryGroup2QualityMajorAlarmLevel_Type()
)
batteryGroup2QualityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2QualityMajorAlarmLevel.setStatus("current")
_BatteryGroup2LVBD_ObjectIdentity = ObjectIdentity
batteryGroup2LVBD = _BatteryGroup2LVBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 13)
)


class _BatteryGroup2LVBDStatus_Type(Integer32):
    """Custom type batteryGroup2LVBDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2LVBDStatus_Type.__name__ = "Integer32"
_BatteryGroup2LVBDStatus_Object = MibScalar
batteryGroup2LVBDStatus = _BatteryGroup2LVBDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 13, 1),
    _BatteryGroup2LVBDStatus_Type()
)
batteryGroup2LVBDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2LVBDStatus.setStatus("current")


class _BatteryGroup2LVBDDescription_Type(DisplayString):
    """Custom type batteryGroup2LVBDDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2LVBDDescription_Type.__name__ = "DisplayString"
_BatteryGroup2LVBDDescription_Object = MibScalar
batteryGroup2LVBDDescription = _BatteryGroup2LVBDDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 13, 2),
    _BatteryGroup2LVBDDescription_Type()
)
batteryGroup2LVBDDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2LVBDDescription.setStatus("current")
_BatteryGroup2LVBDTrapRepeatCounter_Type = Counter32
_BatteryGroup2LVBDTrapRepeatCounter_Object = MibScalar
batteryGroup2LVBDTrapRepeatCounter = _BatteryGroup2LVBDTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 13, 3),
    _BatteryGroup2LVBDTrapRepeatCounter_Type()
)
batteryGroup2LVBDTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2LVBDTrapRepeatCounter.setStatus("current")


class _BatteryGroup2LVBDEnable_Type(Integer32):
    """Custom type batteryGroup2LVBDEnable based on Integer32"""
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


_BatteryGroup2LVBDEnable_Type.__name__ = "Integer32"
_BatteryGroup2LVBDEnable_Object = MibScalar
batteryGroup2LVBDEnable = _BatteryGroup2LVBDEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 13, 4),
    _BatteryGroup2LVBDEnable_Type()
)
batteryGroup2LVBDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2LVBDEnable.setStatus("current")
_BatteryGroup2LVBDValue_Type = Integer32
_BatteryGroup2LVBDValue_Object = MibScalar
batteryGroup2LVBDValue = _BatteryGroup2LVBDValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 13, 5),
    _BatteryGroup2LVBDValue_Type()
)
batteryGroup2LVBDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2LVBDValue.setStatus("current")
_BatteryGroup2LVBDConnectVoltage_Type = Integer32
_BatteryGroup2LVBDConnectVoltage_Object = MibScalar
batteryGroup2LVBDConnectVoltage = _BatteryGroup2LVBDConnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 13, 6),
    _BatteryGroup2LVBDConnectVoltage_Type()
)
batteryGroup2LVBDConnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2LVBDConnectVoltage.setStatus("current")
_BatteryGroup2LVBDDisconnectVoltage_Type = Integer32
_BatteryGroup2LVBDDisconnectVoltage_Object = MibScalar
batteryGroup2LVBDDisconnectVoltage = _BatteryGroup2LVBDDisconnectVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 13, 7),
    _BatteryGroup2LVBDDisconnectVoltage_Type()
)
batteryGroup2LVBDDisconnectVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2LVBDDisconnectVoltage.setStatus("current")
_BatteryGroup2ChargeCurrentLimit_ObjectIdentity = ObjectIdentity
batteryGroup2ChargeCurrentLimit = _BatteryGroup2ChargeCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 14)
)


class _BatteryGroup2ChargeCurrentLimitEnable_Type(Integer32):
    """Custom type batteryGroup2ChargeCurrentLimitEnable based on Integer32"""
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


_BatteryGroup2ChargeCurrentLimitEnable_Type.__name__ = "Integer32"
_BatteryGroup2ChargeCurrentLimitEnable_Object = MibScalar
batteryGroup2ChargeCurrentLimitEnable = _BatteryGroup2ChargeCurrentLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 14, 1),
    _BatteryGroup2ChargeCurrentLimitEnable_Type()
)
batteryGroup2ChargeCurrentLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2ChargeCurrentLimitEnable.setStatus("current")


class _BatteryGroup2ChargeCurrentLimitValue_Type(Integer32):
    """Custom type batteryGroup2ChargeCurrentLimitValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_BatteryGroup2ChargeCurrentLimitValue_Type.__name__ = "Integer32"
_BatteryGroup2ChargeCurrentLimitValue_Object = MibScalar
batteryGroup2ChargeCurrentLimitValue = _BatteryGroup2ChargeCurrentLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 14, 2),
    _BatteryGroup2ChargeCurrentLimitValue_Type()
)
batteryGroup2ChargeCurrentLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2ChargeCurrentLimitValue.setStatus("current")
_BatteryGroup2Boost_ObjectIdentity = ObjectIdentity
batteryGroup2Boost = _BatteryGroup2Boost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 15)
)


class _BatteryGroup2BoostVoltage_Type(Integer32):
    """Custom type batteryGroup2BoostVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(870, 60418),
    )


_BatteryGroup2BoostVoltage_Type.__name__ = "Integer32"
_BatteryGroup2BoostVoltage_Object = MibScalar
batteryGroup2BoostVoltage = _BatteryGroup2BoostVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 15, 1),
    _BatteryGroup2BoostVoltage_Type()
)
batteryGroup2BoostVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2BoostVoltage.setStatus("current")


class _BatteryGroup2BoostCommand_Type(Integer32):
    """Custom type batteryGroup2BoostCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("startboost", 1),
          ("stopboost", 2))
    )


_BatteryGroup2BoostCommand_Type.__name__ = "Integer32"
_BatteryGroup2BoostCommand_Object = MibScalar
batteryGroup2BoostCommand = _BatteryGroup2BoostCommand_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 15, 2),
    _BatteryGroup2BoostCommand_Type()
)
batteryGroup2BoostCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2BoostCommand.setStatus("current")
_BatteryGroup2BoostCurrentThreshold_Type = Integer32
_BatteryGroup2BoostCurrentThreshold_Object = MibScalar
batteryGroup2BoostCurrentThreshold = _BatteryGroup2BoostCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 15, 3),
    _BatteryGroup2BoostCurrentThreshold_Type()
)
batteryGroup2BoostCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2BoostCurrentThreshold.setStatus("current")


class _BatteryGroup2BoostManualMaxDuration_Type(Integer32):
    """Custom type batteryGroup2BoostManualMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_BatteryGroup2BoostManualMaxDuration_Type.__name__ = "Integer32"
_BatteryGroup2BoostManualMaxDuration_Object = MibScalar
batteryGroup2BoostManualMaxDuration = _BatteryGroup2BoostManualMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 15, 4),
    _BatteryGroup2BoostManualMaxDuration_Type()
)
batteryGroup2BoostManualMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2BoostManualMaxDuration.setStatus("current")
_BatteryGroup2Test_ObjectIdentity = ObjectIdentity
batteryGroup2Test = _BatteryGroup2Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16)
)
_BatteryGroup2TestVoltage_Type = Integer32
_BatteryGroup2TestVoltage_Object = MibScalar
batteryGroup2TestVoltage = _BatteryGroup2TestVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 1),
    _BatteryGroup2TestVoltage_Type()
)
batteryGroup2TestVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TestVoltage.setStatus("current")


class _BatteryGroup2TestCommand_Type(Integer32):
    """Custom type batteryGroup2TestCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("starttest", 1),
          ("stoptest", 2))
    )


_BatteryGroup2TestCommand_Type.__name__ = "Integer32"
_BatteryGroup2TestCommand_Object = MibScalar
batteryGroup2TestCommand = _BatteryGroup2TestCommand_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 2),
    _BatteryGroup2TestCommand_Type()
)
batteryGroup2TestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TestCommand.setStatus("current")


class _BatteryGroup2TestNumberOfResults_Type(Integer32):
    """Custom type batteryGroup2TestNumberOfResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_BatteryGroup2TestNumberOfResults_Type.__name__ = "Integer32"
_BatteryGroup2TestNumberOfResults_Object = MibScalar
batteryGroup2TestNumberOfResults = _BatteryGroup2TestNumberOfResults_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 3),
    _BatteryGroup2TestNumberOfResults_Type()
)
batteryGroup2TestNumberOfResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TestNumberOfResults.setStatus("current")
_BatteryGroup2TestResultTable_Object = MibTable
batteryGroup2TestResultTable = _BatteryGroup2TestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 4)
)
if mibBuilder.loadTexts:
    batteryGroup2TestResultTable.setStatus("current")
_BatteryGroup2TestResultEntry_Object = MibTableRow
batteryGroup2TestResultEntry = _BatteryGroup2TestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 4, 1)
)
batteryGroup2TestResultEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2TestResultIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2TestResultEntry.setStatus("current")


class _BatteryGroup2TestResultIndex_Type(Integer32):
    """Custom type batteryGroup2TestResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BatteryGroup2TestResultIndex_Type.__name__ = "Integer32"
_BatteryGroup2TestResultIndex_Object = MibTableColumn
batteryGroup2TestResultIndex = _BatteryGroup2TestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 4, 1, 1),
    _BatteryGroup2TestResultIndex_Type()
)
batteryGroup2TestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2TestResultIndex.setStatus("current")
_BatteryGroup2TestResultStartDateTime_Type = DateAndTime
_BatteryGroup2TestResultStartDateTime_Object = MibTableColumn
batteryGroup2TestResultStartDateTime = _BatteryGroup2TestResultStartDateTime_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 4, 1, 2),
    _BatteryGroup2TestResultStartDateTime_Type()
)
batteryGroup2TestResultStartDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TestResultStartDateTime.setStatus("current")
_BatteryGroup2TestResultDuration_Type = Integer32
_BatteryGroup2TestResultDuration_Object = MibTableColumn
batteryGroup2TestResultDuration = _BatteryGroup2TestResultDuration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 4, 1, 3),
    _BatteryGroup2TestResultDuration_Type()
)
batteryGroup2TestResultDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TestResultDuration.setStatus("current")
_BatteryGroup2TestResultDischarged_Type = Integer32
_BatteryGroup2TestResultDischarged_Object = MibTableColumn
batteryGroup2TestResultDischarged = _BatteryGroup2TestResultDischarged_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 4, 1, 4),
    _BatteryGroup2TestResultDischarged_Type()
)
batteryGroup2TestResultDischarged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TestResultDischarged.setStatus("current")
_BatteryGroup2TestResultQuality_Type = Integer32
_BatteryGroup2TestResultQuality_Object = MibTableColumn
batteryGroup2TestResultQuality = _BatteryGroup2TestResultQuality_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 16, 4, 1, 5),
    _BatteryGroup2TestResultQuality_Type()
)
batteryGroup2TestResultQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TestResultQuality.setStatus("current")
_BatteryGroup2TempComp_ObjectIdentity = ObjectIdentity
batteryGroup2TempComp = _BatteryGroup2TempComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 17)
)


class _BatteryGroup2TempCompEnable_Type(Integer32):
    """Custom type batteryGroup2TempCompEnable based on Integer32"""
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


_BatteryGroup2TempCompEnable_Type.__name__ = "Integer32"
_BatteryGroup2TempCompEnable_Object = MibScalar
batteryGroup2TempCompEnable = _BatteryGroup2TempCompEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 17, 1),
    _BatteryGroup2TempCompEnable_Type()
)
batteryGroup2TempCompEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TempCompEnable.setStatus("current")
_BatteryGroup2Bank_ObjectIdentity = ObjectIdentity
batteryGroup2Bank = _BatteryGroup2Bank_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18)
)


class _BatteryGroup2BankStatus_Type(Integer32):
    """Custom type batteryGroup2BankStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2BankStatus_Type.__name__ = "Integer32"
_BatteryGroup2BankStatus_Object = MibScalar
batteryGroup2BankStatus = _BatteryGroup2BankStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 1),
    _BatteryGroup2BankStatus_Type()
)
batteryGroup2BankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2BankStatus.setStatus("current")
_BatteryGroup2BankNumberOfTemperatures_Type = Integer32
_BatteryGroup2BankNumberOfTemperatures_Object = MibScalar
batteryGroup2BankNumberOfTemperatures = _BatteryGroup2BankNumberOfTemperatures_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 2),
    _BatteryGroup2BankNumberOfTemperatures_Type()
)
batteryGroup2BankNumberOfTemperatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2BankNumberOfTemperatures.setStatus("current")
_BatteryGroup2BankNumberOfCurrents_Type = Integer32
_BatteryGroup2BankNumberOfCurrents_Object = MibScalar
batteryGroup2BankNumberOfCurrents = _BatteryGroup2BankNumberOfCurrents_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 3),
    _BatteryGroup2BankNumberOfCurrents_Type()
)
batteryGroup2BankNumberOfCurrents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2BankNumberOfCurrents.setStatus("current")
_BatteryGroup2BankNumberOfFuses_Type = Integer32
_BatteryGroup2BankNumberOfFuses_Object = MibScalar
batteryGroup2BankNumberOfFuses = _BatteryGroup2BankNumberOfFuses_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 4),
    _BatteryGroup2BankNumberOfFuses_Type()
)
batteryGroup2BankNumberOfFuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2BankNumberOfFuses.setStatus("current")
_BatteryGroup2BankNumberOfSymmetries_Type = Integer32
_BatteryGroup2BankNumberOfSymmetries_Object = MibScalar
batteryGroup2BankNumberOfSymmetries = _BatteryGroup2BankNumberOfSymmetries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 5),
    _BatteryGroup2BankNumberOfSymmetries_Type()
)
batteryGroup2BankNumberOfSymmetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2BankNumberOfSymmetries.setStatus("current")
_BatteryGroup2BankTemperatureTable_Object = MibTable
batteryGroup2BankTemperatureTable = _BatteryGroup2BankTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6)
)
if mibBuilder.loadTexts:
    batteryGroup2BankTemperatureTable.setStatus("current")
_BatteryGroup2BankTemperatureEntry_Object = MibTableRow
batteryGroup2BankTemperatureEntry = _BatteryGroup2BankTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1)
)
batteryGroup2BankTemperatureEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2TemperatureIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2BankTemperatureEntry.setStatus("current")


class _BatteryGroup2TemperatureIndex_Type(Integer32):
    """Custom type batteryGroup2TemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryGroup2TemperatureIndex_Type.__name__ = "Integer32"
_BatteryGroup2TemperatureIndex_Object = MibTableColumn
batteryGroup2TemperatureIndex = _BatteryGroup2TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 1),
    _BatteryGroup2TemperatureIndex_Type()
)
batteryGroup2TemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureIndex.setStatus("current")


class _BatteryGroup2TemperatureStatus_Type(Integer32):
    """Custom type batteryGroup2TemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2TemperatureStatus_Type.__name__ = "Integer32"
_BatteryGroup2TemperatureStatus_Object = MibTableColumn
batteryGroup2TemperatureStatus = _BatteryGroup2TemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 2),
    _BatteryGroup2TemperatureStatus_Type()
)
batteryGroup2TemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureStatus.setStatus("current")


class _BatteryGroup2TemperatureDescription_Type(DisplayString):
    """Custom type batteryGroup2TemperatureDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2TemperatureDescription_Type.__name__ = "DisplayString"
_BatteryGroup2TemperatureDescription_Object = MibTableColumn
batteryGroup2TemperatureDescription = _BatteryGroup2TemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 3),
    _BatteryGroup2TemperatureDescription_Type()
)
batteryGroup2TemperatureDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureDescription.setStatus("current")
_BatteryGroup2TemperatureTrapRepeatCounter_Type = Counter32
_BatteryGroup2TemperatureTrapRepeatCounter_Object = MibTableColumn
batteryGroup2TemperatureTrapRepeatCounter = _BatteryGroup2TemperatureTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 4),
    _BatteryGroup2TemperatureTrapRepeatCounter_Type()
)
batteryGroup2TemperatureTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureTrapRepeatCounter.setStatus("current")


class _BatteryGroup2TemperatureAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2TemperatureAlarmEnable based on Integer32"""
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


_BatteryGroup2TemperatureAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2TemperatureAlarmEnable_Object = MibTableColumn
batteryGroup2TemperatureAlarmEnable = _BatteryGroup2TemperatureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 5),
    _BatteryGroup2TemperatureAlarmEnable_Type()
)
batteryGroup2TemperatureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureAlarmEnable.setStatus("current")
_BatteryGroup2TemperatureValue_Type = Integer32
_BatteryGroup2TemperatureValue_Object = MibTableColumn
batteryGroup2TemperatureValue = _BatteryGroup2TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 6),
    _BatteryGroup2TemperatureValue_Type()
)
batteryGroup2TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureValue.setStatus("current")
_BatteryGroup2TemperatureMajorHighLevel_Type = Integer32
_BatteryGroup2TemperatureMajorHighLevel_Object = MibTableColumn
batteryGroup2TemperatureMajorHighLevel = _BatteryGroup2TemperatureMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 7),
    _BatteryGroup2TemperatureMajorHighLevel_Type()
)
batteryGroup2TemperatureMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureMajorHighLevel.setStatus("current")
_BatteryGroup2TemperatureMinorHighLevel_Type = Integer32
_BatteryGroup2TemperatureMinorHighLevel_Object = MibTableColumn
batteryGroup2TemperatureMinorHighLevel = _BatteryGroup2TemperatureMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 8),
    _BatteryGroup2TemperatureMinorHighLevel_Type()
)
batteryGroup2TemperatureMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureMinorHighLevel.setStatus("current")
_BatteryGroup2TemperatureMinorLowLevel_Type = Integer32
_BatteryGroup2TemperatureMinorLowLevel_Object = MibTableColumn
batteryGroup2TemperatureMinorLowLevel = _BatteryGroup2TemperatureMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 9),
    _BatteryGroup2TemperatureMinorLowLevel_Type()
)
batteryGroup2TemperatureMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureMinorLowLevel.setStatus("current")
_BatteryGroup2TemperatureMajorLowLevel_Type = Integer32
_BatteryGroup2TemperatureMajorLowLevel_Object = MibTableColumn
batteryGroup2TemperatureMajorLowLevel = _BatteryGroup2TemperatureMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 6, 1, 10),
    _BatteryGroup2TemperatureMajorLowLevel_Type()
)
batteryGroup2TemperatureMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2TemperatureMajorLowLevel.setStatus("current")
_BatteryGroup2BankCurrentTable_Object = MibTable
batteryGroup2BankCurrentTable = _BatteryGroup2BankCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7)
)
if mibBuilder.loadTexts:
    batteryGroup2BankCurrentTable.setStatus("current")
_BatteryGroup2BankCurrentEntry_Object = MibTableRow
batteryGroup2BankCurrentEntry = _BatteryGroup2BankCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1)
)
batteryGroup2BankCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2CurrentIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2BankCurrentEntry.setStatus("current")


class _BatteryGroup2CurrentIndex_Type(Integer32):
    """Custom type batteryGroup2CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryGroup2CurrentIndex_Type.__name__ = "Integer32"
_BatteryGroup2CurrentIndex_Object = MibTableColumn
batteryGroup2CurrentIndex = _BatteryGroup2CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 1),
    _BatteryGroup2CurrentIndex_Type()
)
batteryGroup2CurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2CurrentIndex.setStatus("current")


class _BatteryGroup2CurrentStatus_Type(Integer32):
    """Custom type batteryGroup2CurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2CurrentStatus_Type.__name__ = "Integer32"
_BatteryGroup2CurrentStatus_Object = MibTableColumn
batteryGroup2CurrentStatus = _BatteryGroup2CurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 2),
    _BatteryGroup2CurrentStatus_Type()
)
batteryGroup2CurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CurrentStatus.setStatus("current")


class _BatteryGroup2CurrentDescription_Type(DisplayString):
    """Custom type batteryGroup2CurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2CurrentDescription_Type.__name__ = "DisplayString"
_BatteryGroup2CurrentDescription_Object = MibTableColumn
batteryGroup2CurrentDescription = _BatteryGroup2CurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 3),
    _BatteryGroup2CurrentDescription_Type()
)
batteryGroup2CurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentDescription.setStatus("current")
_BatteryGroup2CurrentTrapRepeatCounter_Type = Counter32
_BatteryGroup2CurrentTrapRepeatCounter_Object = MibTableColumn
batteryGroup2CurrentTrapRepeatCounter = _BatteryGroup2CurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 4),
    _BatteryGroup2CurrentTrapRepeatCounter_Type()
)
batteryGroup2CurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2CurrentTrapRepeatCounter.setStatus("current")


class _BatteryGroup2CurrentAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2CurrentAlarmEnable based on Integer32"""
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


_BatteryGroup2CurrentAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2CurrentAlarmEnable_Object = MibTableColumn
batteryGroup2CurrentAlarmEnable = _BatteryGroup2CurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 5),
    _BatteryGroup2CurrentAlarmEnable_Type()
)
batteryGroup2CurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentAlarmEnable.setStatus("current")
_BatteryGroup2CurrentValue_Type = Integer32
_BatteryGroup2CurrentValue_Object = MibTableColumn
batteryGroup2CurrentValue = _BatteryGroup2CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 6),
    _BatteryGroup2CurrentValue_Type()
)
batteryGroup2CurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CurrentValue.setStatus("current")
_BatteryGroup2CurrentMajorHighLevel_Type = Integer32
_BatteryGroup2CurrentMajorHighLevel_Object = MibTableColumn
batteryGroup2CurrentMajorHighLevel = _BatteryGroup2CurrentMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 7),
    _BatteryGroup2CurrentMajorHighLevel_Type()
)
batteryGroup2CurrentMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentMajorHighLevel.setStatus("current")
_BatteryGroup2CurrentMinorHighLevel_Type = Integer32
_BatteryGroup2CurrentMinorHighLevel_Object = MibTableColumn
batteryGroup2CurrentMinorHighLevel = _BatteryGroup2CurrentMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 8),
    _BatteryGroup2CurrentMinorHighLevel_Type()
)
batteryGroup2CurrentMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentMinorHighLevel.setStatus("current")
_BatteryGroup2CurrentMinorLowLevel_Type = Integer32
_BatteryGroup2CurrentMinorLowLevel_Object = MibTableColumn
batteryGroup2CurrentMinorLowLevel = _BatteryGroup2CurrentMinorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 9),
    _BatteryGroup2CurrentMinorLowLevel_Type()
)
batteryGroup2CurrentMinorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentMinorLowLevel.setStatus("current")
_BatteryGroup2CurrentMajorLowLevel_Type = Integer32
_BatteryGroup2CurrentMajorLowLevel_Object = MibTableColumn
batteryGroup2CurrentMajorLowLevel = _BatteryGroup2CurrentMajorLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 7, 1, 10),
    _BatteryGroup2CurrentMajorLowLevel_Type()
)
batteryGroup2CurrentMajorLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2CurrentMajorLowLevel.setStatus("current")
_BatteryGroup2BankFuseTable_Object = MibTable
batteryGroup2BankFuseTable = _BatteryGroup2BankFuseTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 8)
)
if mibBuilder.loadTexts:
    batteryGroup2BankFuseTable.setStatus("current")
_BatteryGroup2BankFuseEntry_Object = MibTableRow
batteryGroup2BankFuseEntry = _BatteryGroup2BankFuseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 8, 1)
)
batteryGroup2BankFuseEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2FuseIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2BankFuseEntry.setStatus("current")


class _BatteryGroup2FuseIndex_Type(Integer32):
    """Custom type batteryGroup2FuseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BatteryGroup2FuseIndex_Type.__name__ = "Integer32"
_BatteryGroup2FuseIndex_Object = MibTableColumn
batteryGroup2FuseIndex = _BatteryGroup2FuseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 8, 1, 1),
    _BatteryGroup2FuseIndex_Type()
)
batteryGroup2FuseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2FuseIndex.setStatus("current")


class _BatteryGroup2FuseStatus_Type(Integer32):
    """Custom type batteryGroup2FuseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2FuseStatus_Type.__name__ = "Integer32"
_BatteryGroup2FuseStatus_Object = MibTableColumn
batteryGroup2FuseStatus = _BatteryGroup2FuseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 8, 1, 2),
    _BatteryGroup2FuseStatus_Type()
)
batteryGroup2FuseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2FuseStatus.setStatus("current")


class _BatteryGroup2FuseDescription_Type(DisplayString):
    """Custom type batteryGroup2FuseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2FuseDescription_Type.__name__ = "DisplayString"
_BatteryGroup2FuseDescription_Object = MibTableColumn
batteryGroup2FuseDescription = _BatteryGroup2FuseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 8, 1, 3),
    _BatteryGroup2FuseDescription_Type()
)
batteryGroup2FuseDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2FuseDescription.setStatus("current")
_BatteryGroup2FuseTrapRepeatCounter_Type = Counter32
_BatteryGroup2FuseTrapRepeatCounter_Object = MibTableColumn
batteryGroup2FuseTrapRepeatCounter = _BatteryGroup2FuseTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 8, 1, 4),
    _BatteryGroup2FuseTrapRepeatCounter_Type()
)
batteryGroup2FuseTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2FuseTrapRepeatCounter.setStatus("current")


class _BatteryGroup2FuseAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2FuseAlarmEnable based on Integer32"""
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


_BatteryGroup2FuseAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2FuseAlarmEnable_Object = MibTableColumn
batteryGroup2FuseAlarmEnable = _BatteryGroup2FuseAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 8, 1, 5),
    _BatteryGroup2FuseAlarmEnable_Type()
)
batteryGroup2FuseAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2FuseAlarmEnable.setStatus("current")
_BatteryGroup2FuseValue_Type = Integer32
_BatteryGroup2FuseValue_Object = MibTableColumn
batteryGroup2FuseValue = _BatteryGroup2FuseValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 8, 1, 6),
    _BatteryGroup2FuseValue_Type()
)
batteryGroup2FuseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2FuseValue.setStatus("current")
_BatteryGroup2BankSymmetryTable_Object = MibTable
batteryGroup2BankSymmetryTable = _BatteryGroup2BankSymmetryTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9)
)
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryTable.setStatus("current")
_BatteryGroup2BankSymmetryEntry_Object = MibTableRow
batteryGroup2BankSymmetryEntry = _BatteryGroup2BankSymmetryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1)
)
batteryGroup2BankSymmetryEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2BankSymmetryIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryEntry.setStatus("current")


class _BatteryGroup2BankSymmetryIndex_Type(Integer32):
    """Custom type batteryGroup2BankSymmetryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BatteryGroup2BankSymmetryIndex_Type.__name__ = "Integer32"
_BatteryGroup2BankSymmetryIndex_Object = MibTableColumn
batteryGroup2BankSymmetryIndex = _BatteryGroup2BankSymmetryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 1),
    _BatteryGroup2BankSymmetryIndex_Type()
)
batteryGroup2BankSymmetryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryIndex.setStatus("current")


class _BatteryGroup2BankSymmetryStatus_Type(Integer32):
    """Custom type batteryGroup2BankSymmetryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2BankSymmetryStatus_Type.__name__ = "Integer32"
_BatteryGroup2BankSymmetryStatus_Object = MibTableColumn
batteryGroup2BankSymmetryStatus = _BatteryGroup2BankSymmetryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 2),
    _BatteryGroup2BankSymmetryStatus_Type()
)
batteryGroup2BankSymmetryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryStatus.setStatus("current")


class _BatteryGroup2BankSymmetryDescription_Type(DisplayString):
    """Custom type batteryGroup2BankSymmetryDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2BankSymmetryDescription_Type.__name__ = "DisplayString"
_BatteryGroup2BankSymmetryDescription_Object = MibTableColumn
batteryGroup2BankSymmetryDescription = _BatteryGroup2BankSymmetryDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 3),
    _BatteryGroup2BankSymmetryDescription_Type()
)
batteryGroup2BankSymmetryDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryDescription.setStatus("current")
_BatteryGroup2BankSymmetryTrapRepeatCounter_Type = Counter32
_BatteryGroup2BankSymmetryTrapRepeatCounter_Object = MibTableColumn
batteryGroup2BankSymmetryTrapRepeatCounter = _BatteryGroup2BankSymmetryTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 4),
    _BatteryGroup2BankSymmetryTrapRepeatCounter_Type()
)
batteryGroup2BankSymmetryTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryTrapRepeatCounter.setStatus("current")


class _BatteryGroup2BankSymmetryAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2BankSymmetryAlarmEnable based on Integer32"""
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


_BatteryGroup2BankSymmetryAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2BankSymmetryAlarmEnable_Object = MibTableColumn
batteryGroup2BankSymmetryAlarmEnable = _BatteryGroup2BankSymmetryAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 5),
    _BatteryGroup2BankSymmetryAlarmEnable_Type()
)
batteryGroup2BankSymmetryAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryAlarmEnable.setStatus("current")
_BatteryGroup2BankSymmetryMeasureValue_Type = Integer32
_BatteryGroup2BankSymmetryMeasureValue_Object = MibTableColumn
batteryGroup2BankSymmetryMeasureValue = _BatteryGroup2BankSymmetryMeasureValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 6),
    _BatteryGroup2BankSymmetryMeasureValue_Type()
)
batteryGroup2BankSymmetryMeasureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryMeasureValue.setStatus("current")
_BatteryGroup2BankSymmetryDeltaValue_Type = Integer32
_BatteryGroup2BankSymmetryDeltaValue_Object = MibTableColumn
batteryGroup2BankSymmetryDeltaValue = _BatteryGroup2BankSymmetryDeltaValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 7),
    _BatteryGroup2BankSymmetryDeltaValue_Type()
)
batteryGroup2BankSymmetryDeltaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryDeltaValue.setStatus("current")
_BatteryGroup2BankSymmetryMajorAlarmLevel_Type = Integer32
_BatteryGroup2BankSymmetryMajorAlarmLevel_Object = MibTableColumn
batteryGroup2BankSymmetryMajorAlarmLevel = _BatteryGroup2BankSymmetryMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 8),
    _BatteryGroup2BankSymmetryMajorAlarmLevel_Type()
)
batteryGroup2BankSymmetryMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryMajorAlarmLevel.setStatus("current")
_BatteryGroup2BankSymmetryMinorAlarmLevel_Type = Integer32
_BatteryGroup2BankSymmetryMinorAlarmLevel_Object = MibTableColumn
batteryGroup2BankSymmetryMinorAlarmLevel = _BatteryGroup2BankSymmetryMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 18, 9, 1, 9),
    _BatteryGroup2BankSymmetryMinorAlarmLevel_Type()
)
batteryGroup2BankSymmetryMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2BankSymmetryMinorAlarmLevel.setStatus("current")
_BatteryGroup2EnergyLog_ObjectIdentity = ObjectIdentity
batteryGroup2EnergyLog = _BatteryGroup2EnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19)
)
_BatteryGroup2EnergyLogAccumulated_Type = Integer32
_BatteryGroup2EnergyLogAccumulated_Object = MibScalar
batteryGroup2EnergyLogAccumulated = _BatteryGroup2EnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 1),
    _BatteryGroup2EnergyLogAccumulated_Type()
)
batteryGroup2EnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogAccumulated.setStatus("current")


class _BatteryGroup2EnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type batteryGroup2EnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryGroup2EnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_BatteryGroup2EnergyLogLastHoursNumberOfEntries_Object = MibScalar
batteryGroup2EnergyLogLastHoursNumberOfEntries = _BatteryGroup2EnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 2),
    _BatteryGroup2EnergyLogLastHoursNumberOfEntries_Type()
)
batteryGroup2EnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastHoursNumberOfEntries.setStatus("current")
_BatteryGroup2EnergyLogLastHoursTable_Object = MibTable
batteryGroup2EnergyLogLastHoursTable = _BatteryGroup2EnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 3)
)
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastHoursTable.setStatus("current")
_BatteryGroup2EnergyLogLastHoursEntry_Object = MibTableRow
batteryGroup2EnergyLogLastHoursEntry = _BatteryGroup2EnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 3, 1)
)
batteryGroup2EnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2EnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastHoursEntry.setStatus("current")


class _BatteryGroup2EnergyLogLastHoursIndex_Type(Integer32):
    """Custom type batteryGroup2EnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryGroup2EnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_BatteryGroup2EnergyLogLastHoursIndex_Object = MibTableColumn
batteryGroup2EnergyLogLastHoursIndex = _BatteryGroup2EnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 3, 1, 1),
    _BatteryGroup2EnergyLogLastHoursIndex_Type()
)
batteryGroup2EnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastHoursIndex.setStatus("current")
_BatteryGroup2EnergyLogLastHoursValue_Type = Integer32
_BatteryGroup2EnergyLogLastHoursValue_Object = MibTableColumn
batteryGroup2EnergyLogLastHoursValue = _BatteryGroup2EnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 3, 1, 2),
    _BatteryGroup2EnergyLogLastHoursValue_Type()
)
batteryGroup2EnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastHoursValue.setStatus("current")


class _BatteryGroup2EnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type batteryGroup2EnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryGroup2EnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_BatteryGroup2EnergyLogLastDaysNumberOfEntries_Object = MibScalar
batteryGroup2EnergyLogLastDaysNumberOfEntries = _BatteryGroup2EnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 4),
    _BatteryGroup2EnergyLogLastDaysNumberOfEntries_Type()
)
batteryGroup2EnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastDaysNumberOfEntries.setStatus("current")
_BatteryGroup2EnergyLogLastDaysTable_Object = MibTable
batteryGroup2EnergyLogLastDaysTable = _BatteryGroup2EnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 5)
)
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastDaysTable.setStatus("current")
_BatteryGroup2EnergyLogLastDaysEntry_Object = MibTableRow
batteryGroup2EnergyLogLastDaysEntry = _BatteryGroup2EnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 5, 1)
)
batteryGroup2EnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2EnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastDaysEntry.setStatus("current")


class _BatteryGroup2EnergyLogLastDaysIndex_Type(Integer32):
    """Custom type batteryGroup2EnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryGroup2EnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_BatteryGroup2EnergyLogLastDaysIndex_Object = MibTableColumn
batteryGroup2EnergyLogLastDaysIndex = _BatteryGroup2EnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 5, 1, 1),
    _BatteryGroup2EnergyLogLastDaysIndex_Type()
)
batteryGroup2EnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastDaysIndex.setStatus("current")
_BatteryGroup2EnergyLogLastDaysValue_Type = Integer32
_BatteryGroup2EnergyLogLastDaysValue_Object = MibTableColumn
batteryGroup2EnergyLogLastDaysValue = _BatteryGroup2EnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 5, 1, 2),
    _BatteryGroup2EnergyLogLastDaysValue_Type()
)
batteryGroup2EnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastDaysValue.setStatus("current")


class _BatteryGroup2EnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type batteryGroup2EnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryGroup2EnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_BatteryGroup2EnergyLogLastWeeksNumberOfEntries_Object = MibScalar
batteryGroup2EnergyLogLastWeeksNumberOfEntries = _BatteryGroup2EnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 6),
    _BatteryGroup2EnergyLogLastWeeksNumberOfEntries_Type()
)
batteryGroup2EnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastWeeksNumberOfEntries.setStatus("current")
_BatteryGroup2EnergyLogLastWeeksTable_Object = MibTable
batteryGroup2EnergyLogLastWeeksTable = _BatteryGroup2EnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 7)
)
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastWeeksTable.setStatus("current")
_BatteryGroup2EnergyLogLastWeeksEntry_Object = MibTableRow
batteryGroup2EnergyLogLastWeeksEntry = _BatteryGroup2EnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 7, 1)
)
batteryGroup2EnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2EnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastWeeksEntry.setStatus("current")


class _BatteryGroup2EnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type batteryGroup2EnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryGroup2EnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_BatteryGroup2EnergyLogLastWeeksIndex_Object = MibTableColumn
batteryGroup2EnergyLogLastWeeksIndex = _BatteryGroup2EnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 7, 1, 1),
    _BatteryGroup2EnergyLogLastWeeksIndex_Type()
)
batteryGroup2EnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastWeeksIndex.setStatus("current")
_BatteryGroup2EnergyLogLastWeeksValue_Type = Integer32
_BatteryGroup2EnergyLogLastWeeksValue_Object = MibTableColumn
batteryGroup2EnergyLogLastWeeksValue = _BatteryGroup2EnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 19, 7, 1, 2),
    _BatteryGroup2EnergyLogLastWeeksValue_Type()
)
batteryGroup2EnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2EnergyLogLastWeeksValue.setStatus("current")
_BatteryGroup2CycleLog_ObjectIdentity = ObjectIdentity
batteryGroup2CycleLog = _BatteryGroup2CycleLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20)
)
_BatteryGroup2CycleLogTotalCycles_Type = Integer32
_BatteryGroup2CycleLogTotalCycles_Object = MibScalar
batteryGroup2CycleLogTotalCycles = _BatteryGroup2CycleLogTotalCycles_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 1),
    _BatteryGroup2CycleLogTotalCycles_Type()
)
batteryGroup2CycleLogTotalCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogTotalCycles.setStatus("current")


class _BatteryGroup2CycleLogDaysNumberOfEntries_Type(Integer32):
    """Custom type batteryGroup2CycleLogDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryGroup2CycleLogDaysNumberOfEntries_Type.__name__ = "Integer32"
_BatteryGroup2CycleLogDaysNumberOfEntries_Object = MibScalar
batteryGroup2CycleLogDaysNumberOfEntries = _BatteryGroup2CycleLogDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 2),
    _BatteryGroup2CycleLogDaysNumberOfEntries_Type()
)
batteryGroup2CycleLogDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogDaysNumberOfEntries.setStatus("current")
_BatteryGroup2CycleLogDaysTable_Object = MibTable
batteryGroup2CycleLogDaysTable = _BatteryGroup2CycleLogDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 3)
)
if mibBuilder.loadTexts:
    batteryGroup2CycleLogDaysTable.setStatus("current")
_BatteryGroup2CycleLogDaysEntry_Object = MibTableRow
batteryGroup2CycleLogDaysEntry = _BatteryGroup2CycleLogDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 3, 1)
)
batteryGroup2CycleLogDaysEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2CycleLogDaysIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2CycleLogDaysEntry.setStatus("current")


class _BatteryGroup2CycleLogDaysIndex_Type(Integer32):
    """Custom type batteryGroup2CycleLogDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryGroup2CycleLogDaysIndex_Type.__name__ = "Integer32"
_BatteryGroup2CycleLogDaysIndex_Object = MibTableColumn
batteryGroup2CycleLogDaysIndex = _BatteryGroup2CycleLogDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 3, 1, 1),
    _BatteryGroup2CycleLogDaysIndex_Type()
)
batteryGroup2CycleLogDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogDaysIndex.setStatus("current")
_BatteryGroup2CycleLogDaysValue_Type = Integer32
_BatteryGroup2CycleLogDaysValue_Object = MibTableColumn
batteryGroup2CycleLogDaysValue = _BatteryGroup2CycleLogDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 3, 1, 2),
    _BatteryGroup2CycleLogDaysValue_Type()
)
batteryGroup2CycleLogDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogDaysValue.setStatus("current")


class _BatteryGroup2CycleLogWeeksNumberOfEntries_Type(Integer32):
    """Custom type batteryGroup2CycleLogWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryGroup2CycleLogWeeksNumberOfEntries_Type.__name__ = "Integer32"
_BatteryGroup2CycleLogWeeksNumberOfEntries_Object = MibScalar
batteryGroup2CycleLogWeeksNumberOfEntries = _BatteryGroup2CycleLogWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 4),
    _BatteryGroup2CycleLogWeeksNumberOfEntries_Type()
)
batteryGroup2CycleLogWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogWeeksNumberOfEntries.setStatus("current")
_BatteryGroup2CycleLogWeeksTable_Object = MibTable
batteryGroup2CycleLogWeeksTable = _BatteryGroup2CycleLogWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 5)
)
if mibBuilder.loadTexts:
    batteryGroup2CycleLogWeeksTable.setStatus("current")
_BatteryGroup2CycleLogWeeksEntry_Object = MibTableRow
batteryGroup2CycleLogWeeksEntry = _BatteryGroup2CycleLogWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 5, 1)
)
batteryGroup2CycleLogWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2CycleLogWeeksIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2CycleLogWeeksEntry.setStatus("current")


class _BatteryGroup2CycleLogWeeksIndex_Type(Integer32):
    """Custom type batteryGroup2CycleLogWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryGroup2CycleLogWeeksIndex_Type.__name__ = "Integer32"
_BatteryGroup2CycleLogWeeksIndex_Object = MibTableColumn
batteryGroup2CycleLogWeeksIndex = _BatteryGroup2CycleLogWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 5, 1, 1),
    _BatteryGroup2CycleLogWeeksIndex_Type()
)
batteryGroup2CycleLogWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogWeeksIndex.setStatus("current")
_BatteryGroup2CycleLogWeeksValue_Type = Integer32
_BatteryGroup2CycleLogWeeksValue_Object = MibTableColumn
batteryGroup2CycleLogWeeksValue = _BatteryGroup2CycleLogWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 5, 1, 2),
    _BatteryGroup2CycleLogWeeksValue_Type()
)
batteryGroup2CycleLogWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogWeeksValue.setStatus("current")


class _BatteryGroup2CycleLogMonthsNumberOfEntries_Type(Integer32):
    """Custom type batteryGroup2CycleLogMonthsNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_BatteryGroup2CycleLogMonthsNumberOfEntries_Type.__name__ = "Integer32"
_BatteryGroup2CycleLogMonthsNumberOfEntries_Object = MibScalar
batteryGroup2CycleLogMonthsNumberOfEntries = _BatteryGroup2CycleLogMonthsNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 6),
    _BatteryGroup2CycleLogMonthsNumberOfEntries_Type()
)
batteryGroup2CycleLogMonthsNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogMonthsNumberOfEntries.setStatus("current")
_BatteryGroup2CycleLogMonthsTable_Object = MibTable
batteryGroup2CycleLogMonthsTable = _BatteryGroup2CycleLogMonthsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 7)
)
if mibBuilder.loadTexts:
    batteryGroup2CycleLogMonthsTable.setStatus("current")
_BatteryGroup2CycleLogMonthsEntry_Object = MibTableRow
batteryGroup2CycleLogMonthsEntry = _BatteryGroup2CycleLogMonthsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 7, 1)
)
batteryGroup2CycleLogMonthsEntry.setIndexNames(
    (0, "SP2-MIB", "batteryGroup2CycleLogMonthsIndex"),
)
if mibBuilder.loadTexts:
    batteryGroup2CycleLogMonthsEntry.setStatus("current")


class _BatteryGroup2CycleLogMonthsIndex_Type(Integer32):
    """Custom type batteryGroup2CycleLogMonthsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_BatteryGroup2CycleLogMonthsIndex_Type.__name__ = "Integer32"
_BatteryGroup2CycleLogMonthsIndex_Object = MibTableColumn
batteryGroup2CycleLogMonthsIndex = _BatteryGroup2CycleLogMonthsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 7, 1, 1),
    _BatteryGroup2CycleLogMonthsIndex_Type()
)
batteryGroup2CycleLogMonthsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogMonthsIndex.setStatus("current")
_BatteryGroup2CycleLogMonthsValue_Type = Integer32
_BatteryGroup2CycleLogMonthsValue_Object = MibTableColumn
batteryGroup2CycleLogMonthsValue = _BatteryGroup2CycleLogMonthsValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 20, 7, 1, 2),
    _BatteryGroup2CycleLogMonthsValue_Type()
)
batteryGroup2CycleLogMonthsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2CycleLogMonthsValue.setStatus("current")
_BatteryGroup2Equalize_ObjectIdentity = ObjectIdentity
batteryGroup2Equalize = _BatteryGroup2Equalize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 21)
)


class _BatteryGroup2EqualizeVoltage_Type(Integer32):
    """Custom type batteryGroup2EqualizeVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(870, 60418),
    )


_BatteryGroup2EqualizeVoltage_Type.__name__ = "Integer32"
_BatteryGroup2EqualizeVoltage_Object = MibScalar
batteryGroup2EqualizeVoltage = _BatteryGroup2EqualizeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 21, 1),
    _BatteryGroup2EqualizeVoltage_Type()
)
batteryGroup2EqualizeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2EqualizeVoltage.setStatus("current")


class _BatteryGroup2EqualizeCommand_Type(Integer32):
    """Custom type batteryGroup2EqualizeCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pushbutton", 0),
          ("startequalize", 1),
          ("stopequalize", 2))
    )


_BatteryGroup2EqualizeCommand_Type.__name__ = "Integer32"
_BatteryGroup2EqualizeCommand_Object = MibScalar
batteryGroup2EqualizeCommand = _BatteryGroup2EqualizeCommand_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 21, 2),
    _BatteryGroup2EqualizeCommand_Type()
)
batteryGroup2EqualizeCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2EqualizeCommand.setStatus("current")
_BatteryGroup2EqualizeCurrentThreshold_Type = Integer32
_BatteryGroup2EqualizeCurrentThreshold_Object = MibScalar
batteryGroup2EqualizeCurrentThreshold = _BatteryGroup2EqualizeCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 21, 3),
    _BatteryGroup2EqualizeCurrentThreshold_Type()
)
batteryGroup2EqualizeCurrentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2EqualizeCurrentThreshold.setStatus("current")


class _BatteryGroup2EqualizeManualMaxDuration_Type(Integer32):
    """Custom type batteryGroup2EqualizeManualMaxDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_BatteryGroup2EqualizeManualMaxDuration_Type.__name__ = "Integer32"
_BatteryGroup2EqualizeManualMaxDuration_Object = MibScalar
batteryGroup2EqualizeManualMaxDuration = _BatteryGroup2EqualizeManualMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 21, 4),
    _BatteryGroup2EqualizeManualMaxDuration_Type()
)
batteryGroup2EqualizeManualMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2EqualizeManualMaxDuration.setStatus("current")
_BatteryGroup2AhCharged_ObjectIdentity = ObjectIdentity
batteryGroup2AhCharged = _BatteryGroup2AhCharged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 22)
)


class _BatteryGroup2AhChargedStatus_Type(Integer32):
    """Custom type batteryGroup2AhChargedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2AhChargedStatus_Type.__name__ = "Integer32"
_BatteryGroup2AhChargedStatus_Object = MibScalar
batteryGroup2AhChargedStatus = _BatteryGroup2AhChargedStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 22, 1),
    _BatteryGroup2AhChargedStatus_Type()
)
batteryGroup2AhChargedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2AhChargedStatus.setStatus("current")


class _BatteryGroup2AhChargedDescription_Type(DisplayString):
    """Custom type batteryGroup2AhChargedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2AhChargedDescription_Type.__name__ = "DisplayString"
_BatteryGroup2AhChargedDescription_Object = MibScalar
batteryGroup2AhChargedDescription = _BatteryGroup2AhChargedDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 22, 2),
    _BatteryGroup2AhChargedDescription_Type()
)
batteryGroup2AhChargedDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2AhChargedDescription.setStatus("current")
_BatteryGroup2AhChargedTrapRepeatCounter_Type = Counter32
_BatteryGroup2AhChargedTrapRepeatCounter_Object = MibScalar
batteryGroup2AhChargedTrapRepeatCounter = _BatteryGroup2AhChargedTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 22, 3),
    _BatteryGroup2AhChargedTrapRepeatCounter_Type()
)
batteryGroup2AhChargedTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2AhChargedTrapRepeatCounter.setStatus("current")


class _BatteryGroup2AhChargedAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2AhChargedAlarmEnable based on Integer32"""
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


_BatteryGroup2AhChargedAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2AhChargedAlarmEnable_Object = MibScalar
batteryGroup2AhChargedAlarmEnable = _BatteryGroup2AhChargedAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 22, 4),
    _BatteryGroup2AhChargedAlarmEnable_Type()
)
batteryGroup2AhChargedAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2AhChargedAlarmEnable.setStatus("current")
_BatteryGroup2AhChargedValue_Type = Integer32
_BatteryGroup2AhChargedValue_Object = MibScalar
batteryGroup2AhChargedValue = _BatteryGroup2AhChargedValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 22, 5),
    _BatteryGroup2AhChargedValue_Type()
)
batteryGroup2AhChargedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2AhChargedValue.setStatus("current")
_BatteryGroup2AhChargedMinorHighLevel_Type = Integer32
_BatteryGroup2AhChargedMinorHighLevel_Object = MibScalar
batteryGroup2AhChargedMinorHighLevel = _BatteryGroup2AhChargedMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 22, 6),
    _BatteryGroup2AhChargedMinorHighLevel_Type()
)
batteryGroup2AhChargedMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2AhChargedMinorHighLevel.setStatus("current")
_BatteryGroup2AhChargedMajorHighLevel_Type = Integer32
_BatteryGroup2AhChargedMajorHighLevel_Object = MibScalar
batteryGroup2AhChargedMajorHighLevel = _BatteryGroup2AhChargedMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 22, 7),
    _BatteryGroup2AhChargedMajorHighLevel_Type()
)
batteryGroup2AhChargedMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2AhChargedMajorHighLevel.setStatus("current")
_BatteryGroup2AhDischarged_ObjectIdentity = ObjectIdentity
batteryGroup2AhDischarged = _BatteryGroup2AhDischarged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 23)
)


class _BatteryGroup2AhDischargedStatus_Type(Integer32):
    """Custom type batteryGroup2AhDischargedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_BatteryGroup2AhDischargedStatus_Type.__name__ = "Integer32"
_BatteryGroup2AhDischargedStatus_Object = MibScalar
batteryGroup2AhDischargedStatus = _BatteryGroup2AhDischargedStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 23, 1),
    _BatteryGroup2AhDischargedStatus_Type()
)
batteryGroup2AhDischargedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2AhDischargedStatus.setStatus("current")


class _BatteryGroup2AhDischargedDescription_Type(DisplayString):
    """Custom type batteryGroup2AhDischargedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BatteryGroup2AhDischargedDescription_Type.__name__ = "DisplayString"
_BatteryGroup2AhDischargedDescription_Object = MibScalar
batteryGroup2AhDischargedDescription = _BatteryGroup2AhDischargedDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 23, 2),
    _BatteryGroup2AhDischargedDescription_Type()
)
batteryGroup2AhDischargedDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2AhDischargedDescription.setStatus("current")
_BatteryGroup2AhDischargedTrapRepeatCounter_Type = Counter32
_BatteryGroup2AhDischargedTrapRepeatCounter_Object = MibScalar
batteryGroup2AhDischargedTrapRepeatCounter = _BatteryGroup2AhDischargedTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 23, 3),
    _BatteryGroup2AhDischargedTrapRepeatCounter_Type()
)
batteryGroup2AhDischargedTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    batteryGroup2AhDischargedTrapRepeatCounter.setStatus("current")


class _BatteryGroup2AhDischargedAlarmEnable_Type(Integer32):
    """Custom type batteryGroup2AhDischargedAlarmEnable based on Integer32"""
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


_BatteryGroup2AhDischargedAlarmEnable_Type.__name__ = "Integer32"
_BatteryGroup2AhDischargedAlarmEnable_Object = MibScalar
batteryGroup2AhDischargedAlarmEnable = _BatteryGroup2AhDischargedAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 23, 4),
    _BatteryGroup2AhDischargedAlarmEnable_Type()
)
batteryGroup2AhDischargedAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2AhDischargedAlarmEnable.setStatus("current")
_BatteryGroup2AhDischargedValue_Type = Integer32
_BatteryGroup2AhDischargedValue_Object = MibScalar
batteryGroup2AhDischargedValue = _BatteryGroup2AhDischargedValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 23, 5),
    _BatteryGroup2AhDischargedValue_Type()
)
batteryGroup2AhDischargedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batteryGroup2AhDischargedValue.setStatus("current")
_BatteryGroup2AhDischargedMinorHighLevel_Type = Integer32
_BatteryGroup2AhDischargedMinorHighLevel_Object = MibScalar
batteryGroup2AhDischargedMinorHighLevel = _BatteryGroup2AhDischargedMinorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 23, 6),
    _BatteryGroup2AhDischargedMinorHighLevel_Type()
)
batteryGroup2AhDischargedMinorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2AhDischargedMinorHighLevel.setStatus("current")
_BatteryGroup2AhDischargedMajorHighLevel_Type = Integer32
_BatteryGroup2AhDischargedMajorHighLevel_Object = MibScalar
batteryGroup2AhDischargedMajorHighLevel = _BatteryGroup2AhDischargedMajorHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 15, 23, 7),
    _BatteryGroup2AhDischargedMajorHighLevel_Type()
)
batteryGroup2AhDischargedMajorHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batteryGroup2AhDischargedMajorHighLevel.setStatus("current")
_Inverters_ObjectIdentity = ObjectIdentity
inverters = _Inverters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16)
)


class _InvertersStatus_Type(Integer32):
    """Custom type invertersStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InvertersStatus_Type.__name__ = "Integer32"
_InvertersStatus_Object = MibScalar
invertersStatus = _InvertersStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 1),
    _InvertersStatus_Type()
)
invertersStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersStatus.setStatus("current")
_InvertersCurrent_ObjectIdentity = ObjectIdentity
invertersCurrent = _InvertersCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 2)
)


class _InvertersCurrentStatus_Type(Integer32):
    """Custom type invertersCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InvertersCurrentStatus_Type.__name__ = "Integer32"
_InvertersCurrentStatus_Object = MibScalar
invertersCurrentStatus = _InvertersCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 2, 1),
    _InvertersCurrentStatus_Type()
)
invertersCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersCurrentStatus.setStatus("current")


class _InvertersCurrentDescription_Type(DisplayString):
    """Custom type invertersCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InvertersCurrentDescription_Type.__name__ = "DisplayString"
_InvertersCurrentDescription_Object = MibScalar
invertersCurrentDescription = _InvertersCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 2, 2),
    _InvertersCurrentDescription_Type()
)
invertersCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersCurrentDescription.setStatus("current")
_InvertersCurrentTrapRepeatCounter_Type = Counter32
_InvertersCurrentTrapRepeatCounter_Object = MibScalar
invertersCurrentTrapRepeatCounter = _InvertersCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 2, 3),
    _InvertersCurrentTrapRepeatCounter_Type()
)
invertersCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    invertersCurrentTrapRepeatCounter.setStatus("current")


class _InvertersCurrentAlarmEnable_Type(Integer32):
    """Custom type invertersCurrentAlarmEnable based on Integer32"""
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


_InvertersCurrentAlarmEnable_Type.__name__ = "Integer32"
_InvertersCurrentAlarmEnable_Object = MibScalar
invertersCurrentAlarmEnable = _InvertersCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 2, 4),
    _InvertersCurrentAlarmEnable_Type()
)
invertersCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersCurrentAlarmEnable.setStatus("current")
_InvertersCurrentValue_Type = Integer32
_InvertersCurrentValue_Object = MibScalar
invertersCurrentValue = _InvertersCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 2, 5),
    _InvertersCurrentValue_Type()
)
invertersCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersCurrentValue.setStatus("current")
_InvertersCurrentMajorAlarmLevel_Type = Integer32
_InvertersCurrentMajorAlarmLevel_Object = MibScalar
invertersCurrentMajorAlarmLevel = _InvertersCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 2, 6),
    _InvertersCurrentMajorAlarmLevel_Type()
)
invertersCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersCurrentMajorAlarmLevel.setStatus("current")
_InvertersCurrentMinorAlarmLevel_Type = Integer32
_InvertersCurrentMinorAlarmLevel_Object = MibScalar
invertersCurrentMinorAlarmLevel = _InvertersCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 2, 7),
    _InvertersCurrentMinorAlarmLevel_Type()
)
invertersCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersCurrentMinorAlarmLevel.setStatus("current")
_InvertersCapacity_ObjectIdentity = ObjectIdentity
invertersCapacity = _InvertersCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 3)
)


class _InvertersCapacityStatus_Type(Integer32):
    """Custom type invertersCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InvertersCapacityStatus_Type.__name__ = "Integer32"
_InvertersCapacityStatus_Object = MibScalar
invertersCapacityStatus = _InvertersCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 3, 1),
    _InvertersCapacityStatus_Type()
)
invertersCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersCapacityStatus.setStatus("current")


class _InvertersCapacityDescription_Type(DisplayString):
    """Custom type invertersCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InvertersCapacityDescription_Type.__name__ = "DisplayString"
_InvertersCapacityDescription_Object = MibScalar
invertersCapacityDescription = _InvertersCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 3, 2),
    _InvertersCapacityDescription_Type()
)
invertersCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersCapacityDescription.setStatus("current")
_InvertersCapacityTrapRepeatCounter_Type = Counter32
_InvertersCapacityTrapRepeatCounter_Object = MibScalar
invertersCapacityTrapRepeatCounter = _InvertersCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 3, 3),
    _InvertersCapacityTrapRepeatCounter_Type()
)
invertersCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    invertersCapacityTrapRepeatCounter.setStatus("current")


class _InvertersCapacityAlarmEnable_Type(Integer32):
    """Custom type invertersCapacityAlarmEnable based on Integer32"""
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


_InvertersCapacityAlarmEnable_Type.__name__ = "Integer32"
_InvertersCapacityAlarmEnable_Object = MibScalar
invertersCapacityAlarmEnable = _InvertersCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 3, 4),
    _InvertersCapacityAlarmEnable_Type()
)
invertersCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersCapacityAlarmEnable.setStatus("current")
_InvertersCapacityValue_Type = Integer32
_InvertersCapacityValue_Object = MibScalar
invertersCapacityValue = _InvertersCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 3, 5),
    _InvertersCapacityValue_Type()
)
invertersCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersCapacityValue.setStatus("current")
_InvertersCapacityMajorAlarmLevel_Type = Integer32
_InvertersCapacityMajorAlarmLevel_Object = MibScalar
invertersCapacityMajorAlarmLevel = _InvertersCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 3, 6),
    _InvertersCapacityMajorAlarmLevel_Type()
)
invertersCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersCapacityMajorAlarmLevel.setStatus("current")
_InvertersCapacityMinorAlarmLevel_Type = Integer32
_InvertersCapacityMinorAlarmLevel_Object = MibScalar
invertersCapacityMinorAlarmLevel = _InvertersCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 3, 7),
    _InvertersCapacityMinorAlarmLevel_Type()
)
invertersCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersCapacityMinorAlarmLevel.setStatus("current")
_InvertersError_ObjectIdentity = ObjectIdentity
invertersError = _InvertersError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 4)
)


class _InvertersErrorStatus_Type(Integer32):
    """Custom type invertersErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InvertersErrorStatus_Type.__name__ = "Integer32"
_InvertersErrorStatus_Object = MibScalar
invertersErrorStatus = _InvertersErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 4, 1),
    _InvertersErrorStatus_Type()
)
invertersErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersErrorStatus.setStatus("current")


class _InvertersErrorDescription_Type(DisplayString):
    """Custom type invertersErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InvertersErrorDescription_Type.__name__ = "DisplayString"
_InvertersErrorDescription_Object = MibScalar
invertersErrorDescription = _InvertersErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 4, 2),
    _InvertersErrorDescription_Type()
)
invertersErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersErrorDescription.setStatus("current")
_InvertersErrorTrapRepeatCounter_Type = Counter32
_InvertersErrorTrapRepeatCounter_Object = MibScalar
invertersErrorTrapRepeatCounter = _InvertersErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 4, 3),
    _InvertersErrorTrapRepeatCounter_Type()
)
invertersErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    invertersErrorTrapRepeatCounter.setStatus("current")


class _InvertersErrorEnable_Type(Integer32):
    """Custom type invertersErrorEnable based on Integer32"""
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


_InvertersErrorEnable_Type.__name__ = "Integer32"
_InvertersErrorEnable_Object = MibScalar
invertersErrorEnable = _InvertersErrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 4, 4),
    _InvertersErrorEnable_Type()
)
invertersErrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersErrorEnable.setStatus("current")
_InvertersErrorValue_Type = Integer32
_InvertersErrorValue_Object = MibScalar
invertersErrorValue = _InvertersErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 4, 5),
    _InvertersErrorValue_Type()
)
invertersErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersErrorValue.setStatus("current")
_InvertersErrorMajorAlarmLevel_Type = Integer32
_InvertersErrorMajorAlarmLevel_Object = MibScalar
invertersErrorMajorAlarmLevel = _InvertersErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 4, 6),
    _InvertersErrorMajorAlarmLevel_Type()
)
invertersErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersErrorMajorAlarmLevel.setStatus("current")
_InvertersErrorMinorAlarmLevel_Type = Integer32
_InvertersErrorMinorAlarmLevel_Object = MibScalar
invertersErrorMinorAlarmLevel = _InvertersErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 4, 7),
    _InvertersErrorMinorAlarmLevel_Type()
)
invertersErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersErrorMinorAlarmLevel.setStatus("current")


class _InvertersNumberOfInverters_Type(Integer32):
    """Custom type invertersNumberOfInverters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_InvertersNumberOfInverters_Type.__name__ = "Integer32"
_InvertersNumberOfInverters_Object = MibScalar
invertersNumberOfInverters = _InvertersNumberOfInverters_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 5),
    _InvertersNumberOfInverters_Type()
)
invertersNumberOfInverters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    invertersNumberOfInverters.setStatus("current")
_InverterTable_Object = MibTable
inverterTable = _InverterTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6)
)
if mibBuilder.loadTexts:
    inverterTable.setStatus("current")
_InverterEntry_Object = MibTableRow
inverterEntry = _InverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1)
)
inverterEntry.setIndexNames(
    (0, "SP2-MIB", "inverterIndex"),
)
if mibBuilder.loadTexts:
    inverterEntry.setStatus("current")


class _InverterIndex_Type(Integer32):
    """Custom type inverterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_InverterIndex_Type.__name__ = "Integer32"
_InverterIndex_Object = MibTableColumn
inverterIndex = _InverterIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 1),
    _InverterIndex_Type()
)
inverterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterIndex.setStatus("current")


class _InverterStatus_Type(Integer32):
    """Custom type inverterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InverterStatus_Type.__name__ = "Integer32"
_InverterStatus_Object = MibTableColumn
inverterStatus = _InverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 2),
    _InverterStatus_Type()
)
inverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterStatus.setStatus("current")
_InverterOutputCurrentValue_Type = Integer32
_InverterOutputCurrentValue_Object = MibTableColumn
inverterOutputCurrentValue = _InverterOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 3),
    _InverterOutputCurrentValue_Type()
)
inverterOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterOutputCurrentValue.setStatus("current")
_InverterOutputVoltageValue_Type = Integer32
_InverterOutputVoltageValue_Object = MibTableColumn
inverterOutputVoltageValue = _InverterOutputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 4),
    _InverterOutputVoltageValue_Type()
)
inverterOutputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterOutputVoltageValue.setStatus("current")


class _InverterType_Type(DisplayString):
    """Custom type inverterType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_InverterType_Type.__name__ = "DisplayString"
_InverterType_Object = MibTableColumn
inverterType = _InverterType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 5),
    _InverterType_Type()
)
inverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterType.setStatus("current")


class _InverterHwPartNumber_Type(DisplayString):
    """Custom type inverterHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_InverterHwPartNumber_Type.__name__ = "DisplayString"
_InverterHwPartNumber_Object = MibTableColumn
inverterHwPartNumber = _InverterHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 6),
    _InverterHwPartNumber_Type()
)
inverterHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterHwPartNumber.setStatus("current")


class _InverterHwVersion_Type(DisplayString):
    """Custom type inverterHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_InverterHwVersion_Type.__name__ = "DisplayString"
_InverterHwVersion_Object = MibTableColumn
inverterHwVersion = _InverterHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 7),
    _InverterHwVersion_Type()
)
inverterHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterHwVersion.setStatus("current")


class _InverterSwPartNumber_Type(DisplayString):
    """Custom type inverterSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_InverterSwPartNumber_Type.__name__ = "DisplayString"
_InverterSwPartNumber_Object = MibTableColumn
inverterSwPartNumber = _InverterSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 8),
    _InverterSwPartNumber_Type()
)
inverterSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterSwPartNumber.setStatus("current")


class _InverterSwVersion_Type(DisplayString):
    """Custom type inverterSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_InverterSwVersion_Type.__name__ = "DisplayString"
_InverterSwVersion_Object = MibTableColumn
inverterSwVersion = _InverterSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 9),
    _InverterSwVersion_Type()
)
inverterSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterSwVersion.setStatus("current")
_InverterOutputFrequencyValue_Type = Integer32
_InverterOutputFrequencyValue_Object = MibTableColumn
inverterOutputFrequencyValue = _InverterOutputFrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 10),
    _InverterOutputFrequencyValue_Type()
)
inverterOutputFrequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterOutputFrequencyValue.setStatus("current")
_InverterOutputPowerValue_Type = Integer32
_InverterOutputPowerValue_Object = MibTableColumn
inverterOutputPowerValue = _InverterOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 11),
    _InverterOutputPowerValue_Type()
)
inverterOutputPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterOutputPowerValue.setStatus("current")
_InverterOutputReactivePowerValue_Type = Integer32
_InverterOutputReactivePowerValue_Object = MibTableColumn
inverterOutputReactivePowerValue = _InverterOutputReactivePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 6, 1, 12),
    _InverterOutputReactivePowerValue_Type()
)
inverterOutputReactivePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterOutputReactivePowerValue.setStatus("current")
_InvertersNumberOfGroups_Type = Integer32
_InvertersNumberOfGroups_Object = MibScalar
invertersNumberOfGroups = _InvertersNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 7),
    _InvertersNumberOfGroups_Type()
)
invertersNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersNumberOfGroups.setStatus("current")
_InverterGroupsTable_Object = MibTable
inverterGroupsTable = _InverterGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 8)
)
if mibBuilder.loadTexts:
    inverterGroupsTable.setStatus("current")
_InverterGroupsEntry_Object = MibTableRow
inverterGroupsEntry = _InverterGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 8, 1)
)
inverterGroupsEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupsEntry.setStatus("current")


class _InverterGroupIndex_Type(Integer32):
    """Custom type inverterGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_InverterGroupIndex_Type.__name__ = "Integer32"
_InverterGroupIndex_Object = MibTableColumn
inverterGroupIndex = _InverterGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 8, 1, 1),
    _InverterGroupIndex_Type()
)
inverterGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterGroupIndex.setStatus("current")


class _InverterGroupStatus_Type(Integer32):
    """Custom type inverterGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InverterGroupStatus_Type.__name__ = "Integer32"
_InverterGroupStatus_Object = MibTableColumn
inverterGroupStatus = _InverterGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 8, 1, 2),
    _InverterGroupStatus_Type()
)
inverterGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupStatus.setStatus("current")


class _InverterGroupNumberOfInverters_Type(Integer32):
    """Custom type inverterGroupNumberOfInverters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_InverterGroupNumberOfInverters_Type.__name__ = "Integer32"
_InverterGroupNumberOfInverters_Object = MibTableColumn
inverterGroupNumberOfInverters = _InverterGroupNumberOfInverters_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 8, 1, 3),
    _InverterGroupNumberOfInverters_Type()
)
inverterGroupNumberOfInverters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupNumberOfInverters.setStatus("current")
_InverterGroupCurrentTable_Object = MibTable
inverterGroupCurrentTable = _InverterGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9)
)
if mibBuilder.loadTexts:
    inverterGroupCurrentTable.setStatus("current")
_InverterGroupCurrentEntry_Object = MibTableRow
inverterGroupCurrentEntry = _InverterGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9, 1)
)
inverterGroupCurrentEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupCurrentEntry.setStatus("current")


class _InverterGroupCurrentStatus_Type(Integer32):
    """Custom type inverterGroupCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InverterGroupCurrentStatus_Type.__name__ = "Integer32"
_InverterGroupCurrentStatus_Object = MibTableColumn
inverterGroupCurrentStatus = _InverterGroupCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9, 1, 1),
    _InverterGroupCurrentStatus_Type()
)
inverterGroupCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupCurrentStatus.setStatus("current")


class _InverterGroupCurrentDescription_Type(DisplayString):
    """Custom type inverterGroupCurrentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InverterGroupCurrentDescription_Type.__name__ = "DisplayString"
_InverterGroupCurrentDescription_Object = MibTableColumn
inverterGroupCurrentDescription = _InverterGroupCurrentDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9, 1, 2),
    _InverterGroupCurrentDescription_Type()
)
inverterGroupCurrentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupCurrentDescription.setStatus("current")
_InverterGroupCurrentTrapRepeatCounter_Type = Integer32
_InverterGroupCurrentTrapRepeatCounter_Object = MibTableColumn
inverterGroupCurrentTrapRepeatCounter = _InverterGroupCurrentTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9, 1, 3),
    _InverterGroupCurrentTrapRepeatCounter_Type()
)
inverterGroupCurrentTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inverterGroupCurrentTrapRepeatCounter.setStatus("current")


class _InverterGroupCurrentAlarmEnable_Type(Integer32):
    """Custom type inverterGroupCurrentAlarmEnable based on Integer32"""
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


_InverterGroupCurrentAlarmEnable_Type.__name__ = "Integer32"
_InverterGroupCurrentAlarmEnable_Object = MibTableColumn
inverterGroupCurrentAlarmEnable = _InverterGroupCurrentAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9, 1, 4),
    _InverterGroupCurrentAlarmEnable_Type()
)
inverterGroupCurrentAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupCurrentAlarmEnable.setStatus("current")
_InverterGroupCurrentValue_Type = Integer32
_InverterGroupCurrentValue_Object = MibTableColumn
inverterGroupCurrentValue = _InverterGroupCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9, 1, 5),
    _InverterGroupCurrentValue_Type()
)
inverterGroupCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupCurrentValue.setStatus("current")
_InverterGroupCurrentMajorAlarmLevel_Type = Integer32
_InverterGroupCurrentMajorAlarmLevel_Object = MibTableColumn
inverterGroupCurrentMajorAlarmLevel = _InverterGroupCurrentMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9, 1, 6),
    _InverterGroupCurrentMajorAlarmLevel_Type()
)
inverterGroupCurrentMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupCurrentMajorAlarmLevel.setStatus("current")
_InverterGroupCurrentMinorAlarmLevel_Type = Integer32
_InverterGroupCurrentMinorAlarmLevel_Object = MibTableColumn
inverterGroupCurrentMinorAlarmLevel = _InverterGroupCurrentMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 9, 1, 7),
    _InverterGroupCurrentMinorAlarmLevel_Type()
)
inverterGroupCurrentMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupCurrentMinorAlarmLevel.setStatus("current")
_InverterGroupCapacityTable_Object = MibTable
inverterGroupCapacityTable = _InverterGroupCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10)
)
if mibBuilder.loadTexts:
    inverterGroupCapacityTable.setStatus("current")
_InverterGroupCapacityEntry_Object = MibTableRow
inverterGroupCapacityEntry = _InverterGroupCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10, 1)
)
inverterGroupCapacityEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupCapacityEntry.setStatus("current")


class _InverterGroupCapacityStatus_Type(Integer32):
    """Custom type inverterGroupCapacityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InverterGroupCapacityStatus_Type.__name__ = "Integer32"
_InverterGroupCapacityStatus_Object = MibTableColumn
inverterGroupCapacityStatus = _InverterGroupCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10, 1, 1),
    _InverterGroupCapacityStatus_Type()
)
inverterGroupCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupCapacityStatus.setStatus("current")


class _InverterGroupCapacityDescription_Type(DisplayString):
    """Custom type inverterGroupCapacityDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InverterGroupCapacityDescription_Type.__name__ = "DisplayString"
_InverterGroupCapacityDescription_Object = MibTableColumn
inverterGroupCapacityDescription = _InverterGroupCapacityDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10, 1, 2),
    _InverterGroupCapacityDescription_Type()
)
inverterGroupCapacityDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupCapacityDescription.setStatus("current")
_InverterGroupCapacityTrapRepeatCounter_Type = Integer32
_InverterGroupCapacityTrapRepeatCounter_Object = MibTableColumn
inverterGroupCapacityTrapRepeatCounter = _InverterGroupCapacityTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10, 1, 3),
    _InverterGroupCapacityTrapRepeatCounter_Type()
)
inverterGroupCapacityTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inverterGroupCapacityTrapRepeatCounter.setStatus("current")


class _InverterGroupCapacityAlarmEnable_Type(Integer32):
    """Custom type inverterGroupCapacityAlarmEnable based on Integer32"""
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


_InverterGroupCapacityAlarmEnable_Type.__name__ = "Integer32"
_InverterGroupCapacityAlarmEnable_Object = MibTableColumn
inverterGroupCapacityAlarmEnable = _InverterGroupCapacityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10, 1, 4),
    _InverterGroupCapacityAlarmEnable_Type()
)
inverterGroupCapacityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupCapacityAlarmEnable.setStatus("current")
_InverterGroupCapacityValue_Type = Integer32
_InverterGroupCapacityValue_Object = MibTableColumn
inverterGroupCapacityValue = _InverterGroupCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10, 1, 5),
    _InverterGroupCapacityValue_Type()
)
inverterGroupCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupCapacityValue.setStatus("current")
_InverterGroupCapacityMajorAlarmLevel_Type = Integer32
_InverterGroupCapacityMajorAlarmLevel_Object = MibTableColumn
inverterGroupCapacityMajorAlarmLevel = _InverterGroupCapacityMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10, 1, 6),
    _InverterGroupCapacityMajorAlarmLevel_Type()
)
inverterGroupCapacityMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupCapacityMajorAlarmLevel.setStatus("current")
_InverterGroupCapacityMinorAlarmLevel_Type = Integer32
_InverterGroupCapacityMinorAlarmLevel_Object = MibTableColumn
inverterGroupCapacityMinorAlarmLevel = _InverterGroupCapacityMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 10, 1, 7),
    _InverterGroupCapacityMinorAlarmLevel_Type()
)
inverterGroupCapacityMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupCapacityMinorAlarmLevel.setStatus("current")
_InverterGroupErrorTable_Object = MibTable
inverterGroupErrorTable = _InverterGroupErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11)
)
if mibBuilder.loadTexts:
    inverterGroupErrorTable.setStatus("current")
_InverterGroupErrorEntry_Object = MibTableRow
inverterGroupErrorEntry = _InverterGroupErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11, 1)
)
inverterGroupErrorEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupErrorEntry.setStatus("current")


class _InverterGroupErrorStatus_Type(Integer32):
    """Custom type inverterGroupErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InverterGroupErrorStatus_Type.__name__ = "Integer32"
_InverterGroupErrorStatus_Object = MibTableColumn
inverterGroupErrorStatus = _InverterGroupErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11, 1, 1),
    _InverterGroupErrorStatus_Type()
)
inverterGroupErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupErrorStatus.setStatus("current")


class _InverterGroupErrorDescription_Type(DisplayString):
    """Custom type inverterGroupErrorDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InverterGroupErrorDescription_Type.__name__ = "DisplayString"
_InverterGroupErrorDescription_Object = MibTableColumn
inverterGroupErrorDescription = _InverterGroupErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11, 1, 2),
    _InverterGroupErrorDescription_Type()
)
inverterGroupErrorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupErrorDescription.setStatus("current")
_InverterGroupErrorTrapRepeatCounter_Type = Integer32
_InverterGroupErrorTrapRepeatCounter_Object = MibTableColumn
inverterGroupErrorTrapRepeatCounter = _InverterGroupErrorTrapRepeatCounter_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11, 1, 3),
    _InverterGroupErrorTrapRepeatCounter_Type()
)
inverterGroupErrorTrapRepeatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    inverterGroupErrorTrapRepeatCounter.setStatus("current")


class _InverterGroupErrorAlarmEnable_Type(Integer32):
    """Custom type inverterGroupErrorAlarmEnable based on Integer32"""
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


_InverterGroupErrorAlarmEnable_Type.__name__ = "Integer32"
_InverterGroupErrorAlarmEnable_Object = MibTableColumn
inverterGroupErrorAlarmEnable = _InverterGroupErrorAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11, 1, 4),
    _InverterGroupErrorAlarmEnable_Type()
)
inverterGroupErrorAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupErrorAlarmEnable.setStatus("current")
_InverterGroupErrorValue_Type = Integer32
_InverterGroupErrorValue_Object = MibTableColumn
inverterGroupErrorValue = _InverterGroupErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11, 1, 5),
    _InverterGroupErrorValue_Type()
)
inverterGroupErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupErrorValue.setStatus("current")
_InverterGroupErrorMajorAlarmLevel_Type = Integer32
_InverterGroupErrorMajorAlarmLevel_Object = MibTableColumn
inverterGroupErrorMajorAlarmLevel = _InverterGroupErrorMajorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11, 1, 6),
    _InverterGroupErrorMajorAlarmLevel_Type()
)
inverterGroupErrorMajorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupErrorMajorAlarmLevel.setStatus("current")
_InverterGroupErrorMinorAlarmLevel_Type = Integer32
_InverterGroupErrorMinorAlarmLevel_Object = MibTableColumn
inverterGroupErrorMinorAlarmLevel = _InverterGroupErrorMinorAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 11, 1, 7),
    _InverterGroupErrorMinorAlarmLevel_Type()
)
inverterGroupErrorMinorAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inverterGroupErrorMinorAlarmLevel.setStatus("current")
_InverterGroupInverterTable_Object = MibTable
inverterGroupInverterTable = _InverterGroupInverterTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12)
)
if mibBuilder.loadTexts:
    inverterGroupInverterTable.setStatus("current")
_InverterGroupInverterEntry_Object = MibTableRow
inverterGroupInverterEntry = _InverterGroupInverterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1)
)
inverterGroupInverterEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
    (0, "SP2-MIB", "inverterGroupInverterIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupInverterEntry.setStatus("current")


class _InverterGroupInverterIndex_Type(Integer32):
    """Custom type inverterGroupInverterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_InverterGroupInverterIndex_Type.__name__ = "Integer32"
_InverterGroupInverterIndex_Object = MibTableColumn
inverterGroupInverterIndex = _InverterGroupInverterIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 1),
    _InverterGroupInverterIndex_Type()
)
inverterGroupInverterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterGroupInverterIndex.setStatus("current")


class _InverterGroupInverterStatus_Type(Integer32):
    """Custom type inverterGroupInverterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("normal", 1),
          ("minorAlarm", 2),
          ("majorAlarm", 3),
          ("disabled", 4),
          ("disconnected", 5),
          ("notPresent", 6),
          ("minorAndMajor", 7),
          ("majorLow", 8),
          ("minorLow", 9),
          ("majorHigh", 10),
          ("minorHigh", 11),
          ("event", 12),
          ("valueVolt", 13),
          ("valueAmp", 14),
          ("valueTemp", 15),
          ("valueUnit", 16),
          ("valuePerCent", 17),
          ("critical", 18),
          ("warning", 19))
    )


_InverterGroupInverterStatus_Type.__name__ = "Integer32"
_InverterGroupInverterStatus_Object = MibTableColumn
inverterGroupInverterStatus = _InverterGroupInverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 2),
    _InverterGroupInverterStatus_Type()
)
inverterGroupInverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterStatus.setStatus("current")
_InverterGroupInverterOutputCurrentValue_Type = Integer32
_InverterGroupInverterOutputCurrentValue_Object = MibTableColumn
inverterGroupInverterOutputCurrentValue = _InverterGroupInverterOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 3),
    _InverterGroupInverterOutputCurrentValue_Type()
)
inverterGroupInverterOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterOutputCurrentValue.setStatus("current")
_InverterGroupInverterOutputVoltageValue_Type = Integer32
_InverterGroupInverterOutputVoltageValue_Object = MibTableColumn
inverterGroupInverterOutputVoltageValue = _InverterGroupInverterOutputVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 4),
    _InverterGroupInverterOutputVoltageValue_Type()
)
inverterGroupInverterOutputVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterOutputVoltageValue.setStatus("current")


class _InverterGroupInverterType_Type(DisplayString):
    """Custom type inverterGroupInverterType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )


_InverterGroupInverterType_Type.__name__ = "DisplayString"
_InverterGroupInverterType_Object = MibTableColumn
inverterGroupInverterType = _InverterGroupInverterType_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 5),
    _InverterGroupInverterType_Type()
)
inverterGroupInverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterType.setStatus("current")


class _InverterGroupInverterHwPartNumber_Type(DisplayString):
    """Custom type inverterGroupInverterHwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_InverterGroupInverterHwPartNumber_Type.__name__ = "DisplayString"
_InverterGroupInverterHwPartNumber_Object = MibTableColumn
inverterGroupInverterHwPartNumber = _InverterGroupInverterHwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 6),
    _InverterGroupInverterHwPartNumber_Type()
)
inverterGroupInverterHwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterHwPartNumber.setStatus("current")


class _InverterGroupInverterHwVersion_Type(DisplayString):
    """Custom type inverterGroupInverterHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_InverterGroupInverterHwVersion_Type.__name__ = "DisplayString"
_InverterGroupInverterHwVersion_Object = MibTableColumn
inverterGroupInverterHwVersion = _InverterGroupInverterHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 7),
    _InverterGroupInverterHwVersion_Type()
)
inverterGroupInverterHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterHwVersion.setStatus("current")


class _InverterGroupInverterSwPartNumber_Type(DisplayString):
    """Custom type inverterGroupInverterSwPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_InverterGroupInverterSwPartNumber_Type.__name__ = "DisplayString"
_InverterGroupInverterSwPartNumber_Object = MibTableColumn
inverterGroupInverterSwPartNumber = _InverterGroupInverterSwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 8),
    _InverterGroupInverterSwPartNumber_Type()
)
inverterGroupInverterSwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterSwPartNumber.setStatus("current")


class _InverterGroupInverterSwVersion_Type(DisplayString):
    """Custom type inverterGroupInverterSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_InverterGroupInverterSwVersion_Type.__name__ = "DisplayString"
_InverterGroupInverterSwVersion_Object = MibTableColumn
inverterGroupInverterSwVersion = _InverterGroupInverterSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 9),
    _InverterGroupInverterSwVersion_Type()
)
inverterGroupInverterSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterSwVersion.setStatus("current")
_InverterGroupInverterOutputFrequencyValue_Type = Integer32
_InverterGroupInverterOutputFrequencyValue_Object = MibTableColumn
inverterGroupInverterOutputFrequencyValue = _InverterGroupInverterOutputFrequencyValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 10),
    _InverterGroupInverterOutputFrequencyValue_Type()
)
inverterGroupInverterOutputFrequencyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterOutputFrequencyValue.setStatus("current")
_InverterGroupInverterOutputPowerValue_Type = Integer32
_InverterGroupInverterOutputPowerValue_Object = MibTableColumn
inverterGroupInverterOutputPowerValue = _InverterGroupInverterOutputPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 11),
    _InverterGroupInverterOutputPowerValue_Type()
)
inverterGroupInverterOutputPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterOutputPowerValue.setStatus("current")
_InverterGroupInverterOutputReactivePowerValue_Type = Integer32
_InverterGroupInverterOutputReactivePowerValue_Object = MibTableColumn
inverterGroupInverterOutputReactivePowerValue = _InverterGroupInverterOutputReactivePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 12, 1, 12),
    _InverterGroupInverterOutputReactivePowerValue_Type()
)
inverterGroupInverterOutputReactivePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupInverterOutputReactivePowerValue.setStatus("current")
_InvertersEnergyLog_ObjectIdentity = ObjectIdentity
invertersEnergyLog = _InvertersEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13)
)
_InvertersEnergyLogAccumulated_Type = Integer32
_InvertersEnergyLogAccumulated_Object = MibScalar
invertersEnergyLogAccumulated = _InvertersEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 1),
    _InvertersEnergyLogAccumulated_Type()
)
invertersEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersEnergyLogAccumulated.setStatus("current")


class _InvertersEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type invertersEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_InvertersEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_InvertersEnergyLogLastHoursNumberOfEntries_Object = MibScalar
invertersEnergyLogLastHoursNumberOfEntries = _InvertersEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 2),
    _InvertersEnergyLogLastHoursNumberOfEntries_Type()
)
invertersEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersEnergyLogLastHoursNumberOfEntries.setStatus("current")
_InvertersEnergyLogLastHoursTable_Object = MibTable
invertersEnergyLogLastHoursTable = _InvertersEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 3)
)
if mibBuilder.loadTexts:
    invertersEnergyLogLastHoursTable.setStatus("current")
_InvertersEnergyLogLastHoursEntry_Object = MibTableRow
invertersEnergyLogLastHoursEntry = _InvertersEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 3, 1)
)
invertersEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "invertersEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    invertersEnergyLogLastHoursEntry.setStatus("current")


class _InvertersEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type invertersEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InvertersEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_InvertersEnergyLogLastHoursIndex_Object = MibTableColumn
invertersEnergyLogLastHoursIndex = _InvertersEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 3, 1, 1),
    _InvertersEnergyLogLastHoursIndex_Type()
)
invertersEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invertersEnergyLogLastHoursIndex.setStatus("current")
_InvertersEnergyLogLastHoursValue_Type = Integer32
_InvertersEnergyLogLastHoursValue_Object = MibTableColumn
invertersEnergyLogLastHoursValue = _InvertersEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 3, 1, 2),
    _InvertersEnergyLogLastHoursValue_Type()
)
invertersEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersEnergyLogLastHoursValue.setStatus("current")


class _InvertersEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type invertersEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_InvertersEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_InvertersEnergyLogLastDaysNumberOfEntries_Object = MibScalar
invertersEnergyLogLastDaysNumberOfEntries = _InvertersEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 4),
    _InvertersEnergyLogLastDaysNumberOfEntries_Type()
)
invertersEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersEnergyLogLastDaysNumberOfEntries.setStatus("current")
_InvertersEnergyLogLastDaysTable_Object = MibTable
invertersEnergyLogLastDaysTable = _InvertersEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 5)
)
if mibBuilder.loadTexts:
    invertersEnergyLogLastDaysTable.setStatus("current")
_InvertersEnergyLogLastDaysEntry_Object = MibTableRow
invertersEnergyLogLastDaysEntry = _InvertersEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 5, 1)
)
invertersEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "invertersEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    invertersEnergyLogLastDaysEntry.setStatus("current")


class _InvertersEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type invertersEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InvertersEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_InvertersEnergyLogLastDaysIndex_Object = MibTableColumn
invertersEnergyLogLastDaysIndex = _InvertersEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 5, 1, 1),
    _InvertersEnergyLogLastDaysIndex_Type()
)
invertersEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invertersEnergyLogLastDaysIndex.setStatus("current")
_InvertersEnergyLogLastDaysValue_Type = Integer32
_InvertersEnergyLogLastDaysValue_Object = MibTableColumn
invertersEnergyLogLastDaysValue = _InvertersEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 5, 1, 2),
    _InvertersEnergyLogLastDaysValue_Type()
)
invertersEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersEnergyLogLastDaysValue.setStatus("current")


class _InvertersEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type invertersEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_InvertersEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_InvertersEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
invertersEnergyLogLastWeeksNumberOfEntries = _InvertersEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 6),
    _InvertersEnergyLogLastWeeksNumberOfEntries_Type()
)
invertersEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_InvertersEnergyLogLastWeeksTable_Object = MibTable
invertersEnergyLogLastWeeksTable = _InvertersEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 7)
)
if mibBuilder.loadTexts:
    invertersEnergyLogLastWeeksTable.setStatus("current")
_InvertersEnergyLogLastWeeksEntry_Object = MibTableRow
invertersEnergyLogLastWeeksEntry = _InvertersEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 7, 1)
)
invertersEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "invertersEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    invertersEnergyLogLastWeeksEntry.setStatus("current")


class _InvertersEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type invertersEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InvertersEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_InvertersEnergyLogLastWeeksIndex_Object = MibTableColumn
invertersEnergyLogLastWeeksIndex = _InvertersEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 7, 1, 1),
    _InvertersEnergyLogLastWeeksIndex_Type()
)
invertersEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invertersEnergyLogLastWeeksIndex.setStatus("current")
_InvertersEnergyLogLastWeeksValue_Type = Integer32
_InvertersEnergyLogLastWeeksValue_Object = MibTableColumn
invertersEnergyLogLastWeeksValue = _InvertersEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 13, 7, 1, 2),
    _InvertersEnergyLogLastWeeksValue_Type()
)
invertersEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersEnergyLogLastWeeksValue.setStatus("current")
_InverterGroupEnergyLogTable_Object = MibTable
inverterGroupEnergyLogTable = _InverterGroupEnergyLogTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 14)
)
if mibBuilder.loadTexts:
    inverterGroupEnergyLogTable.setStatus("current")
_InverterGroupEnergyLogEntry_Object = MibTableRow
inverterGroupEnergyLogEntry = _InverterGroupEnergyLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 14, 1)
)
inverterGroupEnergyLogEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupEnergyLogEntry.setStatus("current")
_InverterGroupEnergyLogAccumulated_Type = Integer32
_InverterGroupEnergyLogAccumulated_Object = MibTableColumn
inverterGroupEnergyLogAccumulated = _InverterGroupEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 14, 1, 1),
    _InverterGroupEnergyLogAccumulated_Type()
)
inverterGroupEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogAccumulated.setStatus("current")
_InverterGroupEnergyLogLastHoursNumberOfEntries_Type = Integer32
_InverterGroupEnergyLogLastHoursNumberOfEntries_Object = MibTableColumn
inverterGroupEnergyLogLastHoursNumberOfEntries = _InverterGroupEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 14, 1, 2),
    _InverterGroupEnergyLogLastHoursNumberOfEntries_Type()
)
inverterGroupEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastHoursNumberOfEntries.setStatus("current")
_InverterGroupEnergyLogLastDaysNumberOfEntries_Type = Integer32
_InverterGroupEnergyLogLastDaysNumberOfEntries_Object = MibTableColumn
inverterGroupEnergyLogLastDaysNumberOfEntries = _InverterGroupEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 14, 1, 3),
    _InverterGroupEnergyLogLastDaysNumberOfEntries_Type()
)
inverterGroupEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastDaysNumberOfEntries.setStatus("current")
_InverterGroupEnergyLogLastWeeksNumberOfEntries_Type = Integer32
_InverterGroupEnergyLogLastWeeksNumberOfEntries_Object = MibTableColumn
inverterGroupEnergyLogLastWeeksNumberOfEntries = _InverterGroupEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 14, 1, 4),
    _InverterGroupEnergyLogLastWeeksNumberOfEntries_Type()
)
inverterGroupEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_InverterGroupEnergyLogLastHoursTable_Object = MibTable
inverterGroupEnergyLogLastHoursTable = _InverterGroupEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 15)
)
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastHoursTable.setStatus("current")
_InverterGroupEnergyLogLastHoursEntry_Object = MibTableRow
inverterGroupEnergyLogLastHoursEntry = _InverterGroupEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 15, 1)
)
inverterGroupEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
    (0, "SP2-MIB", "inverterGroupEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastHoursEntry.setStatus("current")


class _InverterGroupEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type inverterGroupEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InverterGroupEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_InverterGroupEnergyLogLastHoursIndex_Object = MibTableColumn
inverterGroupEnergyLogLastHoursIndex = _InverterGroupEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 15, 1, 1),
    _InverterGroupEnergyLogLastHoursIndex_Type()
)
inverterGroupEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastHoursIndex.setStatus("current")
_InverterGroupEnergyLogLastHoursValue_Type = Integer32
_InverterGroupEnergyLogLastHoursValue_Object = MibTableColumn
inverterGroupEnergyLogLastHoursValue = _InverterGroupEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 15, 1, 2),
    _InverterGroupEnergyLogLastHoursValue_Type()
)
inverterGroupEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastHoursValue.setStatus("current")
_InverterGroupEnergyLogLastDaysTable_Object = MibTable
inverterGroupEnergyLogLastDaysTable = _InverterGroupEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 16)
)
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastDaysTable.setStatus("current")
_InverterGroupEnergyLogLastDaysEntry_Object = MibTableRow
inverterGroupEnergyLogLastDaysEntry = _InverterGroupEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 16, 1)
)
inverterGroupEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
    (0, "SP2-MIB", "inverterGroupEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastDaysEntry.setStatus("current")


class _InverterGroupEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type inverterGroupEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InverterGroupEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_InverterGroupEnergyLogLastDaysIndex_Object = MibTableColumn
inverterGroupEnergyLogLastDaysIndex = _InverterGroupEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 16, 1, 1),
    _InverterGroupEnergyLogLastDaysIndex_Type()
)
inverterGroupEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastDaysIndex.setStatus("current")
_InverterGroupEnergyLogLastDaysValue_Type = Integer32
_InverterGroupEnergyLogLastDaysValue_Object = MibTableColumn
inverterGroupEnergyLogLastDaysValue = _InverterGroupEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 16, 1, 2),
    _InverterGroupEnergyLogLastDaysValue_Type()
)
inverterGroupEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastDaysValue.setStatus("current")
_InverterGroupEnergyLogLastWeeksTable_Object = MibTable
inverterGroupEnergyLogLastWeeksTable = _InverterGroupEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 17)
)
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastWeeksTable.setStatus("current")
_InverterGroupEnergyLogLastWeeksEntry_Object = MibTableRow
inverterGroupEnergyLogLastWeeksEntry = _InverterGroupEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 17, 1)
)
inverterGroupEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
    (0, "SP2-MIB", "inverterGroupEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastWeeksEntry.setStatus("current")


class _InverterGroupEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type inverterGroupEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InverterGroupEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_InverterGroupEnergyLogLastWeeksIndex_Object = MibTableColumn
inverterGroupEnergyLogLastWeeksIndex = _InverterGroupEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 17, 1, 1),
    _InverterGroupEnergyLogLastWeeksIndex_Type()
)
inverterGroupEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastWeeksIndex.setStatus("current")
_InverterGroupEnergyLogLastWeeksValue_Type = Integer32
_InverterGroupEnergyLogLastWeeksValue_Object = MibTableColumn
inverterGroupEnergyLogLastWeeksValue = _InverterGroupEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 17, 1, 2),
    _InverterGroupEnergyLogLastWeeksValue_Type()
)
inverterGroupEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupEnergyLogLastWeeksValue.setStatus("current")
_InvertersReactiveEnergyLog_ObjectIdentity = ObjectIdentity
invertersReactiveEnergyLog = _InvertersReactiveEnergyLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18)
)
_InvertersReactiveEnergyLogAccumulated_Type = Integer32
_InvertersReactiveEnergyLogAccumulated_Object = MibScalar
invertersReactiveEnergyLogAccumulated = _InvertersReactiveEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 1),
    _InvertersReactiveEnergyLogAccumulated_Type()
)
invertersReactiveEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogAccumulated.setStatus("current")


class _InvertersReactiveEnergyLogLastHoursNumberOfEntries_Type(Integer32):
    """Custom type invertersReactiveEnergyLogLastHoursNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_InvertersReactiveEnergyLogLastHoursNumberOfEntries_Type.__name__ = "Integer32"
_InvertersReactiveEnergyLogLastHoursNumberOfEntries_Object = MibScalar
invertersReactiveEnergyLogLastHoursNumberOfEntries = _InvertersReactiveEnergyLogLastHoursNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 2),
    _InvertersReactiveEnergyLogLastHoursNumberOfEntries_Type()
)
invertersReactiveEnergyLogLastHoursNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastHoursNumberOfEntries.setStatus("current")
_InvertersReactiveEnergyLogLastHoursTable_Object = MibTable
invertersReactiveEnergyLogLastHoursTable = _InvertersReactiveEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 3)
)
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastHoursTable.setStatus("current")
_InvertersReactiveEnergyLogLastHoursEntry_Object = MibTableRow
invertersReactiveEnergyLogLastHoursEntry = _InvertersReactiveEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 3, 1)
)
invertersReactiveEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "invertersReactiveEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastHoursEntry.setStatus("current")


class _InvertersReactiveEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type invertersReactiveEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InvertersReactiveEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_InvertersReactiveEnergyLogLastHoursIndex_Object = MibTableColumn
invertersReactiveEnergyLogLastHoursIndex = _InvertersReactiveEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 3, 1, 1),
    _InvertersReactiveEnergyLogLastHoursIndex_Type()
)
invertersReactiveEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastHoursIndex.setStatus("current")
_InvertersReactiveEnergyLogLastHoursValue_Type = Integer32
_InvertersReactiveEnergyLogLastHoursValue_Object = MibTableColumn
invertersReactiveEnergyLogLastHoursValue = _InvertersReactiveEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 3, 1, 2),
    _InvertersReactiveEnergyLogLastHoursValue_Type()
)
invertersReactiveEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastHoursValue.setStatus("current")


class _InvertersReactiveEnergyLogLastDaysNumberOfEntries_Type(Integer32):
    """Custom type invertersReactiveEnergyLogLastDaysNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_InvertersReactiveEnergyLogLastDaysNumberOfEntries_Type.__name__ = "Integer32"
_InvertersReactiveEnergyLogLastDaysNumberOfEntries_Object = MibScalar
invertersReactiveEnergyLogLastDaysNumberOfEntries = _InvertersReactiveEnergyLogLastDaysNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 4),
    _InvertersReactiveEnergyLogLastDaysNumberOfEntries_Type()
)
invertersReactiveEnergyLogLastDaysNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastDaysNumberOfEntries.setStatus("current")
_InvertersReactiveEnergyLogLastDaysTable_Object = MibTable
invertersReactiveEnergyLogLastDaysTable = _InvertersReactiveEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 5)
)
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastDaysTable.setStatus("current")
_InvertersReactiveEnergyLogLastDaysEntry_Object = MibTableRow
invertersReactiveEnergyLogLastDaysEntry = _InvertersReactiveEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 5, 1)
)
invertersReactiveEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "invertersReactiveEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastDaysEntry.setStatus("current")


class _InvertersReactiveEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type invertersReactiveEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InvertersReactiveEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_InvertersReactiveEnergyLogLastDaysIndex_Object = MibTableColumn
invertersReactiveEnergyLogLastDaysIndex = _InvertersReactiveEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 5, 1, 1),
    _InvertersReactiveEnergyLogLastDaysIndex_Type()
)
invertersReactiveEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastDaysIndex.setStatus("current")
_InvertersReactiveEnergyLogLastDaysValue_Type = Integer32
_InvertersReactiveEnergyLogLastDaysValue_Object = MibTableColumn
invertersReactiveEnergyLogLastDaysValue = _InvertersReactiveEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 5, 1, 2),
    _InvertersReactiveEnergyLogLastDaysValue_Type()
)
invertersReactiveEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastDaysValue.setStatus("current")


class _InvertersReactiveEnergyLogLastWeeksNumberOfEntries_Type(Integer32):
    """Custom type invertersReactiveEnergyLogLastWeeksNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_InvertersReactiveEnergyLogLastWeeksNumberOfEntries_Type.__name__ = "Integer32"
_InvertersReactiveEnergyLogLastWeeksNumberOfEntries_Object = MibScalar
invertersReactiveEnergyLogLastWeeksNumberOfEntries = _InvertersReactiveEnergyLogLastWeeksNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 6),
    _InvertersReactiveEnergyLogLastWeeksNumberOfEntries_Type()
)
invertersReactiveEnergyLogLastWeeksNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastWeeksNumberOfEntries.setStatus("current")
_InvertersReactiveEnergyLogLastWeeksTable_Object = MibTable
invertersReactiveEnergyLogLastWeeksTable = _InvertersReactiveEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 7)
)
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastWeeksTable.setStatus("current")
_InvertersReactiveEnergyLogLastWeeksEntry_Object = MibTableRow
invertersReactiveEnergyLogLastWeeksEntry = _InvertersReactiveEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 7, 1)
)
invertersReactiveEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "invertersReactiveEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastWeeksEntry.setStatus("current")


class _InvertersReactiveEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type invertersReactiveEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InvertersReactiveEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_InvertersReactiveEnergyLogLastWeeksIndex_Object = MibTableColumn
invertersReactiveEnergyLogLastWeeksIndex = _InvertersReactiveEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 7, 1, 1),
    _InvertersReactiveEnergyLogLastWeeksIndex_Type()
)
invertersReactiveEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastWeeksIndex.setStatus("current")
_InvertersReactiveEnergyLogLastWeeksValue_Type = Integer32
_InvertersReactiveEnergyLogLastWeeksValue_Object = MibTableColumn
invertersReactiveEnergyLogLastWeeksValue = _InvertersReactiveEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 18, 7, 1, 2),
    _InvertersReactiveEnergyLogLastWeeksValue_Type()
)
invertersReactiveEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invertersReactiveEnergyLogLastWeeksValue.setStatus("current")
_InverterGroupReactiveEnergyLogTable_Object = MibTable
inverterGroupReactiveEnergyLogTable = _InverterGroupReactiveEnergyLogTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 19)
)
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogTable.setStatus("current")
_InverterGroupReactiveEnergyLogEntry_Object = MibTableRow
inverterGroupReactiveEnergyLogEntry = _InverterGroupReactiveEnergyLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 19, 1)
)
inverterGroupReactiveEnergyLogEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogEntry.setStatus("current")
_InverterGroupReactiveEnergyLogAccumulated_Type = Integer32
_InverterGroupReactiveEnergyLogAccumulated_Object = MibTableColumn
inverterGroupReactiveEnergyLogAccumulated = _InverterGroupReactiveEnergyLogAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 19, 1, 1),
    _InverterGroupReactiveEnergyLogAccumulated_Type()
)
inverterGroupReactiveEnergyLogAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogAccumulated.setStatus("current")
_InverterGroupReactiveEnergyLogLastHoursNoOfEntries_Type = Integer32
_InverterGroupReactiveEnergyLogLastHoursNoOfEntries_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastHoursNoOfEntries = _InverterGroupReactiveEnergyLogLastHoursNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 19, 1, 2),
    _InverterGroupReactiveEnergyLogLastHoursNoOfEntries_Type()
)
inverterGroupReactiveEnergyLogLastHoursNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastHoursNoOfEntries.setStatus("current")
_InverterGroupReactiveEnergyLogLastDaysNoOfEntries_Type = Integer32
_InverterGroupReactiveEnergyLogLastDaysNoOfEntries_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastDaysNoOfEntries = _InverterGroupReactiveEnergyLogLastDaysNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 19, 1, 3),
    _InverterGroupReactiveEnergyLogLastDaysNoOfEntries_Type()
)
inverterGroupReactiveEnergyLogLastDaysNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastDaysNoOfEntries.setStatus("current")
_InverterGroupReactiveEnergyLogLastWeeksNoOfEntries_Type = Integer32
_InverterGroupReactiveEnergyLogLastWeeksNoOfEntries_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastWeeksNoOfEntries = _InverterGroupReactiveEnergyLogLastWeeksNoOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 19, 1, 4),
    _InverterGroupReactiveEnergyLogLastWeeksNoOfEntries_Type()
)
inverterGroupReactiveEnergyLogLastWeeksNoOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastWeeksNoOfEntries.setStatus("current")
_InverterGroupReactiveEnergyLogLastHoursTable_Object = MibTable
inverterGroupReactiveEnergyLogLastHoursTable = _InverterGroupReactiveEnergyLogLastHoursTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 20)
)
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastHoursTable.setStatus("current")
_InverterGroupReactiveEnergyLogLastHoursEntry_Object = MibTableRow
inverterGroupReactiveEnergyLogLastHoursEntry = _InverterGroupReactiveEnergyLogLastHoursEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 20, 1)
)
inverterGroupReactiveEnergyLogLastHoursEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
    (0, "SP2-MIB", "inverterGroupReactiveEnergyLogLastHoursIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastHoursEntry.setStatus("current")


class _InverterGroupReactiveEnergyLogLastHoursIndex_Type(Integer32):
    """Custom type inverterGroupReactiveEnergyLogLastHoursIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InverterGroupReactiveEnergyLogLastHoursIndex_Type.__name__ = "Integer32"
_InverterGroupReactiveEnergyLogLastHoursIndex_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastHoursIndex = _InverterGroupReactiveEnergyLogLastHoursIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 20, 1, 1),
    _InverterGroupReactiveEnergyLogLastHoursIndex_Type()
)
inverterGroupReactiveEnergyLogLastHoursIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastHoursIndex.setStatus("current")
_InverterGroupReactiveEnergyLogLastHoursValue_Type = Integer32
_InverterGroupReactiveEnergyLogLastHoursValue_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastHoursValue = _InverterGroupReactiveEnergyLogLastHoursValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 20, 1, 2),
    _InverterGroupReactiveEnergyLogLastHoursValue_Type()
)
inverterGroupReactiveEnergyLogLastHoursValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastHoursValue.setStatus("current")
_InverterGroupReactiveEnergyLogLastDaysTable_Object = MibTable
inverterGroupReactiveEnergyLogLastDaysTable = _InverterGroupReactiveEnergyLogLastDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 21)
)
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastDaysTable.setStatus("current")
_InverterGroupReactiveEnergyLogLastDaysEntry_Object = MibTableRow
inverterGroupReactiveEnergyLogLastDaysEntry = _InverterGroupReactiveEnergyLogLastDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 21, 1)
)
inverterGroupReactiveEnergyLogLastDaysEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
    (0, "SP2-MIB", "inverterGroupReactiveEnergyLogLastDaysIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastDaysEntry.setStatus("current")


class _InverterGroupReactiveEnergyLogLastDaysIndex_Type(Integer32):
    """Custom type inverterGroupReactiveEnergyLogLastDaysIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InverterGroupReactiveEnergyLogLastDaysIndex_Type.__name__ = "Integer32"
_InverterGroupReactiveEnergyLogLastDaysIndex_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastDaysIndex = _InverterGroupReactiveEnergyLogLastDaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 21, 1, 1),
    _InverterGroupReactiveEnergyLogLastDaysIndex_Type()
)
inverterGroupReactiveEnergyLogLastDaysIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastDaysIndex.setStatus("current")
_InverterGroupReactiveEnergyLogLastDaysValue_Type = Integer32
_InverterGroupReactiveEnergyLogLastDaysValue_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastDaysValue = _InverterGroupReactiveEnergyLogLastDaysValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 21, 1, 2),
    _InverterGroupReactiveEnergyLogLastDaysValue_Type()
)
inverterGroupReactiveEnergyLogLastDaysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastDaysValue.setStatus("current")
_InverterGroupReactiveEnergyLogLastWeeksTable_Object = MibTable
inverterGroupReactiveEnergyLogLastWeeksTable = _InverterGroupReactiveEnergyLogLastWeeksTable_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 22)
)
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastWeeksTable.setStatus("current")
_InverterGroupReactiveEnergyLogLastWeeksEntry_Object = MibTableRow
inverterGroupReactiveEnergyLogLastWeeksEntry = _InverterGroupReactiveEnergyLogLastWeeksEntry_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 22, 1)
)
inverterGroupReactiveEnergyLogLastWeeksEntry.setIndexNames(
    (0, "SP2-MIB", "inverterGroupIndex"),
    (0, "SP2-MIB", "inverterGroupReactiveEnergyLogLastWeeksIndex"),
)
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastWeeksEntry.setStatus("current")


class _InverterGroupReactiveEnergyLogLastWeeksIndex_Type(Integer32):
    """Custom type inverterGroupReactiveEnergyLogLastWeeksIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_InverterGroupReactiveEnergyLogLastWeeksIndex_Type.__name__ = "Integer32"
_InverterGroupReactiveEnergyLogLastWeeksIndex_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastWeeksIndex = _InverterGroupReactiveEnergyLogLastWeeksIndex_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 22, 1, 1),
    _InverterGroupReactiveEnergyLogLastWeeksIndex_Type()
)
inverterGroupReactiveEnergyLogLastWeeksIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastWeeksIndex.setStatus("current")
_InverterGroupReactiveEnergyLogLastWeeksValue_Type = Integer32
_InverterGroupReactiveEnergyLogLastWeeksValue_Object = MibTableColumn
inverterGroupReactiveEnergyLogLastWeeksValue = _InverterGroupReactiveEnergyLogLastWeeksValue_Object(
    (1, 3, 6, 1, 4, 1, 12148, 10, 16, 22, 1, 2),
    _InverterGroupReactiveEnergyLogLastWeeksValue_Type()
)
inverterGroupReactiveEnergyLogLastWeeksValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inverterGroupReactiveEnergyLogLastWeeksValue.setStatus("current")

# Managed Objects groups


# Notification objects

alarmPowerSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 1)
)
alarmPowerSystemTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmPowerSystemTrap.setStatus(
        "current"
    )

alarmBatteryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 2)
)
alarmBatteryTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmBatteryTrap.setStatus(
        "current"
    )

alarmLoadGroupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 3)
)
alarmLoadGroupTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmLoadGroupTrap.setStatus(
        "current"
    )

alarmMainsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 4)
)
alarmMainsTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmMainsTrap.setStatus(
        "current"
    )

alarmRectifierTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 5)
)
alarmRectifierTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmRectifierTrap.setStatus(
        "current"
    )

alarmControlSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 6)
)
alarmControlSystemTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmControlSystemTrap.setStatus(
        "current"
    )

alarmDcDcTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 7)
)
alarmDcDcTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmDcDcTrap.setStatus(
        "current"
    )

alarmInputsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 8)
)
alarmInputsTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmInputsTrap.setStatus(
        "current"
    )

alarmOutputsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 9)
)
alarmOutputsTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmOutputsTrap.setStatus(
        "current"
    )

alarmGeneratorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 10)
)
alarmGeneratorTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmGeneratorTrap.setStatus(
        "current"
    )

alarmSolarChargerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 11)
)
alarmSolarChargerTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmSolarChargerTrap.setStatus(
        "current"
    )

alarmWindChargerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 12)
)
alarmWindChargerTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmWindChargerTrap.setStatus(
        "current"
    )

infoHeartBeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 13)
)
infoHeartBeatTrap.setObjects(
    ("SP2-MIB", "alarmSubsysSourceDescr")
)
if mibBuilder.loadTexts:
    infoHeartBeatTrap.setStatus(
        "current"
    )

alarmInverterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 2, 14)
)
alarmInverterTrap.setObjects(
      *(("SP2-MIB", "alarmSubsysSourceDescr"),
        ("SP2-MIB", "alarmSubsysStatusOid"),
        ("SP2-MIB", "alarmSubsysStatusValue"),
        ("SP2-MIB", "alarmSubsysStatusOnOff"),
        ("SP2-MIB", "alarmMeasuredVarOid"),
        ("SP2-MIB", "alarmMeasuredVarValue"),
        ("SP2-MIB", "alarmTrapCounterVarValue"))
)
if mibBuilder.loadTexts:
    alarmInverterTrap.setStatus(
        "current"
    )


# Notifications groups

powerSystemTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12148, 10, 1, 3)
)
powerSystemTrapsGroup.setObjects(
      *(("SP2-MIB", "alarmBatteryTrap"),
        ("SP2-MIB", "alarmControlSystemTrap"),
        ("SP2-MIB", "alarmDcDcTrap"),
        ("SP2-MIB", "alarmGeneratorTrap"),
        ("SP2-MIB", "alarmInputsTrap"),
        ("SP2-MIB", "alarmInverterTrap"),
        ("SP2-MIB", "alarmLoadGroupTrap"),
        ("SP2-MIB", "alarmMainsTrap"),
        ("SP2-MIB", "alarmOutputsTrap"),
        ("SP2-MIB", "alarmPowerSystemTrap"),
        ("SP2-MIB", "alarmRectifierTrap"),
        ("SP2-MIB", "alarmSolarChargerTrap"),
        ("SP2-MIB", "alarmWindChargerTrap"))
)
if mibBuilder.loadTexts:
    powerSystemTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SP2-MIB",
    **{"eNexus": eNexus,
       "eltekTraps": eltekTraps,
       "powerAlarmVars": powerAlarmVars,
       "alarmSubsysSourceDescr": alarmSubsysSourceDescr,
       "alarmSubsysStatusOid": alarmSubsysStatusOid,
       "alarmSubsysStatusValue": alarmSubsysStatusValue,
       "alarmSubsysStatusOnOff": alarmSubsysStatusOnOff,
       "alarmMeasuredVarOid": alarmMeasuredVarOid,
       "alarmMeasuredVarValue": alarmMeasuredVarValue,
       "alarmTrapCounterVarValue": alarmTrapCounterVarValue,
       "powerSystemTraps": powerSystemTraps,
       "alarmPowerSystemTrap": alarmPowerSystemTrap,
       "alarmBatteryTrap": alarmBatteryTrap,
       "alarmLoadGroupTrap": alarmLoadGroupTrap,
       "alarmMainsTrap": alarmMainsTrap,
       "alarmRectifierTrap": alarmRectifierTrap,
       "alarmControlSystemTrap": alarmControlSystemTrap,
       "alarmDcDcTrap": alarmDcDcTrap,
       "alarmInputsTrap": alarmInputsTrap,
       "alarmOutputsTrap": alarmOutputsTrap,
       "alarmGeneratorTrap": alarmGeneratorTrap,
       "alarmSolarChargerTrap": alarmSolarChargerTrap,
       "alarmWindChargerTrap": alarmWindChargerTrap,
       "infoHeartBeatTrap": infoHeartBeatTrap,
       "alarmInverterTrap": alarmInverterTrap,
       "powerSystemTrapsGroup": powerSystemTrapsGroup,
       "powerSystem": powerSystem,
       "powerSystemStatus": powerSystemStatus,
       "powerSystemType": powerSystemType,
       "powerSystemMode": powerSystemMode,
       "powerSystemCompany": powerSystemCompany,
       "powerSystemSite": powerSystemSite,
       "powerSystemModel": powerSystemModel,
       "powerSystemSerialNumber": powerSystemSerialNumber,
       "powerSystemInstallDate": powerSystemInstallDate,
       "powerSystemNominalVoltage": powerSystemNominalVoltage,
       "powerSystemLongitude": powerSystemLongitude,
       "powerSystemLongitudeDecimal": powerSystemLongitudeDecimal,
       "powerSystemLatitude": powerSystemLatitude,
       "powerSystemLatitudeDecimal": powerSystemLatitudeDecimal,
       "powerSystemElevation": powerSystemElevation,
       "powerSystemCurrentDecimalSetting": powerSystemCurrentDecimalSetting,
       "powerSystemTemperatureScale": powerSystemTemperatureScale,
       "powerSystemCapacityScale": powerSystemCapacityScale,
       "mains": mains,
       "mainsStatus": mainsStatus,
       "mainsMainsFailure": mainsMainsFailure,
       "mainsMainsFailureStatus": mainsMainsFailureStatus,
       "mainsMainsFailureDescription": mainsMainsFailureDescription,
       "mainsMainsFailureTrapRepeatCounter": mainsMainsFailureTrapRepeatCounter,
       "mainsMainsFailureAlarmEnable": mainsMainsFailureAlarmEnable,
       "mainsMainsFailureValue": mainsMainsFailureValue,
       "mainsMainsFailureMajorAlarmLevel": mainsMainsFailureMajorAlarmLevel,
       "mainsMainsFailureMinorAlarmLevel": mainsMainsFailureMinorAlarmLevel,
       "mainsNumberOfPhases": mainsNumberOfPhases,
       "mainsVoltageTable": mainsVoltageTable,
       "mainsVoltageEntry": mainsVoltageEntry,
       "mainsVoltageIndex": mainsVoltageIndex,
       "mainsVoltageStatus": mainsVoltageStatus,
       "mainsVoltageDescription": mainsVoltageDescription,
       "mainsVoltageTrapRepeatCounter": mainsVoltageTrapRepeatCounter,
       "mainsVoltageAlarmEnable": mainsVoltageAlarmEnable,
       "mainsVoltageValue": mainsVoltageValue,
       "mainsVoltageMajorHighLevel": mainsVoltageMajorHighLevel,
       "mainsVoltageMinorHighLevel": mainsVoltageMinorHighLevel,
       "mainsVoltageMinorLowLevel": mainsVoltageMinorLowLevel,
       "mainsVoltageMajorLowLevel": mainsVoltageMajorLowLevel,
       "mainsMonitors": mainsMonitors,
       "mainsMonitorsNumberOfUnits": mainsMonitorsNumberOfUnits,
       "mainsMonitorsTable": mainsMonitorsTable,
       "mainsMonitorsEntry": mainsMonitorsEntry,
       "mainsMonitorIndex": mainsMonitorIndex,
       "mainsMonitorNumberOfVoltages": mainsMonitorNumberOfVoltages,
       "mainsMonitorNumberOfCurrents": mainsMonitorNumberOfCurrents,
       "mainsMonitorNumberOfFrequencies": mainsMonitorNumberOfFrequencies,
       "mainsMonitorVoltageTable": mainsMonitorVoltageTable,
       "mainsMonitorVoltageEntry": mainsMonitorVoltageEntry,
       "mainsMonitorPhaseIndex": mainsMonitorPhaseIndex,
       "mainsMonitorVoltageStatus": mainsMonitorVoltageStatus,
       "mainsMonitorVoltageDescription": mainsMonitorVoltageDescription,
       "mainsMonitorVoltageTrapRepeatCounter": mainsMonitorVoltageTrapRepeatCounter,
       "mainsMonitorVoltageAlarmEnable": mainsMonitorVoltageAlarmEnable,
       "mainsMonitorVoltageValue": mainsMonitorVoltageValue,
       "mainsMonitorVoltageMajorHighLevel": mainsMonitorVoltageMajorHighLevel,
       "mainsMonitorVoltageMinorHighLevel": mainsMonitorVoltageMinorHighLevel,
       "mainsMonitorVoltageMinorLowLevel": mainsMonitorVoltageMinorLowLevel,
       "mainsMonitorVoltageMajorLowLevel": mainsMonitorVoltageMajorLowLevel,
       "mainsMonitorCurrentTable": mainsMonitorCurrentTable,
       "mainsMonitorCurrentEntry": mainsMonitorCurrentEntry,
       "mainsMonitorCurrentStatus": mainsMonitorCurrentStatus,
       "mainsMonitorCurrentDescription": mainsMonitorCurrentDescription,
       "mainsMonitorCurrentTrapRepeatCounter": mainsMonitorCurrentTrapRepeatCounter,
       "mainsMonitorCurrentAlarmEnable": mainsMonitorCurrentAlarmEnable,
       "mainsMonitorCurrentValue": mainsMonitorCurrentValue,
       "mainsMonitorCurrentMajorHighLevel": mainsMonitorCurrentMajorHighLevel,
       "mainsMonitorCurrentMinorHighLevel": mainsMonitorCurrentMinorHighLevel,
       "mainsMonitorFrequencyTable": mainsMonitorFrequencyTable,
       "mainsMonitorFrequencyEntry": mainsMonitorFrequencyEntry,
       "mainsMonitorFrequencyStatus": mainsMonitorFrequencyStatus,
       "mainsMonitorFrequencyDescription": mainsMonitorFrequencyDescription,
       "mainsMonitorFrequencyTrapRepeatCounter": mainsMonitorFrequencyTrapRepeatCounter,
       "mainsMonitorFrequencyAlarmEnable": mainsMonitorFrequencyAlarmEnable,
       "mainsMonitorFrequencyValue": mainsMonitorFrequencyValue,
       "mainsMonitorFrequencyMajorHighLevel": mainsMonitorFrequencyMajorHighLevel,
       "mainsMonitorFrequencyMinorHighLevel": mainsMonitorFrequencyMinorHighLevel,
       "mainsMonitorFrequencyMinorLowLevel": mainsMonitorFrequencyMinorLowLevel,
       "mainsMonitorFrequencyMajorLowLevel": mainsMonitorFrequencyMajorLowLevel,
       "mainsMonitorEnergyLogAccumulatedTable": mainsMonitorEnergyLogAccumulatedTable,
       "mainsMonitorEnergyLogAccumulatedEntry": mainsMonitorEnergyLogAccumulatedEntry,
       "mainsMonitorEnergyLogAccumulated": mainsMonitorEnergyLogAccumulated,
       "mainsMonitorEnergyLogLastHoursNumberOfEntries": mainsMonitorEnergyLogLastHoursNumberOfEntries,
       "mainsMonitorEnergyLogLastHoursTable": mainsMonitorEnergyLogLastHoursTable,
       "mainsMonitorEnergyLogLastHoursEntry": mainsMonitorEnergyLogLastHoursEntry,
       "mainsMonitorEnergyLogLastHoursIndex": mainsMonitorEnergyLogLastHoursIndex,
       "mainsMonitorEnergyLogLastHoursValue": mainsMonitorEnergyLogLastHoursValue,
       "mainsMonitorEnergyLogLastDaysNumberOfEntries": mainsMonitorEnergyLogLastDaysNumberOfEntries,
       "mainsMonitorEnergyLogLastDaysTable": mainsMonitorEnergyLogLastDaysTable,
       "mainsMonitorEnergyLogLastDaysEntry": mainsMonitorEnergyLogLastDaysEntry,
       "mainsMonitorEnergyLogLastDaysIndex": mainsMonitorEnergyLogLastDaysIndex,
       "mainsMonitorEnergyLogLastDaysValue": mainsMonitorEnergyLogLastDaysValue,
       "mainsMonitorEnergyLogLastWeeksNumberOfEntries": mainsMonitorEnergyLogLastWeeksNumberOfEntries,
       "mainsMonitorEnergyLogLastWeeksTable": mainsMonitorEnergyLogLastWeeksTable,
       "mainsMonitorEnergyLogLastWeeksEntry": mainsMonitorEnergyLogLastWeeksEntry,
       "mainsMonitorEnergyLogLastWeeksIndex": mainsMonitorEnergyLogLastWeeksIndex,
       "mainsMonitorEnergyLogLastWeeksValue": mainsMonitorEnergyLogLastWeeksValue,
       "mainsOutageLog": mainsOutageLog,
       "mainsOutageTotal": mainsOutageTotal,
       "mainsOutageLogDaysNumberOfEntries": mainsOutageLogDaysNumberOfEntries,
       "mainsOutageLogDaysTable": mainsOutageLogDaysTable,
       "mainsOutageLogDaysEntry": mainsOutageLogDaysEntry,
       "mainsOutageLogDaysIndex": mainsOutageLogDaysIndex,
       "mainsOutageLogDaysValue": mainsOutageLogDaysValue,
       "mainsOutageLogWeeksNumberOfEntries": mainsOutageLogWeeksNumberOfEntries,
       "mainsOutageLogWeeksTable": mainsOutageLogWeeksTable,
       "mainsOutageLogWeeksEntry": mainsOutageLogWeeksEntry,
       "mainsOutageLogWeeksIndex": mainsOutageLogWeeksIndex,
       "mainsOutageLogWeeksValue": mainsOutageLogWeeksValue,
       "mainsOutageLogMonthsNumberOfEntries": mainsOutageLogMonthsNumberOfEntries,
       "mainsOutageLogMonthsTable": mainsOutageLogMonthsTable,
       "mainsOutageLogMonthsEntry": mainsOutageLogMonthsEntry,
       "mainsOutageLogMonthsIndex": mainsOutageLogMonthsIndex,
       "mainsOutageLogMonthsValue": mainsOutageLogMonthsValue,
       "mainsNumberOfGroups": mainsNumberOfGroups,
       "mainsGroupsTable": mainsGroupsTable,
       "mainsGroupsEntry": mainsGroupsEntry,
       "mainsGroupIndex": mainsGroupIndex,
       "mainsGroupStatus": mainsGroupStatus,
       "mainsGroupNumberOfPhases": mainsGroupNumberOfPhases,
       "mainsGroupMainsFailureTable": mainsGroupMainsFailureTable,
       "mainsGroupMainsFailureEntry": mainsGroupMainsFailureEntry,
       "mainsGroupMainsFailureStatus": mainsGroupMainsFailureStatus,
       "mainsGroupMainsFailureDescription": mainsGroupMainsFailureDescription,
       "mainsGroupMainsFailureTrapRepeatCounter": mainsGroupMainsFailureTrapRepeatCounter,
       "mainsGroupMainsFailureAlarmEnable": mainsGroupMainsFailureAlarmEnable,
       "mainsGroupMainsFailureValue": mainsGroupMainsFailureValue,
       "mainsGroupMainsFailureMajorAlarmLevel": mainsGroupMainsFailureMajorAlarmLevel,
       "mainsGroupMainsFailureMinorAlarmLevel": mainsGroupMainsFailureMinorAlarmLevel,
       "mainsGroupVoltageTable": mainsGroupVoltageTable,
       "mainsGroupVoltageEntry": mainsGroupVoltageEntry,
       "mainsGroupVoltageIndex": mainsGroupVoltageIndex,
       "mainsGroupVoltageStatus": mainsGroupVoltageStatus,
       "mainsGroupVoltageDescription": mainsGroupVoltageDescription,
       "mainsGroupVoltageTrapRepeatCounter": mainsGroupVoltageTrapRepeatCounter,
       "mainsGroupVoltageAlarmEnable": mainsGroupVoltageAlarmEnable,
       "mainsGroupVoltageValue": mainsGroupVoltageValue,
       "mainsGroupVoltageMajorHighLevel": mainsGroupVoltageMajorHighLevel,
       "mainsGroupVoltageMinorHighLevel": mainsGroupVoltageMinorHighLevel,
       "mainsGroupVoltageMinorLowLevel": mainsGroupVoltageMinorLowLevel,
       "mainsGroupVoltageMajorLowLevel": mainsGroupVoltageMajorLowLevel,
       "mainsGroupOutageLogTable": mainsGroupOutageLogTable,
       "mainsGroupOutageLogEntry": mainsGroupOutageLogEntry,
       "mainsGroupOutageTotal": mainsGroupOutageTotal,
       "mainsGroupOutageLogDaysNumberOfEntries": mainsGroupOutageLogDaysNumberOfEntries,
       "mainsGroupOutageLogWeeksNumberOfEntries": mainsGroupOutageLogWeeksNumberOfEntries,
       "mainsGroupOutageLogMonthsNumberOfEntries": mainsGroupOutageLogMonthsNumberOfEntries,
       "mainsGroupOutageLogDaysTable": mainsGroupOutageLogDaysTable,
       "mainsGroupOutageLogDaysEntry": mainsGroupOutageLogDaysEntry,
       "mainsGroupOutageLogDaysIndex": mainsGroupOutageLogDaysIndex,
       "mainsGroupOutageLogDaysValue": mainsGroupOutageLogDaysValue,
       "mainsGroupOutageLogWeeksTable": mainsGroupOutageLogWeeksTable,
       "mainsGroupOutageLogWeeksEntry": mainsGroupOutageLogWeeksEntry,
       "mainsGroupOutageLogWeeksIndex": mainsGroupOutageLogWeeksIndex,
       "mainsGroupOutageLogWeeksValue": mainsGroupOutageLogWeeksValue,
       "mainsGroupOutageLogMonthsTable": mainsGroupOutageLogMonthsTable,
       "mainsGroupOutageLogMonthsEntry": mainsGroupOutageLogMonthsEntry,
       "mainsGroupOutageLogMonthsIndex": mainsGroupOutageLogMonthsIndex,
       "mainsGroupOutageLogMonthsValue": mainsGroupOutageLogMonthsValue,
       "generator": generator,
       "generatorStatus": generatorStatus,
       "generatorFailStatus": generatorFailStatus,
       "generatorActivation": generatorActivation,
       "generatorDischargeValue": generatorDischargeValue,
       "generatorMainsDelay": generatorMainsDelay,
       "generatorChargeTime": generatorChargeTime,
       "generatorCapacityControlledStartStopEnable": generatorCapacityControlledStartStopEnable,
       "generatorCapacityStartOnDischargeLimit": generatorCapacityStartOnDischargeLimit,
       "generatorCapacityStopOnChargeLimit": generatorCapacityStopOnChargeLimit,
       "generatorCurrentLimitControlledStopEnable": generatorCurrentLimitControlledStopEnable,
       "generatorCurrentLimitControlledStopValue": generatorCurrentLimitControlledStopValue,
       "generatorVoltageControlledStartEnable": generatorVoltageControlledStartEnable,
       "generatorVoltageControlStartVoltage": generatorVoltageControlStartVoltage,
       "generatorVoltageControlStopAfter": generatorVoltageControlStopAfter,
       "generatorDailyRunEnable": generatorDailyRunEnable,
       "generatorDailyRunSetupTable": generatorDailyRunSetupTable,
       "generatorDailyRunSetupEntry": generatorDailyRunSetupEntry,
       "generatorDailyRunDayIndex": generatorDailyRunDayIndex,
       "generatorDailyRunStartHour": generatorDailyRunStartHour,
       "generatorDailyRunStopHour": generatorDailyRunStopHour,
       "generatorMonthlyRunEnable": generatorMonthlyRunEnable,
       "generatorMonthlyRunStartTime": generatorMonthlyRunStartTime,
       "generatorMonthlyRunStartDayinMonth1": generatorMonthlyRunStartDayinMonth1,
       "generatorMonthlyRunStartDayinMonth2": generatorMonthlyRunStartDayinMonth2,
       "generatorTankNumberOfTanks": generatorTankNumberOfTanks,
       "generatorTankTable": generatorTankTable,
       "generatorTankEntry": generatorTankEntry,
       "generatorTankIndex": generatorTankIndex,
       "generatorTankStatus": generatorTankStatus,
       "generatorTankDescription": generatorTankDescription,
       "generatorTankTrapRepeatCounter": generatorTankTrapRepeatCounter,
       "generatorTankEnable": generatorTankEnable,
       "generatorTankValue": generatorTankValue,
       "generatorTankMajorHighLevel": generatorTankMajorHighLevel,
       "generatorTankMinorHighLevel": generatorTankMinorHighLevel,
       "generatorTankMinorLowLevel": generatorTankMinorLowLevel,
       "generatorTankMajorLowLevel": generatorTankMajorLowLevel,
       "generatorEnergyLog": generatorEnergyLog,
       "generatorEnergyLogAccumulated": generatorEnergyLogAccumulated,
       "generatorEnergyLogLastHoursNumberOfEntries": generatorEnergyLogLastHoursNumberOfEntries,
       "generatorEnergyLogLastHoursTable": generatorEnergyLogLastHoursTable,
       "generatorEnergyLogLastHoursEntry": generatorEnergyLogLastHoursEntry,
       "generatorEnergyLogLastHoursIndex": generatorEnergyLogLastHoursIndex,
       "generatorEnergyLogLastHoursValue": generatorEnergyLogLastHoursValue,
       "generatorEnergyLogLastDaysNumberOfEntries": generatorEnergyLogLastDaysNumberOfEntries,
       "generatorEnergyLogLastDaysTable": generatorEnergyLogLastDaysTable,
       "generatorEnergyLogLastDaysEntry": generatorEnergyLogLastDaysEntry,
       "generatorEnergyLogLastDaysIndex": generatorEnergyLogLastDaysIndex,
       "generatorEnergyLogLastDaysValue": generatorEnergyLogLastDaysValue,
       "generatorEnergyLogLastWeeksNumberOfEntries": generatorEnergyLogLastWeeksNumberOfEntries,
       "generatorEnergyLogLastWeeksTable": generatorEnergyLogLastWeeksTable,
       "generatorEnergyLogLastWeeksEntry": generatorEnergyLogLastWeeksEntry,
       "generatorEnergyLogLastWeeksIndex": generatorEnergyLogLastWeeksIndex,
       "generatorEnergyLogLastWeeksValue": generatorEnergyLogLastWeeksValue,
       "generatorRunHoursLog": generatorRunHoursLog,
       "generatorRunHoursTotalHours": generatorRunHoursTotalHours,
       "generatorRunHoursLogLastDaysNumberOfEntries": generatorRunHoursLogLastDaysNumberOfEntries,
       "generatorRunHoursLogLastDaysTable": generatorRunHoursLogLastDaysTable,
       "generatorRunHoursLogLastDaysEntry": generatorRunHoursLogLastDaysEntry,
       "generatorRunHoursLogLastDaysIndex": generatorRunHoursLogLastDaysIndex,
       "generatorRunHoursLogLastDaysValue": generatorRunHoursLogLastDaysValue,
       "generatorRunHoursLogLastWeeksNumberOfEntries": generatorRunHoursLogLastWeeksNumberOfEntries,
       "generatorRunHoursLogLastWeeksTable": generatorRunHoursLogLastWeeksTable,
       "generatorRunHoursLogLastWeeksEntry": generatorRunHoursLogLastWeeksEntry,
       "generatorRunHoursLogLastWeeksIndex": generatorRunHoursLogLastWeeksIndex,
       "generatorRunHoursLogLastWeeksValue": generatorRunHoursLogLastWeeksValue,
       "generatorRunHoursLogLastMonthsNumberOfEntries": generatorRunHoursLogLastMonthsNumberOfEntries,
       "generatorRunHoursLogLastMonthsTable": generatorRunHoursLogLastMonthsTable,
       "generatorRunHoursLogLastMonthsEntry": generatorRunHoursLogLastMonthsEntry,
       "generatorRunHoursLogLastMonthsIndex": generatorRunHoursLogLastMonthsIndex,
       "generatorRunHoursLogLastMonthsValue": generatorRunHoursLogLastMonthsValue,
       "generatorFuelConsumptionLog": generatorFuelConsumptionLog,
       "generatorFuelConsumptionTotalUsedTable": generatorFuelConsumptionTotalUsedTable,
       "generatorFuelConsumptionTotalUsedEntry": generatorFuelConsumptionTotalUsedEntry,
       "generatorFuelConsumptionTotalUsed": generatorFuelConsumptionTotalUsed,
       "generatorFuelConsumptionLogLastDaysNoOfEntries": generatorFuelConsumptionLogLastDaysNoOfEntries,
       "generatorFuelConsumptionLogLastDaysTable": generatorFuelConsumptionLogLastDaysTable,
       "generatorFuelConsumptionLogLastDaysEntry": generatorFuelConsumptionLogLastDaysEntry,
       "generatorFuelConsumptionLogLastDaysIndex": generatorFuelConsumptionLogLastDaysIndex,
       "generatorFuelConsumptionLogLastDaysValue": generatorFuelConsumptionLogLastDaysValue,
       "generatorFuelConsumptionLogLastWeeksNoOfEntries": generatorFuelConsumptionLogLastWeeksNoOfEntries,
       "generatorFuelConsumptionLogLastWeeksTable": generatorFuelConsumptionLogLastWeeksTable,
       "generatorFuelConsumptionLogLastWeeksEntry": generatorFuelConsumptionLogLastWeeksEntry,
       "generatorFuelConsumptionLogLastWeeksIndex": generatorFuelConsumptionLogLastWeeksIndex,
       "generatorFuelConsumptionLogLastWeeksValue": generatorFuelConsumptionLogLastWeeksValue,
       "generatorFuelConsumptionLogLastMonthsNoOfEntries": generatorFuelConsumptionLogLastMonthsNoOfEntries,
       "generatorFuelConsumptionLogLastMonthsTable": generatorFuelConsumptionLogLastMonthsTable,
       "generatorFuelConsumptionLogLastMonthsEntry": generatorFuelConsumptionLogLastMonthsEntry,
       "generatorFuelConsumptionLogLastMonthsIndex": generatorFuelConsumptionLogLastMonthsIndex,
       "generatorFuelConsumptionLogLastMonthsValue": generatorFuelConsumptionLogLastMonthsValue,
       "rectifiers": rectifiers,
       "rectifiersStatus": rectifiersStatus,
       "rectifiersCurrent": rectifiersCurrent,
       "rectifiersCurrentStatus": rectifiersCurrentStatus,
       "rectifiersCurrentDescription": rectifiersCurrentDescription,
       "rectifiersCurrentTrapRepeatCounter": rectifiersCurrentTrapRepeatCounter,
       "rectifiersCurrentAlarmEnable": rectifiersCurrentAlarmEnable,
       "rectifiersCurrentValue": rectifiersCurrentValue,
       "rectifiersCurrentMajorAlarmLevel": rectifiersCurrentMajorAlarmLevel,
       "rectifiersCurrentMinorAlarmLevel": rectifiersCurrentMinorAlarmLevel,
       "rectifiersCapacity": rectifiersCapacity,
       "rectifiersCapacityStatus": rectifiersCapacityStatus,
       "rectifiersCapacityDescription": rectifiersCapacityDescription,
       "rectifiersCapacityTrapRepeatCounter": rectifiersCapacityTrapRepeatCounter,
       "rectifiersCapacityAlarmEnable": rectifiersCapacityAlarmEnable,
       "rectifiersCapacityValue": rectifiersCapacityValue,
       "rectifiersCapacityMajorAlarmLevel": rectifiersCapacityMajorAlarmLevel,
       "rectifiersCapacityMinorAlarmLevel": rectifiersCapacityMinorAlarmLevel,
       "rectifiersError": rectifiersError,
       "rectifiersErrorStatus": rectifiersErrorStatus,
       "rectifiersErrorDescription": rectifiersErrorDescription,
       "rectifiersErrorTrapRepeatCounter": rectifiersErrorTrapRepeatCounter,
       "rectifiersErrorEnable": rectifiersErrorEnable,
       "rectifiersErrorValue": rectifiersErrorValue,
       "rectifiersErrorMajorAlarmLevel": rectifiersErrorMajorAlarmLevel,
       "rectifiersErrorMinorAlarmLevel": rectifiersErrorMinorAlarmLevel,
       "rectifiersNumberOfRectifiers": rectifiersNumberOfRectifiers,
       "rectifierTable": rectifierTable,
       "rectifierEntry": rectifierEntry,
       "rectifierIndex": rectifierIndex,
       "rectifierStatus": rectifierStatus,
       "rectifierOutputCurrentValue": rectifierOutputCurrentValue,
       "rectifierInputVoltageValue": rectifierInputVoltageValue,
       "rectifierType": rectifierType,
       "rectifierHwPartNumber": rectifierHwPartNumber,
       "rectifierHwVersion": rectifierHwVersion,
       "rectifierSwPartNumber": rectifierSwPartNumber,
       "rectifierSwVersion": rectifierSwVersion,
       "rectifiersEnergyLog": rectifiersEnergyLog,
       "rectifiersEnergyLogAccumulated": rectifiersEnergyLogAccumulated,
       "rectifiersEnergyLogLastHoursNumberOfEntries": rectifiersEnergyLogLastHoursNumberOfEntries,
       "rectifiersEnergyLogLastHoursTable": rectifiersEnergyLogLastHoursTable,
       "rectifiersEnergyLogLastHoursEntry": rectifiersEnergyLogLastHoursEntry,
       "rectifiersEnergyLogLastHoursIndex": rectifiersEnergyLogLastHoursIndex,
       "rectifiersEnergyLogLastHoursValue": rectifiersEnergyLogLastHoursValue,
       "rectifiersEnergyLogLastDaysNumberOfEntries": rectifiersEnergyLogLastDaysNumberOfEntries,
       "rectifiersEnergyLogLastDaysTable": rectifiersEnergyLogLastDaysTable,
       "rectifiersEnergyLogLastDaysEntry": rectifiersEnergyLogLastDaysEntry,
       "rectifiersEnergyLogLastDaysIndex": rectifiersEnergyLogLastDaysIndex,
       "rectifiersEnergyLogLastDaysValue": rectifiersEnergyLogLastDaysValue,
       "rectifiersEnergyLogLastWeeksNumberOfEntries": rectifiersEnergyLogLastWeeksNumberOfEntries,
       "rectifiersEnergyLogLastWeeksTable": rectifiersEnergyLogLastWeeksTable,
       "rectifiersEnergyLogLastWeeksEntry": rectifiersEnergyLogLastWeeksEntry,
       "rectifiersEnergyLogLastWeeksIndex": rectifiersEnergyLogLastWeeksIndex,
       "rectifiersEnergyLogLastWeeksValue": rectifiersEnergyLogLastWeeksValue,
       "rectifiersNumberOfGroups": rectifiersNumberOfGroups,
       "rectifierGroupsTable": rectifierGroupsTable,
       "rectifierGroupsEntry": rectifierGroupsEntry,
       "rectifierGroupIndex": rectifierGroupIndex,
       "rectifierGroupStatus": rectifierGroupStatus,
       "rectifierGroupNumberOfRectifiers": rectifierGroupNumberOfRectifiers,
       "rectifierGroupCurrentTable": rectifierGroupCurrentTable,
       "rectifierGroupCurrentEntry": rectifierGroupCurrentEntry,
       "rectifierGroupCurrentStatus": rectifierGroupCurrentStatus,
       "rectifierGroupCurrentDescription": rectifierGroupCurrentDescription,
       "rectifierGroupCurrentTrapRepeatCounter": rectifierGroupCurrentTrapRepeatCounter,
       "rectifierGroupCurrentAlarmEnable": rectifierGroupCurrentAlarmEnable,
       "rectifierGroupCurrentValue": rectifierGroupCurrentValue,
       "rectifierGroupCurrentMajorAlarmLevel": rectifierGroupCurrentMajorAlarmLevel,
       "rectifierGroupCurrentMinorAlarmLevel": rectifierGroupCurrentMinorAlarmLevel,
       "rectifierGroupCapacityTable": rectifierGroupCapacityTable,
       "rectifierGroupCapacityEntry": rectifierGroupCapacityEntry,
       "rectifierGroupCapacityStatus": rectifierGroupCapacityStatus,
       "rectifierGroupCapacityDescription": rectifierGroupCapacityDescription,
       "rectifierGroupCapacityTrapRepeatCounter": rectifierGroupCapacityTrapRepeatCounter,
       "rectifierGroupCapacityAlarmEnable": rectifierGroupCapacityAlarmEnable,
       "rectifierGroupCapacityValue": rectifierGroupCapacityValue,
       "rectifierGroupCapacityMajorAlarmLevel": rectifierGroupCapacityMajorAlarmLevel,
       "rectifierGroupCapacityMinorAlarmLevel": rectifierGroupCapacityMinorAlarmLevel,
       "rectifierGroupErrorTable": rectifierGroupErrorTable,
       "rectifierGroupErrorEntry": rectifierGroupErrorEntry,
       "rectifierGroupErrorStatus": rectifierGroupErrorStatus,
       "rectifierGroupErrorDescription": rectifierGroupErrorDescription,
       "rectifierGroupErrorTrapRepeatCounter": rectifierGroupErrorTrapRepeatCounter,
       "rectifierGroupErrorAlarmEnable": rectifierGroupErrorAlarmEnable,
       "rectifierGroupErrorValue": rectifierGroupErrorValue,
       "rectifierGroupErrorMajorAlarmLevel": rectifierGroupErrorMajorAlarmLevel,
       "rectifierGroupErrorMinorAlarmLevel": rectifierGroupErrorMinorAlarmLevel,
       "rectifierGroupRectifierTable": rectifierGroupRectifierTable,
       "rectifierGroupRectifierEntry": rectifierGroupRectifierEntry,
       "rectifierGroupRectifierIndex": rectifierGroupRectifierIndex,
       "rectifierGroupRectifierStatus": rectifierGroupRectifierStatus,
       "rectifierGroupRectifierOutputCurrentValue": rectifierGroupRectifierOutputCurrentValue,
       "rectifierGroupRectifierInputVoltageValue": rectifierGroupRectifierInputVoltageValue,
       "rectifierGroupRectifierType": rectifierGroupRectifierType,
       "rectifierGroupRectifierHwPartNumber": rectifierGroupRectifierHwPartNumber,
       "rectifierGroupRectifierHwVersion": rectifierGroupRectifierHwVersion,
       "rectifierGroupRectifierSwPartNumber": rectifierGroupRectifierSwPartNumber,
       "rectifierGroupRectifierSwVersion": rectifierGroupRectifierSwVersion,
       "rectifierGroupEnergyLogTable": rectifierGroupEnergyLogTable,
       "rectifierGroupEnergyLogEntry": rectifierGroupEnergyLogEntry,
       "rectifierGroupEnergyLogAccumulated": rectifierGroupEnergyLogAccumulated,
       "rectifierGroupEnergyLogLastHoursNumberOfEntries": rectifierGroupEnergyLogLastHoursNumberOfEntries,
       "rectifierGroupEnergyLogLastDaysNumberOfEntries": rectifierGroupEnergyLogLastDaysNumberOfEntries,
       "rectifierGroupEnergyLogLastWeeksNumberOfEntries": rectifierGroupEnergyLogLastWeeksNumberOfEntries,
       "rectifierGroupEnergyLogLastHoursTable": rectifierGroupEnergyLogLastHoursTable,
       "rectifierGroupEnergyLogLastHoursEntry": rectifierGroupEnergyLogLastHoursEntry,
       "rectifierGroupEnergyLogLastHoursIndex": rectifierGroupEnergyLogLastHoursIndex,
       "rectifierGroupEnergyLogLastHoursValue": rectifierGroupEnergyLogLastHoursValue,
       "rectifierGroupEnergyLogLastDaysTable": rectifierGroupEnergyLogLastDaysTable,
       "rectifierGroupEnergyLogLastDaysEntry": rectifierGroupEnergyLogLastDaysEntry,
       "rectifierGroupEnergyLogLastDaysIndex": rectifierGroupEnergyLogLastDaysIndex,
       "rectifierGroupEnergyLogLastDaysValue": rectifierGroupEnergyLogLastDaysValue,
       "rectifierGroupEnergyLogLastWeeksTable": rectifierGroupEnergyLogLastWeeksTable,
       "rectifierGroupEnergyLogLastWeeksEntry": rectifierGroupEnergyLogLastWeeksEntry,
       "rectifierGroupEnergyLogLastWeeksIndex": rectifierGroupEnergyLogLastWeeksIndex,
       "rectifierGroupEnergyLogLastWeeksValue": rectifierGroupEnergyLogLastWeeksValue,
       "rectifiersTemperature": rectifiersTemperature,
       "rectifiersTemperatureStatus": rectifiersTemperatureStatus,
       "rectifiersTemperatureDescription": rectifiersTemperatureDescription,
       "rectifiersTemperatureTrapRepeatCounter": rectifiersTemperatureTrapRepeatCounter,
       "rectifiersTemperatureAlarmEnable": rectifiersTemperatureAlarmEnable,
       "rectifiersTemperatureValue": rectifiersTemperatureValue,
       "rectifiersTemperatureMajorHighLevel": rectifiersTemperatureMajorHighLevel,
       "rectifiersTemperatureMinorHighLevel": rectifiersTemperatureMinorHighLevel,
       "rectifiersTemperatureMinorLowLevel": rectifiersTemperatureMinorLowLevel,
       "rectifiersTemperatureMajorLowLevel": rectifiersTemperatureMajorLowLevel,
       "rectifierGroupTemperatureTable": rectifierGroupTemperatureTable,
       "rectifierGroupTemperatureEntry": rectifierGroupTemperatureEntry,
       "rectifierGroupTemperatureStatus": rectifierGroupTemperatureStatus,
       "rectifierGroupTemperatureDescription": rectifierGroupTemperatureDescription,
       "rectifierGroupTemperatureTrapRepeatCounter": rectifierGroupTemperatureTrapRepeatCounter,
       "rectifierGroupTemperatureAlarmEnable": rectifierGroupTemperatureAlarmEnable,
       "rectifierGroupTemperatureValue": rectifierGroupTemperatureValue,
       "rectifierGroupTemperatureMajorHighLevel": rectifierGroupTemperatureMajorHighLevel,
       "rectifierGroupTemperatureMinorHighLevel": rectifierGroupTemperatureMinorHighLevel,
       "rectifierGroupTemperatureMinorLowLevel": rectifierGroupTemperatureMinorLowLevel,
       "rectifierGroupTemperatureMajorLowLevel": rectifierGroupTemperatureMajorLowLevel,
       "dcdc": dcdc,
       "dcdcNumberOfGroups": dcdcNumberOfGroups,
       "dcdcGroupsTable": dcdcGroupsTable,
       "dcdcGroupsEntry": dcdcGroupsEntry,
       "dcdcGroupIndex": dcdcGroupIndex,
       "dcdcGroupStatus": dcdcGroupStatus,
       "dcdcGroupNumberOfDcdcConverters": dcdcGroupNumberOfDcdcConverters,
       "dcdcGroupOutputVoltage": dcdcGroupOutputVoltage,
       "dcdcNumberOfCurrents": dcdcNumberOfCurrents,
       "dcdcNumberOfCapacities": dcdcNumberOfCapacities,
       "dcdcNumberOfAlarms": dcdcNumberOfAlarms,
       "dcdcCurrentTable": dcdcCurrentTable,
       "dcdcCurrentEntry": dcdcCurrentEntry,
       "dcdcCurrentStatus": dcdcCurrentStatus,
       "dcdcCurrentDescription": dcdcCurrentDescription,
       "dcdcCurrentTrapRepeatCounter": dcdcCurrentTrapRepeatCounter,
       "dcdcCurrentAlarmEnable": dcdcCurrentAlarmEnable,
       "dcdcCurrentValue": dcdcCurrentValue,
       "dcdcCurrentMajorAlarmLevel": dcdcCurrentMajorAlarmLevel,
       "dcdcCurrentMinorAlarmLevel": dcdcCurrentMinorAlarmLevel,
       "dcdcCapacityTable": dcdcCapacityTable,
       "dcdcCapacityEntry": dcdcCapacityEntry,
       "dcdcCapacityStatus": dcdcCapacityStatus,
       "dcdcCapacityDescription": dcdcCapacityDescription,
       "dcdcCapacityTrapRepeatCounter": dcdcCapacityTrapRepeatCounter,
       "dcdcCapacityAlarmEnable": dcdcCapacityAlarmEnable,
       "dcdcCapacityValue": dcdcCapacityValue,
       "dcdcCapacityMajorAlarmLevel": dcdcCapacityMajorAlarmLevel,
       "dcdcCapacityMinorAlarmLevel": dcdcCapacityMinorAlarmLevel,
       "dcdcTable": dcdcTable,
       "dcdcEntry": dcdcEntry,
       "dcdcIndex": dcdcIndex,
       "dcdcStatus": dcdcStatus,
       "dcdcOutputCurrentValue": dcdcOutputCurrentValue,
       "dcdcInputVoltageValue": dcdcInputVoltageValue,
       "dcdcType": dcdcType,
       "dcdcHwPartNumber": dcdcHwPartNumber,
       "dcdcHwVersion": dcdcHwVersion,
       "dcdcSwPartNumber": dcdcSwPartNumber,
       "dcdcSwVersion": dcdcSwVersion,
       "dcdcErrorTable": dcdcErrorTable,
       "dcdcErrorEntry": dcdcErrorEntry,
       "dcdcErrorStatus": dcdcErrorStatus,
       "dcdcErrorDescription": dcdcErrorDescription,
       "dcdcErrorTrapRepeatCounter": dcdcErrorTrapRepeatCounter,
       "dcdcErrorEnable": dcdcErrorEnable,
       "dcdcErrorValue": dcdcErrorValue,
       "dcdcErrorMajorAlarmLevel": dcdcErrorMajorAlarmLevel,
       "dcdcErrorMinorAlarmLevel": dcdcErrorMinorAlarmLevel,
       "dcdcObsolete": dcdcObsolete,
       "solarChargers": solarChargers,
       "solarChargersStatus": solarChargersStatus,
       "solarChargersCurrent": solarChargersCurrent,
       "solarChargersCurrentStatus": solarChargersCurrentStatus,
       "solarChargersCurrentDescription": solarChargersCurrentDescription,
       "solarChargersCurrentTrapRepeatCounter": solarChargersCurrentTrapRepeatCounter,
       "solarChargersCurrentAlarmEnable": solarChargersCurrentAlarmEnable,
       "solarChargersCurrentValue": solarChargersCurrentValue,
       "solarChargersCurrentMajorAlarmLevel": solarChargersCurrentMajorAlarmLevel,
       "solarChargersCurrentMinorAlarmLevel": solarChargersCurrentMinorAlarmLevel,
       "solarChargersObsolete": solarChargersObsolete,
       "solarChargersError": solarChargersError,
       "solarChargersErrorStatus": solarChargersErrorStatus,
       "solarChargersErrorDescription": solarChargersErrorDescription,
       "solarChargersErrorTrapRepeatCounter": solarChargersErrorTrapRepeatCounter,
       "solarChargersErrorEnable": solarChargersErrorEnable,
       "solarChargersErrorValue": solarChargersErrorValue,
       "solarChargersErrorMajorAlarmLevel": solarChargersErrorMajorAlarmLevel,
       "solarChargersErrorMinorAlarmLevel": solarChargersErrorMinorAlarmLevel,
       "solarChargersNumberOfSolarChargers": solarChargersNumberOfSolarChargers,
       "solarChargerTable": solarChargerTable,
       "solarChargerEntry": solarChargerEntry,
       "solarChargerIndex": solarChargerIndex,
       "solarChargerStatus": solarChargerStatus,
       "solarChargerOutputCurrentValue": solarChargerOutputCurrentValue,
       "solarChargerInputVoltageValue": solarChargerInputVoltageValue,
       "solarChargerType": solarChargerType,
       "solarChargerHwPartNumber": solarChargerHwPartNumber,
       "solarChargerHwVersion": solarChargerHwVersion,
       "solarChargerSwPartNumber": solarChargerSwPartNumber,
       "solarChargerSwVersion": solarChargerSwVersion,
       "solarChargersEnergyLog": solarChargersEnergyLog,
       "solarChargersEnergyLogAccumulated": solarChargersEnergyLogAccumulated,
       "solarChargersEnergyLogLastHoursNumberOfEntries": solarChargersEnergyLogLastHoursNumberOfEntries,
       "solarChargersEnergyLogLastHoursTable": solarChargersEnergyLogLastHoursTable,
       "solarChargersEnergyLogLastHoursEntry": solarChargersEnergyLogLastHoursEntry,
       "solarChargersEnergyLogLastHoursIndex": solarChargersEnergyLogLastHoursIndex,
       "solarChargersEnergyLogLastHoursValue": solarChargersEnergyLogLastHoursValue,
       "solarChargersEnergyLogLastDaysNumberOfEntries": solarChargersEnergyLogLastDaysNumberOfEntries,
       "solarChargersEnergyLogLastDaysTable": solarChargersEnergyLogLastDaysTable,
       "solarChargersEnergyLogLastDaysEntry": solarChargersEnergyLogLastDaysEntry,
       "solarChargersEnergyLogLastDaysIndex": solarChargersEnergyLogLastDaysIndex,
       "solarChargersEnergyLogLastDaysValue": solarChargersEnergyLogLastDaysValue,
       "solarChargersEnergyLogLastWeeksNumberOfEntries": solarChargersEnergyLogLastWeeksNumberOfEntries,
       "solarChargersEnergyLogLastWeeksTable": solarChargersEnergyLogLastWeeksTable,
       "solarChargersEnergyLogLastWeeksEntry": solarChargersEnergyLogLastWeeksEntry,
       "solarChargersEnergyLogLastWeeksIndex": solarChargersEnergyLogLastWeeksIndex,
       "solarChargersEnergyLogLastWeeksValue": solarChargersEnergyLogLastWeeksValue,
       "windChargers": windChargers,
       "windChargersStatus": windChargersStatus,
       "windChargersCurrent": windChargersCurrent,
       "windChargersCurrentStatus": windChargersCurrentStatus,
       "windChargersCurrentDescription": windChargersCurrentDescription,
       "windChargersCurrentTrapRepeatCounter": windChargersCurrentTrapRepeatCounter,
       "windChargersCurrentAlarmEnable": windChargersCurrentAlarmEnable,
       "windChargersCurrentValue": windChargersCurrentValue,
       "windChargersCurrentMajorAlarmLevel": windChargersCurrentMajorAlarmLevel,
       "windChargersCurrentMinorAlarmLevel": windChargersCurrentMinorAlarmLevel,
       "windChargersObsolete": windChargersObsolete,
       "windChargersError": windChargersError,
       "windChargersErrorStatus": windChargersErrorStatus,
       "windChargersErrorDescription": windChargersErrorDescription,
       "windChargersErrorTrapRepeatCounter": windChargersErrorTrapRepeatCounter,
       "windChargersErrorEnable": windChargersErrorEnable,
       "windChargersErrorValue": windChargersErrorValue,
       "windChargersErrorMajorAlarmLevel": windChargersErrorMajorAlarmLevel,
       "windChargersErrorMinorAlarmLevel": windChargersErrorMinorAlarmLevel,
       "windChargersNumberOfWindChargers": windChargersNumberOfWindChargers,
       "windChargerTable": windChargerTable,
       "windChargerEntry": windChargerEntry,
       "windChargerIndex": windChargerIndex,
       "windChargerStatus": windChargerStatus,
       "windChargerOutputCurrentValue": windChargerOutputCurrentValue,
       "windChargerInputVoltageValue": windChargerInputVoltageValue,
       "windChargerType": windChargerType,
       "windChargerHwPartNumber": windChargerHwPartNumber,
       "windChargerHwVersion": windChargerHwVersion,
       "windChargerSwPartNumber": windChargerSwPartNumber,
       "windChargerSwVersion": windChargerSwVersion,
       "windChargersEnergyLog": windChargersEnergyLog,
       "windChargersEnergyLogAccumulated": windChargersEnergyLogAccumulated,
       "windChargersEnergyLogLastHoursNumberOfEntries": windChargersEnergyLogLastHoursNumberOfEntries,
       "windChargersEnergyLogLastHoursTable": windChargersEnergyLogLastHoursTable,
       "windChargersEnergyLogLastHoursEntry": windChargersEnergyLogLastHoursEntry,
       "windChargersEnergyLogLastHoursIndex": windChargersEnergyLogLastHoursIndex,
       "windChargersEnergyLogLastHoursValue": windChargersEnergyLogLastHoursValue,
       "windChargersEnergyLogLastDaysNumberOfEntries": windChargersEnergyLogLastDaysNumberOfEntries,
       "windChargersEnergyLogLastDaysTable": windChargersEnergyLogLastDaysTable,
       "windChargersEnergyLogLastDaysEntry": windChargersEnergyLogLastDaysEntry,
       "windChargersEnergyLogLastDaysIndex": windChargersEnergyLogLastDaysIndex,
       "windChargersEnergyLogLastDaysValue": windChargersEnergyLogLastDaysValue,
       "windChargersEnergyLogLastWeeksNumberOfEntries": windChargersEnergyLogLastWeeksNumberOfEntries,
       "windChargersEnergyLogLastWeeksTable": windChargersEnergyLogLastWeeksTable,
       "windChargersEnergyLogLastWeeksEntry": windChargersEnergyLogLastWeeksEntry,
       "windChargersEnergyLogLastWeeksIndex": windChargersEnergyLogLastWeeksIndex,
       "windChargersEnergyLogLastWeeksValue": windChargersEnergyLogLastWeeksValue,
       "load": load,
       "loadStatus": loadStatus,
       "loadCurrent": loadCurrent,
       "loadCurrentStatus": loadCurrentStatus,
       "loadCurrentDescription": loadCurrentDescription,
       "loadCurrentTrapRepeatCounter": loadCurrentTrapRepeatCounter,
       "loadCurrentAlarmEnable": loadCurrentAlarmEnable,
       "loadCurrentValue": loadCurrentValue,
       "loadCurrentMajorHighLevel": loadCurrentMajorHighLevel,
       "loadCurrentMinorHighLevel": loadCurrentMinorHighLevel,
       "loadFusesStatus": loadFusesStatus,
       "loadNumberOfGroups": loadNumberOfGroups,
       "loadGroupTable": loadGroupTable,
       "loadGroupEntry": loadGroupEntry,
       "loadGroupIndex": loadGroupIndex,
       "loadGroupStatus": loadGroupStatus,
       "loadNumberOfLVLDs": loadNumberOfLVLDs,
       "loadNumberOfVoltages": loadNumberOfVoltages,
       "loadLVLDTable": loadLVLDTable,
       "loadLVLDEntry": loadLVLDEntry,
       "loadLVLDIndex": loadLVLDIndex,
       "loadLVLDStatus": loadLVLDStatus,
       "loadLVLDDescription": loadLVLDDescription,
       "loadLVLDTrapRepeatCounter": loadLVLDTrapRepeatCounter,
       "loadLVLDEnable": loadLVLDEnable,
       "loadLVLDValue": loadLVLDValue,
       "loadLVLDConnectVoltage": loadLVLDConnectVoltage,
       "loadLVLDDisconnectVoltage": loadLVLDDisconnectVoltage,
       "loadFuseTable": loadFuseTable,
       "loadFuseEntry": loadFuseEntry,
       "loadFuseStatus": loadFuseStatus,
       "loadFuseDescription": loadFuseDescription,
       "loadFuseTrapRepeatCounter": loadFuseTrapRepeatCounter,
       "loadFuseAlarmEnable": loadFuseAlarmEnable,
       "loadFuseValue": loadFuseValue,
       "loadEnergyLog": loadEnergyLog,
       "loadEnergyLogAccumulated": loadEnergyLogAccumulated,
       "loadEnergyLogLastHoursNumberOfEntries": loadEnergyLogLastHoursNumberOfEntries,
       "loadEnergyLogLastHoursTable": loadEnergyLogLastHoursTable,
       "loadEnergyLogLastHoursEntry": loadEnergyLogLastHoursEntry,
       "loadEnergyLogLastHoursIndex": loadEnergyLogLastHoursIndex,
       "loadEnergyLogLastHoursValue": loadEnergyLogLastHoursValue,
       "loadEnergyLogLastDaysNumberOfEntries": loadEnergyLogLastDaysNumberOfEntries,
       "loadEnergyLogLastDaysTable": loadEnergyLogLastDaysTable,
       "loadEnergyLogLastDaysEntry": loadEnergyLogLastDaysEntry,
       "loadEnergyLogLastDaysIndex": loadEnergyLogLastDaysIndex,
       "loadEnergyLogLastDaysValue": loadEnergyLogLastDaysValue,
       "loadEnergyLogLastWeeksNumberOfEntries": loadEnergyLogLastWeeksNumberOfEntries,
       "loadEnergyLogLastWeeksTable": loadEnergyLogLastWeeksTable,
       "loadEnergyLogLastWeeksEntry": loadEnergyLogLastWeeksEntry,
       "loadEnergyLogLastWeeksIndex": loadEnergyLogLastWeeksIndex,
       "loadEnergyLogLastWeeksValue": loadEnergyLogLastWeeksValue,
       "loadVoltageTable": loadVoltageTable,
       "loadVoltageEntry": loadVoltageEntry,
       "loadVoltageIndex": loadVoltageIndex,
       "loadVoltageStatus": loadVoltageStatus,
       "loadVoltageDescription": loadVoltageDescription,
       "loadVoltageTrapRepeatCounter": loadVoltageTrapRepeatCounter,
       "loadVoltageEnable": loadVoltageEnable,
       "loadVoltageValue": loadVoltageValue,
       "battery": battery,
       "batteryStatus": batteryStatus,
       "batteryDescription": batteryDescription,
       "batteryReferenceVoltage": batteryReferenceVoltage,
       "batteryFusesStatus": batteryFusesStatus,
       "batteryVoltage": batteryVoltage,
       "batteryVoltageStatus": batteryVoltageStatus,
       "batteryVoltageDescription": batteryVoltageDescription,
       "batteryVoltageTrapRepeatCounter": batteryVoltageTrapRepeatCounter,
       "batteryVoltageAlarmEnable": batteryVoltageAlarmEnable,
       "batteryVoltageValue": batteryVoltageValue,
       "batteryVoltageMajorHighLevel": batteryVoltageMajorHighLevel,
       "batteryVoltageMinorHighLevel": batteryVoltageMinorHighLevel,
       "batteryVoltageMinorLowLevel": batteryVoltageMinorLowLevel,
       "batteryVoltageMajorLowLevel": batteryVoltageMajorLowLevel,
       "batteryCurrents": batteryCurrents,
       "batteryCurrentsStatus": batteryCurrentsStatus,
       "batteryCurrentsDescription": batteryCurrentsDescription,
       "batteryCurrentsTrapRepeatCounter": batteryCurrentsTrapRepeatCounter,
       "batteryCurrentsAlarmEnable": batteryCurrentsAlarmEnable,
       "batteryCurrentsValue": batteryCurrentsValue,
       "batteryCurrentsMajorHighLevel": batteryCurrentsMajorHighLevel,
       "batteryCurrentsMinorHighLevel": batteryCurrentsMinorHighLevel,
       "batteryCurrentsMinorLowLevel": batteryCurrentsMinorLowLevel,
       "batteryCurrentsMajorLowLevel": batteryCurrentsMajorLowLevel,
       "batteryTemperatures": batteryTemperatures,
       "batteryTemperaturesStatus": batteryTemperaturesStatus,
       "batteryTemperaturesDescription": batteryTemperaturesDescription,
       "batteryTemperaturesTrapRepeatCounter": batteryTemperaturesTrapRepeatCounter,
       "batteryTemperaturesAlarmEnable": batteryTemperaturesAlarmEnable,
       "batteryTemperaturesValue": batteryTemperaturesValue,
       "batteryTemperaturesMajorHighLevel": batteryTemperaturesMajorHighLevel,
       "batteryTemperaturesMinorHighLevel": batteryTemperaturesMinorHighLevel,
       "batteryTemperaturesMinorLowLevel": batteryTemperaturesMinorLowLevel,
       "batteryTemperaturesMajorLowLevel": batteryTemperaturesMajorLowLevel,
       "batteryTimeLeft": batteryTimeLeft,
       "batteryTimeLeftStatus": batteryTimeLeftStatus,
       "batteryTimeLeftDescription": batteryTimeLeftDescription,
       "batteryTimeLeftTrapRepeatCounter": batteryTimeLeftTrapRepeatCounter,
       "batteryTimeLeftAlarmEnable": batteryTimeLeftAlarmEnable,
       "batteryTimeLeftValue": batteryTimeLeftValue,
       "batteryTimeLeftMinorAlarmLevel": batteryTimeLeftMinorAlarmLevel,
       "batteryTimeLeftMajorAlarmLevel": batteryTimeLeftMajorAlarmLevel,
       "batteryRemainingCapacity": batteryRemainingCapacity,
       "batteryRemainingCapacityStatus": batteryRemainingCapacityStatus,
       "batteryRemainingCapacityDescription": batteryRemainingCapacityDescription,
       "batteryRemainingCapacityTrapRepeatCounter": batteryRemainingCapacityTrapRepeatCounter,
       "batteryRemainingCapacityAlarmEnable": batteryRemainingCapacityAlarmEnable,
       "batteryRemainingCapacityValue": batteryRemainingCapacityValue,
       "batteryRemainingCapacityMinorLowLevel": batteryRemainingCapacityMinorLowLevel,
       "batteryRemainingCapacityMajorLowLevel": batteryRemainingCapacityMajorLowLevel,
       "batteryUsedCapacity": batteryUsedCapacity,
       "batteryUsedCapacityStatus": batteryUsedCapacityStatus,
       "batteryUsedCapacityDescription": batteryUsedCapacityDescription,
       "batteryUsedCapacityTrapRepeatCounter": batteryUsedCapacityTrapRepeatCounter,
       "batteryUsedCapacityAlarmEnable": batteryUsedCapacityAlarmEnable,
       "batteryUsedCapacityValue": batteryUsedCapacityValue,
       "batteryUsedCapacityMajorAlarmLevel": batteryUsedCapacityMajorAlarmLevel,
       "batteryUsedCapacityMinorAlarmLevel": batteryUsedCapacityMinorAlarmLevel,
       "batteryTotalCapacity": batteryTotalCapacity,
       "batteryTotalCapacityStatus": batteryTotalCapacityStatus,
       "batteryTotalCapacityDescription": batteryTotalCapacityDescription,
       "batteryTotalCapacityTrapRepeatCounter": batteryTotalCapacityTrapRepeatCounter,
       "batteryTotalCapacityAlarmEnable": batteryTotalCapacityAlarmEnable,
       "batteryTotalCapacityValue": batteryTotalCapacityValue,
       "batteryTotalCapacityMinorLowLevel": batteryTotalCapacityMinorLowLevel,
       "batteryTotalCapacityMajorLowLevel": batteryTotalCapacityMajorLowLevel,
       "batteryQuality": batteryQuality,
       "batteryQualityStatus": batteryQualityStatus,
       "batteryQualityDescription": batteryQualityDescription,
       "batteryQualityTrapRepeatCounter": batteryQualityTrapRepeatCounter,
       "batteryQualityAlarmEnable": batteryQualityAlarmEnable,
       "batteryQualityValue": batteryQualityValue,
       "batteryQualityMinorAlarmLevel": batteryQualityMinorAlarmLevel,
       "batteryQualityMajorAlarmLevel": batteryQualityMajorAlarmLevel,
       "batteryLVBD": batteryLVBD,
       "batteryLVBDStatus": batteryLVBDStatus,
       "batteryLVBDDescription": batteryLVBDDescription,
       "batteryLVBDTrapRepeatCounter": batteryLVBDTrapRepeatCounter,
       "batteryLVBDEnable": batteryLVBDEnable,
       "batteryLVBDValue": batteryLVBDValue,
       "batteryLVBDConnectVoltage": batteryLVBDConnectVoltage,
       "batteryLVBDDisconnectVoltage": batteryLVBDDisconnectVoltage,
       "batteryChargeCurrentLimit": batteryChargeCurrentLimit,
       "batteryChargeCurrentLimitEnable": batteryChargeCurrentLimitEnable,
       "batteryChargeCurrentLimitValue": batteryChargeCurrentLimitValue,
       "batteryBoost": batteryBoost,
       "batteryBoostVoltage": batteryBoostVoltage,
       "batteryBoostCommand": batteryBoostCommand,
       "batteryBoostCurrentThreshold": batteryBoostCurrentThreshold,
       "batteryBoostManualMaxDuration": batteryBoostManualMaxDuration,
       "batteryTest": batteryTest,
       "batteryTestVoltage": batteryTestVoltage,
       "batteryTestCommand": batteryTestCommand,
       "batteryTestNumberOfResults": batteryTestNumberOfResults,
       "batteryTestResultTable": batteryTestResultTable,
       "batteryTestResultEntry": batteryTestResultEntry,
       "batteryTestResultIndex": batteryTestResultIndex,
       "batteryTestResultStartDateTime": batteryTestResultStartDateTime,
       "batteryTestResultDuration": batteryTestResultDuration,
       "batteryTestResultDischarged": batteryTestResultDischarged,
       "batteryTestResultQuality": batteryTestResultQuality,
       "batteryTempComp": batteryTempComp,
       "batteryTempCompEnable": batteryTempCompEnable,
       "batteryBank": batteryBank,
       "batteryBankNumberOfBanks": batteryBankNumberOfBanks,
       "batteryBankTable": batteryBankTable,
       "batteryBankEntry": batteryBankEntry,
       "batteryBankIndex": batteryBankIndex,
       "batteryBankStatus": batteryBankStatus,
       "batteryBankNumberOfTemperatures": batteryBankNumberOfTemperatures,
       "batteryBankNumberOfCurrents": batteryBankNumberOfCurrents,
       "batteryBankNumberOfFuses": batteryBankNumberOfFuses,
       "batteryBankNumberOfSymmetries": batteryBankNumberOfSymmetries,
       "batteryBankTemperatureTable": batteryBankTemperatureTable,
       "batteryBankTemperatureEntry": batteryBankTemperatureEntry,
       "batteryTemperatureIndex": batteryTemperatureIndex,
       "batteryTemperatureStatus": batteryTemperatureStatus,
       "batteryTemperatureDescription": batteryTemperatureDescription,
       "batteryTemperatureTrapRepeatCounter": batteryTemperatureTrapRepeatCounter,
       "batteryTemperatureAlarmEnable": batteryTemperatureAlarmEnable,
       "batteryTemperatureValue": batteryTemperatureValue,
       "batteryTemperatureMajorHighLevel": batteryTemperatureMajorHighLevel,
       "batteryTemperatureMinorHighLevel": batteryTemperatureMinorHighLevel,
       "batteryTemperatureMinorLowLevel": batteryTemperatureMinorLowLevel,
       "batteryTemperatureMajorLowLevel": batteryTemperatureMajorLowLevel,
       "batteryBankCurrentTable": batteryBankCurrentTable,
       "batteryBankCurrentEntry": batteryBankCurrentEntry,
       "batteryCurrentIndex": batteryCurrentIndex,
       "batteryCurrentStatus": batteryCurrentStatus,
       "batteryCurrentDescription": batteryCurrentDescription,
       "batteryCurrentTrapRepeatCounter": batteryCurrentTrapRepeatCounter,
       "batteryCurrentAlarmEnable": batteryCurrentAlarmEnable,
       "batteryCurrentValue": batteryCurrentValue,
       "batteryCurrentMajorHighLevel": batteryCurrentMajorHighLevel,
       "batteryCurrentMinorHighLevel": batteryCurrentMinorHighLevel,
       "batteryCurrentMinorLowLevel": batteryCurrentMinorLowLevel,
       "batteryCurrentMajorLowLevel": batteryCurrentMajorLowLevel,
       "batteryBankFuseTable": batteryBankFuseTable,
       "batteryBankFuseEntry": batteryBankFuseEntry,
       "batteryFuseIndex": batteryFuseIndex,
       "batteryFuseStatus": batteryFuseStatus,
       "batteryFuseDescription": batteryFuseDescription,
       "batteryFuseTrapRepeatCounter": batteryFuseTrapRepeatCounter,
       "batteryFuseAlarmEnable": batteryFuseAlarmEnable,
       "batteryFuseValue": batteryFuseValue,
       "batteryBankSymmetryTable": batteryBankSymmetryTable,
       "batteryBankSymmetryEntry": batteryBankSymmetryEntry,
       "batteryBankSymmetryIndex": batteryBankSymmetryIndex,
       "batteryBankSymmetryStatus": batteryBankSymmetryStatus,
       "batteryBankSymmetryDescription": batteryBankSymmetryDescription,
       "batteryBankSymmetryTrapRepeatCounter": batteryBankSymmetryTrapRepeatCounter,
       "batteryBankSymmetryAlarmEnable": batteryBankSymmetryAlarmEnable,
       "batteryBankSymmetryMeasureValue": batteryBankSymmetryMeasureValue,
       "batteryBankSymmetryDeltaValue": batteryBankSymmetryDeltaValue,
       "batteryBankSymmetryMajorAlarmLevel": batteryBankSymmetryMajorAlarmLevel,
       "batteryBankSymmetryMinorAlarmLevel": batteryBankSymmetryMinorAlarmLevel,
       "batteryMonitors": batteryMonitors,
       "batteryMonitorsNumberOfUnits": batteryMonitorsNumberOfUnits,
       "batteryMonitorsTable": batteryMonitorsTable,
       "batteryMonitorsEntry": batteryMonitorsEntry,
       "batteryMonitorIndex": batteryMonitorIndex,
       "batteryMonitorNumberOfTemperatures": batteryMonitorNumberOfTemperatures,
       "batteryMonitorNumberOfCurrents": batteryMonitorNumberOfCurrents,
       "batteryMonitorNumberOfFuses": batteryMonitorNumberOfFuses,
       "batteryMonitorNumberOfSymmetries": batteryMonitorNumberOfSymmetries,
       "batteryMonitorTemperatureTable": batteryMonitorTemperatureTable,
       "batteryMonitorTemperatureEntry": batteryMonitorTemperatureEntry,
       "batteryMonitorTemperatureIndex": batteryMonitorTemperatureIndex,
       "batteryMonitorTemperatureStatus": batteryMonitorTemperatureStatus,
       "batteryMonitorTemperatureDescription": batteryMonitorTemperatureDescription,
       "batteryMonitorTemperatureTrapRepeatCounter": batteryMonitorTemperatureTrapRepeatCounter,
       "batteryMonitorTemperatureAlarmEnable": batteryMonitorTemperatureAlarmEnable,
       "batteryMonitorTemperatureValue": batteryMonitorTemperatureValue,
       "batteryMonitorTemperatureMajorHighLevel": batteryMonitorTemperatureMajorHighLevel,
       "batteryMonitorTemperatureMinorHighLevel": batteryMonitorTemperatureMinorHighLevel,
       "batteryMonitorTemperatureMinorLowLevel": batteryMonitorTemperatureMinorLowLevel,
       "batteryMonitorTemperatureMajorLowLevel": batteryMonitorTemperatureMajorLowLevel,
       "batteryMonitorCurrentTable": batteryMonitorCurrentTable,
       "batteryMonitorCurrentEntry": batteryMonitorCurrentEntry,
       "batteryMonitorCurrentIndex": batteryMonitorCurrentIndex,
       "batteryMonitorCurrentStatus": batteryMonitorCurrentStatus,
       "batteryMonitorCurrentDescription": batteryMonitorCurrentDescription,
       "batteryMonitorCurrentTrapRepeatCounter": batteryMonitorCurrentTrapRepeatCounter,
       "batteryMonitorCurrentAlarmEnable": batteryMonitorCurrentAlarmEnable,
       "batteryMonitorCurrentValue": batteryMonitorCurrentValue,
       "batteryMonitorCurrentMajorHighLevel": batteryMonitorCurrentMajorHighLevel,
       "batteryMonitorCurrentMinorHighLevel": batteryMonitorCurrentMinorHighLevel,
       "batteryMonitorCurrentMinorLowLevel": batteryMonitorCurrentMinorLowLevel,
       "batteryMonitorCurrentMajorLowLevel": batteryMonitorCurrentMajorLowLevel,
       "batteryMonitorFuseTable": batteryMonitorFuseTable,
       "batteryMonitorFuseEntry": batteryMonitorFuseEntry,
       "batteryMonitorFuseIndex": batteryMonitorFuseIndex,
       "batteryMonitorFuseStatus": batteryMonitorFuseStatus,
       "batteryMonitorFuseDescription": batteryMonitorFuseDescription,
       "batteryMonitorFuseTrapRepeatCounter": batteryMonitorFuseTrapRepeatCounter,
       "batteryMonitorFuseAlarmEnable": batteryMonitorFuseAlarmEnable,
       "batteryMonitorFuseValue": batteryMonitorFuseValue,
       "batteryMonitorSymmetryTable": batteryMonitorSymmetryTable,
       "batteryMonitorSymmetryEntry": batteryMonitorSymmetryEntry,
       "batteryMonitorSymmetryIndex": batteryMonitorSymmetryIndex,
       "batteryMonitorSymmetryStatus": batteryMonitorSymmetryStatus,
       "batteryMonitorSymmetryDescription": batteryMonitorSymmetryDescription,
       "batteryMonitorSymmetryTrapRepeatCounter": batteryMonitorSymmetryTrapRepeatCounter,
       "batteryMonitorSymmetryAlarmEnable": batteryMonitorSymmetryAlarmEnable,
       "batteryMonitorSymmetryMeasureValue": batteryMonitorSymmetryMeasureValue,
       "batteryMonitorSymmetryDeltaValue": batteryMonitorSymmetryDeltaValue,
       "batteryMonitorSymmetryMajorAlarmLevel": batteryMonitorSymmetryMajorAlarmLevel,
       "batteryMonitorSymmetryMinorAlarmLevel": batteryMonitorSymmetryMinorAlarmLevel,
       "batteryEnergyLog": batteryEnergyLog,
       "batteryEnergyLogAccumulated": batteryEnergyLogAccumulated,
       "batteryEnergyLogLastHoursNumberOfEntries": batteryEnergyLogLastHoursNumberOfEntries,
       "batteryEnergyLogLastHoursTable": batteryEnergyLogLastHoursTable,
       "batteryEnergyLogLastHoursEntry": batteryEnergyLogLastHoursEntry,
       "batteryEnergyLogLastHoursIndex": batteryEnergyLogLastHoursIndex,
       "batteryEnergyLogLastHoursValue": batteryEnergyLogLastHoursValue,
       "batteryEnergyLogLastDaysNumberOfEntries": batteryEnergyLogLastDaysNumberOfEntries,
       "batteryEnergyLogLastDaysTable": batteryEnergyLogLastDaysTable,
       "batteryEnergyLogLastDaysEntry": batteryEnergyLogLastDaysEntry,
       "batteryEnergyLogLastDaysIndex": batteryEnergyLogLastDaysIndex,
       "batteryEnergyLogLastDaysValue": batteryEnergyLogLastDaysValue,
       "batteryEnergyLogLastWeeksNumberOfEntries": batteryEnergyLogLastWeeksNumberOfEntries,
       "batteryEnergyLogLastWeeksTable": batteryEnergyLogLastWeeksTable,
       "batteryEnergyLogLastWeeksEntry": batteryEnergyLogLastWeeksEntry,
       "batteryEnergyLogLastWeeksIndex": batteryEnergyLogLastWeeksIndex,
       "batteryEnergyLogLastWeeksValue": batteryEnergyLogLastWeeksValue,
       "batteryCycleLog": batteryCycleLog,
       "batteryCycleLogTotalCycles": batteryCycleLogTotalCycles,
       "batteryCycleLogDaysNumberOfEntries": batteryCycleLogDaysNumberOfEntries,
       "batteryCycleLogDaysTable": batteryCycleLogDaysTable,
       "batteryCycleLogDaysEntry": batteryCycleLogDaysEntry,
       "batteryCycleLogDaysIndex": batteryCycleLogDaysIndex,
       "batteryCycleLogDaysValue": batteryCycleLogDaysValue,
       "batteryCycleLogWeeksNumberOfEntries": batteryCycleLogWeeksNumberOfEntries,
       "batteryCycleLogWeeksTable": batteryCycleLogWeeksTable,
       "batteryCycleLogWeeksEntry": batteryCycleLogWeeksEntry,
       "batteryCycleLogWeeksIndex": batteryCycleLogWeeksIndex,
       "batteryCycleLogWeeksValue": batteryCycleLogWeeksValue,
       "batteryCycleLogMonthsNumberOfEntries": batteryCycleLogMonthsNumberOfEntries,
       "batteryCycleLogMonthsTable": batteryCycleLogMonthsTable,
       "batteryCycleLogMonthsEntry": batteryCycleLogMonthsEntry,
       "batteryCycleLogMonthsIndex": batteryCycleLogMonthsIndex,
       "batteryCycleLogMonthsValue": batteryCycleLogMonthsValue,
       "batteryEqualize": batteryEqualize,
       "batteryEqualizeVoltage": batteryEqualizeVoltage,
       "batteryEqualizeCommand": batteryEqualizeCommand,
       "batteryEqualizeCurrentThreshold": batteryEqualizeCurrentThreshold,
       "batteryEqualizeManualMaxDuration": batteryEqualizeManualMaxDuration,
       "batteryAhCharged": batteryAhCharged,
       "batteryAhChargedStatus": batteryAhChargedStatus,
       "batteryAhChargedDescription": batteryAhChargedDescription,
       "batteryAhChargedTrapRepeatCounter": batteryAhChargedTrapRepeatCounter,
       "batteryAhChargedAlarmEnable": batteryAhChargedAlarmEnable,
       "batteryAhChargedValue": batteryAhChargedValue,
       "batteryAhChargedMinorHighLevel": batteryAhChargedMinorHighLevel,
       "batteryAhChargedMajorHighLevel": batteryAhChargedMajorHighLevel,
       "batteryAhDischarged": batteryAhDischarged,
       "batteryAhDischargedStatus": batteryAhDischargedStatus,
       "batteryAhDischargedDescription": batteryAhDischargedDescription,
       "batteryAhDischargedTrapRepeatCounter": batteryAhDischargedTrapRepeatCounter,
       "batteryAhDischargedAlarmEnable": batteryAhDischargedAlarmEnable,
       "batteryAhDischargedValue": batteryAhDischargedValue,
       "batteryAhDischargedMinorHighLevel": batteryAhDischargedMinorHighLevel,
       "batteryAhDischargedMajorHighLevel": batteryAhDischargedMajorHighLevel,
       "inputs": inputs,
       "inputControlUnitsTable": inputControlUnitsTable,
       "inputControlUnitsEntry": inputControlUnitsEntry,
       "inputControlUnitIndex": inputControlUnitIndex,
       "inputControlUnitNumberOfInputs": inputControlUnitNumberOfInputs,
       "inputControlUnitInputTable": inputControlUnitInputTable,
       "inputControlUnitInputEntry": inputControlUnitInputEntry,
       "inputControlUnitInputIndex": inputControlUnitInputIndex,
       "inputControlUnitInputStatus": inputControlUnitInputStatus,
       "inputControlUnitInputDescription": inputControlUnitInputDescription,
       "inputControlUnitInputTrapRepeatCounter": inputControlUnitInputTrapRepeatCounter,
       "inputControlUnitInputAlarmEnable": inputControlUnitInputAlarmEnable,
       "inputControlUnitInputValue": inputControlUnitInputValue,
       "inputControlUnitInputConfiguration": inputControlUnitInputConfiguration,
       "inputIoUnitsTable": inputIoUnitsTable,
       "inputIoUnitsEntry": inputIoUnitsEntry,
       "inputIoUnitIndex": inputIoUnitIndex,
       "inputIoUnitNumberOfInputs": inputIoUnitNumberOfInputs,
       "inputIoUnitProgInputTable": inputIoUnitProgInputTable,
       "inputIoUnitProgInputEntry": inputIoUnitProgInputEntry,
       "inputIoUnitProgInputIndex": inputIoUnitProgInputIndex,
       "inputIoUnitProgInputStatus": inputIoUnitProgInputStatus,
       "inputIoUnitProgInputDescription": inputIoUnitProgInputDescription,
       "inputIoUnitProgInputTrapRepeatCounter": inputIoUnitProgInputTrapRepeatCounter,
       "inputIoUnitProgInputAlarmEnable": inputIoUnitProgInputAlarmEnable,
       "inputIoUnitProgInputValue": inputIoUnitProgInputValue,
       "inputIoUnitProgInputConfiguration": inputIoUnitProgInputConfiguration,
       "outputs": outputs,
       "outputControlUnitTable": outputControlUnitTable,
       "outputControlUnitEntry": outputControlUnitEntry,
       "outputControlUnitIndex": outputControlUnitIndex,
       "outputControlUnitNumberOfOutputs": outputControlUnitNumberOfOutputs,
       "outputControlUnitOutputTable": outputControlUnitOutputTable,
       "outputControlUnitOutputEntry": outputControlUnitOutputEntry,
       "outputControlUnitOutputIndex": outputControlUnitOutputIndex,
       "outputControlUnitOutputStatus": outputControlUnitOutputStatus,
       "outputControlUnitOutputDescription": outputControlUnitOutputDescription,
       "outputIoUnitTable": outputIoUnitTable,
       "outputIoUnitEntry": outputIoUnitEntry,
       "outputIoUnitIndex": outputIoUnitIndex,
       "outputIoUnitNumberOfOutputs": outputIoUnitNumberOfOutputs,
       "outputIoUnitOutputTable": outputIoUnitOutputTable,
       "outputIoUnitOutputEntry": outputIoUnitOutputEntry,
       "outputIoUnitOutputIndex": outputIoUnitOutputIndex,
       "outputIoUnitOutputStatus": outputIoUnitOutputStatus,
       "outputIoUnitOutputDescription": outputIoUnitOutputDescription,
       "controlSystem": controlSystem,
       "controlSystemStatus": controlSystemStatus,
       "controlSystemClock": controlSystemClock,
       "controlSystemNumberOfControlUnits": controlSystemNumberOfControlUnits,
       "snmp": snmp,
       "snmpSendOffTraps": snmpSendOffTraps,
       "snmpTrapRepeatRate": snmpTrapRepeatRate,
       "snmpHeartBeatTrapRepeatRate": snmpHeartBeatTrapRepeatRate,
       "snmpInhibitTraps": snmpInhibitTraps,
       "controlSystemResetManualAlarms": controlSystemResetManualAlarms,
       "controlSystemResetNumberOfModules": controlSystemResetNumberOfModules,
       "controlSystemIoUnits": controlSystemIoUnits,
       "controlSystemIoUnitsNumberOfUnits": controlSystemIoUnitsNumberOfUnits,
       "controlSystemIoUnitsTable": controlSystemIoUnitsTable,
       "controlSystemIoUnitsEntry": controlSystemIoUnitsEntry,
       "controlSystemIoUnitIndex": controlSystemIoUnitIndex,
       "controlSystemIoUnitNumberOfTemperatures": controlSystemIoUnitNumberOfTemperatures,
       "controlSystemIoUnitNumberOfFans": controlSystemIoUnitNumberOfFans,
       "controlSystemIoUnitTemperatureTable": controlSystemIoUnitTemperatureTable,
       "controlSystemIoUnitTemperatureEntry": controlSystemIoUnitTemperatureEntry,
       "controlSystemIoUnitTemperatureIndex": controlSystemIoUnitTemperatureIndex,
       "controlSystemIoUnitTemperatureStatus": controlSystemIoUnitTemperatureStatus,
       "controlSystemIoUnitTemperatureDescription": controlSystemIoUnitTemperatureDescription,
       "controlSystemIoUnitTemperatureTrapRepeatCounter": controlSystemIoUnitTemperatureTrapRepeatCounter,
       "controlSystemIoUnitTemperatureAlarmEnable": controlSystemIoUnitTemperatureAlarmEnable,
       "controlSystemIoUnitTemperatureValue": controlSystemIoUnitTemperatureValue,
       "controlSystemIoUnitTemperatureMajorHighLevel": controlSystemIoUnitTemperatureMajorHighLevel,
       "controlSystemIoUnitTemperatureMinorHighLevel": controlSystemIoUnitTemperatureMinorHighLevel,
       "controlSystemIoUnitTemperatureMinorLowLevel": controlSystemIoUnitTemperatureMinorLowLevel,
       "controlSystemIoUnitTemperatureMajorLowLevel": controlSystemIoUnitTemperatureMajorLowLevel,
       "controlSystemIoUnitFanTable": controlSystemIoUnitFanTable,
       "controlSystemIoUnitFanEntry": controlSystemIoUnitFanEntry,
       "controlSystemIoUnitFanIndex": controlSystemIoUnitFanIndex,
       "controlSystemIoUnitFanSpeedValue": controlSystemIoUnitFanSpeedValue,
       "controlSystemIoUnitFanSpeedDeviation": controlSystemIoUnitFanSpeedDeviation,
       "controlSystemIoUnitFanControl": controlSystemIoUnitFanControl,
       "controlSystemInventory": controlSystemInventory,
       "controlUnitNumberOfUnits": controlUnitNumberOfUnits,
       "controlUnitTable": controlUnitTable,
       "controlUnitEntry": controlUnitEntry,
       "controlUnitIndex": controlUnitIndex,
       "controlUnitDescription": controlUnitDescription,
       "controlUnitStatus": controlUnitStatus,
       "controlUnitSerialNumber": controlUnitSerialNumber,
       "controlUnitHwPartNumber": controlUnitHwPartNumber,
       "controlUnitHwVersion": controlUnitHwVersion,
       "controlUnitSwPartNumber": controlUnitSwPartNumber,
       "controlUnitSwVersion": controlUnitSwVersion,
       "currentMonitors": currentMonitors,
       "currentMonitorsNumberOfUnits": currentMonitorsNumberOfUnits,
       "currentMonitorsTable": currentMonitorsTable,
       "currentMonitorsEntry": currentMonitorsEntry,
       "currentMonitorIndex": currentMonitorIndex,
       "currentMonitorType": currentMonitorType,
       "currentMonitorId": currentMonitorId,
       "currentMonitorNumberOfFuses": currentMonitorNumberOfFuses,
       "currentMonitorNumberOfCurrents": currentMonitorNumberOfCurrents,
       "currentMonitorFuseTable": currentMonitorFuseTable,
       "currentMonitorFuseEntry": currentMonitorFuseEntry,
       "currentMonitorFuseIndex": currentMonitorFuseIndex,
       "currentMonitorFuseStatus": currentMonitorFuseStatus,
       "currentMonitorFuseDescription": currentMonitorFuseDescription,
       "currentMonitorFuseTrapRepeatCounter": currentMonitorFuseTrapRepeatCounter,
       "currentMonitorFuseAlarmEnable": currentMonitorFuseAlarmEnable,
       "currentMonitorFuseValue": currentMonitorFuseValue,
       "currentMonitorCurrentTable": currentMonitorCurrentTable,
       "currentMonitorCurrentEntry": currentMonitorCurrentEntry,
       "currentMonitorCurrentIndex": currentMonitorCurrentIndex,
       "currentMonitorCurrentStatus": currentMonitorCurrentStatus,
       "currentMonitorCurrentDescription": currentMonitorCurrentDescription,
       "currentMonitorCurrentTrapRepeatCounter": currentMonitorCurrentTrapRepeatCounter,
       "currentMonitorCurrentAlarmEnable": currentMonitorCurrentAlarmEnable,
       "currentMonitorCurrentValue": currentMonitorCurrentValue,
       "currentMonitorCurrentMajorAlarmLevel": currentMonitorCurrentMajorAlarmLevel,
       "currentMonitorCurrentMinorAlarmLevel": currentMonitorCurrentMinorAlarmLevel,
       "currentMonitorEnergyLogAccumulatedTable": currentMonitorEnergyLogAccumulatedTable,
       "currentMonitorEnergyLogAccumulatedEntry": currentMonitorEnergyLogAccumulatedEntry,
       "currentMonitorEnergyLogAccumulated": currentMonitorEnergyLogAccumulated,
       "currentMonitorEnergyLogLastHoursNumberOfEntries": currentMonitorEnergyLogLastHoursNumberOfEntries,
       "currentMonitorEnergyLogLastHoursTable": currentMonitorEnergyLogLastHoursTable,
       "currentMonitorEnergyLogLastHoursEntry": currentMonitorEnergyLogLastHoursEntry,
       "currentMonitorEnergyLogLastHoursIndex": currentMonitorEnergyLogLastHoursIndex,
       "currentMonitorEnergyLogLastHoursValue": currentMonitorEnergyLogLastHoursValue,
       "currentMonitorEnergyLogLastDaysNumberOfEntries": currentMonitorEnergyLogLastDaysNumberOfEntries,
       "currentMonitorEnergyLogLastDaysTable": currentMonitorEnergyLogLastDaysTable,
       "currentMonitorEnergyLogLastDaysEntry": currentMonitorEnergyLogLastDaysEntry,
       "currentMonitorEnergyLogLastDaysIndex": currentMonitorEnergyLogLastDaysIndex,
       "currentMonitorEnergyLogLastDaysValue": currentMonitorEnergyLogLastDaysValue,
       "currentMonitorEnergyLogLastWeeksNumberOfEntries": currentMonitorEnergyLogLastWeeksNumberOfEntries,
       "currentMonitorEnergyLogLastWeeksTable": currentMonitorEnergyLogLastWeeksTable,
       "currentMonitorEnergyLogLastWeeksEntry": currentMonitorEnergyLogLastWeeksEntry,
       "currentMonitorEnergyLogLastWeeksIndex": currentMonitorEnergyLogLastWeeksIndex,
       "currentMonitorEnergyLogLastWeeksValue": currentMonitorEnergyLogLastWeeksValue,
       "flexiMonitors": flexiMonitors,
       "flexiMonitorsNumberOfUnits": flexiMonitorsNumberOfUnits,
       "flexiMonitorsTable": flexiMonitorsTable,
       "flexiMonitorsEntry": flexiMonitorsEntry,
       "flexiMonitorIndex": flexiMonitorIndex,
       "flexiMonitorType": flexiMonitorType,
       "flexiMonitorId": flexiMonitorId,
       "flexiMonitorNumberOfInputs": flexiMonitorNumberOfInputs,
       "flexiMonitorNumberOfOutputs": flexiMonitorNumberOfOutputs,
       "flexiMonitorInputTable": flexiMonitorInputTable,
       "flexiMonitorInputEntry": flexiMonitorInputEntry,
       "flexiMonitorInputIndex": flexiMonitorInputIndex,
       "flexiMonitorInputStatus": flexiMonitorInputStatus,
       "flexiMonitorInputDescription": flexiMonitorInputDescription,
       "flexiMonitorInputTrapRepeatCounter": flexiMonitorInputTrapRepeatCounter,
       "flexiMonitorInputAlarmEnable": flexiMonitorInputAlarmEnable,
       "flexiMonitorInputValue": flexiMonitorInputValue,
       "flexiMonitorInputConfiguration": flexiMonitorInputConfiguration,
       "flexiMonitorOutputTable": flexiMonitorOutputTable,
       "flexiMonitorOutputEntry": flexiMonitorOutputEntry,
       "flexiMonitorOutputIndex": flexiMonitorOutputIndex,
       "flexiMonitorOutputStatus": flexiMonitorOutputStatus,
       "flexiMonitorOutputDescription": flexiMonitorOutputDescription,
       "mainControlUnits": mainControlUnits,
       "mainControlUnitsTable": mainControlUnitsTable,
       "mainControlUnitsEntry": mainControlUnitsEntry,
       "mainControlUnitIndex": mainControlUnitIndex,
       "mainControlUnitNumberOfTemperatures": mainControlUnitNumberOfTemperatures,
       "mainControlUnitTemperatureTable": mainControlUnitTemperatureTable,
       "mainControlUnitTemperatureEntry": mainControlUnitTemperatureEntry,
       "mainControlUnitTemperatureIndex": mainControlUnitTemperatureIndex,
       "mainControlUnitTemperatureStatus": mainControlUnitTemperatureStatus,
       "mainControlUnitTemperatureDescription": mainControlUnitTemperatureDescription,
       "mainControlUnitTemperatureTrapRepeatCounter": mainControlUnitTemperatureTrapRepeatCounter,
       "mainControlUnitTemperatureAlarmEnable": mainControlUnitTemperatureAlarmEnable,
       "mainControlUnitTemperatureValue": mainControlUnitTemperatureValue,
       "mainControlUnitTemperatureMajorHighLevel": mainControlUnitTemperatureMajorHighLevel,
       "mainControlUnitTemperatureMinorHighLevel": mainControlUnitTemperatureMinorHighLevel,
       "mainControlUnitTemperatureMinorLowLevel": mainControlUnitTemperatureMinorLowLevel,
       "mainControlUnitTemperatureMajorLowLevel": mainControlUnitTemperatureMajorLowLevel,
       "mainControlUnitEarthFaultTable": mainControlUnitEarthFaultTable,
       "mainControlUnitEarthFaultEntry": mainControlUnitEarthFaultEntry,
       "mainControlUnitEarthFaultStatus": mainControlUnitEarthFaultStatus,
       "mainControlUnitEarthFaultDescription": mainControlUnitEarthFaultDescription,
       "mainControlUnitEarthFaultTrapRepeatCounter": mainControlUnitEarthFaultTrapRepeatCounter,
       "mainControlUnitEarthFaultAlarmEnable": mainControlUnitEarthFaultAlarmEnable,
       "mainControlUnitEarthFaultValue": mainControlUnitEarthFaultValue,
       "mainControlUnitEarthFaultMajorAlarmLevel": mainControlUnitEarthFaultMajorAlarmLevel,
       "controlSystemSummary": controlSystemSummary,
       "mainControlUnitsError": mainControlUnitsError,
       "mainControlUnitsErrorStatus": mainControlUnitsErrorStatus,
       "mainControlUnitsErrorDescription": mainControlUnitsErrorDescription,
       "mainControlUnitsErrorTrapRepeatCounter": mainControlUnitsErrorTrapRepeatCounter,
       "mainControlUnitsErrorAlarmEnable": mainControlUnitsErrorAlarmEnable,
       "mainControlUnitsErrorValue": mainControlUnitsErrorValue,
       "mainControlUnitsErrorMajorAlarmLevel": mainControlUnitsErrorMajorAlarmLevel,
       "mainControlUnitsErrorMinorAlarmLevel": mainControlUnitsErrorMinorAlarmLevel,
       "smartNodeError": smartNodeError,
       "smartNodeErrorStatus": smartNodeErrorStatus,
       "smartNodeErrorDescription": smartNodeErrorDescription,
       "smartNodeErrorTrapRepeatCounter": smartNodeErrorTrapRepeatCounter,
       "smartNodeErrorAlarmEnable": smartNodeErrorAlarmEnable,
       "smartNodeErrorValue": smartNodeErrorValue,
       "smartNodeErrorMajorAlarmLevel": smartNodeErrorMajorAlarmLevel,
       "smartNodeErrorMinorAlarmLevel": smartNodeErrorMinorAlarmLevel,
       "batteryMonitorError": batteryMonitorError,
       "batteryMonitorErrorStatus": batteryMonitorErrorStatus,
       "batteryMonitorErrorDescription": batteryMonitorErrorDescription,
       "batteryMonitorErrorTrapRepeatCounter": batteryMonitorErrorTrapRepeatCounter,
       "batteryMonitorErrorAlarmEnable": batteryMonitorErrorAlarmEnable,
       "batteryMonitorErrorValue": batteryMonitorErrorValue,
       "batteryMonitorErrorMajorAlarmLevel": batteryMonitorErrorMajorAlarmLevel,
       "batteryMonitorErrorMinorAlarmLevel": batteryMonitorErrorMinorAlarmLevel,
       "loadMonitorError": loadMonitorError,
       "loadMonitorErrorStatus": loadMonitorErrorStatus,
       "loadMonitorErrorDescription": loadMonitorErrorDescription,
       "loadMonitorErrorTrapRepeatCounter": loadMonitorErrorTrapRepeatCounter,
       "loadMonitorErrorAlarmEnable": loadMonitorErrorAlarmEnable,
       "loadMonitorErrorValue": loadMonitorErrorValue,
       "loadMonitorErrorMajorAlarmLevel": loadMonitorErrorMajorAlarmLevel,
       "loadMonitorErrorMinorAlarmLevel": loadMonitorErrorMinorAlarmLevel,
       "ioUnitError": ioUnitError,
       "ioUnitErrorStatus": ioUnitErrorStatus,
       "ioUnitErrorDescription": ioUnitErrorDescription,
       "ioUnitErrorTrapRepeatCounter": ioUnitErrorTrapRepeatCounter,
       "ioUnitErrorAlarmEnable": ioUnitErrorAlarmEnable,
       "ioUnitErrorValue": ioUnitErrorValue,
       "ioUnitErrorMajorAlarmLevel": ioUnitErrorMajorAlarmLevel,
       "ioUnitErrorMinorAlarmLevel": ioUnitErrorMinorAlarmLevel,
       "mainsMonitorError": mainsMonitorError,
       "mainsMonitorErrorStatus": mainsMonitorErrorStatus,
       "mainsMonitorErrorDescription": mainsMonitorErrorDescription,
       "mainsMonitorErrorTrapRepeatCounter": mainsMonitorErrorTrapRepeatCounter,
       "mainsMonitorErrorAlarmEnable": mainsMonitorErrorAlarmEnable,
       "mainsMonitorErrorValue": mainsMonitorErrorValue,
       "mainsMonitorErrorMajorAlarmLevel": mainsMonitorErrorMajorAlarmLevel,
       "mainsMonitorErrorMinorAlarmLevel": mainsMonitorErrorMinorAlarmLevel,
       "flexiMonitorError": flexiMonitorError,
       "flexiMonitorErrorStatus": flexiMonitorErrorStatus,
       "flexiMonitorErrorDescription": flexiMonitorErrorDescription,
       "flexiMonitorErrorTrapRepeatCounter": flexiMonitorErrorTrapRepeatCounter,
       "flexiMonitorErrorAlarmEnable": flexiMonitorErrorAlarmEnable,
       "flexiMonitorErrorValue": flexiMonitorErrorValue,
       "flexiMonitorErrorMajorAlarmLevel": flexiMonitorErrorMajorAlarmLevel,
       "flexiMonitorErrorMinorAlarmLevel": flexiMonitorErrorMinorAlarmLevel,
       "ambientTemperature": ambientTemperature,
       "ambientTemperatureStatus": ambientTemperatureStatus,
       "ambientTemperatureDescription": ambientTemperatureDescription,
       "ambientTemperatureTrapRepeatCounter": ambientTemperatureTrapRepeatCounter,
       "ambientTemperatureAlarmEnable": ambientTemperatureAlarmEnable,
       "ambientTemperatureValue": ambientTemperatureValue,
       "ambientTemperatureMajorHighLevel": ambientTemperatureMajorHighLevel,
       "ambientTemperatureMinorHighLevel": ambientTemperatureMinorHighLevel,
       "ambientTemperatureMinorLowLevel": ambientTemperatureMinorLowLevel,
       "ambientTemperatureMajorLowLevel": ambientTemperatureMajorLowLevel,
       "deltaTemperature": deltaTemperature,
       "deltaTemperatureStatus": deltaTemperatureStatus,
       "deltaTemperatureDescription": deltaTemperatureDescription,
       "deltaTemperatureTrapRepeatCounter": deltaTemperatureTrapRepeatCounter,
       "deltaTemperatureAlarmEnable": deltaTemperatureAlarmEnable,
       "deltaTemperatureValue": deltaTemperatureValue,
       "deltaTemperatureMajorHighLevel": deltaTemperatureMajorHighLevel,
       "deltaTemperatureMinorHighLevel": deltaTemperatureMinorHighLevel,
       "deltaTemperatureMinorLowLevel": deltaTemperatureMinorLowLevel,
       "deltaTemperatureMajorLowLevel": deltaTemperatureMajorLowLevel,
       "userSuspended": userSuspended,
       "userSuspendedStatus": userSuspendedStatus,
       "userSuspendedDescription": userSuspendedDescription,
       "userSuspendedTrapRepeatCounter": userSuspendedTrapRepeatCounter,
       "userSuspendedAlarmEnable": userSuspendedAlarmEnable,
       "userSuspendedValue": userSuspendedValue,
       "userSuspendedMajorAlarmLevel": userSuspendedMajorAlarmLevel,
       "alarmGroups": alarmGroups,
       "alarmGroupTable": alarmGroupTable,
       "alarmGroupEntry": alarmGroupEntry,
       "alarmGroupIndex": alarmGroupIndex,
       "alarmGroupStatus": alarmGroupStatus,
       "alarmGroupDescription": alarmGroupDescription,
       "batteryGroup2": batteryGroup2,
       "batteryGroup2Status": batteryGroup2Status,
       "batteryGroup2Description": batteryGroup2Description,
       "batteryGroup2ReferenceVoltage": batteryGroup2ReferenceVoltage,
       "batteryGroup2FusesStatus": batteryGroup2FusesStatus,
       "batteryGroup2Voltage": batteryGroup2Voltage,
       "batteryGroup2VoltageStatus": batteryGroup2VoltageStatus,
       "batteryGroup2VoltageDescription": batteryGroup2VoltageDescription,
       "batteryGroup2VoltageTrapRepeatCounter": batteryGroup2VoltageTrapRepeatCounter,
       "batteryGroup2VoltageAlarmEnable": batteryGroup2VoltageAlarmEnable,
       "batteryGroup2VoltageValue": batteryGroup2VoltageValue,
       "batteryGroup2VoltageMajorHighLevel": batteryGroup2VoltageMajorHighLevel,
       "batteryGroup2VoltageMinorHighLevel": batteryGroup2VoltageMinorHighLevel,
       "batteryGroup2VoltageMinorLowLevel": batteryGroup2VoltageMinorLowLevel,
       "batteryGroup2VoltageMajorLowLevel": batteryGroup2VoltageMajorLowLevel,
       "batteryGroup2Currents": batteryGroup2Currents,
       "batteryGroup2CurrentsStatus": batteryGroup2CurrentsStatus,
       "batteryGroup2CurrentsDescription": batteryGroup2CurrentsDescription,
       "batteryGroup2CurrentsTrapRepeatCounter": batteryGroup2CurrentsTrapRepeatCounter,
       "batteryGroup2CurrentsAlarmEnable": batteryGroup2CurrentsAlarmEnable,
       "batteryGroup2CurrentsValue": batteryGroup2CurrentsValue,
       "batteryGroup2CurrentsMajorHighLevel": batteryGroup2CurrentsMajorHighLevel,
       "batteryGroup2CurrentsMinorHighLevel": batteryGroup2CurrentsMinorHighLevel,
       "batteryGroup2CurrentsMinorLowLevel": batteryGroup2CurrentsMinorLowLevel,
       "batteryGroup2CurrentsMajorLowLevel": batteryGroup2CurrentsMajorLowLevel,
       "batteryGroup2Temperatures": batteryGroup2Temperatures,
       "batteryGroup2TemperaturesStatus": batteryGroup2TemperaturesStatus,
       "batteryGroup2TemperaturesDescription": batteryGroup2TemperaturesDescription,
       "batteryGroup2TemperaturesTrapRepeatCounter": batteryGroup2TemperaturesTrapRepeatCounter,
       "batteryGroup2TemperaturesAlarmEnable": batteryGroup2TemperaturesAlarmEnable,
       "batteryGroup2TemperaturesValue": batteryGroup2TemperaturesValue,
       "batteryGroup2TemperaturesMajorHighLevel": batteryGroup2TemperaturesMajorHighLevel,
       "batteryGroup2TemperaturesMinorHighLevel": batteryGroup2TemperaturesMinorHighLevel,
       "batteryGroup2TemperaturesMinorLowLevel": batteryGroup2TemperaturesMinorLowLevel,
       "batteryGroup2TemperaturesMajorLowLevel": batteryGroup2TemperaturesMajorLowLevel,
       "batteryGroup2TimeLeft": batteryGroup2TimeLeft,
       "batteryGroup2TimeLeftStatus": batteryGroup2TimeLeftStatus,
       "batteryGroup2TimeLeftDescription": batteryGroup2TimeLeftDescription,
       "batteryGroup2TimeLeftTrapRepeatCounter": batteryGroup2TimeLeftTrapRepeatCounter,
       "batteryGroup2TimeLeftAlarmEnable": batteryGroup2TimeLeftAlarmEnable,
       "batteryGroup2TimeLeftValue": batteryGroup2TimeLeftValue,
       "batteryGroup2TimeLeftMinorAlarmLevel": batteryGroup2TimeLeftMinorAlarmLevel,
       "batteryGroup2TimeLeftMajorAlarmLevel": batteryGroup2TimeLeftMajorAlarmLevel,
       "batteryGroup2RemainingCapacity": batteryGroup2RemainingCapacity,
       "batteryGroup2RemainingCapacityStatus": batteryGroup2RemainingCapacityStatus,
       "batteryGroup2RemainingCapacityDescription": batteryGroup2RemainingCapacityDescription,
       "batteryGroup2RemainingCapacityTrapRepeatCounter": batteryGroup2RemainingCapacityTrapRepeatCounter,
       "batteryGroup2RemainingCapacityAlarmEnable": batteryGroup2RemainingCapacityAlarmEnable,
       "batteryGroup2RemainingCapacityValue": batteryGroup2RemainingCapacityValue,
       "batteryGroup2RemainingCapacityMinorLowLevel": batteryGroup2RemainingCapacityMinorLowLevel,
       "batteryGroup2RemainingCapacityMajorLowLevel": batteryGroup2RemainingCapacityMajorLowLevel,
       "batteryGroup2UsedCapacity": batteryGroup2UsedCapacity,
       "batteryGroup2UsedCapacityStatus": batteryGroup2UsedCapacityStatus,
       "batteryGroup2UsedCapacityDescription": batteryGroup2UsedCapacityDescription,
       "batteryGroup2UsedCapacityTrapRepeatCounter": batteryGroup2UsedCapacityTrapRepeatCounter,
       "batteryGroup2UsedCapacityAlarmEnable": batteryGroup2UsedCapacityAlarmEnable,
       "batteryGroup2UsedCapacityValue": batteryGroup2UsedCapacityValue,
       "batteryGroup2UsedCapacityMajorAlarmLevel": batteryGroup2UsedCapacityMajorAlarmLevel,
       "batteryGroup2UsedCapacityMinorAlarmLevel": batteryGroup2UsedCapacityMinorAlarmLevel,
       "batteryGroup2TotalCapacity": batteryGroup2TotalCapacity,
       "batteryGroup2TotalCapacityStatus": batteryGroup2TotalCapacityStatus,
       "batteryGroup2TotalCapacityDescription": batteryGroup2TotalCapacityDescription,
       "batteryGroup2TotalCapacityTrapRepeatCounter": batteryGroup2TotalCapacityTrapRepeatCounter,
       "batteryGroup2TotalCapacityAlarmEnable": batteryGroup2TotalCapacityAlarmEnable,
       "batteryGroup2TotalCapacityValue": batteryGroup2TotalCapacityValue,
       "batteryGroup2TotalCapacityMinorLowLevel": batteryGroup2TotalCapacityMinorLowLevel,
       "batteryGroup2TotalCapacityMajorLowLevel": batteryGroup2TotalCapacityMajorLowLevel,
       "batteryGroup2Quality": batteryGroup2Quality,
       "batteryGroup2QualityStatus": batteryGroup2QualityStatus,
       "batteryGroup2QualityDescription": batteryGroup2QualityDescription,
       "batteryGroup2QualityTrapRepeatCounter": batteryGroup2QualityTrapRepeatCounter,
       "batteryGroup2QualityAlarmEnable": batteryGroup2QualityAlarmEnable,
       "batteryGroup2QualityValue": batteryGroup2QualityValue,
       "batteryGroup2QualityMinorAlarmLevel": batteryGroup2QualityMinorAlarmLevel,
       "batteryGroup2QualityMajorAlarmLevel": batteryGroup2QualityMajorAlarmLevel,
       "batteryGroup2LVBD": batteryGroup2LVBD,
       "batteryGroup2LVBDStatus": batteryGroup2LVBDStatus,
       "batteryGroup2LVBDDescription": batteryGroup2LVBDDescription,
       "batteryGroup2LVBDTrapRepeatCounter": batteryGroup2LVBDTrapRepeatCounter,
       "batteryGroup2LVBDEnable": batteryGroup2LVBDEnable,
       "batteryGroup2LVBDValue": batteryGroup2LVBDValue,
       "batteryGroup2LVBDConnectVoltage": batteryGroup2LVBDConnectVoltage,
       "batteryGroup2LVBDDisconnectVoltage": batteryGroup2LVBDDisconnectVoltage,
       "batteryGroup2ChargeCurrentLimit": batteryGroup2ChargeCurrentLimit,
       "batteryGroup2ChargeCurrentLimitEnable": batteryGroup2ChargeCurrentLimitEnable,
       "batteryGroup2ChargeCurrentLimitValue": batteryGroup2ChargeCurrentLimitValue,
       "batteryGroup2Boost": batteryGroup2Boost,
       "batteryGroup2BoostVoltage": batteryGroup2BoostVoltage,
       "batteryGroup2BoostCommand": batteryGroup2BoostCommand,
       "batteryGroup2BoostCurrentThreshold": batteryGroup2BoostCurrentThreshold,
       "batteryGroup2BoostManualMaxDuration": batteryGroup2BoostManualMaxDuration,
       "batteryGroup2Test": batteryGroup2Test,
       "batteryGroup2TestVoltage": batteryGroup2TestVoltage,
       "batteryGroup2TestCommand": batteryGroup2TestCommand,
       "batteryGroup2TestNumberOfResults": batteryGroup2TestNumberOfResults,
       "batteryGroup2TestResultTable": batteryGroup2TestResultTable,
       "batteryGroup2TestResultEntry": batteryGroup2TestResultEntry,
       "batteryGroup2TestResultIndex": batteryGroup2TestResultIndex,
       "batteryGroup2TestResultStartDateTime": batteryGroup2TestResultStartDateTime,
       "batteryGroup2TestResultDuration": batteryGroup2TestResultDuration,
       "batteryGroup2TestResultDischarged": batteryGroup2TestResultDischarged,
       "batteryGroup2TestResultQuality": batteryGroup2TestResultQuality,
       "batteryGroup2TempComp": batteryGroup2TempComp,
       "batteryGroup2TempCompEnable": batteryGroup2TempCompEnable,
       "batteryGroup2Bank": batteryGroup2Bank,
       "batteryGroup2BankStatus": batteryGroup2BankStatus,
       "batteryGroup2BankNumberOfTemperatures": batteryGroup2BankNumberOfTemperatures,
       "batteryGroup2BankNumberOfCurrents": batteryGroup2BankNumberOfCurrents,
       "batteryGroup2BankNumberOfFuses": batteryGroup2BankNumberOfFuses,
       "batteryGroup2BankNumberOfSymmetries": batteryGroup2BankNumberOfSymmetries,
       "batteryGroup2BankTemperatureTable": batteryGroup2BankTemperatureTable,
       "batteryGroup2BankTemperatureEntry": batteryGroup2BankTemperatureEntry,
       "batteryGroup2TemperatureIndex": batteryGroup2TemperatureIndex,
       "batteryGroup2TemperatureStatus": batteryGroup2TemperatureStatus,
       "batteryGroup2TemperatureDescription": batteryGroup2TemperatureDescription,
       "batteryGroup2TemperatureTrapRepeatCounter": batteryGroup2TemperatureTrapRepeatCounter,
       "batteryGroup2TemperatureAlarmEnable": batteryGroup2TemperatureAlarmEnable,
       "batteryGroup2TemperatureValue": batteryGroup2TemperatureValue,
       "batteryGroup2TemperatureMajorHighLevel": batteryGroup2TemperatureMajorHighLevel,
       "batteryGroup2TemperatureMinorHighLevel": batteryGroup2TemperatureMinorHighLevel,
       "batteryGroup2TemperatureMinorLowLevel": batteryGroup2TemperatureMinorLowLevel,
       "batteryGroup2TemperatureMajorLowLevel": batteryGroup2TemperatureMajorLowLevel,
       "batteryGroup2BankCurrentTable": batteryGroup2BankCurrentTable,
       "batteryGroup2BankCurrentEntry": batteryGroup2BankCurrentEntry,
       "batteryGroup2CurrentIndex": batteryGroup2CurrentIndex,
       "batteryGroup2CurrentStatus": batteryGroup2CurrentStatus,
       "batteryGroup2CurrentDescription": batteryGroup2CurrentDescription,
       "batteryGroup2CurrentTrapRepeatCounter": batteryGroup2CurrentTrapRepeatCounter,
       "batteryGroup2CurrentAlarmEnable": batteryGroup2CurrentAlarmEnable,
       "batteryGroup2CurrentValue": batteryGroup2CurrentValue,
       "batteryGroup2CurrentMajorHighLevel": batteryGroup2CurrentMajorHighLevel,
       "batteryGroup2CurrentMinorHighLevel": batteryGroup2CurrentMinorHighLevel,
       "batteryGroup2CurrentMinorLowLevel": batteryGroup2CurrentMinorLowLevel,
       "batteryGroup2CurrentMajorLowLevel": batteryGroup2CurrentMajorLowLevel,
       "batteryGroup2BankFuseTable": batteryGroup2BankFuseTable,
       "batteryGroup2BankFuseEntry": batteryGroup2BankFuseEntry,
       "batteryGroup2FuseIndex": batteryGroup2FuseIndex,
       "batteryGroup2FuseStatus": batteryGroup2FuseStatus,
       "batteryGroup2FuseDescription": batteryGroup2FuseDescription,
       "batteryGroup2FuseTrapRepeatCounter": batteryGroup2FuseTrapRepeatCounter,
       "batteryGroup2FuseAlarmEnable": batteryGroup2FuseAlarmEnable,
       "batteryGroup2FuseValue": batteryGroup2FuseValue,
       "batteryGroup2BankSymmetryTable": batteryGroup2BankSymmetryTable,
       "batteryGroup2BankSymmetryEntry": batteryGroup2BankSymmetryEntry,
       "batteryGroup2BankSymmetryIndex": batteryGroup2BankSymmetryIndex,
       "batteryGroup2BankSymmetryStatus": batteryGroup2BankSymmetryStatus,
       "batteryGroup2BankSymmetryDescription": batteryGroup2BankSymmetryDescription,
       "batteryGroup2BankSymmetryTrapRepeatCounter": batteryGroup2BankSymmetryTrapRepeatCounter,
       "batteryGroup2BankSymmetryAlarmEnable": batteryGroup2BankSymmetryAlarmEnable,
       "batteryGroup2BankSymmetryMeasureValue": batteryGroup2BankSymmetryMeasureValue,
       "batteryGroup2BankSymmetryDeltaValue": batteryGroup2BankSymmetryDeltaValue,
       "batteryGroup2BankSymmetryMajorAlarmLevel": batteryGroup2BankSymmetryMajorAlarmLevel,
       "batteryGroup2BankSymmetryMinorAlarmLevel": batteryGroup2BankSymmetryMinorAlarmLevel,
       "batteryGroup2EnergyLog": batteryGroup2EnergyLog,
       "batteryGroup2EnergyLogAccumulated": batteryGroup2EnergyLogAccumulated,
       "batteryGroup2EnergyLogLastHoursNumberOfEntries": batteryGroup2EnergyLogLastHoursNumberOfEntries,
       "batteryGroup2EnergyLogLastHoursTable": batteryGroup2EnergyLogLastHoursTable,
       "batteryGroup2EnergyLogLastHoursEntry": batteryGroup2EnergyLogLastHoursEntry,
       "batteryGroup2EnergyLogLastHoursIndex": batteryGroup2EnergyLogLastHoursIndex,
       "batteryGroup2EnergyLogLastHoursValue": batteryGroup2EnergyLogLastHoursValue,
       "batteryGroup2EnergyLogLastDaysNumberOfEntries": batteryGroup2EnergyLogLastDaysNumberOfEntries,
       "batteryGroup2EnergyLogLastDaysTable": batteryGroup2EnergyLogLastDaysTable,
       "batteryGroup2EnergyLogLastDaysEntry": batteryGroup2EnergyLogLastDaysEntry,
       "batteryGroup2EnergyLogLastDaysIndex": batteryGroup2EnergyLogLastDaysIndex,
       "batteryGroup2EnergyLogLastDaysValue": batteryGroup2EnergyLogLastDaysValue,
       "batteryGroup2EnergyLogLastWeeksNumberOfEntries": batteryGroup2EnergyLogLastWeeksNumberOfEntries,
       "batteryGroup2EnergyLogLastWeeksTable": batteryGroup2EnergyLogLastWeeksTable,
       "batteryGroup2EnergyLogLastWeeksEntry": batteryGroup2EnergyLogLastWeeksEntry,
       "batteryGroup2EnergyLogLastWeeksIndex": batteryGroup2EnergyLogLastWeeksIndex,
       "batteryGroup2EnergyLogLastWeeksValue": batteryGroup2EnergyLogLastWeeksValue,
       "batteryGroup2CycleLog": batteryGroup2CycleLog,
       "batteryGroup2CycleLogTotalCycles": batteryGroup2CycleLogTotalCycles,
       "batteryGroup2CycleLogDaysNumberOfEntries": batteryGroup2CycleLogDaysNumberOfEntries,
       "batteryGroup2CycleLogDaysTable": batteryGroup2CycleLogDaysTable,
       "batteryGroup2CycleLogDaysEntry": batteryGroup2CycleLogDaysEntry,
       "batteryGroup2CycleLogDaysIndex": batteryGroup2CycleLogDaysIndex,
       "batteryGroup2CycleLogDaysValue": batteryGroup2CycleLogDaysValue,
       "batteryGroup2CycleLogWeeksNumberOfEntries": batteryGroup2CycleLogWeeksNumberOfEntries,
       "batteryGroup2CycleLogWeeksTable": batteryGroup2CycleLogWeeksTable,
       "batteryGroup2CycleLogWeeksEntry": batteryGroup2CycleLogWeeksEntry,
       "batteryGroup2CycleLogWeeksIndex": batteryGroup2CycleLogWeeksIndex,
       "batteryGroup2CycleLogWeeksValue": batteryGroup2CycleLogWeeksValue,
       "batteryGroup2CycleLogMonthsNumberOfEntries": batteryGroup2CycleLogMonthsNumberOfEntries,
       "batteryGroup2CycleLogMonthsTable": batteryGroup2CycleLogMonthsTable,
       "batteryGroup2CycleLogMonthsEntry": batteryGroup2CycleLogMonthsEntry,
       "batteryGroup2CycleLogMonthsIndex": batteryGroup2CycleLogMonthsIndex,
       "batteryGroup2CycleLogMonthsValue": batteryGroup2CycleLogMonthsValue,
       "batteryGroup2Equalize": batteryGroup2Equalize,
       "batteryGroup2EqualizeVoltage": batteryGroup2EqualizeVoltage,
       "batteryGroup2EqualizeCommand": batteryGroup2EqualizeCommand,
       "batteryGroup2EqualizeCurrentThreshold": batteryGroup2EqualizeCurrentThreshold,
       "batteryGroup2EqualizeManualMaxDuration": batteryGroup2EqualizeManualMaxDuration,
       "batteryGroup2AhCharged": batteryGroup2AhCharged,
       "batteryGroup2AhChargedStatus": batteryGroup2AhChargedStatus,
       "batteryGroup2AhChargedDescription": batteryGroup2AhChargedDescription,
       "batteryGroup2AhChargedTrapRepeatCounter": batteryGroup2AhChargedTrapRepeatCounter,
       "batteryGroup2AhChargedAlarmEnable": batteryGroup2AhChargedAlarmEnable,
       "batteryGroup2AhChargedValue": batteryGroup2AhChargedValue,
       "batteryGroup2AhChargedMinorHighLevel": batteryGroup2AhChargedMinorHighLevel,
       "batteryGroup2AhChargedMajorHighLevel": batteryGroup2AhChargedMajorHighLevel,
       "batteryGroup2AhDischarged": batteryGroup2AhDischarged,
       "batteryGroup2AhDischargedStatus": batteryGroup2AhDischargedStatus,
       "batteryGroup2AhDischargedDescription": batteryGroup2AhDischargedDescription,
       "batteryGroup2AhDischargedTrapRepeatCounter": batteryGroup2AhDischargedTrapRepeatCounter,
       "batteryGroup2AhDischargedAlarmEnable": batteryGroup2AhDischargedAlarmEnable,
       "batteryGroup2AhDischargedValue": batteryGroup2AhDischargedValue,
       "batteryGroup2AhDischargedMinorHighLevel": batteryGroup2AhDischargedMinorHighLevel,
       "batteryGroup2AhDischargedMajorHighLevel": batteryGroup2AhDischargedMajorHighLevel,
       "inverters": inverters,
       "invertersStatus": invertersStatus,
       "invertersCurrent": invertersCurrent,
       "invertersCurrentStatus": invertersCurrentStatus,
       "invertersCurrentDescription": invertersCurrentDescription,
       "invertersCurrentTrapRepeatCounter": invertersCurrentTrapRepeatCounter,
       "invertersCurrentAlarmEnable": invertersCurrentAlarmEnable,
       "invertersCurrentValue": invertersCurrentValue,
       "invertersCurrentMajorAlarmLevel": invertersCurrentMajorAlarmLevel,
       "invertersCurrentMinorAlarmLevel": invertersCurrentMinorAlarmLevel,
       "invertersCapacity": invertersCapacity,
       "invertersCapacityStatus": invertersCapacityStatus,
       "invertersCapacityDescription": invertersCapacityDescription,
       "invertersCapacityTrapRepeatCounter": invertersCapacityTrapRepeatCounter,
       "invertersCapacityAlarmEnable": invertersCapacityAlarmEnable,
       "invertersCapacityValue": invertersCapacityValue,
       "invertersCapacityMajorAlarmLevel": invertersCapacityMajorAlarmLevel,
       "invertersCapacityMinorAlarmLevel": invertersCapacityMinorAlarmLevel,
       "invertersError": invertersError,
       "invertersErrorStatus": invertersErrorStatus,
       "invertersErrorDescription": invertersErrorDescription,
       "invertersErrorTrapRepeatCounter": invertersErrorTrapRepeatCounter,
       "invertersErrorEnable": invertersErrorEnable,
       "invertersErrorValue": invertersErrorValue,
       "invertersErrorMajorAlarmLevel": invertersErrorMajorAlarmLevel,
       "invertersErrorMinorAlarmLevel": invertersErrorMinorAlarmLevel,
       "invertersNumberOfInverters": invertersNumberOfInverters,
       "inverterTable": inverterTable,
       "inverterEntry": inverterEntry,
       "inverterIndex": inverterIndex,
       "inverterStatus": inverterStatus,
       "inverterOutputCurrentValue": inverterOutputCurrentValue,
       "inverterOutputVoltageValue": inverterOutputVoltageValue,
       "inverterType": inverterType,
       "inverterHwPartNumber": inverterHwPartNumber,
       "inverterHwVersion": inverterHwVersion,
       "inverterSwPartNumber": inverterSwPartNumber,
       "inverterSwVersion": inverterSwVersion,
       "inverterOutputFrequencyValue": inverterOutputFrequencyValue,
       "inverterOutputPowerValue": inverterOutputPowerValue,
       "inverterOutputReactivePowerValue": inverterOutputReactivePowerValue,
       "invertersNumberOfGroups": invertersNumberOfGroups,
       "inverterGroupsTable": inverterGroupsTable,
       "inverterGroupsEntry": inverterGroupsEntry,
       "inverterGroupIndex": inverterGroupIndex,
       "inverterGroupStatus": inverterGroupStatus,
       "inverterGroupNumberOfInverters": inverterGroupNumberOfInverters,
       "inverterGroupCurrentTable": inverterGroupCurrentTable,
       "inverterGroupCurrentEntry": inverterGroupCurrentEntry,
       "inverterGroupCurrentStatus": inverterGroupCurrentStatus,
       "inverterGroupCurrentDescription": inverterGroupCurrentDescription,
       "inverterGroupCurrentTrapRepeatCounter": inverterGroupCurrentTrapRepeatCounter,
       "inverterGroupCurrentAlarmEnable": inverterGroupCurrentAlarmEnable,
       "inverterGroupCurrentValue": inverterGroupCurrentValue,
       "inverterGroupCurrentMajorAlarmLevel": inverterGroupCurrentMajorAlarmLevel,
       "inverterGroupCurrentMinorAlarmLevel": inverterGroupCurrentMinorAlarmLevel,
       "inverterGroupCapacityTable": inverterGroupCapacityTable,
       "inverterGroupCapacityEntry": inverterGroupCapacityEntry,
       "inverterGroupCapacityStatus": inverterGroupCapacityStatus,
       "inverterGroupCapacityDescription": inverterGroupCapacityDescription,
       "inverterGroupCapacityTrapRepeatCounter": inverterGroupCapacityTrapRepeatCounter,
       "inverterGroupCapacityAlarmEnable": inverterGroupCapacityAlarmEnable,
       "inverterGroupCapacityValue": inverterGroupCapacityValue,
       "inverterGroupCapacityMajorAlarmLevel": inverterGroupCapacityMajorAlarmLevel,
       "inverterGroupCapacityMinorAlarmLevel": inverterGroupCapacityMinorAlarmLevel,
       "inverterGroupErrorTable": inverterGroupErrorTable,
       "inverterGroupErrorEntry": inverterGroupErrorEntry,
       "inverterGroupErrorStatus": inverterGroupErrorStatus,
       "inverterGroupErrorDescription": inverterGroupErrorDescription,
       "inverterGroupErrorTrapRepeatCounter": inverterGroupErrorTrapRepeatCounter,
       "inverterGroupErrorAlarmEnable": inverterGroupErrorAlarmEnable,
       "inverterGroupErrorValue": inverterGroupErrorValue,
       "inverterGroupErrorMajorAlarmLevel": inverterGroupErrorMajorAlarmLevel,
       "inverterGroupErrorMinorAlarmLevel": inverterGroupErrorMinorAlarmLevel,
       "inverterGroupInverterTable": inverterGroupInverterTable,
       "inverterGroupInverterEntry": inverterGroupInverterEntry,
       "inverterGroupInverterIndex": inverterGroupInverterIndex,
       "inverterGroupInverterStatus": inverterGroupInverterStatus,
       "inverterGroupInverterOutputCurrentValue": inverterGroupInverterOutputCurrentValue,
       "inverterGroupInverterOutputVoltageValue": inverterGroupInverterOutputVoltageValue,
       "inverterGroupInverterType": inverterGroupInverterType,
       "inverterGroupInverterHwPartNumber": inverterGroupInverterHwPartNumber,
       "inverterGroupInverterHwVersion": inverterGroupInverterHwVersion,
       "inverterGroupInverterSwPartNumber": inverterGroupInverterSwPartNumber,
       "inverterGroupInverterSwVersion": inverterGroupInverterSwVersion,
       "inverterGroupInverterOutputFrequencyValue": inverterGroupInverterOutputFrequencyValue,
       "inverterGroupInverterOutputPowerValue": inverterGroupInverterOutputPowerValue,
       "inverterGroupInverterOutputReactivePowerValue": inverterGroupInverterOutputReactivePowerValue,
       "invertersEnergyLog": invertersEnergyLog,
       "invertersEnergyLogAccumulated": invertersEnergyLogAccumulated,
       "invertersEnergyLogLastHoursNumberOfEntries": invertersEnergyLogLastHoursNumberOfEntries,
       "invertersEnergyLogLastHoursTable": invertersEnergyLogLastHoursTable,
       "invertersEnergyLogLastHoursEntry": invertersEnergyLogLastHoursEntry,
       "invertersEnergyLogLastHoursIndex": invertersEnergyLogLastHoursIndex,
       "invertersEnergyLogLastHoursValue": invertersEnergyLogLastHoursValue,
       "invertersEnergyLogLastDaysNumberOfEntries": invertersEnergyLogLastDaysNumberOfEntries,
       "invertersEnergyLogLastDaysTable": invertersEnergyLogLastDaysTable,
       "invertersEnergyLogLastDaysEntry": invertersEnergyLogLastDaysEntry,
       "invertersEnergyLogLastDaysIndex": invertersEnergyLogLastDaysIndex,
       "invertersEnergyLogLastDaysValue": invertersEnergyLogLastDaysValue,
       "invertersEnergyLogLastWeeksNumberOfEntries": invertersEnergyLogLastWeeksNumberOfEntries,
       "invertersEnergyLogLastWeeksTable": invertersEnergyLogLastWeeksTable,
       "invertersEnergyLogLastWeeksEntry": invertersEnergyLogLastWeeksEntry,
       "invertersEnergyLogLastWeeksIndex": invertersEnergyLogLastWeeksIndex,
       "invertersEnergyLogLastWeeksValue": invertersEnergyLogLastWeeksValue,
       "inverterGroupEnergyLogTable": inverterGroupEnergyLogTable,
       "inverterGroupEnergyLogEntry": inverterGroupEnergyLogEntry,
       "inverterGroupEnergyLogAccumulated": inverterGroupEnergyLogAccumulated,
       "inverterGroupEnergyLogLastHoursNumberOfEntries": inverterGroupEnergyLogLastHoursNumberOfEntries,
       "inverterGroupEnergyLogLastDaysNumberOfEntries": inverterGroupEnergyLogLastDaysNumberOfEntries,
       "inverterGroupEnergyLogLastWeeksNumberOfEntries": inverterGroupEnergyLogLastWeeksNumberOfEntries,
       "inverterGroupEnergyLogLastHoursTable": inverterGroupEnergyLogLastHoursTable,
       "inverterGroupEnergyLogLastHoursEntry": inverterGroupEnergyLogLastHoursEntry,
       "inverterGroupEnergyLogLastHoursIndex": inverterGroupEnergyLogLastHoursIndex,
       "inverterGroupEnergyLogLastHoursValue": inverterGroupEnergyLogLastHoursValue,
       "inverterGroupEnergyLogLastDaysTable": inverterGroupEnergyLogLastDaysTable,
       "inverterGroupEnergyLogLastDaysEntry": inverterGroupEnergyLogLastDaysEntry,
       "inverterGroupEnergyLogLastDaysIndex": inverterGroupEnergyLogLastDaysIndex,
       "inverterGroupEnergyLogLastDaysValue": inverterGroupEnergyLogLastDaysValue,
       "inverterGroupEnergyLogLastWeeksTable": inverterGroupEnergyLogLastWeeksTable,
       "inverterGroupEnergyLogLastWeeksEntry": inverterGroupEnergyLogLastWeeksEntry,
       "inverterGroupEnergyLogLastWeeksIndex": inverterGroupEnergyLogLastWeeksIndex,
       "inverterGroupEnergyLogLastWeeksValue": inverterGroupEnergyLogLastWeeksValue,
       "invertersReactiveEnergyLog": invertersReactiveEnergyLog,
       "invertersReactiveEnergyLogAccumulated": invertersReactiveEnergyLogAccumulated,
       "invertersReactiveEnergyLogLastHoursNumberOfEntries": invertersReactiveEnergyLogLastHoursNumberOfEntries,
       "invertersReactiveEnergyLogLastHoursTable": invertersReactiveEnergyLogLastHoursTable,
       "invertersReactiveEnergyLogLastHoursEntry": invertersReactiveEnergyLogLastHoursEntry,
       "invertersReactiveEnergyLogLastHoursIndex": invertersReactiveEnergyLogLastHoursIndex,
       "invertersReactiveEnergyLogLastHoursValue": invertersReactiveEnergyLogLastHoursValue,
       "invertersReactiveEnergyLogLastDaysNumberOfEntries": invertersReactiveEnergyLogLastDaysNumberOfEntries,
       "invertersReactiveEnergyLogLastDaysTable": invertersReactiveEnergyLogLastDaysTable,
       "invertersReactiveEnergyLogLastDaysEntry": invertersReactiveEnergyLogLastDaysEntry,
       "invertersReactiveEnergyLogLastDaysIndex": invertersReactiveEnergyLogLastDaysIndex,
       "invertersReactiveEnergyLogLastDaysValue": invertersReactiveEnergyLogLastDaysValue,
       "invertersReactiveEnergyLogLastWeeksNumberOfEntries": invertersReactiveEnergyLogLastWeeksNumberOfEntries,
       "invertersReactiveEnergyLogLastWeeksTable": invertersReactiveEnergyLogLastWeeksTable,
       "invertersReactiveEnergyLogLastWeeksEntry": invertersReactiveEnergyLogLastWeeksEntry,
       "invertersReactiveEnergyLogLastWeeksIndex": invertersReactiveEnergyLogLastWeeksIndex,
       "invertersReactiveEnergyLogLastWeeksValue": invertersReactiveEnergyLogLastWeeksValue,
       "inverterGroupReactiveEnergyLogTable": inverterGroupReactiveEnergyLogTable,
       "inverterGroupReactiveEnergyLogEntry": inverterGroupReactiveEnergyLogEntry,
       "inverterGroupReactiveEnergyLogAccumulated": inverterGroupReactiveEnergyLogAccumulated,
       "inverterGroupReactiveEnergyLogLastHoursNoOfEntries": inverterGroupReactiveEnergyLogLastHoursNoOfEntries,
       "inverterGroupReactiveEnergyLogLastDaysNoOfEntries": inverterGroupReactiveEnergyLogLastDaysNoOfEntries,
       "inverterGroupReactiveEnergyLogLastWeeksNoOfEntries": inverterGroupReactiveEnergyLogLastWeeksNoOfEntries,
       "inverterGroupReactiveEnergyLogLastHoursTable": inverterGroupReactiveEnergyLogLastHoursTable,
       "inverterGroupReactiveEnergyLogLastHoursEntry": inverterGroupReactiveEnergyLogLastHoursEntry,
       "inverterGroupReactiveEnergyLogLastHoursIndex": inverterGroupReactiveEnergyLogLastHoursIndex,
       "inverterGroupReactiveEnergyLogLastHoursValue": inverterGroupReactiveEnergyLogLastHoursValue,
       "inverterGroupReactiveEnergyLogLastDaysTable": inverterGroupReactiveEnergyLogLastDaysTable,
       "inverterGroupReactiveEnergyLogLastDaysEntry": inverterGroupReactiveEnergyLogLastDaysEntry,
       "inverterGroupReactiveEnergyLogLastDaysIndex": inverterGroupReactiveEnergyLogLastDaysIndex,
       "inverterGroupReactiveEnergyLogLastDaysValue": inverterGroupReactiveEnergyLogLastDaysValue,
       "inverterGroupReactiveEnergyLogLastWeeksTable": inverterGroupReactiveEnergyLogLastWeeksTable,
       "inverterGroupReactiveEnergyLogLastWeeksEntry": inverterGroupReactiveEnergyLogLastWeeksEntry,
       "inverterGroupReactiveEnergyLogLastWeeksIndex": inverterGroupReactiveEnergyLogLastWeeksIndex,
       "inverterGroupReactiveEnergyLogLastWeeksValue": inverterGroupReactiveEnergyLogLastWeeksValue}
)
