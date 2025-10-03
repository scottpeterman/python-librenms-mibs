# SNMP MIB module (AATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bats\AATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:49 2025
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

aats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37069)
)
if mibBuilder.loadTexts:
    aats.setRevisions(
        ("2021-02-24 18:15",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AatsDot1_ObjectIdentity = ObjectIdentity
aatsDot1 = _AatsDot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 1)
)


class _Status_Type(DisplayString):
    """Custom type status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Status_Type.__name__ = "DisplayString"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 1, 1),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")


class _Active_Type(Integer32):
    """Custom type active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_Active_Type.__name__ = "Integer32"
_Active_Object = MibScalar
active = _Active_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 1, 2),
    _Active_Type()
)
active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    active.setStatus("current")


class _Stowed_Type(Integer32):
    """Custom type stowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unstowed", 0),
          ("stowed", 1))
    )


_Stowed_Type.__name__ = "Integer32"
_Stowed_Object = MibScalar
stowed = _Stowed_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 1, 3),
    _Stowed_Type()
)
stowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stowed.setStatus("current")
_CpuTemp_Type = Integer32
_CpuTemp_Object = MibScalar
cpuTemp = _CpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 1, 4),
    _CpuTemp_Type()
)
cpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemp.setStatus("current")
_Radio_ObjectIdentity = ObjectIdentity
radio = _Radio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2)
)


class _RadioName_Type(DisplayString):
    """Custom type radioName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RadioName_Type.__name__ = "DisplayString"
_RadioName_Object = MibScalar
radioName = _RadioName_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 1),
    _RadioName_Type()
)
radioName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioName.setStatus("current")


class _RadioConnected_Type(Integer32):
    """Custom type radioConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_RadioConnected_Type.__name__ = "Integer32"
_RadioConnected_Object = MibScalar
radioConnected = _RadioConnected_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 2),
    _RadioConnected_Type()
)
radioConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioConnected.setStatus("current")
_LinkStatus_ObjectIdentity = ObjectIdentity
linkStatus = _LinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 3)
)


class _LinkStatusString_Type(DisplayString):
    """Custom type linkStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LinkStatusString_Type.__name__ = "DisplayString"
_LinkStatusString_Object = MibScalar
linkStatusString = _LinkStatusString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 3, 1),
    _LinkStatusString_Type()
)
linkStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusString.setStatus("current")


class _LinkStatusInt_Type(Integer32):
    """Custom type linkStatusInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("marginal", 1),
          ("connected", 2))
    )


_LinkStatusInt_Type.__name__ = "Integer32"
_LinkStatusInt_Object = MibScalar
linkStatusInt = _LinkStatusInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 3, 2),
    _LinkStatusInt_Type()
)
linkStatusInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusInt.setStatus("current")


class _LinkStatusVal_Type(DisplayString):
    """Custom type linkStatusVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LinkStatusVal_Type.__name__ = "DisplayString"
_LinkStatusVal_Object = MibScalar
linkStatusVal = _LinkStatusVal_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 3, 3),
    _LinkStatusVal_Type()
)
linkStatusVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatusVal.setStatus("current")
_Rssi_ObjectIdentity = ObjectIdentity
rssi = _Rssi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 4)
)


class _RssiString_Type(DisplayString):
    """Custom type rssiString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RssiString_Type.__name__ = "DisplayString"
_RssiString_Object = MibScalar
rssiString = _RssiString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 4, 1),
    _RssiString_Type()
)
rssiString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiString.setStatus("current")
_RssiInt_Type = Integer32
_RssiInt_Object = MibScalar
rssiInt = _RssiInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 4, 2),
    _RssiInt_Type()
)
rssiInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiInt.setStatus("current")


class _RssiFloat_Type(DisplayString):
    """Custom type rssiFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RssiFloat_Type.__name__ = "DisplayString"
_RssiFloat_Object = MibScalar
rssiFloat = _RssiFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 4, 3),
    _RssiFloat_Type()
)
rssiFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiFloat.setStatus("current")
_Snr_ObjectIdentity = ObjectIdentity
snr = _Snr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 5)
)


class _SnrString_Type(DisplayString):
    """Custom type snrString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnrString_Type.__name__ = "DisplayString"
_SnrString_Object = MibScalar
snrString = _SnrString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 5, 1),
    _SnrString_Type()
)
snrString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrString.setStatus("current")
_SnrInt_Type = Integer32
_SnrInt_Object = MibScalar
snrInt = _SnrInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 5, 2),
    _SnrInt_Type()
)
snrInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrInt.setStatus("current")


class _SnrFloat_Type(DisplayString):
    """Custom type snrFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnrFloat_Type.__name__ = "DisplayString"
_SnrFloat_Object = MibScalar
snrFloat = _SnrFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 5, 3),
    _SnrFloat_Type()
)
snrFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snrFloat.setStatus("current")
_LinkDistance_ObjectIdentity = ObjectIdentity
linkDistance = _LinkDistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 6)
)


class _LinkDistanceString_Type(DisplayString):
    """Custom type linkDistanceString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LinkDistanceString_Type.__name__ = "DisplayString"
_LinkDistanceString_Object = MibScalar
linkDistanceString = _LinkDistanceString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 6, 1),
    _LinkDistanceString_Type()
)
linkDistanceString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDistanceString.setStatus("current")
_LinkDistanceMeters_Type = Integer32
_LinkDistanceMeters_Object = MibScalar
linkDistanceMeters = _LinkDistanceMeters_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 6, 2),
    _LinkDistanceMeters_Type()
)
linkDistanceMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDistanceMeters.setStatus("current")
_LinkDistanceMiles_Type = Integer32
_LinkDistanceMiles_Object = MibScalar
linkDistanceMiles = _LinkDistanceMiles_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 6, 3),
    _LinkDistanceMiles_Type()
)
linkDistanceMiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDistanceMiles.setStatus("current")
_Remote_ObjectIdentity = ObjectIdentity
remote = _Remote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 7)
)


class _RemoteString_Type(DisplayString):
    """Custom type remoteString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteString_Type.__name__ = "DisplayString"
_RemoteString_Object = MibScalar
remoteString = _RemoteString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 7, 1),
    _RemoteString_Type()
)
remoteString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteString.setStatus("current")
_RemoteIP_Type = IpAddress
_RemoteIP_Object = MibScalar
remoteIP = _RemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 7, 2),
    _RemoteIP_Type()
)
remoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIP.setStatus("current")


class _RemoteMAC_Type(DisplayString):
    """Custom type remoteMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RemoteMAC_Type.__name__ = "DisplayString"
_RemoteMAC_Object = MibScalar
remoteMAC = _RemoteMAC_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 2, 7, 3),
    _RemoteMAC_Type()
)
remoteMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteMAC.setStatus("current")
_Positioner_ObjectIdentity = ObjectIdentity
positioner = _Positioner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3)
)
_PositionerDot1_ObjectIdentity = ObjectIdentity
positionerDot1 = _PositionerDot1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1)
)


class _PositionerConnected_Type(Integer32):
    """Custom type positionerConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_PositionerConnected_Type.__name__ = "Integer32"
_PositionerConnected_Object = MibScalar
positionerConnected = _PositionerConnected_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 1),
    _PositionerConnected_Type()
)
positionerConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    positionerConnected.setStatus("current")


class _PositionerMoving_Type(Integer32):
    """Custom type positionerMoving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stopped", 0),
          ("moving", 1))
    )


_PositionerMoving_Type.__name__ = "Integer32"
_PositionerMoving_Object = MibScalar
positionerMoving = _PositionerMoving_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 2),
    _PositionerMoving_Type()
)
positionerMoving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    positionerMoving.setStatus("current")
_Azimuth_ObjectIdentity = ObjectIdentity
azimuth = _Azimuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 3)
)


class _AzimuthString_Type(DisplayString):
    """Custom type azimuthString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AzimuthString_Type.__name__ = "DisplayString"
_AzimuthString_Object = MibScalar
azimuthString = _AzimuthString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 3, 1),
    _AzimuthString_Type()
)
azimuthString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azimuthString.setStatus("current")
_AzimuthInt_Type = Integer32
_AzimuthInt_Object = MibScalar
azimuthInt = _AzimuthInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 3, 2),
    _AzimuthInt_Type()
)
azimuthInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azimuthInt.setStatus("current")


class _AzimuthFloat_Type(DisplayString):
    """Custom type azimuthFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AzimuthFloat_Type.__name__ = "DisplayString"
_AzimuthFloat_Object = MibScalar
azimuthFloat = _AzimuthFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 3, 3),
    _AzimuthFloat_Type()
)
azimuthFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azimuthFloat.setStatus("current")
_Azimuth360ScaleInt_Type = Integer32
_Azimuth360ScaleInt_Object = MibScalar
azimuth360ScaleInt = _Azimuth360ScaleInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 3, 4),
    _Azimuth360ScaleInt_Type()
)
azimuth360ScaleInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azimuth360ScaleInt.setStatus("current")


class _Azimuth360ScaleFloat_Type(DisplayString):
    """Custom type azimuth360ScaleFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Azimuth360ScaleFloat_Type.__name__ = "DisplayString"
