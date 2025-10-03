# SNMP MIB module (TERACOM-TCW241-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teracom\TERACOM-TCW241-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:10 2025
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    snmpMIB.setRevisions(
        ("2019-04-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CONTROLLED(TextualConvention, Integer32):
    status = "current"
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("sensor11", 1),
          ("sensor12", 2),
          ("sensor21", 3),
          ("sensor22", 4),
          ("sensor31", 5),
          ("sensor32", 6),
          ("sensor41", 7),
          ("sensor42", 8),
          ("sensor51", 9),
          ("sensor52", 10),
          ("sensor61", 11),
          ("sensor62", 12),
          ("sensor71", 13),
          ("sensor72", 14),
          ("sensor81", 15),
          ("sensor82", 16),
          ("analog1", 17),
          ("analog2", 18),
          ("analog3", 19),
          ("analog4", 20),
          ("digital1", 21),
          ("digital2", 22),
          ("digital3", 23),
          ("digital4", 24),
          ("anyAlarm", 25),
          ("anySensor", 26),
          ("anyAnalog", 27),
          ("anyDigital", 28),
          ("func1", 29),
          ("func2", 30),
          ("func3", 31),
          ("func4", 32),
          ("shedule1", 33),
          ("shedule2", 34),
          ("shedule3", 35),
          ("shedule4", 36),
          ("virtual1", 37),
          ("virtual2", 38),
          ("virtual3", 39),
          ("virtual4", 40))
    )



class RELAYACTION(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("turnon", 0),
          ("pulse", 2))
    )



class VIRTUALPARENT(TextualConvention, Integer32):
    status = "current"
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
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sensor11", 1),
          ("sensor12", 2),
          ("sensor21", 3),
          ("sensor22", 4),
          ("sensor31", 5),
          ("sensor32", 6),
          ("sensor41", 7),
          ("sensor42", 8),
          ("sensor51", 9),
          ("sensor52", 10),
          ("sensor61", 11),
          ("sensor62", 12),
          ("sensor71", 13),
          ("sensor72", 14),
          ("sensor81", 15),
          ("sensor82", 16),
          ("analog1", 17),
          ("analog2", 18),
          ("analog3", 19),
          ("analog4", 20))
    )



class SensorId(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class AnalogValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class SensorValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class VirtualValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-3"


class ALARMSTATUS(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_Teracom_ObjectIdentity = ObjectIdentity
teracom = _Teracom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783)
)
_Tcw241_ObjectIdentity = ObjectIdentity
tcw241 = _Tcw241_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3)
)
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_DateTime_Type = DateAndTime
_DateTime_Object = MibScalar
dateTime = _DateTime_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 1, 3),
    _DateTime_Type()
)
dateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateTime.setStatus("current")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 1)
)
_DeviceID_Type = MacAddress
_DeviceID_Object = MibScalar
deviceID = _DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 1, 1),
    _DeviceID_Type()
)
deviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceID.setStatus("current")


class _HostName_Type(DisplayString):
    """Custom type hostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_HostName_Type.__name__ = "DisplayString"
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_DeviceIP_Type = IpAddress
_DeviceIP_Object = MibScalar
deviceIP = _DeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 1, 3),
    _DeviceIP_Type()
)
deviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIP.setStatus("current")
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2)
)
_SensorsSetup_ObjectIdentity = ObjectIdentity
sensorsSetup = _SensorsSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1)
)
_Sensor1setup_ObjectIdentity = ObjectIdentity
sensor1setup = _Sensor1setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1)
)


class _S1description_Type(DisplayString):
    """Custom type s1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S1description_Type.__name__ = "DisplayString"
_S1description_Object = MibScalar
s1description = _S1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 1),
    _S1description_Type()
)
s1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s1description.setStatus("current")
_Sensor11setup_ObjectIdentity = ObjectIdentity
sensor11setup = _Sensor11setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 2)
)
_S11MAXInt_Type = SensorValue
_S11MAXInt_Object = MibScalar
s11MAXInt = _S11MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 2, 1),
    _S11MAXInt_Type()
)
s11MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11MAXInt.setStatus("current")
_S11MINInt_Type = SensorValue
_S11MINInt_Object = MibScalar
s11MINInt = _S11MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 2, 2),
    _S11MINInt_Type()
)
s11MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11MINInt.setStatus("current")
_S11HYSTInt_Type = SensorValue
_S11HYSTInt_Object = MibScalar
s11HYSTInt = _S11HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 2, 3),
    _S11HYSTInt_Type()
)
s11HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11HYSTInt.setStatus("current")
_Sensor12setup_ObjectIdentity = ObjectIdentity
sensor12setup = _Sensor12setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 3)
)
_S12MAXInt_Type = SensorValue
_S12MAXInt_Object = MibScalar
s12MAXInt = _S12MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 3, 1),
    _S12MAXInt_Type()
)
s12MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12MAXInt.setStatus("current")
_S12MINInt_Type = SensorValue
_S12MINInt_Object = MibScalar
s12MINInt = _S12MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 3, 2),
    _S12MINInt_Type()
)
s12MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12MINInt.setStatus("current")
_S12HYSTInt_Type = SensorValue
_S12HYSTInt_Object = MibScalar
s12HYSTInt = _S12HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 1, 3, 3),
    _S12HYSTInt_Type()
)
s12HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12HYSTInt.setStatus("current")
_Sensor2setup_ObjectIdentity = ObjectIdentity
sensor2setup = _Sensor2setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2)
)


class _S2description_Type(DisplayString):
    """Custom type s2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S2description_Type.__name__ = "DisplayString"
_S2description_Object = MibScalar
s2description = _S2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 1),
    _S2description_Type()
)
s2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s2description.setStatus("current")
_Sensor21setup_ObjectIdentity = ObjectIdentity
sensor21setup = _Sensor21setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 2)
)
_S21MAXInt_Type = SensorValue
_S21MAXInt_Object = MibScalar
s21MAXInt = _S21MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 2, 1),
    _S21MAXInt_Type()
)
s21MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21MAXInt.setStatus("current")
_S21MINInt_Type = SensorValue
_S21MINInt_Object = MibScalar
s21MINInt = _S21MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 2, 2),
    _S21MINInt_Type()
)
s21MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21MINInt.setStatus("current")
_S21HYSTInt_Type = SensorValue
_S21HYSTInt_Object = MibScalar
s21HYSTInt = _S21HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 2, 3),
    _S21HYSTInt_Type()
)
s21HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21HYSTInt.setStatus("current")
_Sensor22setup_ObjectIdentity = ObjectIdentity
sensor22setup = _Sensor22setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 3)
)
_S22MAXInt_Type = SensorValue
_S22MAXInt_Object = MibScalar
s22MAXInt = _S22MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 3, 1),
    _S22MAXInt_Type()
)
s22MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22MAXInt.setStatus("current")
_S22MINInt_Type = SensorValue
_S22MINInt_Object = MibScalar
s22MINInt = _S22MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 3, 2),
    _S22MINInt_Type()
)
s22MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22MINInt.setStatus("current")
_S22HYSTInt_Type = SensorValue
_S22HYSTInt_Object = MibScalar
s22HYSTInt = _S22HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 2, 3, 3),
    _S22HYSTInt_Type()
)
s22HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22HYSTInt.setStatus("current")
_Sensor3setup_ObjectIdentity = ObjectIdentity
sensor3setup = _Sensor3setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3)
)


class _S3description_Type(DisplayString):
    """Custom type s3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S3description_Type.__name__ = "DisplayString"
_S3description_Object = MibScalar
s3description = _S3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 1),
    _S3description_Type()
)
s3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3description.setStatus("current")
_Sensor31setup_ObjectIdentity = ObjectIdentity
sensor31setup = _Sensor31setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 2)
)
_S31MAXInt_Type = SensorValue
_S31MAXInt_Object = MibScalar
s31MAXInt = _S31MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 2, 1),
    _S31MAXInt_Type()
)
s31MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31MAXInt.setStatus("current")
_S31MINInt_Type = SensorValue
_S31MINInt_Object = MibScalar
s31MINInt = _S31MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 2, 2),
    _S31MINInt_Type()
)
s31MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31MINInt.setStatus("current")
_S31HYSTInt_Type = SensorValue
_S31HYSTInt_Object = MibScalar
s31HYSTInt = _S31HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 2, 3),
    _S31HYSTInt_Type()
)
s31HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31HYSTInt.setStatus("current")
_Sensor32setup_ObjectIdentity = ObjectIdentity
sensor32setup = _Sensor32setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 3)
)
_S32MAXInt_Type = SensorValue
_S32MAXInt_Object = MibScalar
s32MAXInt = _S32MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 3, 1),
    _S32MAXInt_Type()
)
s32MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32MAXInt.setStatus("current")
_S32MINInt_Type = SensorValue
_S32MINInt_Object = MibScalar
s32MINInt = _S32MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 3, 2),
    _S32MINInt_Type()
)
s32MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32MINInt.setStatus("current")
_S32HYSTInt_Type = SensorValue
_S32HYSTInt_Object = MibScalar
s32HYSTInt = _S32HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 3, 3, 3),
    _S32HYSTInt_Type()
)
s32HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32HYSTInt.setStatus("current")
_Sensor4setup_ObjectIdentity = ObjectIdentity
sensor4setup = _Sensor4setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4)
)


class _S4description_Type(DisplayString):
    """Custom type s4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S4description_Type.__name__ = "DisplayString"
_S4description_Object = MibScalar
s4description = _S4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 1),
    _S4description_Type()
)
s4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s4description.setStatus("current")
_Sensor41setup_ObjectIdentity = ObjectIdentity
sensor41setup = _Sensor41setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 2)
)
_S41MAXInt_Type = SensorValue
_S41MAXInt_Object = MibScalar
s41MAXInt = _S41MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 2, 1),
    _S41MAXInt_Type()
)
s41MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41MAXInt.setStatus("current")
_S41MINInt_Type = SensorValue
_S41MINInt_Object = MibScalar
s41MINInt = _S41MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 2, 2),
    _S41MINInt_Type()
)
s41MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41MINInt.setStatus("current")
_S41HYSTInt_Type = SensorValue
_S41HYSTInt_Object = MibScalar
s41HYSTInt = _S41HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 2, 3),
    _S41HYSTInt_Type()
)
s41HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41HYSTInt.setStatus("current")
_Sensor42setup_ObjectIdentity = ObjectIdentity
sensor42setup = _Sensor42setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 3)
)
_S42MAXInt_Type = SensorValue
_S42MAXInt_Object = MibScalar
s42MAXInt = _S42MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 3, 1),
    _S42MAXInt_Type()
)
s42MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42MAXInt.setStatus("current")
_S42MINInt_Type = SensorValue
_S42MINInt_Object = MibScalar
s42MINInt = _S42MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 3, 2),
    _S42MINInt_Type()
)
s42MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42MINInt.setStatus("current")
_S42HYSTInt_Type = SensorValue
_S42HYSTInt_Object = MibScalar
s42HYSTInt = _S42HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 4, 3, 3),
    _S42HYSTInt_Type()
)
s42HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42HYSTInt.setStatus("current")
_Sensor5setup_ObjectIdentity = ObjectIdentity
sensor5setup = _Sensor5setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5)
)


class _S5description_Type(DisplayString):
    """Custom type s5description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S5description_Type.__name__ = "DisplayString"
