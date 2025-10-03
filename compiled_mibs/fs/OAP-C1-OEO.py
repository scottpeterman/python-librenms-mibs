# SNMP MIB module (OAP-C1-OEO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\OAP-C1-OEO
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:03 2025
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

tryin = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40989)
)
if mibBuilder.loadTexts:
    tryin.setRevisions(
        ("2015-05-08 17:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10)
)
_Oap_ObjectIdentity = ObjectIdentity
oap = _Oap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16)
)
_Card1_ObjectIdentity = ObjectIdentity
card1 = _Card1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1)
)
_Oeo_ObjectIdentity = ObjectIdentity
oeo = _Oeo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2)
)


class _VCardState_Type(Integer32):
    """Custom type vCardState based on Integer32"""
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


_VCardState_Type.__name__ = "Integer32"
_VCardState_Object = MibScalar
vCardState = _VCardState_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 1),
    _VCardState_Type()
)
vCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCardState.setStatus("current")
_VDeviceType_Type = OctetString
_VDeviceType_Object = MibScalar
vDeviceType = _VDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 2),
    _VDeviceType_Type()
)
vDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDeviceType.setStatus("current")
_VDeviceDescription_Type = OctetString
_VDeviceDescription_Object = MibScalar
vDeviceDescription = _VDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 3),
    _VDeviceDescription_Type()
)
vDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vDeviceDescription.setStatus("current")
_VSoftwareVerion_Type = OctetString
_VSoftwareVerion_Object = MibScalar
vSoftwareVerion = _VSoftwareVerion_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 4),
    _VSoftwareVerion_Type()
)
vSoftwareVerion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSoftwareVerion.setStatus("current")
_VHardwareVerion_Type = OctetString
_VHardwareVerion_Object = MibScalar
vHardwareVerion = _VHardwareVerion_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 5),
    _VHardwareVerion_Type()
)
vHardwareVerion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vHardwareVerion.setStatus("current")
_VSerialNumber_Type = OctetString
_VSerialNumber_Object = MibScalar
vSerialNumber = _VSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 6),
    _VSerialNumber_Type()
)
vSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSerialNumber.setStatus("current")
_VFactoryDate_Type = OctetString
_VFactoryDate_Object = MibScalar
vFactoryDate = _VFactoryDate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 7),
    _VFactoryDate_Type()
)
vFactoryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vFactoryDate.setStatus("current")
_VSFPA1_ObjectIdentity = ObjectIdentity
vSFPA1 = _VSFPA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11)
)


class _VSFPA1State_Type(Integer32):
    """Custom type vSFPA1State based on Integer32"""
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


_VSFPA1State_Type.__name__ = "Integer32"
_VSFPA1State_Object = MibScalar
vSFPA1State = _VSFPA1State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 1),
    _VSFPA1State_Type()
)
vSFPA1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1State.setStatus("current")


class _VSFPA1WorkMode_Type(Integer32):
    """Custom type vSFPA1WorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loopback", 3))
    )


_VSFPA1WorkMode_Type.__name__ = "Integer32"
_VSFPA1WorkMode_Object = MibScalar
vSFPA1WorkMode = _VSFPA1WorkMode_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 2),
    _VSFPA1WorkMode_Type()
)
vSFPA1WorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPA1WorkMode.setStatus("current")


class _VSFPA1TxPowerControl_Type(Integer32):
    """Custom type vSFPA1TxPowerControl based on Integer32"""
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
          ("auto", 2))
    )


_VSFPA1TxPowerControl_Type.__name__ = "Integer32"
_VSFPA1TxPowerControl_Object = MibScalar
vSFPA1TxPowerControl = _VSFPA1TxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 3),
    _VSFPA1TxPowerControl_Type()
)
vSFPA1TxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPA1TxPowerControl.setStatus("current")
_VSFPA1TxPower_Type = Integer32
_VSFPA1TxPower_Object = MibScalar
vSFPA1TxPower = _VSFPA1TxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 4),
    _VSFPA1TxPower_Type()
)
vSFPA1TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1TxPower.setStatus("current")
_VSFPA1RxPower_Type = Integer32
_VSFPA1RxPower_Object = MibScalar
vSFPA1RxPower = _VSFPA1RxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 5),
    _VSFPA1RxPower_Type()
)
vSFPA1RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1RxPower.setStatus("current")
_VSFPA1ModeWave_Type = Integer32
_VSFPA1ModeWave_Object = MibScalar
vSFPA1ModeWave = _VSFPA1ModeWave_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 6),
    _VSFPA1ModeWave_Type()
)
vSFPA1ModeWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1ModeWave.setStatus("current")


class _VSFPA1ModeTransmissionDistance_Type(Integer32):
    """Custom type vSFPA1ModeTransmissionDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPA1ModeTransmissionDistance_Type.__name__ = "Integer32"
_VSFPA1ModeTransmissionDistance_Object = MibScalar
vSFPA1ModeTransmissionDistance = _VSFPA1ModeTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 7),
    _VSFPA1ModeTransmissionDistance_Type()
)
vSFPA1ModeTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1ModeTransmissionDistance.setStatus("current")
_VSFPA1ModeTransmissionRate_Type = Integer32
_VSFPA1ModeTransmissionRate_Object = MibScalar
vSFPA1ModeTransmissionRate = _VSFPA1ModeTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 8),
    _VSFPA1ModeTransmissionRate_Type()
)
vSFPA1ModeTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1ModeTransmissionRate.setStatus("current")


class _VSFPA1ModeTemperature_Type(Integer32):
    """Custom type vSFPA1ModeTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPA1ModeTemperature_Type.__name__ = "Integer32"
_VSFPA1ModeTemperature_Object = MibScalar
vSFPA1ModeTemperature = _VSFPA1ModeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 9),
    _VSFPA1ModeTemperature_Type()
)
vSFPA1ModeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1ModeTemperature.setStatus("current")


class _VSFPA1TxPowerAlarm_Type(Integer32):
    """Custom type vSFPA1TxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPA1TxPowerAlarm_Type.__name__ = "Integer32"
_VSFPA1TxPowerAlarm_Object = MibScalar
vSFPA1TxPowerAlarm = _VSFPA1TxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 10),
    _VSFPA1TxPowerAlarm_Type()
)
vSFPA1TxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1TxPowerAlarm.setStatus("current")


class _VSFPA1RxPowerAlarm_Type(Integer32):
    """Custom type vSFPA1RxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPA1RxPowerAlarm_Type.__name__ = "Integer32"
_VSFPA1RxPowerAlarm_Object = MibScalar
vSFPA1RxPowerAlarm = _VSFPA1RxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 11),
    _VSFPA1RxPowerAlarm_Type()
)
vSFPA1RxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1RxPowerAlarm.setStatus("current")


class _VSFPA1ModeTemperatureAlarm_Type(Integer32):
    """Custom type vSFPA1ModeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPA1ModeTemperatureAlarm_Type.__name__ = "Integer32"
