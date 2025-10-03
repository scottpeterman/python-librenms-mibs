# SNMP MIB module (GUDEADS-ESB7213-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\gude\GUDEADS-ESB7213-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:48:01 2025
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

gudeads = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28507)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsESB7213_ObjectIdentity = ObjectIdentity
gadsESB7213 = _GadsESB7213_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66)
)
_Esb7213Objects_ObjectIdentity = ObjectIdentity
esb7213Objects = _Esb7213Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1)
)
_Esb7213CommonConfig_ObjectIdentity = ObjectIdentity
esb7213CommonConfig = _Esb7213CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 1)
)
_Esb7213SNMPaccess_ObjectIdentity = ObjectIdentity
esb7213SNMPaccess = _Esb7213SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 1, 1)
)


class _Esb7213TrapCtrl_Type(Integer32):
    """Custom type esb7213TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Esb7213TrapCtrl_Type.__name__ = "Integer32"
_Esb7213TrapCtrl_Object = MibScalar
esb7213TrapCtrl = _Esb7213TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 1, 1, 1),
    _Esb7213TrapCtrl_Type()
)
esb7213TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7213TrapCtrl.setStatus("current")
_Esb7213TrapIPTable_Object = MibTable
esb7213TrapIPTable = _Esb7213TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    esb7213TrapIPTable.setStatus("current")
_Esb7213TrapIPEntry_Object = MibTableRow
esb7213TrapIPEntry = _Esb7213TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 1, 1, 2, 1)
)
esb7213TrapIPEntry.setIndexNames(
    (0, "GUDEADS-ESB7213-MIB", "esb7213TrapIPIndex"),
)
if mibBuilder.loadTexts:
    esb7213TrapIPEntry.setStatus("current")


class _Esb7213TrapIPIndex_Type(Integer32):
    """Custom type esb7213TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Esb7213TrapIPIndex_Type.__name__ = "Integer32"
_Esb7213TrapIPIndex_Object = MibTableColumn
esb7213TrapIPIndex = _Esb7213TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 1, 1, 2, 1, 1),
    _Esb7213TrapIPIndex_Type()
)
esb7213TrapIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213TrapIPIndex.setStatus("current")


class _Esb7213TrapAddr_Type(OctetString):
    """Custom type esb7213TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Esb7213TrapAddr_Type.__name__ = "OctetString"
_Esb7213TrapAddr_Object = MibTableColumn
esb7213TrapAddr = _Esb7213TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 1, 1, 2, 1, 2),
    _Esb7213TrapAddr_Type()
)
esb7213TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7213TrapAddr.setStatus("current")
_Esb7213DeviceConfig_ObjectIdentity = ObjectIdentity
esb7213DeviceConfig = _Esb7213DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 2)
)
_Esb7213IntActors_ObjectIdentity = ObjectIdentity
esb7213IntActors = _Esb7213IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 3)
)
_Esb7213ExtActors_ObjectIdentity = ObjectIdentity
esb7213ExtActors = _Esb7213ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 4)
)
_Esb7213IntSensors_ObjectIdentity = ObjectIdentity
esb7213IntSensors = _Esb7213IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 5)
)


class _Esb7213POE_Type(Integer32):
    """Custom type esb7213POE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Esb7213POE_Type.__name__ = "Integer32"
_Esb7213POE_Object = MibScalar
esb7213POE = _Esb7213POE_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 5, 10),
    _Esb7213POE_Type()
)
esb7213POE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213POE.setStatus("current")
if mibBuilder.loadTexts:
    esb7213POE.setUnits("0 = no POE, 1 = POE available")
_Esb7213NTPClient_ObjectIdentity = ObjectIdentity
esb7213NTPClient = _Esb7213NTPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 5, 15)
)


