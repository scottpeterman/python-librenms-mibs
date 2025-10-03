# SNMP MIB module (TERACOM-TCW210-TH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\teracom\TERACOM-TCW210-TH-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:30:08 2025
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
        ("2021-04-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SensorId(TextualConvention, OctetString):
    status = "current"
    displayHint = "16a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



class SensorValue(TextualConvention, Integer32):
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
_Tcw210th_ObjectIdentity = ObjectIdentity
tcw210th = _Tcw210th_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4)
)
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_DateTime_Type = DateAndTime
_DateTime_Object = MibScalar
dateTime = _DateTime_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 1, 3),
    _DateTime_Type()
)
dateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dateTime.setStatus("current")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 1)
)
_DeviceID_Type = MacAddress
_DeviceID_Object = MibScalar
deviceID = _DeviceID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("current")
_DeviceIP_Type = IpAddress
_DeviceIP_Object = MibScalar
deviceIP = _DeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 1, 3),
    _DeviceIP_Type()
)
deviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIP.setStatus("current")
_Io_ObjectIdentity = ObjectIdentity
io = _Io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2)
)
_SensorsSetup_ObjectIdentity = ObjectIdentity
sensorsSetup = _SensorsSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1)
)
_Sensor1setup_ObjectIdentity = ObjectIdentity
sensor1setup = _Sensor1setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 1),
    _S1description_Type()
)
s1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s1description.setStatus("current")
_Sensor11setup_ObjectIdentity = ObjectIdentity
sensor11setup = _Sensor11setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 2)
)
_S11MAXInt_Type = SensorValue
_S11MAXInt_Object = MibScalar
s11MAXInt = _S11MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 2, 1),
    _S11MAXInt_Type()
)
s11MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11MAXInt.setStatus("current")
_S11MINInt_Type = SensorValue
_S11MINInt_Object = MibScalar
s11MINInt = _S11MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 2, 2),
    _S11MINInt_Type()
)
s11MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11MINInt.setStatus("current")
_S11HYSTInt_Type = SensorValue
_S11HYSTInt_Object = MibScalar
s11HYSTInt = _S11HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 2, 3),
    _S11HYSTInt_Type()
)
s11HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11HYSTInt.setStatus("current")
_S11MULTInt_Type = SensorValue
_S11MULTInt_Object = MibScalar
s11MULTInt = _S11MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 2, 4),
    _S11MULTInt_Type()
)
s11MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11MULTInt.setStatus("current")
_S11OFFSETInt_Type = SensorValue
_S11OFFSETInt_Object = MibScalar
s11OFFSETInt = _S11OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 2, 5),
    _S11OFFSETInt_Type()
)
s11OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s11OFFSETInt.setStatus("current")
_Sensor12setup_ObjectIdentity = ObjectIdentity
sensor12setup = _Sensor12setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 3)
)
_S12MAXInt_Type = SensorValue
_S12MAXInt_Object = MibScalar
s12MAXInt = _S12MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 3, 1),
    _S12MAXInt_Type()
)
s12MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12MAXInt.setStatus("current")
_S12MINInt_Type = SensorValue
_S12MINInt_Object = MibScalar
s12MINInt = _S12MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 3, 2),
    _S12MINInt_Type()
)
s12MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12MINInt.setStatus("current")
_S12HYSTInt_Type = SensorValue
_S12HYSTInt_Object = MibScalar
s12HYSTInt = _S12HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 3, 3),
    _S12HYSTInt_Type()
)
s12HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12HYSTInt.setStatus("current")
_S12MULTInt_Type = SensorValue
_S12MULTInt_Object = MibScalar
s12MULTInt = _S12MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 3, 4),
    _S12MULTInt_Type()
)
s12MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12MULTInt.setStatus("current")
_S12OFFSETInt_Type = SensorValue
_S12OFFSETInt_Object = MibScalar
s12OFFSETInt = _S12OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 3, 5),
    _S12OFFSETInt_Type()
)
s12OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s12OFFSETInt.setStatus("current")
_Sensor13setup_ObjectIdentity = ObjectIdentity
sensor13setup = _Sensor13setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 4)
)
_S13MAXInt_Type = SensorValue
_S13MAXInt_Object = MibScalar
s13MAXInt = _S13MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 4, 1),
    _S13MAXInt_Type()
)
s13MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s13MAXInt.setStatus("current")
_S13MINInt_Type = SensorValue
_S13MINInt_Object = MibScalar
s13MINInt = _S13MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 4, 2),
    _S13MINInt_Type()
)
s13MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s13MINInt.setStatus("current")
_S13HYSTInt_Type = SensorValue
_S13HYSTInt_Object = MibScalar
s13HYSTInt = _S13HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 1, 4, 3),
    _S13HYSTInt_Type()
)
s13HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s13HYSTInt.setStatus("current")
_Sensor2setup_ObjectIdentity = ObjectIdentity
sensor2setup = _Sensor2setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 1),
    _S2description_Type()
)
s2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s2description.setStatus("current")
_Sensor21setup_ObjectIdentity = ObjectIdentity
sensor21setup = _Sensor21setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 2)
)
_S21MAXInt_Type = SensorValue
_S21MAXInt_Object = MibScalar
s21MAXInt = _S21MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 2, 1),
    _S21MAXInt_Type()
)
s21MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21MAXInt.setStatus("current")
_S21MINInt_Type = SensorValue
_S21MINInt_Object = MibScalar
s21MINInt = _S21MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 2, 2),
    _S21MINInt_Type()
)
s21MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21MINInt.setStatus("current")
_S21HYSTInt_Type = SensorValue
_S21HYSTInt_Object = MibScalar
s21HYSTInt = _S21HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 2, 3),
    _S21HYSTInt_Type()
)
s21HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21HYSTInt.setStatus("current")
_S21MULTInt_Type = SensorValue
_S21MULTInt_Object = MibScalar
s21MULTInt = _S21MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 2, 4),
    _S21MULTInt_Type()
)
s21MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21MULTInt.setStatus("current")
_S21OFFSETInt_Type = SensorValue
_S21OFFSETInt_Object = MibScalar
s21OFFSETInt = _S21OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 2, 5),
    _S21OFFSETInt_Type()
)
s21OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s21OFFSETInt.setStatus("current")
_Sensor22setup_ObjectIdentity = ObjectIdentity
sensor22setup = _Sensor22setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 3)
)
_S22MAXInt_Type = SensorValue
_S22MAXInt_Object = MibScalar
s22MAXInt = _S22MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 3, 1),
    _S22MAXInt_Type()
)
s22MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22MAXInt.setStatus("current")
_S22MINInt_Type = SensorValue
_S22MINInt_Object = MibScalar
s22MINInt = _S22MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 3, 2),
    _S22MINInt_Type()
)
s22MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22MINInt.setStatus("current")
_S22HYSTInt_Type = SensorValue
_S22HYSTInt_Object = MibScalar
s22HYSTInt = _S22HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 3, 3),
    _S22HYSTInt_Type()
)
s22HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22HYSTInt.setStatus("current")
_S22MULTInt_Type = SensorValue
_S22MULTInt_Object = MibScalar
s22MULTInt = _S22MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 3, 4),
    _S22MULTInt_Type()
)
s22MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22MULTInt.setStatus("current")
_S22OFFSETInt_Type = SensorValue
_S22OFFSETInt_Object = MibScalar
s22OFFSETInt = _S22OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 3, 5),
    _S22OFFSETInt_Type()
)
s22OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s22OFFSETInt.setStatus("current")
_Sensor23setup_ObjectIdentity = ObjectIdentity
sensor23setup = _Sensor23setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 4)
)
_S23MAXInt_Type = SensorValue
_S23MAXInt_Object = MibScalar
s23MAXInt = _S23MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 4, 1),
    _S23MAXInt_Type()
)
s23MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s23MAXInt.setStatus("current")
_S23MINInt_Type = SensorValue
_S23MINInt_Object = MibScalar
s23MINInt = _S23MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 4, 2),
    _S23MINInt_Type()
)
s23MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s23MINInt.setStatus("current")
_S23HYSTInt_Type = SensorValue
_S23HYSTInt_Object = MibScalar
s23HYSTInt = _S23HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 2, 4, 3),
    _S23HYSTInt_Type()
)
s23HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s23HYSTInt.setStatus("current")
_Sensor3setup_ObjectIdentity = ObjectIdentity
sensor3setup = _Sensor3setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 1),
    _S3description_Type()
)
s3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3description.setStatus("current")
_Sensor31setup_ObjectIdentity = ObjectIdentity
sensor31setup = _Sensor31setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 2)
)
_S31MAXInt_Type = SensorValue
_S31MAXInt_Object = MibScalar
s31MAXInt = _S31MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 2, 1),
    _S31MAXInt_Type()
)
s31MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31MAXInt.setStatus("current")
_S31MINInt_Type = SensorValue
_S31MINInt_Object = MibScalar
s31MINInt = _S31MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 2, 2),
    _S31MINInt_Type()
)
s31MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31MINInt.setStatus("current")
_S31HYSTInt_Type = SensorValue
_S31HYSTInt_Object = MibScalar
s31HYSTInt = _S31HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 2, 3),
    _S31HYSTInt_Type()
)
s31HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31HYSTInt.setStatus("current")
_S31MULTInt_Type = SensorValue
_S31MULTInt_Object = MibScalar
s31MULTInt = _S31MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 2, 4),
    _S31MULTInt_Type()
)
s31MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31MULTInt.setStatus("current")
_S31OFFSETInt_Type = SensorValue
_S31OFFSETInt_Object = MibScalar
s31OFFSETInt = _S31OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 2, 5),
    _S31OFFSETInt_Type()
)
s31OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s31OFFSETInt.setStatus("current")
_Sensor32setup_ObjectIdentity = ObjectIdentity
sensor32setup = _Sensor32setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 3)
)
_S32MAXInt_Type = SensorValue
_S32MAXInt_Object = MibScalar
s32MAXInt = _S32MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 3, 1),
    _S32MAXInt_Type()
)
s32MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32MAXInt.setStatus("current")
_S32MINInt_Type = SensorValue
_S32MINInt_Object = MibScalar
s32MINInt = _S32MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 3, 2),
    _S32MINInt_Type()
)
s32MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32MINInt.setStatus("current")
_S32HYSTInt_Type = SensorValue
_S32HYSTInt_Object = MibScalar
s32HYSTInt = _S32HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 3, 3),
    _S32HYSTInt_Type()
)
s32HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32HYSTInt.setStatus("current")
_S32MULTInt_Type = SensorValue
_S32MULTInt_Object = MibScalar
s32MULTInt = _S32MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 3, 4),
    _S32MULTInt_Type()
)
s32MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32MULTInt.setStatus("current")
_S32OFFSETInt_Type = SensorValue
_S32OFFSETInt_Object = MibScalar
s32OFFSETInt = _S32OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 3, 5),
    _S32OFFSETInt_Type()
)
s32OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s32OFFSETInt.setStatus("current")
_Sensor33setup_ObjectIdentity = ObjectIdentity
sensor33setup = _Sensor33setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 4)
)
_S33MAXInt_Type = SensorValue
_S33MAXInt_Object = MibScalar
s33MAXInt = _S33MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 4, 1),
    _S33MAXInt_Type()
)
s33MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s33MAXInt.setStatus("current")
_S33MINInt_Type = SensorValue
_S33MINInt_Object = MibScalar
s33MINInt = _S33MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 4, 2),
    _S33MINInt_Type()
)
s33MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s33MINInt.setStatus("current")
_S33HYSTInt_Type = SensorValue
_S33HYSTInt_Object = MibScalar
s33HYSTInt = _S33HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 3, 4, 3),
    _S33HYSTInt_Type()
)
s33HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s33HYSTInt.setStatus("current")
_Sensor4setup_ObjectIdentity = ObjectIdentity
sensor4setup = _Sensor4setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 1),
    _S4description_Type()
)
s4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s4description.setStatus("current")
_Sensor41setup_ObjectIdentity = ObjectIdentity
sensor41setup = _Sensor41setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 2)
)
_S41MAXInt_Type = SensorValue
_S41MAXInt_Object = MibScalar
s41MAXInt = _S41MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 2, 1),
    _S41MAXInt_Type()
)
s41MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41MAXInt.setStatus("current")
_S41MINInt_Type = SensorValue
_S41MINInt_Object = MibScalar
s41MINInt = _S41MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 2, 2),
    _S41MINInt_Type()
)
s41MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41MINInt.setStatus("current")
_S41HYSTInt_Type = SensorValue
_S41HYSTInt_Object = MibScalar
s41HYSTInt = _S41HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 2, 3),
    _S41HYSTInt_Type()
)
s41HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41HYSTInt.setStatus("current")
_S41MULTInt_Type = SensorValue
_S41MULTInt_Object = MibScalar
s41MULTInt = _S41MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 2, 4),
    _S41MULTInt_Type()
)
s41MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41MULTInt.setStatus("current")
_S41OFFSETInt_Type = SensorValue
_S41OFFSETInt_Object = MibScalar
s41OFFSETInt = _S41OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 2, 5),
    _S41OFFSETInt_Type()
)
s41OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s41OFFSETInt.setStatus("current")
_Sensor42setup_ObjectIdentity = ObjectIdentity
sensor42setup = _Sensor42setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 3)
)
_S42MAXInt_Type = SensorValue
_S42MAXInt_Object = MibScalar
s42MAXInt = _S42MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 3, 1),
    _S42MAXInt_Type()
)
s42MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42MAXInt.setStatus("current")
_S42MINInt_Type = SensorValue
_S42MINInt_Object = MibScalar
s42MINInt = _S42MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 3, 2),
    _S42MINInt_Type()
)
s42MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42MINInt.setStatus("current")
_S42HYSTInt_Type = SensorValue
_S42HYSTInt_Object = MibScalar
s42HYSTInt = _S42HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 3, 3),
    _S42HYSTInt_Type()
)
s42HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42HYSTInt.setStatus("current")
_S42MULTInt_Type = SensorValue
_S42MULTInt_Object = MibScalar
s42MULTInt = _S42MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 3, 4),
    _S42MULTInt_Type()
)
s42MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42MULTInt.setStatus("current")
_S42OFFSETInt_Type = SensorValue
_S42OFFSETInt_Object = MibScalar
s42OFFSETInt = _S42OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 3, 5),
    _S42OFFSETInt_Type()
)
s42OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s42OFFSETInt.setStatus("current")
_Sensor43setup_ObjectIdentity = ObjectIdentity
sensor43setup = _Sensor43setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 4)
)
_S43MAXInt_Type = SensorValue
_S43MAXInt_Object = MibScalar
s43MAXInt = _S43MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 4, 1),
    _S43MAXInt_Type()
)
s43MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s43MAXInt.setStatus("current")
_S43MINInt_Type = SensorValue
_S43MINInt_Object = MibScalar
s43MINInt = _S43MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 4, 2),
    _S43MINInt_Type()
)
s43MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s43MINInt.setStatus("current")
_S43HYSTInt_Type = SensorValue
_S43HYSTInt_Object = MibScalar
s43HYSTInt = _S43HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 4, 4, 3),
    _S43HYSTInt_Type()
)
s43HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s43HYSTInt.setStatus("current")
_Sensor5setup_ObjectIdentity = ObjectIdentity
sensor5setup = _Sensor5setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 1),
    _S5description_Type()
)
s5description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5description.setStatus("current")
_Sensor51setup_ObjectIdentity = ObjectIdentity
sensor51setup = _Sensor51setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 2)
)
_S51MAXInt_Type = SensorValue
_S51MAXInt_Object = MibScalar
s51MAXInt = _S51MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 2, 1),
    _S51MAXInt_Type()
)
s51MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51MAXInt.setStatus("current")
_S51MINInt_Type = SensorValue
_S51MINInt_Object = MibScalar
s51MINInt = _S51MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 2, 2),
    _S51MINInt_Type()
)
s51MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51MINInt.setStatus("current")
_S51HYSTInt_Type = SensorValue
_S51HYSTInt_Object = MibScalar
s51HYSTInt = _S51HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 2, 3),
    _S51HYSTInt_Type()
)
s51HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51HYSTInt.setStatus("current")
_S51MULTInt_Type = SensorValue
_S51MULTInt_Object = MibScalar
s51MULTInt = _S51MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 2, 4),
    _S51MULTInt_Type()
)
s51MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51MULTInt.setStatus("current")
_S51OFFSETInt_Type = SensorValue
_S51OFFSETInt_Object = MibScalar
s51OFFSETInt = _S51OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 2, 5),
    _S51OFFSETInt_Type()
)
s51OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s51OFFSETInt.setStatus("current")
_Sensor52setup_ObjectIdentity = ObjectIdentity
sensor52setup = _Sensor52setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 3)
)
_S52MAXInt_Type = SensorValue
_S52MAXInt_Object = MibScalar
s52MAXInt = _S52MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 3, 1),
    _S52MAXInt_Type()
)
s52MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52MAXInt.setStatus("current")
_S52MINInt_Type = SensorValue
_S52MINInt_Object = MibScalar
s52MINInt = _S52MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 3, 2),
    _S52MINInt_Type()
)
s52MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52MINInt.setStatus("current")
_S52HYSTInt_Type = SensorValue
_S52HYSTInt_Object = MibScalar
s52HYSTInt = _S52HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 3, 3),
    _S52HYSTInt_Type()
)
s52HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52HYSTInt.setStatus("current")
_S52MULTInt_Type = SensorValue
_S52MULTInt_Object = MibScalar
s52MULTInt = _S52MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 3, 4),
    _S52MULTInt_Type()
)
s52MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52MULTInt.setStatus("current")
_S52OFFSETInt_Type = SensorValue
_S52OFFSETInt_Object = MibScalar
s52OFFSETInt = _S52OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 3, 5),
    _S52OFFSETInt_Type()
)
s52OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s52OFFSETInt.setStatus("current")
_Sensor53setup_ObjectIdentity = ObjectIdentity
sensor53setup = _Sensor53setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 4)
)
_S53MAXInt_Type = SensorValue
_S53MAXInt_Object = MibScalar
s53MAXInt = _S53MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 4, 1),
    _S53MAXInt_Type()
)
s53MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s53MAXInt.setStatus("current")
_S53MINInt_Type = SensorValue
_S53MINInt_Object = MibScalar
s53MINInt = _S53MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 4, 2),
    _S53MINInt_Type()
)
s53MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s53MINInt.setStatus("current")
_S53HYSTInt_Type = SensorValue
_S53HYSTInt_Object = MibScalar
s53HYSTInt = _S53HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 5, 4, 3),
    _S53HYSTInt_Type()
)
s53HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s53HYSTInt.setStatus("current")
_Sensor6setup_ObjectIdentity = ObjectIdentity
sensor6setup = _Sensor6setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6)
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 1),
    _S6description_Type()
)
s6description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s6description.setStatus("current")
_Sensor61setup_ObjectIdentity = ObjectIdentity
sensor61setup = _Sensor61setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 2)
)
_S61MAXInt_Type = SensorValue
_S61MAXInt_Object = MibScalar
s61MAXInt = _S61MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 2, 1),
    _S61MAXInt_Type()
)
s61MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61MAXInt.setStatus("current")
_S61MINInt_Type = SensorValue
_S61MINInt_Object = MibScalar
s61MINInt = _S61MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 2, 2),
    _S61MINInt_Type()
)
s61MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61MINInt.setStatus("current")
_S61HYSTInt_Type = SensorValue
_S61HYSTInt_Object = MibScalar
s61HYSTInt = _S61HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 2, 3),
    _S61HYSTInt_Type()
)
s61HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61HYSTInt.setStatus("current")
_S61MULTInt_Type = SensorValue
_S61MULTInt_Object = MibScalar
s61MULTInt = _S61MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 2, 4),
    _S61MULTInt_Type()
)
s61MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61MULTInt.setStatus("current")
_S61OFFSETInt_Type = SensorValue
_S61OFFSETInt_Object = MibScalar
s61OFFSETInt = _S61OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 2, 5),
    _S61OFFSETInt_Type()
)
s61OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s61OFFSETInt.setStatus("current")
_Sensor62setup_ObjectIdentity = ObjectIdentity
sensor62setup = _Sensor62setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 3)
)
_S62MAXInt_Type = SensorValue
_S62MAXInt_Object = MibScalar
s62MAXInt = _S62MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 3, 1),
    _S62MAXInt_Type()
)
s62MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62MAXInt.setStatus("current")
_S62MINInt_Type = SensorValue
_S62MINInt_Object = MibScalar
s62MINInt = _S62MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 3, 2),
    _S62MINInt_Type()
)
s62MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62MINInt.setStatus("current")
_S62HYSTInt_Type = SensorValue
_S62HYSTInt_Object = MibScalar
s62HYSTInt = _S62HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 3, 3),
    _S62HYSTInt_Type()
)
s62HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62HYSTInt.setStatus("current")
_S62MULTInt_Type = SensorValue
_S62MULTInt_Object = MibScalar
s62MULTInt = _S62MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 3, 4),
    _S62MULTInt_Type()
)
s62MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62MULTInt.setStatus("current")
_S62OFFSETInt_Type = SensorValue
_S62OFFSETInt_Object = MibScalar
s62OFFSETInt = _S62OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 3, 5),
    _S62OFFSETInt_Type()
)
s62OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s62OFFSETInt.setStatus("current")
_Sensor63setup_ObjectIdentity = ObjectIdentity
sensor63setup = _Sensor63setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 4)
)
_S63MAXInt_Type = SensorValue
_S63MAXInt_Object = MibScalar
s63MAXInt = _S63MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 4, 1),
    _S63MAXInt_Type()
)
s63MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s63MAXInt.setStatus("current")
_S63MINInt_Type = SensorValue
_S63MINInt_Object = MibScalar
s63MINInt = _S63MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 4, 2),
    _S63MINInt_Type()
)
s63MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s63MINInt.setStatus("current")
_S63HYSTInt_Type = SensorValue
_S63HYSTInt_Object = MibScalar
s63HYSTInt = _S63HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 6, 4, 3),
    _S63HYSTInt_Type()
)
s63HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s63HYSTInt.setStatus("current")
_Sensor7setup_ObjectIdentity = ObjectIdentity
sensor7setup = _Sensor7setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 1),
    _S7description_Type()
)
s7description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s7description.setStatus("current")
_Sensor71setup_ObjectIdentity = ObjectIdentity
sensor71setup = _Sensor71setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 2)
)
_S71MAXInt_Type = SensorValue
_S71MAXInt_Object = MibScalar
s71MAXInt = _S71MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 2, 1),
    _S71MAXInt_Type()
)
s71MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71MAXInt.setStatus("current")
_S71MINInt_Type = SensorValue
_S71MINInt_Object = MibScalar
s71MINInt = _S71MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 2, 2),
    _S71MINInt_Type()
)
s71MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71MINInt.setStatus("current")
_S71HYSTInt_Type = SensorValue
_S71HYSTInt_Object = MibScalar
s71HYSTInt = _S71HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 2, 3),
    _S71HYSTInt_Type()
)
s71HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71HYSTInt.setStatus("current")
_S71MULTInt_Type = SensorValue
_S71MULTInt_Object = MibScalar
s71MULTInt = _S71MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 2, 4),
    _S71MULTInt_Type()
)
s71MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71MULTInt.setStatus("current")
_S71OFFSETInt_Type = SensorValue
_S71OFFSETInt_Object = MibScalar
s71OFFSETInt = _S71OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 2, 5),
    _S71OFFSETInt_Type()
)
s71OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s71OFFSETInt.setStatus("current")
_Sensor72setup_ObjectIdentity = ObjectIdentity
sensor72setup = _Sensor72setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 3)
)
_S72MAXInt_Type = SensorValue
_S72MAXInt_Object = MibScalar
s72MAXInt = _S72MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 3, 1),
    _S72MAXInt_Type()
)
s72MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72MAXInt.setStatus("current")
_S72MINInt_Type = SensorValue
_S72MINInt_Object = MibScalar
s72MINInt = _S72MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 3, 2),
    _S72MINInt_Type()
)
s72MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72MINInt.setStatus("current")
_S72HYSTInt_Type = SensorValue
_S72HYSTInt_Object = MibScalar
s72HYSTInt = _S72HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 3, 3),
    _S72HYSTInt_Type()
)
s72HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72HYSTInt.setStatus("current")
_S72MULTInt_Type = SensorValue
_S72MULTInt_Object = MibScalar
s72MULTInt = _S72MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 3, 4),
    _S72MULTInt_Type()
)
s72MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72MULTInt.setStatus("current")
_S72OFFSETInt_Type = SensorValue
_S72OFFSETInt_Object = MibScalar
s72OFFSETInt = _S72OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 3, 5),
    _S72OFFSETInt_Type()
)
s72OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s72OFFSETInt.setStatus("current")
_Sensor73setup_ObjectIdentity = ObjectIdentity
sensor73setup = _Sensor73setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 4)
)
_S73MAXInt_Type = SensorValue
_S73MAXInt_Object = MibScalar
s73MAXInt = _S73MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 4, 1),
    _S73MAXInt_Type()
)
s73MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s73MAXInt.setStatus("current")
_S73MINInt_Type = SensorValue
_S73MINInt_Object = MibScalar
s73MINInt = _S73MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 4, 2),
    _S73MINInt_Type()
)
s73MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s73MINInt.setStatus("current")
_S73HYSTInt_Type = SensorValue
_S73HYSTInt_Object = MibScalar
s73HYSTInt = _S73HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 7, 4, 3),
    _S73HYSTInt_Type()
)
s73HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s73HYSTInt.setStatus("current")
_Sensor8setup_ObjectIdentity = ObjectIdentity
sensor8setup = _Sensor8setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8)
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 1),
    _S8description_Type()
)
s8description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s8description.setStatus("current")
_Sensor81setup_ObjectIdentity = ObjectIdentity
sensor81setup = _Sensor81setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 2)
)
_S81MAXInt_Type = SensorValue
_S81MAXInt_Object = MibScalar
s81MAXInt = _S81MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 2, 1),
    _S81MAXInt_Type()
)
s81MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81MAXInt.setStatus("current")
_S81MINInt_Type = SensorValue
_S81MINInt_Object = MibScalar
s81MINInt = _S81MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 2, 2),
    _S81MINInt_Type()
)
s81MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81MINInt.setStatus("current")
_S81HYSTInt_Type = SensorValue
_S81HYSTInt_Object = MibScalar
s81HYSTInt = _S81HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 2, 3),
    _S81HYSTInt_Type()
)
s81HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81HYSTInt.setStatus("current")
_S81MULTInt_Type = SensorValue
_S81MULTInt_Object = MibScalar
s81MULTInt = _S81MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 2, 4),
    _S81MULTInt_Type()
)
s81MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81MULTInt.setStatus("current")
_S81OFFSETInt_Type = SensorValue
_S81OFFSETInt_Object = MibScalar
s81OFFSETInt = _S81OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 2, 5),
    _S81OFFSETInt_Type()
)
s81OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s81OFFSETInt.setStatus("current")
_Sensor82setup_ObjectIdentity = ObjectIdentity
sensor82setup = _Sensor82setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 3)
)
_S82MAXInt_Type = SensorValue
_S82MAXInt_Object = MibScalar
s82MAXInt = _S82MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 3, 1),
    _S82MAXInt_Type()
)
s82MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82MAXInt.setStatus("current")
_S82MINInt_Type = SensorValue
_S82MINInt_Object = MibScalar
s82MINInt = _S82MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 3, 2),
    _S82MINInt_Type()
)
s82MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82MINInt.setStatus("current")
_S82HYSTInt_Type = SensorValue
_S82HYSTInt_Object = MibScalar
s82HYSTInt = _S82HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 3, 3),
    _S82HYSTInt_Type()
)
s82HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82HYSTInt.setStatus("current")
_S82MULTInt_Type = SensorValue
_S82MULTInt_Object = MibScalar
s82MULTInt = _S82MULTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 3, 4),
    _S82MULTInt_Type()
)
s82MULTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82MULTInt.setStatus("current")
_S82OFFSETInt_Type = SensorValue
_S82OFFSETInt_Object = MibScalar
s82OFFSETInt = _S82OFFSETInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 3, 5),
    _S82OFFSETInt_Type()
)
s82OFFSETInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s82OFFSETInt.setStatus("current")
_Sensor83setup_ObjectIdentity = ObjectIdentity
sensor83setup = _Sensor83setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 4)
)
_S83MAXInt_Type = SensorValue
_S83MAXInt_Object = MibScalar
s83MAXInt = _S83MAXInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 4, 1),
    _S83MAXInt_Type()
)
s83MAXInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s83MAXInt.setStatus("current")
_S83MINInt_Type = SensorValue
_S83MINInt_Object = MibScalar
s83MINInt = _S83MINInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 4, 2),
    _S83MINInt_Type()
)
s83MINInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s83MINInt.setStatus("current")
_S83HYSTInt_Type = SensorValue
_S83HYSTInt_Object = MibScalar
s83HYSTInt = _S83HYSTInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2, 2, 1, 8, 4, 3),
    _S83HYSTInt_Type()
)
s83HYSTInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s83HYSTInt.setStatus("current")
_MonitorNcontrol_ObjectIdentity = ObjectIdentity
monitorNcontrol = _MonitorNcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1)
)
_Sensor1_ObjectIdentity = ObjectIdentity
sensor1 = _Sensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1)
)
_S11Int_Type = SensorValue
_S11Int_Object = MibScalar
s11Int = _S11Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 1),
    _S11Int_Type()
)
s11Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s11Int.setStatus("current")
_S12Int_Type = SensorValue
_S12Int_Object = MibScalar
s12Int = _S12Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 2),
    _S12Int_Type()
)
s12Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s12Int.setStatus("current")
_S13Int_Type = SensorValue
_S13Int_Object = MibScalar
s13Int = _S13Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 3),
    _S13Int_Type()
)
s13Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s13Int.setStatus("current")
_S1ID_Type = SensorId
_S1ID_Object = MibScalar
s1ID = _S1ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 4),
    _S1ID_Type()
)
s1ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s1ID.setStatus("current")
_S1Alarm_ObjectIdentity = ObjectIdentity
s1Alarm = _S1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 5)
)
_S11Al_Type = ALARMSTATUS
_S11Al_Object = MibScalar
s11Al = _S11Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 5, 1),
    _S11Al_Type()
)
s11Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s11Al.setStatus("current")
_S12Al_Type = ALARMSTATUS
_S12Al_Object = MibScalar
s12Al = _S12Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 5, 2),
    _S12Al_Type()
)
s12Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s12Al.setStatus("current")
_S13Al_Type = ALARMSTATUS
_S13Al_Object = MibScalar
s13Al = _S13Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 5, 3),
    _S13Al_Type()
)
s13Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s13Al.setStatus("current")
_S11RawInt_Type = SensorValue
_S11RawInt_Object = MibScalar
s11RawInt = _S11RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 6),
    _S11RawInt_Type()
)
s11RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s11RawInt.setStatus("current")
_S12RawInt_Type = SensorValue
_S12RawInt_Object = MibScalar
s12RawInt = _S12RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 1, 7),
    _S12RawInt_Type()
)
s12RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s12RawInt.setStatus("current")
_Sensor2_ObjectIdentity = ObjectIdentity
sensor2 = _Sensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2)
)
_S21Int_Type = SensorValue
_S21Int_Object = MibScalar
s21Int = _S21Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 1),
    _S21Int_Type()
)
s21Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s21Int.setStatus("current")
_S22Int_Type = SensorValue
_S22Int_Object = MibScalar
s22Int = _S22Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 2),
    _S22Int_Type()
)
s22Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s22Int.setStatus("current")
_S23Int_Type = SensorValue
_S23Int_Object = MibScalar
s23Int = _S23Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 3),
    _S23Int_Type()
)
s23Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s23Int.setStatus("current")
_S2ID_Type = SensorId
_S2ID_Object = MibScalar
s2ID = _S2ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 4),
    _S2ID_Type()
)
s2ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s2ID.setStatus("current")
_S2Alarm_ObjectIdentity = ObjectIdentity
s2Alarm = _S2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 5)
)
_S21Al_Type = ALARMSTATUS
_S21Al_Object = MibScalar
s21Al = _S21Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 5, 1),
    _S21Al_Type()
)
s21Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s21Al.setStatus("current")
_S22Al_Type = ALARMSTATUS
_S22Al_Object = MibScalar
s22Al = _S22Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 5, 2),
    _S22Al_Type()
)
s22Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s22Al.setStatus("current")
_S23Al_Type = ALARMSTATUS
_S23Al_Object = MibScalar
s23Al = _S23Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 5, 3),
    _S23Al_Type()
)
s23Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s23Al.setStatus("current")
_S21RawInt_Type = SensorValue
_S21RawInt_Object = MibScalar
s21RawInt = _S21RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 6),
    _S21RawInt_Type()
)
s21RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s21RawInt.setStatus("current")
_S22RawInt_Type = SensorValue
_S22RawInt_Object = MibScalar
s22RawInt = _S22RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 2, 7),
    _S22RawInt_Type()
)
s22RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s22RawInt.setStatus("current")
_Sensor3_ObjectIdentity = ObjectIdentity
sensor3 = _Sensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3)
)
_S31Int_Type = SensorValue
_S31Int_Object = MibScalar
s31Int = _S31Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 1),
    _S31Int_Type()
)
s31Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s31Int.setStatus("current")
_S32Int_Type = SensorValue
_S32Int_Object = MibScalar
s32Int = _S32Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 2),
    _S32Int_Type()
)
s32Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s32Int.setStatus("current")
_S33Int_Type = SensorValue
_S33Int_Object = MibScalar
s33Int = _S33Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 3),
    _S33Int_Type()
)
s33Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s33Int.setStatus("current")
_S3ID_Type = SensorId
_S3ID_Object = MibScalar
s3ID = _S3ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 4),
    _S3ID_Type()
)
s3ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3ID.setStatus("current")
_S3Alarm_ObjectIdentity = ObjectIdentity
s3Alarm = _S3Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 5)
)
_S31Al_Type = ALARMSTATUS
_S31Al_Object = MibScalar
s31Al = _S31Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 5, 1),
    _S31Al_Type()
)
s31Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s31Al.setStatus("current")
_S32Al_Type = ALARMSTATUS
_S32Al_Object = MibScalar
s32Al = _S32Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 5, 2),
    _S32Al_Type()
)
s32Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s32Al.setStatus("current")
_S33Al_Type = ALARMSTATUS
_S33Al_Object = MibScalar
s33Al = _S33Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 5, 3),
    _S33Al_Type()
)
s33Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s33Al.setStatus("current")
_S31RawInt_Type = SensorValue
_S31RawInt_Object = MibScalar
s31RawInt = _S31RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 6),
    _S31RawInt_Type()
)
s31RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s31RawInt.setStatus("current")
_S32RawInt_Type = SensorValue
_S32RawInt_Object = MibScalar
s32RawInt = _S32RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 3, 7),
    _S32RawInt_Type()
)
s32RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s32RawInt.setStatus("current")
_Sensor4_ObjectIdentity = ObjectIdentity
sensor4 = _Sensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4)
)
_S41Int_Type = SensorValue
_S41Int_Object = MibScalar
s41Int = _S41Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 1),
    _S41Int_Type()
)
s41Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s41Int.setStatus("current")
_S42Int_Type = SensorValue
_S42Int_Object = MibScalar
s42Int = _S42Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 2),
    _S42Int_Type()
)
s42Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s42Int.setStatus("current")
_S43Int_Type = SensorValue
_S43Int_Object = MibScalar
s43Int = _S43Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 3),
    _S43Int_Type()
)
s43Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s43Int.setStatus("current")
_S4ID_Type = SensorId
_S4ID_Object = MibScalar
s4ID = _S4ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 4),
    _S4ID_Type()
)
s4ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s4ID.setStatus("current")
_S4Alarm_ObjectIdentity = ObjectIdentity
s4Alarm = _S4Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 5)
)
_S41Al_Type = ALARMSTATUS
_S41Al_Object = MibScalar
s41Al = _S41Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 5, 1),
    _S41Al_Type()
)
s41Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s41Al.setStatus("current")
_S42Al_Type = ALARMSTATUS
_S42Al_Object = MibScalar
s42Al = _S42Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 5, 2),
    _S42Al_Type()
)
s42Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s42Al.setStatus("current")
_S43Al_Type = ALARMSTATUS
_S43Al_Object = MibScalar
s43Al = _S43Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 5, 3),
    _S43Al_Type()
)
s43Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s43Al.setStatus("current")
_S41RawInt_Type = SensorValue
_S41RawInt_Object = MibScalar
s41RawInt = _S41RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 6),
    _S41RawInt_Type()
)
s41RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s41RawInt.setStatus("current")
_S42RawInt_Type = SensorValue
_S42RawInt_Object = MibScalar
s42RawInt = _S42RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 4, 7),
    _S42RawInt_Type()
)
s42RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s42RawInt.setStatus("current")
_Sensor5_ObjectIdentity = ObjectIdentity
sensor5 = _Sensor5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5)
)
_S51Int_Type = SensorValue
_S51Int_Object = MibScalar
s51Int = _S51Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 1),
    _S51Int_Type()
)
s51Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s51Int.setStatus("current")
_S52Int_Type = SensorValue
_S52Int_Object = MibScalar
s52Int = _S52Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 2),
    _S52Int_Type()
)
s52Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s52Int.setStatus("current")
_S53Int_Type = SensorValue
_S53Int_Object = MibScalar
s53Int = _S53Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 3),
    _S53Int_Type()
)
s53Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s53Int.setStatus("current")
_S5ID_Type = SensorId
_S5ID_Object = MibScalar
s5ID = _S5ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 4),
    _S5ID_Type()
)
s5ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5ID.setStatus("current")
_S5Alarm_ObjectIdentity = ObjectIdentity
s5Alarm = _S5Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 5)
)
_S51Al_Type = ALARMSTATUS
_S51Al_Object = MibScalar
s51Al = _S51Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 5, 1),
    _S51Al_Type()
)
s51Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s51Al.setStatus("current")
_S52Al_Type = ALARMSTATUS
_S52Al_Object = MibScalar
s52Al = _S52Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 5, 2),
    _S52Al_Type()
)
s52Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s52Al.setStatus("current")
_S53Al_Type = ALARMSTATUS
_S53Al_Object = MibScalar
s53Al = _S53Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 5, 3),
    _S53Al_Type()
)
s53Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s53Al.setStatus("current")
_S51RawInt_Type = SensorValue
_S51RawInt_Object = MibScalar
s51RawInt = _S51RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 6),
    _S51RawInt_Type()
)
s51RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s51RawInt.setStatus("current")
_S52RawInt_Type = SensorValue
_S52RawInt_Object = MibScalar
s52RawInt = _S52RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 5, 7),
    _S52RawInt_Type()
)
s52RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s52RawInt.setStatus("current")
_Sensor6_ObjectIdentity = ObjectIdentity
sensor6 = _Sensor6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6)
)
_S61Int_Type = SensorValue
_S61Int_Object = MibScalar
s61Int = _S61Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 1),
    _S61Int_Type()
)
s61Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s61Int.setStatus("current")
_S62Int_Type = SensorValue
_S62Int_Object = MibScalar
s62Int = _S62Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 2),
    _S62Int_Type()
)
s62Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s62Int.setStatus("current")
_S63Int_Type = SensorValue
_S63Int_Object = MibScalar
s63Int = _S63Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 3),
    _S63Int_Type()
)
s63Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s63Int.setStatus("current")
_S6ID_Type = SensorId
_S6ID_Object = MibScalar
s6ID = _S6ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 4),
    _S6ID_Type()
)
s6ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s6ID.setStatus("current")
_S6Alarm_ObjectIdentity = ObjectIdentity
s6Alarm = _S6Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 5)
)
_S61Al_Type = ALARMSTATUS
_S61Al_Object = MibScalar
s61Al = _S61Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 5, 1),
    _S61Al_Type()
)
s61Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s61Al.setStatus("current")
_S62Al_Type = ALARMSTATUS
_S62Al_Object = MibScalar
s62Al = _S62Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 5, 2),
    _S62Al_Type()
)
s62Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s62Al.setStatus("current")
_S63Al_Type = ALARMSTATUS
_S63Al_Object = MibScalar
s63Al = _S63Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 5, 3),
    _S63Al_Type()
)
s63Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s63Al.setStatus("current")
_S61RawInt_Type = SensorValue
_S61RawInt_Object = MibScalar
s61RawInt = _S61RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 6),
    _S61RawInt_Type()
)
s61RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s61RawInt.setStatus("current")
_S62RawInt_Type = SensorValue
_S62RawInt_Object = MibScalar
s62RawInt = _S62RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 6, 7),
    _S62RawInt_Type()
)
s62RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s62RawInt.setStatus("current")
_Sensor7_ObjectIdentity = ObjectIdentity
sensor7 = _Sensor7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7)
)
_S71Int_Type = SensorValue
_S71Int_Object = MibScalar
s71Int = _S71Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 1),
    _S71Int_Type()
)
s71Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s71Int.setStatus("current")
_S72Int_Type = SensorValue
_S72Int_Object = MibScalar
s72Int = _S72Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 2),
    _S72Int_Type()
)
s72Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s72Int.setStatus("current")
_S73Int_Type = SensorValue
_S73Int_Object = MibScalar
s73Int = _S73Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 3),
    _S73Int_Type()
)
s73Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s73Int.setStatus("current")
_S7ID_Type = SensorId
_S7ID_Object = MibScalar
s7ID = _S7ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 4),
    _S7ID_Type()
)
s7ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s7ID.setStatus("current")
_S7Alarm_ObjectIdentity = ObjectIdentity
s7Alarm = _S7Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 5)
)
_S71Al_Type = ALARMSTATUS
_S71Al_Object = MibScalar
s71Al = _S71Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 5, 1),
    _S71Al_Type()
)
s71Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s71Al.setStatus("current")
_S72Al_Type = ALARMSTATUS
_S72Al_Object = MibScalar
s72Al = _S72Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 5, 2),
    _S72Al_Type()
)
s72Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s72Al.setStatus("current")
_S73Al_Type = ALARMSTATUS
_S73Al_Object = MibScalar
s73Al = _S73Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 5, 3),
    _S73Al_Type()
)
s73Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s73Al.setStatus("current")
_S71RawInt_Type = SensorValue
_S71RawInt_Object = MibScalar
s71RawInt = _S71RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 6),
    _S71RawInt_Type()
)
s71RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s71RawInt.setStatus("current")
_S72RawInt_Type = SensorValue
_S72RawInt_Object = MibScalar
s72RawInt = _S72RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 7, 7),
    _S72RawInt_Type()
)
s72RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s72RawInt.setStatus("current")
_Sensor8_ObjectIdentity = ObjectIdentity
sensor8 = _Sensor8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8)
)
_S81Int_Type = SensorValue
_S81Int_Object = MibScalar
s81Int = _S81Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 1),
    _S81Int_Type()
)
s81Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s81Int.setStatus("current")
_S82Int_Type = SensorValue
_S82Int_Object = MibScalar
s82Int = _S82Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 2),
    _S82Int_Type()
)
s82Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s82Int.setStatus("current")
_S83Int_Type = SensorValue
_S83Int_Object = MibScalar
s83Int = _S83Int_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 3),
    _S83Int_Type()
)
s83Int.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s83Int.setStatus("current")
_S8ID_Type = SensorId
_S8ID_Object = MibScalar
s8ID = _S8ID_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 4),
    _S8ID_Type()
)
s8ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s8ID.setStatus("current")
_S8Alarm_ObjectIdentity = ObjectIdentity
s8Alarm = _S8Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 5)
)
_S81Al_Type = ALARMSTATUS
_S81Al_Object = MibScalar
s81Al = _S81Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 5, 1),
    _S81Al_Type()
)
s81Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s81Al.setStatus("current")
_S82Al_Type = ALARMSTATUS
_S82Al_Object = MibScalar
s82Al = _S82Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 5, 2),
    _S82Al_Type()
)
s82Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s82Al.setStatus("current")
_S83Al_Type = ALARMSTATUS
_S83Al_Object = MibScalar
s83Al = _S83Al_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 5, 3),
    _S83Al_Type()
)
s83Al.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s83Al.setStatus("current")
_S81RawInt_Type = SensorValue
_S81RawInt_Object = MibScalar
s81RawInt = _S81RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 6),
    _S81RawInt_Type()
)
s81RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s81RawInt.setStatus("current")
_S82RawInt_Type = SensorValue
_S82RawInt_Object = MibScalar
s82RawInt = _S82RawInt_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 1, 8, 7),
    _S82RawInt_Type()
)
s82RawInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s82RawInt.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 38783, 4, 3, 8),
    _HardwareErr_Type()
)
hardwareErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareErr.setStatus("current")
_Tcw210thMIBConformance_ObjectIdentity = ObjectIdentity
tcw210thMIBConformance = _Tcw210thMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4)
)
_Tcw210thMIBCompliances_ObjectIdentity = ObjectIdentity
tcw210thMIBCompliances = _Tcw210thMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4, 1)
)
_Tcw210thMIBGroups_ObjectIdentity = ObjectIdentity
tcw210thMIBGroups = _Tcw210thMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4, 2)
)