_S5description_Object = MibScalar
s5description = _S5description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 1),
    _S5description_Type()
)
s5description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5description.setStatus("current")
_Sensor51setup_ObjectIdentity = ObjectIdentity
sensor51setup = _Sensor51setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 2)
)
_S51MAXInt_Type = SensorValue
_S51MAXInt_Object = MibScalar
s51MAXInt = _S51MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 2, 1),
    _S51MAXInt_Type()
)
s51MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51MAXInt.setStatus("current")
_S51MINInt_Type = SensorValue
_S51MINInt_Object = MibScalar
s51MINInt = _S51MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 2, 2),
    _S51MINInt_Type()
)
s51MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51MINInt.setStatus("current")
_S51HYSTInt_Type = SensorValue
_S51HYSTInt_Object = MibScalar
s51HYSTInt = _S51HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 2, 3),
    _S51HYSTInt_Type()
)
s51HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51HYSTInt.setStatus("current")
_Sensor52setup_ObjectIdentity = ObjectIdentity
sensor52setup = _Sensor52setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 3)
)
_S52MAXInt_Type = SensorValue
_S52MAXInt_Object = MibScalar
s52MAXInt = _S52MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 3, 1),
    _S52MAXInt_Type()
)
s52MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52MAXInt.setStatus("current")
_S52MINInt_Type = SensorValue
_S52MINInt_Object = MibScalar
s52MINInt = _S52MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 3, 2),
    _S52MINInt_Type()
)
s52MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52MINInt.setStatus("current")
_S52HYSTInt_Type = SensorValue
_S52HYSTInt_Object = MibScalar
s52HYSTInt = _S52HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 5, 3, 3),
    _S52HYSTInt_Type()
)
s52HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52HYSTInt.setStatus("current")
_Sensor6setup_ObjectIdentity = ObjectIdentity
sensor6setup = _Sensor6setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6)
)


class _S6description_Type(DisplayString):
    """Custom type s6description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S6description_Type.__name__ = "DisplayString"
_S6description_Object = MibScalar
s6description = _S6description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 1),
    _S6description_Type()
)
s6description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s6description.setStatus("current")
_Sensor61setup_ObjectIdentity = ObjectIdentity
sensor61setup = _Sensor61setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 2)
)
_S61MAXInt_Type = SensorValue
_S61MAXInt_Object = MibScalar
s61MAXInt = _S61MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 2, 1),
    _S61MAXInt_Type()
)
s61MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61MAXInt.setStatus("current")
_S61MINInt_Type = SensorValue
_S61MINInt_Object = MibScalar
s61MINInt = _S61MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 2, 2),
    _S61MINInt_Type()
)
s61MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61MINInt.setStatus("current")
_S61HYSTInt_Type = SensorValue
_S61HYSTInt_Object = MibScalar
s61HYSTInt = _S61HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 2, 3),
    _S61HYSTInt_Type()
)
s61HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61HYSTInt.setStatus("current")
_Sensor62setup_ObjectIdentity = ObjectIdentity
sensor62setup = _Sensor62setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 3)
)
_S62MAXInt_Type = SensorValue
_S62MAXInt_Object = MibScalar
s62MAXInt = _S62MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 3, 1),
    _S62MAXInt_Type()
)
s62MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62MAXInt.setStatus("current")
_S62MINInt_Type = SensorValue
_S62MINInt_Object = MibScalar
s62MINInt = _S62MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 3, 2),
    _S62MINInt_Type()
)
s62MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62MINInt.setStatus("current")
_S62HYSTInt_Type = SensorValue
_S62HYSTInt_Object = MibScalar
s62HYSTInt = _S62HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 6, 3, 3),
    _S62HYSTInt_Type()
)
s62HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62HYSTInt.setStatus("current")
_Sensor7setup_ObjectIdentity = ObjectIdentity
sensor7setup = _Sensor7setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7)
)


class _S7description_Type(DisplayString):
    """Custom type s7description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S7description_Type.__name__ = "DisplayString"
_S7description_Object = MibScalar
s7description = _S7description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 1),
    _S7description_Type()
)
s7description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s7description.setStatus("current")
_Sensor71setup_ObjectIdentity = ObjectIdentity
sensor71setup = _Sensor71setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 2)
)
_S71MAXInt_Type = SensorValue
_S71MAXInt_Object = MibScalar
s71MAXInt = _S71MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 2, 1),
    _S71MAXInt_Type()
)
s71MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71MAXInt.setStatus("current")
_S71MINInt_Type = SensorValue
_S71MINInt_Object = MibScalar
s71MINInt = _S71MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 2, 2),
    _S71MINInt_Type()
)
s71MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71MINInt.setStatus("current")
_S71HYSTInt_Type = SensorValue
_S71HYSTInt_Object = MibScalar
s71HYSTInt = _S71HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 2, 3),
    _S71HYSTInt_Type()
)
s71HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71HYSTInt.setStatus("current")
_Sensor72setup_ObjectIdentity = ObjectIdentity
sensor72setup = _Sensor72setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 3)
)
_S72MAXInt_Type = SensorValue
_S72MAXInt_Object = MibScalar
s72MAXInt = _S72MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 3, 1),
    _S72MAXInt_Type()
)
s72MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72MAXInt.setStatus("current")
_S72MINInt_Type = SensorValue
_S72MINInt_Object = MibScalar
s72MINInt = _S72MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 3, 2),
    _S72MINInt_Type()
)
s72MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72MINInt.setStatus("current")
_S72HYSTInt_Type = SensorValue
_S72HYSTInt_Object = MibScalar
s72HYSTInt = _S72HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 7, 3, 3),
    _S72HYSTInt_Type()
)
s72HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72HYSTInt.setStatus("current")
_Sensor8setup_ObjectIdentity = ObjectIdentity
sensor8setup = _Sensor8setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8)
)


class _S8description_Type(DisplayString):
    """Custom type s8description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_S8description_Type.__name__ = "DisplayString"
_S8description_Object = MibScalar
s8description = _S8description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 1),
    _S8description_Type()
)
s8description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s8description.setStatus("current")
_Sensor81setup_ObjectIdentity = ObjectIdentity
sensor81setup = _Sensor81setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 2)
)
_S81MAXInt_Type = SensorValue
_S81MAXInt_Object = MibScalar
s81MAXInt = _S81MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 2, 1),
    _S81MAXInt_Type()
)
s81MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81MAXInt.setStatus("current")
_S81MINInt_Type = SensorValue
_S81MINInt_Object = MibScalar
s81MINInt = _S81MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 2, 2),
    _S81MINInt_Type()
)
s81MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81MINInt.setStatus("current")
_S81HYSTInt_Type = SensorValue
_S81HYSTInt_Object = MibScalar
s81HYSTInt = _S81HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 2, 3),
    _S81HYSTInt_Type()
)
s81HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81HYSTInt.setStatus("current")
_Sensor82setup_ObjectIdentity = ObjectIdentity
sensor82setup = _Sensor82setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 3)
)
_S82MAXInt_Type = SensorValue
_S82MAXInt_Object = MibScalar
s82MAXInt = _S82MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 3, 1),
    _S82MAXInt_Type()
)
s82MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82MAXInt.setStatus("current")
_S82MINInt_Type = SensorValue
_S82MINInt_Object = MibScalar
s82MINInt = _S82MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 3, 2),
    _S82MINInt_Type()
)
s82MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82MINInt.setStatus("current")
_S82HYSTInt_Type = SensorValue
_S82HYSTInt_Object = MibScalar
s82HYSTInt = _S82HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 1, 8, 3, 3),
    _S82HYSTInt_Type()
)
s82HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82HYSTInt.setStatus("current")
_AnalogSetup_ObjectIdentity = ObjectIdentity
analogSetup = _AnalogSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2)
)
_Analog1setup_ObjectIdentity = ObjectIdentity
analog1setup = _Analog1setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 1)
)


class _Voltage1description_Type(DisplayString):
    """Custom type voltage1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Voltage1description_Type.__name__ = "DisplayString"
_Voltage1description_Object = MibScalar
voltage1description = _Voltage1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 1, 1),
    _Voltage1description_Type()
)
voltage1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage1description.setStatus("current")
_Voltage1max_Type = AnalogValue
_Voltage1max_Object = MibScalar
voltage1max = _Voltage1max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 1, 2),
    _Voltage1max_Type()
)
voltage1max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage1max.setStatus("current")
_Voltage1min_Type = AnalogValue
_Voltage1min_Object = MibScalar
voltage1min = _Voltage1min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 1, 3),
    _Voltage1min_Type()
)
voltage1min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage1min.setStatus("current")
_Voltage1hyst_Type = AnalogValue
_Voltage1hyst_Object = MibScalar
voltage1hyst = _Voltage1hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 1, 4),
    _Voltage1hyst_Type()
)
voltage1hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage1hyst.setStatus("current")
_Analog2setup_ObjectIdentity = ObjectIdentity
analog2setup = _Analog2setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 2)
)


class _Voltage2description_Type(DisplayString):
    """Custom type voltage2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Voltage2description_Type.__name__ = "DisplayString"
_Voltage2description_Object = MibScalar
voltage2description = _Voltage2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 2, 1),
    _Voltage2description_Type()
)
voltage2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage2description.setStatus("current")
_Voltage2max_Type = AnalogValue
_Voltage2max_Object = MibScalar
voltage2max = _Voltage2max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 2, 2),
    _Voltage2max_Type()
)
voltage2max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage2max.setStatus("current")
_Voltage2min_Type = AnalogValue
_Voltage2min_Object = MibScalar
voltage2min = _Voltage2min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 2, 3),
    _Voltage2min_Type()
)
voltage2min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage2min.setStatus("current")
_Voltage2hyst_Type = AnalogValue
_Voltage2hyst_Object = MibScalar
voltage2hyst = _Voltage2hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 2, 4),
    _Voltage2hyst_Type()
)
voltage2hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage2hyst.setStatus("current")
_Analog3setup_ObjectIdentity = ObjectIdentity
analog3setup = _Analog3setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 3)
)


class _Voltage3description_Type(DisplayString):
    """Custom type voltage3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Voltage3description_Type.__name__ = "DisplayString"
_Voltage3description_Object = MibScalar
voltage3description = _Voltage3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 3, 1),
    _Voltage3description_Type()
)
voltage3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage3description.setStatus("current")
_Voltage3max_Type = AnalogValue
_Voltage3max_Object = MibScalar
voltage3max = _Voltage3max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 3, 2),
    _Voltage3max_Type()
)
voltage3max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage3max.setStatus("current")
_Voltage3min_Type = AnalogValue
_Voltage3min_Object = MibScalar
voltage3min = _Voltage3min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 3, 3),
    _Voltage3min_Type()
)
voltage3min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage3min.setStatus("current")
_Voltage3hyst_Type = AnalogValue
_Voltage3hyst_Object = MibScalar
voltage3hyst = _Voltage3hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 3, 4),
    _Voltage3hyst_Type()
)
voltage3hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage3hyst.setStatus("current")
_Analog4setup_ObjectIdentity = ObjectIdentity
analog4setup = _Analog4setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 4)
)


