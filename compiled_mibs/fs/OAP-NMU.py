# SNMP MIB module (OAP-NMU) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fs\OAP-NMU
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:04 2025
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
_Nmu_ObjectIdentity = ObjectIdentity
nmu = _Nmu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20)
)
_DeviceType_Type = OctetString
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 1),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 2),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 3),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_GateWay_Type = IpAddress
_GateWay_Object = MibScalar
gateWay = _GateWay_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 4),
    _GateWay_Type()
)
gateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateWay.setStatus("current")
_MacAddress_Type = OctetString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 5),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _KeyLock_Type(Integer32):
    """Custom type keyLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lock", 0),
          ("unlock", 1))
    )


_KeyLock_Type.__name__ = "Integer32"
_KeyLock_Object = MibScalar
keyLock = _KeyLock_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 6),
    _KeyLock_Type()
)
keyLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyLock.setStatus("current")


class _BuzzerSet_Type(Integer32):
    """Custom type buzzerSet based on Integer32"""
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


_BuzzerSet_Type.__name__ = "Integer32"
_BuzzerSet_Object = MibScalar
buzzerSet = _BuzzerSet_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 7),
    _BuzzerSet_Type()
)
buzzerSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buzzerSet.setStatus("current")


class _BuzzerState_Type(Integer32):
    """Custom type buzzerState based on Integer32"""
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


_BuzzerState_Type.__name__ = "Integer32"
_BuzzerState_Object = MibScalar
buzzerState = _BuzzerState_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 8),
    _BuzzerState_Type()
)
buzzerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buzzerState.setStatus("current")


class _FanSet_Type(Integer32):
    """Custom type fanSet based on Integer32"""
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


_FanSet_Type.__name__ = "Integer32"
_FanSet_Object = MibScalar
fanSet = _FanSet_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 9),
    _FanSet_Type()
)
fanSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanSet.setStatus("current")


class _FanState_Type(Integer32):
    """Custom type fanState based on Integer32"""
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


_FanState_Type.__name__ = "Integer32"
_FanState_Object = MibScalar
fanState = _FanState_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 10),
    _FanState_Type()
)
fanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanState.setStatus("current")


class _Power1State_Type(Integer32):
    """Custom type power1State based on Integer32"""
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


_Power1State_Type.__name__ = "Integer32"
_Power1State_Object = MibScalar
power1State = _Power1State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 11),
    _Power1State_Type()
)
power1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power1State.setStatus("current")


class _Power2State_Type(Integer32):
    """Custom type power2State based on Integer32"""
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


_Power2State_Type.__name__ = "Integer32"
_Power2State_Object = MibScalar
power2State = _Power2State_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 12),
    _Power2State_Type()
)
power2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power2State.setStatus("current")
_SoftwareVersion_Type = OctetString
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 13),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_HardwareVersion_Type = OctetString
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 14),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")
_SerialNumber_Type = OctetString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 15),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_Manufacturingdate_Type = OctetString
_Manufacturingdate_Object = MibScalar
manufacturingdate = _Manufacturingdate_Object(
    (1, 3, 6, 1, 4, 1, 40989, 10, 16, 20, 16),
    _Manufacturingdate_Type()
)
manufacturingdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturingdate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OAP-NMU",
    **{"tryin": tryin,
       "device": device,
       "oap": oap,
       "nmu": nmu,
       "deviceType": deviceType,
       "ipAddress": ipAddress,
       "subnetMask": subnetMask,
       "gateWay": gateWay,
       "macAddress": macAddress,
       "keyLock": keyLock,
       "buzzerSet": buzzerSet,
       "buzzerState": buzzerState,
       "fanSet": fanSet,
       "fanState": fanState,
       "power1State": power1State,
       "power2State": power2State,
       "softwareVersion": softwareVersion,
       "hardwareVersion": hardwareVersion,
       "serialNumber": serialNumber,
       "manufacturingdate": manufacturingdate}
)
