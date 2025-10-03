# SNMP MIB module (PANDUIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\panduit\PANDUIT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:23 2025
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

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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

g5 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10)
)
if mibBuilder.loadTexts:
    g5.setRevisions(
        ("2023-07-24 12:00",
         "2023-06-27 12:00",
         "2023-03-13 12:00",
         "2023-02-13 12:00",
         "2022-12-15 12:00",
         "2022-10-17 12:00",
         "2022-07-12 12:00",
         "2022-02-04 12:00",
         "2021-02-02 12:00",
         "2020-06-30 12:00",
         "2020-03-30 12:00",
         "2019-02-12 12:00",
         "2018-01-12 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Panduit_ObjectIdentity = ObjectIdentity
panduit = _Panduit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536)
)
_Pdug5_ObjectIdentity = ObjectIdentity
pdug5 = _Pdug5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1)
)
_Pdug5Ident_ObjectIdentity = ObjectIdentity
pdug5Ident = _Pdug5Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1)
)


class _Pdug5NumberPDU_Type(Integer32):
    """Custom type pdug5NumberPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Pdug5NumberPDU_Type.__name__ = "Integer32"
_Pdug5NumberPDU_Object = MibScalar
pdug5NumberPDU = _Pdug5NumberPDU_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 1),
    _Pdug5NumberPDU_Type()
)
pdug5NumberPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5NumberPDU.setStatus("current")
_Pdug5IdentTable_Object = MibTable
pdug5IdentTable = _Pdug5IdentTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdug5IdentTable.setStatus("current")
_Pdug5IdentEntry_Object = MibTableRow
pdug5IdentEntry = _Pdug5IdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1)
)
pdug5IdentEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
)
if mibBuilder.loadTexts:
    pdug5IdentEntry.setStatus("current")


class _Pdug5IdentIndex_Type(Integer32):
    """Custom type pdug5IdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Pdug5IdentIndex_Type.__name__ = "Integer32"
_Pdug5IdentIndex_Object = MibTableColumn
pdug5IdentIndex = _Pdug5IdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 1),
    _Pdug5IdentIndex_Type()
)
pdug5IdentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5IdentIndex.setStatus("current")


class _Pdug5Name_Type(DisplayString):
    """Custom type pdug5Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdug5Name_Type.__name__ = "DisplayString"
_Pdug5Name_Object = MibTableColumn
pdug5Name = _Pdug5Name_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 2),
    _Pdug5Name_Type()
)
pdug5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5Name.setStatus("current")


class _Pdug5Model_Type(DisplayString):
    """Custom type pdug5Model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdug5Model_Type.__name__ = "DisplayString"
_Pdug5Model_Object = MibTableColumn
pdug5Model = _Pdug5Model_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 3),
    _Pdug5Model_Type()
)
pdug5Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5Model.setStatus("current")


class _Pdug5Manufacturer_Type(DisplayString):
    """Custom type pdug5Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdug5Manufacturer_Type.__name__ = "DisplayString"
_Pdug5Manufacturer_Object = MibTableColumn
pdug5Manufacturer = _Pdug5Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 4),
    _Pdug5Manufacturer_Type()
)
pdug5Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5Manufacturer.setStatus("current")


class _Pdug5FirmwareVersion_Type(DisplayString):
    """Custom type pdug5FirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdug5FirmwareVersion_Type.__name__ = "DisplayString"
_Pdug5FirmwareVersion_Object = MibTableColumn
pdug5FirmwareVersion = _Pdug5FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 5),
    _Pdug5FirmwareVersion_Type()
)
pdug5FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5FirmwareVersion.setStatus("current")
_Pdug5FirmwareVersionTimeStamp_Type = DisplayString
_Pdug5FirmwareVersionTimeStamp_Object = MibTableColumn
pdug5FirmwareVersionTimeStamp = _Pdug5FirmwareVersionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 6),
    _Pdug5FirmwareVersionTimeStamp_Type()
)
pdug5FirmwareVersionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5FirmwareVersionTimeStamp.setStatus("current")


class _Pdug5PartNumber_Type(DisplayString):
    """Custom type pdug5PartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdug5PartNumber_Type.__name__ = "DisplayString"
_Pdug5PartNumber_Object = MibTableColumn
pdug5PartNumber = _Pdug5PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 7),
    _Pdug5PartNumber_Type()
)
pdug5PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5PartNumber.setStatus("current")


class _Pdug5SerialNumber_Type(DisplayString):
    """Custom type pdug5SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdug5SerialNumber_Type.__name__ = "DisplayString"
_Pdug5SerialNumber_Object = MibTableColumn
pdug5SerialNumber = _Pdug5SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 8),
    _Pdug5SerialNumber_Type()
)
pdug5SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5SerialNumber.setStatus("current")


class _Pdug5Status_Type(Integer32):
    """Custom type pdug5Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_Pdug5Status_Type.__name__ = "Integer32"
_Pdug5Status_Object = MibTableColumn
pdug5Status = _Pdug5Status_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 9),
    _Pdug5Status_Type()
)
pdug5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5Status.setStatus("current")


class _Pdug5Controllable_Type(Integer32):
    """Custom type pdug5Controllable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Pdug5Controllable_Type.__name__ = "Integer32"
_Pdug5Controllable_Object = MibTableColumn
pdug5Controllable = _Pdug5Controllable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 10),
    _Pdug5Controllable_Type()
)
pdug5Controllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5Controllable.setStatus("current")


class _Pdug5InputPhaseCount_Type(Integer32):
    """Custom type pdug5InputPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdug5InputPhaseCount_Type.__name__ = "Integer32"
_Pdug5InputPhaseCount_Object = MibTableColumn
pdug5InputPhaseCount = _Pdug5InputPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 11),
    _Pdug5InputPhaseCount_Type()
)
pdug5InputPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseCount.setStatus("current")


class _Pdug5GroupCount_Type(Integer32):
    """Custom type pdug5GroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Pdug5GroupCount_Type.__name__ = "Integer32"
_Pdug5GroupCount_Object = MibTableColumn
pdug5GroupCount = _Pdug5GroupCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 12),
    _Pdug5GroupCount_Type()
)
pdug5GroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupCount.setStatus("current")


class _Pdug5OutletCount_Type(Integer32):
    """Custom type pdug5OutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_Pdug5OutletCount_Type.__name__ = "Integer32"
_Pdug5OutletCount_Object = MibTableColumn
pdug5OutletCount = _Pdug5OutletCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 13),
    _Pdug5OutletCount_Type()
)
pdug5OutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletCount.setStatus("current")
_Pdug5MACAddress_Type = DisplayString
_Pdug5MACAddress_Object = MibTableColumn
pdug5MACAddress = _Pdug5MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 14),
    _Pdug5MACAddress_Type()
)
pdug5MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5MACAddress.setStatus("current")
_Pdug5IPv4Address_Type = IpAddress
_Pdug5IPv4Address_Object = MibTableColumn
pdug5IPv4Address = _Pdug5IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 15),
    _Pdug5IPv4Address_Type()
)
pdug5IPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5IPv4Address.setStatus("current")
_Pdug5IPv6Address_Type = DisplayString
_Pdug5IPv6Address_Object = MibTableColumn
pdug5IPv6Address = _Pdug5IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 16),
    _Pdug5IPv6Address_Type()
)
pdug5IPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5IPv6Address.setStatus("current")
_Pdug5HWVersion_Type = DisplayString
_Pdug5HWVersion_Object = MibTableColumn
pdug5HWVersion = _Pdug5HWVersion_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 2, 1, 17),
    _Pdug5HWVersion_Type()
)
pdug5HWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5HWVersion.setStatus("current")
_Pdug5ConfigTable_Object = MibTable
pdug5ConfigTable = _Pdug5ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pdug5ConfigTable.setStatus("current")
_Pdug5ConfigEntry_Object = MibTableRow
pdug5ConfigEntry = _Pdug5ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1)
)
pdug5ConfigEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5ConfigIndex"),
)
if mibBuilder.loadTexts:
    pdug5ConfigEntry.setStatus("current")


class _Pdug5ConfigIndex_Type(Integer32):
    """Custom type pdug5ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Pdug5ConfigIndex_Type.__name__ = "Integer32"
_Pdug5ConfigIndex_Object = MibTableColumn
pdug5ConfigIndex = _Pdug5ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 1),
    _Pdug5ConfigIndex_Type()
)
pdug5ConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5ConfigIndex.setStatus("current")


class _Pdug5ConfigSsh_Type(Integer32):
    """Custom type pdug5ConfigSsh based on Integer32"""
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


_Pdug5ConfigSsh_Type.__name__ = "Integer32"
_Pdug5ConfigSsh_Object = MibTableColumn
pdug5ConfigSsh = _Pdug5ConfigSsh_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 2),
    _Pdug5ConfigSsh_Type()
)
pdug5ConfigSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigSsh.setStatus("current")


class _Pdug5ConfigFtps_Type(Integer32):
    """Custom type pdug5ConfigFtps based on Integer32"""
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


_Pdug5ConfigFtps_Type.__name__ = "Integer32"
_Pdug5ConfigFtps_Object = MibTableColumn
pdug5ConfigFtps = _Pdug5ConfigFtps_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 3),
    _Pdug5ConfigFtps_Type()
)
pdug5ConfigFtps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigFtps.setStatus("current")


class _Pdug5ConfigHttp_Type(Integer32):
    """Custom type pdug5ConfigHttp based on Integer32"""
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


_Pdug5ConfigHttp_Type.__name__ = "Integer32"
_Pdug5ConfigHttp_Object = MibTableColumn
pdug5ConfigHttp = _Pdug5ConfigHttp_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 4),
    _Pdug5ConfigHttp_Type()
)
pdug5ConfigHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigHttp.setStatus("current")


class _Pdug5ConfigHttps_Type(Integer32):
    """Custom type pdug5ConfigHttps based on Integer32"""
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


_Pdug5ConfigHttps_Type.__name__ = "Integer32"
_Pdug5ConfigHttps_Object = MibTableColumn
pdug5ConfigHttps = _Pdug5ConfigHttps_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 5),
    _Pdug5ConfigHttps_Type()
)
pdug5ConfigHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigHttps.setStatus("current")


class _Pdug5ConfigIPv4IPv6Switch_Type(Integer32):
    """Custom type pdug5ConfigIPv4IPv6Switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 1),
          ("iPv6", 2),
          ("iPv4IPv6", 3))
    )


_Pdug5ConfigIPv4IPv6Switch_Type.__name__ = "Integer32"
_Pdug5ConfigIPv4IPv6Switch_Object = MibTableColumn
pdug5ConfigIPv4IPv6Switch = _Pdug5ConfigIPv4IPv6Switch_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 6),
    _Pdug5ConfigIPv4IPv6Switch_Type()
)
pdug5ConfigIPv4IPv6Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigIPv4IPv6Switch.setStatus("current")


class _Pdug5ConfigRedfishAPI_Type(Integer32):
    """Custom type pdug5ConfigRedfishAPI based on Integer32"""
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


_Pdug5ConfigRedfishAPI_Type.__name__ = "Integer32"
_Pdug5ConfigRedfishAPI_Object = MibTableColumn
pdug5ConfigRedfishAPI = _Pdug5ConfigRedfishAPI_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 7),
    _Pdug5ConfigRedfishAPI_Type()
)
pdug5ConfigRedfishAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigRedfishAPI.setStatus("current")


class _Pdug5ConfigOledDispalyOrientation_Type(Integer32):
    """Custom type pdug5ConfigOledDispalyOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("displayNormal", 1),
          ("displayReverse", 2))
    )


_Pdug5ConfigOledDispalyOrientation_Type.__name__ = "Integer32"
_Pdug5ConfigOledDispalyOrientation_Object = MibTableColumn
pdug5ConfigOledDispalyOrientation = _Pdug5ConfigOledDispalyOrientation_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 8),
    _Pdug5ConfigOledDispalyOrientation_Type()
)
pdug5ConfigOledDispalyOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigOledDispalyOrientation.setStatus("current")


class _Pdug5ConfigEnergyReset_Type(Integer32):
    """Custom type pdug5ConfigEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2),
          ("notSupported", 3))
    )


_Pdug5ConfigEnergyReset_Type.__name__ = "Integer32"
_Pdug5ConfigEnergyReset_Object = MibTableColumn
pdug5ConfigEnergyReset = _Pdug5ConfigEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 9),
    _Pdug5ConfigEnergyReset_Type()
)
pdug5ConfigEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigEnergyReset.setStatus("current")


class _Pdug5ConfigNetworkManagementCardReset_Type(Integer32):
    """Custom type pdug5ConfigNetworkManagementCardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("reset", 1))
    )


_Pdug5ConfigNetworkManagementCardReset_Type.__name__ = "Integer32"
_Pdug5ConfigNetworkManagementCardReset_Object = MibTableColumn
pdug5ConfigNetworkManagementCardReset = _Pdug5ConfigNetworkManagementCardReset_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 10),
    _Pdug5ConfigNetworkManagementCardReset_Type()
)
pdug5ConfigNetworkManagementCardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigNetworkManagementCardReset.setStatus("current")


class _Pdug5ConfigDaisyChainStatus_Type(Integer32):
    """Custom type pdug5ConfigDaisyChainStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("daisychain", 0),
          ("rna", 1))
    )


_Pdug5ConfigDaisyChainStatus_Type.__name__ = "Integer32"
_Pdug5ConfigDaisyChainStatus_Object = MibTableColumn
pdug5ConfigDaisyChainStatus = _Pdug5ConfigDaisyChainStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 3, 1, 11),
    _Pdug5ConfigDaisyChainStatus_Type()
)
pdug5ConfigDaisyChainStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5ConfigDaisyChainStatus.setStatus("current")
_Pdug5PowershareTable_Object = MibTable
pdug5PowershareTable = _Pdug5PowershareTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pdug5PowershareTable.setStatus("current")
_Pdug5PowershareEntry_Object = MibTableRow
pdug5PowershareEntry = _Pdug5PowershareEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4, 1)
)
pdug5PowershareEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5PowershareIndex"),
)
if mibBuilder.loadTexts:
    pdug5PowershareEntry.setStatus("current")


class _Pdug5PowershareIndex_Type(Integer32):
    """Custom type pdug5PowershareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Pdug5PowershareIndex_Type.__name__ = "Integer32"
_Pdug5PowershareIndex_Object = MibTableColumn
pdug5PowershareIndex = _Pdug5PowershareIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4, 1, 1),
    _Pdug5PowershareIndex_Type()
)
pdug5PowershareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5PowershareIndex.setStatus("current")


class _Pdug5PowershareFunctionStatus_Type(Integer32):
    """Custom type pdug5PowershareFunctionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("available", 1))
    )


_Pdug5PowershareFunctionStatus_Type.__name__ = "Integer32"
_Pdug5PowershareFunctionStatus_Object = MibTableColumn
pdug5PowershareFunctionStatus = _Pdug5PowershareFunctionStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4, 1, 2),
    _Pdug5PowershareFunctionStatus_Type()
)
pdug5PowershareFunctionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5PowershareFunctionStatus.setStatus("current")


class _Pdug5PowershareFunctionUpstreamStatus_Type(Integer32):
    """Custom type pdug5PowershareFunctionUpstreamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("available", 1))
    )


_Pdug5PowershareFunctionUpstreamStatus_Type.__name__ = "Integer32"
_Pdug5PowershareFunctionUpstreamStatus_Object = MibTableColumn
pdug5PowershareFunctionUpstreamStatus = _Pdug5PowershareFunctionUpstreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4, 1, 3),
    _Pdug5PowershareFunctionUpstreamStatus_Type()
)
pdug5PowershareFunctionUpstreamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5PowershareFunctionUpstreamStatus.setStatus("current")


class _Pdug5PowershareOutput_Type(Integer32):
    """Custom type pdug5PowershareOutput based on Integer32"""
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


_Pdug5PowershareOutput_Type.__name__ = "Integer32"
_Pdug5PowershareOutput_Object = MibTableColumn
pdug5PowershareOutput = _Pdug5PowershareOutput_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4, 1, 4),
    _Pdug5PowershareOutput_Type()
)
pdug5PowershareOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5PowershareOutput.setStatus("current")


class _Pdug5PowershareInput_Type(Integer32):
    """Custom type pdug5PowershareInput based on Integer32"""
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


_Pdug5PowershareInput_Type.__name__ = "Integer32"
_Pdug5PowershareInput_Object = MibTableColumn
pdug5PowershareInput = _Pdug5PowershareInput_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4, 1, 5),
    _Pdug5PowershareInput_Type()
)
pdug5PowershareInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5PowershareInput.setStatus("current")


class _Pdug5PowershareOptMode_Type(Integer32):
    """Custom type pdug5PowershareOptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("powerByPowershare", 0),
          ("powerByMains", 1))
    )


_Pdug5PowershareOptMode_Type.__name__ = "Integer32"
_Pdug5PowershareOptMode_Object = MibTableColumn
pdug5PowershareOptMode = _Pdug5PowershareOptMode_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4, 1, 6),
    _Pdug5PowershareOptMode_Type()
)
pdug5PowershareOptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5PowershareOptMode.setStatus("current")


class _Pdug5PowershareFunc_Type(Integer32):
    """Custom type pdug5PowershareFunc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disablePowershare", 0),
          ("enablePowershare", 1))
    )


_Pdug5PowershareFunc_Type.__name__ = "Integer32"
_Pdug5PowershareFunc_Object = MibTableColumn
pdug5PowershareFunc = _Pdug5PowershareFunc_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 1, 4, 1, 7),
    _Pdug5PowershareFunc_Type()
)
pdug5PowershareFunc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5PowershareFunc.setStatus("current")
_Pdug5Input_ObjectIdentity = ObjectIdentity
pdug5Input = _Pdug5Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2)
)
_Pdug5InputTable_Object = MibTable
pdug5InputTable = _Pdug5InputTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdug5InputTable.setStatus("current")
_Pdug5InputEntry_Object = MibTableRow
pdug5InputEntry = _Pdug5InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1)
)
pdug5InputEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
)
if mibBuilder.loadTexts:
    pdug5InputEntry.setStatus("current")


class _Pdug5InputType_Type(Integer32):
    """Custom type pdug5InputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("splitPhase", 2),
          ("threePhaseDelta", 3),
          ("threePhaseWye", 4))
    )


_Pdug5InputType_Type.__name__ = "Integer32"
_Pdug5InputType_Object = MibTableColumn
pdug5InputType = _Pdug5InputType_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 1),
    _Pdug5InputType_Type()
)
pdug5InputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputType.setStatus("current")


class _Pdug5InputFrequency_Type(Integer32):
    """Custom type pdug5InputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Pdug5InputFrequency_Type.__name__ = "Integer32"
_Pdug5InputFrequency_Object = MibTableColumn
pdug5InputFrequency = _Pdug5InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 2),
    _Pdug5InputFrequency_Type()
)
pdug5InputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputFrequency.setStatus("current")


class _Pdug5InputFrequencyStatus_Type(Integer32):
    """Custom type pdug5InputFrequencyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("outOfRange", 2))
    )


_Pdug5InputFrequencyStatus_Type.__name__ = "Integer32"
_Pdug5InputFrequencyStatus_Object = MibTableColumn
pdug5InputFrequencyStatus = _Pdug5InputFrequencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 3),
    _Pdug5InputFrequencyStatus_Type()
)
pdug5InputFrequencyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputFrequencyStatus.setStatus("current")
_Pdug5InputPowerVA_Type = Integer32
_Pdug5InputPowerVA_Object = MibTableColumn
pdug5InputPowerVA = _Pdug5InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 4),
    _Pdug5InputPowerVA_Type()
)
pdug5InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPowerVA.setStatus("current")
_Pdug5InputPowerWatts_Type = Integer32
_Pdug5InputPowerWatts_Object = MibTableColumn
pdug5InputPowerWatts = _Pdug5InputPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 5),
    _Pdug5InputPowerWatts_Type()
)
pdug5InputPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPowerWatts.setStatus("current")
_Pdug5InputTotalEnergy_Type = Integer32
_Pdug5InputTotalEnergy_Object = MibTableColumn
pdug5InputTotalEnergy = _Pdug5InputTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 6),
    _Pdug5InputTotalEnergy_Type()
)
pdug5InputTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputTotalEnergy.setStatus("current")


class _Pdug5InputPowerWattHourTimer_Type(DisplayString):
    """Custom type pdug5InputPowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdug5InputPowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdug5InputPowerWattHourTimer_Object = MibTableColumn
