# SNMP MIB module (NETTRACK-E3METER-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\riedo\NETTRACK-E3METER-SNMP-MIB
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

e3Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10)
)
if mibBuilder.loadTexts:
    e3Mib.setRevisions(
        ("2018-10-09 00:00",
         "2018-10-08 00:00",
         "2016-04-18 00:00",
         "2016-02-03 00:00",
         "2012-04-12 00:00",
         "2011-11-02 00:00",
         "2011-08-19 00:00",
         "2011-01-26 00:00",
         "2010-12-06 00:00",
         "2010-10-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Watts(TextualConvention, Integer32):
    status = "current"


class VoltAmpereReactives(TextualConvention, Integer32):
    status = "current"


class VoltAmperes(TextualConvention, Integer32):
    status = "current"


class WattHours(TextualConvention, Integer32):
    status = "current"


class VoltAmpereReactiveHours(TextualConvention, Integer32):
    status = "current"


class VoltAmpereHours(TextualConvention, Integer32):
    status = "current"


class MilliAmperes(TextualConvention, Integer32):
    status = "current"


class MilliVolts(TextualConvention, Integer32):
    status = "current"


class MilliHertz(TextualConvention, Integer32):
    status = "current"


class DeciDegreesCelsius(TextualConvention, Integer32):
    status = "current"


class Permil(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Nettrack_ObjectIdentity = ObjectIdentity
nettrack = _Nettrack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21695)
)
_Public_ObjectIdentity = ObjectIdentity
public = _Public_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21695, 1)
)
_E3Ipm_ObjectIdentity = ObjectIdentity
e3Ipm = _E3Ipm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7)
)
_E3IpmInfo_ObjectIdentity = ObjectIdentity
e3IpmInfo = _E3IpmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1)
)
_E3IpmInfoSerial_Type = Integer32
_E3IpmInfoSerial_Object = MibScalar
e3IpmInfoSerial = _E3IpmInfoSerial_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 1),
    _E3IpmInfoSerial_Type()
)
e3IpmInfoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmInfoSerial.setStatus("current")
_E3IpmInfoModel_Type = Integer32
_E3IpmInfoModel_Object = MibScalar
e3IpmInfoModel = _E3IpmInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 2),
    _E3IpmInfoModel_Type()
)
e3IpmInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmInfoModel.setStatus("current")