class _Esb7213NTPTimeValid_Type(Integer32):
    """Custom type esb7213NTPTimeValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notime", 0),
          ("valid", 1))
    )


_Esb7213NTPTimeValid_Type.__name__ = "Integer32"
_Esb7213NTPTimeValid_Object = MibScalar
esb7213NTPTimeValid = _Esb7213NTPTimeValid_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 5, 15, 1),
    _Esb7213NTPTimeValid_Type()
)
esb7213NTPTimeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213NTPTimeValid.setStatus("current")
_Esb7213NTPUnixTime_Type = Unsigned32
_Esb7213NTPUnixTime_Object = MibScalar
esb7213NTPUnixTime = _Esb7213NTPUnixTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 5, 15, 2),
    _Esb7213NTPUnixTime_Type()
)
esb7213NTPUnixTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213NTPUnixTime.setStatus("current")
if mibBuilder.loadTexts:
    esb7213NTPUnixTime.setUnits("s")
_Esb7213NTPLastValidTimestamp_Type = Unsigned32
_Esb7213NTPLastValidTimestamp_Object = MibScalar
esb7213NTPLastValidTimestamp = _Esb7213NTPLastValidTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 5, 15, 3),
    _Esb7213NTPLastValidTimestamp_Type()
)
esb7213NTPLastValidTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213NTPLastValidTimestamp.setStatus("current")
if mibBuilder.loadTexts:
    esb7213NTPLastValidTimestamp.setUnits("s")
_Esb7213ExtSensors_ObjectIdentity = ObjectIdentity
esb7213ExtSensors = _Esb7213ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6)
)
_Esb7213SensorTable_Object = MibTable
esb7213SensorTable = _Esb7213SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1)
)
if mibBuilder.loadTexts:
    esb7213SensorTable.setStatus("current")
_Esb7213SensorEntry_Object = MibTableRow
esb7213SensorEntry = _Esb7213SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1)
)
esb7213SensorEntry.setIndexNames(
    (0, "GUDEADS-ESB7213-MIB", "esb7213SensorIndex"),
)
if mibBuilder.loadTexts:
    esb7213SensorEntry.setStatus("current")


class _Esb7213SensorIndex_Type(Integer32):
    """Custom type esb7213SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Esb7213SensorIndex_Type.__name__ = "Integer32"
_Esb7213SensorIndex_Object = MibTableColumn
esb7213SensorIndex = _Esb7213SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1, 1),
    _Esb7213SensorIndex_Type()
)
esb7213SensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213SensorIndex.setStatus("current")
_Esb7213TempSensor_Type = Integer32
_Esb7213TempSensor_Object = MibTableColumn
esb7213TempSensor = _Esb7213TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1, 2),
    _Esb7213TempSensor_Type()
)
esb7213TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    esb7213TempSensor.setUnits("0.1 degree Celsius")
_Esb7213HygroSensor_Type = Integer32
_Esb7213HygroSensor_Object = MibTableColumn
esb7213HygroSensor = _Esb7213HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1, 3),
    _Esb7213HygroSensor_Type()
)
esb7213HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    esb7213HygroSensor.setUnits("0.1 percent humidity")


class _Esb7213InputSensor_Type(Integer32):
    """Custom type esb7213InputSensor based on Integer32"""
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


_Esb7213InputSensor_Type.__name__ = "Integer32"
_Esb7213InputSensor_Object = MibTableColumn
esb7213InputSensor = _Esb7213InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1, 4),
    _Esb7213InputSensor_Type()
)
esb7213InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213InputSensor.setStatus("current")
_Esb7213AirPressure_Type = Integer32
_Esb7213AirPressure_Object = MibTableColumn
esb7213AirPressure = _Esb7213AirPressure_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1, 5),
    _Esb7213AirPressure_Type()
)
esb7213AirPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213AirPressure.setStatus("current")
if mibBuilder.loadTexts:
    esb7213AirPressure.setUnits("1 hPA (hectopascal) ~ 1 milibar")
_Esb7213DewPoint_Type = Integer32
_Esb7213DewPoint_Object = MibTableColumn
esb7213DewPoint = _Esb7213DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1, 6),
    _Esb7213DewPoint_Type()
)
esb7213DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213DewPoint.setStatus("current")
if mibBuilder.loadTexts:
    esb7213DewPoint.setUnits("0.1 degree Celsius")