pdug5InputPowerWattHourTimer = _Pdug5InputPowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 7),
    _Pdug5InputPowerWattHourTimer_Type()
)
pdug5InputPowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPowerWattHourTimer.setStatus("current")
_Pdug5InputResettableEnergy_Type = Integer32
_Pdug5InputResettableEnergy_Object = MibTableColumn
pdug5InputResettableEnergy = _Pdug5InputResettableEnergy_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 8),
    _Pdug5InputResettableEnergy_Type()
)
pdug5InputResettableEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputResettableEnergy.setStatus("current")
_Pdug5InputPowerFactor_Type = Integer32
_Pdug5InputPowerFactor_Object = MibTableColumn
pdug5InputPowerFactor = _Pdug5InputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 9),
    _Pdug5InputPowerFactor_Type()
)
pdug5InputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPowerFactor.setStatus("current")
_Pdug5InputPowerVAR_Type = Integer32
_Pdug5InputPowerVAR_Object = MibTableColumn
pdug5InputPowerVAR = _Pdug5InputPowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 10),
    _Pdug5InputPowerVAR_Type()
)
pdug5InputPowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPowerVAR.setStatus("current")
_Pdug5InputTotalCurrent_Type = Integer32
_Pdug5InputTotalCurrent_Object = MibTableColumn
pdug5InputTotalCurrent = _Pdug5InputTotalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 1, 1, 11),
    _Pdug5InputTotalCurrent_Type()
)
pdug5InputTotalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputTotalCurrent.setStatus("current")
_Pdug5InputPhaseTable_Object = MibTable
pdug5InputPhaseTable = _Pdug5InputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pdug5InputPhaseTable.setStatus("current")
_Pdug5InputPhaseEntry_Object = MibTableRow
pdug5InputPhaseEntry = _Pdug5InputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1)
)
pdug5InputPhaseEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5InputPhaseIndex"),
)
if mibBuilder.loadTexts:
    pdug5InputPhaseEntry.setStatus("current")


class _Pdug5InputPhaseIndex_Type(Integer32):
    """Custom type pdug5InputPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdug5InputPhaseIndex_Type.__name__ = "Integer32"
_Pdug5InputPhaseIndex_Object = MibTableColumn
pdug5InputPhaseIndex = _Pdug5InputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 1),
    _Pdug5InputPhaseIndex_Type()
)
pdug5InputPhaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5InputPhaseIndex.setStatus("current")


class _Pdug5InputPhaseVoltageMeasType_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("phase1toN", 2),
          ("phase2toN", 3),
          ("phase3toN", 4),
          ("phase1to2", 5),
          ("phase2to3", 6),
          ("phase3to1", 7))
    )


_Pdug5InputPhaseVoltageMeasType_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageMeasType_Object = MibTableColumn
pdug5InputPhaseVoltageMeasType = _Pdug5InputPhaseVoltageMeasType_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 2),
    _Pdug5InputPhaseVoltageMeasType_Type()
)
pdug5InputPhaseVoltageMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageMeasType.setStatus("current")
_Pdug5InputPhaseVoltage_Type = Integer32
_Pdug5InputPhaseVoltage_Object = MibTableColumn
pdug5InputPhaseVoltage = _Pdug5InputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 3),
    _Pdug5InputPhaseVoltage_Type()
)
pdug5InputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltage.setStatus("current")


class _Pdug5InputPhaseVoltageThStatus_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdug5InputPhaseVoltageThStatus_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageThStatus_Object = MibTableColumn
pdug5InputPhaseVoltageThStatus = _Pdug5InputPhaseVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 4),
    _Pdug5InputPhaseVoltageThStatus_Type()
)
pdug5InputPhaseVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageThStatus.setStatus("current")


class _Pdug5InputPhaseVoltageThLowerWarning_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputPhaseVoltageThLowerWarning_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageThLowerWarning_Object = MibTableColumn
pdug5InputPhaseVoltageThLowerWarning = _Pdug5InputPhaseVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 5),
    _Pdug5InputPhaseVoltageThLowerWarning_Type()
)
pdug5InputPhaseVoltageThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageThLowerWarning.setStatus("current")


class _Pdug5InputPhaseVoltageThLowerCritical_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputPhaseVoltageThLowerCritical_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageThLowerCritical_Object = MibTableColumn
pdug5InputPhaseVoltageThLowerCritical = _Pdug5InputPhaseVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 6),
    _Pdug5InputPhaseVoltageThLowerCritical_Type()
)
pdug5InputPhaseVoltageThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageThLowerCritical.setStatus("current")


class _Pdug5InputPhaseVoltageThUpperWarning_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputPhaseVoltageThUpperWarning_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageThUpperWarning_Object = MibTableColumn
pdug5InputPhaseVoltageThUpperWarning = _Pdug5InputPhaseVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 7),
    _Pdug5InputPhaseVoltageThUpperWarning_Type()
)
pdug5InputPhaseVoltageThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageThUpperWarning.setStatus("current")


class _Pdug5InputPhaseVoltageThUpperCritical_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputPhaseVoltageThUpperCritical_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageThUpperCritical_Object = MibTableColumn
pdug5InputPhaseVoltageThUpperCritical = _Pdug5InputPhaseVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 8),
    _Pdug5InputPhaseVoltageThUpperCritical_Type()
)
pdug5InputPhaseVoltageThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageThUpperCritical.setStatus("current")


class _Pdug5InputPhaseCurrentMeasType_Type(Integer32):
    """Custom type pdug5InputPhaseCurrentMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("neutral", 2),
          ("phase1", 3),
          ("phase2", 4),
          ("phase3", 5))
    )


_Pdug5InputPhaseCurrentMeasType_Type.__name__ = "Integer32"
_Pdug5InputPhaseCurrentMeasType_Object = MibTableColumn
pdug5InputPhaseCurrentMeasType = _Pdug5InputPhaseCurrentMeasType_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 9),
    _Pdug5InputPhaseCurrentMeasType_Type()
)
pdug5InputPhaseCurrentMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentMeasType.setStatus("current")
_Pdug5InputPhaseCurrentRating_Type = Integer32
_Pdug5InputPhaseCurrentRating_Object = MibTableColumn
pdug5InputPhaseCurrentRating = _Pdug5InputPhaseCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 10),
    _Pdug5InputPhaseCurrentRating_Type()
)
pdug5InputPhaseCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentRating.setStatus("current")
_Pdug5InputPhaseCurrent_Type = Integer32
_Pdug5InputPhaseCurrent_Object = MibTableColumn
pdug5InputPhaseCurrent = _Pdug5InputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 11),
    _Pdug5InputPhaseCurrent_Type()
)
pdug5InputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrent.setStatus("current")


class _Pdug5InputPhaseCurrentThStatus_Type(Integer32):
    """Custom type pdug5InputPhaseCurrentThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdug5InputPhaseCurrentThStatus_Type.__name__ = "Integer32"
_Pdug5InputPhaseCurrentThStatus_Object = MibTableColumn
pdug5InputPhaseCurrentThStatus = _Pdug5InputPhaseCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 12),
    _Pdug5InputPhaseCurrentThStatus_Type()
)
pdug5InputPhaseCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentThStatus.setStatus("current")


class _Pdug5InputPhaseCurrentThLowerWarning_Type(Integer32):
    """Custom type pdug5InputPhaseCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdug5InputPhaseCurrentThLowerWarning_Type.__name__ = "Integer32"
_Pdug5InputPhaseCurrentThLowerWarning_Object = MibTableColumn
pdug5InputPhaseCurrentThLowerWarning = _Pdug5InputPhaseCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 13),
    _Pdug5InputPhaseCurrentThLowerWarning_Type()
)
pdug5InputPhaseCurrentThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentThLowerWarning.setStatus("current")


class _Pdug5InputPhaseCurrentThLowerCritical_Type(Integer32):
    """Custom type pdug5InputPhaseCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdug5InputPhaseCurrentThLowerCritical_Type.__name__ = "Integer32"
_Pdug5InputPhaseCurrentThLowerCritical_Object = MibTableColumn
pdug5InputPhaseCurrentThLowerCritical = _Pdug5InputPhaseCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 14),
    _Pdug5InputPhaseCurrentThLowerCritical_Type()
)
pdug5InputPhaseCurrentThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentThLowerCritical.setStatus("current")


class _Pdug5InputPhaseCurrentThUpperWarning_Type(Integer32):
    """Custom type pdug5InputPhaseCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdug5InputPhaseCurrentThUpperWarning_Type.__name__ = "Integer32"
_Pdug5InputPhaseCurrentThUpperWarning_Object = MibTableColumn
pdug5InputPhaseCurrentThUpperWarning = _Pdug5InputPhaseCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 15),
    _Pdug5InputPhaseCurrentThUpperWarning_Type()
)
pdug5InputPhaseCurrentThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentThUpperWarning.setStatus("current")


class _Pdug5InputPhaseCurrentThUpperCritical_Type(Integer32):
    """Custom type pdug5InputPhaseCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdug5InputPhaseCurrentThUpperCritical_Type.__name__ = "Integer32"
_Pdug5InputPhaseCurrentThUpperCritical_Object = MibTableColumn
pdug5InputPhaseCurrentThUpperCritical = _Pdug5InputPhaseCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 16),
    _Pdug5InputPhaseCurrentThUpperCritical_Type()
)
pdug5InputPhaseCurrentThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentThUpperCritical.setStatus("current")
_Pdug5InputPhaseCurrentPercentLoad_Type = Integer32
_Pdug5InputPhaseCurrentPercentLoad_Object = MibTableColumn
pdug5InputPhaseCurrentPercentLoad = _Pdug5InputPhaseCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 17),
    _Pdug5InputPhaseCurrentPercentLoad_Type()
)
pdug5InputPhaseCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentPercentLoad.setStatus("current")


class _Pdug5InputPhasePowerMeasType_Type(Integer32):
    """Custom type pdug5InputPhasePowerMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("neutral", 2),
          ("phase1", 3),
          ("phase2", 4),
          ("phase3", 5))
    )


_Pdug5InputPhasePowerMeasType_Type.__name__ = "Integer32"
_Pdug5InputPhasePowerMeasType_Object = MibTableColumn
pdug5InputPhasePowerMeasType = _Pdug5InputPhasePowerMeasType_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 18),
    _Pdug5InputPhasePowerMeasType_Type()
)
pdug5InputPhasePowerMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhasePowerMeasType.setStatus("current")
_Pdug5InputPhasePowerVA_Type = Integer32
_Pdug5InputPhasePowerVA_Object = MibTableColumn
pdug5InputPhasePowerVA = _Pdug5InputPhasePowerVA_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 19),
    _Pdug5InputPhasePowerVA_Type()
)
pdug5InputPhasePowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhasePowerVA.setStatus("current")
_Pdug5InputPhasePowerWatts_Type = Integer32
_Pdug5InputPhasePowerWatts_Object = MibTableColumn
pdug5InputPhasePowerWatts = _Pdug5InputPhasePowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 20),
    _Pdug5InputPhasePowerWatts_Type()
)
pdug5InputPhasePowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhasePowerWatts.setStatus("current")
_Pdug5InputPhasePowerWattHour_Type = Integer32
_Pdug5InputPhasePowerWattHour_Object = MibTableColumn
pdug5InputPhasePowerWattHour = _Pdug5InputPhasePowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 21),
    _Pdug5InputPhasePowerWattHour_Type()
)
pdug5InputPhasePowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhasePowerWattHour.setStatus("current")


class _Pdug5InputPhasePowerWattHourTimer_Type(DisplayString):
    """Custom type pdug5InputPhasePowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdug5InputPhasePowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdug5InputPhasePowerWattHourTimer_Object = MibTableColumn
pdug5InputPhasePowerWattHourTimer = _Pdug5InputPhasePowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 22),
    _Pdug5InputPhasePowerWattHourTimer_Type()
)
pdug5InputPhasePowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhasePowerWattHourTimer.setStatus("current")
_Pdug5InputPhasePowerFactor_Type = Integer32
_Pdug5InputPhasePowerFactor_Object = MibTableColumn
pdug5InputPhasePowerFactor = _Pdug5InputPhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 23),
    _Pdug5InputPhasePowerFactor_Type()
)
pdug5InputPhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhasePowerFactor.setStatus("current")
_Pdug5InputPhasePowerVAR_Type = Integer32
_Pdug5InputPhasePowerVAR_Object = MibTableColumn
pdug5InputPhasePowerVAR = _Pdug5InputPhasePowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 24),
    _Pdug5InputPhasePowerVAR_Type()
)
pdug5InputPhasePowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhasePowerVAR.setStatus("current")


class _Pdug5InputPhaseVoltageThResetThld_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageThResetThld based on Integer32"""
    defaultValue = 0


_Pdug5InputPhaseVoltageThResetThld_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageThResetThld_Object = MibTableColumn
pdug5InputPhaseVoltageThResetThld = _Pdug5InputPhaseVoltageThResetThld_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 25),
    _Pdug5InputPhaseVoltageThResetThld_Type()
)
pdug5InputPhaseVoltageThResetThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageThResetThld.setStatus("current")


class _Pdug5InputPhaseVoltageThChangeDelay_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageThChangeDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdug5InputPhaseVoltageThChangeDelay_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageThChangeDelay_Object = MibTableColumn
pdug5InputPhaseVoltageThChangeDelay = _Pdug5InputPhaseVoltageThChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 26),
    _Pdug5InputPhaseVoltageThChangeDelay_Type()
)
pdug5InputPhaseVoltageThChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageThChangeDelay.setStatus("current")


class _Pdug5InputPhaseVoltageThCtrl_Type(Integer32):
    """Custom type pdug5InputPhaseVoltageThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5InputPhaseVoltageThCtrl_Type.__name__ = "Integer32"
_Pdug5InputPhaseVoltageThCtrl_Object = MibTableColumn
pdug5InputPhaseVoltageThCtrl = _Pdug5InputPhaseVoltageThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 27),
    _Pdug5InputPhaseVoltageThCtrl_Type()
)
pdug5InputPhaseVoltageThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseVoltageThCtrl.setStatus("current")
_Pdug5InputPhaseCurrentThResetThld_Type = Integer32
_Pdug5InputPhaseCurrentThResetThld_Object = MibTableColumn
pdug5InputPhaseCurrentThResetThld = _Pdug5InputPhaseCurrentThResetThld_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 28),
    _Pdug5InputPhaseCurrentThResetThld_Type()
)
pdug5InputPhaseCurrentThResetThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentThResetThld.setStatus("current")


class _Pdug5InputPhaseCurrentThChangeDelay_Type(Integer32):
    """Custom type pdug5InputPhaseCurrentThChangeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdug5InputPhaseCurrentThChangeDelay_Type.__name__ = "Integer32"
_Pdug5InputPhaseCurrentThChangeDelay_Object = MibTableColumn
pdug5InputPhaseCurrentThChangeDelay = _Pdug5InputPhaseCurrentThChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 29),
    _Pdug5InputPhaseCurrentThChangeDelay_Type()
)
pdug5InputPhaseCurrentThChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentThChangeDelay.setStatus("current")


class _Pdug5InputPhaseCurrentThCtrl_Type(Integer32):
    """Custom type pdug5InputPhaseCurrentThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5InputPhaseCurrentThCtrl_Type.__name__ = "Integer32"
_Pdug5InputPhaseCurrentThCtrl_Object = MibTableColumn
pdug5InputPhaseCurrentThCtrl = _Pdug5InputPhaseCurrentThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 30),
    _Pdug5InputPhaseCurrentThCtrl_Type()
)
pdug5InputPhaseCurrentThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPhaseCurrentThCtrl.setStatus("current")


class _Pdug5InputPowerThresholdThLowerWarning_Type(Integer32):
    """Custom type pdug5InputPowerThresholdThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputPowerThresholdThLowerWarning_Type.__name__ = "Integer32"
_Pdug5InputPowerThresholdThLowerWarning_Object = MibTableColumn
pdug5InputPowerThresholdThLowerWarning = _Pdug5InputPowerThresholdThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 31),
    _Pdug5InputPowerThresholdThLowerWarning_Type()
)
pdug5InputPowerThresholdThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPowerThresholdThLowerWarning.setStatus("current")


class _Pdug5InputPowerThresholdThLowerCritical_Type(Integer32):
    """Custom type pdug5InputPowerThresholdThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputPowerThresholdThLowerCritical_Type.__name__ = "Integer32"
_Pdug5InputPowerThresholdThLowerCritical_Object = MibTableColumn
pdug5InputPowerThresholdThLowerCritical = _Pdug5InputPowerThresholdThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 32),
    _Pdug5InputPowerThresholdThLowerCritical_Type()
)
pdug5InputPowerThresholdThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPowerThresholdThLowerCritical.setStatus("current")


class _Pdug5InputPowerThresholdThUpperWarning_Type(Integer32):
    """Custom type pdug5InputPowerThresholdThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputPowerThresholdThUpperWarning_Type.__name__ = "Integer32"
_Pdug5InputPowerThresholdThUpperWarning_Object = MibTableColumn
pdug5InputPowerThresholdThUpperWarning = _Pdug5InputPowerThresholdThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 33),
    _Pdug5InputPowerThresholdThUpperWarning_Type()
)
pdug5InputPowerThresholdThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPowerThresholdThUpperWarning.setStatus("current")


class _Pdug5InputPowerThresholdThUpperCritical_Type(Integer32):
    """Custom type pdug5InputPowerThresholdThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputPowerThresholdThUpperCritical_Type.__name__ = "Integer32"
_Pdug5InputPowerThresholdThUpperCritical_Object = MibTableColumn
pdug5InputPowerThresholdThUpperCritical = _Pdug5InputPowerThresholdThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 34),
    _Pdug5InputPowerThresholdThUpperCritical_Type()
)
pdug5InputPowerThresholdThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPowerThresholdThUpperCritical.setStatus("current")
_Pdug5InputPowerThresholdThResetThld_Type = Integer32
_Pdug5InputPowerThresholdThResetThld_Object = MibTableColumn
pdug5InputPowerThresholdThResetThld = _Pdug5InputPowerThresholdThResetThld_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 35),
    _Pdug5InputPowerThresholdThResetThld_Type()
)
pdug5InputPowerThresholdThResetThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPowerThresholdThResetThld.setStatus("current")


class _Pdug5InputPowerThresholdThChangeDelay_Type(Integer32):
    """Custom type pdug5InputPowerThresholdThChangeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdug5InputPowerThresholdThChangeDelay_Type.__name__ = "Integer32"
_Pdug5InputPowerThresholdThChangeDelay_Object = MibTableColumn
pdug5InputPowerThresholdThChangeDelay = _Pdug5InputPowerThresholdThChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 36),
    _Pdug5InputPowerThresholdThChangeDelay_Type()
)
pdug5InputPowerThresholdThChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPowerThresholdThChangeDelay.setStatus("current")