_Azimuth360ScaleFloat_Object = MibScalar
azimuth360ScaleFloat = _Azimuth360ScaleFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 3, 5),
    _Azimuth360ScaleFloat_Type()
)
azimuth360ScaleFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    azimuth360ScaleFloat.setStatus("current")
_Elevation_ObjectIdentity = ObjectIdentity
elevation = _Elevation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 4)
)


class _ElevationString_Type(DisplayString):
    """Custom type elevationString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ElevationString_Type.__name__ = "DisplayString"
_ElevationString_Object = MibScalar
elevationString = _ElevationString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 4, 1),
    _ElevationString_Type()
)
elevationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elevationString.setStatus("current")
_ElevationInt_Type = Integer32
_ElevationInt_Object = MibScalar
elevationInt = _ElevationInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 4, 2),
    _ElevationInt_Type()
)
elevationInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elevationInt.setStatus("current")


class _ElevationFloat_Type(DisplayString):
    """Custom type elevationFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ElevationFloat_Type.__name__ = "DisplayString"
_ElevationFloat_Object = MibScalar
elevationFloat = _ElevationFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 4, 3),
    _ElevationFloat_Type()
)
elevationFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elevationFloat.setStatus("current")
_AntennaHeading_ObjectIdentity = ObjectIdentity
antennaHeading = _AntennaHeading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 5)
)


class _AntennaHeadingString_Type(DisplayString):
    """Custom type antennaHeadingString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AntennaHeadingString_Type.__name__ = "DisplayString"
_AntennaHeadingString_Object = MibScalar
antennaHeadingString = _AntennaHeadingString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 5, 1),
    _AntennaHeadingString_Type()
)
antennaHeadingString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennaHeadingString.setStatus("current")
_AntennaHeadingInt_Type = Integer32
_AntennaHeadingInt_Object = MibScalar
antennaHeadingInt = _AntennaHeadingInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 5, 2),
    _AntennaHeadingInt_Type()
)
antennaHeadingInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennaHeadingInt.setStatus("current")


class _AntennaHeadingFloat_Type(DisplayString):
    """Custom type antennaHeadingFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AntennaHeadingFloat_Type.__name__ = "DisplayString"
_AntennaHeadingFloat_Object = MibScalar
antennaHeadingFloat = _AntennaHeadingFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 5, 3),
    _AntennaHeadingFloat_Type()
)
antennaHeadingFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennaHeadingFloat.setStatus("current")
_AntennaHeading360ScaleInt_Type = Integer32
_AntennaHeading360ScaleInt_Object = MibScalar
antennaHeading360ScaleInt = _AntennaHeading360ScaleInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 5, 4),
    _AntennaHeading360ScaleInt_Type()
)
antennaHeading360ScaleInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennaHeading360ScaleInt.setStatus("current")


class _AntennaHeading360ScaleFloat_Type(DisplayString):
    """Custom type antennaHeading360ScaleFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AntennaHeading360ScaleFloat_Type.__name__ = "DisplayString"
_AntennaHeading360ScaleFloat_Object = MibScalar
antennaHeading360ScaleFloat = _AntennaHeading360ScaleFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 3, 1, 5, 5),
    _AntennaHeading360ScaleFloat_Type()
)
antennaHeading360ScaleFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antennaHeading360ScaleFloat.setStatus("current")
_CurrentGPSHdgAcl_ObjectIdentity = ObjectIdentity
currentGPSHdgAcl = _CurrentGPSHdgAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4)
)


class _CurrentGPSHdgAclString_Type(DisplayString):
    """Custom type currentGPSHdgAclString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSHdgAclString_Type.__name__ = "DisplayString"
_CurrentGPSHdgAclString_Object = MibScalar
currentGPSHdgAclString = _CurrentGPSHdgAclString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 1),
    _CurrentGPSHdgAclString_Type()
)
currentGPSHdgAclString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSHdgAclString.setStatus("current")
_CurrentGPSStatus_ObjectIdentity = ObjectIdentity
currentGPSStatus = _CurrentGPSStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 2)
)


class _CurrentGPSStatusString_Type(DisplayString):
    """Custom type currentGPSStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSStatusString_Type.__name__ = "DisplayString"
_CurrentGPSStatusString_Object = MibScalar
currentGPSStatusString = _CurrentGPSStatusString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 2, 1),
    _CurrentGPSStatusString_Type()
)
currentGPSStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSStatusString.setStatus("current")


class _CurrentGPSStatusInt_Type(Integer32):
    """Custom type currentGPSStatusInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_CurrentGPSStatusInt_Type.__name__ = "Integer32"
_CurrentGPSStatusInt_Object = MibScalar
currentGPSStatusInt = _CurrentGPSStatusInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 2, 2),
    _CurrentGPSStatusInt_Type()
)
currentGPSStatusInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSStatusInt.setStatus("current")


class _CurrentGPSStatusValue_Type(DisplayString):
    """Custom type currentGPSStatusValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSStatusValue_Type.__name__ = "DisplayString"
_CurrentGPSStatusValue_Object = MibScalar
currentGPSStatusValue = _CurrentGPSStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 2, 3),
    _CurrentGPSStatusValue_Type()
)
currentGPSStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSStatusValue.setStatus("current")
_CurrentGPSTimestamp_ObjectIdentity = ObjectIdentity
currentGPSTimestamp = _CurrentGPSTimestamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 3)
)


class _CurrentGPSTimestampString_Type(DisplayString):
    """Custom type currentGPSTimestampString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSTimestampString_Type.__name__ = "DisplayString"
_CurrentGPSTimestampString_Object = MibScalar
currentGPSTimestampString = _CurrentGPSTimestampString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 3, 1),
    _CurrentGPSTimestampString_Type()
)
currentGPSTimestampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSTimestampString.setStatus("current")
_CurrentGPSTimestampInt_Type = Integer32
_CurrentGPSTimestampInt_Object = MibScalar
currentGPSTimestampInt = _CurrentGPSTimestampInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 3, 2),
    _CurrentGPSTimestampInt_Type()
)
currentGPSTimestampInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSTimestampInt.setStatus("current")


class _CurrentGPSTimestampValue_Type(DisplayString):
    """Custom type currentGPSTimestampValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSTimestampValue_Type.__name__ = "DisplayString"
_CurrentGPSTimestampValue_Object = MibScalar
currentGPSTimestampValue = _CurrentGPSTimestampValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 3, 3),
    _CurrentGPSTimestampValue_Type()
)
currentGPSTimestampValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSTimestampValue.setStatus("current")
_CurrentGPSLatitude_ObjectIdentity = ObjectIdentity
currentGPSLatitude = _CurrentGPSLatitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 4)
)


class _CurrentGPSLatitudeString_Type(DisplayString):
    """Custom type currentGPSLatitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSLatitudeString_Type.__name__ = "DisplayString"
_CurrentGPSLatitudeString_Object = MibScalar
currentGPSLatitudeString = _CurrentGPSLatitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 4, 1),
    _CurrentGPSLatitudeString_Type()
)
currentGPSLatitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSLatitudeString.setStatus("current")
_CurrentGPSLatitudeInt_Type = Integer32
_CurrentGPSLatitudeInt_Object = MibScalar
currentGPSLatitudeInt = _CurrentGPSLatitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 4, 2),
    _CurrentGPSLatitudeInt_Type()
)
currentGPSLatitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSLatitudeInt.setStatus("current")


class _CurrentGPSLatitudeFloat_Type(DisplayString):
    """Custom type currentGPSLatitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSLatitudeFloat_Type.__name__ = "DisplayString"
_CurrentGPSLatitudeFloat_Object = MibScalar
currentGPSLatitudeFloat = _CurrentGPSLatitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 4, 3),
    _CurrentGPSLatitudeFloat_Type()
)
currentGPSLatitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSLatitudeFloat.setStatus("current")
_CurrentGPSLongitude_ObjectIdentity = ObjectIdentity
currentGPSLongitude = _CurrentGPSLongitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 5)
)


class _CurrentGPSLongitudeString_Type(DisplayString):
    """Custom type currentGPSLongitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSLongitudeString_Type.__name__ = "DisplayString"
_CurrentGPSLongitudeString_Object = MibScalar
currentGPSLongitudeString = _CurrentGPSLongitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 5, 1),
    _CurrentGPSLongitudeString_Type()
)
currentGPSLongitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSLongitudeString.setStatus("current")
_CurrentGPSLongitudeInt_Type = Integer32
_CurrentGPSLongitudeInt_Object = MibScalar
currentGPSLongitudeInt = _CurrentGPSLongitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 5, 2),
    _CurrentGPSLongitudeInt_Type()
)
currentGPSLongitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSLongitudeInt.setStatus("current")