class _E3IpmInfoHWVersion_Type(Integer32):
    """Custom type e3IpmInfoHWVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rev-a", 0),
          ("rev-b", 1))
    )


_E3IpmInfoHWVersion_Type.__name__ = "Integer32"
_E3IpmInfoHWVersion_Object = MibScalar
e3IpmInfoHWVersion = _E3IpmInfoHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 3),
    _E3IpmInfoHWVersion_Type()
)
e3IpmInfoHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmInfoHWVersion.setStatus("current")
_E3IpmInfoFWVersion_Type = Integer32
_E3IpmInfoFWVersion_Object = MibScalar
e3IpmInfoFWVersion = _E3IpmInfoFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 4),
    _E3IpmInfoFWVersion_Type()
)
e3IpmInfoFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmInfoFWVersion.setStatus("current")
_E3IpmInfoMeters_Type = Integer32
_E3IpmInfoMeters_Object = MibScalar
e3IpmInfoMeters = _E3IpmInfoMeters_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 5),
    _E3IpmInfoMeters_Type()
)
e3IpmInfoMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmInfoMeters.setStatus("current")
_E3IpmMeterTable_Object = MibTable
e3IpmMeterTable = _E3IpmMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2)
)
if mibBuilder.loadTexts:
    e3IpmMeterTable.setStatus("current")
_E3IpmMeterEntry_Object = MibTableRow
e3IpmMeterEntry = _E3IpmMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1)
)
e3IpmMeterEntry.setIndexNames(
    (0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmMeter"),
)
if mibBuilder.loadTexts:
    e3IpmMeterEntry.setStatus("current")
_E3IpmMeter_Type = Integer32
_E3IpmMeter_Object = MibTableColumn
e3IpmMeter = _E3IpmMeter_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 1),
    _E3IpmMeter_Type()
)
e3IpmMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmMeter.setStatus("current")
_E3IpmEnergyP_Type = WattHours
_E3IpmEnergyP_Object = MibTableColumn
e3IpmEnergyP = _E3IpmEnergyP_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 2),
    _E3IpmEnergyP_Type()
)
e3IpmEnergyP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmEnergyP.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmEnergyP.setUnits("Wh")
_E3IpmEnergyQ_Type = VoltAmpereReactiveHours
_E3IpmEnergyQ_Object = MibTableColumn
e3IpmEnergyQ = _E3IpmEnergyQ_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 3),
    _E3IpmEnergyQ_Type()
)
e3IpmEnergyQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmEnergyQ.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmEnergyQ.setUnits("varh")
_E3IpmEnergyS_Type = VoltAmpereHours
_E3IpmEnergyS_Object = MibTableColumn
e3IpmEnergyS = _E3IpmEnergyS_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 4),
    _E3IpmEnergyS_Type()
)
e3IpmEnergyS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmEnergyS.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmEnergyS.setUnits("VAh")
_E3IpmPowerP_Type = Watts
_E3IpmPowerP_Object = MibTableColumn
e3IpmPowerP = _E3IpmPowerP_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 5),
    _E3IpmPowerP_Type()
)
e3IpmPowerP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPowerP.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPowerP.setUnits("W")
_E3IpmPowerQ_Type = VoltAmpereReactives
_E3IpmPowerQ_Object = MibTableColumn
e3IpmPowerQ = _E3IpmPowerQ_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 6),
    _E3IpmPowerQ_Type()
)
e3IpmPowerQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPowerQ.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPowerQ.setUnits("var")
_E3IpmPowerS_Type = VoltAmperes
_E3IpmPowerS_Object = MibTableColumn
e3IpmPowerS = _E3IpmPowerS_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 7),
    _E3IpmPowerS_Type()
)
e3IpmPowerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPowerS.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPowerS.setUnits("VA")
_E3IpmUrms_Type = MilliVolts
_E3IpmUrms_Object = MibTableColumn
e3IpmUrms = _E3IpmUrms_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 8),
    _E3IpmUrms_Type()
)
e3IpmUrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUrms.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmUrms.setUnits("mV")
_E3IpmIrms_Type = MilliAmperes
_E3IpmIrms_Object = MibTableColumn
e3IpmIrms = _E3IpmIrms_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 9),
    _E3IpmIrms_Type()
)
e3IpmIrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmIrms.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmIrms.setUnits("mA")
_E3IpmFrequency_Type = MilliHertz
_E3IpmFrequency_Object = MibTableColumn
e3IpmFrequency = _E3IpmFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 10),
    _E3IpmFrequency_Type()
)
e3IpmFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmFrequency.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmFrequency.setUnits("mHz")


class _E3IpmChannelName_Type(OctetString):
    """Custom type e3IpmChannelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_E3IpmChannelName_Type.__name__ = "OctetString"
_E3IpmChannelName_Object = MibTableColumn
e3IpmChannelName = _E3IpmChannelName_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 11),
    _E3IpmChannelName_Type()
)
e3IpmChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmChannelName.setStatus("current")


class _E3IpmChannelType_Type(Integer32):
    """Custom type e3IpmChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("live-wire", 0),
          ("neutral-wire", 1))
    )


_E3IpmChannelType_Type.__name__ = "Integer32"
_E3IpmChannelType_Object = MibTableColumn
e3IpmChannelType = _E3IpmChannelType_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 12),
    _E3IpmChannelType_Type()
)
e3IpmChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmChannelType.setStatus("current")
_E3IpmSensorTable_Object = MibTable
e3IpmSensorTable = _E3IpmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3)
)
if mibBuilder.loadTexts:
    e3IpmSensorTable.setStatus("current")
_E3IpmSensorEntry_Object = MibTableRow
e3IpmSensorEntry = _E3IpmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1)
)
e3IpmSensorEntry.setIndexNames(
    (0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
)
if mibBuilder.loadTexts:
    e3IpmSensorEntry.setStatus("current")
_E3IpmSensor_Type = Integer32
_E3IpmSensor_Object = MibTableColumn
e3IpmSensor = _E3IpmSensor_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 1),
    _E3IpmSensor_Type()
)
e3IpmSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmSensor.setStatus("current")


class _E3IpmSensorType_Type(Integer32):
    """Custom type e3IpmSensorType based on Integer32"""
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
          ("temp-humidity", 2))
    )


_E3IpmSensorType_Type.__name__ = "Integer32"
_E3IpmSensorType_Object = MibTableColumn
e3IpmSensorType = _E3IpmSensorType_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 2),
    _E3IpmSensorType_Type()
)
e3IpmSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmSensorType.setStatus("current")


class _E3IpmSensorVersion_Type(OctetString):
    """Custom type e3IpmSensorVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_E3IpmSensorVersion_Type.__name__ = "OctetString"
