# SNMP MIB module (T3610-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comet\T3610-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:37 2025
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Comet_ObjectIdentity = ObjectIdentity
comet = _Comet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1)
)
_T3610_ObjectIdentity = ObjectIdentity
t3610 = _T3610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2)
)
_Values_ObjectIdentity = ObjectIdentity
values = _Values_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1)
)


class _Temp_Type(DisplayString):
    """Custom type temp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Temp_Type.__name__ = "DisplayString"
_Temp_Object = MibScalar
temp = _Temp_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 1),
    _Temp_Type()
)
temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temp.setStatus("mandatory")


class _Hum_Type(DisplayString):
    """Custom type hum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Hum_Type.__name__ = "DisplayString"
_Hum_Object = MibScalar
hum = _Hum_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 2),
    _Hum_Type()
)
hum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hum.setStatus("mandatory")


class _CompVal_Type(DisplayString):
    """Custom type compVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CompVal_Type.__name__ = "DisplayString"
_CompVal_Object = MibScalar
compVal = _CompVal_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 3),
    _CompVal_Type()
)
compVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compVal.setStatus("mandatory")


class _TempAlarm_Type(DisplayString):
    """Custom type tempAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempAlarm_Type.__name__ = "DisplayString"
_TempAlarm_Object = MibScalar
tempAlarm = _TempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 5),
    _TempAlarm_Type()
)
tempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarm.setStatus("mandatory")


class _HumAlarm_Type(DisplayString):
    """Custom type humAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HumAlarm_Type.__name__ = "DisplayString"
_HumAlarm_Object = MibScalar
humAlarm = _HumAlarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 6),
    _HumAlarm_Type()
)
humAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humAlarm.setStatus("mandatory")


class _CompValAlarm_Type(DisplayString):
    """Custom type compValAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CompValAlarm_Type.__name__ = "DisplayString"
_CompValAlarm_Object = MibScalar
compValAlarm = _CompValAlarm_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 7),
    _CompValAlarm_Type()
)
compValAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValAlarm.setStatus("mandatory")


class _TempUnit_Type(DisplayString):
    """Custom type tempUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempUnit_Type.__name__ = "DisplayString"
_TempUnit_Object = MibScalar
tempUnit = _TempUnit_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 9),
    _TempUnit_Type()
)
tempUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempUnit.setStatus("mandatory")


class _HumUnit_Type(DisplayString):
    """Custom type humUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HumUnit_Type.__name__ = "DisplayString"
_HumUnit_Object = MibScalar
humUnit = _HumUnit_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 10),
    _HumUnit_Type()
)
humUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humUnit.setStatus("mandatory")


class _CompValUnit_Type(DisplayString):
    """Custom type compValUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CompValUnit_Type.__name__ = "DisplayString"
_CompValUnit_Object = MibScalar
compValUnit = _CompValUnit_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 11),
    _CompValUnit_Type()
)
compValUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValUnit.setStatus("mandatory")


class _TempMin_Type(DisplayString):
    """Custom type tempMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempMin_Type.__name__ = "DisplayString"
_TempMin_Object = MibScalar
tempMin = _TempMin_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 13),
    _TempMin_Type()
)
tempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMin.setStatus("mandatory")


class _HumMin_Type(DisplayString):
    """Custom type humMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HumMin_Type.__name__ = "DisplayString"
_HumMin_Object = MibScalar
humMin = _HumMin_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 14),
    _HumMin_Type()
)
humMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humMin.setStatus("mandatory")


class _CompValMin_Type(DisplayString):
    """Custom type compValMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CompValMin_Type.__name__ = "DisplayString"
_CompValMin_Object = MibScalar
compValMin = _CompValMin_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 15),
    _CompValMin_Type()
)
compValMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValMin.setStatus("mandatory")


class _TempMax_Type(DisplayString):
    """Custom type tempMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TempMax_Type.__name__ = "DisplayString"
_TempMax_Object = MibScalar
tempMax = _TempMax_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 17),
    _TempMax_Type()
)
tempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMax.setStatus("mandatory")


class _HumMax_Type(DisplayString):
    """Custom type humMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HumMax_Type.__name__ = "DisplayString"
