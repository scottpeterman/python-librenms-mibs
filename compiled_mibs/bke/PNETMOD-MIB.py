# SNMP MIB module (PNETMOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bke\PNETMOD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:21:19 2025
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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



class OnOff(Integer32):
    """Custom type OnOff based on Integer32"""
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





class OKFail(Integer32):
    """Custom type OKFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("OK", 0),
          ("Fail", 1))
    )





class ValueType(Integer32):
    """Custom type ValueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("DI", 1),
          ("AI", 2))
    )





class AlarmDescription(Integer32):
    """Custom type AlarmDescription based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("InputGridFailure", 1),
          ("InputFuseFailure", 2),
          ("PowerSourceFailure", 3),
          ("PowerSourceCurrentOutOfRange", 4),
          ("BatteryVoltageOutOfRange", 5),
          ("BatteryCurrentChargeOutOfRange", 6),
          ("BatteryTemperatureOutOfRange", 7),
          ("BatteryFuseFailure", 8),
          ("OutputFuseFailure", 9),
          ("OutputStateDisconnected", 10))
    )





class SignedNumber(Integer32):
    """Custom type SignedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32758, 32757),
    )





class Index(Integer32):
    """Custom type Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class TimeStamp(TimeTicks):
    """Custom type TimeStamp based on TimeTicks"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bke_ObjectIdentity = ObjectIdentity
bke = _Bke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27533)
)
_PnetMod_ObjectIdentity = ObjectIdentity
pnetMod = _PnetMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27533, 5)
)
_Grid_ObjectIdentity = ObjectIdentity
grid = _Grid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27533, 5, 1)
)
_GridState_Type = OKFail
_GridState_Object = MibScalar
gridState = _GridState_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 1, 1),
    _GridState_Type()
)
gridState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gridState.setStatus("current")
_GridFuse_Type = OKFail
_GridFuse_Object = MibScalar
gridFuse = _GridFuse_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 1, 2),
    _GridFuse_Type()
)
gridFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gridFuse.setStatus("current")
_PowerSource_ObjectIdentity = ObjectIdentity
powerSource = _PowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27533, 5, 2)
)
_PowerSourceState_Type = OKFail
_PowerSourceState_Object = MibScalar
powerSourceState = _PowerSourceState_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 2, 1),
    _PowerSourceState_Type()
)
powerSourceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSourceState.setStatus("current")
_PowerSourceCurrent_Type = SignedNumber
_PowerSourceCurrent_Object = MibScalar
powerSourceCurrent = _PowerSourceCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 2, 2),
    _PowerSourceCurrent_Type()
)
powerSourceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSourceCurrent.setStatus("current")
_Accumulator_ObjectIdentity = ObjectIdentity
accumulator = _Accumulator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27533, 5, 3)
)
_AccuVoltage_Type = SignedNumber
_AccuVoltage_Object = MibScalar
accuVoltage = _AccuVoltage_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 3, 1),
    _AccuVoltage_Type()
)
accuVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accuVoltage.setStatus("current")
_AccuCurrent_Type = SignedNumber
_AccuCurrent_Object = MibScalar
accuCurrent = _AccuCurrent_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 3, 2),
    _AccuCurrent_Type()
)
accuCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accuCurrent.setStatus("current")
_AccuTemperature_Type = SignedNumber
_AccuTemperature_Object = MibScalar
accuTemperature = _AccuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 3, 3),
    _AccuTemperature_Type()
)
accuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accuTemperature.setStatus("current")
_AccuFuse_Type = OKFail
_AccuFuse_Object = MibScalar
accuFuse = _AccuFuse_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 3, 4),
    _AccuFuse_Type()
)
accuFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accuFuse.setStatus("current")
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27533, 5, 4)
)
_OutFuse_Type = OKFail
_OutFuse_Object = MibScalar
outFuse = _OutFuse_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 4, 1),
    _OutFuse_Type()
)
outFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outFuse.setStatus("current")
_OutState_Type = OnOff
_OutState_Object = MibScalar
outState = _OutState_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 4, 2),
    _OutState_Type()
)
outState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outState.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27533, 5, 10)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 10, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 10, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "PNETMOD-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
_AlarmIndex_Type = Index
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 10, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
_AlarmDescription_Type = AlarmDescription
_AlarmDescription_Object = MibTableColumn
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 10, 1, 1, 2),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("current")
_ValueType_Type = ValueType
_ValueType_Object = MibTableColumn
valueType = _ValueType_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 10, 1, 1, 3),
    _ValueType_Type()
)
valueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueType.setStatus("current")
_Value_Type = SignedNumber
_Value_Object = MibTableColumn
value = _Value_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 10, 1, 1, 4),
    _Value_Type()
)
value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    value.setStatus("current")
_AlarmTimeStamp_Type = TimeStamp
_AlarmTimeStamp_Object = MibTableColumn
alarmTimeStamp = _AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 27533, 5, 10, 1, 1, 5),
    _AlarmTimeStamp_Type()
)
alarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects

tsTrapAlarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 27533, 5, 0, 1)
)
tsTrapAlarmStart.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PNETMOD-MIB", "alarmDescription"),
        ("PNETMOD-MIB", "valueType"),
        ("PNETMOD-MIB", "value"))
)
if mibBuilder.loadTexts:
    tsTrapAlarmStart.setStatus(
        ""
    )

tsTrapAlarmEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 27533, 5, 0, 2)
)
tsTrapAlarmEnd.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PNETMOD-MIB", "alarmDescription"),
        ("PNETMOD-MIB", "valueType"),
        ("PNETMOD-MIB", "value"))
)
if mibBuilder.loadTexts:
    tsTrapAlarmEnd.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PNETMOD-MIB",
    **{"OnOff": OnOff,
       "OKFail": OKFail,
       "ValueType": ValueType,
       "AlarmDescription": AlarmDescription,
       "SignedNumber": SignedNumber,
       "Index": Index,
       "TimeStamp": TimeStamp,
       "bke": bke,
       "pnetMod": pnetMod,
       "tsTrapAlarmStart": tsTrapAlarmStart,
       "tsTrapAlarmEnd": tsTrapAlarmEnd,
       "grid": grid,
       "gridState": gridState,
       "gridFuse": gridFuse,
       "powerSource": powerSource,
       "powerSourceState": powerSourceState,
       "powerSourceCurrent": powerSourceCurrent,
       "accumulator": accumulator,
       "accuVoltage": accuVoltage,
       "accuCurrent": accuCurrent,
       "accuTemperature": accuTemperature,
       "accuFuse": accuFuse,
       "output": output,
       "outFuse": outFuse,
       "outState": outState,
       "alarms": alarms,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmDescription": alarmDescription,
       "valueType": valueType,
       "value": value,
       "alarmTimeStamp": alarmTimeStamp}
)
