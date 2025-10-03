# SNMP MIB module (RNX-UPDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\riedo\RNX-UPDU-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:22 2025
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

rnx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 55108)
)
if mibBuilder.loadTexts:
    rnx.setRevisions(
        ("2022-09-09 00:00",
         "2022-07-06 00:00",
         "2022-06-22 00:00",
         "2020-12-16 00:00",
         "2020-06-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Watts(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class VoltAmpereReactives(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class VoltAmperes(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class WattHours(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class VoltAmpereReactiveHours(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class MilliAmperes(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TenthMilliAmperes(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class MilliVolts(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class TenthDegreesCelsius(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class Permil(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_UpduMib_ObjectIdentity = ObjectIdentity
upduMib = _UpduMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55108, 1)
)
_UpduInfo_ObjectIdentity = ObjectIdentity
upduInfo = _UpduInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55108, 1, 1)
)
_UpduInfoPartNumber_Type = OctetString
_UpduInfoPartNumber_Object = MibScalar
upduInfoPartNumber = _UpduInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 1, 1),
    _UpduInfoPartNumber_Type()
)
upduInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduInfoPartNumber.setStatus("current")
_UpduInfoSerialNumber_Type = Integer32
_UpduInfoSerialNumber_Object = MibScalar
upduInfoSerialNumber = _UpduInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 1, 2),
    _UpduInfoSerialNumber_Type()
)
upduInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduInfoSerialNumber.setStatus("current")
_UpduInfoLotNumber_Type = OctetString
_UpduInfoLotNumber_Object = MibScalar
upduInfoLotNumber = _UpduInfoLotNumber_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 1, 3),
    _UpduInfoLotNumber_Type()
)
upduInfoLotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduInfoLotNumber.setStatus("current")
_UpduInventory_ObjectIdentity = ObjectIdentity
upduInventory = _UpduInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55108, 1, 2)
)
_UpduModuleTable_Object = MibTable
upduModuleTable = _UpduModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 2, 1)
)
if mibBuilder.loadTexts:
    upduModuleTable.setStatus("current")
_UpduModuleEntry_Object = MibTableRow
upduModuleEntry = _UpduModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1)
)
upduModuleEntry.setIndexNames(
    (0, "RNX-UPDU-MIB", "upduModuleIndex"),
)
if mibBuilder.loadTexts:
    upduModuleEntry.setStatus("current")


class _UpduModuleIndex_Type(Integer32):
    """Custom type upduModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_UpduModuleIndex_Type.__name__ = "Integer32"
_UpduModuleIndex_Object = MibTableColumn
upduModuleIndex = _UpduModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 1),
    _UpduModuleIndex_Type()
)
upduModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upduModuleIndex.setStatus("current")


class _UpduModuleType_Type(Integer32):
    """Custom type upduModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("icm", 1),
          ("meterModule", 2))
    )


_UpduModuleType_Type.__name__ = "Integer32"
_UpduModuleType_Object = MibTableColumn
upduModuleType = _UpduModuleType_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 2),
    _UpduModuleType_Type()
)
upduModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduModuleType.setStatus("current")
_UpduModulePartNumber_Type = OctetString
_UpduModulePartNumber_Object = MibTableColumn
upduModulePartNumber = _UpduModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 3),
    _UpduModulePartNumber_Type()
)
upduModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduModulePartNumber.setStatus("current")
_UpduModuleSerialNumber_Type = Integer32
_UpduModuleSerialNumber_Object = MibTableColumn
upduModuleSerialNumber = _UpduModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 4),
    _UpduModuleSerialNumber_Type()
)
upduModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduModuleSerialNumber.setStatus("current")
_UpduModuleLotNumber_Type = OctetString
_UpduModuleLotNumber_Object = MibTableColumn
upduModuleLotNumber = _UpduModuleLotNumber_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 2, 1, 1, 5),
    _UpduModuleLotNumber_Type()
)
upduModuleLotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduModuleLotNumber.setStatus("current")
_UpduMeasurements_ObjectIdentity = ObjectIdentity
upduMeasurements = _UpduMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3)
)
_UpduMeterTable_Object = MibTable
upduMeterTable = _UpduMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1)
)
if mibBuilder.loadTexts:
    upduMeterTable.setStatus("current")