_VSFPA1ModeTemperatureAlarm_Object = MibScalar
vSFPA1ModeTemperatureAlarm = _VSFPA1ModeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 12),
    _VSFPA1ModeTemperatureAlarm_Type()
)
vSFPA1ModeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA1ModeTemperatureAlarm.setStatus("current")
_VSFPA1RxPowerThreshold_Type = Integer32
_VSFPA1RxPowerThreshold_Object = MibScalar
vSFPA1RxPowerThreshold = _VSFPA1RxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 11, 13),
    _VSFPA1RxPowerThreshold_Type()
)
vSFPA1RxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPA1RxPowerThreshold.setStatus("current")
_VSFPA2_ObjectIdentity = ObjectIdentity
vSFPA2 = _VSFPA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12)
)


class _VSFPA2State_Type(Integer32):
    """Custom type vSFPA2State based on Integer32"""
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


_VSFPA2State_Type.__name__ = "Integer32"
_VSFPA2State_Object = MibScalar
vSFPA2State = _VSFPA2State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 1),
    _VSFPA2State_Type()
)
vSFPA2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2State.setStatus("current")


class _VSFPA2WorkMode_Type(Integer32):
    """Custom type vSFPA2WorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loopback", 3))
    )


_VSFPA2WorkMode_Type.__name__ = "Integer32"
_VSFPA2WorkMode_Object = MibScalar
vSFPA2WorkMode = _VSFPA2WorkMode_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 2),
    _VSFPA2WorkMode_Type()
)
vSFPA2WorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPA2WorkMode.setStatus("current")


class _VSFPA2TxPowerControl_Type(Integer32):
    """Custom type vSFPA2TxPowerControl based on Integer32"""
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
          ("auto", 2))
    )


_VSFPA2TxPowerControl_Type.__name__ = "Integer32"
_VSFPA2TxPowerControl_Object = MibScalar
vSFPA2TxPowerControl = _VSFPA2TxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 3),
    _VSFPA2TxPowerControl_Type()
)
vSFPA2TxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPA2TxPowerControl.setStatus("current")
_VSFPA2TxPower_Type = Integer32
_VSFPA2TxPower_Object = MibScalar
vSFPA2TxPower = _VSFPA2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 4),
    _VSFPA2TxPower_Type()
)
vSFPA2TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2TxPower.setStatus("current")
_VSFPA2RxPower_Type = Integer32
_VSFPA2RxPower_Object = MibScalar
vSFPA2RxPower = _VSFPA2RxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 5),
    _VSFPA2RxPower_Type()
)
vSFPA2RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2RxPower.setStatus("current")
_VSFPA2ModeWave_Type = Integer32
_VSFPA2ModeWave_Object = MibScalar
vSFPA2ModeWave = _VSFPA2ModeWave_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 6),
    _VSFPA2ModeWave_Type()
)
vSFPA2ModeWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2ModeWave.setStatus("current")


class _VSFPA2ModeTransmissionDistance_Type(Integer32):
    """Custom type vSFPA2ModeTransmissionDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPA2ModeTransmissionDistance_Type.__name__ = "Integer32"
_VSFPA2ModeTransmissionDistance_Object = MibScalar
vSFPA2ModeTransmissionDistance = _VSFPA2ModeTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 7),
    _VSFPA2ModeTransmissionDistance_Type()
)
vSFPA2ModeTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2ModeTransmissionDistance.setStatus("current")
_VSFPA2ModeTransmissionRate_Type = Integer32
_VSFPA2ModeTransmissionRate_Object = MibScalar
vSFPA2ModeTransmissionRate = _VSFPA2ModeTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 8),
    _VSFPA2ModeTransmissionRate_Type()
)
vSFPA2ModeTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2ModeTransmissionRate.setStatus("current")


class _VSFPA2ModeTemperature_Type(Integer32):
    """Custom type vSFPA2ModeTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPA2ModeTemperature_Type.__name__ = "Integer32"
_VSFPA2ModeTemperature_Object = MibScalar
vSFPA2ModeTemperature = _VSFPA2ModeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 9),
    _VSFPA2ModeTemperature_Type()
)
vSFPA2ModeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2ModeTemperature.setStatus("current")


class _VSFPA2TxPowerAlarm_Type(Integer32):
    """Custom type vSFPA2TxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPA2TxPowerAlarm_Type.__name__ = "Integer32"
_VSFPA2TxPowerAlarm_Object = MibScalar
vSFPA2TxPowerAlarm = _VSFPA2TxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 10),
    _VSFPA2TxPowerAlarm_Type()
)
vSFPA2TxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2TxPowerAlarm.setStatus("current")


class _VSFPA2RxPowerAlarm_Type(Integer32):
    """Custom type vSFPA2RxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPA2RxPowerAlarm_Type.__name__ = "Integer32"
_VSFPA2RxPowerAlarm_Object = MibScalar
vSFPA2RxPowerAlarm = _VSFPA2RxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 11),
    _VSFPA2RxPowerAlarm_Type()
)
vSFPA2RxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2RxPowerAlarm.setStatus("current")


class _VSFPA2ModeTemperatureAlarm_Type(Integer32):
    """Custom type vSFPA2ModeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPA2ModeTemperatureAlarm_Type.__name__ = "Integer32"
_VSFPA2ModeTemperatureAlarm_Object = MibScalar
vSFPA2ModeTemperatureAlarm = _VSFPA2ModeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 12),
    _VSFPA2ModeTemperatureAlarm_Type()
)
vSFPA2ModeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPA2ModeTemperatureAlarm.setStatus("current")
_VSFPA2RxPowerThreshold_Type = Integer32
_VSFPA2RxPowerThreshold_Object = MibScalar
vSFPA2RxPowerThreshold = _VSFPA2RxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 12, 13),
    _VSFPA2RxPowerThreshold_Type()
)
vSFPA2RxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPA2RxPowerThreshold.setStatus("current")
_VSFPB1_ObjectIdentity = ObjectIdentity
vSFPB1 = _VSFPB1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13)
)


class _VSFPB1State_Type(Integer32):
    """Custom type vSFPB1State based on Integer32"""
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


_VSFPB1State_Type.__name__ = "Integer32"
_VSFPB1State_Object = MibScalar
vSFPB1State = _VSFPB1State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 1),
    _VSFPB1State_Type()
)
vSFPB1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1State.setStatus("current")