class _Voltage4description_Type(DisplayString):
    """Custom type voltage4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Voltage4description_Type.__name__ = "DisplayString"
_Voltage4description_Object = MibScalar
voltage4description = _Voltage4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 4, 1),
    _Voltage4description_Type()
)
voltage4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage4description.setStatus("current")
_Voltage4max_Type = AnalogValue
_Voltage4max_Object = MibScalar
voltage4max = _Voltage4max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 4, 2),
    _Voltage4max_Type()
)
voltage4max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage4max.setStatus("current")
_Voltage4min_Type = AnalogValue
_Voltage4min_Object = MibScalar
voltage4min = _Voltage4min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 4, 3),
    _Voltage4min_Type()
)
voltage4min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage4min.setStatus("current")
_Voltage4hyst_Type = AnalogValue
_Voltage4hyst_Object = MibScalar
voltage4hyst = _Voltage4hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 2, 4, 4),
    _Voltage4hyst_Type()
)
voltage4hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltage4hyst.setStatus("current")
_DigitalSetup_ObjectIdentity = ObjectIdentity
digitalSetup = _DigitalSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 3)
)


class _DigitalInput1description_Type(DisplayString):
    """Custom type digitalInput1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DigitalInput1description_Type.__name__ = "DisplayString"
_DigitalInput1description_Object = MibScalar
digitalInput1description = _DigitalInput1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 3, 1),
    _DigitalInput1description_Type()
)
digitalInput1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput1description.setStatus("current")


class _DigitalInput2description_Type(DisplayString):
    """Custom type digitalInput2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DigitalInput2description_Type.__name__ = "DisplayString"
_DigitalInput2description_Object = MibScalar
digitalInput2description = _DigitalInput2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 3, 2),
    _DigitalInput2description_Type()
)
digitalInput2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput2description.setStatus("current")


class _DigitalInput3description_Type(DisplayString):
    """Custom type digitalInput3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DigitalInput3description_Type.__name__ = "DisplayString"
_DigitalInput3description_Object = MibScalar
digitalInput3description = _DigitalInput3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 3, 3),
    _DigitalInput3description_Type()
)
digitalInput3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput3description.setStatus("current")


class _DigitalInput4description_Type(DisplayString):
    """Custom type digitalInput4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_DigitalInput4description_Type.__name__ = "DisplayString"
_DigitalInput4description_Object = MibScalar
digitalInput4description = _DigitalInput4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 3, 4),
    _DigitalInput4description_Type()
)
digitalInput4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInput4description.setStatus("current")
_RelaysSetup_ObjectIdentity = ObjectIdentity
relaysSetup = _RelaysSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4)
)
_Relay1setup_ObjectIdentity = ObjectIdentity
relay1setup = _Relay1setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 1)
)


class _Relay1description_Type(DisplayString):
    """Custom type relay1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Relay1description_Type.__name__ = "DisplayString"
_Relay1description_Object = MibScalar
relay1description = _Relay1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 1, 1),
    _Relay1description_Type()
)
relay1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1description.setStatus("current")


class _Relay1pulseWidth_Type(Integer32):
    """Custom type relay1pulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Relay1pulseWidth_Type.__name__ = "Integer32"
_Relay1pulseWidth_Object = MibScalar
relay1pulseWidth = _Relay1pulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 1, 2),
    _Relay1pulseWidth_Type()
)
relay1pulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1pulseWidth.setStatus("current")
_Relay1controlledBy_Type = CONTROLLED
_Relay1controlledBy_Object = MibScalar
relay1controlledBy = _Relay1controlledBy_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 1, 3),
    _Relay1controlledBy_Type()
)
relay1controlledBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1controlledBy.setStatus("current")
_Relay1action_Type = RELAYACTION
_Relay1action_Object = MibScalar
relay1action = _Relay1action_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 1, 4),
    _Relay1action_Type()
)
relay1action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1action.setStatus("current")
_Relay2setup_ObjectIdentity = ObjectIdentity
relay2setup = _Relay2setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 2)
)


class _Relay2description_Type(DisplayString):
    """Custom type relay2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Relay2description_Type.__name__ = "DisplayString"
_Relay2description_Object = MibScalar
relay2description = _Relay2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 2, 1),
    _Relay2description_Type()
)
relay2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2description.setStatus("current")


class _Relay2pulseWidth_Type(Integer32):
    """Custom type relay2pulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Relay2pulseWidth_Type.__name__ = "Integer32"
_Relay2pulseWidth_Object = MibScalar
relay2pulseWidth = _Relay2pulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 2, 2),
    _Relay2pulseWidth_Type()
)
relay2pulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2pulseWidth.setStatus("current")
_Relay2controlledBy_Type = CONTROLLED
_Relay2controlledBy_Object = MibScalar
relay2controlledBy = _Relay2controlledBy_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 2, 3),
    _Relay2controlledBy_Type()
)
relay2controlledBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2controlledBy.setStatus("current")
_Relay2action_Type = RELAYACTION
_Relay2action_Object = MibScalar
relay2action = _Relay2action_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 2, 4),
    _Relay2action_Type()
)
relay2action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2action.setStatus("current")
_Relay3setup_ObjectIdentity = ObjectIdentity
relay3setup = _Relay3setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 3)
)


class _Relay3description_Type(DisplayString):
    """Custom type relay3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Relay3description_Type.__name__ = "DisplayString"
_Relay3description_Object = MibScalar
relay3description = _Relay3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 3, 1),
    _Relay3description_Type()
)
relay3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3description.setStatus("current")


class _Relay3pulseWidth_Type(Integer32):
    """Custom type relay3pulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Relay3pulseWidth_Type.__name__ = "Integer32"
_Relay3pulseWidth_Object = MibScalar
relay3pulseWidth = _Relay3pulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 3, 2),
    _Relay3pulseWidth_Type()
)
relay3pulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3pulseWidth.setStatus("current")
_Relay3controlledBy_Type = CONTROLLED
_Relay3controlledBy_Object = MibScalar
relay3controlledBy = _Relay3controlledBy_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 3, 3),
    _Relay3controlledBy_Type()
)
relay3controlledBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3controlledBy.setStatus("current")
_Relay3action_Type = RELAYACTION
_Relay3action_Object = MibScalar
relay3action = _Relay3action_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 3, 4),
    _Relay3action_Type()
)
relay3action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3action.setStatus("current")
_Relay4setup_ObjectIdentity = ObjectIdentity
relay4setup = _Relay4setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 4)
)


class _Relay4description_Type(DisplayString):
    """Custom type relay4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Relay4description_Type.__name__ = "DisplayString"
_Relay4description_Object = MibScalar
relay4description = _Relay4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 4, 1),
    _Relay4description_Type()
)
relay4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4description.setStatus("current")


class _Relay4pulseWidth_Type(Integer32):
    """Custom type relay4pulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Relay4pulseWidth_Type.__name__ = "Integer32"
_Relay4pulseWidth_Object = MibScalar
relay4pulseWidth = _Relay4pulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 4, 2),
    _Relay4pulseWidth_Type()
)
relay4pulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4pulseWidth.setStatus("current")
_Relay4controlledBy_Type = CONTROLLED
_Relay4controlledBy_Object = MibScalar
relay4controlledBy = _Relay4controlledBy_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 4, 3),
    _Relay4controlledBy_Type()
)
relay4controlledBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4controlledBy.setStatus("current")
_Relay4action_Type = RELAYACTION
_Relay4action_Object = MibScalar
relay4action = _Relay4action_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 4, 4, 4),
    _Relay4action_Type()
)
relay4action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4action.setStatus("current")
_VirtualSetup_ObjectIdentity = ObjectIdentity
virtualSetup = _VirtualSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5)
)
_Virtual1setup_ObjectIdentity = ObjectIdentity
virtual1setup = _Virtual1setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 1)
)


class _VirtualInput1description_Type(DisplayString):
    """Custom type virtualInput1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VirtualInput1description_Type.__name__ = "DisplayString"
_VirtualInput1description_Object = MibScalar
virtualInput1description = _VirtualInput1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 1, 1),
    _VirtualInput1description_Type()
)
virtualInput1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput1description.setStatus("current")
_VirtualInput1max_Type = VirtualValue
_VirtualInput1max_Object = MibScalar
virtualInput1max = _VirtualInput1max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 1, 2),
    _VirtualInput1max_Type()
)
virtualInput1max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput1max.setStatus("current")
_VirtualInput1min_Type = VirtualValue
_VirtualInput1min_Object = MibScalar
virtualInput1min = _VirtualInput1min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 1, 3),
    _VirtualInput1min_Type()
)
virtualInput1min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput1min.setStatus("current")
_VirtualInput1hyst_Type = VirtualValue
_VirtualInput1hyst_Object = MibScalar
virtualInput1hyst = _VirtualInput1hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 1, 4),
    _VirtualInput1hyst_Type()
)
virtualInput1hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput1hyst.setStatus("current")
_VirtualInput1Parent_Type = VIRTUALPARENT
_VirtualInput1Parent_Object = MibScalar
virtualInput1Parent = _VirtualInput1Parent_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 1, 5),
    _VirtualInput1Parent_Type()
)
virtualInput1Parent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput1Parent.setStatus("current")
_Virtual2setup_ObjectIdentity = ObjectIdentity
virtual2setup = _Virtual2setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 2)
)


class _VirtualInput2description_Type(DisplayString):
    """Custom type virtualInput2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VirtualInput2description_Type.__name__ = "DisplayString"
_VirtualInput2description_Object = MibScalar
virtualInput2description = _VirtualInput2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 2, 1),
    _VirtualInput2description_Type()
)
virtualInput2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput2description.setStatus("current")
_VirtualInput2max_Type = VirtualValue
_VirtualInput2max_Object = MibScalar
virtualInput2max = _VirtualInput2max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 2, 2),
    _VirtualInput2max_Type()
)
virtualInput2max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput2max.setStatus("current")
_VirtualInput2min_Type = VirtualValue
_VirtualInput2min_Object = MibScalar
virtualInput2min = _VirtualInput2min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 2, 3),
    _VirtualInput2min_Type()
)
virtualInput2min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput2min.setStatus("current")
_VirtualInput2hyst_Type = VirtualValue
_VirtualInput2hyst_Object = MibScalar
virtualInput2hyst = _VirtualInput2hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 2, 4),
    _VirtualInput2hyst_Type()
)
virtualInput2hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput2hyst.setStatus("current")
_VirtualInput2Parent_Type = VIRTUALPARENT
_VirtualInput2Parent_Object = MibScalar
virtualInput2Parent = _VirtualInput2Parent_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 2, 5),
    _VirtualInput2Parent_Type()
)
virtualInput2Parent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput2Parent.setStatus("current")
_Virtual3setup_ObjectIdentity = ObjectIdentity
virtual3setup = _Virtual3setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 3)
)


class _VirtualInput3description_Type(DisplayString):
    """Custom type virtualInput3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VirtualInput3description_Type.__name__ = "DisplayString"
_VirtualInput3description_Object = MibScalar
virtualInput3description = _VirtualInput3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 3, 1),
    _VirtualInput3description_Type()
)
virtualInput3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput3description.setStatus("current")
_VirtualInput3max_Type = VirtualValue
_VirtualInput3max_Object = MibScalar
virtualInput3max = _VirtualInput3max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 3, 2),
    _VirtualInput3max_Type()
)
virtualInput3max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput3max.setStatus("current")
_VirtualInput3min_Type = VirtualValue
_VirtualInput3min_Object = MibScalar
virtualInput3min = _VirtualInput3min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 3, 3),
    _VirtualInput3min_Type()
)
virtualInput3min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput3min.setStatus("current")
_VirtualInput3hyst_Type = VirtualValue
_VirtualInput3hyst_Object = MibScalar
virtualInput3hyst = _VirtualInput3hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 3, 4),
    _VirtualInput3hyst_Type()
)
virtualInput3hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput3hyst.setStatus("current")
_VirtualInput3Parent_Type = VIRTUALPARENT
_VirtualInput3Parent_Object = MibScalar
virtualInput3Parent = _VirtualInput3Parent_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 3, 5),
    _VirtualInput3Parent_Type()
)
virtualInput3Parent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput3Parent.setStatus("current")
_Virtual4setup_ObjectIdentity = ObjectIdentity
virtual4setup = _Virtual4setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 4)
)