# Managed Objects groups

tcw210thProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4, 2, 1)
)
tcw210thProductGroup.setObjects(
      *(("TERACOM-TCW210-TH-MIB", "name"),
        ("TERACOM-TCW210-TH-MIB", "version"),
        ("TERACOM-TCW210-TH-MIB", "dateTime"))
)
if mibBuilder.loadTexts:
    tcw210thProductGroup.setStatus("current")

tcw210thSetupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4, 2, 2)
)
tcw210thSetupGroup.setObjects(
      *(("TERACOM-TCW210-TH-MIB", "deviceID"),
        ("TERACOM-TCW210-TH-MIB", "hostName"),
        ("TERACOM-TCW210-TH-MIB", "deviceIP"),
        ("TERACOM-TCW210-TH-MIB", "s1description"),
        ("TERACOM-TCW210-TH-MIB", "s11MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s11MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s11HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s11MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s11OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s12MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s12MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s12HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s12MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s12OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s13MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s13MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s13HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s2description"),
        ("TERACOM-TCW210-TH-MIB", "s21MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s21MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s21HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s21MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s21OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s22MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s22MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s22HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s22MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s22OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s23MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s23MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s23HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s3description"),
        ("TERACOM-TCW210-TH-MIB", "s31MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s31MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s31HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s31MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s31OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s32MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s32MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s32HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s32MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s32OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s33MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s33MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s33HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s4description"),
        ("TERACOM-TCW210-TH-MIB", "s41MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s41MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s41HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s41MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s41OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s42MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s42MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s42HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s42MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s42OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s43MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s43MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s43HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s5description"),
        ("TERACOM-TCW210-TH-MIB", "s51MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s51MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s51HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s51MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s51OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s52MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s52MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s52HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s52MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s52OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s53MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s53MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s53HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s6description"),
        ("TERACOM-TCW210-TH-MIB", "s61MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s61MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s61HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s61MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s61OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s62MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s62MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s62HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s62MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s62OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s63MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s63MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s63HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s7description"),
        ("TERACOM-TCW210-TH-MIB", "s71MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s71MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s71HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s71MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s71OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s72MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s72MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s72HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s72MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s72OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s73MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s73MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s73HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s8description"),
        ("TERACOM-TCW210-TH-MIB", "s81MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s81MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s81HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s81MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s81OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s82MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s82MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s82HYSTInt"),
        ("TERACOM-TCW210-TH-MIB", "s82MULTInt"),
        ("TERACOM-TCW210-TH-MIB", "s82OFFSETInt"),
        ("TERACOM-TCW210-TH-MIB", "s83MAXInt"),
        ("TERACOM-TCW210-TH-MIB", "s83MINInt"),
        ("TERACOM-TCW210-TH-MIB", "s83HYSTInt"))
)
if mibBuilder.loadTexts:
    tcw210thSetupGroup.setStatus("current")