class _Pdug5InputPowerThresholdThCtrl_Type(Integer32):
    """Custom type pdug5InputPowerThresholdThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5InputPowerThresholdThCtrl_Type.__name__ = "Integer32"
_Pdug5InputPowerThresholdThCtrl_Object = MibTableColumn
pdug5InputPowerThresholdThCtrl = _Pdug5InputPowerThresholdThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 37),
    _Pdug5InputPowerThresholdThCtrl_Type()
)
pdug5InputPowerThresholdThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputPowerThresholdThCtrl.setStatus("current")


class _Pdug5InputEnergyThresholdThUpperWarning_Type(Integer32):
    """Custom type pdug5InputEnergyThresholdThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputEnergyThresholdThUpperWarning_Type.__name__ = "Integer32"
_Pdug5InputEnergyThresholdThUpperWarning_Object = MibTableColumn
pdug5InputEnergyThresholdThUpperWarning = _Pdug5InputEnergyThresholdThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 38),
    _Pdug5InputEnergyThresholdThUpperWarning_Type()
)
pdug5InputEnergyThresholdThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputEnergyThresholdThUpperWarning.setStatus("current")


class _Pdug5InputEnergyThresholdThUpperCritical_Type(Integer32):
    """Custom type pdug5InputEnergyThresholdThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5InputEnergyThresholdThUpperCritical_Type.__name__ = "Integer32"
_Pdug5InputEnergyThresholdThUpperCritical_Object = MibTableColumn
pdug5InputEnergyThresholdThUpperCritical = _Pdug5InputEnergyThresholdThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 39),
    _Pdug5InputEnergyThresholdThUpperCritical_Type()
)
pdug5InputEnergyThresholdThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputEnergyThresholdThUpperCritical.setStatus("current")
_Pdug5InputEnergyThresholdThResetThld_Type = Integer32
_Pdug5InputEnergyThresholdThResetThld_Object = MibTableColumn
pdug5InputEnergyThresholdThResetThld = _Pdug5InputEnergyThresholdThResetThld_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 40),
    _Pdug5InputEnergyThresholdThResetThld_Type()
)
pdug5InputEnergyThresholdThResetThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputEnergyThresholdThResetThld.setStatus("current")


class _Pdug5InputEnergyThresholdThChangeDelay_Type(Integer32):
    """Custom type pdug5InputEnergyThresholdThChangeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdug5InputEnergyThresholdThChangeDelay_Type.__name__ = "Integer32"
_Pdug5InputEnergyThresholdThChangeDelay_Object = MibTableColumn
pdug5InputEnergyThresholdThChangeDelay = _Pdug5InputEnergyThresholdThChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 41),
    _Pdug5InputEnergyThresholdThChangeDelay_Type()
)
pdug5InputEnergyThresholdThChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputEnergyThresholdThChangeDelay.setStatus("current")


class _Pdug5InputEnergyThresholdThCtrl_Type(Integer32):
    """Custom type pdug5InputEnergyThresholdThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5InputEnergyThresholdThCtrl_Type.__name__ = "Integer32"
_Pdug5InputEnergyThresholdThCtrl_Object = MibTableColumn
pdug5InputEnergyThresholdThCtrl = _Pdug5InputEnergyThresholdThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 42),
    _Pdug5InputEnergyThresholdThCtrl_Type()
)
pdug5InputEnergyThresholdThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputEnergyThresholdThCtrl.setStatus("current")


class _Pdug5InputPhasePowerThStatus_Type(Integer32):
    """Custom type pdug5InputPhasePowerThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdug5InputPhasePowerThStatus_Type.__name__ = "Integer32"
_Pdug5InputPhasePowerThStatus_Object = MibTableColumn
pdug5InputPhasePowerThStatus = _Pdug5InputPhasePowerThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 2, 1, 43),
    _Pdug5InputPhasePowerThStatus_Type()
)
pdug5InputPhasePowerThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputPhasePowerThStatus.setStatus("current")
_Pdug5InputRcmTable_Object = MibTable
pdug5InputRcmTable = _Pdug5InputRcmTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pdug5InputRcmTable.setStatus("current")
_Pdug5InputRcmEntry_Object = MibTableRow
pdug5InputRcmEntry = _Pdug5InputRcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1)
)
pdug5InputRcmEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
)
if mibBuilder.loadTexts:
    pdug5InputRcmEntry.setStatus("current")


class _Pdug5InputRcmEnabled_Type(Integer32):
    """Custom type pdug5InputRcmEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("featureNotAvailable", -1),
          ("off", 0),
          ("on", 1))
    )


_Pdug5InputRcmEnabled_Type.__name__ = "Integer32"
_Pdug5InputRcmEnabled_Object = MibTableColumn
pdug5InputRcmEnabled = _Pdug5InputRcmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 1),
    _Pdug5InputRcmEnabled_Type()
)
pdug5InputRcmEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputRcmEnabled.setStatus("current")


class _Pdug5InputRcmModStatus_Type(Integer32):
    """Custom type pdug5InputRcmModStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("featureNotAvailable", -1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_Pdug5InputRcmModStatus_Type.__name__ = "Integer32"
_Pdug5InputRcmModStatus_Object = MibTableColumn
pdug5InputRcmModStatus = _Pdug5InputRcmModStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 2),
    _Pdug5InputRcmModStatus_Type()
)
pdug5InputRcmModStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputRcmModStatus.setStatus("current")


class _Pdug5InputRcmThUpperWarning_Type(Integer32):
    """Custom type pdug5InputRcmThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_Pdug5InputRcmThUpperWarning_Type.__name__ = "Integer32"
_Pdug5InputRcmThUpperWarning_Object = MibTableColumn
pdug5InputRcmThUpperWarning = _Pdug5InputRcmThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 3),
    _Pdug5InputRcmThUpperWarning_Type()
)
pdug5InputRcmThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmThUpperWarning.setStatus("current")


class _Pdug5InputRcmThUpperCritical_Type(Integer32):
    """Custom type pdug5InputRcmThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_Pdug5InputRcmThUpperCritical_Type.__name__ = "Integer32"
_Pdug5InputRcmThUpperCritical_Object = MibTableColumn
pdug5InputRcmThUpperCritical = _Pdug5InputRcmThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 4),
    _Pdug5InputRcmThUpperCritical_Type()
)
pdug5InputRcmThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmThUpperCritical.setStatus("current")


class _Pdug5InputRcmThResetThld_Type(Integer32):
    """Custom type pdug5InputRcmThResetThld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Pdug5InputRcmThResetThld_Type.__name__ = "Integer32"
_Pdug5InputRcmThResetThld_Object = MibTableColumn
pdug5InputRcmThResetThld = _Pdug5InputRcmThResetThld_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 5),
    _Pdug5InputRcmThResetThld_Type()
)
pdug5InputRcmThResetThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmThResetThld.setStatus("current")


class _Pdug5InputRcmThChangeDelay_Type(Integer32):
    """Custom type pdug5InputRcmThChangeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdug5InputRcmThChangeDelay_Type.__name__ = "Integer32"
_Pdug5InputRcmThChangeDelay_Object = MibTableColumn
pdug5InputRcmThChangeDelay = _Pdug5InputRcmThChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 6),
    _Pdug5InputRcmThChangeDelay_Type()
)
pdug5InputRcmThChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmThChangeDelay.setStatus("current")


class _Pdug5InputRcmThCtrl_Type(Integer32):
    """Custom type pdug5InputRcmThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5InputRcmThCtrl_Type.__name__ = "Integer32"
_Pdug5InputRcmThCtrl_Object = MibTableColumn
pdug5InputRcmThCtrl = _Pdug5InputRcmThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 7),
    _Pdug5InputRcmThCtrl_Type()
)
pdug5InputRcmThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmThCtrl.setStatus("current")


class _Pdug5InputRcmThStatus_Type(Integer32):
    """Custom type pdug5InputRcmThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("featureNotAvailable", -1),
          ("good", 1),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdug5InputRcmThStatus_Type.__name__ = "Integer32"
_Pdug5InputRcmThStatus_Object = MibTableColumn
pdug5InputRcmThStatus = _Pdug5InputRcmThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 8),
    _Pdug5InputRcmThStatus_Type()
)
pdug5InputRcmThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputRcmThStatus.setStatus("current")
_Pdug5InputRcmCurrent_Type = Integer32
_Pdug5InputRcmCurrent_Object = MibTableColumn
pdug5InputRcmCurrent = _Pdug5InputRcmCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 3, 1, 9),
    _Pdug5InputRcmCurrent_Type()
)
pdug5InputRcmCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputRcmCurrent.setStatus("current")
_Pdug5InputRcmSelfTestTable_Object = MibTable
pdug5InputRcmSelfTestTable = _Pdug5InputRcmSelfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestTable.setStatus("current")
_Pdug5InputRcmSelfTestEntry_Object = MibTableRow
pdug5InputRcmSelfTestEntry = _Pdug5InputRcmSelfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1)
)
pdug5InputRcmSelfTestEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
)
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestEntry.setStatus("current")


class _Pdug5InputRcmSelfTestEnable_Type(Integer32):
    """Custom type pdug5InputRcmSelfTestEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("featureNotAvailable", -1),
          ("disable", 0),
          ("enable", 1))
    )


_Pdug5InputRcmSelfTestEnable_Type.__name__ = "Integer32"
_Pdug5InputRcmSelfTestEnable_Object = MibTableColumn
pdug5InputRcmSelfTestEnable = _Pdug5InputRcmSelfTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 1),
    _Pdug5InputRcmSelfTestEnable_Type()
)
pdug5InputRcmSelfTestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestEnable.setStatus("current")


class _Pdug5InputRcmSelfTestFreq_Type(Integer32):
    """Custom type pdug5InputRcmSelfTestFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("featureNotAvailable", -1),
          ("daily", 1),
          ("weekly", 2),
          ("monthly", 3),
          ("yearly", 4))
    )


_Pdug5InputRcmSelfTestFreq_Type.__name__ = "Integer32"
_Pdug5InputRcmSelfTestFreq_Object = MibTableColumn
pdug5InputRcmSelfTestFreq = _Pdug5InputRcmSelfTestFreq_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 2),
    _Pdug5InputRcmSelfTestFreq_Type()
)
pdug5InputRcmSelfTestFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestFreq.setStatus("current")


class _Pdug5InputRcmSelfTestHour_Type(Integer32):
    """Custom type pdug5InputRcmSelfTestHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 23),
    )


_Pdug5InputRcmSelfTestHour_Type.__name__ = "Integer32"
_Pdug5InputRcmSelfTestHour_Object = MibTableColumn
pdug5InputRcmSelfTestHour = _Pdug5InputRcmSelfTestHour_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 3),
    _Pdug5InputRcmSelfTestHour_Type()
)
pdug5InputRcmSelfTestHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestHour.setStatus("current")


class _Pdug5InputRcmSelfTestMinute_Type(Integer32):
    """Custom type pdug5InputRcmSelfTestMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 59),
    )


_Pdug5InputRcmSelfTestMinute_Type.__name__ = "Integer32"
_Pdug5InputRcmSelfTestMinute_Object = MibTableColumn
pdug5InputRcmSelfTestMinute = _Pdug5InputRcmSelfTestMinute_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 4),
    _Pdug5InputRcmSelfTestMinute_Type()
)
pdug5InputRcmSelfTestMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestMinute.setStatus("current")


class _Pdug5InputRcmSelfTestDay_Type(Integer32):
    """Custom type pdug5InputRcmSelfTestDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("featureNotAvailable", -1),
          ("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )


_Pdug5InputRcmSelfTestDay_Type.__name__ = "Integer32"
_Pdug5InputRcmSelfTestDay_Object = MibTableColumn
pdug5InputRcmSelfTestDay = _Pdug5InputRcmSelfTestDay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 5),
    _Pdug5InputRcmSelfTestDay_Type()
)
pdug5InputRcmSelfTestDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestDay.setStatus("current")


class _Pdug5InputRcmSelfTestMonth_Type(Integer32):
    """Custom type pdug5InputRcmSelfTestMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("featureNotAvailable", -1),
          ("january", 0),
          ("february", 1),
          ("march", 2),
          ("april", 3),
          ("may", 4),
          ("june", 5),
          ("july", 6),
          ("august", 7),
          ("september", 8),
          ("october", 9),
          ("november", 10),
          ("december", 11))
    )


_Pdug5InputRcmSelfTestMonth_Type.__name__ = "Integer32"
_Pdug5InputRcmSelfTestMonth_Object = MibTableColumn
pdug5InputRcmSelfTestMonth = _Pdug5InputRcmSelfTestMonth_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 6),
    _Pdug5InputRcmSelfTestMonth_Type()
)
pdug5InputRcmSelfTestMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestMonth.setStatus("current")
_Pdug5InputRcmSelfTestNextRunTime_Type = DisplayString
_Pdug5InputRcmSelfTestNextRunTime_Object = MibTableColumn
pdug5InputRcmSelfTestNextRunTime = _Pdug5InputRcmSelfTestNextRunTime_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 7),
    _Pdug5InputRcmSelfTestNextRunTime_Type()
)
pdug5InputRcmSelfTestNextRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestNextRunTime.setStatus("current")
_Pdug5InputRcmSelfTestLastRunTime_Type = DisplayString
_Pdug5InputRcmSelfTestLastRunTime_Object = MibTableColumn
pdug5InputRcmSelfTestLastRunTime = _Pdug5InputRcmSelfTestLastRunTime_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 8),
    _Pdug5InputRcmSelfTestLastRunTime_Type()
)
pdug5InputRcmSelfTestLastRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestLastRunTime.setStatus("current")


class _Pdug5InputRcmSelfTestLastRunStatus_Type(Integer32):
    """Custom type pdug5InputRcmSelfTestLastRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("featureNotAvailable", -1),
          ("passed", 1),
          ("failed", 2),
          ("pending", 3))
    )


_Pdug5InputRcmSelfTestLastRunStatus_Type.__name__ = "Integer32"
_Pdug5InputRcmSelfTestLastRunStatus_Object = MibTableColumn
pdug5InputRcmSelfTestLastRunStatus = _Pdug5InputRcmSelfTestLastRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 2, 4, 1, 9),
    _Pdug5InputRcmSelfTestLastRunStatus_Type()
)
pdug5InputRcmSelfTestLastRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5InputRcmSelfTestLastRunStatus.setStatus("current")
_Pdug5Group_ObjectIdentity = ObjectIdentity
pdug5Group = _Pdug5Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3)
)
_Pdug5GroupTable_Object = MibTable
pdug5GroupTable = _Pdug5GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pdug5GroupTable.setStatus("current")
_Pdug5GroupEntry_Object = MibTableRow
pdug5GroupEntry = _Pdug5GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1)
)
pdug5GroupEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5GroupIndex"),
)
if mibBuilder.loadTexts:
    pdug5GroupEntry.setStatus("current")


class _Pdug5GroupIndex_Type(Integer32):
    """Custom type pdug5GroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Pdug5GroupIndex_Type.__name__ = "Integer32"
_Pdug5GroupIndex_Object = MibTableColumn
pdug5GroupIndex = _Pdug5GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 1),
    _Pdug5GroupIndex_Type()
)
pdug5GroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5GroupIndex.setStatus("current")


class _Pdug5GroupName_Type(DisplayString):
    """Custom type pdug5GroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdug5GroupName_Type.__name__ = "DisplayString"
_Pdug5GroupName_Object = MibTableColumn
pdug5GroupName = _Pdug5GroupName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 2),
    _Pdug5GroupName_Type()
)
pdug5GroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5GroupName.setStatus("current")


class _Pdug5GroupType_Type(Integer32):
    """Custom type pdug5GroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("breaker1pole", 2),
          ("breaker2pole", 3),
          ("breaker3pole", 4),
          ("outletSection", 5))
    )


_Pdug5GroupType_Type.__name__ = "Integer32"
_Pdug5GroupType_Object = MibTableColumn
pdug5GroupType = _Pdug5GroupType_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 3),
    _Pdug5GroupType_Type()
)
pdug5GroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupType.setStatus("current")


class _Pdug5GroupVoltageMeasType_Type(Integer32):
    """Custom type pdug5GroupVoltageMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("phase1toN", 2),
          ("phase2toN", 3),
          ("phase3toN", 4),
          ("phase1to2", 5),
          ("phase2to3", 6),
          ("phase3to1", 7))
    )


_Pdug5GroupVoltageMeasType_Type.__name__ = "Integer32"
_Pdug5GroupVoltageMeasType_Object = MibTableColumn
pdug5GroupVoltageMeasType = _Pdug5GroupVoltageMeasType_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 4),
    _Pdug5GroupVoltageMeasType_Type()
)
pdug5GroupVoltageMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupVoltageMeasType.setStatus("current")
_Pdug5GroupVoltage_Type = Integer32
_Pdug5GroupVoltage_Object = MibTableColumn
pdug5GroupVoltage = _Pdug5GroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 5),
    _Pdug5GroupVoltage_Type()
)
pdug5GroupVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupVoltage.setStatus("current")


class _Pdug5GroupVoltageThStatus_Type(Integer32):
    """Custom type pdug5GroupVoltageThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdug5GroupVoltageThStatus_Type.__name__ = "Integer32"
_Pdug5GroupVoltageThStatus_Object = MibTableColumn
pdug5GroupVoltageThStatus = _Pdug5GroupVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 6),
    _Pdug5GroupVoltageThStatus_Type()
)
pdug5GroupVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupVoltageThStatus.setStatus("current")


class _Pdug5GroupVoltageThLowerWarning_Type(Integer32):
    """Custom type pdug5GroupVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5GroupVoltageThLowerWarning_Type.__name__ = "Integer32"
_Pdug5GroupVoltageThLowerWarning_Object = MibTableColumn
pdug5GroupVoltageThLowerWarning = _Pdug5GroupVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 7),
    _Pdug5GroupVoltageThLowerWarning_Type()
)
pdug5GroupVoltageThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupVoltageThLowerWarning.setStatus("current")


class _Pdug5GroupVoltageThLowerCritical_Type(Integer32):
    """Custom type pdug5GroupVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5GroupVoltageThLowerCritical_Type.__name__ = "Integer32"
_Pdug5GroupVoltageThLowerCritical_Object = MibTableColumn
pdug5GroupVoltageThLowerCritical = _Pdug5GroupVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 8),
    _Pdug5GroupVoltageThLowerCritical_Type()
)
pdug5GroupVoltageThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupVoltageThLowerCritical.setStatus("current")


class _Pdug5GroupVoltageThUpperWarning_Type(Integer32):
    """Custom type pdug5GroupVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5GroupVoltageThUpperWarning_Type.__name__ = "Integer32"
_Pdug5GroupVoltageThUpperWarning_Object = MibTableColumn
pdug5GroupVoltageThUpperWarning = _Pdug5GroupVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 9),
    _Pdug5GroupVoltageThUpperWarning_Type()
)
pdug5GroupVoltageThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupVoltageThUpperWarning.setStatus("current")


class _Pdug5GroupVoltageThUpperCritical_Type(Integer32):
    """Custom type pdug5GroupVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdug5GroupVoltageThUpperCritical_Type.__name__ = "Integer32"
_Pdug5GroupVoltageThUpperCritical_Object = MibTableColumn
pdug5GroupVoltageThUpperCritical = _Pdug5GroupVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 10),
    _Pdug5GroupVoltageThUpperCritical_Type()
)
pdug5GroupVoltageThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupVoltageThUpperCritical.setStatus("current")
_Pdug5groupCurrentRating_Type = Integer32
_Pdug5groupCurrentRating_Object = MibTableColumn
pdug5groupCurrentRating = _Pdug5groupCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 11),
    _Pdug5groupCurrentRating_Type()
)
pdug5groupCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5groupCurrentRating.setStatus("current")
_Pdug5GroupCurrent_Type = Integer32
_Pdug5GroupCurrent_Object = MibTableColumn
pdug5GroupCurrent = _Pdug5GroupCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 12),
    _Pdug5GroupCurrent_Type()
)
pdug5GroupCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupCurrent.setStatus("current")