class _CurrentGPSLongitudeFloat_Type(DisplayString):
    """Custom type currentGPSLongitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSLongitudeFloat_Type.__name__ = "DisplayString"
_CurrentGPSLongitudeFloat_Object = MibScalar
currentGPSLongitudeFloat = _CurrentGPSLongitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 5, 3),
    _CurrentGPSLongitudeFloat_Type()
)
currentGPSLongitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSLongitudeFloat.setStatus("current")
_CurrentGPSAltitude_ObjectIdentity = ObjectIdentity
currentGPSAltitude = _CurrentGPSAltitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 6)
)


class _CurrentGPSAltitudeString_Type(DisplayString):
    """Custom type currentGPSAltitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSAltitudeString_Type.__name__ = "DisplayString"
_CurrentGPSAltitudeString_Object = MibScalar
currentGPSAltitudeString = _CurrentGPSAltitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 6, 1),
    _CurrentGPSAltitudeString_Type()
)
currentGPSAltitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSAltitudeString.setStatus("current")
_CurrentGPSAltitudeInt_Type = Integer32
_CurrentGPSAltitudeInt_Object = MibScalar
currentGPSAltitudeInt = _CurrentGPSAltitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 6, 2),
    _CurrentGPSAltitudeInt_Type()
)
currentGPSAltitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSAltitudeInt.setStatus("current")


class _CurrentGPSAltitudeFloat_Type(DisplayString):
    """Custom type currentGPSAltitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSAltitudeFloat_Type.__name__ = "DisplayString"
_CurrentGPSAltitudeFloat_Object = MibScalar
currentGPSAltitudeFloat = _CurrentGPSAltitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 6, 3),
    _CurrentGPSAltitudeFloat_Type()
)
currentGPSAltitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSAltitudeFloat.setStatus("current")
_CurrentGPSAltitudeFeetInt_Type = Integer32
_CurrentGPSAltitudeFeetInt_Object = MibScalar
currentGPSAltitudeFeetInt = _CurrentGPSAltitudeFeetInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 6, 4),
    _CurrentGPSAltitudeFeetInt_Type()
)
currentGPSAltitudeFeetInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSAltitudeFeetInt.setStatus("current")


class _CurrentGPSAltitudeFeetFloat_Type(DisplayString):
    """Custom type currentGPSAltitudeFeetFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentGPSAltitudeFeetFloat_Type.__name__ = "DisplayString"
_CurrentGPSAltitudeFeetFloat_Object = MibScalar
currentGPSAltitudeFeetFloat = _CurrentGPSAltitudeFeetFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 6, 5),
    _CurrentGPSAltitudeFeetFloat_Type()
)
currentGPSAltitudeFeetFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentGPSAltitudeFeetFloat.setStatus("current")
_CurrentHeadingSection_ObjectIdentity = ObjectIdentity
currentHeadingSection = _CurrentHeadingSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7)
)
_CurrentHeadingStatus_ObjectIdentity = ObjectIdentity
currentHeadingStatus = _CurrentHeadingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 1)
)


class _CurrentHeadingStatusString_Type(DisplayString):
    """Custom type currentHeadingStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentHeadingStatusString_Type.__name__ = "DisplayString"
_CurrentHeadingStatusString_Object = MibScalar
currentHeadingStatusString = _CurrentHeadingStatusString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 1, 1),
    _CurrentHeadingStatusString_Type()
)
currentHeadingStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentHeadingStatusString.setStatus("current")


class _CurrentHeadingStatusInt_Type(Integer32):
    """Custom type currentHeadingStatusInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_CurrentHeadingStatusInt_Type.__name__ = "Integer32"
_CurrentHeadingStatusInt_Object = MibScalar
currentHeadingStatusInt = _CurrentHeadingStatusInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 1, 2),
    _CurrentHeadingStatusInt_Type()
)
currentHeadingStatusInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentHeadingStatusInt.setStatus("current")


class _CurrentHeadingStatusValue_Type(DisplayString):
    """Custom type currentHeadingStatusValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentHeadingStatusValue_Type.__name__ = "DisplayString"
_CurrentHeadingStatusValue_Object = MibScalar
currentHeadingStatusValue = _CurrentHeadingStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 1, 3),
    _CurrentHeadingStatusValue_Type()
)
currentHeadingStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentHeadingStatusValue.setStatus("current")
_CurrentHeading_ObjectIdentity = ObjectIdentity
currentHeading = _CurrentHeading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 2)
)


class _CurrentHeadingString_Type(DisplayString):
    """Custom type currentHeadingString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentHeadingString_Type.__name__ = "DisplayString"
_CurrentHeadingString_Object = MibScalar
currentHeadingString = _CurrentHeadingString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 2, 1),
    _CurrentHeadingString_Type()
)
currentHeadingString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentHeadingString.setStatus("current")
_CurrentHeadingInt_Type = Integer32
_CurrentHeadingInt_Object = MibScalar
currentHeadingInt = _CurrentHeadingInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 2, 2),
    _CurrentHeadingInt_Type()
)
currentHeadingInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentHeadingInt.setStatus("current")


class _CurrentHeadingFloat_Type(DisplayString):
    """Custom type currentHeadingFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentHeadingFloat_Type.__name__ = "DisplayString"
_CurrentHeadingFloat_Object = MibScalar
currentHeadingFloat = _CurrentHeadingFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 2, 3),
    _CurrentHeadingFloat_Type()
)
currentHeadingFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentHeadingFloat.setStatus("current")
_CurrentHeading360ScaleInt_Type = Integer32
_CurrentHeading360ScaleInt_Object = MibScalar
currentHeading360ScaleInt = _CurrentHeading360ScaleInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 2, 4),
    _CurrentHeading360ScaleInt_Type()
)
currentHeading360ScaleInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentHeading360ScaleInt.setStatus("current")


class _CurrentHeading360ScaleFloat_Type(DisplayString):
    """Custom type currentHeading360ScaleFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentHeading360ScaleFloat_Type.__name__ = "DisplayString"
_CurrentHeading360ScaleFloat_Object = MibScalar
currentHeading360ScaleFloat = _CurrentHeading360ScaleFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 7, 2, 5),
    _CurrentHeading360ScaleFloat_Type()
)
currentHeading360ScaleFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentHeading360ScaleFloat.setStatus("current")
_CurrentAccel_ObjectIdentity = ObjectIdentity
currentAccel = _CurrentAccel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8)
)
_CurrentPitch_ObjectIdentity = ObjectIdentity
currentPitch = _CurrentPitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8, 1)
)


class _CurrentPitchString_Type(DisplayString):
    """Custom type currentPitchString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentPitchString_Type.__name__ = "DisplayString"
_CurrentPitchString_Object = MibScalar
currentPitchString = _CurrentPitchString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8, 1, 1),
    _CurrentPitchString_Type()
)
currentPitchString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentPitchString.setStatus("current")
_CurrentPitchInt_Type = Integer32
_CurrentPitchInt_Object = MibScalar
currentPitchInt = _CurrentPitchInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8, 1, 2),
    _CurrentPitchInt_Type()
)
currentPitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentPitchInt.setStatus("current")


class _CurrentPitchFloat_Type(DisplayString):
    """Custom type currentPitchFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentPitchFloat_Type.__name__ = "DisplayString"
_CurrentPitchFloat_Object = MibScalar
currentPitchFloat = _CurrentPitchFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8, 1, 3),
    _CurrentPitchFloat_Type()
)
currentPitchFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentPitchFloat.setStatus("current")
_CurrentRoll_ObjectIdentity = ObjectIdentity
currentRoll = _CurrentRoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8, 2)
)


class _CurrentRollString_Type(DisplayString):
    """Custom type currentRollString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentRollString_Type.__name__ = "DisplayString"
_CurrentRollString_Object = MibScalar
currentRollString = _CurrentRollString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8, 2, 1),
    _CurrentRollString_Type()
)
currentRollString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentRollString.setStatus("current")
_CurrentRollInt_Type = Integer32
_CurrentRollInt_Object = MibScalar
currentRollInt = _CurrentRollInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8, 2, 2),
    _CurrentRollInt_Type()
)
currentRollInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentRollInt.setStatus("current")


class _CurrentRollFloat_Type(DisplayString):
    """Custom type currentRollFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentRollFloat_Type.__name__ = "DisplayString"
_CurrentRollFloat_Object = MibScalar
currentRollFloat = _CurrentRollFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 4, 8, 2, 3),
    _CurrentRollFloat_Type()
)
currentRollFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentRollFloat.setStatus("current")
_LocalGPSHdgAcl_ObjectIdentity = ObjectIdentity
localGPSHdgAcl = _LocalGPSHdgAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5)
)


class _LocalGPSHdgAclString_Type(DisplayString):
    """Custom type localGPSHdgAclString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSHdgAclString_Type.__name__ = "DisplayString"
_LocalGPSHdgAclString_Object = MibScalar
localGPSHdgAclString = _LocalGPSHdgAclString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 1),
    _LocalGPSHdgAclString_Type()
)
localGPSHdgAclString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSHdgAclString.setStatus("current")
_LocalGPSStatus_ObjectIdentity = ObjectIdentity
localGPSStatus = _LocalGPSStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 2)
)


class _LocalGPSStatusString_Type(DisplayString):
    """Custom type localGPSStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSStatusString_Type.__name__ = "DisplayString"