_Esb7213DewPointDiff_Type = Integer32
_Esb7213DewPointDiff_Object = MibTableColumn
esb7213DewPointDiff = _Esb7213DewPointDiff_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1, 7),
    _Esb7213DewPointDiff_Type()
)
esb7213DewPointDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213DewPointDiff.setStatus("current")
if mibBuilder.loadTexts:
    esb7213DewPointDiff.setUnits("0.1 degree Celsius")


class _Esb7213ExtSensorName_Type(OctetString):
    """Custom type esb7213ExtSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Esb7213ExtSensorName_Type.__name__ = "OctetString"
_Esb7213ExtSensorName_Object = MibTableColumn
esb7213ExtSensorName = _Esb7213ExtSensorName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 1, 1, 32),
    _Esb7213ExtSensorName_Type()
)
esb7213ExtSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7213ExtSensorName.setStatus("current")
_Esb7213ExtInputs_ObjectIdentity = ObjectIdentity
esb7213ExtInputs = _Esb7213ExtInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2)
)


class _Esb7213ExtActiveInputs_Type(Unsigned32):
    """Custom type esb7213ExtActiveInputs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Esb7213ExtActiveInputs_Type.__name__ = "Unsigned32"
_Esb7213ExtActiveInputs_Object = MibScalar
esb7213ExtActiveInputs = _Esb7213ExtActiveInputs_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2, 1),
    _Esb7213ExtActiveInputs_Type()
)
esb7213ExtActiveInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213ExtActiveInputs.setStatus("current")
_Esb7213ExtInputTable_Object = MibTable
esb7213ExtInputTable = _Esb7213ExtInputTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    esb7213ExtInputTable.setStatus("current")
_Esb7213ExtInputEntry_Object = MibTableRow
esb7213ExtInputEntry = _Esb7213ExtInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2, 2, 1)
)
esb7213ExtInputEntry.setIndexNames(
    (0, "GUDEADS-ESB7213-MIB", "esb7213ExtInputIndex"),
)
if mibBuilder.loadTexts:
    esb7213ExtInputEntry.setStatus("current")
_Esb7213ExtInputIndex_Type = Unsigned32
_Esb7213ExtInputIndex_Object = MibTableColumn
esb7213ExtInputIndex = _Esb7213ExtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2, 2, 1, 1),
    _Esb7213ExtInputIndex_Type()
)
esb7213ExtInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213ExtInputIndex.setStatus("current")


class _Esb7213ExtInput_Type(Integer32):
    """Custom type esb7213ExtInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lo", 0),
          ("hi", 1))
    )


_Esb7213ExtInput_Type.__name__ = "Integer32"
_Esb7213ExtInput_Object = MibTableColumn
esb7213ExtInput = _Esb7213ExtInput_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2, 2, 1, 2),
    _Esb7213ExtInput_Type()
)
esb7213ExtInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213ExtInput.setStatus("current")


class _Esb7213ExtInputName_Type(OctetString):
    """Custom type esb7213ExtInputName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Esb7213ExtInputName_Type.__name__ = "OctetString"
_Esb7213ExtInputName_Object = MibTableColumn
esb7213ExtInputName = _Esb7213ExtInputName_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2, 2, 1, 32),
    _Esb7213ExtInputName_Type()
)
esb7213ExtInputName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esb7213ExtInputName.setStatus("current")
_Esb7213ExtInputPortNum_Type = Integer32
_Esb7213ExtInputPortNum_Object = MibTableColumn
esb7213ExtInputPortNum = _Esb7213ExtInputPortNum_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2, 2, 1, 33),
    _Esb7213ExtInputPortNum_Type()
)
esb7213ExtInputPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213ExtInputPortNum.setStatus("current")
_Esb7213ExtInputBlockIndex_Type = Integer32
_Esb7213ExtInputBlockIndex_Object = MibTableColumn
esb7213ExtInputBlockIndex = _Esb7213ExtInputBlockIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 66, 1, 6, 2, 2, 1, 34),
    _Esb7213ExtInputBlockIndex_Type()
)
esb7213ExtInputBlockIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esb7213ExtInputBlockIndex.setStatus("current")
_Esb7213Conf_ObjectIdentity = ObjectIdentity
esb7213Conf = _Esb7213Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 2)
)
_Esb7213Groups_ObjectIdentity = ObjectIdentity
esb7213Groups = _Esb7213Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 2, 1)
)
_Esb7213Compls_ObjectIdentity = ObjectIdentity
esb7213Compls = _Esb7213Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 2, 2)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 66, 3)
)