class _VirtualInput4description_Type(DisplayString):
    """Custom type virtualInput4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_VirtualInput4description_Type.__name__ = "DisplayString"
_VirtualInput4description_Object = MibScalar
virtualInput4description = _VirtualInput4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 4, 1),
    _VirtualInput4description_Type()
)
virtualInput4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput4description.setStatus("current")
_VirtualInput4max_Type = VirtualValue
_VirtualInput4max_Object = MibScalar
virtualInput4max = _VirtualInput4max_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 4, 2),
    _VirtualInput4max_Type()
)
virtualInput4max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput4max.setStatus("current")
_VirtualInput4min_Type = VirtualValue
_VirtualInput4min_Object = MibScalar
virtualInput4min = _VirtualInput4min_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 4, 3),
    _VirtualInput4min_Type()
)
virtualInput4min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput4min.setStatus("current")
_VirtualInput4hyst_Type = VirtualValue
_VirtualInput4hyst_Object = MibScalar
virtualInput4hyst = _VirtualInput4hyst_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 4, 4),
    _VirtualInput4hyst_Type()
)
virtualInput4hyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput4hyst.setStatus("current")
_VirtualInput4Parent_Type = VIRTUALPARENT
_VirtualInput4Parent_Object = MibScalar
virtualInput4Parent = _VirtualInput4Parent_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2, 2, 5, 4, 5),
    _VirtualInput4Parent_Type()
)
virtualInput4Parent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    virtualInput4Parent.setStatus("current")
_MonitorNcontrol_ObjectIdentity = ObjectIdentity
monitorNcontrol = _MonitorNcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1)
)
_Sensor1_ObjectIdentity = ObjectIdentity
sensor1 = _Sensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 1)
)
_S11Int_Type = SensorValue
_S11Int_Object = MibScalar
s11Int = _S11Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 1, 1),
    _S11Int_Type()
)
s11Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s11Int.setStatus("current")
_S12Int_Type = SensorValue
_S12Int_Object = MibScalar
s12Int = _S12Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 1, 2),
    _S12Int_Type()
)
s12Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s12Int.setStatus("current")
_S1ID_Type = SensorId
_S1ID_Object = MibScalar
s1ID = _S1ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 1, 3),
    _S1ID_Type()
)
s1ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s1ID.setStatus("current")
_S1Alarm_ObjectIdentity = ObjectIdentity
s1Alarm = _S1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 1, 4)
)
_S11Al_Type = ALARMSTATUS
_S11Al_Object = MibScalar
s11Al = _S11Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 1, 4, 1),
    _S11Al_Type()
)
s11Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s11Al.setStatus("current")
_S12Al_Type = ALARMSTATUS
_S12Al_Object = MibScalar
s12Al = _S12Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 1, 4, 2),
    _S12Al_Type()
)
s12Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s12Al.setStatus("current")
_Sensor2_ObjectIdentity = ObjectIdentity
sensor2 = _Sensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 2)
)
_S21Int_Type = SensorValue
_S21Int_Object = MibScalar
s21Int = _S21Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 2, 1),
    _S21Int_Type()
)
s21Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s21Int.setStatus("current")
_S22Int_Type = SensorValue
_S22Int_Object = MibScalar
s22Int = _S22Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 2, 2),
    _S22Int_Type()
)
s22Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s22Int.setStatus("current")
_S2ID_Type = SensorId
_S2ID_Object = MibScalar
s2ID = _S2ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 2, 3),
    _S2ID_Type()
)
s2ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2ID.setStatus("current")
_S2Alarm_ObjectIdentity = ObjectIdentity
s2Alarm = _S2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 2, 4)
)
_S21Al_Type = ALARMSTATUS
_S21Al_Object = MibScalar
s21Al = _S21Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 2, 4, 1),
    _S21Al_Type()
)
s21Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s21Al.setStatus("current")
_S22Al_Type = ALARMSTATUS
_S22Al_Object = MibScalar
s22Al = _S22Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 2, 4, 2),
    _S22Al_Type()
)
s22Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s22Al.setStatus("current")
_Sensor3_ObjectIdentity = ObjectIdentity
sensor3 = _Sensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 3)
)
_S31Int_Type = SensorValue
_S31Int_Object = MibScalar
s31Int = _S31Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 3, 1),
    _S31Int_Type()
)
s31Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s31Int.setStatus("current")
_S32Int_Type = SensorValue
_S32Int_Object = MibScalar
s32Int = _S32Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 3, 2),
    _S32Int_Type()
)
s32Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s32Int.setStatus("current")
_S3ID_Type = SensorId
_S3ID_Object = MibScalar
s3ID = _S3ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 3, 3),
    _S3ID_Type()
)
s3ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3ID.setStatus("current")
_S3Alarm_ObjectIdentity = ObjectIdentity
s3Alarm = _S3Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 3, 4)
)
_S31Al_Type = ALARMSTATUS
_S31Al_Object = MibScalar
s31Al = _S31Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 3, 4, 1),
    _S31Al_Type()
)
s31Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s31Al.setStatus("current")
_S32Al_Type = ALARMSTATUS
_S32Al_Object = MibScalar
s32Al = _S32Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 3, 4, 2),
    _S32Al_Type()
)
s32Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s32Al.setStatus("current")
_Sensor4_ObjectIdentity = ObjectIdentity
sensor4 = _Sensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 4)
)
_S41Int_Type = SensorValue
_S41Int_Object = MibScalar
s41Int = _S41Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 4, 1),
    _S41Int_Type()
)
s41Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s41Int.setStatus("current")
_S42Int_Type = SensorValue
_S42Int_Object = MibScalar
s42Int = _S42Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 4, 2),
    _S42Int_Type()
)
s42Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s42Int.setStatus("current")
_S4ID_Type = SensorId
_S4ID_Object = MibScalar
s4ID = _S4ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 4, 3),
    _S4ID_Type()
)
s4ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s4ID.setStatus("current")
_S4Alarm_ObjectIdentity = ObjectIdentity
s4Alarm = _S4Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 4, 4)
)
_S41Al_Type = ALARMSTATUS
_S41Al_Object = MibScalar
s41Al = _S41Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 4, 4, 1),
    _S41Al_Type()
)
s41Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s41Al.setStatus("current")
_S42Al_Type = ALARMSTATUS
_S42Al_Object = MibScalar
s42Al = _S42Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 4, 4, 2),
    _S42Al_Type()
)
s42Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s42Al.setStatus("current")
_Sensor5_ObjectIdentity = ObjectIdentity
sensor5 = _Sensor5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 5)
)
_S51Int_Type = SensorValue
_S51Int_Object = MibScalar
s51Int = _S51Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 5, 1),
    _S51Int_Type()
)
s51Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s51Int.setStatus("current")
_S52Int_Type = SensorValue
_S52Int_Object = MibScalar
s52Int = _S52Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 5, 2),
    _S52Int_Type()
)
s52Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s52Int.setStatus("current")
_S5ID_Type = SensorId
_S5ID_Object = MibScalar
s5ID = _S5ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 5, 3),
    _S5ID_Type()
)
s5ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ID.setStatus("current")
_S5Alarm_ObjectIdentity = ObjectIdentity
s5Alarm = _S5Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 5, 4)
)
_S51Al_Type = ALARMSTATUS
_S51Al_Object = MibScalar
s51Al = _S51Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 5, 4, 1),
    _S51Al_Type()
)
s51Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s51Al.setStatus("current")
_S52Al_Type = ALARMSTATUS
_S52Al_Object = MibScalar
s52Al = _S52Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 5, 4, 2),
    _S52Al_Type()
)
s52Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s52Al.setStatus("current")
_Sensor6_ObjectIdentity = ObjectIdentity
sensor6 = _Sensor6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 6)
)
_S61Int_Type = SensorValue
_S61Int_Object = MibScalar
s61Int = _S61Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 6, 1),
    _S61Int_Type()
)
s61Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s61Int.setStatus("current")
_S62Int_Type = SensorValue
_S62Int_Object = MibScalar
s62Int = _S62Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 6, 2),
    _S62Int_Type()
)
s62Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s62Int.setStatus("current")
_S6ID_Type = SensorId
_S6ID_Object = MibScalar
s6ID = _S6ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 6, 3),
    _S6ID_Type()
)
s6ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6ID.setStatus("current")
_S6Alarm_ObjectIdentity = ObjectIdentity
s6Alarm = _S6Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 6, 4)
)
_S61Al_Type = ALARMSTATUS
_S61Al_Object = MibScalar
s61Al = _S61Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 6, 4, 1),
    _S61Al_Type()
)
s61Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s61Al.setStatus("current")
_S62Al_Type = ALARMSTATUS
_S62Al_Object = MibScalar
s62Al = _S62Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 6, 4, 2),
    _S62Al_Type()
)
s62Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s62Al.setStatus("current")
_Sensor7_ObjectIdentity = ObjectIdentity
sensor7 = _Sensor7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 7)
)
_S71Int_Type = SensorValue
_S71Int_Object = MibScalar
s71Int = _S71Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 7, 1),
    _S71Int_Type()
)
s71Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s71Int.setStatus("current")
_S72Int_Type = SensorValue
_S72Int_Object = MibScalar
s72Int = _S72Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 7, 2),
    _S72Int_Type()
)
s72Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s72Int.setStatus("current")
_S7ID_Type = SensorId
_S7ID_Object = MibScalar
s7ID = _S7ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 7, 3),
    _S7ID_Type()
)
s7ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s7ID.setStatus("current")
_S7Alarm_ObjectIdentity = ObjectIdentity
s7Alarm = _S7Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 7, 4)
)
_S71Al_Type = ALARMSTATUS
_S71Al_Object = MibScalar
s71Al = _S71Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 7, 4, 1),
    _S71Al_Type()
)
s71Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s71Al.setStatus("current")
_S72Al_Type = ALARMSTATUS
_S72Al_Object = MibScalar
s72Al = _S72Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 7, 4, 2),
    _S72Al_Type()
)
s72Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s72Al.setStatus("current")
_Sensor8_ObjectIdentity = ObjectIdentity
sensor8 = _Sensor8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 8)
)
_S81Int_Type = SensorValue
_S81Int_Object = MibScalar
s81Int = _S81Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 8, 1),
    _S81Int_Type()
)
s81Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s81Int.setStatus("current")
_S82Int_Type = SensorValue
_S82Int_Object = MibScalar
s82Int = _S82Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 8, 2),
    _S82Int_Type()
)
s82Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s82Int.setStatus("current")
_S8ID_Type = SensorId
_S8ID_Object = MibScalar
s8ID = _S8ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 8, 3),
    _S8ID_Type()
)
s8ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s8ID.setStatus("current")
_S8Alarm_ObjectIdentity = ObjectIdentity
s8Alarm = _S8Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 8, 4)
)
_S81Al_Type = ALARMSTATUS
_S81Al_Object = MibScalar
s81Al = _S81Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 8, 4, 1),
    _S81Al_Type()
)
s81Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s81Al.setStatus("current")
_S82Al_Type = ALARMSTATUS
_S82Al_Object = MibScalar
s82Al = _S82Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 1, 8, 4, 2),
    _S82Al_Type()
)
s82Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s82Al.setStatus("current")
_Analog_ObjectIdentity = ObjectIdentity
analog = _Analog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2)
)
_Voltage1Int_Type = AnalogValue
_Voltage1Int_Object = MibScalar
voltage1Int = _Voltage1Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 1),
    _Voltage1Int_Type()
)
voltage1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage1Int.setStatus("current")
_Voltage2Int_Type = AnalogValue
_Voltage2Int_Object = MibScalar
voltage2Int = _Voltage2Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 2),
    _Voltage2Int_Type()
)
voltage2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage2Int.setStatus("current")
_Voltage3Int_Type = AnalogValue
_Voltage3Int_Object = MibScalar
voltage3Int = _Voltage3Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 3),
    _Voltage3Int_Type()
)
voltage3Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage3Int.setStatus("current")
_Voltage4Int_Type = AnalogValue
_Voltage4Int_Object = MibScalar
voltage4Int = _Voltage4Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 4),
    _Voltage4Int_Type()
)
voltage4Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage4Int.setStatus("current")
_AnalogAlarm_ObjectIdentity = ObjectIdentity
analogAlarm = _AnalogAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 5)
)
_Volt1Al_Type = ALARMSTATUS
_Volt1Al_Object = MibScalar
volt1Al = _Volt1Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 5, 1),
    _Volt1Al_Type()
)
volt1Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt1Al.setStatus("current")
_Volt2Al_Type = ALARMSTATUS
_Volt2Al_Object = MibScalar
volt2Al = _Volt2Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 5, 2),
    _Volt2Al_Type()
)
volt2Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt2Al.setStatus("current")
_Volt3Al_Type = ALARMSTATUS
_Volt3Al_Object = MibScalar
volt3Al = _Volt3Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 5, 3),
    _Volt3Al_Type()
)
volt3Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt3Al.setStatus("current")
_Volt4Al_Type = ALARMSTATUS
_Volt4Al_Object = MibScalar
volt4Al = _Volt4Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 2, 5, 4),
    _Volt4Al_Type()
)
volt4Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volt4Al.setStatus("current")
_Digital_ObjectIdentity = ObjectIdentity
digital = _Digital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3)
)


class _DigitalInput1State_Type(Integer32):
    """Custom type digitalInput1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput1State_Type.__name__ = "Integer32"