_LocalGPSStatusString_Object = MibScalar
localGPSStatusString = _LocalGPSStatusString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 2, 1),
    _LocalGPSStatusString_Type()
)
localGPSStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSStatusString.setStatus("current")


class _LocalGPSStatusInt_Type(Integer32):
    """Custom type localGPSStatusInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_LocalGPSStatusInt_Type.__name__ = "Integer32"
_LocalGPSStatusInt_Object = MibScalar
localGPSStatusInt = _LocalGPSStatusInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 2, 2),
    _LocalGPSStatusInt_Type()
)
localGPSStatusInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSStatusInt.setStatus("current")


class _LocalGPSStatusValue_Type(DisplayString):
    """Custom type localGPSStatusValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSStatusValue_Type.__name__ = "DisplayString"
_LocalGPSStatusValue_Object = MibScalar
localGPSStatusValue = _LocalGPSStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 2, 3),
    _LocalGPSStatusValue_Type()
)
localGPSStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSStatusValue.setStatus("current")
_LocalGPSTimestamp_ObjectIdentity = ObjectIdentity
localGPSTimestamp = _LocalGPSTimestamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 3)
)


class _LocalGPSTimestampString_Type(DisplayString):
    """Custom type localGPSTimestampString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSTimestampString_Type.__name__ = "DisplayString"
_LocalGPSTimestampString_Object = MibScalar
localGPSTimestampString = _LocalGPSTimestampString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 3, 1),
    _LocalGPSTimestampString_Type()
)
localGPSTimestampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSTimestampString.setStatus("current")
_LocalGPSTimestampInt_Type = Integer32
_LocalGPSTimestampInt_Object = MibScalar
localGPSTimestampInt = _LocalGPSTimestampInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 3, 2),
    _LocalGPSTimestampInt_Type()
)
localGPSTimestampInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSTimestampInt.setStatus("current")


class _LocalGPSTimestampValue_Type(DisplayString):
    """Custom type localGPSTimestampValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSTimestampValue_Type.__name__ = "DisplayString"
_LocalGPSTimestampValue_Object = MibScalar
localGPSTimestampValue = _LocalGPSTimestampValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 3, 3),
    _LocalGPSTimestampValue_Type()
)
localGPSTimestampValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSTimestampValue.setStatus("current")
_LocalGPSLatitude_ObjectIdentity = ObjectIdentity
localGPSLatitude = _LocalGPSLatitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 4)
)


class _LocalGPSLatitudeString_Type(DisplayString):
    """Custom type localGPSLatitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSLatitudeString_Type.__name__ = "DisplayString"
_LocalGPSLatitudeString_Object = MibScalar
localGPSLatitudeString = _LocalGPSLatitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 4, 1),
    _LocalGPSLatitudeString_Type()
)
localGPSLatitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSLatitudeString.setStatus("current")
_LocalGPSLatitudeInt_Type = Integer32
_LocalGPSLatitudeInt_Object = MibScalar
localGPSLatitudeInt = _LocalGPSLatitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 4, 2),
    _LocalGPSLatitudeInt_Type()
)
localGPSLatitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSLatitudeInt.setStatus("current")


class _LocalGPSLatitudeFloat_Type(DisplayString):
    """Custom type localGPSLatitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSLatitudeFloat_Type.__name__ = "DisplayString"
_LocalGPSLatitudeFloat_Object = MibScalar
localGPSLatitudeFloat = _LocalGPSLatitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 4, 3),
    _LocalGPSLatitudeFloat_Type()
)
localGPSLatitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSLatitudeFloat.setStatus("current")
_LocalGPSLongitude_ObjectIdentity = ObjectIdentity
localGPSLongitude = _LocalGPSLongitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 5)
)


class _LocalGPSLongitudeString_Type(DisplayString):
    """Custom type localGPSLongitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSLongitudeString_Type.__name__ = "DisplayString"
_LocalGPSLongitudeString_Object = MibScalar
localGPSLongitudeString = _LocalGPSLongitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 5, 1),
    _LocalGPSLongitudeString_Type()
)
localGPSLongitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSLongitudeString.setStatus("current")
_LocalGPSLongitudeInt_Type = Integer32
_LocalGPSLongitudeInt_Object = MibScalar
localGPSLongitudeInt = _LocalGPSLongitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 5, 2),
    _LocalGPSLongitudeInt_Type()
)
localGPSLongitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSLongitudeInt.setStatus("current")


class _LocalGPSLongitudeFloat_Type(DisplayString):
    """Custom type localGPSLongitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSLongitudeFloat_Type.__name__ = "DisplayString"
_LocalGPSLongitudeFloat_Object = MibScalar
localGPSLongitudeFloat = _LocalGPSLongitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 5, 3),
    _LocalGPSLongitudeFloat_Type()
)
localGPSLongitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSLongitudeFloat.setStatus("current")
_LocalGPSAltitude_ObjectIdentity = ObjectIdentity
localGPSAltitude = _LocalGPSAltitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 6)
)


class _LocalGPSAltitudeString_Type(DisplayString):
    """Custom type localGPSAltitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSAltitudeString_Type.__name__ = "DisplayString"
_LocalGPSAltitudeString_Object = MibScalar
localGPSAltitudeString = _LocalGPSAltitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 6, 1),
    _LocalGPSAltitudeString_Type()
)
localGPSAltitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSAltitudeString.setStatus("current")
_LocalGPSAltitudeInt_Type = Integer32
_LocalGPSAltitudeInt_Object = MibScalar
localGPSAltitudeInt = _LocalGPSAltitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 6, 2),
    _LocalGPSAltitudeInt_Type()
)
localGPSAltitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSAltitudeInt.setStatus("current")


class _LocalGPSAltitudeFloat_Type(DisplayString):
    """Custom type localGPSAltitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSAltitudeFloat_Type.__name__ = "DisplayString"
_LocalGPSAltitudeFloat_Object = MibScalar
localGPSAltitudeFloat = _LocalGPSAltitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 6, 3),
    _LocalGPSAltitudeFloat_Type()
)
localGPSAltitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSAltitudeFloat.setStatus("current")
_LocalGPSAltitudeFeetInt_Type = Integer32
_LocalGPSAltitudeFeetInt_Object = MibScalar
localGPSAltitudeFeetInt = _LocalGPSAltitudeFeetInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 6, 4),
    _LocalGPSAltitudeFeetInt_Type()
)
localGPSAltitudeFeetInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSAltitudeFeetInt.setStatus("current")


class _LocalGPSAltitudeFeetFloat_Type(DisplayString):
    """Custom type localGPSAltitudeFeetFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalGPSAltitudeFeetFloat_Type.__name__ = "DisplayString"
_LocalGPSAltitudeFeetFloat_Object = MibScalar
localGPSAltitudeFeetFloat = _LocalGPSAltitudeFeetFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 6, 5),
    _LocalGPSAltitudeFeetFloat_Type()
)
localGPSAltitudeFeetFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localGPSAltitudeFeetFloat.setStatus("current")
_LocalHeadingSection_ObjectIdentity = ObjectIdentity
localHeadingSection = _LocalHeadingSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7)
)
_LocalHeadingStatus_ObjectIdentity = ObjectIdentity
localHeadingStatus = _LocalHeadingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 1)
)


class _LocalHeadingStatusString_Type(DisplayString):
    """Custom type localHeadingStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalHeadingStatusString_Type.__name__ = "DisplayString"
_LocalHeadingStatusString_Object = MibScalar
localHeadingStatusString = _LocalHeadingStatusString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 1, 1),
    _LocalHeadingStatusString_Type()
)
localHeadingStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHeadingStatusString.setStatus("current")


class _LocalHeadingStatusInt_Type(Integer32):
    """Custom type localHeadingStatusInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_LocalHeadingStatusInt_Type.__name__ = "Integer32"
_LocalHeadingStatusInt_Object = MibScalar
localHeadingStatusInt = _LocalHeadingStatusInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 1, 2),
    _LocalHeadingStatusInt_Type()
)
localHeadingStatusInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHeadingStatusInt.setStatus("current")


class _LocalHeadingStatusValue_Type(DisplayString):
    """Custom type localHeadingStatusValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalHeadingStatusValue_Type.__name__ = "DisplayString"
_LocalHeadingStatusValue_Object = MibScalar
localHeadingStatusValue = _LocalHeadingStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 1, 3),
    _LocalHeadingStatusValue_Type()
)
localHeadingStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHeadingStatusValue.setStatus("current")
_LocalHeading_ObjectIdentity = ObjectIdentity
localHeading = _LocalHeading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 2)
)


class _LocalHeadingString_Type(DisplayString):
    """Custom type localHeadingString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalHeadingString_Type.__name__ = "DisplayString"
_LocalHeadingString_Object = MibScalar
localHeadingString = _LocalHeadingString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 2, 1),
    _LocalHeadingString_Type()
)
localHeadingString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHeadingString.setStatus("current")
_LocalHeadingInt_Type = Integer32
_LocalHeadingInt_Object = MibScalar
localHeadingInt = _LocalHeadingInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 2, 2),
    _LocalHeadingInt_Type()
)
localHeadingInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHeadingInt.setStatus("current")


class _LocalHeadingFloat_Type(DisplayString):
    """Custom type localHeadingFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalHeadingFloat_Type.__name__ = "DisplayString"