class _VSFPB1WorkMode_Type(Integer32):
    """Custom type vSFPB1WorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loopback", 3))
    )


_VSFPB1WorkMode_Type.__name__ = "Integer32"
_VSFPB1WorkMode_Object = MibScalar
vSFPB1WorkMode = _VSFPB1WorkMode_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 2),
    _VSFPB1WorkMode_Type()
)
vSFPB1WorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPB1WorkMode.setStatus("current")


class _VSFPB1TxPowerControl_Type(Integer32):
    """Custom type vSFPB1TxPowerControl based on Integer32"""
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
          ("auto", 2))
    )


_VSFPB1TxPowerControl_Type.__name__ = "Integer32"
_VSFPB1TxPowerControl_Object = MibScalar
vSFPB1TxPowerControl = _VSFPB1TxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 3),
    _VSFPB1TxPowerControl_Type()
)
vSFPB1TxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPB1TxPowerControl.setStatus("current")
_VSFPB1TxPower_Type = Integer32
_VSFPB1TxPower_Object = MibScalar
vSFPB1TxPower = _VSFPB1TxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 4),
    _VSFPB1TxPower_Type()
)
vSFPB1TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1TxPower.setStatus("current")
_VSFPB1RxPower_Type = Integer32
_VSFPB1RxPower_Object = MibScalar
vSFPB1RxPower = _VSFPB1RxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 5),
    _VSFPB1RxPower_Type()
)
vSFPB1RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1RxPower.setStatus("current")
_VSFPB1ModeWave_Type = Integer32
_VSFPB1ModeWave_Object = MibScalar
vSFPB1ModeWave = _VSFPB1ModeWave_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 6),
    _VSFPB1ModeWave_Type()
)
vSFPB1ModeWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1ModeWave.setStatus("current")


class _VSFPB1ModeTransmissionDistance_Type(Integer32):
    """Custom type vSFPB1ModeTransmissionDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPB1ModeTransmissionDistance_Type.__name__ = "Integer32"
_VSFPB1ModeTransmissionDistance_Object = MibScalar
vSFPB1ModeTransmissionDistance = _VSFPB1ModeTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 7),
    _VSFPB1ModeTransmissionDistance_Type()
)
vSFPB1ModeTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1ModeTransmissionDistance.setStatus("current")
_VSFPB1ModeTransmissionRate_Type = Integer32
_VSFPB1ModeTransmissionRate_Object = MibScalar
vSFPB1ModeTransmissionRate = _VSFPB1ModeTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 8),
    _VSFPB1ModeTransmissionRate_Type()
)
vSFPB1ModeTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1ModeTransmissionRate.setStatus("current")


class _VSFPB1ModeTemperature_Type(Integer32):
    """Custom type vSFPB1ModeTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPB1ModeTemperature_Type.__name__ = "Integer32"
_VSFPB1ModeTemperature_Object = MibScalar
vSFPB1ModeTemperature = _VSFPB1ModeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 9),
    _VSFPB1ModeTemperature_Type()
)
vSFPB1ModeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1ModeTemperature.setStatus("current")


class _VSFPB1TxPowerAlarm_Type(Integer32):
    """Custom type vSFPB1TxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPB1TxPowerAlarm_Type.__name__ = "Integer32"
_VSFPB1TxPowerAlarm_Object = MibScalar
vSFPB1TxPowerAlarm = _VSFPB1TxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 10),
    _VSFPB1TxPowerAlarm_Type()
)
vSFPB1TxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1TxPowerAlarm.setStatus("current")


class _VSFPB1RxPowerAlarm_Type(Integer32):
    """Custom type vSFPB1RxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPB1RxPowerAlarm_Type.__name__ = "Integer32"
_VSFPB1RxPowerAlarm_Object = MibScalar
vSFPB1RxPowerAlarm = _VSFPB1RxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 11),
    _VSFPB1RxPowerAlarm_Type()
)
vSFPB1RxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1RxPowerAlarm.setStatus("current")


class _VSFPB1ModeTemperatureAlarm_Type(Integer32):
    """Custom type vSFPB1ModeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPB1ModeTemperatureAlarm_Type.__name__ = "Integer32"
_VSFPB1ModeTemperatureAlarm_Object = MibScalar
vSFPB1ModeTemperatureAlarm = _VSFPB1ModeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 12),
    _VSFPB1ModeTemperatureAlarm_Type()
)
vSFPB1ModeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB1ModeTemperatureAlarm.setStatus("current")
_VSFPB1RxPowerThreshold_Type = Integer32
_VSFPB1RxPowerThreshold_Object = MibScalar
vSFPB1RxPowerThreshold = _VSFPB1RxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 13, 13),
    _VSFPB1RxPowerThreshold_Type()
)
vSFPB1RxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPB1RxPowerThreshold.setStatus("current")
_VSFPB2_ObjectIdentity = ObjectIdentity
vSFPB2 = _VSFPB2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14)
)


class _VSFPB2State_Type(Integer32):
    """Custom type vSFPB2State based on Integer32"""
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


_VSFPB2State_Type.__name__ = "Integer32"
_VSFPB2State_Object = MibScalar
vSFPB2State = _VSFPB2State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 1),
    _VSFPB2State_Type()
)
vSFPB2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2State.setStatus("current")


class _VSFPB2WorkMode_Type(Integer32):
    """Custom type vSFPB2WorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loopback", 3))
    )


_VSFPB2WorkMode_Type.__name__ = "Integer32"
_VSFPB2WorkMode_Object = MibScalar
vSFPB2WorkMode = _VSFPB2WorkMode_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 2),
    _VSFPB2WorkMode_Type()
)
vSFPB2WorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPB2WorkMode.setStatus("current")


class _VSFPB2TxPowerControl_Type(Integer32):
    """Custom type vSFPB2TxPowerControl based on Integer32"""
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
          ("auto", 2))
    )


_VSFPB2TxPowerControl_Type.__name__ = "Integer32"
_VSFPB2TxPowerControl_Object = MibScalar
vSFPB2TxPowerControl = _VSFPB2TxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 3),
    _VSFPB2TxPowerControl_Type()
)
vSFPB2TxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPB2TxPowerControl.setStatus("current")
_VSFPB2TxPower_Type = Integer32
_VSFPB2TxPower_Object = MibScalar
vSFPB2TxPower = _VSFPB2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 4),
    _VSFPB2TxPower_Type()
)
vSFPB2TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2TxPower.setStatus("current")
_VSFPB2RxPower_Type = Integer32
_VSFPB2RxPower_Object = MibScalar
vSFPB2RxPower = _VSFPB2RxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 5),
    _VSFPB2RxPower_Type()
)
vSFPB2RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2RxPower.setStatus("current")
_VSFPB2ModeWave_Type = Integer32
_VSFPB2ModeWave_Object = MibScalar
vSFPB2ModeWave = _VSFPB2ModeWave_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 6),
    _VSFPB2ModeWave_Type()
)
vSFPB2ModeWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2ModeWave.setStatus("current")


class _VSFPB2ModeTransmissionDistance_Type(Integer32):
    """Custom type vSFPB2ModeTransmissionDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPB2ModeTransmissionDistance_Type.__name__ = "Integer32"