class _Pdug5GroupCurrentThStatus_Type(Integer32):
    """Custom type pdug5GroupCurrentThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5),
          ("cbOff", 6))
    )


_Pdug5GroupCurrentThStatus_Type.__name__ = "Integer32"
_Pdug5GroupCurrentThStatus_Object = MibTableColumn
pdug5GroupCurrentThStatus = _Pdug5GroupCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 13),
    _Pdug5GroupCurrentThStatus_Type()
)
pdug5GroupCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupCurrentThStatus.setStatus("current")


class _Pdug5GroupCurrentThLowerWarning_Type(Integer32):
    """Custom type pdug5GroupCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdug5GroupCurrentThLowerWarning_Type.__name__ = "Integer32"
_Pdug5GroupCurrentThLowerWarning_Object = MibTableColumn
pdug5GroupCurrentThLowerWarning = _Pdug5GroupCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 14),
    _Pdug5GroupCurrentThLowerWarning_Type()
)
pdug5GroupCurrentThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5GroupCurrentThLowerWarning.setStatus("current")


class _Pdug5GroupCurrentThLowerCritical_Type(Integer32):
    """Custom type pdug5GroupCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdug5GroupCurrentThLowerCritical_Type.__name__ = "Integer32"
_Pdug5GroupCurrentThLowerCritical_Object = MibTableColumn
pdug5GroupCurrentThLowerCritical = _Pdug5GroupCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 15),
    _Pdug5GroupCurrentThLowerCritical_Type()
)
pdug5GroupCurrentThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5GroupCurrentThLowerCritical.setStatus("current")


class _Pdug5GroupCurrentThUpperWarning_Type(Integer32):
    """Custom type pdug5GroupCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdug5GroupCurrentThUpperWarning_Type.__name__ = "Integer32"
_Pdug5GroupCurrentThUpperWarning_Object = MibTableColumn
pdug5GroupCurrentThUpperWarning = _Pdug5GroupCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 16),
    _Pdug5GroupCurrentThUpperWarning_Type()
)
pdug5GroupCurrentThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5GroupCurrentThUpperWarning.setStatus("current")


class _Pdug5GroupCurrentThUpperCritical_Type(Integer32):
    """Custom type pdug5GroupCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdug5GroupCurrentThUpperCritical_Type.__name__ = "Integer32"
_Pdug5GroupCurrentThUpperCritical_Object = MibTableColumn
pdug5GroupCurrentThUpperCritical = _Pdug5GroupCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 17),
    _Pdug5GroupCurrentThUpperCritical_Type()
)
pdug5GroupCurrentThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5GroupCurrentThUpperCritical.setStatus("current")
_Pdug5GroupCurrentPercentLoad_Type = Integer32
_Pdug5GroupCurrentPercentLoad_Object = MibTableColumn
pdug5GroupCurrentPercentLoad = _Pdug5GroupCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 18),
    _Pdug5GroupCurrentPercentLoad_Type()
)
pdug5GroupCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupCurrentPercentLoad.setStatus("current")
_Pdug5GroupPowerVA_Type = Integer32
_Pdug5GroupPowerVA_Object = MibTableColumn
pdug5GroupPowerVA = _Pdug5GroupPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 19),
    _Pdug5GroupPowerVA_Type()
)
pdug5GroupPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupPowerVA.setStatus("current")
_Pdug5GroupPowerWatts_Type = Integer32
_Pdug5GroupPowerWatts_Object = MibTableColumn
pdug5GroupPowerWatts = _Pdug5GroupPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 20),
    _Pdug5GroupPowerWatts_Type()
)
pdug5GroupPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupPowerWatts.setStatus("current")
_Pdug5GroupPowerWattHour_Type = Integer32
_Pdug5GroupPowerWattHour_Object = MibTableColumn
pdug5GroupPowerWattHour = _Pdug5GroupPowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 21),
    _Pdug5GroupPowerWattHour_Type()
)
pdug5GroupPowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupPowerWattHour.setStatus("current")


class _Pdug5GroupPowerWattHourTimer_Type(DisplayString):
    """Custom type pdug5GroupPowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdug5GroupPowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdug5GroupPowerWattHourTimer_Object = MibTableColumn
pdug5GroupPowerWattHourTimer = _Pdug5GroupPowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 22),
    _Pdug5GroupPowerWattHourTimer_Type()
)
pdug5GroupPowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupPowerWattHourTimer.setStatus("current")
_Pdug5GroupPowerFactor_Type = Integer32
_Pdug5GroupPowerFactor_Object = MibTableColumn
pdug5GroupPowerFactor = _Pdug5GroupPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 23),
    _Pdug5GroupPowerFactor_Type()
)
pdug5GroupPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupPowerFactor.setStatus("current")
_Pdug5GroupPowerVAR_Type = Integer32
_Pdug5GroupPowerVAR_Object = MibTableColumn
pdug5GroupPowerVAR = _Pdug5GroupPowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 24),
    _Pdug5GroupPowerVAR_Type()
)
pdug5GroupPowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupPowerVAR.setStatus("current")


class _Pdug5GroupOutletCount_Type(Integer32):
    """Custom type pdug5GroupOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_Pdug5GroupOutletCount_Type.__name__ = "Integer32"
_Pdug5GroupOutletCount_Object = MibTableColumn
pdug5GroupOutletCount = _Pdug5GroupOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 25),
    _Pdug5GroupOutletCount_Type()
)
pdug5GroupOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupOutletCount.setStatus("current")


class _Pdug5GroupBreakerStatus_Type(Integer32):
    """Custom type pdug5GroupBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("breakerOn", 2),
          ("breakerOff", 3))
    )


_Pdug5GroupBreakerStatus_Type.__name__ = "Integer32"
_Pdug5GroupBreakerStatus_Object = MibTableColumn
pdug5GroupBreakerStatus = _Pdug5GroupBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 26),
    _Pdug5GroupBreakerStatus_Type()
)
pdug5GroupBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupBreakerStatus.setStatus("current")


class _Pdug5GroupVoltageThCtrl_Type(Integer32):
    """Custom type pdug5GroupVoltageThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5GroupVoltageThCtrl_Type.__name__ = "Integer32"
_Pdug5GroupVoltageThCtrl_Object = MibTableColumn
pdug5GroupVoltageThCtrl = _Pdug5GroupVoltageThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 27),
    _Pdug5GroupVoltageThCtrl_Type()
)
pdug5GroupVoltageThCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5GroupVoltageThCtrl.setStatus("current")
_Pdug5GroupCurrentThCtrl_Type = Integer32
_Pdug5GroupCurrentThCtrl_Object = MibTableColumn
pdug5GroupCurrentThCtrl = _Pdug5GroupCurrentThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 3, 1, 1, 28),
    _Pdug5GroupCurrentThCtrl_Type()
)
pdug5GroupCurrentThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5GroupCurrentThCtrl.setStatus("current")
_Pdug5Environment_ObjectIdentity = ObjectIdentity
pdug5Environment = _Pdug5Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4)
)
_Pdug5EnvProbeTable_Object = MibTable
pdug5EnvProbeTable = _Pdug5EnvProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pdug5EnvProbeTable.setStatus("current")
_Pdug5EnvProbeEntry_Object = MibTableRow
pdug5EnvProbeEntry = _Pdug5EnvProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1)
)
pdug5EnvProbeEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
)
if mibBuilder.loadTexts:
    pdug5EnvProbeEntry.setStatus("current")


class _Pdug5TemperatureScale_Type(Integer32):
    """Custom type pdug5TemperatureScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_Pdug5TemperatureScale_Type.__name__ = "Integer32"
_Pdug5TemperatureScale_Object = MibTableColumn
pdug5TemperatureScale = _Pdug5TemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1, 1),
    _Pdug5TemperatureScale_Type()
)
pdug5TemperatureScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5TemperatureScale.setStatus("current")
_Pdug5TemperatureCount_Type = Integer32
_Pdug5TemperatureCount_Object = MibTableColumn
pdug5TemperatureCount = _Pdug5TemperatureCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1, 2),
    _Pdug5TemperatureCount_Type()
)
pdug5TemperatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5TemperatureCount.setStatus("current")
_Pdug5HumidityCount_Type = Integer32
_Pdug5HumidityCount_Object = MibTableColumn
pdug5HumidityCount = _Pdug5HumidityCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1, 3),
    _Pdug5HumidityCount_Type()
)
pdug5HumidityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5HumidityCount.setStatus("current")
_Pdug5DoorCount_Type = Integer32
_Pdug5DoorCount_Object = MibTableColumn
pdug5DoorCount = _Pdug5DoorCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1, 4),
    _Pdug5DoorCount_Type()
)
pdug5DoorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5DoorCount.setStatus("current")
_Pdug5DryCount_Type = Integer32
_Pdug5DryCount_Object = MibTableColumn
pdug5DryCount = _Pdug5DryCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1, 5),
    _Pdug5DryCount_Type()
)
pdug5DryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5DryCount.setStatus("current")
_Pdug5SpotCount_Type = Integer32
_Pdug5SpotCount_Object = MibTableColumn
pdug5SpotCount = _Pdug5SpotCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1, 6),
    _Pdug5SpotCount_Type()
)
pdug5SpotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5SpotCount.setStatus("current")
_Pdug5RopeCount_Type = Integer32
_Pdug5RopeCount_Object = MibTableColumn
pdug5RopeCount = _Pdug5RopeCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1, 7),
    _Pdug5RopeCount_Type()
)
pdug5RopeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5RopeCount.setStatus("current")
_Pdug5HidCount_Type = Integer32
_Pdug5HidCount_Object = MibTableColumn
pdug5HidCount = _Pdug5HidCount_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 1, 1, 10),
    _Pdug5HidCount_Type()
)
pdug5HidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5HidCount.setStatus("current")
_Pdug5TemperatureTable_Object = MibTable
pdug5TemperatureTable = _Pdug5TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2)
)
if mibBuilder.loadTexts:
    pdug5TemperatureTable.setStatus("current")
_Pdug5TemperatureEntry_Object = MibTableRow
pdug5TemperatureEntry = _Pdug5TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1)
)
pdug5TemperatureEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5TemperatureIndex"),
)
if mibBuilder.loadTexts:
    pdug5TemperatureEntry.setStatus("current")


class _Pdug5TemperatureIndex_Type(Integer32):
    """Custom type pdug5TemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Pdug5TemperatureIndex_Type.__name__ = "Integer32"
_Pdug5TemperatureIndex_Object = MibTableColumn
pdug5TemperatureIndex = _Pdug5TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 1),
    _Pdug5TemperatureIndex_Type()
)
pdug5TemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5TemperatureIndex.setStatus("current")


class _Pdug5TemperatureName_Type(DisplayString):
    """Custom type pdug5TemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Pdug5TemperatureName_Type.__name__ = "DisplayString"
_Pdug5TemperatureName_Object = MibTableColumn
pdug5TemperatureName = _Pdug5TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 2),
    _Pdug5TemperatureName_Type()
)
pdug5TemperatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5TemperatureName.setStatus("current")


class _Pdug5TemperatureProbeStatus_Type(Integer32):
    """Custom type pdug5TemperatureProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdug5TemperatureProbeStatus_Type.__name__ = "Integer32"
_Pdug5TemperatureProbeStatus_Object = MibTableColumn
pdug5TemperatureProbeStatus = _Pdug5TemperatureProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 3),
    _Pdug5TemperatureProbeStatus_Type()
)
pdug5TemperatureProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5TemperatureProbeStatus.setStatus("current")
_Pdug5TemperatureValue_Type = Integer32
_Pdug5TemperatureValue_Object = MibTableColumn
pdug5TemperatureValue = _Pdug5TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 4),
    _Pdug5TemperatureValue_Type()
)
pdug5TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5TemperatureValue.setStatus("current")


class _Pdug5TemperatureThStatus_Type(Integer32):
    """Custom type pdug5TemperatureThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdug5TemperatureThStatus_Type.__name__ = "Integer32"
_Pdug5TemperatureThStatus_Object = MibTableColumn
pdug5TemperatureThStatus = _Pdug5TemperatureThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 5),
    _Pdug5TemperatureThStatus_Type()
)
pdug5TemperatureThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5TemperatureThStatus.setStatus("current")


class _Pdug5TemperatureThLowerWarning_Type(Integer32):
    """Custom type pdug5TemperatureThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdug5TemperatureThLowerWarning_Type.__name__ = "Integer32"
_Pdug5TemperatureThLowerWarning_Object = MibTableColumn
pdug5TemperatureThLowerWarning = _Pdug5TemperatureThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 6),
    _Pdug5TemperatureThLowerWarning_Type()
)
pdug5TemperatureThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5TemperatureThLowerWarning.setStatus("current")


class _Pdug5TemperatureThLowerCritical_Type(Integer32):
    """Custom type pdug5TemperatureThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdug5TemperatureThLowerCritical_Type.__name__ = "Integer32"
_Pdug5TemperatureThLowerCritical_Object = MibTableColumn
pdug5TemperatureThLowerCritical = _Pdug5TemperatureThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 7),
    _Pdug5TemperatureThLowerCritical_Type()
)
pdug5TemperatureThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5TemperatureThLowerCritical.setStatus("current")


class _Pdug5TemperatureThUpperWarning_Type(Integer32):
    """Custom type pdug5TemperatureThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdug5TemperatureThUpperWarning_Type.__name__ = "Integer32"
_Pdug5TemperatureThUpperWarning_Object = MibTableColumn
pdug5TemperatureThUpperWarning = _Pdug5TemperatureThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 8),
    _Pdug5TemperatureThUpperWarning_Type()
)
pdug5TemperatureThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5TemperatureThUpperWarning.setStatus("current")


class _Pdug5TemperatureThUpperCritical_Type(Integer32):
    """Custom type pdug5TemperatureThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdug5TemperatureThUpperCritical_Type.__name__ = "Integer32"
_Pdug5TemperatureThUpperCritical_Object = MibTableColumn
pdug5TemperatureThUpperCritical = _Pdug5TemperatureThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 9),
    _Pdug5TemperatureThUpperCritical_Type()
)
pdug5TemperatureThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5TemperatureThUpperCritical.setStatus("current")


class _Pdug5TemperatureThCtrl_Type(Integer32):
    """Custom type pdug5TemperatureThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5TemperatureThCtrl_Type.__name__ = "Integer32"
_Pdug5TemperatureThCtrl_Object = MibTableColumn
pdug5TemperatureThCtrl = _Pdug5TemperatureThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 2, 1, 10),
    _Pdug5TemperatureThCtrl_Type()
)
pdug5TemperatureThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5TemperatureThCtrl.setStatus("current")
_Pdug5HumidityTable_Object = MibTable
pdug5HumidityTable = _Pdug5HumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3)
)
if mibBuilder.loadTexts:
    pdug5HumidityTable.setStatus("current")
_Pdug5HumidityEntry_Object = MibTableRow
pdug5HumidityEntry = _Pdug5HumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1)
)
pdug5HumidityEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5HumidityIndex"),
)
if mibBuilder.loadTexts:
    pdug5HumidityEntry.setStatus("current")


class _Pdug5HumidityIndex_Type(Integer32):
    """Custom type pdug5HumidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Pdug5HumidityIndex_Type.__name__ = "Integer32"
_Pdug5HumidityIndex_Object = MibTableColumn
pdug5HumidityIndex = _Pdug5HumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 1),
    _Pdug5HumidityIndex_Type()
)
pdug5HumidityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5HumidityIndex.setStatus("current")


class _Pdug5HumidityName_Type(DisplayString):
    """Custom type pdug5HumidityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Pdug5HumidityName_Type.__name__ = "DisplayString"
_Pdug5HumidityName_Object = MibTableColumn
pdug5HumidityName = _Pdug5HumidityName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 2),
    _Pdug5HumidityName_Type()
)
pdug5HumidityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HumidityName.setStatus("current")


class _Pdug5HumidityProbeStatus_Type(Integer32):
    """Custom type pdug5HumidityProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdug5HumidityProbeStatus_Type.__name__ = "Integer32"
_Pdug5HumidityProbeStatus_Object = MibTableColumn
pdug5HumidityProbeStatus = _Pdug5HumidityProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 3),
    _Pdug5HumidityProbeStatus_Type()
)
pdug5HumidityProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5HumidityProbeStatus.setStatus("current")
_Pdug5HumidityValue_Type = Integer32
_Pdug5HumidityValue_Object = MibTableColumn
pdug5HumidityValue = _Pdug5HumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 4),
    _Pdug5HumidityValue_Type()
)
pdug5HumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5HumidityValue.setStatus("current")


class _Pdug5HumidityThStatus_Type(Integer32):
    """Custom type pdug5HumidityThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdug5HumidityThStatus_Type.__name__ = "Integer32"
_Pdug5HumidityThStatus_Object = MibTableColumn
pdug5HumidityThStatus = _Pdug5HumidityThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 5),
    _Pdug5HumidityThStatus_Type()
)
pdug5HumidityThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5HumidityThStatus.setStatus("current")


class _Pdug5HumidityThLowerWarning_Type(Integer32):
    """Custom type pdug5HumidityThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdug5HumidityThLowerWarning_Type.__name__ = "Integer32"
_Pdug5HumidityThLowerWarning_Object = MibTableColumn
pdug5HumidityThLowerWarning = _Pdug5HumidityThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 6),
    _Pdug5HumidityThLowerWarning_Type()
)
pdug5HumidityThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HumidityThLowerWarning.setStatus("current")


class _Pdug5HumidityThLowerCritical_Type(Integer32):
    """Custom type pdug5HumidityThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdug5HumidityThLowerCritical_Type.__name__ = "Integer32"
_Pdug5HumidityThLowerCritical_Object = MibTableColumn
pdug5HumidityThLowerCritical = _Pdug5HumidityThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 7),
    _Pdug5HumidityThLowerCritical_Type()
)
pdug5HumidityThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HumidityThLowerCritical.setStatus("current")


class _Pdug5HumidityThUpperWarning_Type(Integer32):
    """Custom type pdug5HumidityThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdug5HumidityThUpperWarning_Type.__name__ = "Integer32"
_Pdug5HumidityThUpperWarning_Object = MibTableColumn
pdug5HumidityThUpperWarning = _Pdug5HumidityThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 8),
    _Pdug5HumidityThUpperWarning_Type()
)
pdug5HumidityThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HumidityThUpperWarning.setStatus("current")


class _Pdug5HumidityThUpperCritical_Type(Integer32):
    """Custom type pdug5HumidityThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdug5HumidityThUpperCritical_Type.__name__ = "Integer32"
_Pdug5HumidityThUpperCritical_Object = MibTableColumn
pdug5HumidityThUpperCritical = _Pdug5HumidityThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 9),
    _Pdug5HumidityThUpperCritical_Type()
)
pdug5HumidityThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HumidityThUpperCritical.setStatus("current")


class _Pdug5HumidityThCtrl_Type(Integer32):
    """Custom type pdug5HumidityThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5HumidityThCtrl_Type.__name__ = "Integer32"
_Pdug5HumidityThCtrl_Object = MibTableColumn
pdug5HumidityThCtrl = _Pdug5HumidityThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 3, 1, 10),
    _Pdug5HumidityThCtrl_Type()
)
pdug5HumidityThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HumidityThCtrl.setStatus("current")
_Pdug5DoorTable_Object = MibTable
pdug5DoorTable = _Pdug5DoorTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 4)
)
if mibBuilder.loadTexts:
    pdug5DoorTable.setStatus("current")