tcw210thMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4, 2, 3)
)
tcw210thMonitorGroup.setObjects(
      *(("TERACOM-TCW210-TH-MIB", "s11Int"),
        ("TERACOM-TCW210-TH-MIB", "s12Int"),
        ("TERACOM-TCW210-TH-MIB", "s13Int"),
        ("TERACOM-TCW210-TH-MIB", "s1ID"),
        ("TERACOM-TCW210-TH-MIB", "s11Al"),
        ("TERACOM-TCW210-TH-MIB", "s12Al"),
        ("TERACOM-TCW210-TH-MIB", "s13Al"),
        ("TERACOM-TCW210-TH-MIB", "s11RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s12RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s21Int"),
        ("TERACOM-TCW210-TH-MIB", "s22Int"),
        ("TERACOM-TCW210-TH-MIB", "s23Int"),
        ("TERACOM-TCW210-TH-MIB", "s2ID"),
        ("TERACOM-TCW210-TH-MIB", "s21Al"),
        ("TERACOM-TCW210-TH-MIB", "s22Al"),
        ("TERACOM-TCW210-TH-MIB", "s23Al"),
        ("TERACOM-TCW210-TH-MIB", "s21RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s22RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s31Int"),
        ("TERACOM-TCW210-TH-MIB", "s32Int"),
        ("TERACOM-TCW210-TH-MIB", "s33Int"),
        ("TERACOM-TCW210-TH-MIB", "s3ID"),
        ("TERACOM-TCW210-TH-MIB", "s31Al"),
        ("TERACOM-TCW210-TH-MIB", "s32Al"),
        ("TERACOM-TCW210-TH-MIB", "s33Al"),
        ("TERACOM-TCW210-TH-MIB", "s31RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s32RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s41Int"),
        ("TERACOM-TCW210-TH-MIB", "s42Int"),
        ("TERACOM-TCW210-TH-MIB", "s43Int"),
        ("TERACOM-TCW210-TH-MIB", "s4ID"),
        ("TERACOM-TCW210-TH-MIB", "s41Al"),
        ("TERACOM-TCW210-TH-MIB", "s42Al"),
        ("TERACOM-TCW210-TH-MIB", "s43Al"),
        ("TERACOM-TCW210-TH-MIB", "s41RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s42RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s51Int"),
        ("TERACOM-TCW210-TH-MIB", "s52Int"),
        ("TERACOM-TCW210-TH-MIB", "s53Int"),
        ("TERACOM-TCW210-TH-MIB", "s5ID"),
        ("TERACOM-TCW210-TH-MIB", "s51Al"),
        ("TERACOM-TCW210-TH-MIB", "s52Al"),
        ("TERACOM-TCW210-TH-MIB", "s53Al"),
        ("TERACOM-TCW210-TH-MIB", "s51RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s52RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s61Int"),
        ("TERACOM-TCW210-TH-MIB", "s62Int"),
        ("TERACOM-TCW210-TH-MIB", "s63Int"),
        ("TERACOM-TCW210-TH-MIB", "s6ID"),
        ("TERACOM-TCW210-TH-MIB", "s61Al"),
        ("TERACOM-TCW210-TH-MIB", "s62Al"),
        ("TERACOM-TCW210-TH-MIB", "s63Al"),
        ("TERACOM-TCW210-TH-MIB", "s61RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s62RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s71Int"),
        ("TERACOM-TCW210-TH-MIB", "s72Int"),
        ("TERACOM-TCW210-TH-MIB", "s73Int"),
        ("TERACOM-TCW210-TH-MIB", "s7ID"),
        ("TERACOM-TCW210-TH-MIB", "s71Al"),
        ("TERACOM-TCW210-TH-MIB", "s72Al"),
        ("TERACOM-TCW210-TH-MIB", "s73Al"),
        ("TERACOM-TCW210-TH-MIB", "s71RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s72RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s81Int"),
        ("TERACOM-TCW210-TH-MIB", "s82Int"),
        ("TERACOM-TCW210-TH-MIB", "s83Int"),
        ("TERACOM-TCW210-TH-MIB", "s8ID"),
        ("TERACOM-TCW210-TH-MIB", "s81Al"),
        ("TERACOM-TCW210-TH-MIB", "s82Al"),
        ("TERACOM-TCW210-TH-MIB", "s83Al"),
        ("TERACOM-TCW210-TH-MIB", "s81RawInt"),
        ("TERACOM-TCW210-TH-MIB", "s82RawInt"),
        ("TERACOM-TCW210-TH-MIB", "configurationSaved"),
        ("TERACOM-TCW210-TH-MIB", "restartDevice"),
        ("TERACOM-TCW210-TH-MIB", "temperatureUnit"),
        ("TERACOM-TCW210-TH-MIB", "hardwareErr"))
)
if mibBuilder.loadTexts:
    tcw210thMonitorGroup.setStatus("current")