_E3IpmSensorVersion_Object = MibTableColumn
e3IpmSensorVersion = _E3IpmSensorVersion_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 3),
    _E3IpmSensorVersion_Type()
)
e3IpmSensorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmSensorVersion.setStatus("current")
_E3IpmSensorTemperatureCelsius_Type = DeciDegreesCelsius
_E3IpmSensorTemperatureCelsius_Object = MibTableColumn
e3IpmSensorTemperatureCelsius = _E3IpmSensorTemperatureCelsius_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 4),
    _E3IpmSensorTemperatureCelsius_Type()
)
e3IpmSensorTemperatureCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmSensorTemperatureCelsius.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmSensorTemperatureCelsius.setUnits("deg-C/10")
_E3IpmSensorHumidity_Type = Permil
_E3IpmSensorHumidity_Object = MibTableColumn
e3IpmSensorHumidity = _E3IpmSensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 5),
    _E3IpmSensorHumidity_Type()
)
e3IpmSensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmSensorHumidity.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmSensorHumidity.setUnits("/1000")
_E3IpmPGroupTable_Object = MibTable
e3IpmPGroupTable = _E3IpmPGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4)
)
if mibBuilder.loadTexts:
    e3IpmPGroupTable.setStatus("current")
_E3IpmPGroupEntry_Object = MibTableRow
e3IpmPGroupEntry = _E3IpmPGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1)
)
e3IpmPGroupEntry.setIndexNames(
    (0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmPGroup"),
)
if mibBuilder.loadTexts:
    e3IpmPGroupEntry.setStatus("current")
_E3IpmPGroup_Type = Integer32
_E3IpmPGroup_Object = MibTableColumn
e3IpmPGroup = _E3IpmPGroup_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 1),
    _E3IpmPGroup_Type()
)
e3IpmPGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGroup.setStatus("current")


class _E3IpmPGName_Type(OctetString):
    """Custom type e3IpmPGName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_E3IpmPGName_Type.__name__ = "OctetString"
_E3IpmPGName_Object = MibTableColumn
e3IpmPGName = _E3IpmPGName_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 2),
    _E3IpmPGName_Type()
)
e3IpmPGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGName.setStatus("current")
_E3IpmPGMembers_Type = Integer32
_E3IpmPGMembers_Object = MibTableColumn
e3IpmPGMembers = _E3IpmPGMembers_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 3),
    _E3IpmPGMembers_Type()
)
e3IpmPGMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGMembers.setStatus("current")
_E3IpmPGEnergyP_Type = WattHours
_E3IpmPGEnergyP_Object = MibTableColumn
e3IpmPGEnergyP = _E3IpmPGEnergyP_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 4),
    _E3IpmPGEnergyP_Type()
)
e3IpmPGEnergyP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGEnergyP.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPGEnergyP.setUnits("Wh")
_E3IpmPGEnergyQ_Type = VoltAmpereReactiveHours
_E3IpmPGEnergyQ_Object = MibTableColumn
e3IpmPGEnergyQ = _E3IpmPGEnergyQ_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 5),
    _E3IpmPGEnergyQ_Type()
)
e3IpmPGEnergyQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGEnergyQ.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPGEnergyQ.setUnits("varh")
_E3IpmPGEnergyS_Type = VoltAmpereHours
_E3IpmPGEnergyS_Object = MibTableColumn
e3IpmPGEnergyS = _E3IpmPGEnergyS_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 6),
    _E3IpmPGEnergyS_Type()
)
e3IpmPGEnergyS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGEnergyS.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPGEnergyS.setUnits("VAh")
_E3IpmPGPowerP_Type = Watts
_E3IpmPGPowerP_Object = MibTableColumn
e3IpmPGPowerP = _E3IpmPGPowerP_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 7),
    _E3IpmPGPowerP_Type()
)
e3IpmPGPowerP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGPowerP.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPGPowerP.setUnits("W")
_E3IpmPGPowerQ_Type = VoltAmpereReactives
_E3IpmPGPowerQ_Object = MibTableColumn
e3IpmPGPowerQ = _E3IpmPGPowerQ_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 8),
    _E3IpmPGPowerQ_Type()
)
e3IpmPGPowerQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGPowerQ.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPGPowerQ.setUnits("var")
_E3IpmPGPowerS_Type = VoltAmperes
_E3IpmPGPowerS_Object = MibTableColumn
e3IpmPGPowerS = _E3IpmPGPowerS_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 9),
    _E3IpmPGPowerS_Type()
)
e3IpmPGPowerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGPowerS.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPGPowerS.setUnits("VA")
_E3IpmPGIrms_Type = MilliAmperes
_E3IpmPGIrms_Object = MibTableColumn
e3IpmPGIrms = _E3IpmPGIrms_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 10),
    _E3IpmPGIrms_Type()
)
e3IpmPGIrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmPGIrms.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmPGIrms.setUnits("mA")
_E3IpmUGroupTable_Object = MibTable
e3IpmUGroupTable = _E3IpmUGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5)
)
if mibBuilder.loadTexts:
    e3IpmUGroupTable.setStatus("current")
_E3IpmUGroupEntry_Object = MibTableRow
e3IpmUGroupEntry = _E3IpmUGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1)
)
e3IpmUGroupEntry.setIndexNames(
    (0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmUGroup"),
)
if mibBuilder.loadTexts:
    e3IpmUGroupEntry.setStatus("current")
_E3IpmUGroup_Type = Integer32
_E3IpmUGroup_Object = MibTableColumn
e3IpmUGroup = _E3IpmUGroup_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 1),
    _E3IpmUGroup_Type()
)
e3IpmUGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGroup.setStatus("current")


class _E3IpmUGName_Type(OctetString):
    """Custom type e3IpmUGName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_E3IpmUGName_Type.__name__ = "OctetString"