_HumMax_Object = MibScalar
humMax = _HumMax_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 18),
    _HumMax_Type()
)
humMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humMax.setStatus("mandatory")


class _CompValMax_Type(DisplayString):
    """Custom type compValMax based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CompValMax_Type.__name__ = "DisplayString"
_CompValMax_Object = MibScalar
compValMax = _CompValMax_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 1, 19),
    _CompValMax_Type()
)
compValMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValMax.setStatus("mandatory")
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2)
)


class _SensorName_Type(DisplayString):
    """Custom type sensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 68),
    )


_SensorName_Type.__name__ = "DisplayString"
_SensorName_Object = MibScalar
sensorName = _SensorName_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 1),
    _SensorName_Type()
)
sensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorName.setStatus("mandatory")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")


class _DeviceType_Type(Integer32):
    """Custom type deviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_DeviceType_Type.__name__ = "Integer32"
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 2, 3),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("mandatory")
_ValuesInt_ObjectIdentity = ObjectIdentity
valuesInt = _ValuesInt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3)
)


class _TempInt_Type(Integer32):
    """Custom type tempInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_TempInt_Type.__name__ = "Integer32"
_TempInt_Object = MibScalar
tempInt = _TempInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 1),
    _TempInt_Type()
)
tempInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempInt.setStatus("mandatory")


class _HumInt_Type(Integer32):
    """Custom type humInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HumInt_Type.__name__ = "Integer32"
_HumInt_Object = MibScalar
humInt = _HumInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 2),
    _HumInt_Type()
)
humInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humInt.setStatus("mandatory")


class _CompValInt_Type(Integer32):
    """Custom type compValInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_CompValInt_Type.__name__ = "Integer32"
_CompValInt_Object = MibScalar
compValInt = _CompValInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 3),
    _CompValInt_Type()
)
compValInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValInt.setStatus("mandatory")


class _TempAlarmInt_Type(Integer32):
    """Custom type tempAlarmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TempAlarmInt_Type.__name__ = "Integer32"
_TempAlarmInt_Object = MibScalar
tempAlarmInt = _TempAlarmInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 5),
    _TempAlarmInt_Type()
)
tempAlarmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempAlarmInt.setStatus("mandatory")


class _HumAlarmInt_Type(Integer32):
    """Custom type humAlarmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HumAlarmInt_Type.__name__ = "Integer32"
_HumAlarmInt_Object = MibScalar
humAlarmInt = _HumAlarmInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 6),
    _HumAlarmInt_Type()
)
humAlarmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humAlarmInt.setStatus("mandatory")


class _CompValAlarmInt_Type(Integer32):
    """Custom type compValAlarmInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CompValAlarmInt_Type.__name__ = "Integer32"
_CompValAlarmInt_Object = MibScalar
compValAlarmInt = _CompValAlarmInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 3, 7),
    _CompValAlarmInt_Type()
)
compValAlarmInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValAlarmInt.setStatus("mandatory")
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4)
)


class _TempLowInt_Type(Integer32):
    """Custom type tempLowInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_TempLowInt_Type.__name__ = "Integer32"
_TempLowInt_Object = MibScalar
tempLowInt = _TempLowInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 1),
    _TempLowInt_Type()
)
tempLowInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLowInt.setStatus("mandatory")


class _TempHighInt_Type(Integer32):
    """Custom type tempHighInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_TempHighInt_Type.__name__ = "Integer32"
_TempHighInt_Object = MibScalar
tempHighInt = _TempHighInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 2),
    _TempHighInt_Type()
)
tempHighInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighInt.setStatus("mandatory")


class _HumLowInt_Type(Integer32):
    """Custom type humLowInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HumLowInt_Type.__name__ = "Integer32"
_HumLowInt_Object = MibScalar
humLowInt = _HumLowInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 3),
    _HumLowInt_Type()
)
humLowInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humLowInt.setStatus("mandatory")