_UpduMeterEntry_Object = MibTableRow
upduMeterEntry = _UpduMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1)
)
upduMeterEntry.setIndexNames(
    (0, "RNX-UPDU-MIB", "upduModuleIndex"),
    (0, "RNX-UPDU-MIB", "upduMeterIndex"),
)
if mibBuilder.loadTexts:
    upduMeterEntry.setStatus("current")


class _UpduMeterIndex_Type(Integer32):
    """Custom type upduMeterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_UpduMeterIndex_Type.__name__ = "Integer32"
_UpduMeterIndex_Object = MibTableColumn
upduMeterIndex = _UpduMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 1),
    _UpduMeterIndex_Type()
)
upduMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upduMeterIndex.setStatus("current")


class _UpduMeterName_Type(OctetString):
    """Custom type upduMeterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpduMeterName_Type.__name__ = "OctetString"
_UpduMeterName_Object = MibTableColumn
upduMeterName = _UpduMeterName_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 2),
    _UpduMeterName_Type()
)
upduMeterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterName.setStatus("current")


class _UpduMeterType_Type(Integer32):
    """Custom type upduMeterType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("pduTotal", 0),
          ("pduTotalCalc", 1),
          ("phaseTotal", 2),
          ("phaseTotalCalc", 3),
          ("moduleTotal", 4),
          ("moduleTotalCalc", 5),
          ("outlet", 6),
          ("outletGroup", 7))
    )


_UpduMeterType_Type.__name__ = "Integer32"
_UpduMeterType_Object = MibTableColumn
upduMeterType = _UpduMeterType_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 3),
    _UpduMeterType_Type()
)
upduMeterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterType.setStatus("current")
_UpduMeterEnergyP_Type = WattHours
_UpduMeterEnergyP_Object = MibTableColumn
upduMeterEnergyP = _UpduMeterEnergyP_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 4),
    _UpduMeterEnergyP_Type()
)
upduMeterEnergyP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterEnergyP.setStatus("current")
if mibBuilder.loadTexts:
    upduMeterEnergyP.setUnits("Wh")
_UpduMeterEnergyR1_Type = VoltAmpereReactiveHours
_UpduMeterEnergyR1_Object = MibTableColumn
upduMeterEnergyR1 = _UpduMeterEnergyR1_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 5),
    _UpduMeterEnergyR1_Type()
)
upduMeterEnergyR1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterEnergyR1.setStatus("current")
if mibBuilder.loadTexts:
    upduMeterEnergyR1.setUnits("varh")
_UpduMeterEnergyR4_Type = VoltAmpereReactiveHours
_UpduMeterEnergyR4_Object = MibTableColumn
upduMeterEnergyR4 = _UpduMeterEnergyR4_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 6),
    _UpduMeterEnergyR4_Type()
)
upduMeterEnergyR4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterEnergyR4.setStatus("current")
if mibBuilder.loadTexts:
    upduMeterEnergyR4.setUnits("varh")
_UpduMeterPowerP_Type = Watts
_UpduMeterPowerP_Object = MibTableColumn
upduMeterPowerP = _UpduMeterPowerP_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 7),
    _UpduMeterPowerP_Type()
)
upduMeterPowerP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterPowerP.setStatus("current")
if mibBuilder.loadTexts:
    upduMeterPowerP.setUnits("W")
_UpduMeterPowerQ_Type = VoltAmpereReactives
_UpduMeterPowerQ_Object = MibTableColumn
upduMeterPowerQ = _UpduMeterPowerQ_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 8),
    _UpduMeterPowerQ_Type()
)
upduMeterPowerQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterPowerQ.setStatus("current")
if mibBuilder.loadTexts:
    upduMeterPowerQ.setUnits("var")
_UpduMeterPowerS_Type = VoltAmperes
_UpduMeterPowerS_Object = MibTableColumn
upduMeterPowerS = _UpduMeterPowerS_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 9),
    _UpduMeterPowerS_Type()
)
upduMeterPowerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterPowerS.setStatus("current")
if mibBuilder.loadTexts:
    upduMeterPowerS.setUnits("VA")
_UpduMeterUrms_Type = MilliVolts
_UpduMeterUrms_Object = MibTableColumn
upduMeterUrms = _UpduMeterUrms_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 10),
    _UpduMeterUrms_Type()
)
upduMeterUrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterUrms.setStatus("current")
if mibBuilder.loadTexts:
    upduMeterUrms.setUnits("mV")
_UpduMeterIrms_Type = MilliAmperes
_UpduMeterIrms_Object = MibTableColumn
upduMeterIrms = _UpduMeterIrms_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 11),
    _UpduMeterIrms_Type()
)
upduMeterIrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterIrms.setStatus("current")
if mibBuilder.loadTexts:
    upduMeterIrms.setUnits("mA")
_UpduMeterSystemName_Type = OctetString
_UpduMeterSystemName_Object = MibTableColumn
upduMeterSystemName = _UpduMeterSystemName_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 12),
    _UpduMeterSystemName_Type()
)
upduMeterSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterSystemName.setStatus("current")


class _UpduMeterCustomName_Type(OctetString):
    """Custom type upduMeterCustomName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_UpduMeterCustomName_Type.__name__ = "OctetString"