_VSFPB2ModeTransmissionDistance_Object = MibScalar
vSFPB2ModeTransmissionDistance = _VSFPB2ModeTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 7),
    _VSFPB2ModeTransmissionDistance_Type()
)
vSFPB2ModeTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2ModeTransmissionDistance.setStatus("current")
_VSFPB2ModeTransmissionRate_Type = Integer32
_VSFPB2ModeTransmissionRate_Object = MibScalar
vSFPB2ModeTransmissionRate = _VSFPB2ModeTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 8),
    _VSFPB2ModeTransmissionRate_Type()
)
vSFPB2ModeTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2ModeTransmissionRate.setStatus("current")


class _VSFPB2ModeTemperature_Type(Integer32):
    """Custom type vSFPB2ModeTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPB2ModeTemperature_Type.__name__ = "Integer32"
_VSFPB2ModeTemperature_Object = MibScalar
vSFPB2ModeTemperature = _VSFPB2ModeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 9),
    _VSFPB2ModeTemperature_Type()
)
vSFPB2ModeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2ModeTemperature.setStatus("current")


class _VSFPB2TxPowerAlarm_Type(Integer32):
    """Custom type vSFPB2TxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPB2TxPowerAlarm_Type.__name__ = "Integer32"
_VSFPB2TxPowerAlarm_Object = MibScalar
vSFPB2TxPowerAlarm = _VSFPB2TxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 10),
    _VSFPB2TxPowerAlarm_Type()
)
vSFPB2TxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2TxPowerAlarm.setStatus("current")


class _VSFPB2RxPowerAlarm_Type(Integer32):
    """Custom type vSFPB2RxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPB2RxPowerAlarm_Type.__name__ = "Integer32"
_VSFPB2RxPowerAlarm_Object = MibScalar
vSFPB2RxPowerAlarm = _VSFPB2RxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 11),
    _VSFPB2RxPowerAlarm_Type()
)
vSFPB2RxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2RxPowerAlarm.setStatus("current")


class _VSFPB2ModeTemperatureAlarm_Type(Integer32):
    """Custom type vSFPB2ModeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPB2ModeTemperatureAlarm_Type.__name__ = "Integer32"
_VSFPB2ModeTemperatureAlarm_Object = MibScalar
vSFPB2ModeTemperatureAlarm = _VSFPB2ModeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 12),
    _VSFPB2ModeTemperatureAlarm_Type()
)
vSFPB2ModeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPB2ModeTemperatureAlarm.setStatus("current")
_VSFPB2RxPowerThreshold_Type = Integer32
_VSFPB2RxPowerThreshold_Object = MibScalar
vSFPB2RxPowerThreshold = _VSFPB2RxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 14, 13),
    _VSFPB2RxPowerThreshold_Type()
)
vSFPB2RxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPB2RxPowerThreshold.setStatus("current")
_VSFPC1_ObjectIdentity = ObjectIdentity
vSFPC1 = _VSFPC1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15)
)


class _VSFPC1State_Type(Integer32):
    """Custom type vSFPC1State based on Integer32"""
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


_VSFPC1State_Type.__name__ = "Integer32"
_VSFPC1State_Object = MibScalar
vSFPC1State = _VSFPC1State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 1),
    _VSFPC1State_Type()
)
vSFPC1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1State.setStatus("current")


class _VSFPC1WorkMode_Type(Integer32):
    """Custom type vSFPC1WorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loopback", 3))
    )


_VSFPC1WorkMode_Type.__name__ = "Integer32"
_VSFPC1WorkMode_Object = MibScalar
vSFPC1WorkMode = _VSFPC1WorkMode_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 2),
    _VSFPC1WorkMode_Type()
)
vSFPC1WorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPC1WorkMode.setStatus("current")


class _VSFPC1TxPowerControl_Type(Integer32):
    """Custom type vSFPC1TxPowerControl based on Integer32"""
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
          ("auto", 2))
    )


_VSFPC1TxPowerControl_Type.__name__ = "Integer32"
_VSFPC1TxPowerControl_Object = MibScalar
vSFPC1TxPowerControl = _VSFPC1TxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 3),
    _VSFPC1TxPowerControl_Type()
)
vSFPC1TxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPC1TxPowerControl.setStatus("current")
_VSFPC1TxPower_Type = Integer32
_VSFPC1TxPower_Object = MibScalar
vSFPC1TxPower = _VSFPC1TxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 4),
    _VSFPC1TxPower_Type()
)
vSFPC1TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1TxPower.setStatus("current")
_VSFPC1RxPower_Type = Integer32
_VSFPC1RxPower_Object = MibScalar
vSFPC1RxPower = _VSFPC1RxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 5),
    _VSFPC1RxPower_Type()
)
vSFPC1RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1RxPower.setStatus("current")
_VSFPC1ModeWave_Type = Integer32
_VSFPC1ModeWave_Object = MibScalar
vSFPC1ModeWave = _VSFPC1ModeWave_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 6),
    _VSFPC1ModeWave_Type()
)
vSFPC1ModeWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1ModeWave.setStatus("current")


class _VSFPC1ModeTransmissionDistance_Type(Integer32):
    """Custom type vSFPC1ModeTransmissionDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPC1ModeTransmissionDistance_Type.__name__ = "Integer32"
_VSFPC1ModeTransmissionDistance_Object = MibScalar
vSFPC1ModeTransmissionDistance = _VSFPC1ModeTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 7),
    _VSFPC1ModeTransmissionDistance_Type()
)
vSFPC1ModeTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1ModeTransmissionDistance.setStatus("current")
_VSFPC1ModeTransmissionRate_Type = Integer32
_VSFPC1ModeTransmissionRate_Object = MibScalar
vSFPC1ModeTransmissionRate = _VSFPC1ModeTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 8),
    _VSFPC1ModeTransmissionRate_Type()
)
vSFPC1ModeTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1ModeTransmissionRate.setStatus("current")