# Notification objects

snmp_trap_notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 38783, 4, 0, 1)
)
snmp_trap_notification.setObjects(
      *(("TERACOM-TCW210-TH-MIB", "s11Int"),
        ("TERACOM-TCW210-TH-MIB", "s12Int"),
        ("TERACOM-TCW210-TH-MIB", "s13Int"),
        ("TERACOM-TCW210-TH-MIB", "s11Al"),
        ("TERACOM-TCW210-TH-MIB", "s12Al"),
        ("TERACOM-TCW210-TH-MIB", "s13Al"),
        ("TERACOM-TCW210-TH-MIB", "s21Int"),
        ("TERACOM-TCW210-TH-MIB", "s22Int"),
        ("TERACOM-TCW210-TH-MIB", "s23Int"),
        ("TERACOM-TCW210-TH-MIB", "s21Al"),
        ("TERACOM-TCW210-TH-MIB", "s22Al"),
        ("TERACOM-TCW210-TH-MIB", "s23Al"),
        ("TERACOM-TCW210-TH-MIB", "s31Int"),
        ("TERACOM-TCW210-TH-MIB", "s32Int"),
        ("TERACOM-TCW210-TH-MIB", "s33Int"),
        ("TERACOM-TCW210-TH-MIB", "s31Al"),
        ("TERACOM-TCW210-TH-MIB", "s32Al"),
        ("TERACOM-TCW210-TH-MIB", "s33Al"),
        ("TERACOM-TCW210-TH-MIB", "s41Int"),
        ("TERACOM-TCW210-TH-MIB", "s42Int"),
        ("TERACOM-TCW210-TH-MIB", "s43Int"),
        ("TERACOM-TCW210-TH-MIB", "s41Al"),
        ("TERACOM-TCW210-TH-MIB", "s42Al"),
        ("TERACOM-TCW210-TH-MIB", "s43Al"),
        ("TERACOM-TCW210-TH-MIB", "s51Int"),
        ("TERACOM-TCW210-TH-MIB", "s52Int"),
        ("TERACOM-TCW210-TH-MIB", "s53Int"),
        ("TERACOM-TCW210-TH-MIB", "s51Al"),
        ("TERACOM-TCW210-TH-MIB", "s52Al"),
        ("TERACOM-TCW210-TH-MIB", "s53Al"),
        ("TERACOM-TCW210-TH-MIB", "s61Int"),
        ("TERACOM-TCW210-TH-MIB", "s62Int"),
        ("TERACOM-TCW210-TH-MIB", "s63Int"),
        ("TERACOM-TCW210-TH-MIB", "s61Al"),
        ("TERACOM-TCW210-TH-MIB", "s62Al"),
        ("TERACOM-TCW210-TH-MIB", "s63Al"),
        ("TERACOM-TCW210-TH-MIB", "s71Int"),
        ("TERACOM-TCW210-TH-MIB", "s72Int"),
        ("TERACOM-TCW210-TH-MIB", "s73Int"),
        ("TERACOM-TCW210-TH-MIB", "s71Al"),
        ("TERACOM-TCW210-TH-MIB", "s72Al"),
        ("TERACOM-TCW210-TH-MIB", "s73Al"),
        ("TERACOM-TCW210-TH-MIB", "s81Int"),
        ("TERACOM-TCW210-TH-MIB", "s82Int"),
        ("TERACOM-TCW210-TH-MIB", "s83Int"),
        ("TERACOM-TCW210-TH-MIB", "s81Al"),
        ("TERACOM-TCW210-TH-MIB", "s82Al"),
        ("TERACOM-TCW210-TH-MIB", "s83Al"),
        ("TERACOM-TCW210-TH-MIB", "restartDevice"),
        ("TERACOM-TCW210-TH-MIB", "deviceIP"))
)
if mibBuilder.loadTexts:
    snmp_trap_notification.setStatus(
        "current"
    )