class _HumHighInt_Type(Integer32):
    """Custom type humHighInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HumHighInt_Type.__name__ = "Integer32"
_HumHighInt_Object = MibScalar
humHighInt = _HumHighInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 4),
    _HumHighInt_Type()
)
humHighInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humHighInt.setStatus("mandatory")


class _CompValLowInt_Type(Integer32):
    """Custom type compValLowInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_CompValLowInt_Type.__name__ = "Integer32"
_CompValLowInt_Object = MibScalar
compValLowInt = _CompValLowInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 5),
    _CompValLowInt_Type()
)
compValLowInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValLowInt.setStatus("mandatory")


class _CompValHighInt_Type(Integer32):
    """Custom type compValHighInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_CompValHighInt_Type.__name__ = "Integer32"
_CompValHighInt_Object = MibScalar
compValHighInt = _CompValHighInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 6),
    _CompValHighInt_Type()
)
compValHighInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValHighInt.setStatus("mandatory")


class _TempDelayInt_Type(Integer32):
    """Custom type tempDelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4500),
    )


_TempDelayInt_Type.__name__ = "Integer32"
_TempDelayInt_Object = MibScalar
tempDelayInt = _TempDelayInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 7),
    _TempDelayInt_Type()
)
tempDelayInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDelayInt.setStatus("mandatory")


class _HumDelayInt_Type(Integer32):
    """Custom type humDelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4500),
    )


_HumDelayInt_Type.__name__ = "Integer32"
_HumDelayInt_Object = MibScalar
humDelayInt = _HumDelayInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 8),
    _HumDelayInt_Type()
)
humDelayInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humDelayInt.setStatus("mandatory")


class _CompValDelayInt_Type(Integer32):
    """Custom type compValDelayInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4500),
    )


_CompValDelayInt_Type.__name__ = "Integer32"
_CompValDelayInt_Object = MibScalar
compValDelayInt = _CompValDelayInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 9),
    _CompValDelayInt_Type()
)
compValDelayInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValDelayInt.setStatus("mandatory")


class _TempHystInt_Type(Integer32):
    """Custom type tempHystInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TempHystInt_Type.__name__ = "Integer32"
_TempHystInt_Object = MibScalar
tempHystInt = _TempHystInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 10),
    _TempHystInt_Type()
)
tempHystInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHystInt.setStatus("mandatory")


class _HumHystInt_Type(Integer32):
    """Custom type humHystInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HumHystInt_Type.__name__ = "Integer32"
_HumHystInt_Object = MibScalar
humHystInt = _HumHystInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 11),
    _HumHystInt_Type()
)
humHystInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humHystInt.setStatus("mandatory")


class _CompValHystInt_Type(Integer32):
    """Custom type compValHystInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CompValHystInt_Type.__name__ = "Integer32"
_CompValHystInt_Object = MibScalar
compValHystInt = _CompValHystInt_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 4, 12),
    _CompValHystInt_Type()
)
compValHystInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compValHystInt.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5)
)


class _MessageString_Type(DisplayString):
    """Custom type messageString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MessageString_Type.__name__ = "DisplayString"
_MessageString_Object = MibScalar
messageString = _MessageString_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 5, 1),
    _MessageString_Type()
)
messageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageString.setStatus("mandatory")
_Tables_ObjectIdentity = ObjectIdentity
tables = _Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6)
)
_HistoryTable_Object = MibTable
historyTable = _HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    historyTable.setStatus("mandatory")
_HistoryEntry_Object = MibTableRow
historyEntry = _HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1)
)
historyEntry.setIndexNames(
    (0, "T3610-MIB", "histTemp"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("optional")


class _HistTemp_Type(Integer32):
    """Custom type histTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HistTemp_Type.__name__ = "Integer32"
_HistTemp_Object = MibTableColumn
histTemp = _HistTemp_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 1),
    _HistTemp_Type()
)
histTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histTemp.setStatus("mandatory")


class _HistHum_Type(Integer32):
    """Custom type histHum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HistHum_Type.__name__ = "Integer32"
_HistHum_Object = MibTableColumn
histHum = _HistHum_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 2),
    _HistHum_Type()
)
histHum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histHum.setStatus("mandatory")