_E3IpmUGName_Object = MibTableColumn
e3IpmUGName = _E3IpmUGName_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 2),
    _E3IpmUGName_Type()
)
e3IpmUGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGName.setStatus("current")
_E3IpmUGMembers_Type = Integer32
_E3IpmUGMembers_Object = MibTableColumn
e3IpmUGMembers = _E3IpmUGMembers_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 3),
    _E3IpmUGMembers_Type()
)
e3IpmUGMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGMembers.setStatus("current")
_E3IpmUGEnergyP_Type = WattHours
_E3IpmUGEnergyP_Object = MibTableColumn
e3IpmUGEnergyP = _E3IpmUGEnergyP_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 4),
    _E3IpmUGEnergyP_Type()
)
e3IpmUGEnergyP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGEnergyP.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmUGEnergyP.setUnits("Wh")
_E3IpmUGEnergyQ_Type = VoltAmpereReactiveHours
_E3IpmUGEnergyQ_Object = MibTableColumn
e3IpmUGEnergyQ = _E3IpmUGEnergyQ_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 5),
    _E3IpmUGEnergyQ_Type()
)
e3IpmUGEnergyQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGEnergyQ.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmUGEnergyQ.setUnits("varh")
_E3IpmUGEnergyS_Type = VoltAmpereHours
_E3IpmUGEnergyS_Object = MibTableColumn
e3IpmUGEnergyS = _E3IpmUGEnergyS_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 6),
    _E3IpmUGEnergyS_Type()
)
e3IpmUGEnergyS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGEnergyS.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmUGEnergyS.setUnits("VAh")
_E3IpmUGPowerP_Type = Watts
_E3IpmUGPowerP_Object = MibTableColumn
e3IpmUGPowerP = _E3IpmUGPowerP_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 7),
    _E3IpmUGPowerP_Type()
)
e3IpmUGPowerP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGPowerP.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmUGPowerP.setUnits("W")
_E3IpmUGPowerQ_Type = VoltAmpereReactives
_E3IpmUGPowerQ_Object = MibTableColumn
e3IpmUGPowerQ = _E3IpmUGPowerQ_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 8),
    _E3IpmUGPowerQ_Type()
)
e3IpmUGPowerQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGPowerQ.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmUGPowerQ.setUnits("var")
_E3IpmUGPowerS_Type = VoltAmperes
_E3IpmUGPowerS_Object = MibTableColumn
e3IpmUGPowerS = _E3IpmUGPowerS_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 9),
    _E3IpmUGPowerS_Type()
)
e3IpmUGPowerS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGPowerS.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmUGPowerS.setUnits("VA")
_E3IpmUGIrms_Type = MilliAmperes
_E3IpmUGIrms_Object = MibTableColumn
e3IpmUGIrms = _E3IpmUGIrms_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 10),
    _E3IpmUGIrms_Type()
)
e3IpmUGIrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmUGIrms.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmUGIrms.setUnits("mA")
_E3IpmAlarmTable_Object = MibTable
e3IpmAlarmTable = _E3IpmAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6)
)
if mibBuilder.loadTexts:
    e3IpmAlarmTable.setStatus("current")