# Notifications groups

tcw210thTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4, 2, 4)
)
tcw210thTrapGroup.setObjects(
    ("TERACOM-TCW210-TH-MIB", "snmp-trap-notification")
)
if mibBuilder.loadTexts:
    tcw210thTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tcw210thMIBCompliances1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4, 1, 1)
)
tcw210thMIBCompliances1.setObjects(
      *(("TERACOM-TCW210-TH-MIB", "tcw210thProductGroup"),
        ("TERACOM-TCW210-TH-MIB", "tcw210thSetupGroup"),
        ("TERACOM-TCW210-TH-MIB", "tcw210thMonitorGroup"),
        ("TERACOM-TCW210-TH-MIB", "tcw210thTrapGroup"))
)
if mibBuilder.loadTexts:
    tcw210thMIBCompliances1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERACOM-TCW210-TH-MIB",
    **{"SensorId": SensorId,
       "SensorValue": SensorValue,
       "ALARMSTATUS": ALARMSTATUS,
       "teracom": teracom,
       "tcw210th": tcw210th,
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
       "s11MULTInt": s11MULTInt,
       "s11OFFSETInt": s11OFFSETInt,
       "sensor12setup": sensor12setup,
       "s12MAXInt": s12MAXInt,
       "s12MINInt": s12MINInt,
       "s12HYSTInt": s12HYSTInt,
       "s12MULTInt": s12MULTInt,
       "s12OFFSETInt": s12OFFSETInt,
       "sensor13setup": sensor13setup,
       "s13MAXInt": s13MAXInt,
       "s13MINInt": s13MINInt,
       "s13HYSTInt": s13HYSTInt,
       "sensor2setup": sensor2setup,
       "s2description": s2description,
       "sensor21setup": sensor21setup,
       "s21MAXInt": s21MAXInt,
       "s21MINInt": s21MINInt,
       "s21HYSTInt": s21HYSTInt,
       "s21MULTInt": s21MULTInt,
       "s21OFFSETInt": s21OFFSETInt,
       "sensor22setup": sensor22setup,
       "s22MAXInt": s22MAXInt,
       "s22MINInt": s22MINInt,
       "s22HYSTInt": s22HYSTInt,
       "s22MULTInt": s22MULTInt,
       "s22OFFSETInt": s22OFFSETInt,
       "sensor23setup": sensor23setup,
       "s23MAXInt": s23MAXInt,
       "s23MINInt": s23MINInt,
       "s23HYSTInt": s23HYSTInt,
       "sensor3setup": sensor3setup,
       "s3description": s3description,
       "sensor31setup": sensor31setup,
       "s31MAXInt": s31MAXInt,
       "s31MINInt": s31MINInt,
       "s31HYSTInt": s31HYSTInt,
       "s31MULTInt": s31MULTInt,
       "s31OFFSETInt": s31OFFSETInt,
       "sensor32setup": sensor32setup,
       "s32MAXInt": s32MAXInt,
       "s32MINInt": s32MINInt,
       "s32HYSTInt": s32HYSTInt,
       "s32MULTInt": s32MULTInt,
       "s32OFFSETInt": s32OFFSETInt,
       "sensor33setup": sensor33setup,
       "s33MAXInt": s33MAXInt,
       "s33MINInt": s33MINInt,
       "s33HYSTInt": s33HYSTInt,
       "sensor4setup": sensor4setup,
       "s4description": s4description,
       "sensor41setup": sensor41setup,
       "s41MAXInt": s41MAXInt,
       "s41MINInt": s41MINInt,
       "s41HYSTInt": s41HYSTInt,
       "s41MULTInt": s41MULTInt,
       "s41OFFSETInt": s41OFFSETInt,
       "sensor42setup": sensor42setup,
       "s42MAXInt": s42MAXInt,
       "s42MINInt": s42MINInt,
       "s42HYSTInt": s42HYSTInt,
       "s42MULTInt": s42MULTInt,
       "s42OFFSETInt": s42OFFSETInt,
       "sensor43setup": sensor43setup,
       "s43MAXInt": s43MAXInt,
       "s43MINInt": s43MINInt,
       "s43HYSTInt": s43HYSTInt,
       "sensor5setup": sensor5setup,
       "s5description": s5description,
       "sensor51setup": sensor51setup,
       "s51MAXInt": s51MAXInt,
       "s51MINInt": s51MINInt,
       "s51HYSTInt": s51HYSTInt,
       "s51MULTInt": s51MULTInt,
       "s51OFFSETInt": s51OFFSETInt,
       "sensor52setup": sensor52setup,
       "s52MAXInt": s52MAXInt,
       "s52MINInt": s52MINInt,
       "s52HYSTInt": s52HYSTInt,
       "s52MULTInt": s52MULTInt,
       "s52OFFSETInt": s52OFFSETInt,
       "sensor53setup": sensor53setup,
       "s53MAXInt": s53MAXInt,
       "s53MINInt": s53MINInt,
       "s53HYSTInt": s53HYSTInt,
       "sensor6setup": sensor6setup,
       "s6description": s6description,
       "sensor61setup": sensor61setup,
       "s61MAXInt": s61MAXInt,
       "s61MINInt": s61MINInt,
       "s61HYSTInt": s61HYSTInt,
       "s61MULTInt": s61MULTInt,
       "s61OFFSETInt": s61OFFSETInt,
       "sensor62setup": sensor62setup,
       "s62MAXInt": s62MAXInt,
       "s62MINInt": s62MINInt,
       "s62HYSTInt": s62HYSTInt,
       "s62MULTInt": s62MULTInt,
       "s62OFFSETInt": s62OFFSETInt,
       "sensor63setup": sensor63setup,
       "s63MAXInt": s63MAXInt,
       "s63MINInt": s63MINInt,
       "s63HYSTInt": s63HYSTInt,
       "sensor7setup": sensor7setup,
       "s7description": s7description,
       "sensor71setup": sensor71setup,
       "s71MAXInt": s71MAXInt,
       "s71MINInt": s71MINInt,
       "s71HYSTInt": s71HYSTInt,
       "s71MULTInt": s71MULTInt,
       "s71OFFSETInt": s71OFFSETInt,
       "sensor72setup": sensor72setup,
       "s72MAXInt": s72MAXInt,
       "s72MINInt": s72MINInt,
       "s72HYSTInt": s72HYSTInt,
       "s72MULTInt": s72MULTInt,
       "s72OFFSETInt": s72OFFSETInt,
       "sensor73setup": sensor73setup,
       "s73MAXInt": s73MAXInt,
       "s73MINInt": s73MINInt,
       "s73HYSTInt": s73HYSTInt,
       "sensor8setup": sensor8setup,
       "s8description": s8description,
       "sensor81setup": sensor81setup,
       "s81MAXInt": s81MAXInt,
       "s81MINInt": s81MINInt,
       "s81HYSTInt": s81HYSTInt,
       "s81MULTInt": s81MULTInt,
       "s81OFFSETInt": s81OFFSETInt,
       "sensor82setup": sensor82setup,
       "s82MAXInt": s82MAXInt,
       "s82MINInt": s82MINInt,
       "s82HYSTInt": s82HYSTInt,
       "s82MULTInt": s82MULTInt,
       "s82OFFSETInt": s82OFFSETInt,
       "sensor83setup": sensor83setup,
       "s83MAXInt": s83MAXInt,
       "s83MINInt": s83MINInt,
       "s83HYSTInt": s83HYSTInt,
       "monitorNcontrol": monitorNcontrol,
       "sensors": sensors,
       "sensor1": sensor1,
       "s11Int": s11Int,
       "s12Int": s12Int,
       "s13Int": s13Int,
       "s1ID": s1ID,
       "s1Alarm": s1Alarm,
       "s11Al": s11Al,
       "s12Al": s12Al,
       "s13Al": s13Al,
       "s11RawInt": s11RawInt,
       "s12RawInt": s12RawInt,
       "sensor2": sensor2,
       "s21Int": s21Int,
       "s22Int": s22Int,
       "s23Int": s23Int,
       "s2ID": s2ID,
       "s2Alarm": s2Alarm,
       "s21Al": s21Al,
       "s22Al": s22Al,
       "s23Al": s23Al,
       "s21RawInt": s21RawInt,
       "s22RawInt": s22RawInt,
       "sensor3": sensor3,
       "s31Int": s31Int,
       "s32Int": s32Int,
       "s33Int": s33Int,
       "s3ID": s3ID,
       "s3Alarm": s3Alarm,
       "s31Al": s31Al,
       "s32Al": s32Al,
       "s33Al": s33Al,
       "s31RawInt": s31RawInt,
       "s32RawInt": s32RawInt,
       "sensor4": sensor4,
       "s41Int": s41Int,
       "s42Int": s42Int,
       "s43Int": s43Int,
       "s4ID": s4ID,
       "s4Alarm": s4Alarm,
       "s41Al": s41Al,
       "s42Al": s42Al,
       "s43Al": s43Al,
       "s41RawInt": s41RawInt,
       "s42RawInt": s42RawInt,
       "sensor5": sensor5,
       "s51Int": s51Int,
       "s52Int": s52Int,
       "s53Int": s53Int,
       "s5ID": s5ID,
       "s5Alarm": s5Alarm,
       "s51Al": s51Al,
       "s52Al": s52Al,
       "s53Al": s53Al,
       "s51RawInt": s51RawInt,
       "s52RawInt": s52RawInt,
       "sensor6": sensor6,
       "s61Int": s61Int,
       "s62Int": s62Int,
       "s63Int": s63Int,
       "s6ID": s6ID,
       "s6Alarm": s6Alarm,
       "s61Al": s61Al,
       "s62Al": s62Al,
       "s63Al": s63Al,
       "s61RawInt": s61RawInt,
       "s62RawInt": s62RawInt,
       "sensor7": sensor7,
       "s71Int": s71Int,
       "s72Int": s72Int,
       "s73Int": s73Int,
       "s7ID": s7ID,
       "s7Alarm": s7Alarm,
       "s71Al": s71Al,
       "s72Al": s72Al,
       "s73Al": s73Al,
       "s71RawInt": s71RawInt,
       "s72RawInt": s72RawInt,
       "sensor8": sensor8,
       "s81Int": s81Int,
       "s82Int": s82Int,
       "s83Int": s83Int,
       "s8ID": s8ID,
       "s8Alarm": s8Alarm,
       "s81Al": s81Al,
       "s82Al": s82Al,
       "s83Al": s83Al,
       "s81RawInt": s81RawInt,
       "s82RawInt": s82RawInt,
       "configurationSaved": configurationSaved,
       "restartDevice": restartDevice,
       "temperatureUnit": temperatureUnit,
       "hardwareErr": hardwareErr,
       "tcw210thMIBConformance": tcw210thMIBConformance,
       "tcw210thMIBCompliances": tcw210thMIBCompliances,
       "tcw210thMIBCompliances1": tcw210thMIBCompliances1,
       "tcw210thMIBGroups": tcw210thMIBGroups,
       "tcw210thProductGroup": tcw210thProductGroup,
       "tcw210thSetupGroup": tcw210thSetupGroup,
       "tcw210thMonitorGroup": tcw210thMonitorGroup,
       "tcw210thTrapGroup": tcw210thTrapGroup,
       "snmpMIB": snmpMIB}
)