class _VSFPC1ModeTemperature_Type(Integer32):
    """Custom type vSFPC1ModeTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPC1ModeTemperature_Type.__name__ = "Integer32"
_VSFPC1ModeTemperature_Object = MibScalar
vSFPC1ModeTemperature = _VSFPC1ModeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 9),
    _VSFPC1ModeTemperature_Type()
)
vSFPC1ModeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1ModeTemperature.setStatus("current")


class _VSFPC1TxPowerAlarm_Type(Integer32):
    """Custom type vSFPC1TxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPC1TxPowerAlarm_Type.__name__ = "Integer32"
_VSFPC1TxPowerAlarm_Object = MibScalar
vSFPC1TxPowerAlarm = _VSFPC1TxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 10),
    _VSFPC1TxPowerAlarm_Type()
)
vSFPC1TxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1TxPowerAlarm.setStatus("current")


class _VSFPC1RxPowerAlarm_Type(Integer32):
    """Custom type vSFPC1RxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPC1RxPowerAlarm_Type.__name__ = "Integer32"
_VSFPC1RxPowerAlarm_Object = MibScalar
vSFPC1RxPowerAlarm = _VSFPC1RxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 11),
    _VSFPC1RxPowerAlarm_Type()
)
vSFPC1RxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1RxPowerAlarm.setStatus("current")


class _VSFPC1ModeTemperatureAlarm_Type(Integer32):
    """Custom type vSFPC1ModeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPC1ModeTemperatureAlarm_Type.__name__ = "Integer32"
_VSFPC1ModeTemperatureAlarm_Object = MibScalar
vSFPC1ModeTemperatureAlarm = _VSFPC1ModeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 12),
    _VSFPC1ModeTemperatureAlarm_Type()
)
vSFPC1ModeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC1ModeTemperatureAlarm.setStatus("current")
_VSFPC1RxPowerThreshold_Type = Integer32
_VSFPC1RxPowerThreshold_Object = MibScalar
vSFPC1RxPowerThreshold = _VSFPC1RxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 15, 13),
    _VSFPC1RxPowerThreshold_Type()
)
vSFPC1RxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPC1RxPowerThreshold.setStatus("current")
_VSFPC2_ObjectIdentity = ObjectIdentity
vSFPC2 = _VSFPC2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16)
)


class _VSFPC2State_Type(Integer32):
    """Custom type vSFPC2State based on Integer32"""
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


_VSFPC2State_Type.__name__ = "Integer32"
_VSFPC2State_Object = MibScalar
vSFPC2State = _VSFPC2State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 1),
    _VSFPC2State_Type()
)
vSFPC2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2State.setStatus("current")


class _VSFPC2WorkMode_Type(Integer32):
    """Custom type vSFPC2WorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loopback", 3))
    )


_VSFPC2WorkMode_Type.__name__ = "Integer32"
_VSFPC2WorkMode_Object = MibScalar
vSFPC2WorkMode = _VSFPC2WorkMode_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 2),
    _VSFPC2WorkMode_Type()
)
vSFPC2WorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPC2WorkMode.setStatus("current")


class _VSFPC2TxPowerControl_Type(Integer32):
    """Custom type vSFPC2TxPowerControl based on Integer32"""
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
          ("auto", 2))
    )


_VSFPC2TxPowerControl_Type.__name__ = "Integer32"
_VSFPC2TxPowerControl_Object = MibScalar
vSFPC2TxPowerControl = _VSFPC2TxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 3),
    _VSFPC2TxPowerControl_Type()
)
vSFPC2TxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPC2TxPowerControl.setStatus("current")
_VSFPC2TxPower_Type = Integer32
_VSFPC2TxPower_Object = MibScalar
vSFPC2TxPower = _VSFPC2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 4),
    _VSFPC2TxPower_Type()
)
vSFPC2TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2TxPower.setStatus("current")
_VSFPC2RxPower_Type = Integer32
_VSFPC2RxPower_Object = MibScalar
vSFPC2RxPower = _VSFPC2RxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 5),
    _VSFPC2RxPower_Type()
)
vSFPC2RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2RxPower.setStatus("current")
_VSFPC2ModeWave_Type = Integer32
_VSFPC2ModeWave_Object = MibScalar
vSFPC2ModeWave = _VSFPC2ModeWave_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 6),
    _VSFPC2ModeWave_Type()
)
vSFPC2ModeWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2ModeWave.setStatus("current")


class _VSFPC2ModeTransmissionDistance_Type(Integer32):
    """Custom type vSFPC2ModeTransmissionDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPC2ModeTransmissionDistance_Type.__name__ = "Integer32"
_VSFPC2ModeTransmissionDistance_Object = MibScalar
vSFPC2ModeTransmissionDistance = _VSFPC2ModeTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 7),
    _VSFPC2ModeTransmissionDistance_Type()
)
vSFPC2ModeTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2ModeTransmissionDistance.setStatus("current")
_VSFPC2ModeTransmissionRate_Type = Integer32
_VSFPC2ModeTransmissionRate_Object = MibScalar
vSFPC2ModeTransmissionRate = _VSFPC2ModeTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 8),
    _VSFPC2ModeTransmissionRate_Type()
)
vSFPC2ModeTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2ModeTransmissionRate.setStatus("current")


class _VSFPC2ModeTemperature_Type(Integer32):
    """Custom type vSFPC2ModeTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPC2ModeTemperature_Type.__name__ = "Integer32"
_VSFPC2ModeTemperature_Object = MibScalar
vSFPC2ModeTemperature = _VSFPC2ModeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 9),
    _VSFPC2ModeTemperature_Type()
)
vSFPC2ModeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2ModeTemperature.setStatus("current")


class _VSFPC2TxPowerAlarm_Type(Integer32):
    """Custom type vSFPC2TxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPC2TxPowerAlarm_Type.__name__ = "Integer32"
_VSFPC2TxPowerAlarm_Object = MibScalar
vSFPC2TxPowerAlarm = _VSFPC2TxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 10),
    _VSFPC2TxPowerAlarm_Type()
)
vSFPC2TxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2TxPowerAlarm.setStatus("current")


class _VSFPC2RxPowerAlarm_Type(Integer32):
    """Custom type vSFPC2RxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPC2RxPowerAlarm_Type.__name__ = "Integer32"
_VSFPC2RxPowerAlarm_Object = MibScalar
vSFPC2RxPowerAlarm = _VSFPC2RxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 11),
    _VSFPC2RxPowerAlarm_Type()
)
vSFPC2RxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2RxPowerAlarm.setStatus("current")


class _VSFPC2ModeTemperatureAlarm_Type(Integer32):
    """Custom type vSFPC2ModeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPC2ModeTemperatureAlarm_Type.__name__ = "Integer32"