_UpduMeterCustomName_Object = MibTableColumn
upduMeterCustomName = _UpduMeterCustomName_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 13),
    _UpduMeterCustomName_Type()
)
upduMeterCustomName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upduMeterCustomName.setStatus("current")


class _UpduMeterDescription_Type(OctetString):
    """Custom type upduMeterDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UpduMeterDescription_Type.__name__ = "OctetString"
_UpduMeterDescription_Object = MibTableColumn
upduMeterDescription = _UpduMeterDescription_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 14),
    _UpduMeterDescription_Type()
)
upduMeterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upduMeterDescription.setStatus("current")


class _UpduMeterDataQuality_Type(Integer32):
    """Custom type upduMeterDataQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("expired", 1),
          ("noData", 2))
    )


_UpduMeterDataQuality_Type.__name__ = "Integer32"
_UpduMeterDataQuality_Object = MibTableColumn
upduMeterDataQuality = _UpduMeterDataQuality_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 1, 1, 15),
    _UpduMeterDataQuality_Type()
)
upduMeterDataQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduMeterDataQuality.setStatus("current")
_UpduSensorTable_Object = MibTable
upduSensorTable = _UpduSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 2)
)
if mibBuilder.loadTexts:
    upduSensorTable.setStatus("current")
_UpduSensorEntry_Object = MibTableRow
upduSensorEntry = _UpduSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1)
)
upduSensorEntry.setIndexNames(
    (0, "RNX-UPDU-MIB", "upduSensorPort"),
)
if mibBuilder.loadTexts:
    upduSensorEntry.setStatus("current")


class _UpduSensorPort_Type(Integer32):
    """Custom type upduSensorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_UpduSensorPort_Type.__name__ = "Integer32"
_UpduSensorPort_Object = MibTableColumn
upduSensorPort = _UpduSensorPort_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 1),
    _UpduSensorPort_Type()
)
upduSensorPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upduSensorPort.setStatus("current")
_UpduSensorPortName_Type = OctetString
_UpduSensorPortName_Object = MibTableColumn
upduSensorPortName = _UpduSensorPortName_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 2),
    _UpduSensorPortName_Type()
)
upduSensorPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduSensorPortName.setStatus("current")


class _UpduSensorType_Type(Integer32):
    """Custom type upduSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("temp", 1),
          ("tempHumidity", 2))
    )


_UpduSensorType_Type.__name__ = "Integer32"
_UpduSensorType_Object = MibTableColumn
upduSensorType = _UpduSensorType_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 3),
    _UpduSensorType_Type()
)
upduSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduSensorType.setStatus("current")
_UpduSensorTemperatureCelsius_Type = TenthDegreesCelsius
_UpduSensorTemperatureCelsius_Object = MibTableColumn
upduSensorTemperatureCelsius = _UpduSensorTemperatureCelsius_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 4),
    _UpduSensorTemperatureCelsius_Type()
)
upduSensorTemperatureCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduSensorTemperatureCelsius.setStatus("current")
if mibBuilder.loadTexts:
    upduSensorTemperatureCelsius.setUnits("deg-C/10")