_Pdug5DoorEntry_Object = MibTableRow
pdug5DoorEntry = _Pdug5DoorEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 4, 1)
)
pdug5DoorEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5DoorIndex"),
)
if mibBuilder.loadTexts:
    pdug5DoorEntry.setStatus("current")


class _Pdug5DoorIndex_Type(Integer32):
    """Custom type pdug5DoorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdug5DoorIndex_Type.__name__ = "Integer32"
_Pdug5DoorIndex_Object = MibTableColumn
pdug5DoorIndex = _Pdug5DoorIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 4, 1, 1),
    _Pdug5DoorIndex_Type()
)
pdug5DoorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5DoorIndex.setStatus("current")


class _Pdug5DoorName_Type(DisplayString):
    """Custom type pdug5DoorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Pdug5DoorName_Type.__name__ = "DisplayString"
_Pdug5DoorName_Object = MibTableColumn
pdug5DoorName = _Pdug5DoorName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 4, 1, 2),
    _Pdug5DoorName_Type()
)
pdug5DoorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5DoorName.setStatus("current")


class _Pdug5DoorProbeStatus_Type(Integer32):
    """Custom type pdug5DoorProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdug5DoorProbeStatus_Type.__name__ = "Integer32"
_Pdug5DoorProbeStatus_Object = MibTableColumn
pdug5DoorProbeStatus = _Pdug5DoorProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 4, 1, 3),
    _Pdug5DoorProbeStatus_Type()
)
pdug5DoorProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5DoorProbeStatus.setStatus("current")


class _Pdug5DoorState_Type(Integer32):
    """Custom type pdug5DoorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("doorOpen", 1),
          ("doorClosed", 2),
          ("badDoorSensor", 3))
    )


_Pdug5DoorState_Type.__name__ = "Integer32"
_Pdug5DoorState_Object = MibTableColumn
pdug5DoorState = _Pdug5DoorState_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 4, 1, 4),
    _Pdug5DoorState_Type()
)
pdug5DoorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5DoorState.setStatus("current")
_Pdug5DryTable_Object = MibTable
pdug5DryTable = _Pdug5DryTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 5)
)
if mibBuilder.loadTexts:
    pdug5DryTable.setStatus("current")
_Pdug5DryEntry_Object = MibTableRow
pdug5DryEntry = _Pdug5DryEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 5, 1)
)
pdug5DryEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5DryIndex"),
)
if mibBuilder.loadTexts:
    pdug5DryEntry.setStatus("current")


class _Pdug5DryIndex_Type(Integer32):
    """Custom type pdug5DryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdug5DryIndex_Type.__name__ = "Integer32"
_Pdug5DryIndex_Object = MibTableColumn
pdug5DryIndex = _Pdug5DryIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 5, 1, 1),
    _Pdug5DryIndex_Type()
)
pdug5DryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5DryIndex.setStatus("current")


class _Pdug5DryName_Type(DisplayString):
    """Custom type pdug5DryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Pdug5DryName_Type.__name__ = "DisplayString"
_Pdug5DryName_Object = MibTableColumn
pdug5DryName = _Pdug5DryName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 5, 1, 2),
    _Pdug5DryName_Type()
)
pdug5DryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5DryName.setStatus("current")


class _Pdug5DryProbeStatus_Type(Integer32):
    """Custom type pdug5DryProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdug5DryProbeStatus_Type.__name__ = "Integer32"
_Pdug5DryProbeStatus_Object = MibTableColumn
pdug5DryProbeStatus = _Pdug5DryProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 5, 1, 3),
    _Pdug5DryProbeStatus_Type()
)
pdug5DryProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5DryProbeStatus.setStatus("current")


class _Pdug5DryState_Type(Integer32):
    """Custom type pdug5DryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("alarmed", 2))
    )


_Pdug5DryState_Type.__name__ = "Integer32"
_Pdug5DryState_Object = MibTableColumn
pdug5DryState = _Pdug5DryState_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 5, 1, 4),
    _Pdug5DryState_Type()
)
pdug5DryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5DryState.setStatus("current")
_Pdug5SpotTable_Object = MibTable
pdug5SpotTable = _Pdug5SpotTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 6)
)
if mibBuilder.loadTexts:
    pdug5SpotTable.setStatus("current")
_Pdug5SpotEntry_Object = MibTableRow
pdug5SpotEntry = _Pdug5SpotEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 6, 1)
)
pdug5SpotEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5SpotIndex"),
)
if mibBuilder.loadTexts:
    pdug5SpotEntry.setStatus("current")


class _Pdug5SpotIndex_Type(Integer32):
    """Custom type pdug5SpotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdug5SpotIndex_Type.__name__ = "Integer32"
_Pdug5SpotIndex_Object = MibTableColumn
pdug5SpotIndex = _Pdug5SpotIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 6, 1, 1),
    _Pdug5SpotIndex_Type()
)
pdug5SpotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5SpotIndex.setStatus("current")


class _Pdug5SpotName_Type(DisplayString):
    """Custom type pdug5SpotName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Pdug5SpotName_Type.__name__ = "DisplayString"
_Pdug5SpotName_Object = MibTableColumn
pdug5SpotName = _Pdug5SpotName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 6, 1, 2),
    _Pdug5SpotName_Type()
)
pdug5SpotName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5SpotName.setStatus("current")


class _Pdug5SpotProbeStatus_Type(Integer32):
    """Custom type pdug5SpotProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdug5SpotProbeStatus_Type.__name__ = "Integer32"
_Pdug5SpotProbeStatus_Object = MibTableColumn
pdug5SpotProbeStatus = _Pdug5SpotProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 6, 1, 3),
    _Pdug5SpotProbeStatus_Type()
)
pdug5SpotProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5SpotProbeStatus.setStatus("current")


class _Pdug5SpotState_Type(Integer32):
    """Custom type pdug5SpotState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noleak", 1),
          ("leak", 2))
    )


_Pdug5SpotState_Type.__name__ = "Integer32"
_Pdug5SpotState_Object = MibTableColumn
pdug5SpotState = _Pdug5SpotState_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 6, 1, 4),
    _Pdug5SpotState_Type()
)
pdug5SpotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5SpotState.setStatus("current")
_Pdug5RopeTable_Object = MibTable
pdug5RopeTable = _Pdug5RopeTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 7)
)
if mibBuilder.loadTexts:
    pdug5RopeTable.setStatus("current")
_Pdug5RopeEntry_Object = MibTableRow
pdug5RopeEntry = _Pdug5RopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 7, 1)
)
pdug5RopeEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5RopeIndex"),
)
if mibBuilder.loadTexts:
    pdug5RopeEntry.setStatus("current")


class _Pdug5RopeIndex_Type(Integer32):
    """Custom type pdug5RopeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdug5RopeIndex_Type.__name__ = "Integer32"
_Pdug5RopeIndex_Object = MibTableColumn
pdug5RopeIndex = _Pdug5RopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 7, 1, 1),
    _Pdug5RopeIndex_Type()
)
pdug5RopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5RopeIndex.setStatus("current")


class _Pdug5RopeName_Type(DisplayString):
    """Custom type pdug5RopeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Pdug5RopeName_Type.__name__ = "DisplayString"
_Pdug5RopeName_Object = MibTableColumn
pdug5RopeName = _Pdug5RopeName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 7, 1, 2),
    _Pdug5RopeName_Type()
)
pdug5RopeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5RopeName.setStatus("current")


class _Pdug5RopeProbeStatus_Type(Integer32):
    """Custom type pdug5RopeProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdug5RopeProbeStatus_Type.__name__ = "Integer32"
_Pdug5RopeProbeStatus_Object = MibTableColumn
pdug5RopeProbeStatus = _Pdug5RopeProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 7, 1, 3),
    _Pdug5RopeProbeStatus_Type()
)
pdug5RopeProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5RopeProbeStatus.setStatus("current")


class _Pdug5RopeState_Type(Integer32):
    """Custom type pdug5RopeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noleak", 1),
          ("leak", 2))
    )


_Pdug5RopeState_Type.__name__ = "Integer32"
_Pdug5RopeState_Object = MibTableColumn
pdug5RopeState = _Pdug5RopeState_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 7, 1, 4),
    _Pdug5RopeState_Type()
)
pdug5RopeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5RopeState.setStatus("current")
_Pdug5EnvHID_ObjectIdentity = ObjectIdentity
pdug5EnvHID = _Pdug5EnvHID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10)
)
_Pdug5EnvHidTable_Object = MibTable
pdug5EnvHidTable = _Pdug5EnvHidTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1)
)
if mibBuilder.loadTexts:
    pdug5EnvHidTable.setStatus("current")
_Pdug5EnvHidEntry_Object = MibTableRow
pdug5EnvHidEntry = _Pdug5EnvHidEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1)
)
pdug5EnvHidEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5HIDIndex"),
)
if mibBuilder.loadTexts:
    pdug5EnvHidEntry.setStatus("current")


class _Pdug5HIDIndex_Type(Integer32):
    """Custom type pdug5HIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdug5HIDIndex_Type.__name__ = "Integer32"
_Pdug5HIDIndex_Object = MibTableColumn
pdug5HIDIndex = _Pdug5HIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 1),
    _Pdug5HIDIndex_Type()
)
pdug5HIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5HIDIndex.setStatus("current")


class _Pdug5HidAisle_Type(Integer32):
    """Custom type pdug5HidAisle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("hot", 2))
    )


_Pdug5HidAisle_Type.__name__ = "Integer32"
_Pdug5HidAisle_Object = MibTableColumn
pdug5HidAisle = _Pdug5HidAisle_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 2),
    _Pdug5HidAisle_Type()
)
pdug5HidAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5HidAisle.setStatus("current")


class _Pdug5HidHandleOperation_Type(Integer32):
    """Custom type pdug5HidHandleOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 1),
          ("lock", 2))
    )


_Pdug5HidHandleOperation_Type.__name__ = "Integer32"
_Pdug5HidHandleOperation_Object = MibTableColumn
pdug5HidHandleOperation = _Pdug5HidHandleOperation_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 3),
    _Pdug5HidHandleOperation_Type()
)
pdug5HidHandleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidHandleOperation.setStatus("current")


class _PduHIDVer_Type(DisplayString):
    """Custom type pduHIDVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduHIDVer_Type.__name__ = "DisplayString"
_PduHIDVer_Object = MibTableColumn
pduHIDVer = _PduHIDVer_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 4),
    _PduHIDVer_Type()
)
pduHIDVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduHIDVer.setStatus("current")


class _Pdug5MechanicalLock_Type(Integer32):
    """Custom type pdug5MechanicalLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 1),
          ("lock", 2))
    )


_Pdug5MechanicalLock_Type.__name__ = "Integer32"
_Pdug5MechanicalLock_Object = MibTableColumn
pdug5MechanicalLock = _Pdug5MechanicalLock_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 5),
    _Pdug5MechanicalLock_Type()
)
pdug5MechanicalLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5MechanicalLock.setStatus("current")


class _PduHIDSerial_Type(DisplayString):
    """Custom type pduHIDSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduHIDSerial_Type.__name__ = "DisplayString"
_PduHIDSerial_Object = MibTableColumn
pduHIDSerial = _PduHIDSerial_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 6),
    _PduHIDSerial_Type()
)
pduHIDSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduHIDSerial.setStatus("current")


class _PduHIDHwVer_Type(DisplayString):
    """Custom type pduHIDHwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduHIDHwVer_Type.__name__ = "DisplayString"
_PduHIDHwVer_Object = MibTableColumn
pduHIDHwVer = _PduHIDHwVer_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 7),
    _PduHIDHwVer_Type()
)
pduHIDHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduHIDHwVer.setStatus("current")
_Pdug5HIDAutoLockTime_Type = Integer32
_Pdug5HIDAutoLockTime_Object = MibTableColumn
pdug5HIDAutoLockTime = _Pdug5HIDAutoLockTime_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 8),
    _Pdug5HIDAutoLockTime_Type()
)
pdug5HIDAutoLockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HIDAutoLockTime.setStatus("current")
_Pdug5HIDDoorOpenTime_Type = Integer32
_Pdug5HIDDoorOpenTime_Object = MibTableColumn
pdug5HIDDoorOpenTime = _Pdug5HIDDoorOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 9),
    _Pdug5HIDDoorOpenTime_Type()
)
pdug5HIDDoorOpenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HIDDoorOpenTime.setStatus("current")
_Pdug5HIDMaxDoorOpenTime_Type = Integer32
_Pdug5HIDMaxDoorOpenTime_Object = MibTableColumn
pdug5HIDMaxDoorOpenTime = _Pdug5HIDMaxDoorOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 10),
    _Pdug5HIDMaxDoorOpenTime_Type()
)
pdug5HIDMaxDoorOpenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HIDMaxDoorOpenTime.setStatus("current")
_Pdug5HIDUserPinLength_Type = Integer32
_Pdug5HIDUserPinLength_Object = MibTableColumn
pdug5HIDUserPinLength = _Pdug5HIDUserPinLength_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 11),
    _Pdug5HIDUserPinLength_Type()
)
pdug5HIDUserPinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HIDUserPinLength.setStatus("current")


class _Pdug5HIDUserPinMode_Type(Integer32):
    """Custom type pdug5HIDUserPinMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("visible", 1),
          ("hidden", 2))
    )


_Pdug5HIDUserPinMode_Type.__name__ = "Integer32"
_Pdug5HIDUserPinMode_Object = MibTableColumn
pdug5HIDUserPinMode = _Pdug5HIDUserPinMode_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 12),
    _Pdug5HIDUserPinMode_Type()
)
pdug5HIDUserPinMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HIDUserPinMode.setStatus("current")


class _Pdug5HIDAisleControl_Type(Integer32):
    """Custom type pdug5HIDAisleControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("combined", 1),
          ("standalone", 2))
    )


_Pdug5HIDAisleControl_Type.__name__ = "Integer32"
_Pdug5HIDAisleControl_Object = MibTableColumn
pdug5HIDAisleControl = _Pdug5HIDAisleControl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 13),
    _Pdug5HIDAisleControl_Type()
)
pdug5HIDAisleControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HIDAisleControl.setStatus("current")


class _Pdug5HIDBeaconFuncControl_Type(Integer32):
    """Custom type pdug5HIDBeaconFuncControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locate", 0),
          ("standby", 1))
    )


_Pdug5HIDBeaconFuncControl_Type.__name__ = "Integer32"
_Pdug5HIDBeaconFuncControl_Object = MibTableColumn
pdug5HIDBeaconFuncControl = _Pdug5HIDBeaconFuncControl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 14),
    _Pdug5HIDBeaconFuncControl_Type()
)
pdug5HIDBeaconFuncControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HIDBeaconFuncControl.setStatus("current")


class _Pdug5HidBeaconColorControl_Type(Integer32):
    """Custom type pdug5HidBeaconColorControl based on Integer32"""
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
        *(("red", 0),
          ("green", 1),
          ("blue", 2),
          ("yellow", 3),
          ("magenta", 4),
          ("aqua", 5),
          ("white", 6),
          ("beaconoff", 7))
    )


_Pdug5HidBeaconColorControl_Type.__name__ = "Integer32"
_Pdug5HidBeaconColorControl_Object = MibTableColumn
pdug5HidBeaconColorControl = _Pdug5HidBeaconColorControl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 1, 1, 15),
    _Pdug5HidBeaconColorControl_Type()
)
pdug5HidBeaconColorControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidBeaconColorControl.setStatus("current")
_Pdug5EnvHidControlTable_Object = MibTable
pdug5EnvHidControlTable = _Pdug5EnvHidControlTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2)
)
if mibBuilder.loadTexts:
    pdug5EnvHidControlTable.setStatus("current")
_Pdug5EnvHidControlEntry_Object = MibTableRow
pdug5EnvHidControlEntry = _Pdug5EnvHidControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1)
)
pdug5EnvHidControlEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5HidControlIndex"),
)
if mibBuilder.loadTexts:
    pdug5EnvHidControlEntry.setStatus("current")


class _Pdug5HidControlIndex_Type(Integer32):
    """Custom type pdug5HidControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Pdug5HidControlIndex_Type.__name__ = "Integer32"
_Pdug5HidControlIndex_Object = MibTableColumn
pdug5HidControlIndex = _Pdug5HidControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 1),
    _Pdug5HidControlIndex_Type()
)
pdug5HidControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5HidControlIndex.setStatus("current")
_Pdug5HidControlUserName_Type = DisplayString
_Pdug5HidControlUserName_Object = MibTableColumn
pdug5HidControlUserName = _Pdug5HidControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 2),
    _Pdug5HidControlUserName_Type()
)
pdug5HidControlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidControlUserName.setStatus("current")
_Pdug5HidControlCardID_Type = Integer32
_Pdug5HidControlCardID_Object = MibTableColumn
pdug5HidControlCardID = _Pdug5HidControlCardID_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 3),
    _Pdug5HidControlCardID_Type()
)
pdug5HidControlCardID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidControlCardID.setStatus("current")
_Pdug5HidControlTimestamp_Type = DisplayString
_Pdug5HidControlTimestamp_Object = MibTableColumn
pdug5HidControlTimestamp = _Pdug5HidControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 4),
    _Pdug5HidControlTimestamp_Type()
)
pdug5HidControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5HidControlTimestamp.setStatus("current")


class _Pdug5HidControlCardAisle_Type(Integer32):
    """Custom type pdug5HidControlCardAisle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("hot", 2),
          ("both", 3))
    )


_Pdug5HidControlCardAisle_Type.__name__ = "Integer32"
_Pdug5HidControlCardAisle_Object = MibTableColumn
pdug5HidControlCardAisle = _Pdug5HidControlCardAisle_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 5),
    _Pdug5HidControlCardAisle_Type()
)
pdug5HidControlCardAisle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidControlCardAisle.setStatus("current")
_Pdug5HidControlStartTime_Type = DisplayString
_Pdug5HidControlStartTime_Object = MibTableColumn
pdug5HidControlStartTime = _Pdug5HidControlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 6),
    _Pdug5HidControlStartTime_Type()
)
pdug5HidControlStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidControlStartTime.setStatus("current")
_Pdug5HidControlExpireTime_Type = DisplayString
_Pdug5HidControlExpireTime_Object = MibTableColumn
pdug5HidControlExpireTime = _Pdug5HidControlExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 7),
    _Pdug5HidControlExpireTime_Type()
)
pdug5HidControlExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidControlExpireTime.setStatus("current")


class _Pdug5HidControlTempUser_Type(Integer32):
    """Custom type pdug5HidControlTempUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Pdug5HidControlTempUser_Type.__name__ = "Integer32"
_Pdug5HidControlTempUser_Object = MibTableColumn
pdug5HidControlTempUser = _Pdug5HidControlTempUser_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 8),
    _Pdug5HidControlTempUser_Type()
)
pdug5HidControlTempUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidControlTempUser.setStatus("current")
_Pdug5HidControlPin_Type = DisplayString
_Pdug5HidControlPin_Object = MibTableColumn
pdug5HidControlPin = _Pdug5HidControlPin_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 9),
    _Pdug5HidControlPin_Type()
)
pdug5HidControlPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidControlPin.setStatus("current")
_Pdug5HidControlCardIdStr_Type = DisplayString
_Pdug5HidControlCardIdStr_Object = MibTableColumn
pdug5HidControlCardIdStr = _Pdug5HidControlCardIdStr_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 4, 10, 2, 1, 10),
    _Pdug5HidControlCardIdStr_Type()
)
pdug5HidControlCardIdStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5HidControlCardIdStr.setStatus("current")
_Pdug5Outlet_ObjectIdentity = ObjectIdentity
pdug5Outlet = _Pdug5Outlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5)
)
_Pdug5OutletTable_Object = MibTable
pdug5OutletTable = _Pdug5OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1)
)
if mibBuilder.loadTexts:
    pdug5OutletTable.setStatus("current")
_Pdug5OutletEntry_Object = MibTableRow
pdug5OutletEntry = _Pdug5OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1)
)
pdug5OutletEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5OutletIndex"),
)
if mibBuilder.loadTexts:
    pdug5OutletEntry.setStatus("current")


class _Pdug5OutletIndex_Type(Integer32):
    """Custom type pdug5OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_Pdug5OutletIndex_Type.__name__ = "Integer32"