# Managed Objects groups

esb7213BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 66, 2, 1, 1)
)
esb7213BasicGroup.setObjects(
      *(("GUDEADS-ESB7213-MIB", "esb7213TrapCtrl"),
        ("GUDEADS-ESB7213-MIB", "esb7213TrapIPIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213TrapAddr"),
        ("GUDEADS-ESB7213-MIB", "esb7213POE"),
        ("GUDEADS-ESB7213-MIB", "esb7213SensorIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213TempSensor"),
        ("GUDEADS-ESB7213-MIB", "esb7213HygroSensor"),
        ("GUDEADS-ESB7213-MIB", "esb7213InputSensor"),
        ("GUDEADS-ESB7213-MIB", "esb7213AirPressure"),
        ("GUDEADS-ESB7213-MIB", "esb7213DewPoint"),
        ("GUDEADS-ESB7213-MIB", "esb7213DewPointDiff"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtSensorName"),
        ("GUDEADS-ESB7213-MIB", "esb7213NTPTimeValid"),
        ("GUDEADS-ESB7213-MIB", "esb7213NTPUnixTime"),
        ("GUDEADS-ESB7213-MIB", "esb7213NTPLastValidTimestamp"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtActiveInputs"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInputIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInput"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInputName"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInputPortNum"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInputBlockIndex"))
)
if mibBuilder.loadTexts:
    esb7213BasicGroup.setStatus("current")


# Notification objects

esb7213TempEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 66, 3, 1)
)
esb7213TempEvtSen.setObjects(
      *(("GUDEADS-ESB7213-MIB", "esb7213SensorIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213TempSensor"))
)
if mibBuilder.loadTexts:
    esb7213TempEvtSen.setStatus(
        "current"
    )

esb7213HygroEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 66, 3, 2)
)
esb7213HygroEvtSen.setObjects(
      *(("GUDEADS-ESB7213-MIB", "esb7213SensorIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213HygroSensor"))
)
if mibBuilder.loadTexts:
    esb7213HygroEvtSen.setStatus(
        "current"
    )

esb7213InputEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 66, 3, 3)
)
esb7213InputEvtSen.setObjects(
      *(("GUDEADS-ESB7213-MIB", "esb7213SensorIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213InputSensor"))
)
if mibBuilder.loadTexts:
    esb7213InputEvtSen.setStatus(
        "current"
    )

esb7213AirPressureEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 66, 3, 4)
)
esb7213AirPressureEvtSen.setObjects(
      *(("GUDEADS-ESB7213-MIB", "esb7213SensorIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213AirPressure"))
)
if mibBuilder.loadTexts:
    esb7213AirPressureEvtSen.setStatus(
        "current"
    )

esb7213DewPtDiffEvtSen = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 66, 3, 5)
)
esb7213DewPtDiffEvtSen.setObjects(
      *(("GUDEADS-ESB7213-MIB", "esb7213SensorIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213DewPointDiff"))
)
if mibBuilder.loadTexts:
    esb7213DewPtDiffEvtSen.setStatus(
        "current"
    )

esb7213POEEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 66, 3, 6)
)
esb7213POEEvt.setObjects(
    ("GUDEADS-ESB7213-MIB", "esb7213POE")
)
if mibBuilder.loadTexts:
    esb7213POEEvt.setStatus(
        "current"
    )

esb7213ExtInputEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 66, 3, 25)
)
esb7213ExtInputEvt.setObjects(
      *(("GUDEADS-ESB7213-MIB", "esb7213ExtInputIndex"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInput"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInputName"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInputPortNum"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInputBlockIndex"))
)
if mibBuilder.loadTexts:
    esb7213ExtInputEvt.setStatus(
        "current"
    )


# Notifications groups