_UpduSensorHumidity_Type = Permil
_UpduSensorHumidity_Object = MibTableColumn
upduSensorHumidity = _UpduSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 2, 1, 5),
    _UpduSensorHumidity_Type()
)
upduSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    upduSensorHumidity.setUnits("/1000")
_UpduRcmTable_Object = MibTable
upduRcmTable = _UpduRcmTable_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 3)
)
if mibBuilder.loadTexts:
    upduRcmTable.setStatus("current")
_UpduRcmEntry_Object = MibTableRow
upduRcmEntry = _UpduRcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1)
)
upduRcmEntry.setIndexNames(
    (0, "RNX-UPDU-MIB", "upduModuleIndex"),
    (0, "RNX-UPDU-MIB", "upduRcmIndex"),
)
if mibBuilder.loadTexts:
    upduRcmEntry.setStatus("current")


class _UpduRcmIndex_Type(Integer32):
    """Custom type upduRcmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_UpduRcmIndex_Type.__name__ = "Integer32"
_UpduRcmIndex_Object = MibTableColumn
upduRcmIndex = _UpduRcmIndex_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 1),
    _UpduRcmIndex_Type()
)
upduRcmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upduRcmIndex.setStatus("current")


class _UpduRcmName_Type(OctetString):
    """Custom type upduRcmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpduRcmName_Type.__name__ = "OctetString"
_UpduRcmName_Object = MibTableColumn
upduRcmName = _UpduRcmName_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 2),
    _UpduRcmName_Type()
)
upduRcmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduRcmName.setStatus("current")
_UpduRcmCurrentRms_Type = TenthMilliAmperes
_UpduRcmCurrentRms_Object = MibTableColumn
upduRcmCurrentRms = _UpduRcmCurrentRms_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 3),
    _UpduRcmCurrentRms_Type()
)
upduRcmCurrentRms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduRcmCurrentRms.setStatus("current")
if mibBuilder.loadTexts:
    upduRcmCurrentRms.setUnits("mA/10")
_UpduRcmCurrentDc_Type = TenthMilliAmperes
_UpduRcmCurrentDc_Object = MibTableColumn
upduRcmCurrentDc = _UpduRcmCurrentDc_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 4),
    _UpduRcmCurrentDc_Type()
)
upduRcmCurrentDc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduRcmCurrentDc.setStatus("current")
if mibBuilder.loadTexts:
    upduRcmCurrentDc.setUnits("mA/10")


class _UpduRcmSensorQuality_Type(Integer32):
    """Custom type upduRcmSensorQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("nodata", 1),
          ("timeout", 2),
          ("internalerror", 3),
          ("selftestfailed", 4))
    )


_UpduRcmSensorQuality_Type.__name__ = "Integer32"
_UpduRcmSensorQuality_Object = MibTableColumn
upduRcmSensorQuality = _UpduRcmSensorQuality_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 3, 3, 1, 5),
    _UpduRcmSensorQuality_Type()
)
upduRcmSensorQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduRcmSensorQuality.setStatus("current")
_UpduControl_ObjectIdentity = ObjectIdentity
upduControl = _UpduControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55108, 1, 4)
)
_UpduRelayTable_Object = MibTable
upduRelayTable = _UpduRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 4, 1)
)
if mibBuilder.loadTexts:
    upduRelayTable.setStatus("current")
_UpduRelayEntry_Object = MibTableRow
upduRelayEntry = _UpduRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1)
)
upduRelayEntry.setIndexNames(
    (0, "RNX-UPDU-MIB", "upduModuleIndex"),
    (0, "RNX-UPDU-MIB", "upduRelayIndex"),
)
if mibBuilder.loadTexts:
    upduRelayEntry.setStatus("current")


class _UpduRelayIndex_Type(Integer32):
    """Custom type upduRelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_UpduRelayIndex_Type.__name__ = "Integer32"
_UpduRelayIndex_Object = MibTableColumn
upduRelayIndex = _UpduRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 1),
    _UpduRelayIndex_Type()
)
upduRelayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upduRelayIndex.setStatus("current")


class _UpduRelayMeterNames_Type(OctetString):
    """Custom type upduRelayMeterNames based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpduRelayMeterNames_Type.__name__ = "OctetString"
_UpduRelayMeterNames_Object = MibTableColumn
upduRelayMeterNames = _UpduRelayMeterNames_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 2),
    _UpduRelayMeterNames_Type()
)
upduRelayMeterNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduRelayMeterNames.setStatus("current")


class _UpduRelayAdminStatus_Type(Integer32):
    """Custom type upduRelayAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", 2))
    )