class _HistCompVal_Type(Integer32):
    """Custom type histCompVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-5000, 20000),
    )


_HistCompVal_Type.__name__ = "Integer32"
_HistCompVal_Object = MibTableColumn
histCompVal = _HistCompVal_Object(
    (1, 3, 6, 1, 4, 1, 22626, 1, 2, 6, 1, 1, 3),
    _HistCompVal_Type()
)
histCompVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    histCompVal.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 0)
)
trapTest.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        ""
    )

trapNTPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 1)
)
trapNTPError.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapNTPError.setStatus(
        ""
    )

trapEmailErrLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 2)
)
trapEmailErrLogin.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrLogin.setStatus(
        ""
    )

trapEmailErrAuth = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 3)
)
trapEmailErrAuth.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrAuth.setStatus(
        ""
    )

trapEmailErrSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 4)
)
trapEmailErrSome.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSome.setStatus(
        ""
    )

trapEmailErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 5)
)
trapEmailErrSocket.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrSocket.setStatus(
        ""
    )

trapEmailErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 6)
)
trapEmailErrDNS.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapEmailErrDNS.setStatus(
        ""
    )

trapSOAPErrFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 7)
)
trapSOAPErrFile.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrFile.setStatus(
        ""
    )

trapSOAPErrDNS = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 8)
)
trapSOAPErrDNS.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDNS.setStatus(
        ""
    )

trapSOAPErrSocket = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 9)
)
trapSOAPErrSocket.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrSocket.setStatus(
        ""
    )

trapSOAPErrDelivery = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 10)
)
trapSOAPErrDelivery.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"))
)
if mibBuilder.loadTexts:
    trapSOAPErrDelivery.setStatus(
        ""
    )

trapTempHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 11)
)
trapTempHighAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "temp"),
        ("T3610-MIB", "tempAlarmInt"))
)
if mibBuilder.loadTexts:
    trapTempHighAlarm.setStatus(
        ""
    )

trapHumHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 12)
)
trapHumHighAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "hum"),
        ("T3610-MIB", "humAlarmInt"))
)
if mibBuilder.loadTexts:
    trapHumHighAlarm.setStatus(
        ""
    )

trapCompValHighAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 13)
)
trapCompValHighAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "compVal"),
        ("T3610-MIB", "compValAlarmInt"))
)
if mibBuilder.loadTexts:
    trapCompValHighAlarm.setStatus(
        ""
    )

trapTempLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 21)
)
trapTempLowAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "temp"),
        ("T3610-MIB", "tempAlarmInt"))
)
if mibBuilder.loadTexts:
    trapTempLowAlarm.setStatus(
        ""
    )

trapHumLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 22)
)
trapHumLowAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "hum"),
        ("T3610-MIB", "humAlarmInt"))
)
if mibBuilder.loadTexts:
    trapHumLowAlarm.setStatus(
        ""
    )

trapCompValLowAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 23)
)
trapCompValLowAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "compVal"),
        ("T3610-MIB", "compValAlarmInt"))
)
if mibBuilder.loadTexts:
    trapCompValLowAlarm.setStatus(
        ""
    )

trapTempClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 31)
)
trapTempClrAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "temp"),
        ("T3610-MIB", "tempAlarmInt"))
)
if mibBuilder.loadTexts:
    trapTempClrAlarm.setStatus(
        ""
    )

trapHumClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 32)
)
trapHumClrAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "hum"),
        ("T3610-MIB", "humAlarmInt"))
)
if mibBuilder.loadTexts:
    trapHumClrAlarm.setStatus(
        ""
    )

trapCompValClrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 33)
)
trapCompValClrAlarm.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "compVal"),
        ("T3610-MIB", "compValAlarmInt"))
)
if mibBuilder.loadTexts:
    trapCompValClrAlarm.setStatus(
        ""
    )

trapTempError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 41)
)
trapTempError.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "temp"),
        ("T3610-MIB", "tempAlarmInt"))
)
if mibBuilder.loadTexts:
    trapTempError.setStatus(
        ""
    )

trapHumError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 42)
)
trapHumError.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "hum"),
        ("T3610-MIB", "humAlarmInt"))
)
if mibBuilder.loadTexts:
    trapHumError.setStatus(
        ""
    )

trapCompValError = NotificationType(
    (1, 3, 6, 1, 4, 1, 22626, 0, 43)
)
trapCompValError.setObjects(
      *(("T3610-MIB", "sensorName"),
        ("T3610-MIB", "messageString"),
        ("T3610-MIB", "compVal"),
        ("T3610-MIB", "compValAlarmInt"))
)
if mibBuilder.loadTexts:
    trapCompValError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T3610-MIB",
    **{"DisplayString": DisplayString,
       "comet": comet,
       "trapTest": trapTest,
       "trapNTPError": trapNTPError,
       "trapEmailErrLogin": trapEmailErrLogin,
       "trapEmailErrAuth": trapEmailErrAuth,
       "trapEmailErrSome": trapEmailErrSome,
       "trapEmailErrSocket": trapEmailErrSocket,
       "trapEmailErrDNS": trapEmailErrDNS,
       "trapSOAPErrFile": trapSOAPErrFile,
       "trapSOAPErrDNS": trapSOAPErrDNS,
       "trapSOAPErrSocket": trapSOAPErrSocket,
       "trapSOAPErrDelivery": trapSOAPErrDelivery,
       "trapTempHighAlarm": trapTempHighAlarm,
       "trapHumHighAlarm": trapHumHighAlarm,
       "trapCompValHighAlarm": trapCompValHighAlarm,
       "trapTempLowAlarm": trapTempLowAlarm,
       "trapHumLowAlarm": trapHumLowAlarm,
       "trapCompValLowAlarm": trapCompValLowAlarm,
       "trapTempClrAlarm": trapTempClrAlarm,
       "trapHumClrAlarm": trapHumClrAlarm,
       "trapCompValClrAlarm": trapCompValClrAlarm,
       "trapTempError": trapTempError,
       "trapHumError": trapHumError,
       "trapCompValError": trapCompValError,
       "products": products,
       "t3610": t3610,
       "values": values,
       "temp": temp,
       "hum": hum,
       "compVal": compVal,
       "tempAlarm": tempAlarm,
       "humAlarm": humAlarm,
       "compValAlarm": compValAlarm,
       "tempUnit": tempUnit,
       "humUnit": humUnit,
       "compValUnit": compValUnit,
       "tempMin": tempMin,
       "humMin": humMin,
       "compValMin": compValMin,
       "tempMax": tempMax,
       "humMax": humMax,
       "compValMax": compValMax,
       "global": _pysmi_global,
       "sensorName": sensorName,
       "serialNumber": serialNumber,
       "deviceType": deviceType,
       "valuesInt": valuesInt,
       "tempInt": tempInt,
       "humInt": humInt,
       "compValInt": compValInt,
       "tempAlarmInt": tempAlarmInt,
       "humAlarmInt": humAlarmInt,
       "compValAlarmInt": compValAlarmInt,
       "settings": settings,
       "tempLowInt": tempLowInt,
       "tempHighInt": tempHighInt,
       "humLowInt": humLowInt,
       "humHighInt": humHighInt,
       "compValLowInt": compValLowInt,
       "compValHighInt": compValHighInt,
       "tempDelayInt": tempDelayInt,
       "humDelayInt": humDelayInt,
       "compValDelayInt": compValDelayInt,
       "tempHystInt": tempHystInt,
       "humHystInt": humHystInt,
       "compValHystInt": compValHystInt,
       "traps": traps,
       "messageString": messageString,
       "tables": tables,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "histTemp": histTemp,
       "histHum": histHum,
       "histCompVal": histCompVal}
)