_LocalHeadingFloat_Object = MibScalar
localHeadingFloat = _LocalHeadingFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 2, 3),
    _LocalHeadingFloat_Type()
)
localHeadingFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHeadingFloat.setStatus("current")
_LocalHeading360ScaleInt_Type = Integer32
_LocalHeading360ScaleInt_Object = MibScalar
localHeading360ScaleInt = _LocalHeading360ScaleInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 2, 4),
    _LocalHeading360ScaleInt_Type()
)
localHeading360ScaleInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHeading360ScaleInt.setStatus("current")


class _LocalHeading360ScaleFloat_Type(DisplayString):
    """Custom type localHeading360ScaleFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalHeading360ScaleFloat_Type.__name__ = "DisplayString"
_LocalHeading360ScaleFloat_Object = MibScalar
localHeading360ScaleFloat = _LocalHeading360ScaleFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 7, 2, 5),
    _LocalHeading360ScaleFloat_Type()
)
localHeading360ScaleFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localHeading360ScaleFloat.setStatus("current")
_LocalAccel_ObjectIdentity = ObjectIdentity
localAccel = _LocalAccel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8)
)
_LocalPitch_ObjectIdentity = ObjectIdentity
localPitch = _LocalPitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8, 1)
)


class _LocalPitchString_Type(DisplayString):
    """Custom type localPitchString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalPitchString_Type.__name__ = "DisplayString"
_LocalPitchString_Object = MibScalar
localPitchString = _LocalPitchString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8, 1, 1),
    _LocalPitchString_Type()
)
localPitchString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localPitchString.setStatus("current")
_LocalPitchInt_Type = Integer32
_LocalPitchInt_Object = MibScalar
localPitchInt = _LocalPitchInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8, 1, 2),
    _LocalPitchInt_Type()
)
localPitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localPitchInt.setStatus("current")


class _LocalPitchFloat_Type(DisplayString):
    """Custom type localPitchFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalPitchFloat_Type.__name__ = "DisplayString"
_LocalPitchFloat_Object = MibScalar
localPitchFloat = _LocalPitchFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8, 1, 3),
    _LocalPitchFloat_Type()
)
localPitchFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localPitchFloat.setStatus("current")
_LocalRoll_ObjectIdentity = ObjectIdentity
localRoll = _LocalRoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8, 2)
)


class _LocalRollString_Type(DisplayString):
    """Custom type localRollString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalRollString_Type.__name__ = "DisplayString"
_LocalRollString_Object = MibScalar
localRollString = _LocalRollString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8, 2, 1),
    _LocalRollString_Type()
)
localRollString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRollString.setStatus("current")
_LocalRollInt_Type = Integer32
_LocalRollInt_Object = MibScalar
localRollInt = _LocalRollInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8, 2, 2),
    _LocalRollInt_Type()
)
localRollInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRollInt.setStatus("current")


class _LocalRollFloat_Type(DisplayString):
    """Custom type localRollFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LocalRollFloat_Type.__name__ = "DisplayString"
_LocalRollFloat_Object = MibScalar
localRollFloat = _LocalRollFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 5, 8, 2, 3),
    _LocalRollFloat_Type()
)
localRollFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRollFloat.setStatus("current")
_NetworkGPSHdgAcl_ObjectIdentity = ObjectIdentity
networkGPSHdgAcl = _NetworkGPSHdgAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6)
)


class _NetworkGPSHdgAclString_Type(DisplayString):
    """Custom type networkGPSHdgAclString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSHdgAclString_Type.__name__ = "DisplayString"
_NetworkGPSHdgAclString_Object = MibScalar
networkGPSHdgAclString = _NetworkGPSHdgAclString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 1),
    _NetworkGPSHdgAclString_Type()
)
networkGPSHdgAclString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSHdgAclString.setStatus("current")
_NetworkGPSStatus_ObjectIdentity = ObjectIdentity
networkGPSStatus = _NetworkGPSStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 2)
)


class _NetworkGPSStatusString_Type(DisplayString):
    """Custom type networkGPSStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSStatusString_Type.__name__ = "DisplayString"
_NetworkGPSStatusString_Object = MibScalar
networkGPSStatusString = _NetworkGPSStatusString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 2, 1),
    _NetworkGPSStatusString_Type()
)
networkGPSStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSStatusString.setStatus("current")


class _NetworkGPSStatusInt_Type(Integer32):
    """Custom type networkGPSStatusInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_NetworkGPSStatusInt_Type.__name__ = "Integer32"
_NetworkGPSStatusInt_Object = MibScalar
networkGPSStatusInt = _NetworkGPSStatusInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 2, 2),
    _NetworkGPSStatusInt_Type()
)
networkGPSStatusInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSStatusInt.setStatus("current")


class _NetworkGPSStatusValue_Type(DisplayString):
    """Custom type networkGPSStatusValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSStatusValue_Type.__name__ = "DisplayString"
_NetworkGPSStatusValue_Object = MibScalar
networkGPSStatusValue = _NetworkGPSStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 2, 3),
    _NetworkGPSStatusValue_Type()
)
networkGPSStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSStatusValue.setStatus("current")
_NetworkGPSTimestamp_ObjectIdentity = ObjectIdentity
networkGPSTimestamp = _NetworkGPSTimestamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 3)
)


class _NetworkGPSTimestampString_Type(DisplayString):
    """Custom type networkGPSTimestampString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSTimestampString_Type.__name__ = "DisplayString"
_NetworkGPSTimestampString_Object = MibScalar
networkGPSTimestampString = _NetworkGPSTimestampString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 3, 1),
    _NetworkGPSTimestampString_Type()
)
networkGPSTimestampString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSTimestampString.setStatus("current")
_NetworkGPSTimestampInt_Type = Integer32
_NetworkGPSTimestampInt_Object = MibScalar
networkGPSTimestampInt = _NetworkGPSTimestampInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 3, 2),
    _NetworkGPSTimestampInt_Type()
)
networkGPSTimestampInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSTimestampInt.setStatus("current")


class _NetworkGPSTimestampValue_Type(DisplayString):
    """Custom type networkGPSTimestampValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSTimestampValue_Type.__name__ = "DisplayString"
_NetworkGPSTimestampValue_Object = MibScalar
networkGPSTimestampValue = _NetworkGPSTimestampValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 3, 3),
    _NetworkGPSTimestampValue_Type()
)
networkGPSTimestampValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSTimestampValue.setStatus("current")
_NetworkGPSLatitude_ObjectIdentity = ObjectIdentity
networkGPSLatitude = _NetworkGPSLatitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 4)
)


class _NetworkGPSLatitudeString_Type(DisplayString):
    """Custom type networkGPSLatitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSLatitudeString_Type.__name__ = "DisplayString"
_NetworkGPSLatitudeString_Object = MibScalar
networkGPSLatitudeString = _NetworkGPSLatitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 4, 1),
    _NetworkGPSLatitudeString_Type()
)
networkGPSLatitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSLatitudeString.setStatus("current")
_NetworkGPSLatitudeInt_Type = Integer32
_NetworkGPSLatitudeInt_Object = MibScalar
networkGPSLatitudeInt = _NetworkGPSLatitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 4, 2),
    _NetworkGPSLatitudeInt_Type()
)
networkGPSLatitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSLatitudeInt.setStatus("current")


class _NetworkGPSLatitudeFloat_Type(DisplayString):
    """Custom type networkGPSLatitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSLatitudeFloat_Type.__name__ = "DisplayString"
_NetworkGPSLatitudeFloat_Object = MibScalar
networkGPSLatitudeFloat = _NetworkGPSLatitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 4, 3),
    _NetworkGPSLatitudeFloat_Type()
)
networkGPSLatitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSLatitudeFloat.setStatus("current")
_NetworkGPSLongitude_ObjectIdentity = ObjectIdentity
networkGPSLongitude = _NetworkGPSLongitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 5)
)


class _NetworkGPSLongitudeString_Type(DisplayString):
    """Custom type networkGPSLongitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSLongitudeString_Type.__name__ = "DisplayString"
_NetworkGPSLongitudeString_Object = MibScalar
networkGPSLongitudeString = _NetworkGPSLongitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 5, 1),
    _NetworkGPSLongitudeString_Type()
)
networkGPSLongitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSLongitudeString.setStatus("current")
_NetworkGPSLongitudeInt_Type = Integer32
_NetworkGPSLongitudeInt_Object = MibScalar
networkGPSLongitudeInt = _NetworkGPSLongitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 5, 2),
    _NetworkGPSLongitudeInt_Type()
)
networkGPSLongitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSLongitudeInt.setStatus("current")