_DigitalInput1State_Object = MibScalar
digitalInput1State = _DigitalInput1State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 1),
    _DigitalInput1State_Type()
)
digitalInput1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput1State.setStatus("current")


class _DigitalInput2State_Type(Integer32):
    """Custom type digitalInput2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput2State_Type.__name__ = "Integer32"
_DigitalInput2State_Object = MibScalar
digitalInput2State = _DigitalInput2State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 2),
    _DigitalInput2State_Type()
)
digitalInput2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput2State.setStatus("current")


class _DigitalInput3State_Type(Integer32):
    """Custom type digitalInput3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput3State_Type.__name__ = "Integer32"
_DigitalInput3State_Object = MibScalar
digitalInput3State = _DigitalInput3State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 3),
    _DigitalInput3State_Type()
)
digitalInput3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput3State.setStatus("current")


class _DigitalInput4State_Type(Integer32):
    """Custom type digitalInput4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput4State_Type.__name__ = "Integer32"
_DigitalInput4State_Object = MibScalar
digitalInput4State = _DigitalInput4State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 4),
    _DigitalInput4State_Type()
)
digitalInput4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput4State.setStatus("current")
_DigAlarm_ObjectIdentity = ObjectIdentity
digAlarm = _DigAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 5)
)
_Dig1Al_Type = ALARMSTATUS
_Dig1Al_Object = MibScalar
dig1Al = _Dig1Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 5, 1),
    _Dig1Al_Type()
)
dig1Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dig1Al.setStatus("current")
_Dig2Al_Type = ALARMSTATUS
_Dig2Al_Object = MibScalar
dig2Al = _Dig2Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 5, 2),
    _Dig2Al_Type()
)
dig2Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dig2Al.setStatus("current")
_Dig3Al_Type = ALARMSTATUS
_Dig3Al_Object = MibScalar
dig3Al = _Dig3Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 5, 3),
    _Dig3Al_Type()
)
dig3Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dig3Al.setStatus("current")
_Dig4Al_Type = ALARMSTATUS
_Dig4Al_Object = MibScalar
dig4Al = _Dig4Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 3, 5, 4),
    _Dig4Al_Type()
)
dig4Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dig4Al.setStatus("current")
_Relays_ObjectIdentity = ObjectIdentity
relays = _Relays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4)
)
_Relay1_ObjectIdentity = ObjectIdentity
relay1 = _Relay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 1)
)


class _Relay1State_Type(Integer32):
    """Custom type relay1State based on Integer32"""
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


_Relay1State_Type.__name__ = "Integer32"
_Relay1State_Object = MibScalar
relay1State = _Relay1State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 1, 1),
    _Relay1State_Type()
)
relay1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1State.setStatus("current")


class _Relay1Pulse_Type(Integer32):
    """Custom type relay1Pulse based on Integer32"""
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


_Relay1Pulse_Type.__name__ = "Integer32"
_Relay1Pulse_Object = MibScalar
relay1Pulse = _Relay1Pulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 1, 2),
    _Relay1Pulse_Type()
)
relay1Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1Pulse.setStatus("current")
_Relay2_ObjectIdentity = ObjectIdentity
relay2 = _Relay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 2)
)


class _Relay2State_Type(Integer32):
    """Custom type relay2State based on Integer32"""
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


_Relay2State_Type.__name__ = "Integer32"
_Relay2State_Object = MibScalar
relay2State = _Relay2State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 2, 1),
    _Relay2State_Type()
)
relay2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2State.setStatus("current")


class _Relay2Pulse_Type(Integer32):
    """Custom type relay2Pulse based on Integer32"""
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


_Relay2Pulse_Type.__name__ = "Integer32"
_Relay2Pulse_Object = MibScalar
relay2Pulse = _Relay2Pulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 2, 2),
    _Relay2Pulse_Type()
)
relay2Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2Pulse.setStatus("current")
_Relay3_ObjectIdentity = ObjectIdentity
relay3 = _Relay3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 3)
)


class _Relay3State_Type(Integer32):
    """Custom type relay3State based on Integer32"""
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


_Relay3State_Type.__name__ = "Integer32"
_Relay3State_Object = MibScalar
relay3State = _Relay3State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 3, 1),
    _Relay3State_Type()
)
relay3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3State.setStatus("current")


class _Relay3Pulse_Type(Integer32):
    """Custom type relay3Pulse based on Integer32"""
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


_Relay3Pulse_Type.__name__ = "Integer32"
_Relay3Pulse_Object = MibScalar
relay3Pulse = _Relay3Pulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 3, 2),
    _Relay3Pulse_Type()
)
relay3Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3Pulse.setStatus("current")
_Relay4_ObjectIdentity = ObjectIdentity
relay4 = _Relay4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 4)
)


class _Relay4State_Type(Integer32):
    """Custom type relay4State based on Integer32"""
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


_Relay4State_Type.__name__ = "Integer32"
_Relay4State_Object = MibScalar
relay4State = _Relay4State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 4, 1),
    _Relay4State_Type()
)
relay4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4State.setStatus("current")


class _Relay4Pulse_Type(Integer32):
    """Custom type relay4Pulse based on Integer32"""
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


_Relay4Pulse_Type.__name__ = "Integer32"
_Relay4Pulse_Object = MibScalar
relay4Pulse = _Relay4Pulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 4, 4, 2),
    _Relay4Pulse_Type()
)
relay4Pulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4Pulse.setStatus("current")


class _ConfigurationSaved_Type(Integer32):
    """Custom type configurationSaved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsaved", 0),
          ("saved", 1))
    )


_ConfigurationSaved_Type.__name__ = "Integer32"
_ConfigurationSaved_Object = MibScalar
configurationSaved = _ConfigurationSaved_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 5),
    _ConfigurationSaved_Type()
)
configurationSaved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationSaved.setStatus("current")


class _RestartDevice_Type(Integer32):
    """Custom type restartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 0),
          ("restart", 1))
    )


_RestartDevice_Type.__name__ = "Integer32"
_RestartDevice_Object = MibScalar
restartDevice = _RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 6),
    _RestartDevice_Type()
)
restartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDevice.setStatus("current")


class _TemperatureUnit_Type(Integer32):
    """Custom type temperatureUnit based on Integer32"""
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


_TemperatureUnit_Type.__name__ = "Integer32"
_TemperatureUnit_Object = MibScalar
temperatureUnit = _TemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 7),
    _TemperatureUnit_Type()
)
temperatureUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureUnit.setStatus("current")


class _HardwareErr_Type(Integer32):
    """Custom type hardwareErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noErr", 0),
          ("owErr", 1),
          ("hwErr", 2))
    )


_HardwareErr_Type.__name__ = "Integer32"
_HardwareErr_Object = MibScalar
hardwareErr = _HardwareErr_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 8),
    _HardwareErr_Type()
)
hardwareErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareErr.setStatus("current")


class _PressureUnit_Type(Integer32):
    """Custom type pressureUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hPa", 0),
          ("mbar", 1),
          ("mmhg", 2))
    )


_PressureUnit_Type.__name__ = "Integer32"
_PressureUnit_Object = MibScalar
pressureUnit = _PressureUnit_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 9),
    _PressureUnit_Type()
)
pressureUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pressureUnit.setStatus("current")
_Functions_ObjectIdentity = ObjectIdentity
functions = _Functions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10)
)


class _Func1State_Type(Integer32):
    """Custom type func1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Func1State_Type.__name__ = "Integer32"
_Func1State_Object = MibScalar
func1State = _Func1State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 1),
    _Func1State_Type()
)
func1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    func1State.setStatus("current")


class _Func2State_Type(Integer32):
    """Custom type func2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Func2State_Type.__name__ = "Integer32"
_Func2State_Object = MibScalar
func2State = _Func2State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 2),
    _Func2State_Type()
)
func2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    func2State.setStatus("current")


class _Func3State_Type(Integer32):
    """Custom type func3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Func3State_Type.__name__ = "Integer32"
_Func3State_Object = MibScalar
func3State = _Func3State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 3),
    _Func3State_Type()
)
func3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    func3State.setStatus("current")