_E3IpmAlarmTableEntry_Object = MibTableRow
e3IpmAlarmTableEntry = _E3IpmAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1)
)
e3IpmAlarmTableEntry.setIndexNames(
    (0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmAlarmIndex"),
)
if mibBuilder.loadTexts:
    e3IpmAlarmTableEntry.setStatus("current")


class _E3IpmAlarmIndex_Type(Integer32):
    """Custom type e3IpmAlarmIndex based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("current-l1", 0),
          ("current-l2", 1),
          ("current-l3", 2),
          ("current-n", 3),
          ("temp-int", 4),
          ("temp-ext1", 5),
          ("temp-ext2", 6),
          ("rh-ext1", 7),
          ("rh-ext2", 8))
    )


_E3IpmAlarmIndex_Type.__name__ = "Integer32"
_E3IpmAlarmIndex_Object = MibTableColumn
e3IpmAlarmIndex = _E3IpmAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 1),
    _E3IpmAlarmIndex_Type()
)
e3IpmAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmIndex.setStatus("current")


class _E3IpmAlarmState_Type(Integer32):
    """Custom type e3IpmAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical-low", 0),
          ("warn-low", 1),
          ("normal", 2),
          ("warn-high", 3),
          ("critical-high", 4),
          ("unknown", 5))
    )


_E3IpmAlarmState_Type.__name__ = "Integer32"
_E3IpmAlarmState_Object = MibTableColumn
e3IpmAlarmState = _E3IpmAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 2),
    _E3IpmAlarmState_Type()
)
e3IpmAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmState.setStatus("current")
_E3IpmAlarmCritLowSet_Type = TruthValue
_E3IpmAlarmCritLowSet_Object = MibTableColumn
e3IpmAlarmCritLowSet = _E3IpmAlarmCritLowSet_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 3),
    _E3IpmAlarmCritLowSet_Type()
)
e3IpmAlarmCritLowSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmCritLowSet.setStatus("current")
_E3IpmAlarmCritLow_Type = Integer32
_E3IpmAlarmCritLow_Object = MibTableColumn
e3IpmAlarmCritLow = _E3IpmAlarmCritLow_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 4),
    _E3IpmAlarmCritLow_Type()
)
e3IpmAlarmCritLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmCritLow.setStatus("current")
_E3IpmAlarmWarnLowSet_Type = TruthValue
_E3IpmAlarmWarnLowSet_Object = MibTableColumn
e3IpmAlarmWarnLowSet = _E3IpmAlarmWarnLowSet_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 5),
    _E3IpmAlarmWarnLowSet_Type()
)
e3IpmAlarmWarnLowSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmWarnLowSet.setStatus("current")
_E3IpmAlarmWarnLow_Type = Integer32
_E3IpmAlarmWarnLow_Object = MibTableColumn
e3IpmAlarmWarnLow = _E3IpmAlarmWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 6),
    _E3IpmAlarmWarnLow_Type()
)
e3IpmAlarmWarnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmWarnLow.setStatus("current")
_E3IpmAlarmWarnHighSet_Type = TruthValue
_E3IpmAlarmWarnHighSet_Object = MibTableColumn
e3IpmAlarmWarnHighSet = _E3IpmAlarmWarnHighSet_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 7),
    _E3IpmAlarmWarnHighSet_Type()
)
e3IpmAlarmWarnHighSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmWarnHighSet.setStatus("current")
_E3IpmAlarmWarnHigh_Type = Integer32
_E3IpmAlarmWarnHigh_Object = MibTableColumn
e3IpmAlarmWarnHigh = _E3IpmAlarmWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 8),
    _E3IpmAlarmWarnHigh_Type()
)
e3IpmAlarmWarnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmWarnHigh.setStatus("current")
_E3IpmAlarmCritHighSet_Type = TruthValue
_E3IpmAlarmCritHighSet_Object = MibTableColumn
e3IpmAlarmCritHighSet = _E3IpmAlarmCritHighSet_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 9),
    _E3IpmAlarmCritHighSet_Type()
)
e3IpmAlarmCritHighSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmCritHighSet.setStatus("current")
_E3IpmAlarmCritHigh_Type = Integer32
_E3IpmAlarmCritHigh_Object = MibTableColumn
e3IpmAlarmCritHigh = _E3IpmAlarmCritHigh_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 6, 1, 10),
    _E3IpmAlarmCritHigh_Type()
)
e3IpmAlarmCritHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmAlarmCritHigh.setStatus("current")
_E3IpmRcmTable_Type = Integer32
_E3IpmRcmTable_Object = MibScalar
e3IpmRcmTable = _E3IpmRcmTable_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 7),
    _E3IpmRcmTable_Type()
)
e3IpmRcmTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmRcmTable.setStatus("current")
_E3IpmRcmTableEntry_Object = MibTableRow
e3IpmRcmTableEntry = _E3IpmRcmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 7, 1)
)
e3IpmRcmTableEntry.setIndexNames(
    (0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmChannel"),
)
if mibBuilder.loadTexts:
    e3IpmRcmTableEntry.setStatus("current")


class _E3IpmRcmChannel_Type(Integer32):
    """Custom type e3IpmRcmChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("total", 0)
    )


_E3IpmRcmChannel_Type.__name__ = "Integer32"
_E3IpmRcmChannel_Object = MibTableColumn
e3IpmRcmChannel = _E3IpmRcmChannel_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 7, 1, 1),
    _E3IpmRcmChannel_Type()
)
e3IpmRcmChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmRcmChannel.setStatus("current")
_E3IpmRcmAcLimit_Type = MilliAmperes
_E3IpmRcmAcLimit_Object = MibTableColumn
e3IpmRcmAcLimit = _E3IpmRcmAcLimit_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 7, 1, 2),
    _E3IpmRcmAcLimit_Type()
)
e3IpmRcmAcLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmRcmAcLimit.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmRcmAcLimit.setUnits("mA")
_E3IpmRcmDcLimit_Type = MilliAmperes
_E3IpmRcmDcLimit_Object = MibTableColumn
e3IpmRcmDcLimit = _E3IpmRcmDcLimit_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 7, 1, 3),
    _E3IpmRcmDcLimit_Type()
)
e3IpmRcmDcLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmRcmDcLimit.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmRcmDcLimit.setUnits("mA")


class _E3IpmRcmStatus_Type(Integer32):
    """Custom type e3IpmRcmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("valid", 1))
    )