class _NetworkGPSLongitudeFloat_Type(DisplayString):
    """Custom type networkGPSLongitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSLongitudeFloat_Type.__name__ = "DisplayString"
_NetworkGPSLongitudeFloat_Object = MibScalar
networkGPSLongitudeFloat = _NetworkGPSLongitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 5, 3),
    _NetworkGPSLongitudeFloat_Type()
)
networkGPSLongitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSLongitudeFloat.setStatus("current")
_NetworkGPSAltitude_ObjectIdentity = ObjectIdentity
networkGPSAltitude = _NetworkGPSAltitude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 6)
)


class _NetworkGPSAltitudeString_Type(DisplayString):
    """Custom type networkGPSAltitudeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSAltitudeString_Type.__name__ = "DisplayString"
_NetworkGPSAltitudeString_Object = MibScalar
networkGPSAltitudeString = _NetworkGPSAltitudeString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 6, 1),
    _NetworkGPSAltitudeString_Type()
)
networkGPSAltitudeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSAltitudeString.setStatus("current")
_NetworkGPSAltitudeInt_Type = Integer32
_NetworkGPSAltitudeInt_Object = MibScalar
networkGPSAltitudeInt = _NetworkGPSAltitudeInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 6, 2),
    _NetworkGPSAltitudeInt_Type()
)
networkGPSAltitudeInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSAltitudeInt.setStatus("current")


class _NetworkGPSAltitudeFloat_Type(DisplayString):
    """Custom type networkGPSAltitudeFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSAltitudeFloat_Type.__name__ = "DisplayString"
_NetworkGPSAltitudeFloat_Object = MibScalar
networkGPSAltitudeFloat = _NetworkGPSAltitudeFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 6, 3),
    _NetworkGPSAltitudeFloat_Type()
)
networkGPSAltitudeFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSAltitudeFloat.setStatus("current")
_NetworkGPSAltitudeFeetInt_Type = Integer32
_NetworkGPSAltitudeFeetInt_Object = MibScalar
networkGPSAltitudeFeetInt = _NetworkGPSAltitudeFeetInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 6, 4),
    _NetworkGPSAltitudeFeetInt_Type()
)
networkGPSAltitudeFeetInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSAltitudeFeetInt.setStatus("current")


class _NetworkGPSAltitudeFeetFloat_Type(DisplayString):
    """Custom type networkGPSAltitudeFeetFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkGPSAltitudeFeetFloat_Type.__name__ = "DisplayString"
_NetworkGPSAltitudeFeetFloat_Object = MibScalar
networkGPSAltitudeFeetFloat = _NetworkGPSAltitudeFeetFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 6, 5),
    _NetworkGPSAltitudeFeetFloat_Type()
)
networkGPSAltitudeFeetFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkGPSAltitudeFeetFloat.setStatus("current")
_NetworkHeadingSection_ObjectIdentity = ObjectIdentity
networkHeadingSection = _NetworkHeadingSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7)
)
_NetworkHeadingStatus_ObjectIdentity = ObjectIdentity
networkHeadingStatus = _NetworkHeadingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 1)
)


class _NetworkHeadingStatusString_Type(DisplayString):
    """Custom type networkHeadingStatusString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkHeadingStatusString_Type.__name__ = "DisplayString"
_NetworkHeadingStatusString_Object = MibScalar
networkHeadingStatusString = _NetworkHeadingStatusString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 1, 1),
    _NetworkHeadingStatusString_Type()
)
networkHeadingStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkHeadingStatusString.setStatus("current")


class _NetworkHeadingStatusInt_Type(Integer32):
    """Custom type networkHeadingStatusInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("valid", 1))
    )


_NetworkHeadingStatusInt_Type.__name__ = "Integer32"
_NetworkHeadingStatusInt_Object = MibScalar
networkHeadingStatusInt = _NetworkHeadingStatusInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 1, 2),
    _NetworkHeadingStatusInt_Type()
)
networkHeadingStatusInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkHeadingStatusInt.setStatus("current")


class _NetworkHeadingStatusValue_Type(DisplayString):
    """Custom type networkHeadingStatusValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkHeadingStatusValue_Type.__name__ = "DisplayString"
_NetworkHeadingStatusValue_Object = MibScalar
networkHeadingStatusValue = _NetworkHeadingStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 1, 3),
    _NetworkHeadingStatusValue_Type()
)
networkHeadingStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkHeadingStatusValue.setStatus("current")
_NetworkHeading_ObjectIdentity = ObjectIdentity
networkHeading = _NetworkHeading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 2)
)


class _NetworkHeadingString_Type(DisplayString):
    """Custom type networkHeadingString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkHeadingString_Type.__name__ = "DisplayString"
_NetworkHeadingString_Object = MibScalar
networkHeadingString = _NetworkHeadingString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 2, 1),
    _NetworkHeadingString_Type()
)
networkHeadingString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkHeadingString.setStatus("current")
_NetworkHeadingInt_Type = Integer32
_NetworkHeadingInt_Object = MibScalar
networkHeadingInt = _NetworkHeadingInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 2, 2),
    _NetworkHeadingInt_Type()
)
networkHeadingInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkHeadingInt.setStatus("current")


class _NetworkHeadingFloat_Type(DisplayString):
    """Custom type networkHeadingFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkHeadingFloat_Type.__name__ = "DisplayString"
_NetworkHeadingFloat_Object = MibScalar
networkHeadingFloat = _NetworkHeadingFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 2, 3),
    _NetworkHeadingFloat_Type()
)
networkHeadingFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkHeadingFloat.setStatus("current")
_NetworkHeading360ScaleInt_Type = Integer32
_NetworkHeading360ScaleInt_Object = MibScalar
networkHeading360ScaleInt = _NetworkHeading360ScaleInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 2, 4),
    _NetworkHeading360ScaleInt_Type()
)
networkHeading360ScaleInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkHeading360ScaleInt.setStatus("current")


class _NetworkHeading360ScaleFloat_Type(DisplayString):
    """Custom type networkHeading360ScaleFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkHeading360ScaleFloat_Type.__name__ = "DisplayString"
_NetworkHeading360ScaleFloat_Object = MibScalar
networkHeading360ScaleFloat = _NetworkHeading360ScaleFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 7, 2, 5),
    _NetworkHeading360ScaleFloat_Type()
)
networkHeading360ScaleFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkHeading360ScaleFloat.setStatus("current")
_NetworkAccel_ObjectIdentity = ObjectIdentity
networkAccel = _NetworkAccel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8)
)
_NetworkPitch_ObjectIdentity = ObjectIdentity
networkPitch = _NetworkPitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8, 1)
)


class _NetworkPitchString_Type(DisplayString):
    """Custom type networkPitchString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkPitchString_Type.__name__ = "DisplayString"
_NetworkPitchString_Object = MibScalar
networkPitchString = _NetworkPitchString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8, 1, 1),
    _NetworkPitchString_Type()
)
networkPitchString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkPitchString.setStatus("current")
_NetworkPitchInt_Type = Integer32
_NetworkPitchInt_Object = MibScalar
networkPitchInt = _NetworkPitchInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8, 1, 2),
    _NetworkPitchInt_Type()
)
networkPitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkPitchInt.setStatus("current")


class _NetworkPitchFloat_Type(DisplayString):
    """Custom type networkPitchFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkPitchFloat_Type.__name__ = "DisplayString"
_NetworkPitchFloat_Object = MibScalar
networkPitchFloat = _NetworkPitchFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8, 1, 3),
    _NetworkPitchFloat_Type()
)
networkPitchFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkPitchFloat.setStatus("current")
_NetworkRoll_ObjectIdentity = ObjectIdentity
networkRoll = _NetworkRoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8, 2)
)


class _NetworkRollString_Type(DisplayString):
    """Custom type networkRollString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkRollString_Type.__name__ = "DisplayString"
_NetworkRollString_Object = MibScalar
networkRollString = _NetworkRollString_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8, 2, 1),
    _NetworkRollString_Type()
)
networkRollString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRollString.setStatus("current")
_NetworkRollInt_Type = Integer32
_NetworkRollInt_Object = MibScalar
networkRollInt = _NetworkRollInt_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8, 2, 2),
    _NetworkRollInt_Type()
)
networkRollInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRollInt.setStatus("current")


class _NetworkRollFloat_Type(DisplayString):
    """Custom type networkRollFloat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NetworkRollFloat_Type.__name__ = "DisplayString"
_NetworkRollFloat_Object = MibScalar
networkRollFloat = _NetworkRollFloat_Object(
    (1, 3, 6, 1, 4, 1, 37069, 1, 6, 8, 2, 3),
    _NetworkRollFloat_Type()
)
networkRollFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRollFloat.setStatus("current")
_AatsMIBConformance_ObjectIdentity = ObjectIdentity
aatsMIBConformance = _AatsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 97)
)
_AatsMIBCompliances_ObjectIdentity = ObjectIdentity
aatsMIBCompliances = _AatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 97, 1)
)
_AatsMIBGroups_ObjectIdentity = ObjectIdentity
aatsMIBGroups = _AatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37069, 97, 2)
)

# Managed Objects groups

aatsSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 37069, 97, 2, 8)
)
aatsSnmpGroup.setObjects(
      *(("AATS-MIB", "status"),
        ("AATS-MIB", "active"),
        ("AATS-MIB", "stowed"),
        ("AATS-MIB", "cpuTemp"),
        ("AATS-MIB", "radioName"),
        ("AATS-MIB", "radioConnected"),
        ("AATS-MIB", "linkStatusString"),
        ("AATS-MIB", "linkStatusInt"),
        ("AATS-MIB", "linkStatusVal"),
        ("AATS-MIB", "rssiString"),
        ("AATS-MIB", "rssiInt"),
        ("AATS-MIB", "rssiFloat"),
        ("AATS-MIB", "snrString"),
        ("AATS-MIB", "snrInt"),
        ("AATS-MIB", "snrFloat"),
        ("AATS-MIB", "linkDistanceString"),
        ("AATS-MIB", "linkDistanceMeters"),
        ("AATS-MIB", "linkDistanceMiles"),
        ("AATS-MIB", "remoteString"),
        ("AATS-MIB", "remoteIP"),
        ("AATS-MIB", "remoteMAC"),
        ("AATS-MIB", "positionerConnected"),
        ("AATS-MIB", "positionerMoving"),
        ("AATS-MIB", "azimuthString"),
        ("AATS-MIB", "azimuthInt"),
        ("AATS-MIB", "azimuthFloat"),
        ("AATS-MIB", "azimuth360ScaleInt"),
        ("AATS-MIB", "azimuth360ScaleFloat"),
        ("AATS-MIB", "elevationString"),
        ("AATS-MIB", "elevationInt"),
        ("AATS-MIB", "elevationFloat"),
        ("AATS-MIB", "antennaHeadingString"),
        ("AATS-MIB", "antennaHeadingInt"),
        ("AATS-MIB", "antennaHeadingFloat"),
        ("AATS-MIB", "antennaHeading360ScaleInt"),
        ("AATS-MIB", "antennaHeading360ScaleFloat"),
        ("AATS-MIB", "currentGPSHdgAclString"),
        ("AATS-MIB", "currentGPSStatusString"),
        ("AATS-MIB", "currentGPSStatusInt"),
        ("AATS-MIB", "currentGPSStatusValue"),
        ("AATS-MIB", "currentGPSTimestampString"),
        ("AATS-MIB", "currentGPSTimestampInt"),
        ("AATS-MIB", "currentGPSTimestampValue"),
        ("AATS-MIB", "currentGPSLatitudeString"),
        ("AATS-MIB", "currentGPSLatitudeInt"),
        ("AATS-MIB", "currentGPSLatitudeFloat"),
        ("AATS-MIB", "currentGPSLongitudeString"),
        ("AATS-MIB", "currentGPSLongitudeInt"),
        ("AATS-MIB", "currentGPSLongitudeFloat"),
        ("AATS-MIB", "currentGPSAltitudeString"),
        ("AATS-MIB", "currentGPSAltitudeInt"),
        ("AATS-MIB", "currentGPSAltitudeFloat"),
        ("AATS-MIB", "currentGPSAltitudeFeetInt"),
        ("AATS-MIB", "currentGPSAltitudeFeetFloat"),
        ("AATS-MIB", "currentHeadingStatusString"),
        ("AATS-MIB", "currentHeadingStatusInt"),
        ("AATS-MIB", "currentHeadingStatusValue"),
        ("AATS-MIB", "currentHeadingString"),
        ("AATS-MIB", "currentHeadingInt"),
        ("AATS-MIB", "currentHeadingFloat"),
        ("AATS-MIB", "currentHeading360ScaleInt"),
        ("AATS-MIB", "currentHeading360ScaleFloat"),
        ("AATS-MIB", "currentPitchString"),
        ("AATS-MIB", "currentPitchInt"),
        ("AATS-MIB", "currentPitchFloat"),
        ("AATS-MIB", "currentRollString"),
        ("AATS-MIB", "currentRollInt"),
        ("AATS-MIB", "currentRollFloat"),
        ("AATS-MIB", "localGPSHdgAclString"),
        ("AATS-MIB", "localGPSStatusString"),
        ("AATS-MIB", "localGPSStatusInt"),
        ("AATS-MIB", "localGPSStatusValue"),
        ("AATS-MIB", "localGPSTimestampString"),
        ("AATS-MIB", "localGPSTimestampInt"),
        ("AATS-MIB", "localGPSTimestampValue"),
        ("AATS-MIB", "localGPSLatitudeString"),
        ("AATS-MIB", "localGPSLatitudeInt"),
        ("AATS-MIB", "localGPSLatitudeFloat"),
        ("AATS-MIB", "localGPSLongitudeString"),
        ("AATS-MIB", "localGPSLongitudeInt"),
        ("AATS-MIB", "localGPSLongitudeFloat"),
        ("AATS-MIB", "localGPSAltitudeString"),
        ("AATS-MIB", "localGPSAltitudeInt"),
        ("AATS-MIB", "localGPSAltitudeFloat"),
        ("AATS-MIB", "localGPSAltitudeFeetInt"),
        ("AATS-MIB", "localGPSAltitudeFeetFloat"),
        ("AATS-MIB", "localHeadingStatusString"),
        ("AATS-MIB", "localHeadingStatusInt"),
        ("AATS-MIB", "localHeadingStatusValue"),
        ("AATS-MIB", "localHeadingString"),
        ("AATS-MIB", "localHeadingInt"),
        ("AATS-MIB", "localHeadingFloat"),
        ("AATS-MIB", "localHeading360ScaleInt"),
        ("AATS-MIB", "localHeading360ScaleFloat"),
        ("AATS-MIB", "localPitchString"),
        ("AATS-MIB", "localPitchInt"),
        ("AATS-MIB", "localPitchFloat"),
        ("AATS-MIB", "localRollString"),
        ("AATS-MIB", "localRollInt"),
        ("AATS-MIB", "localRollFloat"),
        ("AATS-MIB", "networkGPSHdgAclString"),
        ("AATS-MIB", "networkGPSStatusString"),
        ("AATS-MIB", "networkGPSStatusInt"),
        ("AATS-MIB", "networkGPSStatusValue"),
        ("AATS-MIB", "networkGPSTimestampString"),
        ("AATS-MIB", "networkGPSTimestampInt"),
        ("AATS-MIB", "networkGPSTimestampValue"),
        ("AATS-MIB", "networkGPSLatitudeString"),
        ("AATS-MIB", "networkGPSLatitudeInt"),
        ("AATS-MIB", "networkGPSLatitudeFloat"),
        ("AATS-MIB", "networkGPSLongitudeString"),
        ("AATS-MIB", "networkGPSLongitudeInt"),
        ("AATS-MIB", "networkGPSLongitudeFloat"),
        ("AATS-MIB", "networkGPSAltitudeString"),
        ("AATS-MIB", "networkGPSAltitudeInt"),
        ("AATS-MIB", "networkGPSAltitudeFloat"),
        ("AATS-MIB", "networkGPSAltitudeFeetInt"),
        ("AATS-MIB", "networkGPSAltitudeFeetFloat"),
        ("AATS-MIB", "networkHeadingStatusString"),
        ("AATS-MIB", "networkHeadingStatusInt"),
        ("AATS-MIB", "networkHeadingStatusValue"),
        ("AATS-MIB", "networkHeadingString"),
        ("AATS-MIB", "networkHeadingInt"),
        ("AATS-MIB", "networkHeadingFloat"),
        ("AATS-MIB", "networkHeading360ScaleInt"),
        ("AATS-MIB", "networkHeading360ScaleFloat"),
        ("AATS-MIB", "networkPitchString"),
        ("AATS-MIB", "networkPitchInt"),
        ("AATS-MIB", "networkPitchFloat"),
        ("AATS-MIB", "networkRollString"),
        ("AATS-MIB", "networkRollInt"),
        ("AATS-MIB", "networkRollFloat"))
)
if mibBuilder.loadTexts:
    aatsSnmpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aatsBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 37069, 97, 1, 2)
)
aatsBasicCompliance.setObjects(
      *(("AATS-MIB", "aatsSnmpGroup"),
        ("AATS-MIB", "aatsSnmpGroup"))
)
if mibBuilder.loadTexts:
    aatsBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AATS-MIB",
    **{"aats": aats,
       "aatsDot1": aatsDot1,
       "system": system,
       "status": status,
       "active": active,
       "stowed": stowed,
       "cpuTemp": cpuTemp,
       "radio": radio,
       "radioName": radioName,
       "radioConnected": radioConnected,
       "linkStatus": linkStatus,
       "linkStatusString": linkStatusString,
       "linkStatusInt": linkStatusInt,
       "linkStatusVal": linkStatusVal,
       "rssi": rssi,
       "rssiString": rssiString,
       "rssiInt": rssiInt,
       "rssiFloat": rssiFloat,
       "snr": snr,
       "snrString": snrString,
       "snrInt": snrInt,
       "snrFloat": snrFloat,
       "linkDistance": linkDistance,
       "linkDistanceString": linkDistanceString,
       "linkDistanceMeters": linkDistanceMeters,
       "linkDistanceMiles": linkDistanceMiles,
       "remote": remote,
       "remoteString": remoteString,
       "remoteIP": remoteIP,
       "remoteMAC": remoteMAC,
       "positioner": positioner,
       "positionerDot1": positionerDot1,
       "positionerConnected": positionerConnected,
       "positionerMoving": positionerMoving,
       "azimuth": azimuth,
       "azimuthString": azimuthString,
       "azimuthInt": azimuthInt,
       "azimuthFloat": azimuthFloat,
       "azimuth360ScaleInt": azimuth360ScaleInt,
       "azimuth360ScaleFloat": azimuth360ScaleFloat,
       "elevation": elevation,
       "elevationString": elevationString,
       "elevationInt": elevationInt,
       "elevationFloat": elevationFloat,
       "antennaHeading": antennaHeading,
       "antennaHeadingString": antennaHeadingString,
       "antennaHeadingInt": antennaHeadingInt,
       "antennaHeadingFloat": antennaHeadingFloat,
       "antennaHeading360ScaleInt": antennaHeading360ScaleInt,
       "antennaHeading360ScaleFloat": antennaHeading360ScaleFloat,
       "currentGPSHdgAcl": currentGPSHdgAcl,
       "currentGPSHdgAclString": currentGPSHdgAclString,
       "currentGPSStatus": currentGPSStatus,
       "currentGPSStatusString": currentGPSStatusString,
       "currentGPSStatusInt": currentGPSStatusInt,
       "currentGPSStatusValue": currentGPSStatusValue,
       "currentGPSTimestamp": currentGPSTimestamp,
       "currentGPSTimestampString": currentGPSTimestampString,
       "currentGPSTimestampInt": currentGPSTimestampInt,
       "currentGPSTimestampValue": currentGPSTimestampValue,
       "currentGPSLatitude": currentGPSLatitude,
       "currentGPSLatitudeString": currentGPSLatitudeString,
       "currentGPSLatitudeInt": currentGPSLatitudeInt,
       "currentGPSLatitudeFloat": currentGPSLatitudeFloat,
       "currentGPSLongitude": currentGPSLongitude,
       "currentGPSLongitudeString": currentGPSLongitudeString,
       "currentGPSLongitudeInt": currentGPSLongitudeInt,
       "currentGPSLongitudeFloat": currentGPSLongitudeFloat,
       "currentGPSAltitude": currentGPSAltitude,
       "currentGPSAltitudeString": currentGPSAltitudeString,
       "currentGPSAltitudeInt": currentGPSAltitudeInt,
       "currentGPSAltitudeFloat": currentGPSAltitudeFloat,
       "currentGPSAltitudeFeetInt": currentGPSAltitudeFeetInt,
       "currentGPSAltitudeFeetFloat": currentGPSAltitudeFeetFloat,
       "currentHeadingSection": currentHeadingSection,
       "currentHeadingStatus": currentHeadingStatus,
       "currentHeadingStatusString": currentHeadingStatusString,
       "currentHeadingStatusInt": currentHeadingStatusInt,
       "currentHeadingStatusValue": currentHeadingStatusValue,
       "currentHeading": currentHeading,
       "currentHeadingString": currentHeadingString,
       "currentHeadingInt": currentHeadingInt,
       "currentHeadingFloat": currentHeadingFloat,
       "currentHeading360ScaleInt": currentHeading360ScaleInt,
       "currentHeading360ScaleFloat": currentHeading360ScaleFloat,
       "currentAccel": currentAccel,
       "currentPitch": currentPitch,
       "currentPitchString": currentPitchString,
       "currentPitchInt": currentPitchInt,
       "currentPitchFloat": currentPitchFloat,
       "currentRoll": currentRoll,
       "currentRollString": currentRollString,
       "currentRollInt": currentRollInt,
       "currentRollFloat": currentRollFloat,
       "localGPSHdgAcl": localGPSHdgAcl,
       "localGPSHdgAclString": localGPSHdgAclString,
       "localGPSStatus": localGPSStatus,
       "localGPSStatusString": localGPSStatusString,
       "localGPSStatusInt": localGPSStatusInt,
       "localGPSStatusValue": localGPSStatusValue,
       "localGPSTimestamp": localGPSTimestamp,
       "localGPSTimestampString": localGPSTimestampString,
       "localGPSTimestampInt": localGPSTimestampInt,
       "localGPSTimestampValue": localGPSTimestampValue,
       "localGPSLatitude": localGPSLatitude,
       "localGPSLatitudeString": localGPSLatitudeString,
       "localGPSLatitudeInt": localGPSLatitudeInt,
       "localGPSLatitudeFloat": localGPSLatitudeFloat,
       "localGPSLongitude": localGPSLongitude,
       "localGPSLongitudeString": localGPSLongitudeString,
       "localGPSLongitudeInt": localGPSLongitudeInt,
       "localGPSLongitudeFloat": localGPSLongitudeFloat,
       "localGPSAltitude": localGPSAltitude,
       "localGPSAltitudeString": localGPSAltitudeString,
       "localGPSAltitudeInt": localGPSAltitudeInt,
       "localGPSAltitudeFloat": localGPSAltitudeFloat,
       "localGPSAltitudeFeetInt": localGPSAltitudeFeetInt,
       "localGPSAltitudeFeetFloat": localGPSAltitudeFeetFloat,
       "localHeadingSection": localHeadingSection,
       "localHeadingStatus": localHeadingStatus,
       "localHeadingStatusString": localHeadingStatusString,
       "localHeadingStatusInt": localHeadingStatusInt,
       "localHeadingStatusValue": localHeadingStatusValue,
       "localHeading": localHeading,
       "localHeadingString": localHeadingString,
       "localHeadingInt": localHeadingInt,
       "localHeadingFloat": localHeadingFloat,
       "localHeading360ScaleInt": localHeading360ScaleInt,
       "localHeading360ScaleFloat": localHeading360ScaleFloat,
       "localAccel": localAccel,
       "localPitch": localPitch,
       "localPitchString": localPitchString,
       "localPitchInt": localPitchInt,
       "localPitchFloat": localPitchFloat,
       "localRoll": localRoll,
       "localRollString": localRollString,
       "localRollInt": localRollInt,
       "localRollFloat": localRollFloat,
       "networkGPSHdgAcl": networkGPSHdgAcl,
       "networkGPSHdgAclString": networkGPSHdgAclString,
       "networkGPSStatus": networkGPSStatus,
       "networkGPSStatusString": networkGPSStatusString,
       "networkGPSStatusInt": networkGPSStatusInt,
       "networkGPSStatusValue": networkGPSStatusValue,
       "networkGPSTimestamp": networkGPSTimestamp,
       "networkGPSTimestampString": networkGPSTimestampString,
       "networkGPSTimestampInt": networkGPSTimestampInt,
       "networkGPSTimestampValue": networkGPSTimestampValue,
       "networkGPSLatitude": networkGPSLatitude,
       "networkGPSLatitudeString": networkGPSLatitudeString,
       "networkGPSLatitudeInt": networkGPSLatitudeInt,
       "networkGPSLatitudeFloat": networkGPSLatitudeFloat,
       "networkGPSLongitude": networkGPSLongitude,
       "networkGPSLongitudeString": networkGPSLongitudeString,
       "networkGPSLongitudeInt": networkGPSLongitudeInt,
       "networkGPSLongitudeFloat": networkGPSLongitudeFloat,
       "networkGPSAltitude": networkGPSAltitude,
       "networkGPSAltitudeString": networkGPSAltitudeString,
       "networkGPSAltitudeInt": networkGPSAltitudeInt,
       "networkGPSAltitudeFloat": networkGPSAltitudeFloat,
       "networkGPSAltitudeFeetInt": networkGPSAltitudeFeetInt,
       "networkGPSAltitudeFeetFloat": networkGPSAltitudeFeetFloat,
       "networkHeadingSection": networkHeadingSection,
       "networkHeadingStatus": networkHeadingStatus,
       "networkHeadingStatusString": networkHeadingStatusString,
       "networkHeadingStatusInt": networkHeadingStatusInt,
       "networkHeadingStatusValue": networkHeadingStatusValue,
       "networkHeading": networkHeading,
       "networkHeadingString": networkHeadingString,
       "networkHeadingInt": networkHeadingInt,
       "networkHeadingFloat": networkHeadingFloat,
       "networkHeading360ScaleInt": networkHeading360ScaleInt,
       "networkHeading360ScaleFloat": networkHeading360ScaleFloat,
       "networkAccel": networkAccel,
       "networkPitch": networkPitch,
       "networkPitchString": networkPitchString,
       "networkPitchInt": networkPitchInt,
       "networkPitchFloat": networkPitchFloat,
       "networkRoll": networkRoll,
       "networkRollString": networkRollString,
       "networkRollInt": networkRollInt,
       "networkRollFloat": networkRollFloat,
       "aatsMIBConformance": aatsMIBConformance,
       "aatsMIBCompliances": aatsMIBCompliances,
       "aatsBasicCompliance": aatsBasicCompliance,
       "aatsMIBGroups": aatsMIBGroups,
       "aatsSnmpGroup": aatsSnmpGroup}
)