_UpduRelayAdminStatus_Type.__name__ = "Integer32"
_UpduRelayAdminStatus_Object = MibTableColumn
upduRelayAdminStatus = _UpduRelayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 3),
    _UpduRelayAdminStatus_Type()
)
upduRelayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upduRelayAdminStatus.setStatus("current")


class _UpduRelayOperStatus_Type(Integer32):
    """Custom type upduRelayOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", 2))
    )


_UpduRelayOperStatus_Type.__name__ = "Integer32"
_UpduRelayOperStatus_Object = MibTableColumn
upduRelayOperStatus = _UpduRelayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 4),
    _UpduRelayOperStatus_Type()
)
upduRelayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduRelayOperStatus.setStatus("current")


class _UpduRelayCondition_Type(Integer32):
    """Custom type upduRelayCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("unknown", 2))
    )


_UpduRelayCondition_Type.__name__ = "Integer32"
_UpduRelayCondition_Object = MibTableColumn
upduRelayCondition = _UpduRelayCondition_Object(
    (1, 3, 6, 1, 4, 1, 55108, 1, 4, 1, 1, 5),
    _UpduRelayCondition_Type()
)
upduRelayCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upduRelayCondition.setStatus("current")
_UpduConformance_ObjectIdentity = ObjectIdentity
upduConformance = _UpduConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55108, 1, 5)
)
_UpduMibCompliances_ObjectIdentity = ObjectIdentity
upduMibCompliances = _UpduMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55108, 1, 5, 1)
)
_UpduMibGroups_ObjectIdentity = ObjectIdentity
upduMibGroups = _UpduMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55108, 1, 5, 2)
)

# Managed Objects groups

upduMibGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 55108, 1, 5, 2, 1)
)
upduMibGroupRev1.setObjects(
      *(("RNX-UPDU-MIB", "upduInfoPartNumber"),
        ("RNX-UPDU-MIB", "upduInfoSerialNumber"),
        ("RNX-UPDU-MIB", "upduInfoLotNumber"),
        ("RNX-UPDU-MIB", "upduModuleType"),
        ("RNX-UPDU-MIB", "upduModulePartNumber"),
        ("RNX-UPDU-MIB", "upduModuleSerialNumber"),
        ("RNX-UPDU-MIB", "upduModuleLotNumber"),
        ("RNX-UPDU-MIB", "upduMeterName"),
        ("RNX-UPDU-MIB", "upduMeterType"),
        ("RNX-UPDU-MIB", "upduMeterEnergyP"),
        ("RNX-UPDU-MIB", "upduMeterEnergyR1"),
        ("RNX-UPDU-MIB", "upduMeterEnergyR4"),
        ("RNX-UPDU-MIB", "upduMeterPowerP"),
        ("RNX-UPDU-MIB", "upduMeterPowerQ"),
        ("RNX-UPDU-MIB", "upduMeterPowerS"),
        ("RNX-UPDU-MIB", "upduMeterUrms"),
        ("RNX-UPDU-MIB", "upduMeterIrms"),
        ("RNX-UPDU-MIB", "upduMeterSystemName"),
        ("RNX-UPDU-MIB", "upduMeterCustomName"),
        ("RNX-UPDU-MIB", "upduMeterDescription"),
        ("RNX-UPDU-MIB", "upduMeterDataQuality"),
        ("RNX-UPDU-MIB", "upduRelayMeterNames"),
        ("RNX-UPDU-MIB", "upduRelayAdminStatus"),
        ("RNX-UPDU-MIB", "upduRelayOperStatus"),
        ("RNX-UPDU-MIB", "upduRelayCondition"),
        ("RNX-UPDU-MIB", "upduSensorPortName"),
        ("RNX-UPDU-MIB", "upduSensorType"),
        ("RNX-UPDU-MIB", "upduSensorTemperatureCelsius"),
        ("RNX-UPDU-MIB", "upduSensorHumidity"),
        ("RNX-UPDU-MIB", "upduRcmName"),
        ("RNX-UPDU-MIB", "upduRcmCurrentRms"),
        ("RNX-UPDU-MIB", "upduRcmCurrentDc"),
        ("RNX-UPDU-MIB", "upduRcmSensorQuality"))
)
if mibBuilder.loadTexts:
    upduMibGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

upduMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 55108, 1, 5, 1, 1)
)
upduMibCompliance.setObjects(
    ("RNX-UPDU-MIB", "upduMibGroupRev1")
)
if mibBuilder.loadTexts:
    upduMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RNX-UPDU-MIB",
    **{"Watts": Watts,
       "VoltAmpereReactives": VoltAmpereReactives,
       "VoltAmperes": VoltAmperes,
       "WattHours": WattHours,
       "VoltAmpereReactiveHours": VoltAmpereReactiveHours,
       "MilliAmperes": MilliAmperes,
       "TenthMilliAmperes": TenthMilliAmperes,
       "MilliVolts": MilliVolts,
       "TenthDegreesCelsius": TenthDegreesCelsius,
       "Permil": Permil,
       "rnx": rnx,
       "upduMib": upduMib,
       "upduInfo": upduInfo,
       "upduInfoPartNumber": upduInfoPartNumber,
       "upduInfoSerialNumber": upduInfoSerialNumber,
       "upduInfoLotNumber": upduInfoLotNumber,
       "upduInventory": upduInventory,
       "upduModuleTable": upduModuleTable,
       "upduModuleEntry": upduModuleEntry,
       "upduModuleIndex": upduModuleIndex,
       "upduModuleType": upduModuleType,
       "upduModulePartNumber": upduModulePartNumber,
       "upduModuleSerialNumber": upduModuleSerialNumber,
       "upduModuleLotNumber": upduModuleLotNumber,
       "upduMeasurements": upduMeasurements,
       "upduMeterTable": upduMeterTable,
       "upduMeterEntry": upduMeterEntry,
       "upduMeterIndex": upduMeterIndex,
       "upduMeterName": upduMeterName,
       "upduMeterType": upduMeterType,
       "upduMeterEnergyP": upduMeterEnergyP,
       "upduMeterEnergyR1": upduMeterEnergyR1,
       "upduMeterEnergyR4": upduMeterEnergyR4,
       "upduMeterPowerP": upduMeterPowerP,
       "upduMeterPowerQ": upduMeterPowerQ,
       "upduMeterPowerS": upduMeterPowerS,
       "upduMeterUrms": upduMeterUrms,
       "upduMeterIrms": upduMeterIrms,
       "upduMeterSystemName": upduMeterSystemName,
       "upduMeterCustomName": upduMeterCustomName,
       "upduMeterDescription": upduMeterDescription,
       "upduMeterDataQuality": upduMeterDataQuality,
       "upduSensorTable": upduSensorTable,
       "upduSensorEntry": upduSensorEntry,
       "upduSensorPort": upduSensorPort,
       "upduSensorPortName": upduSensorPortName,
       "upduSensorType": upduSensorType,
       "upduSensorTemperatureCelsius": upduSensorTemperatureCelsius,
       "upduSensorHumidity": upduSensorHumidity,
       "upduRcmTable": upduRcmTable,
       "upduRcmEntry": upduRcmEntry,
       "upduRcmIndex": upduRcmIndex,
       "upduRcmName": upduRcmName,
       "upduRcmCurrentRms": upduRcmCurrentRms,
       "upduRcmCurrentDc": upduRcmCurrentDc,
       "upduRcmSensorQuality": upduRcmSensorQuality,
       "upduControl": upduControl,
       "upduRelayTable": upduRelayTable,
       "upduRelayEntry": upduRelayEntry,
       "upduRelayIndex": upduRelayIndex,
       "upduRelayMeterNames": upduRelayMeterNames,
       "upduRelayAdminStatus": upduRelayAdminStatus,
       "upduRelayOperStatus": upduRelayOperStatus,
       "upduRelayCondition": upduRelayCondition,
       "upduConformance": upduConformance,
       "upduMibCompliances": upduMibCompliances,
       "upduMibCompliance": upduMibCompliance,
       "upduMibGroups": upduMibGroups,
       "upduMibGroupRev1": upduMibGroupRev1}
)