_E3IpmRcmStatus_Type.__name__ = "Integer32"
_E3IpmRcmStatus_Object = MibTableColumn
e3IpmRcmStatus = _E3IpmRcmStatus_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 7, 1, 4),
    _E3IpmRcmStatus_Type()
)
e3IpmRcmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmRcmStatus.setStatus("current")
_E3IpmRcmAc_Type = MilliAmperes
_E3IpmRcmAc_Object = MibTableColumn
e3IpmRcmAc = _E3IpmRcmAc_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 7, 1, 5),
    _E3IpmRcmAc_Type()
)
e3IpmRcmAc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmRcmAc.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmRcmAc.setUnits("mA")
_E3IpmRcmDc_Type = MilliAmperes
_E3IpmRcmDc_Object = MibTableColumn
e3IpmRcmDc = _E3IpmRcmDc_Object(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 7, 1, 6),
    _E3IpmRcmDc_Type()
)
e3IpmRcmDc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e3IpmRcmDc.setStatus("current")
if mibBuilder.loadTexts:
    e3IpmRcmDc.setUnits("mA")
_E3IpmTraps_ObjectIdentity = ObjectIdentity
e3IpmTraps = _E3IpmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8)
)

# Managed Objects groups


# Notification objects

e3IpmCurrentCritLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 1)
)
e3IpmCurrentCritLow.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmMeter"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmIrms"))
)
if mibBuilder.loadTexts:
    e3IpmCurrentCritLow.setStatus(
        "current"
    )

e3IpmCurrentWarnLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 2)
)
e3IpmCurrentWarnLow.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmMeter"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmIrms"))
)
if mibBuilder.loadTexts:
    e3IpmCurrentWarnLow.setStatus(
        "current"
    )

e3IpmCurrentNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 3)
)
e3IpmCurrentNormal.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmMeter"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmIrms"))
)
if mibBuilder.loadTexts:
    e3IpmCurrentNormal.setStatus(
        "current"
    )

e3IpmCurrentWarnHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 4)
)
e3IpmCurrentWarnHigh.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmMeter"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmIrms"))
)
if mibBuilder.loadTexts:
    e3IpmCurrentWarnHigh.setStatus(
        "current"
    )

e3IpmCurrentCritHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 5)
)
e3IpmCurrentCritHigh.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmMeter"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmIrms"))
)
if mibBuilder.loadTexts:
    e3IpmCurrentCritHigh.setStatus(
        "current"
    )

e3IpmTempCritLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 6)
)
e3IpmTempCritLow.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorTemperatureCelsius"))
)
if mibBuilder.loadTexts:
    e3IpmTempCritLow.setStatus(
        "current"
    )

e3IpmTempWarnLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 7)
)
e3IpmTempWarnLow.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorTemperatureCelsius"))
)
if mibBuilder.loadTexts:
    e3IpmTempWarnLow.setStatus(
        "current"
    )

e3IpmTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 8)
)
e3IpmTempNormal.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorTemperatureCelsius"))
)
if mibBuilder.loadTexts:
    e3IpmTempNormal.setStatus(
        "current"
    )

e3IpmTempWarnHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 9)
)
e3IpmTempWarnHigh.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorTemperatureCelsius"))
)
if mibBuilder.loadTexts:
    e3IpmTempWarnHigh.setStatus(
        "current"
    )

e3IpmTempCritHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 10)
)
e3IpmTempCritHigh.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorTemperatureCelsius"))
)
if mibBuilder.loadTexts:
    e3IpmTempCritHigh.setStatus(
        "current"
    )