_Pdug5OutletIndex_Object = MibTableColumn
pdug5OutletIndex = _Pdug5OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 1),
    _Pdug5OutletIndex_Type()
)
pdug5OutletIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdug5OutletIndex.setStatus("current")


class _Pdug5OutletName_Type(DisplayString):
    """Custom type pdug5OutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdug5OutletName_Type.__name__ = "DisplayString"
_Pdug5OutletName_Object = MibTableColumn
pdug5OutletName = _Pdug5OutletName_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 2),
    _Pdug5OutletName_Type()
)
pdug5OutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletName.setStatus("current")


class _Pdug5OutletType_Type(Integer32):
    """Custom type pdug5OutletType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10,
              11,
              12,
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
              30)
        )
    )
    namedValues = NamedValues(
        *(("iecC13", 1),
          ("iecC19", 2),
          ("nema5-20R", 3),
          ("iecC13iecC15combo", 4),
          ("iecC13iecC15iec19combo", 5),
          ("uk", 10),
          ("french", 11),
          ("schuko", 12),
          ("nema515", 20),
          ("nema51520", 21),
          ("nema520", 22),
          ("nemaL520", 23),
          ("nemaL530", 24),
          ("nema615", 25),
          ("nema620", 26),
          ("nemaL620", 27),
          ("nemaL630", 28),
          ("nemaL715", 29),
          ("rf203p277", 30))
    )


_Pdug5OutletType_Type.__name__ = "Integer32"
_Pdug5OutletType_Object = MibTableColumn
pdug5OutletType = _Pdug5OutletType_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 3),
    _Pdug5OutletType_Type()
)
pdug5OutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletType.setStatus("current")
_Pdug5OutletCurrentRating_Type = Integer32
_Pdug5OutletCurrentRating_Object = MibTableColumn
pdug5OutletCurrentRating = _Pdug5OutletCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 4),
    _Pdug5OutletCurrentRating_Type()
)
pdug5OutletCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletCurrentRating.setStatus("current")
_Pdug5OutletCurrent_Type = Integer32
_Pdug5OutletCurrent_Object = MibTableColumn
pdug5OutletCurrent = _Pdug5OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 5),
    _Pdug5OutletCurrent_Type()
)
pdug5OutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletCurrent.setStatus("current")


class _Pdug5OutletActivePowerThStatus_Type(Integer32):
    """Custom type pdug5OutletActivePowerThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdug5OutletActivePowerThStatus_Type.__name__ = "Integer32"
_Pdug5OutletActivePowerThStatus_Object = MibTableColumn
pdug5OutletActivePowerThStatus = _Pdug5OutletActivePowerThStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 6),
    _Pdug5OutletActivePowerThStatus_Type()
)
pdug5OutletActivePowerThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletActivePowerThStatus.setStatus("current")


class _Pdug5OutletActivePowerThLowerWarning_Type(Integer32):
    """Custom type pdug5OutletActivePowerThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdug5OutletActivePowerThLowerWarning_Type.__name__ = "Integer32"
_Pdug5OutletActivePowerThLowerWarning_Object = MibTableColumn
pdug5OutletActivePowerThLowerWarning = _Pdug5OutletActivePowerThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 7),
    _Pdug5OutletActivePowerThLowerWarning_Type()
)
pdug5OutletActivePowerThLowerWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletActivePowerThLowerWarning.setStatus("current")


class _Pdug5OutletActivePowerThLowerCritical_Type(Integer32):
    """Custom type pdug5OutletActivePowerThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdug5OutletActivePowerThLowerCritical_Type.__name__ = "Integer32"
_Pdug5OutletActivePowerThLowerCritical_Object = MibTableColumn
pdug5OutletActivePowerThLowerCritical = _Pdug5OutletActivePowerThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 8),
    _Pdug5OutletActivePowerThLowerCritical_Type()
)
pdug5OutletActivePowerThLowerCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletActivePowerThLowerCritical.setStatus("current")


class _Pdug5OutletActivePowerThUpperWarning_Type(Integer32):
    """Custom type pdug5OutletActivePowerThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdug5OutletActivePowerThUpperWarning_Type.__name__ = "Integer32"
_Pdug5OutletActivePowerThUpperWarning_Object = MibTableColumn
pdug5OutletActivePowerThUpperWarning = _Pdug5OutletActivePowerThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 9),
    _Pdug5OutletActivePowerThUpperWarning_Type()
)
pdug5OutletActivePowerThUpperWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletActivePowerThUpperWarning.setStatus("current")


class _Pdug5OutletActivePowerThUpperCritical_Type(Integer32):
    """Custom type pdug5OutletActivePowerThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdug5OutletActivePowerThUpperCritical_Type.__name__ = "Integer32"
_Pdug5OutletActivePowerThUpperCritical_Object = MibTableColumn
pdug5OutletActivePowerThUpperCritical = _Pdug5OutletActivePowerThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 10),
    _Pdug5OutletActivePowerThUpperCritical_Type()
)
pdug5OutletActivePowerThUpperCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletActivePowerThUpperCritical.setStatus("current")
_Pdug5OutletCurrentPercentLoad_Type = Integer32
_Pdug5OutletCurrentPercentLoad_Object = MibTableColumn
pdug5OutletCurrentPercentLoad = _Pdug5OutletCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 11),
    _Pdug5OutletCurrentPercentLoad_Type()
)
pdug5OutletCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletCurrentPercentLoad.setStatus("current")
_Pdug5OutletVA_Type = Integer32
_Pdug5OutletVA_Object = MibTableColumn
pdug5OutletVA = _Pdug5OutletVA_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 12),
    _Pdug5OutletVA_Type()
)
pdug5OutletVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletVA.setStatus("current")
_Pdug5OutletWatts_Type = Integer32
_Pdug5OutletWatts_Object = MibTableColumn
pdug5OutletWatts = _Pdug5OutletWatts_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 13),
    _Pdug5OutletWatts_Type()
)
pdug5OutletWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletWatts.setStatus("current")
_Pdug5OutletWh_Type = Integer32
_Pdug5OutletWh_Object = MibTableColumn
pdug5OutletWh = _Pdug5OutletWh_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 14),
    _Pdug5OutletWh_Type()
)
pdug5OutletWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletWh.setStatus("current")


class _Pdug5OutletWhTimer_Type(DisplayString):
    """Custom type pdug5OutletWhTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdug5OutletWhTimer_Type.__name__ = "DisplayString"
_Pdug5OutletWhTimer_Object = MibTableColumn
pdug5OutletWhTimer = _Pdug5OutletWhTimer_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 15),
    _Pdug5OutletWhTimer_Type()
)
pdug5OutletWhTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletWhTimer.setStatus("current")
_Pdug5OutletPowerFactor_Type = Integer32
_Pdug5OutletPowerFactor_Object = MibTableColumn
pdug5OutletPowerFactor = _Pdug5OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 16),
    _Pdug5OutletPowerFactor_Type()
)
pdug5OutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletPowerFactor.setStatus("current")
_Pdug5OutletVAR_Type = Integer32
_Pdug5OutletVAR_Object = MibTableColumn
pdug5OutletVAR = _Pdug5OutletVAR_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 17),
    _Pdug5OutletVAR_Type()
)
pdug5OutletVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletVAR.setStatus("current")
_Pdug5OutletBranch_Type = Integer32
_Pdug5OutletBranch_Object = MibTableColumn
pdug5OutletBranch = _Pdug5OutletBranch_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 18),
    _Pdug5OutletBranch_Type()
)
pdug5OutletBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletBranch.setStatus("current")


class _Pdug5OutletActivePowerThResetThld_Type(Integer32):
    """Custom type pdug5OutletActivePowerThResetThld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdug5OutletActivePowerThResetThld_Type.__name__ = "Integer32"
_Pdug5OutletActivePowerThResetThld_Object = MibTableColumn
pdug5OutletActivePowerThResetThld = _Pdug5OutletActivePowerThResetThld_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 19),
    _Pdug5OutletActivePowerThResetThld_Type()
)
pdug5OutletActivePowerThResetThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletActivePowerThResetThld.setStatus("current")


class _Pdug5OutletActivePowerThChangeDelay_Type(Integer32):
    """Custom type pdug5OutletActivePowerThChangeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdug5OutletActivePowerThChangeDelay_Type.__name__ = "Integer32"
_Pdug5OutletActivePowerThChangeDelay_Object = MibTableColumn
pdug5OutletActivePowerThChangeDelay = _Pdug5OutletActivePowerThChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 20),
    _Pdug5OutletActivePowerThChangeDelay_Type()
)
pdug5OutletActivePowerThChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletActivePowerThChangeDelay.setStatus("current")


class _Pdug5OutletActivePowerThCtrl_Type(Integer32):
    """Custom type pdug5OutletActivePowerThCtrl based on Integer32"""
    defaultValue = 0


_Pdug5OutletActivePowerThCtrl_Type.__name__ = "Integer32"
_Pdug5OutletActivePowerThCtrl_Object = MibTableColumn
pdug5OutletActivePowerThCtrl = _Pdug5OutletActivePowerThCtrl_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 1, 1, 21),
    _Pdug5OutletActivePowerThCtrl_Type()
)
pdug5OutletActivePowerThCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletActivePowerThCtrl.setStatus("current")
_Pdug5OutletControlTable_Object = MibTable
pdug5OutletControlTable = _Pdug5OutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2)
)
if mibBuilder.loadTexts:
    pdug5OutletControlTable.setStatus("current")
_Pdug5OutletControlEntry_Object = MibTableRow
pdug5OutletControlEntry = _Pdug5OutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1)
)
pdug5OutletControlEntry.setIndexNames(
    (0, "PANDUIT-MIB", "pdug5IdentIndex"),
    (0, "PANDUIT-MIB", "pdug5OutletIndex"),
)
if mibBuilder.loadTexts:
    pdug5OutletControlEntry.setStatus("current")


class _Pdug5OutletControlStatus_Type(Integer32):
    """Custom type pdug5OutletControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("pendingOff", 3),
          ("pendingOn", 4))
    )


_Pdug5OutletControlStatus_Type.__name__ = "Integer32"
_Pdug5OutletControlStatus_Object = MibTableColumn
pdug5OutletControlStatus = _Pdug5OutletControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 1),
    _Pdug5OutletControlStatus_Type()
)
pdug5OutletControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdug5OutletControlStatus.setStatus("current")


class _Pdug5OutletControlOffCmd_Type(Integer32):
    """Custom type pdug5OutletControlOffCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdug5OutletControlOffCmd_Type.__name__ = "Integer32"
_Pdug5OutletControlOffCmd_Object = MibTableColumn
pdug5OutletControlOffCmd = _Pdug5OutletControlOffCmd_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 2),
    _Pdug5OutletControlOffCmd_Type()
)
pdug5OutletControlOffCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlOffCmd.setStatus("current")


class _Pdug5OutletControlOnCmd_Type(Integer32):
    """Custom type pdug5OutletControlOnCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdug5OutletControlOnCmd_Type.__name__ = "Integer32"
_Pdug5OutletControlOnCmd_Object = MibTableColumn
pdug5OutletControlOnCmd = _Pdug5OutletControlOnCmd_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 3),
    _Pdug5OutletControlOnCmd_Type()
)
pdug5OutletControlOnCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlOnCmd.setStatus("current")


class _Pdug5OutletControlRebootCmd_Type(Integer32):
    """Custom type pdug5OutletControlRebootCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdug5OutletControlRebootCmd_Type.__name__ = "Integer32"
_Pdug5OutletControlRebootCmd_Object = MibTableColumn
pdug5OutletControlRebootCmd = _Pdug5OutletControlRebootCmd_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 4),
    _Pdug5OutletControlRebootCmd_Type()
)
pdug5OutletControlRebootCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlRebootCmd.setStatus("current")


class _Pdug5OutletControlPowerOnState_Type(Integer32):
    """Custom type pdug5OutletControlPowerOnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("lastState", 3))
    )


_Pdug5OutletControlPowerOnState_Type.__name__ = "Integer32"
_Pdug5OutletControlPowerOnState_Object = MibTableColumn
pdug5OutletControlPowerOnState = _Pdug5OutletControlPowerOnState_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 5),
    _Pdug5OutletControlPowerOnState_Type()
)
pdug5OutletControlPowerOnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlPowerOnState.setStatus("current")


class _Pdug5OutletControlSequenceDelay_Type(Integer32):
    """Custom type pdug5OutletControlSequenceDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7200),
    )


_Pdug5OutletControlSequenceDelay_Type.__name__ = "Integer32"
_Pdug5OutletControlSequenceDelay_Object = MibTableColumn
pdug5OutletControlSequenceDelay = _Pdug5OutletControlSequenceDelay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 6),
    _Pdug5OutletControlSequenceDelay_Type()
)
pdug5OutletControlSequenceDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlSequenceDelay.setStatus("current")


class _Pdug5OutletControlRebootOffTime_Type(Integer32):
    """Custom type pdug5OutletControlRebootOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_Pdug5OutletControlRebootOffTime_Type.__name__ = "Integer32"
_Pdug5OutletControlRebootOffTime_Object = MibTableColumn
pdug5OutletControlRebootOffTime = _Pdug5OutletControlRebootOffTime_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 7),
    _Pdug5OutletControlRebootOffTime_Type()
)
pdug5OutletControlRebootOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlRebootOffTime.setStatus("current")


class _Pdug5OutletControlSwitchable_Type(Integer32):
    """Custom type pdug5OutletControlSwitchable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchable", 1),
          ("notSwitchable", 2))
    )


_Pdug5OutletControlSwitchable_Type.__name__ = "Integer32"
_Pdug5OutletControlSwitchable_Object = MibTableColumn
pdug5OutletControlSwitchable = _Pdug5OutletControlSwitchable_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 8),
    _Pdug5OutletControlSwitchable_Type()
)
pdug5OutletControlSwitchable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlSwitchable.setStatus("current")


class _Pdug5OutletControlShutoffDelay_Type(Integer32):
    """Custom type pdug5OutletControlShutoffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7200),
    )


_Pdug5OutletControlShutoffDelay_Type.__name__ = "Integer32"
_Pdug5OutletControlShutoffDelay_Object = MibTableColumn
pdug5OutletControlShutoffDelay = _Pdug5OutletControlShutoffDelay_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 9),
    _Pdug5OutletControlShutoffDelay_Type()
)
pdug5OutletControlShutoffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlShutoffDelay.setStatus("current")


class _Pdug5OutletControlCommand_Type(Integer32):
    """Custom type pdug5OutletControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 1),
          ("immediateOn", 2),
          ("delayedOff", 3),
          ("delayedOn", 4),
          ("immediateReboot", 5),
          ("delayedReboot", 6),
          ("outletUnknown", 7))
    )


_Pdug5OutletControlCommand_Type.__name__ = "Integer32"
_Pdug5OutletControlCommand_Object = MibTableColumn
pdug5OutletControlCommand = _Pdug5OutletControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 5, 2, 1, 10),
    _Pdug5OutletControlCommand_Type()
)
pdug5OutletControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdug5OutletControlCommand.setStatus("current")
_Pdug5Traps_ObjectIdentity = ObjectIdentity
pdug5Traps = _Pdug5Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 6)
)
_Pdug5TrapInfo_ObjectIdentity = ObjectIdentity
pdug5TrapInfo = _Pdug5TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 7)
)
_Pdug5TrapInfoEntry_ObjectIdentity = ObjectIdentity
pdug5TrapInfoEntry = _Pdug5TrapInfoEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 7, 1)
)
_TrapCode_Type = Integer32
_TrapCode_Object = MibScalar
trapCode = _TrapCode_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 7, 1, 1),
    _TrapCode_Type()
)
trapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCode.setStatus("current")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 7, 1, 2),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("current")
_Pdug5Conformance_ObjectIdentity = ObjectIdentity
pdug5Conformance = _Pdug5Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8)
)
_Pdug5Compliances_ObjectIdentity = ObjectIdentity
pdug5Compliances = _Pdug5Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 1)
)
_Pdug5Groups_ObjectIdentity = ObjectIdentity
pdug5Groups = _Pdug5Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 2)
)

# Managed Objects groups

pdug5IdentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 2, 1)
)
pdug5IdentGroup.setObjects(
      *(("PANDUIT-MIB", "pdug5NumberPDU"),
        ("PANDUIT-MIB", "pdug5Name"),
        ("PANDUIT-MIB", "pdug5Model"),
        ("PANDUIT-MIB", "pdug5Manufacturer"),
        ("PANDUIT-MIB", "pdug5FirmwareVersion"),
        ("PANDUIT-MIB", "pdug5FirmwareVersionTimeStamp"),
        ("PANDUIT-MIB", "pdug5PartNumber"),
        ("PANDUIT-MIB", "pdug5SerialNumber"),
        ("PANDUIT-MIB", "pdug5Status"),
        ("PANDUIT-MIB", "pdug5Controllable"),
        ("PANDUIT-MIB", "pdug5InputPhaseCount"),
        ("PANDUIT-MIB", "pdug5GroupCount"),
        ("PANDUIT-MIB", "pdug5OutletCount"),
        ("PANDUIT-MIB", "pdug5MACAddress"),
        ("PANDUIT-MIB", "pdug5IPv4Address"),
        ("PANDUIT-MIB", "pdug5IPv6Address"),
        ("PANDUIT-MIB", "pdug5HWVersion"),
        ("PANDUIT-MIB", "pdug5ConfigSsh"),
        ("PANDUIT-MIB", "pdug5ConfigFtps"),
        ("PANDUIT-MIB", "pdug5ConfigHttp"),
        ("PANDUIT-MIB", "pdug5ConfigHttps"),
        ("PANDUIT-MIB", "pdug5ConfigIPv4IPv6Switch"),
        ("PANDUIT-MIB", "pdug5ConfigRedfishAPI"),
        ("PANDUIT-MIB", "pdug5ConfigOledDispalyOrientation"),
        ("PANDUIT-MIB", "pdug5ConfigEnergyReset"),
        ("PANDUIT-MIB", "pdug5ConfigNetworkManagementCardReset"),
        ("PANDUIT-MIB", "pdug5ConfigDaisyChainStatus"),
        ("PANDUIT-MIB", "pdug5PowershareFunctionStatus"),
        ("PANDUIT-MIB", "pdug5PowershareFunctionUpstreamStatus"),
        ("PANDUIT-MIB", "pdug5PowershareOutput"),
        ("PANDUIT-MIB", "pdug5PowershareInput"),
        ("PANDUIT-MIB", "pdug5PowershareOptMode"),
        ("PANDUIT-MIB", "pdug5PowershareFunc"))
)
if mibBuilder.loadTexts:
    pdug5IdentGroup.setStatus("current")