_VSFPC2ModeTemperatureAlarm_Object = MibScalar
vSFPC2ModeTemperatureAlarm = _VSFPC2ModeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 12),
    _VSFPC2ModeTemperatureAlarm_Type()
)
vSFPC2ModeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPC2ModeTemperatureAlarm.setStatus("current")
_VSFPC2RxPowerThreshold_Type = Integer32
_VSFPC2RxPowerThreshold_Object = MibScalar
vSFPC2RxPowerThreshold = _VSFPC2RxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 16, 13),
    _VSFPC2RxPowerThreshold_Type()
)
vSFPC2RxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPC2RxPowerThreshold.setStatus("current")
_VSFPD1_ObjectIdentity = ObjectIdentity
vSFPD1 = _VSFPD1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17)
)


class _VSFPD1State_Type(Integer32):
    """Custom type vSFPD1State based on Integer32"""
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


_VSFPD1State_Type.__name__ = "Integer32"
_VSFPD1State_Object = MibScalar
vSFPD1State = _VSFPD1State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 1),
    _VSFPD1State_Type()
)
vSFPD1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1State.setStatus("current")


class _VSFPD1WorkMode_Type(Integer32):
    """Custom type vSFPD1WorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loopback", 3))
    )


_VSFPD1WorkMode_Type.__name__ = "Integer32"
_VSFPD1WorkMode_Object = MibScalar
vSFPD1WorkMode = _VSFPD1WorkMode_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 2),
    _VSFPD1WorkMode_Type()
)
vSFPD1WorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPD1WorkMode.setStatus("current")


class _VSFPD1TxPowerControl_Type(Integer32):
    """Custom type vSFPD1TxPowerControl based on Integer32"""
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
          ("auto", 2))
    )


_VSFPD1TxPowerControl_Type.__name__ = "Integer32"
_VSFPD1TxPowerControl_Object = MibScalar
vSFPD1TxPowerControl = _VSFPD1TxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 3),
    _VSFPD1TxPowerControl_Type()
)
vSFPD1TxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPD1TxPowerControl.setStatus("current")
_VSFPD1TxPower_Type = Integer32
_VSFPD1TxPower_Object = MibScalar
vSFPD1TxPower = _VSFPD1TxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 4),
    _VSFPD1TxPower_Type()
)
vSFPD1TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1TxPower.setStatus("current")
_VSFPD1RxPower_Type = Integer32
_VSFPD1RxPower_Object = MibScalar
vSFPD1RxPower = _VSFPD1RxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 5),
    _VSFPD1RxPower_Type()
)
vSFPD1RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1RxPower.setStatus("current")
_VSFPD1ModeWave_Type = Integer32
_VSFPD1ModeWave_Object = MibScalar
vSFPD1ModeWave = _VSFPD1ModeWave_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 6),
    _VSFPD1ModeWave_Type()
)
vSFPD1ModeWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1ModeWave.setStatus("current")


class _VSFPD1ModeTransmissionDistance_Type(Integer32):
    """Custom type vSFPD1ModeTransmissionDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPD1ModeTransmissionDistance_Type.__name__ = "Integer32"
_VSFPD1ModeTransmissionDistance_Object = MibScalar
vSFPD1ModeTransmissionDistance = _VSFPD1ModeTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 7),
    _VSFPD1ModeTransmissionDistance_Type()
)
vSFPD1ModeTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1ModeTransmissionDistance.setStatus("current")
_VSFPD1ModeTransmissionRate_Type = Integer32
_VSFPD1ModeTransmissionRate_Object = MibScalar
vSFPD1ModeTransmissionRate = _VSFPD1ModeTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 8),
    _VSFPD1ModeTransmissionRate_Type()
)
vSFPD1ModeTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1ModeTransmissionRate.setStatus("current")


class _VSFPD1ModeTemperature_Type(Integer32):
    """Custom type vSFPD1ModeTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPD1ModeTemperature_Type.__name__ = "Integer32"
_VSFPD1ModeTemperature_Object = MibScalar
vSFPD1ModeTemperature = _VSFPD1ModeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 9),
    _VSFPD1ModeTemperature_Type()
)
vSFPD1ModeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1ModeTemperature.setStatus("current")


class _VSFPD1TxPowerAlarm_Type(Integer32):
    """Custom type vSFPD1TxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPD1TxPowerAlarm_Type.__name__ = "Integer32"
_VSFPD1TxPowerAlarm_Object = MibScalar
vSFPD1TxPowerAlarm = _VSFPD1TxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 10),
    _VSFPD1TxPowerAlarm_Type()
)
vSFPD1TxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1TxPowerAlarm.setStatus("current")


class _VSFPD1RxPowerAlarm_Type(Integer32):
    """Custom type vSFPD1RxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPD1RxPowerAlarm_Type.__name__ = "Integer32"
_VSFPD1RxPowerAlarm_Object = MibScalar
vSFPD1RxPowerAlarm = _VSFPD1RxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 11),
    _VSFPD1RxPowerAlarm_Type()
)
vSFPD1RxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1RxPowerAlarm.setStatus("current")


class _VSFPD1ModeTemperatureAlarm_Type(Integer32):
    """Custom type vSFPD1ModeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPD1ModeTemperatureAlarm_Type.__name__ = "Integer32"
_VSFPD1ModeTemperatureAlarm_Object = MibScalar
vSFPD1ModeTemperatureAlarm = _VSFPD1ModeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 12),
    _VSFPD1ModeTemperatureAlarm_Type()
)
vSFPD1ModeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD1ModeTemperatureAlarm.setStatus("current")
_VSFPD1RxPowerThreshold_Type = Integer32
_VSFPD1RxPowerThreshold_Object = MibScalar
vSFPD1RxPowerThreshold = _VSFPD1RxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 17, 13),
    _VSFPD1RxPowerThreshold_Type()
)
vSFPD1RxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPD1RxPowerThreshold.setStatus("current")
_VSFPD2_ObjectIdentity = ObjectIdentity
vSFPD2 = _VSFPD2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18)
)


class _VSFPD2State_Type(Integer32):
    """Custom type vSFPD2State based on Integer32"""
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


_VSFPD2State_Type.__name__ = "Integer32"
_VSFPD2State_Object = MibScalar
vSFPD2State = _VSFPD2State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 1),
    _VSFPD2State_Type()
)
vSFPD2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2State.setStatus("current")