e3IpmRHCritLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 11)
)
e3IpmRHCritLow.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorHumidity"))
)
if mibBuilder.loadTexts:
    e3IpmRHCritLow.setStatus(
        "current"
    )

e3IpmRHWarnLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 12)
)
e3IpmRHWarnLow.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorHumidity"))
)
if mibBuilder.loadTexts:
    e3IpmRHWarnLow.setStatus(
        "current"
    )

e3IpmRHNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 13)
)
e3IpmRHNormal.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorHumidity"))
)
if mibBuilder.loadTexts:
    e3IpmRHNormal.setStatus(
        "current"
    )

e3IpmRHWarnHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 14)
)
e3IpmRHWarnHigh.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorHumidity"))
)
if mibBuilder.loadTexts:
    e3IpmRHWarnHigh.setStatus(
        "current"
    )

e3IpmRHCritHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 15)
)
e3IpmRHCritHigh.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmSensorHumidity"))
)
if mibBuilder.loadTexts:
    e3IpmRHCritHigh.setStatus(
        "current"
    )

e3IpmRcmAcNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 16)
)
e3IpmRcmAcNormal.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmChannel"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmAc"))
)
if mibBuilder.loadTexts:
    e3IpmRcmAcNormal.setStatus(
        "current"
    )

e3IpmRcmAcCritHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 17)
)
e3IpmRcmAcCritHigh.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmChannel"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmAc"))
)
if mibBuilder.loadTexts:
    e3IpmRcmAcCritHigh.setStatus(
        "current"
    )

e3IpmRcmDcNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 18)
)
e3IpmRcmDcNormal.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmChannel"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmDc"))
)
if mibBuilder.loadTexts:
    e3IpmRcmDcNormal.setStatus(
        "current"
    )