class _Func4State_Type(Integer32):
    """Custom type func4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Func4State_Type.__name__ = "Integer32"
_Func4State_Object = MibScalar
func4State = _Func4State_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 4),
    _Func4State_Type()
)
func4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    func4State.setStatus("current")
_FuncAlarm_ObjectIdentity = ObjectIdentity
funcAlarm = _FuncAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 5)
)
_Func1Al_Type = ALARMSTATUS
_Func1Al_Object = MibScalar
func1Al = _Func1Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 5, 1),
    _Func1Al_Type()
)
func1Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    func1Al.setStatus("current")
_Func2Al_Type = ALARMSTATUS
_Func2Al_Object = MibScalar
func2Al = _Func2Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 5, 2),
    _Func2Al_Type()
)
func2Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    func2Al.setStatus("current")
_Func3Al_Type = ALARMSTATUS
_Func3Al_Object = MibScalar
func3Al = _Func3Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 5, 3),
    _Func3Al_Type()
)
func3Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    func3Al.setStatus("current")
_Func4Al_Type = ALARMSTATUS
_Func4Al_Object = MibScalar
func4Al = _Func4Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 10, 5, 4),
    _Func4Al_Type()
)
func4Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    func4Al.setStatus("current")
_Virtual_ObjectIdentity = ObjectIdentity
virtual = _Virtual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11)
)
_VirtualInput1Int_Type = VirtualValue
_VirtualInput1Int_Object = MibScalar
virtualInput1Int = _VirtualInput1Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 1),
    _VirtualInput1Int_Type()
)
virtualInput1Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualInput1Int.setStatus("current")
_VirtualInput2Int_Type = VirtualValue
_VirtualInput2Int_Object = MibScalar
virtualInput2Int = _VirtualInput2Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 2),
    _VirtualInput2Int_Type()
)
virtualInput2Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualInput2Int.setStatus("current")
_VirtualInput3Int_Type = VirtualValue
_VirtualInput3Int_Object = MibScalar
virtualInput3Int = _VirtualInput3Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 3),
    _VirtualInput3Int_Type()
)
virtualInput3Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualInput3Int.setStatus("current")
_VirtualInput4Int_Type = VirtualValue
_VirtualInput4Int_Object = MibScalar
virtualInput4Int = _VirtualInput4Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 4),
    _VirtualInput4Int_Type()
)
virtualInput4Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualInput4Int.setStatus("current")
_VirtAlarm_ObjectIdentity = ObjectIdentity
virtAlarm = _VirtAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 5)
)
_Virt1Al_Type = ALARMSTATUS
_Virt1Al_Object = MibScalar
virt1Al = _Virt1Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 5, 1),
    _Virt1Al_Type()
)
virt1Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virt1Al.setStatus("current")
_Virt2Al_Type = ALARMSTATUS
_Virt2Al_Object = MibScalar
virt2Al = _Virt2Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 5, 2),
    _Virt2Al_Type()
)
virt2Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virt2Al.setStatus("current")
_Virt3Al_Type = ALARMSTATUS
_Virt3Al_Object = MibScalar
virt3Al = _Virt3Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 5, 3),
    _Virt3Al_Type()
)
virt3Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virt3Al.setStatus("current")
_Virt4Al_Type = ALARMSTATUS
_Virt4Al_Object = MibScalar
virt4Al = _Virt4Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3, 11, 5, 4),
    _Virt4Al_Type()
)
virt4Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virt4Al.setStatus("current")
_Tcw241MIBConformance_ObjectIdentity = ObjectIdentity
tcw241MIBConformance = _Tcw241MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4)
)
_Tcw241MIBCompliances_ObjectIdentity = ObjectIdentity
tcw241MIBCompliances = _Tcw241MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4, 1)
)
_Tcw241MIBGroups_ObjectIdentity = ObjectIdentity
tcw241MIBGroups = _Tcw241MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4, 2)
)

# Managed Objects groups

tcw241ProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4, 2, 1)
)
tcw241ProductGroup.setObjects(
      *(("TERACOM-TCW241-MIB", "name"),
        ("TERACOM-TCW241-MIB", "version"),
        ("TERACOM-TCW241-MIB", "dateTime"))
)
if mibBuilder.loadTexts:
    tcw241ProductGroup.setStatus("current")

tcw241SetupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4, 2, 2)
)
tcw241SetupGroup.setObjects(
      *(("TERACOM-TCW241-MIB", "deviceID"),
        ("TERACOM-TCW241-MIB", "hostName"),
        ("TERACOM-TCW241-MIB", "deviceIP"),
        ("TERACOM-TCW241-MIB", "s1description"),
        ("TERACOM-TCW241-MIB", "s11MAXInt"),
        ("TERACOM-TCW241-MIB", "s11MINInt"),
        ("TERACOM-TCW241-MIB", "s11HYSTInt"),
        ("TERACOM-TCW241-MIB", "s12MAXInt"),
        ("TERACOM-TCW241-MIB", "s12MINInt"),
        ("TERACOM-TCW241-MIB", "s12HYSTInt"),
        ("TERACOM-TCW241-MIB", "s2description"),
        ("TERACOM-TCW241-MIB", "s21MAXInt"),
        ("TERACOM-TCW241-MIB", "s21MINInt"),
        ("TERACOM-TCW241-MIB", "s21HYSTInt"),
        ("TERACOM-TCW241-MIB", "s22MAXInt"),
        ("TERACOM-TCW241-MIB", "s22MINInt"),
        ("TERACOM-TCW241-MIB", "s22HYSTInt"),
        ("TERACOM-TCW241-MIB", "s3description"),
        ("TERACOM-TCW241-MIB", "s31MAXInt"),
        ("TERACOM-TCW241-MIB", "s31MINInt"),
        ("TERACOM-TCW241-MIB", "s31HYSTInt"),
        ("TERACOM-TCW241-MIB", "s32MAXInt"),
        ("TERACOM-TCW241-MIB", "s32MINInt"),
        ("TERACOM-TCW241-MIB", "s32HYSTInt"),
        ("TERACOM-TCW241-MIB", "s4description"),
        ("TERACOM-TCW241-MIB", "s41MAXInt"),
        ("TERACOM-TCW241-MIB", "s41MINInt"),
        ("TERACOM-TCW241-MIB", "s41HYSTInt"),
        ("TERACOM-TCW241-MIB", "s42MAXInt"),
        ("TERACOM-TCW241-MIB", "s42MINInt"),
        ("TERACOM-TCW241-MIB", "s42HYSTInt"),
        ("TERACOM-TCW241-MIB", "s5description"),
        ("TERACOM-TCW241-MIB", "s51MAXInt"),
        ("TERACOM-TCW241-MIB", "s51MINInt"),
        ("TERACOM-TCW241-MIB", "s51HYSTInt"),
        ("TERACOM-TCW241-MIB", "s52MAXInt"),
        ("TERACOM-TCW241-MIB", "s52MINInt"),
        ("TERACOM-TCW241-MIB", "s52HYSTInt"),
        ("TERACOM-TCW241-MIB", "s6description"),
        ("TERACOM-TCW241-MIB", "s61MAXInt"),
        ("TERACOM-TCW241-MIB", "s61MINInt"),
        ("TERACOM-TCW241-MIB", "s61HYSTInt"),
        ("TERACOM-TCW241-MIB", "s62MAXInt"),
        ("TERACOM-TCW241-MIB", "s62MINInt"),
        ("TERACOM-TCW241-MIB", "s62HYSTInt"),
        ("TERACOM-TCW241-MIB", "s7description"),
        ("TERACOM-TCW241-MIB", "s71MAXInt"),
        ("TERACOM-TCW241-MIB", "s71MINInt"),
        ("TERACOM-TCW241-MIB", "s71HYSTInt"),
        ("TERACOM-TCW241-MIB", "s72MAXInt"),
        ("TERACOM-TCW241-MIB", "s72MINInt"),
        ("TERACOM-TCW241-MIB", "s72HYSTInt"),
        ("TERACOM-TCW241-MIB", "s8description"),
        ("TERACOM-TCW241-MIB", "s81MAXInt"),
        ("TERACOM-TCW241-MIB", "s81MINInt"),
        ("TERACOM-TCW241-MIB", "s81HYSTInt"),
        ("TERACOM-TCW241-MIB", "s82MAXInt"),
        ("TERACOM-TCW241-MIB", "s82MINInt"),
        ("TERACOM-TCW241-MIB", "s82HYSTInt"),
        ("TERACOM-TCW241-MIB", "voltage1description"),
        ("TERACOM-TCW241-MIB", "voltage1max"),
        ("TERACOM-TCW241-MIB", "voltage1min"),
        ("TERACOM-TCW241-MIB", "voltage1hyst"),
        ("TERACOM-TCW241-MIB", "voltage2description"),
        ("TERACOM-TCW241-MIB", "voltage2max"),
        ("TERACOM-TCW241-MIB", "voltage2min"),
        ("TERACOM-TCW241-MIB", "voltage2hyst"),
        ("TERACOM-TCW241-MIB", "voltage3description"),
        ("TERACOM-TCW241-MIB", "voltage3max"),
        ("TERACOM-TCW241-MIB", "voltage3min"),
        ("TERACOM-TCW241-MIB", "voltage3hyst"),
        ("TERACOM-TCW241-MIB", "voltage4description"),
        ("TERACOM-TCW241-MIB", "voltage4max"),
        ("TERACOM-TCW241-MIB", "voltage4min"),
        ("TERACOM-TCW241-MIB", "voltage4hyst"),
        ("TERACOM-TCW241-MIB", "digitalInput1description"),
        ("TERACOM-TCW241-MIB", "digitalInput2description"),
        ("TERACOM-TCW241-MIB", "digitalInput3description"),
        ("TERACOM-TCW241-MIB", "digitalInput4description"),
        ("TERACOM-TCW241-MIB", "relay1description"),
        ("TERACOM-TCW241-MIB", "relay1pulseWidth"),
        ("TERACOM-TCW241-MIB", "relay1controlledBy"),
        ("TERACOM-TCW241-MIB", "relay1action"),
        ("TERACOM-TCW241-MIB", "relay2description"),
        ("TERACOM-TCW241-MIB", "relay2pulseWidth"),
        ("TERACOM-TCW241-MIB", "relay2controlledBy"),
        ("TERACOM-TCW241-MIB", "relay2action"),
        ("TERACOM-TCW241-MIB", "relay3description"),
        ("TERACOM-TCW241-MIB", "relay3pulseWidth"),
        ("TERACOM-TCW241-MIB", "relay3controlledBy"),
        ("TERACOM-TCW241-MIB", "relay3action"),
        ("TERACOM-TCW241-MIB", "relay4description"),
        ("TERACOM-TCW241-MIB", "relay4pulseWidth"),
        ("TERACOM-TCW241-MIB", "relay4controlledBy"),
        ("TERACOM-TCW241-MIB", "relay4action"),
        ("TERACOM-TCW241-MIB", "virtualInput1description"),
        ("TERACOM-TCW241-MIB", "virtualInput1max"),
        ("TERACOM-TCW241-MIB", "virtualInput1min"),
        ("TERACOM-TCW241-MIB", "virtualInput1hyst"),
        ("TERACOM-TCW241-MIB", "virtualInput1Parent"),
        ("TERACOM-TCW241-MIB", "virtualInput2description"),
        ("TERACOM-TCW241-MIB", "virtualInput2max"),
        ("TERACOM-TCW241-MIB", "virtualInput2min"),
        ("TERACOM-TCW241-MIB", "virtualInput2hyst"),
        ("TERACOM-TCW241-MIB", "virtualInput2Parent"),
        ("TERACOM-TCW241-MIB", "virtualInput3description"),
        ("TERACOM-TCW241-MIB", "virtualInput3max"),
        ("TERACOM-TCW241-MIB", "virtualInput3min"),
        ("TERACOM-TCW241-MIB", "virtualInput3hyst"),
        ("TERACOM-TCW241-MIB", "virtualInput3Parent"),
        ("TERACOM-TCW241-MIB", "virtualInput4description"),
        ("TERACOM-TCW241-MIB", "virtualInput4max"),
        ("TERACOM-TCW241-MIB", "virtualInput4min"),
        ("TERACOM-TCW241-MIB", "virtualInput4hyst"),
        ("TERACOM-TCW241-MIB", "virtualInput4Parent"))
)
if mibBuilder.loadTexts:
    tcw241SetupGroup.setStatus("current")

tcw241MonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4, 2, 3)
)
tcw241MonitorGroup.setObjects(
      *(("TERACOM-TCW241-MIB", "s11Int"),
        ("TERACOM-TCW241-MIB", "s12Int"),
        ("TERACOM-TCW241-MIB", "s1ID"),
        ("TERACOM-TCW241-MIB", "s11Al"),
        ("TERACOM-TCW241-MIB", "s12Al"),
        ("TERACOM-TCW241-MIB", "s21Int"),
        ("TERACOM-TCW241-MIB", "s22Int"),
        ("TERACOM-TCW241-MIB", "s2ID"),
        ("TERACOM-TCW241-MIB", "s21Al"),
        ("TERACOM-TCW241-MIB", "s22Al"),
        ("TERACOM-TCW241-MIB", "s31Int"),
        ("TERACOM-TCW241-MIB", "s32Int"),
        ("TERACOM-TCW241-MIB", "s3ID"),
        ("TERACOM-TCW241-MIB", "s31Al"),
        ("TERACOM-TCW241-MIB", "s32Al"),
        ("TERACOM-TCW241-MIB", "s41Int"),
        ("TERACOM-TCW241-MIB", "s42Int"),
        ("TERACOM-TCW241-MIB", "s4ID"),
        ("TERACOM-TCW241-MIB", "s41Al"),
        ("TERACOM-TCW241-MIB", "s42Al"),
        ("TERACOM-TCW241-MIB", "s51Int"),
        ("TERACOM-TCW241-MIB", "s52Int"),
        ("TERACOM-TCW241-MIB", "s5ID"),
        ("TERACOM-TCW241-MIB", "s51Al"),
        ("TERACOM-TCW241-MIB", "s52Al"),
        ("TERACOM-TCW241-MIB", "s61Int"),
        ("TERACOM-TCW241-MIB", "s62Int"),
        ("TERACOM-TCW241-MIB", "s6ID"),
        ("TERACOM-TCW241-MIB", "s61Al"),
        ("TERACOM-TCW241-MIB", "s62Al"),
        ("TERACOM-TCW241-MIB", "s71Int"),
        ("TERACOM-TCW241-MIB", "s72Int"),
        ("TERACOM-TCW241-MIB", "s7ID"),
        ("TERACOM-TCW241-MIB", "s71Al"),
        ("TERACOM-TCW241-MIB", "s72Al"),
        ("TERACOM-TCW241-MIB", "s81Int"),
        ("TERACOM-TCW241-MIB", "s82Int"),
        ("TERACOM-TCW241-MIB", "s8ID"),
        ("TERACOM-TCW241-MIB", "s81Al"),
        ("TERACOM-TCW241-MIB", "s82Al"),
        ("TERACOM-TCW241-MIB", "voltage1Int"),
        ("TERACOM-TCW241-MIB", "voltage2Int"),
        ("TERACOM-TCW241-MIB", "voltage3Int"),
        ("TERACOM-TCW241-MIB", "voltage4Int"),
        ("TERACOM-TCW241-MIB", "volt1Al"),
        ("TERACOM-TCW241-MIB", "volt2Al"),
        ("TERACOM-TCW241-MIB", "volt3Al"),
        ("TERACOM-TCW241-MIB", "volt4Al"),
        ("TERACOM-TCW241-MIB", "digitalInput1State"),
        ("TERACOM-TCW241-MIB", "digitalInput2State"),
        ("TERACOM-TCW241-MIB", "digitalInput3State"),
        ("TERACOM-TCW241-MIB", "digitalInput4State"),
        ("TERACOM-TCW241-MIB", "dig1Al"),
        ("TERACOM-TCW241-MIB", "dig2Al"),
        ("TERACOM-TCW241-MIB", "dig3Al"),
        ("TERACOM-TCW241-MIB", "dig4Al"),
        ("TERACOM-TCW241-MIB", "relay1State"),
        ("TERACOM-TCW241-MIB", "relay1Pulse"),
        ("TERACOM-TCW241-MIB", "relay2State"),
        ("TERACOM-TCW241-MIB", "relay2Pulse"),
        ("TERACOM-TCW241-MIB", "relay3State"),
        ("TERACOM-TCW241-MIB", "relay3Pulse"),
        ("TERACOM-TCW241-MIB", "relay4State"),
        ("TERACOM-TCW241-MIB", "relay4Pulse"),
        ("TERACOM-TCW241-MIB", "configurationSaved"),
        ("TERACOM-TCW241-MIB", "restartDevice"),
        ("TERACOM-TCW241-MIB", "temperatureUnit"),
        ("TERACOM-TCW241-MIB", "hardwareErr"),
        ("TERACOM-TCW241-MIB", "pressureUnit"),
        ("TERACOM-TCW241-MIB", "func1State"),
        ("TERACOM-TCW241-MIB", "func2State"),
        ("TERACOM-TCW241-MIB", "func3State"),
        ("TERACOM-TCW241-MIB", "func4State"),
        ("TERACOM-TCW241-MIB", "func1Al"),
        ("TERACOM-TCW241-MIB", "func2Al"),
        ("TERACOM-TCW241-MIB", "func3Al"),
        ("TERACOM-TCW241-MIB", "func4Al"),
        ("TERACOM-TCW241-MIB", "virtualInput1Int"),
        ("TERACOM-TCW241-MIB", "virtualInput2Int"),
        ("TERACOM-TCW241-MIB", "virtualInput3Int"),
        ("TERACOM-TCW241-MIB", "virtualInput4Int"),
        ("TERACOM-TCW241-MIB", "virt1Al"),
        ("TERACOM-TCW241-MIB", "virt2Al"),
        ("TERACOM-TCW241-MIB", "virt3Al"),
        ("TERACOM-TCW241-MIB", "virt4Al"))
)
if mibBuilder.loadTexts:
    tcw241MonitorGroup.setStatus("current")


# Notification objects

snmp_trap_notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 38783, 3, 0, 1)
)
snmp_trap_notification.setObjects(
      *(("TERACOM-TCW241-MIB", "digitalInput1State"),
        ("TERACOM-TCW241-MIB", "digitalInput2State"),
        ("TERACOM-TCW241-MIB", "digitalInput3State"),
        ("TERACOM-TCW241-MIB", "digitalInput4State"),
        ("TERACOM-TCW241-MIB", "dig1Al"),
        ("TERACOM-TCW241-MIB", "dig2Al"),
        ("TERACOM-TCW241-MIB", "dig3Al"),
        ("TERACOM-TCW241-MIB", "dig4Al"),
        ("TERACOM-TCW241-MIB", "voltage1Int"),
        ("TERACOM-TCW241-MIB", "voltage2Int"),
        ("TERACOM-TCW241-MIB", "voltage3Int"),
        ("TERACOM-TCW241-MIB", "voltage4Int"),
        ("TERACOM-TCW241-MIB", "volt1Al"),
        ("TERACOM-TCW241-MIB", "volt2Al"),
        ("TERACOM-TCW241-MIB", "volt3Al"),
        ("TERACOM-TCW241-MIB", "volt4Al"),
        ("TERACOM-TCW241-MIB", "s11Int"),
        ("TERACOM-TCW241-MIB", "s12Int"),
        ("TERACOM-TCW241-MIB", "s11Al"),
        ("TERACOM-TCW241-MIB", "s12Al"),
        ("TERACOM-TCW241-MIB", "s21Int"),
        ("TERACOM-TCW241-MIB", "s22Int"),
        ("TERACOM-TCW241-MIB", "s21Al"),
        ("TERACOM-TCW241-MIB", "s22Al"),
        ("TERACOM-TCW241-MIB", "s31Int"),
        ("TERACOM-TCW241-MIB", "s32Int"),
        ("TERACOM-TCW241-MIB", "s31Al"),
        ("TERACOM-TCW241-MIB", "s32Al"),
        ("TERACOM-TCW241-MIB", "s41Int"),
        ("TERACOM-TCW241-MIB", "s42Int"),
        ("TERACOM-TCW241-MIB", "s41Al"),
        ("TERACOM-TCW241-MIB", "s42Al"),
        ("TERACOM-TCW241-MIB", "s51Int"),
        ("TERACOM-TCW241-MIB", "s52Int"),
        ("TERACOM-TCW241-MIB", "s51Al"),
        ("TERACOM-TCW241-MIB", "s52Al"),
        ("TERACOM-TCW241-MIB", "s61Int"),
        ("TERACOM-TCW241-MIB", "s62Int"),
        ("TERACOM-TCW241-MIB", "s61Al"),
        ("TERACOM-TCW241-MIB", "s62Al"),
        ("TERACOM-TCW241-MIB", "s71Int"),
        ("TERACOM-TCW241-MIB", "s72Int"),
        ("TERACOM-TCW241-MIB", "s71Al"),
        ("TERACOM-TCW241-MIB", "s72Al"),
        ("TERACOM-TCW241-MIB", "s81Int"),
        ("TERACOM-TCW241-MIB", "s82Int"),
        ("TERACOM-TCW241-MIB", "s81Al"),
        ("TERACOM-TCW241-MIB", "s82Al"),
        ("TERACOM-TCW241-MIB", "restartDevice"),
        ("TERACOM-TCW241-MIB", "deviceIP"),
        ("TERACOM-TCW241-MIB", "func1State"),
        ("TERACOM-TCW241-MIB", "func2State"),
        ("TERACOM-TCW241-MIB", "func3State"),
        ("TERACOM-TCW241-MIB", "func4State"),
        ("TERACOM-TCW241-MIB", "func1Al"),
        ("TERACOM-TCW241-MIB", "func2Al"),
        ("TERACOM-TCW241-MIB", "func3Al"),
        ("TERACOM-TCW241-MIB", "func4Al"),
        ("TERACOM-TCW241-MIB", "virtualInput1Int"),
        ("TERACOM-TCW241-MIB", "virtualInput2Int"),
        ("TERACOM-TCW241-MIB", "virtualInput3Int"),
        ("TERACOM-TCW241-MIB", "virtualInput4Int"),
        ("TERACOM-TCW241-MIB", "virt1Al"),
        ("TERACOM-TCW241-MIB", "virt2Al"),
        ("TERACOM-TCW241-MIB", "virt3Al"),
        ("TERACOM-TCW241-MIB", "virt4Al"))
)
if mibBuilder.loadTexts:
    snmp_trap_notification.setStatus(
        "current"
    )


# Notifications groups

tcw241TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4, 2, 4)
)
tcw241TrapGroup.setObjects(
    ("TERACOM-TCW241-MIB", "snmp-trap-notification")
)
if mibBuilder.loadTexts:
    tcw241TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tcw241MIBCompliances1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4, 1, 1)
)
tcw241MIBCompliances1.setObjects(
      *(("TERACOM-TCW241-MIB", "tcw241ProductGroup"),
        ("TERACOM-TCW241-MIB", "tcw241SetupGroup"),
        ("TERACOM-TCW241-MIB", "tcw241MonitorGroup"),
        ("TERACOM-TCW241-MIB", "tcw241TrapGroup"))
)
if mibBuilder.loadTexts:
    tcw241MIBCompliances1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERACOM-TCW241-MIB",
    **{"CONTROLLED": CONTROLLED,
       "RELAYACTION": RELAYACTION,
       "VIRTUALPARENT": VIRTUALPARENT,
       "SensorId": SensorId,
       "AnalogValue": AnalogValue,
       "SensorValue": SensorValue,
       "VirtualValue": VirtualValue,
       "ALARMSTATUS": ALARMSTATUS,
       "teracom": teracom,
       "tcw241": tcw241,
       "trapNotifications": trapNotifications,
       "snmp-trap-notification": snmp_trap_notification,
       "product": product,
       "name": name,
       "version": version,
       "dateTime": dateTime,
       "setup": setup,
       "network": network,
       "deviceID": deviceID,
       "hostName": hostName,
       "deviceIP": deviceIP,
       "io": io,
       "sensorsSetup": sensorsSetup,
       "sensor1setup": sensor1setup,
       "s1description": s1description,
       "sensor11setup": sensor11setup,
       "s11MAXInt": s11MAXInt,
       "s11MINInt": s11MINInt,
       "s11HYSTInt": s11HYSTInt,
       "sensor12setup": sensor12setup,
       "s12MAXInt": s12MAXInt,
       "s12MINInt": s12MINInt,
       "s12HYSTInt": s12HYSTInt,
       "sensor2setup": sensor2setup,
       "s2description": s2description,
       "sensor21setup": sensor21setup,
       "s21MAXInt": s21MAXInt,
       "s21MINInt": s21MINInt,
       "s21HYSTInt": s21HYSTInt,
       "sensor22setup": sensor22setup,
       "s22MAXInt": s22MAXInt,
       "s22MINInt": s22MINInt,
       "s22HYSTInt": s22HYSTInt,
       "sensor3setup": sensor3setup,
       "s3description": s3description,
       "sensor31setup": sensor31setup,
       "s31MAXInt": s31MAXInt,
       "s31MINInt": s31MINInt,
       "s31HYSTInt": s31HYSTInt,
       "sensor32setup": sensor32setup,
       "s32MAXInt": s32MAXInt,
       "s32MINInt": s32MINInt,
       "s32HYSTInt": s32HYSTInt,
       "sensor4setup": sensor4setup,
       "s4description": s4description,
       "sensor41setup": sensor41setup,
       "s41MAXInt": s41MAXInt,
       "s41MINInt": s41MINInt,
       "s41HYSTInt": s41HYSTInt,
       "sensor42setup": sensor42setup,
       "s42MAXInt": s42MAXInt,
       "s42MINInt": s42MINInt,
       "s42HYSTInt": s42HYSTInt,
       "sensor5setup": sensor5setup,
       "s5description": s5description,
       "sensor51setup": sensor51setup,
       "s51MAXInt": s51MAXInt,
       "s51MINInt": s51MINInt,
       "s51HYSTInt": s51HYSTInt,
       "sensor52setup": sensor52setup,
       "s52MAXInt": s52MAXInt,
       "s52MINInt": s52MINInt,
       "s52HYSTInt": s52HYSTInt,
       "sensor6setup": sensor6setup,
       "s6description": s6description,
       "sensor61setup": sensor61setup,
       "s61MAXInt": s61MAXInt,
       "s61MINInt": s61MINInt,
       "s61HYSTInt": s61HYSTInt,
       "sensor62setup": sensor62setup,
       "s62MAXInt": s62MAXInt,
       "s62MINInt": s62MINInt,
       "s62HYSTInt": s62HYSTInt,
       "sensor7setup": sensor7setup,
       "s7description": s7description,
       "sensor71setup": sensor71setup,
       "s71MAXInt": s71MAXInt,
       "s71MINInt": s71MINInt,
       "s71HYSTInt": s71HYSTInt,
       "sensor72setup": sensor72setup,
       "s72MAXInt": s72MAXInt,
       "s72MINInt": s72MINInt,
       "s72HYSTInt": s72HYSTInt,
       "sensor8setup": sensor8setup,
       "s8description": s8description,
       "sensor81setup": sensor81setup,
       "s81MAXInt": s81MAXInt,
       "s81MINInt": s81MINInt,
       "s81HYSTInt": s81HYSTInt,
       "sensor82setup": sensor82setup,
       "s82MAXInt": s82MAXInt,
       "s82MINInt": s82MINInt,
       "s82HYSTInt": s82HYSTInt,
       "analogSetup": analogSetup,
       "analog1setup": analog1setup,
       "voltage1description": voltage1description,
       "voltage1max": voltage1max,
       "voltage1min": voltage1min,
       "voltage1hyst": voltage1hyst,
       "analog2setup": analog2setup,
       "voltage2description": voltage2description,
       "voltage2max": voltage2max,
       "voltage2min": voltage2min,
       "voltage2hyst": voltage2hyst,
       "analog3setup": analog3setup,
       "voltage3description": voltage3description,
       "voltage3max": voltage3max,
       "voltage3min": voltage3min,
       "voltage3hyst": voltage3hyst,
       "analog4setup": analog4setup,
       "voltage4description": voltage4description,
       "voltage4max": voltage4max,
       "voltage4min": voltage4min,
       "voltage4hyst": voltage4hyst,
       "digitalSetup": digitalSetup,
       "digitalInput1description": digitalInput1description,
       "digitalInput2description": digitalInput2description,
       "digitalInput3description": digitalInput3description,
       "digitalInput4description": digitalInput4description,
       "relaysSetup": relaysSetup,
       "relay1setup": relay1setup,
       "relay1description": relay1description,
       "relay1pulseWidth": relay1pulseWidth,
       "relay1controlledBy": relay1controlledBy,
       "relay1action": relay1action,
       "relay2setup": relay2setup,
       "relay2description": relay2description,
       "relay2pulseWidth": relay2pulseWidth,
       "relay2controlledBy": relay2controlledBy,
       "relay2action": relay2action,
       "relay3setup": relay3setup,
       "relay3description": relay3description,
       "relay3pulseWidth": relay3pulseWidth,
       "relay3controlledBy": relay3controlledBy,
       "relay3action": relay3action,
       "relay4setup": relay4setup,
       "relay4description": relay4description,
       "relay4pulseWidth": relay4pulseWidth,
       "relay4controlledBy": relay4controlledBy,
       "relay4action": relay4action,
       "virtualSetup": virtualSetup,
       "virtual1setup": virtual1setup,
       "virtualInput1description": virtualInput1description,
       "virtualInput1max": virtualInput1max,
       "virtualInput1min": virtualInput1min,
       "virtualInput1hyst": virtualInput1hyst,
       "virtualInput1Parent": virtualInput1Parent,
       "virtual2setup": virtual2setup,
       "virtualInput2description": virtualInput2description,
       "virtualInput2max": virtualInput2max,
       "virtualInput2min": virtualInput2min,
       "virtualInput2hyst": virtualInput2hyst,
       "virtualInput2Parent": virtualInput2Parent,
       "virtual3setup": virtual3setup,
       "virtualInput3description": virtualInput3description,
       "virtualInput3max": virtualInput3max,
       "virtualInput3min": virtualInput3min,
       "virtualInput3hyst": virtualInput3hyst,
       "virtualInput3Parent": virtualInput3Parent,
       "virtual4setup": virtual4setup,
       "virtualInput4description": virtualInput4description,
       "virtualInput4max": virtualInput4max,
       "virtualInput4min": virtualInput4min,
       "virtualInput4hyst": virtualInput4hyst,
       "virtualInput4Parent": virtualInput4Parent,
       "monitorNcontrol": monitorNcontrol,
       "sensors": sensors,
       "sensor1": sensor1,
       "s11Int": s11Int,
       "s12Int": s12Int,
       "s1ID": s1ID,
       "s1Alarm": s1Alarm,
       "s11Al": s11Al,
       "s12Al": s12Al,
       "sensor2": sensor2,
       "s21Int": s21Int,
       "s22Int": s22Int,
       "s2ID": s2ID,
       "s2Alarm": s2Alarm,
       "s21Al": s21Al,
       "s22Al": s22Al,
       "sensor3": sensor3,
       "s31Int": s31Int,
       "s32Int": s32Int,
       "s3ID": s3ID,
       "s3Alarm": s3Alarm,
       "s31Al": s31Al,
       "s32Al": s32Al,
       "sensor4": sensor4,
       "s41Int": s41Int,
       "s42Int": s42Int,
       "s4ID": s4ID,
       "s4Alarm": s4Alarm,
       "s41Al": s41Al,
       "s42Al": s42Al,
       "sensor5": sensor5,
       "s51Int": s51Int,
       "s52Int": s52Int,
       "s5ID": s5ID,
       "s5Alarm": s5Alarm,
       "s51Al": s51Al,
       "s52Al": s52Al,
       "sensor6": sensor6,
       "s61Int": s61Int,
       "s62Int": s62Int,
       "s6ID": s6ID,
       "s6Alarm": s6Alarm,
       "s61Al": s61Al,
       "s62Al": s62Al,
       "sensor7": sensor7,
       "s71Int": s71Int,
       "s72Int": s72Int,
       "s7ID": s7ID,
       "s7Alarm": s7Alarm,
       "s71Al": s71Al,
       "s72Al": s72Al,
       "sensor8": sensor8,
       "s81Int": s81Int,
       "s82Int": s82Int,
       "s8ID": s8ID,
       "s8Alarm": s8Alarm,
       "s81Al": s81Al,
       "s82Al": s82Al,
       "analog": analog,
       "voltage1Int": voltage1Int,
       "voltage2Int": voltage2Int,
       "voltage3Int": voltage3Int,
       "voltage4Int": voltage4Int,
       "analogAlarm": analogAlarm,
       "volt1Al": volt1Al,
       "volt2Al": volt2Al,
       "volt3Al": volt3Al,
       "volt4Al": volt4Al,
       "digital": digital,
       "digitalInput1State": digitalInput1State,
       "digitalInput2State": digitalInput2State,
       "digitalInput3State": digitalInput3State,
       "digitalInput4State": digitalInput4State,
       "digAlarm": digAlarm,
       "dig1Al": dig1Al,
       "dig2Al": dig2Al,
       "dig3Al": dig3Al,
       "dig4Al": dig4Al,
       "relays": relays,
       "relay1": relay1,
       "relay1State": relay1State,
       "relay1Pulse": relay1Pulse,
       "relay2": relay2,
       "relay2State": relay2State,
       "relay2Pulse": relay2Pulse,
       "relay3": relay3,
       "relay3State": relay3State,
       "relay3Pulse": relay3Pulse,
       "relay4": relay4,
       "relay4State": relay4State,
       "relay4Pulse": relay4Pulse,
       "configurationSaved": configurationSaved,
       "restartDevice": restartDevice,
       "temperatureUnit": temperatureUnit,
       "hardwareErr": hardwareErr,
       "pressureUnit": pressureUnit,
       "functions": functions,
       "func1State": func1State,
       "func2State": func2State,
       "func3State": func3State,
       "func4State": func4State,
       "funcAlarm": funcAlarm,
       "func1Al": func1Al,
       "func2Al": func2Al,
       "func3Al": func3Al,
       "func4Al": func4Al,
       "virtual": virtual,
       "virtualInput1Int": virtualInput1Int,
       "virtualInput2Int": virtualInput2Int,
       "virtualInput3Int": virtualInput3Int,
       "virtualInput4Int": virtualInput4Int,
       "virtAlarm": virtAlarm,
       "virt1Al": virt1Al,
       "virt2Al": virt2Al,
       "virt3Al": virt3Al,
       "virt4Al": virt4Al,
       "tcw241MIBConformance": tcw241MIBConformance,
       "tcw241MIBCompliances": tcw241MIBCompliances,
       "tcw241MIBCompliances1": tcw241MIBCompliances1,
       "tcw241MIBGroups": tcw241MIBGroups,
       "tcw241ProductGroup": tcw241ProductGroup,
       "tcw241SetupGroup": tcw241SetupGroup,
       "tcw241MonitorGroup": tcw241MonitorGroup,
       "tcw241TrapGroup": tcw241TrapGroup,
       "snmpMIB": snmpMIB}
)