class _VSFPD2WorkMode_Type(Integer32):
    """Custom type vSFPD2WorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loopback", 3))
    )


_VSFPD2WorkMode_Type.__name__ = "Integer32"
_VSFPD2WorkMode_Object = MibScalar
vSFPD2WorkMode = _VSFPD2WorkMode_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 2),
    _VSFPD2WorkMode_Type()
)
vSFPD2WorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPD2WorkMode.setStatus("current")


class _VSFPD2TxPowerControl_Type(Integer32):
    """Custom type vSFPD2TxPowerControl based on Integer32"""
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
          ("auto", 2))
    )


_VSFPD2TxPowerControl_Type.__name__ = "Integer32"
_VSFPD2TxPowerControl_Object = MibScalar
vSFPD2TxPowerControl = _VSFPD2TxPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 3),
    _VSFPD2TxPowerControl_Type()
)
vSFPD2TxPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPD2TxPowerControl.setStatus("current")
_VSFPD2TxPower_Type = Integer32
_VSFPD2TxPower_Object = MibScalar
vSFPD2TxPower = _VSFPD2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 4),
    _VSFPD2TxPower_Type()
)
vSFPD2TxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2TxPower.setStatus("current")
_VSFPD2RxPower_Type = Integer32
_VSFPD2RxPower_Object = MibScalar
vSFPD2RxPower = _VSFPD2RxPower_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 5),
    _VSFPD2RxPower_Type()
)
vSFPD2RxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2RxPower.setStatus("current")
_VSFPD2ModeWave_Type = Integer32
_VSFPD2ModeWave_Object = MibScalar
vSFPD2ModeWave = _VSFPD2ModeWave_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 6),
    _VSFPD2ModeWave_Type()
)
vSFPD2ModeWave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2ModeWave.setStatus("current")


class _VSFPD2ModeTransmissionDistance_Type(Integer32):
    """Custom type vSFPD2ModeTransmissionDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPD2ModeTransmissionDistance_Type.__name__ = "Integer32"
_VSFPD2ModeTransmissionDistance_Object = MibScalar
vSFPD2ModeTransmissionDistance = _VSFPD2ModeTransmissionDistance_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 7),
    _VSFPD2ModeTransmissionDistance_Type()
)
vSFPD2ModeTransmissionDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2ModeTransmissionDistance.setStatus("current")
_VSFPD2ModeTransmissionRate_Type = Integer32
_VSFPD2ModeTransmissionRate_Object = MibScalar
vSFPD2ModeTransmissionRate = _VSFPD2ModeTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 8),
    _VSFPD2ModeTransmissionRate_Type()
)
vSFPD2ModeTransmissionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2ModeTransmissionRate.setStatus("current")


class _VSFPD2ModeTemperature_Type(Integer32):
    """Custom type vSFPD2ModeTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_VSFPD2ModeTemperature_Type.__name__ = "Integer32"
_VSFPD2ModeTemperature_Object = MibScalar
vSFPD2ModeTemperature = _VSFPD2ModeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 9),
    _VSFPD2ModeTemperature_Type()
)
vSFPD2ModeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2ModeTemperature.setStatus("current")


class _VSFPD2TxPowerAlarm_Type(Integer32):
    """Custom type vSFPD2TxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPD2TxPowerAlarm_Type.__name__ = "Integer32"
_VSFPD2TxPowerAlarm_Object = MibScalar
vSFPD2TxPowerAlarm = _VSFPD2TxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 10),
    _VSFPD2TxPowerAlarm_Type()
)
vSFPD2TxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2TxPowerAlarm.setStatus("current")


class _VSFPD2RxPowerAlarm_Type(Integer32):
    """Custom type vSFPD2RxPowerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPD2RxPowerAlarm_Type.__name__ = "Integer32"
_VSFPD2RxPowerAlarm_Object = MibScalar
vSFPD2RxPowerAlarm = _VSFPD2RxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 11),
    _VSFPD2RxPowerAlarm_Type()
)
vSFPD2RxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2RxPowerAlarm.setStatus("current")


class _VSFPD2ModeTemperatureAlarm_Type(Integer32):
    """Custom type vSFPD2ModeTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 0),
          ("normal", 1))
    )