e3IpmRcmDcCritHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 21695, 1, 10, 8, 19)
)
e3IpmRcmDcCritHigh.setObjects(
      *(("NETTRACK-E3METER-SNMP-MIB", "e3IpmInfoSerial"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmChannel"),
        ("NETTRACK-E3METER-SNMP-MIB", "e3IpmRcmDc"))
)
if mibBuilder.loadTexts:
    e3IpmRcmDcCritHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETTRACK-E3METER-SNMP-MIB",
    **{"Watts": Watts,
       "VoltAmpereReactives": VoltAmpereReactives,
       "VoltAmperes": VoltAmperes,
       "WattHours": WattHours,
       "VoltAmpereReactiveHours": VoltAmpereReactiveHours,
       "VoltAmpereHours": VoltAmpereHours,
       "MilliAmperes": MilliAmperes,
       "MilliVolts": MilliVolts,
       "MilliHertz": MilliHertz,
       "DeciDegreesCelsius": DeciDegreesCelsius,
       "Permil": Permil,
       "nettrack": nettrack,
       "public": public,
       "e3Mib": e3Mib,
       "e3Ipm": e3Ipm,
       "e3IpmInfo": e3IpmInfo,
       "e3IpmInfoSerial": e3IpmInfoSerial,
       "e3IpmInfoModel": e3IpmInfoModel,
       "e3IpmInfoHWVersion": e3IpmInfoHWVersion,
       "e3IpmInfoFWVersion": e3IpmInfoFWVersion,
       "e3IpmInfoMeters": e3IpmInfoMeters,
       "e3IpmMeterTable": e3IpmMeterTable,
       "e3IpmMeterEntry": e3IpmMeterEntry,
       "e3IpmMeter": e3IpmMeter,
       "e3IpmEnergyP": e3IpmEnergyP,
       "e3IpmEnergyQ": e3IpmEnergyQ,
       "e3IpmEnergyS": e3IpmEnergyS,
       "e3IpmPowerP": e3IpmPowerP,
       "e3IpmPowerQ": e3IpmPowerQ,
       "e3IpmPowerS": e3IpmPowerS,
       "e3IpmUrms": e3IpmUrms,
       "e3IpmIrms": e3IpmIrms,
       "e3IpmFrequency": e3IpmFrequency,
       "e3IpmChannelName": e3IpmChannelName,
       "e3IpmChannelType": e3IpmChannelType,
       "e3IpmSensorTable": e3IpmSensorTable,
       "e3IpmSensorEntry": e3IpmSensorEntry,
       "e3IpmSensor": e3IpmSensor,
       "e3IpmSensorType": e3IpmSensorType,
       "e3IpmSensorVersion": e3IpmSensorVersion,
       "e3IpmSensorTemperatureCelsius": e3IpmSensorTemperatureCelsius,
       "e3IpmSensorHumidity": e3IpmSensorHumidity,
       "e3IpmPGroupTable": e3IpmPGroupTable,
       "e3IpmPGroupEntry": e3IpmPGroupEntry,
       "e3IpmPGroup": e3IpmPGroup,
       "e3IpmPGName": e3IpmPGName,
       "e3IpmPGMembers": e3IpmPGMembers,
       "e3IpmPGEnergyP": e3IpmPGEnergyP,
       "e3IpmPGEnergyQ": e3IpmPGEnergyQ,
       "e3IpmPGEnergyS": e3IpmPGEnergyS,
       "e3IpmPGPowerP": e3IpmPGPowerP,
       "e3IpmPGPowerQ": e3IpmPGPowerQ,
       "e3IpmPGPowerS": e3IpmPGPowerS,
       "e3IpmPGIrms": e3IpmPGIrms,
       "e3IpmUGroupTable": e3IpmUGroupTable,
       "e3IpmUGroupEntry": e3IpmUGroupEntry,
       "e3IpmUGroup": e3IpmUGroup,
       "e3IpmUGName": e3IpmUGName,
       "e3IpmUGMembers": e3IpmUGMembers,
       "e3IpmUGEnergyP": e3IpmUGEnergyP,
       "e3IpmUGEnergyQ": e3IpmUGEnergyQ,
       "e3IpmUGEnergyS": e3IpmUGEnergyS,
       "e3IpmUGPowerP": e3IpmUGPowerP,
       "e3IpmUGPowerQ": e3IpmUGPowerQ,
       "e3IpmUGPowerS": e3IpmUGPowerS,
       "e3IpmUGIrms": e3IpmUGIrms,
       "e3IpmAlarmTable": e3IpmAlarmTable,
       "e3IpmAlarmTableEntry": e3IpmAlarmTableEntry,
       "e3IpmAlarmIndex": e3IpmAlarmIndex,
       "e3IpmAlarmState": e3IpmAlarmState,
       "e3IpmAlarmCritLowSet": e3IpmAlarmCritLowSet,
       "e3IpmAlarmCritLow": e3IpmAlarmCritLow,
       "e3IpmAlarmWarnLowSet": e3IpmAlarmWarnLowSet,
       "e3IpmAlarmWarnLow": e3IpmAlarmWarnLow,
       "e3IpmAlarmWarnHighSet": e3IpmAlarmWarnHighSet,
       "e3IpmAlarmWarnHigh": e3IpmAlarmWarnHigh,
       "e3IpmAlarmCritHighSet": e3IpmAlarmCritHighSet,
       "e3IpmAlarmCritHigh": e3IpmAlarmCritHigh,
       "e3IpmRcmTable": e3IpmRcmTable,
       "e3IpmRcmTableEntry": e3IpmRcmTableEntry,
       "e3IpmRcmChannel": e3IpmRcmChannel,
       "e3IpmRcmAcLimit": e3IpmRcmAcLimit,
       "e3IpmRcmDcLimit": e3IpmRcmDcLimit,
       "e3IpmRcmStatus": e3IpmRcmStatus,
       "e3IpmRcmAc": e3IpmRcmAc,
       "e3IpmRcmDc": e3IpmRcmDc,
       "e3IpmTraps": e3IpmTraps,
       "e3IpmCurrentCritLow": e3IpmCurrentCritLow,
       "e3IpmCurrentWarnLow": e3IpmCurrentWarnLow,
       "e3IpmCurrentNormal": e3IpmCurrentNormal,
       "e3IpmCurrentWarnHigh": e3IpmCurrentWarnHigh,
       "e3IpmCurrentCritHigh": e3IpmCurrentCritHigh,
       "e3IpmTempCritLow": e3IpmTempCritLow,
       "e3IpmTempWarnLow": e3IpmTempWarnLow,
       "e3IpmTempNormal": e3IpmTempNormal,
       "e3IpmTempWarnHigh": e3IpmTempWarnHigh,
       "e3IpmTempCritHigh": e3IpmTempCritHigh,
       "e3IpmRHCritLow": e3IpmRHCritLow,
       "e3IpmRHWarnLow": e3IpmRHWarnLow,
       "e3IpmRHNormal": e3IpmRHNormal,
       "e3IpmRHWarnHigh": e3IpmRHWarnHigh,
       "e3IpmRHCritHigh": e3IpmRHCritHigh,
       "e3IpmRcmAcNormal": e3IpmRcmAcNormal,
       "e3IpmRcmAcCritHigh": e3IpmRcmAcCritHigh,
       "e3IpmRcmDcNormal": e3IpmRcmDcNormal,
       "e3IpmRcmDcCritHigh": e3IpmRcmDcCritHigh}
)