pdug5InputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 2, 2)
)
pdug5InputGroup.setObjects(
      *(("PANDUIT-MIB", "pdug5InputType"),
        ("PANDUIT-MIB", "pdug5InputFrequency"),
        ("PANDUIT-MIB", "pdug5InputFrequencyStatus"),
        ("PANDUIT-MIB", "pdug5InputPowerVA"),
        ("PANDUIT-MIB", "pdug5InputPowerWatts"),
        ("PANDUIT-MIB", "pdug5InputTotalEnergy"),
        ("PANDUIT-MIB", "pdug5InputPowerWattHourTimer"),
        ("PANDUIT-MIB", "pdug5InputResettableEnergy"),
        ("PANDUIT-MIB", "pdug5InputPowerFactor"),
        ("PANDUIT-MIB", "pdug5InputPowerVAR"),
        ("PANDUIT-MIB", "pdug5InputTotalCurrent"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageMeasType"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltage"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageThStatus"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageThLowerWarning"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageThLowerCritical"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageThUpperWarning"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageThUpperCritical"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentMeasType"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentRating"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrent"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentThStatus"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentThLowerWarning"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentThLowerCritical"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentThUpperWarning"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentThUpperCritical"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentPercentLoad"),
        ("PANDUIT-MIB", "pdug5InputPhasePowerMeasType"),
        ("PANDUIT-MIB", "pdug5InputPhasePowerVA"),
        ("PANDUIT-MIB", "pdug5InputPhasePowerWatts"),
        ("PANDUIT-MIB", "pdug5InputPhasePowerWattHour"),
        ("PANDUIT-MIB", "pdug5InputPhasePowerWattHourTimer"),
        ("PANDUIT-MIB", "pdug5InputPhasePowerFactor"),
        ("PANDUIT-MIB", "pdug5InputPhasePowerVAR"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageThResetThld"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageThChangeDelay"),
        ("PANDUIT-MIB", "pdug5InputPhaseVoltageThCtrl"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentThResetThld"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentThChangeDelay"),
        ("PANDUIT-MIB", "pdug5InputPhaseCurrentThCtrl"),
        ("PANDUIT-MIB", "pdug5InputPowerThresholdThLowerWarning"),
        ("PANDUIT-MIB", "pdug5InputPowerThresholdThLowerCritical"),
        ("PANDUIT-MIB", "pdug5InputPowerThresholdThUpperWarning"),
        ("PANDUIT-MIB", "pdug5InputPowerThresholdThUpperCritical"),
        ("PANDUIT-MIB", "pdug5InputPowerThresholdThResetThld"),
        ("PANDUIT-MIB", "pdug5InputPowerThresholdThChangeDelay"),
        ("PANDUIT-MIB", "pdug5InputPowerThresholdThCtrl"),
        ("PANDUIT-MIB", "pdug5InputEnergyThresholdThUpperWarning"),
        ("PANDUIT-MIB", "pdug5InputEnergyThresholdThUpperCritical"),
        ("PANDUIT-MIB", "pdug5InputEnergyThresholdThResetThld"),
        ("PANDUIT-MIB", "pdug5InputEnergyThresholdThChangeDelay"),
        ("PANDUIT-MIB", "pdug5InputEnergyThresholdThCtrl"),
        ("PANDUIT-MIB", "pdug5InputPhasePowerThStatus"),
        ("PANDUIT-MIB", "pdug5InputRcmEnabled"),
        ("PANDUIT-MIB", "pdug5InputRcmModStatus"),
        ("PANDUIT-MIB", "pdug5InputRcmThUpperWarning"),
        ("PANDUIT-MIB", "pdug5InputRcmThUpperCritical"),
        ("PANDUIT-MIB", "pdug5InputRcmThResetThld"),
        ("PANDUIT-MIB", "pdug5InputRcmThChangeDelay"),
        ("PANDUIT-MIB", "pdug5InputRcmThCtrl"),
        ("PANDUIT-MIB", "pdug5InputRcmThStatus"),
        ("PANDUIT-MIB", "pdug5InputRcmCurrent"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestEnable"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestFreq"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestHour"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestMinute"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestDay"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestMonth"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestNextRunTime"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestLastRunTime"),
        ("PANDUIT-MIB", "pdug5InputRcmSelfTestLastRunStatus"))
)
if mibBuilder.loadTexts:
    pdug5InputGroup.setStatus("current")

pdug5GroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 2, 3)
)
pdug5GroupGroup.setObjects(
      *(("PANDUIT-MIB", "pdug5GroupName"),
        ("PANDUIT-MIB", "pdug5GroupType"),
        ("PANDUIT-MIB", "pdug5GroupVoltageMeasType"),
        ("PANDUIT-MIB", "pdug5GroupVoltage"),
        ("PANDUIT-MIB", "pdug5GroupVoltageThStatus"),
        ("PANDUIT-MIB", "pdug5GroupVoltageThLowerWarning"),
        ("PANDUIT-MIB", "pdug5GroupVoltageThLowerCritical"),
        ("PANDUIT-MIB", "pdug5GroupVoltageThUpperWarning"),
        ("PANDUIT-MIB", "pdug5GroupVoltageThUpperCritical"),
        ("PANDUIT-MIB", "pdug5groupCurrentRating"),
        ("PANDUIT-MIB", "pdug5GroupCurrent"),
        ("PANDUIT-MIB", "pdug5GroupCurrentThStatus"),
        ("PANDUIT-MIB", "pdug5GroupCurrentThLowerWarning"),
        ("PANDUIT-MIB", "pdug5GroupCurrentThLowerCritical"),
        ("PANDUIT-MIB", "pdug5GroupCurrentThUpperWarning"),
        ("PANDUIT-MIB", "pdug5GroupCurrentThUpperCritical"),
        ("PANDUIT-MIB", "pdug5GroupCurrentPercentLoad"),
        ("PANDUIT-MIB", "pdug5GroupPowerVA"),
        ("PANDUIT-MIB", "pdug5GroupPowerWatts"),
        ("PANDUIT-MIB", "pdug5GroupPowerWattHour"),
        ("PANDUIT-MIB", "pdug5GroupPowerWattHourTimer"),
        ("PANDUIT-MIB", "pdug5GroupPowerFactor"),
        ("PANDUIT-MIB", "pdug5GroupPowerVAR"),
        ("PANDUIT-MIB", "pdug5GroupOutletCount"),
        ("PANDUIT-MIB", "pdug5GroupBreakerStatus"),
        ("PANDUIT-MIB", "pdug5GroupVoltageThCtrl"),
        ("PANDUIT-MIB", "pdug5GroupCurrentThCtrl"))
)
if mibBuilder.loadTexts:
    pdug5GroupGroup.setStatus("current")

pdug5EnvironmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 2, 4)
)
pdug5EnvironmentGroup.setObjects(
      *(("PANDUIT-MIB", "pdug5TemperatureScale"),
        ("PANDUIT-MIB", "pdug5TemperatureCount"),
        ("PANDUIT-MIB", "pdug5HumidityCount"),
        ("PANDUIT-MIB", "pdug5DoorCount"),
        ("PANDUIT-MIB", "pdug5DryCount"),
        ("PANDUIT-MIB", "pdug5SpotCount"),
        ("PANDUIT-MIB", "pdug5RopeCount"),
        ("PANDUIT-MIB", "pdug5HidCount"),
        ("PANDUIT-MIB", "pdug5TemperatureName"),
        ("PANDUIT-MIB", "pdug5TemperatureProbeStatus"),
        ("PANDUIT-MIB", "pdug5TemperatureValue"),
        ("PANDUIT-MIB", "pdug5TemperatureThStatus"),
        ("PANDUIT-MIB", "pdug5TemperatureThLowerWarning"),
        ("PANDUIT-MIB", "pdug5TemperatureThLowerCritical"),
        ("PANDUIT-MIB", "pdug5TemperatureThUpperWarning"),
        ("PANDUIT-MIB", "pdug5TemperatureThUpperCritical"),
        ("PANDUIT-MIB", "pdug5TemperatureThCtrl"),
        ("PANDUIT-MIB", "pdug5HumidityName"),
        ("PANDUIT-MIB", "pdug5HumidityProbeStatus"),
        ("PANDUIT-MIB", "pdug5HumidityValue"),
        ("PANDUIT-MIB", "pdug5HumidityThStatus"),
        ("PANDUIT-MIB", "pdug5HumidityThLowerWarning"),
        ("PANDUIT-MIB", "pdug5HumidityThLowerCritical"),
        ("PANDUIT-MIB", "pdug5HumidityThUpperWarning"),
        ("PANDUIT-MIB", "pdug5HumidityThUpperCritical"),
        ("PANDUIT-MIB", "pdug5HumidityThCtrl"),
        ("PANDUIT-MIB", "pdug5DoorName"),
        ("PANDUIT-MIB", "pdug5DoorProbeStatus"),
        ("PANDUIT-MIB", "pdug5DoorState"),
        ("PANDUIT-MIB", "pdug5DryName"),
        ("PANDUIT-MIB", "pdug5DryProbeStatus"),
        ("PANDUIT-MIB", "pdug5DryState"),
        ("PANDUIT-MIB", "pdug5SpotName"),
        ("PANDUIT-MIB", "pdug5SpotProbeStatus"),
        ("PANDUIT-MIB", "pdug5SpotState"),
        ("PANDUIT-MIB", "pdug5RopeName"),
        ("PANDUIT-MIB", "pdug5RopeProbeStatus"),
        ("PANDUIT-MIB", "pdug5RopeState"),
        ("PANDUIT-MIB", "pdug5HidAisle"),
        ("PANDUIT-MIB", "pdug5HidHandleOperation"),
        ("PANDUIT-MIB", "pduHIDVer"),
        ("PANDUIT-MIB", "pdug5MechanicalLock"),
        ("PANDUIT-MIB", "pduHIDSerial"),
        ("PANDUIT-MIB", "pduHIDHwVer"),
        ("PANDUIT-MIB", "pdug5HIDAutoLockTime"),
        ("PANDUIT-MIB", "pdug5HIDDoorOpenTime"),
        ("PANDUIT-MIB", "pdug5HIDMaxDoorOpenTime"),
        ("PANDUIT-MIB", "pdug5HIDUserPinLength"),
        ("PANDUIT-MIB", "pdug5HIDUserPinMode"),
        ("PANDUIT-MIB", "pdug5HIDAisleControl"),
        ("PANDUIT-MIB", "pdug5HIDBeaconFuncControl"),
        ("PANDUIT-MIB", "pdug5HidBeaconColorControl"),
        ("PANDUIT-MIB", "pdug5HidControlUserName"),
        ("PANDUIT-MIB", "pdug5HidControlCardID"),
        ("PANDUIT-MIB", "pdug5HidControlTimestamp"),
        ("PANDUIT-MIB", "pdug5HidControlCardAisle"),
        ("PANDUIT-MIB", "pdug5HidControlStartTime"),
        ("PANDUIT-MIB", "pdug5HidControlExpireTime"),
        ("PANDUIT-MIB", "pdug5HidControlTempUser"),
        ("PANDUIT-MIB", "pdug5HidControlPin"),
        ("PANDUIT-MIB", "pdug5HidControlCardIdStr"))
)
if mibBuilder.loadTexts:
    pdug5EnvironmentGroup.setStatus("current")

pdug5OutletGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 2, 5)
)
pdug5OutletGroup.setObjects(
      *(("PANDUIT-MIB", "pdug5OutletName"),
        ("PANDUIT-MIB", "pdug5OutletType"),
        ("PANDUIT-MIB", "pdug5OutletCurrentRating"),
        ("PANDUIT-MIB", "pdug5OutletCurrent"),
        ("PANDUIT-MIB", "pdug5OutletActivePowerThStatus"),
        ("PANDUIT-MIB", "pdug5OutletActivePowerThLowerWarning"),
        ("PANDUIT-MIB", "pdug5OutletActivePowerThLowerCritical"),
        ("PANDUIT-MIB", "pdug5OutletActivePowerThUpperWarning"),
        ("PANDUIT-MIB", "pdug5OutletActivePowerThUpperCritical"),
        ("PANDUIT-MIB", "pdug5OutletCurrentPercentLoad"),
        ("PANDUIT-MIB", "pdug5OutletVA"),
        ("PANDUIT-MIB", "pdug5OutletWatts"),
        ("PANDUIT-MIB", "pdug5OutletWh"),
        ("PANDUIT-MIB", "pdug5OutletWhTimer"),
        ("PANDUIT-MIB", "pdug5OutletPowerFactor"),
        ("PANDUIT-MIB", "pdug5OutletVAR"),
        ("PANDUIT-MIB", "pdug5OutletBranch"),
        ("PANDUIT-MIB", "pdug5OutletActivePowerThResetThld"),
        ("PANDUIT-MIB", "pdug5OutletActivePowerThChangeDelay"),
        ("PANDUIT-MIB", "pdug5OutletActivePowerThCtrl"),
        ("PANDUIT-MIB", "pdug5OutletControlStatus"),
        ("PANDUIT-MIB", "pdug5OutletControlOffCmd"),
        ("PANDUIT-MIB", "pdug5OutletControlOnCmd"),
        ("PANDUIT-MIB", "pdug5OutletControlRebootCmd"),
        ("PANDUIT-MIB", "pdug5OutletControlPowerOnState"),
        ("PANDUIT-MIB", "pdug5OutletControlSequenceDelay"),
        ("PANDUIT-MIB", "pdug5OutletControlRebootOffTime"),
        ("PANDUIT-MIB", "pdug5OutletControlSwitchable"),
        ("PANDUIT-MIB", "pdug5OutletControlShutoffDelay"),
        ("PANDUIT-MIB", "pdug5OutletControlCommand"))
)
if mibBuilder.loadTexts:
    pdug5OutletGroup.setStatus("current")

pdug5TrapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 2, 7)
)
pdug5TrapInfoGroup.setObjects(
      *(("PANDUIT-MIB", "trapCode"),
        ("PANDUIT-MIB", "trapDescription"))
)
if mibBuilder.loadTexts:
    pdug5TrapInfoGroup.setStatus("current")


# Notification objects

trapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 6, 1)
)
trapCritical.setObjects(
      *(("PANDUIT-MIB", "trapCode"),
        ("PANDUIT-MIB", "trapDescription"),
        ("SNMPv2-MIB", "sysDescr"),
        ("PANDUIT-MIB", "pdug5IPv4Address"),
        ("PANDUIT-MIB", "pdug5IPv6Address"))
)
if mibBuilder.loadTexts:
    trapCritical.setStatus(
        "current"
    )

trapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 6, 2)
)
trapWarning.setObjects(
      *(("PANDUIT-MIB", "trapCode"),
        ("PANDUIT-MIB", "trapDescription"),
        ("SNMPv2-MIB", "sysDescr"),
        ("PANDUIT-MIB", "pdug5IPv4Address"),
        ("PANDUIT-MIB", "pdug5IPv6Address"))
)
if mibBuilder.loadTexts:
    trapWarning.setStatus(
        "current"
    )

trapInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 6, 3)
)
trapInformation.setObjects(
      *(("PANDUIT-MIB", "trapCode"),
        ("PANDUIT-MIB", "trapDescription"),
        ("SNMPv2-MIB", "sysDescr"),
        ("PANDUIT-MIB", "pdug5IPv4Address"),
        ("PANDUIT-MIB", "pdug5IPv6Address"))
)
if mibBuilder.loadTexts:
    trapInformation.setStatus(
        "current"
    )

trapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 6, 4)
)
trapCleared.setObjects(
      *(("PANDUIT-MIB", "trapCode"),
        ("PANDUIT-MIB", "trapDescription"),
        ("SNMPv2-MIB", "sysDescr"),
        ("PANDUIT-MIB", "pdug5IPv4Address"),
        ("PANDUIT-MIB", "pdug5IPv6Address"))
)
if mibBuilder.loadTexts:
    trapCleared.setStatus(
        "current"
    )

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 6, 5)
)
trapTest.setObjects(
      *(("PANDUIT-MIB", "trapCode"),
        ("PANDUIT-MIB", "trapDescription"),
        ("SNMPv2-MIB", "sysDescr"),
        ("PANDUIT-MIB", "pdug5IPv4Address"),
        ("PANDUIT-MIB", "pdug5IPv6Address"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        "current"
    )


# Notifications groups

pdug5TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 2, 6)
)
pdug5TrapGroup.setObjects(
      *(("PANDUIT-MIB", "trapCritical"),
        ("PANDUIT-MIB", "trapWarning"),
        ("PANDUIT-MIB", "trapInformation"),
        ("PANDUIT-MIB", "trapCleared"),
        ("PANDUIT-MIB", "trapTest"))
)
if mibBuilder.loadTexts:
    pdug5TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pdug5FullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19536, 10, 1, 8, 1, 1)
)
pdug5FullCompliance.setObjects(
      *(("PANDUIT-MIB", "pdug5IdentGroup"),
        ("PANDUIT-MIB", "pdug5InputGroup"),
        ("PANDUIT-MIB", "pdug5GroupGroup"),
        ("PANDUIT-MIB", "pdug5EnvironmentGroup"),
        ("PANDUIT-MIB", "pdug5OutletGroup"),
        ("PANDUIT-MIB", "pdug5TrapGroup"),
        ("PANDUIT-MIB", "pdug5TrapInfoGroup"))
)
if mibBuilder.loadTexts:
    pdug5FullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PANDUIT-MIB",
    **{"panduit": panduit,
       "g5": g5,
       "pdug5": pdug5,
       "pdug5Ident": pdug5Ident,
       "pdug5NumberPDU": pdug5NumberPDU,
       "pdug5IdentTable": pdug5IdentTable,
       "pdug5IdentEntry": pdug5IdentEntry,
       "pdug5IdentIndex": pdug5IdentIndex,
       "pdug5Name": pdug5Name,
       "pdug5Model": pdug5Model,
       "pdug5Manufacturer": pdug5Manufacturer,
       "pdug5FirmwareVersion": pdug5FirmwareVersion,
       "pdug5FirmwareVersionTimeStamp": pdug5FirmwareVersionTimeStamp,
       "pdug5PartNumber": pdug5PartNumber,
       "pdug5SerialNumber": pdug5SerialNumber,
       "pdug5Status": pdug5Status,
       "pdug5Controllable": pdug5Controllable,
       "pdug5InputPhaseCount": pdug5InputPhaseCount,
       "pdug5GroupCount": pdug5GroupCount,
       "pdug5OutletCount": pdug5OutletCount,
       "pdug5MACAddress": pdug5MACAddress,
       "pdug5IPv4Address": pdug5IPv4Address,
       "pdug5IPv6Address": pdug5IPv6Address,
       "pdug5HWVersion": pdug5HWVersion,
       "pdug5ConfigTable": pdug5ConfigTable,
       "pdug5ConfigEntry": pdug5ConfigEntry,
       "pdug5ConfigIndex": pdug5ConfigIndex,
       "pdug5ConfigSsh": pdug5ConfigSsh,
       "pdug5ConfigFtps": pdug5ConfigFtps,
       "pdug5ConfigHttp": pdug5ConfigHttp,
       "pdug5ConfigHttps": pdug5ConfigHttps,
       "pdug5ConfigIPv4IPv6Switch": pdug5ConfigIPv4IPv6Switch,
       "pdug5ConfigRedfishAPI": pdug5ConfigRedfishAPI,
       "pdug5ConfigOledDispalyOrientation": pdug5ConfigOledDispalyOrientation,
       "pdug5ConfigEnergyReset": pdug5ConfigEnergyReset,
       "pdug5ConfigNetworkManagementCardReset": pdug5ConfigNetworkManagementCardReset,
       "pdug5ConfigDaisyChainStatus": pdug5ConfigDaisyChainStatus,
       "pdug5PowershareTable": pdug5PowershareTable,
       "pdug5PowershareEntry": pdug5PowershareEntry,
       "pdug5PowershareIndex": pdug5PowershareIndex,
       "pdug5PowershareFunctionStatus": pdug5PowershareFunctionStatus,
       "pdug5PowershareFunctionUpstreamStatus": pdug5PowershareFunctionUpstreamStatus,
       "pdug5PowershareOutput": pdug5PowershareOutput,
       "pdug5PowershareInput": pdug5PowershareInput,
       "pdug5PowershareOptMode": pdug5PowershareOptMode,
       "pdug5PowershareFunc": pdug5PowershareFunc,
       "pdug5Input": pdug5Input,
       "pdug5InputTable": pdug5InputTable,
       "pdug5InputEntry": pdug5InputEntry,
       "pdug5InputType": pdug5InputType,
       "pdug5InputFrequency": pdug5InputFrequency,
       "pdug5InputFrequencyStatus": pdug5InputFrequencyStatus,
       "pdug5InputPowerVA": pdug5InputPowerVA,
       "pdug5InputPowerWatts": pdug5InputPowerWatts,
       "pdug5InputTotalEnergy": pdug5InputTotalEnergy,
       "pdug5InputPowerWattHourTimer": pdug5InputPowerWattHourTimer,
       "pdug5InputResettableEnergy": pdug5InputResettableEnergy,
       "pdug5InputPowerFactor": pdug5InputPowerFactor,
       "pdug5InputPowerVAR": pdug5InputPowerVAR,
       "pdug5InputTotalCurrent": pdug5InputTotalCurrent,
       "pdug5InputPhaseTable": pdug5InputPhaseTable,
       "pdug5InputPhaseEntry": pdug5InputPhaseEntry,
       "pdug5InputPhaseIndex": pdug5InputPhaseIndex,
       "pdug5InputPhaseVoltageMeasType": pdug5InputPhaseVoltageMeasType,
       "pdug5InputPhaseVoltage": pdug5InputPhaseVoltage,
       "pdug5InputPhaseVoltageThStatus": pdug5InputPhaseVoltageThStatus,
       "pdug5InputPhaseVoltageThLowerWarning": pdug5InputPhaseVoltageThLowerWarning,
       "pdug5InputPhaseVoltageThLowerCritical": pdug5InputPhaseVoltageThLowerCritical,
       "pdug5InputPhaseVoltageThUpperWarning": pdug5InputPhaseVoltageThUpperWarning,
       "pdug5InputPhaseVoltageThUpperCritical": pdug5InputPhaseVoltageThUpperCritical,
       "pdug5InputPhaseCurrentMeasType": pdug5InputPhaseCurrentMeasType,
       "pdug5InputPhaseCurrentRating": pdug5InputPhaseCurrentRating,
       "pdug5InputPhaseCurrent": pdug5InputPhaseCurrent,
       "pdug5InputPhaseCurrentThStatus": pdug5InputPhaseCurrentThStatus,
       "pdug5InputPhaseCurrentThLowerWarning": pdug5InputPhaseCurrentThLowerWarning,
       "pdug5InputPhaseCurrentThLowerCritical": pdug5InputPhaseCurrentThLowerCritical,
       "pdug5InputPhaseCurrentThUpperWarning": pdug5InputPhaseCurrentThUpperWarning,
       "pdug5InputPhaseCurrentThUpperCritical": pdug5InputPhaseCurrentThUpperCritical,
       "pdug5InputPhaseCurrentPercentLoad": pdug5InputPhaseCurrentPercentLoad,
       "pdug5InputPhasePowerMeasType": pdug5InputPhasePowerMeasType,
       "pdug5InputPhasePowerVA": pdug5InputPhasePowerVA,
       "pdug5InputPhasePowerWatts": pdug5InputPhasePowerWatts,
       "pdug5InputPhasePowerWattHour": pdug5InputPhasePowerWattHour,
       "pdug5InputPhasePowerWattHourTimer": pdug5InputPhasePowerWattHourTimer,
       "pdug5InputPhasePowerFactor": pdug5InputPhasePowerFactor,
       "pdug5InputPhasePowerVAR": pdug5InputPhasePowerVAR,
       "pdug5InputPhaseVoltageThResetThld": pdug5InputPhaseVoltageThResetThld,
       "pdug5InputPhaseVoltageThChangeDelay": pdug5InputPhaseVoltageThChangeDelay,
       "pdug5InputPhaseVoltageThCtrl": pdug5InputPhaseVoltageThCtrl,
       "pdug5InputPhaseCurrentThResetThld": pdug5InputPhaseCurrentThResetThld,
       "pdug5InputPhaseCurrentThChangeDelay": pdug5InputPhaseCurrentThChangeDelay,
       "pdug5InputPhaseCurrentThCtrl": pdug5InputPhaseCurrentThCtrl,
       "pdug5InputPowerThresholdThLowerWarning": pdug5InputPowerThresholdThLowerWarning,
       "pdug5InputPowerThresholdThLowerCritical": pdug5InputPowerThresholdThLowerCritical,
       "pdug5InputPowerThresholdThUpperWarning": pdug5InputPowerThresholdThUpperWarning,
       "pdug5InputPowerThresholdThUpperCritical": pdug5InputPowerThresholdThUpperCritical,
       "pdug5InputPowerThresholdThResetThld": pdug5InputPowerThresholdThResetThld,
       "pdug5InputPowerThresholdThChangeDelay": pdug5InputPowerThresholdThChangeDelay,
       "pdug5InputPowerThresholdThCtrl": pdug5InputPowerThresholdThCtrl,
       "pdug5InputEnergyThresholdThUpperWarning": pdug5InputEnergyThresholdThUpperWarning,
       "pdug5InputEnergyThresholdThUpperCritical": pdug5InputEnergyThresholdThUpperCritical,
       "pdug5InputEnergyThresholdThResetThld": pdug5InputEnergyThresholdThResetThld,
       "pdug5InputEnergyThresholdThChangeDelay": pdug5InputEnergyThresholdThChangeDelay,
       "pdug5InputEnergyThresholdThCtrl": pdug5InputEnergyThresholdThCtrl,
       "pdug5InputPhasePowerThStatus": pdug5InputPhasePowerThStatus,
       "pdug5InputRcmTable": pdug5InputRcmTable,
       "pdug5InputRcmEntry": pdug5InputRcmEntry,
       "pdug5InputRcmEnabled": pdug5InputRcmEnabled,
       "pdug5InputRcmModStatus": pdug5InputRcmModStatus,
       "pdug5InputRcmThUpperWarning": pdug5InputRcmThUpperWarning,
       "pdug5InputRcmThUpperCritical": pdug5InputRcmThUpperCritical,
       "pdug5InputRcmThResetThld": pdug5InputRcmThResetThld,
       "pdug5InputRcmThChangeDelay": pdug5InputRcmThChangeDelay,
       "pdug5InputRcmThCtrl": pdug5InputRcmThCtrl,
       "pdug5InputRcmThStatus": pdug5InputRcmThStatus,
       "pdug5InputRcmCurrent": pdug5InputRcmCurrent,
       "pdug5InputRcmSelfTestTable": pdug5InputRcmSelfTestTable,
       "pdug5InputRcmSelfTestEntry": pdug5InputRcmSelfTestEntry,
       "pdug5InputRcmSelfTestEnable": pdug5InputRcmSelfTestEnable,
       "pdug5InputRcmSelfTestFreq": pdug5InputRcmSelfTestFreq,
       "pdug5InputRcmSelfTestHour": pdug5InputRcmSelfTestHour,
       "pdug5InputRcmSelfTestMinute": pdug5InputRcmSelfTestMinute,
       "pdug5InputRcmSelfTestDay": pdug5InputRcmSelfTestDay,
       "pdug5InputRcmSelfTestMonth": pdug5InputRcmSelfTestMonth,
       "pdug5InputRcmSelfTestNextRunTime": pdug5InputRcmSelfTestNextRunTime,
       "pdug5InputRcmSelfTestLastRunTime": pdug5InputRcmSelfTestLastRunTime,
       "pdug5InputRcmSelfTestLastRunStatus": pdug5InputRcmSelfTestLastRunStatus,
       "pdug5Group": pdug5Group,
       "pdug5GroupTable": pdug5GroupTable,
       "pdug5GroupEntry": pdug5GroupEntry,
       "pdug5GroupIndex": pdug5GroupIndex,
       "pdug5GroupName": pdug5GroupName,
       "pdug5GroupType": pdug5GroupType,
       "pdug5GroupVoltageMeasType": pdug5GroupVoltageMeasType,
       "pdug5GroupVoltage": pdug5GroupVoltage,
       "pdug5GroupVoltageThStatus": pdug5GroupVoltageThStatus,
       "pdug5GroupVoltageThLowerWarning": pdug5GroupVoltageThLowerWarning,
       "pdug5GroupVoltageThLowerCritical": pdug5GroupVoltageThLowerCritical,
       "pdug5GroupVoltageThUpperWarning": pdug5GroupVoltageThUpperWarning,
       "pdug5GroupVoltageThUpperCritical": pdug5GroupVoltageThUpperCritical,
       "pdug5groupCurrentRating": pdug5groupCurrentRating,
       "pdug5GroupCurrent": pdug5GroupCurrent,
       "pdug5GroupCurrentThStatus": pdug5GroupCurrentThStatus,
       "pdug5GroupCurrentThLowerWarning": pdug5GroupCurrentThLowerWarning,
       "pdug5GroupCurrentThLowerCritical": pdug5GroupCurrentThLowerCritical,
       "pdug5GroupCurrentThUpperWarning": pdug5GroupCurrentThUpperWarning,
       "pdug5GroupCurrentThUpperCritical": pdug5GroupCurrentThUpperCritical,
       "pdug5GroupCurrentPercentLoad": pdug5GroupCurrentPercentLoad,
       "pdug5GroupPowerVA": pdug5GroupPowerVA,
       "pdug5GroupPowerWatts": pdug5GroupPowerWatts,
       "pdug5GroupPowerWattHour": pdug5GroupPowerWattHour,
       "pdug5GroupPowerWattHourTimer": pdug5GroupPowerWattHourTimer,
       "pdug5GroupPowerFactor": pdug5GroupPowerFactor,
       "pdug5GroupPowerVAR": pdug5GroupPowerVAR,
       "pdug5GroupOutletCount": pdug5GroupOutletCount,
       "pdug5GroupBreakerStatus": pdug5GroupBreakerStatus,
       "pdug5GroupVoltageThCtrl": pdug5GroupVoltageThCtrl,
       "pdug5GroupCurrentThCtrl": pdug5GroupCurrentThCtrl,
       "pdug5Environment": pdug5Environment,
       "pdug5EnvProbeTable": pdug5EnvProbeTable,
       "pdug5EnvProbeEntry": pdug5EnvProbeEntry,
       "pdug5TemperatureScale": pdug5TemperatureScale,
       "pdug5TemperatureCount": pdug5TemperatureCount,
       "pdug5HumidityCount": pdug5HumidityCount,
       "pdug5DoorCount": pdug5DoorCount,
       "pdug5DryCount": pdug5DryCount,
       "pdug5SpotCount": pdug5SpotCount,
       "pdug5RopeCount": pdug5RopeCount,
       "pdug5HidCount": pdug5HidCount,
       "pdug5TemperatureTable": pdug5TemperatureTable,
       "pdug5TemperatureEntry": pdug5TemperatureEntry,
       "pdug5TemperatureIndex": pdug5TemperatureIndex,
       "pdug5TemperatureName": pdug5TemperatureName,
       "pdug5TemperatureProbeStatus": pdug5TemperatureProbeStatus,
       "pdug5TemperatureValue": pdug5TemperatureValue,
       "pdug5TemperatureThStatus": pdug5TemperatureThStatus,
       "pdug5TemperatureThLowerWarning": pdug5TemperatureThLowerWarning,
       "pdug5TemperatureThLowerCritical": pdug5TemperatureThLowerCritical,
       "pdug5TemperatureThUpperWarning": pdug5TemperatureThUpperWarning,
       "pdug5TemperatureThUpperCritical": pdug5TemperatureThUpperCritical,
       "pdug5TemperatureThCtrl": pdug5TemperatureThCtrl,
       "pdug5HumidityTable": pdug5HumidityTable,
       "pdug5HumidityEntry": pdug5HumidityEntry,
       "pdug5HumidityIndex": pdug5HumidityIndex,
       "pdug5HumidityName": pdug5HumidityName,
       "pdug5HumidityProbeStatus": pdug5HumidityProbeStatus,
       "pdug5HumidityValue": pdug5HumidityValue,
       "pdug5HumidityThStatus": pdug5HumidityThStatus,
       "pdug5HumidityThLowerWarning": pdug5HumidityThLowerWarning,
       "pdug5HumidityThLowerCritical": pdug5HumidityThLowerCritical,
       "pdug5HumidityThUpperWarning": pdug5HumidityThUpperWarning,
       "pdug5HumidityThUpperCritical": pdug5HumidityThUpperCritical,
       "pdug5HumidityThCtrl": pdug5HumidityThCtrl,
       "pdug5DoorTable": pdug5DoorTable,
       "pdug5DoorEntry": pdug5DoorEntry,
       "pdug5DoorIndex": pdug5DoorIndex,
       "pdug5DoorName": pdug5DoorName,
       "pdug5DoorProbeStatus": pdug5DoorProbeStatus,
       "pdug5DoorState": pdug5DoorState,
       "pdug5DryTable": pdug5DryTable,
       "pdug5DryEntry": pdug5DryEntry,
       "pdug5DryIndex": pdug5DryIndex,
       "pdug5DryName": pdug5DryName,
       "pdug5DryProbeStatus": pdug5DryProbeStatus,
       "pdug5DryState": pdug5DryState,
       "pdug5SpotTable": pdug5SpotTable,
       "pdug5SpotEntry": pdug5SpotEntry,
       "pdug5SpotIndex": pdug5SpotIndex,
       "pdug5SpotName": pdug5SpotName,
       "pdug5SpotProbeStatus": pdug5SpotProbeStatus,
       "pdug5SpotState": pdug5SpotState,
       "pdug5RopeTable": pdug5RopeTable,
       "pdug5RopeEntry": pdug5RopeEntry,
       "pdug5RopeIndex": pdug5RopeIndex,
       "pdug5RopeName": pdug5RopeName,
       "pdug5RopeProbeStatus": pdug5RopeProbeStatus,
       "pdug5RopeState": pdug5RopeState,
       "pdug5EnvHID": pdug5EnvHID,
       "pdug5EnvHidTable": pdug5EnvHidTable,
       "pdug5EnvHidEntry": pdug5EnvHidEntry,
       "pdug5HIDIndex": pdug5HIDIndex,
       "pdug5HidAisle": pdug5HidAisle,
       "pdug5HidHandleOperation": pdug5HidHandleOperation,
       "pduHIDVer": pduHIDVer,
       "pdug5MechanicalLock": pdug5MechanicalLock,
       "pduHIDSerial": pduHIDSerial,
       "pduHIDHwVer": pduHIDHwVer,
       "pdug5HIDAutoLockTime": pdug5HIDAutoLockTime,
       "pdug5HIDDoorOpenTime": pdug5HIDDoorOpenTime,
       "pdug5HIDMaxDoorOpenTime": pdug5HIDMaxDoorOpenTime,
       "pdug5HIDUserPinLength": pdug5HIDUserPinLength,
       "pdug5HIDUserPinMode": pdug5HIDUserPinMode,
       "pdug5HIDAisleControl": pdug5HIDAisleControl,
       "pdug5HIDBeaconFuncControl": pdug5HIDBeaconFuncControl,
       "pdug5HidBeaconColorControl": pdug5HidBeaconColorControl,
       "pdug5EnvHidControlTable": pdug5EnvHidControlTable,
       "pdug5EnvHidControlEntry": pdug5EnvHidControlEntry,
       "pdug5HidControlIndex": pdug5HidControlIndex,
       "pdug5HidControlUserName": pdug5HidControlUserName,
       "pdug5HidControlCardID": pdug5HidControlCardID,
       "pdug5HidControlTimestamp": pdug5HidControlTimestamp,
       "pdug5HidControlCardAisle": pdug5HidControlCardAisle,
       "pdug5HidControlStartTime": pdug5HidControlStartTime,
       "pdug5HidControlExpireTime": pdug5HidControlExpireTime,
       "pdug5HidControlTempUser": pdug5HidControlTempUser,
       "pdug5HidControlPin": pdug5HidControlPin,
       "pdug5HidControlCardIdStr": pdug5HidControlCardIdStr,
       "pdug5Outlet": pdug5Outlet,
       "pdug5OutletTable": pdug5OutletTable,
       "pdug5OutletEntry": pdug5OutletEntry,
       "pdug5OutletIndex": pdug5OutletIndex,
       "pdug5OutletName": pdug5OutletName,
       "pdug5OutletType": pdug5OutletType,
       "pdug5OutletCurrentRating": pdug5OutletCurrentRating,
       "pdug5OutletCurrent": pdug5OutletCurrent,
       "pdug5OutletActivePowerThStatus": pdug5OutletActivePowerThStatus,
       "pdug5OutletActivePowerThLowerWarning": pdug5OutletActivePowerThLowerWarning,
       "pdug5OutletActivePowerThLowerCritical": pdug5OutletActivePowerThLowerCritical,
       "pdug5OutletActivePowerThUpperWarning": pdug5OutletActivePowerThUpperWarning,
       "pdug5OutletActivePowerThUpperCritical": pdug5OutletActivePowerThUpperCritical,
       "pdug5OutletCurrentPercentLoad": pdug5OutletCurrentPercentLoad,
       "pdug5OutletVA": pdug5OutletVA,
       "pdug5OutletWatts": pdug5OutletWatts,
       "pdug5OutletWh": pdug5OutletWh,
       "pdug5OutletWhTimer": pdug5OutletWhTimer,
       "pdug5OutletPowerFactor": pdug5OutletPowerFactor,
       "pdug5OutletVAR": pdug5OutletVAR,
       "pdug5OutletBranch": pdug5OutletBranch,
       "pdug5OutletActivePowerThResetThld": pdug5OutletActivePowerThResetThld,
       "pdug5OutletActivePowerThChangeDelay": pdug5OutletActivePowerThChangeDelay,
       "pdug5OutletActivePowerThCtrl": pdug5OutletActivePowerThCtrl,
       "pdug5OutletControlTable": pdug5OutletControlTable,
       "pdug5OutletControlEntry": pdug5OutletControlEntry,
       "pdug5OutletControlStatus": pdug5OutletControlStatus,
       "pdug5OutletControlOffCmd": pdug5OutletControlOffCmd,
       "pdug5OutletControlOnCmd": pdug5OutletControlOnCmd,
       "pdug5OutletControlRebootCmd": pdug5OutletControlRebootCmd,
       "pdug5OutletControlPowerOnState": pdug5OutletControlPowerOnState,
       "pdug5OutletControlSequenceDelay": pdug5OutletControlSequenceDelay,
       "pdug5OutletControlRebootOffTime": pdug5OutletControlRebootOffTime,
       "pdug5OutletControlSwitchable": pdug5OutletControlSwitchable,
       "pdug5OutletControlShutoffDelay": pdug5OutletControlShutoffDelay,
       "pdug5OutletControlCommand": pdug5OutletControlCommand,
       "pdug5Traps": pdug5Traps,
       "trapCritical": trapCritical,
       "trapWarning": trapWarning,
       "trapInformation": trapInformation,
       "trapCleared": trapCleared,
       "trapTest": trapTest,
       "pdug5TrapInfo": pdug5TrapInfo,
       "pdug5TrapInfoEntry": pdug5TrapInfoEntry,
       "trapCode": trapCode,
       "trapDescription": trapDescription,
       "pdug5Conformance": pdug5Conformance,
       "pdug5Compliances": pdug5Compliances,
       "pdug5FullCompliance": pdug5FullCompliance,
       "pdug5Groups": pdug5Groups,
       "pdug5IdentGroup": pdug5IdentGroup,
       "pdug5InputGroup": pdug5InputGroup,
       "pdug5GroupGroup": pdug5GroupGroup,
       "pdug5EnvironmentGroup": pdug5EnvironmentGroup,
       "pdug5OutletGroup": pdug5OutletGroup,
       "pdug5TrapGroup": pdug5TrapGroup,
       "pdug5TrapInfoGroup": pdug5TrapInfoGroup}
)