_VSFPD2ModeTemperatureAlarm_Type.__name__ = "Integer32"
_VSFPD2ModeTemperatureAlarm_Object = MibScalar
vSFPD2ModeTemperatureAlarm = _VSFPD2ModeTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 12),
    _VSFPD2ModeTemperatureAlarm_Type()
)
vSFPD2ModeTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSFPD2ModeTemperatureAlarm.setStatus("current")
_VSFPD2RxPowerThreshold_Type = Integer32
_VSFPD2RxPowerThreshold_Object = MibScalar
vSFPD2RxPowerThreshold = _VSFPD2RxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 1, 2, 18, 13),
    _VSFPD2RxPowerThreshold_Type()
)
vSFPD2RxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSFPD2RxPowerThreshold.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OAP-C1-OEO",
    **{"tryin": tryin,
       "device": device,
       "oap": oap,
       "card1": card1,
       "oeo": oeo,
       "vCardState": vCardState,
       "vDeviceType": vDeviceType,
       "vDeviceDescription": vDeviceDescription,
       "vSoftwareVerion": vSoftwareVerion,
       "vHardwareVerion": vHardwareVerion,
       "vSerialNumber": vSerialNumber,
       "vFactoryDate": vFactoryDate,
       "vSFPA1": vSFPA1,
       "vSFPA1State": vSFPA1State,
       "vSFPA1WorkMode": vSFPA1WorkMode,
       "vSFPA1TxPowerControl": vSFPA1TxPowerControl,
       "vSFPA1TxPower": vSFPA1TxPower,
       "vSFPA1RxPower": vSFPA1RxPower,
       "vSFPA1ModeWave": vSFPA1ModeWave,
       "vSFPA1ModeTransmissionDistance": vSFPA1ModeTransmissionDistance,
       "vSFPA1ModeTransmissionRate": vSFPA1ModeTransmissionRate,
       "vSFPA1ModeTemperature": vSFPA1ModeTemperature,
       "vSFPA1TxPowerAlarm": vSFPA1TxPowerAlarm,
       "vSFPA1RxPowerAlarm": vSFPA1RxPowerAlarm,
       "vSFPA1ModeTemperatureAlarm": vSFPA1ModeTemperatureAlarm,
       "vSFPA1RxPowerThreshold": vSFPA1RxPowerThreshold,
       "vSFPA2": vSFPA2,
       "vSFPA2State": vSFPA2State,
       "vSFPA2WorkMode": vSFPA2WorkMode,
       "vSFPA2TxPowerControl": vSFPA2TxPowerControl,
       "vSFPA2TxPower": vSFPA2TxPower,
       "vSFPA2RxPower": vSFPA2RxPower,
       "vSFPA2ModeWave": vSFPA2ModeWave,
       "vSFPA2ModeTransmissionDistance": vSFPA2ModeTransmissionDistance,
       "vSFPA2ModeTransmissionRate": vSFPA2ModeTransmissionRate,
       "vSFPA2ModeTemperature": vSFPA2ModeTemperature,
       "vSFPA2TxPowerAlarm": vSFPA2TxPowerAlarm,
       "vSFPA2RxPowerAlarm": vSFPA2RxPowerAlarm,
       "vSFPA2ModeTemperatureAlarm": vSFPA2ModeTemperatureAlarm,
       "vSFPA2RxPowerThreshold": vSFPA2RxPowerThreshold,
       "vSFPB1": vSFPB1,
       "vSFPB1State": vSFPB1State,
       "vSFPB1WorkMode": vSFPB1WorkMode,
       "vSFPB1TxPowerControl": vSFPB1TxPowerControl,
       "vSFPB1TxPower": vSFPB1TxPower,
       "vSFPB1RxPower": vSFPB1RxPower,
       "vSFPB1ModeWave": vSFPB1ModeWave,
       "vSFPB1ModeTransmissionDistance": vSFPB1ModeTransmissionDistance,
       "vSFPB1ModeTransmissionRate": vSFPB1ModeTransmissionRate,
       "vSFPB1ModeTemperature": vSFPB1ModeTemperature,
       "vSFPB1TxPowerAlarm": vSFPB1TxPowerAlarm,
       "vSFPB1RxPowerAlarm": vSFPB1RxPowerAlarm,
       "vSFPB1ModeTemperatureAlarm": vSFPB1ModeTemperatureAlarm,
       "vSFPB1RxPowerThreshold": vSFPB1RxPowerThreshold,
       "vSFPB2": vSFPB2,
       "vSFPB2State": vSFPB2State,
       "vSFPB2WorkMode": vSFPB2WorkMode,
       "vSFPB2TxPowerControl": vSFPB2TxPowerControl,
       "vSFPB2TxPower": vSFPB2TxPower,
       "vSFPB2RxPower": vSFPB2RxPower,
       "vSFPB2ModeWave": vSFPB2ModeWave,
       "vSFPB2ModeTransmissionDistance": vSFPB2ModeTransmissionDistance,
       "vSFPB2ModeTransmissionRate": vSFPB2ModeTransmissionRate,
       "vSFPB2ModeTemperature": vSFPB2ModeTemperature,
       "vSFPB2TxPowerAlarm": vSFPB2TxPowerAlarm,
       "vSFPB2RxPowerAlarm": vSFPB2RxPowerAlarm,
       "vSFPB2ModeTemperatureAlarm": vSFPB2ModeTemperatureAlarm,
       "vSFPB2RxPowerThreshold": vSFPB2RxPowerThreshold,
       "vSFPC1": vSFPC1,
       "vSFPC1State": vSFPC1State,
       "vSFPC1WorkMode": vSFPC1WorkMode,
       "vSFPC1TxPowerControl": vSFPC1TxPowerControl,
       "vSFPC1TxPower": vSFPC1TxPower,
       "vSFPC1RxPower": vSFPC1RxPower,
       "vSFPC1ModeWave": vSFPC1ModeWave,
       "vSFPC1ModeTransmissionDistance": vSFPC1ModeTransmissionDistance,
       "vSFPC1ModeTransmissionRate": vSFPC1ModeTransmissionRate,
       "vSFPC1ModeTemperature": vSFPC1ModeTemperature,
       "vSFPC1TxPowerAlarm": vSFPC1TxPowerAlarm,
       "vSFPC1RxPowerAlarm": vSFPC1RxPowerAlarm,
       "vSFPC1ModeTemperatureAlarm": vSFPC1ModeTemperatureAlarm,
       "vSFPC1RxPowerThreshold": vSFPC1RxPowerThreshold,
       "vSFPC2": vSFPC2,
       "vSFPC2State": vSFPC2State,
       "vSFPC2WorkMode": vSFPC2WorkMode,
       "vSFPC2TxPowerControl": vSFPC2TxPowerControl,
       "vSFPC2TxPower": vSFPC2TxPower,
       "vSFPC2RxPower": vSFPC2RxPower,
       "vSFPC2ModeWave": vSFPC2ModeWave,
       "vSFPC2ModeTransmissionDistance": vSFPC2ModeTransmissionDistance,
       "vSFPC2ModeTransmissionRate": vSFPC2ModeTransmissionRate,
       "vSFPC2ModeTemperature": vSFPC2ModeTemperature,
       "vSFPC2TxPowerAlarm": vSFPC2TxPowerAlarm,
       "vSFPC2RxPowerAlarm": vSFPC2RxPowerAlarm,
       "vSFPC2ModeTemperatureAlarm": vSFPC2ModeTemperatureAlarm,
       "vSFPC2RxPowerThreshold": vSFPC2RxPowerThreshold,
       "vSFPD1": vSFPD1,
       "vSFPD1State": vSFPD1State,
       "vSFPD1WorkMode": vSFPD1WorkMode,
       "vSFPD1TxPowerControl": vSFPD1TxPowerControl,
       "vSFPD1TxPower": vSFPD1TxPower,
       "vSFPD1RxPower": vSFPD1RxPower,
       "vSFPD1ModeWave": vSFPD1ModeWave,
       "vSFPD1ModeTransmissionDistance": vSFPD1ModeTransmissionDistance,
       "vSFPD1ModeTransmissionRate": vSFPD1ModeTransmissionRate,
       "vSFPD1ModeTemperature": vSFPD1ModeTemperature,
       "vSFPD1TxPowerAlarm": vSFPD1TxPowerAlarm,
       "vSFPD1RxPowerAlarm": vSFPD1RxPowerAlarm,
       "vSFPD1ModeTemperatureAlarm": vSFPD1ModeTemperatureAlarm,
       "vSFPD1RxPowerThreshold": vSFPD1RxPowerThreshold,
       "vSFPD2": vSFPD2,
       "vSFPD2State": vSFPD2State,
       "vSFPD2WorkMode": vSFPD2WorkMode,
       "vSFPD2TxPowerControl": vSFPD2TxPowerControl,
       "vSFPD2TxPower": vSFPD2TxPower,
       "vSFPD2RxPower": vSFPD2RxPower,
       "vSFPD2ModeWave": vSFPD2ModeWave,
       "vSFPD2ModeTransmissionDistance": vSFPD2ModeTransmissionDistance,
       "vSFPD2ModeTransmissionRate": vSFPD2ModeTransmissionRate,
       "vSFPD2ModeTemperature": vSFPD2ModeTemperature,
       "vSFPD2TxPowerAlarm": vSFPD2TxPowerAlarm,
       "vSFPD2RxPowerAlarm": vSFPD2RxPowerAlarm,
       "vSFPD2ModeTemperatureAlarm": vSFPD2ModeTemperatureAlarm,
       "vSFPD2RxPowerThreshold": vSFPD2RxPowerThreshold}
)
