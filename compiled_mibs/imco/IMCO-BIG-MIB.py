# SNMP MIB module (IMCO-BIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\imco\IMCO-BIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:29 2025
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

imcoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3)
)
if mibBuilder.loadTexts:
    imcoMIB.setRevisions(
        ("2006-03-20 10:30",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PositiveInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NonNegativeInteger(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_NetPartner_ObjectIdentity = ObjectIdentity
netPartner = _NetPartner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185)
)
_NpModules_ObjectIdentity = ObjectIdentity
npModules = _NpModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1)
)
_ImcoObjects3_ObjectIdentity = ObjectIdentity
imcoObjects3 = _ImcoObjects3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11)
)
_Imco3Ident_ObjectIdentity = ObjectIdentity
imco3Ident = _Imco3Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 1)
)


class _Imco3IdentManufacturer_Type(DisplayString):
    """Custom type imco3IdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Imco3IdentManufacturer_Type.__name__ = "DisplayString"
_Imco3IdentManufacturer_Object = MibScalar
imco3IdentManufacturer = _Imco3IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 1, 1),
    _Imco3IdentManufacturer_Type()
)
imco3IdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3IdentManufacturer.setStatus("current")


class _Imco3IdentModel_Type(DisplayString):
    """Custom type imco3IdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Imco3IdentModel_Type.__name__ = "DisplayString"
_Imco3IdentModel_Object = MibScalar
imco3IdentModel = _Imco3IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 1, 2),
    _Imco3IdentModel_Type()
)
imco3IdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3IdentModel.setStatus("current")


class _Imco3IdentSwVersion_Type(DisplayString):
    """Custom type imco3IdentSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Imco3IdentSwVersion_Type.__name__ = "DisplayString"
_Imco3IdentSwVersion_Object = MibScalar
imco3IdentSwVersion = _Imco3IdentSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 1, 3),
    _Imco3IdentSwVersion_Type()
)
imco3IdentSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3IdentSwVersion.setStatus("current")


class _Imco3IdentAgentVersion_Type(DisplayString):
    """Custom type imco3IdentAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Imco3IdentAgentVersion_Type.__name__ = "DisplayString"
_Imco3IdentAgentVersion_Object = MibScalar
imco3IdentAgentVersion = _Imco3IdentAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 1, 4),
    _Imco3IdentAgentVersion_Type()
)
imco3IdentAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3IdentAgentVersion.setStatus("current")


class _Imco3IdentName_Type(DisplayString):
    """Custom type imco3IdentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Imco3IdentName_Type.__name__ = "DisplayString"
_Imco3IdentName_Object = MibScalar
imco3IdentName = _Imco3IdentName_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 1, 5),
    _Imco3IdentName_Type()
)
imco3IdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imco3IdentName.setStatus("current")


class _Imco3IdentAttachedDevices_Type(DisplayString):
    """Custom type imco3IdentAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Imco3IdentAttachedDevices_Type.__name__ = "DisplayString"
_Imco3IdentAttachedDevices_Object = MibScalar
imco3IdentAttachedDevices = _Imco3IdentAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 1, 6),
    _Imco3IdentAttachedDevices_Type()
)
imco3IdentAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imco3IdentAttachedDevices.setStatus("current")
_Imco3IdentPMnumber_Type = Integer32
_Imco3IdentPMnumber_Object = MibScalar
imco3IdentPMnumber = _Imco3IdentPMnumber_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 1, 10),
    _Imco3IdentPMnumber_Type()
)
imco3IdentPMnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3IdentPMnumber.setStatus("current")
_Imco3PanM_ObjectIdentity = ObjectIdentity
imco3PanM = _Imco3PanM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2)
)
_ImPanM1_ObjectIdentity = ObjectIdentity
imPanM1 = _ImPanM1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1)
)
_ImPM1SystemID_ObjectIdentity = ObjectIdentity
imPM1SystemID = _ImPM1SystemID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1)
)


class _ImPM1SystemIDManufacturer_Type(DisplayString):
    """Custom type imPM1SystemIDManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM1SystemIDManufacturer_Type.__name__ = "DisplayString"
_ImPM1SystemIDManufacturer_Object = MibScalar
imPM1SystemIDManufacturer = _ImPM1SystemIDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 1),
    _ImPM1SystemIDManufacturer_Type()
)
imPM1SystemIDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDManufacturer.setStatus("current")


class _ImPM1SystemIDType_Type(DisplayString):
    """Custom type imPM1SystemIDType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1SystemIDType_Type.__name__ = "DisplayString"
_ImPM1SystemIDType_Object = MibScalar
imPM1SystemIDType = _ImPM1SystemIDType_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 2),
    _ImPM1SystemIDType_Type()
)
imPM1SystemIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDType.setStatus("current")


class _ImPM1SystemIDserNumb_Type(DisplayString):
    """Custom type imPM1SystemIDserNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1SystemIDserNumb_Type.__name__ = "DisplayString"
_ImPM1SystemIDserNumb_Object = MibScalar
imPM1SystemIDserNumb = _ImPM1SystemIDserNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 3),
    _ImPM1SystemIDserNumb_Type()
)
imPM1SystemIDserNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDserNumb.setStatus("current")


class _ImPM1SystemIDnextServiceDate_Type(DisplayString):
    """Custom type imPM1SystemIDnextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1SystemIDnextServiceDate_Type.__name__ = "DisplayString"
_ImPM1SystemIDnextServiceDate_Object = MibScalar
imPM1SystemIDnextServiceDate = _ImPM1SystemIDnextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 4),
    _ImPM1SystemIDnextServiceDate_Type()
)
imPM1SystemIDnextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDnextServiceDate.setStatus("current")
_ImPM1SystemIDaddress_Type = NonNegativeInteger
_ImPM1SystemIDaddress_Object = MibScalar
imPM1SystemIDaddress = _ImPM1SystemIDaddress_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 5),
    _ImPM1SystemIDaddress_Type()
)
imPM1SystemIDaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDaddress.setStatus("current")
_ImPM1SystemIDhwVersion_Type = NonNegativeInteger
_ImPM1SystemIDhwVersion_Object = MibScalar
imPM1SystemIDhwVersion = _ImPM1SystemIDhwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 6),
    _ImPM1SystemIDhwVersion_Type()
)
imPM1SystemIDhwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDhwVersion.setStatus("current")
_ImPM1SystemIDswVersion_Type = NonNegativeInteger
_ImPM1SystemIDswVersion_Object = MibScalar
imPM1SystemIDswVersion = _ImPM1SystemIDswVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 7),
    _ImPM1SystemIDswVersion_Type()
)
imPM1SystemIDswVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDswVersion.setStatus("current")


class _ImPM1SystemIDPMserialNumber_Type(DisplayString):
    """Custom type imPM1SystemIDPMserialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1SystemIDPMserialNumber_Type.__name__ = "DisplayString"
_ImPM1SystemIDPMserialNumber_Object = MibScalar
imPM1SystemIDPMserialNumber = _ImPM1SystemIDPMserialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 8),
    _ImPM1SystemIDPMserialNumber_Type()
)
imPM1SystemIDPMserialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDPMserialNumber.setStatus("current")


class _ImPM1SystemIDbuttonName_Type(DisplayString):
    """Custom type imPM1SystemIDbuttonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1SystemIDbuttonName_Type.__name__ = "DisplayString"
_ImPM1SystemIDbuttonName_Object = MibScalar
imPM1SystemIDbuttonName = _ImPM1SystemIDbuttonName_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 1, 9),
    _ImPM1SystemIDbuttonName_Type()
)
imPM1SystemIDbuttonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemIDbuttonName.setStatus("current")
_ImPM1SystemGEN_ObjectIdentity = ObjectIdentity
imPM1SystemGEN = _ImPM1SystemGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2)
)


class _ImPM1SystemGENSurgeArrester_Type(Integer32):
    """Custom type imPM1SystemGENSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1SystemGENSurgeArrester_Type.__name__ = "Integer32"
_ImPM1SystemGENSurgeArrester_Object = MibScalar
imPM1SystemGENSurgeArrester = _ImPM1SystemGENSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 1),
    _ImPM1SystemGENSurgeArrester_Type()
)
imPM1SystemGENSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENSurgeArrester.setStatus("current")


class _ImPM1SystemGENDoor1_Type(Integer32):
    """Custom type imPM1SystemGENDoor1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_ImPM1SystemGENDoor1_Type.__name__ = "Integer32"
_ImPM1SystemGENDoor1_Object = MibScalar
imPM1SystemGENDoor1 = _ImPM1SystemGENDoor1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 2),
    _ImPM1SystemGENDoor1_Type()
)
imPM1SystemGENDoor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENDoor1.setStatus("current")


class _ImPM1SystemGENDoor2_Type(Integer32):
    """Custom type imPM1SystemGENDoor2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_ImPM1SystemGENDoor2_Type.__name__ = "Integer32"
_ImPM1SystemGENDoor2_Object = MibScalar
imPM1SystemGENDoor2 = _ImPM1SystemGENDoor2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 3),
    _ImPM1SystemGENDoor2_Type()
)
imPM1SystemGENDoor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENDoor2.setStatus("current")


class _ImPM1SystemGENFan_Type(Integer32):
    """Custom type imPM1SystemGENFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_ImPM1SystemGENFan_Type.__name__ = "Integer32"
_ImPM1SystemGENFan_Object = MibScalar
imPM1SystemGENFan = _ImPM1SystemGENFan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 4),
    _ImPM1SystemGENFan_Type()
)
imPM1SystemGENFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENFan.setStatus("current")


class _ImPM1SystemGENuser1_Type(Integer32):
    """Custom type imPM1SystemGENuser1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1SystemGENuser1_Type.__name__ = "Integer32"
_ImPM1SystemGENuser1_Object = MibScalar
imPM1SystemGENuser1 = _ImPM1SystemGENuser1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 5),
    _ImPM1SystemGENuser1_Type()
)
imPM1SystemGENuser1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENuser1.setStatus("current")


class _ImPM1SystemGENuser2_Type(Integer32):
    """Custom type imPM1SystemGENuser2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1SystemGENuser2_Type.__name__ = "Integer32"
_ImPM1SystemGENuser2_Object = MibScalar
imPM1SystemGENuser2 = _ImPM1SystemGENuser2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 6),
    _ImPM1SystemGENuser2_Type()
)
imPM1SystemGENuser2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENuser2.setStatus("current")


class _ImPM1SystemGENuser3_Type(Integer32):
    """Custom type imPM1SystemGENuser3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1SystemGENuser3_Type.__name__ = "Integer32"
_ImPM1SystemGENuser3_Object = MibScalar
imPM1SystemGENuser3 = _ImPM1SystemGENuser3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 7),
    _ImPM1SystemGENuser3_Type()
)
imPM1SystemGENuser3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENuser3.setStatus("current")


class _ImPM1SystemGENuser4_Type(Integer32):
    """Custom type imPM1SystemGENuser4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1SystemGENuser4_Type.__name__ = "Integer32"
_ImPM1SystemGENuser4_Object = MibScalar
imPM1SystemGENuser4 = _ImPM1SystemGENuser4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 8),
    _ImPM1SystemGENuser4_Type()
)
imPM1SystemGENuser4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENuser4.setStatus("current")
_ImPM1SystemGENtemperature_Type = NonNegativeInteger
_ImPM1SystemGENtemperature_Object = MibScalar
imPM1SystemGENtemperature = _ImPM1SystemGENtemperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 2, 9),
    _ImPM1SystemGENtemperature_Type()
)
imPM1SystemGENtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1SystemGENtemperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM1SystemGENtemperature.setUnits("degrees Centigrade")
_ImPM1Power1_ObjectIdentity = ObjectIdentity
imPM1Power1 = _ImPM1Power1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3)
)


class _ImPM1Power1Manufacturer_Type(DisplayString):
    """Custom type imPM1Power1Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM1Power1Manufacturer_Type.__name__ = "DisplayString"
_ImPM1Power1Manufacturer_Object = MibScalar
imPM1Power1Manufacturer = _ImPM1Power1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 1),
    _ImPM1Power1Manufacturer_Type()
)
imPM1Power1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Manufacturer.setStatus("current")


class _ImPM1Power1Type_Type(DisplayString):
    """Custom type imPM1Power1Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power1Type_Type.__name__ = "DisplayString"
_ImPM1Power1Type_Object = MibScalar
imPM1Power1Type = _ImPM1Power1Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 2),
    _ImPM1Power1Type_Type()
)
imPM1Power1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Type.setStatus("current")


class _ImPM1Power1serNumb_Type(DisplayString):
    """Custom type imPM1Power1serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power1serNumb_Type.__name__ = "DisplayString"
_ImPM1Power1serNumb_Object = MibScalar
imPM1Power1serNumb = _ImPM1Power1serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 3),
    _ImPM1Power1serNumb_Type()
)
imPM1Power1serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1serNumb.setStatus("current")


class _ImPM1Power1nextServiceDate_Type(DisplayString):
    """Custom type imPM1Power1nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power1nextServiceDate_Type.__name__ = "DisplayString"
_ImPM1Power1nextServiceDate_Object = MibScalar
imPM1Power1nextServiceDate = _ImPM1Power1nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 4),
    _ImPM1Power1nextServiceDate_Type()
)
imPM1Power1nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1nextServiceDate.setStatus("current")
_ImPm1Power1InputVoltage_Type = Integer32
_ImPm1Power1InputVoltage_Object = MibScalar
imPm1Power1InputVoltage = _ImPm1Power1InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 5),
    _ImPm1Power1InputVoltage_Type()
)
imPm1Power1InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputVoltage.setUnits("0.1 V")
_ImPm1Power1InputCurrent_Type = Integer32
_ImPm1Power1InputCurrent_Object = MibScalar
imPm1Power1InputCurrent = _ImPm1Power1InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 6),
    _ImPm1Power1InputCurrent_Type()
)
imPm1Power1InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputCurrent.setUnits("0.1 A")
_ImPm1Power1InputPowerVA_Type = Integer32
_ImPm1Power1InputPowerVA_Object = MibScalar
imPm1Power1InputPowerVA = _ImPm1Power1InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 7),
    _ImPm1Power1InputPowerVA_Type()
)
imPm1Power1InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerVA.setUnits("VA")
_ImPm1Power1InputPowerKVA_Type = Integer32
_ImPm1Power1InputPowerKVA_Object = MibScalar
imPm1Power1InputPowerKVA = _ImPm1Power1InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 8),
    _ImPm1Power1InputPowerKVA_Type()
)
imPm1Power1InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKVA.setUnits("0.1 kVA")
_ImPm1Power1InputPowerW_Type = Integer32
_ImPm1Power1InputPowerW_Object = MibScalar
imPm1Power1InputPowerW = _ImPm1Power1InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 9),
    _ImPm1Power1InputPowerW_Type()
)
imPm1Power1InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerW.setUnits("W")
_ImPm1Power1InputPowerKW_Type = Integer32
_ImPm1Power1InputPowerKW_Object = MibScalar
imPm1Power1InputPowerKW = _ImPm1Power1InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 10),
    _ImPm1Power1InputPowerKW_Type()
)
imPm1Power1InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKW.setUnits("0.1 kW")
_ImPm1Power1InputVoltagePhase1_Type = Integer32
_ImPm1Power1InputVoltagePhase1_Object = MibScalar
imPm1Power1InputVoltagePhase1 = _ImPm1Power1InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 11),
    _ImPm1Power1InputVoltagePhase1_Type()
)
imPm1Power1InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputVoltagePhase1.setUnits("0.1 V")
_ImPm1Power1InputCurrentPhase1_Type = Integer32
_ImPm1Power1InputCurrentPhase1_Object = MibScalar
imPm1Power1InputCurrentPhase1 = _ImPm1Power1InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 12),
    _ImPm1Power1InputCurrentPhase1_Type()
)
imPm1Power1InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputCurrentPhase1.setUnits("0.1 A")
_ImPm1Power1InputPowerVAphase1_Type = Integer32
_ImPm1Power1InputPowerVAphase1_Object = MibScalar
imPm1Power1InputPowerVAphase1 = _ImPm1Power1InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 13),
    _ImPm1Power1InputPowerVAphase1_Type()
)
imPm1Power1InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerVAphase1.setUnits("VA")
_ImPm1Power1InputPowerKVAphase1_Type = Integer32
_ImPm1Power1InputPowerKVAphase1_Object = MibScalar
imPm1Power1InputPowerKVAphase1 = _ImPm1Power1InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 14),
    _ImPm1Power1InputPowerKVAphase1_Type()
)
imPm1Power1InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPm1Power1InputVoltagePhase2_Type = Integer32
_ImPm1Power1InputVoltagePhase2_Object = MibScalar
imPm1Power1InputVoltagePhase2 = _ImPm1Power1InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 15),
    _ImPm1Power1InputVoltagePhase2_Type()
)
imPm1Power1InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputVoltagePhase2.setUnits("0.1 V")
_ImPm1Power1InputCurrentPhase2_Type = Integer32
_ImPm1Power1InputCurrentPhase2_Object = MibScalar
imPm1Power1InputCurrentPhase2 = _ImPm1Power1InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 16),
    _ImPm1Power1InputCurrentPhase2_Type()
)
imPm1Power1InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputCurrentPhase2.setUnits("0.1 A")
_ImPm1Power1InputPowerVAphase2_Type = Integer32
_ImPm1Power1InputPowerVAphase2_Object = MibScalar
imPm1Power1InputPowerVAphase2 = _ImPm1Power1InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 17),
    _ImPm1Power1InputPowerVAphase2_Type()
)
imPm1Power1InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerVAphase2.setUnits("VA")
_ImPm1Power1InputPowerKVAphase2_Type = Integer32
_ImPm1Power1InputPowerKVAphase2_Object = MibScalar
imPm1Power1InputPowerKVAphase2 = _ImPm1Power1InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 18),
    _ImPm1Power1InputPowerKVAphase2_Type()
)
imPm1Power1InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPm1Power1InputVoltagePhase3_Type = Integer32
_ImPm1Power1InputVoltagePhase3_Object = MibScalar
imPm1Power1InputVoltagePhase3 = _ImPm1Power1InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 19),
    _ImPm1Power1InputVoltagePhase3_Type()
)
imPm1Power1InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputVoltagePhase3.setUnits("0.1 V")
_ImPm1Power1InputCurrentPhase3_Type = Integer32
_ImPm1Power1InputCurrentPhase3_Object = MibScalar
imPm1Power1InputCurrentPhase3 = _ImPm1Power1InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 20),
    _ImPm1Power1InputCurrentPhase3_Type()
)
imPm1Power1InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputCurrentPhase3.setUnits("0.1 A")
_ImPm1Power1InputPowerVAphase3_Type = Integer32
_ImPm1Power1InputPowerVAphase3_Object = MibScalar
imPm1Power1InputPowerVAphase3 = _ImPm1Power1InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 21),
    _ImPm1Power1InputPowerVAphase3_Type()
)
imPm1Power1InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerVAphase3.setUnits("VA")
_ImPm1Power1InputPowerKVAphase3_Type = Integer32
_ImPm1Power1InputPowerKVAphase3_Object = MibScalar
imPm1Power1InputPowerKVAphase3 = _ImPm1Power1InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 22),
    _ImPm1Power1InputPowerKVAphase3_Type()
)
imPm1Power1InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPm1Power1OutputVoltage_Type = Integer32
_ImPm1Power1OutputVoltage_Object = MibScalar
imPm1Power1OutputVoltage = _ImPm1Power1OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 23),
    _ImPm1Power1OutputVoltage_Type()
)
imPm1Power1OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputVoltage.setUnits("0.1 V")
_ImPm1Power1OutputCurrent_Type = Integer32
_ImPm1Power1OutputCurrent_Object = MibScalar
imPm1Power1OutputCurrent = _ImPm1Power1OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 24),
    _ImPm1Power1OutputCurrent_Type()
)
imPm1Power1OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputCurrent.setUnits("0.1 A")
_ImPm1Power1OutputPowerVA_Type = Integer32
_ImPm1Power1OutputPowerVA_Object = MibScalar
imPm1Power1OutputPowerVA = _ImPm1Power1OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 25),
    _ImPm1Power1OutputPowerVA_Type()
)
imPm1Power1OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerVA.setUnits("VA")
_ImPm1Power1OutputPowerKVA_Type = Integer32
_ImPm1Power1OutputPowerKVA_Object = MibScalar
imPm1Power1OutputPowerKVA = _ImPm1Power1OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 26),
    _ImPm1Power1OutputPowerKVA_Type()
)
imPm1Power1OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKVA.setUnits("0.1 kVA")
_ImPm1Power1OutputPowerW_Type = Integer32
_ImPm1Power1OutputPowerW_Object = MibScalar
imPm1Power1OutputPowerW = _ImPm1Power1OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 27),
    _ImPm1Power1OutputPowerW_Type()
)
imPm1Power1OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerW.setUnits("W")
_ImPm1Power1OutputPowerKW_Type = Integer32
_ImPm1Power1OutputPowerKW_Object = MibScalar
imPm1Power1OutputPowerKW = _ImPm1Power1OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 28),
    _ImPm1Power1OutputPowerKW_Type()
)
imPm1Power1OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKW.setUnits("0.1 kW")
_ImPm1Power1OutputLoad_Type = Integer32
_ImPm1Power1OutputLoad_Object = MibScalar
imPm1Power1OutputLoad = _ImPm1Power1OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 29),
    _ImPm1Power1OutputLoad_Type()
)
imPm1Power1OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputLoad.setUnits("%")
_ImPm1Power1OutputFrequency_Type = NonNegativeInteger
_ImPm1Power1OutputFrequency_Object = MibScalar
imPm1Power1OutputFrequency = _ImPm1Power1OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 30),
    _ImPm1Power1OutputFrequency_Type()
)
imPm1Power1OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputFrequency.setUnits("0.1 Hz")
_ImPm1Power1Temperature_Type = Integer32
_ImPm1Power1Temperature_Object = MibScalar
imPm1Power1Temperature = _ImPm1Power1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 31),
    _ImPm1Power1Temperature_Type()
)
imPm1Power1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1Temperature.setUnits("degrees Centigrade")


class _ImPM1Power1Running1_Type(Integer32):
    """Custom type imPM1Power1Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Running1_Type.__name__ = "Integer32"
_ImPM1Power1Running1_Object = MibScalar
imPM1Power1Running1 = _ImPM1Power1Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 32),
    _ImPM1Power1Running1_Type()
)
imPM1Power1Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Running1.setStatus("current")


class _ImPM1Power1Running2_Type(Integer32):
    """Custom type imPM1Power1Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Running2_Type.__name__ = "Integer32"
_ImPM1Power1Running2_Object = MibScalar
imPM1Power1Running2 = _ImPM1Power1Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 33),
    _ImPM1Power1Running2_Type()
)
imPM1Power1Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Running2.setStatus("current")


class _ImPM1Power1Running3_Type(Integer32):
    """Custom type imPM1Power1Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Running3_Type.__name__ = "Integer32"
_ImPM1Power1Running3_Object = MibScalar
imPM1Power1Running3 = _ImPM1Power1Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 34),
    _ImPM1Power1Running3_Type()
)
imPM1Power1Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Running3.setStatus("current")


class _ImPM1Power1Running4_Type(Integer32):
    """Custom type imPM1Power1Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Running4_Type.__name__ = "Integer32"
_ImPM1Power1Running4_Object = MibScalar
imPM1Power1Running4 = _ImPM1Power1Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 35),
    _ImPM1Power1Running4_Type()
)
imPM1Power1Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Running4.setStatus("current")


class _ImPM1Power1Running5_Type(Integer32):
    """Custom type imPM1Power1Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Running5_Type.__name__ = "Integer32"
_ImPM1Power1Running5_Object = MibScalar
imPM1Power1Running5 = _ImPM1Power1Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 36),
    _ImPM1Power1Running5_Type()
)
imPM1Power1Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Running5.setStatus("current")


class _ImPM1Power1Running6_Type(Integer32):
    """Custom type imPM1Power1Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Running6_Type.__name__ = "Integer32"
_ImPM1Power1Running6_Object = MibScalar
imPM1Power1Running6 = _ImPM1Power1Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 37),
    _ImPM1Power1Running6_Type()
)
imPM1Power1Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Running6.setStatus("current")


class _ImPM1Power1Running7_Type(Integer32):
    """Custom type imPM1Power1Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Running7_Type.__name__ = "Integer32"
_ImPM1Power1Running7_Object = MibScalar
imPM1Power1Running7 = _ImPM1Power1Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 38),
    _ImPM1Power1Running7_Type()
)
imPM1Power1Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Running7.setStatus("current")


class _ImPM1Power1Running8_Type(Integer32):
    """Custom type imPM1Power1Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Running8_Type.__name__ = "Integer32"
_ImPM1Power1Running8_Object = MibScalar
imPM1Power1Running8 = _ImPM1Power1Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 39),
    _ImPM1Power1Running8_Type()
)
imPM1Power1Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Running8.setStatus("current")


class _ImPM1Power1InputFuse_Type(Integer32):
    """Custom type imPM1Power1InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputFuse_Type.__name__ = "Integer32"
_ImPM1Power1InputFuse_Object = MibScalar
imPM1Power1InputFuse = _ImPM1Power1InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 40),
    _ImPM1Power1InputFuse_Type()
)
imPM1Power1InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputFuse.setStatus("current")


class _ImPM1Power1InputFuse1_Type(Integer32):
    """Custom type imPM1Power1InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputFuse1_Type.__name__ = "Integer32"
_ImPM1Power1InputFuse1_Object = MibScalar
imPM1Power1InputFuse1 = _ImPM1Power1InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 41),
    _ImPM1Power1InputFuse1_Type()
)
imPM1Power1InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputFuse1.setStatus("current")


class _ImPM1Power1InputFuse2_Type(Integer32):
    """Custom type imPM1Power1InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputFuse2_Type.__name__ = "Integer32"
_ImPM1Power1InputFuse2_Object = MibScalar
imPM1Power1InputFuse2 = _ImPM1Power1InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 42),
    _ImPM1Power1InputFuse2_Type()
)
imPM1Power1InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputFuse2.setStatus("current")


class _ImPM1Power1InputFuse3_Type(Integer32):
    """Custom type imPM1Power1InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputFuse3_Type.__name__ = "Integer32"
_ImPM1Power1InputFuse3_Object = MibScalar
imPM1Power1InputFuse3 = _ImPM1Power1InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 43),
    _ImPM1Power1InputFuse3_Type()
)
imPM1Power1InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputFuse3.setStatus("current")


class _ImPM1Power1InputBreaker_Type(Integer32):
    """Custom type imPM1Power1InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputBreaker_Type.__name__ = "Integer32"
_ImPM1Power1InputBreaker_Object = MibScalar
imPM1Power1InputBreaker = _ImPM1Power1InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 44),
    _ImPM1Power1InputBreaker_Type()
)
imPM1Power1InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputBreaker.setStatus("current")


class _ImPM1Power1InputBreaker1_Type(Integer32):
    """Custom type imPM1Power1InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputBreaker1_Type.__name__ = "Integer32"
_ImPM1Power1InputBreaker1_Object = MibScalar
imPM1Power1InputBreaker1 = _ImPM1Power1InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 45),
    _ImPM1Power1InputBreaker1_Type()
)
imPM1Power1InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputBreaker1.setStatus("current")


class _ImPM1Power1InputBreaker2_Type(Integer32):
    """Custom type imPM1Power1InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputBreaker2_Type.__name__ = "Integer32"
_ImPM1Power1InputBreaker2_Object = MibScalar
imPM1Power1InputBreaker2 = _ImPM1Power1InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 46),
    _ImPM1Power1InputBreaker2_Type()
)
imPM1Power1InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputBreaker2.setStatus("current")


class _ImPM1Power1InputBreaker3_Type(Integer32):
    """Custom type imPM1Power1InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputBreaker3_Type.__name__ = "Integer32"
_ImPM1Power1InputBreaker3_Object = MibScalar
imPM1Power1InputBreaker3 = _ImPM1Power1InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 47),
    _ImPM1Power1InputBreaker3_Type()
)
imPM1Power1InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputBreaker3.setStatus("current")


class _ImPM1Power1InputSurgeArrester_Type(Integer32):
    """Custom type imPM1Power1InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM1Power1InputSurgeArrester_Object = MibScalar
imPM1Power1InputSurgeArrester = _ImPM1Power1InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 48),
    _ImPM1Power1InputSurgeArrester_Type()
)
imPM1Power1InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1InputSurgeArrester.setStatus("current")


class _ImPM1Power1OutputFuse_Type(Integer32):
    """Custom type imPM1Power1OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1OutputFuse_Type.__name__ = "Integer32"
_ImPM1Power1OutputFuse_Object = MibScalar
imPM1Power1OutputFuse = _ImPM1Power1OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 49),
    _ImPM1Power1OutputFuse_Type()
)
imPM1Power1OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1OutputFuse.setStatus("current")


class _ImPM1Power1OutputFuse1_Type(Integer32):
    """Custom type imPM1Power1OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1OutputFuse1_Type.__name__ = "Integer32"
_ImPM1Power1OutputFuse1_Object = MibScalar
imPM1Power1OutputFuse1 = _ImPM1Power1OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 50),
    _ImPM1Power1OutputFuse1_Type()
)
imPM1Power1OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1OutputFuse1.setStatus("current")


class _ImPM1Power1OutputFuse2_Type(Integer32):
    """Custom type imPM1Power1OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1OutputFuse2_Type.__name__ = "Integer32"
_ImPM1Power1OutputFuse2_Object = MibScalar
imPM1Power1OutputFuse2 = _ImPM1Power1OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 51),
    _ImPM1Power1OutputFuse2_Type()
)
imPM1Power1OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1OutputFuse2.setStatus("current")


class _ImPM1Power1OutputBreaker_Type(Integer32):
    """Custom type imPM1Power1OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1OutputBreaker_Type.__name__ = "Integer32"
_ImPM1Power1OutputBreaker_Object = MibScalar
imPM1Power1OutputBreaker = _ImPM1Power1OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 52),
    _ImPM1Power1OutputBreaker_Type()
)
imPM1Power1OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1OutputBreaker.setStatus("current")


class _ImPM1Power1OutputBreaker1_Type(Integer32):
    """Custom type imPM1Power1OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1OutputBreaker1_Type.__name__ = "Integer32"
_ImPM1Power1OutputBreaker1_Object = MibScalar
imPM1Power1OutputBreaker1 = _ImPM1Power1OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 53),
    _ImPM1Power1OutputBreaker1_Type()
)
imPM1Power1OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1OutputBreaker1.setStatus("current")


class _ImPM1Power1OutputBreaker2_Type(Integer32):
    """Custom type imPM1Power1OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1OutputBreaker2_Type.__name__ = "Integer32"
_ImPM1Power1OutputBreaker2_Object = MibScalar
imPM1Power1OutputBreaker2 = _ImPM1Power1OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 54),
    _ImPM1Power1OutputBreaker2_Type()
)
imPM1Power1OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1OutputBreaker2.setStatus("current")


class _ImPM1Power1Fan_Type(Integer32):
    """Custom type imPM1Power1Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1Fan_Type.__name__ = "Integer32"
_ImPM1Power1Fan_Object = MibScalar
imPM1Power1Fan = _ImPM1Power1Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 55),
    _ImPM1Power1Fan_Type()
)
imPM1Power1Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1Fan.setStatus("current")


class _ImPM1Power1BatteryAvailable_Type(Integer32):
    """Custom type imPM1Power1BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power1BatteryAvailable_Type.__name__ = "Integer32"
_ImPM1Power1BatteryAvailable_Object = MibScalar
imPM1Power1BatteryAvailable = _ImPM1Power1BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 56),
    _ImPM1Power1BatteryAvailable_Type()
)
imPM1Power1BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power1BatteryAvailable.setStatus("current")
_ImPm1Power1OutputVoltagePhase1_Type = Integer32
_ImPm1Power1OutputVoltagePhase1_Object = MibScalar
imPm1Power1OutputVoltagePhase1 = _ImPm1Power1OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 57),
    _ImPm1Power1OutputVoltagePhase1_Type()
)
imPm1Power1OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputVoltagePhase1.setUnits("0.1 V")
_ImPm1Power1OutputCurrentPhase1_Type = Integer32
_ImPm1Power1OutputCurrentPhase1_Object = MibScalar
imPm1Power1OutputCurrentPhase1 = _ImPm1Power1OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 58),
    _ImPm1Power1OutputCurrentPhase1_Type()
)
imPm1Power1OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputCurrentPhase1.setUnits("0.1 A")
_ImPm1Power1OutputPowerVAphase1_Type = Integer32
_ImPm1Power1OutputPowerVAphase1_Object = MibScalar
imPm1Power1OutputPowerVAphase1 = _ImPm1Power1OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 59),
    _ImPm1Power1OutputPowerVAphase1_Type()
)
imPm1Power1OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerVAphase1.setUnits("VA")
_ImPm1Power1OutputPowerKVAphase1_Type = Integer32
_ImPm1Power1OutputPowerKVAphase1_Object = MibScalar
imPm1Power1OutputPowerKVAphase1 = _ImPm1Power1OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 60),
    _ImPm1Power1OutputPowerKVAphase1_Type()
)
imPm1Power1OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPm1Power1OutputVoltagePhase2_Type = Integer32
_ImPm1Power1OutputVoltagePhase2_Object = MibScalar
imPm1Power1OutputVoltagePhase2 = _ImPm1Power1OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 61),
    _ImPm1Power1OutputVoltagePhase2_Type()
)
imPm1Power1OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputVoltagePhase2.setUnits("0.1 V")
_ImPm1Power1OutputCurrentPhase2_Type = Integer32
_ImPm1Power1OutputCurrentPhase2_Object = MibScalar
imPm1Power1OutputCurrentPhase2 = _ImPm1Power1OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 62),
    _ImPm1Power1OutputCurrentPhase2_Type()
)
imPm1Power1OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputCurrentPhase2.setUnits("0.1 A")
_ImPm1Power1OutputPowerVAphase2_Type = Integer32
_ImPm1Power1OutputPowerVAphase2_Object = MibScalar
imPm1Power1OutputPowerVAphase2 = _ImPm1Power1OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 63),
    _ImPm1Power1OutputPowerVAphase2_Type()
)
imPm1Power1OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerVAphase2.setUnits("VA")
_ImPm1Power1OutputPowerKVAphase2_Type = Integer32
_ImPm1Power1OutputPowerKVAphase2_Object = MibScalar
imPm1Power1OutputPowerKVAphase2 = _ImPm1Power1OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 64),
    _ImPm1Power1OutputPowerKVAphase2_Type()
)
imPm1Power1OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPm1Power1OutputVoltagePhase3_Type = Integer32
_ImPm1Power1OutputVoltagePhase3_Object = MibScalar
imPm1Power1OutputVoltagePhase3 = _ImPm1Power1OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 65),
    _ImPm1Power1OutputVoltagePhase3_Type()
)
imPm1Power1OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputVoltagePhase3.setUnits("0.1 V")
_ImPm1Power1OutputCurrentPhase3_Type = Integer32
_ImPm1Power1OutputCurrentPhase3_Object = MibScalar
imPm1Power1OutputCurrentPhase3 = _ImPm1Power1OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 66),
    _ImPm1Power1OutputCurrentPhase3_Type()
)
imPm1Power1OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputCurrentPhase3.setUnits("0.1 A")
_ImPm1Power1OutputPowerVAphase3_Type = Integer32
_ImPm1Power1OutputPowerVAphase3_Object = MibScalar
imPm1Power1OutputPowerVAphase3 = _ImPm1Power1OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 67),
    _ImPm1Power1OutputPowerVAphase3_Type()
)
imPm1Power1OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerVAphase3.setUnits("VA")
_ImPm1Power1OutputPowerKVAphase3_Type = Integer32
_ImPm1Power1OutputPowerKVAphase3_Object = MibScalar
imPm1Power1OutputPowerKVAphase3 = _ImPm1Power1OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 3, 68),
    _ImPm1Power1OutputPowerKVAphase3_Type()
)
imPm1Power1OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power1OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM1Power2_ObjectIdentity = ObjectIdentity
imPM1Power2 = _ImPM1Power2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4)
)


class _ImPM1Power2Manufacturer_Type(DisplayString):
    """Custom type imPM1Power2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM1Power2Manufacturer_Type.__name__ = "DisplayString"
_ImPM1Power2Manufacturer_Object = MibScalar
imPM1Power2Manufacturer = _ImPM1Power2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 1),
    _ImPM1Power2Manufacturer_Type()
)
imPM1Power2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Manufacturer.setStatus("current")


class _ImPM1Power2Type_Type(DisplayString):
    """Custom type imPM1Power2Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power2Type_Type.__name__ = "DisplayString"
_ImPM1Power2Type_Object = MibScalar
imPM1Power2Type = _ImPM1Power2Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 2),
    _ImPM1Power2Type_Type()
)
imPM1Power2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Type.setStatus("current")


class _ImPM1Power2serNumb_Type(DisplayString):
    """Custom type imPM1Power2serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power2serNumb_Type.__name__ = "DisplayString"
_ImPM1Power2serNumb_Object = MibScalar
imPM1Power2serNumb = _ImPM1Power2serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 3),
    _ImPM1Power2serNumb_Type()
)
imPM1Power2serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2serNumb.setStatus("current")


class _ImPM1Power2nextServiceDate_Type(DisplayString):
    """Custom type imPM1Power2nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power2nextServiceDate_Type.__name__ = "DisplayString"
_ImPM1Power2nextServiceDate_Object = MibScalar
imPM1Power2nextServiceDate = _ImPM1Power2nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 4),
    _ImPM1Power2nextServiceDate_Type()
)
imPM1Power2nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2nextServiceDate.setStatus("current")
_ImPm1Power2InputVoltage_Type = Integer32
_ImPm1Power2InputVoltage_Object = MibScalar
imPm1Power2InputVoltage = _ImPm1Power2InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 5),
    _ImPm1Power2InputVoltage_Type()
)
imPm1Power2InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputVoltage.setUnits("0.1 V")
_ImPm1Power2InputCurrent_Type = Integer32
_ImPm1Power2InputCurrent_Object = MibScalar
imPm1Power2InputCurrent = _ImPm1Power2InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 6),
    _ImPm1Power2InputCurrent_Type()
)
imPm1Power2InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputCurrent.setUnits("0.1 A")
_ImPm1Power2InputPowerVA_Type = Integer32
_ImPm1Power2InputPowerVA_Object = MibScalar
imPm1Power2InputPowerVA = _ImPm1Power2InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 7),
    _ImPm1Power2InputPowerVA_Type()
)
imPm1Power2InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerVA.setUnits("VA")
_ImPm1Power2InputPowerKVA_Type = Integer32
_ImPm1Power2InputPowerKVA_Object = MibScalar
imPm1Power2InputPowerKVA = _ImPm1Power2InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 8),
    _ImPm1Power2InputPowerKVA_Type()
)
imPm1Power2InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKVA.setUnits("0.1 kVA")
_ImPm1Power2InputPowerW_Type = Integer32
_ImPm1Power2InputPowerW_Object = MibScalar
imPm1Power2InputPowerW = _ImPm1Power2InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 9),
    _ImPm1Power2InputPowerW_Type()
)
imPm1Power2InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerW.setUnits("W")
_ImPm1Power2InputPowerKW_Type = Integer32
_ImPm1Power2InputPowerKW_Object = MibScalar
imPm1Power2InputPowerKW = _ImPm1Power2InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 10),
    _ImPm1Power2InputPowerKW_Type()
)
imPm1Power2InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKW.setUnits("0.1 kW")
_ImPm1Power2InputVoltagePhase1_Type = Integer32
_ImPm1Power2InputVoltagePhase1_Object = MibScalar
imPm1Power2InputVoltagePhase1 = _ImPm1Power2InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 11),
    _ImPm1Power2InputVoltagePhase1_Type()
)
imPm1Power2InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputVoltagePhase1.setUnits("0.1 V")
_ImPm1Power2InputCurrentPhase1_Type = Integer32
_ImPm1Power2InputCurrentPhase1_Object = MibScalar
imPm1Power2InputCurrentPhase1 = _ImPm1Power2InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 12),
    _ImPm1Power2InputCurrentPhase1_Type()
)
imPm1Power2InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputCurrentPhase1.setUnits("0.1 A")
_ImPm1Power2InputPowerVAphase1_Type = Integer32
_ImPm1Power2InputPowerVAphase1_Object = MibScalar
imPm1Power2InputPowerVAphase1 = _ImPm1Power2InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 13),
    _ImPm1Power2InputPowerVAphase1_Type()
)
imPm1Power2InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerVAphase1.setUnits("VA")
_ImPm1Power2InputPowerKVAphase1_Type = Integer32
_ImPm1Power2InputPowerKVAphase1_Object = MibScalar
imPm1Power2InputPowerKVAphase1 = _ImPm1Power2InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 14),
    _ImPm1Power2InputPowerKVAphase1_Type()
)
imPm1Power2InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPm1Power2InputVoltagePhase2_Type = Integer32
_ImPm1Power2InputVoltagePhase2_Object = MibScalar
imPm1Power2InputVoltagePhase2 = _ImPm1Power2InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 15),
    _ImPm1Power2InputVoltagePhase2_Type()
)
imPm1Power2InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputVoltagePhase2.setUnits("0.1 V")
_ImPm1Power2InputCurrentPhase2_Type = Integer32
_ImPm1Power2InputCurrentPhase2_Object = MibScalar
imPm1Power2InputCurrentPhase2 = _ImPm1Power2InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 16),
    _ImPm1Power2InputCurrentPhase2_Type()
)
imPm1Power2InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputCurrentPhase2.setUnits("0.1 A")
_ImPm1Power2InputPowerVAphase2_Type = Integer32
_ImPm1Power2InputPowerVAphase2_Object = MibScalar
imPm1Power2InputPowerVAphase2 = _ImPm1Power2InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 17),
    _ImPm1Power2InputPowerVAphase2_Type()
)
imPm1Power2InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerVAphase2.setUnits("VA")
_ImPm1Power2InputPowerKVAphase2_Type = Integer32
_ImPm1Power2InputPowerKVAphase2_Object = MibScalar
imPm1Power2InputPowerKVAphase2 = _ImPm1Power2InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 18),
    _ImPm1Power2InputPowerKVAphase2_Type()
)
imPm1Power2InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPm1Power2InputVoltagePhase3_Type = Integer32
_ImPm1Power2InputVoltagePhase3_Object = MibScalar
imPm1Power2InputVoltagePhase3 = _ImPm1Power2InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 19),
    _ImPm1Power2InputVoltagePhase3_Type()
)
imPm1Power2InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputVoltagePhase3.setUnits("0.1 V")
_ImPm1Power2InputCurrentPhase3_Type = Integer32
_ImPm1Power2InputCurrentPhase3_Object = MibScalar
imPm1Power2InputCurrentPhase3 = _ImPm1Power2InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 20),
    _ImPm1Power2InputCurrentPhase3_Type()
)
imPm1Power2InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputCurrentPhase3.setUnits("0.1 A")
_ImPm1Power2InputPowerVAphase3_Type = Integer32
_ImPm1Power2InputPowerVAphase3_Object = MibScalar
imPm1Power2InputPowerVAphase3 = _ImPm1Power2InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 21),
    _ImPm1Power2InputPowerVAphase3_Type()
)
imPm1Power2InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerVAphase3.setUnits("VA")
_ImPm1Power2InputPowerKVAphase3_Type = Integer32
_ImPm1Power2InputPowerKVAphase3_Object = MibScalar
imPm1Power2InputPowerKVAphase3 = _ImPm1Power2InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 22),
    _ImPm1Power2InputPowerKVAphase3_Type()
)
imPm1Power2InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPm1Power2OutputVoltage_Type = Integer32
_ImPm1Power2OutputVoltage_Object = MibScalar
imPm1Power2OutputVoltage = _ImPm1Power2OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 23),
    _ImPm1Power2OutputVoltage_Type()
)
imPm1Power2OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2OutputVoltage.setUnits("0.1 V")
_ImPm1Power2OutputCurrent_Type = Integer32
_ImPm1Power2OutputCurrent_Object = MibScalar
imPm1Power2OutputCurrent = _ImPm1Power2OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 24),
    _ImPm1Power2OutputCurrent_Type()
)
imPm1Power2OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2OutputCurrent.setUnits("0.1 A")
_ImPm1Power2OutputPowerVA_Type = Integer32
_ImPm1Power2OutputPowerVA_Object = MibScalar
imPm1Power2OutputPowerVA = _ImPm1Power2OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 25),
    _ImPm1Power2OutputPowerVA_Type()
)
imPm1Power2OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2OutputPowerVA.setUnits("VA")
_ImPm1Power2OutputPowerKVA_Type = Integer32
_ImPm1Power2OutputPowerKVA_Object = MibScalar
imPm1Power2OutputPowerKVA = _ImPm1Power2OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 26),
    _ImPm1Power2OutputPowerKVA_Type()
)
imPm1Power2OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2OutputPowerKVA.setUnits("0.1 kVA")
_ImPm1Power2OutputPowerW_Type = Integer32
_ImPm1Power2OutputPowerW_Object = MibScalar
imPm1Power2OutputPowerW = _ImPm1Power2OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 27),
    _ImPm1Power2OutputPowerW_Type()
)
imPm1Power2OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2OutputPowerW.setUnits("W")
_ImPm1Power2OutputPowerKW_Type = Integer32
_ImPm1Power2OutputPowerKW_Object = MibScalar
imPm1Power2OutputPowerKW = _ImPm1Power2OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 28),
    _ImPm1Power2OutputPowerKW_Type()
)
imPm1Power2OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2OutputPowerKW.setUnits("0.1 kW")
_ImPm1Power2OutputLoad_Type = Integer32
_ImPm1Power2OutputLoad_Object = MibScalar
imPm1Power2OutputLoad = _ImPm1Power2OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 29),
    _ImPm1Power2OutputLoad_Type()
)
imPm1Power2OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2OutputLoad.setUnits("%")
_ImPm1Power2OutputFrequency_Type = NonNegativeInteger
_ImPm1Power2OutputFrequency_Object = MibScalar
imPm1Power2OutputFrequency = _ImPm1Power2OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 30),
    _ImPm1Power2OutputFrequency_Type()
)
imPm1Power2OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2OutputFrequency.setUnits("0.1 Hz")
_ImPm1Power2Temperature_Type = Integer32
_ImPm1Power2Temperature_Object = MibScalar
imPm1Power2Temperature = _ImPm1Power2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 31),
    _ImPm1Power2Temperature_Type()
)
imPm1Power2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power2Temperature.setUnits("degrees Centigrade")


class _ImPM1Power2Running1_Type(Integer32):
    """Custom type imPM1Power2Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Running1_Type.__name__ = "Integer32"
_ImPM1Power2Running1_Object = MibScalar
imPM1Power2Running1 = _ImPM1Power2Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 32),
    _ImPM1Power2Running1_Type()
)
imPM1Power2Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Running1.setStatus("current")


class _ImPM1Power2Running2_Type(Integer32):
    """Custom type imPM1Power2Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Running2_Type.__name__ = "Integer32"
_ImPM1Power2Running2_Object = MibScalar
imPM1Power2Running2 = _ImPM1Power2Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 33),
    _ImPM1Power2Running2_Type()
)
imPM1Power2Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Running2.setStatus("current")


class _ImPM1Power2Running3_Type(Integer32):
    """Custom type imPM1Power2Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Running3_Type.__name__ = "Integer32"
_ImPM1Power2Running3_Object = MibScalar
imPM1Power2Running3 = _ImPM1Power2Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 34),
    _ImPM1Power2Running3_Type()
)
imPM1Power2Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Running3.setStatus("current")


class _ImPM1Power2Running4_Type(Integer32):
    """Custom type imPM1Power2Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Running4_Type.__name__ = "Integer32"
_ImPM1Power2Running4_Object = MibScalar
imPM1Power2Running4 = _ImPM1Power2Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 35),
    _ImPM1Power2Running4_Type()
)
imPM1Power2Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Running4.setStatus("current")


class _ImPM1Power2Running5_Type(Integer32):
    """Custom type imPM1Power2Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Running5_Type.__name__ = "Integer32"
_ImPM1Power2Running5_Object = MibScalar
imPM1Power2Running5 = _ImPM1Power2Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 36),
    _ImPM1Power2Running5_Type()
)
imPM1Power2Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Running5.setStatus("current")


class _ImPM1Power2Running6_Type(Integer32):
    """Custom type imPM1Power2Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Running6_Type.__name__ = "Integer32"
_ImPM1Power2Running6_Object = MibScalar
imPM1Power2Running6 = _ImPM1Power2Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 37),
    _ImPM1Power2Running6_Type()
)
imPM1Power2Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Running6.setStatus("current")


class _ImPM1Power2Running7_Type(Integer32):
    """Custom type imPM1Power2Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Running7_Type.__name__ = "Integer32"
_ImPM1Power2Running7_Object = MibScalar
imPM1Power2Running7 = _ImPM1Power2Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 38),
    _ImPM1Power2Running7_Type()
)
imPM1Power2Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Running7.setStatus("current")


class _ImPM1Power2Running8_Type(Integer32):
    """Custom type imPM1Power2Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Running8_Type.__name__ = "Integer32"
_ImPM1Power2Running8_Object = MibScalar
imPM1Power2Running8 = _ImPM1Power2Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 39),
    _ImPM1Power2Running8_Type()
)
imPM1Power2Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Running8.setStatus("current")


class _ImPM1Power2InputFuse_Type(Integer32):
    """Custom type imPM1Power2InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputFuse_Type.__name__ = "Integer32"
_ImPM1Power2InputFuse_Object = MibScalar
imPM1Power2InputFuse = _ImPM1Power2InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 40),
    _ImPM1Power2InputFuse_Type()
)
imPM1Power2InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputFuse.setStatus("current")


class _ImPM1Power2InputFuse1_Type(Integer32):
    """Custom type imPM1Power2InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputFuse1_Type.__name__ = "Integer32"
_ImPM1Power2InputFuse1_Object = MibScalar
imPM1Power2InputFuse1 = _ImPM1Power2InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 41),
    _ImPM1Power2InputFuse1_Type()
)
imPM1Power2InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputFuse1.setStatus("current")


class _ImPM1Power2InputFuse2_Type(Integer32):
    """Custom type imPM1Power2InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputFuse2_Type.__name__ = "Integer32"
_ImPM1Power2InputFuse2_Object = MibScalar
imPM1Power2InputFuse2 = _ImPM1Power2InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 42),
    _ImPM1Power2InputFuse2_Type()
)
imPM1Power2InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputFuse2.setStatus("current")


class _ImPM1Power2InputFuse3_Type(Integer32):
    """Custom type imPM1Power2InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputFuse3_Type.__name__ = "Integer32"
_ImPM1Power2InputFuse3_Object = MibScalar
imPM1Power2InputFuse3 = _ImPM1Power2InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 43),
    _ImPM1Power2InputFuse3_Type()
)
imPM1Power2InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputFuse3.setStatus("current")


class _ImPM1Power2InputBreaker_Type(Integer32):
    """Custom type imPM1Power2InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputBreaker_Type.__name__ = "Integer32"
_ImPM1Power2InputBreaker_Object = MibScalar
imPM1Power2InputBreaker = _ImPM1Power2InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 44),
    _ImPM1Power2InputBreaker_Type()
)
imPM1Power2InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputBreaker.setStatus("current")


class _ImPM1Power2InputBreaker1_Type(Integer32):
    """Custom type imPM1Power2InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputBreaker1_Type.__name__ = "Integer32"
_ImPM1Power2InputBreaker1_Object = MibScalar
imPM1Power2InputBreaker1 = _ImPM1Power2InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 45),
    _ImPM1Power2InputBreaker1_Type()
)
imPM1Power2InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputBreaker1.setStatus("current")


class _ImPM1Power2InputBreaker2_Type(Integer32):
    """Custom type imPM1Power2InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputBreaker2_Type.__name__ = "Integer32"
_ImPM1Power2InputBreaker2_Object = MibScalar
imPM1Power2InputBreaker2 = _ImPM1Power2InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 46),
    _ImPM1Power2InputBreaker2_Type()
)
imPM1Power2InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputBreaker2.setStatus("current")


class _ImPM1Power2InputBreaker3_Type(Integer32):
    """Custom type imPM1Power2InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputBreaker3_Type.__name__ = "Integer32"
_ImPM1Power2InputBreaker3_Object = MibScalar
imPM1Power2InputBreaker3 = _ImPM1Power2InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 47),
    _ImPM1Power2InputBreaker3_Type()
)
imPM1Power2InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputBreaker3.setStatus("current")


class _ImPM1Power2InputSurgeArrester_Type(Integer32):
    """Custom type imPM1Power2InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM1Power2InputSurgeArrester_Object = MibScalar
imPM1Power2InputSurgeArrester = _ImPM1Power2InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 48),
    _ImPM1Power2InputSurgeArrester_Type()
)
imPM1Power2InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2InputSurgeArrester.setStatus("current")


class _ImPM1Power2OutputFuse_Type(Integer32):
    """Custom type imPM1Power2OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2OutputFuse_Type.__name__ = "Integer32"
_ImPM1Power2OutputFuse_Object = MibScalar
imPM1Power2OutputFuse = _ImPM1Power2OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 49),
    _ImPM1Power2OutputFuse_Type()
)
imPM1Power2OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputFuse.setStatus("current")


class _ImPM1Power2OutputFuse1_Type(Integer32):
    """Custom type imPM1Power2OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2OutputFuse1_Type.__name__ = "Integer32"
_ImPM1Power2OutputFuse1_Object = MibScalar
imPM1Power2OutputFuse1 = _ImPM1Power2OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 50),
    _ImPM1Power2OutputFuse1_Type()
)
imPM1Power2OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputFuse1.setStatus("current")


class _ImPM1Power2OutputFuse2_Type(Integer32):
    """Custom type imPM1Power2OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2OutputFuse2_Type.__name__ = "Integer32"
_ImPM1Power2OutputFuse2_Object = MibScalar
imPM1Power2OutputFuse2 = _ImPM1Power2OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 51),
    _ImPM1Power2OutputFuse2_Type()
)
imPM1Power2OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputFuse2.setStatus("current")


class _ImPM1Power2OutputBreaker_Type(Integer32):
    """Custom type imPM1Power2OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2OutputBreaker_Type.__name__ = "Integer32"
_ImPM1Power2OutputBreaker_Object = MibScalar
imPM1Power2OutputBreaker = _ImPM1Power2OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 52),
    _ImPM1Power2OutputBreaker_Type()
)
imPM1Power2OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputBreaker.setStatus("current")


class _ImPM1Power2OutputBreaker1_Type(Integer32):
    """Custom type imPM1Power2OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2OutputBreaker1_Type.__name__ = "Integer32"
_ImPM1Power2OutputBreaker1_Object = MibScalar
imPM1Power2OutputBreaker1 = _ImPM1Power2OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 53),
    _ImPM1Power2OutputBreaker1_Type()
)
imPM1Power2OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputBreaker1.setStatus("current")


class _ImPM1Power2OutputBreaker2_Type(Integer32):
    """Custom type imPM1Power2OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2OutputBreaker2_Type.__name__ = "Integer32"
_ImPM1Power2OutputBreaker2_Object = MibScalar
imPM1Power2OutputBreaker2 = _ImPM1Power2OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 54),
    _ImPM1Power2OutputBreaker2_Type()
)
imPM1Power2OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputBreaker2.setStatus("current")


class _ImPM1Power2Fan_Type(Integer32):
    """Custom type imPM1Power2Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2Fan_Type.__name__ = "Integer32"
_ImPM1Power2Fan_Object = MibScalar
imPM1Power2Fan = _ImPM1Power2Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 55),
    _ImPM1Power2Fan_Type()
)
imPM1Power2Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2Fan.setStatus("current")


class _ImPM1Power2BatteryAvailable_Type(Integer32):
    """Custom type imPM1Power2BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power2BatteryAvailable_Type.__name__ = "Integer32"
_ImPM1Power2BatteryAvailable_Object = MibScalar
imPM1Power2BatteryAvailable = _ImPM1Power2BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 56),
    _ImPM1Power2BatteryAvailable_Type()
)
imPM1Power2BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2BatteryAvailable.setStatus("current")
_ImPM1Power2OutputVoltagePhase1_Type = Integer32
_ImPM1Power2OutputVoltagePhase1_Object = MibScalar
imPM1Power2OutputVoltagePhase1 = _ImPM1Power2OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 57),
    _ImPM1Power2OutputVoltagePhase1_Type()
)
imPM1Power2OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputVoltagePhase1.setUnits("0.1 V")
_ImPM1Power2OutputCurrentPhase1_Type = Integer32
_ImPM1Power2OutputCurrentPhase1_Object = MibScalar
imPM1Power2OutputCurrentPhase1 = _ImPM1Power2OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 58),
    _ImPM1Power2OutputCurrentPhase1_Type()
)
imPM1Power2OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputCurrentPhase1.setUnits("0.1 A")
_ImPM1Power2OutputPowerVAphase1_Type = Integer32
_ImPM1Power2OutputPowerVAphase1_Object = MibScalar
imPM1Power2OutputPowerVAphase1 = _ImPM1Power2OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 59),
    _ImPM1Power2OutputPowerVAphase1_Type()
)
imPM1Power2OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerVAphase1.setUnits("VA")
_ImPM1Power2OutputPowerKVAphase1_Type = Integer32
_ImPM1Power2OutputPowerKVAphase1_Object = MibScalar
imPM1Power2OutputPowerKVAphase1 = _ImPM1Power2OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 60),
    _ImPM1Power2OutputPowerKVAphase1_Type()
)
imPM1Power2OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM1Power2OutputVoltagePhase2_Type = Integer32
_ImPM1Power2OutputVoltagePhase2_Object = MibScalar
imPM1Power2OutputVoltagePhase2 = _ImPM1Power2OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 61),
    _ImPM1Power2OutputVoltagePhase2_Type()
)
imPM1Power2OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputVoltagePhase2.setUnits("0.1 V")
_ImPM1Power2OutputCurrentPhase2_Type = Integer32
_ImPM1Power2OutputCurrentPhase2_Object = MibScalar
imPM1Power2OutputCurrentPhase2 = _ImPM1Power2OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 62),
    _ImPM1Power2OutputCurrentPhase2_Type()
)
imPM1Power2OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputCurrentPhase2.setUnits("0.1 A")
_ImPM1Power2OutputPowerVAphase2_Type = Integer32
_ImPM1Power2OutputPowerVAphase2_Object = MibScalar
imPM1Power2OutputPowerVAphase2 = _ImPM1Power2OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 63),
    _ImPM1Power2OutputPowerVAphase2_Type()
)
imPM1Power2OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerVAphase2.setUnits("VA")
_ImPM1Power2OutputPowerKVAphase2_Type = Integer32
_ImPM1Power2OutputPowerKVAphase2_Object = MibScalar
imPM1Power2OutputPowerKVAphase2 = _ImPM1Power2OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 64),
    _ImPM1Power2OutputPowerKVAphase2_Type()
)
imPM1Power2OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM1Power2OutputVoltagePhase3_Type = Integer32
_ImPM1Power2OutputVoltagePhase3_Object = MibScalar
imPM1Power2OutputVoltagePhase3 = _ImPM1Power2OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 65),
    _ImPM1Power2OutputVoltagePhase3_Type()
)
imPM1Power2OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputVoltagePhase3.setUnits("0.1 V")
_ImPM1Power2OutputCurrentPhase3_Type = Integer32
_ImPM1Power2OutputCurrentPhase3_Object = MibScalar
imPM1Power2OutputCurrentPhase3 = _ImPM1Power2OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 66),
    _ImPM1Power2OutputCurrentPhase3_Type()
)
imPM1Power2OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputCurrentPhase3.setUnits("0.1 A")
_ImPM1Power2OutputPowerVAphase3_Type = Integer32
_ImPM1Power2OutputPowerVAphase3_Object = MibScalar
imPM1Power2OutputPowerVAphase3 = _ImPM1Power2OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 67),
    _ImPM1Power2OutputPowerVAphase3_Type()
)
imPM1Power2OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerVAphase3.setUnits("VA")
_ImPM1Power2OutputPowerKVAphase3_Type = Integer32
_ImPM1Power2OutputPowerKVAphase3_Object = MibScalar
imPM1Power2OutputPowerKVAphase3 = _ImPM1Power2OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 4, 68),
    _ImPM1Power2OutputPowerKVAphase3_Type()
)
imPM1Power2OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power2OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM1Power3_ObjectIdentity = ObjectIdentity
imPM1Power3 = _ImPM1Power3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5)
)


class _ImPM1Power3Manufacturer_Type(DisplayString):
    """Custom type imPM1Power3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM1Power3Manufacturer_Type.__name__ = "DisplayString"
_ImPM1Power3Manufacturer_Object = MibScalar
imPM1Power3Manufacturer = _ImPM1Power3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 1),
    _ImPM1Power3Manufacturer_Type()
)
imPM1Power3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Manufacturer.setStatus("current")


class _ImPM1Power3Type_Type(DisplayString):
    """Custom type imPM1Power3Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power3Type_Type.__name__ = "DisplayString"
_ImPM1Power3Type_Object = MibScalar
imPM1Power3Type = _ImPM1Power3Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 2),
    _ImPM1Power3Type_Type()
)
imPM1Power3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Type.setStatus("current")


class _ImPM1Power3serNumb_Type(DisplayString):
    """Custom type imPM1Power3serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power3serNumb_Type.__name__ = "DisplayString"
_ImPM1Power3serNumb_Object = MibScalar
imPM1Power3serNumb = _ImPM1Power3serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 3),
    _ImPM1Power3serNumb_Type()
)
imPM1Power3serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3serNumb.setStatus("current")


class _ImPM1Power3nextServiceDate_Type(DisplayString):
    """Custom type imPM1Power3nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1Power3nextServiceDate_Type.__name__ = "DisplayString"
_ImPM1Power3nextServiceDate_Object = MibScalar
imPM1Power3nextServiceDate = _ImPM1Power3nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 4),
    _ImPM1Power3nextServiceDate_Type()
)
imPM1Power3nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3nextServiceDate.setStatus("current")
_ImPm1Power3InputVoltage_Type = Integer32
_ImPm1Power3InputVoltage_Object = MibScalar
imPm1Power3InputVoltage = _ImPm1Power3InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 5),
    _ImPm1Power3InputVoltage_Type()
)
imPm1Power3InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputVoltage.setUnits("0.1 V")
_ImPm1Power3InputCurrent_Type = Integer32
_ImPm1Power3InputCurrent_Object = MibScalar
imPm1Power3InputCurrent = _ImPm1Power3InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 6),
    _ImPm1Power3InputCurrent_Type()
)
imPm1Power3InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputCurrent.setUnits("0.1 A")
_ImPm1Power3InputPowerVA_Type = Integer32
_ImPm1Power3InputPowerVA_Object = MibScalar
imPm1Power3InputPowerVA = _ImPm1Power3InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 7),
    _ImPm1Power3InputPowerVA_Type()
)
imPm1Power3InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerVA.setUnits("VA")
_ImPm1Power3InputPowerKVA_Type = Integer32
_ImPm1Power3InputPowerKVA_Object = MibScalar
imPm1Power3InputPowerKVA = _ImPm1Power3InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 8),
    _ImPm1Power3InputPowerKVA_Type()
)
imPm1Power3InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKVA.setUnits("0.1 kVA")
_ImPm1Power3InputPowerW_Type = Integer32
_ImPm1Power3InputPowerW_Object = MibScalar
imPm1Power3InputPowerW = _ImPm1Power3InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 9),
    _ImPm1Power3InputPowerW_Type()
)
imPm1Power3InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerW.setUnits("W")
_ImPm1Power3InputPowerKW_Type = Integer32
_ImPm1Power3InputPowerKW_Object = MibScalar
imPm1Power3InputPowerKW = _ImPm1Power3InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 10),
    _ImPm1Power3InputPowerKW_Type()
)
imPm1Power3InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKW.setUnits("0.1 kW")
_ImPm1Power3InputVoltagePhase1_Type = Integer32
_ImPm1Power3InputVoltagePhase1_Object = MibScalar
imPm1Power3InputVoltagePhase1 = _ImPm1Power3InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 11),
    _ImPm1Power3InputVoltagePhase1_Type()
)
imPm1Power3InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputVoltagePhase1.setUnits("0.1 V")
_ImPm1Power3InputCurrentPhase1_Type = Integer32
_ImPm1Power3InputCurrentPhase1_Object = MibScalar
imPm1Power3InputCurrentPhase1 = _ImPm1Power3InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 12),
    _ImPm1Power3InputCurrentPhase1_Type()
)
imPm1Power3InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputCurrentPhase1.setUnits("0.1 A")
_ImPm1Power3InputPowerVAphase1_Type = Integer32
_ImPm1Power3InputPowerVAphase1_Object = MibScalar
imPm1Power3InputPowerVAphase1 = _ImPm1Power3InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 13),
    _ImPm1Power3InputPowerVAphase1_Type()
)
imPm1Power3InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerVAphase1.setUnits("VA")
_ImPm1Power3InputPowerKVAphase1_Type = Integer32
_ImPm1Power3InputPowerKVAphase1_Object = MibScalar
imPm1Power3InputPowerKVAphase1 = _ImPm1Power3InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 14),
    _ImPm1Power3InputPowerKVAphase1_Type()
)
imPm1Power3InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPm1Power3InputVoltagePhase2_Type = Integer32
_ImPm1Power3InputVoltagePhase2_Object = MibScalar
imPm1Power3InputVoltagePhase2 = _ImPm1Power3InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 15),
    _ImPm1Power3InputVoltagePhase2_Type()
)
imPm1Power3InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputVoltagePhase2.setUnits("0.1 V")
_ImPm1Power3InputCurrentPhase2_Type = Integer32
_ImPm1Power3InputCurrentPhase2_Object = MibScalar
imPm1Power3InputCurrentPhase2 = _ImPm1Power3InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 16),
    _ImPm1Power3InputCurrentPhase2_Type()
)
imPm1Power3InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputCurrentPhase2.setUnits("0.1 A")
_ImPm1Power3InputPowerVAphase2_Type = Integer32
_ImPm1Power3InputPowerVAphase2_Object = MibScalar
imPm1Power3InputPowerVAphase2 = _ImPm1Power3InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 17),
    _ImPm1Power3InputPowerVAphase2_Type()
)
imPm1Power3InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerVAphase2.setUnits("VA")
_ImPm1Power3InputPowerKVAphase2_Type = Integer32
_ImPm1Power3InputPowerKVAphase2_Object = MibScalar
imPm1Power3InputPowerKVAphase2 = _ImPm1Power3InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 18),
    _ImPm1Power3InputPowerKVAphase2_Type()
)
imPm1Power3InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPm1Power3InputVoltagePhase3_Type = Integer32
_ImPm1Power3InputVoltagePhase3_Object = MibScalar
imPm1Power3InputVoltagePhase3 = _ImPm1Power3InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 19),
    _ImPm1Power3InputVoltagePhase3_Type()
)
imPm1Power3InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputVoltagePhase3.setUnits("0.1 V")
_ImPm1Power3InputCurrentPhase3_Type = Integer32
_ImPm1Power3InputCurrentPhase3_Object = MibScalar
imPm1Power3InputCurrentPhase3 = _ImPm1Power3InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 20),
    _ImPm1Power3InputCurrentPhase3_Type()
)
imPm1Power3InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputCurrentPhase3.setUnits("0.1 A")
_ImPm1Power3InputPowerVAphase3_Type = Integer32
_ImPm1Power3InputPowerVAphase3_Object = MibScalar
imPm1Power3InputPowerVAphase3 = _ImPm1Power3InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 21),
    _ImPm1Power3InputPowerVAphase3_Type()
)
imPm1Power3InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerVAphase3.setUnits("VA")
_ImPm1Power3InputPowerKVAphase3_Type = Integer32
_ImPm1Power3InputPowerKVAphase3_Object = MibScalar
imPm1Power3InputPowerKVAphase3 = _ImPm1Power3InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 22),
    _ImPm1Power3InputPowerKVAphase3_Type()
)
imPm1Power3InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPm1Power3OutputVoltage_Type = Integer32
_ImPm1Power3OutputVoltage_Object = MibScalar
imPm1Power3OutputVoltage = _ImPm1Power3OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 23),
    _ImPm1Power3OutputVoltage_Type()
)
imPm1Power3OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3OutputVoltage.setUnits("0.1 V")
_ImPm1Power3OutputCurrent_Type = Integer32
_ImPm1Power3OutputCurrent_Object = MibScalar
imPm1Power3OutputCurrent = _ImPm1Power3OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 24),
    _ImPm1Power3OutputCurrent_Type()
)
imPm1Power3OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3OutputCurrent.setUnits("0.1 A")
_ImPm1Power3OutputPowerVA_Type = Integer32
_ImPm1Power3OutputPowerVA_Object = MibScalar
imPm1Power3OutputPowerVA = _ImPm1Power3OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 25),
    _ImPm1Power3OutputPowerVA_Type()
)
imPm1Power3OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3OutputPowerVA.setUnits("VA")
_ImPm1Power3OutputPowerKVA_Type = Integer32
_ImPm1Power3OutputPowerKVA_Object = MibScalar
imPm1Power3OutputPowerKVA = _ImPm1Power3OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 26),
    _ImPm1Power3OutputPowerKVA_Type()
)
imPm1Power3OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3OutputPowerKVA.setUnits("0.1 kVA")
_ImPm1Power3OutputPowerW_Type = Integer32
_ImPm1Power3OutputPowerW_Object = MibScalar
imPm1Power3OutputPowerW = _ImPm1Power3OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 27),
    _ImPm1Power3OutputPowerW_Type()
)
imPm1Power3OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3OutputPowerW.setUnits("W")
_ImPm1Power3OutputPowerKW_Type = Integer32
_ImPm1Power3OutputPowerKW_Object = MibScalar
imPm1Power3OutputPowerKW = _ImPm1Power3OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 28),
    _ImPm1Power3OutputPowerKW_Type()
)
imPm1Power3OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3OutputPowerKW.setUnits("0.1 kW")
_ImPm1Power3OutputLoad_Type = Integer32
_ImPm1Power3OutputLoad_Object = MibScalar
imPm1Power3OutputLoad = _ImPm1Power3OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 29),
    _ImPm1Power3OutputLoad_Type()
)
imPm1Power3OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3OutputLoad.setUnits("%")
_ImPm1Power3OutputFrequency_Type = NonNegativeInteger
_ImPm1Power3OutputFrequency_Object = MibScalar
imPm1Power3OutputFrequency = _ImPm1Power3OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 30),
    _ImPm1Power3OutputFrequency_Type()
)
imPm1Power3OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3OutputFrequency.setUnits("0.1 Hz")
_ImPm1Power3Temperature_Type = Integer32
_ImPm1Power3Temperature_Object = MibScalar
imPm1Power3Temperature = _ImPm1Power3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 31),
    _ImPm1Power3Temperature_Type()
)
imPm1Power3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Power3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Power3Temperature.setUnits("degrees Centigrade")


class _ImPM1Power3Running1_Type(Integer32):
    """Custom type imPM1Power3Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Running1_Type.__name__ = "Integer32"
_ImPM1Power3Running1_Object = MibScalar
imPM1Power3Running1 = _ImPM1Power3Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 32),
    _ImPM1Power3Running1_Type()
)
imPM1Power3Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Running1.setStatus("current")


class _ImPM1Power3Running2_Type(Integer32):
    """Custom type imPM1Power3Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Running2_Type.__name__ = "Integer32"
_ImPM1Power3Running2_Object = MibScalar
imPM1Power3Running2 = _ImPM1Power3Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 33),
    _ImPM1Power3Running2_Type()
)
imPM1Power3Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Running2.setStatus("current")


class _ImPM1Power3Running3_Type(Integer32):
    """Custom type imPM1Power3Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Running3_Type.__name__ = "Integer32"
_ImPM1Power3Running3_Object = MibScalar
imPM1Power3Running3 = _ImPM1Power3Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 34),
    _ImPM1Power3Running3_Type()
)
imPM1Power3Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Running3.setStatus("current")


class _ImPM1Power3Running4_Type(Integer32):
    """Custom type imPM1Power3Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Running4_Type.__name__ = "Integer32"
_ImPM1Power3Running4_Object = MibScalar
imPM1Power3Running4 = _ImPM1Power3Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 35),
    _ImPM1Power3Running4_Type()
)
imPM1Power3Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Running4.setStatus("current")


class _ImPM1Power3Running5_Type(Integer32):
    """Custom type imPM1Power3Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Running5_Type.__name__ = "Integer32"
_ImPM1Power3Running5_Object = MibScalar
imPM1Power3Running5 = _ImPM1Power3Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 36),
    _ImPM1Power3Running5_Type()
)
imPM1Power3Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Running5.setStatus("current")


class _ImPM1Power3Running6_Type(Integer32):
    """Custom type imPM1Power3Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Running6_Type.__name__ = "Integer32"
_ImPM1Power3Running6_Object = MibScalar
imPM1Power3Running6 = _ImPM1Power3Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 37),
    _ImPM1Power3Running6_Type()
)
imPM1Power3Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Running6.setStatus("current")


class _ImPM1Power3Running7_Type(Integer32):
    """Custom type imPM1Power3Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Running7_Type.__name__ = "Integer32"
_ImPM1Power3Running7_Object = MibScalar
imPM1Power3Running7 = _ImPM1Power3Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 38),
    _ImPM1Power3Running7_Type()
)
imPM1Power3Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Running7.setStatus("current")


class _ImPM1Power3Running8_Type(Integer32):
    """Custom type imPM1Power3Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Running8_Type.__name__ = "Integer32"
_ImPM1Power3Running8_Object = MibScalar
imPM1Power3Running8 = _ImPM1Power3Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 39),
    _ImPM1Power3Running8_Type()
)
imPM1Power3Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Running8.setStatus("current")


class _ImPM1Power3InputFuse_Type(Integer32):
    """Custom type imPM1Power3InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputFuse_Type.__name__ = "Integer32"
_ImPM1Power3InputFuse_Object = MibScalar
imPM1Power3InputFuse = _ImPM1Power3InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 40),
    _ImPM1Power3InputFuse_Type()
)
imPM1Power3InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputFuse.setStatus("current")


class _ImPM1Power3InputFuse1_Type(Integer32):
    """Custom type imPM1Power3InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputFuse1_Type.__name__ = "Integer32"
_ImPM1Power3InputFuse1_Object = MibScalar
imPM1Power3InputFuse1 = _ImPM1Power3InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 41),
    _ImPM1Power3InputFuse1_Type()
)
imPM1Power3InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputFuse1.setStatus("current")


class _ImPM1Power3InputFuse2_Type(Integer32):
    """Custom type imPM1Power3InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputFuse2_Type.__name__ = "Integer32"
_ImPM1Power3InputFuse2_Object = MibScalar
imPM1Power3InputFuse2 = _ImPM1Power3InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 42),
    _ImPM1Power3InputFuse2_Type()
)
imPM1Power3InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputFuse2.setStatus("current")


class _ImPM1Power3InputFuse3_Type(Integer32):
    """Custom type imPM1Power3InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputFuse3_Type.__name__ = "Integer32"
_ImPM1Power3InputFuse3_Object = MibScalar
imPM1Power3InputFuse3 = _ImPM1Power3InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 43),
    _ImPM1Power3InputFuse3_Type()
)
imPM1Power3InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputFuse3.setStatus("current")


class _ImPM1Power3InputBreaker_Type(Integer32):
    """Custom type imPM1Power3InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputBreaker_Type.__name__ = "Integer32"
_ImPM1Power3InputBreaker_Object = MibScalar
imPM1Power3InputBreaker = _ImPM1Power3InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 44),
    _ImPM1Power3InputBreaker_Type()
)
imPM1Power3InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputBreaker.setStatus("current")


class _ImPM1Power3InputBreaker1_Type(Integer32):
    """Custom type imPM1Power3InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputBreaker1_Type.__name__ = "Integer32"
_ImPM1Power3InputBreaker1_Object = MibScalar
imPM1Power3InputBreaker1 = _ImPM1Power3InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 45),
    _ImPM1Power3InputBreaker1_Type()
)
imPM1Power3InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputBreaker1.setStatus("current")


class _ImPM1Power3InputBreaker2_Type(Integer32):
    """Custom type imPM1Power3InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputBreaker2_Type.__name__ = "Integer32"
_ImPM1Power3InputBreaker2_Object = MibScalar
imPM1Power3InputBreaker2 = _ImPM1Power3InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 46),
    _ImPM1Power3InputBreaker2_Type()
)
imPM1Power3InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputBreaker2.setStatus("current")


class _ImPM1Power3InputBreaker3_Type(Integer32):
    """Custom type imPM1Power3InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputBreaker3_Type.__name__ = "Integer32"
_ImPM1Power3InputBreaker3_Object = MibScalar
imPM1Power3InputBreaker3 = _ImPM1Power3InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 47),
    _ImPM1Power3InputBreaker3_Type()
)
imPM1Power3InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputBreaker3.setStatus("current")


class _ImPM1Power3InputSurgeArrester_Type(Integer32):
    """Custom type imPM1Power3InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM1Power3InputSurgeArrester_Object = MibScalar
imPM1Power3InputSurgeArrester = _ImPM1Power3InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 48),
    _ImPM1Power3InputSurgeArrester_Type()
)
imPM1Power3InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3InputSurgeArrester.setStatus("current")


class _ImPM1Power3OutputFuse_Type(Integer32):
    """Custom type imPM1Power3OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3OutputFuse_Type.__name__ = "Integer32"
_ImPM1Power3OutputFuse_Object = MibScalar
imPM1Power3OutputFuse = _ImPM1Power3OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 49),
    _ImPM1Power3OutputFuse_Type()
)
imPM1Power3OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputFuse.setStatus("current")


class _ImPM1Power3OutputFuse1_Type(Integer32):
    """Custom type imPM1Power3OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3OutputFuse1_Type.__name__ = "Integer32"
_ImPM1Power3OutputFuse1_Object = MibScalar
imPM1Power3OutputFuse1 = _ImPM1Power3OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 50),
    _ImPM1Power3OutputFuse1_Type()
)
imPM1Power3OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputFuse1.setStatus("current")


class _ImPM1Power3OutputFuse2_Type(Integer32):
    """Custom type imPM1Power3OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3OutputFuse2_Type.__name__ = "Integer32"
_ImPM1Power3OutputFuse2_Object = MibScalar
imPM1Power3OutputFuse2 = _ImPM1Power3OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 51),
    _ImPM1Power3OutputFuse2_Type()
)
imPM1Power3OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputFuse2.setStatus("current")


class _ImPM1Power3OutputBreaker_Type(Integer32):
    """Custom type imPM1Power3OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3OutputBreaker_Type.__name__ = "Integer32"
_ImPM1Power3OutputBreaker_Object = MibScalar
imPM1Power3OutputBreaker = _ImPM1Power3OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 52),
    _ImPM1Power3OutputBreaker_Type()
)
imPM1Power3OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputBreaker.setStatus("current")


class _ImPM1Power3OutputBreaker1_Type(Integer32):
    """Custom type imPM1Power3OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3OutputBreaker1_Type.__name__ = "Integer32"
_ImPM1Power3OutputBreaker1_Object = MibScalar
imPM1Power3OutputBreaker1 = _ImPM1Power3OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 53),
    _ImPM1Power3OutputBreaker1_Type()
)
imPM1Power3OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputBreaker1.setStatus("current")


class _ImPM1Power3OutputBreaker2_Type(Integer32):
    """Custom type imPM1Power3OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3OutputBreaker2_Type.__name__ = "Integer32"
_ImPM1Power3OutputBreaker2_Object = MibScalar
imPM1Power3OutputBreaker2 = _ImPM1Power3OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 54),
    _ImPM1Power3OutputBreaker2_Type()
)
imPM1Power3OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputBreaker2.setStatus("current")


class _ImPM1Power3Fan_Type(Integer32):
    """Custom type imPM1Power3Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3Fan_Type.__name__ = "Integer32"
_ImPM1Power3Fan_Object = MibScalar
imPM1Power3Fan = _ImPM1Power3Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 55),
    _ImPM1Power3Fan_Type()
)
imPM1Power3Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3Fan.setStatus("current")


class _ImPM1Power3BatteryAvailable_Type(Integer32):
    """Custom type imPM1Power3BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1Power3BatteryAvailable_Type.__name__ = "Integer32"
_ImPM1Power3BatteryAvailable_Object = MibScalar
imPM1Power3BatteryAvailable = _ImPM1Power3BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 56),
    _ImPM1Power3BatteryAvailable_Type()
)
imPM1Power3BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3BatteryAvailable.setStatus("current")
_ImPM1Power3OutputVoltagePhase1_Type = Integer32
_ImPM1Power3OutputVoltagePhase1_Object = MibScalar
imPM1Power3OutputVoltagePhase1 = _ImPM1Power3OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 57),
    _ImPM1Power3OutputVoltagePhase1_Type()
)
imPM1Power3OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputVoltagePhase1.setUnits("0.1 V")
_ImPM1Power3OutputCurrentPhase1_Type = Integer32
_ImPM1Power3OutputCurrentPhase1_Object = MibScalar
imPM1Power3OutputCurrentPhase1 = _ImPM1Power3OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 58),
    _ImPM1Power3OutputCurrentPhase1_Type()
)
imPM1Power3OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputCurrentPhase1.setUnits("0.1 A")
_ImPM1Power3OutputPowerVAphase1_Type = Integer32
_ImPM1Power3OutputPowerVAphase1_Object = MibScalar
imPM1Power3OutputPowerVAphase1 = _ImPM1Power3OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 59),
    _ImPM1Power3OutputPowerVAphase1_Type()
)
imPM1Power3OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerVAphase1.setUnits("VA")
_ImPM1Power3OutputPowerKVAphase1_Type = Integer32
_ImPM1Power3OutputPowerKVAphase1_Object = MibScalar
imPM1Power3OutputPowerKVAphase1 = _ImPM1Power3OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 60),
    _ImPM1Power3OutputPowerKVAphase1_Type()
)
imPM1Power3OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM1Power3OutputVoltagePhase2_Type = Integer32
_ImPM1Power3OutputVoltagePhase2_Object = MibScalar
imPM1Power3OutputVoltagePhase2 = _ImPM1Power3OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 61),
    _ImPM1Power3OutputVoltagePhase2_Type()
)
imPM1Power3OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputVoltagePhase2.setUnits("0.1 V")
_ImPM1Power3OutputCurrentPhase2_Type = Integer32
_ImPM1Power3OutputCurrentPhase2_Object = MibScalar
imPM1Power3OutputCurrentPhase2 = _ImPM1Power3OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 62),
    _ImPM1Power3OutputCurrentPhase2_Type()
)
imPM1Power3OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputCurrentPhase2.setUnits("0.1 A")
_ImPM1Power3OutputPowerVAphase2_Type = Integer32
_ImPM1Power3OutputPowerVAphase2_Object = MibScalar
imPM1Power3OutputPowerVAphase2 = _ImPM1Power3OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 63),
    _ImPM1Power3OutputPowerVAphase2_Type()
)
imPM1Power3OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerVAphase2.setUnits("VA")
_ImPM1Power3OutputPowerKVAphase2_Type = Integer32
_ImPM1Power3OutputPowerKVAphase2_Object = MibScalar
imPM1Power3OutputPowerKVAphase2 = _ImPM1Power3OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 64),
    _ImPM1Power3OutputPowerKVAphase2_Type()
)
imPM1Power3OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM1Power3OutputVoltagePhase3_Type = Integer32
_ImPM1Power3OutputVoltagePhase3_Object = MibScalar
imPM1Power3OutputVoltagePhase3 = _ImPM1Power3OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 65),
    _ImPM1Power3OutputVoltagePhase3_Type()
)
imPM1Power3OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputVoltagePhase3.setUnits("0.1 V")
_ImPM1Power3OutputCurrentPhase3_Type = Integer32
_ImPM1Power3OutputCurrentPhase3_Object = MibScalar
imPM1Power3OutputCurrentPhase3 = _ImPM1Power3OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 66),
    _ImPM1Power3OutputCurrentPhase3_Type()
)
imPM1Power3OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputCurrentPhase3.setUnits("0.1 A")
_ImPM1Power3OutputPowerVAphase3_Type = Integer32
_ImPM1Power3OutputPowerVAphase3_Object = MibScalar
imPM1Power3OutputPowerVAphase3 = _ImPM1Power3OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 67),
    _ImPM1Power3OutputPowerVAphase3_Type()
)
imPM1Power3OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerVAphase3.setUnits("VA")
_ImPM1Power3OutputPowerKVAphase3_Type = Integer32
_ImPM1Power3OutputPowerKVAphase3_Object = MibScalar
imPM1Power3OutputPowerKVAphase3 = _ImPM1Power3OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 5, 68),
    _ImPM1Power3OutputPowerKVAphase3_Type()
)
imPM1Power3OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM1Power3OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM1Battery_ObjectIdentity = ObjectIdentity
imPM1Battery = _ImPM1Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 6)
)
_ImPm1BatteryNominalCapacity_Type = NonNegativeInteger
_ImPm1BatteryNominalCapacity_Object = MibScalar
imPm1BatteryNominalCapacity = _ImPm1BatteryNominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 6, 1),
    _ImPm1BatteryNominalCapacity_Type()
)
imPm1BatteryNominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatteryNominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatteryNominalCapacity.setUnits("Ah")
_ImPm1BatteryVoltage_Type = Integer32
_ImPm1BatteryVoltage_Object = MibScalar
imPm1BatteryVoltage = _ImPm1BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 6, 2),
    _ImPm1BatteryVoltage_Type()
)
imPm1BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatteryVoltage.setUnits("0.1 V")
_ImPm1BatteryCurrent_Type = Integer32
_ImPm1BatteryCurrent_Object = MibScalar
imPm1BatteryCurrent = _ImPm1BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 6, 3),
    _ImPm1BatteryCurrent_Type()
)
imPm1BatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatteryCurrent.setUnits("0.1 A")
_ImPm1BatteryChargeState_Type = NonNegativeInteger
_ImPm1BatteryChargeState_Object = MibScalar
imPm1BatteryChargeState = _ImPm1BatteryChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 6, 4),
    _ImPm1BatteryChargeState_Type()
)
imPm1BatteryChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatteryChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatteryChargeState.setUnits("%")
_ImPm1BatteryAutonomyTime_Type = NonNegativeInteger
_ImPm1BatteryAutonomyTime_Object = MibScalar
imPm1BatteryAutonomyTime = _ImPm1BatteryAutonomyTime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 6, 5),
    _ImPm1BatteryAutonomyTime_Type()
)
imPm1BatteryAutonomyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatteryAutonomyTime.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatteryAutonomyTime.setUnits("min")
_ImPm1BatteryTimeOnBattery_Type = NonNegativeInteger
_ImPm1BatteryTimeOnBattery_Object = MibScalar
imPm1BatteryTimeOnBattery = _ImPm1BatteryTimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 6, 6),
    _ImPm1BatteryTimeOnBattery_Type()
)
imPm1BatteryTimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatteryTimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatteryTimeOnBattery.setUnits("min")
_ImPM1BatLeg1_ObjectIdentity = ObjectIdentity
imPM1BatLeg1 = _ImPM1BatLeg1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7)
)


class _ImPM1BatLeg1Manufacturer_Type(DisplayString):
    """Custom type imPM1BatLeg1Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM1BatLeg1Manufacturer_Type.__name__ = "DisplayString"
_ImPM1BatLeg1Manufacturer_Object = MibScalar
imPM1BatLeg1Manufacturer = _ImPM1BatLeg1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 1),
    _ImPM1BatLeg1Manufacturer_Type()
)
imPM1BatLeg1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg1Manufacturer.setStatus("current")


class _ImPM1BatLeg1Type_Type(DisplayString):
    """Custom type imPM1BatLeg1Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg1Type_Type.__name__ = "DisplayString"
_ImPM1BatLeg1Type_Object = MibScalar
imPM1BatLeg1Type = _ImPM1BatLeg1Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 2),
    _ImPM1BatLeg1Type_Type()
)
imPM1BatLeg1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg1Type.setStatus("current")


class _ImPM1BatLeg1serNumb_Type(DisplayString):
    """Custom type imPM1BatLeg1serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg1serNumb_Type.__name__ = "DisplayString"
_ImPM1BatLeg1serNumb_Object = MibScalar
imPM1BatLeg1serNumb = _ImPM1BatLeg1serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 3),
    _ImPM1BatLeg1serNumb_Type()
)
imPM1BatLeg1serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg1serNumb.setStatus("current")


class _ImPM1BatLeg1nextServiceDate_Type(DisplayString):
    """Custom type imPM1BatLeg1nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg1nextServiceDate_Type.__name__ = "DisplayString"
_ImPM1BatLeg1nextServiceDate_Object = MibScalar
imPM1BatLeg1nextServiceDate = _ImPM1BatLeg1nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 4),
    _ImPM1BatLeg1nextServiceDate_Type()
)
imPM1BatLeg1nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg1nextServiceDate.setStatus("current")


class _ImPM1BatLeg1InstallationDate_Type(DisplayString):
    """Custom type imPM1BatLeg1InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg1InstallationDate_Type.__name__ = "DisplayString"
_ImPM1BatLeg1InstallationDate_Object = MibScalar
imPM1BatLeg1InstallationDate = _ImPM1BatLeg1InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 5),
    _ImPM1BatLeg1InstallationDate_Type()
)
imPM1BatLeg1InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg1InstallationDate.setStatus("current")
_ImPm1BatLeg1NominalVoltage_Type = Integer32
_ImPm1BatLeg1NominalVoltage_Object = MibScalar
imPm1BatLeg1NominalVoltage = _ImPm1BatLeg1NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 6),
    _ImPm1BatLeg1NominalVoltage_Type()
)
imPm1BatLeg1NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1NominalVoltage.setUnits("0.1 V")
_ImPm1BatLeg1NominalCapacity_Type = NonNegativeInteger
_ImPm1BatLeg1NominalCapacity_Object = MibScalar
imPm1BatLeg1NominalCapacity = _ImPm1BatLeg1NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 7),
    _ImPm1BatLeg1NominalCapacity_Type()
)
imPm1BatLeg1NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1NominalCapacity.setUnits("Ah")
_ImPm1BatLeg1Lifetime_Type = NonNegativeInteger
_ImPm1BatLeg1Lifetime_Object = MibScalar
imPm1BatLeg1Lifetime = _ImPm1BatLeg1Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 8),
    _ImPm1BatLeg1Lifetime_Type()
)
imPm1BatLeg1Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1Lifetime.setUnits("years")
_ImPm1BatLeg1Voltage_Type = Integer32
_ImPm1BatLeg1Voltage_Object = MibScalar
imPm1BatLeg1Voltage = _ImPm1BatLeg1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 9),
    _ImPm1BatLeg1Voltage_Type()
)
imPm1BatLeg1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1Voltage.setUnits("0.1 V")
_ImPm1BatLeg1Current_Type = Integer32
_ImPm1BatLeg1Current_Object = MibScalar
imPm1BatLeg1Current = _ImPm1BatLeg1Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 10),
    _ImPm1BatLeg1Current_Type()
)
imPm1BatLeg1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1Current.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1Current.setUnits("0.1 A")
_ImPm1BatLeg1Temperature_Type = Integer32
_ImPm1BatLeg1Temperature_Object = MibScalar
imPm1BatLeg1Temperature = _ImPm1BatLeg1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 11),
    _ImPm1BatLeg1Temperature_Type()
)
imPm1BatLeg1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1Temperature.setUnits("degrees Centigrade")
_ImPm1BatLeg1ChargeState_Type = NonNegativeInteger
_ImPm1BatLeg1ChargeState_Object = MibScalar
imPm1BatLeg1ChargeState = _ImPm1BatLeg1ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 12),
    _ImPm1BatLeg1ChargeState_Type()
)
imPm1BatLeg1ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1ChargeState.setUnits("%")
_ImPm1BatLeg1RestCapacity_Type = NonNegativeInteger
_ImPm1BatLeg1RestCapacity_Object = MibScalar
imPm1BatLeg1RestCapacity = _ImPm1BatLeg1RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 13),
    _ImPm1BatLeg1RestCapacity_Type()
)
imPm1BatLeg1RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1RestCapacity.setUnits("Ah")
_ImPm1BatLeg1Autonomytime_Type = NonNegativeInteger
_ImPm1BatLeg1Autonomytime_Object = MibScalar
imPm1BatLeg1Autonomytime = _ImPm1BatLeg1Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 14),
    _ImPm1BatLeg1Autonomytime_Type()
)
imPm1BatLeg1Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1Autonomytime.setUnits("min")
_ImPm1BatLeg1TimeOnBattery_Type = NonNegativeInteger
_ImPm1BatLeg1TimeOnBattery_Object = MibScalar
imPm1BatLeg1TimeOnBattery = _ImPm1BatLeg1TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 15),
    _ImPm1BatLeg1TimeOnBattery_Type()
)
imPm1BatLeg1TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg1TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg1TimeOnBattery.setUnits("min")


class _ImPM1BatLeg1Fuse_Type(Integer32):
    """Custom type imPM1BatLeg1Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg1Fuse_Type.__name__ = "Integer32"
_ImPM1BatLeg1Fuse_Object = MibScalar
imPM1BatLeg1Fuse = _ImPM1BatLeg1Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 16),
    _ImPM1BatLeg1Fuse_Type()
)
imPM1BatLeg1Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg1Fuse.setStatus("current")


class _ImPM1BatLeg1Breaker_Type(Integer32):
    """Custom type imPM1BatLeg1Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg1Breaker_Type.__name__ = "Integer32"
_ImPM1BatLeg1Breaker_Object = MibScalar
imPM1BatLeg1Breaker = _ImPM1BatLeg1Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 17),
    _ImPM1BatLeg1Breaker_Type()
)
imPM1BatLeg1Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg1Breaker.setStatus("current")


class _ImPM1BatLeg1LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM1BatLeg1LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg1LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM1BatLeg1LowVoltageDisconnect_Object = MibScalar
imPM1BatLeg1LowVoltageDisconnect = _ImPM1BatLeg1LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 7, 18),
    _ImPM1BatLeg1LowVoltageDisconnect_Type()
)
imPM1BatLeg1LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg1LowVoltageDisconnect.setStatus("current")
_ImPM1BatLeg2_ObjectIdentity = ObjectIdentity
imPM1BatLeg2 = _ImPM1BatLeg2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8)
)


class _ImPM1BatLeg2Manufacturer_Type(DisplayString):
    """Custom type imPM1BatLeg2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM1BatLeg2Manufacturer_Type.__name__ = "DisplayString"
_ImPM1BatLeg2Manufacturer_Object = MibScalar
imPM1BatLeg2Manufacturer = _ImPM1BatLeg2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 1),
    _ImPM1BatLeg2Manufacturer_Type()
)
imPM1BatLeg2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg2Manufacturer.setStatus("current")


class _ImPM1BatLeg2Type_Type(DisplayString):
    """Custom type imPM1BatLeg2Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg2Type_Type.__name__ = "DisplayString"
_ImPM1BatLeg2Type_Object = MibScalar
imPM1BatLeg2Type = _ImPM1BatLeg2Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 2),
    _ImPM1BatLeg2Type_Type()
)
imPM1BatLeg2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg2Type.setStatus("current")


class _ImPM1BatLeg2serNumb_Type(DisplayString):
    """Custom type imPM1BatLeg2serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg2serNumb_Type.__name__ = "DisplayString"
_ImPM1BatLeg2serNumb_Object = MibScalar
imPM1BatLeg2serNumb = _ImPM1BatLeg2serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 3),
    _ImPM1BatLeg2serNumb_Type()
)
imPM1BatLeg2serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg2serNumb.setStatus("current")


class _ImPM1BatLeg2nextServiceDate_Type(DisplayString):
    """Custom type imPM1BatLeg2nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg2nextServiceDate_Type.__name__ = "DisplayString"
_ImPM1BatLeg2nextServiceDate_Object = MibScalar
imPM1BatLeg2nextServiceDate = _ImPM1BatLeg2nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 4),
    _ImPM1BatLeg2nextServiceDate_Type()
)
imPM1BatLeg2nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg2nextServiceDate.setStatus("current")


class _ImPM1BatLeg2InstallationDate_Type(DisplayString):
    """Custom type imPM1BatLeg2InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg2InstallationDate_Type.__name__ = "DisplayString"
_ImPM1BatLeg2InstallationDate_Object = MibScalar
imPM1BatLeg2InstallationDate = _ImPM1BatLeg2InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 5),
    _ImPM1BatLeg2InstallationDate_Type()
)
imPM1BatLeg2InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg2InstallationDate.setStatus("current")
_ImPm1BatLeg2NominalVoltage_Type = Integer32
_ImPm1BatLeg2NominalVoltage_Object = MibScalar
imPm1BatLeg2NominalVoltage = _ImPm1BatLeg2NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 6),
    _ImPm1BatLeg2NominalVoltage_Type()
)
imPm1BatLeg2NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2NominalVoltage.setUnits("0.1 V")
_ImPm1BatLeg2NominalCapacity_Type = NonNegativeInteger
_ImPm1BatLeg2NominalCapacity_Object = MibScalar
imPm1BatLeg2NominalCapacity = _ImPm1BatLeg2NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 7),
    _ImPm1BatLeg2NominalCapacity_Type()
)
imPm1BatLeg2NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2NominalCapacity.setUnits("Ah")
_ImPm1BatLeg2Lifetime_Type = NonNegativeInteger
_ImPm1BatLeg2Lifetime_Object = MibScalar
imPm1BatLeg2Lifetime = _ImPm1BatLeg2Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 8),
    _ImPm1BatLeg2Lifetime_Type()
)
imPm1BatLeg2Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2Lifetime.setUnits("years")
_ImPm1BatLeg2Voltage_Type = Integer32
_ImPm1BatLeg2Voltage_Object = MibScalar
imPm1BatLeg2Voltage = _ImPm1BatLeg2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 9),
    _ImPm1BatLeg2Voltage_Type()
)
imPm1BatLeg2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2Voltage.setUnits("0.1 V")
_ImPm1BatLeg2Current_Type = Integer32
_ImPm1BatLeg2Current_Object = MibScalar
imPm1BatLeg2Current = _ImPm1BatLeg2Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 10),
    _ImPm1BatLeg2Current_Type()
)
imPm1BatLeg2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2Current.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2Current.setUnits("0.1 A")
_ImPm1BatLeg2Temperature_Type = Integer32
_ImPm1BatLeg2Temperature_Object = MibScalar
imPm1BatLeg2Temperature = _ImPm1BatLeg2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 11),
    _ImPm1BatLeg2Temperature_Type()
)
imPm1BatLeg2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2Temperature.setUnits("degrees Centigrade")
_ImPm1BatLeg2ChargeState_Type = NonNegativeInteger
_ImPm1BatLeg2ChargeState_Object = MibScalar
imPm1BatLeg2ChargeState = _ImPm1BatLeg2ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 12),
    _ImPm1BatLeg2ChargeState_Type()
)
imPm1BatLeg2ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2ChargeState.setUnits("%")
_ImPm1BatLeg2RestCapacity_Type = NonNegativeInteger
_ImPm1BatLeg2RestCapacity_Object = MibScalar
imPm1BatLeg2RestCapacity = _ImPm1BatLeg2RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 13),
    _ImPm1BatLeg2RestCapacity_Type()
)
imPm1BatLeg2RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2RestCapacity.setUnits("Ah")
_ImPm1BatLeg2Autonomytime_Type = NonNegativeInteger
_ImPm1BatLeg2Autonomytime_Object = MibScalar
imPm1BatLeg2Autonomytime = _ImPm1BatLeg2Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 14),
    _ImPm1BatLeg2Autonomytime_Type()
)
imPm1BatLeg2Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2Autonomytime.setUnits("min")
_ImPm1BatLeg2TimeOnBattery_Type = NonNegativeInteger
_ImPm1BatLeg2TimeOnBattery_Object = MibScalar
imPm1BatLeg2TimeOnBattery = _ImPm1BatLeg2TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 15),
    _ImPm1BatLeg2TimeOnBattery_Type()
)
imPm1BatLeg2TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg2TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg2TimeOnBattery.setUnits("min")


class _ImPM1BatLeg2Fuse_Type(Integer32):
    """Custom type imPM1BatLeg2Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg2Fuse_Type.__name__ = "Integer32"
_ImPM1BatLeg2Fuse_Object = MibScalar
imPM1BatLeg2Fuse = _ImPM1BatLeg2Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 16),
    _ImPM1BatLeg2Fuse_Type()
)
imPM1BatLeg2Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg2Fuse.setStatus("current")


class _ImPM1BatLeg2Breaker_Type(Integer32):
    """Custom type imPM1BatLeg2Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg2Breaker_Type.__name__ = "Integer32"
_ImPM1BatLeg2Breaker_Object = MibScalar
imPM1BatLeg2Breaker = _ImPM1BatLeg2Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 17),
    _ImPM1BatLeg2Breaker_Type()
)
imPM1BatLeg2Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg2Breaker.setStatus("current")


class _ImPM1BatLeg2LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM1BatLeg2LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg2LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM1BatLeg2LowVoltageDisconnect_Object = MibScalar
imPM1BatLeg2LowVoltageDisconnect = _ImPM1BatLeg2LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 8, 18),
    _ImPM1BatLeg2LowVoltageDisconnect_Type()
)
imPM1BatLeg2LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg2LowVoltageDisconnect.setStatus("current")
_ImPM1BatLeg3_ObjectIdentity = ObjectIdentity
imPM1BatLeg3 = _ImPM1BatLeg3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9)
)


class _ImPM1BatLeg3Manufacturer_Type(DisplayString):
    """Custom type imPM1BatLeg3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM1BatLeg3Manufacturer_Type.__name__ = "DisplayString"
_ImPM1BatLeg3Manufacturer_Object = MibScalar
imPM1BatLeg3Manufacturer = _ImPM1BatLeg3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 1),
    _ImPM1BatLeg3Manufacturer_Type()
)
imPM1BatLeg3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg3Manufacturer.setStatus("current")


class _ImPM1BatLeg3Type_Type(DisplayString):
    """Custom type imPM1BatLeg3Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg3Type_Type.__name__ = "DisplayString"
_ImPM1BatLeg3Type_Object = MibScalar
imPM1BatLeg3Type = _ImPM1BatLeg3Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 2),
    _ImPM1BatLeg3Type_Type()
)
imPM1BatLeg3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg3Type.setStatus("current")


class _ImPM1BatLeg3serNumb_Type(DisplayString):
    """Custom type imPM1BatLeg3serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg3serNumb_Type.__name__ = "DisplayString"
_ImPM1BatLeg3serNumb_Object = MibScalar
imPM1BatLeg3serNumb = _ImPM1BatLeg3serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 3),
    _ImPM1BatLeg3serNumb_Type()
)
imPM1BatLeg3serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg3serNumb.setStatus("current")


class _ImPM1BatLeg3nextServiceDate_Type(DisplayString):
    """Custom type imPM1BatLeg3nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg3nextServiceDate_Type.__name__ = "DisplayString"
_ImPM1BatLeg3nextServiceDate_Object = MibScalar
imPM1BatLeg3nextServiceDate = _ImPM1BatLeg3nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 4),
    _ImPM1BatLeg3nextServiceDate_Type()
)
imPM1BatLeg3nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg3nextServiceDate.setStatus("current")


class _ImPM1BatLeg3InstallationDate_Type(DisplayString):
    """Custom type imPM1BatLeg3InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM1BatLeg3InstallationDate_Type.__name__ = "DisplayString"
_ImPM1BatLeg3InstallationDate_Object = MibScalar
imPM1BatLeg3InstallationDate = _ImPM1BatLeg3InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 5),
    _ImPM1BatLeg3InstallationDate_Type()
)
imPM1BatLeg3InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg3InstallationDate.setStatus("current")
_ImPm1BatLeg3NominalVoltage_Type = Integer32
_ImPm1BatLeg3NominalVoltage_Object = MibScalar
imPm1BatLeg3NominalVoltage = _ImPm1BatLeg3NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 6),
    _ImPm1BatLeg3NominalVoltage_Type()
)
imPm1BatLeg3NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3NominalVoltage.setUnits("0.1 V")
_ImPm1BatLeg3NominalCapacity_Type = NonNegativeInteger
_ImPm1BatLeg3NominalCapacity_Object = MibScalar
imPm1BatLeg3NominalCapacity = _ImPm1BatLeg3NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 7),
    _ImPm1BatLeg3NominalCapacity_Type()
)
imPm1BatLeg3NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3NominalCapacity.setUnits("Ah")
_ImPm1BatLeg3Lifetime_Type = NonNegativeInteger
_ImPm1BatLeg3Lifetime_Object = MibScalar
imPm1BatLeg3Lifetime = _ImPm1BatLeg3Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 8),
    _ImPm1BatLeg3Lifetime_Type()
)
imPm1BatLeg3Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3Lifetime.setUnits("years")
_ImPm1BatLeg3Voltage_Type = Integer32
_ImPm1BatLeg3Voltage_Object = MibScalar
imPm1BatLeg3Voltage = _ImPm1BatLeg3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 9),
    _ImPm1BatLeg3Voltage_Type()
)
imPm1BatLeg3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3Voltage.setUnits("0.1 V")
_ImPm1BatLeg3Current_Type = Integer32
_ImPm1BatLeg3Current_Object = MibScalar
imPm1BatLeg3Current = _ImPm1BatLeg3Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 10),
    _ImPm1BatLeg3Current_Type()
)
imPm1BatLeg3Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3Current.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3Current.setUnits("0.1 A")
_ImPm1BatLeg3Temperature_Type = Integer32
_ImPm1BatLeg3Temperature_Object = MibScalar
imPm1BatLeg3Temperature = _ImPm1BatLeg3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 11),
    _ImPm1BatLeg3Temperature_Type()
)
imPm1BatLeg3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3Temperature.setUnits("degrees Centigrade")
_ImPm1BatLeg3ChargeState_Type = NonNegativeInteger
_ImPm1BatLeg3ChargeState_Object = MibScalar
imPm1BatLeg3ChargeState = _ImPm1BatLeg3ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 12),
    _ImPm1BatLeg3ChargeState_Type()
)
imPm1BatLeg3ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3ChargeState.setUnits("%")
_ImPm1BatLeg3RestCapacity_Type = NonNegativeInteger
_ImPm1BatLeg3RestCapacity_Object = MibScalar
imPm1BatLeg3RestCapacity = _ImPm1BatLeg3RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 13),
    _ImPm1BatLeg3RestCapacity_Type()
)
imPm1BatLeg3RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3RestCapacity.setUnits("Ah")
_ImPm1BatLeg3Autonomytime_Type = NonNegativeInteger
_ImPm1BatLeg3Autonomytime_Object = MibScalar
imPm1BatLeg3Autonomytime = _ImPm1BatLeg3Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 14),
    _ImPm1BatLeg3Autonomytime_Type()
)
imPm1BatLeg3Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3Autonomytime.setUnits("min")
_ImPm1BatLeg3TimeOnBattery_Type = NonNegativeInteger
_ImPm1BatLeg3TimeOnBattery_Object = MibScalar
imPm1BatLeg3TimeOnBattery = _ImPm1BatLeg3TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 15),
    _ImPm1BatLeg3TimeOnBattery_Type()
)
imPm1BatLeg3TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1BatLeg3TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPm1BatLeg3TimeOnBattery.setUnits("min")


class _ImPM1BatLeg3Fuse_Type(Integer32):
    """Custom type imPM1BatLeg3Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg3Fuse_Type.__name__ = "Integer32"
_ImPM1BatLeg3Fuse_Object = MibScalar
imPM1BatLeg3Fuse = _ImPM1BatLeg3Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 16),
    _ImPM1BatLeg3Fuse_Type()
)
imPM1BatLeg3Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg3Fuse.setStatus("current")


class _ImPM1BatLeg3Breaker_Type(Integer32):
    """Custom type imPM1BatLeg3Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg3Breaker_Type.__name__ = "Integer32"
_ImPM1BatLeg3Breaker_Object = MibScalar
imPM1BatLeg3Breaker = _ImPM1BatLeg3Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 17),
    _ImPM1BatLeg3Breaker_Type()
)
imPM1BatLeg3Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg3Breaker.setStatus("current")


class _ImPM1BatLeg3LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM1BatLeg3LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1BatLeg3LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM1BatLeg3LowVoltageDisconnect_Object = MibScalar
imPM1BatLeg3LowVoltageDisconnect = _ImPM1BatLeg3LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 9, 18),
    _ImPM1BatLeg3LowVoltageDisconnect_Type()
)
imPM1BatLeg3LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1BatLeg3LowVoltageDisconnect.setStatus("current")
_ImPM1Distrib_ObjectIdentity = ObjectIdentity
imPM1Distrib = _ImPM1Distrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 10)
)
_ImPm1Distrib_Type = Integer32
_ImPm1Distrib_Object = MibScalar
imPm1Distrib = _ImPm1Distrib_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 10, 1),
    _ImPm1Distrib_Type()
)
imPm1Distrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm1Distrib.setStatus("current")
if mibBuilder.loadTexts:
    imPm1Distrib.setUnits("degrees Centigrade")
_ImPM1DistTable_Object = MibTable
imPM1DistTable = _ImPM1DistTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    imPM1DistTable.setStatus("current")
_ImPM1DistEntry_Object = MibTableRow
imPM1DistEntry = _ImPM1DistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 10, 2, 1)
)
imPM1DistEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imPM1DistId"),
)
if mibBuilder.loadTexts:
    imPM1DistEntry.setStatus("current")
_ImPM1DistId_Type = PositiveInteger
_ImPM1DistId_Object = MibTableColumn
imPM1DistId = _ImPM1DistId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 10, 2, 1, 1),
    _ImPM1DistId_Type()
)
imPM1DistId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imPM1DistId.setStatus("current")


class _ImPM1DistFuse_Type(Integer32):
    """Custom type imPM1DistFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1DistFuse_Type.__name__ = "Integer32"
_ImPM1DistFuse_Object = MibTableColumn
imPM1DistFuse = _ImPM1DistFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 10, 2, 1, 2),
    _ImPM1DistFuse_Type()
)
imPM1DistFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1DistFuse.setStatus("current")


class _ImPM1DistBreaker_Type(Integer32):
    """Custom type imPM1DistBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM1DistBreaker_Type.__name__ = "Integer32"
_ImPM1DistBreaker_Object = MibTableColumn
imPM1DistBreaker = _ImPM1DistBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 10, 2, 1, 3),
    _ImPM1DistBreaker_Type()
)
imPM1DistBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1DistBreaker.setStatus("current")
_ImPM1Control_ObjectIdentity = ObjectIdentity
imPM1Control = _ImPM1Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11)
)
_ImPM1ContTable_Object = MibTable
imPM1ContTable = _ImPM1ContTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    imPM1ContTable.setStatus("current")
_ImPM1ContEntry_Object = MibTableRow
imPM1ContEntry = _ImPM1ContEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 1, 1)
)
imPM1ContEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imPM1ContId"),
)
if mibBuilder.loadTexts:
    imPM1ContEntry.setStatus("current")
_ImPM1ContId_Type = PositiveInteger
_ImPM1ContId_Object = MibTableColumn
imPM1ContId = _ImPM1ContId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 1, 1, 1),
    _ImPM1ContId_Type()
)
imPM1ContId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imPM1ContId.setStatus("current")


class _ImPM1ContState_Type(Integer32):
    """Custom type imPM1ContState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_ImPM1ContState_Type.__name__ = "Integer32"
_ImPM1ContState_Object = MibTableColumn
imPM1ContState = _ImPM1ContState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 1, 1, 2),
    _ImPM1ContState_Type()
)
imPM1ContState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM1ContState.setStatus("current")


class _ImPM1ContLabel_Type(DisplayString):
    """Custom type imPM1ContLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM1ContLabel_Type.__name__ = "DisplayString"
_ImPM1ContLabel_Object = MibTableColumn
imPM1ContLabel = _ImPM1ContLabel_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 1, 1, 3),
    _ImPM1ContLabel_Type()
)
imPM1ContLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1ContLabel.setStatus("current")
_ImPM1ContTimeOFF_Type = Integer32
_ImPM1ContTimeOFF_Object = MibTableColumn
imPM1ContTimeOFF = _ImPM1ContTimeOFF_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 1, 1, 4),
    _ImPM1ContTimeOFF_Type()
)
imPM1ContTimeOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM1ContTimeOFF.setStatus("current")
if mibBuilder.loadTexts:
    imPM1ContTimeOFF.setUnits("min")


class _ImPM1ContAuto_Type(Integer32):
    """Custom type imPM1ContAuto based on Integer32"""
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


_ImPM1ContAuto_Type.__name__ = "Integer32"
_ImPM1ContAuto_Object = MibTableColumn
imPM1ContAuto = _ImPM1ContAuto_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 1, 1, 5),
    _ImPM1ContAuto_Type()
)
imPM1ContAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM1ContAuto.setStatus("current")


class _ImPM1ContTestCAPcommand_Type(Integer32):
    """Custom type imPM1ContTestCAPcommand based on Integer32"""
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


_ImPM1ContTestCAPcommand_Type.__name__ = "Integer32"
_ImPM1ContTestCAPcommand_Object = MibScalar
imPM1ContTestCAPcommand = _ImPM1ContTestCAPcommand_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 2),
    _ImPM1ContTestCAPcommand_Type()
)
imPM1ContTestCAPcommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM1ContTestCAPcommand.setStatus("current")
_ImPM1ContTestCAPvoltage_Type = Integer32
_ImPM1ContTestCAPvoltage_Object = MibScalar
imPM1ContTestCAPvoltage = _ImPM1ContTestCAPvoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 3),
    _ImPM1ContTestCAPvoltage_Type()
)
imPM1ContTestCAPvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1ContTestCAPvoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM1ContTestCAPvoltage.setUnits("0.1 V")
_ImPM1ContTestCAPcurrent_Type = Integer32
_ImPM1ContTestCAPcurrent_Object = MibScalar
imPM1ContTestCAPcurrent = _ImPM1ContTestCAPcurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 4),
    _ImPM1ContTestCAPcurrent_Type()
)
imPM1ContTestCAPcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1ContTestCAPcurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM1ContTestCAPcurrent.setUnits("0.1 A")
_ImPM1ContTestCAPtemperature_Type = Integer32
_ImPM1ContTestCAPtemperature_Object = MibScalar
imPM1ContTestCAPtemperature = _ImPM1ContTestCAPtemperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 5),
    _ImPM1ContTestCAPtemperature_Type()
)
imPM1ContTestCAPtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1ContTestCAPtemperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM1ContTestCAPtemperature.setUnits("degrees Centigrade")
_ImPM1ContTestCAPduration_Type = Integer32
_ImPM1ContTestCAPduration_Object = MibScalar
imPM1ContTestCAPduration = _ImPM1ContTestCAPduration_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 6),
    _ImPM1ContTestCAPduration_Type()
)
imPM1ContTestCAPduration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1ContTestCAPduration.setStatus("current")
if mibBuilder.loadTexts:
    imPM1ContTestCAPduration.setUnits("min")
_ImPM1ContTestCAPstatus_Type = Integer32
_ImPM1ContTestCAPstatus_Object = MibScalar
imPM1ContTestCAPstatus = _ImPM1ContTestCAPstatus_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 1, 11, 7),
    _ImPM1ContTestCAPstatus_Type()
)
imPM1ContTestCAPstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM1ContTestCAPstatus.setStatus("current")
_ImPanM2_ObjectIdentity = ObjectIdentity
imPanM2 = _ImPanM2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2)
)
_ImPM2SystemID_ObjectIdentity = ObjectIdentity
imPM2SystemID = _ImPM2SystemID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1)
)


class _ImPM2SystemIDManufacturer_Type(DisplayString):
    """Custom type imPM2SystemIDManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM2SystemIDManufacturer_Type.__name__ = "DisplayString"
_ImPM2SystemIDManufacturer_Object = MibScalar
imPM2SystemIDManufacturer = _ImPM2SystemIDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 1),
    _ImPM2SystemIDManufacturer_Type()
)
imPM2SystemIDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDManufacturer.setStatus("current")


class _ImPM2SystemIDType_Type(DisplayString):
    """Custom type imPM2SystemIDType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2SystemIDType_Type.__name__ = "DisplayString"
_ImPM2SystemIDType_Object = MibScalar
imPM2SystemIDType = _ImPM2SystemIDType_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 2),
    _ImPM2SystemIDType_Type()
)
imPM2SystemIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDType.setStatus("current")


class _ImPM2SystemIDserNumb_Type(DisplayString):
    """Custom type imPM2SystemIDserNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2SystemIDserNumb_Type.__name__ = "DisplayString"
_ImPM2SystemIDserNumb_Object = MibScalar
imPM2SystemIDserNumb = _ImPM2SystemIDserNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 3),
    _ImPM2SystemIDserNumb_Type()
)
imPM2SystemIDserNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDserNumb.setStatus("current")


class _ImPM2SystemIDnextServiceDate_Type(DisplayString):
    """Custom type imPM2SystemIDnextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2SystemIDnextServiceDate_Type.__name__ = "DisplayString"
_ImPM2SystemIDnextServiceDate_Object = MibScalar
imPM2SystemIDnextServiceDate = _ImPM2SystemIDnextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 4),
    _ImPM2SystemIDnextServiceDate_Type()
)
imPM2SystemIDnextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDnextServiceDate.setStatus("current")
_ImPM2SystemIDaddress_Type = NonNegativeInteger
_ImPM2SystemIDaddress_Object = MibScalar
imPM2SystemIDaddress = _ImPM2SystemIDaddress_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 5),
    _ImPM2SystemIDaddress_Type()
)
imPM2SystemIDaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDaddress.setStatus("current")
_ImPM2SystemIDhwVersion_Type = NonNegativeInteger
_ImPM2SystemIDhwVersion_Object = MibScalar
imPM2SystemIDhwVersion = _ImPM2SystemIDhwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 6),
    _ImPM2SystemIDhwVersion_Type()
)
imPM2SystemIDhwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDhwVersion.setStatus("current")
_ImPM2SystemIDswVersion_Type = NonNegativeInteger
_ImPM2SystemIDswVersion_Object = MibScalar
imPM2SystemIDswVersion = _ImPM2SystemIDswVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 7),
    _ImPM2SystemIDswVersion_Type()
)
imPM2SystemIDswVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDswVersion.setStatus("current")


class _ImPM2SystemIDPMserialNumber_Type(DisplayString):
    """Custom type imPM2SystemIDPMserialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2SystemIDPMserialNumber_Type.__name__ = "DisplayString"
_ImPM2SystemIDPMserialNumber_Object = MibScalar
imPM2SystemIDPMserialNumber = _ImPM2SystemIDPMserialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 8),
    _ImPM2SystemIDPMserialNumber_Type()
)
imPM2SystemIDPMserialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDPMserialNumber.setStatus("current")


class _ImPM2SystemIDbuttonName_Type(DisplayString):
    """Custom type imPM2SystemIDbuttonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2SystemIDbuttonName_Type.__name__ = "DisplayString"
_ImPM2SystemIDbuttonName_Object = MibScalar
imPM2SystemIDbuttonName = _ImPM2SystemIDbuttonName_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 1, 9),
    _ImPM2SystemIDbuttonName_Type()
)
imPM2SystemIDbuttonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemIDbuttonName.setStatus("current")
_ImPM2SystemGEN_ObjectIdentity = ObjectIdentity
imPM2SystemGEN = _ImPM2SystemGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2)
)


class _ImPM2SystemGENSurgeArrester_Type(Integer32):
    """Custom type imPM2SystemGENSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2SystemGENSurgeArrester_Type.__name__ = "Integer32"
_ImPM2SystemGENSurgeArrester_Object = MibScalar
imPM2SystemGENSurgeArrester = _ImPM2SystemGENSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 1),
    _ImPM2SystemGENSurgeArrester_Type()
)
imPM2SystemGENSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENSurgeArrester.setStatus("current")


class _ImPM2SystemGENDoor1_Type(Integer32):
    """Custom type imPM2SystemGENDoor1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_ImPM2SystemGENDoor1_Type.__name__ = "Integer32"
_ImPM2SystemGENDoor1_Object = MibScalar
imPM2SystemGENDoor1 = _ImPM2SystemGENDoor1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 2),
    _ImPM2SystemGENDoor1_Type()
)
imPM2SystemGENDoor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENDoor1.setStatus("current")


class _ImPM2SystemGENDoor2_Type(Integer32):
    """Custom type imPM2SystemGENDoor2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_ImPM2SystemGENDoor2_Type.__name__ = "Integer32"
_ImPM2SystemGENDoor2_Object = MibScalar
imPM2SystemGENDoor2 = _ImPM2SystemGENDoor2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 3),
    _ImPM2SystemGENDoor2_Type()
)
imPM2SystemGENDoor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENDoor2.setStatus("current")


class _ImPM2SystemGENFan_Type(Integer32):
    """Custom type imPM2SystemGENFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_ImPM2SystemGENFan_Type.__name__ = "Integer32"
_ImPM2SystemGENFan_Object = MibScalar
imPM2SystemGENFan = _ImPM2SystemGENFan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 4),
    _ImPM2SystemGENFan_Type()
)
imPM2SystemGENFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENFan.setStatus("current")


class _ImPM2SystemGENuser1_Type(Integer32):
    """Custom type imPM2SystemGENuser1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2SystemGENuser1_Type.__name__ = "Integer32"
_ImPM2SystemGENuser1_Object = MibScalar
imPM2SystemGENuser1 = _ImPM2SystemGENuser1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 5),
    _ImPM2SystemGENuser1_Type()
)
imPM2SystemGENuser1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENuser1.setStatus("current")


class _ImPM2SystemGENuser2_Type(Integer32):
    """Custom type imPM2SystemGENuser2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2SystemGENuser2_Type.__name__ = "Integer32"
_ImPM2SystemGENuser2_Object = MibScalar
imPM2SystemGENuser2 = _ImPM2SystemGENuser2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 6),
    _ImPM2SystemGENuser2_Type()
)
imPM2SystemGENuser2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENuser2.setStatus("current")


class _ImPM2SystemGENuser3_Type(Integer32):
    """Custom type imPM2SystemGENuser3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2SystemGENuser3_Type.__name__ = "Integer32"
_ImPM2SystemGENuser3_Object = MibScalar
imPM2SystemGENuser3 = _ImPM2SystemGENuser3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 7),
    _ImPM2SystemGENuser3_Type()
)
imPM2SystemGENuser3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENuser3.setStatus("current")


class _ImPM2SystemGENuser4_Type(Integer32):
    """Custom type imPM2SystemGENuser4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2SystemGENuser4_Type.__name__ = "Integer32"
_ImPM2SystemGENuser4_Object = MibScalar
imPM2SystemGENuser4 = _ImPM2SystemGENuser4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 8),
    _ImPM2SystemGENuser4_Type()
)
imPM2SystemGENuser4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENuser4.setStatus("current")
_ImPM2SystemGENtemperature_Type = NonNegativeInteger
_ImPM2SystemGENtemperature_Object = MibScalar
imPM2SystemGENtemperature = _ImPM2SystemGENtemperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 2, 9),
    _ImPM2SystemGENtemperature_Type()
)
imPM2SystemGENtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2SystemGENtemperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM2SystemGENtemperature.setUnits("degrees Centigrade")
_ImPM2Power1_ObjectIdentity = ObjectIdentity
imPM2Power1 = _ImPM2Power1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3)
)


class _ImPM2Power1Manufacturer_Type(DisplayString):
    """Custom type imPM2Power1Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM2Power1Manufacturer_Type.__name__ = "DisplayString"
_ImPM2Power1Manufacturer_Object = MibScalar
imPM2Power1Manufacturer = _ImPM2Power1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 1),
    _ImPM2Power1Manufacturer_Type()
)
imPM2Power1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Manufacturer.setStatus("current")


class _ImPM2Power1Type_Type(DisplayString):
    """Custom type imPM2Power1Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power1Type_Type.__name__ = "DisplayString"
_ImPM2Power1Type_Object = MibScalar
imPM2Power1Type = _ImPM2Power1Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 2),
    _ImPM2Power1Type_Type()
)
imPM2Power1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Type.setStatus("current")


class _ImPM2Power1serNumb_Type(DisplayString):
    """Custom type imPM2Power1serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power1serNumb_Type.__name__ = "DisplayString"
_ImPM2Power1serNumb_Object = MibScalar
imPM2Power1serNumb = _ImPM2Power1serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 3),
    _ImPM2Power1serNumb_Type()
)
imPM2Power1serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1serNumb.setStatus("current")


class _ImPM2Power1nextServiceDate_Type(DisplayString):
    """Custom type imPM2Power1nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power1nextServiceDate_Type.__name__ = "DisplayString"
_ImPM2Power1nextServiceDate_Object = MibScalar
imPM2Power1nextServiceDate = _ImPM2Power1nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 4),
    _ImPM2Power1nextServiceDate_Type()
)
imPM2Power1nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1nextServiceDate.setStatus("current")
_ImPM2Power1InputVoltage_Type = Integer32
_ImPM2Power1InputVoltage_Object = MibScalar
imPM2Power1InputVoltage = _ImPM2Power1InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 5),
    _ImPM2Power1InputVoltage_Type()
)
imPM2Power1InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputVoltage.setUnits("0.1 V")
_ImPM2Power1InputCurrent_Type = Integer32
_ImPM2Power1InputCurrent_Object = MibScalar
imPM2Power1InputCurrent = _ImPM2Power1InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 6),
    _ImPM2Power1InputCurrent_Type()
)
imPM2Power1InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputCurrent.setUnits("0.1 A")
_ImPM2Power1InputPowerVA_Type = Integer32
_ImPM2Power1InputPowerVA_Object = MibScalar
imPM2Power1InputPowerVA = _ImPM2Power1InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 7),
    _ImPM2Power1InputPowerVA_Type()
)
imPM2Power1InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerVA.setUnits("VA")
_ImPM2Power1InputPowerKVA_Type = Integer32
_ImPM2Power1InputPowerKVA_Object = MibScalar
imPM2Power1InputPowerKVA = _ImPM2Power1InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 8),
    _ImPM2Power1InputPowerKVA_Type()
)
imPM2Power1InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKVA.setUnits("0.1 kVA")
_ImPM2Power1InputPowerW_Type = Integer32
_ImPM2Power1InputPowerW_Object = MibScalar
imPM2Power1InputPowerW = _ImPM2Power1InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 9),
    _ImPM2Power1InputPowerW_Type()
)
imPM2Power1InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerW.setUnits("W")
_ImPM2Power1InputPowerKW_Type = Integer32
_ImPM2Power1InputPowerKW_Object = MibScalar
imPM2Power1InputPowerKW = _ImPM2Power1InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 10),
    _ImPM2Power1InputPowerKW_Type()
)
imPM2Power1InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKW.setUnits("0.1 kW")
_ImPM2Power1InputVoltagePhase1_Type = Integer32
_ImPM2Power1InputVoltagePhase1_Object = MibScalar
imPM2Power1InputVoltagePhase1 = _ImPM2Power1InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 11),
    _ImPM2Power1InputVoltagePhase1_Type()
)
imPM2Power1InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputVoltagePhase1.setUnits("0.1 V")
_ImPM2Power1InputCurrentPhase1_Type = Integer32
_ImPM2Power1InputCurrentPhase1_Object = MibScalar
imPM2Power1InputCurrentPhase1 = _ImPM2Power1InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 12),
    _ImPM2Power1InputCurrentPhase1_Type()
)
imPM2Power1InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputCurrentPhase1.setUnits("0.1 A")
_ImPM2Power1InputPowerVAphase1_Type = Integer32
_ImPM2Power1InputPowerVAphase1_Object = MibScalar
imPM2Power1InputPowerVAphase1 = _ImPM2Power1InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 13),
    _ImPM2Power1InputPowerVAphase1_Type()
)
imPM2Power1InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerVAphase1.setUnits("VA")
_ImPM2Power1InputPowerKVAphase1_Type = Integer32
_ImPM2Power1InputPowerKVAphase1_Object = MibScalar
imPM2Power1InputPowerKVAphase1 = _ImPM2Power1InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 14),
    _ImPM2Power1InputPowerKVAphase1_Type()
)
imPM2Power1InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM2Power1InputVoltagePhase2_Type = Integer32
_ImPM2Power1InputVoltagePhase2_Object = MibScalar
imPM2Power1InputVoltagePhase2 = _ImPM2Power1InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 15),
    _ImPM2Power1InputVoltagePhase2_Type()
)
imPM2Power1InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputVoltagePhase2.setUnits("0.1 V")
_ImPM2Power1InputCurrentPhase2_Type = Integer32
_ImPM2Power1InputCurrentPhase2_Object = MibScalar
imPM2Power1InputCurrentPhase2 = _ImPM2Power1InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 16),
    _ImPM2Power1InputCurrentPhase2_Type()
)
imPM2Power1InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputCurrentPhase2.setUnits("0.1 A")
_ImPM2Power1InputPowerVAphase2_Type = Integer32
_ImPM2Power1InputPowerVAphase2_Object = MibScalar
imPM2Power1InputPowerVAphase2 = _ImPM2Power1InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 17),
    _ImPM2Power1InputPowerVAphase2_Type()
)
imPM2Power1InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerVAphase2.setUnits("VA")
_ImPM2Power1InputPowerKVAphase2_Type = Integer32
_ImPM2Power1InputPowerKVAphase2_Object = MibScalar
imPM2Power1InputPowerKVAphase2 = _ImPM2Power1InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 18),
    _ImPM2Power1InputPowerKVAphase2_Type()
)
imPM2Power1InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM2Power1InputVoltagePhase3_Type = Integer32
_ImPM2Power1InputVoltagePhase3_Object = MibScalar
imPM2Power1InputVoltagePhase3 = _ImPM2Power1InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 19),
    _ImPM2Power1InputVoltagePhase3_Type()
)
imPM2Power1InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputVoltagePhase3.setUnits("0.1 V")
_ImPM2Power1InputCurrentPhase3_Type = Integer32
_ImPM2Power1InputCurrentPhase3_Object = MibScalar
imPM2Power1InputCurrentPhase3 = _ImPM2Power1InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 20),
    _ImPM2Power1InputCurrentPhase3_Type()
)
imPM2Power1InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputCurrentPhase3.setUnits("0.1 A")
_ImPM2Power1InputPowerVAphase3_Type = Integer32
_ImPM2Power1InputPowerVAphase3_Object = MibScalar
imPM2Power1InputPowerVAphase3 = _ImPM2Power1InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 21),
    _ImPM2Power1InputPowerVAphase3_Type()
)
imPM2Power1InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerVAphase3.setUnits("VA")
_ImPM2Power1InputPowerKVAphase3_Type = Integer32
_ImPM2Power1InputPowerKVAphase3_Object = MibScalar
imPM2Power1InputPowerKVAphase3 = _ImPM2Power1InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 22),
    _ImPM2Power1InputPowerKVAphase3_Type()
)
imPM2Power1InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM2Power1OutputVoltage_Type = Integer32
_ImPM2Power1OutputVoltage_Object = MibScalar
imPM2Power1OutputVoltage = _ImPM2Power1OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 23),
    _ImPM2Power1OutputVoltage_Type()
)
imPM2Power1OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputVoltage.setUnits("0.1 V")
_ImPM2Power1OutputCurrent_Type = Integer32
_ImPM2Power1OutputCurrent_Object = MibScalar
imPM2Power1OutputCurrent = _ImPM2Power1OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 24),
    _ImPM2Power1OutputCurrent_Type()
)
imPM2Power1OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputCurrent.setUnits("0.1 A")
_ImPM2Power1OutputPowerVA_Type = Integer32
_ImPM2Power1OutputPowerVA_Object = MibScalar
imPM2Power1OutputPowerVA = _ImPM2Power1OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 25),
    _ImPM2Power1OutputPowerVA_Type()
)
imPM2Power1OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerVA.setUnits("VA")
_ImPM2Power1OutputPowerKVA_Type = Integer32
_ImPM2Power1OutputPowerKVA_Object = MibScalar
imPM2Power1OutputPowerKVA = _ImPM2Power1OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 26),
    _ImPM2Power1OutputPowerKVA_Type()
)
imPM2Power1OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKVA.setUnits("0.1 kVA")
_ImPM2Power1OutputPowerW_Type = Integer32
_ImPM2Power1OutputPowerW_Object = MibScalar
imPM2Power1OutputPowerW = _ImPM2Power1OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 27),
    _ImPM2Power1OutputPowerW_Type()
)
imPM2Power1OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerW.setUnits("W")
_ImPM2Power1OutputPowerKW_Type = Integer32
_ImPM2Power1OutputPowerKW_Object = MibScalar
imPM2Power1OutputPowerKW = _ImPM2Power1OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 28),
    _ImPM2Power1OutputPowerKW_Type()
)
imPM2Power1OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKW.setUnits("0.1 kW")
_ImPM2Power1OutputLoad_Type = Integer32
_ImPM2Power1OutputLoad_Object = MibScalar
imPM2Power1OutputLoad = _ImPM2Power1OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 29),
    _ImPM2Power1OutputLoad_Type()
)
imPM2Power1OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputLoad.setUnits("%")
_ImPM2Power1OutputFrequency_Type = NonNegativeInteger
_ImPM2Power1OutputFrequency_Object = MibScalar
imPM2Power1OutputFrequency = _ImPM2Power1OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 30),
    _ImPM2Power1OutputFrequency_Type()
)
imPM2Power1OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputFrequency.setUnits("0.1 Hz")
_ImPM2Power1Temperature_Type = Integer32
_ImPM2Power1Temperature_Object = MibScalar
imPM2Power1Temperature = _ImPM2Power1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 31),
    _ImPM2Power1Temperature_Type()
)
imPM2Power1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1Temperature.setUnits("degrees Centigrade")


class _ImPM2Power1Running1_Type(Integer32):
    """Custom type imPM2Power1Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Running1_Type.__name__ = "Integer32"
_ImPM2Power1Running1_Object = MibScalar
imPM2Power1Running1 = _ImPM2Power1Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 32),
    _ImPM2Power1Running1_Type()
)
imPM2Power1Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Running1.setStatus("current")


class _ImPM2Power1Running2_Type(Integer32):
    """Custom type imPM2Power1Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Running2_Type.__name__ = "Integer32"
_ImPM2Power1Running2_Object = MibScalar
imPM2Power1Running2 = _ImPM2Power1Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 33),
    _ImPM2Power1Running2_Type()
)
imPM2Power1Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Running2.setStatus("current")


class _ImPM2Power1Running3_Type(Integer32):
    """Custom type imPM2Power1Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Running3_Type.__name__ = "Integer32"
_ImPM2Power1Running3_Object = MibScalar
imPM2Power1Running3 = _ImPM2Power1Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 34),
    _ImPM2Power1Running3_Type()
)
imPM2Power1Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Running3.setStatus("current")


class _ImPM2Power1Running4_Type(Integer32):
    """Custom type imPM2Power1Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Running4_Type.__name__ = "Integer32"
_ImPM2Power1Running4_Object = MibScalar
imPM2Power1Running4 = _ImPM2Power1Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 35),
    _ImPM2Power1Running4_Type()
)
imPM2Power1Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Running4.setStatus("current")


class _ImPM2Power1Running5_Type(Integer32):
    """Custom type imPM2Power1Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Running5_Type.__name__ = "Integer32"
_ImPM2Power1Running5_Object = MibScalar
imPM2Power1Running5 = _ImPM2Power1Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 36),
    _ImPM2Power1Running5_Type()
)
imPM2Power1Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Running5.setStatus("current")


class _ImPM2Power1Running6_Type(Integer32):
    """Custom type imPM2Power1Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Running6_Type.__name__ = "Integer32"
_ImPM2Power1Running6_Object = MibScalar
imPM2Power1Running6 = _ImPM2Power1Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 37),
    _ImPM2Power1Running6_Type()
)
imPM2Power1Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Running6.setStatus("current")


class _ImPM2Power1Running7_Type(Integer32):
    """Custom type imPM2Power1Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Running7_Type.__name__ = "Integer32"
_ImPM2Power1Running7_Object = MibScalar
imPM2Power1Running7 = _ImPM2Power1Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 38),
    _ImPM2Power1Running7_Type()
)
imPM2Power1Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Running7.setStatus("current")


class _ImPM2Power1Running8_Type(Integer32):
    """Custom type imPM2Power1Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Running8_Type.__name__ = "Integer32"
_ImPM2Power1Running8_Object = MibScalar
imPM2Power1Running8 = _ImPM2Power1Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 39),
    _ImPM2Power1Running8_Type()
)
imPM2Power1Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Running8.setStatus("current")


class _ImPM2Power1InputFuse_Type(Integer32):
    """Custom type imPM2Power1InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputFuse_Type.__name__ = "Integer32"
_ImPM2Power1InputFuse_Object = MibScalar
imPM2Power1InputFuse = _ImPM2Power1InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 40),
    _ImPM2Power1InputFuse_Type()
)
imPM2Power1InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputFuse.setStatus("current")


class _ImPM2Power1InputFuse1_Type(Integer32):
    """Custom type imPM2Power1InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputFuse1_Type.__name__ = "Integer32"
_ImPM2Power1InputFuse1_Object = MibScalar
imPM2Power1InputFuse1 = _ImPM2Power1InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 41),
    _ImPM2Power1InputFuse1_Type()
)
imPM2Power1InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputFuse1.setStatus("current")


class _ImPM2Power1InputFuse2_Type(Integer32):
    """Custom type imPM2Power1InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputFuse2_Type.__name__ = "Integer32"
_ImPM2Power1InputFuse2_Object = MibScalar
imPM2Power1InputFuse2 = _ImPM2Power1InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 42),
    _ImPM2Power1InputFuse2_Type()
)
imPM2Power1InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputFuse2.setStatus("current")


class _ImPM2Power1InputFuse3_Type(Integer32):
    """Custom type imPM2Power1InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputFuse3_Type.__name__ = "Integer32"
_ImPM2Power1InputFuse3_Object = MibScalar
imPM2Power1InputFuse3 = _ImPM2Power1InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 43),
    _ImPM2Power1InputFuse3_Type()
)
imPM2Power1InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputFuse3.setStatus("current")


class _ImPM2Power1InputBreaker_Type(Integer32):
    """Custom type imPM2Power1InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputBreaker_Type.__name__ = "Integer32"
_ImPM2Power1InputBreaker_Object = MibScalar
imPM2Power1InputBreaker = _ImPM2Power1InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 44),
    _ImPM2Power1InputBreaker_Type()
)
imPM2Power1InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputBreaker.setStatus("current")


class _ImPM2Power1InputBreaker1_Type(Integer32):
    """Custom type imPM2Power1InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputBreaker1_Type.__name__ = "Integer32"
_ImPM2Power1InputBreaker1_Object = MibScalar
imPM2Power1InputBreaker1 = _ImPM2Power1InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 45),
    _ImPM2Power1InputBreaker1_Type()
)
imPM2Power1InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputBreaker1.setStatus("current")


class _ImPM2Power1InputBreaker2_Type(Integer32):
    """Custom type imPM2Power1InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputBreaker2_Type.__name__ = "Integer32"
_ImPM2Power1InputBreaker2_Object = MibScalar
imPM2Power1InputBreaker2 = _ImPM2Power1InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 46),
    _ImPM2Power1InputBreaker2_Type()
)
imPM2Power1InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputBreaker2.setStatus("current")


class _ImPM2Power1InputBreaker3_Type(Integer32):
    """Custom type imPM2Power1InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputBreaker3_Type.__name__ = "Integer32"
_ImPM2Power1InputBreaker3_Object = MibScalar
imPM2Power1InputBreaker3 = _ImPM2Power1InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 47),
    _ImPM2Power1InputBreaker3_Type()
)
imPM2Power1InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputBreaker3.setStatus("current")


class _ImPM2Power1InputSurgeArrester_Type(Integer32):
    """Custom type imPM2Power1InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM2Power1InputSurgeArrester_Object = MibScalar
imPM2Power1InputSurgeArrester = _ImPM2Power1InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 48),
    _ImPM2Power1InputSurgeArrester_Type()
)
imPM2Power1InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1InputSurgeArrester.setStatus("current")


class _ImPM2Power1OutputFuse_Type(Integer32):
    """Custom type imPM2Power1OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1OutputFuse_Type.__name__ = "Integer32"
_ImPM2Power1OutputFuse_Object = MibScalar
imPM2Power1OutputFuse = _ImPM2Power1OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 49),
    _ImPM2Power1OutputFuse_Type()
)
imPM2Power1OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputFuse.setStatus("current")


class _ImPM2Power1OutputFuse1_Type(Integer32):
    """Custom type imPM2Power1OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1OutputFuse1_Type.__name__ = "Integer32"
_ImPM2Power1OutputFuse1_Object = MibScalar
imPM2Power1OutputFuse1 = _ImPM2Power1OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 50),
    _ImPM2Power1OutputFuse1_Type()
)
imPM2Power1OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputFuse1.setStatus("current")


class _ImPM2Power1OutputFuse2_Type(Integer32):
    """Custom type imPM2Power1OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1OutputFuse2_Type.__name__ = "Integer32"
_ImPM2Power1OutputFuse2_Object = MibScalar
imPM2Power1OutputFuse2 = _ImPM2Power1OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 51),
    _ImPM2Power1OutputFuse2_Type()
)
imPM2Power1OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputFuse2.setStatus("current")


class _ImPM2Power1OutputBreaker_Type(Integer32):
    """Custom type imPM2Power1OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1OutputBreaker_Type.__name__ = "Integer32"
_ImPM2Power1OutputBreaker_Object = MibScalar
imPM2Power1OutputBreaker = _ImPM2Power1OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 52),
    _ImPM2Power1OutputBreaker_Type()
)
imPM2Power1OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputBreaker.setStatus("current")


class _ImPM2Power1OutputBreaker1_Type(Integer32):
    """Custom type imPM2Power1OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1OutputBreaker1_Type.__name__ = "Integer32"
_ImPM2Power1OutputBreaker1_Object = MibScalar
imPM2Power1OutputBreaker1 = _ImPM2Power1OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 53),
    _ImPM2Power1OutputBreaker1_Type()
)
imPM2Power1OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputBreaker1.setStatus("current")


class _ImPM2Power1OutputBreaker2_Type(Integer32):
    """Custom type imPM2Power1OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1OutputBreaker2_Type.__name__ = "Integer32"
_ImPM2Power1OutputBreaker2_Object = MibScalar
imPM2Power1OutputBreaker2 = _ImPM2Power1OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 54),
    _ImPM2Power1OutputBreaker2_Type()
)
imPM2Power1OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputBreaker2.setStatus("current")


class _ImPM2Power1Fan_Type(Integer32):
    """Custom type imPM2Power1Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1Fan_Type.__name__ = "Integer32"
_ImPM2Power1Fan_Object = MibScalar
imPM2Power1Fan = _ImPM2Power1Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 55),
    _ImPM2Power1Fan_Type()
)
imPM2Power1Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1Fan.setStatus("current")


class _ImPM2Power1BatteryAvailable_Type(Integer32):
    """Custom type imPM2Power1BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power1BatteryAvailable_Type.__name__ = "Integer32"
_ImPM2Power1BatteryAvailable_Object = MibScalar
imPM2Power1BatteryAvailable = _ImPM2Power1BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 56),
    _ImPM2Power1BatteryAvailable_Type()
)
imPM2Power1BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1BatteryAvailable.setStatus("current")
_ImPM2Power1OutputVoltagePhase1_Type = Integer32
_ImPM2Power1OutputVoltagePhase1_Object = MibScalar
imPM2Power1OutputVoltagePhase1 = _ImPM2Power1OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 57),
    _ImPM2Power1OutputVoltagePhase1_Type()
)
imPM2Power1OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputVoltagePhase1.setUnits("0.1 V")
_ImPM2Power1OutputCurrentPhase1_Type = Integer32
_ImPM2Power1OutputCurrentPhase1_Object = MibScalar
imPM2Power1OutputCurrentPhase1 = _ImPM2Power1OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 58),
    _ImPM2Power1OutputCurrentPhase1_Type()
)
imPM2Power1OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputCurrentPhase1.setUnits("0.1 A")
_ImPM2Power1OutputPowerVAphase1_Type = Integer32
_ImPM2Power1OutputPowerVAphase1_Object = MibScalar
imPM2Power1OutputPowerVAphase1 = _ImPM2Power1OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 59),
    _ImPM2Power1OutputPowerVAphase1_Type()
)
imPM2Power1OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerVAphase1.setUnits("VA")
_ImPM2Power1OutputPowerKVAphase1_Type = Integer32
_ImPM2Power1OutputPowerKVAphase1_Object = MibScalar
imPM2Power1OutputPowerKVAphase1 = _ImPM2Power1OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 60),
    _ImPM2Power1OutputPowerKVAphase1_Type()
)
imPM2Power1OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM2Power1OutputVoltagePhase2_Type = Integer32
_ImPM2Power1OutputVoltagePhase2_Object = MibScalar
imPM2Power1OutputVoltagePhase2 = _ImPM2Power1OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 61),
    _ImPM2Power1OutputVoltagePhase2_Type()
)
imPM2Power1OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputVoltagePhase2.setUnits("0.1 V")
_ImPM2Power1OutputCurrentPhase2_Type = Integer32
_ImPM2Power1OutputCurrentPhase2_Object = MibScalar
imPM2Power1OutputCurrentPhase2 = _ImPM2Power1OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 62),
    _ImPM2Power1OutputCurrentPhase2_Type()
)
imPM2Power1OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputCurrentPhase2.setUnits("0.1 A")
_ImPM2Power1OutputPowerVAphase2_Type = Integer32
_ImPM2Power1OutputPowerVAphase2_Object = MibScalar
imPM2Power1OutputPowerVAphase2 = _ImPM2Power1OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 63),
    _ImPM2Power1OutputPowerVAphase2_Type()
)
imPM2Power1OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerVAphase2.setUnits("VA")
_ImPM2Power1OutputPowerKVAphase2_Type = Integer32
_ImPM2Power1OutputPowerKVAphase2_Object = MibScalar
imPM2Power1OutputPowerKVAphase2 = _ImPM2Power1OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 64),
    _ImPM2Power1OutputPowerKVAphase2_Type()
)
imPM2Power1OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM2Power1OutputVoltagePhase3_Type = Integer32
_ImPM2Power1OutputVoltagePhase3_Object = MibScalar
imPM2Power1OutputVoltagePhase3 = _ImPM2Power1OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 65),
    _ImPM2Power1OutputVoltagePhase3_Type()
)
imPM2Power1OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputVoltagePhase3.setUnits("0.1 V")
_ImPM2Power1OutputCurrentPhase3_Type = Integer32
_ImPM2Power1OutputCurrentPhase3_Object = MibScalar
imPM2Power1OutputCurrentPhase3 = _ImPM2Power1OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 66),
    _ImPM2Power1OutputCurrentPhase3_Type()
)
imPM2Power1OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputCurrentPhase3.setUnits("0.1 A")
_ImPM2Power1OutputPowerVAphase3_Type = Integer32
_ImPM2Power1OutputPowerVAphase3_Object = MibScalar
imPM2Power1OutputPowerVAphase3 = _ImPM2Power1OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 67),
    _ImPM2Power1OutputPowerVAphase3_Type()
)
imPM2Power1OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerVAphase3.setUnits("VA")
_ImPM2Power1OutputPowerKVAphase3_Type = Integer32
_ImPM2Power1OutputPowerKVAphase3_Object = MibScalar
imPM2Power1OutputPowerKVAphase3 = _ImPM2Power1OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 3, 68),
    _ImPM2Power1OutputPowerKVAphase3_Type()
)
imPM2Power1OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power1OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM2Power2_ObjectIdentity = ObjectIdentity
imPM2Power2 = _ImPM2Power2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4)
)


class _ImPM2Power2Manufacturer_Type(DisplayString):
    """Custom type imPM2Power2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM2Power2Manufacturer_Type.__name__ = "DisplayString"
_ImPM2Power2Manufacturer_Object = MibScalar
imPM2Power2Manufacturer = _ImPM2Power2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 1),
    _ImPM2Power2Manufacturer_Type()
)
imPM2Power2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Manufacturer.setStatus("current")


class _ImPM2Power2Type_Type(DisplayString):
    """Custom type imPM2Power2Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power2Type_Type.__name__ = "DisplayString"
_ImPM2Power2Type_Object = MibScalar
imPM2Power2Type = _ImPM2Power2Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 2),
    _ImPM2Power2Type_Type()
)
imPM2Power2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Type.setStatus("current")


class _ImPM2Power2serNumb_Type(DisplayString):
    """Custom type imPM2Power2serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power2serNumb_Type.__name__ = "DisplayString"
_ImPM2Power2serNumb_Object = MibScalar
imPM2Power2serNumb = _ImPM2Power2serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 3),
    _ImPM2Power2serNumb_Type()
)
imPM2Power2serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2serNumb.setStatus("current")


class _ImPM2Power2nextServiceDate_Type(DisplayString):
    """Custom type imPM2Power2nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power2nextServiceDate_Type.__name__ = "DisplayString"
_ImPM2Power2nextServiceDate_Object = MibScalar
imPM2Power2nextServiceDate = _ImPM2Power2nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 4),
    _ImPM2Power2nextServiceDate_Type()
)
imPM2Power2nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2nextServiceDate.setStatus("current")
_ImPM2Power2InputVoltage_Type = Integer32
_ImPM2Power2InputVoltage_Object = MibScalar
imPM2Power2InputVoltage = _ImPM2Power2InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 5),
    _ImPM2Power2InputVoltage_Type()
)
imPM2Power2InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputVoltage.setUnits("0.1 V")
_ImPM2Power2InputCurrent_Type = Integer32
_ImPM2Power2InputCurrent_Object = MibScalar
imPM2Power2InputCurrent = _ImPM2Power2InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 6),
    _ImPM2Power2InputCurrent_Type()
)
imPM2Power2InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputCurrent.setUnits("0.1 A")
_ImPM2Power2InputPowerVA_Type = Integer32
_ImPM2Power2InputPowerVA_Object = MibScalar
imPM2Power2InputPowerVA = _ImPM2Power2InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 7),
    _ImPM2Power2InputPowerVA_Type()
)
imPM2Power2InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerVA.setUnits("VA")
_ImPM2Power2InputPowerKVA_Type = Integer32
_ImPM2Power2InputPowerKVA_Object = MibScalar
imPM2Power2InputPowerKVA = _ImPM2Power2InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 8),
    _ImPM2Power2InputPowerKVA_Type()
)
imPM2Power2InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKVA.setUnits("0.1 kVA")
_ImPM2Power2InputPowerW_Type = Integer32
_ImPM2Power2InputPowerW_Object = MibScalar
imPM2Power2InputPowerW = _ImPM2Power2InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 9),
    _ImPM2Power2InputPowerW_Type()
)
imPM2Power2InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerW.setUnits("W")
_ImPM2Power2InputPowerKW_Type = Integer32
_ImPM2Power2InputPowerKW_Object = MibScalar
imPM2Power2InputPowerKW = _ImPM2Power2InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 10),
    _ImPM2Power2InputPowerKW_Type()
)
imPM2Power2InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKW.setUnits("0.1 kW")
_ImPM2Power2InputVoltagePhase1_Type = Integer32
_ImPM2Power2InputVoltagePhase1_Object = MibScalar
imPM2Power2InputVoltagePhase1 = _ImPM2Power2InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 11),
    _ImPM2Power2InputVoltagePhase1_Type()
)
imPM2Power2InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputVoltagePhase1.setUnits("0.1 V")
_ImPM2Power2InputCurrentPhase1_Type = Integer32
_ImPM2Power2InputCurrentPhase1_Object = MibScalar
imPM2Power2InputCurrentPhase1 = _ImPM2Power2InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 12),
    _ImPM2Power2InputCurrentPhase1_Type()
)
imPM2Power2InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputCurrentPhase1.setUnits("0.1 A")
_ImPM2Power2InputPowerVAphase1_Type = Integer32
_ImPM2Power2InputPowerVAphase1_Object = MibScalar
imPM2Power2InputPowerVAphase1 = _ImPM2Power2InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 13),
    _ImPM2Power2InputPowerVAphase1_Type()
)
imPM2Power2InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerVAphase1.setUnits("VA")
_ImPM2Power2InputPowerKVAphase1_Type = Integer32
_ImPM2Power2InputPowerKVAphase1_Object = MibScalar
imPM2Power2InputPowerKVAphase1 = _ImPM2Power2InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 14),
    _ImPM2Power2InputPowerKVAphase1_Type()
)
imPM2Power2InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM2Power2InputVoltagePhase2_Type = Integer32
_ImPM2Power2InputVoltagePhase2_Object = MibScalar
imPM2Power2InputVoltagePhase2 = _ImPM2Power2InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 15),
    _ImPM2Power2InputVoltagePhase2_Type()
)
imPM2Power2InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputVoltagePhase2.setUnits("0.1 V")
_ImPM2Power2InputCurrentPhase2_Type = Integer32
_ImPM2Power2InputCurrentPhase2_Object = MibScalar
imPM2Power2InputCurrentPhase2 = _ImPM2Power2InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 16),
    _ImPM2Power2InputCurrentPhase2_Type()
)
imPM2Power2InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputCurrentPhase2.setUnits("0.1 A")
_ImPM2Power2InputPowerVAphase2_Type = Integer32
_ImPM2Power2InputPowerVAphase2_Object = MibScalar
imPM2Power2InputPowerVAphase2 = _ImPM2Power2InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 17),
    _ImPM2Power2InputPowerVAphase2_Type()
)
imPM2Power2InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerVAphase2.setUnits("VA")
_ImPM2Power2InputPowerKVAphase2_Type = Integer32
_ImPM2Power2InputPowerKVAphase2_Object = MibScalar
imPM2Power2InputPowerKVAphase2 = _ImPM2Power2InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 18),
    _ImPM2Power2InputPowerKVAphase2_Type()
)
imPM2Power2InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM2Power2InputVoltagePhase3_Type = Integer32
_ImPM2Power2InputVoltagePhase3_Object = MibScalar
imPM2Power2InputVoltagePhase3 = _ImPM2Power2InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 19),
    _ImPM2Power2InputVoltagePhase3_Type()
)
imPM2Power2InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputVoltagePhase3.setUnits("0.1 V")
_ImPM2Power2InputCurrentPhase3_Type = Integer32
_ImPM2Power2InputCurrentPhase3_Object = MibScalar
imPM2Power2InputCurrentPhase3 = _ImPM2Power2InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 20),
    _ImPM2Power2InputCurrentPhase3_Type()
)
imPM2Power2InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputCurrentPhase3.setUnits("0.1 A")
_ImPM2Power2InputPowerVAphase3_Type = Integer32
_ImPM2Power2InputPowerVAphase3_Object = MibScalar
imPM2Power2InputPowerVAphase3 = _ImPM2Power2InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 21),
    _ImPM2Power2InputPowerVAphase3_Type()
)
imPM2Power2InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerVAphase3.setUnits("VA")
_ImPM2Power2InputPowerKVAphase3_Type = Integer32
_ImPM2Power2InputPowerKVAphase3_Object = MibScalar
imPM2Power2InputPowerKVAphase3 = _ImPM2Power2InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 22),
    _ImPM2Power2InputPowerKVAphase3_Type()
)
imPM2Power2InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM2Power2OutputVoltage_Type = Integer32
_ImPM2Power2OutputVoltage_Object = MibScalar
imPM2Power2OutputVoltage = _ImPM2Power2OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 23),
    _ImPM2Power2OutputVoltage_Type()
)
imPM2Power2OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputVoltage.setUnits("0.1 V")
_ImPM2Power2OutputCurrent_Type = Integer32
_ImPM2Power2OutputCurrent_Object = MibScalar
imPM2Power2OutputCurrent = _ImPM2Power2OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 24),
    _ImPM2Power2OutputCurrent_Type()
)
imPM2Power2OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputCurrent.setUnits("0.1 A")
_ImPM2Power2OutputPowerVA_Type = Integer32
_ImPM2Power2OutputPowerVA_Object = MibScalar
imPM2Power2OutputPowerVA = _ImPM2Power2OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 25),
    _ImPM2Power2OutputPowerVA_Type()
)
imPM2Power2OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerVA.setUnits("VA")
_ImPM2Power2OutputPowerKVA_Type = Integer32
_ImPM2Power2OutputPowerKVA_Object = MibScalar
imPM2Power2OutputPowerKVA = _ImPM2Power2OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 26),
    _ImPM2Power2OutputPowerKVA_Type()
)
imPM2Power2OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKVA.setUnits("0.1 kVA")
_ImPM2Power2OutputPowerW_Type = Integer32
_ImPM2Power2OutputPowerW_Object = MibScalar
imPM2Power2OutputPowerW = _ImPM2Power2OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 27),
    _ImPM2Power2OutputPowerW_Type()
)
imPM2Power2OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerW.setUnits("W")
_ImPM2Power2OutputPowerKW_Type = Integer32
_ImPM2Power2OutputPowerKW_Object = MibScalar
imPM2Power2OutputPowerKW = _ImPM2Power2OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 28),
    _ImPM2Power2OutputPowerKW_Type()
)
imPM2Power2OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKW.setUnits("0.1 kW")
_ImPM2Power2OutputLoad_Type = Integer32
_ImPM2Power2OutputLoad_Object = MibScalar
imPM2Power2OutputLoad = _ImPM2Power2OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 29),
    _ImPM2Power2OutputLoad_Type()
)
imPM2Power2OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputLoad.setUnits("%")
_ImPM2Power2OutputFrequency_Type = NonNegativeInteger
_ImPM2Power2OutputFrequency_Object = MibScalar
imPM2Power2OutputFrequency = _ImPM2Power2OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 30),
    _ImPM2Power2OutputFrequency_Type()
)
imPM2Power2OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputFrequency.setUnits("0.1 Hz")
_ImPM2Power2Temperature_Type = Integer32
_ImPM2Power2Temperature_Object = MibScalar
imPM2Power2Temperature = _ImPM2Power2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 31),
    _ImPM2Power2Temperature_Type()
)
imPM2Power2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2Temperature.setUnits("degrees Centigrade")


class _ImPM2Power2Running1_Type(Integer32):
    """Custom type imPM2Power2Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Running1_Type.__name__ = "Integer32"
_ImPM2Power2Running1_Object = MibScalar
imPM2Power2Running1 = _ImPM2Power2Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 32),
    _ImPM2Power2Running1_Type()
)
imPM2Power2Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Running1.setStatus("current")


class _ImPM2Power2Running2_Type(Integer32):
    """Custom type imPM2Power2Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Running2_Type.__name__ = "Integer32"
_ImPM2Power2Running2_Object = MibScalar
imPM2Power2Running2 = _ImPM2Power2Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 33),
    _ImPM2Power2Running2_Type()
)
imPM2Power2Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Running2.setStatus("current")


class _ImPM2Power2Running3_Type(Integer32):
    """Custom type imPM2Power2Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Running3_Type.__name__ = "Integer32"
_ImPM2Power2Running3_Object = MibScalar
imPM2Power2Running3 = _ImPM2Power2Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 34),
    _ImPM2Power2Running3_Type()
)
imPM2Power2Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Running3.setStatus("current")


class _ImPM2Power2Running4_Type(Integer32):
    """Custom type imPM2Power2Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Running4_Type.__name__ = "Integer32"
_ImPM2Power2Running4_Object = MibScalar
imPM2Power2Running4 = _ImPM2Power2Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 35),
    _ImPM2Power2Running4_Type()
)
imPM2Power2Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Running4.setStatus("current")


class _ImPM2Power2Running5_Type(Integer32):
    """Custom type imPM2Power2Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Running5_Type.__name__ = "Integer32"
_ImPM2Power2Running5_Object = MibScalar
imPM2Power2Running5 = _ImPM2Power2Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 36),
    _ImPM2Power2Running5_Type()
)
imPM2Power2Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Running5.setStatus("current")


class _ImPM2Power2Running6_Type(Integer32):
    """Custom type imPM2Power2Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Running6_Type.__name__ = "Integer32"
_ImPM2Power2Running6_Object = MibScalar
imPM2Power2Running6 = _ImPM2Power2Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 37),
    _ImPM2Power2Running6_Type()
)
imPM2Power2Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Running6.setStatus("current")


class _ImPM2Power2Running7_Type(Integer32):
    """Custom type imPM2Power2Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Running7_Type.__name__ = "Integer32"
_ImPM2Power2Running7_Object = MibScalar
imPM2Power2Running7 = _ImPM2Power2Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 38),
    _ImPM2Power2Running7_Type()
)
imPM2Power2Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Running7.setStatus("current")


class _ImPM2Power2Running8_Type(Integer32):
    """Custom type imPM2Power2Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Running8_Type.__name__ = "Integer32"
_ImPM2Power2Running8_Object = MibScalar
imPM2Power2Running8 = _ImPM2Power2Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 39),
    _ImPM2Power2Running8_Type()
)
imPM2Power2Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Running8.setStatus("current")


class _ImPM2Power2InputFuse_Type(Integer32):
    """Custom type imPM2Power2InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputFuse_Type.__name__ = "Integer32"
_ImPM2Power2InputFuse_Object = MibScalar
imPM2Power2InputFuse = _ImPM2Power2InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 40),
    _ImPM2Power2InputFuse_Type()
)
imPM2Power2InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputFuse.setStatus("current")


class _ImPM2Power2InputFuse1_Type(Integer32):
    """Custom type imPM2Power2InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputFuse1_Type.__name__ = "Integer32"
_ImPM2Power2InputFuse1_Object = MibScalar
imPM2Power2InputFuse1 = _ImPM2Power2InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 41),
    _ImPM2Power2InputFuse1_Type()
)
imPM2Power2InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputFuse1.setStatus("current")


class _ImPM2Power2InputFuse2_Type(Integer32):
    """Custom type imPM2Power2InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputFuse2_Type.__name__ = "Integer32"
_ImPM2Power2InputFuse2_Object = MibScalar
imPM2Power2InputFuse2 = _ImPM2Power2InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 42),
    _ImPM2Power2InputFuse2_Type()
)
imPM2Power2InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputFuse2.setStatus("current")


class _ImPM2Power2InputFuse3_Type(Integer32):
    """Custom type imPM2Power2InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputFuse3_Type.__name__ = "Integer32"
_ImPM2Power2InputFuse3_Object = MibScalar
imPM2Power2InputFuse3 = _ImPM2Power2InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 43),
    _ImPM2Power2InputFuse3_Type()
)
imPM2Power2InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputFuse3.setStatus("current")


class _ImPM2Power2InputBreaker_Type(Integer32):
    """Custom type imPM2Power2InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputBreaker_Type.__name__ = "Integer32"
_ImPM2Power2InputBreaker_Object = MibScalar
imPM2Power2InputBreaker = _ImPM2Power2InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 44),
    _ImPM2Power2InputBreaker_Type()
)
imPM2Power2InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputBreaker.setStatus("current")


class _ImPM2Power2InputBreaker1_Type(Integer32):
    """Custom type imPM2Power2InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputBreaker1_Type.__name__ = "Integer32"
_ImPM2Power2InputBreaker1_Object = MibScalar
imPM2Power2InputBreaker1 = _ImPM2Power2InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 45),
    _ImPM2Power2InputBreaker1_Type()
)
imPM2Power2InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputBreaker1.setStatus("current")


class _ImPM2Power2InputBreaker2_Type(Integer32):
    """Custom type imPM2Power2InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputBreaker2_Type.__name__ = "Integer32"
_ImPM2Power2InputBreaker2_Object = MibScalar
imPM2Power2InputBreaker2 = _ImPM2Power2InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 46),
    _ImPM2Power2InputBreaker2_Type()
)
imPM2Power2InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputBreaker2.setStatus("current")


class _ImPM2Power2InputBreaker3_Type(Integer32):
    """Custom type imPM2Power2InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputBreaker3_Type.__name__ = "Integer32"
_ImPM2Power2InputBreaker3_Object = MibScalar
imPM2Power2InputBreaker3 = _ImPM2Power2InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 47),
    _ImPM2Power2InputBreaker3_Type()
)
imPM2Power2InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputBreaker3.setStatus("current")


class _ImPM2Power2InputSurgeArrester_Type(Integer32):
    """Custom type imPM2Power2InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM2Power2InputSurgeArrester_Object = MibScalar
imPM2Power2InputSurgeArrester = _ImPM2Power2InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 48),
    _ImPM2Power2InputSurgeArrester_Type()
)
imPM2Power2InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2InputSurgeArrester.setStatus("current")


class _ImPM2Power2OutputFuse_Type(Integer32):
    """Custom type imPM2Power2OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2OutputFuse_Type.__name__ = "Integer32"
_ImPM2Power2OutputFuse_Object = MibScalar
imPM2Power2OutputFuse = _ImPM2Power2OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 49),
    _ImPM2Power2OutputFuse_Type()
)
imPM2Power2OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputFuse.setStatus("current")


class _ImPM2Power2OutputFuse1_Type(Integer32):
    """Custom type imPM2Power2OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2OutputFuse1_Type.__name__ = "Integer32"
_ImPM2Power2OutputFuse1_Object = MibScalar
imPM2Power2OutputFuse1 = _ImPM2Power2OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 50),
    _ImPM2Power2OutputFuse1_Type()
)
imPM2Power2OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputFuse1.setStatus("current")


class _ImPM2Power2OutputFuse2_Type(Integer32):
    """Custom type imPM2Power2OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2OutputFuse2_Type.__name__ = "Integer32"
_ImPM2Power2OutputFuse2_Object = MibScalar
imPM2Power2OutputFuse2 = _ImPM2Power2OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 51),
    _ImPM2Power2OutputFuse2_Type()
)
imPM2Power2OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputFuse2.setStatus("current")


class _ImPM2Power2OutputBreaker_Type(Integer32):
    """Custom type imPM2Power2OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2OutputBreaker_Type.__name__ = "Integer32"
_ImPM2Power2OutputBreaker_Object = MibScalar
imPM2Power2OutputBreaker = _ImPM2Power2OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 52),
    _ImPM2Power2OutputBreaker_Type()
)
imPM2Power2OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputBreaker.setStatus("current")


class _ImPM2Power2OutputBreaker1_Type(Integer32):
    """Custom type imPM2Power2OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2OutputBreaker1_Type.__name__ = "Integer32"
_ImPM2Power2OutputBreaker1_Object = MibScalar
imPM2Power2OutputBreaker1 = _ImPM2Power2OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 53),
    _ImPM2Power2OutputBreaker1_Type()
)
imPM2Power2OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputBreaker1.setStatus("current")


class _ImPM2Power2OutputBreaker2_Type(Integer32):
    """Custom type imPM2Power2OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2OutputBreaker2_Type.__name__ = "Integer32"
_ImPM2Power2OutputBreaker2_Object = MibScalar
imPM2Power2OutputBreaker2 = _ImPM2Power2OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 54),
    _ImPM2Power2OutputBreaker2_Type()
)
imPM2Power2OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputBreaker2.setStatus("current")


class _ImPM2Power2Fan_Type(Integer32):
    """Custom type imPM2Power2Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2Fan_Type.__name__ = "Integer32"
_ImPM2Power2Fan_Object = MibScalar
imPM2Power2Fan = _ImPM2Power2Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 55),
    _ImPM2Power2Fan_Type()
)
imPM2Power2Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2Fan.setStatus("current")


class _ImPM2Power2BatteryAvailable_Type(Integer32):
    """Custom type imPM2Power2BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power2BatteryAvailable_Type.__name__ = "Integer32"
_ImPM2Power2BatteryAvailable_Object = MibScalar
imPM2Power2BatteryAvailable = _ImPM2Power2BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 56),
    _ImPM2Power2BatteryAvailable_Type()
)
imPM2Power2BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2BatteryAvailable.setStatus("current")
_ImPM2Power2OutputVoltagePhase1_Type = Integer32
_ImPM2Power2OutputVoltagePhase1_Object = MibScalar
imPM2Power2OutputVoltagePhase1 = _ImPM2Power2OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 57),
    _ImPM2Power2OutputVoltagePhase1_Type()
)
imPM2Power2OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputVoltagePhase1.setUnits("0.1 V")
_ImPM2Power2OutputCurrentPhase1_Type = Integer32
_ImPM2Power2OutputCurrentPhase1_Object = MibScalar
imPM2Power2OutputCurrentPhase1 = _ImPM2Power2OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 58),
    _ImPM2Power2OutputCurrentPhase1_Type()
)
imPM2Power2OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputCurrentPhase1.setUnits("0.1 A")
_ImPM2Power2OutputPowerVAphase1_Type = Integer32
_ImPM2Power2OutputPowerVAphase1_Object = MibScalar
imPM2Power2OutputPowerVAphase1 = _ImPM2Power2OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 59),
    _ImPM2Power2OutputPowerVAphase1_Type()
)
imPM2Power2OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerVAphase1.setUnits("VA")
_ImPM2Power2OutputPowerKVAphase1_Type = Integer32
_ImPM2Power2OutputPowerKVAphase1_Object = MibScalar
imPM2Power2OutputPowerKVAphase1 = _ImPM2Power2OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 60),
    _ImPM2Power2OutputPowerKVAphase1_Type()
)
imPM2Power2OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM2Power2OutputVoltagePhase2_Type = Integer32
_ImPM2Power2OutputVoltagePhase2_Object = MibScalar
imPM2Power2OutputVoltagePhase2 = _ImPM2Power2OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 61),
    _ImPM2Power2OutputVoltagePhase2_Type()
)
imPM2Power2OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputVoltagePhase2.setUnits("0.1 V")
_ImPM2Power2OutputCurrentPhase2_Type = Integer32
_ImPM2Power2OutputCurrentPhase2_Object = MibScalar
imPM2Power2OutputCurrentPhase2 = _ImPM2Power2OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 62),
    _ImPM2Power2OutputCurrentPhase2_Type()
)
imPM2Power2OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputCurrentPhase2.setUnits("0.1 A")
_ImPM2Power2OutputPowerVAphase2_Type = Integer32
_ImPM2Power2OutputPowerVAphase2_Object = MibScalar
imPM2Power2OutputPowerVAphase2 = _ImPM2Power2OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 63),
    _ImPM2Power2OutputPowerVAphase2_Type()
)
imPM2Power2OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerVAphase2.setUnits("VA")
_ImPM2Power2OutputPowerKVAphase2_Type = Integer32
_ImPM2Power2OutputPowerKVAphase2_Object = MibScalar
imPM2Power2OutputPowerKVAphase2 = _ImPM2Power2OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 64),
    _ImPM2Power2OutputPowerKVAphase2_Type()
)
imPM2Power2OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM2Power2OutputVoltagePhase3_Type = Integer32
_ImPM2Power2OutputVoltagePhase3_Object = MibScalar
imPM2Power2OutputVoltagePhase3 = _ImPM2Power2OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 65),
    _ImPM2Power2OutputVoltagePhase3_Type()
)
imPM2Power2OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputVoltagePhase3.setUnits("0.1 V")
_ImPM2Power2OutputCurrentPhase3_Type = Integer32
_ImPM2Power2OutputCurrentPhase3_Object = MibScalar
imPM2Power2OutputCurrentPhase3 = _ImPM2Power2OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 66),
    _ImPM2Power2OutputCurrentPhase3_Type()
)
imPM2Power2OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputCurrentPhase3.setUnits("0.1 A")
_ImPM2Power2OutputPowerVAphase3_Type = Integer32
_ImPM2Power2OutputPowerVAphase3_Object = MibScalar
imPM2Power2OutputPowerVAphase3 = _ImPM2Power2OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 67),
    _ImPM2Power2OutputPowerVAphase3_Type()
)
imPM2Power2OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerVAphase3.setUnits("VA")
_ImPM2Power2OutputPowerKVAphase3_Type = Integer32
_ImPM2Power2OutputPowerKVAphase3_Object = MibScalar
imPM2Power2OutputPowerKVAphase3 = _ImPM2Power2OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 4, 68),
    _ImPM2Power2OutputPowerKVAphase3_Type()
)
imPM2Power2OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power2OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM2Power3_ObjectIdentity = ObjectIdentity
imPM2Power3 = _ImPM2Power3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5)
)


class _ImPM2Power3Manufacturer_Type(DisplayString):
    """Custom type imPM2Power3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM2Power3Manufacturer_Type.__name__ = "DisplayString"
_ImPM2Power3Manufacturer_Object = MibScalar
imPM2Power3Manufacturer = _ImPM2Power3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 1),
    _ImPM2Power3Manufacturer_Type()
)
imPM2Power3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Manufacturer.setStatus("current")


class _ImPM2Power3Type_Type(DisplayString):
    """Custom type imPM2Power3Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power3Type_Type.__name__ = "DisplayString"
_ImPM2Power3Type_Object = MibScalar
imPM2Power3Type = _ImPM2Power3Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 2),
    _ImPM2Power3Type_Type()
)
imPM2Power3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Type.setStatus("current")


class _ImPM2Power3serNumb_Type(DisplayString):
    """Custom type imPM2Power3serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power3serNumb_Type.__name__ = "DisplayString"
_ImPM2Power3serNumb_Object = MibScalar
imPM2Power3serNumb = _ImPM2Power3serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 3),
    _ImPM2Power3serNumb_Type()
)
imPM2Power3serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3serNumb.setStatus("current")


class _ImPM2Power3nextServiceDate_Type(DisplayString):
    """Custom type imPM2Power3nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2Power3nextServiceDate_Type.__name__ = "DisplayString"
_ImPM2Power3nextServiceDate_Object = MibScalar
imPM2Power3nextServiceDate = _ImPM2Power3nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 4),
    _ImPM2Power3nextServiceDate_Type()
)
imPM2Power3nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3nextServiceDate.setStatus("current")
_ImPM2Power3InputVoltage_Type = Integer32
_ImPM2Power3InputVoltage_Object = MibScalar
imPM2Power3InputVoltage = _ImPM2Power3InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 5),
    _ImPM2Power3InputVoltage_Type()
)
imPM2Power3InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputVoltage.setUnits("0.1 V")
_ImPM2Power3InputCurrent_Type = Integer32
_ImPM2Power3InputCurrent_Object = MibScalar
imPM2Power3InputCurrent = _ImPM2Power3InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 6),
    _ImPM2Power3InputCurrent_Type()
)
imPM2Power3InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputCurrent.setUnits("0.1 A")
_ImPM2Power3InputPowerVA_Type = Integer32
_ImPM2Power3InputPowerVA_Object = MibScalar
imPM2Power3InputPowerVA = _ImPM2Power3InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 7),
    _ImPM2Power3InputPowerVA_Type()
)
imPM2Power3InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerVA.setUnits("VA")
_ImPM2Power3InputPowerKVA_Type = Integer32
_ImPM2Power3InputPowerKVA_Object = MibScalar
imPM2Power3InputPowerKVA = _ImPM2Power3InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 8),
    _ImPM2Power3InputPowerKVA_Type()
)
imPM2Power3InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKVA.setUnits("0.1 kVA")
_ImPM2Power3InputPowerW_Type = Integer32
_ImPM2Power3InputPowerW_Object = MibScalar
imPM2Power3InputPowerW = _ImPM2Power3InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 9),
    _ImPM2Power3InputPowerW_Type()
)
imPM2Power3InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerW.setUnits("W")
_ImPM2Power3InputPowerKW_Type = Integer32
_ImPM2Power3InputPowerKW_Object = MibScalar
imPM2Power3InputPowerKW = _ImPM2Power3InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 10),
    _ImPM2Power3InputPowerKW_Type()
)
imPM2Power3InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKW.setUnits("0.1 kW")
_ImPM2Power3InputVoltagePhase1_Type = Integer32
_ImPM2Power3InputVoltagePhase1_Object = MibScalar
imPM2Power3InputVoltagePhase1 = _ImPM2Power3InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 11),
    _ImPM2Power3InputVoltagePhase1_Type()
)
imPM2Power3InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputVoltagePhase1.setUnits("0.1 V")
_ImPM2Power3InputCurrentPhase1_Type = Integer32
_ImPM2Power3InputCurrentPhase1_Object = MibScalar
imPM2Power3InputCurrentPhase1 = _ImPM2Power3InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 12),
    _ImPM2Power3InputCurrentPhase1_Type()
)
imPM2Power3InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputCurrentPhase1.setUnits("0.1 A")
_ImPM2Power3InputPowerVAphase1_Type = Integer32
_ImPM2Power3InputPowerVAphase1_Object = MibScalar
imPM2Power3InputPowerVAphase1 = _ImPM2Power3InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 13),
    _ImPM2Power3InputPowerVAphase1_Type()
)
imPM2Power3InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerVAphase1.setUnits("VA")
_ImPM2Power3InputPowerKVAphase1_Type = Integer32
_ImPM2Power3InputPowerKVAphase1_Object = MibScalar
imPM2Power3InputPowerKVAphase1 = _ImPM2Power3InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 14),
    _ImPM2Power3InputPowerKVAphase1_Type()
)
imPM2Power3InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM2Power3InputVoltagePhase2_Type = Integer32
_ImPM2Power3InputVoltagePhase2_Object = MibScalar
imPM2Power3InputVoltagePhase2 = _ImPM2Power3InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 15),
    _ImPM2Power3InputVoltagePhase2_Type()
)
imPM2Power3InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputVoltagePhase2.setUnits("0.1 V")
_ImPM2Power3InputCurrentPhase2_Type = Integer32
_ImPM2Power3InputCurrentPhase2_Object = MibScalar
imPM2Power3InputCurrentPhase2 = _ImPM2Power3InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 16),
    _ImPM2Power3InputCurrentPhase2_Type()
)
imPM2Power3InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputCurrentPhase2.setUnits("0.1 A")
_ImPM2Power3InputPowerVAphase2_Type = Integer32
_ImPM2Power3InputPowerVAphase2_Object = MibScalar
imPM2Power3InputPowerVAphase2 = _ImPM2Power3InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 17),
    _ImPM2Power3InputPowerVAphase2_Type()
)
imPM2Power3InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerVAphase2.setUnits("VA")
_ImPM2Power3InputPowerKVAphase2_Type = Integer32
_ImPM2Power3InputPowerKVAphase2_Object = MibScalar
imPM2Power3InputPowerKVAphase2 = _ImPM2Power3InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 18),
    _ImPM2Power3InputPowerKVAphase2_Type()
)
imPM2Power3InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM2Power3InputVoltagePhase3_Type = Integer32
_ImPM2Power3InputVoltagePhase3_Object = MibScalar
imPM2Power3InputVoltagePhase3 = _ImPM2Power3InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 19),
    _ImPM2Power3InputVoltagePhase3_Type()
)
imPM2Power3InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputVoltagePhase3.setUnits("0.1 V")
_ImPM2Power3InputCurrentPhase3_Type = Integer32
_ImPM2Power3InputCurrentPhase3_Object = MibScalar
imPM2Power3InputCurrentPhase3 = _ImPM2Power3InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 20),
    _ImPM2Power3InputCurrentPhase3_Type()
)
imPM2Power3InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputCurrentPhase3.setUnits("0.1 A")
_ImPM2Power3InputPowerVAphase3_Type = Integer32
_ImPM2Power3InputPowerVAphase3_Object = MibScalar
imPM2Power3InputPowerVAphase3 = _ImPM2Power3InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 21),
    _ImPM2Power3InputPowerVAphase3_Type()
)
imPM2Power3InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerVAphase3.setUnits("VA")
_ImPM2Power3InputPowerKVAphase3_Type = Integer32
_ImPM2Power3InputPowerKVAphase3_Object = MibScalar
imPM2Power3InputPowerKVAphase3 = _ImPM2Power3InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 22),
    _ImPM2Power3InputPowerKVAphase3_Type()
)
imPM2Power3InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM2Power3OutputVoltage_Type = Integer32
_ImPM2Power3OutputVoltage_Object = MibScalar
imPM2Power3OutputVoltage = _ImPM2Power3OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 23),
    _ImPM2Power3OutputVoltage_Type()
)
imPM2Power3OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputVoltage.setUnits("0.1 V")
_ImPM2Power3OutputCurrent_Type = Integer32
_ImPM2Power3OutputCurrent_Object = MibScalar
imPM2Power3OutputCurrent = _ImPM2Power3OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 24),
    _ImPM2Power3OutputCurrent_Type()
)
imPM2Power3OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputCurrent.setUnits("0.1 A")
_ImPM2Power3OutputPowerVA_Type = Integer32
_ImPM2Power3OutputPowerVA_Object = MibScalar
imPM2Power3OutputPowerVA = _ImPM2Power3OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 25),
    _ImPM2Power3OutputPowerVA_Type()
)
imPM2Power3OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerVA.setUnits("VA")
_ImPM2Power3OutputPowerKVA_Type = Integer32
_ImPM2Power3OutputPowerKVA_Object = MibScalar
imPM2Power3OutputPowerKVA = _ImPM2Power3OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 26),
    _ImPM2Power3OutputPowerKVA_Type()
)
imPM2Power3OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKVA.setUnits("0.1 kVA")
_ImPM2Power3OutputPowerW_Type = Integer32
_ImPM2Power3OutputPowerW_Object = MibScalar
imPM2Power3OutputPowerW = _ImPM2Power3OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 27),
    _ImPM2Power3OutputPowerW_Type()
)
imPM2Power3OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerW.setUnits("W")
_ImPM2Power3OutputPowerKW_Type = Integer32
_ImPM2Power3OutputPowerKW_Object = MibScalar
imPM2Power3OutputPowerKW = _ImPM2Power3OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 28),
    _ImPM2Power3OutputPowerKW_Type()
)
imPM2Power3OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKW.setUnits("0.1 kW")
_ImPM2Power3OutputLoad_Type = Integer32
_ImPM2Power3OutputLoad_Object = MibScalar
imPM2Power3OutputLoad = _ImPM2Power3OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 29),
    _ImPM2Power3OutputLoad_Type()
)
imPM2Power3OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputLoad.setUnits("%")
_ImPM2Power3OutputFrequency_Type = NonNegativeInteger
_ImPM2Power3OutputFrequency_Object = MibScalar
imPM2Power3OutputFrequency = _ImPM2Power3OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 30),
    _ImPM2Power3OutputFrequency_Type()
)
imPM2Power3OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputFrequency.setUnits("0.1 Hz")
_ImPM2Power3Temperature_Type = Integer32
_ImPM2Power3Temperature_Object = MibScalar
imPM2Power3Temperature = _ImPM2Power3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 31),
    _ImPM2Power3Temperature_Type()
)
imPM2Power3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3Temperature.setUnits("degrees Centigrade")


class _ImPM2Power3Running1_Type(Integer32):
    """Custom type imPM2Power3Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Running1_Type.__name__ = "Integer32"
_ImPM2Power3Running1_Object = MibScalar
imPM2Power3Running1 = _ImPM2Power3Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 32),
    _ImPM2Power3Running1_Type()
)
imPM2Power3Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Running1.setStatus("current")


class _ImPM2Power3Running2_Type(Integer32):
    """Custom type imPM2Power3Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Running2_Type.__name__ = "Integer32"
_ImPM2Power3Running2_Object = MibScalar
imPM2Power3Running2 = _ImPM2Power3Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 33),
    _ImPM2Power3Running2_Type()
)
imPM2Power3Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Running2.setStatus("current")


class _ImPM2Power3Running3_Type(Integer32):
    """Custom type imPM2Power3Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Running3_Type.__name__ = "Integer32"
_ImPM2Power3Running3_Object = MibScalar
imPM2Power3Running3 = _ImPM2Power3Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 34),
    _ImPM2Power3Running3_Type()
)
imPM2Power3Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Running3.setStatus("current")


class _ImPM2Power3Running4_Type(Integer32):
    """Custom type imPM2Power3Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Running4_Type.__name__ = "Integer32"
_ImPM2Power3Running4_Object = MibScalar
imPM2Power3Running4 = _ImPM2Power3Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 35),
    _ImPM2Power3Running4_Type()
)
imPM2Power3Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Running4.setStatus("current")


class _ImPM2Power3Running5_Type(Integer32):
    """Custom type imPM2Power3Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Running5_Type.__name__ = "Integer32"
_ImPM2Power3Running5_Object = MibScalar
imPM2Power3Running5 = _ImPM2Power3Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 36),
    _ImPM2Power3Running5_Type()
)
imPM2Power3Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Running5.setStatus("current")


class _ImPM2Power3Running6_Type(Integer32):
    """Custom type imPM2Power3Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Running6_Type.__name__ = "Integer32"
_ImPM2Power3Running6_Object = MibScalar
imPM2Power3Running6 = _ImPM2Power3Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 37),
    _ImPM2Power3Running6_Type()
)
imPM2Power3Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Running6.setStatus("current")


class _ImPM2Power3Running7_Type(Integer32):
    """Custom type imPM2Power3Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Running7_Type.__name__ = "Integer32"
_ImPM2Power3Running7_Object = MibScalar
imPM2Power3Running7 = _ImPM2Power3Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 38),
    _ImPM2Power3Running7_Type()
)
imPM2Power3Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Running7.setStatus("current")


class _ImPM2Power3Running8_Type(Integer32):
    """Custom type imPM2Power3Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Running8_Type.__name__ = "Integer32"
_ImPM2Power3Running8_Object = MibScalar
imPM2Power3Running8 = _ImPM2Power3Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 39),
    _ImPM2Power3Running8_Type()
)
imPM2Power3Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Running8.setStatus("current")


class _ImPM2Power3InputFuse_Type(Integer32):
    """Custom type imPM2Power3InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputFuse_Type.__name__ = "Integer32"
_ImPM2Power3InputFuse_Object = MibScalar
imPM2Power3InputFuse = _ImPM2Power3InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 40),
    _ImPM2Power3InputFuse_Type()
)
imPM2Power3InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputFuse.setStatus("current")


class _ImPM2Power3InputFuse1_Type(Integer32):
    """Custom type imPM2Power3InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputFuse1_Type.__name__ = "Integer32"
_ImPM2Power3InputFuse1_Object = MibScalar
imPM2Power3InputFuse1 = _ImPM2Power3InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 41),
    _ImPM2Power3InputFuse1_Type()
)
imPM2Power3InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputFuse1.setStatus("current")


class _ImPM2Power3InputFuse2_Type(Integer32):
    """Custom type imPM2Power3InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputFuse2_Type.__name__ = "Integer32"
_ImPM2Power3InputFuse2_Object = MibScalar
imPM2Power3InputFuse2 = _ImPM2Power3InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 42),
    _ImPM2Power3InputFuse2_Type()
)
imPM2Power3InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputFuse2.setStatus("current")


class _ImPM2Power3InputFuse3_Type(Integer32):
    """Custom type imPM2Power3InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputFuse3_Type.__name__ = "Integer32"
_ImPM2Power3InputFuse3_Object = MibScalar
imPM2Power3InputFuse3 = _ImPM2Power3InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 43),
    _ImPM2Power3InputFuse3_Type()
)
imPM2Power3InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputFuse3.setStatus("current")


class _ImPM2Power3InputBreaker_Type(Integer32):
    """Custom type imPM2Power3InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputBreaker_Type.__name__ = "Integer32"
_ImPM2Power3InputBreaker_Object = MibScalar
imPM2Power3InputBreaker = _ImPM2Power3InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 44),
    _ImPM2Power3InputBreaker_Type()
)
imPM2Power3InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputBreaker.setStatus("current")


class _ImPM2Power3InputBreaker1_Type(Integer32):
    """Custom type imPM2Power3InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputBreaker1_Type.__name__ = "Integer32"
_ImPM2Power3InputBreaker1_Object = MibScalar
imPM2Power3InputBreaker1 = _ImPM2Power3InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 45),
    _ImPM2Power3InputBreaker1_Type()
)
imPM2Power3InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputBreaker1.setStatus("current")


class _ImPM2Power3InputBreaker2_Type(Integer32):
    """Custom type imPM2Power3InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputBreaker2_Type.__name__ = "Integer32"
_ImPM2Power3InputBreaker2_Object = MibScalar
imPM2Power3InputBreaker2 = _ImPM2Power3InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 46),
    _ImPM2Power3InputBreaker2_Type()
)
imPM2Power3InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputBreaker2.setStatus("current")


class _ImPM2Power3InputBreaker3_Type(Integer32):
    """Custom type imPM2Power3InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputBreaker3_Type.__name__ = "Integer32"
_ImPM2Power3InputBreaker3_Object = MibScalar
imPM2Power3InputBreaker3 = _ImPM2Power3InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 47),
    _ImPM2Power3InputBreaker3_Type()
)
imPM2Power3InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputBreaker3.setStatus("current")


class _ImPM2Power3InputSurgeArrester_Type(Integer32):
    """Custom type imPM2Power3InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM2Power3InputSurgeArrester_Object = MibScalar
imPM2Power3InputSurgeArrester = _ImPM2Power3InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 48),
    _ImPM2Power3InputSurgeArrester_Type()
)
imPM2Power3InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3InputSurgeArrester.setStatus("current")


class _ImPM2Power3OutputFuse_Type(Integer32):
    """Custom type imPM2Power3OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3OutputFuse_Type.__name__ = "Integer32"
_ImPM2Power3OutputFuse_Object = MibScalar
imPM2Power3OutputFuse = _ImPM2Power3OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 49),
    _ImPM2Power3OutputFuse_Type()
)
imPM2Power3OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputFuse.setStatus("current")


class _ImPM2Power3OutputFuse1_Type(Integer32):
    """Custom type imPM2Power3OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3OutputFuse1_Type.__name__ = "Integer32"
_ImPM2Power3OutputFuse1_Object = MibScalar
imPM2Power3OutputFuse1 = _ImPM2Power3OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 50),
    _ImPM2Power3OutputFuse1_Type()
)
imPM2Power3OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputFuse1.setStatus("current")


class _ImPM2Power3OutputFuse2_Type(Integer32):
    """Custom type imPM2Power3OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3OutputFuse2_Type.__name__ = "Integer32"
_ImPM2Power3OutputFuse2_Object = MibScalar
imPM2Power3OutputFuse2 = _ImPM2Power3OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 51),
    _ImPM2Power3OutputFuse2_Type()
)
imPM2Power3OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputFuse2.setStatus("current")


class _ImPM2Power3OutputBreaker_Type(Integer32):
    """Custom type imPM2Power3OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3OutputBreaker_Type.__name__ = "Integer32"
_ImPM2Power3OutputBreaker_Object = MibScalar
imPM2Power3OutputBreaker = _ImPM2Power3OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 52),
    _ImPM2Power3OutputBreaker_Type()
)
imPM2Power3OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputBreaker.setStatus("current")


class _ImPM2Power3OutputBreaker1_Type(Integer32):
    """Custom type imPM2Power3OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3OutputBreaker1_Type.__name__ = "Integer32"
_ImPM2Power3OutputBreaker1_Object = MibScalar
imPM2Power3OutputBreaker1 = _ImPM2Power3OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 53),
    _ImPM2Power3OutputBreaker1_Type()
)
imPM2Power3OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputBreaker1.setStatus("current")


class _ImPM2Power3OutputBreaker2_Type(Integer32):
    """Custom type imPM2Power3OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3OutputBreaker2_Type.__name__ = "Integer32"
_ImPM2Power3OutputBreaker2_Object = MibScalar
imPM2Power3OutputBreaker2 = _ImPM2Power3OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 54),
    _ImPM2Power3OutputBreaker2_Type()
)
imPM2Power3OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputBreaker2.setStatus("current")


class _ImPM2Power3Fan_Type(Integer32):
    """Custom type imPM2Power3Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3Fan_Type.__name__ = "Integer32"
_ImPM2Power3Fan_Object = MibScalar
imPM2Power3Fan = _ImPM2Power3Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 55),
    _ImPM2Power3Fan_Type()
)
imPM2Power3Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3Fan.setStatus("current")


class _ImPM2Power3BatteryAvailable_Type(Integer32):
    """Custom type imPM2Power3BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2Power3BatteryAvailable_Type.__name__ = "Integer32"
_ImPM2Power3BatteryAvailable_Object = MibScalar
imPM2Power3BatteryAvailable = _ImPM2Power3BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 56),
    _ImPM2Power3BatteryAvailable_Type()
)
imPM2Power3BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3BatteryAvailable.setStatus("current")
_ImPM2Power3OutputVoltagePhase1_Type = Integer32
_ImPM2Power3OutputVoltagePhase1_Object = MibScalar
imPM2Power3OutputVoltagePhase1 = _ImPM2Power3OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 57),
    _ImPM2Power3OutputVoltagePhase1_Type()
)
imPM2Power3OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputVoltagePhase1.setUnits("0.1 V")
_ImPM2Power3OutputCurrentPhase1_Type = Integer32
_ImPM2Power3OutputCurrentPhase1_Object = MibScalar
imPM2Power3OutputCurrentPhase1 = _ImPM2Power3OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 58),
    _ImPM2Power3OutputCurrentPhase1_Type()
)
imPM2Power3OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputCurrentPhase1.setUnits("0.1 A")
_ImPM2Power3OutputPowerVAphase1_Type = Integer32
_ImPM2Power3OutputPowerVAphase1_Object = MibScalar
imPM2Power3OutputPowerVAphase1 = _ImPM2Power3OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 59),
    _ImPM2Power3OutputPowerVAphase1_Type()
)
imPM2Power3OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerVAphase1.setUnits("VA")
_ImPM2Power3OutputPowerKVAphase1_Type = Integer32
_ImPM2Power3OutputPowerKVAphase1_Object = MibScalar
imPM2Power3OutputPowerKVAphase1 = _ImPM2Power3OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 60),
    _ImPM2Power3OutputPowerKVAphase1_Type()
)
imPM2Power3OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM2Power3OutputVoltagePhase2_Type = Integer32
_ImPM2Power3OutputVoltagePhase2_Object = MibScalar
imPM2Power3OutputVoltagePhase2 = _ImPM2Power3OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 61),
    _ImPM2Power3OutputVoltagePhase2_Type()
)
imPM2Power3OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputVoltagePhase2.setUnits("0.1 V")
_ImPM2Power3OutputCurrentPhase2_Type = Integer32
_ImPM2Power3OutputCurrentPhase2_Object = MibScalar
imPM2Power3OutputCurrentPhase2 = _ImPM2Power3OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 62),
    _ImPM2Power3OutputCurrentPhase2_Type()
)
imPM2Power3OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputCurrentPhase2.setUnits("0.1 A")
_ImPM2Power3OutputPowerVAphase2_Type = Integer32
_ImPM2Power3OutputPowerVAphase2_Object = MibScalar
imPM2Power3OutputPowerVAphase2 = _ImPM2Power3OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 63),
    _ImPM2Power3OutputPowerVAphase2_Type()
)
imPM2Power3OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerVAphase2.setUnits("VA")
_ImPM2Power3OutputPowerKVAphase2_Type = Integer32
_ImPM2Power3OutputPowerKVAphase2_Object = MibScalar
imPM2Power3OutputPowerKVAphase2 = _ImPM2Power3OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 64),
    _ImPM2Power3OutputPowerKVAphase2_Type()
)
imPM2Power3OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM2Power3OutputVoltagePhase3_Type = Integer32
_ImPM2Power3OutputVoltagePhase3_Object = MibScalar
imPM2Power3OutputVoltagePhase3 = _ImPM2Power3OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 65),
    _ImPM2Power3OutputVoltagePhase3_Type()
)
imPM2Power3OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputVoltagePhase3.setUnits("0.1 V")
_ImPM2Power3OutputCurrentPhase3_Type = Integer32
_ImPM2Power3OutputCurrentPhase3_Object = MibScalar
imPM2Power3OutputCurrentPhase3 = _ImPM2Power3OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 66),
    _ImPM2Power3OutputCurrentPhase3_Type()
)
imPM2Power3OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputCurrentPhase3.setUnits("0.1 A")
_ImPM2Power3OutputPowerVAphase3_Type = Integer32
_ImPM2Power3OutputPowerVAphase3_Object = MibScalar
imPM2Power3OutputPowerVAphase3 = _ImPM2Power3OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 67),
    _ImPM2Power3OutputPowerVAphase3_Type()
)
imPM2Power3OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerVAphase3.setUnits("VA")
_ImPM2Power3OutputPowerKVAphase3_Type = Integer32
_ImPM2Power3OutputPowerKVAphase3_Object = MibScalar
imPM2Power3OutputPowerKVAphase3 = _ImPM2Power3OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 5, 68),
    _ImPM2Power3OutputPowerKVAphase3_Type()
)
imPM2Power3OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM2Power3OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM2Battery_ObjectIdentity = ObjectIdentity
imPM2Battery = _ImPM2Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 6)
)
_ImPM2BatteryNominalCapacity_Type = NonNegativeInteger
_ImPM2BatteryNominalCapacity_Object = MibScalar
imPM2BatteryNominalCapacity = _ImPM2BatteryNominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 6, 1),
    _ImPM2BatteryNominalCapacity_Type()
)
imPM2BatteryNominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatteryNominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatteryNominalCapacity.setUnits("Ah")
_ImPM2BatteryVoltage_Type = Integer32
_ImPM2BatteryVoltage_Object = MibScalar
imPM2BatteryVoltage = _ImPM2BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 6, 2),
    _ImPM2BatteryVoltage_Type()
)
imPM2BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatteryVoltage.setUnits("0.1 V")
_ImPM2BatteryCurrent_Type = Integer32
_ImPM2BatteryCurrent_Object = MibScalar
imPM2BatteryCurrent = _ImPM2BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 6, 3),
    _ImPM2BatteryCurrent_Type()
)
imPM2BatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatteryCurrent.setUnits("0.1 A")
_ImPM2BatteryChargeState_Type = NonNegativeInteger
_ImPM2BatteryChargeState_Object = MibScalar
imPM2BatteryChargeState = _ImPM2BatteryChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 6, 4),
    _ImPM2BatteryChargeState_Type()
)
imPM2BatteryChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatteryChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatteryChargeState.setUnits("%")
_ImPM2BatteryAutonomyTime_Type = NonNegativeInteger
_ImPM2BatteryAutonomyTime_Object = MibScalar
imPM2BatteryAutonomyTime = _ImPM2BatteryAutonomyTime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 6, 5),
    _ImPM2BatteryAutonomyTime_Type()
)
imPM2BatteryAutonomyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatteryAutonomyTime.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatteryAutonomyTime.setUnits("min")
_ImPM2BatteryTimeOnBattery_Type = NonNegativeInteger
_ImPM2BatteryTimeOnBattery_Object = MibScalar
imPM2BatteryTimeOnBattery = _ImPM2BatteryTimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 6, 6),
    _ImPM2BatteryTimeOnBattery_Type()
)
imPM2BatteryTimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatteryTimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatteryTimeOnBattery.setUnits("min")
_ImPM2BatLeg1_ObjectIdentity = ObjectIdentity
imPM2BatLeg1 = _ImPM2BatLeg1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7)
)


class _ImPM2BatLeg1Manufacturer_Type(DisplayString):
    """Custom type imPM2BatLeg1Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM2BatLeg1Manufacturer_Type.__name__ = "DisplayString"
_ImPM2BatLeg1Manufacturer_Object = MibScalar
imPM2BatLeg1Manufacturer = _ImPM2BatLeg1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 1),
    _ImPM2BatLeg1Manufacturer_Type()
)
imPM2BatLeg1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Manufacturer.setStatus("current")


class _ImPM2BatLeg1Type_Type(DisplayString):
    """Custom type imPM2BatLeg1Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg1Type_Type.__name__ = "DisplayString"
_ImPM2BatLeg1Type_Object = MibScalar
imPM2BatLeg1Type = _ImPM2BatLeg1Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 2),
    _ImPM2BatLeg1Type_Type()
)
imPM2BatLeg1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Type.setStatus("current")


class _ImPM2BatLeg1serNumb_Type(DisplayString):
    """Custom type imPM2BatLeg1serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg1serNumb_Type.__name__ = "DisplayString"
_ImPM2BatLeg1serNumb_Object = MibScalar
imPM2BatLeg1serNumb = _ImPM2BatLeg1serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 3),
    _ImPM2BatLeg1serNumb_Type()
)
imPM2BatLeg1serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1serNumb.setStatus("current")


class _ImPM2BatLeg1nextServiceDate_Type(DisplayString):
    """Custom type imPM2BatLeg1nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg1nextServiceDate_Type.__name__ = "DisplayString"
_ImPM2BatLeg1nextServiceDate_Object = MibScalar
imPM2BatLeg1nextServiceDate = _ImPM2BatLeg1nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 4),
    _ImPM2BatLeg1nextServiceDate_Type()
)
imPM2BatLeg1nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1nextServiceDate.setStatus("current")


class _ImPM2BatLeg1InstallationDate_Type(DisplayString):
    """Custom type imPM2BatLeg1InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg1InstallationDate_Type.__name__ = "DisplayString"
_ImPM2BatLeg1InstallationDate_Object = MibScalar
imPM2BatLeg1InstallationDate = _ImPM2BatLeg1InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 5),
    _ImPM2BatLeg1InstallationDate_Type()
)
imPM2BatLeg1InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1InstallationDate.setStatus("current")
_ImPM2BatLeg1NominalVoltage_Type = Integer32
_ImPM2BatLeg1NominalVoltage_Object = MibScalar
imPM2BatLeg1NominalVoltage = _ImPM2BatLeg1NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 6),
    _ImPM2BatLeg1NominalVoltage_Type()
)
imPM2BatLeg1NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1NominalVoltage.setUnits("0.1 V")
_ImPM2BatLeg1NominalCapacity_Type = NonNegativeInteger
_ImPM2BatLeg1NominalCapacity_Object = MibScalar
imPM2BatLeg1NominalCapacity = _ImPM2BatLeg1NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 7),
    _ImPM2BatLeg1NominalCapacity_Type()
)
imPM2BatLeg1NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1NominalCapacity.setUnits("Ah")
_ImPM2BatLeg1Lifetime_Type = NonNegativeInteger
_ImPM2BatLeg1Lifetime_Object = MibScalar
imPM2BatLeg1Lifetime = _ImPM2BatLeg1Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 8),
    _ImPM2BatLeg1Lifetime_Type()
)
imPM2BatLeg1Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1Lifetime.setUnits("years")
_ImPM2BatLeg1Voltage_Type = Integer32
_ImPM2BatLeg1Voltage_Object = MibScalar
imPM2BatLeg1Voltage = _ImPM2BatLeg1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 9),
    _ImPM2BatLeg1Voltage_Type()
)
imPM2BatLeg1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1Voltage.setUnits("0.1 V")
_ImPM2BatLeg1Current_Type = Integer32
_ImPM2BatLeg1Current_Object = MibScalar
imPM2BatLeg1Current = _ImPM2BatLeg1Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 10),
    _ImPM2BatLeg1Current_Type()
)
imPM2BatLeg1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1Current.setUnits("0.1 A")
_ImPM2BatLeg1Temperature_Type = Integer32
_ImPM2BatLeg1Temperature_Object = MibScalar
imPM2BatLeg1Temperature = _ImPM2BatLeg1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 11),
    _ImPM2BatLeg1Temperature_Type()
)
imPM2BatLeg1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1Temperature.setUnits("degrees Centigrade")
_ImPM2BatLeg1ChargeState_Type = NonNegativeInteger
_ImPM2BatLeg1ChargeState_Object = MibScalar
imPM2BatLeg1ChargeState = _ImPM2BatLeg1ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 12),
    _ImPM2BatLeg1ChargeState_Type()
)
imPM2BatLeg1ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1ChargeState.setUnits("%")
_ImPM2BatLeg1RestCapacity_Type = NonNegativeInteger
_ImPM2BatLeg1RestCapacity_Object = MibScalar
imPM2BatLeg1RestCapacity = _ImPM2BatLeg1RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 13),
    _ImPM2BatLeg1RestCapacity_Type()
)
imPM2BatLeg1RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1RestCapacity.setUnits("Ah")
_ImPM2BatLeg1Autonomytime_Type = NonNegativeInteger
_ImPM2BatLeg1Autonomytime_Object = MibScalar
imPM2BatLeg1Autonomytime = _ImPM2BatLeg1Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 14),
    _ImPM2BatLeg1Autonomytime_Type()
)
imPM2BatLeg1Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1Autonomytime.setUnits("min")
_ImPM2BatLeg1TimeOnBattery_Type = NonNegativeInteger
_ImPM2BatLeg1TimeOnBattery_Object = MibScalar
imPM2BatLeg1TimeOnBattery = _ImPM2BatLeg1TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 15),
    _ImPM2BatLeg1TimeOnBattery_Type()
)
imPM2BatLeg1TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg1TimeOnBattery.setUnits("min")


class _ImPM2BatLeg1Fuse_Type(Integer32):
    """Custom type imPM2BatLeg1Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg1Fuse_Type.__name__ = "Integer32"
_ImPM2BatLeg1Fuse_Object = MibScalar
imPM2BatLeg1Fuse = _ImPM2BatLeg1Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 16),
    _ImPM2BatLeg1Fuse_Type()
)
imPM2BatLeg1Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Fuse.setStatus("current")


class _ImPM2BatLeg1Breaker_Type(Integer32):
    """Custom type imPM2BatLeg1Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg1Breaker_Type.__name__ = "Integer32"
_ImPM2BatLeg1Breaker_Object = MibScalar
imPM2BatLeg1Breaker = _ImPM2BatLeg1Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 17),
    _ImPM2BatLeg1Breaker_Type()
)
imPM2BatLeg1Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1Breaker.setStatus("current")


class _ImPM2BatLeg1LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM2BatLeg1LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg1LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM2BatLeg1LowVoltageDisconnect_Object = MibScalar
imPM2BatLeg1LowVoltageDisconnect = _ImPM2BatLeg1LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 7, 18),
    _ImPM2BatLeg1LowVoltageDisconnect_Type()
)
imPM2BatLeg1LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg1LowVoltageDisconnect.setStatus("current")
_ImPM2BatLeg2_ObjectIdentity = ObjectIdentity
imPM2BatLeg2 = _ImPM2BatLeg2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8)
)


class _ImPM2BatLeg2Manufacturer_Type(DisplayString):
    """Custom type imPM2BatLeg2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM2BatLeg2Manufacturer_Type.__name__ = "DisplayString"
_ImPM2BatLeg2Manufacturer_Object = MibScalar
imPM2BatLeg2Manufacturer = _ImPM2BatLeg2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 1),
    _ImPM2BatLeg2Manufacturer_Type()
)
imPM2BatLeg2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Manufacturer.setStatus("current")


class _ImPM2BatLeg2Type_Type(DisplayString):
    """Custom type imPM2BatLeg2Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg2Type_Type.__name__ = "DisplayString"
_ImPM2BatLeg2Type_Object = MibScalar
imPM2BatLeg2Type = _ImPM2BatLeg2Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 2),
    _ImPM2BatLeg2Type_Type()
)
imPM2BatLeg2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Type.setStatus("current")


class _ImPM2BatLeg2serNumb_Type(DisplayString):
    """Custom type imPM2BatLeg2serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg2serNumb_Type.__name__ = "DisplayString"
_ImPM2BatLeg2serNumb_Object = MibScalar
imPM2BatLeg2serNumb = _ImPM2BatLeg2serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 3),
    _ImPM2BatLeg2serNumb_Type()
)
imPM2BatLeg2serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2serNumb.setStatus("current")


class _ImPM2BatLeg2nextServiceDate_Type(DisplayString):
    """Custom type imPM2BatLeg2nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg2nextServiceDate_Type.__name__ = "DisplayString"
_ImPM2BatLeg2nextServiceDate_Object = MibScalar
imPM2BatLeg2nextServiceDate = _ImPM2BatLeg2nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 4),
    _ImPM2BatLeg2nextServiceDate_Type()
)
imPM2BatLeg2nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2nextServiceDate.setStatus("current")


class _ImPM2BatLeg2InstallationDate_Type(DisplayString):
    """Custom type imPM2BatLeg2InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg2InstallationDate_Type.__name__ = "DisplayString"
_ImPM2BatLeg2InstallationDate_Object = MibScalar
imPM2BatLeg2InstallationDate = _ImPM2BatLeg2InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 5),
    _ImPM2BatLeg2InstallationDate_Type()
)
imPM2BatLeg2InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2InstallationDate.setStatus("current")
_ImPM2BatLeg2NominalVoltage_Type = Integer32
_ImPM2BatLeg2NominalVoltage_Object = MibScalar
imPM2BatLeg2NominalVoltage = _ImPM2BatLeg2NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 6),
    _ImPM2BatLeg2NominalVoltage_Type()
)
imPM2BatLeg2NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2NominalVoltage.setUnits("0.1 V")
_ImPM2BatLeg2NominalCapacity_Type = NonNegativeInteger
_ImPM2BatLeg2NominalCapacity_Object = MibScalar
imPM2BatLeg2NominalCapacity = _ImPM2BatLeg2NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 7),
    _ImPM2BatLeg2NominalCapacity_Type()
)
imPM2BatLeg2NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2NominalCapacity.setUnits("Ah")
_ImPM2BatLeg2Lifetime_Type = NonNegativeInteger
_ImPM2BatLeg2Lifetime_Object = MibScalar
imPM2BatLeg2Lifetime = _ImPM2BatLeg2Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 8),
    _ImPM2BatLeg2Lifetime_Type()
)
imPM2BatLeg2Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2Lifetime.setUnits("years")
_ImPM2BatLeg2Voltage_Type = Integer32
_ImPM2BatLeg2Voltage_Object = MibScalar
imPM2BatLeg2Voltage = _ImPM2BatLeg2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 9),
    _ImPM2BatLeg2Voltage_Type()
)
imPM2BatLeg2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2Voltage.setUnits("0.1 V")
_ImPM2BatLeg2Current_Type = Integer32
_ImPM2BatLeg2Current_Object = MibScalar
imPM2BatLeg2Current = _ImPM2BatLeg2Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 10),
    _ImPM2BatLeg2Current_Type()
)
imPM2BatLeg2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2Current.setUnits("0.1 A")
_ImPM2BatLeg2Temperature_Type = Integer32
_ImPM2BatLeg2Temperature_Object = MibScalar
imPM2BatLeg2Temperature = _ImPM2BatLeg2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 11),
    _ImPM2BatLeg2Temperature_Type()
)
imPM2BatLeg2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2Temperature.setUnits("degrees Centigrade")
_ImPM2BatLeg2ChargeState_Type = NonNegativeInteger
_ImPM2BatLeg2ChargeState_Object = MibScalar
imPM2BatLeg2ChargeState = _ImPM2BatLeg2ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 12),
    _ImPM2BatLeg2ChargeState_Type()
)
imPM2BatLeg2ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2ChargeState.setUnits("%")
_ImPM2BatLeg2RestCapacity_Type = NonNegativeInteger
_ImPM2BatLeg2RestCapacity_Object = MibScalar
imPM2BatLeg2RestCapacity = _ImPM2BatLeg2RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 13),
    _ImPM2BatLeg2RestCapacity_Type()
)
imPM2BatLeg2RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2RestCapacity.setUnits("Ah")
_ImPM2BatLeg2Autonomytime_Type = NonNegativeInteger
_ImPM2BatLeg2Autonomytime_Object = MibScalar
imPM2BatLeg2Autonomytime = _ImPM2BatLeg2Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 14),
    _ImPM2BatLeg2Autonomytime_Type()
)
imPM2BatLeg2Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2Autonomytime.setUnits("min")
_ImPM2BatLeg2TimeOnBattery_Type = NonNegativeInteger
_ImPM2BatLeg2TimeOnBattery_Object = MibScalar
imPM2BatLeg2TimeOnBattery = _ImPM2BatLeg2TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 15),
    _ImPM2BatLeg2TimeOnBattery_Type()
)
imPM2BatLeg2TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg2TimeOnBattery.setUnits("min")


class _ImPM2BatLeg2Fuse_Type(Integer32):
    """Custom type imPM2BatLeg2Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg2Fuse_Type.__name__ = "Integer32"
_ImPM2BatLeg2Fuse_Object = MibScalar
imPM2BatLeg2Fuse = _ImPM2BatLeg2Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 16),
    _ImPM2BatLeg2Fuse_Type()
)
imPM2BatLeg2Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Fuse.setStatus("current")


class _ImPM2BatLeg2Breaker_Type(Integer32):
    """Custom type imPM2BatLeg2Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg2Breaker_Type.__name__ = "Integer32"
_ImPM2BatLeg2Breaker_Object = MibScalar
imPM2BatLeg2Breaker = _ImPM2BatLeg2Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 17),
    _ImPM2BatLeg2Breaker_Type()
)
imPM2BatLeg2Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2Breaker.setStatus("current")


class _ImPM2BatLeg2LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM2BatLeg2LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg2LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM2BatLeg2LowVoltageDisconnect_Object = MibScalar
imPM2BatLeg2LowVoltageDisconnect = _ImPM2BatLeg2LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 8, 18),
    _ImPM2BatLeg2LowVoltageDisconnect_Type()
)
imPM2BatLeg2LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg2LowVoltageDisconnect.setStatus("current")
_ImPM2BatLeg3_ObjectIdentity = ObjectIdentity
imPM2BatLeg3 = _ImPM2BatLeg3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9)
)


class _ImPM2BatLeg3Manufacturer_Type(DisplayString):
    """Custom type imPM2BatLeg3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM2BatLeg3Manufacturer_Type.__name__ = "DisplayString"
_ImPM2BatLeg3Manufacturer_Object = MibScalar
imPM2BatLeg3Manufacturer = _ImPM2BatLeg3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 1),
    _ImPM2BatLeg3Manufacturer_Type()
)
imPM2BatLeg3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Manufacturer.setStatus("current")


class _ImPM2BatLeg3Type_Type(DisplayString):
    """Custom type imPM2BatLeg3Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg3Type_Type.__name__ = "DisplayString"
_ImPM2BatLeg3Type_Object = MibScalar
imPM2BatLeg3Type = _ImPM2BatLeg3Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 2),
    _ImPM2BatLeg3Type_Type()
)
imPM2BatLeg3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Type.setStatus("current")


class _ImPM2BatLeg3serNumb_Type(DisplayString):
    """Custom type imPM2BatLeg3serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg3serNumb_Type.__name__ = "DisplayString"
_ImPM2BatLeg3serNumb_Object = MibScalar
imPM2BatLeg3serNumb = _ImPM2BatLeg3serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 3),
    _ImPM2BatLeg3serNumb_Type()
)
imPM2BatLeg3serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3serNumb.setStatus("current")


class _ImPM2BatLeg3nextServiceDate_Type(DisplayString):
    """Custom type imPM2BatLeg3nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg3nextServiceDate_Type.__name__ = "DisplayString"
_ImPM2BatLeg3nextServiceDate_Object = MibScalar
imPM2BatLeg3nextServiceDate = _ImPM2BatLeg3nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 4),
    _ImPM2BatLeg3nextServiceDate_Type()
)
imPM2BatLeg3nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3nextServiceDate.setStatus("current")


class _ImPM2BatLeg3InstallationDate_Type(DisplayString):
    """Custom type imPM2BatLeg3InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM2BatLeg3InstallationDate_Type.__name__ = "DisplayString"
_ImPM2BatLeg3InstallationDate_Object = MibScalar
imPM2BatLeg3InstallationDate = _ImPM2BatLeg3InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 5),
    _ImPM2BatLeg3InstallationDate_Type()
)
imPM2BatLeg3InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3InstallationDate.setStatus("current")
_ImPM2BatLeg3NominalVoltage_Type = Integer32
_ImPM2BatLeg3NominalVoltage_Object = MibScalar
imPM2BatLeg3NominalVoltage = _ImPM2BatLeg3NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 6),
    _ImPM2BatLeg3NominalVoltage_Type()
)
imPM2BatLeg3NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3NominalVoltage.setUnits("0.1 V")
_ImPM2BatLeg3NominalCapacity_Type = NonNegativeInteger
_ImPM2BatLeg3NominalCapacity_Object = MibScalar
imPM2BatLeg3NominalCapacity = _ImPM2BatLeg3NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 7),
    _ImPM2BatLeg3NominalCapacity_Type()
)
imPM2BatLeg3NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3NominalCapacity.setUnits("Ah")
_ImPM2BatLeg3Lifetime_Type = NonNegativeInteger
_ImPM2BatLeg3Lifetime_Object = MibScalar
imPM2BatLeg3Lifetime = _ImPM2BatLeg3Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 8),
    _ImPM2BatLeg3Lifetime_Type()
)
imPM2BatLeg3Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3Lifetime.setUnits("years")
_ImPM2BatLeg3Voltage_Type = Integer32
_ImPM2BatLeg3Voltage_Object = MibScalar
imPM2BatLeg3Voltage = _ImPM2BatLeg3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 9),
    _ImPM2BatLeg3Voltage_Type()
)
imPM2BatLeg3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3Voltage.setUnits("0.1 V")
_ImPM2BatLeg3Current_Type = Integer32
_ImPM2BatLeg3Current_Object = MibScalar
imPM2BatLeg3Current = _ImPM2BatLeg3Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 10),
    _ImPM2BatLeg3Current_Type()
)
imPM2BatLeg3Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3Current.setUnits("0.1 A")
_ImPM2BatLeg3Temperature_Type = Integer32
_ImPM2BatLeg3Temperature_Object = MibScalar
imPM2BatLeg3Temperature = _ImPM2BatLeg3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 11),
    _ImPM2BatLeg3Temperature_Type()
)
imPM2BatLeg3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3Temperature.setUnits("degrees Centigrade")
_ImPM2BatLeg3ChargeState_Type = NonNegativeInteger
_ImPM2BatLeg3ChargeState_Object = MibScalar
imPM2BatLeg3ChargeState = _ImPM2BatLeg3ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 12),
    _ImPM2BatLeg3ChargeState_Type()
)
imPM2BatLeg3ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3ChargeState.setUnits("%")
_ImPM2BatLeg3RestCapacity_Type = NonNegativeInteger
_ImPM2BatLeg3RestCapacity_Object = MibScalar
imPM2BatLeg3RestCapacity = _ImPM2BatLeg3RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 13),
    _ImPM2BatLeg3RestCapacity_Type()
)
imPM2BatLeg3RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3RestCapacity.setUnits("Ah")
_ImPM2BatLeg3Autonomytime_Type = NonNegativeInteger
_ImPM2BatLeg3Autonomytime_Object = MibScalar
imPM2BatLeg3Autonomytime = _ImPM2BatLeg3Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 14),
    _ImPM2BatLeg3Autonomytime_Type()
)
imPM2BatLeg3Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3Autonomytime.setUnits("min")
_ImPM2BatLeg3TimeOnBattery_Type = NonNegativeInteger
_ImPM2BatLeg3TimeOnBattery_Object = MibScalar
imPM2BatLeg3TimeOnBattery = _ImPM2BatLeg3TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 15),
    _ImPM2BatLeg3TimeOnBattery_Type()
)
imPM2BatLeg3TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM2BatLeg3TimeOnBattery.setUnits("min")


class _ImPM2BatLeg3Fuse_Type(Integer32):
    """Custom type imPM2BatLeg3Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg3Fuse_Type.__name__ = "Integer32"
_ImPM2BatLeg3Fuse_Object = MibScalar
imPM2BatLeg3Fuse = _ImPM2BatLeg3Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 16),
    _ImPM2BatLeg3Fuse_Type()
)
imPM2BatLeg3Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Fuse.setStatus("current")


class _ImPM2BatLeg3Breaker_Type(Integer32):
    """Custom type imPM2BatLeg3Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg3Breaker_Type.__name__ = "Integer32"
_ImPM2BatLeg3Breaker_Object = MibScalar
imPM2BatLeg3Breaker = _ImPM2BatLeg3Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 17),
    _ImPM2BatLeg3Breaker_Type()
)
imPM2BatLeg3Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3Breaker.setStatus("current")


class _ImPM2BatLeg3LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM2BatLeg3LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2BatLeg3LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM2BatLeg3LowVoltageDisconnect_Object = MibScalar
imPM2BatLeg3LowVoltageDisconnect = _ImPM2BatLeg3LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 9, 18),
    _ImPM2BatLeg3LowVoltageDisconnect_Type()
)
imPM2BatLeg3LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2BatLeg3LowVoltageDisconnect.setStatus("current")
_ImPM2Distrib_ObjectIdentity = ObjectIdentity
imPM2Distrib = _ImPM2Distrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 10)
)
_ImPm2Distrib_Type = Integer32
_ImPm2Distrib_Object = MibScalar
imPm2Distrib = _ImPm2Distrib_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 10, 1),
    _ImPm2Distrib_Type()
)
imPm2Distrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm2Distrib.setStatus("current")
if mibBuilder.loadTexts:
    imPm2Distrib.setUnits("degrees Centigrade")
_ImPM2DistTable_Object = MibTable
imPM2DistTable = _ImPM2DistTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    imPM2DistTable.setStatus("current")
_ImPM2DistEntry_Object = MibTableRow
imPM2DistEntry = _ImPM2DistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 10, 2, 1)
)
imPM2DistEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imPM2DistId"),
)
if mibBuilder.loadTexts:
    imPM2DistEntry.setStatus("current")
_ImPM2DistId_Type = PositiveInteger
_ImPM2DistId_Object = MibTableColumn
imPM2DistId = _ImPM2DistId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 10, 2, 1, 1),
    _ImPM2DistId_Type()
)
imPM2DistId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imPM2DistId.setStatus("current")


class _ImPM2DistFuse_Type(Integer32):
    """Custom type imPM2DistFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2DistFuse_Type.__name__ = "Integer32"
_ImPM2DistFuse_Object = MibTableColumn
imPM2DistFuse = _ImPM2DistFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 10, 2, 1, 2),
    _ImPM2DistFuse_Type()
)
imPM2DistFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2DistFuse.setStatus("current")


class _ImPM2DistBreaker_Type(Integer32):
    """Custom type imPM2DistBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM2DistBreaker_Type.__name__ = "Integer32"
_ImPM2DistBreaker_Object = MibTableColumn
imPM2DistBreaker = _ImPM2DistBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 10, 2, 1, 3),
    _ImPM2DistBreaker_Type()
)
imPM2DistBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2DistBreaker.setStatus("current")
_ImPM2Control_ObjectIdentity = ObjectIdentity
imPM2Control = _ImPM2Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11)
)
_ImPM2ContTable_Object = MibTable
imPM2ContTable = _ImPM2ContTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 1)
)
if mibBuilder.loadTexts:
    imPM2ContTable.setStatus("current")
_ImPM2ContEntry_Object = MibTableRow
imPM2ContEntry = _ImPM2ContEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 1, 1)
)
imPM2ContEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imPM2ContId"),
)
if mibBuilder.loadTexts:
    imPM2ContEntry.setStatus("current")
_ImPM2ContId_Type = PositiveInteger
_ImPM2ContId_Object = MibTableColumn
imPM2ContId = _ImPM2ContId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 1, 1, 1),
    _ImPM2ContId_Type()
)
imPM2ContId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imPM2ContId.setStatus("current")


class _ImPM2ContState_Type(Integer32):
    """Custom type imPM2ContState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_ImPM2ContState_Type.__name__ = "Integer32"
_ImPM2ContState_Object = MibTableColumn
imPM2ContState = _ImPM2ContState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 1, 1, 2),
    _ImPM2ContState_Type()
)
imPM2ContState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM2ContState.setStatus("current")


class _ImPM2ContLabel_Type(DisplayString):
    """Custom type imPM2ContLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM2ContLabel_Type.__name__ = "DisplayString"
_ImPM2ContLabel_Object = MibTableColumn
imPM2ContLabel = _ImPM2ContLabel_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 1, 1, 3),
    _ImPM2ContLabel_Type()
)
imPM2ContLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2ContLabel.setStatus("current")
_ImPM2ContTimeOFF_Type = Integer32
_ImPM2ContTimeOFF_Object = MibTableColumn
imPM2ContTimeOFF = _ImPM2ContTimeOFF_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 1, 1, 4),
    _ImPM2ContTimeOFF_Type()
)
imPM2ContTimeOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM2ContTimeOFF.setStatus("current")
if mibBuilder.loadTexts:
    imPM2ContTimeOFF.setUnits("min")


class _ImPM2ContAuto_Type(Integer32):
    """Custom type imPM2ContAuto based on Integer32"""
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


_ImPM2ContAuto_Type.__name__ = "Integer32"
_ImPM2ContAuto_Object = MibTableColumn
imPM2ContAuto = _ImPM2ContAuto_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 1, 1, 5),
    _ImPM2ContAuto_Type()
)
imPM2ContAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM2ContAuto.setStatus("current")


class _ImPM2ContTestCAPcommand_Type(Integer32):
    """Custom type imPM2ContTestCAPcommand based on Integer32"""
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


_ImPM2ContTestCAPcommand_Type.__name__ = "Integer32"
_ImPM2ContTestCAPcommand_Object = MibScalar
imPM2ContTestCAPcommand = _ImPM2ContTestCAPcommand_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 2),
    _ImPM2ContTestCAPcommand_Type()
)
imPM2ContTestCAPcommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM2ContTestCAPcommand.setStatus("current")
_ImPM2ContTestCAPvoltage_Type = Integer32
_ImPM2ContTestCAPvoltage_Object = MibScalar
imPM2ContTestCAPvoltage = _ImPM2ContTestCAPvoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 3),
    _ImPM2ContTestCAPvoltage_Type()
)
imPM2ContTestCAPvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2ContTestCAPvoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM2ContTestCAPvoltage.setUnits("0.1 V")
_ImPM2ContTestCAPcurrent_Type = Integer32
_ImPM2ContTestCAPcurrent_Object = MibScalar
imPM2ContTestCAPcurrent = _ImPM2ContTestCAPcurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 4),
    _ImPM2ContTestCAPcurrent_Type()
)
imPM2ContTestCAPcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2ContTestCAPcurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM2ContTestCAPcurrent.setUnits("0.1 A")
_ImPM2ContTestCAPtemperature_Type = Integer32
_ImPM2ContTestCAPtemperature_Object = MibScalar
imPM2ContTestCAPtemperature = _ImPM2ContTestCAPtemperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 5),
    _ImPM2ContTestCAPtemperature_Type()
)
imPM2ContTestCAPtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2ContTestCAPtemperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM2ContTestCAPtemperature.setUnits("degrees Centigrade")
_ImPM2ContTestCAPduration_Type = Integer32
_ImPM2ContTestCAPduration_Object = MibScalar
imPM2ContTestCAPduration = _ImPM2ContTestCAPduration_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 6),
    _ImPM2ContTestCAPduration_Type()
)
imPM2ContTestCAPduration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2ContTestCAPduration.setStatus("current")
if mibBuilder.loadTexts:
    imPM2ContTestCAPduration.setUnits("min")
_ImPM2ContTestCAPstatus_Type = Integer32
_ImPM2ContTestCAPstatus_Object = MibScalar
imPM2ContTestCAPstatus = _ImPM2ContTestCAPstatus_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 2, 11, 7),
    _ImPM2ContTestCAPstatus_Type()
)
imPM2ContTestCAPstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM2ContTestCAPstatus.setStatus("current")
_ImPanM3_ObjectIdentity = ObjectIdentity
imPanM3 = _ImPanM3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3)
)
_ImPM3SystemID_ObjectIdentity = ObjectIdentity
imPM3SystemID = _ImPM3SystemID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1)
)


class _ImPM3SystemIDManufacturer_Type(DisplayString):
    """Custom type imPM3SystemIDManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM3SystemIDManufacturer_Type.__name__ = "DisplayString"
_ImPM3SystemIDManufacturer_Object = MibScalar
imPM3SystemIDManufacturer = _ImPM3SystemIDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 1),
    _ImPM3SystemIDManufacturer_Type()
)
imPM3SystemIDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDManufacturer.setStatus("current")


class _ImPM3SystemIDType_Type(DisplayString):
    """Custom type imPM3SystemIDType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3SystemIDType_Type.__name__ = "DisplayString"
_ImPM3SystemIDType_Object = MibScalar
imPM3SystemIDType = _ImPM3SystemIDType_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 2),
    _ImPM3SystemIDType_Type()
)
imPM3SystemIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDType.setStatus("current")


class _ImPM3SystemIDserNumb_Type(DisplayString):
    """Custom type imPM3SystemIDserNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3SystemIDserNumb_Type.__name__ = "DisplayString"
_ImPM3SystemIDserNumb_Object = MibScalar
imPM3SystemIDserNumb = _ImPM3SystemIDserNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 3),
    _ImPM3SystemIDserNumb_Type()
)
imPM3SystemIDserNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDserNumb.setStatus("current")


class _ImPM3SystemIDnextServiceDate_Type(DisplayString):
    """Custom type imPM3SystemIDnextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3SystemIDnextServiceDate_Type.__name__ = "DisplayString"
_ImPM3SystemIDnextServiceDate_Object = MibScalar
imPM3SystemIDnextServiceDate = _ImPM3SystemIDnextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 4),
    _ImPM3SystemIDnextServiceDate_Type()
)
imPM3SystemIDnextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDnextServiceDate.setStatus("current")
_ImPM3SystemIDaddress_Type = NonNegativeInteger
_ImPM3SystemIDaddress_Object = MibScalar
imPM3SystemIDaddress = _ImPM3SystemIDaddress_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 5),
    _ImPM3SystemIDaddress_Type()
)
imPM3SystemIDaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDaddress.setStatus("current")
_ImPM3SystemIDhwVersion_Type = NonNegativeInteger
_ImPM3SystemIDhwVersion_Object = MibScalar
imPM3SystemIDhwVersion = _ImPM3SystemIDhwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 6),
    _ImPM3SystemIDhwVersion_Type()
)
imPM3SystemIDhwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDhwVersion.setStatus("current")
_ImPM3SystemIDswVersion_Type = NonNegativeInteger
_ImPM3SystemIDswVersion_Object = MibScalar
imPM3SystemIDswVersion = _ImPM3SystemIDswVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 7),
    _ImPM3SystemIDswVersion_Type()
)
imPM3SystemIDswVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDswVersion.setStatus("current")


class _ImPM3SystemIDPMserialNumber_Type(DisplayString):
    """Custom type imPM3SystemIDPMserialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3SystemIDPMserialNumber_Type.__name__ = "DisplayString"
_ImPM3SystemIDPMserialNumber_Object = MibScalar
imPM3SystemIDPMserialNumber = _ImPM3SystemIDPMserialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 8),
    _ImPM3SystemIDPMserialNumber_Type()
)
imPM3SystemIDPMserialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDPMserialNumber.setStatus("current")


class _ImPM3SystemIDbuttonName_Type(DisplayString):
    """Custom type imPM3SystemIDbuttonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3SystemIDbuttonName_Type.__name__ = "DisplayString"
_ImPM3SystemIDbuttonName_Object = MibScalar
imPM3SystemIDbuttonName = _ImPM3SystemIDbuttonName_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 1, 9),
    _ImPM3SystemIDbuttonName_Type()
)
imPM3SystemIDbuttonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemIDbuttonName.setStatus("current")
_ImPM3SystemGEN_ObjectIdentity = ObjectIdentity
imPM3SystemGEN = _ImPM3SystemGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2)
)


class _ImPM3SystemGENSurgeArrester_Type(Integer32):
    """Custom type imPM3SystemGENSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3SystemGENSurgeArrester_Type.__name__ = "Integer32"
_ImPM3SystemGENSurgeArrester_Object = MibScalar
imPM3SystemGENSurgeArrester = _ImPM3SystemGENSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 1),
    _ImPM3SystemGENSurgeArrester_Type()
)
imPM3SystemGENSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENSurgeArrester.setStatus("current")


class _ImPM3SystemGENDoor1_Type(Integer32):
    """Custom type imPM3SystemGENDoor1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_ImPM3SystemGENDoor1_Type.__name__ = "Integer32"
_ImPM3SystemGENDoor1_Object = MibScalar
imPM3SystemGENDoor1 = _ImPM3SystemGENDoor1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 2),
    _ImPM3SystemGENDoor1_Type()
)
imPM3SystemGENDoor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENDoor1.setStatus("current")


class _ImPM3SystemGENDoor2_Type(Integer32):
    """Custom type imPM3SystemGENDoor2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_ImPM3SystemGENDoor2_Type.__name__ = "Integer32"
_ImPM3SystemGENDoor2_Object = MibScalar
imPM3SystemGENDoor2 = _ImPM3SystemGENDoor2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 3),
    _ImPM3SystemGENDoor2_Type()
)
imPM3SystemGENDoor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENDoor2.setStatus("current")


class _ImPM3SystemGENFan_Type(Integer32):
    """Custom type imPM3SystemGENFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_ImPM3SystemGENFan_Type.__name__ = "Integer32"
_ImPM3SystemGENFan_Object = MibScalar
imPM3SystemGENFan = _ImPM3SystemGENFan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 4),
    _ImPM3SystemGENFan_Type()
)
imPM3SystemGENFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENFan.setStatus("current")


class _ImPM3SystemGENuser1_Type(Integer32):
    """Custom type imPM3SystemGENuser1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3SystemGENuser1_Type.__name__ = "Integer32"
_ImPM3SystemGENuser1_Object = MibScalar
imPM3SystemGENuser1 = _ImPM3SystemGENuser1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 5),
    _ImPM3SystemGENuser1_Type()
)
imPM3SystemGENuser1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENuser1.setStatus("current")


class _ImPM3SystemGENuser2_Type(Integer32):
    """Custom type imPM3SystemGENuser2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3SystemGENuser2_Type.__name__ = "Integer32"
_ImPM3SystemGENuser2_Object = MibScalar
imPM3SystemGENuser2 = _ImPM3SystemGENuser2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 6),
    _ImPM3SystemGENuser2_Type()
)
imPM3SystemGENuser2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENuser2.setStatus("current")


class _ImPM3SystemGENuser3_Type(Integer32):
    """Custom type imPM3SystemGENuser3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3SystemGENuser3_Type.__name__ = "Integer32"
_ImPM3SystemGENuser3_Object = MibScalar
imPM3SystemGENuser3 = _ImPM3SystemGENuser3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 7),
    _ImPM3SystemGENuser3_Type()
)
imPM3SystemGENuser3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENuser3.setStatus("current")


class _ImPM3SystemGENuser4_Type(Integer32):
    """Custom type imPM3SystemGENuser4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3SystemGENuser4_Type.__name__ = "Integer32"
_ImPM3SystemGENuser4_Object = MibScalar
imPM3SystemGENuser4 = _ImPM3SystemGENuser4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 8),
    _ImPM3SystemGENuser4_Type()
)
imPM3SystemGENuser4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENuser4.setStatus("current")
_ImPM3SystemGENtemperature_Type = NonNegativeInteger
_ImPM3SystemGENtemperature_Object = MibScalar
imPM3SystemGENtemperature = _ImPM3SystemGENtemperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 2, 9),
    _ImPM3SystemGENtemperature_Type()
)
imPM3SystemGENtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3SystemGENtemperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM3SystemGENtemperature.setUnits("degrees Centigrade")
_ImPM3Power1_ObjectIdentity = ObjectIdentity
imPM3Power1 = _ImPM3Power1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3)
)


class _ImPM3Power1Manufacturer_Type(DisplayString):
    """Custom type imPM3Power1Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM3Power1Manufacturer_Type.__name__ = "DisplayString"
_ImPM3Power1Manufacturer_Object = MibScalar
imPM3Power1Manufacturer = _ImPM3Power1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 1),
    _ImPM3Power1Manufacturer_Type()
)
imPM3Power1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Manufacturer.setStatus("current")


class _ImPM3Power1Type_Type(DisplayString):
    """Custom type imPM3Power1Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power1Type_Type.__name__ = "DisplayString"
_ImPM3Power1Type_Object = MibScalar
imPM3Power1Type = _ImPM3Power1Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 2),
    _ImPM3Power1Type_Type()
)
imPM3Power1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Type.setStatus("current")


class _ImPM3Power1serNumb_Type(DisplayString):
    """Custom type imPM3Power1serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power1serNumb_Type.__name__ = "DisplayString"
_ImPM3Power1serNumb_Object = MibScalar
imPM3Power1serNumb = _ImPM3Power1serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 3),
    _ImPM3Power1serNumb_Type()
)
imPM3Power1serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1serNumb.setStatus("current")


class _ImPM3Power1nextServiceDate_Type(DisplayString):
    """Custom type imPM3Power1nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power1nextServiceDate_Type.__name__ = "DisplayString"
_ImPM3Power1nextServiceDate_Object = MibScalar
imPM3Power1nextServiceDate = _ImPM3Power1nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 4),
    _ImPM3Power1nextServiceDate_Type()
)
imPM3Power1nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1nextServiceDate.setStatus("current")
_ImPM3Power1InputVoltage_Type = Integer32
_ImPM3Power1InputVoltage_Object = MibScalar
imPM3Power1InputVoltage = _ImPM3Power1InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 5),
    _ImPM3Power1InputVoltage_Type()
)
imPM3Power1InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputVoltage.setUnits("0.1 V")
_ImPM3Power1InputCurrent_Type = Integer32
_ImPM3Power1InputCurrent_Object = MibScalar
imPM3Power1InputCurrent = _ImPM3Power1InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 6),
    _ImPM3Power1InputCurrent_Type()
)
imPM3Power1InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputCurrent.setUnits("0.1 A")
_ImPM3Power1InputPowerVA_Type = Integer32
_ImPM3Power1InputPowerVA_Object = MibScalar
imPM3Power1InputPowerVA = _ImPM3Power1InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 7),
    _ImPM3Power1InputPowerVA_Type()
)
imPM3Power1InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerVA.setUnits("VA")
_ImPM3Power1InputPowerKVA_Type = Integer32
_ImPM3Power1InputPowerKVA_Object = MibScalar
imPM3Power1InputPowerKVA = _ImPM3Power1InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 8),
    _ImPM3Power1InputPowerKVA_Type()
)
imPM3Power1InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKVA.setUnits("0.1 kVA")
_ImPM3Power1InputPowerW_Type = Integer32
_ImPM3Power1InputPowerW_Object = MibScalar
imPM3Power1InputPowerW = _ImPM3Power1InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 9),
    _ImPM3Power1InputPowerW_Type()
)
imPM3Power1InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerW.setUnits("W")
_ImPM3Power1InputPowerKW_Type = Integer32
_ImPM3Power1InputPowerKW_Object = MibScalar
imPM3Power1InputPowerKW = _ImPM3Power1InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 10),
    _ImPM3Power1InputPowerKW_Type()
)
imPM3Power1InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKW.setUnits("0.1 kW")
_ImPM3Power1InputVoltagePhase1_Type = Integer32
_ImPM3Power1InputVoltagePhase1_Object = MibScalar
imPM3Power1InputVoltagePhase1 = _ImPM3Power1InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 11),
    _ImPM3Power1InputVoltagePhase1_Type()
)
imPM3Power1InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputVoltagePhase1.setUnits("0.1 V")
_ImPM3Power1InputCurrentPhase1_Type = Integer32
_ImPM3Power1InputCurrentPhase1_Object = MibScalar
imPM3Power1InputCurrentPhase1 = _ImPM3Power1InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 12),
    _ImPM3Power1InputCurrentPhase1_Type()
)
imPM3Power1InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputCurrentPhase1.setUnits("0.1 A")
_ImPM3Power1InputPowerVAphase1_Type = Integer32
_ImPM3Power1InputPowerVAphase1_Object = MibScalar
imPM3Power1InputPowerVAphase1 = _ImPM3Power1InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 13),
    _ImPM3Power1InputPowerVAphase1_Type()
)
imPM3Power1InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerVAphase1.setUnits("VA")
_ImPM3Power1InputPowerKVAphase1_Type = Integer32
_ImPM3Power1InputPowerKVAphase1_Object = MibScalar
imPM3Power1InputPowerKVAphase1 = _ImPM3Power1InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 14),
    _ImPM3Power1InputPowerKVAphase1_Type()
)
imPM3Power1InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM3Power1InputVoltagePhase2_Type = Integer32
_ImPM3Power1InputVoltagePhase2_Object = MibScalar
imPM3Power1InputVoltagePhase2 = _ImPM3Power1InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 15),
    _ImPM3Power1InputVoltagePhase2_Type()
)
imPM3Power1InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputVoltagePhase2.setUnits("0.1 V")
_ImPM3Power1InputCurrentPhase2_Type = Integer32
_ImPM3Power1InputCurrentPhase2_Object = MibScalar
imPM3Power1InputCurrentPhase2 = _ImPM3Power1InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 16),
    _ImPM3Power1InputCurrentPhase2_Type()
)
imPM3Power1InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputCurrentPhase2.setUnits("0.1 A")
_ImPM3Power1InputPowerVAphase2_Type = Integer32
_ImPM3Power1InputPowerVAphase2_Object = MibScalar
imPM3Power1InputPowerVAphase2 = _ImPM3Power1InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 17),
    _ImPM3Power1InputPowerVAphase2_Type()
)
imPM3Power1InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerVAphase2.setUnits("VA")
_ImPM3Power1InputPowerKVAphase2_Type = Integer32
_ImPM3Power1InputPowerKVAphase2_Object = MibScalar
imPM3Power1InputPowerKVAphase2 = _ImPM3Power1InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 18),
    _ImPM3Power1InputPowerKVAphase2_Type()
)
imPM3Power1InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM3Power1InputVoltagePhase3_Type = Integer32
_ImPM3Power1InputVoltagePhase3_Object = MibScalar
imPM3Power1InputVoltagePhase3 = _ImPM3Power1InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 19),
    _ImPM3Power1InputVoltagePhase3_Type()
)
imPM3Power1InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputVoltagePhase3.setUnits("0.1 V")
_ImPM3Power1InputCurrentPhase3_Type = Integer32
_ImPM3Power1InputCurrentPhase3_Object = MibScalar
imPM3Power1InputCurrentPhase3 = _ImPM3Power1InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 20),
    _ImPM3Power1InputCurrentPhase3_Type()
)
imPM3Power1InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputCurrentPhase3.setUnits("0.1 A")
_ImPM3Power1InputPowerVAphase3_Type = Integer32
_ImPM3Power1InputPowerVAphase3_Object = MibScalar
imPM3Power1InputPowerVAphase3 = _ImPM3Power1InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 21),
    _ImPM3Power1InputPowerVAphase3_Type()
)
imPM3Power1InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerVAphase3.setUnits("VA")
_ImPM3Power1InputPowerKVAphase3_Type = Integer32
_ImPM3Power1InputPowerKVAphase3_Object = MibScalar
imPM3Power1InputPowerKVAphase3 = _ImPM3Power1InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 22),
    _ImPM3Power1InputPowerKVAphase3_Type()
)
imPM3Power1InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM3Power1OutputVoltage_Type = Integer32
_ImPM3Power1OutputVoltage_Object = MibScalar
imPM3Power1OutputVoltage = _ImPM3Power1OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 23),
    _ImPM3Power1OutputVoltage_Type()
)
imPM3Power1OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputVoltage.setUnits("0.1 V")
_ImPM3Power1OutputCurrent_Type = Integer32
_ImPM3Power1OutputCurrent_Object = MibScalar
imPM3Power1OutputCurrent = _ImPM3Power1OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 24),
    _ImPM3Power1OutputCurrent_Type()
)
imPM3Power1OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputCurrent.setUnits("0.1 A")
_ImPM3Power1OutputPowerVA_Type = Integer32
_ImPM3Power1OutputPowerVA_Object = MibScalar
imPM3Power1OutputPowerVA = _ImPM3Power1OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 25),
    _ImPM3Power1OutputPowerVA_Type()
)
imPM3Power1OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerVA.setUnits("VA")
_ImPM3Power1OutputPowerKVA_Type = Integer32
_ImPM3Power1OutputPowerKVA_Object = MibScalar
imPM3Power1OutputPowerKVA = _ImPM3Power1OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 26),
    _ImPM3Power1OutputPowerKVA_Type()
)
imPM3Power1OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKVA.setUnits("0.1 kVA")
_ImPM3Power1OutputPowerW_Type = Integer32
_ImPM3Power1OutputPowerW_Object = MibScalar
imPM3Power1OutputPowerW = _ImPM3Power1OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 27),
    _ImPM3Power1OutputPowerW_Type()
)
imPM3Power1OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerW.setUnits("W")
_ImPM3Power1OutputPowerKW_Type = Integer32
_ImPM3Power1OutputPowerKW_Object = MibScalar
imPM3Power1OutputPowerKW = _ImPM3Power1OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 28),
    _ImPM3Power1OutputPowerKW_Type()
)
imPM3Power1OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKW.setUnits("0.1 kW")
_ImPM3Power1OutputLoad_Type = Integer32
_ImPM3Power1OutputLoad_Object = MibScalar
imPM3Power1OutputLoad = _ImPM3Power1OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 29),
    _ImPM3Power1OutputLoad_Type()
)
imPM3Power1OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputLoad.setUnits("%")
_ImPM3Power1OutputFrequency_Type = NonNegativeInteger
_ImPM3Power1OutputFrequency_Object = MibScalar
imPM3Power1OutputFrequency = _ImPM3Power1OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 30),
    _ImPM3Power1OutputFrequency_Type()
)
imPM3Power1OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputFrequency.setUnits("0.1 Hz")
_ImPM3Power1Temperature_Type = Integer32
_ImPM3Power1Temperature_Object = MibScalar
imPM3Power1Temperature = _ImPM3Power1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 31),
    _ImPM3Power1Temperature_Type()
)
imPM3Power1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1Temperature.setUnits("degrees Centigrade")


class _ImPM3Power1Running1_Type(Integer32):
    """Custom type imPM3Power1Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Running1_Type.__name__ = "Integer32"
_ImPM3Power1Running1_Object = MibScalar
imPM3Power1Running1 = _ImPM3Power1Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 32),
    _ImPM3Power1Running1_Type()
)
imPM3Power1Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Running1.setStatus("current")


class _ImPM3Power1Running2_Type(Integer32):
    """Custom type imPM3Power1Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Running2_Type.__name__ = "Integer32"
_ImPM3Power1Running2_Object = MibScalar
imPM3Power1Running2 = _ImPM3Power1Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 33),
    _ImPM3Power1Running2_Type()
)
imPM3Power1Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Running2.setStatus("current")


class _ImPM3Power1Running3_Type(Integer32):
    """Custom type imPM3Power1Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Running3_Type.__name__ = "Integer32"
_ImPM3Power1Running3_Object = MibScalar
imPM3Power1Running3 = _ImPM3Power1Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 34),
    _ImPM3Power1Running3_Type()
)
imPM3Power1Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Running3.setStatus("current")


class _ImPM3Power1Running4_Type(Integer32):
    """Custom type imPM3Power1Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Running4_Type.__name__ = "Integer32"
_ImPM3Power1Running4_Object = MibScalar
imPM3Power1Running4 = _ImPM3Power1Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 35),
    _ImPM3Power1Running4_Type()
)
imPM3Power1Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Running4.setStatus("current")


class _ImPM3Power1Running5_Type(Integer32):
    """Custom type imPM3Power1Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Running5_Type.__name__ = "Integer32"
_ImPM3Power1Running5_Object = MibScalar
imPM3Power1Running5 = _ImPM3Power1Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 36),
    _ImPM3Power1Running5_Type()
)
imPM3Power1Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Running5.setStatus("current")


class _ImPM3Power1Running6_Type(Integer32):
    """Custom type imPM3Power1Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Running6_Type.__name__ = "Integer32"
_ImPM3Power1Running6_Object = MibScalar
imPM3Power1Running6 = _ImPM3Power1Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 37),
    _ImPM3Power1Running6_Type()
)
imPM3Power1Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Running6.setStatus("current")


class _ImPM3Power1Running7_Type(Integer32):
    """Custom type imPM3Power1Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Running7_Type.__name__ = "Integer32"
_ImPM3Power1Running7_Object = MibScalar
imPM3Power1Running7 = _ImPM3Power1Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 38),
    _ImPM3Power1Running7_Type()
)
imPM3Power1Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Running7.setStatus("current")


class _ImPM3Power1Running8_Type(Integer32):
    """Custom type imPM3Power1Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Running8_Type.__name__ = "Integer32"
_ImPM3Power1Running8_Object = MibScalar
imPM3Power1Running8 = _ImPM3Power1Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 39),
    _ImPM3Power1Running8_Type()
)
imPM3Power1Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Running8.setStatus("current")


class _ImPM3Power1InputFuse_Type(Integer32):
    """Custom type imPM3Power1InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputFuse_Type.__name__ = "Integer32"
_ImPM3Power1InputFuse_Object = MibScalar
imPM3Power1InputFuse = _ImPM3Power1InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 40),
    _ImPM3Power1InputFuse_Type()
)
imPM3Power1InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputFuse.setStatus("current")


class _ImPM3Power1InputFuse1_Type(Integer32):
    """Custom type imPM3Power1InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputFuse1_Type.__name__ = "Integer32"
_ImPM3Power1InputFuse1_Object = MibScalar
imPM3Power1InputFuse1 = _ImPM3Power1InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 41),
    _ImPM3Power1InputFuse1_Type()
)
imPM3Power1InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputFuse1.setStatus("current")


class _ImPM3Power1InputFuse2_Type(Integer32):
    """Custom type imPM3Power1InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputFuse2_Type.__name__ = "Integer32"
_ImPM3Power1InputFuse2_Object = MibScalar
imPM3Power1InputFuse2 = _ImPM3Power1InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 42),
    _ImPM3Power1InputFuse2_Type()
)
imPM3Power1InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputFuse2.setStatus("current")


class _ImPM3Power1InputFuse3_Type(Integer32):
    """Custom type imPM3Power1InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputFuse3_Type.__name__ = "Integer32"
_ImPM3Power1InputFuse3_Object = MibScalar
imPM3Power1InputFuse3 = _ImPM3Power1InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 43),
    _ImPM3Power1InputFuse3_Type()
)
imPM3Power1InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputFuse3.setStatus("current")


class _ImPM3Power1InputBreaker_Type(Integer32):
    """Custom type imPM3Power1InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputBreaker_Type.__name__ = "Integer32"
_ImPM3Power1InputBreaker_Object = MibScalar
imPM3Power1InputBreaker = _ImPM3Power1InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 44),
    _ImPM3Power1InputBreaker_Type()
)
imPM3Power1InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputBreaker.setStatus("current")


class _ImPM3Power1InputBreaker1_Type(Integer32):
    """Custom type imPM3Power1InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputBreaker1_Type.__name__ = "Integer32"
_ImPM3Power1InputBreaker1_Object = MibScalar
imPM3Power1InputBreaker1 = _ImPM3Power1InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 45),
    _ImPM3Power1InputBreaker1_Type()
)
imPM3Power1InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputBreaker1.setStatus("current")


class _ImPM3Power1InputBreaker2_Type(Integer32):
    """Custom type imPM3Power1InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputBreaker2_Type.__name__ = "Integer32"
_ImPM3Power1InputBreaker2_Object = MibScalar
imPM3Power1InputBreaker2 = _ImPM3Power1InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 46),
    _ImPM3Power1InputBreaker2_Type()
)
imPM3Power1InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputBreaker2.setStatus("current")


class _ImPM3Power1InputBreaker3_Type(Integer32):
    """Custom type imPM3Power1InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputBreaker3_Type.__name__ = "Integer32"
_ImPM3Power1InputBreaker3_Object = MibScalar
imPM3Power1InputBreaker3 = _ImPM3Power1InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 47),
    _ImPM3Power1InputBreaker3_Type()
)
imPM3Power1InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputBreaker3.setStatus("current")


class _ImPM3Power1InputSurgeArrester_Type(Integer32):
    """Custom type imPM3Power1InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM3Power1InputSurgeArrester_Object = MibScalar
imPM3Power1InputSurgeArrester = _ImPM3Power1InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 48),
    _ImPM3Power1InputSurgeArrester_Type()
)
imPM3Power1InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1InputSurgeArrester.setStatus("current")


class _ImPM3Power1OutputFuse_Type(Integer32):
    """Custom type imPM3Power1OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1OutputFuse_Type.__name__ = "Integer32"
_ImPM3Power1OutputFuse_Object = MibScalar
imPM3Power1OutputFuse = _ImPM3Power1OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 49),
    _ImPM3Power1OutputFuse_Type()
)
imPM3Power1OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputFuse.setStatus("current")


class _ImPM3Power1OutputFuse1_Type(Integer32):
    """Custom type imPM3Power1OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1OutputFuse1_Type.__name__ = "Integer32"
_ImPM3Power1OutputFuse1_Object = MibScalar
imPM3Power1OutputFuse1 = _ImPM3Power1OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 50),
    _ImPM3Power1OutputFuse1_Type()
)
imPM3Power1OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputFuse1.setStatus("current")


class _ImPM3Power1OutputFuse2_Type(Integer32):
    """Custom type imPM3Power1OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1OutputFuse2_Type.__name__ = "Integer32"
_ImPM3Power1OutputFuse2_Object = MibScalar
imPM3Power1OutputFuse2 = _ImPM3Power1OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 51),
    _ImPM3Power1OutputFuse2_Type()
)
imPM3Power1OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputFuse2.setStatus("current")


class _ImPM3Power1OutputBreaker_Type(Integer32):
    """Custom type imPM3Power1OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1OutputBreaker_Type.__name__ = "Integer32"
_ImPM3Power1OutputBreaker_Object = MibScalar
imPM3Power1OutputBreaker = _ImPM3Power1OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 52),
    _ImPM3Power1OutputBreaker_Type()
)
imPM3Power1OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputBreaker.setStatus("current")


class _ImPM3Power1OutputBreaker1_Type(Integer32):
    """Custom type imPM3Power1OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1OutputBreaker1_Type.__name__ = "Integer32"
_ImPM3Power1OutputBreaker1_Object = MibScalar
imPM3Power1OutputBreaker1 = _ImPM3Power1OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 53),
    _ImPM3Power1OutputBreaker1_Type()
)
imPM3Power1OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputBreaker1.setStatus("current")


class _ImPM3Power1OutputBreaker2_Type(Integer32):
    """Custom type imPM3Power1OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1OutputBreaker2_Type.__name__ = "Integer32"
_ImPM3Power1OutputBreaker2_Object = MibScalar
imPM3Power1OutputBreaker2 = _ImPM3Power1OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 54),
    _ImPM3Power1OutputBreaker2_Type()
)
imPM3Power1OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputBreaker2.setStatus("current")


class _ImPM3Power1Fan_Type(Integer32):
    """Custom type imPM3Power1Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1Fan_Type.__name__ = "Integer32"
_ImPM3Power1Fan_Object = MibScalar
imPM3Power1Fan = _ImPM3Power1Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 55),
    _ImPM3Power1Fan_Type()
)
imPM3Power1Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1Fan.setStatus("current")


class _ImPM3Power1BatteryAvailable_Type(Integer32):
    """Custom type imPM3Power1BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power1BatteryAvailable_Type.__name__ = "Integer32"
_ImPM3Power1BatteryAvailable_Object = MibScalar
imPM3Power1BatteryAvailable = _ImPM3Power1BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 56),
    _ImPM3Power1BatteryAvailable_Type()
)
imPM3Power1BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1BatteryAvailable.setStatus("current")
_ImPM3Power1OutputVoltagePhase1_Type = Integer32
_ImPM3Power1OutputVoltagePhase1_Object = MibScalar
imPM3Power1OutputVoltagePhase1 = _ImPM3Power1OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 57),
    _ImPM3Power1OutputVoltagePhase1_Type()
)
imPM3Power1OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputVoltagePhase1.setUnits("0.1 V")
_ImPM3Power1OutputCurrentPhase1_Type = Integer32
_ImPM3Power1OutputCurrentPhase1_Object = MibScalar
imPM3Power1OutputCurrentPhase1 = _ImPM3Power1OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 58),
    _ImPM3Power1OutputCurrentPhase1_Type()
)
imPM3Power1OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputCurrentPhase1.setUnits("0.1 A")
_ImPM3Power1OutputPowerVAphase1_Type = Integer32
_ImPM3Power1OutputPowerVAphase1_Object = MibScalar
imPM3Power1OutputPowerVAphase1 = _ImPM3Power1OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 59),
    _ImPM3Power1OutputPowerVAphase1_Type()
)
imPM3Power1OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerVAphase1.setUnits("VA")
_ImPM3Power1OutputPowerKVAphase1_Type = Integer32
_ImPM3Power1OutputPowerKVAphase1_Object = MibScalar
imPM3Power1OutputPowerKVAphase1 = _ImPM3Power1OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 60),
    _ImPM3Power1OutputPowerKVAphase1_Type()
)
imPM3Power1OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM3Power1OutputVoltagePhase2_Type = Integer32
_ImPM3Power1OutputVoltagePhase2_Object = MibScalar
imPM3Power1OutputVoltagePhase2 = _ImPM3Power1OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 61),
    _ImPM3Power1OutputVoltagePhase2_Type()
)
imPM3Power1OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputVoltagePhase2.setUnits("0.1 V")
_ImPM3Power1OutputCurrentPhase2_Type = Integer32
_ImPM3Power1OutputCurrentPhase2_Object = MibScalar
imPM3Power1OutputCurrentPhase2 = _ImPM3Power1OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 62),
    _ImPM3Power1OutputCurrentPhase2_Type()
)
imPM3Power1OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputCurrentPhase2.setUnits("0.1 A")
_ImPM3Power1OutputPowerVAphase2_Type = Integer32
_ImPM3Power1OutputPowerVAphase2_Object = MibScalar
imPM3Power1OutputPowerVAphase2 = _ImPM3Power1OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 63),
    _ImPM3Power1OutputPowerVAphase2_Type()
)
imPM3Power1OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerVAphase2.setUnits("VA")
_ImPM3Power1OutputPowerKVAphase2_Type = Integer32
_ImPM3Power1OutputPowerKVAphase2_Object = MibScalar
imPM3Power1OutputPowerKVAphase2 = _ImPM3Power1OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 64),
    _ImPM3Power1OutputPowerKVAphase2_Type()
)
imPM3Power1OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM3Power1OutputVoltagePhase3_Type = Integer32
_ImPM3Power1OutputVoltagePhase3_Object = MibScalar
imPM3Power1OutputVoltagePhase3 = _ImPM3Power1OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 65),
    _ImPM3Power1OutputVoltagePhase3_Type()
)
imPM3Power1OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputVoltagePhase3.setUnits("0.1 V")
_ImPM3Power1OutputCurrentPhase3_Type = Integer32
_ImPM3Power1OutputCurrentPhase3_Object = MibScalar
imPM3Power1OutputCurrentPhase3 = _ImPM3Power1OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 66),
    _ImPM3Power1OutputCurrentPhase3_Type()
)
imPM3Power1OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputCurrentPhase3.setUnits("0.1 A")
_ImPM3Power1OutputPowerVAphase3_Type = Integer32
_ImPM3Power1OutputPowerVAphase3_Object = MibScalar
imPM3Power1OutputPowerVAphase3 = _ImPM3Power1OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 67),
    _ImPM3Power1OutputPowerVAphase3_Type()
)
imPM3Power1OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerVAphase3.setUnits("VA")
_ImPM3Power1OutputPowerKVAphase3_Type = Integer32
_ImPM3Power1OutputPowerKVAphase3_Object = MibScalar
imPM3Power1OutputPowerKVAphase3 = _ImPM3Power1OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 3, 68),
    _ImPM3Power1OutputPowerKVAphase3_Type()
)
imPM3Power1OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power1OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM3Power2_ObjectIdentity = ObjectIdentity
imPM3Power2 = _ImPM3Power2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4)
)


class _ImPM3Power2Manufacturer_Type(DisplayString):
    """Custom type imPM3Power2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM3Power2Manufacturer_Type.__name__ = "DisplayString"
_ImPM3Power2Manufacturer_Object = MibScalar
imPM3Power2Manufacturer = _ImPM3Power2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 1),
    _ImPM3Power2Manufacturer_Type()
)
imPM3Power2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Manufacturer.setStatus("current")


class _ImPM3Power2Type_Type(DisplayString):
    """Custom type imPM3Power2Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power2Type_Type.__name__ = "DisplayString"
_ImPM3Power2Type_Object = MibScalar
imPM3Power2Type = _ImPM3Power2Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 2),
    _ImPM3Power2Type_Type()
)
imPM3Power2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Type.setStatus("current")


class _ImPM3Power2serNumb_Type(DisplayString):
    """Custom type imPM3Power2serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power2serNumb_Type.__name__ = "DisplayString"
_ImPM3Power2serNumb_Object = MibScalar
imPM3Power2serNumb = _ImPM3Power2serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 3),
    _ImPM3Power2serNumb_Type()
)
imPM3Power2serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2serNumb.setStatus("current")


class _ImPM3Power2nextServiceDate_Type(DisplayString):
    """Custom type imPM3Power2nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power2nextServiceDate_Type.__name__ = "DisplayString"
_ImPM3Power2nextServiceDate_Object = MibScalar
imPM3Power2nextServiceDate = _ImPM3Power2nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 4),
    _ImPM3Power2nextServiceDate_Type()
)
imPM3Power2nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2nextServiceDate.setStatus("current")
_ImPM3Power2InputVoltage_Type = Integer32
_ImPM3Power2InputVoltage_Object = MibScalar
imPM3Power2InputVoltage = _ImPM3Power2InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 5),
    _ImPM3Power2InputVoltage_Type()
)
imPM3Power2InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputVoltage.setUnits("0.1 V")
_ImPM3Power2InputCurrent_Type = Integer32
_ImPM3Power2InputCurrent_Object = MibScalar
imPM3Power2InputCurrent = _ImPM3Power2InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 6),
    _ImPM3Power2InputCurrent_Type()
)
imPM3Power2InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputCurrent.setUnits("0.1 A")
_ImPM3Power2InputPowerVA_Type = Integer32
_ImPM3Power2InputPowerVA_Object = MibScalar
imPM3Power2InputPowerVA = _ImPM3Power2InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 7),
    _ImPM3Power2InputPowerVA_Type()
)
imPM3Power2InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerVA.setUnits("VA")
_ImPM3Power2InputPowerKVA_Type = Integer32
_ImPM3Power2InputPowerKVA_Object = MibScalar
imPM3Power2InputPowerKVA = _ImPM3Power2InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 8),
    _ImPM3Power2InputPowerKVA_Type()
)
imPM3Power2InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKVA.setUnits("0.1 kVA")
_ImPM3Power2InputPowerW_Type = Integer32
_ImPM3Power2InputPowerW_Object = MibScalar
imPM3Power2InputPowerW = _ImPM3Power2InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 9),
    _ImPM3Power2InputPowerW_Type()
)
imPM3Power2InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerW.setUnits("W")
_ImPM3Power2InputPowerKW_Type = Integer32
_ImPM3Power2InputPowerKW_Object = MibScalar
imPM3Power2InputPowerKW = _ImPM3Power2InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 10),
    _ImPM3Power2InputPowerKW_Type()
)
imPM3Power2InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKW.setUnits("0.1 kW")
_ImPM3Power2InputVoltagePhase1_Type = Integer32
_ImPM3Power2InputVoltagePhase1_Object = MibScalar
imPM3Power2InputVoltagePhase1 = _ImPM3Power2InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 11),
    _ImPM3Power2InputVoltagePhase1_Type()
)
imPM3Power2InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputVoltagePhase1.setUnits("0.1 V")
_ImPM3Power2InputCurrentPhase1_Type = Integer32
_ImPM3Power2InputCurrentPhase1_Object = MibScalar
imPM3Power2InputCurrentPhase1 = _ImPM3Power2InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 12),
    _ImPM3Power2InputCurrentPhase1_Type()
)
imPM3Power2InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputCurrentPhase1.setUnits("0.1 A")
_ImPM3Power2InputPowerVAphase1_Type = Integer32
_ImPM3Power2InputPowerVAphase1_Object = MibScalar
imPM3Power2InputPowerVAphase1 = _ImPM3Power2InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 13),
    _ImPM3Power2InputPowerVAphase1_Type()
)
imPM3Power2InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerVAphase1.setUnits("VA")
_ImPM3Power2InputPowerKVAphase1_Type = Integer32
_ImPM3Power2InputPowerKVAphase1_Object = MibScalar
imPM3Power2InputPowerKVAphase1 = _ImPM3Power2InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 14),
    _ImPM3Power2InputPowerKVAphase1_Type()
)
imPM3Power2InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM3Power2InputVoltagePhase2_Type = Integer32
_ImPM3Power2InputVoltagePhase2_Object = MibScalar
imPM3Power2InputVoltagePhase2 = _ImPM3Power2InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 15),
    _ImPM3Power2InputVoltagePhase2_Type()
)
imPM3Power2InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputVoltagePhase2.setUnits("0.1 V")
_ImPM3Power2InputCurrentPhase2_Type = Integer32
_ImPM3Power2InputCurrentPhase2_Object = MibScalar
imPM3Power2InputCurrentPhase2 = _ImPM3Power2InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 16),
    _ImPM3Power2InputCurrentPhase2_Type()
)
imPM3Power2InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputCurrentPhase2.setUnits("0.1 A")
_ImPM3Power2InputPowerVAphase2_Type = Integer32
_ImPM3Power2InputPowerVAphase2_Object = MibScalar
imPM3Power2InputPowerVAphase2 = _ImPM3Power2InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 17),
    _ImPM3Power2InputPowerVAphase2_Type()
)
imPM3Power2InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerVAphase2.setUnits("VA")
_ImPM3Power2InputPowerKVAphase2_Type = Integer32
_ImPM3Power2InputPowerKVAphase2_Object = MibScalar
imPM3Power2InputPowerKVAphase2 = _ImPM3Power2InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 18),
    _ImPM3Power2InputPowerKVAphase2_Type()
)
imPM3Power2InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM3Power2InputVoltagePhase3_Type = Integer32
_ImPM3Power2InputVoltagePhase3_Object = MibScalar
imPM3Power2InputVoltagePhase3 = _ImPM3Power2InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 19),
    _ImPM3Power2InputVoltagePhase3_Type()
)
imPM3Power2InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputVoltagePhase3.setUnits("0.1 V")
_ImPM3Power2InputCurrentPhase3_Type = Integer32
_ImPM3Power2InputCurrentPhase3_Object = MibScalar
imPM3Power2InputCurrentPhase3 = _ImPM3Power2InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 20),
    _ImPM3Power2InputCurrentPhase3_Type()
)
imPM3Power2InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputCurrentPhase3.setUnits("0.1 A")
_ImPM3Power2InputPowerVAphase3_Type = Integer32
_ImPM3Power2InputPowerVAphase3_Object = MibScalar
imPM3Power2InputPowerVAphase3 = _ImPM3Power2InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 21),
    _ImPM3Power2InputPowerVAphase3_Type()
)
imPM3Power2InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerVAphase3.setUnits("VA")
_ImPM3Power2InputPowerKVAphase3_Type = Integer32
_ImPM3Power2InputPowerKVAphase3_Object = MibScalar
imPM3Power2InputPowerKVAphase3 = _ImPM3Power2InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 22),
    _ImPM3Power2InputPowerKVAphase3_Type()
)
imPM3Power2InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM3Power2OutputVoltage_Type = Integer32
_ImPM3Power2OutputVoltage_Object = MibScalar
imPM3Power2OutputVoltage = _ImPM3Power2OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 23),
    _ImPM3Power2OutputVoltage_Type()
)
imPM3Power2OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputVoltage.setUnits("0.1 V")
_ImPM3Power2OutputCurrent_Type = Integer32
_ImPM3Power2OutputCurrent_Object = MibScalar
imPM3Power2OutputCurrent = _ImPM3Power2OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 24),
    _ImPM3Power2OutputCurrent_Type()
)
imPM3Power2OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputCurrent.setUnits("0.1 A")
_ImPM3Power2OutputPowerVA_Type = Integer32
_ImPM3Power2OutputPowerVA_Object = MibScalar
imPM3Power2OutputPowerVA = _ImPM3Power2OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 25),
    _ImPM3Power2OutputPowerVA_Type()
)
imPM3Power2OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerVA.setUnits("VA")
_ImPM3Power2OutputPowerKVA_Type = Integer32
_ImPM3Power2OutputPowerKVA_Object = MibScalar
imPM3Power2OutputPowerKVA = _ImPM3Power2OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 26),
    _ImPM3Power2OutputPowerKVA_Type()
)
imPM3Power2OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKVA.setUnits("0.1 kVA")
_ImPM3Power2OutputPowerW_Type = Integer32
_ImPM3Power2OutputPowerW_Object = MibScalar
imPM3Power2OutputPowerW = _ImPM3Power2OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 27),
    _ImPM3Power2OutputPowerW_Type()
)
imPM3Power2OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerW.setUnits("W")
_ImPM3Power2OutputPowerKW_Type = Integer32
_ImPM3Power2OutputPowerKW_Object = MibScalar
imPM3Power2OutputPowerKW = _ImPM3Power2OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 28),
    _ImPM3Power2OutputPowerKW_Type()
)
imPM3Power2OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKW.setUnits("0.1 kW")
_ImPM3Power2OutputLoad_Type = Integer32
_ImPM3Power2OutputLoad_Object = MibScalar
imPM3Power2OutputLoad = _ImPM3Power2OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 29),
    _ImPM3Power2OutputLoad_Type()
)
imPM3Power2OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputLoad.setUnits("%")
_ImPM3Power2OutputFrequency_Type = NonNegativeInteger
_ImPM3Power2OutputFrequency_Object = MibScalar
imPM3Power2OutputFrequency = _ImPM3Power2OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 30),
    _ImPM3Power2OutputFrequency_Type()
)
imPM3Power2OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputFrequency.setUnits("0.1 Hz")
_ImPM3Power2Temperature_Type = Integer32
_ImPM3Power2Temperature_Object = MibScalar
imPM3Power2Temperature = _ImPM3Power2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 31),
    _ImPM3Power2Temperature_Type()
)
imPM3Power2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2Temperature.setUnits("degrees Centigrade")


class _ImPM3Power2Running1_Type(Integer32):
    """Custom type imPM3Power2Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Running1_Type.__name__ = "Integer32"
_ImPM3Power2Running1_Object = MibScalar
imPM3Power2Running1 = _ImPM3Power2Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 32),
    _ImPM3Power2Running1_Type()
)
imPM3Power2Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Running1.setStatus("current")


class _ImPM3Power2Running2_Type(Integer32):
    """Custom type imPM3Power2Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Running2_Type.__name__ = "Integer32"
_ImPM3Power2Running2_Object = MibScalar
imPM3Power2Running2 = _ImPM3Power2Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 33),
    _ImPM3Power2Running2_Type()
)
imPM3Power2Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Running2.setStatus("current")


class _ImPM3Power2Running3_Type(Integer32):
    """Custom type imPM3Power2Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Running3_Type.__name__ = "Integer32"
_ImPM3Power2Running3_Object = MibScalar
imPM3Power2Running3 = _ImPM3Power2Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 34),
    _ImPM3Power2Running3_Type()
)
imPM3Power2Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Running3.setStatus("current")


class _ImPM3Power2Running4_Type(Integer32):
    """Custom type imPM3Power2Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Running4_Type.__name__ = "Integer32"
_ImPM3Power2Running4_Object = MibScalar
imPM3Power2Running4 = _ImPM3Power2Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 35),
    _ImPM3Power2Running4_Type()
)
imPM3Power2Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Running4.setStatus("current")


class _ImPM3Power2Running5_Type(Integer32):
    """Custom type imPM3Power2Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Running5_Type.__name__ = "Integer32"
_ImPM3Power2Running5_Object = MibScalar
imPM3Power2Running5 = _ImPM3Power2Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 36),
    _ImPM3Power2Running5_Type()
)
imPM3Power2Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Running5.setStatus("current")


class _ImPM3Power2Running6_Type(Integer32):
    """Custom type imPM3Power2Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Running6_Type.__name__ = "Integer32"
_ImPM3Power2Running6_Object = MibScalar
imPM3Power2Running6 = _ImPM3Power2Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 37),
    _ImPM3Power2Running6_Type()
)
imPM3Power2Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Running6.setStatus("current")


class _ImPM3Power2Running7_Type(Integer32):
    """Custom type imPM3Power2Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Running7_Type.__name__ = "Integer32"
_ImPM3Power2Running7_Object = MibScalar
imPM3Power2Running7 = _ImPM3Power2Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 38),
    _ImPM3Power2Running7_Type()
)
imPM3Power2Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Running7.setStatus("current")


class _ImPM3Power2Running8_Type(Integer32):
    """Custom type imPM3Power2Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Running8_Type.__name__ = "Integer32"
_ImPM3Power2Running8_Object = MibScalar
imPM3Power2Running8 = _ImPM3Power2Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 39),
    _ImPM3Power2Running8_Type()
)
imPM3Power2Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Running8.setStatus("current")


class _ImPM3Power2InputFuse_Type(Integer32):
    """Custom type imPM3Power2InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputFuse_Type.__name__ = "Integer32"
_ImPM3Power2InputFuse_Object = MibScalar
imPM3Power2InputFuse = _ImPM3Power2InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 40),
    _ImPM3Power2InputFuse_Type()
)
imPM3Power2InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputFuse.setStatus("current")


class _ImPM3Power2InputFuse1_Type(Integer32):
    """Custom type imPM3Power2InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputFuse1_Type.__name__ = "Integer32"
_ImPM3Power2InputFuse1_Object = MibScalar
imPM3Power2InputFuse1 = _ImPM3Power2InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 41),
    _ImPM3Power2InputFuse1_Type()
)
imPM3Power2InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputFuse1.setStatus("current")


class _ImPM3Power2InputFuse2_Type(Integer32):
    """Custom type imPM3Power2InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputFuse2_Type.__name__ = "Integer32"
_ImPM3Power2InputFuse2_Object = MibScalar
imPM3Power2InputFuse2 = _ImPM3Power2InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 42),
    _ImPM3Power2InputFuse2_Type()
)
imPM3Power2InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputFuse2.setStatus("current")


class _ImPM3Power2InputFuse3_Type(Integer32):
    """Custom type imPM3Power2InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputFuse3_Type.__name__ = "Integer32"
_ImPM3Power2InputFuse3_Object = MibScalar
imPM3Power2InputFuse3 = _ImPM3Power2InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 43),
    _ImPM3Power2InputFuse3_Type()
)
imPM3Power2InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputFuse3.setStatus("current")


class _ImPM3Power2InputBreaker_Type(Integer32):
    """Custom type imPM3Power2InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputBreaker_Type.__name__ = "Integer32"
_ImPM3Power2InputBreaker_Object = MibScalar
imPM3Power2InputBreaker = _ImPM3Power2InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 44),
    _ImPM3Power2InputBreaker_Type()
)
imPM3Power2InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputBreaker.setStatus("current")


class _ImPM3Power2InputBreaker1_Type(Integer32):
    """Custom type imPM3Power2InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputBreaker1_Type.__name__ = "Integer32"
_ImPM3Power2InputBreaker1_Object = MibScalar
imPM3Power2InputBreaker1 = _ImPM3Power2InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 45),
    _ImPM3Power2InputBreaker1_Type()
)
imPM3Power2InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputBreaker1.setStatus("current")


class _ImPM3Power2InputBreaker2_Type(Integer32):
    """Custom type imPM3Power2InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputBreaker2_Type.__name__ = "Integer32"
_ImPM3Power2InputBreaker2_Object = MibScalar
imPM3Power2InputBreaker2 = _ImPM3Power2InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 46),
    _ImPM3Power2InputBreaker2_Type()
)
imPM3Power2InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputBreaker2.setStatus("current")


class _ImPM3Power2InputBreaker3_Type(Integer32):
    """Custom type imPM3Power2InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputBreaker3_Type.__name__ = "Integer32"
_ImPM3Power2InputBreaker3_Object = MibScalar
imPM3Power2InputBreaker3 = _ImPM3Power2InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 47),
    _ImPM3Power2InputBreaker3_Type()
)
imPM3Power2InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputBreaker3.setStatus("current")


class _ImPM3Power2InputSurgeArrester_Type(Integer32):
    """Custom type imPM3Power2InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM3Power2InputSurgeArrester_Object = MibScalar
imPM3Power2InputSurgeArrester = _ImPM3Power2InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 48),
    _ImPM3Power2InputSurgeArrester_Type()
)
imPM3Power2InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2InputSurgeArrester.setStatus("current")


class _ImPM3Power2OutputFuse_Type(Integer32):
    """Custom type imPM3Power2OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2OutputFuse_Type.__name__ = "Integer32"
_ImPM3Power2OutputFuse_Object = MibScalar
imPM3Power2OutputFuse = _ImPM3Power2OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 49),
    _ImPM3Power2OutputFuse_Type()
)
imPM3Power2OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputFuse.setStatus("current")


class _ImPM3Power2OutputFuse1_Type(Integer32):
    """Custom type imPM3Power2OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2OutputFuse1_Type.__name__ = "Integer32"
_ImPM3Power2OutputFuse1_Object = MibScalar
imPM3Power2OutputFuse1 = _ImPM3Power2OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 50),
    _ImPM3Power2OutputFuse1_Type()
)
imPM3Power2OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputFuse1.setStatus("current")


class _ImPM3Power2OutputFuse2_Type(Integer32):
    """Custom type imPM3Power2OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2OutputFuse2_Type.__name__ = "Integer32"
_ImPM3Power2OutputFuse2_Object = MibScalar
imPM3Power2OutputFuse2 = _ImPM3Power2OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 51),
    _ImPM3Power2OutputFuse2_Type()
)
imPM3Power2OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputFuse2.setStatus("current")


class _ImPM3Power2OutputBreaker_Type(Integer32):
    """Custom type imPM3Power2OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2OutputBreaker_Type.__name__ = "Integer32"
_ImPM3Power2OutputBreaker_Object = MibScalar
imPM3Power2OutputBreaker = _ImPM3Power2OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 52),
    _ImPM3Power2OutputBreaker_Type()
)
imPM3Power2OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputBreaker.setStatus("current")


class _ImPM3Power2OutputBreaker1_Type(Integer32):
    """Custom type imPM3Power2OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2OutputBreaker1_Type.__name__ = "Integer32"
_ImPM3Power2OutputBreaker1_Object = MibScalar
imPM3Power2OutputBreaker1 = _ImPM3Power2OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 53),
    _ImPM3Power2OutputBreaker1_Type()
)
imPM3Power2OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputBreaker1.setStatus("current")


class _ImPM3Power2OutputBreaker2_Type(Integer32):
    """Custom type imPM3Power2OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2OutputBreaker2_Type.__name__ = "Integer32"
_ImPM3Power2OutputBreaker2_Object = MibScalar
imPM3Power2OutputBreaker2 = _ImPM3Power2OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 54),
    _ImPM3Power2OutputBreaker2_Type()
)
imPM3Power2OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputBreaker2.setStatus("current")


class _ImPM3Power2Fan_Type(Integer32):
    """Custom type imPM3Power2Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2Fan_Type.__name__ = "Integer32"
_ImPM3Power2Fan_Object = MibScalar
imPM3Power2Fan = _ImPM3Power2Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 55),
    _ImPM3Power2Fan_Type()
)
imPM3Power2Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2Fan.setStatus("current")


class _ImPM3Power2BatteryAvailable_Type(Integer32):
    """Custom type imPM3Power2BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power2BatteryAvailable_Type.__name__ = "Integer32"
_ImPM3Power2BatteryAvailable_Object = MibScalar
imPM3Power2BatteryAvailable = _ImPM3Power2BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 56),
    _ImPM3Power2BatteryAvailable_Type()
)
imPM3Power2BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2BatteryAvailable.setStatus("current")
_ImPM3Power2OutputVoltagePhase1_Type = Integer32
_ImPM3Power2OutputVoltagePhase1_Object = MibScalar
imPM3Power2OutputVoltagePhase1 = _ImPM3Power2OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 57),
    _ImPM3Power2OutputVoltagePhase1_Type()
)
imPM3Power2OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputVoltagePhase1.setUnits("0.1 V")
_ImPM3Power2OutputCurrentPhase1_Type = Integer32
_ImPM3Power2OutputCurrentPhase1_Object = MibScalar
imPM3Power2OutputCurrentPhase1 = _ImPM3Power2OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 58),
    _ImPM3Power2OutputCurrentPhase1_Type()
)
imPM3Power2OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputCurrentPhase1.setUnits("0.1 A")
_ImPM3Power2OutputPowerVAphase1_Type = Integer32
_ImPM3Power2OutputPowerVAphase1_Object = MibScalar
imPM3Power2OutputPowerVAphase1 = _ImPM3Power2OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 59),
    _ImPM3Power2OutputPowerVAphase1_Type()
)
imPM3Power2OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerVAphase1.setUnits("VA")
_ImPM3Power2OutputPowerKVAphase1_Type = Integer32
_ImPM3Power2OutputPowerKVAphase1_Object = MibScalar
imPM3Power2OutputPowerKVAphase1 = _ImPM3Power2OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 60),
    _ImPM3Power2OutputPowerKVAphase1_Type()
)
imPM3Power2OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM3Power2OutputVoltagePhase2_Type = Integer32
_ImPM3Power2OutputVoltagePhase2_Object = MibScalar
imPM3Power2OutputVoltagePhase2 = _ImPM3Power2OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 61),
    _ImPM3Power2OutputVoltagePhase2_Type()
)
imPM3Power2OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputVoltagePhase2.setUnits("0.1 V")
_ImPM3Power2OutputCurrentPhase2_Type = Integer32
_ImPM3Power2OutputCurrentPhase2_Object = MibScalar
imPM3Power2OutputCurrentPhase2 = _ImPM3Power2OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 62),
    _ImPM3Power2OutputCurrentPhase2_Type()
)
imPM3Power2OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputCurrentPhase2.setUnits("0.1 A")
_ImPM3Power2OutputPowerVAphase2_Type = Integer32
_ImPM3Power2OutputPowerVAphase2_Object = MibScalar
imPM3Power2OutputPowerVAphase2 = _ImPM3Power2OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 63),
    _ImPM3Power2OutputPowerVAphase2_Type()
)
imPM3Power2OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerVAphase2.setUnits("VA")
_ImPM3Power2OutputPowerKVAphase2_Type = Integer32
_ImPM3Power2OutputPowerKVAphase2_Object = MibScalar
imPM3Power2OutputPowerKVAphase2 = _ImPM3Power2OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 64),
    _ImPM3Power2OutputPowerKVAphase2_Type()
)
imPM3Power2OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM3Power2OutputVoltagePhase3_Type = Integer32
_ImPM3Power2OutputVoltagePhase3_Object = MibScalar
imPM3Power2OutputVoltagePhase3 = _ImPM3Power2OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 65),
    _ImPM3Power2OutputVoltagePhase3_Type()
)
imPM3Power2OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputVoltagePhase3.setUnits("0.1 V")
_ImPM3Power2OutputCurrentPhase3_Type = Integer32
_ImPM3Power2OutputCurrentPhase3_Object = MibScalar
imPM3Power2OutputCurrentPhase3 = _ImPM3Power2OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 66),
    _ImPM3Power2OutputCurrentPhase3_Type()
)
imPM3Power2OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputCurrentPhase3.setUnits("0.1 A")
_ImPM3Power2OutputPowerVAphase3_Type = Integer32
_ImPM3Power2OutputPowerVAphase3_Object = MibScalar
imPM3Power2OutputPowerVAphase3 = _ImPM3Power2OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 67),
    _ImPM3Power2OutputPowerVAphase3_Type()
)
imPM3Power2OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerVAphase3.setUnits("VA")
_ImPM3Power2OutputPowerKVAphase3_Type = Integer32
_ImPM3Power2OutputPowerKVAphase3_Object = MibScalar
imPM3Power2OutputPowerKVAphase3 = _ImPM3Power2OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 4, 68),
    _ImPM3Power2OutputPowerKVAphase3_Type()
)
imPM3Power2OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power2OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM3Power3_ObjectIdentity = ObjectIdentity
imPM3Power3 = _ImPM3Power3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5)
)


class _ImPM3Power3Manufacturer_Type(DisplayString):
    """Custom type imPM3Power3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM3Power3Manufacturer_Type.__name__ = "DisplayString"
_ImPM3Power3Manufacturer_Object = MibScalar
imPM3Power3Manufacturer = _ImPM3Power3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 1),
    _ImPM3Power3Manufacturer_Type()
)
imPM3Power3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Manufacturer.setStatus("current")


class _ImPM3Power3Type_Type(DisplayString):
    """Custom type imPM3Power3Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power3Type_Type.__name__ = "DisplayString"
_ImPM3Power3Type_Object = MibScalar
imPM3Power3Type = _ImPM3Power3Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 2),
    _ImPM3Power3Type_Type()
)
imPM3Power3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Type.setStatus("current")


class _ImPM3Power3serNumb_Type(DisplayString):
    """Custom type imPM3Power3serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power3serNumb_Type.__name__ = "DisplayString"
_ImPM3Power3serNumb_Object = MibScalar
imPM3Power3serNumb = _ImPM3Power3serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 3),
    _ImPM3Power3serNumb_Type()
)
imPM3Power3serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3serNumb.setStatus("current")


class _ImPM3Power3nextServiceDate_Type(DisplayString):
    """Custom type imPM3Power3nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3Power3nextServiceDate_Type.__name__ = "DisplayString"
_ImPM3Power3nextServiceDate_Object = MibScalar
imPM3Power3nextServiceDate = _ImPM3Power3nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 4),
    _ImPM3Power3nextServiceDate_Type()
)
imPM3Power3nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3nextServiceDate.setStatus("current")
_ImPM3Power3InputVoltage_Type = Integer32
_ImPM3Power3InputVoltage_Object = MibScalar
imPM3Power3InputVoltage = _ImPM3Power3InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 5),
    _ImPM3Power3InputVoltage_Type()
)
imPM3Power3InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputVoltage.setUnits("0.1 V")
_ImPM3Power3InputCurrent_Type = Integer32
_ImPM3Power3InputCurrent_Object = MibScalar
imPM3Power3InputCurrent = _ImPM3Power3InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 6),
    _ImPM3Power3InputCurrent_Type()
)
imPM3Power3InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputCurrent.setUnits("0.1 A")
_ImPM3Power3InputPowerVA_Type = Integer32
_ImPM3Power3InputPowerVA_Object = MibScalar
imPM3Power3InputPowerVA = _ImPM3Power3InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 7),
    _ImPM3Power3InputPowerVA_Type()
)
imPM3Power3InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerVA.setUnits("VA")
_ImPM3Power3InputPowerKVA_Type = Integer32
_ImPM3Power3InputPowerKVA_Object = MibScalar
imPM3Power3InputPowerKVA = _ImPM3Power3InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 8),
    _ImPM3Power3InputPowerKVA_Type()
)
imPM3Power3InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKVA.setUnits("0.1 kVA")
_ImPM3Power3InputPowerW_Type = Integer32
_ImPM3Power3InputPowerW_Object = MibScalar
imPM3Power3InputPowerW = _ImPM3Power3InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 9),
    _ImPM3Power3InputPowerW_Type()
)
imPM3Power3InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerW.setUnits("W")
_ImPM3Power3InputPowerKW_Type = Integer32
_ImPM3Power3InputPowerKW_Object = MibScalar
imPM3Power3InputPowerKW = _ImPM3Power3InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 10),
    _ImPM3Power3InputPowerKW_Type()
)
imPM3Power3InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKW.setUnits("0.1 kW")
_ImPM3Power3InputVoltagePhase1_Type = Integer32
_ImPM3Power3InputVoltagePhase1_Object = MibScalar
imPM3Power3InputVoltagePhase1 = _ImPM3Power3InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 11),
    _ImPM3Power3InputVoltagePhase1_Type()
)
imPM3Power3InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputVoltagePhase1.setUnits("0.1 V")
_ImPM3Power3InputCurrentPhase1_Type = Integer32
_ImPM3Power3InputCurrentPhase1_Object = MibScalar
imPM3Power3InputCurrentPhase1 = _ImPM3Power3InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 12),
    _ImPM3Power3InputCurrentPhase1_Type()
)
imPM3Power3InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputCurrentPhase1.setUnits("0.1 A")
_ImPM3Power3InputPowerVAphase1_Type = Integer32
_ImPM3Power3InputPowerVAphase1_Object = MibScalar
imPM3Power3InputPowerVAphase1 = _ImPM3Power3InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 13),
    _ImPM3Power3InputPowerVAphase1_Type()
)
imPM3Power3InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerVAphase1.setUnits("VA")
_ImPM3Power3InputPowerKVAphase1_Type = Integer32
_ImPM3Power3InputPowerKVAphase1_Object = MibScalar
imPM3Power3InputPowerKVAphase1 = _ImPM3Power3InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 14),
    _ImPM3Power3InputPowerKVAphase1_Type()
)
imPM3Power3InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM3Power3InputVoltagePhase2_Type = Integer32
_ImPM3Power3InputVoltagePhase2_Object = MibScalar
imPM3Power3InputVoltagePhase2 = _ImPM3Power3InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 15),
    _ImPM3Power3InputVoltagePhase2_Type()
)
imPM3Power3InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputVoltagePhase2.setUnits("0.1 V")
_ImPM3Power3InputCurrentPhase2_Type = Integer32
_ImPM3Power3InputCurrentPhase2_Object = MibScalar
imPM3Power3InputCurrentPhase2 = _ImPM3Power3InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 16),
    _ImPM3Power3InputCurrentPhase2_Type()
)
imPM3Power3InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputCurrentPhase2.setUnits("0.1 A")
_ImPM3Power3InputPowerVAphase2_Type = Integer32
_ImPM3Power3InputPowerVAphase2_Object = MibScalar
imPM3Power3InputPowerVAphase2 = _ImPM3Power3InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 17),
    _ImPM3Power3InputPowerVAphase2_Type()
)
imPM3Power3InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerVAphase2.setUnits("VA")
_ImPM3Power3InputPowerKVAphase2_Type = Integer32
_ImPM3Power3InputPowerKVAphase2_Object = MibScalar
imPM3Power3InputPowerKVAphase2 = _ImPM3Power3InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 18),
    _ImPM3Power3InputPowerKVAphase2_Type()
)
imPM3Power3InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM3Power3InputVoltagePhase3_Type = Integer32
_ImPM3Power3InputVoltagePhase3_Object = MibScalar
imPM3Power3InputVoltagePhase3 = _ImPM3Power3InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 19),
    _ImPM3Power3InputVoltagePhase3_Type()
)
imPM3Power3InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputVoltagePhase3.setUnits("0.1 V")
_ImPM3Power3InputCurrentPhase3_Type = Integer32
_ImPM3Power3InputCurrentPhase3_Object = MibScalar
imPM3Power3InputCurrentPhase3 = _ImPM3Power3InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 20),
    _ImPM3Power3InputCurrentPhase3_Type()
)
imPM3Power3InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputCurrentPhase3.setUnits("0.1 A")
_ImPM3Power3InputPowerVAphase3_Type = Integer32
_ImPM3Power3InputPowerVAphase3_Object = MibScalar
imPM3Power3InputPowerVAphase3 = _ImPM3Power3InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 21),
    _ImPM3Power3InputPowerVAphase3_Type()
)
imPM3Power3InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerVAphase3.setUnits("VA")
_ImPM3Power3InputPowerKVAphase3_Type = Integer32
_ImPM3Power3InputPowerKVAphase3_Object = MibScalar
imPM3Power3InputPowerKVAphase3 = _ImPM3Power3InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 22),
    _ImPM3Power3InputPowerKVAphase3_Type()
)
imPM3Power3InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM3Power3OutputVoltage_Type = Integer32
_ImPM3Power3OutputVoltage_Object = MibScalar
imPM3Power3OutputVoltage = _ImPM3Power3OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 23),
    _ImPM3Power3OutputVoltage_Type()
)
imPM3Power3OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputVoltage.setUnits("0.1 V")
_ImPM3Power3OutputCurrent_Type = Integer32
_ImPM3Power3OutputCurrent_Object = MibScalar
imPM3Power3OutputCurrent = _ImPM3Power3OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 24),
    _ImPM3Power3OutputCurrent_Type()
)
imPM3Power3OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputCurrent.setUnits("0.1 A")
_ImPM3Power3OutputPowerVA_Type = Integer32
_ImPM3Power3OutputPowerVA_Object = MibScalar
imPM3Power3OutputPowerVA = _ImPM3Power3OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 25),
    _ImPM3Power3OutputPowerVA_Type()
)
imPM3Power3OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerVA.setUnits("VA")
_ImPM3Power3OutputPowerKVA_Type = Integer32
_ImPM3Power3OutputPowerKVA_Object = MibScalar
imPM3Power3OutputPowerKVA = _ImPM3Power3OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 26),
    _ImPM3Power3OutputPowerKVA_Type()
)
imPM3Power3OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKVA.setUnits("0.1 kVA")
_ImPM3Power3OutputPowerW_Type = Integer32
_ImPM3Power3OutputPowerW_Object = MibScalar
imPM3Power3OutputPowerW = _ImPM3Power3OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 27),
    _ImPM3Power3OutputPowerW_Type()
)
imPM3Power3OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerW.setUnits("W")
_ImPM3Power3OutputPowerKW_Type = Integer32
_ImPM3Power3OutputPowerKW_Object = MibScalar
imPM3Power3OutputPowerKW = _ImPM3Power3OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 28),
    _ImPM3Power3OutputPowerKW_Type()
)
imPM3Power3OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKW.setUnits("0.1 kW")
_ImPM3Power3OutputLoad_Type = Integer32
_ImPM3Power3OutputLoad_Object = MibScalar
imPM3Power3OutputLoad = _ImPM3Power3OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 29),
    _ImPM3Power3OutputLoad_Type()
)
imPM3Power3OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputLoad.setUnits("%")
_ImPM3Power3OutputFrequency_Type = NonNegativeInteger
_ImPM3Power3OutputFrequency_Object = MibScalar
imPM3Power3OutputFrequency = _ImPM3Power3OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 30),
    _ImPM3Power3OutputFrequency_Type()
)
imPM3Power3OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputFrequency.setUnits("0.1 Hz")
_ImPM3Power3Temperature_Type = Integer32
_ImPM3Power3Temperature_Object = MibScalar
imPM3Power3Temperature = _ImPM3Power3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 31),
    _ImPM3Power3Temperature_Type()
)
imPM3Power3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3Temperature.setUnits("degrees Centigrade")


class _ImPM3Power3Running1_Type(Integer32):
    """Custom type imPM3Power3Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Running1_Type.__name__ = "Integer32"
_ImPM3Power3Running1_Object = MibScalar
imPM3Power3Running1 = _ImPM3Power3Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 32),
    _ImPM3Power3Running1_Type()
)
imPM3Power3Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Running1.setStatus("current")


class _ImPM3Power3Running2_Type(Integer32):
    """Custom type imPM3Power3Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Running2_Type.__name__ = "Integer32"
_ImPM3Power3Running2_Object = MibScalar
imPM3Power3Running2 = _ImPM3Power3Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 33),
    _ImPM3Power3Running2_Type()
)
imPM3Power3Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Running2.setStatus("current")


class _ImPM3Power3Running3_Type(Integer32):
    """Custom type imPM3Power3Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Running3_Type.__name__ = "Integer32"
_ImPM3Power3Running3_Object = MibScalar
imPM3Power3Running3 = _ImPM3Power3Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 34),
    _ImPM3Power3Running3_Type()
)
imPM3Power3Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Running3.setStatus("current")


class _ImPM3Power3Running4_Type(Integer32):
    """Custom type imPM3Power3Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Running4_Type.__name__ = "Integer32"
_ImPM3Power3Running4_Object = MibScalar
imPM3Power3Running4 = _ImPM3Power3Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 35),
    _ImPM3Power3Running4_Type()
)
imPM3Power3Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Running4.setStatus("current")


class _ImPM3Power3Running5_Type(Integer32):
    """Custom type imPM3Power3Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Running5_Type.__name__ = "Integer32"
_ImPM3Power3Running5_Object = MibScalar
imPM3Power3Running5 = _ImPM3Power3Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 36),
    _ImPM3Power3Running5_Type()
)
imPM3Power3Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Running5.setStatus("current")


class _ImPM3Power3Running6_Type(Integer32):
    """Custom type imPM3Power3Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Running6_Type.__name__ = "Integer32"
_ImPM3Power3Running6_Object = MibScalar
imPM3Power3Running6 = _ImPM3Power3Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 37),
    _ImPM3Power3Running6_Type()
)
imPM3Power3Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Running6.setStatus("current")


class _ImPM3Power3Running7_Type(Integer32):
    """Custom type imPM3Power3Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Running7_Type.__name__ = "Integer32"
_ImPM3Power3Running7_Object = MibScalar
imPM3Power3Running7 = _ImPM3Power3Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 38),
    _ImPM3Power3Running7_Type()
)
imPM3Power3Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Running7.setStatus("current")


class _ImPM3Power3Running8_Type(Integer32):
    """Custom type imPM3Power3Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Running8_Type.__name__ = "Integer32"
_ImPM3Power3Running8_Object = MibScalar
imPM3Power3Running8 = _ImPM3Power3Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 39),
    _ImPM3Power3Running8_Type()
)
imPM3Power3Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Running8.setStatus("current")


class _ImPM3Power3InputFuse_Type(Integer32):
    """Custom type imPM3Power3InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputFuse_Type.__name__ = "Integer32"
_ImPM3Power3InputFuse_Object = MibScalar
imPM3Power3InputFuse = _ImPM3Power3InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 40),
    _ImPM3Power3InputFuse_Type()
)
imPM3Power3InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputFuse.setStatus("current")


class _ImPM3Power3InputFuse1_Type(Integer32):
    """Custom type imPM3Power3InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputFuse1_Type.__name__ = "Integer32"
_ImPM3Power3InputFuse1_Object = MibScalar
imPM3Power3InputFuse1 = _ImPM3Power3InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 41),
    _ImPM3Power3InputFuse1_Type()
)
imPM3Power3InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputFuse1.setStatus("current")


class _ImPM3Power3InputFuse2_Type(Integer32):
    """Custom type imPM3Power3InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputFuse2_Type.__name__ = "Integer32"
_ImPM3Power3InputFuse2_Object = MibScalar
imPM3Power3InputFuse2 = _ImPM3Power3InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 42),
    _ImPM3Power3InputFuse2_Type()
)
imPM3Power3InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputFuse2.setStatus("current")


class _ImPM3Power3InputFuse3_Type(Integer32):
    """Custom type imPM3Power3InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputFuse3_Type.__name__ = "Integer32"
_ImPM3Power3InputFuse3_Object = MibScalar
imPM3Power3InputFuse3 = _ImPM3Power3InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 43),
    _ImPM3Power3InputFuse3_Type()
)
imPM3Power3InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputFuse3.setStatus("current")


class _ImPM3Power3InputBreaker_Type(Integer32):
    """Custom type imPM3Power3InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputBreaker_Type.__name__ = "Integer32"
_ImPM3Power3InputBreaker_Object = MibScalar
imPM3Power3InputBreaker = _ImPM3Power3InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 44),
    _ImPM3Power3InputBreaker_Type()
)
imPM3Power3InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputBreaker.setStatus("current")


class _ImPM3Power3InputBreaker1_Type(Integer32):
    """Custom type imPM3Power3InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputBreaker1_Type.__name__ = "Integer32"
_ImPM3Power3InputBreaker1_Object = MibScalar
imPM3Power3InputBreaker1 = _ImPM3Power3InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 45),
    _ImPM3Power3InputBreaker1_Type()
)
imPM3Power3InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputBreaker1.setStatus("current")


class _ImPM3Power3InputBreaker2_Type(Integer32):
    """Custom type imPM3Power3InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputBreaker2_Type.__name__ = "Integer32"
_ImPM3Power3InputBreaker2_Object = MibScalar
imPM3Power3InputBreaker2 = _ImPM3Power3InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 46),
    _ImPM3Power3InputBreaker2_Type()
)
imPM3Power3InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputBreaker2.setStatus("current")


class _ImPM3Power3InputBreaker3_Type(Integer32):
    """Custom type imPM3Power3InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputBreaker3_Type.__name__ = "Integer32"
_ImPM3Power3InputBreaker3_Object = MibScalar
imPM3Power3InputBreaker3 = _ImPM3Power3InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 47),
    _ImPM3Power3InputBreaker3_Type()
)
imPM3Power3InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputBreaker3.setStatus("current")


class _ImPM3Power3InputSurgeArrester_Type(Integer32):
    """Custom type imPM3Power3InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM3Power3InputSurgeArrester_Object = MibScalar
imPM3Power3InputSurgeArrester = _ImPM3Power3InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 48),
    _ImPM3Power3InputSurgeArrester_Type()
)
imPM3Power3InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3InputSurgeArrester.setStatus("current")


class _ImPM3Power3OutputFuse_Type(Integer32):
    """Custom type imPM3Power3OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3OutputFuse_Type.__name__ = "Integer32"
_ImPM3Power3OutputFuse_Object = MibScalar
imPM3Power3OutputFuse = _ImPM3Power3OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 49),
    _ImPM3Power3OutputFuse_Type()
)
imPM3Power3OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputFuse.setStatus("current")


class _ImPM3Power3OutputFuse1_Type(Integer32):
    """Custom type imPM3Power3OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3OutputFuse1_Type.__name__ = "Integer32"
_ImPM3Power3OutputFuse1_Object = MibScalar
imPM3Power3OutputFuse1 = _ImPM3Power3OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 50),
    _ImPM3Power3OutputFuse1_Type()
)
imPM3Power3OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputFuse1.setStatus("current")


class _ImPM3Power3OutputFuse2_Type(Integer32):
    """Custom type imPM3Power3OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3OutputFuse2_Type.__name__ = "Integer32"
_ImPM3Power3OutputFuse2_Object = MibScalar
imPM3Power3OutputFuse2 = _ImPM3Power3OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 51),
    _ImPM3Power3OutputFuse2_Type()
)
imPM3Power3OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputFuse2.setStatus("current")


class _ImPM3Power3OutputBreaker_Type(Integer32):
    """Custom type imPM3Power3OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3OutputBreaker_Type.__name__ = "Integer32"
_ImPM3Power3OutputBreaker_Object = MibScalar
imPM3Power3OutputBreaker = _ImPM3Power3OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 52),
    _ImPM3Power3OutputBreaker_Type()
)
imPM3Power3OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputBreaker.setStatus("current")


class _ImPM3Power3OutputBreaker1_Type(Integer32):
    """Custom type imPM3Power3OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3OutputBreaker1_Type.__name__ = "Integer32"
_ImPM3Power3OutputBreaker1_Object = MibScalar
imPM3Power3OutputBreaker1 = _ImPM3Power3OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 53),
    _ImPM3Power3OutputBreaker1_Type()
)
imPM3Power3OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputBreaker1.setStatus("current")


class _ImPM3Power3OutputBreaker2_Type(Integer32):
    """Custom type imPM3Power3OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3OutputBreaker2_Type.__name__ = "Integer32"
_ImPM3Power3OutputBreaker2_Object = MibScalar
imPM3Power3OutputBreaker2 = _ImPM3Power3OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 54),
    _ImPM3Power3OutputBreaker2_Type()
)
imPM3Power3OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputBreaker2.setStatus("current")


class _ImPM3Power3Fan_Type(Integer32):
    """Custom type imPM3Power3Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3Fan_Type.__name__ = "Integer32"
_ImPM3Power3Fan_Object = MibScalar
imPM3Power3Fan = _ImPM3Power3Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 55),
    _ImPM3Power3Fan_Type()
)
imPM3Power3Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3Fan.setStatus("current")


class _ImPM3Power3BatteryAvailable_Type(Integer32):
    """Custom type imPM3Power3BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3Power3BatteryAvailable_Type.__name__ = "Integer32"
_ImPM3Power3BatteryAvailable_Object = MibScalar
imPM3Power3BatteryAvailable = _ImPM3Power3BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 56),
    _ImPM3Power3BatteryAvailable_Type()
)
imPM3Power3BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3BatteryAvailable.setStatus("current")
_ImPM3Power3OutputVoltagePhase1_Type = Integer32
_ImPM3Power3OutputVoltagePhase1_Object = MibScalar
imPM3Power3OutputVoltagePhase1 = _ImPM3Power3OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 57),
    _ImPM3Power3OutputVoltagePhase1_Type()
)
imPM3Power3OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputVoltagePhase1.setUnits("0.1 V")
_ImPM3Power3OutputCurrentPhase1_Type = Integer32
_ImPM3Power3OutputCurrentPhase1_Object = MibScalar
imPM3Power3OutputCurrentPhase1 = _ImPM3Power3OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 58),
    _ImPM3Power3OutputCurrentPhase1_Type()
)
imPM3Power3OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputCurrentPhase1.setUnits("0.1 A")
_ImPM3Power3OutputPowerVAphase1_Type = Integer32
_ImPM3Power3OutputPowerVAphase1_Object = MibScalar
imPM3Power3OutputPowerVAphase1 = _ImPM3Power3OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 59),
    _ImPM3Power3OutputPowerVAphase1_Type()
)
imPM3Power3OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerVAphase1.setUnits("VA")
_ImPM3Power3OutputPowerKVAphase1_Type = Integer32
_ImPM3Power3OutputPowerKVAphase1_Object = MibScalar
imPM3Power3OutputPowerKVAphase1 = _ImPM3Power3OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 60),
    _ImPM3Power3OutputPowerKVAphase1_Type()
)
imPM3Power3OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM3Power3OutputVoltagePhase2_Type = Integer32
_ImPM3Power3OutputVoltagePhase2_Object = MibScalar
imPM3Power3OutputVoltagePhase2 = _ImPM3Power3OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 61),
    _ImPM3Power3OutputVoltagePhase2_Type()
)
imPM3Power3OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputVoltagePhase2.setUnits("0.1 V")
_ImPM3Power3OutputCurrentPhase2_Type = Integer32
_ImPM3Power3OutputCurrentPhase2_Object = MibScalar
imPM3Power3OutputCurrentPhase2 = _ImPM3Power3OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 62),
    _ImPM3Power3OutputCurrentPhase2_Type()
)
imPM3Power3OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputCurrentPhase2.setUnits("0.1 A")
_ImPM3Power3OutputPowerVAphase2_Type = Integer32
_ImPM3Power3OutputPowerVAphase2_Object = MibScalar
imPM3Power3OutputPowerVAphase2 = _ImPM3Power3OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 63),
    _ImPM3Power3OutputPowerVAphase2_Type()
)
imPM3Power3OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerVAphase2.setUnits("VA")
_ImPM3Power3OutputPowerKVAphase2_Type = Integer32
_ImPM3Power3OutputPowerKVAphase2_Object = MibScalar
imPM3Power3OutputPowerKVAphase2 = _ImPM3Power3OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 64),
    _ImPM3Power3OutputPowerKVAphase2_Type()
)
imPM3Power3OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM3Power3OutputVoltagePhase3_Type = Integer32
_ImPM3Power3OutputVoltagePhase3_Object = MibScalar
imPM3Power3OutputVoltagePhase3 = _ImPM3Power3OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 65),
    _ImPM3Power3OutputVoltagePhase3_Type()
)
imPM3Power3OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputVoltagePhase3.setUnits("0.1 V")
_ImPM3Power3OutputCurrentPhase3_Type = Integer32
_ImPM3Power3OutputCurrentPhase3_Object = MibScalar
imPM3Power3OutputCurrentPhase3 = _ImPM3Power3OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 66),
    _ImPM3Power3OutputCurrentPhase3_Type()
)
imPM3Power3OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputCurrentPhase3.setUnits("0.1 A")
_ImPM3Power3OutputPowerVAphase3_Type = Integer32
_ImPM3Power3OutputPowerVAphase3_Object = MibScalar
imPM3Power3OutputPowerVAphase3 = _ImPM3Power3OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 67),
    _ImPM3Power3OutputPowerVAphase3_Type()
)
imPM3Power3OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerVAphase3.setUnits("VA")
_ImPM3Power3OutputPowerKVAphase3_Type = Integer32
_ImPM3Power3OutputPowerKVAphase3_Object = MibScalar
imPM3Power3OutputPowerKVAphase3 = _ImPM3Power3OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 5, 68),
    _ImPM3Power3OutputPowerKVAphase3_Type()
)
imPM3Power3OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM3Power3OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM3Battery_ObjectIdentity = ObjectIdentity
imPM3Battery = _ImPM3Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 6)
)
_ImPM3BatteryNominalCapacity_Type = NonNegativeInteger
_ImPM3BatteryNominalCapacity_Object = MibScalar
imPM3BatteryNominalCapacity = _ImPM3BatteryNominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 6, 1),
    _ImPM3BatteryNominalCapacity_Type()
)
imPM3BatteryNominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatteryNominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatteryNominalCapacity.setUnits("Ah")
_ImPM3BatteryVoltage_Type = Integer32
_ImPM3BatteryVoltage_Object = MibScalar
imPM3BatteryVoltage = _ImPM3BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 6, 2),
    _ImPM3BatteryVoltage_Type()
)
imPM3BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatteryVoltage.setUnits("0.1 V")
_ImPM3BatteryCurrent_Type = Integer32
_ImPM3BatteryCurrent_Object = MibScalar
imPM3BatteryCurrent = _ImPM3BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 6, 3),
    _ImPM3BatteryCurrent_Type()
)
imPM3BatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatteryCurrent.setUnits("0.1 A")
_ImPM3BatteryChargeState_Type = NonNegativeInteger
_ImPM3BatteryChargeState_Object = MibScalar
imPM3BatteryChargeState = _ImPM3BatteryChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 6, 4),
    _ImPM3BatteryChargeState_Type()
)
imPM3BatteryChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatteryChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatteryChargeState.setUnits("%")
_ImPM3BatteryAutonomyTime_Type = NonNegativeInteger
_ImPM3BatteryAutonomyTime_Object = MibScalar
imPM3BatteryAutonomyTime = _ImPM3BatteryAutonomyTime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 6, 5),
    _ImPM3BatteryAutonomyTime_Type()
)
imPM3BatteryAutonomyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatteryAutonomyTime.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatteryAutonomyTime.setUnits("min")
_ImPM3BatteryTimeOnBattery_Type = NonNegativeInteger
_ImPM3BatteryTimeOnBattery_Object = MibScalar
imPM3BatteryTimeOnBattery = _ImPM3BatteryTimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 6, 6),
    _ImPM3BatteryTimeOnBattery_Type()
)
imPM3BatteryTimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatteryTimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatteryTimeOnBattery.setUnits("min")
_ImPM3BatLeg1_ObjectIdentity = ObjectIdentity
imPM3BatLeg1 = _ImPM3BatLeg1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7)
)


class _ImPM3BatLeg1Manufacturer_Type(DisplayString):
    """Custom type imPM3BatLeg1Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM3BatLeg1Manufacturer_Type.__name__ = "DisplayString"
_ImPM3BatLeg1Manufacturer_Object = MibScalar
imPM3BatLeg1Manufacturer = _ImPM3BatLeg1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 1),
    _ImPM3BatLeg1Manufacturer_Type()
)
imPM3BatLeg1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Manufacturer.setStatus("current")


class _ImPM3BatLeg1Type_Type(DisplayString):
    """Custom type imPM3BatLeg1Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg1Type_Type.__name__ = "DisplayString"
_ImPM3BatLeg1Type_Object = MibScalar
imPM3BatLeg1Type = _ImPM3BatLeg1Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 2),
    _ImPM3BatLeg1Type_Type()
)
imPM3BatLeg1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Type.setStatus("current")


class _ImPM3BatLeg1serNumb_Type(DisplayString):
    """Custom type imPM3BatLeg1serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg1serNumb_Type.__name__ = "DisplayString"
_ImPM3BatLeg1serNumb_Object = MibScalar
imPM3BatLeg1serNumb = _ImPM3BatLeg1serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 3),
    _ImPM3BatLeg1serNumb_Type()
)
imPM3BatLeg1serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1serNumb.setStatus("current")


class _ImPM3BatLeg1nextServiceDate_Type(DisplayString):
    """Custom type imPM3BatLeg1nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg1nextServiceDate_Type.__name__ = "DisplayString"
_ImPM3BatLeg1nextServiceDate_Object = MibScalar
imPM3BatLeg1nextServiceDate = _ImPM3BatLeg1nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 4),
    _ImPM3BatLeg1nextServiceDate_Type()
)
imPM3BatLeg1nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1nextServiceDate.setStatus("current")


class _ImPM3BatLeg1InstallationDate_Type(DisplayString):
    """Custom type imPM3BatLeg1InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg1InstallationDate_Type.__name__ = "DisplayString"
_ImPM3BatLeg1InstallationDate_Object = MibScalar
imPM3BatLeg1InstallationDate = _ImPM3BatLeg1InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 5),
    _ImPM3BatLeg1InstallationDate_Type()
)
imPM3BatLeg1InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1InstallationDate.setStatus("current")
_ImPM3BatLeg1NominalVoltage_Type = Integer32
_ImPM3BatLeg1NominalVoltage_Object = MibScalar
imPM3BatLeg1NominalVoltage = _ImPM3BatLeg1NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 6),
    _ImPM3BatLeg1NominalVoltage_Type()
)
imPM3BatLeg1NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1NominalVoltage.setUnits("0.1 V")
_ImPM3BatLeg1NominalCapacity_Type = NonNegativeInteger
_ImPM3BatLeg1NominalCapacity_Object = MibScalar
imPM3BatLeg1NominalCapacity = _ImPM3BatLeg1NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 7),
    _ImPM3BatLeg1NominalCapacity_Type()
)
imPM3BatLeg1NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1NominalCapacity.setUnits("Ah")
_ImPM3BatLeg1Lifetime_Type = NonNegativeInteger
_ImPM3BatLeg1Lifetime_Object = MibScalar
imPM3BatLeg1Lifetime = _ImPM3BatLeg1Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 8),
    _ImPM3BatLeg1Lifetime_Type()
)
imPM3BatLeg1Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1Lifetime.setUnits("years")
_ImPM3BatLeg1Voltage_Type = Integer32
_ImPM3BatLeg1Voltage_Object = MibScalar
imPM3BatLeg1Voltage = _ImPM3BatLeg1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 9),
    _ImPM3BatLeg1Voltage_Type()
)
imPM3BatLeg1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1Voltage.setUnits("0.1 V")
_ImPM3BatLeg1Current_Type = Integer32
_ImPM3BatLeg1Current_Object = MibScalar
imPM3BatLeg1Current = _ImPM3BatLeg1Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 10),
    _ImPM3BatLeg1Current_Type()
)
imPM3BatLeg1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1Current.setUnits("0.1 A")
_ImPM3BatLeg1Temperature_Type = Integer32
_ImPM3BatLeg1Temperature_Object = MibScalar
imPM3BatLeg1Temperature = _ImPM3BatLeg1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 11),
    _ImPM3BatLeg1Temperature_Type()
)
imPM3BatLeg1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1Temperature.setUnits("degrees Centigrade")
_ImPM3BatLeg1ChargeState_Type = NonNegativeInteger
_ImPM3BatLeg1ChargeState_Object = MibScalar
imPM3BatLeg1ChargeState = _ImPM3BatLeg1ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 12),
    _ImPM3BatLeg1ChargeState_Type()
)
imPM3BatLeg1ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1ChargeState.setUnits("%")
_ImPM3BatLeg1RestCapacity_Type = NonNegativeInteger
_ImPM3BatLeg1RestCapacity_Object = MibScalar
imPM3BatLeg1RestCapacity = _ImPM3BatLeg1RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 13),
    _ImPM3BatLeg1RestCapacity_Type()
)
imPM3BatLeg1RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1RestCapacity.setUnits("Ah")
_ImPM3BatLeg1Autonomytime_Type = NonNegativeInteger
_ImPM3BatLeg1Autonomytime_Object = MibScalar
imPM3BatLeg1Autonomytime = _ImPM3BatLeg1Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 14),
    _ImPM3BatLeg1Autonomytime_Type()
)
imPM3BatLeg1Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1Autonomytime.setUnits("min")
_ImPM3BatLeg1TimeOnBattery_Type = NonNegativeInteger
_ImPM3BatLeg1TimeOnBattery_Object = MibScalar
imPM3BatLeg1TimeOnBattery = _ImPM3BatLeg1TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 15),
    _ImPM3BatLeg1TimeOnBattery_Type()
)
imPM3BatLeg1TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg1TimeOnBattery.setUnits("min")


class _ImPM3BatLeg1Fuse_Type(Integer32):
    """Custom type imPM3BatLeg1Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg1Fuse_Type.__name__ = "Integer32"
_ImPM3BatLeg1Fuse_Object = MibScalar
imPM3BatLeg1Fuse = _ImPM3BatLeg1Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 16),
    _ImPM3BatLeg1Fuse_Type()
)
imPM3BatLeg1Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Fuse.setStatus("current")


class _ImPM3BatLeg1Breaker_Type(Integer32):
    """Custom type imPM3BatLeg1Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg1Breaker_Type.__name__ = "Integer32"
_ImPM3BatLeg1Breaker_Object = MibScalar
imPM3BatLeg1Breaker = _ImPM3BatLeg1Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 17),
    _ImPM3BatLeg1Breaker_Type()
)
imPM3BatLeg1Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1Breaker.setStatus("current")


class _ImPM3BatLeg1LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM3BatLeg1LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg1LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM3BatLeg1LowVoltageDisconnect_Object = MibScalar
imPM3BatLeg1LowVoltageDisconnect = _ImPM3BatLeg1LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 7, 18),
    _ImPM3BatLeg1LowVoltageDisconnect_Type()
)
imPM3BatLeg1LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg1LowVoltageDisconnect.setStatus("current")
_ImPM3BatLeg2_ObjectIdentity = ObjectIdentity
imPM3BatLeg2 = _ImPM3BatLeg2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8)
)


class _ImPM3BatLeg2Manufacturer_Type(DisplayString):
    """Custom type imPM3BatLeg2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM3BatLeg2Manufacturer_Type.__name__ = "DisplayString"
_ImPM3BatLeg2Manufacturer_Object = MibScalar
imPM3BatLeg2Manufacturer = _ImPM3BatLeg2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 1),
    _ImPM3BatLeg2Manufacturer_Type()
)
imPM3BatLeg2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Manufacturer.setStatus("current")


class _ImPM3BatLeg2Type_Type(DisplayString):
    """Custom type imPM3BatLeg2Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg2Type_Type.__name__ = "DisplayString"
_ImPM3BatLeg2Type_Object = MibScalar
imPM3BatLeg2Type = _ImPM3BatLeg2Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 2),
    _ImPM3BatLeg2Type_Type()
)
imPM3BatLeg2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Type.setStatus("current")


class _ImPM3BatLeg2serNumb_Type(DisplayString):
    """Custom type imPM3BatLeg2serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg2serNumb_Type.__name__ = "DisplayString"
_ImPM3BatLeg2serNumb_Object = MibScalar
imPM3BatLeg2serNumb = _ImPM3BatLeg2serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 3),
    _ImPM3BatLeg2serNumb_Type()
)
imPM3BatLeg2serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2serNumb.setStatus("current")


class _ImPM3BatLeg2nextServiceDate_Type(DisplayString):
    """Custom type imPM3BatLeg2nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg2nextServiceDate_Type.__name__ = "DisplayString"
_ImPM3BatLeg2nextServiceDate_Object = MibScalar
imPM3BatLeg2nextServiceDate = _ImPM3BatLeg2nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 4),
    _ImPM3BatLeg2nextServiceDate_Type()
)
imPM3BatLeg2nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2nextServiceDate.setStatus("current")


class _ImPM3BatLeg2InstallationDate_Type(DisplayString):
    """Custom type imPM3BatLeg2InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg2InstallationDate_Type.__name__ = "DisplayString"
_ImPM3BatLeg2InstallationDate_Object = MibScalar
imPM3BatLeg2InstallationDate = _ImPM3BatLeg2InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 5),
    _ImPM3BatLeg2InstallationDate_Type()
)
imPM3BatLeg2InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2InstallationDate.setStatus("current")
_ImPM3BatLeg2NominalVoltage_Type = Integer32
_ImPM3BatLeg2NominalVoltage_Object = MibScalar
imPM3BatLeg2NominalVoltage = _ImPM3BatLeg2NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 6),
    _ImPM3BatLeg2NominalVoltage_Type()
)
imPM3BatLeg2NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2NominalVoltage.setUnits("0.1 V")
_ImPM3BatLeg2NominalCapacity_Type = NonNegativeInteger
_ImPM3BatLeg2NominalCapacity_Object = MibScalar
imPM3BatLeg2NominalCapacity = _ImPM3BatLeg2NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 7),
    _ImPM3BatLeg2NominalCapacity_Type()
)
imPM3BatLeg2NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2NominalCapacity.setUnits("Ah")
_ImPM3BatLeg2Lifetime_Type = NonNegativeInteger
_ImPM3BatLeg2Lifetime_Object = MibScalar
imPM3BatLeg2Lifetime = _ImPM3BatLeg2Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 8),
    _ImPM3BatLeg2Lifetime_Type()
)
imPM3BatLeg2Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2Lifetime.setUnits("years")
_ImPM3BatLeg2Voltage_Type = Integer32
_ImPM3BatLeg2Voltage_Object = MibScalar
imPM3BatLeg2Voltage = _ImPM3BatLeg2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 9),
    _ImPM3BatLeg2Voltage_Type()
)
imPM3BatLeg2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2Voltage.setUnits("0.1 V")
_ImPM3BatLeg2Current_Type = Integer32
_ImPM3BatLeg2Current_Object = MibScalar
imPM3BatLeg2Current = _ImPM3BatLeg2Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 10),
    _ImPM3BatLeg2Current_Type()
)
imPM3BatLeg2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2Current.setUnits("0.1 A")
_ImPM3BatLeg2Temperature_Type = Integer32
_ImPM3BatLeg2Temperature_Object = MibScalar
imPM3BatLeg2Temperature = _ImPM3BatLeg2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 11),
    _ImPM3BatLeg2Temperature_Type()
)
imPM3BatLeg2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2Temperature.setUnits("degrees Centigrade")
_ImPM3BatLeg2ChargeState_Type = NonNegativeInteger
_ImPM3BatLeg2ChargeState_Object = MibScalar
imPM3BatLeg2ChargeState = _ImPM3BatLeg2ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 12),
    _ImPM3BatLeg2ChargeState_Type()
)
imPM3BatLeg2ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2ChargeState.setUnits("%")
_ImPM3BatLeg2RestCapacity_Type = NonNegativeInteger
_ImPM3BatLeg2RestCapacity_Object = MibScalar
imPM3BatLeg2RestCapacity = _ImPM3BatLeg2RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 13),
    _ImPM3BatLeg2RestCapacity_Type()
)
imPM3BatLeg2RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2RestCapacity.setUnits("Ah")
_ImPM3BatLeg2Autonomytime_Type = NonNegativeInteger
_ImPM3BatLeg2Autonomytime_Object = MibScalar
imPM3BatLeg2Autonomytime = _ImPM3BatLeg2Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 14),
    _ImPM3BatLeg2Autonomytime_Type()
)
imPM3BatLeg2Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2Autonomytime.setUnits("min")
_ImPM3BatLeg2TimeOnBattery_Type = NonNegativeInteger
_ImPM3BatLeg2TimeOnBattery_Object = MibScalar
imPM3BatLeg2TimeOnBattery = _ImPM3BatLeg2TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 15),
    _ImPM3BatLeg2TimeOnBattery_Type()
)
imPM3BatLeg2TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg2TimeOnBattery.setUnits("min")


class _ImPM3BatLeg2Fuse_Type(Integer32):
    """Custom type imPM3BatLeg2Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg2Fuse_Type.__name__ = "Integer32"
_ImPM3BatLeg2Fuse_Object = MibScalar
imPM3BatLeg2Fuse = _ImPM3BatLeg2Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 16),
    _ImPM3BatLeg2Fuse_Type()
)
imPM3BatLeg2Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Fuse.setStatus("current")


class _ImPM3BatLeg2Breaker_Type(Integer32):
    """Custom type imPM3BatLeg2Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg2Breaker_Type.__name__ = "Integer32"
_ImPM3BatLeg2Breaker_Object = MibScalar
imPM3BatLeg2Breaker = _ImPM3BatLeg2Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 17),
    _ImPM3BatLeg2Breaker_Type()
)
imPM3BatLeg2Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2Breaker.setStatus("current")


class _ImPM3BatLeg2LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM3BatLeg2LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg2LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM3BatLeg2LowVoltageDisconnect_Object = MibScalar
imPM3BatLeg2LowVoltageDisconnect = _ImPM3BatLeg2LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 8, 18),
    _ImPM3BatLeg2LowVoltageDisconnect_Type()
)
imPM3BatLeg2LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg2LowVoltageDisconnect.setStatus("current")
_ImPM3BatLeg3_ObjectIdentity = ObjectIdentity
imPM3BatLeg3 = _ImPM3BatLeg3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9)
)


class _ImPM3BatLeg3Manufacturer_Type(DisplayString):
    """Custom type imPM3BatLeg3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM3BatLeg3Manufacturer_Type.__name__ = "DisplayString"
_ImPM3BatLeg3Manufacturer_Object = MibScalar
imPM3BatLeg3Manufacturer = _ImPM3BatLeg3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 1),
    _ImPM3BatLeg3Manufacturer_Type()
)
imPM3BatLeg3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Manufacturer.setStatus("current")


class _ImPM3BatLeg3Type_Type(DisplayString):
    """Custom type imPM3BatLeg3Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg3Type_Type.__name__ = "DisplayString"
_ImPM3BatLeg3Type_Object = MibScalar
imPM3BatLeg3Type = _ImPM3BatLeg3Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 2),
    _ImPM3BatLeg3Type_Type()
)
imPM3BatLeg3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Type.setStatus("current")


class _ImPM3BatLeg3serNumb_Type(DisplayString):
    """Custom type imPM3BatLeg3serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg3serNumb_Type.__name__ = "DisplayString"
_ImPM3BatLeg3serNumb_Object = MibScalar
imPM3BatLeg3serNumb = _ImPM3BatLeg3serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 3),
    _ImPM3BatLeg3serNumb_Type()
)
imPM3BatLeg3serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3serNumb.setStatus("current")


class _ImPM3BatLeg3nextServiceDate_Type(DisplayString):
    """Custom type imPM3BatLeg3nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg3nextServiceDate_Type.__name__ = "DisplayString"
_ImPM3BatLeg3nextServiceDate_Object = MibScalar
imPM3BatLeg3nextServiceDate = _ImPM3BatLeg3nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 4),
    _ImPM3BatLeg3nextServiceDate_Type()
)
imPM3BatLeg3nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3nextServiceDate.setStatus("current")


class _ImPM3BatLeg3InstallationDate_Type(DisplayString):
    """Custom type imPM3BatLeg3InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM3BatLeg3InstallationDate_Type.__name__ = "DisplayString"
_ImPM3BatLeg3InstallationDate_Object = MibScalar
imPM3BatLeg3InstallationDate = _ImPM3BatLeg3InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 5),
    _ImPM3BatLeg3InstallationDate_Type()
)
imPM3BatLeg3InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3InstallationDate.setStatus("current")
_ImPM3BatLeg3NominalVoltage_Type = Integer32
_ImPM3BatLeg3NominalVoltage_Object = MibScalar
imPM3BatLeg3NominalVoltage = _ImPM3BatLeg3NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 6),
    _ImPM3BatLeg3NominalVoltage_Type()
)
imPM3BatLeg3NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3NominalVoltage.setUnits("0.1 V")
_ImPM3BatLeg3NominalCapacity_Type = NonNegativeInteger
_ImPM3BatLeg3NominalCapacity_Object = MibScalar
imPM3BatLeg3NominalCapacity = _ImPM3BatLeg3NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 7),
    _ImPM3BatLeg3NominalCapacity_Type()
)
imPM3BatLeg3NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3NominalCapacity.setUnits("Ah")
_ImPM3BatLeg3Lifetime_Type = NonNegativeInteger
_ImPM3BatLeg3Lifetime_Object = MibScalar
imPM3BatLeg3Lifetime = _ImPM3BatLeg3Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 8),
    _ImPM3BatLeg3Lifetime_Type()
)
imPM3BatLeg3Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3Lifetime.setUnits("years")
_ImPM3BatLeg3Voltage_Type = Integer32
_ImPM3BatLeg3Voltage_Object = MibScalar
imPM3BatLeg3Voltage = _ImPM3BatLeg3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 9),
    _ImPM3BatLeg3Voltage_Type()
)
imPM3BatLeg3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3Voltage.setUnits("0.1 V")
_ImPM3BatLeg3Current_Type = Integer32
_ImPM3BatLeg3Current_Object = MibScalar
imPM3BatLeg3Current = _ImPM3BatLeg3Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 10),
    _ImPM3BatLeg3Current_Type()
)
imPM3BatLeg3Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3Current.setUnits("0.1 A")
_ImPM3BatLeg3Temperature_Type = Integer32
_ImPM3BatLeg3Temperature_Object = MibScalar
imPM3BatLeg3Temperature = _ImPM3BatLeg3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 11),
    _ImPM3BatLeg3Temperature_Type()
)
imPM3BatLeg3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3Temperature.setUnits("degrees Centigrade")
_ImPM3BatLeg3ChargeState_Type = NonNegativeInteger
_ImPM3BatLeg3ChargeState_Object = MibScalar
imPM3BatLeg3ChargeState = _ImPM3BatLeg3ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 12),
    _ImPM3BatLeg3ChargeState_Type()
)
imPM3BatLeg3ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3ChargeState.setUnits("%")
_ImPM3BatLeg3RestCapacity_Type = NonNegativeInteger
_ImPM3BatLeg3RestCapacity_Object = MibScalar
imPM3BatLeg3RestCapacity = _ImPM3BatLeg3RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 13),
    _ImPM3BatLeg3RestCapacity_Type()
)
imPM3BatLeg3RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3RestCapacity.setUnits("Ah")
_ImPM3BatLeg3Autonomytime_Type = NonNegativeInteger
_ImPM3BatLeg3Autonomytime_Object = MibScalar
imPM3BatLeg3Autonomytime = _ImPM3BatLeg3Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 14),
    _ImPM3BatLeg3Autonomytime_Type()
)
imPM3BatLeg3Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3Autonomytime.setUnits("min")
_ImPM3BatLeg3TimeOnBattery_Type = NonNegativeInteger
_ImPM3BatLeg3TimeOnBattery_Object = MibScalar
imPM3BatLeg3TimeOnBattery = _ImPM3BatLeg3TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 15),
    _ImPM3BatLeg3TimeOnBattery_Type()
)
imPM3BatLeg3TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM3BatLeg3TimeOnBattery.setUnits("min")


class _ImPM3BatLeg3Fuse_Type(Integer32):
    """Custom type imPM3BatLeg3Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg3Fuse_Type.__name__ = "Integer32"
_ImPM3BatLeg3Fuse_Object = MibScalar
imPM3BatLeg3Fuse = _ImPM3BatLeg3Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 16),
    _ImPM3BatLeg3Fuse_Type()
)
imPM3BatLeg3Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Fuse.setStatus("current")


class _ImPM3BatLeg3Breaker_Type(Integer32):
    """Custom type imPM3BatLeg3Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg3Breaker_Type.__name__ = "Integer32"
_ImPM3BatLeg3Breaker_Object = MibScalar
imPM3BatLeg3Breaker = _ImPM3BatLeg3Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 17),
    _ImPM3BatLeg3Breaker_Type()
)
imPM3BatLeg3Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3Breaker.setStatus("current")


class _ImPM3BatLeg3LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM3BatLeg3LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3BatLeg3LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM3BatLeg3LowVoltageDisconnect_Object = MibScalar
imPM3BatLeg3LowVoltageDisconnect = _ImPM3BatLeg3LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 9, 18),
    _ImPM3BatLeg3LowVoltageDisconnect_Type()
)
imPM3BatLeg3LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3BatLeg3LowVoltageDisconnect.setStatus("current")
_ImPM3Distrib_ObjectIdentity = ObjectIdentity
imPM3Distrib = _ImPM3Distrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 10)
)
_ImPm3Distrib_Type = Integer32
_ImPm3Distrib_Object = MibScalar
imPm3Distrib = _ImPm3Distrib_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 10, 1),
    _ImPm3Distrib_Type()
)
imPm3Distrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm3Distrib.setStatus("current")
if mibBuilder.loadTexts:
    imPm3Distrib.setUnits("degrees Centigrade")
_ImPM3DistTable_Object = MibTable
imPM3DistTable = _ImPM3DistTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 10, 2)
)
if mibBuilder.loadTexts:
    imPM3DistTable.setStatus("current")
_ImPM3DistEntry_Object = MibTableRow
imPM3DistEntry = _ImPM3DistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 10, 2, 1)
)
imPM3DistEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imPM3DistId"),
)
if mibBuilder.loadTexts:
    imPM3DistEntry.setStatus("current")
_ImPM3DistId_Type = PositiveInteger
_ImPM3DistId_Object = MibTableColumn
imPM3DistId = _ImPM3DistId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 10, 2, 1, 1),
    _ImPM3DistId_Type()
)
imPM3DistId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imPM3DistId.setStatus("current")


class _ImPM3DistFuse_Type(Integer32):
    """Custom type imPM3DistFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3DistFuse_Type.__name__ = "Integer32"
_ImPM3DistFuse_Object = MibTableColumn
imPM3DistFuse = _ImPM3DistFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 10, 2, 1, 2),
    _ImPM3DistFuse_Type()
)
imPM3DistFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3DistFuse.setStatus("current")


class _ImPM3DistBreaker_Type(Integer32):
    """Custom type imPM3DistBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM3DistBreaker_Type.__name__ = "Integer32"
_ImPM3DistBreaker_Object = MibTableColumn
imPM3DistBreaker = _ImPM3DistBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 10, 2, 1, 3),
    _ImPM3DistBreaker_Type()
)
imPM3DistBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3DistBreaker.setStatus("current")
_ImPM3Control_ObjectIdentity = ObjectIdentity
imPM3Control = _ImPM3Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11)
)
_ImPM3ContTable_Object = MibTable
imPM3ContTable = _ImPM3ContTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 1)
)
if mibBuilder.loadTexts:
    imPM3ContTable.setStatus("current")
_ImPM3ContEntry_Object = MibTableRow
imPM3ContEntry = _ImPM3ContEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 1, 1)
)
imPM3ContEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imPM3ContId"),
)
if mibBuilder.loadTexts:
    imPM3ContEntry.setStatus("current")
_ImPM3ContId_Type = PositiveInteger
_ImPM3ContId_Object = MibTableColumn
imPM3ContId = _ImPM3ContId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 1, 1, 1),
    _ImPM3ContId_Type()
)
imPM3ContId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imPM3ContId.setStatus("current")


class _ImPM3ContState_Type(Integer32):
    """Custom type imPM3ContState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_ImPM3ContState_Type.__name__ = "Integer32"
_ImPM3ContState_Object = MibTableColumn
imPM3ContState = _ImPM3ContState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 1, 1, 2),
    _ImPM3ContState_Type()
)
imPM3ContState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM3ContState.setStatus("current")


class _ImPM3ContLabel_Type(DisplayString):
    """Custom type imPM3ContLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM3ContLabel_Type.__name__ = "DisplayString"
_ImPM3ContLabel_Object = MibTableColumn
imPM3ContLabel = _ImPM3ContLabel_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 1, 1, 3),
    _ImPM3ContLabel_Type()
)
imPM3ContLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3ContLabel.setStatus("current")
_ImPM3ContTimeOFF_Type = Integer32
_ImPM3ContTimeOFF_Object = MibTableColumn
imPM3ContTimeOFF = _ImPM3ContTimeOFF_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 1, 1, 4),
    _ImPM3ContTimeOFF_Type()
)
imPM3ContTimeOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM3ContTimeOFF.setStatus("current")
if mibBuilder.loadTexts:
    imPM3ContTimeOFF.setUnits("min")


class _ImPM3ContAuto_Type(Integer32):
    """Custom type imPM3ContAuto based on Integer32"""
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


_ImPM3ContAuto_Type.__name__ = "Integer32"
_ImPM3ContAuto_Object = MibTableColumn
imPM3ContAuto = _ImPM3ContAuto_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 1, 1, 5),
    _ImPM3ContAuto_Type()
)
imPM3ContAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM3ContAuto.setStatus("current")


class _ImPM3ContTestCAPcommand_Type(Integer32):
    """Custom type imPM3ContTestCAPcommand based on Integer32"""
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


_ImPM3ContTestCAPcommand_Type.__name__ = "Integer32"
_ImPM3ContTestCAPcommand_Object = MibScalar
imPM3ContTestCAPcommand = _ImPM3ContTestCAPcommand_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 2),
    _ImPM3ContTestCAPcommand_Type()
)
imPM3ContTestCAPcommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM3ContTestCAPcommand.setStatus("current")
_ImPM3ContTestCAPvoltage_Type = Integer32
_ImPM3ContTestCAPvoltage_Object = MibScalar
imPM3ContTestCAPvoltage = _ImPM3ContTestCAPvoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 3),
    _ImPM3ContTestCAPvoltage_Type()
)
imPM3ContTestCAPvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3ContTestCAPvoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM3ContTestCAPvoltage.setUnits("0.1 V")
_ImPM3ContTestCAPcurrent_Type = Integer32
_ImPM3ContTestCAPcurrent_Object = MibScalar
imPM3ContTestCAPcurrent = _ImPM3ContTestCAPcurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 4),
    _ImPM3ContTestCAPcurrent_Type()
)
imPM3ContTestCAPcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3ContTestCAPcurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM3ContTestCAPcurrent.setUnits("0.1 A")
_ImPM3ContTestCAPtemperature_Type = Integer32
_ImPM3ContTestCAPtemperature_Object = MibScalar
imPM3ContTestCAPtemperature = _ImPM3ContTestCAPtemperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 5),
    _ImPM3ContTestCAPtemperature_Type()
)
imPM3ContTestCAPtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3ContTestCAPtemperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM3ContTestCAPtemperature.setUnits("degrees Centigrade")
_ImPM3ContTestCAPduration_Type = Integer32
_ImPM3ContTestCAPduration_Object = MibScalar
imPM3ContTestCAPduration = _ImPM3ContTestCAPduration_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 6),
    _ImPM3ContTestCAPduration_Type()
)
imPM3ContTestCAPduration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3ContTestCAPduration.setStatus("current")
if mibBuilder.loadTexts:
    imPM3ContTestCAPduration.setUnits("min")
_ImPM3ContTestCAPstatus_Type = Integer32
_ImPM3ContTestCAPstatus_Object = MibScalar
imPM3ContTestCAPstatus = _ImPM3ContTestCAPstatus_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 3, 11, 7),
    _ImPM3ContTestCAPstatus_Type()
)
imPM3ContTestCAPstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM3ContTestCAPstatus.setStatus("current")
_ImPanM4_ObjectIdentity = ObjectIdentity
imPanM4 = _ImPanM4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4)
)
_ImPM4SystemID_ObjectIdentity = ObjectIdentity
imPM4SystemID = _ImPM4SystemID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1)
)


class _ImPM4SystemIDManufacturer_Type(DisplayString):
    """Custom type imPM4SystemIDManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM4SystemIDManufacturer_Type.__name__ = "DisplayString"
_ImPM4SystemIDManufacturer_Object = MibScalar
imPM4SystemIDManufacturer = _ImPM4SystemIDManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 1),
    _ImPM4SystemIDManufacturer_Type()
)
imPM4SystemIDManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDManufacturer.setStatus("current")


class _ImPM4SystemIDType_Type(DisplayString):
    """Custom type imPM4SystemIDType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4SystemIDType_Type.__name__ = "DisplayString"
_ImPM4SystemIDType_Object = MibScalar
imPM4SystemIDType = _ImPM4SystemIDType_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 2),
    _ImPM4SystemIDType_Type()
)
imPM4SystemIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDType.setStatus("current")


class _ImPM4SystemIDserNumb_Type(DisplayString):
    """Custom type imPM4SystemIDserNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4SystemIDserNumb_Type.__name__ = "DisplayString"
_ImPM4SystemIDserNumb_Object = MibScalar
imPM4SystemIDserNumb = _ImPM4SystemIDserNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 3),
    _ImPM4SystemIDserNumb_Type()
)
imPM4SystemIDserNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDserNumb.setStatus("current")


class _ImPM4SystemIDnextServiceDate_Type(DisplayString):
    """Custom type imPM4SystemIDnextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4SystemIDnextServiceDate_Type.__name__ = "DisplayString"
_ImPM4SystemIDnextServiceDate_Object = MibScalar
imPM4SystemIDnextServiceDate = _ImPM4SystemIDnextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 4),
    _ImPM4SystemIDnextServiceDate_Type()
)
imPM4SystemIDnextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDnextServiceDate.setStatus("current")
_ImPM4SystemIDaddress_Type = NonNegativeInteger
_ImPM4SystemIDaddress_Object = MibScalar
imPM4SystemIDaddress = _ImPM4SystemIDaddress_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 5),
    _ImPM4SystemIDaddress_Type()
)
imPM4SystemIDaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDaddress.setStatus("current")
_ImPM4SystemIDhwVersion_Type = NonNegativeInteger
_ImPM4SystemIDhwVersion_Object = MibScalar
imPM4SystemIDhwVersion = _ImPM4SystemIDhwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 6),
    _ImPM4SystemIDhwVersion_Type()
)
imPM4SystemIDhwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDhwVersion.setStatus("current")
_ImPM4SystemIDswVersion_Type = NonNegativeInteger
_ImPM4SystemIDswVersion_Object = MibScalar
imPM4SystemIDswVersion = _ImPM4SystemIDswVersion_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 7),
    _ImPM4SystemIDswVersion_Type()
)
imPM4SystemIDswVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDswVersion.setStatus("current")


class _ImPM4SystemIDPMserialNumber_Type(DisplayString):
    """Custom type imPM4SystemIDPMserialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4SystemIDPMserialNumber_Type.__name__ = "DisplayString"
_ImPM4SystemIDPMserialNumber_Object = MibScalar
imPM4SystemIDPMserialNumber = _ImPM4SystemIDPMserialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 8),
    _ImPM4SystemIDPMserialNumber_Type()
)
imPM4SystemIDPMserialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDPMserialNumber.setStatus("current")


class _ImPM4SystemIDbuttonName_Type(DisplayString):
    """Custom type imPM4SystemIDbuttonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4SystemIDbuttonName_Type.__name__ = "DisplayString"
_ImPM4SystemIDbuttonName_Object = MibScalar
imPM4SystemIDbuttonName = _ImPM4SystemIDbuttonName_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 1, 9),
    _ImPM4SystemIDbuttonName_Type()
)
imPM4SystemIDbuttonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemIDbuttonName.setStatus("current")
_ImPM4SystemGEN_ObjectIdentity = ObjectIdentity
imPM4SystemGEN = _ImPM4SystemGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2)
)


class _ImPM4SystemGENSurgeArrester_Type(Integer32):
    """Custom type imPM4SystemGENSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4SystemGENSurgeArrester_Type.__name__ = "Integer32"
_ImPM4SystemGENSurgeArrester_Object = MibScalar
imPM4SystemGENSurgeArrester = _ImPM4SystemGENSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 1),
    _ImPM4SystemGENSurgeArrester_Type()
)
imPM4SystemGENSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENSurgeArrester.setStatus("current")


class _ImPM4SystemGENDoor1_Type(Integer32):
    """Custom type imPM4SystemGENDoor1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_ImPM4SystemGENDoor1_Type.__name__ = "Integer32"
_ImPM4SystemGENDoor1_Object = MibScalar
imPM4SystemGENDoor1 = _ImPM4SystemGENDoor1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 2),
    _ImPM4SystemGENDoor1_Type()
)
imPM4SystemGENDoor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENDoor1.setStatus("current")


class _ImPM4SystemGENDoor2_Type(Integer32):
    """Custom type imPM4SystemGENDoor2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )


_ImPM4SystemGENDoor2_Type.__name__ = "Integer32"
_ImPM4SystemGENDoor2_Object = MibScalar
imPM4SystemGENDoor2 = _ImPM4SystemGENDoor2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 3),
    _ImPM4SystemGENDoor2_Type()
)
imPM4SystemGENDoor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENDoor2.setStatus("current")


class _ImPM4SystemGENFan_Type(Integer32):
    """Custom type imPM4SystemGENFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_ImPM4SystemGENFan_Type.__name__ = "Integer32"
_ImPM4SystemGENFan_Object = MibScalar
imPM4SystemGENFan = _ImPM4SystemGENFan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 4),
    _ImPM4SystemGENFan_Type()
)
imPM4SystemGENFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENFan.setStatus("current")


class _ImPM4SystemGENuser1_Type(Integer32):
    """Custom type imPM4SystemGENuser1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4SystemGENuser1_Type.__name__ = "Integer32"
_ImPM4SystemGENuser1_Object = MibScalar
imPM4SystemGENuser1 = _ImPM4SystemGENuser1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 5),
    _ImPM4SystemGENuser1_Type()
)
imPM4SystemGENuser1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENuser1.setStatus("current")


class _ImPM4SystemGENuser2_Type(Integer32):
    """Custom type imPM4SystemGENuser2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4SystemGENuser2_Type.__name__ = "Integer32"
_ImPM4SystemGENuser2_Object = MibScalar
imPM4SystemGENuser2 = _ImPM4SystemGENuser2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 6),
    _ImPM4SystemGENuser2_Type()
)
imPM4SystemGENuser2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENuser2.setStatus("current")


class _ImPM4SystemGENuser3_Type(Integer32):
    """Custom type imPM4SystemGENuser3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4SystemGENuser3_Type.__name__ = "Integer32"
_ImPM4SystemGENuser3_Object = MibScalar
imPM4SystemGENuser3 = _ImPM4SystemGENuser3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 7),
    _ImPM4SystemGENuser3_Type()
)
imPM4SystemGENuser3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENuser3.setStatus("current")


class _ImPM4SystemGENuser4_Type(Integer32):
    """Custom type imPM4SystemGENuser4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4SystemGENuser4_Type.__name__ = "Integer32"
_ImPM4SystemGENuser4_Object = MibScalar
imPM4SystemGENuser4 = _ImPM4SystemGENuser4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 8),
    _ImPM4SystemGENuser4_Type()
)
imPM4SystemGENuser4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENuser4.setStatus("current")
_ImPM4SystemGENtemperature_Type = NonNegativeInteger
_ImPM4SystemGENtemperature_Object = MibScalar
imPM4SystemGENtemperature = _ImPM4SystemGENtemperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 2, 9),
    _ImPM4SystemGENtemperature_Type()
)
imPM4SystemGENtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4SystemGENtemperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM4SystemGENtemperature.setUnits("degrees Centigrade")
_ImPM4Power1_ObjectIdentity = ObjectIdentity
imPM4Power1 = _ImPM4Power1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3)
)


class _ImPM4Power1Manufacturer_Type(DisplayString):
    """Custom type imPM4Power1Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM4Power1Manufacturer_Type.__name__ = "DisplayString"
_ImPM4Power1Manufacturer_Object = MibScalar
imPM4Power1Manufacturer = _ImPM4Power1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 1),
    _ImPM4Power1Manufacturer_Type()
)
imPM4Power1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Manufacturer.setStatus("current")


class _ImPM4Power1Type_Type(DisplayString):
    """Custom type imPM4Power1Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power1Type_Type.__name__ = "DisplayString"
_ImPM4Power1Type_Object = MibScalar
imPM4Power1Type = _ImPM4Power1Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 2),
    _ImPM4Power1Type_Type()
)
imPM4Power1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Type.setStatus("current")


class _ImPM4Power1serNumb_Type(DisplayString):
    """Custom type imPM4Power1serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power1serNumb_Type.__name__ = "DisplayString"
_ImPM4Power1serNumb_Object = MibScalar
imPM4Power1serNumb = _ImPM4Power1serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 3),
    _ImPM4Power1serNumb_Type()
)
imPM4Power1serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1serNumb.setStatus("current")


class _ImPM4Power1nextServiceDate_Type(DisplayString):
    """Custom type imPM4Power1nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power1nextServiceDate_Type.__name__ = "DisplayString"
_ImPM4Power1nextServiceDate_Object = MibScalar
imPM4Power1nextServiceDate = _ImPM4Power1nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 4),
    _ImPM4Power1nextServiceDate_Type()
)
imPM4Power1nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1nextServiceDate.setStatus("current")
_ImPM4Power1InputVoltage_Type = Integer32
_ImPM4Power1InputVoltage_Object = MibScalar
imPM4Power1InputVoltage = _ImPM4Power1InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 5),
    _ImPM4Power1InputVoltage_Type()
)
imPM4Power1InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputVoltage.setUnits("0.1 V")
_ImPM4Power1InputCurrent_Type = Integer32
_ImPM4Power1InputCurrent_Object = MibScalar
imPM4Power1InputCurrent = _ImPM4Power1InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 6),
    _ImPM4Power1InputCurrent_Type()
)
imPM4Power1InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputCurrent.setUnits("0.1 A")
_ImPM4Power1InputPowerVA_Type = Integer32
_ImPM4Power1InputPowerVA_Object = MibScalar
imPM4Power1InputPowerVA = _ImPM4Power1InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 7),
    _ImPM4Power1InputPowerVA_Type()
)
imPM4Power1InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerVA.setUnits("VA")
_ImPM4Power1InputPowerKVA_Type = Integer32
_ImPM4Power1InputPowerKVA_Object = MibScalar
imPM4Power1InputPowerKVA = _ImPM4Power1InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 8),
    _ImPM4Power1InputPowerKVA_Type()
)
imPM4Power1InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKVA.setUnits("0.1 kVA")
_ImPM4Power1InputPowerW_Type = Integer32
_ImPM4Power1InputPowerW_Object = MibScalar
imPM4Power1InputPowerW = _ImPM4Power1InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 9),
    _ImPM4Power1InputPowerW_Type()
)
imPM4Power1InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerW.setUnits("W")
_ImPM4Power1InputPowerKW_Type = Integer32
_ImPM4Power1InputPowerKW_Object = MibScalar
imPM4Power1InputPowerKW = _ImPM4Power1InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 10),
    _ImPM4Power1InputPowerKW_Type()
)
imPM4Power1InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKW.setUnits("0.1 kW")
_ImPM4Power1InputVoltagePhase1_Type = Integer32
_ImPM4Power1InputVoltagePhase1_Object = MibScalar
imPM4Power1InputVoltagePhase1 = _ImPM4Power1InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 11),
    _ImPM4Power1InputVoltagePhase1_Type()
)
imPM4Power1InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputVoltagePhase1.setUnits("0.1 V")
_ImPM4Power1InputCurrentPhase1_Type = Integer32
_ImPM4Power1InputCurrentPhase1_Object = MibScalar
imPM4Power1InputCurrentPhase1 = _ImPM4Power1InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 12),
    _ImPM4Power1InputCurrentPhase1_Type()
)
imPM4Power1InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputCurrentPhase1.setUnits("0.1 A")
_ImPM4Power1InputPowerVAphase1_Type = Integer32
_ImPM4Power1InputPowerVAphase1_Object = MibScalar
imPM4Power1InputPowerVAphase1 = _ImPM4Power1InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 13),
    _ImPM4Power1InputPowerVAphase1_Type()
)
imPM4Power1InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerVAphase1.setUnits("VA")
_ImPM4Power1InputPowerKVAphase1_Type = Integer32
_ImPM4Power1InputPowerKVAphase1_Object = MibScalar
imPM4Power1InputPowerKVAphase1 = _ImPM4Power1InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 14),
    _ImPM4Power1InputPowerKVAphase1_Type()
)
imPM4Power1InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM4Power1InputVoltagePhase2_Type = Integer32
_ImPM4Power1InputVoltagePhase2_Object = MibScalar
imPM4Power1InputVoltagePhase2 = _ImPM4Power1InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 15),
    _ImPM4Power1InputVoltagePhase2_Type()
)
imPM4Power1InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputVoltagePhase2.setUnits("0.1 V")
_ImPM4Power1InputCurrentPhase2_Type = Integer32
_ImPM4Power1InputCurrentPhase2_Object = MibScalar
imPM4Power1InputCurrentPhase2 = _ImPM4Power1InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 16),
    _ImPM4Power1InputCurrentPhase2_Type()
)
imPM4Power1InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputCurrentPhase2.setUnits("0.1 A")
_ImPM4Power1InputPowerVAphase2_Type = Integer32
_ImPM4Power1InputPowerVAphase2_Object = MibScalar
imPM4Power1InputPowerVAphase2 = _ImPM4Power1InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 17),
    _ImPM4Power1InputPowerVAphase2_Type()
)
imPM4Power1InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerVAphase2.setUnits("VA")
_ImPM4Power1InputPowerKVAphase2_Type = Integer32
_ImPM4Power1InputPowerKVAphase2_Object = MibScalar
imPM4Power1InputPowerKVAphase2 = _ImPM4Power1InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 18),
    _ImPM4Power1InputPowerKVAphase2_Type()
)
imPM4Power1InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM4Power1InputVoltagePhase3_Type = Integer32
_ImPM4Power1InputVoltagePhase3_Object = MibScalar
imPM4Power1InputVoltagePhase3 = _ImPM4Power1InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 19),
    _ImPM4Power1InputVoltagePhase3_Type()
)
imPM4Power1InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputVoltagePhase3.setUnits("0.1 V")
_ImPM4Power1InputCurrentPhase3_Type = Integer32
_ImPM4Power1InputCurrentPhase3_Object = MibScalar
imPM4Power1InputCurrentPhase3 = _ImPM4Power1InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 20),
    _ImPM4Power1InputCurrentPhase3_Type()
)
imPM4Power1InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputCurrentPhase3.setUnits("0.1 A")
_ImPM4Power1InputPowerVAphase3_Type = Integer32
_ImPM4Power1InputPowerVAphase3_Object = MibScalar
imPM4Power1InputPowerVAphase3 = _ImPM4Power1InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 21),
    _ImPM4Power1InputPowerVAphase3_Type()
)
imPM4Power1InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerVAphase3.setUnits("VA")
_ImPM4Power1InputPowerKVAphase3_Type = Integer32
_ImPM4Power1InputPowerKVAphase3_Object = MibScalar
imPM4Power1InputPowerKVAphase3 = _ImPM4Power1InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 22),
    _ImPM4Power1InputPowerKVAphase3_Type()
)
imPM4Power1InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM4Power1OutputVoltage_Type = Integer32
_ImPM4Power1OutputVoltage_Object = MibScalar
imPM4Power1OutputVoltage = _ImPM4Power1OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 23),
    _ImPM4Power1OutputVoltage_Type()
)
imPM4Power1OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputVoltage.setUnits("0.1 V")
_ImPM4Power1OutputCurrent_Type = Integer32
_ImPM4Power1OutputCurrent_Object = MibScalar
imPM4Power1OutputCurrent = _ImPM4Power1OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 24),
    _ImPM4Power1OutputCurrent_Type()
)
imPM4Power1OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputCurrent.setUnits("0.1 A")
_ImPM4Power1OutputPowerVA_Type = Integer32
_ImPM4Power1OutputPowerVA_Object = MibScalar
imPM4Power1OutputPowerVA = _ImPM4Power1OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 25),
    _ImPM4Power1OutputPowerVA_Type()
)
imPM4Power1OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerVA.setUnits("VA")
_ImPM4Power1OutputPowerKVA_Type = Integer32
_ImPM4Power1OutputPowerKVA_Object = MibScalar
imPM4Power1OutputPowerKVA = _ImPM4Power1OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 26),
    _ImPM4Power1OutputPowerKVA_Type()
)
imPM4Power1OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKVA.setUnits("0.1 kVA")
_ImPM4Power1OutputPowerW_Type = Integer32
_ImPM4Power1OutputPowerW_Object = MibScalar
imPM4Power1OutputPowerW = _ImPM4Power1OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 27),
    _ImPM4Power1OutputPowerW_Type()
)
imPM4Power1OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerW.setUnits("W")
_ImPM4Power1OutputPowerKW_Type = Integer32
_ImPM4Power1OutputPowerKW_Object = MibScalar
imPM4Power1OutputPowerKW = _ImPM4Power1OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 28),
    _ImPM4Power1OutputPowerKW_Type()
)
imPM4Power1OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKW.setUnits("0.1 kW")
_ImPM4Power1OutputLoad_Type = Integer32
_ImPM4Power1OutputLoad_Object = MibScalar
imPM4Power1OutputLoad = _ImPM4Power1OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 29),
    _ImPM4Power1OutputLoad_Type()
)
imPM4Power1OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputLoad.setUnits("%")
_ImPM4Power1OutputFrequency_Type = NonNegativeInteger
_ImPM4Power1OutputFrequency_Object = MibScalar
imPM4Power1OutputFrequency = _ImPM4Power1OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 30),
    _ImPM4Power1OutputFrequency_Type()
)
imPM4Power1OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputFrequency.setUnits("0.1 Hz")
_ImPM4Power1Temperature_Type = Integer32
_ImPM4Power1Temperature_Object = MibScalar
imPM4Power1Temperature = _ImPM4Power1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 31),
    _ImPM4Power1Temperature_Type()
)
imPM4Power1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1Temperature.setUnits("degrees Centigrade")


class _ImPM4Power1Running1_Type(Integer32):
    """Custom type imPM4Power1Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Running1_Type.__name__ = "Integer32"
_ImPM4Power1Running1_Object = MibScalar
imPM4Power1Running1 = _ImPM4Power1Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 32),
    _ImPM4Power1Running1_Type()
)
imPM4Power1Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Running1.setStatus("current")


class _ImPM4Power1Running2_Type(Integer32):
    """Custom type imPM4Power1Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Running2_Type.__name__ = "Integer32"
_ImPM4Power1Running2_Object = MibScalar
imPM4Power1Running2 = _ImPM4Power1Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 33),
    _ImPM4Power1Running2_Type()
)
imPM4Power1Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Running2.setStatus("current")


class _ImPM4Power1Running3_Type(Integer32):
    """Custom type imPM4Power1Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Running3_Type.__name__ = "Integer32"
_ImPM4Power1Running3_Object = MibScalar
imPM4Power1Running3 = _ImPM4Power1Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 34),
    _ImPM4Power1Running3_Type()
)
imPM4Power1Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Running3.setStatus("current")


class _ImPM4Power1Running4_Type(Integer32):
    """Custom type imPM4Power1Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Running4_Type.__name__ = "Integer32"
_ImPM4Power1Running4_Object = MibScalar
imPM4Power1Running4 = _ImPM4Power1Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 35),
    _ImPM4Power1Running4_Type()
)
imPM4Power1Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Running4.setStatus("current")


class _ImPM4Power1Running5_Type(Integer32):
    """Custom type imPM4Power1Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Running5_Type.__name__ = "Integer32"
_ImPM4Power1Running5_Object = MibScalar
imPM4Power1Running5 = _ImPM4Power1Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 36),
    _ImPM4Power1Running5_Type()
)
imPM4Power1Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Running5.setStatus("current")


class _ImPM4Power1Running6_Type(Integer32):
    """Custom type imPM4Power1Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Running6_Type.__name__ = "Integer32"
_ImPM4Power1Running6_Object = MibScalar
imPM4Power1Running6 = _ImPM4Power1Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 37),
    _ImPM4Power1Running6_Type()
)
imPM4Power1Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Running6.setStatus("current")


class _ImPM4Power1Running7_Type(Integer32):
    """Custom type imPM4Power1Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Running7_Type.__name__ = "Integer32"
_ImPM4Power1Running7_Object = MibScalar
imPM4Power1Running7 = _ImPM4Power1Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 38),
    _ImPM4Power1Running7_Type()
)
imPM4Power1Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Running7.setStatus("current")


class _ImPM4Power1Running8_Type(Integer32):
    """Custom type imPM4Power1Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Running8_Type.__name__ = "Integer32"
_ImPM4Power1Running8_Object = MibScalar
imPM4Power1Running8 = _ImPM4Power1Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 39),
    _ImPM4Power1Running8_Type()
)
imPM4Power1Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Running8.setStatus("current")


class _ImPM4Power1InputFuse_Type(Integer32):
    """Custom type imPM4Power1InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputFuse_Type.__name__ = "Integer32"
_ImPM4Power1InputFuse_Object = MibScalar
imPM4Power1InputFuse = _ImPM4Power1InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 40),
    _ImPM4Power1InputFuse_Type()
)
imPM4Power1InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputFuse.setStatus("current")


class _ImPM4Power1InputFuse1_Type(Integer32):
    """Custom type imPM4Power1InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputFuse1_Type.__name__ = "Integer32"
_ImPM4Power1InputFuse1_Object = MibScalar
imPM4Power1InputFuse1 = _ImPM4Power1InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 41),
    _ImPM4Power1InputFuse1_Type()
)
imPM4Power1InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputFuse1.setStatus("current")


class _ImPM4Power1InputFuse2_Type(Integer32):
    """Custom type imPM4Power1InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputFuse2_Type.__name__ = "Integer32"
_ImPM4Power1InputFuse2_Object = MibScalar
imPM4Power1InputFuse2 = _ImPM4Power1InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 42),
    _ImPM4Power1InputFuse2_Type()
)
imPM4Power1InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputFuse2.setStatus("current")


class _ImPM4Power1InputFuse3_Type(Integer32):
    """Custom type imPM4Power1InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputFuse3_Type.__name__ = "Integer32"
_ImPM4Power1InputFuse3_Object = MibScalar
imPM4Power1InputFuse3 = _ImPM4Power1InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 43),
    _ImPM4Power1InputFuse3_Type()
)
imPM4Power1InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputFuse3.setStatus("current")


class _ImPM4Power1InputBreaker_Type(Integer32):
    """Custom type imPM4Power1InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputBreaker_Type.__name__ = "Integer32"
_ImPM4Power1InputBreaker_Object = MibScalar
imPM4Power1InputBreaker = _ImPM4Power1InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 44),
    _ImPM4Power1InputBreaker_Type()
)
imPM4Power1InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputBreaker.setStatus("current")


class _ImPM4Power1InputBreaker1_Type(Integer32):
    """Custom type imPM4Power1InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputBreaker1_Type.__name__ = "Integer32"
_ImPM4Power1InputBreaker1_Object = MibScalar
imPM4Power1InputBreaker1 = _ImPM4Power1InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 45),
    _ImPM4Power1InputBreaker1_Type()
)
imPM4Power1InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputBreaker1.setStatus("current")


class _ImPM4Power1InputBreaker2_Type(Integer32):
    """Custom type imPM4Power1InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputBreaker2_Type.__name__ = "Integer32"
_ImPM4Power1InputBreaker2_Object = MibScalar
imPM4Power1InputBreaker2 = _ImPM4Power1InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 46),
    _ImPM4Power1InputBreaker2_Type()
)
imPM4Power1InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputBreaker2.setStatus("current")


class _ImPM4Power1InputBreaker3_Type(Integer32):
    """Custom type imPM4Power1InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputBreaker3_Type.__name__ = "Integer32"
_ImPM4Power1InputBreaker3_Object = MibScalar
imPM4Power1InputBreaker3 = _ImPM4Power1InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 47),
    _ImPM4Power1InputBreaker3_Type()
)
imPM4Power1InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputBreaker3.setStatus("current")


class _ImPM4Power1InputSurgeArrester_Type(Integer32):
    """Custom type imPM4Power1InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM4Power1InputSurgeArrester_Object = MibScalar
imPM4Power1InputSurgeArrester = _ImPM4Power1InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 48),
    _ImPM4Power1InputSurgeArrester_Type()
)
imPM4Power1InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1InputSurgeArrester.setStatus("current")


class _ImPM4Power1OutputFuse_Type(Integer32):
    """Custom type imPM4Power1OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1OutputFuse_Type.__name__ = "Integer32"
_ImPM4Power1OutputFuse_Object = MibScalar
imPM4Power1OutputFuse = _ImPM4Power1OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 49),
    _ImPM4Power1OutputFuse_Type()
)
imPM4Power1OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputFuse.setStatus("current")


class _ImPM4Power1OutputFuse1_Type(Integer32):
    """Custom type imPM4Power1OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1OutputFuse1_Type.__name__ = "Integer32"
_ImPM4Power1OutputFuse1_Object = MibScalar
imPM4Power1OutputFuse1 = _ImPM4Power1OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 50),
    _ImPM4Power1OutputFuse1_Type()
)
imPM4Power1OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputFuse1.setStatus("current")


class _ImPM4Power1OutputFuse2_Type(Integer32):
    """Custom type imPM4Power1OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1OutputFuse2_Type.__name__ = "Integer32"
_ImPM4Power1OutputFuse2_Object = MibScalar
imPM4Power1OutputFuse2 = _ImPM4Power1OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 51),
    _ImPM4Power1OutputFuse2_Type()
)
imPM4Power1OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputFuse2.setStatus("current")


class _ImPM4Power1OutputBreaker_Type(Integer32):
    """Custom type imPM4Power1OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1OutputBreaker_Type.__name__ = "Integer32"
_ImPM4Power1OutputBreaker_Object = MibScalar
imPM4Power1OutputBreaker = _ImPM4Power1OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 52),
    _ImPM4Power1OutputBreaker_Type()
)
imPM4Power1OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputBreaker.setStatus("current")


class _ImPM4Power1OutputBreaker1_Type(Integer32):
    """Custom type imPM4Power1OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1OutputBreaker1_Type.__name__ = "Integer32"
_ImPM4Power1OutputBreaker1_Object = MibScalar
imPM4Power1OutputBreaker1 = _ImPM4Power1OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 53),
    _ImPM4Power1OutputBreaker1_Type()
)
imPM4Power1OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputBreaker1.setStatus("current")


class _ImPM4Power1OutputBreaker2_Type(Integer32):
    """Custom type imPM4Power1OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1OutputBreaker2_Type.__name__ = "Integer32"
_ImPM4Power1OutputBreaker2_Object = MibScalar
imPM4Power1OutputBreaker2 = _ImPM4Power1OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 54),
    _ImPM4Power1OutputBreaker2_Type()
)
imPM4Power1OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputBreaker2.setStatus("current")


class _ImPM4Power1Fan_Type(Integer32):
    """Custom type imPM4Power1Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1Fan_Type.__name__ = "Integer32"
_ImPM4Power1Fan_Object = MibScalar
imPM4Power1Fan = _ImPM4Power1Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 55),
    _ImPM4Power1Fan_Type()
)
imPM4Power1Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1Fan.setStatus("current")


class _ImPM4Power1BatteryAvailable_Type(Integer32):
    """Custom type imPM4Power1BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power1BatteryAvailable_Type.__name__ = "Integer32"
_ImPM4Power1BatteryAvailable_Object = MibScalar
imPM4Power1BatteryAvailable = _ImPM4Power1BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 56),
    _ImPM4Power1BatteryAvailable_Type()
)
imPM4Power1BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1BatteryAvailable.setStatus("current")
_ImPM4Power1OutputVoltagePhase1_Type = Integer32
_ImPM4Power1OutputVoltagePhase1_Object = MibScalar
imPM4Power1OutputVoltagePhase1 = _ImPM4Power1OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 57),
    _ImPM4Power1OutputVoltagePhase1_Type()
)
imPM4Power1OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputVoltagePhase1.setUnits("0.1 V")
_ImPM4Power1OutputCurrentPhase1_Type = Integer32
_ImPM4Power1OutputCurrentPhase1_Object = MibScalar
imPM4Power1OutputCurrentPhase1 = _ImPM4Power1OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 58),
    _ImPM4Power1OutputCurrentPhase1_Type()
)
imPM4Power1OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputCurrentPhase1.setUnits("0.1 A")
_ImPM4Power1OutputPowerVAphase1_Type = Integer32
_ImPM4Power1OutputPowerVAphase1_Object = MibScalar
imPM4Power1OutputPowerVAphase1 = _ImPM4Power1OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 59),
    _ImPM4Power1OutputPowerVAphase1_Type()
)
imPM4Power1OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerVAphase1.setUnits("VA")
_ImPM4Power1OutputPowerKVAphase1_Type = Integer32
_ImPM4Power1OutputPowerKVAphase1_Object = MibScalar
imPM4Power1OutputPowerKVAphase1 = _ImPM4Power1OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 60),
    _ImPM4Power1OutputPowerKVAphase1_Type()
)
imPM4Power1OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM4Power1OutputVoltagePhase2_Type = Integer32
_ImPM4Power1OutputVoltagePhase2_Object = MibScalar
imPM4Power1OutputVoltagePhase2 = _ImPM4Power1OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 61),
    _ImPM4Power1OutputVoltagePhase2_Type()
)
imPM4Power1OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputVoltagePhase2.setUnits("0.1 V")
_ImPM4Power1OutputCurrentPhase2_Type = Integer32
_ImPM4Power1OutputCurrentPhase2_Object = MibScalar
imPM4Power1OutputCurrentPhase2 = _ImPM4Power1OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 62),
    _ImPM4Power1OutputCurrentPhase2_Type()
)
imPM4Power1OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputCurrentPhase2.setUnits("0.1 A")
_ImPM4Power1OutputPowerVAphase2_Type = Integer32
_ImPM4Power1OutputPowerVAphase2_Object = MibScalar
imPM4Power1OutputPowerVAphase2 = _ImPM4Power1OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 63),
    _ImPM4Power1OutputPowerVAphase2_Type()
)
imPM4Power1OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerVAphase2.setUnits("VA")
_ImPM4Power1OutputPowerKVAphase2_Type = Integer32
_ImPM4Power1OutputPowerKVAphase2_Object = MibScalar
imPM4Power1OutputPowerKVAphase2 = _ImPM4Power1OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 64),
    _ImPM4Power1OutputPowerKVAphase2_Type()
)
imPM4Power1OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM4Power1OutputVoltagePhase3_Type = Integer32
_ImPM4Power1OutputVoltagePhase3_Object = MibScalar
imPM4Power1OutputVoltagePhase3 = _ImPM4Power1OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 65),
    _ImPM4Power1OutputVoltagePhase3_Type()
)
imPM4Power1OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputVoltagePhase3.setUnits("0.1 V")
_ImPM4Power1OutputCurrentPhase3_Type = Integer32
_ImPM4Power1OutputCurrentPhase3_Object = MibScalar
imPM4Power1OutputCurrentPhase3 = _ImPM4Power1OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 66),
    _ImPM4Power1OutputCurrentPhase3_Type()
)
imPM4Power1OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputCurrentPhase3.setUnits("0.1 A")
_ImPM4Power1OutputPowerVAphase3_Type = Integer32
_ImPM4Power1OutputPowerVAphase3_Object = MibScalar
imPM4Power1OutputPowerVAphase3 = _ImPM4Power1OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 67),
    _ImPM4Power1OutputPowerVAphase3_Type()
)
imPM4Power1OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerVAphase3.setUnits("VA")
_ImPM4Power1OutputPowerKVAphase3_Type = Integer32
_ImPM4Power1OutputPowerKVAphase3_Object = MibScalar
imPM4Power1OutputPowerKVAphase3 = _ImPM4Power1OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 3, 68),
    _ImPM4Power1OutputPowerKVAphase3_Type()
)
imPM4Power1OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power1OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM4Power2_ObjectIdentity = ObjectIdentity
imPM4Power2 = _ImPM4Power2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4)
)


class _ImPM4Power2Manufacturer_Type(DisplayString):
    """Custom type imPM4Power2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM4Power2Manufacturer_Type.__name__ = "DisplayString"
_ImPM4Power2Manufacturer_Object = MibScalar
imPM4Power2Manufacturer = _ImPM4Power2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 1),
    _ImPM4Power2Manufacturer_Type()
)
imPM4Power2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Manufacturer.setStatus("current")


class _ImPM4Power2Type_Type(DisplayString):
    """Custom type imPM4Power2Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power2Type_Type.__name__ = "DisplayString"
_ImPM4Power2Type_Object = MibScalar
imPM4Power2Type = _ImPM4Power2Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 2),
    _ImPM4Power2Type_Type()
)
imPM4Power2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Type.setStatus("current")


class _ImPM4Power2serNumb_Type(DisplayString):
    """Custom type imPM4Power2serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power2serNumb_Type.__name__ = "DisplayString"
_ImPM4Power2serNumb_Object = MibScalar
imPM4Power2serNumb = _ImPM4Power2serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 3),
    _ImPM4Power2serNumb_Type()
)
imPM4Power2serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2serNumb.setStatus("current")


class _ImPM4Power2nextServiceDate_Type(DisplayString):
    """Custom type imPM4Power2nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power2nextServiceDate_Type.__name__ = "DisplayString"
_ImPM4Power2nextServiceDate_Object = MibScalar
imPM4Power2nextServiceDate = _ImPM4Power2nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 4),
    _ImPM4Power2nextServiceDate_Type()
)
imPM4Power2nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2nextServiceDate.setStatus("current")
_ImPM4Power2InputVoltage_Type = Integer32
_ImPM4Power2InputVoltage_Object = MibScalar
imPM4Power2InputVoltage = _ImPM4Power2InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 5),
    _ImPM4Power2InputVoltage_Type()
)
imPM4Power2InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputVoltage.setUnits("0.1 V")
_ImPM4Power2InputCurrent_Type = Integer32
_ImPM4Power2InputCurrent_Object = MibScalar
imPM4Power2InputCurrent = _ImPM4Power2InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 6),
    _ImPM4Power2InputCurrent_Type()
)
imPM4Power2InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputCurrent.setUnits("0.1 A")
_ImPM4Power2InputPowerVA_Type = Integer32
_ImPM4Power2InputPowerVA_Object = MibScalar
imPM4Power2InputPowerVA = _ImPM4Power2InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 7),
    _ImPM4Power2InputPowerVA_Type()
)
imPM4Power2InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerVA.setUnits("VA")
_ImPM4Power2InputPowerKVA_Type = Integer32
_ImPM4Power2InputPowerKVA_Object = MibScalar
imPM4Power2InputPowerKVA = _ImPM4Power2InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 8),
    _ImPM4Power2InputPowerKVA_Type()
)
imPM4Power2InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKVA.setUnits("0.1 kVA")
_ImPM4Power2InputPowerW_Type = Integer32
_ImPM4Power2InputPowerW_Object = MibScalar
imPM4Power2InputPowerW = _ImPM4Power2InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 9),
    _ImPM4Power2InputPowerW_Type()
)
imPM4Power2InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerW.setUnits("W")
_ImPM4Power2InputPowerKW_Type = Integer32
_ImPM4Power2InputPowerKW_Object = MibScalar
imPM4Power2InputPowerKW = _ImPM4Power2InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 10),
    _ImPM4Power2InputPowerKW_Type()
)
imPM4Power2InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKW.setUnits("0.1 kW")
_ImPM4Power2InputVoltagePhase1_Type = Integer32
_ImPM4Power2InputVoltagePhase1_Object = MibScalar
imPM4Power2InputVoltagePhase1 = _ImPM4Power2InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 11),
    _ImPM4Power2InputVoltagePhase1_Type()
)
imPM4Power2InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputVoltagePhase1.setUnits("0.1 V")
_ImPM4Power2InputCurrentPhase1_Type = Integer32
_ImPM4Power2InputCurrentPhase1_Object = MibScalar
imPM4Power2InputCurrentPhase1 = _ImPM4Power2InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 12),
    _ImPM4Power2InputCurrentPhase1_Type()
)
imPM4Power2InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputCurrentPhase1.setUnits("0.1 A")
_ImPM4Power2InputPowerVAphase1_Type = Integer32
_ImPM4Power2InputPowerVAphase1_Object = MibScalar
imPM4Power2InputPowerVAphase1 = _ImPM4Power2InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 13),
    _ImPM4Power2InputPowerVAphase1_Type()
)
imPM4Power2InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerVAphase1.setUnits("VA")
_ImPM4Power2InputPowerKVAphase1_Type = Integer32
_ImPM4Power2InputPowerKVAphase1_Object = MibScalar
imPM4Power2InputPowerKVAphase1 = _ImPM4Power2InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 14),
    _ImPM4Power2InputPowerKVAphase1_Type()
)
imPM4Power2InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM4Power2InputVoltagePhase2_Type = Integer32
_ImPM4Power2InputVoltagePhase2_Object = MibScalar
imPM4Power2InputVoltagePhase2 = _ImPM4Power2InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 15),
    _ImPM4Power2InputVoltagePhase2_Type()
)
imPM4Power2InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputVoltagePhase2.setUnits("0.1 V")
_ImPM4Power2InputCurrentPhase2_Type = Integer32
_ImPM4Power2InputCurrentPhase2_Object = MibScalar
imPM4Power2InputCurrentPhase2 = _ImPM4Power2InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 16),
    _ImPM4Power2InputCurrentPhase2_Type()
)
imPM4Power2InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputCurrentPhase2.setUnits("0.1 A")
_ImPM4Power2InputPowerVAphase2_Type = Integer32
_ImPM4Power2InputPowerVAphase2_Object = MibScalar
imPM4Power2InputPowerVAphase2 = _ImPM4Power2InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 17),
    _ImPM4Power2InputPowerVAphase2_Type()
)
imPM4Power2InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerVAphase2.setUnits("VA")
_ImPM4Power2InputPowerKVAphase2_Type = Integer32
_ImPM4Power2InputPowerKVAphase2_Object = MibScalar
imPM4Power2InputPowerKVAphase2 = _ImPM4Power2InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 18),
    _ImPM4Power2InputPowerKVAphase2_Type()
)
imPM4Power2InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM4Power2InputVoltagePhase3_Type = Integer32
_ImPM4Power2InputVoltagePhase3_Object = MibScalar
imPM4Power2InputVoltagePhase3 = _ImPM4Power2InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 19),
    _ImPM4Power2InputVoltagePhase3_Type()
)
imPM4Power2InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputVoltagePhase3.setUnits("0.1 V")
_ImPM4Power2InputCurrentPhase3_Type = Integer32
_ImPM4Power2InputCurrentPhase3_Object = MibScalar
imPM4Power2InputCurrentPhase3 = _ImPM4Power2InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 20),
    _ImPM4Power2InputCurrentPhase3_Type()
)
imPM4Power2InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputCurrentPhase3.setUnits("0.1 A")
_ImPM4Power2InputPowerVAphase3_Type = Integer32
_ImPM4Power2InputPowerVAphase3_Object = MibScalar
imPM4Power2InputPowerVAphase3 = _ImPM4Power2InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 21),
    _ImPM4Power2InputPowerVAphase3_Type()
)
imPM4Power2InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerVAphase3.setUnits("VA")
_ImPM4Power2InputPowerKVAphase3_Type = Integer32
_ImPM4Power2InputPowerKVAphase3_Object = MibScalar
imPM4Power2InputPowerKVAphase3 = _ImPM4Power2InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 22),
    _ImPM4Power2InputPowerKVAphase3_Type()
)
imPM4Power2InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM4Power2OutputVoltage_Type = Integer32
_ImPM4Power2OutputVoltage_Object = MibScalar
imPM4Power2OutputVoltage = _ImPM4Power2OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 23),
    _ImPM4Power2OutputVoltage_Type()
)
imPM4Power2OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputVoltage.setUnits("0.1 V")
_ImPM4Power2OutputCurrent_Type = Integer32
_ImPM4Power2OutputCurrent_Object = MibScalar
imPM4Power2OutputCurrent = _ImPM4Power2OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 24),
    _ImPM4Power2OutputCurrent_Type()
)
imPM4Power2OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputCurrent.setUnits("0.1 A")
_ImPM4Power2OutputPowerVA_Type = Integer32
_ImPM4Power2OutputPowerVA_Object = MibScalar
imPM4Power2OutputPowerVA = _ImPM4Power2OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 25),
    _ImPM4Power2OutputPowerVA_Type()
)
imPM4Power2OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerVA.setUnits("VA")
_ImPM4Power2OutputPowerKVA_Type = Integer32
_ImPM4Power2OutputPowerKVA_Object = MibScalar
imPM4Power2OutputPowerKVA = _ImPM4Power2OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 26),
    _ImPM4Power2OutputPowerKVA_Type()
)
imPM4Power2OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKVA.setUnits("0.1 kVA")
_ImPM4Power2OutputPowerW_Type = Integer32
_ImPM4Power2OutputPowerW_Object = MibScalar
imPM4Power2OutputPowerW = _ImPM4Power2OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 27),
    _ImPM4Power2OutputPowerW_Type()
)
imPM4Power2OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerW.setUnits("W")
_ImPM4Power2OutputPowerKW_Type = Integer32
_ImPM4Power2OutputPowerKW_Object = MibScalar
imPM4Power2OutputPowerKW = _ImPM4Power2OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 28),
    _ImPM4Power2OutputPowerKW_Type()
)
imPM4Power2OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKW.setUnits("0.1 kW")
_ImPM4Power2OutputLoad_Type = Integer32
_ImPM4Power2OutputLoad_Object = MibScalar
imPM4Power2OutputLoad = _ImPM4Power2OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 29),
    _ImPM4Power2OutputLoad_Type()
)
imPM4Power2OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputLoad.setUnits("%")
_ImPM4Power2OutputFrequency_Type = NonNegativeInteger
_ImPM4Power2OutputFrequency_Object = MibScalar
imPM4Power2OutputFrequency = _ImPM4Power2OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 30),
    _ImPM4Power2OutputFrequency_Type()
)
imPM4Power2OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputFrequency.setUnits("0.1 Hz")
_ImPM4Power2Temperature_Type = Integer32
_ImPM4Power2Temperature_Object = MibScalar
imPM4Power2Temperature = _ImPM4Power2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 31),
    _ImPM4Power2Temperature_Type()
)
imPM4Power2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2Temperature.setUnits("degrees Centigrade")


class _ImPM4Power2Running1_Type(Integer32):
    """Custom type imPM4Power2Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Running1_Type.__name__ = "Integer32"
_ImPM4Power2Running1_Object = MibScalar
imPM4Power2Running1 = _ImPM4Power2Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 32),
    _ImPM4Power2Running1_Type()
)
imPM4Power2Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Running1.setStatus("current")


class _ImPM4Power2Running2_Type(Integer32):
    """Custom type imPM4Power2Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Running2_Type.__name__ = "Integer32"
_ImPM4Power2Running2_Object = MibScalar
imPM4Power2Running2 = _ImPM4Power2Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 33),
    _ImPM4Power2Running2_Type()
)
imPM4Power2Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Running2.setStatus("current")


class _ImPM4Power2Running3_Type(Integer32):
    """Custom type imPM4Power2Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Running3_Type.__name__ = "Integer32"
_ImPM4Power2Running3_Object = MibScalar
imPM4Power2Running3 = _ImPM4Power2Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 34),
    _ImPM4Power2Running3_Type()
)
imPM4Power2Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Running3.setStatus("current")


class _ImPM4Power2Running4_Type(Integer32):
    """Custom type imPM4Power2Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Running4_Type.__name__ = "Integer32"
_ImPM4Power2Running4_Object = MibScalar
imPM4Power2Running4 = _ImPM4Power2Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 35),
    _ImPM4Power2Running4_Type()
)
imPM4Power2Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Running4.setStatus("current")


class _ImPM4Power2Running5_Type(Integer32):
    """Custom type imPM4Power2Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Running5_Type.__name__ = "Integer32"
_ImPM4Power2Running5_Object = MibScalar
imPM4Power2Running5 = _ImPM4Power2Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 36),
    _ImPM4Power2Running5_Type()
)
imPM4Power2Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Running5.setStatus("current")


class _ImPM4Power2Running6_Type(Integer32):
    """Custom type imPM4Power2Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Running6_Type.__name__ = "Integer32"
_ImPM4Power2Running6_Object = MibScalar
imPM4Power2Running6 = _ImPM4Power2Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 37),
    _ImPM4Power2Running6_Type()
)
imPM4Power2Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Running6.setStatus("current")


class _ImPM4Power2Running7_Type(Integer32):
    """Custom type imPM4Power2Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Running7_Type.__name__ = "Integer32"
_ImPM4Power2Running7_Object = MibScalar
imPM4Power2Running7 = _ImPM4Power2Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 38),
    _ImPM4Power2Running7_Type()
)
imPM4Power2Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Running7.setStatus("current")


class _ImPM4Power2Running8_Type(Integer32):
    """Custom type imPM4Power2Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Running8_Type.__name__ = "Integer32"
_ImPM4Power2Running8_Object = MibScalar
imPM4Power2Running8 = _ImPM4Power2Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 39),
    _ImPM4Power2Running8_Type()
)
imPM4Power2Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Running8.setStatus("current")


class _ImPM4Power2InputFuse_Type(Integer32):
    """Custom type imPM4Power2InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputFuse_Type.__name__ = "Integer32"
_ImPM4Power2InputFuse_Object = MibScalar
imPM4Power2InputFuse = _ImPM4Power2InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 40),
    _ImPM4Power2InputFuse_Type()
)
imPM4Power2InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputFuse.setStatus("current")


class _ImPM4Power2InputFuse1_Type(Integer32):
    """Custom type imPM4Power2InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputFuse1_Type.__name__ = "Integer32"
_ImPM4Power2InputFuse1_Object = MibScalar
imPM4Power2InputFuse1 = _ImPM4Power2InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 41),
    _ImPM4Power2InputFuse1_Type()
)
imPM4Power2InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputFuse1.setStatus("current")


class _ImPM4Power2InputFuse2_Type(Integer32):
    """Custom type imPM4Power2InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputFuse2_Type.__name__ = "Integer32"
_ImPM4Power2InputFuse2_Object = MibScalar
imPM4Power2InputFuse2 = _ImPM4Power2InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 42),
    _ImPM4Power2InputFuse2_Type()
)
imPM4Power2InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputFuse2.setStatus("current")


class _ImPM4Power2InputFuse3_Type(Integer32):
    """Custom type imPM4Power2InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputFuse3_Type.__name__ = "Integer32"
_ImPM4Power2InputFuse3_Object = MibScalar
imPM4Power2InputFuse3 = _ImPM4Power2InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 43),
    _ImPM4Power2InputFuse3_Type()
)
imPM4Power2InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputFuse3.setStatus("current")


class _ImPM4Power2InputBreaker_Type(Integer32):
    """Custom type imPM4Power2InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputBreaker_Type.__name__ = "Integer32"
_ImPM4Power2InputBreaker_Object = MibScalar
imPM4Power2InputBreaker = _ImPM4Power2InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 44),
    _ImPM4Power2InputBreaker_Type()
)
imPM4Power2InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputBreaker.setStatus("current")


class _ImPM4Power2InputBreaker1_Type(Integer32):
    """Custom type imPM4Power2InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputBreaker1_Type.__name__ = "Integer32"
_ImPM4Power2InputBreaker1_Object = MibScalar
imPM4Power2InputBreaker1 = _ImPM4Power2InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 45),
    _ImPM4Power2InputBreaker1_Type()
)
imPM4Power2InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputBreaker1.setStatus("current")


class _ImPM4Power2InputBreaker2_Type(Integer32):
    """Custom type imPM4Power2InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputBreaker2_Type.__name__ = "Integer32"
_ImPM4Power2InputBreaker2_Object = MibScalar
imPM4Power2InputBreaker2 = _ImPM4Power2InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 46),
    _ImPM4Power2InputBreaker2_Type()
)
imPM4Power2InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputBreaker2.setStatus("current")


class _ImPM4Power2InputBreaker3_Type(Integer32):
    """Custom type imPM4Power2InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputBreaker3_Type.__name__ = "Integer32"
_ImPM4Power2InputBreaker3_Object = MibScalar
imPM4Power2InputBreaker3 = _ImPM4Power2InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 47),
    _ImPM4Power2InputBreaker3_Type()
)
imPM4Power2InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputBreaker3.setStatus("current")


class _ImPM4Power2InputSurgeArrester_Type(Integer32):
    """Custom type imPM4Power2InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM4Power2InputSurgeArrester_Object = MibScalar
imPM4Power2InputSurgeArrester = _ImPM4Power2InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 48),
    _ImPM4Power2InputSurgeArrester_Type()
)
imPM4Power2InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2InputSurgeArrester.setStatus("current")


class _ImPM4Power2OutputFuse_Type(Integer32):
    """Custom type imPM4Power2OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2OutputFuse_Type.__name__ = "Integer32"
_ImPM4Power2OutputFuse_Object = MibScalar
imPM4Power2OutputFuse = _ImPM4Power2OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 49),
    _ImPM4Power2OutputFuse_Type()
)
imPM4Power2OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputFuse.setStatus("current")


class _ImPM4Power2OutputFuse1_Type(Integer32):
    """Custom type imPM4Power2OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2OutputFuse1_Type.__name__ = "Integer32"
_ImPM4Power2OutputFuse1_Object = MibScalar
imPM4Power2OutputFuse1 = _ImPM4Power2OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 50),
    _ImPM4Power2OutputFuse1_Type()
)
imPM4Power2OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputFuse1.setStatus("current")


class _ImPM4Power2OutputFuse2_Type(Integer32):
    """Custom type imPM4Power2OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2OutputFuse2_Type.__name__ = "Integer32"
_ImPM4Power2OutputFuse2_Object = MibScalar
imPM4Power2OutputFuse2 = _ImPM4Power2OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 51),
    _ImPM4Power2OutputFuse2_Type()
)
imPM4Power2OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputFuse2.setStatus("current")


class _ImPM4Power2OutputBreaker_Type(Integer32):
    """Custom type imPM4Power2OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2OutputBreaker_Type.__name__ = "Integer32"
_ImPM4Power2OutputBreaker_Object = MibScalar
imPM4Power2OutputBreaker = _ImPM4Power2OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 52),
    _ImPM4Power2OutputBreaker_Type()
)
imPM4Power2OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputBreaker.setStatus("current")


class _ImPM4Power2OutputBreaker1_Type(Integer32):
    """Custom type imPM4Power2OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2OutputBreaker1_Type.__name__ = "Integer32"
_ImPM4Power2OutputBreaker1_Object = MibScalar
imPM4Power2OutputBreaker1 = _ImPM4Power2OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 53),
    _ImPM4Power2OutputBreaker1_Type()
)
imPM4Power2OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputBreaker1.setStatus("current")


class _ImPM4Power2OutputBreaker2_Type(Integer32):
    """Custom type imPM4Power2OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2OutputBreaker2_Type.__name__ = "Integer32"
_ImPM4Power2OutputBreaker2_Object = MibScalar
imPM4Power2OutputBreaker2 = _ImPM4Power2OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 54),
    _ImPM4Power2OutputBreaker2_Type()
)
imPM4Power2OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputBreaker2.setStatus("current")


class _ImPM4Power2Fan_Type(Integer32):
    """Custom type imPM4Power2Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2Fan_Type.__name__ = "Integer32"
_ImPM4Power2Fan_Object = MibScalar
imPM4Power2Fan = _ImPM4Power2Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 55),
    _ImPM4Power2Fan_Type()
)
imPM4Power2Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2Fan.setStatus("current")


class _ImPM4Power2BatteryAvailable_Type(Integer32):
    """Custom type imPM4Power2BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power2BatteryAvailable_Type.__name__ = "Integer32"
_ImPM4Power2BatteryAvailable_Object = MibScalar
imPM4Power2BatteryAvailable = _ImPM4Power2BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 56),
    _ImPM4Power2BatteryAvailable_Type()
)
imPM4Power2BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2BatteryAvailable.setStatus("current")
_ImPM4Power2OutputVoltagePhase1_Type = Integer32
_ImPM4Power2OutputVoltagePhase1_Object = MibScalar
imPM4Power2OutputVoltagePhase1 = _ImPM4Power2OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 57),
    _ImPM4Power2OutputVoltagePhase1_Type()
)
imPM4Power2OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputVoltagePhase1.setUnits("0.1 V")
_ImPM4Power2OutputCurrentPhase1_Type = Integer32
_ImPM4Power2OutputCurrentPhase1_Object = MibScalar
imPM4Power2OutputCurrentPhase1 = _ImPM4Power2OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 58),
    _ImPM4Power2OutputCurrentPhase1_Type()
)
imPM4Power2OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputCurrentPhase1.setUnits("0.1 A")
_ImPM4Power2OutputPowerVAphase1_Type = Integer32
_ImPM4Power2OutputPowerVAphase1_Object = MibScalar
imPM4Power2OutputPowerVAphase1 = _ImPM4Power2OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 59),
    _ImPM4Power2OutputPowerVAphase1_Type()
)
imPM4Power2OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerVAphase1.setUnits("VA")
_ImPM4Power2OutputPowerKVAphase1_Type = Integer32
_ImPM4Power2OutputPowerKVAphase1_Object = MibScalar
imPM4Power2OutputPowerKVAphase1 = _ImPM4Power2OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 60),
    _ImPM4Power2OutputPowerKVAphase1_Type()
)
imPM4Power2OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM4Power2OutputVoltagePhase2_Type = Integer32
_ImPM4Power2OutputVoltagePhase2_Object = MibScalar
imPM4Power2OutputVoltagePhase2 = _ImPM4Power2OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 61),
    _ImPM4Power2OutputVoltagePhase2_Type()
)
imPM4Power2OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputVoltagePhase2.setUnits("0.1 V")
_ImPM4Power2OutputCurrentPhase2_Type = Integer32
_ImPM4Power2OutputCurrentPhase2_Object = MibScalar
imPM4Power2OutputCurrentPhase2 = _ImPM4Power2OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 62),
    _ImPM4Power2OutputCurrentPhase2_Type()
)
imPM4Power2OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputCurrentPhase2.setUnits("0.1 A")
_ImPM4Power2OutputPowerVAphase2_Type = Integer32
_ImPM4Power2OutputPowerVAphase2_Object = MibScalar
imPM4Power2OutputPowerVAphase2 = _ImPM4Power2OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 63),
    _ImPM4Power2OutputPowerVAphase2_Type()
)
imPM4Power2OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerVAphase2.setUnits("VA")
_ImPM4Power2OutputPowerKVAphase2_Type = Integer32
_ImPM4Power2OutputPowerKVAphase2_Object = MibScalar
imPM4Power2OutputPowerKVAphase2 = _ImPM4Power2OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 64),
    _ImPM4Power2OutputPowerKVAphase2_Type()
)
imPM4Power2OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM4Power2OutputVoltagePhase3_Type = Integer32
_ImPM4Power2OutputVoltagePhase3_Object = MibScalar
imPM4Power2OutputVoltagePhase3 = _ImPM4Power2OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 65),
    _ImPM4Power2OutputVoltagePhase3_Type()
)
imPM4Power2OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputVoltagePhase3.setUnits("0.1 V")
_ImPM4Power2OutputCurrentPhase3_Type = Integer32
_ImPM4Power2OutputCurrentPhase3_Object = MibScalar
imPM4Power2OutputCurrentPhase3 = _ImPM4Power2OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 66),
    _ImPM4Power2OutputCurrentPhase3_Type()
)
imPM4Power2OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputCurrentPhase3.setUnits("0.1 A")
_ImPM4Power2OutputPowerVAphase3_Type = Integer32
_ImPM4Power2OutputPowerVAphase3_Object = MibScalar
imPM4Power2OutputPowerVAphase3 = _ImPM4Power2OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 67),
    _ImPM4Power2OutputPowerVAphase3_Type()
)
imPM4Power2OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerVAphase3.setUnits("VA")
_ImPM4Power2OutputPowerKVAphase3_Type = Integer32
_ImPM4Power2OutputPowerKVAphase3_Object = MibScalar
imPM4Power2OutputPowerKVAphase3 = _ImPM4Power2OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 4, 68),
    _ImPM4Power2OutputPowerKVAphase3_Type()
)
imPM4Power2OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power2OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM4Power3_ObjectIdentity = ObjectIdentity
imPM4Power3 = _ImPM4Power3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5)
)


class _ImPM4Power3Manufacturer_Type(DisplayString):
    """Custom type imPM4Power3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM4Power3Manufacturer_Type.__name__ = "DisplayString"
_ImPM4Power3Manufacturer_Object = MibScalar
imPM4Power3Manufacturer = _ImPM4Power3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 1),
    _ImPM4Power3Manufacturer_Type()
)
imPM4Power3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Manufacturer.setStatus("current")


class _ImPM4Power3Type_Type(DisplayString):
    """Custom type imPM4Power3Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power3Type_Type.__name__ = "DisplayString"
_ImPM4Power3Type_Object = MibScalar
imPM4Power3Type = _ImPM4Power3Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 2),
    _ImPM4Power3Type_Type()
)
imPM4Power3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Type.setStatus("current")


class _ImPM4Power3serNumb_Type(DisplayString):
    """Custom type imPM4Power3serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power3serNumb_Type.__name__ = "DisplayString"
_ImPM4Power3serNumb_Object = MibScalar
imPM4Power3serNumb = _ImPM4Power3serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 3),
    _ImPM4Power3serNumb_Type()
)
imPM4Power3serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3serNumb.setStatus("current")


class _ImPM4Power3nextServiceDate_Type(DisplayString):
    """Custom type imPM4Power3nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4Power3nextServiceDate_Type.__name__ = "DisplayString"
_ImPM4Power3nextServiceDate_Object = MibScalar
imPM4Power3nextServiceDate = _ImPM4Power3nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 4),
    _ImPM4Power3nextServiceDate_Type()
)
imPM4Power3nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3nextServiceDate.setStatus("current")
_ImPM4Power3InputVoltage_Type = Integer32
_ImPM4Power3InputVoltage_Object = MibScalar
imPM4Power3InputVoltage = _ImPM4Power3InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 5),
    _ImPM4Power3InputVoltage_Type()
)
imPM4Power3InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputVoltage.setUnits("0.1 V")
_ImPM4Power3InputCurrent_Type = Integer32
_ImPM4Power3InputCurrent_Object = MibScalar
imPM4Power3InputCurrent = _ImPM4Power3InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 6),
    _ImPM4Power3InputCurrent_Type()
)
imPM4Power3InputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputCurrent.setUnits("0.1 A")
_ImPM4Power3InputPowerVA_Type = Integer32
_ImPM4Power3InputPowerVA_Object = MibScalar
imPM4Power3InputPowerVA = _ImPM4Power3InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 7),
    _ImPM4Power3InputPowerVA_Type()
)
imPM4Power3InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerVA.setUnits("VA")
_ImPM4Power3InputPowerKVA_Type = Integer32
_ImPM4Power3InputPowerKVA_Object = MibScalar
imPM4Power3InputPowerKVA = _ImPM4Power3InputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 8),
    _ImPM4Power3InputPowerKVA_Type()
)
imPM4Power3InputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKVA.setUnits("0.1 kVA")
_ImPM4Power3InputPowerW_Type = Integer32
_ImPM4Power3InputPowerW_Object = MibScalar
imPM4Power3InputPowerW = _ImPM4Power3InputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 9),
    _ImPM4Power3InputPowerW_Type()
)
imPM4Power3InputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerW.setUnits("W")
_ImPM4Power3InputPowerKW_Type = Integer32
_ImPM4Power3InputPowerKW_Object = MibScalar
imPM4Power3InputPowerKW = _ImPM4Power3InputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 10),
    _ImPM4Power3InputPowerKW_Type()
)
imPM4Power3InputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKW.setUnits("0.1 kW")
_ImPM4Power3InputVoltagePhase1_Type = Integer32
_ImPM4Power3InputVoltagePhase1_Object = MibScalar
imPM4Power3InputVoltagePhase1 = _ImPM4Power3InputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 11),
    _ImPM4Power3InputVoltagePhase1_Type()
)
imPM4Power3InputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputVoltagePhase1.setUnits("0.1 V")
_ImPM4Power3InputCurrentPhase1_Type = Integer32
_ImPM4Power3InputCurrentPhase1_Object = MibScalar
imPM4Power3InputCurrentPhase1 = _ImPM4Power3InputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 12),
    _ImPM4Power3InputCurrentPhase1_Type()
)
imPM4Power3InputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputCurrentPhase1.setUnits("0.1 A")
_ImPM4Power3InputPowerVAphase1_Type = Integer32
_ImPM4Power3InputPowerVAphase1_Object = MibScalar
imPM4Power3InputPowerVAphase1 = _ImPM4Power3InputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 13),
    _ImPM4Power3InputPowerVAphase1_Type()
)
imPM4Power3InputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerVAphase1.setUnits("VA")
_ImPM4Power3InputPowerKVAphase1_Type = Integer32
_ImPM4Power3InputPowerKVAphase1_Object = MibScalar
imPM4Power3InputPowerKVAphase1 = _ImPM4Power3InputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 14),
    _ImPM4Power3InputPowerKVAphase1_Type()
)
imPM4Power3InputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM4Power3InputVoltagePhase2_Type = Integer32
_ImPM4Power3InputVoltagePhase2_Object = MibScalar
imPM4Power3InputVoltagePhase2 = _ImPM4Power3InputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 15),
    _ImPM4Power3InputVoltagePhase2_Type()
)
imPM4Power3InputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputVoltagePhase2.setUnits("0.1 V")
_ImPM4Power3InputCurrentPhase2_Type = Integer32
_ImPM4Power3InputCurrentPhase2_Object = MibScalar
imPM4Power3InputCurrentPhase2 = _ImPM4Power3InputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 16),
    _ImPM4Power3InputCurrentPhase2_Type()
)
imPM4Power3InputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputCurrentPhase2.setUnits("0.1 A")
_ImPM4Power3InputPowerVAphase2_Type = Integer32
_ImPM4Power3InputPowerVAphase2_Object = MibScalar
imPM4Power3InputPowerVAphase2 = _ImPM4Power3InputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 17),
    _ImPM4Power3InputPowerVAphase2_Type()
)
imPM4Power3InputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerVAphase2.setUnits("VA")
_ImPM4Power3InputPowerKVAphase2_Type = Integer32
_ImPM4Power3InputPowerKVAphase2_Object = MibScalar
imPM4Power3InputPowerKVAphase2 = _ImPM4Power3InputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 18),
    _ImPM4Power3InputPowerKVAphase2_Type()
)
imPM4Power3InputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM4Power3InputVoltagePhase3_Type = Integer32
_ImPM4Power3InputVoltagePhase3_Object = MibScalar
imPM4Power3InputVoltagePhase3 = _ImPM4Power3InputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 19),
    _ImPM4Power3InputVoltagePhase3_Type()
)
imPM4Power3InputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputVoltagePhase3.setUnits("0.1 V")
_ImPM4Power3InputCurrentPhase3_Type = Integer32
_ImPM4Power3InputCurrentPhase3_Object = MibScalar
imPM4Power3InputCurrentPhase3 = _ImPM4Power3InputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 20),
    _ImPM4Power3InputCurrentPhase3_Type()
)
imPM4Power3InputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputCurrentPhase3.setUnits("0.1 A")
_ImPM4Power3InputPowerVAphase3_Type = Integer32
_ImPM4Power3InputPowerVAphase3_Object = MibScalar
imPM4Power3InputPowerVAphase3 = _ImPM4Power3InputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 21),
    _ImPM4Power3InputPowerVAphase3_Type()
)
imPM4Power3InputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerVAphase3.setUnits("VA")
_ImPM4Power3InputPowerKVAphase3_Type = Integer32
_ImPM4Power3InputPowerKVAphase3_Object = MibScalar
imPM4Power3InputPowerKVAphase3 = _ImPM4Power3InputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 22),
    _ImPM4Power3InputPowerKVAphase3_Type()
)
imPM4Power3InputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3InputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM4Power3OutputVoltage_Type = Integer32
_ImPM4Power3OutputVoltage_Object = MibScalar
imPM4Power3OutputVoltage = _ImPM4Power3OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 23),
    _ImPM4Power3OutputVoltage_Type()
)
imPM4Power3OutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputVoltage.setUnits("0.1 V")
_ImPM4Power3OutputCurrent_Type = Integer32
_ImPM4Power3OutputCurrent_Object = MibScalar
imPM4Power3OutputCurrent = _ImPM4Power3OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 24),
    _ImPM4Power3OutputCurrent_Type()
)
imPM4Power3OutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputCurrent.setUnits("0.1 A")
_ImPM4Power3OutputPowerVA_Type = Integer32
_ImPM4Power3OutputPowerVA_Object = MibScalar
imPM4Power3OutputPowerVA = _ImPM4Power3OutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 25),
    _ImPM4Power3OutputPowerVA_Type()
)
imPM4Power3OutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerVA.setUnits("VA")
_ImPM4Power3OutputPowerKVA_Type = Integer32
_ImPM4Power3OutputPowerKVA_Object = MibScalar
imPM4Power3OutputPowerKVA = _ImPM4Power3OutputPowerKVA_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 26),
    _ImPM4Power3OutputPowerKVA_Type()
)
imPM4Power3OutputPowerKVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKVA.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKVA.setUnits("0.1 kVA")
_ImPM4Power3OutputPowerW_Type = Integer32
_ImPM4Power3OutputPowerW_Object = MibScalar
imPM4Power3OutputPowerW = _ImPM4Power3OutputPowerW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 27),
    _ImPM4Power3OutputPowerW_Type()
)
imPM4Power3OutputPowerW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerW.setUnits("W")
_ImPM4Power3OutputPowerKW_Type = Integer32
_ImPM4Power3OutputPowerKW_Object = MibScalar
imPM4Power3OutputPowerKW = _ImPM4Power3OutputPowerKW_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 28),
    _ImPM4Power3OutputPowerKW_Type()
)
imPM4Power3OutputPowerKW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKW.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKW.setUnits("0.1 kW")
_ImPM4Power3OutputLoad_Type = Integer32
_ImPM4Power3OutputLoad_Object = MibScalar
imPM4Power3OutputLoad = _ImPM4Power3OutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 29),
    _ImPM4Power3OutputLoad_Type()
)
imPM4Power3OutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputLoad.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputLoad.setUnits("%")
_ImPM4Power3OutputFrequency_Type = NonNegativeInteger
_ImPM4Power3OutputFrequency_Object = MibScalar
imPM4Power3OutputFrequency = _ImPM4Power3OutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 30),
    _ImPM4Power3OutputFrequency_Type()
)
imPM4Power3OutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputFrequency.setUnits("0.1 Hz")
_ImPM4Power3Temperature_Type = Integer32
_ImPM4Power3Temperature_Object = MibScalar
imPM4Power3Temperature = _ImPM4Power3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 31),
    _ImPM4Power3Temperature_Type()
)
imPM4Power3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3Temperature.setUnits("degrees Centigrade")


class _ImPM4Power3Running1_Type(Integer32):
    """Custom type imPM4Power3Running1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Running1_Type.__name__ = "Integer32"
_ImPM4Power3Running1_Object = MibScalar
imPM4Power3Running1 = _ImPM4Power3Running1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 32),
    _ImPM4Power3Running1_Type()
)
imPM4Power3Running1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Running1.setStatus("current")


class _ImPM4Power3Running2_Type(Integer32):
    """Custom type imPM4Power3Running2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Running2_Type.__name__ = "Integer32"
_ImPM4Power3Running2_Object = MibScalar
imPM4Power3Running2 = _ImPM4Power3Running2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 33),
    _ImPM4Power3Running2_Type()
)
imPM4Power3Running2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Running2.setStatus("current")


class _ImPM4Power3Running3_Type(Integer32):
    """Custom type imPM4Power3Running3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Running3_Type.__name__ = "Integer32"
_ImPM4Power3Running3_Object = MibScalar
imPM4Power3Running3 = _ImPM4Power3Running3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 34),
    _ImPM4Power3Running3_Type()
)
imPM4Power3Running3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Running3.setStatus("current")


class _ImPM4Power3Running4_Type(Integer32):
    """Custom type imPM4Power3Running4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Running4_Type.__name__ = "Integer32"
_ImPM4Power3Running4_Object = MibScalar
imPM4Power3Running4 = _ImPM4Power3Running4_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 35),
    _ImPM4Power3Running4_Type()
)
imPM4Power3Running4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Running4.setStatus("current")


class _ImPM4Power3Running5_Type(Integer32):
    """Custom type imPM4Power3Running5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Running5_Type.__name__ = "Integer32"
_ImPM4Power3Running5_Object = MibScalar
imPM4Power3Running5 = _ImPM4Power3Running5_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 36),
    _ImPM4Power3Running5_Type()
)
imPM4Power3Running5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Running5.setStatus("current")


class _ImPM4Power3Running6_Type(Integer32):
    """Custom type imPM4Power3Running6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Running6_Type.__name__ = "Integer32"
_ImPM4Power3Running6_Object = MibScalar
imPM4Power3Running6 = _ImPM4Power3Running6_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 37),
    _ImPM4Power3Running6_Type()
)
imPM4Power3Running6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Running6.setStatus("current")


class _ImPM4Power3Running7_Type(Integer32):
    """Custom type imPM4Power3Running7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Running7_Type.__name__ = "Integer32"
_ImPM4Power3Running7_Object = MibScalar
imPM4Power3Running7 = _ImPM4Power3Running7_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 38),
    _ImPM4Power3Running7_Type()
)
imPM4Power3Running7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Running7.setStatus("current")


class _ImPM4Power3Running8_Type(Integer32):
    """Custom type imPM4Power3Running8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Running8_Type.__name__ = "Integer32"
_ImPM4Power3Running8_Object = MibScalar
imPM4Power3Running8 = _ImPM4Power3Running8_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 39),
    _ImPM4Power3Running8_Type()
)
imPM4Power3Running8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Running8.setStatus("current")


class _ImPM4Power3InputFuse_Type(Integer32):
    """Custom type imPM4Power3InputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputFuse_Type.__name__ = "Integer32"
_ImPM4Power3InputFuse_Object = MibScalar
imPM4Power3InputFuse = _ImPM4Power3InputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 40),
    _ImPM4Power3InputFuse_Type()
)
imPM4Power3InputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputFuse.setStatus("current")


class _ImPM4Power3InputFuse1_Type(Integer32):
    """Custom type imPM4Power3InputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputFuse1_Type.__name__ = "Integer32"
_ImPM4Power3InputFuse1_Object = MibScalar
imPM4Power3InputFuse1 = _ImPM4Power3InputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 41),
    _ImPM4Power3InputFuse1_Type()
)
imPM4Power3InputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputFuse1.setStatus("current")


class _ImPM4Power3InputFuse2_Type(Integer32):
    """Custom type imPM4Power3InputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputFuse2_Type.__name__ = "Integer32"
_ImPM4Power3InputFuse2_Object = MibScalar
imPM4Power3InputFuse2 = _ImPM4Power3InputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 42),
    _ImPM4Power3InputFuse2_Type()
)
imPM4Power3InputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputFuse2.setStatus("current")


class _ImPM4Power3InputFuse3_Type(Integer32):
    """Custom type imPM4Power3InputFuse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputFuse3_Type.__name__ = "Integer32"
_ImPM4Power3InputFuse3_Object = MibScalar
imPM4Power3InputFuse3 = _ImPM4Power3InputFuse3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 43),
    _ImPM4Power3InputFuse3_Type()
)
imPM4Power3InputFuse3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputFuse3.setStatus("current")


class _ImPM4Power3InputBreaker_Type(Integer32):
    """Custom type imPM4Power3InputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputBreaker_Type.__name__ = "Integer32"
_ImPM4Power3InputBreaker_Object = MibScalar
imPM4Power3InputBreaker = _ImPM4Power3InputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 44),
    _ImPM4Power3InputBreaker_Type()
)
imPM4Power3InputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputBreaker.setStatus("current")


class _ImPM4Power3InputBreaker1_Type(Integer32):
    """Custom type imPM4Power3InputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputBreaker1_Type.__name__ = "Integer32"
_ImPM4Power3InputBreaker1_Object = MibScalar
imPM4Power3InputBreaker1 = _ImPM4Power3InputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 45),
    _ImPM4Power3InputBreaker1_Type()
)
imPM4Power3InputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputBreaker1.setStatus("current")


class _ImPM4Power3InputBreaker2_Type(Integer32):
    """Custom type imPM4Power3InputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputBreaker2_Type.__name__ = "Integer32"
_ImPM4Power3InputBreaker2_Object = MibScalar
imPM4Power3InputBreaker2 = _ImPM4Power3InputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 46),
    _ImPM4Power3InputBreaker2_Type()
)
imPM4Power3InputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputBreaker2.setStatus("current")


class _ImPM4Power3InputBreaker3_Type(Integer32):
    """Custom type imPM4Power3InputBreaker3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputBreaker3_Type.__name__ = "Integer32"
_ImPM4Power3InputBreaker3_Object = MibScalar
imPM4Power3InputBreaker3 = _ImPM4Power3InputBreaker3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 47),
    _ImPM4Power3InputBreaker3_Type()
)
imPM4Power3InputBreaker3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputBreaker3.setStatus("current")


class _ImPM4Power3InputSurgeArrester_Type(Integer32):
    """Custom type imPM4Power3InputSurgeArrester based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3InputSurgeArrester_Type.__name__ = "Integer32"
_ImPM4Power3InputSurgeArrester_Object = MibScalar
imPM4Power3InputSurgeArrester = _ImPM4Power3InputSurgeArrester_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 48),
    _ImPM4Power3InputSurgeArrester_Type()
)
imPM4Power3InputSurgeArrester.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3InputSurgeArrester.setStatus("current")


class _ImPM4Power3OutputFuse_Type(Integer32):
    """Custom type imPM4Power3OutputFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3OutputFuse_Type.__name__ = "Integer32"
_ImPM4Power3OutputFuse_Object = MibScalar
imPM4Power3OutputFuse = _ImPM4Power3OutputFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 49),
    _ImPM4Power3OutputFuse_Type()
)
imPM4Power3OutputFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputFuse.setStatus("current")


class _ImPM4Power3OutputFuse1_Type(Integer32):
    """Custom type imPM4Power3OutputFuse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3OutputFuse1_Type.__name__ = "Integer32"
_ImPM4Power3OutputFuse1_Object = MibScalar
imPM4Power3OutputFuse1 = _ImPM4Power3OutputFuse1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 50),
    _ImPM4Power3OutputFuse1_Type()
)
imPM4Power3OutputFuse1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputFuse1.setStatus("current")


class _ImPM4Power3OutputFuse2_Type(Integer32):
    """Custom type imPM4Power3OutputFuse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3OutputFuse2_Type.__name__ = "Integer32"
_ImPM4Power3OutputFuse2_Object = MibScalar
imPM4Power3OutputFuse2 = _ImPM4Power3OutputFuse2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 51),
    _ImPM4Power3OutputFuse2_Type()
)
imPM4Power3OutputFuse2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputFuse2.setStatus("current")


class _ImPM4Power3OutputBreaker_Type(Integer32):
    """Custom type imPM4Power3OutputBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3OutputBreaker_Type.__name__ = "Integer32"
_ImPM4Power3OutputBreaker_Object = MibScalar
imPM4Power3OutputBreaker = _ImPM4Power3OutputBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 52),
    _ImPM4Power3OutputBreaker_Type()
)
imPM4Power3OutputBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputBreaker.setStatus("current")


class _ImPM4Power3OutputBreaker1_Type(Integer32):
    """Custom type imPM4Power3OutputBreaker1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3OutputBreaker1_Type.__name__ = "Integer32"
_ImPM4Power3OutputBreaker1_Object = MibScalar
imPM4Power3OutputBreaker1 = _ImPM4Power3OutputBreaker1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 53),
    _ImPM4Power3OutputBreaker1_Type()
)
imPM4Power3OutputBreaker1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputBreaker1.setStatus("current")


class _ImPM4Power3OutputBreaker2_Type(Integer32):
    """Custom type imPM4Power3OutputBreaker2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3OutputBreaker2_Type.__name__ = "Integer32"
_ImPM4Power3OutputBreaker2_Object = MibScalar
imPM4Power3OutputBreaker2 = _ImPM4Power3OutputBreaker2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 54),
    _ImPM4Power3OutputBreaker2_Type()
)
imPM4Power3OutputBreaker2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputBreaker2.setStatus("current")


class _ImPM4Power3Fan_Type(Integer32):
    """Custom type imPM4Power3Fan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3Fan_Type.__name__ = "Integer32"
_ImPM4Power3Fan_Object = MibScalar
imPM4Power3Fan = _ImPM4Power3Fan_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 55),
    _ImPM4Power3Fan_Type()
)
imPM4Power3Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3Fan.setStatus("current")


class _ImPM4Power3BatteryAvailable_Type(Integer32):
    """Custom type imPM4Power3BatteryAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4Power3BatteryAvailable_Type.__name__ = "Integer32"
_ImPM4Power3BatteryAvailable_Object = MibScalar
imPM4Power3BatteryAvailable = _ImPM4Power3BatteryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 56),
    _ImPM4Power3BatteryAvailable_Type()
)
imPM4Power3BatteryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3BatteryAvailable.setStatus("current")
_ImPM4Power3OutputVoltagePhase1_Type = Integer32
_ImPM4Power3OutputVoltagePhase1_Object = MibScalar
imPM4Power3OutputVoltagePhase1 = _ImPM4Power3OutputVoltagePhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 57),
    _ImPM4Power3OutputVoltagePhase1_Type()
)
imPM4Power3OutputVoltagePhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputVoltagePhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputVoltagePhase1.setUnits("0.1 V")
_ImPM4Power3OutputCurrentPhase1_Type = Integer32
_ImPM4Power3OutputCurrentPhase1_Object = MibScalar
imPM4Power3OutputCurrentPhase1 = _ImPM4Power3OutputCurrentPhase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 58),
    _ImPM4Power3OutputCurrentPhase1_Type()
)
imPM4Power3OutputCurrentPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputCurrentPhase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputCurrentPhase1.setUnits("0.1 A")
_ImPM4Power3OutputPowerVAphase1_Type = Integer32
_ImPM4Power3OutputPowerVAphase1_Object = MibScalar
imPM4Power3OutputPowerVAphase1 = _ImPM4Power3OutputPowerVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 59),
    _ImPM4Power3OutputPowerVAphase1_Type()
)
imPM4Power3OutputPowerVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerVAphase1.setUnits("VA")
_ImPM4Power3OutputPowerKVAphase1_Type = Integer32
_ImPM4Power3OutputPowerKVAphase1_Object = MibScalar
imPM4Power3OutputPowerKVAphase1 = _ImPM4Power3OutputPowerKVAphase1_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 60),
    _ImPM4Power3OutputPowerKVAphase1_Type()
)
imPM4Power3OutputPowerKVAphase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKVAphase1.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKVAphase1.setUnits("0.1 kVA")
_ImPM4Power3OutputVoltagePhase2_Type = Integer32
_ImPM4Power3OutputVoltagePhase2_Object = MibScalar
imPM4Power3OutputVoltagePhase2 = _ImPM4Power3OutputVoltagePhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 61),
    _ImPM4Power3OutputVoltagePhase2_Type()
)
imPM4Power3OutputVoltagePhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputVoltagePhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputVoltagePhase2.setUnits("0.1 V")
_ImPM4Power3OutputCurrentPhase2_Type = Integer32
_ImPM4Power3OutputCurrentPhase2_Object = MibScalar
imPM4Power3OutputCurrentPhase2 = _ImPM4Power3OutputCurrentPhase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 62),
    _ImPM4Power3OutputCurrentPhase2_Type()
)
imPM4Power3OutputCurrentPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputCurrentPhase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputCurrentPhase2.setUnits("0.1 A")
_ImPM4Power3OutputPowerVAphase2_Type = Integer32
_ImPM4Power3OutputPowerVAphase2_Object = MibScalar
imPM4Power3OutputPowerVAphase2 = _ImPM4Power3OutputPowerVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 63),
    _ImPM4Power3OutputPowerVAphase2_Type()
)
imPM4Power3OutputPowerVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerVAphase2.setUnits("VA")
_ImPM4Power3OutputPowerKVAphase2_Type = Integer32
_ImPM4Power3OutputPowerKVAphase2_Object = MibScalar
imPM4Power3OutputPowerKVAphase2 = _ImPM4Power3OutputPowerKVAphase2_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 64),
    _ImPM4Power3OutputPowerKVAphase2_Type()
)
imPM4Power3OutputPowerKVAphase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKVAphase2.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKVAphase2.setUnits("0.1 kVA")
_ImPM4Power3OutputVoltagePhase3_Type = Integer32
_ImPM4Power3OutputVoltagePhase3_Object = MibScalar
imPM4Power3OutputVoltagePhase3 = _ImPM4Power3OutputVoltagePhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 65),
    _ImPM4Power3OutputVoltagePhase3_Type()
)
imPM4Power3OutputVoltagePhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputVoltagePhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputVoltagePhase3.setUnits("0.1 V")
_ImPM4Power3OutputCurrentPhase3_Type = Integer32
_ImPM4Power3OutputCurrentPhase3_Object = MibScalar
imPM4Power3OutputCurrentPhase3 = _ImPM4Power3OutputCurrentPhase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 66),
    _ImPM4Power3OutputCurrentPhase3_Type()
)
imPM4Power3OutputCurrentPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputCurrentPhase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputCurrentPhase3.setUnits("0.1 A")
_ImPM4Power3OutputPowerVAphase3_Type = Integer32
_ImPM4Power3OutputPowerVAphase3_Object = MibScalar
imPM4Power3OutputPowerVAphase3 = _ImPM4Power3OutputPowerVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 67),
    _ImPM4Power3OutputPowerVAphase3_Type()
)
imPM4Power3OutputPowerVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerVAphase3.setUnits("VA")
_ImPM4Power3OutputPowerKVAphase3_Type = Integer32
_ImPM4Power3OutputPowerKVAphase3_Object = MibScalar
imPM4Power3OutputPowerKVAphase3 = _ImPM4Power3OutputPowerKVAphase3_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 5, 68),
    _ImPM4Power3OutputPowerKVAphase3_Type()
)
imPM4Power3OutputPowerKVAphase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKVAphase3.setStatus("current")
if mibBuilder.loadTexts:
    imPM4Power3OutputPowerKVAphase3.setUnits("0.1 kVA")
_ImPM4Battery_ObjectIdentity = ObjectIdentity
imPM4Battery = _ImPM4Battery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 6)
)
_ImPM4BatteryNominalCapacity_Type = NonNegativeInteger
_ImPM4BatteryNominalCapacity_Object = MibScalar
imPM4BatteryNominalCapacity = _ImPM4BatteryNominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 6, 1),
    _ImPM4BatteryNominalCapacity_Type()
)
imPM4BatteryNominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatteryNominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatteryNominalCapacity.setUnits("Ah")
_ImPM4BatteryVoltage_Type = Integer32
_ImPM4BatteryVoltage_Object = MibScalar
imPM4BatteryVoltage = _ImPM4BatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 6, 2),
    _ImPM4BatteryVoltage_Type()
)
imPM4BatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatteryVoltage.setUnits("0.1 V")
_ImPM4BatteryCurrent_Type = Integer32
_ImPM4BatteryCurrent_Object = MibScalar
imPM4BatteryCurrent = _ImPM4BatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 6, 3),
    _ImPM4BatteryCurrent_Type()
)
imPM4BatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatteryCurrent.setUnits("0.1 A")
_ImPM4BatteryChargeState_Type = NonNegativeInteger
_ImPM4BatteryChargeState_Object = MibScalar
imPM4BatteryChargeState = _ImPM4BatteryChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 6, 4),
    _ImPM4BatteryChargeState_Type()
)
imPM4BatteryChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatteryChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatteryChargeState.setUnits("%")
_ImPM4BatteryAutonomyTime_Type = NonNegativeInteger
_ImPM4BatteryAutonomyTime_Object = MibScalar
imPM4BatteryAutonomyTime = _ImPM4BatteryAutonomyTime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 6, 5),
    _ImPM4BatteryAutonomyTime_Type()
)
imPM4BatteryAutonomyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatteryAutonomyTime.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatteryAutonomyTime.setUnits("min")
_ImPM4BatteryTimeOnBattery_Type = NonNegativeInteger
_ImPM4BatteryTimeOnBattery_Object = MibScalar
imPM4BatteryTimeOnBattery = _ImPM4BatteryTimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 6, 6),
    _ImPM4BatteryTimeOnBattery_Type()
)
imPM4BatteryTimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatteryTimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatteryTimeOnBattery.setUnits("min")
_ImPM4BatLeg1_ObjectIdentity = ObjectIdentity
imPM4BatLeg1 = _ImPM4BatLeg1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7)
)


class _ImPM4BatLeg1Manufacturer_Type(DisplayString):
    """Custom type imPM4BatLeg1Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM4BatLeg1Manufacturer_Type.__name__ = "DisplayString"
_ImPM4BatLeg1Manufacturer_Object = MibScalar
imPM4BatLeg1Manufacturer = _ImPM4BatLeg1Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 1),
    _ImPM4BatLeg1Manufacturer_Type()
)
imPM4BatLeg1Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Manufacturer.setStatus("current")


class _ImPM4BatLeg1Type_Type(DisplayString):
    """Custom type imPM4BatLeg1Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg1Type_Type.__name__ = "DisplayString"
_ImPM4BatLeg1Type_Object = MibScalar
imPM4BatLeg1Type = _ImPM4BatLeg1Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 2),
    _ImPM4BatLeg1Type_Type()
)
imPM4BatLeg1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Type.setStatus("current")


class _ImPM4BatLeg1serNumb_Type(DisplayString):
    """Custom type imPM4BatLeg1serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg1serNumb_Type.__name__ = "DisplayString"
_ImPM4BatLeg1serNumb_Object = MibScalar
imPM4BatLeg1serNumb = _ImPM4BatLeg1serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 3),
    _ImPM4BatLeg1serNumb_Type()
)
imPM4BatLeg1serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1serNumb.setStatus("current")


class _ImPM4BatLeg1nextServiceDate_Type(DisplayString):
    """Custom type imPM4BatLeg1nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg1nextServiceDate_Type.__name__ = "DisplayString"
_ImPM4BatLeg1nextServiceDate_Object = MibScalar
imPM4BatLeg1nextServiceDate = _ImPM4BatLeg1nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 4),
    _ImPM4BatLeg1nextServiceDate_Type()
)
imPM4BatLeg1nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1nextServiceDate.setStatus("current")


class _ImPM4BatLeg1InstallationDate_Type(DisplayString):
    """Custom type imPM4BatLeg1InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg1InstallationDate_Type.__name__ = "DisplayString"
_ImPM4BatLeg1InstallationDate_Object = MibScalar
imPM4BatLeg1InstallationDate = _ImPM4BatLeg1InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 5),
    _ImPM4BatLeg1InstallationDate_Type()
)
imPM4BatLeg1InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1InstallationDate.setStatus("current")
_ImPM4BatLeg1NominalVoltage_Type = Integer32
_ImPM4BatLeg1NominalVoltage_Object = MibScalar
imPM4BatLeg1NominalVoltage = _ImPM4BatLeg1NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 6),
    _ImPM4BatLeg1NominalVoltage_Type()
)
imPM4BatLeg1NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1NominalVoltage.setUnits("0.1 V")
_ImPM4BatLeg1NominalCapacity_Type = NonNegativeInteger
_ImPM4BatLeg1NominalCapacity_Object = MibScalar
imPM4BatLeg1NominalCapacity = _ImPM4BatLeg1NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 7),
    _ImPM4BatLeg1NominalCapacity_Type()
)
imPM4BatLeg1NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1NominalCapacity.setUnits("Ah")
_ImPM4BatLeg1Lifetime_Type = NonNegativeInteger
_ImPM4BatLeg1Lifetime_Object = MibScalar
imPM4BatLeg1Lifetime = _ImPM4BatLeg1Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 8),
    _ImPM4BatLeg1Lifetime_Type()
)
imPM4BatLeg1Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1Lifetime.setUnits("years")
_ImPM4BatLeg1Voltage_Type = Integer32
_ImPM4BatLeg1Voltage_Object = MibScalar
imPM4BatLeg1Voltage = _ImPM4BatLeg1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 9),
    _ImPM4BatLeg1Voltage_Type()
)
imPM4BatLeg1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1Voltage.setUnits("0.1 V")
_ImPM4BatLeg1Current_Type = Integer32
_ImPM4BatLeg1Current_Object = MibScalar
imPM4BatLeg1Current = _ImPM4BatLeg1Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 10),
    _ImPM4BatLeg1Current_Type()
)
imPM4BatLeg1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1Current.setUnits("0.1 A")
_ImPM4BatLeg1Temperature_Type = Integer32
_ImPM4BatLeg1Temperature_Object = MibScalar
imPM4BatLeg1Temperature = _ImPM4BatLeg1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 11),
    _ImPM4BatLeg1Temperature_Type()
)
imPM4BatLeg1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1Temperature.setUnits("degrees Centigrade")
_ImPM4BatLeg1ChargeState_Type = NonNegativeInteger
_ImPM4BatLeg1ChargeState_Object = MibScalar
imPM4BatLeg1ChargeState = _ImPM4BatLeg1ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 12),
    _ImPM4BatLeg1ChargeState_Type()
)
imPM4BatLeg1ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1ChargeState.setUnits("%")
_ImPM4BatLeg1RestCapacity_Type = NonNegativeInteger
_ImPM4BatLeg1RestCapacity_Object = MibScalar
imPM4BatLeg1RestCapacity = _ImPM4BatLeg1RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 13),
    _ImPM4BatLeg1RestCapacity_Type()
)
imPM4BatLeg1RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1RestCapacity.setUnits("Ah")
_ImPM4BatLeg1Autonomytime_Type = NonNegativeInteger
_ImPM4BatLeg1Autonomytime_Object = MibScalar
imPM4BatLeg1Autonomytime = _ImPM4BatLeg1Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 14),
    _ImPM4BatLeg1Autonomytime_Type()
)
imPM4BatLeg1Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1Autonomytime.setUnits("min")
_ImPM4BatLeg1TimeOnBattery_Type = NonNegativeInteger
_ImPM4BatLeg1TimeOnBattery_Object = MibScalar
imPM4BatLeg1TimeOnBattery = _ImPM4BatLeg1TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 15),
    _ImPM4BatLeg1TimeOnBattery_Type()
)
imPM4BatLeg1TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg1TimeOnBattery.setUnits("min")


class _ImPM4BatLeg1Fuse_Type(Integer32):
    """Custom type imPM4BatLeg1Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg1Fuse_Type.__name__ = "Integer32"
_ImPM4BatLeg1Fuse_Object = MibScalar
imPM4BatLeg1Fuse = _ImPM4BatLeg1Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 16),
    _ImPM4BatLeg1Fuse_Type()
)
imPM4BatLeg1Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Fuse.setStatus("current")


class _ImPM4BatLeg1Breaker_Type(Integer32):
    """Custom type imPM4BatLeg1Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg1Breaker_Type.__name__ = "Integer32"
_ImPM4BatLeg1Breaker_Object = MibScalar
imPM4BatLeg1Breaker = _ImPM4BatLeg1Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 17),
    _ImPM4BatLeg1Breaker_Type()
)
imPM4BatLeg1Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1Breaker.setStatus("current")


class _ImPM4BatLeg1LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM4BatLeg1LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg1LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM4BatLeg1LowVoltageDisconnect_Object = MibScalar
imPM4BatLeg1LowVoltageDisconnect = _ImPM4BatLeg1LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 7, 18),
    _ImPM4BatLeg1LowVoltageDisconnect_Type()
)
imPM4BatLeg1LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg1LowVoltageDisconnect.setStatus("current")
_ImPM4BatLeg2_ObjectIdentity = ObjectIdentity
imPM4BatLeg2 = _ImPM4BatLeg2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8)
)


class _ImPM4BatLeg2Manufacturer_Type(DisplayString):
    """Custom type imPM4BatLeg2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM4BatLeg2Manufacturer_Type.__name__ = "DisplayString"
_ImPM4BatLeg2Manufacturer_Object = MibScalar
imPM4BatLeg2Manufacturer = _ImPM4BatLeg2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 1),
    _ImPM4BatLeg2Manufacturer_Type()
)
imPM4BatLeg2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Manufacturer.setStatus("current")


class _ImPM4BatLeg2Type_Type(DisplayString):
    """Custom type imPM4BatLeg2Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg2Type_Type.__name__ = "DisplayString"
_ImPM4BatLeg2Type_Object = MibScalar
imPM4BatLeg2Type = _ImPM4BatLeg2Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 2),
    _ImPM4BatLeg2Type_Type()
)
imPM4BatLeg2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Type.setStatus("current")


class _ImPM4BatLeg2serNumb_Type(DisplayString):
    """Custom type imPM4BatLeg2serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg2serNumb_Type.__name__ = "DisplayString"
_ImPM4BatLeg2serNumb_Object = MibScalar
imPM4BatLeg2serNumb = _ImPM4BatLeg2serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 3),
    _ImPM4BatLeg2serNumb_Type()
)
imPM4BatLeg2serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2serNumb.setStatus("current")


class _ImPM4BatLeg2nextServiceDate_Type(DisplayString):
    """Custom type imPM4BatLeg2nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg2nextServiceDate_Type.__name__ = "DisplayString"
_ImPM4BatLeg2nextServiceDate_Object = MibScalar
imPM4BatLeg2nextServiceDate = _ImPM4BatLeg2nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 4),
    _ImPM4BatLeg2nextServiceDate_Type()
)
imPM4BatLeg2nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2nextServiceDate.setStatus("current")


class _ImPM4BatLeg2InstallationDate_Type(DisplayString):
    """Custom type imPM4BatLeg2InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg2InstallationDate_Type.__name__ = "DisplayString"
_ImPM4BatLeg2InstallationDate_Object = MibScalar
imPM4BatLeg2InstallationDate = _ImPM4BatLeg2InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 5),
    _ImPM4BatLeg2InstallationDate_Type()
)
imPM4BatLeg2InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2InstallationDate.setStatus("current")
_ImPM4BatLeg2NominalVoltage_Type = Integer32
_ImPM4BatLeg2NominalVoltage_Object = MibScalar
imPM4BatLeg2NominalVoltage = _ImPM4BatLeg2NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 6),
    _ImPM4BatLeg2NominalVoltage_Type()
)
imPM4BatLeg2NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2NominalVoltage.setUnits("0.1 V")
_ImPM4BatLeg2NominalCapacity_Type = NonNegativeInteger
_ImPM4BatLeg2NominalCapacity_Object = MibScalar
imPM4BatLeg2NominalCapacity = _ImPM4BatLeg2NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 7),
    _ImPM4BatLeg2NominalCapacity_Type()
)
imPM4BatLeg2NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2NominalCapacity.setUnits("Ah")
_ImPM4BatLeg2Lifetime_Type = NonNegativeInteger
_ImPM4BatLeg2Lifetime_Object = MibScalar
imPM4BatLeg2Lifetime = _ImPM4BatLeg2Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 8),
    _ImPM4BatLeg2Lifetime_Type()
)
imPM4BatLeg2Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2Lifetime.setUnits("years")
_ImPM4BatLeg2Voltage_Type = Integer32
_ImPM4BatLeg2Voltage_Object = MibScalar
imPM4BatLeg2Voltage = _ImPM4BatLeg2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 9),
    _ImPM4BatLeg2Voltage_Type()
)
imPM4BatLeg2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2Voltage.setUnits("0.1 V")
_ImPM4BatLeg2Current_Type = Integer32
_ImPM4BatLeg2Current_Object = MibScalar
imPM4BatLeg2Current = _ImPM4BatLeg2Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 10),
    _ImPM4BatLeg2Current_Type()
)
imPM4BatLeg2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2Current.setUnits("0.1 A")
_ImPM4BatLeg2Temperature_Type = Integer32
_ImPM4BatLeg2Temperature_Object = MibScalar
imPM4BatLeg2Temperature = _ImPM4BatLeg2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 11),
    _ImPM4BatLeg2Temperature_Type()
)
imPM4BatLeg2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2Temperature.setUnits("degrees Centigrade")
_ImPM4BatLeg2ChargeState_Type = NonNegativeInteger
_ImPM4BatLeg2ChargeState_Object = MibScalar
imPM4BatLeg2ChargeState = _ImPM4BatLeg2ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 12),
    _ImPM4BatLeg2ChargeState_Type()
)
imPM4BatLeg2ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2ChargeState.setUnits("%")
_ImPM4BatLeg2RestCapacity_Type = NonNegativeInteger
_ImPM4BatLeg2RestCapacity_Object = MibScalar
imPM4BatLeg2RestCapacity = _ImPM4BatLeg2RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 13),
    _ImPM4BatLeg2RestCapacity_Type()
)
imPM4BatLeg2RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2RestCapacity.setUnits("Ah")
_ImPM4BatLeg2Autonomytime_Type = NonNegativeInteger
_ImPM4BatLeg2Autonomytime_Object = MibScalar
imPM4BatLeg2Autonomytime = _ImPM4BatLeg2Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 14),
    _ImPM4BatLeg2Autonomytime_Type()
)
imPM4BatLeg2Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2Autonomytime.setUnits("min")
_ImPM4BatLeg2TimeOnBattery_Type = NonNegativeInteger
_ImPM4BatLeg2TimeOnBattery_Object = MibScalar
imPM4BatLeg2TimeOnBattery = _ImPM4BatLeg2TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 15),
    _ImPM4BatLeg2TimeOnBattery_Type()
)
imPM4BatLeg2TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg2TimeOnBattery.setUnits("min")


class _ImPM4BatLeg2Fuse_Type(Integer32):
    """Custom type imPM4BatLeg2Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg2Fuse_Type.__name__ = "Integer32"
_ImPM4BatLeg2Fuse_Object = MibScalar
imPM4BatLeg2Fuse = _ImPM4BatLeg2Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 16),
    _ImPM4BatLeg2Fuse_Type()
)
imPM4BatLeg2Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Fuse.setStatus("current")


class _ImPM4BatLeg2Breaker_Type(Integer32):
    """Custom type imPM4BatLeg2Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg2Breaker_Type.__name__ = "Integer32"
_ImPM4BatLeg2Breaker_Object = MibScalar
imPM4BatLeg2Breaker = _ImPM4BatLeg2Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 17),
    _ImPM4BatLeg2Breaker_Type()
)
imPM4BatLeg2Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2Breaker.setStatus("current")


class _ImPM4BatLeg2LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM4BatLeg2LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg2LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM4BatLeg2LowVoltageDisconnect_Object = MibScalar
imPM4BatLeg2LowVoltageDisconnect = _ImPM4BatLeg2LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 8, 18),
    _ImPM4BatLeg2LowVoltageDisconnect_Type()
)
imPM4BatLeg2LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg2LowVoltageDisconnect.setStatus("current")
_ImPM4BatLeg3_ObjectIdentity = ObjectIdentity
imPM4BatLeg3 = _ImPM4BatLeg3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9)
)


class _ImPM4BatLeg3Manufacturer_Type(DisplayString):
    """Custom type imPM4BatLeg3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM4BatLeg3Manufacturer_Type.__name__ = "DisplayString"
_ImPM4BatLeg3Manufacturer_Object = MibScalar
imPM4BatLeg3Manufacturer = _ImPM4BatLeg3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 1),
    _ImPM4BatLeg3Manufacturer_Type()
)
imPM4BatLeg3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Manufacturer.setStatus("current")


class _ImPM4BatLeg3Type_Type(DisplayString):
    """Custom type imPM4BatLeg3Type based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg3Type_Type.__name__ = "DisplayString"
_ImPM4BatLeg3Type_Object = MibScalar
imPM4BatLeg3Type = _ImPM4BatLeg3Type_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 2),
    _ImPM4BatLeg3Type_Type()
)
imPM4BatLeg3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Type.setStatus("current")


class _ImPM4BatLeg3serNumb_Type(DisplayString):
    """Custom type imPM4BatLeg3serNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg3serNumb_Type.__name__ = "DisplayString"
_ImPM4BatLeg3serNumb_Object = MibScalar
imPM4BatLeg3serNumb = _ImPM4BatLeg3serNumb_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 3),
    _ImPM4BatLeg3serNumb_Type()
)
imPM4BatLeg3serNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3serNumb.setStatus("current")


class _ImPM4BatLeg3nextServiceDate_Type(DisplayString):
    """Custom type imPM4BatLeg3nextServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg3nextServiceDate_Type.__name__ = "DisplayString"
_ImPM4BatLeg3nextServiceDate_Object = MibScalar
imPM4BatLeg3nextServiceDate = _ImPM4BatLeg3nextServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 4),
    _ImPM4BatLeg3nextServiceDate_Type()
)
imPM4BatLeg3nextServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3nextServiceDate.setStatus("current")


class _ImPM4BatLeg3InstallationDate_Type(DisplayString):
    """Custom type imPM4BatLeg3InstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ImPM4BatLeg3InstallationDate_Type.__name__ = "DisplayString"
_ImPM4BatLeg3InstallationDate_Object = MibScalar
imPM4BatLeg3InstallationDate = _ImPM4BatLeg3InstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 5),
    _ImPM4BatLeg3InstallationDate_Type()
)
imPM4BatLeg3InstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3InstallationDate.setStatus("current")
_ImPM4BatLeg3NominalVoltage_Type = Integer32
_ImPM4BatLeg3NominalVoltage_Object = MibScalar
imPM4BatLeg3NominalVoltage = _ImPM4BatLeg3NominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 6),
    _ImPM4BatLeg3NominalVoltage_Type()
)
imPM4BatLeg3NominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3NominalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3NominalVoltage.setUnits("0.1 V")
_ImPM4BatLeg3NominalCapacity_Type = NonNegativeInteger
_ImPM4BatLeg3NominalCapacity_Object = MibScalar
imPM4BatLeg3NominalCapacity = _ImPM4BatLeg3NominalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 7),
    _ImPM4BatLeg3NominalCapacity_Type()
)
imPM4BatLeg3NominalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3NominalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3NominalCapacity.setUnits("Ah")
_ImPM4BatLeg3Lifetime_Type = NonNegativeInteger
_ImPM4BatLeg3Lifetime_Object = MibScalar
imPM4BatLeg3Lifetime = _ImPM4BatLeg3Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 8),
    _ImPM4BatLeg3Lifetime_Type()
)
imPM4BatLeg3Lifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Lifetime.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3Lifetime.setUnits("years")
_ImPM4BatLeg3Voltage_Type = Integer32
_ImPM4BatLeg3Voltage_Object = MibScalar
imPM4BatLeg3Voltage = _ImPM4BatLeg3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 9),
    _ImPM4BatLeg3Voltage_Type()
)
imPM4BatLeg3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Voltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3Voltage.setUnits("0.1 V")
_ImPM4BatLeg3Current_Type = Integer32
_ImPM4BatLeg3Current_Object = MibScalar
imPM4BatLeg3Current = _ImPM4BatLeg3Current_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 10),
    _ImPM4BatLeg3Current_Type()
)
imPM4BatLeg3Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Current.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3Current.setUnits("0.1 A")
_ImPM4BatLeg3Temperature_Type = Integer32
_ImPM4BatLeg3Temperature_Object = MibScalar
imPM4BatLeg3Temperature = _ImPM4BatLeg3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 11),
    _ImPM4BatLeg3Temperature_Type()
)
imPM4BatLeg3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Temperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3Temperature.setUnits("degrees Centigrade")
_ImPM4BatLeg3ChargeState_Type = NonNegativeInteger
_ImPM4BatLeg3ChargeState_Object = MibScalar
imPM4BatLeg3ChargeState = _ImPM4BatLeg3ChargeState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 12),
    _ImPM4BatLeg3ChargeState_Type()
)
imPM4BatLeg3ChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3ChargeState.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3ChargeState.setUnits("%")
_ImPM4BatLeg3RestCapacity_Type = NonNegativeInteger
_ImPM4BatLeg3RestCapacity_Object = MibScalar
imPM4BatLeg3RestCapacity = _ImPM4BatLeg3RestCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 13),
    _ImPM4BatLeg3RestCapacity_Type()
)
imPM4BatLeg3RestCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3RestCapacity.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3RestCapacity.setUnits("Ah")
_ImPM4BatLeg3Autonomytime_Type = NonNegativeInteger
_ImPM4BatLeg3Autonomytime_Object = MibScalar
imPM4BatLeg3Autonomytime = _ImPM4BatLeg3Autonomytime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 14),
    _ImPM4BatLeg3Autonomytime_Type()
)
imPM4BatLeg3Autonomytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Autonomytime.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3Autonomytime.setUnits("min")
_ImPM4BatLeg3TimeOnBattery_Type = NonNegativeInteger
_ImPM4BatLeg3TimeOnBattery_Object = MibScalar
imPM4BatLeg3TimeOnBattery = _ImPM4BatLeg3TimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 15),
    _ImPM4BatLeg3TimeOnBattery_Type()
)
imPM4BatLeg3TimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3TimeOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    imPM4BatLeg3TimeOnBattery.setUnits("min")


class _ImPM4BatLeg3Fuse_Type(Integer32):
    """Custom type imPM4BatLeg3Fuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg3Fuse_Type.__name__ = "Integer32"
_ImPM4BatLeg3Fuse_Object = MibScalar
imPM4BatLeg3Fuse = _ImPM4BatLeg3Fuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 16),
    _ImPM4BatLeg3Fuse_Type()
)
imPM4BatLeg3Fuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Fuse.setStatus("current")


class _ImPM4BatLeg3Breaker_Type(Integer32):
    """Custom type imPM4BatLeg3Breaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg3Breaker_Type.__name__ = "Integer32"
_ImPM4BatLeg3Breaker_Object = MibScalar
imPM4BatLeg3Breaker = _ImPM4BatLeg3Breaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 17),
    _ImPM4BatLeg3Breaker_Type()
)
imPM4BatLeg3Breaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3Breaker.setStatus("current")


class _ImPM4BatLeg3LowVoltageDisconnect_Type(Integer32):
    """Custom type imPM4BatLeg3LowVoltageDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4BatLeg3LowVoltageDisconnect_Type.__name__ = "Integer32"
_ImPM4BatLeg3LowVoltageDisconnect_Object = MibScalar
imPM4BatLeg3LowVoltageDisconnect = _ImPM4BatLeg3LowVoltageDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 9, 18),
    _ImPM4BatLeg3LowVoltageDisconnect_Type()
)
imPM4BatLeg3LowVoltageDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4BatLeg3LowVoltageDisconnect.setStatus("current")
_ImPM4Distrib_ObjectIdentity = ObjectIdentity
imPM4Distrib = _ImPM4Distrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 10)
)
_ImPm4Distrib_Type = Integer32
_ImPm4Distrib_Object = MibScalar
imPm4Distrib = _ImPm4Distrib_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 10, 1),
    _ImPm4Distrib_Type()
)
imPm4Distrib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPm4Distrib.setStatus("current")
if mibBuilder.loadTexts:
    imPm4Distrib.setUnits("degrees Centigrade")
_ImPM4DistTable_Object = MibTable
imPM4DistTable = _ImPM4DistTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 10, 2)
)
if mibBuilder.loadTexts:
    imPM4DistTable.setStatus("current")
_ImPM4DistEntry_Object = MibTableRow
imPM4DistEntry = _ImPM4DistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 10, 2, 1)
)
imPM4DistEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imPM4DistId"),
)
if mibBuilder.loadTexts:
    imPM4DistEntry.setStatus("current")
_ImPM4DistId_Type = PositiveInteger
_ImPM4DistId_Object = MibTableColumn
imPM4DistId = _ImPM4DistId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 10, 2, 1, 1),
    _ImPM4DistId_Type()
)
imPM4DistId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imPM4DistId.setStatus("current")


class _ImPM4DistFuse_Type(Integer32):
    """Custom type imPM4DistFuse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4DistFuse_Type.__name__ = "Integer32"
_ImPM4DistFuse_Object = MibTableColumn
imPM4DistFuse = _ImPM4DistFuse_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 10, 2, 1, 2),
    _ImPM4DistFuse_Type()
)
imPM4DistFuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4DistFuse.setStatus("current")


class _ImPM4DistBreaker_Type(Integer32):
    """Custom type imPM4DistBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("err", 1))
    )


_ImPM4DistBreaker_Type.__name__ = "Integer32"
_ImPM4DistBreaker_Object = MibTableColumn
imPM4DistBreaker = _ImPM4DistBreaker_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 10, 2, 1, 3),
    _ImPM4DistBreaker_Type()
)
imPM4DistBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4DistBreaker.setStatus("current")
_ImPM4Control_ObjectIdentity = ObjectIdentity
imPM4Control = _ImPM4Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11)
)
_ImPM4ContTable_Object = MibTable
imPM4ContTable = _ImPM4ContTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 1)
)
if mibBuilder.loadTexts:
    imPM4ContTable.setStatus("current")
_ImPM4ContEntry_Object = MibTableRow
imPM4ContEntry = _ImPM4ContEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 1, 1)
)
imPM4ContEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imPM4ContId"),
)
if mibBuilder.loadTexts:
    imPM4ContEntry.setStatus("current")
_ImPM4ContId_Type = PositiveInteger
_ImPM4ContId_Object = MibTableColumn
imPM4ContId = _ImPM4ContId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 1, 1, 1),
    _ImPM4ContId_Type()
)
imPM4ContId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imPM4ContId.setStatus("current")


class _ImPM4ContState_Type(Integer32):
    """Custom type imPM4ContState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("on", 0),
          ("off", 1))
    )


_ImPM4ContState_Type.__name__ = "Integer32"
_ImPM4ContState_Object = MibTableColumn
imPM4ContState = _ImPM4ContState_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 1, 1, 2),
    _ImPM4ContState_Type()
)
imPM4ContState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM4ContState.setStatus("current")


class _ImPM4ContLabel_Type(DisplayString):
    """Custom type imPM4ContLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ImPM4ContLabel_Type.__name__ = "DisplayString"
_ImPM4ContLabel_Object = MibTableColumn
imPM4ContLabel = _ImPM4ContLabel_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 1, 1, 3),
    _ImPM4ContLabel_Type()
)
imPM4ContLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4ContLabel.setStatus("current")
_ImPM4ContTimeOFF_Type = Integer32
_ImPM4ContTimeOFF_Object = MibTableColumn
imPM4ContTimeOFF = _ImPM4ContTimeOFF_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 1, 1, 4),
    _ImPM4ContTimeOFF_Type()
)
imPM4ContTimeOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM4ContTimeOFF.setStatus("current")
if mibBuilder.loadTexts:
    imPM4ContTimeOFF.setUnits("min")


class _ImPM4ContAuto_Type(Integer32):
    """Custom type imPM4ContAuto based on Integer32"""
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


_ImPM4ContAuto_Type.__name__ = "Integer32"
_ImPM4ContAuto_Object = MibTableColumn
imPM4ContAuto = _ImPM4ContAuto_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 1, 1, 5),
    _ImPM4ContAuto_Type()
)
imPM4ContAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM4ContAuto.setStatus("current")


class _ImPM4ContTestCAPcommand_Type(Integer32):
    """Custom type imPM4ContTestCAPcommand based on Integer32"""
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


_ImPM4ContTestCAPcommand_Type.__name__ = "Integer32"
_ImPM4ContTestCAPcommand_Object = MibScalar
imPM4ContTestCAPcommand = _ImPM4ContTestCAPcommand_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 2),
    _ImPM4ContTestCAPcommand_Type()
)
imPM4ContTestCAPcommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imPM4ContTestCAPcommand.setStatus("current")
_ImPM4ContTestCAPvoltage_Type = Integer32
_ImPM4ContTestCAPvoltage_Object = MibScalar
imPM4ContTestCAPvoltage = _ImPM4ContTestCAPvoltage_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 3),
    _ImPM4ContTestCAPvoltage_Type()
)
imPM4ContTestCAPvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4ContTestCAPvoltage.setStatus("current")
if mibBuilder.loadTexts:
    imPM4ContTestCAPvoltage.setUnits("0.1 V")
_ImPM4ContTestCAPcurrent_Type = Integer32
_ImPM4ContTestCAPcurrent_Object = MibScalar
imPM4ContTestCAPcurrent = _ImPM4ContTestCAPcurrent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 4),
    _ImPM4ContTestCAPcurrent_Type()
)
imPM4ContTestCAPcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4ContTestCAPcurrent.setStatus("current")
if mibBuilder.loadTexts:
    imPM4ContTestCAPcurrent.setUnits("0.1 A")
_ImPM4ContTestCAPtemperature_Type = Integer32
_ImPM4ContTestCAPtemperature_Object = MibScalar
imPM4ContTestCAPtemperature = _ImPM4ContTestCAPtemperature_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 5),
    _ImPM4ContTestCAPtemperature_Type()
)
imPM4ContTestCAPtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4ContTestCAPtemperature.setStatus("current")
if mibBuilder.loadTexts:
    imPM4ContTestCAPtemperature.setUnits("degrees Centigrade")
_ImPM4ContTestCAPduration_Type = Integer32
_ImPM4ContTestCAPduration_Object = MibScalar
imPM4ContTestCAPduration = _ImPM4ContTestCAPduration_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 6),
    _ImPM4ContTestCAPduration_Type()
)
imPM4ContTestCAPduration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4ContTestCAPduration.setStatus("current")
if mibBuilder.loadTexts:
    imPM4ContTestCAPduration.setUnits("min")
_ImPM4ContTestCAPstatus_Type = Integer32
_ImPM4ContTestCAPstatus_Object = MibScalar
imPM4ContTestCAPstatus = _ImPM4ContTestCAPstatus_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 2, 4, 11, 7),
    _ImPM4ContTestCAPstatus_Type()
)
imPM4ContTestCAPstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imPM4ContTestCAPstatus.setStatus("current")
_Imco3Alarm_ObjectIdentity = ObjectIdentity
imco3Alarm = _Imco3Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 3)
)
_Imco3AlarmsPresent_Type = Gauge32
_Imco3AlarmsPresent_Object = MibScalar
imco3AlarmsPresent = _Imco3AlarmsPresent_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 3, 1),
    _Imco3AlarmsPresent_Type()
)
imco3AlarmsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3AlarmsPresent.setStatus("current")
_Imco3AlarmTable_Object = MibTable
imco3AlarmTable = _Imco3AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 3, 2)
)
if mibBuilder.loadTexts:
    imco3AlarmTable.setStatus("current")
_Imco3AlarmEntry_Object = MibTableRow
imco3AlarmEntry = _Imco3AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 3, 2, 1)
)
imco3AlarmEntry.setIndexNames(
    (0, "IMCO-BIG-MIB", "imco3AlarmId"),
)
if mibBuilder.loadTexts:
    imco3AlarmEntry.setStatus("current")
_Imco3AlarmId_Type = PositiveInteger
_Imco3AlarmId_Object = MibTableColumn
imco3AlarmId = _Imco3AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 3, 2, 1, 1),
    _Imco3AlarmId_Type()
)
imco3AlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imco3AlarmId.setStatus("current")


class _Imco3AlarmDescr_Type(Integer32):
    """Custom type imco3AlarmDescr based on Integer32"""
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
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316)
        )
    )
    namedValues = NamedValues(
        *(("aCommunicationLost", 1),
          ("aLowBattery", 2),
          ("aOnBattery", 3),
          ("aActionAlarm4", 4),
          ("aActionAlarm5", 5),
          ("aActionAlarm6", 6),
          ("aActionAlarm7", 7),
          ("aActionAlarm8", 8),
          ("aTimeforSystemService", 9),
          ("aGeneralSurgeArresterActivated", 10),
          ("aGeneralDoor1Opened", 11),
          ("aGeneralDoor2Opened", 12),
          ("aGeneralFanalarm", 13),
          ("aGeneralOvertemperature", 14),
          ("aGeneralUndertemperature", 15),
          ("aGeneralUser1Alarm", 16),
          ("aGeneralUser2Alarm", 17),
          ("aGeneralUser3Alarm", 18),
          ("aGeneralUser4Alarm", 19),
          ("aTimeforPowerSupply1Service", 20),
          ("aPowerSupply1InputOvervoltage", 21),
          ("aPowerSupply1InputUndervoltage", 22),
          ("aPowerSupply1InputOvercurrent", 23),
          ("aPowerSupply1InputOverload", 24),
          ("aPowerSupply1OutputOvervoltage", 25),
          ("aPowerSupply1OutputUndervoltage", 26),
          ("aPowerSupply1OutputOvercurrent", 27),
          ("aPowerSupply1OutputOverload", 28),
          ("aPowerSupply1Overtemperature", 29),
          ("aPowerSupply1Undertemperature", 30),
          ("aPowerSupply1Converter1notRunning", 31),
          ("aPowerSupply1Converter2notRunning", 32),
          ("aPowerSupply1Converter3notRunning", 33),
          ("aPowerSupply1Converter4notRunning", 34),
          ("aPowerSupply1Converter5notRunning", 35),
          ("aPowerSupply1Converter6notRunning", 36),
          ("aPowerSupply1Converter7notRunning", 37),
          ("aPowerSupply1Converter8notRunning", 38),
          ("aPowerSupply1InputFuseOff", 39),
          ("aPowerSupply1InputFuse1Off", 40),
          ("aPowerSupply1InputFuse2Off", 41),
          ("aPowerSupply1InputFuse3Off", 42),
          ("aPowerSupply1InputBreakerOff", 43),
          ("aPowerSupply1InputBreaker1Off", 44),
          ("aPowerSupply1InputBreaker2Off", 45),
          ("aPowerSupply1InputBreaker3Off", 46),
          ("aPowerSupply1InputSurgeArrester", 47),
          ("aPowerSupply1OutputFuseOff", 48),
          ("aPowerSupply1OutputFuse1Off", 49),
          ("aPowerSupply1OutputFuse2Off", 50),
          ("aPowerSupply1OutputBreakerOff", 51),
          ("aPowerSupply1OutputBreaker1Off", 52),
          ("aPowerSupply1OutputBreaker2Off", 53),
          ("aPowerSupply1FanMalfunction", 54),
          ("aPowerSupply1OutputOutOfPhase", 55),
          ("aPowerSupply1UserAlarm1", 56),
          ("aPowerSupply1UserAlarm2", 57),
          ("aTimeOrPowerSupply2Service", 58),
          ("aPowerSupply2InputOvervoltage", 59),
          ("aPowerSupply2InputUndervoltage", 60),
          ("aPowerSupply2InputOvercurrent", 61),
          ("aPowerSupply2InputOverload", 62),
          ("aPowerSupply2OutputOvervoltage", 63),
          ("aPowerSupply2OutputUndervoltage", 64),
          ("aPowerSupply2OutputOvercurrent", 65),
          ("aPowerSupply2OutputOverload", 66),
          ("aPowerSupply2Overtemperature", 67),
          ("aPowerSupply2Undertemperature", 68),
          ("aPowerSupply2Converter1NotRunning", 69),
          ("aPowerSupply2Converter2NotRunning", 70),
          ("aPowerSupply2Converter3NotRunning", 71),
          ("aPowerSupply2Converter4NotRunning", 72),
          ("aPowerSupply2Converter5NotRunning", 73),
          ("aPowerSupply2Converter6NotRunning", 74),
          ("aPowerSupply2Converter7NotRunning", 75),
          ("aPowerSupply2Converter8NotRunning", 76),
          ("aPowerSupply2InputFuseOff", 77),
          ("aPowerSupply2InputFuse1Off", 78),
          ("aPowerSupply2InputFuse2Off", 79),
          ("aPowerSupply2InputFuse3Off", 80),
          ("aPowerSupply2InputBreakerOff", 81),
          ("aPowerSupply2InputBreaker1Off", 82),
          ("aPowerSupply2InputBreaker2Off", 83),
          ("aPowerSupply2InputBreaker3Off", 84),
          ("aPowerSupply2InputSurgeArrester", 85),
          ("aPowerSupply2OutputFuseOff", 86),
          ("aPowerSupply2OutputFuse1Off", 87),
          ("aPowerSupply2OutputFuse2Off", 88),
          ("aPowerSupply2OutputBreakerOff", 89),
          ("aPowerSupply2OutputBreaker1Off", 90),
          ("aPowerSupply2OutputBreaker2Off", 91),
          ("aPowerSupply2FanMalfunction", 92),
          ("aPowerSupply2OutputOutOfPhase", 93),
          ("aPowerSupply2UserAlarm1", 94),
          ("aPowerSupply2UserAlarm2", 95),
          ("aTimeForPowerSupply3Service", 96),
          ("aPowerSupply3InputOvervoltage", 97),
          ("aPowerSupply3InputUndervoltage", 98),
          ("aPowerSupply3InputOvercurrent", 99),
          ("aPowerSupply3InputOverload", 100),
          ("aPowerSupply3OutputOvervoltage", 101),
          ("aPowerSupply3OutputUndervoltage", 102),
          ("aPowerSupply3OutputOvercurrent", 103),
          ("aPowerSupply3OutputOverload", 104),
          ("aPowerSupply3Overtemperature", 105),
          ("aPowerSupply3Undertemperature", 106),
          ("aPowerSupply3Converter1notRunning", 107),
          ("aPowerSupply3Converter2notRunning", 108),
          ("aPowerSupply3Converter3notRunning", 109),
          ("aPowerSupply3Converter4notRunning", 110),
          ("aPowerSupply3Converter5notRunning", 111),
          ("aPowerSupply3Converter6notRunning", 112),
          ("aPowerSupply3Converter7notRunning", 113),
          ("aPowerSupply3Converter8notRunning", 114),
          ("aPowerSupply3InputFuseOff", 115),
          ("aPowerSupply3InputFuse1Off", 116),
          ("aPowerSupply3InputFuse2Off", 117),
          ("aPowerSupply3InputFuse3Off", 118),
          ("aPowerSupply3InputBreakerOff", 119),
          ("aPowerSupply3InputBreaker1Off", 120),
          ("aPowerSupply3InputBreaker2Off", 121),
          ("aPowerSupply3InputBreaker3Off", 122),
          ("aPowerSupply3InputSurgeArrester", 123),
          ("aPowerSupply3OutputFuseOff", 124),
          ("aPowerSupply3OutputFuse1Off", 125),
          ("aPowerSupply3OutputFuse2Off", 126),
          ("aPowerSupply3OutputBreakerOff", 127),
          ("aPowerSupply3OutputBreaker1Off", 128),
          ("aPowerSupply3OutputBreaker2Off", 129),
          ("aPowerSupply3FanMalfunction", 130),
          ("aPowerSupply3OutputOutOfPhase", 131),
          ("aPowerSupply3UserAlarm1", 132),
          ("aPowerSupply3UserAlarm2", 133),
          ("aBatteryOvervoltage", 134),
          ("aBatteryUndervoltage", 135),
          ("aBatteryOvercurrent", 136),
          ("aRunningOnBattery", 137),
          ("aBatteryLow", 138),
          ("aTimeForBatteryLeg1Service", 139),
          ("aBatteryLeg1LifetimeExpired", 140),
          ("aBatteryLeg1Overvoltage", 141),
          ("aBatteryLeg1Undervoltage", 142),
          ("aBatteryLeg1Overcurrent", 143),
          ("aBatteryLeg1Overtemperature", 144),
          ("aBatteryLeg1Undertemperature", 145),
          ("aRunningOnBatteryLeg1", 146),
          ("aBatteryLeg1Low", 147),
          ("aBatteryLeg1Critical", 148),
          ("aBatteryLeg1FuseOff", 149),
          ("aBatteryLeg1BreakerOff", 150),
          ("aBatteryLeg1LVDOff", 151),
          ("aBatteryLeg1UserAlarm1", 152),
          ("aBatteryLeg1UserAlarm2", 153),
          ("aTimeForBatteryLeg2Service", 154),
          ("aBatteryLeg2LifetimeExpired", 155),
          ("aBatteryLeg2Overvoltage", 156),
          ("aBatteryLeg2Undervoltage", 157),
          ("aBatteryLeg2Overcurrent", 158),
          ("aBatteryLeg2Overtemperature", 159),
          ("aBatteryLeg2Undertemperature", 160),
          ("aRunningOnBatteryLeg2", 161),
          ("aBatteryLeg2Low", 162),
          ("aBatteryLeg2Critical", 163),
          ("aBatteryLeg2FuseOff", 164),
          ("aBatteryLeg2BreakerOff", 165),
          ("aBatteryLeg2LVDOff", 166),
          ("aBatteryLeg2UserAlarm1", 167),
          ("aBatteryLeg2UserAlarm2", 168),
          ("aTimeForBatteryLeg3Service", 169),
          ("aBatteryLeg3LifetimeExpired", 170),
          ("aBatteryLeg3Overvoltage", 171),
          ("aBatteryLeg3Undervoltage", 172),
          ("aBatteryLeg3Overcurrent", 173),
          ("aBatteryLeg3Overtemperature", 174),
          ("aBatteryLeg3Undertemperature", 175),
          ("aRunningOnBatteryLeg3", 176),
          ("aBatteryLeg3Low", 177),
          ("aBatteryLeg3Critical", 178),
          ("aBatteryLeg3FuseOff", 179),
          ("aBatteryLeg3BreakerOff", 180),
          ("aBatteryLeg3LVDOff", 181),
          ("aBatteryLeg3UserAlarm1", 182),
          ("aBatteryLeg3UserAlarm2", 183),
          ("aDistributionFuse1Off", 184),
          ("aDistributionFuse2Off", 185),
          ("aDistributionFuse3Off", 186),
          ("aDistributionFuse4Off", 187),
          ("aDistributionFuse5Off", 188),
          ("aDistributionFuse6Off", 189),
          ("aDistributionFuse7Off", 190),
          ("aDistributionFuse8Off", 191),
          ("aDistributionFuse9Off", 192),
          ("aDistributionFuse10Off", 193),
          ("aDistributionFuse11Off", 194),
          ("aDistributionFuse12Off", 195),
          ("aDistributionFuse13Off", 196),
          ("aDistributionFuse14Off", 197),
          ("aDistributionFuse15Off", 198),
          ("aDistributionFuse16Off", 199),
          ("aDistributionFuse17Off", 200),
          ("aDistributionFuse18Off", 201),
          ("aDistributionFuse19Off", 202),
          ("aDistributionFuse20Off", 203),
          ("aDistributionFuse21Off", 204),
          ("aDistributionFuse22Off", 205),
          ("aDistributionFuse23Off", 206),
          ("aDistributionFuse24Off", 207),
          ("aDistributionFuse25Off", 208),
          ("aDistributionFuse26Off", 209),
          ("aDistributionFuse27Off", 210),
          ("aDistributionFuse28Off", 211),
          ("aDistributionFuse29Off", 212),
          ("aDistributionFuse30Off", 213),
          ("aDistributionFuse31Off", 214),
          ("aDistributionFuse32Off", 215),
          ("aDistributionBreaker1Off", 216),
          ("aDistributionBreaker2Off", 217),
          ("aDistributionBreaker3Off", 218),
          ("aDistributionBreaker4Off", 219),
          ("aDistributionBreaker5Off", 220),
          ("aDistributionBreaker6Off", 221),
          ("aDistributionBreaker7Off", 222),
          ("aDistributionBreaker8Off", 223),
          ("aDistributionBreaker9Off", 224),
          ("aDistributionBreaker10Off", 225),
          ("aDistributionBreaker11Off", 226),
          ("aDistributionBreaker12Off", 227),
          ("aDistributionBreaker13Off", 228),
          ("aDistributionBreaker14Off", 229),
          ("aDistributionBreaker15Off", 230),
          ("aDistributionBreaker16Off", 231),
          ("aDistributionBreaker17Off", 232),
          ("aDistributionBreaker18Off", 233),
          ("aDistributionBreaker19Off", 234),
          ("aDistributionBreaker20Off", 235),
          ("aDistributionBreaker21Off", 236),
          ("aDistributionBreaker22Off", 237),
          ("aDistributionBreaker23Off", 238),
          ("aDistributionBreaker24Off", 239),
          ("aDistributionBreaker25Off", 240),
          ("aDistributionBreaker26Off", 241),
          ("aDistributionBreaker27Off", 242),
          ("aDistributionBreaker28Off", 243),
          ("aDistributionBreaker29Off", 244),
          ("aDistributionBreaker30Off", 245),
          ("aDistributionBreaker31Off", 246),
          ("aDistributionBreaker32Off", 247),
          ("aDistributionBreaker33Off", 248),
          ("aDistributionBreaker34Off", 249),
          ("aDistributionBreaker35Off", 250),
          ("aDistributionBreaker36Off", 251),
          ("aDistributionBreaker37Off", 252),
          ("aDistributionBreaker38Off", 253),
          ("aDistributionBreaker39Off", 254),
          ("aDistributionBreaker40Off", 255),
          ("aDistributionBreaker41Off", 256),
          ("aDistributionBreaker42Off", 257),
          ("aDistributionBreaker43Off", 258),
          ("aDistributionBreaker44Off", 259),
          ("aDistributionBreaker45Off", 260),
          ("aDistributionBreaker46Off", 261),
          ("aDistributionBreaker47Off", 262),
          ("aDistributionBreaker48Off", 263),
          ("aDistributionBreaker49Off", 264),
          ("aDistributionBreaker50Off", 265),
          ("aDistributionBreaker51Off", 266),
          ("aDistributionBreaker52Off", 267),
          ("aDistributionBreaker53Off", 268),
          ("aDistributionBreaker54Off", 269),
          ("aDistributionBreaker55Off", 270),
          ("aDistributionBreaker56Off", 271),
          ("aDistributionBreaker57Off", 272),
          ("aDistributionBreaker58Off", 273),
          ("aDistributionBreaker59Off", 274),
          ("aDistributionBreaker60Off", 275),
          ("aDistributionBreaker61Off", 276),
          ("aDistributionBreaker62Off", 277),
          ("aDistributionBreaker63Off", 278),
          ("aDistributionBreaker64Off", 279),
          ("aDistributionStripOvertemperature", 280),
          ("aSupply1UnitAny", 281),
          ("aSupply1UnitAll", 282),
          ("aSupply1UnitMains", 283),
          ("aSupply1UnitInputPhase1", 284),
          ("aSupply1UnitInputPhase2", 285),
          ("aSupply1UnitInputPhase3", 286),
          ("aSupply1UnitInputPhaseAll", 287),
          ("aSupply1Reserva1", 288),
          ("aSupply1Reserva2", 289),
          ("aSupply1Reserva3", 290),
          ("aSupply1Reserva4", 291),
          ("aSupply1Reserva5", 292),
          ("aSupply2UnitAny", 293),
          ("aSupply2UnitAll", 294),
          ("aSupply2UnitMains", 295),
          ("aSupply2UnitInputPhase1", 296),
          ("aSupply2UnitInputPhase2", 297),
          ("aSupply2UnitInputPhase3", 298),
          ("aSupply2UnitInputPhaseAll", 299),
          ("aSupply2Reserva1", 300),
          ("aSupply2Reserva2", 301),
          ("aSupply2Reserva3", 302),
          ("aSupply2Reserva4", 303),
          ("aSupply2Reserva5", 304),
          ("aSupply3UnitAny", 305),
          ("aSupply3UnitAll", 306),
          ("aSupply3UnitMains", 307),
          ("aSupply3UnitInputPhase1", 308),
          ("aSupply3UnitInputPhase2", 309),
          ("aSupply3UnitInputPhase3", 310),
          ("aSupply3UnitInputPhaseAll", 311),
          ("aSupply3Reserva1", 312),
          ("aSupply3Reserva2", 313),
          ("aSupply3Reserva3", 314),
          ("aSupply3Reserva4", 315),
          ("aSupply3Reserva5", 316))
    )


_Imco3AlarmDescr_Type.__name__ = "Integer32"
_Imco3AlarmDescr_Object = MibTableColumn
imco3AlarmDescr = _Imco3AlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 3, 2, 1, 2),
    _Imco3AlarmDescr_Type()
)
imco3AlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3AlarmDescr.setStatus("current")
_Imco3AlarmTime_Type = TimeStamp
_Imco3AlarmTime_Object = MibTableColumn
imco3AlarmTime = _Imco3AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 3, 2, 1, 3),
    _Imco3AlarmTime_Type()
)
imco3AlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3AlarmTime.setStatus("current")
_Imco3AlarmPMnumber_Type = Integer32
_Imco3AlarmPMnumber_Object = MibTableColumn
imco3AlarmPMnumber = _Imco3AlarmPMnumber_Object(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 11, 3, 2, 1, 4),
    _Imco3AlarmPMnumber_Type()
)
imco3AlarmPMnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imco3AlarmPMnumber.setStatus("current")
_Imco3Traps_ObjectIdentity = ObjectIdentity
imco3Traps = _Imco3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12)
)
_NpProducts_ObjectIdentity = ObjectIdentity
npProducts = _NpProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2185, 2)
)

# Managed Objects groups


# Notification objects

imco3TrapNoDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 1)
)
if mibBuilder.loadTexts:
    imco3TrapNoDevice.setStatus(
        "current"
    )

imco3TrapOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 2)
)
if mibBuilder.loadTexts:
    imco3TrapOnBattery.setStatus(
        "current"
    )

imco3TrapNewAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 3)
)
imco3TrapNewAlarm.setObjects(
      *(("IMCO-BIG-MIB", "imco3AlarmDescr"),
        ("IMCO-BIG-MIB", "imco3AlarmTime"),
        ("IMCO-BIG-MIB", "imco3AlarmPMnumber"))
)
if mibBuilder.loadTexts:
    imco3TrapNewAlarm.setStatus(
        "current"
    )

imco3TrapAlarmEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 4)
)
imco3TrapAlarmEnd.setObjects(
      *(("IMCO-BIG-MIB", "imco3AlarmDescr"),
        ("IMCO-BIG-MIB", "imco3AlarmTime"),
        ("IMCO-BIG-MIB", "imco3AlarmPMnumber"))
)
if mibBuilder.loadTexts:
    imco3TrapAlarmEnd.setStatus(
        "current"
    )

imco3TrapAlarmOut1ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 10)
)
imco3TrapAlarmOut1ON.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut1ON.setStatus(
        "current"
    )

imco3TrapAlarmOut2ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 11)
)
imco3TrapAlarmOut2ON.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut2ON.setStatus(
        "current"
    )

imco3TrapAlarmOut3ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 12)
)
imco3TrapAlarmOut3ON.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut3ON.setStatus(
        "current"
    )

imco3TrapAlarmOut4ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 13)
)
imco3TrapAlarmOut4ON.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut4ON.setStatus(
        "current"
    )

imco3TrapAlarmOut5ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 14)
)
imco3TrapAlarmOut5ON.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut5ON.setStatus(
        "current"
    )

imco3TrapAlarmOut6ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 15)
)
imco3TrapAlarmOut6ON.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut6ON.setStatus(
        "current"
    )

imco3TrapAlarmOut7ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 16)
)
imco3TrapAlarmOut7ON.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut7ON.setStatus(
        "current"
    )

imco3TrapAlarmOut8ON = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 17)
)
imco3TrapAlarmOut8ON.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut8ON.setStatus(
        "current"
    )

imco3TrapAlarmOut1OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 20)
)
imco3TrapAlarmOut1OFF.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut1OFF.setStatus(
        "current"
    )

imco3TrapAlarmOut2OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 21)
)
imco3TrapAlarmOut2OFF.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut2OFF.setStatus(
        "current"
    )

imco3TrapAlarmOut3OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 22)
)
imco3TrapAlarmOut3OFF.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut3OFF.setStatus(
        "current"
    )

imco3TrapAlarmOut4OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 23)
)
imco3TrapAlarmOut4OFF.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut4OFF.setStatus(
        "current"
    )

imco3TrapAlarmOut5OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 24)
)
imco3TrapAlarmOut5OFF.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut5OFF.setStatus(
        "current"
    )

imco3TrapAlarmOut6OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 25)
)
imco3TrapAlarmOut6OFF.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut6OFF.setStatus(
        "current"
    )

imco3TrapAlarmOut7OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 26)
)
imco3TrapAlarmOut7OFF.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut7OFF.setStatus(
        "current"
    )

imco3TrapAlarmOut8OFF = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 27)
)
imco3TrapAlarmOut8OFF.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapAlarmOut8OFF.setStatus(
        "current"
    )

imco3TrapTestCAPstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 30)
)
imco3TrapTestCAPstart.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapTestCAPstart.setStatus(
        "current"
    )

imco3TrapTestCAPstop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2185, 1, 3, 12, 31)
)
imco3TrapTestCAPstop.setObjects(
    ("IMCO-BIG-MIB", "imco3IdentPMnumber")
)
if mibBuilder.loadTexts:
    imco3TrapTestCAPstop.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IMCO-BIG-MIB",
    **{"PositiveInteger": PositiveInteger,
       "NonNegativeInteger": NonNegativeInteger,
       "netPartner": netPartner,
       "npModules": npModules,
       "imcoMIB": imcoMIB,
       "imcoObjects3": imcoObjects3,
       "imco3Ident": imco3Ident,
       "imco3IdentManufacturer": imco3IdentManufacturer,
       "imco3IdentModel": imco3IdentModel,
       "imco3IdentSwVersion": imco3IdentSwVersion,
       "imco3IdentAgentVersion": imco3IdentAgentVersion,
       "imco3IdentName": imco3IdentName,
       "imco3IdentAttachedDevices": imco3IdentAttachedDevices,
       "imco3IdentPMnumber": imco3IdentPMnumber,
       "imco3PanM": imco3PanM,
       "imPanM1": imPanM1,
       "imPM1SystemID": imPM1SystemID,
       "imPM1SystemIDManufacturer": imPM1SystemIDManufacturer,
       "imPM1SystemIDType": imPM1SystemIDType,
       "imPM1SystemIDserNumb": imPM1SystemIDserNumb,
       "imPM1SystemIDnextServiceDate": imPM1SystemIDnextServiceDate,
       "imPM1SystemIDaddress": imPM1SystemIDaddress,
       "imPM1SystemIDhwVersion": imPM1SystemIDhwVersion,
       "imPM1SystemIDswVersion": imPM1SystemIDswVersion,
       "imPM1SystemIDPMserialNumber": imPM1SystemIDPMserialNumber,
       "imPM1SystemIDbuttonName": imPM1SystemIDbuttonName,
       "imPM1SystemGEN": imPM1SystemGEN,
       "imPM1SystemGENSurgeArrester": imPM1SystemGENSurgeArrester,
       "imPM1SystemGENDoor1": imPM1SystemGENDoor1,
       "imPM1SystemGENDoor2": imPM1SystemGENDoor2,
       "imPM1SystemGENFan": imPM1SystemGENFan,
       "imPM1SystemGENuser1": imPM1SystemGENuser1,
       "imPM1SystemGENuser2": imPM1SystemGENuser2,
       "imPM1SystemGENuser3": imPM1SystemGENuser3,
       "imPM1SystemGENuser4": imPM1SystemGENuser4,
       "imPM1SystemGENtemperature": imPM1SystemGENtemperature,
       "imPM1Power1": imPM1Power1,
       "imPM1Power1Manufacturer": imPM1Power1Manufacturer,
       "imPM1Power1Type": imPM1Power1Type,
       "imPM1Power1serNumb": imPM1Power1serNumb,
       "imPM1Power1nextServiceDate": imPM1Power1nextServiceDate,
       "imPm1Power1InputVoltage": imPm1Power1InputVoltage,
       "imPm1Power1InputCurrent": imPm1Power1InputCurrent,
       "imPm1Power1InputPowerVA": imPm1Power1InputPowerVA,
       "imPm1Power1InputPowerKVA": imPm1Power1InputPowerKVA,
       "imPm1Power1InputPowerW": imPm1Power1InputPowerW,
       "imPm1Power1InputPowerKW": imPm1Power1InputPowerKW,
       "imPm1Power1InputVoltagePhase1": imPm1Power1InputVoltagePhase1,
       "imPm1Power1InputCurrentPhase1": imPm1Power1InputCurrentPhase1,
       "imPm1Power1InputPowerVAphase1": imPm1Power1InputPowerVAphase1,
       "imPm1Power1InputPowerKVAphase1": imPm1Power1InputPowerKVAphase1,
       "imPm1Power1InputVoltagePhase2": imPm1Power1InputVoltagePhase2,
       "imPm1Power1InputCurrentPhase2": imPm1Power1InputCurrentPhase2,
       "imPm1Power1InputPowerVAphase2": imPm1Power1InputPowerVAphase2,
       "imPm1Power1InputPowerKVAphase2": imPm1Power1InputPowerKVAphase2,
       "imPm1Power1InputVoltagePhase3": imPm1Power1InputVoltagePhase3,
       "imPm1Power1InputCurrentPhase3": imPm1Power1InputCurrentPhase3,
       "imPm1Power1InputPowerVAphase3": imPm1Power1InputPowerVAphase3,
       "imPm1Power1InputPowerKVAphase3": imPm1Power1InputPowerKVAphase3,
       "imPm1Power1OutputVoltage": imPm1Power1OutputVoltage,
       "imPm1Power1OutputCurrent": imPm1Power1OutputCurrent,
       "imPm1Power1OutputPowerVA": imPm1Power1OutputPowerVA,
       "imPm1Power1OutputPowerKVA": imPm1Power1OutputPowerKVA,
       "imPm1Power1OutputPowerW": imPm1Power1OutputPowerW,
       "imPm1Power1OutputPowerKW": imPm1Power1OutputPowerKW,
       "imPm1Power1OutputLoad": imPm1Power1OutputLoad,
       "imPm1Power1OutputFrequency": imPm1Power1OutputFrequency,
       "imPm1Power1Temperature": imPm1Power1Temperature,
       "imPM1Power1Running1": imPM1Power1Running1,
       "imPM1Power1Running2": imPM1Power1Running2,
       "imPM1Power1Running3": imPM1Power1Running3,
       "imPM1Power1Running4": imPM1Power1Running4,
       "imPM1Power1Running5": imPM1Power1Running5,
       "imPM1Power1Running6": imPM1Power1Running6,
       "imPM1Power1Running7": imPM1Power1Running7,
       "imPM1Power1Running8": imPM1Power1Running8,
       "imPM1Power1InputFuse": imPM1Power1InputFuse,
       "imPM1Power1InputFuse1": imPM1Power1InputFuse1,
       "imPM1Power1InputFuse2": imPM1Power1InputFuse2,
       "imPM1Power1InputFuse3": imPM1Power1InputFuse3,
       "imPM1Power1InputBreaker": imPM1Power1InputBreaker,
       "imPM1Power1InputBreaker1": imPM1Power1InputBreaker1,
       "imPM1Power1InputBreaker2": imPM1Power1InputBreaker2,
       "imPM1Power1InputBreaker3": imPM1Power1InputBreaker3,
       "imPM1Power1InputSurgeArrester": imPM1Power1InputSurgeArrester,
       "imPM1Power1OutputFuse": imPM1Power1OutputFuse,
       "imPM1Power1OutputFuse1": imPM1Power1OutputFuse1,
       "imPM1Power1OutputFuse2": imPM1Power1OutputFuse2,
       "imPM1Power1OutputBreaker": imPM1Power1OutputBreaker,
       "imPM1Power1OutputBreaker1": imPM1Power1OutputBreaker1,
       "imPM1Power1OutputBreaker2": imPM1Power1OutputBreaker2,
       "imPM1Power1Fan": imPM1Power1Fan,
       "imPM1Power1BatteryAvailable": imPM1Power1BatteryAvailable,
       "imPm1Power1OutputVoltagePhase1": imPm1Power1OutputVoltagePhase1,
       "imPm1Power1OutputCurrentPhase1": imPm1Power1OutputCurrentPhase1,
       "imPm1Power1OutputPowerVAphase1": imPm1Power1OutputPowerVAphase1,
       "imPm1Power1OutputPowerKVAphase1": imPm1Power1OutputPowerKVAphase1,
       "imPm1Power1OutputVoltagePhase2": imPm1Power1OutputVoltagePhase2,
       "imPm1Power1OutputCurrentPhase2": imPm1Power1OutputCurrentPhase2,
       "imPm1Power1OutputPowerVAphase2": imPm1Power1OutputPowerVAphase2,
       "imPm1Power1OutputPowerKVAphase2": imPm1Power1OutputPowerKVAphase2,
       "imPm1Power1OutputVoltagePhase3": imPm1Power1OutputVoltagePhase3,
       "imPm1Power1OutputCurrentPhase3": imPm1Power1OutputCurrentPhase3,
       "imPm1Power1OutputPowerVAphase3": imPm1Power1OutputPowerVAphase3,
       "imPm1Power1OutputPowerKVAphase3": imPm1Power1OutputPowerKVAphase3,
       "imPM1Power2": imPM1Power2,
       "imPM1Power2Manufacturer": imPM1Power2Manufacturer,
       "imPM1Power2Type": imPM1Power2Type,
       "imPM1Power2serNumb": imPM1Power2serNumb,
       "imPM1Power2nextServiceDate": imPM1Power2nextServiceDate,
       "imPm1Power2InputVoltage": imPm1Power2InputVoltage,
       "imPm1Power2InputCurrent": imPm1Power2InputCurrent,
       "imPm1Power2InputPowerVA": imPm1Power2InputPowerVA,
       "imPm1Power2InputPowerKVA": imPm1Power2InputPowerKVA,
       "imPm1Power2InputPowerW": imPm1Power2InputPowerW,
       "imPm1Power2InputPowerKW": imPm1Power2InputPowerKW,
       "imPm1Power2InputVoltagePhase1": imPm1Power2InputVoltagePhase1,
       "imPm1Power2InputCurrentPhase1": imPm1Power2InputCurrentPhase1,
       "imPm1Power2InputPowerVAphase1": imPm1Power2InputPowerVAphase1,
       "imPm1Power2InputPowerKVAphase1": imPm1Power2InputPowerKVAphase1,
       "imPm1Power2InputVoltagePhase2": imPm1Power2InputVoltagePhase2,
       "imPm1Power2InputCurrentPhase2": imPm1Power2InputCurrentPhase2,
       "imPm1Power2InputPowerVAphase2": imPm1Power2InputPowerVAphase2,
       "imPm1Power2InputPowerKVAphase2": imPm1Power2InputPowerKVAphase2,
       "imPm1Power2InputVoltagePhase3": imPm1Power2InputVoltagePhase3,
       "imPm1Power2InputCurrentPhase3": imPm1Power2InputCurrentPhase3,
       "imPm1Power2InputPowerVAphase3": imPm1Power2InputPowerVAphase3,
       "imPm1Power2InputPowerKVAphase3": imPm1Power2InputPowerKVAphase3,
       "imPm1Power2OutputVoltage": imPm1Power2OutputVoltage,
       "imPm1Power2OutputCurrent": imPm1Power2OutputCurrent,
       "imPm1Power2OutputPowerVA": imPm1Power2OutputPowerVA,
       "imPm1Power2OutputPowerKVA": imPm1Power2OutputPowerKVA,
       "imPm1Power2OutputPowerW": imPm1Power2OutputPowerW,
       "imPm1Power2OutputPowerKW": imPm1Power2OutputPowerKW,
       "imPm1Power2OutputLoad": imPm1Power2OutputLoad,
       "imPm1Power2OutputFrequency": imPm1Power2OutputFrequency,
       "imPm1Power2Temperature": imPm1Power2Temperature,
       "imPM1Power2Running1": imPM1Power2Running1,
       "imPM1Power2Running2": imPM1Power2Running2,
       "imPM1Power2Running3": imPM1Power2Running3,
       "imPM1Power2Running4": imPM1Power2Running4,
       "imPM1Power2Running5": imPM1Power2Running5,
       "imPM1Power2Running6": imPM1Power2Running6,
       "imPM1Power2Running7": imPM1Power2Running7,
       "imPM1Power2Running8": imPM1Power2Running8,
       "imPM1Power2InputFuse": imPM1Power2InputFuse,
       "imPM1Power2InputFuse1": imPM1Power2InputFuse1,
       "imPM1Power2InputFuse2": imPM1Power2InputFuse2,
       "imPM1Power2InputFuse3": imPM1Power2InputFuse3,
       "imPM1Power2InputBreaker": imPM1Power2InputBreaker,
       "imPM1Power2InputBreaker1": imPM1Power2InputBreaker1,
       "imPM1Power2InputBreaker2": imPM1Power2InputBreaker2,
       "imPM1Power2InputBreaker3": imPM1Power2InputBreaker3,
       "imPM1Power2InputSurgeArrester": imPM1Power2InputSurgeArrester,
       "imPM1Power2OutputFuse": imPM1Power2OutputFuse,
       "imPM1Power2OutputFuse1": imPM1Power2OutputFuse1,
       "imPM1Power2OutputFuse2": imPM1Power2OutputFuse2,
       "imPM1Power2OutputBreaker": imPM1Power2OutputBreaker,
       "imPM1Power2OutputBreaker1": imPM1Power2OutputBreaker1,
       "imPM1Power2OutputBreaker2": imPM1Power2OutputBreaker2,
       "imPM1Power2Fan": imPM1Power2Fan,
       "imPM1Power2BatteryAvailable": imPM1Power2BatteryAvailable,
       "imPM1Power2OutputVoltagePhase1": imPM1Power2OutputVoltagePhase1,
       "imPM1Power2OutputCurrentPhase1": imPM1Power2OutputCurrentPhase1,
       "imPM1Power2OutputPowerVAphase1": imPM1Power2OutputPowerVAphase1,
       "imPM1Power2OutputPowerKVAphase1": imPM1Power2OutputPowerKVAphase1,
       "imPM1Power2OutputVoltagePhase2": imPM1Power2OutputVoltagePhase2,
       "imPM1Power2OutputCurrentPhase2": imPM1Power2OutputCurrentPhase2,
       "imPM1Power2OutputPowerVAphase2": imPM1Power2OutputPowerVAphase2,
       "imPM1Power2OutputPowerKVAphase2": imPM1Power2OutputPowerKVAphase2,
       "imPM1Power2OutputVoltagePhase3": imPM1Power2OutputVoltagePhase3,
       "imPM1Power2OutputCurrentPhase3": imPM1Power2OutputCurrentPhase3,
       "imPM1Power2OutputPowerVAphase3": imPM1Power2OutputPowerVAphase3,
       "imPM1Power2OutputPowerKVAphase3": imPM1Power2OutputPowerKVAphase3,
       "imPM1Power3": imPM1Power3,
       "imPM1Power3Manufacturer": imPM1Power3Manufacturer,
       "imPM1Power3Type": imPM1Power3Type,
       "imPM1Power3serNumb": imPM1Power3serNumb,
       "imPM1Power3nextServiceDate": imPM1Power3nextServiceDate,
       "imPm1Power3InputVoltage": imPm1Power3InputVoltage,
       "imPm1Power3InputCurrent": imPm1Power3InputCurrent,
       "imPm1Power3InputPowerVA": imPm1Power3InputPowerVA,
       "imPm1Power3InputPowerKVA": imPm1Power3InputPowerKVA,
       "imPm1Power3InputPowerW": imPm1Power3InputPowerW,
       "imPm1Power3InputPowerKW": imPm1Power3InputPowerKW,
       "imPm1Power3InputVoltagePhase1": imPm1Power3InputVoltagePhase1,
       "imPm1Power3InputCurrentPhase1": imPm1Power3InputCurrentPhase1,
       "imPm1Power3InputPowerVAphase1": imPm1Power3InputPowerVAphase1,
       "imPm1Power3InputPowerKVAphase1": imPm1Power3InputPowerKVAphase1,
       "imPm1Power3InputVoltagePhase2": imPm1Power3InputVoltagePhase2,
       "imPm1Power3InputCurrentPhase2": imPm1Power3InputCurrentPhase2,
       "imPm1Power3InputPowerVAphase2": imPm1Power3InputPowerVAphase2,
       "imPm1Power3InputPowerKVAphase2": imPm1Power3InputPowerKVAphase2,
       "imPm1Power3InputVoltagePhase3": imPm1Power3InputVoltagePhase3,
       "imPm1Power3InputCurrentPhase3": imPm1Power3InputCurrentPhase3,
       "imPm1Power3InputPowerVAphase3": imPm1Power3InputPowerVAphase3,
       "imPm1Power3InputPowerKVAphase3": imPm1Power3InputPowerKVAphase3,
       "imPm1Power3OutputVoltage": imPm1Power3OutputVoltage,
       "imPm1Power3OutputCurrent": imPm1Power3OutputCurrent,
       "imPm1Power3OutputPowerVA": imPm1Power3OutputPowerVA,
       "imPm1Power3OutputPowerKVA": imPm1Power3OutputPowerKVA,
       "imPm1Power3OutputPowerW": imPm1Power3OutputPowerW,
       "imPm1Power3OutputPowerKW": imPm1Power3OutputPowerKW,
       "imPm1Power3OutputLoad": imPm1Power3OutputLoad,
       "imPm1Power3OutputFrequency": imPm1Power3OutputFrequency,
       "imPm1Power3Temperature": imPm1Power3Temperature,
       "imPM1Power3Running1": imPM1Power3Running1,
       "imPM1Power3Running2": imPM1Power3Running2,
       "imPM1Power3Running3": imPM1Power3Running3,
       "imPM1Power3Running4": imPM1Power3Running4,
       "imPM1Power3Running5": imPM1Power3Running5,
       "imPM1Power3Running6": imPM1Power3Running6,
       "imPM1Power3Running7": imPM1Power3Running7,
       "imPM1Power3Running8": imPM1Power3Running8,
       "imPM1Power3InputFuse": imPM1Power3InputFuse,
       "imPM1Power3InputFuse1": imPM1Power3InputFuse1,
       "imPM1Power3InputFuse2": imPM1Power3InputFuse2,
       "imPM1Power3InputFuse3": imPM1Power3InputFuse3,
       "imPM1Power3InputBreaker": imPM1Power3InputBreaker,
       "imPM1Power3InputBreaker1": imPM1Power3InputBreaker1,
       "imPM1Power3InputBreaker2": imPM1Power3InputBreaker2,
       "imPM1Power3InputBreaker3": imPM1Power3InputBreaker3,
       "imPM1Power3InputSurgeArrester": imPM1Power3InputSurgeArrester,
       "imPM1Power3OutputFuse": imPM1Power3OutputFuse,
       "imPM1Power3OutputFuse1": imPM1Power3OutputFuse1,
       "imPM1Power3OutputFuse2": imPM1Power3OutputFuse2,
       "imPM1Power3OutputBreaker": imPM1Power3OutputBreaker,
       "imPM1Power3OutputBreaker1": imPM1Power3OutputBreaker1,
       "imPM1Power3OutputBreaker2": imPM1Power3OutputBreaker2,
       "imPM1Power3Fan": imPM1Power3Fan,
       "imPM1Power3BatteryAvailable": imPM1Power3BatteryAvailable,
       "imPM1Power3OutputVoltagePhase1": imPM1Power3OutputVoltagePhase1,
       "imPM1Power3OutputCurrentPhase1": imPM1Power3OutputCurrentPhase1,
       "imPM1Power3OutputPowerVAphase1": imPM1Power3OutputPowerVAphase1,
       "imPM1Power3OutputPowerKVAphase1": imPM1Power3OutputPowerKVAphase1,
       "imPM1Power3OutputVoltagePhase2": imPM1Power3OutputVoltagePhase2,
       "imPM1Power3OutputCurrentPhase2": imPM1Power3OutputCurrentPhase2,
       "imPM1Power3OutputPowerVAphase2": imPM1Power3OutputPowerVAphase2,
       "imPM1Power3OutputPowerKVAphase2": imPM1Power3OutputPowerKVAphase2,
       "imPM1Power3OutputVoltagePhase3": imPM1Power3OutputVoltagePhase3,
       "imPM1Power3OutputCurrentPhase3": imPM1Power3OutputCurrentPhase3,
       "imPM1Power3OutputPowerVAphase3": imPM1Power3OutputPowerVAphase3,
       "imPM1Power3OutputPowerKVAphase3": imPM1Power3OutputPowerKVAphase3,
       "imPM1Battery": imPM1Battery,
       "imPm1BatteryNominalCapacity": imPm1BatteryNominalCapacity,
       "imPm1BatteryVoltage": imPm1BatteryVoltage,
       "imPm1BatteryCurrent": imPm1BatteryCurrent,
       "imPm1BatteryChargeState": imPm1BatteryChargeState,
       "imPm1BatteryAutonomyTime": imPm1BatteryAutonomyTime,
       "imPm1BatteryTimeOnBattery": imPm1BatteryTimeOnBattery,
       "imPM1BatLeg1": imPM1BatLeg1,
       "imPM1BatLeg1Manufacturer": imPM1BatLeg1Manufacturer,
       "imPM1BatLeg1Type": imPM1BatLeg1Type,
       "imPM1BatLeg1serNumb": imPM1BatLeg1serNumb,
       "imPM1BatLeg1nextServiceDate": imPM1BatLeg1nextServiceDate,
       "imPM1BatLeg1InstallationDate": imPM1BatLeg1InstallationDate,
       "imPm1BatLeg1NominalVoltage": imPm1BatLeg1NominalVoltage,
       "imPm1BatLeg1NominalCapacity": imPm1BatLeg1NominalCapacity,
       "imPm1BatLeg1Lifetime": imPm1BatLeg1Lifetime,
       "imPm1BatLeg1Voltage": imPm1BatLeg1Voltage,
       "imPm1BatLeg1Current": imPm1BatLeg1Current,
       "imPm1BatLeg1Temperature": imPm1BatLeg1Temperature,
       "imPm1BatLeg1ChargeState": imPm1BatLeg1ChargeState,
       "imPm1BatLeg1RestCapacity": imPm1BatLeg1RestCapacity,
       "imPm1BatLeg1Autonomytime": imPm1BatLeg1Autonomytime,
       "imPm1BatLeg1TimeOnBattery": imPm1BatLeg1TimeOnBattery,
       "imPM1BatLeg1Fuse": imPM1BatLeg1Fuse,
       "imPM1BatLeg1Breaker": imPM1BatLeg1Breaker,
       "imPM1BatLeg1LowVoltageDisconnect": imPM1BatLeg1LowVoltageDisconnect,
       "imPM1BatLeg2": imPM1BatLeg2,
       "imPM1BatLeg2Manufacturer": imPM1BatLeg2Manufacturer,
       "imPM1BatLeg2Type": imPM1BatLeg2Type,
       "imPM1BatLeg2serNumb": imPM1BatLeg2serNumb,
       "imPM1BatLeg2nextServiceDate": imPM1BatLeg2nextServiceDate,
       "imPM1BatLeg2InstallationDate": imPM1BatLeg2InstallationDate,
       "imPm1BatLeg2NominalVoltage": imPm1BatLeg2NominalVoltage,
       "imPm1BatLeg2NominalCapacity": imPm1BatLeg2NominalCapacity,
       "imPm1BatLeg2Lifetime": imPm1BatLeg2Lifetime,
       "imPm1BatLeg2Voltage": imPm1BatLeg2Voltage,
       "imPm1BatLeg2Current": imPm1BatLeg2Current,
       "imPm1BatLeg2Temperature": imPm1BatLeg2Temperature,
       "imPm1BatLeg2ChargeState": imPm1BatLeg2ChargeState,
       "imPm1BatLeg2RestCapacity": imPm1BatLeg2RestCapacity,
       "imPm1BatLeg2Autonomytime": imPm1BatLeg2Autonomytime,
       "imPm1BatLeg2TimeOnBattery": imPm1BatLeg2TimeOnBattery,
       "imPM1BatLeg2Fuse": imPM1BatLeg2Fuse,
       "imPM1BatLeg2Breaker": imPM1BatLeg2Breaker,
       "imPM1BatLeg2LowVoltageDisconnect": imPM1BatLeg2LowVoltageDisconnect,
       "imPM1BatLeg3": imPM1BatLeg3,
       "imPM1BatLeg3Manufacturer": imPM1BatLeg3Manufacturer,
       "imPM1BatLeg3Type": imPM1BatLeg3Type,
       "imPM1BatLeg3serNumb": imPM1BatLeg3serNumb,
       "imPM1BatLeg3nextServiceDate": imPM1BatLeg3nextServiceDate,
       "imPM1BatLeg3InstallationDate": imPM1BatLeg3InstallationDate,
       "imPm1BatLeg3NominalVoltage": imPm1BatLeg3NominalVoltage,
       "imPm1BatLeg3NominalCapacity": imPm1BatLeg3NominalCapacity,
       "imPm1BatLeg3Lifetime": imPm1BatLeg3Lifetime,
       "imPm1BatLeg3Voltage": imPm1BatLeg3Voltage,
       "imPm1BatLeg3Current": imPm1BatLeg3Current,
       "imPm1BatLeg3Temperature": imPm1BatLeg3Temperature,
       "imPm1BatLeg3ChargeState": imPm1BatLeg3ChargeState,
       "imPm1BatLeg3RestCapacity": imPm1BatLeg3RestCapacity,
       "imPm1BatLeg3Autonomytime": imPm1BatLeg3Autonomytime,
       "imPm1BatLeg3TimeOnBattery": imPm1BatLeg3TimeOnBattery,
       "imPM1BatLeg3Fuse": imPM1BatLeg3Fuse,
       "imPM1BatLeg3Breaker": imPM1BatLeg3Breaker,
       "imPM1BatLeg3LowVoltageDisconnect": imPM1BatLeg3LowVoltageDisconnect,
       "imPM1Distrib": imPM1Distrib,
       "imPm1Distrib": imPm1Distrib,
       "imPM1DistTable": imPM1DistTable,
       "imPM1DistEntry": imPM1DistEntry,
       "imPM1DistId": imPM1DistId,
       "imPM1DistFuse": imPM1DistFuse,
       "imPM1DistBreaker": imPM1DistBreaker,
       "imPM1Control": imPM1Control,
       "imPM1ContTable": imPM1ContTable,
       "imPM1ContEntry": imPM1ContEntry,
       "imPM1ContId": imPM1ContId,
       "imPM1ContState": imPM1ContState,
       "imPM1ContLabel": imPM1ContLabel,
       "imPM1ContTimeOFF": imPM1ContTimeOFF,
       "imPM1ContAuto": imPM1ContAuto,
       "imPM1ContTestCAPcommand": imPM1ContTestCAPcommand,
       "imPM1ContTestCAPvoltage": imPM1ContTestCAPvoltage,
       "imPM1ContTestCAPcurrent": imPM1ContTestCAPcurrent,
       "imPM1ContTestCAPtemperature": imPM1ContTestCAPtemperature,
       "imPM1ContTestCAPduration": imPM1ContTestCAPduration,
       "imPM1ContTestCAPstatus": imPM1ContTestCAPstatus,
       "imPanM2": imPanM2,
       "imPM2SystemID": imPM2SystemID,
       "imPM2SystemIDManufacturer": imPM2SystemIDManufacturer,
       "imPM2SystemIDType": imPM2SystemIDType,
       "imPM2SystemIDserNumb": imPM2SystemIDserNumb,
       "imPM2SystemIDnextServiceDate": imPM2SystemIDnextServiceDate,
       "imPM2SystemIDaddress": imPM2SystemIDaddress,
       "imPM2SystemIDhwVersion": imPM2SystemIDhwVersion,
       "imPM2SystemIDswVersion": imPM2SystemIDswVersion,
       "imPM2SystemIDPMserialNumber": imPM2SystemIDPMserialNumber,
       "imPM2SystemIDbuttonName": imPM2SystemIDbuttonName,
       "imPM2SystemGEN": imPM2SystemGEN,
       "imPM2SystemGENSurgeArrester": imPM2SystemGENSurgeArrester,
       "imPM2SystemGENDoor1": imPM2SystemGENDoor1,
       "imPM2SystemGENDoor2": imPM2SystemGENDoor2,
       "imPM2SystemGENFan": imPM2SystemGENFan,
       "imPM2SystemGENuser1": imPM2SystemGENuser1,
       "imPM2SystemGENuser2": imPM2SystemGENuser2,
       "imPM2SystemGENuser3": imPM2SystemGENuser3,
       "imPM2SystemGENuser4": imPM2SystemGENuser4,
       "imPM2SystemGENtemperature": imPM2SystemGENtemperature,
       "imPM2Power1": imPM2Power1,
       "imPM2Power1Manufacturer": imPM2Power1Manufacturer,
       "imPM2Power1Type": imPM2Power1Type,
       "imPM2Power1serNumb": imPM2Power1serNumb,
       "imPM2Power1nextServiceDate": imPM2Power1nextServiceDate,
       "imPM2Power1InputVoltage": imPM2Power1InputVoltage,
       "imPM2Power1InputCurrent": imPM2Power1InputCurrent,
       "imPM2Power1InputPowerVA": imPM2Power1InputPowerVA,
       "imPM2Power1InputPowerKVA": imPM2Power1InputPowerKVA,
       "imPM2Power1InputPowerW": imPM2Power1InputPowerW,
       "imPM2Power1InputPowerKW": imPM2Power1InputPowerKW,
       "imPM2Power1InputVoltagePhase1": imPM2Power1InputVoltagePhase1,
       "imPM2Power1InputCurrentPhase1": imPM2Power1InputCurrentPhase1,
       "imPM2Power1InputPowerVAphase1": imPM2Power1InputPowerVAphase1,
       "imPM2Power1InputPowerKVAphase1": imPM2Power1InputPowerKVAphase1,
       "imPM2Power1InputVoltagePhase2": imPM2Power1InputVoltagePhase2,
       "imPM2Power1InputCurrentPhase2": imPM2Power1InputCurrentPhase2,
       "imPM2Power1InputPowerVAphase2": imPM2Power1InputPowerVAphase2,
       "imPM2Power1InputPowerKVAphase2": imPM2Power1InputPowerKVAphase2,
       "imPM2Power1InputVoltagePhase3": imPM2Power1InputVoltagePhase3,
       "imPM2Power1InputCurrentPhase3": imPM2Power1InputCurrentPhase3,
       "imPM2Power1InputPowerVAphase3": imPM2Power1InputPowerVAphase3,
       "imPM2Power1InputPowerKVAphase3": imPM2Power1InputPowerKVAphase3,
       "imPM2Power1OutputVoltage": imPM2Power1OutputVoltage,
       "imPM2Power1OutputCurrent": imPM2Power1OutputCurrent,
       "imPM2Power1OutputPowerVA": imPM2Power1OutputPowerVA,
       "imPM2Power1OutputPowerKVA": imPM2Power1OutputPowerKVA,
       "imPM2Power1OutputPowerW": imPM2Power1OutputPowerW,
       "imPM2Power1OutputPowerKW": imPM2Power1OutputPowerKW,
       "imPM2Power1OutputLoad": imPM2Power1OutputLoad,
       "imPM2Power1OutputFrequency": imPM2Power1OutputFrequency,
       "imPM2Power1Temperature": imPM2Power1Temperature,
       "imPM2Power1Running1": imPM2Power1Running1,
       "imPM2Power1Running2": imPM2Power1Running2,
       "imPM2Power1Running3": imPM2Power1Running3,
       "imPM2Power1Running4": imPM2Power1Running4,
       "imPM2Power1Running5": imPM2Power1Running5,
       "imPM2Power1Running6": imPM2Power1Running6,
       "imPM2Power1Running7": imPM2Power1Running7,
       "imPM2Power1Running8": imPM2Power1Running8,
       "imPM2Power1InputFuse": imPM2Power1InputFuse,
       "imPM2Power1InputFuse1": imPM2Power1InputFuse1,
       "imPM2Power1InputFuse2": imPM2Power1InputFuse2,
       "imPM2Power1InputFuse3": imPM2Power1InputFuse3,
       "imPM2Power1InputBreaker": imPM2Power1InputBreaker,
       "imPM2Power1InputBreaker1": imPM2Power1InputBreaker1,
       "imPM2Power1InputBreaker2": imPM2Power1InputBreaker2,
       "imPM2Power1InputBreaker3": imPM2Power1InputBreaker3,
       "imPM2Power1InputSurgeArrester": imPM2Power1InputSurgeArrester,
       "imPM2Power1OutputFuse": imPM2Power1OutputFuse,
       "imPM2Power1OutputFuse1": imPM2Power1OutputFuse1,
       "imPM2Power1OutputFuse2": imPM2Power1OutputFuse2,
       "imPM2Power1OutputBreaker": imPM2Power1OutputBreaker,
       "imPM2Power1OutputBreaker1": imPM2Power1OutputBreaker1,
       "imPM2Power1OutputBreaker2": imPM2Power1OutputBreaker2,
       "imPM2Power1Fan": imPM2Power1Fan,
       "imPM2Power1BatteryAvailable": imPM2Power1BatteryAvailable,
       "imPM2Power1OutputVoltagePhase1": imPM2Power1OutputVoltagePhase1,
       "imPM2Power1OutputCurrentPhase1": imPM2Power1OutputCurrentPhase1,
       "imPM2Power1OutputPowerVAphase1": imPM2Power1OutputPowerVAphase1,
       "imPM2Power1OutputPowerKVAphase1": imPM2Power1OutputPowerKVAphase1,
       "imPM2Power1OutputVoltagePhase2": imPM2Power1OutputVoltagePhase2,
       "imPM2Power1OutputCurrentPhase2": imPM2Power1OutputCurrentPhase2,
       "imPM2Power1OutputPowerVAphase2": imPM2Power1OutputPowerVAphase2,
       "imPM2Power1OutputPowerKVAphase2": imPM2Power1OutputPowerKVAphase2,
       "imPM2Power1OutputVoltagePhase3": imPM2Power1OutputVoltagePhase3,
       "imPM2Power1OutputCurrentPhase3": imPM2Power1OutputCurrentPhase3,
       "imPM2Power1OutputPowerVAphase3": imPM2Power1OutputPowerVAphase3,
       "imPM2Power1OutputPowerKVAphase3": imPM2Power1OutputPowerKVAphase3,
       "imPM2Power2": imPM2Power2,
       "imPM2Power2Manufacturer": imPM2Power2Manufacturer,
       "imPM2Power2Type": imPM2Power2Type,
       "imPM2Power2serNumb": imPM2Power2serNumb,
       "imPM2Power2nextServiceDate": imPM2Power2nextServiceDate,
       "imPM2Power2InputVoltage": imPM2Power2InputVoltage,
       "imPM2Power2InputCurrent": imPM2Power2InputCurrent,
       "imPM2Power2InputPowerVA": imPM2Power2InputPowerVA,
       "imPM2Power2InputPowerKVA": imPM2Power2InputPowerKVA,
       "imPM2Power2InputPowerW": imPM2Power2InputPowerW,
       "imPM2Power2InputPowerKW": imPM2Power2InputPowerKW,
       "imPM2Power2InputVoltagePhase1": imPM2Power2InputVoltagePhase1,
       "imPM2Power2InputCurrentPhase1": imPM2Power2InputCurrentPhase1,
       "imPM2Power2InputPowerVAphase1": imPM2Power2InputPowerVAphase1,
       "imPM2Power2InputPowerKVAphase1": imPM2Power2InputPowerKVAphase1,
       "imPM2Power2InputVoltagePhase2": imPM2Power2InputVoltagePhase2,
       "imPM2Power2InputCurrentPhase2": imPM2Power2InputCurrentPhase2,
       "imPM2Power2InputPowerVAphase2": imPM2Power2InputPowerVAphase2,
       "imPM2Power2InputPowerKVAphase2": imPM2Power2InputPowerKVAphase2,
       "imPM2Power2InputVoltagePhase3": imPM2Power2InputVoltagePhase3,
       "imPM2Power2InputCurrentPhase3": imPM2Power2InputCurrentPhase3,
       "imPM2Power2InputPowerVAphase3": imPM2Power2InputPowerVAphase3,
       "imPM2Power2InputPowerKVAphase3": imPM2Power2InputPowerKVAphase3,
       "imPM2Power2OutputVoltage": imPM2Power2OutputVoltage,
       "imPM2Power2OutputCurrent": imPM2Power2OutputCurrent,
       "imPM2Power2OutputPowerVA": imPM2Power2OutputPowerVA,
       "imPM2Power2OutputPowerKVA": imPM2Power2OutputPowerKVA,
       "imPM2Power2OutputPowerW": imPM2Power2OutputPowerW,
       "imPM2Power2OutputPowerKW": imPM2Power2OutputPowerKW,
       "imPM2Power2OutputLoad": imPM2Power2OutputLoad,
       "imPM2Power2OutputFrequency": imPM2Power2OutputFrequency,
       "imPM2Power2Temperature": imPM2Power2Temperature,
       "imPM2Power2Running1": imPM2Power2Running1,
       "imPM2Power2Running2": imPM2Power2Running2,
       "imPM2Power2Running3": imPM2Power2Running3,
       "imPM2Power2Running4": imPM2Power2Running4,
       "imPM2Power2Running5": imPM2Power2Running5,
       "imPM2Power2Running6": imPM2Power2Running6,
       "imPM2Power2Running7": imPM2Power2Running7,
       "imPM2Power2Running8": imPM2Power2Running8,
       "imPM2Power2InputFuse": imPM2Power2InputFuse,
       "imPM2Power2InputFuse1": imPM2Power2InputFuse1,
       "imPM2Power2InputFuse2": imPM2Power2InputFuse2,
       "imPM2Power2InputFuse3": imPM2Power2InputFuse3,
       "imPM2Power2InputBreaker": imPM2Power2InputBreaker,
       "imPM2Power2InputBreaker1": imPM2Power2InputBreaker1,
       "imPM2Power2InputBreaker2": imPM2Power2InputBreaker2,
       "imPM2Power2InputBreaker3": imPM2Power2InputBreaker3,
       "imPM2Power2InputSurgeArrester": imPM2Power2InputSurgeArrester,
       "imPM2Power2OutputFuse": imPM2Power2OutputFuse,
       "imPM2Power2OutputFuse1": imPM2Power2OutputFuse1,
       "imPM2Power2OutputFuse2": imPM2Power2OutputFuse2,
       "imPM2Power2OutputBreaker": imPM2Power2OutputBreaker,
       "imPM2Power2OutputBreaker1": imPM2Power2OutputBreaker1,
       "imPM2Power2OutputBreaker2": imPM2Power2OutputBreaker2,
       "imPM2Power2Fan": imPM2Power2Fan,
       "imPM2Power2BatteryAvailable": imPM2Power2BatteryAvailable,
       "imPM2Power2OutputVoltagePhase1": imPM2Power2OutputVoltagePhase1,
       "imPM2Power2OutputCurrentPhase1": imPM2Power2OutputCurrentPhase1,
       "imPM2Power2OutputPowerVAphase1": imPM2Power2OutputPowerVAphase1,
       "imPM2Power2OutputPowerKVAphase1": imPM2Power2OutputPowerKVAphase1,
       "imPM2Power2OutputVoltagePhase2": imPM2Power2OutputVoltagePhase2,
       "imPM2Power2OutputCurrentPhase2": imPM2Power2OutputCurrentPhase2,
       "imPM2Power2OutputPowerVAphase2": imPM2Power2OutputPowerVAphase2,
       "imPM2Power2OutputPowerKVAphase2": imPM2Power2OutputPowerKVAphase2,
       "imPM2Power2OutputVoltagePhase3": imPM2Power2OutputVoltagePhase3,
       "imPM2Power2OutputCurrentPhase3": imPM2Power2OutputCurrentPhase3,
       "imPM2Power2OutputPowerVAphase3": imPM2Power2OutputPowerVAphase3,
       "imPM2Power2OutputPowerKVAphase3": imPM2Power2OutputPowerKVAphase3,
       "imPM2Power3": imPM2Power3,
       "imPM2Power3Manufacturer": imPM2Power3Manufacturer,
       "imPM2Power3Type": imPM2Power3Type,
       "imPM2Power3serNumb": imPM2Power3serNumb,
       "imPM2Power3nextServiceDate": imPM2Power3nextServiceDate,
       "imPM2Power3InputVoltage": imPM2Power3InputVoltage,
       "imPM2Power3InputCurrent": imPM2Power3InputCurrent,
       "imPM2Power3InputPowerVA": imPM2Power3InputPowerVA,
       "imPM2Power3InputPowerKVA": imPM2Power3InputPowerKVA,
       "imPM2Power3InputPowerW": imPM2Power3InputPowerW,
       "imPM2Power3InputPowerKW": imPM2Power3InputPowerKW,
       "imPM2Power3InputVoltagePhase1": imPM2Power3InputVoltagePhase1,
       "imPM2Power3InputCurrentPhase1": imPM2Power3InputCurrentPhase1,
       "imPM2Power3InputPowerVAphase1": imPM2Power3InputPowerVAphase1,
       "imPM2Power3InputPowerKVAphase1": imPM2Power3InputPowerKVAphase1,
       "imPM2Power3InputVoltagePhase2": imPM2Power3InputVoltagePhase2,
       "imPM2Power3InputCurrentPhase2": imPM2Power3InputCurrentPhase2,
       "imPM2Power3InputPowerVAphase2": imPM2Power3InputPowerVAphase2,
       "imPM2Power3InputPowerKVAphase2": imPM2Power3InputPowerKVAphase2,
       "imPM2Power3InputVoltagePhase3": imPM2Power3InputVoltagePhase3,
       "imPM2Power3InputCurrentPhase3": imPM2Power3InputCurrentPhase3,
       "imPM2Power3InputPowerVAphase3": imPM2Power3InputPowerVAphase3,
       "imPM2Power3InputPowerKVAphase3": imPM2Power3InputPowerKVAphase3,
       "imPM2Power3OutputVoltage": imPM2Power3OutputVoltage,
       "imPM2Power3OutputCurrent": imPM2Power3OutputCurrent,
       "imPM2Power3OutputPowerVA": imPM2Power3OutputPowerVA,
       "imPM2Power3OutputPowerKVA": imPM2Power3OutputPowerKVA,
       "imPM2Power3OutputPowerW": imPM2Power3OutputPowerW,
       "imPM2Power3OutputPowerKW": imPM2Power3OutputPowerKW,
       "imPM2Power3OutputLoad": imPM2Power3OutputLoad,
       "imPM2Power3OutputFrequency": imPM2Power3OutputFrequency,
       "imPM2Power3Temperature": imPM2Power3Temperature,
       "imPM2Power3Running1": imPM2Power3Running1,
       "imPM2Power3Running2": imPM2Power3Running2,
       "imPM2Power3Running3": imPM2Power3Running3,
       "imPM2Power3Running4": imPM2Power3Running4,
       "imPM2Power3Running5": imPM2Power3Running5,
       "imPM2Power3Running6": imPM2Power3Running6,
       "imPM2Power3Running7": imPM2Power3Running7,
       "imPM2Power3Running8": imPM2Power3Running8,
       "imPM2Power3InputFuse": imPM2Power3InputFuse,
       "imPM2Power3InputFuse1": imPM2Power3InputFuse1,
       "imPM2Power3InputFuse2": imPM2Power3InputFuse2,
       "imPM2Power3InputFuse3": imPM2Power3InputFuse3,
       "imPM2Power3InputBreaker": imPM2Power3InputBreaker,
       "imPM2Power3InputBreaker1": imPM2Power3InputBreaker1,
       "imPM2Power3InputBreaker2": imPM2Power3InputBreaker2,
       "imPM2Power3InputBreaker3": imPM2Power3InputBreaker3,
       "imPM2Power3InputSurgeArrester": imPM2Power3InputSurgeArrester,
       "imPM2Power3OutputFuse": imPM2Power3OutputFuse,
       "imPM2Power3OutputFuse1": imPM2Power3OutputFuse1,
       "imPM2Power3OutputFuse2": imPM2Power3OutputFuse2,
       "imPM2Power3OutputBreaker": imPM2Power3OutputBreaker,
       "imPM2Power3OutputBreaker1": imPM2Power3OutputBreaker1,
       "imPM2Power3OutputBreaker2": imPM2Power3OutputBreaker2,
       "imPM2Power3Fan": imPM2Power3Fan,
       "imPM2Power3BatteryAvailable": imPM2Power3BatteryAvailable,
       "imPM2Power3OutputVoltagePhase1": imPM2Power3OutputVoltagePhase1,
       "imPM2Power3OutputCurrentPhase1": imPM2Power3OutputCurrentPhase1,
       "imPM2Power3OutputPowerVAphase1": imPM2Power3OutputPowerVAphase1,
       "imPM2Power3OutputPowerKVAphase1": imPM2Power3OutputPowerKVAphase1,
       "imPM2Power3OutputVoltagePhase2": imPM2Power3OutputVoltagePhase2,
       "imPM2Power3OutputCurrentPhase2": imPM2Power3OutputCurrentPhase2,
       "imPM2Power3OutputPowerVAphase2": imPM2Power3OutputPowerVAphase2,
       "imPM2Power3OutputPowerKVAphase2": imPM2Power3OutputPowerKVAphase2,
       "imPM2Power3OutputVoltagePhase3": imPM2Power3OutputVoltagePhase3,
       "imPM2Power3OutputCurrentPhase3": imPM2Power3OutputCurrentPhase3,
       "imPM2Power3OutputPowerVAphase3": imPM2Power3OutputPowerVAphase3,
       "imPM2Power3OutputPowerKVAphase3": imPM2Power3OutputPowerKVAphase3,
       "imPM2Battery": imPM2Battery,
       "imPM2BatteryNominalCapacity": imPM2BatteryNominalCapacity,
       "imPM2BatteryVoltage": imPM2BatteryVoltage,
       "imPM2BatteryCurrent": imPM2BatteryCurrent,
       "imPM2BatteryChargeState": imPM2BatteryChargeState,
       "imPM2BatteryAutonomyTime": imPM2BatteryAutonomyTime,
       "imPM2BatteryTimeOnBattery": imPM2BatteryTimeOnBattery,
       "imPM2BatLeg1": imPM2BatLeg1,
       "imPM2BatLeg1Manufacturer": imPM2BatLeg1Manufacturer,
       "imPM2BatLeg1Type": imPM2BatLeg1Type,
       "imPM2BatLeg1serNumb": imPM2BatLeg1serNumb,
       "imPM2BatLeg1nextServiceDate": imPM2BatLeg1nextServiceDate,
       "imPM2BatLeg1InstallationDate": imPM2BatLeg1InstallationDate,
       "imPM2BatLeg1NominalVoltage": imPM2BatLeg1NominalVoltage,
       "imPM2BatLeg1NominalCapacity": imPM2BatLeg1NominalCapacity,
       "imPM2BatLeg1Lifetime": imPM2BatLeg1Lifetime,
       "imPM2BatLeg1Voltage": imPM2BatLeg1Voltage,
       "imPM2BatLeg1Current": imPM2BatLeg1Current,
       "imPM2BatLeg1Temperature": imPM2BatLeg1Temperature,
       "imPM2BatLeg1ChargeState": imPM2BatLeg1ChargeState,
       "imPM2BatLeg1RestCapacity": imPM2BatLeg1RestCapacity,
       "imPM2BatLeg1Autonomytime": imPM2BatLeg1Autonomytime,
       "imPM2BatLeg1TimeOnBattery": imPM2BatLeg1TimeOnBattery,
       "imPM2BatLeg1Fuse": imPM2BatLeg1Fuse,
       "imPM2BatLeg1Breaker": imPM2BatLeg1Breaker,
       "imPM2BatLeg1LowVoltageDisconnect": imPM2BatLeg1LowVoltageDisconnect,
       "imPM2BatLeg2": imPM2BatLeg2,
       "imPM2BatLeg2Manufacturer": imPM2BatLeg2Manufacturer,
       "imPM2BatLeg2Type": imPM2BatLeg2Type,
       "imPM2BatLeg2serNumb": imPM2BatLeg2serNumb,
       "imPM2BatLeg2nextServiceDate": imPM2BatLeg2nextServiceDate,
       "imPM2BatLeg2InstallationDate": imPM2BatLeg2InstallationDate,
       "imPM2BatLeg2NominalVoltage": imPM2BatLeg2NominalVoltage,
       "imPM2BatLeg2NominalCapacity": imPM2BatLeg2NominalCapacity,
       "imPM2BatLeg2Lifetime": imPM2BatLeg2Lifetime,
       "imPM2BatLeg2Voltage": imPM2BatLeg2Voltage,
       "imPM2BatLeg2Current": imPM2BatLeg2Current,
       "imPM2BatLeg2Temperature": imPM2BatLeg2Temperature,
       "imPM2BatLeg2ChargeState": imPM2BatLeg2ChargeState,
       "imPM2BatLeg2RestCapacity": imPM2BatLeg2RestCapacity,
       "imPM2BatLeg2Autonomytime": imPM2BatLeg2Autonomytime,
       "imPM2BatLeg2TimeOnBattery": imPM2BatLeg2TimeOnBattery,
       "imPM2BatLeg2Fuse": imPM2BatLeg2Fuse,
       "imPM2BatLeg2Breaker": imPM2BatLeg2Breaker,
       "imPM2BatLeg2LowVoltageDisconnect": imPM2BatLeg2LowVoltageDisconnect,
       "imPM2BatLeg3": imPM2BatLeg3,
       "imPM2BatLeg3Manufacturer": imPM2BatLeg3Manufacturer,
       "imPM2BatLeg3Type": imPM2BatLeg3Type,
       "imPM2BatLeg3serNumb": imPM2BatLeg3serNumb,
       "imPM2BatLeg3nextServiceDate": imPM2BatLeg3nextServiceDate,
       "imPM2BatLeg3InstallationDate": imPM2BatLeg3InstallationDate,
       "imPM2BatLeg3NominalVoltage": imPM2BatLeg3NominalVoltage,
       "imPM2BatLeg3NominalCapacity": imPM2BatLeg3NominalCapacity,
       "imPM2BatLeg3Lifetime": imPM2BatLeg3Lifetime,
       "imPM2BatLeg3Voltage": imPM2BatLeg3Voltage,
       "imPM2BatLeg3Current": imPM2BatLeg3Current,
       "imPM2BatLeg3Temperature": imPM2BatLeg3Temperature,
       "imPM2BatLeg3ChargeState": imPM2BatLeg3ChargeState,
       "imPM2BatLeg3RestCapacity": imPM2BatLeg3RestCapacity,
       "imPM2BatLeg3Autonomytime": imPM2BatLeg3Autonomytime,
       "imPM2BatLeg3TimeOnBattery": imPM2BatLeg3TimeOnBattery,
       "imPM2BatLeg3Fuse": imPM2BatLeg3Fuse,
       "imPM2BatLeg3Breaker": imPM2BatLeg3Breaker,
       "imPM2BatLeg3LowVoltageDisconnect": imPM2BatLeg3LowVoltageDisconnect,
       "imPM2Distrib": imPM2Distrib,
       "imPm2Distrib": imPm2Distrib,
       "imPM2DistTable": imPM2DistTable,
       "imPM2DistEntry": imPM2DistEntry,
       "imPM2DistId": imPM2DistId,
       "imPM2DistFuse": imPM2DistFuse,
       "imPM2DistBreaker": imPM2DistBreaker,
       "imPM2Control": imPM2Control,
       "imPM2ContTable": imPM2ContTable,
       "imPM2ContEntry": imPM2ContEntry,
       "imPM2ContId": imPM2ContId,
       "imPM2ContState": imPM2ContState,
       "imPM2ContLabel": imPM2ContLabel,
       "imPM2ContTimeOFF": imPM2ContTimeOFF,
       "imPM2ContAuto": imPM2ContAuto,
       "imPM2ContTestCAPcommand": imPM2ContTestCAPcommand,
       "imPM2ContTestCAPvoltage": imPM2ContTestCAPvoltage,
       "imPM2ContTestCAPcurrent": imPM2ContTestCAPcurrent,
       "imPM2ContTestCAPtemperature": imPM2ContTestCAPtemperature,
       "imPM2ContTestCAPduration": imPM2ContTestCAPduration,
       "imPM2ContTestCAPstatus": imPM2ContTestCAPstatus,
       "imPanM3": imPanM3,
       "imPM3SystemID": imPM3SystemID,
       "imPM3SystemIDManufacturer": imPM3SystemIDManufacturer,
       "imPM3SystemIDType": imPM3SystemIDType,
       "imPM3SystemIDserNumb": imPM3SystemIDserNumb,
       "imPM3SystemIDnextServiceDate": imPM3SystemIDnextServiceDate,
       "imPM3SystemIDaddress": imPM3SystemIDaddress,
       "imPM3SystemIDhwVersion": imPM3SystemIDhwVersion,
       "imPM3SystemIDswVersion": imPM3SystemIDswVersion,
       "imPM3SystemIDPMserialNumber": imPM3SystemIDPMserialNumber,
       "imPM3SystemIDbuttonName": imPM3SystemIDbuttonName,
       "imPM3SystemGEN": imPM3SystemGEN,
       "imPM3SystemGENSurgeArrester": imPM3SystemGENSurgeArrester,
       "imPM3SystemGENDoor1": imPM3SystemGENDoor1,
       "imPM3SystemGENDoor2": imPM3SystemGENDoor2,
       "imPM3SystemGENFan": imPM3SystemGENFan,
       "imPM3SystemGENuser1": imPM3SystemGENuser1,
       "imPM3SystemGENuser2": imPM3SystemGENuser2,
       "imPM3SystemGENuser3": imPM3SystemGENuser3,
       "imPM3SystemGENuser4": imPM3SystemGENuser4,
       "imPM3SystemGENtemperature": imPM3SystemGENtemperature,
       "imPM3Power1": imPM3Power1,
       "imPM3Power1Manufacturer": imPM3Power1Manufacturer,
       "imPM3Power1Type": imPM3Power1Type,
       "imPM3Power1serNumb": imPM3Power1serNumb,
       "imPM3Power1nextServiceDate": imPM3Power1nextServiceDate,
       "imPM3Power1InputVoltage": imPM3Power1InputVoltage,
       "imPM3Power1InputCurrent": imPM3Power1InputCurrent,
       "imPM3Power1InputPowerVA": imPM3Power1InputPowerVA,
       "imPM3Power1InputPowerKVA": imPM3Power1InputPowerKVA,
       "imPM3Power1InputPowerW": imPM3Power1InputPowerW,
       "imPM3Power1InputPowerKW": imPM3Power1InputPowerKW,
       "imPM3Power1InputVoltagePhase1": imPM3Power1InputVoltagePhase1,
       "imPM3Power1InputCurrentPhase1": imPM3Power1InputCurrentPhase1,
       "imPM3Power1InputPowerVAphase1": imPM3Power1InputPowerVAphase1,
       "imPM3Power1InputPowerKVAphase1": imPM3Power1InputPowerKVAphase1,
       "imPM3Power1InputVoltagePhase2": imPM3Power1InputVoltagePhase2,
       "imPM3Power1InputCurrentPhase2": imPM3Power1InputCurrentPhase2,
       "imPM3Power1InputPowerVAphase2": imPM3Power1InputPowerVAphase2,
       "imPM3Power1InputPowerKVAphase2": imPM3Power1InputPowerKVAphase2,
       "imPM3Power1InputVoltagePhase3": imPM3Power1InputVoltagePhase3,
       "imPM3Power1InputCurrentPhase3": imPM3Power1InputCurrentPhase3,
       "imPM3Power1InputPowerVAphase3": imPM3Power1InputPowerVAphase3,
       "imPM3Power1InputPowerKVAphase3": imPM3Power1InputPowerKVAphase3,
       "imPM3Power1OutputVoltage": imPM3Power1OutputVoltage,
       "imPM3Power1OutputCurrent": imPM3Power1OutputCurrent,
       "imPM3Power1OutputPowerVA": imPM3Power1OutputPowerVA,
       "imPM3Power1OutputPowerKVA": imPM3Power1OutputPowerKVA,
       "imPM3Power1OutputPowerW": imPM3Power1OutputPowerW,
       "imPM3Power1OutputPowerKW": imPM3Power1OutputPowerKW,
       "imPM3Power1OutputLoad": imPM3Power1OutputLoad,
       "imPM3Power1OutputFrequency": imPM3Power1OutputFrequency,
       "imPM3Power1Temperature": imPM3Power1Temperature,
       "imPM3Power1Running1": imPM3Power1Running1,
       "imPM3Power1Running2": imPM3Power1Running2,
       "imPM3Power1Running3": imPM3Power1Running3,
       "imPM3Power1Running4": imPM3Power1Running4,
       "imPM3Power1Running5": imPM3Power1Running5,
       "imPM3Power1Running6": imPM3Power1Running6,
       "imPM3Power1Running7": imPM3Power1Running7,
       "imPM3Power1Running8": imPM3Power1Running8,
       "imPM3Power1InputFuse": imPM3Power1InputFuse,
       "imPM3Power1InputFuse1": imPM3Power1InputFuse1,
       "imPM3Power1InputFuse2": imPM3Power1InputFuse2,
       "imPM3Power1InputFuse3": imPM3Power1InputFuse3,
       "imPM3Power1InputBreaker": imPM3Power1InputBreaker,
       "imPM3Power1InputBreaker1": imPM3Power1InputBreaker1,
       "imPM3Power1InputBreaker2": imPM3Power1InputBreaker2,
       "imPM3Power1InputBreaker3": imPM3Power1InputBreaker3,
       "imPM3Power1InputSurgeArrester": imPM3Power1InputSurgeArrester,
       "imPM3Power1OutputFuse": imPM3Power1OutputFuse,
       "imPM3Power1OutputFuse1": imPM3Power1OutputFuse1,
       "imPM3Power1OutputFuse2": imPM3Power1OutputFuse2,
       "imPM3Power1OutputBreaker": imPM3Power1OutputBreaker,
       "imPM3Power1OutputBreaker1": imPM3Power1OutputBreaker1,
       "imPM3Power1OutputBreaker2": imPM3Power1OutputBreaker2,
       "imPM3Power1Fan": imPM3Power1Fan,
       "imPM3Power1BatteryAvailable": imPM3Power1BatteryAvailable,
       "imPM3Power1OutputVoltagePhase1": imPM3Power1OutputVoltagePhase1,
       "imPM3Power1OutputCurrentPhase1": imPM3Power1OutputCurrentPhase1,
       "imPM3Power1OutputPowerVAphase1": imPM3Power1OutputPowerVAphase1,
       "imPM3Power1OutputPowerKVAphase1": imPM3Power1OutputPowerKVAphase1,
       "imPM3Power1OutputVoltagePhase2": imPM3Power1OutputVoltagePhase2,
       "imPM3Power1OutputCurrentPhase2": imPM3Power1OutputCurrentPhase2,
       "imPM3Power1OutputPowerVAphase2": imPM3Power1OutputPowerVAphase2,
       "imPM3Power1OutputPowerKVAphase2": imPM3Power1OutputPowerKVAphase2,
       "imPM3Power1OutputVoltagePhase3": imPM3Power1OutputVoltagePhase3,
       "imPM3Power1OutputCurrentPhase3": imPM3Power1OutputCurrentPhase3,
       "imPM3Power1OutputPowerVAphase3": imPM3Power1OutputPowerVAphase3,
       "imPM3Power1OutputPowerKVAphase3": imPM3Power1OutputPowerKVAphase3,
       "imPM3Power2": imPM3Power2,
       "imPM3Power2Manufacturer": imPM3Power2Manufacturer,
       "imPM3Power2Type": imPM3Power2Type,
       "imPM3Power2serNumb": imPM3Power2serNumb,
       "imPM3Power2nextServiceDate": imPM3Power2nextServiceDate,
       "imPM3Power2InputVoltage": imPM3Power2InputVoltage,
       "imPM3Power2InputCurrent": imPM3Power2InputCurrent,
       "imPM3Power2InputPowerVA": imPM3Power2InputPowerVA,
       "imPM3Power2InputPowerKVA": imPM3Power2InputPowerKVA,
       "imPM3Power2InputPowerW": imPM3Power2InputPowerW,
       "imPM3Power2InputPowerKW": imPM3Power2InputPowerKW,
       "imPM3Power2InputVoltagePhase1": imPM3Power2InputVoltagePhase1,
       "imPM3Power2InputCurrentPhase1": imPM3Power2InputCurrentPhase1,
       "imPM3Power2InputPowerVAphase1": imPM3Power2InputPowerVAphase1,
       "imPM3Power2InputPowerKVAphase1": imPM3Power2InputPowerKVAphase1,
       "imPM3Power2InputVoltagePhase2": imPM3Power2InputVoltagePhase2,
       "imPM3Power2InputCurrentPhase2": imPM3Power2InputCurrentPhase2,
       "imPM3Power2InputPowerVAphase2": imPM3Power2InputPowerVAphase2,
       "imPM3Power2InputPowerKVAphase2": imPM3Power2InputPowerKVAphase2,
       "imPM3Power2InputVoltagePhase3": imPM3Power2InputVoltagePhase3,
       "imPM3Power2InputCurrentPhase3": imPM3Power2InputCurrentPhase3,
       "imPM3Power2InputPowerVAphase3": imPM3Power2InputPowerVAphase3,
       "imPM3Power2InputPowerKVAphase3": imPM3Power2InputPowerKVAphase3,
       "imPM3Power2OutputVoltage": imPM3Power2OutputVoltage,
       "imPM3Power2OutputCurrent": imPM3Power2OutputCurrent,
       "imPM3Power2OutputPowerVA": imPM3Power2OutputPowerVA,
       "imPM3Power2OutputPowerKVA": imPM3Power2OutputPowerKVA,
       "imPM3Power2OutputPowerW": imPM3Power2OutputPowerW,
       "imPM3Power2OutputPowerKW": imPM3Power2OutputPowerKW,
       "imPM3Power2OutputLoad": imPM3Power2OutputLoad,
       "imPM3Power2OutputFrequency": imPM3Power2OutputFrequency,
       "imPM3Power2Temperature": imPM3Power2Temperature,
       "imPM3Power2Running1": imPM3Power2Running1,
       "imPM3Power2Running2": imPM3Power2Running2,
       "imPM3Power2Running3": imPM3Power2Running3,
       "imPM3Power2Running4": imPM3Power2Running4,
       "imPM3Power2Running5": imPM3Power2Running5,
       "imPM3Power2Running6": imPM3Power2Running6,
       "imPM3Power2Running7": imPM3Power2Running7,
       "imPM3Power2Running8": imPM3Power2Running8,
       "imPM3Power2InputFuse": imPM3Power2InputFuse,
       "imPM3Power2InputFuse1": imPM3Power2InputFuse1,
       "imPM3Power2InputFuse2": imPM3Power2InputFuse2,
       "imPM3Power2InputFuse3": imPM3Power2InputFuse3,
       "imPM3Power2InputBreaker": imPM3Power2InputBreaker,
       "imPM3Power2InputBreaker1": imPM3Power2InputBreaker1,
       "imPM3Power2InputBreaker2": imPM3Power2InputBreaker2,
       "imPM3Power2InputBreaker3": imPM3Power2InputBreaker3,
       "imPM3Power2InputSurgeArrester": imPM3Power2InputSurgeArrester,
       "imPM3Power2OutputFuse": imPM3Power2OutputFuse,
       "imPM3Power2OutputFuse1": imPM3Power2OutputFuse1,
       "imPM3Power2OutputFuse2": imPM3Power2OutputFuse2,
       "imPM3Power2OutputBreaker": imPM3Power2OutputBreaker,
       "imPM3Power2OutputBreaker1": imPM3Power2OutputBreaker1,
       "imPM3Power2OutputBreaker2": imPM3Power2OutputBreaker2,
       "imPM3Power2Fan": imPM3Power2Fan,
       "imPM3Power2BatteryAvailable": imPM3Power2BatteryAvailable,
       "imPM3Power2OutputVoltagePhase1": imPM3Power2OutputVoltagePhase1,
       "imPM3Power2OutputCurrentPhase1": imPM3Power2OutputCurrentPhase1,
       "imPM3Power2OutputPowerVAphase1": imPM3Power2OutputPowerVAphase1,
       "imPM3Power2OutputPowerKVAphase1": imPM3Power2OutputPowerKVAphase1,
       "imPM3Power2OutputVoltagePhase2": imPM3Power2OutputVoltagePhase2,
       "imPM3Power2OutputCurrentPhase2": imPM3Power2OutputCurrentPhase2,
       "imPM3Power2OutputPowerVAphase2": imPM3Power2OutputPowerVAphase2,
       "imPM3Power2OutputPowerKVAphase2": imPM3Power2OutputPowerKVAphase2,
       "imPM3Power2OutputVoltagePhase3": imPM3Power2OutputVoltagePhase3,
       "imPM3Power2OutputCurrentPhase3": imPM3Power2OutputCurrentPhase3,
       "imPM3Power2OutputPowerVAphase3": imPM3Power2OutputPowerVAphase3,
       "imPM3Power2OutputPowerKVAphase3": imPM3Power2OutputPowerKVAphase3,
       "imPM3Power3": imPM3Power3,
       "imPM3Power3Manufacturer": imPM3Power3Manufacturer,
       "imPM3Power3Type": imPM3Power3Type,
       "imPM3Power3serNumb": imPM3Power3serNumb,
       "imPM3Power3nextServiceDate": imPM3Power3nextServiceDate,
       "imPM3Power3InputVoltage": imPM3Power3InputVoltage,
       "imPM3Power3InputCurrent": imPM3Power3InputCurrent,
       "imPM3Power3InputPowerVA": imPM3Power3InputPowerVA,
       "imPM3Power3InputPowerKVA": imPM3Power3InputPowerKVA,
       "imPM3Power3InputPowerW": imPM3Power3InputPowerW,
       "imPM3Power3InputPowerKW": imPM3Power3InputPowerKW,
       "imPM3Power3InputVoltagePhase1": imPM3Power3InputVoltagePhase1,
       "imPM3Power3InputCurrentPhase1": imPM3Power3InputCurrentPhase1,
       "imPM3Power3InputPowerVAphase1": imPM3Power3InputPowerVAphase1,
       "imPM3Power3InputPowerKVAphase1": imPM3Power3InputPowerKVAphase1,
       "imPM3Power3InputVoltagePhase2": imPM3Power3InputVoltagePhase2,
       "imPM3Power3InputCurrentPhase2": imPM3Power3InputCurrentPhase2,
       "imPM3Power3InputPowerVAphase2": imPM3Power3InputPowerVAphase2,
       "imPM3Power3InputPowerKVAphase2": imPM3Power3InputPowerKVAphase2,
       "imPM3Power3InputVoltagePhase3": imPM3Power3InputVoltagePhase3,
       "imPM3Power3InputCurrentPhase3": imPM3Power3InputCurrentPhase3,
       "imPM3Power3InputPowerVAphase3": imPM3Power3InputPowerVAphase3,
       "imPM3Power3InputPowerKVAphase3": imPM3Power3InputPowerKVAphase3,
       "imPM3Power3OutputVoltage": imPM3Power3OutputVoltage,
       "imPM3Power3OutputCurrent": imPM3Power3OutputCurrent,
       "imPM3Power3OutputPowerVA": imPM3Power3OutputPowerVA,
       "imPM3Power3OutputPowerKVA": imPM3Power3OutputPowerKVA,
       "imPM3Power3OutputPowerW": imPM3Power3OutputPowerW,
       "imPM3Power3OutputPowerKW": imPM3Power3OutputPowerKW,
       "imPM3Power3OutputLoad": imPM3Power3OutputLoad,
       "imPM3Power3OutputFrequency": imPM3Power3OutputFrequency,
       "imPM3Power3Temperature": imPM3Power3Temperature,
       "imPM3Power3Running1": imPM3Power3Running1,
       "imPM3Power3Running2": imPM3Power3Running2,
       "imPM3Power3Running3": imPM3Power3Running3,
       "imPM3Power3Running4": imPM3Power3Running4,
       "imPM3Power3Running5": imPM3Power3Running5,
       "imPM3Power3Running6": imPM3Power3Running6,
       "imPM3Power3Running7": imPM3Power3Running7,
       "imPM3Power3Running8": imPM3Power3Running8,
       "imPM3Power3InputFuse": imPM3Power3InputFuse,
       "imPM3Power3InputFuse1": imPM3Power3InputFuse1,
       "imPM3Power3InputFuse2": imPM3Power3InputFuse2,
       "imPM3Power3InputFuse3": imPM3Power3InputFuse3,
       "imPM3Power3InputBreaker": imPM3Power3InputBreaker,
       "imPM3Power3InputBreaker1": imPM3Power3InputBreaker1,
       "imPM3Power3InputBreaker2": imPM3Power3InputBreaker2,
       "imPM3Power3InputBreaker3": imPM3Power3InputBreaker3,
       "imPM3Power3InputSurgeArrester": imPM3Power3InputSurgeArrester,
       "imPM3Power3OutputFuse": imPM3Power3OutputFuse,
       "imPM3Power3OutputFuse1": imPM3Power3OutputFuse1,
       "imPM3Power3OutputFuse2": imPM3Power3OutputFuse2,
       "imPM3Power3OutputBreaker": imPM3Power3OutputBreaker,
       "imPM3Power3OutputBreaker1": imPM3Power3OutputBreaker1,
       "imPM3Power3OutputBreaker2": imPM3Power3OutputBreaker2,
       "imPM3Power3Fan": imPM3Power3Fan,
       "imPM3Power3BatteryAvailable": imPM3Power3BatteryAvailable,
       "imPM3Power3OutputVoltagePhase1": imPM3Power3OutputVoltagePhase1,
       "imPM3Power3OutputCurrentPhase1": imPM3Power3OutputCurrentPhase1,
       "imPM3Power3OutputPowerVAphase1": imPM3Power3OutputPowerVAphase1,
       "imPM3Power3OutputPowerKVAphase1": imPM3Power3OutputPowerKVAphase1,
       "imPM3Power3OutputVoltagePhase2": imPM3Power3OutputVoltagePhase2,
       "imPM3Power3OutputCurrentPhase2": imPM3Power3OutputCurrentPhase2,
       "imPM3Power3OutputPowerVAphase2": imPM3Power3OutputPowerVAphase2,
       "imPM3Power3OutputPowerKVAphase2": imPM3Power3OutputPowerKVAphase2,
       "imPM3Power3OutputVoltagePhase3": imPM3Power3OutputVoltagePhase3,
       "imPM3Power3OutputCurrentPhase3": imPM3Power3OutputCurrentPhase3,
       "imPM3Power3OutputPowerVAphase3": imPM3Power3OutputPowerVAphase3,
       "imPM3Power3OutputPowerKVAphase3": imPM3Power3OutputPowerKVAphase3,
       "imPM3Battery": imPM3Battery,
       "imPM3BatteryNominalCapacity": imPM3BatteryNominalCapacity,
       "imPM3BatteryVoltage": imPM3BatteryVoltage,
       "imPM3BatteryCurrent": imPM3BatteryCurrent,
       "imPM3BatteryChargeState": imPM3BatteryChargeState,
       "imPM3BatteryAutonomyTime": imPM3BatteryAutonomyTime,
       "imPM3BatteryTimeOnBattery": imPM3BatteryTimeOnBattery,
       "imPM3BatLeg1": imPM3BatLeg1,
       "imPM3BatLeg1Manufacturer": imPM3BatLeg1Manufacturer,
       "imPM3BatLeg1Type": imPM3BatLeg1Type,
       "imPM3BatLeg1serNumb": imPM3BatLeg1serNumb,
       "imPM3BatLeg1nextServiceDate": imPM3BatLeg1nextServiceDate,
       "imPM3BatLeg1InstallationDate": imPM3BatLeg1InstallationDate,
       "imPM3BatLeg1NominalVoltage": imPM3BatLeg1NominalVoltage,
       "imPM3BatLeg1NominalCapacity": imPM3BatLeg1NominalCapacity,
       "imPM3BatLeg1Lifetime": imPM3BatLeg1Lifetime,
       "imPM3BatLeg1Voltage": imPM3BatLeg1Voltage,
       "imPM3BatLeg1Current": imPM3BatLeg1Current,
       "imPM3BatLeg1Temperature": imPM3BatLeg1Temperature,
       "imPM3BatLeg1ChargeState": imPM3BatLeg1ChargeState,
       "imPM3BatLeg1RestCapacity": imPM3BatLeg1RestCapacity,
       "imPM3BatLeg1Autonomytime": imPM3BatLeg1Autonomytime,
       "imPM3BatLeg1TimeOnBattery": imPM3BatLeg1TimeOnBattery,
       "imPM3BatLeg1Fuse": imPM3BatLeg1Fuse,
       "imPM3BatLeg1Breaker": imPM3BatLeg1Breaker,
       "imPM3BatLeg1LowVoltageDisconnect": imPM3BatLeg1LowVoltageDisconnect,
       "imPM3BatLeg2": imPM3BatLeg2,
       "imPM3BatLeg2Manufacturer": imPM3BatLeg2Manufacturer,
       "imPM3BatLeg2Type": imPM3BatLeg2Type,
       "imPM3BatLeg2serNumb": imPM3BatLeg2serNumb,
       "imPM3BatLeg2nextServiceDate": imPM3BatLeg2nextServiceDate,
       "imPM3BatLeg2InstallationDate": imPM3BatLeg2InstallationDate,
       "imPM3BatLeg2NominalVoltage": imPM3BatLeg2NominalVoltage,
       "imPM3BatLeg2NominalCapacity": imPM3BatLeg2NominalCapacity,
       "imPM3BatLeg2Lifetime": imPM3BatLeg2Lifetime,
       "imPM3BatLeg2Voltage": imPM3BatLeg2Voltage,
       "imPM3BatLeg2Current": imPM3BatLeg2Current,
       "imPM3BatLeg2Temperature": imPM3BatLeg2Temperature,
       "imPM3BatLeg2ChargeState": imPM3BatLeg2ChargeState,
       "imPM3BatLeg2RestCapacity": imPM3BatLeg2RestCapacity,
       "imPM3BatLeg2Autonomytime": imPM3BatLeg2Autonomytime,
       "imPM3BatLeg2TimeOnBattery": imPM3BatLeg2TimeOnBattery,
       "imPM3BatLeg2Fuse": imPM3BatLeg2Fuse,
       "imPM3BatLeg2Breaker": imPM3BatLeg2Breaker,
       "imPM3BatLeg2LowVoltageDisconnect": imPM3BatLeg2LowVoltageDisconnect,
       "imPM3BatLeg3": imPM3BatLeg3,
       "imPM3BatLeg3Manufacturer": imPM3BatLeg3Manufacturer,
       "imPM3BatLeg3Type": imPM3BatLeg3Type,
       "imPM3BatLeg3serNumb": imPM3BatLeg3serNumb,
       "imPM3BatLeg3nextServiceDate": imPM3BatLeg3nextServiceDate,
       "imPM3BatLeg3InstallationDate": imPM3BatLeg3InstallationDate,
       "imPM3BatLeg3NominalVoltage": imPM3BatLeg3NominalVoltage,
       "imPM3BatLeg3NominalCapacity": imPM3BatLeg3NominalCapacity,
       "imPM3BatLeg3Lifetime": imPM3BatLeg3Lifetime,
       "imPM3BatLeg3Voltage": imPM3BatLeg3Voltage,
       "imPM3BatLeg3Current": imPM3BatLeg3Current,
       "imPM3BatLeg3Temperature": imPM3BatLeg3Temperature,
       "imPM3BatLeg3ChargeState": imPM3BatLeg3ChargeState,
       "imPM3BatLeg3RestCapacity": imPM3BatLeg3RestCapacity,
       "imPM3BatLeg3Autonomytime": imPM3BatLeg3Autonomytime,
       "imPM3BatLeg3TimeOnBattery": imPM3BatLeg3TimeOnBattery,
       "imPM3BatLeg3Fuse": imPM3BatLeg3Fuse,
       "imPM3BatLeg3Breaker": imPM3BatLeg3Breaker,
       "imPM3BatLeg3LowVoltageDisconnect": imPM3BatLeg3LowVoltageDisconnect,
       "imPM3Distrib": imPM3Distrib,
       "imPm3Distrib": imPm3Distrib,
       "imPM3DistTable": imPM3DistTable,
       "imPM3DistEntry": imPM3DistEntry,
       "imPM3DistId": imPM3DistId,
       "imPM3DistFuse": imPM3DistFuse,
       "imPM3DistBreaker": imPM3DistBreaker,
       "imPM3Control": imPM3Control,
       "imPM3ContTable": imPM3ContTable,
       "imPM3ContEntry": imPM3ContEntry,
       "imPM3ContId": imPM3ContId,
       "imPM3ContState": imPM3ContState,
       "imPM3ContLabel": imPM3ContLabel,
       "imPM3ContTimeOFF": imPM3ContTimeOFF,
       "imPM3ContAuto": imPM3ContAuto,
       "imPM3ContTestCAPcommand": imPM3ContTestCAPcommand,
       "imPM3ContTestCAPvoltage": imPM3ContTestCAPvoltage,
       "imPM3ContTestCAPcurrent": imPM3ContTestCAPcurrent,
       "imPM3ContTestCAPtemperature": imPM3ContTestCAPtemperature,
       "imPM3ContTestCAPduration": imPM3ContTestCAPduration,
       "imPM3ContTestCAPstatus": imPM3ContTestCAPstatus,
       "imPanM4": imPanM4,
       "imPM4SystemID": imPM4SystemID,
       "imPM4SystemIDManufacturer": imPM4SystemIDManufacturer,
       "imPM4SystemIDType": imPM4SystemIDType,
       "imPM4SystemIDserNumb": imPM4SystemIDserNumb,
       "imPM4SystemIDnextServiceDate": imPM4SystemIDnextServiceDate,
       "imPM4SystemIDaddress": imPM4SystemIDaddress,
       "imPM4SystemIDhwVersion": imPM4SystemIDhwVersion,
       "imPM4SystemIDswVersion": imPM4SystemIDswVersion,
       "imPM4SystemIDPMserialNumber": imPM4SystemIDPMserialNumber,
       "imPM4SystemIDbuttonName": imPM4SystemIDbuttonName,
       "imPM4SystemGEN": imPM4SystemGEN,
       "imPM4SystemGENSurgeArrester": imPM4SystemGENSurgeArrester,
       "imPM4SystemGENDoor1": imPM4SystemGENDoor1,
       "imPM4SystemGENDoor2": imPM4SystemGENDoor2,
       "imPM4SystemGENFan": imPM4SystemGENFan,
       "imPM4SystemGENuser1": imPM4SystemGENuser1,
       "imPM4SystemGENuser2": imPM4SystemGENuser2,
       "imPM4SystemGENuser3": imPM4SystemGENuser3,
       "imPM4SystemGENuser4": imPM4SystemGENuser4,
       "imPM4SystemGENtemperature": imPM4SystemGENtemperature,
       "imPM4Power1": imPM4Power1,
       "imPM4Power1Manufacturer": imPM4Power1Manufacturer,
       "imPM4Power1Type": imPM4Power1Type,
       "imPM4Power1serNumb": imPM4Power1serNumb,
       "imPM4Power1nextServiceDate": imPM4Power1nextServiceDate,
       "imPM4Power1InputVoltage": imPM4Power1InputVoltage,
       "imPM4Power1InputCurrent": imPM4Power1InputCurrent,
       "imPM4Power1InputPowerVA": imPM4Power1InputPowerVA,
       "imPM4Power1InputPowerKVA": imPM4Power1InputPowerKVA,
       "imPM4Power1InputPowerW": imPM4Power1InputPowerW,
       "imPM4Power1InputPowerKW": imPM4Power1InputPowerKW,
       "imPM4Power1InputVoltagePhase1": imPM4Power1InputVoltagePhase1,
       "imPM4Power1InputCurrentPhase1": imPM4Power1InputCurrentPhase1,
       "imPM4Power1InputPowerVAphase1": imPM4Power1InputPowerVAphase1,
       "imPM4Power1InputPowerKVAphase1": imPM4Power1InputPowerKVAphase1,
       "imPM4Power1InputVoltagePhase2": imPM4Power1InputVoltagePhase2,
       "imPM4Power1InputCurrentPhase2": imPM4Power1InputCurrentPhase2,
       "imPM4Power1InputPowerVAphase2": imPM4Power1InputPowerVAphase2,
       "imPM4Power1InputPowerKVAphase2": imPM4Power1InputPowerKVAphase2,
       "imPM4Power1InputVoltagePhase3": imPM4Power1InputVoltagePhase3,
       "imPM4Power1InputCurrentPhase3": imPM4Power1InputCurrentPhase3,
       "imPM4Power1InputPowerVAphase3": imPM4Power1InputPowerVAphase3,
       "imPM4Power1InputPowerKVAphase3": imPM4Power1InputPowerKVAphase3,
       "imPM4Power1OutputVoltage": imPM4Power1OutputVoltage,
       "imPM4Power1OutputCurrent": imPM4Power1OutputCurrent,
       "imPM4Power1OutputPowerVA": imPM4Power1OutputPowerVA,
       "imPM4Power1OutputPowerKVA": imPM4Power1OutputPowerKVA,
       "imPM4Power1OutputPowerW": imPM4Power1OutputPowerW,
       "imPM4Power1OutputPowerKW": imPM4Power1OutputPowerKW,
       "imPM4Power1OutputLoad": imPM4Power1OutputLoad,
       "imPM4Power1OutputFrequency": imPM4Power1OutputFrequency,
       "imPM4Power1Temperature": imPM4Power1Temperature,
       "imPM4Power1Running1": imPM4Power1Running1,
       "imPM4Power1Running2": imPM4Power1Running2,
       "imPM4Power1Running3": imPM4Power1Running3,
       "imPM4Power1Running4": imPM4Power1Running4,
       "imPM4Power1Running5": imPM4Power1Running5,
       "imPM4Power1Running6": imPM4Power1Running6,
       "imPM4Power1Running7": imPM4Power1Running7,
       "imPM4Power1Running8": imPM4Power1Running8,
       "imPM4Power1InputFuse": imPM4Power1InputFuse,
       "imPM4Power1InputFuse1": imPM4Power1InputFuse1,
       "imPM4Power1InputFuse2": imPM4Power1InputFuse2,
       "imPM4Power1InputFuse3": imPM4Power1InputFuse3,
       "imPM4Power1InputBreaker": imPM4Power1InputBreaker,
       "imPM4Power1InputBreaker1": imPM4Power1InputBreaker1,
       "imPM4Power1InputBreaker2": imPM4Power1InputBreaker2,
       "imPM4Power1InputBreaker3": imPM4Power1InputBreaker3,
       "imPM4Power1InputSurgeArrester": imPM4Power1InputSurgeArrester,
       "imPM4Power1OutputFuse": imPM4Power1OutputFuse,
       "imPM4Power1OutputFuse1": imPM4Power1OutputFuse1,
       "imPM4Power1OutputFuse2": imPM4Power1OutputFuse2,
       "imPM4Power1OutputBreaker": imPM4Power1OutputBreaker,
       "imPM4Power1OutputBreaker1": imPM4Power1OutputBreaker1,
       "imPM4Power1OutputBreaker2": imPM4Power1OutputBreaker2,
       "imPM4Power1Fan": imPM4Power1Fan,
       "imPM4Power1BatteryAvailable": imPM4Power1BatteryAvailable,
       "imPM4Power1OutputVoltagePhase1": imPM4Power1OutputVoltagePhase1,
       "imPM4Power1OutputCurrentPhase1": imPM4Power1OutputCurrentPhase1,
       "imPM4Power1OutputPowerVAphase1": imPM4Power1OutputPowerVAphase1,
       "imPM4Power1OutputPowerKVAphase1": imPM4Power1OutputPowerKVAphase1,
       "imPM4Power1OutputVoltagePhase2": imPM4Power1OutputVoltagePhase2,
       "imPM4Power1OutputCurrentPhase2": imPM4Power1OutputCurrentPhase2,
       "imPM4Power1OutputPowerVAphase2": imPM4Power1OutputPowerVAphase2,
       "imPM4Power1OutputPowerKVAphase2": imPM4Power1OutputPowerKVAphase2,
       "imPM4Power1OutputVoltagePhase3": imPM4Power1OutputVoltagePhase3,
       "imPM4Power1OutputCurrentPhase3": imPM4Power1OutputCurrentPhase3,
       "imPM4Power1OutputPowerVAphase3": imPM4Power1OutputPowerVAphase3,
       "imPM4Power1OutputPowerKVAphase3": imPM4Power1OutputPowerKVAphase3,
       "imPM4Power2": imPM4Power2,
       "imPM4Power2Manufacturer": imPM4Power2Manufacturer,
       "imPM4Power2Type": imPM4Power2Type,
       "imPM4Power2serNumb": imPM4Power2serNumb,
       "imPM4Power2nextServiceDate": imPM4Power2nextServiceDate,
       "imPM4Power2InputVoltage": imPM4Power2InputVoltage,
       "imPM4Power2InputCurrent": imPM4Power2InputCurrent,
       "imPM4Power2InputPowerVA": imPM4Power2InputPowerVA,
       "imPM4Power2InputPowerKVA": imPM4Power2InputPowerKVA,
       "imPM4Power2InputPowerW": imPM4Power2InputPowerW,
       "imPM4Power2InputPowerKW": imPM4Power2InputPowerKW,
       "imPM4Power2InputVoltagePhase1": imPM4Power2InputVoltagePhase1,
       "imPM4Power2InputCurrentPhase1": imPM4Power2InputCurrentPhase1,
       "imPM4Power2InputPowerVAphase1": imPM4Power2InputPowerVAphase1,
       "imPM4Power2InputPowerKVAphase1": imPM4Power2InputPowerKVAphase1,
       "imPM4Power2InputVoltagePhase2": imPM4Power2InputVoltagePhase2,
       "imPM4Power2InputCurrentPhase2": imPM4Power2InputCurrentPhase2,
       "imPM4Power2InputPowerVAphase2": imPM4Power2InputPowerVAphase2,
       "imPM4Power2InputPowerKVAphase2": imPM4Power2InputPowerKVAphase2,
       "imPM4Power2InputVoltagePhase3": imPM4Power2InputVoltagePhase3,
       "imPM4Power2InputCurrentPhase3": imPM4Power2InputCurrentPhase3,
       "imPM4Power2InputPowerVAphase3": imPM4Power2InputPowerVAphase3,
       "imPM4Power2InputPowerKVAphase3": imPM4Power2InputPowerKVAphase3,
       "imPM4Power2OutputVoltage": imPM4Power2OutputVoltage,
       "imPM4Power2OutputCurrent": imPM4Power2OutputCurrent,
       "imPM4Power2OutputPowerVA": imPM4Power2OutputPowerVA,
       "imPM4Power2OutputPowerKVA": imPM4Power2OutputPowerKVA,
       "imPM4Power2OutputPowerW": imPM4Power2OutputPowerW,
       "imPM4Power2OutputPowerKW": imPM4Power2OutputPowerKW,
       "imPM4Power2OutputLoad": imPM4Power2OutputLoad,
       "imPM4Power2OutputFrequency": imPM4Power2OutputFrequency,
       "imPM4Power2Temperature": imPM4Power2Temperature,
       "imPM4Power2Running1": imPM4Power2Running1,
       "imPM4Power2Running2": imPM4Power2Running2,
       "imPM4Power2Running3": imPM4Power2Running3,
       "imPM4Power2Running4": imPM4Power2Running4,
       "imPM4Power2Running5": imPM4Power2Running5,
       "imPM4Power2Running6": imPM4Power2Running6,
       "imPM4Power2Running7": imPM4Power2Running7,
       "imPM4Power2Running8": imPM4Power2Running8,
       "imPM4Power2InputFuse": imPM4Power2InputFuse,
       "imPM4Power2InputFuse1": imPM4Power2InputFuse1,
       "imPM4Power2InputFuse2": imPM4Power2InputFuse2,
       "imPM4Power2InputFuse3": imPM4Power2InputFuse3,
       "imPM4Power2InputBreaker": imPM4Power2InputBreaker,
       "imPM4Power2InputBreaker1": imPM4Power2InputBreaker1,
       "imPM4Power2InputBreaker2": imPM4Power2InputBreaker2,
       "imPM4Power2InputBreaker3": imPM4Power2InputBreaker3,
       "imPM4Power2InputSurgeArrester": imPM4Power2InputSurgeArrester,
       "imPM4Power2OutputFuse": imPM4Power2OutputFuse,
       "imPM4Power2OutputFuse1": imPM4Power2OutputFuse1,
       "imPM4Power2OutputFuse2": imPM4Power2OutputFuse2,
       "imPM4Power2OutputBreaker": imPM4Power2OutputBreaker,
       "imPM4Power2OutputBreaker1": imPM4Power2OutputBreaker1,
       "imPM4Power2OutputBreaker2": imPM4Power2OutputBreaker2,
       "imPM4Power2Fan": imPM4Power2Fan,
       "imPM4Power2BatteryAvailable": imPM4Power2BatteryAvailable,
       "imPM4Power2OutputVoltagePhase1": imPM4Power2OutputVoltagePhase1,
       "imPM4Power2OutputCurrentPhase1": imPM4Power2OutputCurrentPhase1,
       "imPM4Power2OutputPowerVAphase1": imPM4Power2OutputPowerVAphase1,
       "imPM4Power2OutputPowerKVAphase1": imPM4Power2OutputPowerKVAphase1,
       "imPM4Power2OutputVoltagePhase2": imPM4Power2OutputVoltagePhase2,
       "imPM4Power2OutputCurrentPhase2": imPM4Power2OutputCurrentPhase2,
       "imPM4Power2OutputPowerVAphase2": imPM4Power2OutputPowerVAphase2,
       "imPM4Power2OutputPowerKVAphase2": imPM4Power2OutputPowerKVAphase2,
       "imPM4Power2OutputVoltagePhase3": imPM4Power2OutputVoltagePhase3,
       "imPM4Power2OutputCurrentPhase3": imPM4Power2OutputCurrentPhase3,
       "imPM4Power2OutputPowerVAphase3": imPM4Power2OutputPowerVAphase3,
       "imPM4Power2OutputPowerKVAphase3": imPM4Power2OutputPowerKVAphase3,
       "imPM4Power3": imPM4Power3,
       "imPM4Power3Manufacturer": imPM4Power3Manufacturer,
       "imPM4Power3Type": imPM4Power3Type,
       "imPM4Power3serNumb": imPM4Power3serNumb,
       "imPM4Power3nextServiceDate": imPM4Power3nextServiceDate,
       "imPM4Power3InputVoltage": imPM4Power3InputVoltage,
       "imPM4Power3InputCurrent": imPM4Power3InputCurrent,
       "imPM4Power3InputPowerVA": imPM4Power3InputPowerVA,
       "imPM4Power3InputPowerKVA": imPM4Power3InputPowerKVA,
       "imPM4Power3InputPowerW": imPM4Power3InputPowerW,
       "imPM4Power3InputPowerKW": imPM4Power3InputPowerKW,
       "imPM4Power3InputVoltagePhase1": imPM4Power3InputVoltagePhase1,
       "imPM4Power3InputCurrentPhase1": imPM4Power3InputCurrentPhase1,
       "imPM4Power3InputPowerVAphase1": imPM4Power3InputPowerVAphase1,
       "imPM4Power3InputPowerKVAphase1": imPM4Power3InputPowerKVAphase1,
       "imPM4Power3InputVoltagePhase2": imPM4Power3InputVoltagePhase2,
       "imPM4Power3InputCurrentPhase2": imPM4Power3InputCurrentPhase2,
       "imPM4Power3InputPowerVAphase2": imPM4Power3InputPowerVAphase2,
       "imPM4Power3InputPowerKVAphase2": imPM4Power3InputPowerKVAphase2,
       "imPM4Power3InputVoltagePhase3": imPM4Power3InputVoltagePhase3,
       "imPM4Power3InputCurrentPhase3": imPM4Power3InputCurrentPhase3,
       "imPM4Power3InputPowerVAphase3": imPM4Power3InputPowerVAphase3,
       "imPM4Power3InputPowerKVAphase3": imPM4Power3InputPowerKVAphase3,
       "imPM4Power3OutputVoltage": imPM4Power3OutputVoltage,
       "imPM4Power3OutputCurrent": imPM4Power3OutputCurrent,
       "imPM4Power3OutputPowerVA": imPM4Power3OutputPowerVA,
       "imPM4Power3OutputPowerKVA": imPM4Power3OutputPowerKVA,
       "imPM4Power3OutputPowerW": imPM4Power3OutputPowerW,
       "imPM4Power3OutputPowerKW": imPM4Power3OutputPowerKW,
       "imPM4Power3OutputLoad": imPM4Power3OutputLoad,
       "imPM4Power3OutputFrequency": imPM4Power3OutputFrequency,
       "imPM4Power3Temperature": imPM4Power3Temperature,
       "imPM4Power3Running1": imPM4Power3Running1,
       "imPM4Power3Running2": imPM4Power3Running2,
       "imPM4Power3Running3": imPM4Power3Running3,
       "imPM4Power3Running4": imPM4Power3Running4,
       "imPM4Power3Running5": imPM4Power3Running5,
       "imPM4Power3Running6": imPM4Power3Running6,
       "imPM4Power3Running7": imPM4Power3Running7,
       "imPM4Power3Running8": imPM4Power3Running8,
       "imPM4Power3InputFuse": imPM4Power3InputFuse,
       "imPM4Power3InputFuse1": imPM4Power3InputFuse1,
       "imPM4Power3InputFuse2": imPM4Power3InputFuse2,
       "imPM4Power3InputFuse3": imPM4Power3InputFuse3,
       "imPM4Power3InputBreaker": imPM4Power3InputBreaker,
       "imPM4Power3InputBreaker1": imPM4Power3InputBreaker1,
       "imPM4Power3InputBreaker2": imPM4Power3InputBreaker2,
       "imPM4Power3InputBreaker3": imPM4Power3InputBreaker3,
       "imPM4Power3InputSurgeArrester": imPM4Power3InputSurgeArrester,
       "imPM4Power3OutputFuse": imPM4Power3OutputFuse,
       "imPM4Power3OutputFuse1": imPM4Power3OutputFuse1,
       "imPM4Power3OutputFuse2": imPM4Power3OutputFuse2,
       "imPM4Power3OutputBreaker": imPM4Power3OutputBreaker,
       "imPM4Power3OutputBreaker1": imPM4Power3OutputBreaker1,
       "imPM4Power3OutputBreaker2": imPM4Power3OutputBreaker2,
       "imPM4Power3Fan": imPM4Power3Fan,
       "imPM4Power3BatteryAvailable": imPM4Power3BatteryAvailable,
       "imPM4Power3OutputVoltagePhase1": imPM4Power3OutputVoltagePhase1,
       "imPM4Power3OutputCurrentPhase1": imPM4Power3OutputCurrentPhase1,
       "imPM4Power3OutputPowerVAphase1": imPM4Power3OutputPowerVAphase1,
       "imPM4Power3OutputPowerKVAphase1": imPM4Power3OutputPowerKVAphase1,
       "imPM4Power3OutputVoltagePhase2": imPM4Power3OutputVoltagePhase2,
       "imPM4Power3OutputCurrentPhase2": imPM4Power3OutputCurrentPhase2,
       "imPM4Power3OutputPowerVAphase2": imPM4Power3OutputPowerVAphase2,
       "imPM4Power3OutputPowerKVAphase2": imPM4Power3OutputPowerKVAphase2,
       "imPM4Power3OutputVoltagePhase3": imPM4Power3OutputVoltagePhase3,
       "imPM4Power3OutputCurrentPhase3": imPM4Power3OutputCurrentPhase3,
       "imPM4Power3OutputPowerVAphase3": imPM4Power3OutputPowerVAphase3,
       "imPM4Power3OutputPowerKVAphase3": imPM4Power3OutputPowerKVAphase3,
       "imPM4Battery": imPM4Battery,
       "imPM4BatteryNominalCapacity": imPM4BatteryNominalCapacity,
       "imPM4BatteryVoltage": imPM4BatteryVoltage,
       "imPM4BatteryCurrent": imPM4BatteryCurrent,
       "imPM4BatteryChargeState": imPM4BatteryChargeState,
       "imPM4BatteryAutonomyTime": imPM4BatteryAutonomyTime,
       "imPM4BatteryTimeOnBattery": imPM4BatteryTimeOnBattery,
       "imPM4BatLeg1": imPM4BatLeg1,
       "imPM4BatLeg1Manufacturer": imPM4BatLeg1Manufacturer,
       "imPM4BatLeg1Type": imPM4BatLeg1Type,
       "imPM4BatLeg1serNumb": imPM4BatLeg1serNumb,
       "imPM4BatLeg1nextServiceDate": imPM4BatLeg1nextServiceDate,
       "imPM4BatLeg1InstallationDate": imPM4BatLeg1InstallationDate,
       "imPM4BatLeg1NominalVoltage": imPM4BatLeg1NominalVoltage,
       "imPM4BatLeg1NominalCapacity": imPM4BatLeg1NominalCapacity,
       "imPM4BatLeg1Lifetime": imPM4BatLeg1Lifetime,
       "imPM4BatLeg1Voltage": imPM4BatLeg1Voltage,
       "imPM4BatLeg1Current": imPM4BatLeg1Current,
       "imPM4BatLeg1Temperature": imPM4BatLeg1Temperature,
       "imPM4BatLeg1ChargeState": imPM4BatLeg1ChargeState,
       "imPM4BatLeg1RestCapacity": imPM4BatLeg1RestCapacity,
       "imPM4BatLeg1Autonomytime": imPM4BatLeg1Autonomytime,
       "imPM4BatLeg1TimeOnBattery": imPM4BatLeg1TimeOnBattery,
       "imPM4BatLeg1Fuse": imPM4BatLeg1Fuse,
       "imPM4BatLeg1Breaker": imPM4BatLeg1Breaker,
       "imPM4BatLeg1LowVoltageDisconnect": imPM4BatLeg1LowVoltageDisconnect,
       "imPM4BatLeg2": imPM4BatLeg2,
       "imPM4BatLeg2Manufacturer": imPM4BatLeg2Manufacturer,
       "imPM4BatLeg2Type": imPM4BatLeg2Type,
       "imPM4BatLeg2serNumb": imPM4BatLeg2serNumb,
       "imPM4BatLeg2nextServiceDate": imPM4BatLeg2nextServiceDate,
       "imPM4BatLeg2InstallationDate": imPM4BatLeg2InstallationDate,
       "imPM4BatLeg2NominalVoltage": imPM4BatLeg2NominalVoltage,
       "imPM4BatLeg2NominalCapacity": imPM4BatLeg2NominalCapacity,
       "imPM4BatLeg2Lifetime": imPM4BatLeg2Lifetime,
       "imPM4BatLeg2Voltage": imPM4BatLeg2Voltage,
       "imPM4BatLeg2Current": imPM4BatLeg2Current,
       "imPM4BatLeg2Temperature": imPM4BatLeg2Temperature,
       "imPM4BatLeg2ChargeState": imPM4BatLeg2ChargeState,
       "imPM4BatLeg2RestCapacity": imPM4BatLeg2RestCapacity,
       "imPM4BatLeg2Autonomytime": imPM4BatLeg2Autonomytime,
       "imPM4BatLeg2TimeOnBattery": imPM4BatLeg2TimeOnBattery,
       "imPM4BatLeg2Fuse": imPM4BatLeg2Fuse,
       "imPM4BatLeg2Breaker": imPM4BatLeg2Breaker,
       "imPM4BatLeg2LowVoltageDisconnect": imPM4BatLeg2LowVoltageDisconnect,
       "imPM4BatLeg3": imPM4BatLeg3,
       "imPM4BatLeg3Manufacturer": imPM4BatLeg3Manufacturer,
       "imPM4BatLeg3Type": imPM4BatLeg3Type,
       "imPM4BatLeg3serNumb": imPM4BatLeg3serNumb,
       "imPM4BatLeg3nextServiceDate": imPM4BatLeg3nextServiceDate,
       "imPM4BatLeg3InstallationDate": imPM4BatLeg3InstallationDate,
       "imPM4BatLeg3NominalVoltage": imPM4BatLeg3NominalVoltage,
       "imPM4BatLeg3NominalCapacity": imPM4BatLeg3NominalCapacity,
       "imPM4BatLeg3Lifetime": imPM4BatLeg3Lifetime,
       "imPM4BatLeg3Voltage": imPM4BatLeg3Voltage,
       "imPM4BatLeg3Current": imPM4BatLeg3Current,
       "imPM4BatLeg3Temperature": imPM4BatLeg3Temperature,
       "imPM4BatLeg3ChargeState": imPM4BatLeg3ChargeState,
       "imPM4BatLeg3RestCapacity": imPM4BatLeg3RestCapacity,
       "imPM4BatLeg3Autonomytime": imPM4BatLeg3Autonomytime,
       "imPM4BatLeg3TimeOnBattery": imPM4BatLeg3TimeOnBattery,
       "imPM4BatLeg3Fuse": imPM4BatLeg3Fuse,
       "imPM4BatLeg3Breaker": imPM4BatLeg3Breaker,
       "imPM4BatLeg3LowVoltageDisconnect": imPM4BatLeg3LowVoltageDisconnect,
       "imPM4Distrib": imPM4Distrib,
       "imPm4Distrib": imPm4Distrib,
       "imPM4DistTable": imPM4DistTable,
       "imPM4DistEntry": imPM4DistEntry,
       "imPM4DistId": imPM4DistId,
       "imPM4DistFuse": imPM4DistFuse,
       "imPM4DistBreaker": imPM4DistBreaker,
       "imPM4Control": imPM4Control,
       "imPM4ContTable": imPM4ContTable,
       "imPM4ContEntry": imPM4ContEntry,
       "imPM4ContId": imPM4ContId,
       "imPM4ContState": imPM4ContState,
       "imPM4ContLabel": imPM4ContLabel,
       "imPM4ContTimeOFF": imPM4ContTimeOFF,
       "imPM4ContAuto": imPM4ContAuto,
       "imPM4ContTestCAPcommand": imPM4ContTestCAPcommand,
       "imPM4ContTestCAPvoltage": imPM4ContTestCAPvoltage,
       "imPM4ContTestCAPcurrent": imPM4ContTestCAPcurrent,
       "imPM4ContTestCAPtemperature": imPM4ContTestCAPtemperature,
       "imPM4ContTestCAPduration": imPM4ContTestCAPduration,
       "imPM4ContTestCAPstatus": imPM4ContTestCAPstatus,
       "imco3Alarm": imco3Alarm,
       "imco3AlarmsPresent": imco3AlarmsPresent,
       "imco3AlarmTable": imco3AlarmTable,
       "imco3AlarmEntry": imco3AlarmEntry,
       "imco3AlarmId": imco3AlarmId,
       "imco3AlarmDescr": imco3AlarmDescr,
       "imco3AlarmTime": imco3AlarmTime,
       "imco3AlarmPMnumber": imco3AlarmPMnumber,
       "imco3Traps": imco3Traps,
       "imco3TrapNoDevice": imco3TrapNoDevice,
       "imco3TrapOnBattery": imco3TrapOnBattery,
       "imco3TrapNewAlarm": imco3TrapNewAlarm,
       "imco3TrapAlarmEnd": imco3TrapAlarmEnd,
       "imco3TrapAlarmOut1ON": imco3TrapAlarmOut1ON,
       "imco3TrapAlarmOut2ON": imco3TrapAlarmOut2ON,
       "imco3TrapAlarmOut3ON": imco3TrapAlarmOut3ON,
       "imco3TrapAlarmOut4ON": imco3TrapAlarmOut4ON,
       "imco3TrapAlarmOut5ON": imco3TrapAlarmOut5ON,
       "imco3TrapAlarmOut6ON": imco3TrapAlarmOut6ON,
       "imco3TrapAlarmOut7ON": imco3TrapAlarmOut7ON,
       "imco3TrapAlarmOut8ON": imco3TrapAlarmOut8ON,
       "imco3TrapAlarmOut1OFF": imco3TrapAlarmOut1OFF,
       "imco3TrapAlarmOut2OFF": imco3TrapAlarmOut2OFF,
       "imco3TrapAlarmOut3OFF": imco3TrapAlarmOut3OFF,
       "imco3TrapAlarmOut4OFF": imco3TrapAlarmOut4OFF,
       "imco3TrapAlarmOut5OFF": imco3TrapAlarmOut5OFF,
       "imco3TrapAlarmOut6OFF": imco3TrapAlarmOut6OFF,
       "imco3TrapAlarmOut7OFF": imco3TrapAlarmOut7OFF,
       "imco3TrapAlarmOut8OFF": imco3TrapAlarmOut8OFF,
       "imco3TrapTestCAPstart": imco3TrapTestCAPstart,
       "imco3TrapTestCAPstop": imco3TrapTestCAPstop,
       "npProducts": npProducts}
)