esb7213NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 66, 2, 1, 2)
)
esb7213NotificationGroup.setObjects(
      *(("GUDEADS-ESB7213-MIB", "esb7213TempEvtSen"),
        ("GUDEADS-ESB7213-MIB", "esb7213HygroEvtSen"),
        ("GUDEADS-ESB7213-MIB", "esb7213InputEvtSen"),
        ("GUDEADS-ESB7213-MIB", "esb7213AirPressureEvtSen"),
        ("GUDEADS-ESB7213-MIB", "esb7213DewPtDiffEvtSen"),
        ("GUDEADS-ESB7213-MIB", "esb7213POEEvt"),
        ("GUDEADS-ESB7213-MIB", "esb7213ExtInputEvt"))
)
if mibBuilder.loadTexts:
    esb7213NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-ESB7213-MIB",
    **{"gudeads": gudeads,
       "gadsESB7213": gadsESB7213,
       "esb7213Objects": esb7213Objects,
       "esb7213CommonConfig": esb7213CommonConfig,
       "esb7213SNMPaccess": esb7213SNMPaccess,
       "esb7213TrapCtrl": esb7213TrapCtrl,
       "esb7213TrapIPTable": esb7213TrapIPTable,
       "esb7213TrapIPEntry": esb7213TrapIPEntry,
       "esb7213TrapIPIndex": esb7213TrapIPIndex,
       "esb7213TrapAddr": esb7213TrapAddr,
       "esb7213DeviceConfig": esb7213DeviceConfig,
       "esb7213IntActors": esb7213IntActors,
       "esb7213ExtActors": esb7213ExtActors,
       "esb7213IntSensors": esb7213IntSensors,
       "esb7213POE": esb7213POE,
       "esb7213NTPClient": esb7213NTPClient,
       "esb7213NTPTimeValid": esb7213NTPTimeValid,
       "esb7213NTPUnixTime": esb7213NTPUnixTime,
       "esb7213NTPLastValidTimestamp": esb7213NTPLastValidTimestamp,
       "esb7213ExtSensors": esb7213ExtSensors,
       "esb7213SensorTable": esb7213SensorTable,
       "esb7213SensorEntry": esb7213SensorEntry,
       "esb7213SensorIndex": esb7213SensorIndex,
       "esb7213TempSensor": esb7213TempSensor,
       "esb7213HygroSensor": esb7213HygroSensor,
       "esb7213InputSensor": esb7213InputSensor,
       "esb7213AirPressure": esb7213AirPressure,
       "esb7213DewPoint": esb7213DewPoint,
       "esb7213DewPointDiff": esb7213DewPointDiff,
       "esb7213ExtSensorName": esb7213ExtSensorName,
       "esb7213ExtInputs": esb7213ExtInputs,
       "esb7213ExtActiveInputs": esb7213ExtActiveInputs,
       "esb7213ExtInputTable": esb7213ExtInputTable,
       "esb7213ExtInputEntry": esb7213ExtInputEntry,
       "esb7213ExtInputIndex": esb7213ExtInputIndex,
       "esb7213ExtInput": esb7213ExtInput,
       "esb7213ExtInputName": esb7213ExtInputName,
       "esb7213ExtInputPortNum": esb7213ExtInputPortNum,
       "esb7213ExtInputBlockIndex": esb7213ExtInputBlockIndex,
       "esb7213Conf": esb7213Conf,
       "esb7213Groups": esb7213Groups,
       "esb7213BasicGroup": esb7213BasicGroup,
       "esb7213NotificationGroup": esb7213NotificationGroup,
       "esb7213Compls": esb7213Compls,
       "events": events,
       "esb7213TempEvtSen": esb7213TempEvtSen,
       "esb7213HygroEvtSen": esb7213HygroEvtSen,
       "esb7213InputEvtSen": esb7213InputEvtSen,
       "esb7213AirPressureEvtSen": esb7213AirPressureEvtSen,
       "esb7213DewPtDiffEvtSen": esb7213DewPtDiffEvtSen,
       "esb7213POEEvt": esb7213POEEvt,
       "esb7213ExtInputEvt": esb7213ExtInputEvt}
)
